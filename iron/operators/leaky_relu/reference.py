# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def reference(x, alpha=0.01):
    """CPU reference: leaky ReLU with negative slope ``alpha`` (ground truth)."""
    return torch.nn.functional.leaky_relu(x, negative_slope=alpha)


def generate_inputs(input_length: int, seed=42):
    torch.manual_seed(seed)
    val_range = 4
    return torch.rand(input_length, dtype=torch.bfloat16) * val_range - val_range / 2
