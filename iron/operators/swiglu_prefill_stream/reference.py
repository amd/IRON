# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reference SwiGLU-prefill block: ``(SiLU(x @ gate) * (x @ up)) @ down``.

Running this module produces the golden output; exporting it produces the
workload stream-dse generates the design from. Its parameter names are the ONNX
tensor names, hence the operator's runtime buffer names.

Numerical values come from :mod:`iron.operators.swiglu_decode.reference`, which
this operator shares; :func:`swiglu_module` loads them into the module.
"""

import torch
from torch import nn

# Reference weight -> this module's parameter (and so the runtime buffer name).
WEIGHTS = {"w_gate": "weights_1", "w_up": "weights_2", "w_down": "weights_3"}


class SwiGLU(nn.Module):
    """SwiGLU prefill block over a ``[seq_len, embedding_dim]`` activation."""

    def __init__(self, embedding_dim: int, hidden_dim: int, dtype=torch.bfloat16):
        super().__init__()
        gate_up = (embedding_dim, hidden_dim)
        self.weights_1 = nn.Parameter(torch.zeros(gate_up, dtype=dtype))  # gate
        self.weights_2 = nn.Parameter(torch.zeros(gate_up, dtype=dtype))  # up
        self.weights_3 = nn.Parameter(
            torch.zeros((hidden_dim, embedding_dim), dtype=dtype)
        )  # down

    def forward(self, input):
        gate = input @ self.weights_1
        up = input @ self.weights_2
        return (torch.nn.functional.silu(gate) * up) @ self.weights_3


def swiglu_module(embedding_dim, hidden_dim, golden_reference=None) -> SwiGLU:
    """A :class:`SwiGLU`, optionally holding ``golden_reference``'s weights.

    Weight *values* are irrelevant to the exported graph (only shapes and the
    topology are), so the operator builds its design from a zero-filled module.
    """
    module = SwiGLU(embedding_dim, hidden_dim).eval()
    if golden_reference is not None:
        with torch.no_grad():
            for reference, parameter in WEIGHTS.items():
                getattr(module, parameter).copy_(golden_reference[reference])
    return module
