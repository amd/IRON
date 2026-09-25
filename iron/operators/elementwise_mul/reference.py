# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def reference(a, b):
    """CPU reference: element-wise multiplication (ground truth)."""
    return a * b


def generate_inputs(input_length: int, seed=42):
    torch.manual_seed(seed)
    val_range = 4
    a = torch.rand(input_length, dtype=torch.bfloat16) * val_range
    b = torch.rand(input_length, dtype=torch.bfloat16) * val_range
    return a, b
