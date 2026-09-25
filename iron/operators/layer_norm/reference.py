# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def reference(x):
    """CPU reference: layer normalization of each row over its last dim, with no
    learnable affine parameters (ground truth).

    The AIE kernel normalizes one line at a time, computing mean and variance
    over that line alone.
    """
    return torch.nn.functional.layer_norm(x, normalized_shape=(x.shape[-1],))


def generate_inputs(rows: int, cols: int, seed=42):
    torch.manual_seed(seed)
    val_range = 4
    return torch.rand(rows, cols, dtype=torch.bfloat16) * val_range
