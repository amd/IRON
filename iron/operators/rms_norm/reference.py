# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def reference(x, w=None, weighted=False, eps=1e-5):
    """CPU reference: row-wise RMS normalization, optionally weighted (ground truth).

    Matches the AIE kernel: normalize by 1/sqrt(mean(x^2) + eps).
    """
    rms = torch.sqrt(torch.mean(x**2, dim=-1, keepdim=True) + eps)
    out = x / rms
    if weighted:
        out = out * w
    return out


def generate_inputs(rows: int, cols: int, seed=42, weighted=False):
    """The input, and with ``weighted`` the weights too."""
    torch.manual_seed(seed)
    val_range = 4
    x = torch.rand(rows, cols, dtype=torch.bfloat16) * val_range
    if not weighted:
        return (x,)
    return x, torch.rand(cols, dtype=torch.bfloat16) * val_range
