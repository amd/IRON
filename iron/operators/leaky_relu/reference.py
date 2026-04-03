# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def generate_golden_reference(input_length: int, alpha=0.01, dtype="bf16", seed=42):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = (
        torch.rand(input_length, dtype=torch_dtype_map[dtype]) * val_range
        - val_range / 2
    )
    output_tensor = torch.nn.functional.leaky_relu(input_tensor, negative_slope=alpha)
    return {"input": input_tensor, "output": output_tensor}
