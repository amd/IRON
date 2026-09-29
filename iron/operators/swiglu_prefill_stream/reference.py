# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reference SwiGLU-prefill block: ``(SiLU(x @ gate) * (x @ up)) @ down``.

Running this module produces the golden output; exporting it produces the
workload stream-dse generates the design from.

The names below are the block's vocabulary, and they are the keys
``generate_golden_reference`` gives the same tensors. Everything
downstream is named from here: the ONNX tensors, the mapping's layers and runtime arguments, the runtime
buffers, and the tensor handed between fusion groups.
"""

import torch
from torch import nn

INPUT = "input"
OUTPUT = "output"
GATE_PROJECTION = "left"
UP_PROJECTION = "right"
ACTIVATION = "left_swished"
HIDDEN = "intermediate"

WEIGHTS = ("w_gate", "w_up", "w_down")

# Every name this module exports, for the correspondence check in iron/tests/stream.
TENSOR_NAMES = (
    INPUT,
    OUTPUT,
    GATE_PROJECTION,
    UP_PROJECTION,
    ACTIVATION,
    HIDDEN,
    *WEIGHTS,
)


class SwiGLU(nn.Module):
    """SwiGLU prefill block over a ``[seq_len, embedding_dim]`` activation."""

    def __init__(self, embedding_dim: int, hidden_dim: int, dtype=torch.bfloat16):
        super().__init__()
        gate_up = (embedding_dim, hidden_dim)
        self.w_gate = nn.Parameter(torch.zeros(gate_up, dtype=dtype))
        self.w_up = nn.Parameter(torch.zeros(gate_up, dtype=dtype))
        self.w_down = nn.Parameter(
            torch.zeros((hidden_dim, embedding_dim), dtype=dtype)
        )

    def forward(self, input):
        gate = input @ self.w_gate
        up = input @ self.w_up
        return (torch.nn.functional.silu(gate) * up) @ self.w_down


def generate_golden_reference(M=1, K=2048, N=8192, seed=42):
    """Golden data for the block: random inputs and every tensor between them.

    SwiGLU computes: W3 @ (SiLU(W1 @ x) * (W2 @ x))
    where SiLU(x) = x * sigmoid(x)

    Parameters:
        M: Sequence length
        K: Embedding dimension
        N: Hidden dimension (FFN intermediate dimension)
        seed: Random seed

    Returns:
        dict: Contains 'input', 'w_gate', 'w_up', 'w_down', 'left', 'left_swished', 'right', 'intermediate', 'output'
    """
    torch.manual_seed(seed)

    # Generate golden inputs
    val_range = 4
    x = torch.randn(M, K, dtype=torch.bfloat16) * val_range
    w_gate = torch.randn(N, K, dtype=torch.bfloat16).T * val_range  # gate projection
    # bias1 and bias2 are generated but not used; they are retained to preserve
    # the random number sequence from the original reference implementation so
    # that the test weights do not hit the SiLU kernel's tanh saturation region.
    _bias1 = (
        torch.randn(K, dtype=torch.bfloat16) * val_range
    )  # unused; preserves RNG state
    w_up = torch.randn(N, K, dtype=torch.bfloat16).T * val_range  # up projection
    _bias2 = (
        torch.randn(K, dtype=torch.bfloat16) * val_range
    )  # unused; preserves RNG state
    w_down = torch.randn(N, K, dtype=torch.bfloat16) * val_range  # down projection

    # Generate golden outputs
    left = x @ w_gate
    left_swished = torch.nn.functional.silu(left)
    right = x @ w_up
    intermediate = left_swished * right
    y = intermediate @ w_down

    return {
        "input": x,
        "w_gate": w_gate,
        "w_up": w_up,
        "w_down": w_down,
        "left": left,
        "left_swished": left_swished,
        "right": right,
        "intermediate": intermediate,
        "output": y,
    }


def swiglu_module(embedding_dim, hidden_dim, golden_reference=None) -> SwiGLU:
    """A ``SwiGLU``, optionally holding ``golden_reference``'s weights.

    Weight *values* are irrelevant to the exported graph (only shapes and the
    topology are), so the operator builds its design from a zero-filled module.
    """
    module = SwiGLU(embedding_dim, hidden_dim).eval()
    if golden_reference is not None:
        with torch.no_grad():
            for name in WEIGHTS:
                getattr(module, name).copy_(golden_reference[name])
    return module
