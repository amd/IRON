# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Registry binding torch operators to their ONNX form and their stream-dse kernel.
Fused kernels with no ONNX operator are declared with :func:`custom_op`, so the exporter
emits them as one node; ``kernels/<dir>.toml`` describes each kernel."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import torch
from onnx import defs
from onnxscript import opset18
from onnxscript.values import Op, Opset

from iron.common.stream.kernel_library import fixed_dims, library

CUSTOM_DOMAIN = Opset("com.example", 1)

_ELEMENT_TYPES = ["tensor(bfloat16)", "tensor(float)"]


def custom_op(name: str) -> Op:
    """An operator in :data:`CUSTOM_DOMAIN`, emitted by the exporter as one node."""
    schema = defs.OpSchema(
        name,
        CUSTOM_DOMAIN.domain,
        CUSTOM_DOMAIN.version,
        inputs=[defs.OpSchema.FormalParameter("X0", "T")],
        outputs=[defs.OpSchema.FormalParameter("Y", "T")],
        type_constraints=[("T", _ELEMENT_TYPES, "")],
    )
    return Op(CUSTOM_DOMAIN, name, schema)


_INTRINSICS = {"aie2p": "aie2pintrin.h"}


def _mha_artifacts(name, kernels_dir, kernel_dir, m: int):
    """``mha.cc`` with zero.cc, linked by both cores of an online-softmax step, plus the
    copy that snapshots the running scale. Specialized and named on the query block ``m``,
    which matmul_PV's accumulation is compiled for; the key block and head are fixed."""
    from iron.common.compilation import KernelObjectArtifact, SourceArtifact

    fixed = fixed_dims("matmul_PV", kernel_dir)
    zero_source = kernels_dir / "zero" / "zero.cc"
    return [
        KernelObjectArtifact(
            "mha_passThrough.o",
            dependencies=[SourceArtifact(kernels_dir / "eltwise" / "passThrough.cc")],
            extra_flags=["-DBIT_WIDTH=16"],
        ),
        KernelObjectArtifact(
            name,
            dependencies=[
                SourceArtifact(kernels_dir / "linalg" / "mha.cc"),
                SourceArtifact(zero_source),
            ],
            extra_flags=[
                "-Dbf16_bf16_ONLY",
                f"-DDIM_M={m}",
                f"-DDIM_K={fixed['k']}",
                f"-DDIM_N={fixed['n']}",
                "-DROUND_CONV_EVEN",
                "-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16",
                "-DB_COL_MAJ",
                "-DZERO_TYPE=bfloat16",
                f"-DTILE_SIZE={m * fixed['n']}",
                f"-include{_INTRINSICS[kernel_dir]}",
                f"-include{zero_source}",
            ],
            rename_symbols={"zero": "zero_bf16"},
        ),
    ]


def _gemm_artifacts(name, kernels_dir, kernel_dir, m: int, k: int, n: int):
    """``mm.cc`` for one tile shape, with zero.cc compiled into the same object since a
    core links one object. Symbols are renamed to stream-dse's dimension-suffixed ones, so
    GEMMs of different tile shapes coexist in one design."""
    from iron.common.compilation import KernelObjectArtifact, SourceArtifact

    suffix = f"{m}_{k}_{n}"
    zero_source = kernels_dir / "zero" / "zero.cc"
    return [
        KernelObjectArtifact(
            name,
            dependencies=[
                SourceArtifact(kernels_dir / "linalg" / "mm.cc"),
                SourceArtifact(zero_source),
            ],
            extra_flags=[
                f"-DDIM_M={m}",
                f"-DDIM_K={k}",
                f"-DDIM_N={n}",
                "-Dbf16_bf16_ONLY",
                # Emulating the matmul on the bfp16 MACs is what makes the 8-row
                # MAC tile available, so it and the layouts move together.
                "-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16",
                "-DROUND_CONV_EVEN",
                # zero.cc's entry point, over the m x n output tile.
                "-DZERO_TYPE=bfloat16",
                f"-DTILE_SIZE={m * n}",
                # The driver adds the intrinsics header after any -include; zero.cc needs it first.
                f"-include{_INTRINSICS[kernel_dir]}",
                f"-include{zero_source}",
            ],
            rename_symbols={
                "matmul_bf16_bf16": f"matmul_bf16_bf16_{suffix}",
                "zero": f"zero_bf16_{suffix}",
            },
        )
    ]


def _sized(factory):
    """An elementwise object compiled for the elements one call takes, as its mlir-aie
    factory compiles it: with the count known at compile time the loop pipelines, where
    a count only known at run time leaves the call twice as long."""

    def build(name, kernels_dir, kernel_dir, m: int, n: int):
        from iron.common.compilation import KernelObjectArtifact, SourceArtifact

        fn = factory(m * n)
        return [
            KernelObjectArtifact(
                name,
                dependencies=[SourceArtifact(Path(fn.source_file))],
                extra_flags=[*fn.compile_flags, *(f"-I{d}" for d in fn.include_dirs)],
            )
        ]

    return build


