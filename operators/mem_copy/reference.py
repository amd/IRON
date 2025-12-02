# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def generate_golden_reference(input_length):
    torch.manual_seed(42)
    
    # Generate random input data
    val_range = 4
    A = torch.rand(input_length, dtype=torch.bfloat16) * val_range

    return {
        "inout": A,
    }
