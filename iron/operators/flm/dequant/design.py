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
from enum import StrEnum

import numpy as np

from aie.helpers.taplib.tap import TensorAccessPattern
from aie.helpers.util import v8bfp16ebs8
from aie.iron import Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker
from aie.iron.controlflow import range_
from aie.dialects._aie_enum_gen import AIEArch
from aie.dialects.aie import get_target_model

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

# Transfers a shim channel can have outstanding. Nothing in the toolchain
# models this and overrunning it HANGS rather than diagnoses; flm.GEMM measured
# the boundary at K=10240 M=1024, where 4 outstanding run and 8 hang. The
# window below keeps every channel inside it.
SHIM_TASK_QUEUE = 4

# Drain windows kept in flight. A window is retired only once the next has been
# issued, so the runtime sequence never blocks on an await with the shim idle:
# the window being awaited overlaps the one already running.
LIVE_WINDOWS = 2


def _run_geometry(run_out_features, run_period_out_features, n_blocks):
    """Interleave pattern in column blocks. Defaults to one run, no gap."""
    if run_out_features is None and run_period_out_features is None:
        return n_blocks, n_blocks
    if run_out_features is None or run_period_out_features is None:
        raise ValueError("run_out_features and run_period_out_features go together")
    for name, v in (
        ("run_out_features", run_out_features),
        ("run_period_out_features", run_period_out_features),
    ):
        if v % N_TILE:
            raise ValueError(f"{name} ({v}) must be a multiple of {N_TILE}")
    if run_period_out_features < run_out_features:
        raise ValueError("run_period_out_features must be at least run_out_features")
    return run_out_features // N_TILE, run_period_out_features // N_TILE


