# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def reference(x, repeat):
    """CPU reference: repeat-interleave along the leading dimension (ground truth)."""
    return x.repeat_interleave(repeat, dim=0)


def generate_golden_reference(rows: int, cols: int, repeat: int, dtype="bf16", seed=42):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    output_tensor = reference(input_tensor, repeat)
    return {"input": input_tensor, "output": output_tensor}
