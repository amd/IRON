#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Inference harness -- all the necessary code _other_ than the actual model (forward pass).
Exposes a 'harness' function that can be called with a 'forward_pass' function that implements the model.
The 'harness' function does the following:
1. Load and set up model weights, tokenizer, and RoPE angle look-up table.
2. Tokenize the provided input prompt.
3. Run the generation loop to produce new tokens; this calls the provided forward_pass function. Decode and print each generated token.
"""

import torch
import sys
from pathlib import Path
import time
import argparse

import safetensors.torch
import tiktoken, tiktoken.load

# Configuration
# ##########################################################################


class LlamaConfig:
    def __init__(self, weights_path, tokenizer_path):
        # Model architecture
        self.vocab_size = 128256
        self.emb_dim = 2048
        self.n_layers = 16
        self.n_heads = 32
        self.n_kv_groups = 8
        self.head_dim = self.emb_dim // self.n_heads  # 64
        self.hidden_dim = 8192

        # RoPE
        self.rope_base = 500000.0
        self.context_length = 131072

        # Generation
        self.temperature = 0.7
        self.top_k = 50

        # Tokenization
        self.special_tokens = {
            "<|begin_of_text|>": 128000,
            "<|end_of_text|>": 128001,
            "<|start_header_id|>": 128006,
            "<|end_header_id|>": 128007,
            "<|eot_id|>": 128009,
        }
        self.special_tokens.update(
            {
                f"<|reserved_{i}|>": i
                for i in list(range(128002, 128006)) + list(range(128009, 128256))
            }
        )

        # Load model weights and tokenizer
        self.weights = safetensors.torch.load_file(weights_path)
        self.tokenizer = get_tokenizer(tokenizer_path, self.special_tokens)
        # TODO: Assert that weight dimensions match config

        # Compute RoPE angle look-up table
        self.angles = compute_rope_angles(
            self.head_dim, self.context_length, self.rope_base
        )


class LlamaModelState:
    def __init__(self, config):
        # Current IDs of tokens being processed (most recent token for decode; all prompt tokens for prefill)
        self.token_ids = torch.empty(0, dtype=torch.long)
        self.reset_kv_cache(config)

    def reset_kv_cache(self, config):
        self.num_preceding_tokens = 0
        # Set up KV cache -- initially empty
        # This is what passes information from previous tokens to the current token during generation
        self.attn_keys_caches = [
            torch.empty(
                1,
                config.n_kv_groups,
                0,
                config.head_dim,
                dtype=config.weights["model.layers.0.self_attn.k_proj.weight"].dtype,
            )  # (batch_size, n_kv_groups, seq_len, head_dim)
            for _ in range(config.n_layers)
        ]
        self.attn_values_caches = [
            torch.empty(
                1,
                config.n_kv_groups,
                0,
                config.head_dim,
                dtype=config.weights["model.layers.0.self_attn.v_proj.weight"].dtype,
            )  # (batch_size, n_kv_groups, seq_len, head_dim)
            for _ in range(config.n_layers)
        ]


# Utilities
# ##########################################################################


def compute_rope_angles(head_dim, context_length, rope_base=500000.0):
    """Compute RoPE (Rotary Position Embedding) angles."""
    # Precompute the frequency tensor
    inv_freq = 1.0 / (rope_base ** (torch.arange(0, head_dim, 2).float() / head_dim))
    position = torch.arange(context_length).float()
    freqs = torch.outer(position, inv_freq)

    cos = torch.cos(freqs)
    sin = torch.sin(freqs)

    # Interleave cos and sin - create angles buffer
    angles = torch.empty(context_length, head_dim)
    angles[:, ::2] = cos
    angles[:, 1::2] = sin
    return angles


def get_tokenizer(tokenizer_path, special_tokens):
    mergeable = tiktoken.load.load_tiktoken_bpe(tokenizer_path)
    return tiktoken.Encoding(
        name="llama3.2-1b",
        pat_str=r"(?i:'s|'t|'re|'ve|'m|'ll|'d)"
        r"|[^\r\n\p{L}\p{N}]?\p{L}+"
        r"|\p{N}{1,3}"
        r"| ?[^\s\p{L}\p{N}]+[\r\n]*"
        r"|\s*[\r\n]+"
        r"|\s+(?!\S)"
        r"|\s+",
        mergeable_ranks=mergeable,
        special_tokens=special_tokens,
    )


# Generation loop
# ##########################################################################


def generate_token(config, forward_pass, state):
    # Step 1: Forward pass
    logits, state = forward_pass(config, state)

    # Step 2: Get logits for last token
    last_token_logits = logits[:, -1, :]  # (batch, vocab_size)

    # Step 3: Temperature scaling
    if config.temperature > 0:
        last_token_logits = last_token_logits / config.temperature

    # Step 4: Top-k filtering
    if config.top_k is not None:
        top_logits, _ = torch.topk(last_token_logits, config.top_k)
        min_val = top_logits[:, -1:]
        last_token_logits = torch.where(
            last_token_logits < min_val, torch.tensor(float("-inf")), last_token_logits
        )

    # Step 5: Sample
    probs = torch.nn.functional.softmax(last_token_logits, dim=-1)
    next_token = torch.multinomial(probs, num_samples=1)

    return next_token.item(), state


def check_accuracy(
    config, state, forward_pass, ref_config, ref_state, ref_forward_pass, num_tokens
):
    """Teacher-forced comparison of forward_pass's logits against a reference.

    Both models are fed the reference's greedy token at every step, so a
    divergence at step N is the candidate's own error at step N rather than the
    consequence of an earlier different choice. Step 0 is prefill.

    Returns one (kl, top1) pair per step: KL(reference || candidate) of the
    next-token distributions, and whether both rank the same token first.
    """
    ref_state.token_ids = state.token_ids
    results = []
    for step in range(num_tokens):
        logits, state = forward_pass(config, state)
        ref_logits, ref_state = ref_forward_pass(ref_config, ref_state)
        cand = torch.log_softmax(logits[0, -1].float(), dim=0)
        ref = torch.log_softmax(ref_logits[0, -1].float(), dim=0)
        kl = torch.sum(ref.exp() * (ref - cand)).item()
        next_token = int(ref.argmax())
        top1 = int(cand.argmax()) == next_token
        results.append((kl, top1))
        print(f"step {step:3d}  KL {kl:.5f}  top-1 {'match' if top1 else 'MISMATCH'}")
        state.token_ids = torch.tensor([[next_token]], dtype=torch.long)
        ref_state.token_ids = state.token_ids
    return results


def check_determinism(config, prompts, forward_pass, num_tokens, rounds):
    """Run each prompt `rounds` times, alternating, and compare logits bitwise.

    Each round prefills from a fresh state and decodes greedily. Alternating
    prompts with different text matters: a host write that never reaches the
    device then reads the other prompt's data, not a leftover copy of its own.
    Returns how many rounds differ from the first round of the same prompt.
    """
    first = [None] * len(prompts)
    n_differ = 0
    for r in range(rounds * len(prompts)):
        p = r % len(prompts)
        state = LlamaModelState(config)
        state.token_ids = prompts[p]
        logits = []
        for _ in range(num_tokens):
            out, state = forward_pass(config, state)
            logits.append(out[0, -1].clone())
            state.token_ids = out[:, -1:].argmax(dim=-1)
        logits = torch.stack(logits).view(torch.int16)
        if first[p] is None:
            first[p] = logits
            continue
        steps = (logits != first[p]).any(dim=1).nonzero().flatten().tolist()
        if steps:
            n_differ += 1
            print(f"round {r} (prompt {p}): logits differ at steps {steps}")
    return n_differ


def parse_args():
    parser = argparse.ArgumentParser(description="LLaMA 3.2 1B Inference Harness")
    parser.add_argument(
        "weights_path", type=str, help="Path to the model weights (safetensors file)"
    )
    parser.add_argument(
        "tokenizer_path", type=str, help="Path to the tokenizer model (tiktoken file)"
    )
    parser.add_argument(
        "--prompt-len",
        type=int,
        default=2048,
        help="Length of the input prompt in tokens (default: 2048)",
    )
    parser.add_argument(
        "--num-tokens",
        type=int,
        default=40,
        help="Number of tokens to generate (default: 40)",
    )
    parser.add_argument(
        "--check-accuracy",
        action="store_true",
        help="Instead of sampling, compare each step's logits against an fp32 CPU "
        "reference, feeding both the reference's greedy token",
    )
    parser.add_argument(
        "--check-determinism",
        type=int,
        metavar="ROUNDS",
        help="Instead of sampling, run two prompts ROUNDS times each, alternating, "
        "and count the runs whose logits differ bitwise from the first run",
    )
    return parser.parse_args()


def get_prompt(prompt_len):
    with open(Path(__file__).parent / "prompt.txt", "r") as f:
        prompt = f.read()
    prompt = prompt[:prompt_len]
    return prompt


def init(
    weights_path,
    tokenizer_path,
    prompt="The capital of France is ",
):
    config = LlamaConfig(weights_path, tokenizer_path)
    state = LlamaModelState(config)

    seed = 1608560892
    torch.manual_seed(seed)

    # Tokenize prompt
    prompt_token_ids = [config.special_tokens["<|begin_of_text|>"]]
    prompt_token_ids += config.tokenizer.encode(prompt)
    assert (
        len(prompt_token_ids) <= config.context_length
    ), f"Prompt length ({len(prompt_token_ids)} tokens) exceeds model context length ({config.context_length})"
    prompt_token_ids = torch.tensor([prompt_token_ids], dtype=torch.long)

    state.token_ids = prompt_token_ids

    return config, state


def generate(config, state, forward_pass, num_tokens=100, use_kv_cache=True):
    # Generate tokens
    # First token (prefill)
    n_tokens_generated = 0
    t_prefill_start = time.perf_counter()
    first_token, state = generate_token(config, forward_pass, state)
    token_text = config.tokenizer.decode([first_token])
    n_tokens_generated += 1
    print(token_text, end="", flush=True)
    t_prefill_stop = time.perf_counter()

    # Remaining tokens (decode)
    if use_kv_cache:
        state.token_ids = torch.tensor([[first_token]], dtype=torch.long)
    else:
        state.reset_kv_cache(config)
        state.token_ids = torch.cat(
            [state.token_ids, torch.tensor([[first_token]], dtype=torch.long)], dim=1
        )
    t_decode_start = time.perf_counter()
    for _ in range(num_tokens - 1):
        next_token, state = generate_token(config, forward_pass, state)
        token_text = config.tokenizer.decode([next_token])
        n_tokens_generated += 1
        print(token_text, end="", flush=True)
        if use_kv_cache:
            state.token_ids = torch.tensor([[next_token]], dtype=torch.long)
        else:
            state.reset_kv_cache(config)
            state.token_ids = torch.cat(
                [state.token_ids, torch.tensor([[next_token]], dtype=torch.long)], dim=1
            )
    t_decode_end = time.perf_counter()

    t_prefill = t_prefill_stop - t_prefill_start
    t_decode = t_decode_end - t_decode_start
    sys.stderr.write("\n\n=== Performance Statistics ===\n")
    sys.stderr.write(f"[Prefill] Time to first token:   {t_prefill:7.3f} s\n")
    if n_tokens_generated > 1:
        sys.stderr.write(
            f"[Decode]  Time per token (mean): {t_decode / (n_tokens_generated - 1):7.3f} s\n"
        )
        sys.stderr.write(
            f"[Decode]  Tokens per second:     {(n_tokens_generated - 1) / t_decode:7.3f}\n"
        )
    sys.stderr.write(
        f"[Total]   Time per token (mean): {(t_prefill + t_decode) / n_tokens_generated:7.3f} s\n"
    )
    sys.stderr.write(
        f"[Total]   Tokens per second:     {n_tokens_generated / (t_prefill + t_decode):7.3f}\n"
    )
