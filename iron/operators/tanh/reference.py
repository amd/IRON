# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def reference(x):
    """CPU reference: tanh (ground truth)."""
    return torch.tanh(x)


def generate_inputs(input_length: int, seed=42):
    torch.manual_seed(seed)
    val_range = 4
    return torch.rand(input_length, dtype=torch.bfloat16) * val_range
