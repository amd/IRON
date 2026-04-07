# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def generate_golden_reference(rows: int, cols: int, dtype="bf16", seed=42):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    # normalized_shape=(cols,) normalizes each row independently over its `cols` elements.
    # This matches the AIE kernel behavior, which processes one tile (one row) at a time
    # and computes mean and variance per row (no learnable affine parameters).
    output_tensor = torch.nn.functional.layer_norm(
        input_tensor, normalized_shape=(cols,)
    )
    return {"input": input_tensor, "output": output_tensor}
