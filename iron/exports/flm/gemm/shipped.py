# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""FastFlowLM's shipped ``mm`` binary, as a second form of :class:`flm.GEMM`.

The port (:class:`iron.exports.flm.gemm.op.GEMM`) is built from source;
this is the binary it was ported from, downloaded and pinned by digest, and
driven by the same declaration::

    Shipped(M=1024, K=1536, N=6144, epilogue="silu")

It exists so the port can be measured against what it was ported from, on
identical inputs and through the same host path. NPU2 only: the image is
an 8-column binary.

Nothing here is built. The class names what is baked into the xclbin and
visible nowhere in it: the shim channel map (A on MM2S channel 0 of columns
0, 2, 4 and 6; B on MM2S channel 1 of every column; C out of S2MM channel
0 of every column), the address and lock of the eight parameter words every
core reads, and the order the memtiles consume transfers in. The library
emits the sequence against those pins (:mod:`iron.common.external`).

What differs from the port, and why the port is the default: the port
selects its epilogue at build time (a branch-free inner loop, one build per
activation), this binary at run time; the port rounds ``conv_even``, this
binary runs in the core's power-up floor mode and carries a ~1% truncation
bias; the port packs B in ``mm_fused_mmul_2x2``'s k order, this binary in
its own (``overlay_order``). ``GEMM(rounding=Rounding.FLOOR)`` on the port
reproduces this overlay bit for bit without an activation.
"""

import dataclasses
from typing import ClassVar

import numpy as np
from ml_dtypes import bfloat16

from iron.common import In, Out, Shim, Unresolvable, Value, Xclbin, auto, select
from iron.common.tiling import Access
from iron.exports.flm.gemm.design import K_TILE, M_TILE, Epilogue
from iron.exports.flm.gemm.op import GEMM, _device_name

# The FastFlowLM revision the overlay is taken from. A commit SHA rather than
# a branch, so the digest below stays valid.
FASTFLOWLM_COMMIT = "f81eba7140decef5e4eda670d02a91b9d6402ee9"
XCLBIN_PATH = "src/xclbins/Gemma4-E4B-IT-NPU2/mm.xclbin"
XCLBIN_URL = (
    f"https://raw.githubusercontent.com/ROCm/FastFlowLM/{FASTFLOWLM_COMMIT}/"
    f"{XCLBIN_PATH}"
)
XCLBIN_SHA256 = "6f1e5507b84d4545536c9b8281002d0e0e10ed241f8593cb4db50eee63876e5f"

# The binary is a fixed 4x8 NPU2 grid built with n=128; these describe the
# artifact rather than follow the device.
N_TILE = 128
COLS = 8
ROWS = 4
# Which shim column sources the A broadcast for each compute row: alternate
# columns, so each has its own MM2S path and never contends with a B fill.
A_SOURCE_COL = [2 * r for r in range(ROWS)]
# Core data memory holding the runtime parameters, and the lock a core waits
# on before it reads them. Both are baked into the overlay's core programs.
RTP_ADDRESS = 4096
RTP_LOCK_ID = 10
# Outstanding transfers per shim channel. The memtiles hold two objects per
# stream, so a third transfer would overwrite one still in use.
QUEUE_DEPTH = 2
MIN_M = M_TILE * ROWS
MIN_K = K_TILE


def _parameter_words(op) -> list[int]:
    """The image's block of eight words: k_iters, M, N, bias, epilogue mode,
    clamp on, clamp min, clamp max.
    """
    clamp_min, clamp_max = op.clamp if op.clamp is not None else (0.0, 0.0)
    return [
        op.K // K_TILE,
        op.M,
        op.N,
        0,  # bias, which the operator does not expose
        Epilogue(op.epilogue).mode,
        1 if op.clamp is not None else 0,
        int(np.float32(clamp_min).view(np.int32)),
        int(np.float32(clamp_max).view(np.int32)),
    ]


class Shipped(
    GEMM,
    image=Xclbin(
        url=XCLBIN_URL,
        sha256=XCLBIN_SHA256,
        filename=f"flm_mm_{FASTFLOWLM_COMMIT[:8]}.xclbin",
        kernel_name="MLIR_AIE",
    ),
):
    """The shipped 4x8 NPU2 ``mm`` binary: its pins and its parameter block."""

    # The port's knobs, fixed by the binary. B is bf16 (no bfp16 on this
    # image), one row-block per B fetch, and the whole of K in one slice.
    tile_n: int = auto(N_TILE, repr=False, init=False)
    tile_ma: int = auto(M_TILE, repr=False, init=False)
    m_chunk: int = auto(1, repr=False, init=False)
    rows: int = auto(ROWS, repr=False, init=False)
    cols: int = auto(COLS, repr=False, init=False)
    bfp16_b: bool = auto(False, repr=False, init=False)
    b_dtype: object = auto(bfloat16, repr=False, init=False)
    l1_b_depth: int = auto(QUEUE_DEPTH, repr=False, init=False)
    shim_bds: int = auto(16, repr=False, init=False)
    a_l2: int = auto(M_TILE * K_TILE, repr=False, init=False)
    b_l2: int = auto(K_TILE * N_TILE, repr=False, init=False)
    c_l2: int = auto(ROWS * M_TILE * N_TILE, repr=False, init=False)
    b_overlay_order: ClassVar[bool] = True

    # A: one (M_TILE x K_TILE) block per transfer element, broadcast along
    # each compute row from alternate shim columns on MM2S channel 0.
    A = In(
        GEMM.M,
        GEMM.K,
        tile=(M_TILE, K_TILE),
        per=(GEMM.rows,),
        depth=QUEUE_DEPTH,
        via=[Shim(col, 0) for col in A_SOURCE_COL],
    )
    # B: one column's k-blocks, pre-packed, down each column on MM2S channel 1.
    B = In(
        select(GEMM.bfp16_b, (GEMM.packed_blocks,), (GEMM.K, GEMM.N)),
        dtype=GEMM.b_dtype,
        tile=(K_TILE, N_TILE),
        per=(GEMM.cols,),
        depth=QUEUE_DEPTH,
        via=[Shim(c, 1) for c in range(COLS)],
    )
    # C: the joined (ROWS*M_TILE x N_TILE) block, out of every column on
    # S2MM channel 0.
    C = Out(
        GEMM.M,
        GEMM.N,
        tile=(ROWS * M_TILE, N_TILE),
        per=(GEMM.cols,),
        depth=QUEUE_DEPTH,
        via=[Shim(c, 0) for c in range(COLS)],
    )
    # The port's named values are not this image's: it reads one block of
    # eight words behind a lock.
    n_val = m_row_blocks = k_iters = mode = clamp_min = clamp_max = None
    n_chunks = n_units = None
    rtp = Value(
        np.int32, address=RTP_ADDRESS, lock=RTP_LOCK_ID, derive=_parameter_words
    )

    def resolve(self, dev):
        if dev is not None and (dev.resolve().name != "npu2" or dev.cols < 8):
            raise Unresolvable(
                "flm.gemm.Shipped is a prebuilt NPU2 overlay and needs the 8 "
                f"columns of NPU2 (aie2p); got {dev.resolve().name!r} with "
                f"{dev.cols} columns"
            )
        return dataclasses.replace(self)

    @property
    def ct_max_k(self) -> int:
        # The binary holds the whole k tile at once; the port's table for
        # tile_n=128 does not apply.
        return K_TILE

    @property
    def config_name(self) -> str:
        return f"FLM_MM_{FASTFLOWLM_COMMIT[:8]}_{_device_name()}"

    def sequence(self, rt) -> None:
        """One transfer per (column-block, row-block, leg), in the order the
        memtiles consume: column-block outermost, then row-block, then column.
        """
        M, K, N = self.M, self.K, self.N
        k_iters = K // K_TILE
        m_row_blocks = M // MIN_M
        # Sweeps of the whole grid, plus a trailing group of rem_blocks
        # columns. The columns outside that group still receive A, because A
        # is broadcast along a whole compute row and the row stalls if one
        # column stops draining it.
        n_full = N // (N_TILE * COLS)
        rem_blocks = (N % (N_TILE * COLS)) // N_TILE
        a_n, b_n, c_n = self.A.elements, self.B.elements, self.C.elements
        for mega_col in range(n_full + (1 if rem_blocks else 0)):
            active = rem_blocks if (rem_blocks and mega_col == n_full) else COLS
            for mega_row in range(m_row_blocks):
                for c in range(COLS):
                    if c in A_SOURCE_COL:
                        r = A_SOURCE_COL.index(c)
                        rt.fill(
                            self.A.lane(r),
                            Access(
                                a_n,
                                mega_row * ROWS * M_TILE * K + r * M_TILE * K,
                                (1, k_iters, M_TILE, K_TILE),
                                (0, K_TILE, K, 1),
                            ),
                        )
                    if c >= active:
                        continue
                    # One contiguous run: pack_B has already put this
                    # column's k-blocks in the order the memtile writes them.
                    rt.fill(
                        self.B.lane(c),
                        Access(
                            b_n,
                            (mega_col * COLS + c) * N_TILE * K,
                            (1, 1, 1, k_iters * K_TILE * N_TILE),
                            (0, 0, 0, 1),
                        ),
                    )
                    rt.drain(
                        self.C.lane(c),
                        Access(
                            c_n,
                            mega_col * COLS * N_TILE
                            + mega_row * ROWS * M_TILE * N
                            + c * N_TILE,
                            (1, 1, ROWS * M_TILE, N_TILE),
                            (0, 0, N, 1),
                        ),
                    )
