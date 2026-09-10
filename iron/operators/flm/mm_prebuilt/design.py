# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Runtime sequence for the prebuilt FastFlowLM ``mm`` overlay.

The overlay ships as a binary xclbin, so this module emits only the host-side
half of a dispatch: the shim DMA transfers and the runtime parameters. Every
core program, memtile buffer and stream-switch route comes from the xclbin.

Three properties of the overlay set what this sequence must do, and none of
them are visible in the xclbin:

  * **The cores read their shape from runtime parameters.** One overlay serves
    every GEMM in a model, so ``K/K_TILE``, ``M`` and ``N``, the activation
    and the clamp all arrive as words in each core's data memory. A core
    blocks on :data:`RTP_LOCK_ID` until the sequence releases it, so a
    dispatch that writes no parameters hangs.
  * **The shim channel map is fixed.** A arrives on MM2S channel 0 of columns
    0, 2, 4 and 6; B on MM2S channel 1 of every column; C leaves on S2MM
    channel 0 of every column. The allocations below reproduce that map.
  * **B arrives pre-packed**, in the order :func:`iron.operators.flm.packing`
    produces.

``iron.operators.flm.gemm`` is a port of this overlay, so the two agree on
tiling, on the byte order of each transfer and on the packed B layout. Its own
instruction stream still cannot drive this xclbin: it writes no runtime
parameters, and its lowering puts B on MM2S channel 0 in the odd columns.
"""

import numpy as np

from aie.dialects import aie, aiex
from aie.dialects.aie import DMAChannelDir
from aie.extras.context import mlir_mod_ctx
from aie.ir import BF16Type, MemRefType

from iron.operators.flm.gemm.design import (
    EPILOGUE_MODES,
    K_TILE,
    MAX_COLS,
    M_TILE,
    ROWS,
    a_source_cols,
)

# The shipped overlay is built with n=128 on the full 8-column NPU2 grid; every
# other tiling knob matches flm.gemm, whose constants are imported above.
N_TILE = 128
COLS = MAX_COLS
A_SOURCE_COL = a_source_cols(COLS)

# Core data memory holding the runtime parameters, and the lock a core waits
# on before it reads them. Both are baked into the overlay's core programs.
RTP_ADDRESS = 4096
LOCK_ADDRESS_BASE = 0x1F000
RTP_LOCK_ID = 10

# Outstanding transfers per shim channel. The overlay's memtiles hold two
# objects per stream, so a third transfer would overwrite one still in use.
QUEUE_DEPTH = 2

MIN_M = M_TILE * ROWS
MIN_K = K_TILE


def mm_prebuilt(dev, M, K, N, epilogue="none", clamp=None):
    """Emit the MLIR module whose runtime sequence drives the overlay.

    A is ``(M, K)`` row-major and C is ``(M, N)`` row-major, both bf16. B is
    ``(K, N)`` reordered by :meth:`MMPrebuilt.pack_B`.
    """
    if epilogue not in EPILOGUE_MODES:
        raise ValueError(
            f"epilogue must be one of {sorted(EPILOGUE_MODES)}, got {epilogue!r}"
        )
    for name, value, unit in (("M", M, MIN_M), ("K", K, MIN_K), ("N", N, N_TILE)):
        if value % unit != 0:
            raise ValueError(f"{name} ({value}) must be a multiple of {unit}")

    k_iters = K // K_TILE
    m_row_blocks = M // MIN_M
    # Sweeps of the whole grid, plus a trailing group of rem_blocks columns.
    # The columns outside that group still receive A, because A is broadcast
    # along a whole compute row and the row stalls if one column stops
    # draining it.
    n_full = N // (N_TILE * COLS)
    rem_blocks = (N % (N_TILE * COLS)) // N_TILE

    clamp_min, clamp_max = clamp if clamp is not None else (0.0, 0.0)
    parameters = [
        (RTP_ADDRESS + 0, k_iters),
        (RTP_ADDRESS + 4, M),
        (RTP_ADDRESS + 8, N),
        (RTP_ADDRESS + 12, 0),  # bias, which this operator does not expose
        (RTP_ADDRESS + 16, EPILOGUE_MODES[epilogue]),
        (RTP_ADDRESS + 20, 1 if clamp is not None else 0),
        (RTP_ADDRESS + 24, int(np.float32(clamp_min).view(np.int32))),
        (RTP_ADDRESS + 28, int(np.float32(clamp_max).view(np.int32))),
    ]

    with mlir_mod_ctx() as ctx:
        bf16 = BF16Type.get()
        a_ty = MemRefType.get((M * K,), bf16)
        b_ty = MemRefType.get((K * N,), bf16)
        c_ty = MemRefType.get((M * N,), bf16)

        @aie.device(dev.resolve())
        def device_body():
            shim = [aie.tile(c, 0) for c in range(COLS)]
            for r in range(ROWS):
                aie.shim_dma_allocation(
                    f"A_{r}", shim[A_SOURCE_COL[r]], DMAChannelDir.MM2S, 0
                )
            for c in range(COLS):
                aie.shim_dma_allocation(f"B_{c}", shim[c], DMAChannelDir.MM2S, 1)
                aie.shim_dma_allocation(f"C_{c}", shim[c], DMAChannelDir.S2MM, 0)

            @aiex.runtime_sequence(a_ty, b_ty, c_ty)
            def sequence(A, B, C):
                # Every core gets the same parameters; the overlay derives the
                # per-tile work from its own coordinates.
                for row in range(2, 2 + ROWS):
                    for col in range(COLS):
                        for address, value in parameters:
                            aiex.npu_write32(address, value, column=col, row=row)
                        aiex.npu_write32(
                            LOCK_ADDRESS_BASE + 16 * RTP_LOCK_ID,
                            1,
                            column=col,
                            row=row,
                        )

                outstanding = {}

                def transfer(allocation, buffer, offset, sizes, strides):
                    queue = outstanding.setdefault(allocation, [])
                    if len(queue) == QUEUE_DEPTH:
                        aiex.dma_await_task(queue.pop(0))
                    task = aiex.shim_dma_single_bd_task(
                        allocation,
                        buffer,
                        offset=offset,
                        sizes=sizes,
                        strides=strides,
                        issue_token=True,
                    )
                    aiex.dma_start_task(task)
                    queue.append(task)

                # One transfer per (column-block, row-block, leg), matching the
                # order the overlay's memtiles consume: column-block outermost,
                # then row-block, then column.
                for mega_col in range(n_full + (1 if rem_blocks else 0)):
                    active = rem_blocks if (rem_blocks and mega_col == n_full) else COLS
                    for mega_row in range(m_row_blocks):
                        for c in range(COLS):
                            if c in A_SOURCE_COL:
                                r = A_SOURCE_COL.index(c)
                                transfer(
                                    f"A_{r}",
                                    A,
                                    mega_row * ROWS * M_TILE * K + r * M_TILE * K,
                                    [1, k_iters, M_TILE, K_TILE],
                                    [0, K_TILE, K, 1],
                                )
                            if c >= active:
                                continue
                            # One contiguous run: pack_B has already put this
                            # column's k-blocks in the order the memtile
                            # writes them.
                            transfer(
                                f"B_{c}",
                                B,
                                (mega_col * COLS + c) * N_TILE * K,
                                [1, 1, 1, k_iters * K_TILE * N_TILE],
                                [0, 0, 0, 1],
                            )
                            transfer(
                                f"C_{c}",
                                C,
                                mega_col * COLS * N_TILE
                                + mega_row * ROWS * M_TILE * N
                                + c * N_TILE,
                                [1, 1, ROWS * M_TILE, N_TILE],
                                [0, 0, N, 1],
                            )

                for queue in outstanding.values():
                    for task in queue:
                        aiex.dma_await_task(task)

        return str(ctx.module)
