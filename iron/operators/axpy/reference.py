# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def reference(x, y, scalar):
    """CPU reference: ``scalar * x + y`` in fp32, rounded once (ground truth).

    The kernel takes ``scalar`` as bf16 and rounds only the result, where bf16
    arithmetic would round the product as well.
    """
    a = torch.tensor(scalar, dtype=torch.bfloat16).float()
    return (a * x.float() + y.float()).to(x.dtype)


def generate_inputs(input_length: int, seed=42):
    torch.manual_seed(seed)
    val_range = 4
    x = torch.rand(input_length, dtype=torch.bfloat16) * val_range
    y = torch.rand(input_length, dtype=torch.bfloat16) * val_range
    return x, y
