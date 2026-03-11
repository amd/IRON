# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from torch.nn.attention import SDPBackend, sdpa_kernel

import numpy as np
from ml_dtypes import bfloat16


def pad_to_multiple_of_64(tensor, seq_dim, num_pipeline=1):
    """Pad tensor to multiple of 64 along specified dimension."""
    seq_len = tensor.shape[seq_dim]
    padded_seq_len = ((seq_len + 63 * num_pipeline) // (64 * num_pipeline)) * (
        64 * num_pipeline
    )
    if padded_seq_len == seq_len:
        return tensor

    pad_size = padded_seq_len - seq_len
    pad_dims = [0] * (2 * tensor.ndim)
    pad_dims[2 * (tensor.ndim - 1 - seq_dim) + 1] = pad_size

    return torch.nn.functional.pad(tensor, pad_dims)


def generate_golden_reference(
    heads=1,
    S_q=256,
    S_kv=256,
    d=256,
    num_kv_heads=2,
    num_pipeline=1,
    seed=42,
):
    """
    Generate golden reference data for MHA (Multi-Head Attention).

    Parameters:
        heads: Number of query heads
        S_q: Sequence length for query (Q)
        S_kv: Sequence length for key/value (KV)
        d: Embedding dimension per head
        num_kv_heads: Number of heads for Key-Value pairs (0 means same as heads)
        num_pipeline: Number of pipelines for padding calculation
        seed: Random seed

    Returns:
        dict: Contains 'Q' (query), 'K' (key), 'V' (value), 'O' (output)
    """
    torch.manual_seed(seed)
    np.random.seed(seed)

    if num_kv_heads == 0:
        num_kv_heads = heads
    number_of_groups = heads // num_kv_heads

    val_range = 4

    Q = torch.rand(heads, S_q, d, dtype=torch.bfloat16) * val_range
    K = torch.rand(num_kv_heads, S_kv, d, dtype=torch.bfloat16) * val_range
    V = torch.rand(num_kv_heads, S_kv, d, dtype=torch.bfloat16) * val_range

    K_original = K.clone()
    V_original = V.clone()

    K = K.repeat_interleave(number_of_groups, dim=0)
    V = V.repeat_interleave(number_of_groups, dim=0)

    # MHA from PyTorch
    inv_scale = 1 / np.sqrt(K.shape[-1])

    with sdpa_kernel(SDPBackend.FLASH_ATTENTION):
        O = torch.nn.functional.scaled_dot_product_attention(
            Q.to(torch.bfloat16).unsqueeze(0),
            K.to(torch.bfloat16).unsqueeze(0),
            V.to(torch.bfloat16).unsqueeze(0),
            dropout_p=0.0,
            is_causal=True,
            scale=inv_scale,
        ).squeeze(0)

    # Pad all tensors to multiple of 64
    Q = pad_to_multiple_of_64(Q, seq_dim=1, num_pipeline=num_pipeline)
    K_original = pad_to_multiple_of_64(K_original, seq_dim=1, num_pipeline=num_pipeline)
    V_original = pad_to_multiple_of_64(V_original, seq_dim=1, num_pipeline=num_pipeline)
    O = pad_to_multiple_of_64(O, seq_dim=1, num_pipeline=num_pipeline)

    return {
        "Q": Q,
        "K": K_original,
        "V": V_original,
        "O": O,
    }
