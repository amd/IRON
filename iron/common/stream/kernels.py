# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The AIE kernels stream-dse designs run, and the operand layouts they take.

Split out of :mod:`~iron.common.stream.ops` because an operator names its kernels
at import time while the ONNX registry is only needed when a design is built. The
registry pulls in ``onnx``/``onnxscript``, which a core install does not have, so
nothing importable from ``iron.operators`` may reach it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from iron.common.layout import TiledStridedLayout, tiled_2d

# Intrinsic MAC tile dimensions of the aie2p kernels stream-dse targets. The
# operand layouts are the contract the generated DMAs and the compiled kernel
# objects agree on.
# mm.cc takes an 8-row MAC tile when bf16 matmuls run on the bfp16 MACs and a
# 4-row one when they do not.
R, S, T = 4, 8, 8
MAC_ROWS_BFP16 = 8

# Element tile the stream-dse elementwise kernels are written against.
ELEMENTWISE_TILE = (32, 64)


def mac_rows(bfp16_mmul: bool) -> int:
    """Rows of the MAC tile a kernel object compiled this way takes."""
    return MAC_ROWS_BFP16 if bfp16_mmul else R


def gemm_layouts(
    m: int, k: int, n: int, bfp16_mmul: bool = False
) -> tuple[TiledStridedLayout, ...]:
    """Layouts of a GEMM's ``A[m,k]``, ``B[k,n]`` and ``C[m,n]`` operands."""
    rows = mac_rows(bfp16_mmul)
    return (tiled_2d(m, k, rows, S), tiled_2d(k, n, S, T), tiled_2d(m, n, rows, T))


def elementwise_layouts(
    nb_operands: int, bfp16_mmul: bool = False
) -> tuple[TiledStridedLayout, ...]:
    """Identical tiled layout for each operand of an elementwise kernel."""
    return (tiled_2d(*ELEMENTWISE_TILE, mac_rows(bfp16_mmul), T),) * nb_operands


def _gemm_artifacts(kernels_dir, kernel_dir, m: int, k: int, n: int):
    """The ``mm.cc`` object specialized for one tile shape.

    stream-dse emits dimension-suffixed symbols so GEMMs of different tile shapes
    coexist in one design (``GemmKernel.function_name``/``zero_name``); rename
    ``mm.cc``'s unsuffixed symbols to match.
    """
    from iron.common.compilation import KernelObjectArtifact, SourceArtifact

    suffix = f"{m}_{k}_{n}"
    return [
        KernelObjectArtifact(
            f"mm_{suffix}.o",
            dependencies=[SourceArtifact(kernels_dir / kernel_dir / "mm.cc")],
            extra_flags=[
                f"-DDIM_M={m}",
                f"-DDIM_K={k}",
                f"-DDIM_N={n}",
                "-Dbf16_bf16_ONLY",
                # Emulating the matmul on the bfp16 MACs is what makes the 8-row
                # MAC tile available, so it and the layouts move together.
                "-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16",
                "-DROUND_CONV_EVEN",
            ],
            rename_symbols={
                "matmul_bf16_bf16": f"matmul_bf16_bf16_{suffix}",
                "zero_bf16": f"zero_bf16_{suffix}",
            },
        )
    ]


@dataclass(frozen=True)
class StreamKernel:
    """An AIE kernel: its stream-dse identity, its source, and its operand layouts.

    ``source``/``subdir`` name the file in IRON's ``aie_kernels`` library the same
    way the hand-written operators do (``subdir=None`` means the device directory,
    e.g. ``aie2p``). The object name must equal the kernel's ``linkwith_name`` in
    stream-dse, since the generated MLIR links against it.
    """

    key: str  # stream-dse AIEKernels key
    layouts: Callable[..., tuple[TiledStridedLayout, ...]]
    source: str | None = None
    subdir: str | None = None
    artifacts: Callable | None = None  # overrides source/subdir when tile-specialized

    def kernel_artifacts(self, kernels_dir, kernel_dir, **kwargs):
        """Compilation artifacts building this kernel's object file."""
        if self.artifacts is not None:
            return self.artifacts(kernels_dir, kernel_dir, **kwargs)
        from iron.common.compilation import KernelObjectArtifact, SourceArtifact

        subdir = self.subdir or kernel_dir
        return [
            KernelObjectArtifact(
                f"{self.source}.o",
                dependencies=[
                    SourceArtifact(kernels_dir / subdir / f"{self.source}.cc")
                ],
            )
        ]


GEMM = StreamKernel(key="gemm", layouts=gemm_layouts, artifacts=_gemm_artifacts)
SILU = StreamKernel(key="silu", layouts=lambda: elementwise_layouts(2), source="silu")
ELTWISE_MUL = StreamKernel(
    key="eltwise_mul",
    layouts=lambda: elementwise_layouts(3),
    source="mul",
)
