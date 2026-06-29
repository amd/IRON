# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def generate_golden_reference(
    rows: int, cols: int, dtype="bf16", seed=42, num_batches=1
):
    torch.manual_seed(seed)
    val_range = 4
    # num_batches>1: B independent (rows,cols) matrices laid back-to-back; each is
    # transposed independently and the results concatenated in the same order.
    input_tensor = (
        torch.rand(num_batches, rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    )
    output_tensor = torch.stack(
        [torch.transpose(input_tensor[b], 0, 1) for b in range(num_batches)]
    )
    # drop batch dimension if num_batches == 1
    input_tensor = torch.squeeze(input_tensor, 0)
    output_tensor = torch.squeeze(output_tensor, 0)
    return {"input": input_tensor, "output": output_tensor}
