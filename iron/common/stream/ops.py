# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Registry binding torch operators to their ONNX form and their stream-dse kernel.
Fused kernels with no ONNX operator are declared with :func:`custom_op`, so the exporter
emits them as one node; ``kernels/<dir>.toml`` describes each kernel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import torch
from onnx import defs
from onnxscript import opset18
from onnxscript.values import Op, Opset

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
