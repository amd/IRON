# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def reference(x, w=None, weighted=False, eps=1e-5):
    """CPU reference: row-wise RMS normalization, optionally weighted (ground truth).

    Matches the AIE kernel: normalize by 1/sqrt(mean(x^2) + eps).
    """
    rms = torch.sqrt(torch.mean(x**2, dim=-1, keepdim=True) + eps)
    out = x / rms
    if weighted:
        out = out * w
    return out


def generate_golden_reference(
    rows: int, cols: int, dtype="bf16", seed=42, weighted=False, eps=1e-5
):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    if weighted:
        weights = torch.rand(cols, dtype=torch_dtype_map[dtype]) * val_range
        output_tensor = reference(input_tensor, weights, weighted=True, eps=eps)
        return {"input": input_tensor, "weight": weights, "output": output_tensor}
    else:
        output_tensor = reference(input_tensor, eps=eps)
        return {"input": input_tensor, "output": output_tensor}
