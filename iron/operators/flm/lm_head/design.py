# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Final-logits projection against a q4nx vocabulary.

One core owns one 32-out-feature tile at a time and streams the vocabulary past
it: the token is RMS-normalized once on arrival, then every weight block that
lands accumulates into the tile, and a tanh softcap writes the logits out.
"""

import struct

import numpy as np
from ml_dtypes import bfloat16

from aie.dialects._aie_enum_gen import AIEArch
from aie.iron import (
    Buffer,
    ObjectFifo,
    Program,
    Runtime,
    TaskGroup,
    Worker,
    ceildiv,
)
from aie.iron.controlflow import range_
from aie.iron.device import AnyComputeTile, Tile

from aie.iron import kernels

from iron.common.device_utils import call_factory

# q4nx block: 32 out-features x 256 in-features, 32 weights per scale and min.
M_TILE, K_TILE, GROUP = 32, 256, 32
BITS_PER_WEIGHT = 5  # a 4-bit code plus a shared 6-bit scale and min per group
BLOCK_BYTES = M_TILE * K_TILE * BITS_PER_WEIGHT // 8

# Words of the int32 RTP bank. One holds the softcap; the rest pad it to the
# bank granularity the RTP write addresses.
RTP_WORDS = 32

# A shim tile allows 16 live BDs. Each round's transfers go in one TaskGroup
# finished DEPTH rounds later, so the bd-id allocator rotates instead of
# clobbering an in-flight BD.
DEPTH = 2

# The core's stack: b_group_sums scales with dim, so the 1024-byte device
# default is not enough at either Gemma 4 size.
STACK_SIZE = 10 * 1024


def packed_bytes(n_weights: int) -> int:
    """Bytes holding n_weights in q4nx packing."""
    return n_weights * BITS_PER_WEIGHT // 8


def grid(dev):
    """Columns and compute rows the design spreads the vocabulary over."""
    rows = sum(
        dev.get_tile_type(0, r) == AnyComputeTile.tile_type for r in range(dev.rows)
    )
    return dev.cols, rows


def vocab_per_round(dev) -> int:
    """Out-features the whole array produces in one round."""
    cols, rows = grid(dev)
    return cols * rows * M_TILE


def lm_head_kernel(dim: int, device=None):
    """The flm_q4nx_lm_head build this design's cores link."""
    return call_factory(
        kernels.flm_q4nx_lm_head,
        device=device,
        dim=dim,
        m_tile=M_TILE,
        k_tile=K_TILE,
        group=GROUP,
    )


