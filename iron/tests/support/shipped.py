# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""FastFlowLM's shipped ``mm`` binary, as a second form of ``flm.ProjectionGEMM``.

The port (``iron.operators.flm.gemm.op.ProjectionGEMM``) is built from source;
this is the binary it was ported from, downloaded and pinned by digest, and
driven by the same declaration, so the port can be measured against it:

```python
Shipped(M=1024, K=1536, N=6144, epilogue="silu")
```

NPU2 only: its cores and routes are the 8-column image's. It rounds in the
core's floor mode, as ``ProjectionGEMM(rounding=Rounding.FLOOR)`` does.
"""

import dataclasses

import numpy as np
from aie.dialects.aie import AIEArch, DMAChannelDir
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, DmaEndpoint, In, Lock, Out
from aie.iron.device import Tile
from aie.utils.compile.jit.params import Select, param, tunable
from ml_dtypes import bfloat16

from iron.common import Block, Built, Precision, Unresolvable, Xclbin
from iron.operators.flm.gemm.design import (
    K_TILE,
    M_TILE,
    S,
    T,
)
from iron.operators.flm.gemm.op import ProjectionGEMM

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
PARAMETER_WORDS = 8
# Outstanding transfers per shim channel. The memtiles hold two objects per
# stream, so a third transfer would overwrite one still in use.
QUEUE_DEPTH = 2
MIN_M = M_TILE * ROWS


def _parameter_words(op) -> list[int]:
    """Return the image's block of eight words.

    k_iters, M, N, bias, epilogue mode, clamp on, clamp min, clamp max.
    """
    return [
        op.K // K_TILE,
        op.M,
        op.N,
        0,  # bias, which the operator does not expose
        op.epilogue.mode,
        0,  # clamp, which the operator does not expose
        0,
        0,
    ]


@dataclasses.dataclass(frozen=True, kw_only=True)
class _Built(Built):
    """The image's build, with the locks the sequence releases."""

    parameter_locks: list[Lock]


