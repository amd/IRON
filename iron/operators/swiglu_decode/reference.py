# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def generate_golden_reference(M=1, K=2048, N=8192, seed=42):
    """
    Generate golden reference data for SwiGLU decode (for single token).

    SwiGLU computes: W3 @ (SiLU(W1 @ x) * (W2 @ x))
    where SiLU(x) = x * sigmoid(x)

    Parameters:
        M: Batch size (typically 1 for decode)
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
