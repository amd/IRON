# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def interleave_kv_cache(k_cache, v_cache):
    """Interleave K and V cache rows for the FlowKV DMA pattern.

    Input shapes:
        k_cache: (num_kv_heads, seq_len, head_dim)
        v_cache: (num_kv_heads, seq_len, head_dim)

    Output shape: (num_kv_heads, seq_len, 2, head_dim) flattened.

    For each KV head and position, K row comes first, then V row.
    This layout allows the DMA to stream K and V separately using
    strided access patterns (stride = 2 * head_dim).
    """
    num_kv_heads, seq_len, head_dim = k_cache.shape
    interleaved = torch.empty(num_kv_heads, seq_len, 2, head_dim, dtype=k_cache.dtype)
    interleaved[:, :, 0, :] = k_cache
    interleaved[:, :, 1, :] = v_cache
    return interleaved.reshape(-1)


def apply_rope_two_halves(x, cos, sin):
    """Apply RoPE rotation using the two-halves method.

    Args:
        x:   Input tensor, shape (..., head_dim) in any dtype.
        cos: Cosine values, shape (head_dim/2,).
        sin: Sine values, shape (head_dim/2,).

    Returns:
        Rotated tensor, same shape and dtype as x.
    """
    half = x.shape[-1] // 2
    x1 = x[..., :half]
    x2 = x[..., half:]
    out = torch.empty_like(x)
    out[..., :half] = x1 * cos - x2 * sin
    out[..., half:] = x2 * cos + x1 * sin
    return out


def make_rope_angles_interleaved(cos, sin):
    """Create interleaved cos/sin angles for the AIE kernel.

    Args:
        cos: Shape (head_dim/2,) cosine values.
        sin: Shape (head_dim/2,) sine values.

    Returns:
        Shape (head_dim,) interleaved [cos0, sin0, cos1, sin1, ...] in bf16.
    """
    head_dim = cos.shape[0] * 2
    angles = torch.empty(head_dim, dtype=torch.bfloat16)
    angles[0::2] = cos.to(torch.bfloat16)
    angles[1::2] = sin.to(torch.bfloat16)
    return angles


def generate_golden_reference(
    num_heads=32,
    num_kv_heads=8,
    head_dim=64,
    seq_len=128,
    seed=42,
):
    """Generate golden reference data for FlowKV decode attention with fused RoPE.

    Computes scaled dot-product attention for a single decode step with RoPE
    applied to Q before attention scores are computed. K in the cache is
    assumed to be already rotated (standard practice).

        O[h] = softmax(RoPE(Q[h]) @ K[kv_h]^T / sqrt(d)) @ V[kv_h]

    where h is the query head index and kv_h = h // group_size is the
    corresponding KV head.

    Parameters:
        num_heads:    Total number of query heads (32 for Llama 3.2 1B)
        num_kv_heads: Number of KV heads (8 for Llama 3.2 1B)
        head_dim:     Dimension per head (64 for Llama 3.2 1B)
        seq_len:      Current sequence length (number of KV cache positions)
        seed:         Random seed for reproducibility

    Returns:
        dict with:
            Q:              (num_heads, head_dim)           -- unrotated queries
            K_cache:        (num_kv_heads, seq_len, head_dim) -- rotated K cache
            V_cache:        (num_kv_heads, seq_len, head_dim) -- V cache
            KV_interleaved: (num_kv_heads * seq_len * 2 * head_dim,)
            q_angles:       (head_dim,)                     -- interleaved cos/sin
            O:              (num_heads, head_dim)           -- reference output
    """
    torch.manual_seed(seed)
    np.random.seed(seed)

    group_size = num_heads // num_kv_heads

    # Use small value range to keep bf16 precision reasonable
    val_range = 2

    # Generate inputs in bf16 for hardware-accurate reference
    Q = torch.randn(num_heads, head_dim, dtype=torch.bfloat16) * val_range
    K_cache_raw = (
        torch.randn(num_kv_heads, seq_len, head_dim, dtype=torch.bfloat16) * val_range
    )
    V_cache = (
        torch.randn(num_kv_heads, seq_len, head_dim, dtype=torch.bfloat16) * val_range
    )

    # Generate RoPE angles for the current decode position (position = seq_len)
    # and for all K cache positions (0..seq_len-1).
    # Use simple theta_base=10000 without frequency scaling for test simplicity.
    half_dim = head_dim // 2
    inv_freq = 1.0 / (
        10000.0 ** (torch.arange(0, head_dim, 2, dtype=torch.float32) / head_dim)
    )

    # Q position = seq_len (the new token being decoded)
    q_pos = torch.tensor([seq_len], dtype=torch.float32)
    q_cos = torch.cos(q_pos * inv_freq).squeeze(0)  # (half_dim,)
    q_sin = torch.sin(q_pos * inv_freq).squeeze(0)  # (half_dim,)

    # K positions = 0..seq_len-1 (already in the cache)
    k_positions = torch.arange(seq_len, dtype=torch.float32)
    k_cos = torch.cos(
        k_positions.unsqueeze(1) * inv_freq.unsqueeze(0)
    )  # (seq_len, half_dim)
    k_sin = torch.sin(
        k_positions.unsqueeze(1) * inv_freq.unsqueeze(0)
    )  # (seq_len, half_dim)

    # Apply RoPE to K cache (simulating what would have been done during prefill)
    K_cache = torch.empty_like(K_cache_raw)
    for kv_h in range(num_kv_heads):
        for pos in range(seq_len):
            K_cache[kv_h, pos] = apply_rope_two_halves(
                K_cache_raw[kv_h, pos].float(),
                k_cos[pos],
                k_sin[pos],
            ).to(torch.bfloat16)

    # Create interleaved angles for the AIE kernel
    q_angles = make_rope_angles_interleaved(q_cos, q_sin)

    # Apply RoPE to Q in bf16 to match hardware precision
    Q_rotated_bf16 = apply_rope_two_halves(
        Q.float(),
        q_cos,
        q_sin,
    ).to(torch.bfloat16)

    # Compute reference attention output in float32 for precision
    Q_rot_f32 = Q_rotated_bf16.float()
    K_f32 = K_cache.float()
    V_f32 = V_cache.float()

    inv_sqrt_d = 1.0 / np.sqrt(head_dim)

    O = torch.zeros(num_heads, head_dim, dtype=torch.float32)

    for kv_h in range(num_kv_heads):
        k = K_f32[kv_h]  # (seq_len, head_dim)
        v = V_f32[kv_h]  # (seq_len, head_dim)

        for g in range(group_size):
            h = kv_h * group_size + g
            q = Q_rot_f32[h]  # (head_dim,)

            # Attention scores: (seq_len,)
            scores = (q @ k.T) * inv_sqrt_d

            # Softmax
            attn_weights = torch.nn.functional.softmax(scores, dim=-1)

            # Weighted sum: (head_dim,)
            O[h] = attn_weights @ v

    O_bf16 = O.to(torch.bfloat16)

    # Create interleaved KV cache for the design's DDR layout
    kv_interleaved = interleave_kv_cache(K_cache, V_cache)

    return {
        "Q": Q,
        "K_cache": K_cache,
        "V_cache": V_cache,
        "KV_interleaved": kv_interleaved,
        "q_angles": q_angles,
        "O": O_bf16,
    }
