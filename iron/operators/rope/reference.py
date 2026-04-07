# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def compute_rope_params(
    head_dim,
    theta_base=10_000,
    context_length=4096,
    method_type=0,
    freq_config=None,
    dtype=torch.float32,
):
    """Compute RoPE parameters (cos and sin tables)."""
    assert head_dim % 2 == 0, "Embedding dimension must be even"

    # Compute the inverse frequencies
    inv_freq = 1.0 / (
        theta_base
        ** (
            torch.arange(0, head_dim, 2, dtype=dtype)[: (head_dim // 2)].float()
            / head_dim
        )
    )

    # Frequency adjustments
    if freq_config is not None:
        low_freq_wavelen = (
            freq_config["original_context_length"] / freq_config["low_freq_factor"]
        )
        high_freq_wavelen = (
            freq_config["original_context_length"] / freq_config["high_freq_factor"]
        )

        wavelen = 2 * torch.pi / inv_freq

        inv_freq_llama = torch.where(
            wavelen > low_freq_wavelen, inv_freq / freq_config["factor"], inv_freq
        )

        smooth_factor = (
            freq_config["original_context_length"] / wavelen
            - freq_config["low_freq_factor"]
        ) / (freq_config["high_freq_factor"] - freq_config["low_freq_factor"])

        smoothed_inv_freq = (1 - smooth_factor) * (
            inv_freq / freq_config["factor"]
        ) + smooth_factor * inv_freq

        is_medium_freq = (wavelen <= low_freq_wavelen) & (wavelen >= high_freq_wavelen)
        inv_freq_llama = torch.where(is_medium_freq, smoothed_inv_freq, inv_freq_llama)
        inv_freq = inv_freq_llama

    # Generate position indices
    positions = torch.arange(context_length, dtype=dtype)

    # Compute the angles
    angles = positions.unsqueeze(1) * inv_freq.unsqueeze(
        0
    )  # Shape: (context_length, head_dim / 2)

    # Precompute sine and cosine
    cos = torch.cos(angles)
    sin = torch.sin(angles)

    return cos, sin


def apply_rope(x, cos, sin, method_type=0):
    """Apply rotary position embedding to input tensor."""
    if method_type == 0:  # For the two-halves method used in HF transformers
        # x: (n_heads, seq_len, head_dim)
        n_heads, seq_len, head_dim = x.shape
        assert head_dim % 2 == 0, "Head dimension must be even"

        # Split x into first half and second half
        x1 = x[..., : head_dim // 2]  # First half
        x2 = x[..., head_dim // 2 :]  # Second half

        # Adjust sin and cos shapes
        cos = cos[:seq_len, :]  # Shape: (seq_len, head_dim / 2)
        sin = sin[:seq_len, :]

        # Apply the rotary transformation
        x_rotated = torch.empty_like(x)
        x_rotated[..., : head_dim // 2] = (x1 * cos) + (-x2 * sin)
        x_rotated[..., head_dim // 2 :] = (x2 * cos) + (x1 * sin)

        # It's ok to use lower-precision after applying cos and sin rotation
        return x_rotated.to(dtype=x.dtype)
    elif method_type == 1:  # For the interleaved method used in the Llama paper
        # x: (n_heads, seq_len, head_dim)
        n_heads, seq_len, head_dim = x.shape
        assert head_dim % 2 == 0, "Head dimension must be even"

        # Split x into even and odd columns
        x_even = x[..., ::2]  # Even columns
        x_odd = x[..., 1::2]  # Odd columns

        # Adjust sin and cos shapes
        cos = cos[:seq_len, :]  # Shape: (seq_len, head_dim / 2)
        sin = sin[:seq_len, :]

        # Apply the rotary transformation and interleave the even and odd outputs
        x_rotated = torch.empty_like(x)
        x_rotated[..., ::2] = (x_even * cos) - (x_odd * sin)
        x_rotated[..., 1::2] = (x_even * sin) + (x_odd * cos)

        # It's ok to use lower-precision after applying cos and sin rotation
        return x_rotated.to(dtype=x.dtype)
    else:
        raise ValueError("Invalid method_type. Must be 0 or 1.")


def generate_golden_reference(
    rows=4096,
    cols=64,
    context_len=131072,
    method_type=0,
    rope_theta_base=500000.0,
    rope_freq_factor=32.0,
    rope_freq_low_factor=1.0,
    rope_freq_high_factor=4.0,
    rope_freq_orig_ctx_len=8192,
    seed=42,
):
    torch.manual_seed(seed)

    # Generate golden inputs
    freq_config = {
        "factor": rope_freq_factor,
        "low_freq_factor": rope_freq_low_factor,
        "high_freq_factor": rope_freq_high_factor,
        "original_context_length": rope_freq_orig_ctx_len,
    }
    cos, sin = compute_rope_params(
        head_dim=cols,
        theta_base=rope_theta_base,
        context_length=context_len,
        method_type=method_type,
        freq_config=freq_config,
    )
    val_range = 4
    # Head count is inferred from rows and context_len. This logic assumes rows is either
    # smaller than context_len (1 head, seq_len == rows) or an exact multiple of context_len
    # (n_heads == rows // context_len).
    if context_len < rows and rows % context_len != 0:
        raise ValueError(
            f"rows ({rows}) must be a multiple of context_len ({context_len}) when rows > context_len"
        )
    n_heads = rows // context_len if context_len < rows else 1
    seq_len = rows // n_heads
    A = torch.rand(n_heads, seq_len, cols, dtype=torch.bfloat16) * val_range

    # Create the lut by interleaving cos and sin
    B = torch.zeros((seq_len, cols), dtype=torch.bfloat16)
    B[:, ::2] = cos[:seq_len, : cols // 2]
    B[:, 1::2] = sin[:seq_len, : cols // 2]

    # Generate golden outputs
    C = apply_rope(A, cos, sin, method_type)

    return {
        "A": A,
        "B": B,
        "C": C,
    }
