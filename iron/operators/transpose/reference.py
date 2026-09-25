# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def reference(x):
    """CPU reference: transpose of the last two dims (ground truth), so each of
    a batch of ``(rows, cols)`` matrices is transposed on its own."""
    return x.transpose(-2, -1)


def generate_inputs(rows: int, cols: int, seed=42, num_batches=1):
    """``num_batches`` independent ``(rows, cols)`` matrices laid back-to-back;
    the batch dim is dropped when there is one."""
    torch.manual_seed(seed)
    val_range = 4
    x = torch.rand(num_batches, rows, cols, dtype=torch.bfloat16) * val_range
    return torch.squeeze(x, 0)
