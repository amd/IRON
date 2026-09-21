# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the prebuilt FastFlowLM ``mm`` overlay is, as constants.

The overlay ships as a binary xclbin, so nothing here is built: these are the
facts about the artifact that its sequence (``op.py``) must honour and that
are visible nowhere in the xclbin itself.

  * **The cores read their shape from runtime parameters.** One overlay
    serves every GEMM in a model, so ``K/K_TILE``, ``M`` and ``N``, the
    activation and the clamp all arrive as words in each core's data memory
    at :data:`RTP_ADDRESS`. A core blocks on :data:`RTP_LOCK_ID` until the
    sequence releases it, so a dispatch that writes no parameters hangs.
  * **The shim channel map is fixed.** A arrives on MM2S channel 0 of
    columns 0, 2, 4 and 6; B on MM2S channel 1 of every column; C leaves on
    S2MM channel 0 of every column. ``MMPrebuiltOverlay`` pins exactly that.
  * **B arrives pre-packed**, in the order :func:`iron.operators.flm.packing`
    produces with ``overlay_order=True``.

``iron.operators.flm.gemm`` is a port of this overlay, so the two agree on
tiling, on the byte order of each transfer and on the packed B layout. Its
own instruction stream still cannot drive this xclbin: it writes no runtime
parameters, and its lowering puts B on MM2S channel 0 in the odd columns.
"""

from iron.operators.flm.gemm.design import K_TILE, M_TILE

# The shipped overlay is a fixed 4x8 NPU2 binary built with n=128, so unlike
# flm.gemm these do NOT follow the device -- they describe the artifact. Every
# other tiling knob matches flm.gemm, whose constants are imported above.
N_TILE = 128
COLS = 8
ROWS = 4
# Which shim column sources the A broadcast for each compute row. This must
# match the placement baked into the downloaded xclbin: the four A streams go
# to alternate columns so each gets its own shim MM2S path and never contends
# with a B fill.
A_SOURCE_COL = [2 * r for r in range(ROWS)]

# Core data memory holding the runtime parameters, and the lock a core waits
# on before it reads them. Both are baked into the overlay's core programs.
RTP_ADDRESS = 4096
RTP_LOCK_ID = 10

# Outstanding transfers per shim channel. The overlay's memtiles hold two
# objects per stream, so a third transfer would overwrite one still in use.
QUEUE_DEPTH = 2

MIN_M = M_TILE * ROWS
MIN_K = K_TILE
