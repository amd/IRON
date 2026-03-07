# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def generate_golden_reference(
    embedding_dim=2048, q_dim=2048, k_dim=512, v_dim=512, seed=42
):
    """Generate golden reference data for fused QKV projection.

    Computes Q, K, V = Wq @ x, Wk @ x, Wv @ x independently, which is
    equivalent to concatenating [Wq; Wk; Wv] and running a single GEMV
    then splitting the output.

    Args:
        embedding_dim: Input dimension (K in GEMV terms)
        q_dim: Query output dimension (number of rows in Wq)
        k_dim: Key output dimension (number of rows in Wk)
        v_dim: Value output dimension (number of rows in Wv)
        seed: Random seed for reproducibility

    Returns:
        dict with keys: x, Wq, Wk, Wv, Q, K, V
    """
    torch.manual_seed(seed)
    val_range = 4

    x = torch.randn(embedding_dim, dtype=torch.bfloat16) * val_range
    Wq = torch.randn(q_dim, embedding_dim, dtype=torch.bfloat16) * val_range
    Wk = torch.randn(k_dim, embedding_dim, dtype=torch.bfloat16) * val_range
    Wv = torch.randn(v_dim, embedding_dim, dtype=torch.bfloat16) * val_range

    Q = Wq @ x
    K = Wk @ x
    V = Wv @ x

    return {
        "x": x,
        "Wq": Wq,
        "Wk": Wk,
        "Wv": Wv,
        "Q": Q,
        "K": K,
        "V": V,
    }
