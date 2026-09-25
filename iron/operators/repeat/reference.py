# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def reference(x, repeat):
    """CPU reference: repeat-interleave along the leading dimension (ground truth)."""
    return x.repeat_interleave(repeat, dim=0)


def generate_inputs(rows: int, cols: int, seed=42):
    torch.manual_seed(seed)
    val_range = 4
    return torch.rand(rows, cols, dtype=torch.bfloat16) * val_range
