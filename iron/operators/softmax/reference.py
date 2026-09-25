# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reference for the softmax operator."""

import torch


def reference(x):
    """CPU reference: row-wise softmax over the last dim (ground truth)."""
    return torch.softmax(x, dim=-1)


def generate_inputs(rows: int, cols: int, seed=42):
    torch.manual_seed(seed)
    val_range = 4
    return torch.rand(rows, cols, dtype=torch.bfloat16) * val_range