def qw_bytes_for(K, N, run_out_features=None, run_period_out_features=None):
    """Bytes the operator reads, counting any gap it has to stride over."""
    n_blocks = N // N_TILE
    run_blocks, period_blocks = _run_geometry(
        run_out_features, run_period_out_features, n_blocks
    )
    cb_bytes = N_TILE * K * 5 // 8
    last = n_blocks - 1
    return (((last // run_blocks) * period_blocks + last % run_blocks) + 1) * cb_bytes


class QwLayout(StrEnum):
    """How the q4nx blocks are ordered in the buffer handed to the operator.

    Both orders deliver the four blocks of an output tile to the same cores in
    the same sequence, so this changes the shim descriptor and nothing else --
    not the cores, not the join, not DRAIN_DIMS. Verified as index arithmetic
    by ``test_engine_order_matches_file_order``.
    """

    #: The weights file: blocks row-major, ``block_row * blocks_per_row + col``.
    FILE = "file"
    #: What FastFlowLM's engine writes to DRAM, which interleaves pairs of
    #: block-rows. That is exactly the order this design already gathers, so
    #: the descriptor degenerates to a linear read.
    ENGINE = "engine"


def dequant_bfp(
    dev,
    K,
    N,
    tile_n=N_TILE,
    qw_layout=QwLayout.FILE,
    run_out_features=None,
    run_period_out_features=None,
    trace_size=0,
):
    """K in-features, N out-features. B reaches the GEMM as (K, N).

    ``run_out_features`` and ``run_period_out_features`` describe a matrix that
    is interleaved with another one in the same buffer: this matrix occupies
    ``run_out_features`` consecutive out-features, then the next run of it
    starts ``run_period_out_features`` later. FastFlowLM packs gate and up that
    way, 512 out-features each in a 1024 period. Leave both ``None`` for a
    matrix that is contiguous over all of N.

    The caller points the operator at the matrix's own start, so these describe
    the stride pattern only, never a base offset.
    """
    # Coerce rather than compare by identity. The design generator round-trips
    # its arguments, and a StrEnum comes back as a plain str -- an `is` test
    # against it is silently false, which would take the file-order branch and
    # emit a wrongly ordered buffer of the right size.
    qw_layout = QwLayout(qw_layout)
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

    # A shim tile's buffer descriptor ids are shared across its channels and
    # directions, and TaskGroup.finish() returns them to a COMPILE-TIME
    # allocator that does not check the transfer finished. So a window's worth
    # of transfers has to fit the tile, and the window has to be awaited before
    # the next one reprograms those ids.
    #
    # One TaskGroup per column block would queue BDS_PER_K_TILE * k_tiles of
    # them, which overflows a 16-BD tile at k_tiles >= 6 and the channel queue
    # well before that. E2B reaches k_tiles = 24 at K = 12288.
    # Two windows are live at once -- the previous one is retired only after
    # the next is issued -- so both budgets count 2 * k_window. The fill is one
    # descriptor per column block and outlives them all.
    shim_bds = get_target_model(dev.resolve()).get_num_bds(0, 0)
    k_window = min(
        k_tiles,
        SHIM_TASK_QUEUE // LIVE_WINDOWS,
        (shim_bds - 1) // (LIVE_WINDOWS * HALVES),
    )
    if k_window < 1:
        raise ValueError(
            f"a shim tile with {shim_bds} descriptors and a queue of "
            f"{SHIM_TASK_QUEUE} cannot hold one drain window"
        )

    # One column block is N_TILE out-features over all of K, and its q4nx
    # blocks are contiguous in both layouts.
    cb_bytes = N_TILE * K * 5 // 8
    run_blocks, period_blocks = _run_geometry(
        run_out_features, run_period_out_features, n_blocks
    )

    def qw_offset(cb):
        """Byte offset of column block cb, from the start of this matrix."""
        return ((cb // run_blocks) * period_blocks + cb % run_blocks) * cb_bytes

    # The buffer has to span the gaps, so it is the reach of the last column
    # block rather than the matrix's own size.
    qw_bytes = qw_offset(n_blocks - 1) + cb_bytes
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

    # Both layouts hand the cores the same blocks in the same sequence; only
    # the descriptor that produces that sequence differs.
    #
    # In file order the fill walks (block-column, n-half, block bytes). The
    # k-half and the k-tile index both step whole blocks along a row, so they
    # collapse into one dimension of blocks_per_row -- which leaves a dimension
    # free to split the 5120-byte block into 10 x 512, keeping the innermost
    # size inside the BD's 10-bit field.
    #
    # In engine order those blocks are already adjacent, so the gather
    # degenerates to a linear read of the whole column block. At K = 12288 the
    # outer count is 960, inside the same field.
    #
    # One fill carries a whole column block. In engine order that is a single
    # linear burst of every k-tile at once, which is why the fill costs one
    # descriptor no matter how tall K is -- only the drains scale with k_tiles.
    if qw_layout is QwLayout.ENGINE:
        qw_sizes = [blocks_per_row, 2, BLOCK_BYTES // 512, 512]
        qw_strides = [2 * BLOCK_BYTES, BLOCK_BYTES, 512, 1]
    else:
        qw_sizes = [blocks_per_row, 2, BLOCK_BYTES // 512, 512]
        qw_strides = [BLOCK_BYTES, blocks_per_row * BLOCK_BYTES, 512, 1]

    def qw_tap(cb):
        return TensorAccessPattern((1, qw_bytes), qw_offset(cb), qw_sizes, qw_strides)

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
            # The fill has to outlive every drain window that consumes it, so
            # it gets its own group. Its descriptor is freed once the round's
            # last drain has been awaited.
            tg_fill = TaskGroup()
            for c in range(COLS):
                cb = r * COLS + c
                if cb < n_blocks:
                    qw_prod_hs[c].fill(QW, qw_tap(cb), group=tg_fill)

            prev = None
            for kb0 in range(0, k_tiles, k_window):
                tg = TaskGroup()
                for c in range(COLS):
                    cb = r * COLS + c
                    if cb >= n_blocks:
                        continue
                    for kb in range(kb0, min(kb0 + k_window, k_tiles)):
                        for h in range(HALVES):
                            out_cons_hs[c][h].drain(
                                OUT, out_tap(cb, kb, h), wait=True, group=tg
                            )
                # Retire the PREVIOUS window, now that this one is issued and
                # running. finish() awaits, so doing it here overlaps the wait
                # with live transfers instead of draining the shim first.
                if prev is not None:
                    prev.finish()
                prev = tg
            if prev is not None:
                prev.finish()
            tg_fill.finish()

    rt = Runtime(sequence, [qw_l3_ty, out_l3_ty, qw_prods, out_conses])
    prog = Program(dev, rt, workers=workers)
    if trace_size > 0:
        prog.enable_trace(trace_size)
    return prog.resolve_program()