class Shipped(
    ProjectionGEMM,
    image=Xclbin(
        url=XCLBIN_URL,
        sha256=XCLBIN_SHA256,
        filename=f"flm_mm_{FASTFLOWLM_COMMIT[:8]}.xclbin",
        kernel_name="MLIR_AIE",
    ),
):
    """The shipped 4x8 NPU2 ``mm`` binary: its pins and its parameter block."""

    # The port's tunables, fixed by the binary. B is bf16 (no bfp16 on this
    # image), one row-block per B fetch, and the whole of K in one slice.
    tile_n: int = tunable(default=N_TILE, repr=False, init=False)
    k_tile: int = tunable(default=K_TILE, repr=False, init=False)
    ct_k: int = tunable(default=K_TILE, repr=False, init=False)
    tile_ma: int = tunable(default=M_TILE, repr=False, init=False)
    m_chunk: int = tunable(default=1, repr=False, init=False)
    rows: int = tunable(default=ROWS, repr=False, init=False)
    cols: int = tunable(default=COLS, repr=False, init=False)
    joins: int = tunable(default=1, repr=False, init=False)
    precision: Precision = param(
        default=Precision.MEDIUM, array=True, repr=False, init=False
    )
    emulate_bf16_mmul_with_bfp16: bool = tunable(default=True, repr=False, init=False)
    bfp16_b: bool = param(default=False, array=True, repr=False, init=False)
    b_dtype: object = param(default=bfloat16, repr=False, init=False)
    l1_b_depth: int = tunable(default=QUEUE_DEPTH, repr=False, init=False)
    a_l2: int = tunable(default=M_TILE * K_TILE, repr=False, init=False)
    b_l2: int = tunable(default=K_TILE * N_TILE, repr=False, init=False)
    c_l2: int = tunable(default=ROWS * M_TILE * N_TILE, repr=False, init=False)

    # One (M_TILE x K_TILE) block per object, broadcast along a compute row.
    A = In(
        ProjectionGEMM.M,
        ProjectionGEMM.K,
        obj_shape=(M_TILE, K_TILE),
        per=(ProjectionGEMM.rows,),
        depth=QUEUE_DEPTH,
    )
    B = In(
        Select(
            bfp16_b,
            (ProjectionGEMM.packed_blocks,),
            (ProjectionGEMM.K, ProjectionGEMM.N),
        ),
        dtype=b_dtype,
        obj_shape=(K_TILE, N_TILE),
        per=(ProjectionGEMM.cols,),
        depth=QUEUE_DEPTH,
    )
    # The joined (ROWS*M_TILE x N_TILE) block.
    C = Out(
        ProjectionGEMM.M,
        ProjectionGEMM.N,
        obj_shape=(ROWS * M_TILE * N_TILE,),
        per=(ProjectionGEMM.cols,),
        depth=QUEUE_DEPTH,
    )
    # The port's named values are not this image's: it reads one block of
    # eight words behind a lock, written once per shape.
    n_val = m_row_blocks = k_iters = mode = clamp_min = clamp_max = None
    n_units = units_valid = units_repeat = a_half = c_half = valid = None
    b_passes_repeat = b_resident = None
    parameters = Block(PARAMETER_WORDS, derive=_parameter_words)

    def build(self) -> Built:
        """Return what the sequence reaches of the image.

        The shim channels each operand's lanes stream on, each core's
        parameter block at the address its program reads, and the lock it
        waits on, which the sequence releases (``parameter_locks``).
        """
        mm2s, s2mm = DMAChannelDir.MM2S, DMAChannelDir.S2MM
        shims = [Tile(c, 0) for c in range(COLS)]
        pins = [
            (self.A, [DmaEndpoint(shims[c], mm2s, 0) for c in A_SOURCE_COL]),
            (self.B, [DmaEndpoint(shims[c], mm2s, 1) for c in range(COLS)]),
            (self.C, [DmaEndpoint(shims[c], s2mm, 0) for c in range(COLS)]),
        ]
        for operand, ends in pins:
            operand.pin(ends)
        dev = self.dev
        cores = [Tile(col, row) for row in dev.core_rows for col in range(dev.cols)]
        blocks = [
            Buffer(
                np.ndarray[(PARAMETER_WORDS,), np.dtype[np.int32]],
                name=f"rtp_{tile.col}_{tile.row}",
                tile=tile,
                use_write_rtp=True,
                address=RTP_ADDRESS,
            )
            for tile in cores
        ]
        locks = [Lock(tile, lock_id=RTP_LOCK_ID) for tile in cores]
        ends = [end for _, lane_ends in pins for end in lane_ends]
        return _Built([*ends, *blocks, *locks], parameter_locks=locks)

    def resolve(self, dev):
        if dev is not None and (dev.arch is not AIEArch.AIE2p or dev.cols < 8):
            raise Unresolvable(
                "flm.gemm.Shipped is a prebuilt NPU2 overlay and needs the 8 "
                f"columns of NPU2 (aie2p); got {dev.name!r} ({dev.arch}) with "
                f"{dev.cols} columns"
            )
        return self.replace()

    def pack_b(self, B):
        """Return a row-major ``(K, N)`` B in the overlay's own order: bf16, a whole k tile a slice.

        And within a block the ``s`` rows outer and the ``K_TILE // s``
        columns inner, the reverse of ``pack_b``'s.
        """
        K, N = B.shape
        blocked = B.reshape(K // K_TILE, K_TILE // S, S, N // N_TILE, N_TILE // T, T)
        # (kb, i, s_in, cb, tb, t_in) -> (cb, kb, tb, s_in, i, t_in)
        out = blocked.transpose(3, 0, 4, 2, 1, 5)
        return np.ascontiguousarray(out).reshape(-1).astype(bfloat16)

    @property
    def config_name(self) -> str:
        dev = self.dev
        if dev is None:
            raise Unresolvable("the shipped FLM GEMM names its device; none is bound")
        return f"FLM_MM_{FASTFLOWLM_COMMIT[:8]}_{dev.name}"

    def sequence(self, rt) -> None:
        """Write the parameter blocks, then their release, then one transfer per leg.

        One per (column-block, row-block, leg), in the order the memtiles
        consume: column-block outermost, then row-block, then column.
        """
        # Every word precedes the first release, so no core reads a
        # half-written block.
        rt.preamble()
        for lock in rt.built.parameter_locks:
            lock.set(1)
        M, K, N = self.M, self.K, self.N
        k_iters = K // K_TILE
        m_row_blocks = M // MIN_M
        # Sweeps of the whole grid, plus a trailing group of rem_blocks
        # columns. The columns outside that group still receive A, because A
        # is broadcast along a whole compute row and the row stalls if one
        # column stops draining it.
        n_full = N // (N_TILE * COLS)
        rem_blocks = (N % (N_TILE * COLS)) // N_TILE
        A = TensorAccessPattern.full((m_row_blocks, ROWS, M_TILE, k_iters, K_TILE))
        B = TensorAccessPattern.full((N // N_TILE, k_iters * K_TILE * N_TILE))
        C = TensorAccessPattern.full((m_row_blocks, ROWS * M_TILE, N // N_TILE, N_TILE))
        for mega_col in range(n_full + (1 if rem_blocks else 0)):
            active = rem_blocks if (rem_blocks and mega_col == n_full) else COLS
            for mega_row in range(m_row_blocks):
                for c in range(COLS):
                    if c in A_SOURCE_COL:
                        r = A_SOURCE_COL.index(c)
                        self.A.fill(A[mega_row, r].permute((1, 0, 2)), lane=r)
                    if c >= active:
                        continue
                    # One contiguous run: pack_b has already put this
                    # column's k-blocks in the order the memtile writes them.
                    self.B.fill(B[mega_col * COLS + c], lane=c)
                    self.C.drain(C[mega_row, :, mega_col * COLS + c], lane=c)
