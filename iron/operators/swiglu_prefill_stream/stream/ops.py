# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Registry binding ONNX operators to their AIE kernel.

A new op is one ``StreamKernel`` plus one ``STREAM_OPS`` entry; ops ONNX
has no operator for live in ``CUSTOM_DOMAIN``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

from aie.iron import ExternalFunction

from iron.operators.swiglu_prefill_stream.layout import TiledStridedLayout, tiled_2d

# mm.cc's MAC tile rows: 8 on the bfp16 MACs, 4 otherwise.
R, S, T = 4, 8, 8
MAC_ROWS_BFP16 = 8

# Element tile the stream-dse elementwise kernels are written against.
ELEMENTWISE_TILE = (32, 64)

# Private domain for ops that exist as an AIE kernel but not as an ONNX operator.
CUSTOM_DOMAIN = "com.example"


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


def _gemm_declare(kernels_dir, m: int, k: int, n: int):
    """Compile ``mm.cc`` for one tile shape, and say what its symbols became.

    stream-dse suffixes the symbols with the tile shape, and ExternalFunction
    can only prefix, so the generated MLIR is rewritten through the returned
    map. One object holds mm.cc and zero.cc: a core links one object.
    """
    suffix = f"{m}_{k}_{n}"
    prefix = f"mm{suffix}"
    ExternalFunction(
        # Only compiles the object: stream-dse emits the func.func, so no digest prefix.
        "matmul_bf16_bf16",
        source_string="".join(
            f'#include "{kernels_dir / source}"\n'
            for source in ("linalg/mm.cc", "zero/zero.cc")
        ),
        arg_types=[],
        object_file_name=f"mm_{suffix}.o",
        symbol_prefix=prefix,
        compile_flags=[
            f"-DDIM_M={m}",
            f"-DDIM_K={k}",
            f"-DDIM_N={n}",
            "-Dbf16_bf16_ONLY",
            # The bfp16 MACs give the 8-row tile: it and the layouts move together.
            "-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16",
            "-DROUND_CONV_EVEN",
            # zero.cc's entry point, over the m x n output tile.
            "-DZERO_TYPE=bfloat16",
            f"-DTILE_SIZE={m * n}",
        ],
    )
    return {
        f"matmul_bf16_bf16_{suffix}": f"{prefix}_matmul_bf16_bf16",
        f"zero_bf16_{suffix}": f"{prefix}_zero",
    }


@dataclass(frozen=True)
class StreamKernel:
    """An AIE kernel: its stream-dse identity, its source, and its operand
    layouts. The object name is the kernel's ``linkwith_name`` in stream-dse.
    """

    key: str  # stream-dse AIEKernels key
    layouts: Callable[..., tuple[TiledStridedLayout, ...]]
    source: str | None = None
    subdir: str | None = None
    declare: Callable | None = None  # overrides source/subdir when tile-specialized

    def declare_kernels(self, kernels_dir, **kwargs) -> dict:
        """Compile this kernel, and return any symbol renames it forces.

        Called inside the design: CompilableDesign clears ExternalFunctions built
        before it starts generating.
        """
        if self.declare is not None:
            return self.declare(kernels_dir, **kwargs)
        assert self.source is not None and self.subdir is not None, self.key
        # No prefix: the generated MLIR calls these by the source's names.
        ExternalFunction(
            self.source,
            source_file=str(kernels_dir / self.subdir / f"{self.source}.cc"),
            arg_types=[],
            object_file_name=f"{self.source}.o",
        )
        return {}


GEMM = StreamKernel(key="gemm", layouts=gemm_layouts, declare=_gemm_declare)
SILU = StreamKernel(
    key="silu",
    layouts=lambda: elementwise_layouts(2),
    source="silu",
    subdir="activation",
)
ELTWISE_MUL = StreamKernel(
    key="eltwise_mul",
    layouts=lambda: elementwise_layouts(3),
    source="mul",
    subdir="eltwise",
)


@dataclass(frozen=True)
class StreamOp:
    """One ONNX operator, and which kernel runs it."""

    onnx_type: str
    kernel: StreamKernel
    domain: str = ""
    attributes: dict = field(default_factory=dict)


# Gemm, not MatMul: its parser iterates (m, k, n), the mappings' D0/D1/D2.
STREAM_OPS = {
    op.onnx_type: op
    for op in (
        StreamOp(
            "Gemm", GEMM, attributes=dict(alpha=1.0, beta=1.0, transA=0, transB=0)
        ),
        StreamOp("Silu", SILU, CUSTOM_DOMAIN),
        StreamOp("Mul", ELTWISE_MUL),
    )
}


def op_for_onnx_type(onnx_type: str) -> StreamOp:
    """The ``StreamOp`` a workload node's operator type belongs to."""
    try:
        return STREAM_OPS[onnx_type]
    except KeyError:
        raise NotImplementedError(
            f"ONNX operator '{onnx_type}' has no stream-dse mapping; "
            f"add it to iron.operators.swiglu_prefill_stream.stream.ops.STREAM_OPS"
        ) from None
