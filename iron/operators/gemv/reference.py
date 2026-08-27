# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def reference(A, B):
    """CPU reference: matrix-vector product ``C = A @ B`` (ground truth)."""
    return A @ B


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
    C = reference(A, B)

    return {
        "A": A,
        "B": B,
        "C": C,
    }


def generate_golden_reference_batched(M=128, K=128, num_batches=2, seed=42):
    """
    Generate golden reference data for a batched GEMV (num_batches independent
    matrix-vector products stacked contiguously, matching the GEMV op layout).

    Parameters:
        M: Number of rows of each matrix A
        K: Number of columns of each matrix A (equals vector B length)
        num_batches: Number of independent GEMVs
        seed: Random seed

    Returns:
        dict: Contains 'A' (matrices), 'B' (vectors), 'C' (output vectors)
    """
    torch.manual_seed(seed)
    val_range = 4
    A = torch.randn(num_batches, M, K, dtype=torch.bfloat16) * val_range
    B = torch.randn(num_batches, K, dtype=torch.bfloat16) * val_range
    C = torch.empty(num_batches, M, dtype=torch.bfloat16)
    for b in range(num_batches):
        C[b] = A[b] @ B[b]
    return {"A": A, "B": B, "C": C}


def gelu_tanh_approx(x):
    """Tanh-approximation GELU, matching aie_kernels/aie2p/gelu.cc.

    0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3))). Computed in float32.
    """
    xf = np.asarray(x, dtype=np.float32)
    inner = 0.79788456 * (xf + 0.044715 * xf**3)
    return 0.5 * xf * (1.0 + np.tanh(inner))


def rms_norm_ref(x, epsilon=1e-5):
    """RMSNorm, matching aie_kernels/{aie2,aie2p}/rms_norm.cc's rms_norm_bf16_vector:
    f32 sum-of-squares reduction, affine-free (gamma=1), computed in float32.
    """
    xf = np.asarray(x, dtype=np.float32)
    inv_rms = 1.0 / np.sqrt(np.mean(xf * xf) + epsilon)
    return xf * inv_rms


def layer_norm_ref(x, epsilon=1e-5):
    """LayerNorm, matching aie_kernels/{aie2,aie2p}/layer_norm.cc's layer_norm:
    f32 mean/var reduction, affine-free (gamma=1, beta=0), computed in float32.
    """
    xf = np.asarray(x, dtype=np.float32)
    mean = np.mean(xf)
    var = np.mean(xf * xf) - mean * mean
    return (xf - mean) / np.sqrt(var + epsilon)
