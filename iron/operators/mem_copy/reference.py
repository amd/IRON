# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def reference(x):
    """CPU reference: a copy (ground truth)."""
    return x.clone()


def generate_inputs(input_length):
    torch.manual_seed(42)
    val_range = 4
    return torch.rand(input_length, dtype=torch.bfloat16) * val_range
