# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def generate_random_inputs(H, G, d, E, S, causal=True, seed=42):
    """Generate just the *inputs* needed for the core MHA attention test, with
    no expensive PyTorch reference computation.

    Suitable for the benchmark test (which doesn't verify the full output) and
    for very large sequence lengths where the full golden reference is
    impractical.  The causal mask is built with a single ``torch.triu`` instead
    of the H*S² nested-loop construction in :func:`generate_golden_reference`.

    Returned dict matches the input keys consumed by the benchmark test
    (``queries_deinterleaved``, ``keys_for_scores``, ``values_for_context``),
    plus ``_scale`` (the scalar 1/sqrt(d)) and ``_causal`` (the bool flag) for
    use by sample verification.

    Note: the scale factor and causal mask are baked into the operator's
    kernels (no host-side buffers), so this function deliberately does *not*
    materialise the H*S*S scale/mask tensors — at large S those would be tens
    of GB each and OOM the machine (e.g. ~24 GB apiece at S=32768, H=12).
    """
    torch.manual_seed(seed)
    val_range = 0.5

    # Pre-deinterleaved/transposed/repeated Q, K, V (the layout the
    # AttentionPrefillFused operator consumes directly).
    queries_deinterleaved = (torch.randn(H, S, d) * val_range).to(torch.bfloat16)
    keys_for_scores = (torch.randn(H, d, S) * val_range).to(torch.bfloat16)
    values_for_context = (torch.randn(H, S, d) * val_range).to(torch.bfloat16)

    scale = 1.0 / (d**0.5)

    out = {
        "queries_deinterleaved": queries_deinterleaved,
        "keys_for_scores": keys_for_scores,
        "values_for_context": values_for_context,
        "_scale": scale,
        "_causal": causal,
    }

    return out


def compute_attn_context_at_rows(
    queries_deinterleaved,
    keys_for_scores,
    values_for_context,
    scale,
    causal,
    sample_hms,
):
    """Compute the expected ``attn_context[h, m, :]`` row for each (h, m) in
    ``sample_hms``.

    Cheap even at very large S: per sample is O(S * d) — a single (1, d) @ (d, S)
    matmul plus an O(S) softmax plus an (S,) @ (S, d) reduction.

    Args:
        queries_deinterleaved: (H, S, d) bfloat16 tensor
        keys_for_scores:       (H, d, S) bfloat16 tensor
        values_for_context:    (H, S, d) bfloat16 tensor
        scale:                 1 / sqrt(d) (Python float)
        causal:                bool — apply causal mask (zero out k > m)
        sample_hms:            iterable of (h, m) tuples to compute

    Returns:
        dict mapping (h, m) -> torch.Tensor of shape (d,) in bfloat16.
    """
    out = {}
    for h, m in sample_hms:
        q = queries_deinterleaved[h, m, :].float()  # (d,)
        k = keys_for_scores[h, :, :].float()  # (d, S)
        scores = q @ k  # (S,)
        scaled = scores * scale  # (S,)
        if causal:
            # Match the operator's behaviour: positions strictly greater than m
            # receive -inf and contribute zero after softmax.
            scaled = scaled.clone()
            scaled[m + 1 :] = float("-inf")
        weights = torch.softmax(scaled, dim=-1)  # (S,)
        v = values_for_context[h, :, :].float()  # (S, d)
        out[(h, m)] = (weights @ v).to(torch.bfloat16)  # (d,)
    return out


def _apply_rope_4d(x, angles):
    """Apply RoPE to a 4D tensor using interleaved cos/sin angles.

    x: (batch, heads, seq_len, head_dim)
    angles: (seq_len, head_dim) with interleaved [cos_0, sin_0, cos_1, sin_1, ...]
    Returns: same shape as x with RoPE applied (two-halves method).
    """
    half = x.shape[-1] // 2
    cos = angles[:, ::2].unsqueeze(0).unsqueeze(0)  # (1, 1, S, half)
    sin = angles[:, 1::2].unsqueeze(0).unsqueeze(0)  # (1, 1, S, half)
    x1, x2 = x[..., :half], x[..., half:]
    return torch.cat([x1 * cos - x2 * sin, x2 * cos + x1 * sin], dim=-1)


def _bf16_matmul(a, b):
    """(float32 matmul) → bfloat16, matching NPU accumulation."""
    return (a.float() @ b.float()).to(torch.bfloat16)


