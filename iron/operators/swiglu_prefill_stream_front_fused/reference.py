# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reference SwiGLU-prefill block: ``(SiLU(x @ gate) * (x @ up)) @ down``.

Running this module produces the golden output; exporting it produces the
workload stream-dse generates the design from.

The names below are the block's vocabulary, and they are the ones
:mod:`iron.operators.swiglu_decode.reference` -- the golden reference this
operator shares -- gives the same tensors. Everything downstream is named from
here: the ONNX tensors, the mapping's layers and runtime arguments, the runtime
buffers, and the tensor handed between fusion groups.
"""
from onnx import defs
from onnxscript.values import Op, Opset
import torch
from torch import nn

NAME_INPUT = "input"
NAME_FUSED = "fused"
NAME_OUTPUT = "output"

NAME_WEIGHTS = ("w_fused", "w_down")

# Every name this module exports, for the correspondence check in iron/tests/stream.
TENSOR_NAMES = (
    NAME_INPUT,
    NAME_OUTPUT,
    NAME_FUSED,
    *NAME_WEIGHTS,
)


class SwiGLUFrontFused(nn.Module):
    """SwiGLU prefill block over a ``[seq_len, embedding_dim]`` activation."""

    def __init__(self, embedding_dim: int, hidden_dim: int, dtype=torch.bfloat16):
        super().__init__()
        self.w_front = nn.Parameter(torch.zeros((embedding_dim, 2, hidden_dim), dtype=dtype))
        self.w_down = nn.Parameter(torch.zeros((hidden_dim, embedding_dim), dtype=dtype))

    def forward(self, input):
        front = torch_swiglu_front_fused(input, self.w_front)
        return front @ self.w_down


def swiglu_module(embedding_dim, hidden_dim, golden_reference=None) -> SwiGLUFrontFused:
    """A :class:`SwiGLU`, optionally holding ``golden_reference``'s weights.

    Weight *values* are irrelevant to the exported graph (only shapes and the
    topology are), so the operator builds its design from a zero-filled module.
    """
    module = SwiGLUFrontFused(embedding_dim, hidden_dim).eval()
    if golden_reference is not None:
        with torch.no_grad():
            for name in NAME_WEIGHTS:
                getattr(module, name).copy_(golden_reference[name])
    return module


# custom pytorch operator
@torch.library.custom_op("custom::swiglu_fused_front", mutates_args=())
def torch_swiglu_front_fused(x: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
    m, xk = x.shape
    wk, t, n = w.shape
    assert xk == wk and t == 2

    gate = x @ w[:, 0, :]
    up = x @ w[:, 1, :]
    return torch.nn.functional.silu(gate) * up


@torch_swiglu_front_fused.register_fake
def _(x: torch.Tensor, w: torch.Tensor):
    m, xk = x.shape
    wk, t, n = w.shape
    assert xk == wk and t == 2

    return torch.empty((m, n), dtype=x.dtype, device=x.device)


# custom onnx operator
onnx_custom_domain = Opset(domain="custom", version=1)
onnx_swiglu_front_fused = Op(
    onnx_custom_domain,
    "SwigluFrontFused",
    defs.OpSchema(
        "SwigluFrontFused",
        onnx_custom_domain.domain,
        onnx_custom_domain.version,
        inputs=[
            defs.OpSchema.FormalParameter("X", "T"),
            defs.OpSchema.FormalParameter("W", "T"),
        ],
        outputs=[defs.OpSchema.FormalParameter("Y", "T")],
        type_constraints=[("T", ["tensor(bfloat16)"], "")],
    ),
)

TRANSLATION_TABLE = {
    torch.ops.custom.swiglu_fused_front.default: onnx_swiglu_front_fused,
}


def main():
    onnx_program = torch.onnx.export(
        SwiGLUFrontFused(256, 512).eval(),
        (torch.randn(4, 256, dtype=torch.bfloat16),),
        dynamo=True,
        custom_translation_table=TRANSLATION_TABLE,
    )

    onnx_program.save("model.onnx")


if __name__ == '__main__':
    main()
