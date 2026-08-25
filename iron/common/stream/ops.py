# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Registry binding torch operators to their ONNX form and their AIE kernel.

One :class:`StreamOp` entry per supported torch operator is all a stream-dse-backed
operator needs: how the op is emitted by the ONNX exporter, which stream-dse kernel
implements it, which ``aie_kernels`` source that kernel is compiled from, and what
operand layouts the generated DMAs must use.

Ops stream-dse implements with a fused kernel but ONNX has no operator for are
declared with :func:`custom_op`, which gives them a schema in a private domain so
the exporter emits them as a single node.

Supporting a new op is one :class:`~iron.common.stream.kernels.StreamKernel` plus one
:data:`TORCH_OPS` entry -- the kernel source is IRON's existing
``aie_kernels/<dir>/<name>.cc``, exactly as the hand-written operators use it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import torch
from onnx import defs
from onnxscript import opset18
from onnxscript.values import Op, Opset

from iron.common.stream.kernels import ELTWISE_MUL, GEMM, SILU, StreamKernel

# Private domain for ops that exist as an AIE kernel but not as an ONNX operator.
CUSTOM_DOMAIN = Opset("com.example", 1)

_ELEMENT_TYPES = ["tensor(bfloat16)", "tensor(float)"]


def custom_op(name: str, arity: int = 1) -> Op:
    """An operator in :data:`CUSTOM_DOMAIN`, emitted by the exporter as one node."""
    schema = defs.OpSchema(
        name,
        CUSTOM_DOMAIN.domain,
        CUSTOM_DOMAIN.version,
        inputs=[defs.OpSchema.FormalParameter(f"X{i}", "T") for i in range(arity)],
        outputs=[defs.OpSchema.FormalParameter("Y", "T")],
        type_constraints=[("T", _ELEMENT_TYPES, "")],
    )
    return Op(CUSTOM_DOMAIN, name, schema)


Silu = custom_op("Silu")


def _to_gemm(a, b):
    return opset18.Gemm(a, b)


def _to_silu(x):
    return Silu(x)


def _to_mul(a, b):
    return opset18.Mul(a, b)


@dataclass(frozen=True)
class StreamOp:
    """How one torch operator is exported, and which kernel runs it.

    ``translation`` overrides how the exporter lowers the operator, and is needed
    only when its default lowering is not what stream-dse parses. Leaving it unset
    keeps the exporter's own lowering and just binds the resulting ONNX operator to
    a kernel.
    """

    onnx_type: str
    kernel: StreamKernel
    translation: Callable | None = None


# torch operator -> its ONNX form and AIE kernel. Gemm rather than the exporter's
# default MatMul because stream-dse's Gemm parser iterates (m, k, n), which is the
# order the mappings address as D0/D1/D2.
TORCH_OPS: dict[Callable, StreamOp] = {
    torch.ops.aten.matmul.default: StreamOp("Gemm", GEMM, _to_gemm),
    torch.ops.aten.silu.default: StreamOp("Silu", SILU, _to_silu),
    torch.ops.aten.mul.Tensor: StreamOp("Mul", ELTWISE_MUL, _to_mul),
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