def generate_golden_reference(
    num_heads,
    num_kv_groups,
    head_dim,
    embedding_dim,
    seq_len,
    seed=42,
):
    """Generate golden reference for fused attention prefill.

    Parameters:
        num_heads (H): number of query attention heads
        num_kv_groups (G): number of KV heads (G=H for MHA, G<H for GQA)
        head_dim (d): dimension per head
        embedding_dim (E): model embedding dimension
        seq_len (S): sequence length (= max_seq_len for prefill)
        seed: random seed

    Returns:
        dict with all intermediate and final tensors
    """
    torch.manual_seed(seed)
    H, G, d, E, S = num_heads, num_kv_groups, head_dim, embedding_dim, seq_len
    group_size = H // G

    val_range = 0.5

    # Input: (S, E)
    x = torch.randn(S, E, dtype=torch.float32).to(torch.bfloat16) * val_range

    # RoPE angles for all S positions: shape (S, d)
    # LUT format: interleaved [cos_0, sin_0, cos_1, sin_1, ...]
    freqs = 1.0 / (10000.0 ** (torch.arange(0, d, 2, dtype=torch.float32) / d))
    rope_angles = torch.zeros(S, d, dtype=torch.float32)
    for pos in range(S):
        angles_half = freqs * pos
        rope_angles[pos, ::2] = torch.cos(angles_half)
        rope_angles[pos, 1::2] = torch.sin(angles_half)
    rope_angles = rope_angles.to(torch.bfloat16)

    # Weight matrices (transposed for GEMM: input @ W → output)
    W_query = torch.randn(E, H * d, dtype=torch.bfloat16) * val_range
    W_key = torch.randn(E, G * d, dtype=torch.bfloat16) * val_range
    W_value = torch.randn(E, G * d, dtype=torch.bfloat16) * val_range
    W_output = torch.randn(H * d, E, dtype=torch.bfloat16) * val_range

    # Scale factor: 1/sqrt(d), broadcast to (H*S*S,)
    scale = 1.0 / (d**0.5)
    attn_scale_factor = torch.full((H * S * S,), scale, dtype=torch.bfloat16)

    # Causal mask: (H*S, S) — 0 for valid positions, -inf for future
    causal_mask = torch.zeros(H * S, S, dtype=torch.bfloat16)
    for h in range(H):
        for i in range(S):
            for j in range(i + 1, S):
                causal_mask[h * S + i, j] = torch.tensor(float("-inf")).to(
                    torch.bfloat16
                )

    # ---- Q/K/V projections ----
    queries_raw = _bf16_matmul(x, W_query)  # (S, H*d)
    keys_raw = _bf16_matmul(x, W_key)  # (S, G*d)
    values_raw = _bf16_matmul(x, W_value)  # (S, G*d)

    # ---- RoPE (reuses rope_utils.apply_rope with 4D interface) ----
    # Reshape interleaved (S, N*d) → (1, N, S, d) for rope_utils
    queries_roped = (
        _apply_rope_4d(
            queries_raw.reshape(S, H, d).permute(1, 0, 2).unsqueeze(0),  # (1, H, S, d)
            rope_angles,
        )
        .squeeze(0)
        .permute(1, 0, 2)
        .contiguous()
        .reshape(S * H, d)
    )  # (S*H, d)

    keys_roped = (
        _apply_rope_4d(
            keys_raw.reshape(S, G, d).permute(1, 0, 2).unsqueeze(0),  # (1, G, S, d)
            rope_angles,
        )
        .squeeze(0)
        .permute(1, 0, 2)
        .contiguous()
        .reshape(S * G, d)
    )  # (S*G, d)

    # ---- Deinterleave Q/K/V ----
    queries_deinterleaved = (
        queries_roped.reshape(S, H, d).transpose(0, 1).contiguous()
    )  # (H, S, d)
    keys_deinterleaved = (
        keys_roped.reshape(S, G, d).transpose(0, 1).contiguous()
    )  # (G, S, d)
    keys_transposed = keys_deinterleaved.transpose(1, 2).contiguous()  # (G, d, S)
    values_deinterleaved = (
        values_raw.reshape(S, G, d).transpose(0, 1).contiguous()
    )  # (G, S, d)

    # ---- GQA repeat ----
    if group_size > 1:
        keys_for_scores = (
            keys_transposed.reshape(G, d * S)
            .repeat_interleave(group_size, dim=0)
            .reshape(H, d, S)
        )
        values_for_context = (
            values_deinterleaved.reshape(G, S * d)
            .repeat_interleave(group_size, dim=0)
            .reshape(H, S, d)
        )
    else:
        keys_for_scores = keys_transposed  # (H, d, S)
        values_for_context = values_deinterleaved  # (H, S, d)

    # ---- Score GEMM per head ----
    attn_scores = torch.stack(
        [_bf16_matmul(queries_deinterleaved[h], keys_for_scores[h]) for h in range(H)]
    )  # (H, S, S)

    # ---- Scale ----
    attn_scores_scaled = (attn_scores.float() * scale).to(torch.bfloat16)

    # ---- Causal mask ----
    attn_scores_masked = (
        attn_scores_scaled.reshape(H * S, S).float() + causal_mask.float()
    ).to(torch.bfloat16)

    # ---- Softmax ----
    attn_weights = torch.nn.functional.softmax(
        attn_scores_masked.float().reshape(H, S, S), dim=-1
    ).to(
        torch.bfloat16
    )  # (H, S, S)

    # ---- Context GEMM per head ----
    attn_context = torch.stack(
        [_bf16_matmul(attn_weights[h], values_for_context[h]) for h in range(H)]
    )  # (H, S, d)

    # ---- Re-interleave context: (H, S, d) → (S, H*d) ----
    context_interleaved = attn_context.transpose(0, 1).contiguous().reshape(S, H * d)

    # ---- Output projection ----
    attn_output = _bf16_matmul(context_interleaved, W_output)

    return {
        "input": x,
        "rope_angles": rope_angles,
        "W_query": W_query,
        "W_key": W_key,
        "W_value": W_value,
        "W_output": W_output,
        "attn_scale_factor": attn_scale_factor,
        "causal_mask": causal_mask,
        "queries_raw": queries_raw,
        "keys_raw": keys_raw,
        "values_raw": values_raw,
        "queries_roped": queries_roped,
        "keys_roped": keys_roped,
        "queries_deinterleaved": queries_deinterleaved,
        "keys_deinterleaved": keys_deinterleaved,
        "keys_transposed": keys_transposed,
        "values_deinterleaved": values_deinterleaved,
        "keys_for_scores": keys_for_scores,
        "values_for_context": values_for_context,
        "attn_scores": attn_scores,
        "attn_scores_scaled": attn_scores_scaled,
        "attn_scores_masked": attn_scores_masked,
        "attn_weights": attn_weights,
        "attn_context": attn_context,
        "context_interleaved": context_interleaved,
        "attn_output": attn_output,
    }
