# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Softcapped logits from a q4nx vocabulary.

Each core RMS-normalizes the token once. Each round, the core computes M_TILE
out-features. The core accumulates one weight block per K_TILE in-features and
applies the tanh softcap to the sums.
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
)
from aie.iron.controlflow import range_
from aie.iron.device import Tile

from aie.iron import kernels

from iron.common.device_utils import call_factory
from iron.operators.flm.dataflow import grid
from iron.operators.flm.q4nx import BLOCK_BYTES, GROUP, K_TILE, M_TILE, packed_bytes

# Words of the int32 RTP buffer. Word 0 holds the softcap. The other words pad
# the buffer to the granularity of the RTP write addresses.
RTP_WORDS = 32

# The sequence finishes each round's TaskGroup DEPTH rounds later. The finish
# frees the round's BDs for the bd-id allocator. A shim tile holds 16 BDs.
DEPTH = 2

# Core stack bytes. The kernel's b_group_sums array grows with dim. The array
# overflows the default stack of 1024 bytes at both Gemma 4 sizes.
STACK_SIZE = 10 * 1024


def vocab_per_round(dev) -> int:
    """Out-features the whole array produces in one round."""
    cols, rows = grid(dev)
    return cols * rows * M_TILE


def check_shape(dev, dim, vocab):
    """Reject a device or shape the design does not support."""
    if dev.arch != AIEArch.AIE2p:
        raise NotImplementedError("the q4nx_lm_head kernel is AIE2P only")
    if dim % K_TILE:
        raise ValueError(f"dim ({dim}) must be a multiple of {K_TILE}")
    if vocab % vocab_per_round(dev):
        raise ValueError(
            f"vocab ({vocab}) must be a multiple of {vocab_per_round(dev)}, "
            "the out-features one round produces"
        )


def lm_head_kernel(dim: int, device=None):
    """The flm_gemma4_q4nx_lm_head kernel build that the cores link."""
    return call_factory(
        kernels.flm_gemma4_q4nx_lm_head,
        device=device,
        dim=dim,
        m_tile=M_TILE,
        k_tile=K_TILE,
        group=GROUP,
    )


def lm_head(dev, dim, vocab, softcap, trace_size=0):
    """Program for :class:`~iron.operators.flm.LMHead`, which documents the arguments.

    X holds the token and its RMS weight. One transfer therefore carries both norm inputs.
    """
    check_shape(dev, dim, vocab)

    COLS, ROWS = grid(dev)
    K_BLKS = dim // K_TILE
    ROUNDS = vocab // vocab_per_round(dev)

    bf16 = np.dtype[bfloat16]

    # The w fifos move q4nx blocks as bf16 elements. The kernel reinterprets
    # the bytes.
    w_blk = BLOCK_BYTES // np.dtype(bfloat16).itemsize

    # ObjectFifo element types. A w or y column object holds one block per core
    # row. The split and the join separate or combine the blocks.
    x_ty = np.ndarray[(dim, 2), bf16]
    w_col_ty = np.ndarray[(ROWS, w_blk), bf16]
    w_blk_ty = np.ndarray[(w_blk,), bf16]
    y_col_ty = np.ndarray[(ROWS, M_TILE), bf16]
    y_blk_ty = np.ndarray[(M_TILE,), bf16]

    # Core-local scratch.
    y_acc_ty = np.ndarray[(M_TILE,), np.dtype[np.float32]]
    sums_ty = np.ndarray[(dim // GROUP,), bf16]
    rtp_ty = np.ndarray[(RTP_WORDS,), np.dtype[np.int32]]

    kernel = lm_head_kernel(dim, dev)
    k_rms = kernel.entry("q4nx_lm_head_rms", [x_ty, sums_ty])
    k_zero = kernel.entry("q4nx_lm_head_zero", [y_acc_ty])
    k_block = kernel.entry(
        "q4nx_lm_head_block", [w_blk_ty, x_ty, y_acc_ty, sums_ty, np.int32]
    )
    k_epi = kernel.entry("q4nx_lm_head_epilogue", [y_blk_ty, y_acc_ty, rtp_ty])

    # The host addresses the DMAs by column. The design therefore pins the shim
    # tiles. The placer places the other tiles.
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

    y_l3_ty = np.ndarray[(vocab,), bf16]
    w_l3_ty = np.ndarray[
        (packed_bytes(vocab * dim) // np.dtype(np.uint32).itemsize,),
        np.dtype[np.uint32],
    ]
    x_l3_ty = np.ndarray[(2 * dim,), bf16]

    of_x = ObjectFifo(x_ty, name="x")
    x_prod = of_x.prod(tile=IT[0])

    workers, w_prods, y_conses, rtps = [], [], [], []
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

    # npu_write_rtp writes i32 words. The softcap travels as its f32 bit
    # pattern.
    softcap_bits = struct.unpack("<i", struct.pack("<f", float(softcap)))[0]

    def sequence(Y, W, X, x_prod, w_prods, y_conses, rtps):
        for rtp in rtps:
            rtp[0] = softcap_bits

        # One broadcast sends the token to every core. The broadcast has no
        # completion token. x_task.free() frees its BD at the end.
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
                # A strided descriptor places weight rows at the wrong on-chip
                # positions. Each column therefore reads one contiguous slice.
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
