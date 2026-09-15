# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""q4nx -> bfp16 dequantization, emitting B in ``flm.GEMM``'s packed order.

The shipped FastFlowLM pipeline dequantizes to bf16 and hands that to its ``mm``
overlay. ``flm.GEMM`` takes bfp16ebs8 instead, at 9 bytes per 8 values rather
than 16, so a drop-in replacement has to change both the element format and the
blocking. This design does both on the device, which is what lets the weights
stay 4-bit on disk.

Where each reorder happens is forced by the hardware, not chosen:

* A DMA addresses memory in 4-byte units, and a bfp16 block is 9 bytes. Nothing
  finer than a whole 8x8 tile (72 bytes) is expressible in a buffer descriptor,
  so the tile interior is the core's job.
* The 8 values in a block share an exponent. No permutation of them exists once
  the conversion has run, so the core must transpose *before* converting.
* Everything coarser than a tile is a multiple of 72 bytes, so a buffer
  descriptor covers the rest. That one sits on the drain; see DRAIN_DIMS.

Nothing in the device configuration depends on K or N, so one xclbin serves
every shape and only the instruction stream is rebuilt. See ``core_body``.

``iron/tests/operators/flm_dequant_layout.py`` proves the composition below
reproduces ``packing.pack_b`` exactly, which is the only check that catches a
wrong stride: a mis-ordered buffer has the right size and fails silently.
"""

import sys

import numpy as np

from aie.helpers.taplib.tap import TensorAccessPattern
from aie.helpers.util import v8bfp16ebs8
from aie.iron import Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker
from aie.iron.controlflow import range_
from aie.dialects._aie_enum_gen import AIEArch

from iron.common.device_utils import get_kernel_dir

# q4nx block geometry, fixed by the weights file: 32 out-features x 256
# in-features, stored as a scale table, a min table, then the 4-bit codes.
M_TILE, K_TILE, GROUP = 32, 256, 32
BLOCK_BYTES = M_TILE * K_TILE * 5 // 8  # 5120
SCALE_BYTES = (K_TILE // GROUP) * M_TILE * 2  # 512

# flm.GEMM's B tiling. These must agree with gemm/design.py or the GEMM reads
# the buffer in a different order than this design writes it.
#
# tile_n is fixed at 64, which is what flm.GEMM picks for every shape except
# K == 512. At tile_n = 128 an output tile spans 128 out-features, so it takes
# eight q4nx blocks rather than four, and a column has four cores -- the
# one-core-per-quarter-tile mapping below does not hold. dequant_bfp() rejects
# that case instead of emitting a buffer of the right size in the wrong order.
N_TILE, K_TILE_B, CT_K = 64, 512, 128
S = T = 8
BFP16_GROUP = 8

ROWS, COLS = 4, 8

# One core covers one q4nx block, which is a quarter of a (64 n x 512 k) output
# tile: two halves in n, two in k.
CORE_BLOCKS = M_TILE * K_TILE // BFP16_GROUP  # 1024
TILE_BLOCKS = N_TILE * K_TILE_B // BFP16_GROUP  # 4096

# The contiguous run one core emits for one k-slice: every n it owns, every k
# group inside that slice.
RUN = (M_TILE // T) * (CT_K // S) * T  # 512 blocks

# A column joins its four cores into TWO memtile objects, one per k-half of the
# output tile, rather than one object of the whole tile. Two limits force it,
# and each rules out the other's workaround:
#
# * A shim BD carries three access dimensions plus a hardware repeat. Unpicking
#   a whole tile needs four dimensions BEFORE the split below, which leaves
#   nothing for the repeat.
# * The BD's size field counts 4-BYTE GRANULES, not elements, and tops out at
#   1023. RUN is 512 bfp16 blocks = 4608 bytes = 1152 granules, so the run has
#   to be split in two regardless, costing a dimension.
#
# Halving the object spends the k-half on the offset instead of on a dimension,
# which pays for the split. The reorder still happens entirely on the drain: a
# join gives each core one contiguous segment, and a core's share of the tile
# interleaves with its neighbours'.
HALF_BLOCKS = TILE_BLOCKS // 2
SPLIT = 2

# Read outermost first: which n-half, which k-slice inside the q4nx block, then
# the core's dense run, split so the innermost size fits the field.
DRAIN_DIMS = [
    (N_TILE // M_TILE, RUN),
    (K_TILE // CT_K, (N_TILE // T) * (CT_K // S) * T),
    (SPLIT, RUN // SPLIT),
    (RUN // SPLIT, 1),
]

# Core i takes n-half i % 2 and k-half i // 2, so cores 0/1 form the k-half 0
# object and cores 2/3 the k-half 1 object. That is the order the fill delivers
# the four q4nx blocks in and the order DRAIN_DIMS unpicks.
CORE_JOIN_OFFSETS = [0, CORE_BLOCKS]
HALVES = 2


def dequant_bfp(dev, K, N, tile_n=N_TILE, trace_size=0):
    """K in-features, N out-features. B reaches the GEMM as (K, N)."""
    if dev.arch != AIEArch.AIE2p:
        raise NotImplementedError("bfp16ebs8 exists only on AIE2P")
    if tile_n != N_TILE:
        raise NotImplementedError(
            f"tile_n must be {N_TILE}; flm.GEMM picks {tile_n} for this shape, "
            "and the two must agree or the GEMM reads B in the wrong order"
        )
    if K % K_TILE_B:
        raise ValueError(f"K ({K}) must be a multiple of {K_TILE_B}")
    if N % N_TILE:
        raise ValueError(f"N ({N}) must be a multiple of {N_TILE}")

    k_tiles = K // K_TILE_B  # output tiles per column block
    blocks_per_row = K // K_TILE  # q4nx blocks across one block-row
    n_blocks = N // N_TILE  # column blocks in the whole matrix
    # Column c takes every COLS'th column block. A trailing group shorter than
    # the grid leaves some columns without work for that round, which costs
    # nothing: the cores loop forever and park on an empty input fifo.
    rounds = -(-n_blocks // COLS)

    qw_bytes = N * K * 5 // 8
    out_blocks = K * N // BFP16_GROUP

    qw_l3_ty = np.ndarray[(qw_bytes,), np.dtype[np.uint8]]
    out_l3_ty = np.ndarray[(out_blocks,), np.dtype[v8bfp16ebs8]]
    qw_col_ty = np.ndarray[(ROWS * BLOCK_BYTES,), np.dtype[np.uint8]]
    qw_blk_ty = np.ndarray[(BLOCK_BYTES,), np.dtype[np.uint8]]
    out_half_ty = np.ndarray[(HALF_BLOCKS,), np.dtype[v8bfp16ebs8]]
    out_blk_ty = np.ndarray[(CORE_BLOCKS,), np.dtype[v8bfp16ebs8]]

    kernel = Kernel(
        "q4nx_dequant_bfp",
        f"q4nx_dequant_{get_kernel_dir(dev)}.o",
        [qw_blk_ty, out_blk_ty],
    )

    def core_body(qw_in, out_of, k):
        """One iteration is one q4nx block, and every block is identical work.

        The loop therefore carries no trip count and reads no runtime
        parameter: nothing a core does depends on K or N. The shim sequence
        bounds the real work, and the loop parks on an empty input fifo once
        that sequence has delivered its last block. That is what keeps the
        device configuration shape-independent, so one xclbin serves every
        shape and only the instruction stream is rebuilt.

        A bounded loop would put K and N in the core program and cost an
        xclbin per shape. Making the bound a runtime parameter would fix that
        but needs a barrier and a re-read per dispatch; a core that does the
        same thing every iteration needs neither.
        """
        for _ in range_(sys.maxsize):
            qw = qw_in.acquire(1)
            out = out_of.acquire(1)
            k(qw, out)
            qw_in.release(1)
            out_of.release(1)

    workers = []
    qw_prods, out_conses = [], []

    for c in range(COLS):
        of_qw = ObjectFifo(qw_col_ty, name=f"qw_{c}", depth=2)
        qw_prods.append(of_qw.prod())
        qw_cores = of_qw.cons().split(
            [BLOCK_BYTES * r for r in range(ROWS)],
            obj_types=[qw_blk_ty] * ROWS,
            names=[f"qw_{c}_{r}" for r in range(ROWS)],
        )

        out_cores = []
        halves = []
        for h in range(HALVES):
            of_out = ObjectFifo(out_half_ty, name=f"w_{c}_{h}", depth=2)
            halves.append(of_out.cons())
            out_cores += of_out.prod().join(
                CORE_JOIN_OFFSETS,
                obj_types=[out_blk_ty] * (ROWS // HALVES),
                names=[f"w_{c}_{h}_{r}" for r in range(ROWS // HALVES)],
            )
        out_conses.append(halves)

        # The eight per-column bf16 vectors the kernel holds live across the
        # transpose do not fit the 1024-byte device default; aiecc measures
        # 1216. The margin is for the measurement moving, since it depends on
        # register allocation rather than on anything this design states.
        workers += [
            Worker(
                core_body,
                [qw_cores[r].cons(), out_cores[r].prod(), kernel],
                stack_size=2048,
            )
            for r in range(ROWS)
        ]

    # The fill walks (block-column, n-half, block bytes). The k-half and the
    # k-tile index both step whole blocks along a row, so they collapse into
    # one dimension of blocks_per_row -- which is what leaves a dimension free
    # to split the 5120-byte block into 10 x 512, keeping the innermost size
    # inside the BD's 10-bit field.
    def qw_tap(cb):
        return TensorAccessPattern(
            (1, qw_bytes),
            2 * cb * blocks_per_row * BLOCK_BYTES,
            [blocks_per_row, 2, BLOCK_BYTES // 512, 512],
            [BLOCK_BYTES, blocks_per_row * BLOCK_BYTES, 512, 1],
        )

    # One drain per k-half of each output tile. DRAIN_DIMS spends every
    # dimension on the half, so the tile index and the half both ride in the
    # offset.
    def out_tap(cb, kb, h):
        return TensorAccessPattern(
            (1, out_blocks),
            (cb * k_tiles + kb) * TILE_BLOCKS + h * HALF_BLOCKS,
            [d[0] for d in DRAIN_DIMS],
            [d[1] for d in DRAIN_DIMS],
        )

    def sequence(QW, OUT, qw_prod_hs, out_cons_hs):
        for r in range(rounds):
            tg = TaskGroup()
            for c in range(COLS):
                cb = r * COLS + c
                if cb >= n_blocks:
                    continue
                qw_prod_hs[c].fill(QW, qw_tap(cb), group=tg)
                for kb in range(k_tiles):
                    for h in range(HALVES):
                        out_cons_hs[c][h].drain(
                            OUT, out_tap(cb, kb, h), wait=True, group=tg
                        )
            tg.finish()

    rt = Runtime(sequence, [qw_l3_ty, out_l3_ty, qw_prods, out_conses])
    prog = Program(dev, rt, workers=workers)
    if trace_size > 0:
        prog.enable_trace(trace_size)
    return prog.resolve_program()
