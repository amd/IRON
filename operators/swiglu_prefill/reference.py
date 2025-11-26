# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def generate_golden_reference(M=2048, K=2048, N=8192, seed=42):
    """
    Generate golden reference data for SwiGLU prefill (for multiple tokens).

    SwiGLU computes: (SiLU(x @ W1.T) * (x @ W2.T)) @ W3.T
    where SiLU(x) = x * sigmoid(x)

    Parameters:
        M: Sequence length (number of tokens)
        K: Embedding dimension
        N: Hidden dimension (FFN intermediate dimension)
        seed: Random seed

    Returns:
        dict: Contains 'x', 'w_gate', 'w_up', 'w_down', 'left', 'left_swished', 'right', 'intermediate', 'y'
    """
    torch.manual_seed(seed)

    # Generate golden inputs
    val_range = 4
    x = torch.randn(M, K, dtype=torch.bfloat16) * val_range
    w_gate = torch.randn(N, K, dtype=torch.bfloat16) * val_range  # gate projection
    w_up = torch.randn(N, K, dtype=torch.bfloat16) * val_range    # up projection
    w_down = torch.randn(K, N, dtype=torch.bfloat16) * val_range  # down projection

    # Generate golden outputs (prefill uses matrix-matrix multiply)
    left = x @ w_gate.T
    left_swished = torch.nn.functional.silu(left)
    right = x @ w_up.T
    intermediate = left_swished * right
    y = intermediate @ w_down.T

    return {
        "x": x.numpy().view(np.uint16).view(bfloat16),
        "w_gate": w_gate.numpy().view(np.uint16).view(bfloat16),
        "w_up": w_up.numpy().view(np.uint16).view(bfloat16),
        "w_down": w_down.numpy().view(np.uint16).view(bfloat16),
        "left": left.numpy().view(np.uint16).view(bfloat16),
        "left_swished": left_swished.numpy().view(np.uint16).view(bfloat16),
        "right": right.numpy().view(np.uint16).view(bfloat16),
        "intermediate": intermediate.numpy().view(np.uint16).view(bfloat16),
        "y": y.numpy().view(np.uint16).view(bfloat16),
    }
