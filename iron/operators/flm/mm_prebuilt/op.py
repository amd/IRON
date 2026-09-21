# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""FastFlowLM's shipped ``mm`` overlay, declared as a foreign overlay.

:class:`MMPrebuiltOverlay` has no ``design()``: it names the downloaded
xclbin, pins every stream to the shim column and channel the binary was
built with, and declares the parameter block the cores read. The library
emits the sequence against those pins (:mod:`iron.common.foreign`).
:class:`MMPrebuilt` is a shape on it, and exists so the shipped kernel can
be measured against :class:`iron.operators.flm.GEMM`, the IRON port, at the
same shapes and on the same inputs.
"""

from pathlib import Path
from typing import Any, Callable

import numpy as np

import aie.utils as aie_utils

from iron.common.declare import (
    In,
    Operator,
    Out,
    Overlay,
    Resident,
    Shim,
    StreamIn,
    StreamOut,
    Untunable,
    Xclbin,
    dim,
    operator,
    tunable,
)
from iron.common.tiling import Access
from iron.operators.flm.gemm.design import Epilogue, K_TILE, M_TILE, S, T
from iron.operators.flm.mm_prebuilt.design import (
    A_SOURCE_COL,
    COLS,
    MIN_K,
    MIN_M,
    N_TILE,
    QUEUE_DEPTH,
    ROWS,
    RTP_ADDRESS,
    RTP_LOCK_ID,
)
from iron.operators.flm.packing import pack_b

# The FastFlowLM revision the overlay is taken from. A commit SHA rather than
# a branch, so the digest below stays valid.
FASTFLOWLM_COMMIT = "f81eba7140decef5e4eda670d02a91b9d6402ee9"
XCLBIN_PATH = "src/xclbins/Gemma4-E4B-IT-NPU2/mm.xclbin"
XCLBIN_URL = (
    f"https://raw.githubusercontent.com/ROCm/FastFlowLM/{FASTFLOWLM_COMMIT}/"
    f"{XCLBIN_PATH}"
)
XCLBIN_SHA256 = "6f1e5507b84d4545536c9b8281002d0e0e10ed241f8593cb4db50eee63876e5f"
XCLBIN_KERNEL_NAME = "MLIR_AIE"

# The overlay's k slice. Its B layout is fixed by the shipped binary, so unlike
# flm.gemm this is not a tuning knob.
CT_K = K_TILE


@operator
class MMPrebuiltOverlay(Overlay):
    """The shipped 4x8 NPU2 ``mm`` binary: its pins and its parameter block."""

    image = Xclbin(
        url=XCLBIN_URL,
        sha256=XCLBIN_SHA256,
        filename=f"flm_mm_{FASTFLOWLM_COMMIT[:8]}.xclbin",
        kernel_name=XCLBIN_KERNEL_NAME,
    )

    # Fixed by the binary, not tuned: named so the streams can be per=.
    rows: int = tunable(ROWS, repr=False)
    cols: int = tunable(COLS, repr=False)

    # A: one (M_TILE x K_TILE) block per transfer element, broadcast along
    # each compute row from alternate shim columns on MM2S channel 0.
    a = StreamIn(
        M_TILE,
        K_TILE,
        per=rows,
        depth=QUEUE_DEPTH,
        via=[Shim(col, 0) for col in A_SOURCE_COL],
    )
    # B: one column's k-blocks, pre-packed, down each column on MM2S channel 1.
    b = StreamIn(
        K_TILE,
        N_TILE,
        per=cols,
        depth=QUEUE_DEPTH,
        via=[Shim(c, 1) for c in range(COLS)],
    )
    # C: the joined (ROWS*M_TILE x N_TILE) block, out of every column on
    # S2MM channel 0.
    c = StreamOut(
        ROWS * M_TILE,
        N_TILE,
        per=cols,
        depth=QUEUE_DEPTH,
        via=[Shim(c, 0) for c in range(COLS)],
    )
    # The eight parameter words every core reads once the lock is released:
    # k_iters, M, N, bias (unused), epilogue mode, clamp on, clamp min, max.
    rtp = Resident(np.int32, address=RTP_ADDRESS, lock=RTP_LOCK_ID)

    def tuning(self, dev) -> "MMPrebuiltOverlay":
        if dev is not None and (dev.resolve().name != "npu2" or dev.cols < 8):
            raise Untunable(
                "flm.MMPrebuilt runs a prebuilt NPU2 overlay and needs the 8 "
                f"columns of NPU2 (aie2p); got {dev.resolve().name!r} with "
                f"{dev.cols} columns"
            )
        return self


@operator
class MMPrebuilt(Operator[MMPrebuiltOverlay]):
    """bf16 GEMM running FastFlowLM's shipped ``mm`` overlay unmodified.

    NPU2 only: the overlay is built for the 8-column grid. B must be
    pre-packed; use :meth:`pack_B`.

    The epilogue here is selected through a runtime parameter, because one
    overlay serves every projection in a model. ``flm.GEMM`` compiles the
    selectable set in instead, which is what lets its inner loop be
    branch-free.
    """

    M: int = dim()
    K: int = dim()
    N: int = dim()
    epilogue: Epilogue = Epilogue.NONE
    clamp: tuple | None = None

    A = In(M, K, to=MMPrebuiltOverlay.a)
    # B, pre-packed by pack_B -- same element count, different order.
    B = In(K, N, to=MMPrebuiltOverlay.b)
    C = Out(M, N, from_=MMPrebuiltOverlay.c)


    @property
    def name(self) -> str:
        """Artifact stem. Prefixed for the same reason as flm.GEMM's."""
        return f"FLM_{super().name}"

    def validate(self) -> None:
        for name, value, unit in (
            ("M", self.M, MIN_M),
            ("K", self.K, MIN_K),
            ("N", self.N, N_TILE),
        ):
            if value % unit != 0:
                raise ValueError(f"{name} ({value}) must be a multiple of {unit}")
        self.epilogue = Epilogue(self.epilogue)
        if self.clamp is not None and self.clamp[0] > self.clamp[1]:
            raise ValueError(
                f"clamp min ({self.clamp[0]}) must be <= max ({self.clamp[1]})"
            )

    def residents(self) -> dict[str, Any]:
        clamp_min, clamp_max = self.clamp if self.clamp is not None else (0.0, 0.0)
        return {
            "rtp": [
                self.K // K_TILE,
                self.M,
                self.N,
                0,  # bias, which this operator does not expose
                Epilogue(self.epilogue).mode,
                1 if self.clamp is not None else 0,
                int(np.float32(clamp_min).view(np.int32)),
                int(np.float32(clamp_max).view(np.int32)),
            ]
        }

    def design(self, rt):
        ov = self.ov
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

        # One transfer per (column-block, row-block, leg), matching the order
        # the overlay's memtiles consume: column-block outermost, then
        # row-block, then column.
        for mega_col in range(n_full + (1 if rem_blocks else 0)):
            active = rem_blocks if (rem_blocks and mega_col == n_full) else COLS
            for mega_row in range(m_row_blocks):
                for c in range(COLS):
                    if c in A_SOURCE_COL:
                        r = A_SOURCE_COL.index(c)
                        rt.fill(
                            ov.a[r],
                            (
                                self.A,
                                Access(
                                    a_n,
                                    mega_row * ROWS * M_TILE * K + r * M_TILE * K,
                                    (1, k_iters, M_TILE, K_TILE),
                                    (0, K_TILE, K, 1),
                                ),
                            ),
                        )
                    if c >= active:
                        continue
                    # One contiguous run: pack_B has already put this
                    # column's k-blocks in the order the memtile writes them.
                    rt.fill(
                        ov.b[c],
                        (
                            self.B,
                            Access(
                                b_n,
                                (mega_col * COLS + c) * N_TILE * K,
                                (1, 1, 1, k_iters * K_TILE * N_TILE),
                                (0, 0, 0, 1),
                            ),
                        ),
                    )
                    rt.drain(
                        ov.c[c],
                        (
                            self.C,
                            Access(
                                c_n,
                                mega_col * COLS * N_TILE
                                + mega_row * ROWS * M_TILE * N
                                + c * N_TILE,
                                (1, 1, ROWS * M_TILE, N_TILE),
                                (0, 0, N, 1),
                            ),
                        ),
                    )

    # -- packaging: the downloaded image plus this shape's instructions --------

    def set_up_artifacts(self) -> None:
        from iron.common import RemoteFileArtifact

        # Only the download. The xclbin is fetched rather than built, which is
        # what this operator exists for.
        image = self.ov.foreign
        self.xclbin_artifact = RemoteFileArtifact(
            image.filename, url=image.url, sha256=image.sha256
        )
        self.add_artifacts([self.xclbin_artifact])

    def link_xclbin(self) -> None:
        """Compile this shape's instruction stream; the image is the downloaded one."""
        if getattr(self, "_insts_path", None) is not None:
            return
        from iron.common.jit_compile import compile_insts

        build_dir = Path(self.context.build_dir)
        self._insts_path = compile_insts(
            self.get_mlir_artifact().generator, build_dir / f"{self.name}.bin"
        )

    def get_callable(self) -> Callable[..., Any]:
        from aie.utils.npukernel import NPUKernel

        if not self.artifacts:
            self.set_up_artifacts()
        self.link_xclbin()
        npu_kernel = NPUKernel(
            xclbin_path=self.xclbin_artifact.filename,
            kernel_name=self.ov.foreign.kernel_name,
            insts_path=str(self._insts_path),
        )
        handle = aie_utils.DefaultNPURuntime.load(npu_kernel)

        def call(*args):
            return aie_utils.DefaultNPURuntime.run(handle, list(args))

        return call

    # -- host-side helpers -------------------------------------------------------

    def pack_B(self, B):
        """Reorder a row-major ``(K, N)`` weight matrix into the order the B
        transfers read. Returns a flat bf16 tensor.

        NOT the same layout ``flm.GEMM.pack_B`` produces: the overlay's own
        loop nest sweeps the two within-block k axes in the opposite order
        from ``mm_fused_mmul_2x2``'s, so this needs ``overlay_order``.
        """
        return pack_b(
            B, k_tile=K_TILE, n_tile=N_TILE, s=S, t=T, ct_k=CT_K, overlay_order=True
        )

    def reference(self, A, B):
        """CPU reference: ``C = epilogue(A @ B)``."""
        from iron.operators.flm.gemm.reference import reference

        return reference(A, B, self.epilogue, self.clamp)
