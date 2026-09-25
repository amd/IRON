# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def compute_rope_params(
    head_dim,
    theta_base=10_000,
    context_length=4096,
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


def reference(x, angles, method_type=0):
    """CPU reference for RoPE from the operator's packed ``angles`` buffer.

    ``angles`` holds interleaved [cos, sin, cos, sin, ...] pairs along the last
    dim. ``method_type`` 0 rotates the two halves of each row (HF
    transformers); 1 rotates its interleaved even/odd pairs (the Llama paper).
    The rotation is computed in fp32 and rounded once.

    ``angles`` may have fewer rows than ``x``; each angle row then applies to
    ``rows / angles.shape[0]`` *consecutive* rows of ``x``, matching the device
    kernel (design.py's ``core_body`` acquires one angle row and applies it to
    that many consecutive input rows before moving on).
    """
    rows = x.shape[0]
    if rows % angles.shape[0] != 0:
        raise ValueError(
            f"{rows} rows cannot share {angles.shape[0]} angle rows evenly"
        )
    rep = rows // angles.shape[0]
    cos = angles[..., 0::2].to(torch.float32).repeat_interleave(rep, dim=0)
    sin = angles[..., 1::2].to(torch.float32).repeat_interleave(rep, dim=0)
    x32 = x.to(torch.float32)
    if method_type == 0:
        half = x.shape[-1] // 2
        x1, x2 = x32[..., :half], x32[..., half:]
        y = torch.cat([x1 * cos - x2 * sin, x2 * cos + x1 * sin], dim=-1)
    elif method_type == 1:
        xe, xo = x32[..., 0::2], x32[..., 1::2]
        y = torch.empty_like(x32)
        y[..., 0::2] = xe * cos - xo * sin
        y[..., 1::2] = xe * sin + xo * cos
    else:
        raise ValueError(f"method_type must be 0 or 1, got {method_type}")
    return y.to(torch.bfloat16)


def generate_inputs(
    rows=4096,
    cols=64,
    context_len=131072,
    rope_theta_base=500000.0,
    rope_freq_factor=32.0,
    rope_freq_low_factor=1.0,
    rope_freq_high_factor=4.0,
    rope_freq_orig_ctx_len=8192,
    seed=42,
):
    """Random input rows and their cos/sin table, laid out as the operator
    takes them: ``x`` is ``(rows, cols)`` with a sequence position's heads on
    consecutive rows, and the table is one row per position."""
    torch.manual_seed(seed)

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
    x = torch.rand(n_heads, seq_len, cols, dtype=torch.bfloat16) * val_range

    # The lut interleaves cos and sin
    angles = torch.zeros((seq_len, cols), dtype=torch.bfloat16)
    angles[:, ::2] = cos[:seq_len, : cols // 2]
    angles[:, 1::2] = sin[:seq_len, : cols // 2]

    return x.transpose(0, 1).reshape(rows, cols).contiguous(), angles