def lm_head(dev, dim, vocab, softcap, trace_size=0):
    """dim in-features, vocab out-features, softcap the tanh bound.

    X carries the token followed by its RMS weight, so one transfer feeds the
    norm. W is the q4nx vocabulary, Y the softcapped logits.
    """
    if dev.arch != AIEArch.AIE2p:
        raise NotImplementedError("the q4nx_lm_head kernel is AIE2P only")
    if dim % K_TILE:
        raise ValueError(f"dim ({dim}) must be a multiple of {K_TILE}")
    if vocab % vocab_per_round(dev):
        raise ValueError(
            f"vocab ({vocab}) must be a multiple of {vocab_per_round(dev)}, "
            "the out-features one round produces"
        )

    COLS, ROWS = grid(dev)
    K_BLKS = ceildiv(dim, K_TILE)
    ROUNDS = vocab // vocab_per_round(dev)

    bf16 = np.dtype[bfloat16]

    # One packed q4nx block, counted in bf16 elements: that is the unit the w
    # fifos move, and the kernel reinterprets it.
    w_blk = BLOCK_BYTES // np.dtype(bfloat16).itemsize

    # ObjectFifo element types. The w and y column objects carry one row per
    # core and are split or joined a row at a time.
    x_ty = np.ndarray[(dim, 2), bf16]  # token and its rms weight
    w_col_ty = np.ndarray[(ROWS, w_blk), bf16]
    w_blk_ty = np.ndarray[(w_blk,), bf16]
    y_col_ty = np.ndarray[(ROWS, M_TILE), bf16]
    y_blk_ty = np.ndarray[(M_TILE,), bf16]

    # Core-local scratch.
    y_acc_ty = np.ndarray[(M_TILE,), np.dtype[np.float32]]
    sums_ty = np.ndarray[(dim // GROUP,), bf16]
    rtp_ty = np.ndarray[(RTP_WORDS,), np.dtype[np.int32]]

    kernel_object = lm_head_kernel(dim, dev).object_file
    k_rms = kernel_object.bind("q4nx_lm_head_rms", [x_ty, sums_ty])
    k_zero = kernel_object.bind("q4nx_lm_head_zero", [y_acc_ty])
    k_block = kernel_object.bind(
        "q4nx_lm_head_block", [w_blk_ty, x_ty, y_acc_ty, sums_ty, np.int32]
    )
    k_epi = kernel_object.bind("q4nx_lm_head_epilogue", [y_blk_ty, y_acc_ty, rtp_ty])

    # Only the shim tiles are pinned: the host addresses them by column for the
    # DMAs and the RTP writes. The placer sites the rest, held to the matching
    # column by the fifo routing.
    IT = [Tile(j, 0) for j in range(COLS)]

    def core_fn(x_in, w_in, y_out, k_rms, k_zero, k_block, k_epi, y_acc, sums, rtp):
        x = x_in.acquire(1)
        k_rms(x, sums)
        for _ in range_(ROUNDS):
            k_zero(y_acc)
            for k in range_(K_BLKS):
                w = w_in.acquire(1)
                k_block(w, x, y_acc, sums, k)
                w_in.release(1)
            y = y_out.acquire(1)
            k_epi(y, y_acc, rtp)
            y_out.release(1)
        x_in.release(1)

    # Host buffers. The order (y, w, x) is the operator's argument order.
    y_l3_ty = np.ndarray[(vocab,), bf16]
    w_l3_ty = np.ndarray[
        (packed_bytes(vocab * dim) // np.dtype(np.uint32).itemsize,),
        np.dtype[np.uint32],
    ]
    x_l3_ty = np.ndarray[(2 * dim,), bf16]

    of_x = ObjectFifo(x_ty, name="x")
    x_prod = of_x.prod(tile=IT[0])

    workers = []
    w_prods, y_conses, rtps = [], [], []
    for j in range(COLS):
        of_w = ObjectFifo(w_col_ty, name=f"w{j}")
        w_prods.append(of_w.prod(tile=IT[j]))
        w_cores = of_w.cons().split(
            [w_blk * i for i in range(ROWS)],
            obj_types=[w_blk_ty] * ROWS,
            names=[f"w{j}_{i}" for i in range(ROWS)],
        )

        of_y = ObjectFifo(y_col_ty, name=f"y{j}")
        y_conses.append(of_y.cons(tile=IT[j]))
        y_cores = of_y.prod().join(
            [M_TILE * i for i in range(ROWS)],
            obj_types=[y_blk_ty] * ROWS,
            names=[f"y{j}_{i}" for i in range(ROWS)],
        )

        for i in range(ROWS):
            y_acc = Buffer(type=y_acc_ty, name=f"yacc_{i}_{j}")
            sums = Buffer(type=sums_ty, name=f"sums_{i}_{j}")
            rtp = Buffer(type=rtp_ty, name=f"rtp_{i}_{j}", use_write_rtp=True)
            rtps.append(rtp)
            workers.append(
                Worker(
                    core_fn,
                    [
                        of_x.cons(),
                        w_cores[i].cons(),
                        y_cores[i].prod(),
                        k_rms,
                        k_zero,
                        k_block,
                        k_epi,
                        y_acc,
                        sums,
                        rtp,
                    ],
                    stack_size=STACK_SIZE,
                )
            )

    M_PER_COL = ROWS * M_TILE  # y elements one column drains per round
    M_PER_ROUND = COLS * M_PER_COL
    W_PER_COL = packed_bytes(M_PER_COL * dim) // np.dtype(np.uint32).itemsize
    W_PER_ROUND = W_PER_COL * COLS

    # npu_write_rtp writes i32, so the softcap travels as its float bit pattern
    # and the kernel reads it back as a float.
    softcap_bits = struct.unpack("<i", struct.pack("<f", float(softcap)))[0]

    def sequence(Y, W, X, x_prod, w_prods, y_conses, rtps):
        for rtp in rtps:
            rtp[0] = softcap_bits

        # One broadcast of the token to every core, with no completion token.
        # Its BD is retired at the tail.
        x_task = x_prod.fill(
            X,
            sizes=[1, 1, 1, 2 * dim],
            strides=[0, 0, 0, 1],
            offset=0,
            transfer_len=2 * dim,
            wait=False,
            managed=False,
        )

        window = []
        for rnd in range(ROUNDS):
            tg = TaskGroup()
            for col in range(COLS):
                y_conses[col].drain(
                    Y,
                    sizes=[1, 1, 1, M_PER_COL],
                    strides=[0, 0, 0, 1],
                    offset=rnd * M_PER_ROUND + col * M_PER_COL,
                    transfer_len=M_PER_COL,
                    wait=True,
                    group=tg,
                )
                # A contiguous slice. A strided descriptor lands weight rows at
                # the wrong on-chip positions.
                w_prods[col].fill(
                    W,
                    sizes=[1, 1, 1, W_PER_COL],
                    strides=[0, 0, 0, 1],
                    offset=rnd * W_PER_ROUND + col * W_PER_COL,
                    transfer_len=W_PER_COL,
                    wait=False,
                    group=tg,
                )

            window.append(tg)
            if len(window) > DEPTH:
                window.pop(0).finish()

        for tg in window:
            tg.finish()
        x_task.free()

    rt = Runtime(sequence, [y_l3_ty, w_l3_ty, x_l3_ty, x_prod, w_prods, y_conses, rtps])
    prog = Program(dev, rt, workers=workers)
    if trace_size > 0:
        prog.enable_trace(trace_size)
    return prog.resolve_program()
