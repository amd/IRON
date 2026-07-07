# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def reference(x):
    """CPU reference: SiLU activation (ground truth)."""
    return torch.nn.functional.silu(x)


def generate_golden_reference(input_length: int, dtype="bf16", seed=42):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(input_length, dtype=torch_dtype_map[dtype]) * val_range
    output_tensor = reference(input_tensor)
    return {"input": input_tensor, "output": output_tensor}