def _silu(elements):
    from aie.iron.kernels import activation

    return activation.silu_sized(elements)


def _mul(elements):
    from aie.iron.kernels import eltwise

    return eltwise.mul_sized(elements)


_BUILDERS = {
    "mm.cc": _gemm_artifacts,
    "mha.cc": _mha_artifacts,
    "silu.cc": _sized(_silu),
    "mul.cc": _sized(_mul),
}


def linked_objects(mlir_text: str) -> list[str]:
    """The kernel objects a generated design links, in first-seen order."""
    return list(dict.fromkeys(re.findall(r'link_with\s*=\s*"([^"]+)"', mlir_text)))


def _object_shape(template: str, name: str) -> dict[str, int] | None:
    pattern = re.sub(r"\\\{(\w+)\\\}", r"(?P<\1>\\d+)", re.escape(template))
    match = re.fullmatch(pattern, name)
    return {k: int(v) for k, v in match.groupdict().items()} if match else None


def artifacts_for_object(name: str, kernels_dir, kernel_dir) -> list:
    """The compilation artifacts building one linked object, found by the kernel library's object names."""
    from iron.common.compilation import KernelObjectArtifact, SourceArtifact

    for spec in library(kernel_dir).kernels.values():
        if spec.object is None or (shape := _object_shape(spec.object, name)) is None:
            continue
        if build := _BUILDERS.get(Path(spec.source).name):
            return build(name, kernels_dir, kernel_dir, **shape)
        source = SourceArtifact(kernels_dir / spec.source)
        return [KernelObjectArtifact(name, dependencies=[source])]
    raise ValueError(f"no rule builds the kernel object {name!r}")


Silu = custom_op("Silu")
PartialSoftmax = custom_op("PartialSoftmax")


@torch.library.custom_op("iron_stream::partial_softmax", mutates_args=())
def partial_softmax(x: torch.Tensor) -> torch.Tensor:
    """One online-softmax step over a key block: exponentials, left unnormalised. The
    kernel owns the running max and sum, the causal mask and the division, so the graph
    sees an elementwise node whose key axis is free to be blocked."""
    return torch.exp(x - x.amax(dim=-1, keepdim=True))


@partial_softmax.register_fake
def _(x: torch.Tensor) -> torch.Tensor:
    return torch.empty_like(x)


def _to_silu(x):
    return Silu(x)


def _to_partial_softmax(x):
    return PartialSoftmax(x)


def _to_mul(a, b):
    return opset18.Mul(a, b)


def _to_softmax(x, dim):
    """Pinned to a single node: the torchlib lowering can add a ``Cast``, and any
    extra node shifts the positional renaming of the exported graph. A ``dtype``
    argument has nowhere to go here and is rejected rather than dropped."""
    return opset18.Softmax(x, axis=dim)


@dataclass(frozen=True)
class StreamOp:
    """How one torch operator is exported, and which kernel runs it.

    ``translation`` overrides how the exporter lowers the operator, and is needed
    only when its default lowering is not what stream-dse parses. Leaving it unset
    keeps the exporter's own lowering and just binds the resulting ONNX operator to
    a kernel.
    """

    onnx_type: str
    kernel: str
    translation: Callable | None = None


# torch operator -> its ONNX form and AIE kernel. A matmul keeps the exporter's MatMul,
# whose leading axes are batch axes, such as attention's heads.
TORCH_OPS: dict[Callable, StreamOp] = {
    torch.ops.aten.matmul.default: StreamOp("MatMul", "gemm"),
    torch.ops.aten.silu.default: StreamOp("Silu", "silu", _to_silu),
    torch.ops.aten.mul.Tensor: StreamOp("Mul", "eltwise_mul", _to_mul),
    torch.ops.aten.softmax.int: StreamOp("Softmax", "softmax", _to_softmax),
    torch.ops.iron_stream.partial_softmax.default: StreamOp(
        "PartialSoftmax", "partial_softmax", _to_partial_softmax
    ),
}

_BY_ONNX_TYPE = {op.onnx_type: op for op in TORCH_OPS.values()}


def translation_table() -> dict[Callable, Callable]:
    """The ``custom_translation_table`` for :func:`torch.onnx.export`."""
    return {
        target: op.translation
        for target, op in TORCH_OPS.items()
        if op.translation is not None
    }


def op_for_onnx_type(onnx_type: str) -> StreamOp:
    """The :class:`StreamOp` an exported node's operator type belongs to."""
    try:
        return _BY_ONNX_TYPE[onnx_type]
    except KeyError:
        raise NotImplementedError(
            f"ONNX operator '{onnx_type}' has no stream-dse mapping; "
            f"add it to iron.common.stream.ops.TORCH_OPS"
        ) from None
