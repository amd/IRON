# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def generate_golden_reference(
    M=128, K=128, seed=42
):  # Defaults are tile-aligned minimums; tests always pass explicit values
    """
    Generate golden reference data for GEMV (General Matrix-Vector Multiplication).

    Parameters:
        M: Number of rows of matrix A
        K: Number of columns of matrix A (equals vector B length)
        seed: Random seed

    Returns:
        dict: Contains 'A' (matrix), 'B' (vector), 'C' (output vector)
    """
    torch.manual_seed(seed)

    # Generate golden inputs
    val_range = 4
    A = torch.randn(M, K, dtype=torch.bfloat16) * val_range
    B = torch.randn(K, dtype=torch.bfloat16) * val_range

    # Generate golden outputs
    C = A @ B

    return {
        "A": A,
        "B": B,
        "C": C,
    }
