# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def reference(x, y, scalar):
    """CPU reference: ``scalar * x + y`` in fp32, rounded once (ground truth).

    The vectorized kernel accepts ``scalar`` as fp32 but broadcasts
    ``bfloat16(a)`` internally. The product stays in an fp32 accumulator until
    after adding ``y``; only the coefficient and final result round to bf16.
    """
    a = torch.tensor(scalar, dtype=torch.bfloat16).float()
    return (a * x.float() + y.float()).to(x.dtype)


def generate_inputs(input_length: int, seed=42):
    torch.manual_seed(seed)
    val_range = 4
    x = torch.rand(input_length, dtype=torch.bfloat16) * val_range
    y = torch.rand(input_length, dtype=torch.bfloat16) * val_range
    return x, y
