# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def generate_golden_reference(M=2048, K=2048, seed=42):
    """Generate golden reference for dual-GEMV + SiLU + Mul.

    Computes: output = silu(W1 @ x) * (W2 @ x)

    Returns dict with W1, W2, x, and output tensors.
    """
    torch.manual_seed(seed)
    val_range = 4
    W1 = torch.randn(M, K, dtype=torch.bfloat16) * val_range
    W2 = torch.randn(M, K, dtype=torch.bfloat16) * val_range
    x = torch.randn(K, dtype=torch.bfloat16) * val_range

    left = W1 @ x
    right = W2 @ x
    output = torch.nn.functional.silu(left) * right

    return {"W1": W1, "W2": W2, "x": x, "output": output}
