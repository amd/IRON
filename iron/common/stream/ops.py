# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Each torch operator's ONNX form and the stream-dse kernel that runs it.

A fused kernel with no ONNX operator is declared with ``custom_op``, so the
exporter emits it as one node; ``kernels/<arch>.toml`` describes each kernel.
"""

# stream-dse, torch and onnxscript are requirements_stream.txt's.
# pyright: reportMissingImports=false

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
    """Return an operator in ``CUSTOM_DOMAIN``, which the exporter emits as one node."""
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
    """Return one online-softmax step over a key block, its exponentials unnormalised.

    The kernel owns the running max and sum, the causal mask and the
    division, so the graph sees an elementwise node whose key axis is free
    to be blocked.
    """
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
    # One node: the default lowering may add a Cast, which would shift the
    # positional renaming of the exported graph.
    return opset18.Softmax(x, axis=dim)


@dataclass(frozen=True)
class StreamOp:
    """How one torch operator is exported, and which kernel runs it.

    Attributes:
        onnx_type: The ONNX operator it is exported as.
        kernel: The stream-dse kernel that runs that node.
        translation: Its lowering, where the exporter's own is not what
            stream-dse parses; None keeps the exporter's.
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
    """Return the ``custom_translation_table`` for ``torch.onnx.export``."""
    return {
        target: op.translation
        for target, op in TORCH_OPS.items()
        if op.translation is not None
    }


def op_for_onnx_type(onnx_type: str) -> StreamOp:
    """Return the ``StreamOp`` an exported node's operator type belongs to.

    Raises:
        NotImplementedError: No torch operator is exported as ``onnx_type``.
    """
    try:
        return _BY_ONNX_TYPE[onnx_type]
    except KeyError:
        raise NotImplementedError(
            f"ONNX operator '{onnx_type}' has no stream-dse mapping; "
            f"add it to iron.common.stream.ops.TORCH_OPS"
        ) from None
