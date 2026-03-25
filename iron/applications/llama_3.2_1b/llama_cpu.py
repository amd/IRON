#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import math
import llama_inference_harness as harness

# Operators
# ##########################################################################


def rope_forward(x, angles):
    """Rotary positional embedding using precomputed angles"""
    # x: (batch, seq_len, num_heads, head_dim) after view and before transpose
    # angles: (seq_len, head_dim) already sliced to the correct position range by the caller
    _, seq_len, _, head_dim = x.shape

    # Split into even and odd dimensions
    x1 = x[..., : head_dim // 2]  # (batch, seq_len, num_heads, head_dim//2)
    x2 = x[..., head_dim // 2 :]  # (batch, seq_len, num_heads, head_dim//2)

    # Get cos and sin from angles
    cos = angles[:, ::2]  # (seq_len, head_dim//2)
    sin = angles[:, 1::2]  # (seq_len, head_dim//2)

    # Reshape for broadcasting: (1, seq_len, 1, head_dim//2)
    # (The same cosine and sine values are used across batch and heads.)
    cos = cos.unsqueeze(0).unsqueeze(2)
    sin = sin.unsqueeze(0).unsqueeze(2)

    # Rotate: [x1*cos - x2*sin, x1*sin + x2*cos]
    rotated = torch.empty_like(x)
    rotated[..., : head_dim // 2] = x1 * cos - x2 * sin
    rotated[..., head_dim // 2 :] = x1 * sin + x2 * cos

    return rotated


def rms_norm_forward(x, weight, eps=1e-5):
    """Root Mean Square Layer Normalization"""
    # x: (batch, seq_len, dim)
    variance = x.pow(2).mean(-1, keepdim=True)
    x = x * torch.rsqrt(variance + eps)
    return weight * x


def grouped_query_attention_forward(
    x,
    keys_cache,
    values_cache,
    W_query,
    W_key,
    W_value,
    W_out,
    angles,
    mask=None,
    num_heads=32,
    num_kv_groups=8,
):
    batch, seq_len, d_in = x.shape
    assert W_query.shape[0] >= num_heads and W_query.shape[0] % num_heads == 0
    head_dim = W_query.shape[0] // num_heads
    assert W_key.shape[0] == num_kv_groups * head_dim
    assert W_value.shape[0] == num_kv_groups * head_dim
    num_preceding_tokens = keys_cache.shape[2]
    assert keys_cache.shape == (batch, num_kv_groups, num_preceding_tokens, head_dim)
    assert values_cache.shape == (batch, num_kv_groups, num_preceding_tokens, head_dim)

    # Step 1: Linear projections
    # This multiplication produces queries, keys and values for all tokens in the sequence.
    # The weight matrix is such that multiple queries, keys and values are generated for each token.
    # For each token, each head corresponds to one query.
    # In particular, each token gets `num_heads` queries and `num_kv_groups` keys/values (keys/values shared for multiple queries).
    # Due to the structure of the matmul, all queries, keys and values are contiguous for each token.
    # Note that during the decode phase, seq_len=1, and we are only calculating the projections for the most recent token -- the keys and values of previous tokens will be concatenated in step 4.
    queries = torch.nn.functional.linear(
        x, W_query
    )  # (batch, seq_len, num_heads * head_dim)
    keys = torch.nn.functional.linear(
        x, W_key
    )  # (batch, seq_len, num_kv_groups * head_dim)
    values = torch.nn.functional.linear(
        x, W_value
    )  # (batch, seq_len, num_kv_groups * head_dim)
    queries = queries.view(
        batch, seq_len, num_heads, head_dim
    )  # (batch, seq_len, num_heads, head_dim)
    keys = keys.view(
        batch, seq_len, num_kv_groups, head_dim
    )  # (batch, seq_len, num_kv_groups, head_dim)
    values = values.view(
        batch, seq_len, num_kv_groups, head_dim
    )  # (batch, seq_len, num_kv_groups, head_dim)

    # Step 2: Apply RoPE
    queries = rope_forward(
        queries, angles[num_preceding_tokens : num_preceding_tokens + seq_len]
    )
    keys = rope_forward(
        keys, angles[num_preceding_tokens : num_preceding_tokens + seq_len]
    )

    # Step 3: Transpose for attention computation
    # As a result of the attention projections, the queries, keys and values for each head are interspersed with each other.
    # Transpose so that heads are consecutive for attention computation: (batch, seq_len, num_heads, head_dim) -> (batch, num_heads, seq_len, head_dim)
    queries = queries.transpose(1, 2)  # (batch, num_heads, seq_len, head_dim)
    keys = keys.transpose(1, 2)  # (batch, num_kv_groups, seq_len, head_dim)
    values = values.transpose(1, 2)  # (batch, num_kv_groups, seq_len, head_dim)

    # Step 4: Combine newly computed keys/values for most recent token with cache; these values are used as the updated cache and will be returned to use in the next iteration.
    keys_cache = torch.cat([keys_cache, keys], dim=2)
    values_cache = torch.cat([values_cache, values], dim=2)
    keys = keys_cache
    values = values_cache

    # Step 5: Repeat keys and values for grouped attention -- multiple queries get the same key/value
    group_size = num_heads // num_kv_groups
    keys = keys.repeat_interleave(group_size, dim=1)
    values = values.repeat_interleave(group_size, dim=1)

    # Step 6: Compute attention scores
    # (batch, num_heads, seq_len, head_dim) @ (batch, num_heads, head_dim, seq_len)
    # -> (batch, num_heads, seq_len, seq_len)
    # Entry at row i, column j, indicates how much token i's query attends to token j's key.
    scores = torch.matmul(queries, keys.transpose(-2, -1)) / math.sqrt(head_dim)

    # Step 7: Apply mask
    # This ensures causality, so that tokens in the future cannot attend to tokens in the past.
    if mask is not None:
        scores = scores.masked_fill(mask, float("-inf"))

    # Step 8: Apply softmax to squeeze scores into probabilities (0, 1)
    attention_weights = torch.nn.functional.softmax(scores, dim=-1)

    # Step 9: Compute attention output
    # (batch, num_heads, seq_len, seq_len) @ (batch, num_heads, seq_len, head_dim)
    # -> (batch, num_heads, seq_len, head_dim)
    context = torch.matmul(attention_weights, values)

    # Step 10: Concatenate heads and project
    # (batch, seq_len, num_heads, head_dim) -> (batch, seq_len, num_heads * head_dim)
    context = context.transpose(1, 2).contiguous().view(batch, seq_len, -1)

    output = torch.nn.functional.linear(context, W_out)

    return output, keys_cache, values_cache


def swiglu_ffn_forward(x, fc1_weight, fc2_weight, fc3_weight):
    # Step 1: Parallel projections: (batch, seq_len, embedding_dim) -> (batch, seq_len, swiglu_hidden_dim)
    gate = torch.nn.functional.linear(x, fc1_weight)  # gate projection
    up = torch.nn.functional.linear(x, fc2_weight)  # up projection

    # Step 2: Apply SiLU activation
    gate_activated = torch.nn.functional.silu(
        gate
    )  # (batch, seq_len, swiglu_hidden_dim)

    # Step 3: Element-wise multiplication (apply the 'gating')
    hidden = gate_activated * up  # (batch, seq_len, swiglu_hidden_dim)

    # Step 4: Down projection: (batch, seq_len, swiglu_hidden_dim) -> (batch, seq_len, embedding_dim)
    output = torch.nn.functional.linear(hidden, fc3_weight)

    return output


def transformer_block_forward(
    x,
    attn_keys_cache,
    attn_values_cache,
    num_heads,
    num_kv_groups,
    W_norm1,
    W_attn_query,
    W_attn_key,
    W_attn_value,
    W_attn_out,
    W_norm2,
    W_ffn_fc1,
    W_ffn_fc2,
    W_ffn_fc3,
    rope_angles,
    attn_mask,
):
    # Step 1: RMS normalization
    x_norm = rms_norm_forward(x, W_norm1)

    # Step 2: Attention
    attn_output, attn_keys, attn_values = grouped_query_attention_forward(
        x_norm,
        attn_keys_cache,
        attn_values_cache,
        W_attn_query,
        W_attn_key,
        W_attn_value,
        W_attn_out,
        rope_angles,
        attn_mask,
        num_heads,
        num_kv_groups,
    )

    # Step 3: Residual
    x = x + attn_output

    # Step 4: Post-norm
    x_norm = rms_norm_forward(x, W_norm2)

    # Step 5: fully-connected feed-forward network
    ffn_output = swiglu_ffn_forward(x_norm, W_ffn_fc1, W_ffn_fc2, W_ffn_fc3)

    # Step 6: Residual
    x = x + ffn_output

    return x, attn_keys, attn_values


def llama_forward_pass(config, state):
    batch, seq_len = state.token_ids.shape

    # Step 1: Token embedding
    tok_emb_weight = config.weights["model.embed_tokens.weight"]
    x = torch.nn.functional.embedding(
        state.token_ids, tok_emb_weight
    )  # (batch, seq_len, emb_dim)

    # Step 2: Create causal mask
    attn_mask = torch.triu(
        torch.ones(seq_len, seq_len, device=x.device, dtype=torch.bool), diagonal=1
    )

    # Step 3: Apply transformer blocks
    for layer_idx in range(config.n_layers):
        x, state.attn_keys_caches[layer_idx], state.attn_values_caches[layer_idx] = (
            transformer_block_forward(
                x,
                state.attn_keys_caches[layer_idx],
                state.attn_values_caches[layer_idx],
                config.n_heads,
                config.n_kv_groups,
                W_norm1=config.weights[
                    f"model.layers.{layer_idx}.input_layernorm.weight"
                ],
                W_attn_query=config.weights[
                    f"model.layers.{layer_idx}.self_attn.q_proj.weight"
                ],
                W_attn_key=config.weights[
                    f"model.layers.{layer_idx}.self_attn.k_proj.weight"
                ],
                W_attn_value=config.weights[
                    f"model.layers.{layer_idx}.self_attn.v_proj.weight"
                ],
                W_attn_out=config.weights[
                    f"model.layers.{layer_idx}.self_attn.o_proj.weight"
                ],
                W_ffn_fc1=config.weights[
                    f"model.layers.{layer_idx}.mlp.gate_proj.weight"
                ],
                W_ffn_fc2=config.weights[
                    f"model.layers.{layer_idx}.mlp.up_proj.weight"
                ],
                W_ffn_fc3=config.weights[
                    f"model.layers.{layer_idx}.mlp.down_proj.weight"
                ],
                W_norm2=config.weights[
                    f"model.layers.{layer_idx}.post_attention_layernorm.weight"
                ],
                rope_angles=config.angles,
                attn_mask=attn_mask,
            )
        )

    # Step 4: Final normalization
    final_norm_weight = config.weights["model.norm.weight"]
    x = rms_norm_forward(x, final_norm_weight)

    # Step 5: Output projection
    logits = torch.nn.functional.linear(
        x, config.weights["model.embed_tokens.weight"]
    )  # (batch, seq_len, vocab_size)

    return logits, state


# Main
# ##########################################################################


def main():
    args = harness.parse_args()
    prompt = harness.get_prompt(args.prompt_len)
    config, state = harness.init(args.weights_path, args.tokenizer_path, prompt=prompt)
    print(prompt, end="", flush=True)
    harness.generate(config, state, llama_forward_pass, num_tokens=args.num_tokens)


if __name__ == "__main__":
    main()
