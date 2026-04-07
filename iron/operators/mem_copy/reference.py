# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def generate_golden_reference(input_length):
    torch.manual_seed(42)

    # Generate random input data
    val_range = 4
    A = torch.rand(input_length, dtype=torch.bfloat16) * val_range

    return {
        "input": A,
        "output": A.clone(),
    }
