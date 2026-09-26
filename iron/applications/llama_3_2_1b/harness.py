#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Inference harness -- all the necessary code _other_ than the actual model (forward pass).
``init`` maps the weights, loads the tokenizer, builds the RoPE table and
tokenizes the prompt; ``generate`` runs the generation loop, calling the
given ``forward_pass(config, state)`` for the prompt and then per token, and
decodes and prints each token.

A forward pass takes the token ids as an ``int64`` array ``(1, n)`` and
returns the logits as an array ``(1, 1, vocab_size)``: numpy throughout, so
nothing here needs torch. Only the CPU reference does (:mod:`.reference`).
"""

import argparse
import sys
import time
from pathlib import Path

import numpy as np
import tiktoken
import tiktoken.load

from .sampling import Sampler
from .weights import Llama3RopeScaling, LlamaWeights, rope_angles

#: Seeds the sampler, so a run's text is reproducible.
SEED = 1608560892

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
        self.rope_scaling = Llama3RopeScaling(
            factor=32.0,
            low_freq_factor=1.0,
            high_freq_factor=4.0,
            original_max_position_embeddings=8192,
        )
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

        # Map the weights and load the tokenizer. The mapping is read as the
        # weights are uploaded, not here; the tree is strict about keys and
        # shapes, and _check_weights about this config, so a checkpoint that
        # disagrees with either fails here rather than at the first dispatch.
        self.weights = LlamaWeights.load(weights_path)
        self._check_weights()
        self.tokenizer = get_tokenizer(tokenizer_path, self.special_tokens)

        # The RoPE angle look-up table, float32; the NPU and the CPU reference
        # both read this one.
        self.angles = rope_angles(
            self.head_dim, self.context_length, self.rope_base, self.rope_scaling
        )

    def _check_weights(self):
        layer = self.weights.layers[0]
        found = {
            "n_layers": len(self.weights.layers),
            "vocab_size": self.weights.vocab_size,
            "emb_dim": self.weights.emb_dim,
            "n_heads * head_dim": layer.q.shape[0],
            "n_kv_groups * head_dim": layer.k.shape[0],
            "hidden_dim": layer.gate.shape[0],
        }
        expected = {
            "n_layers": self.n_layers,
            "vocab_size": self.vocab_size,
            "emb_dim": self.emb_dim,
            "n_heads * head_dim": self.n_heads * self.head_dim,
            "n_kv_groups * head_dim": self.n_kv_groups * self.head_dim,
            "hidden_dim": self.hidden_dim,
        }
        wrong = {k: (found[k], v) for k, v in expected.items() if found[k] != v}
        if wrong:
            raise ValueError(
                "checkpoint disagrees with the config: "
                + ", ".join(f"{k} is {f}, expected {e}" for k, (f, e) in wrong.items())
            )


class LlamaModelState:
    """What a forward pass is given: the tokens to run (the whole prompt for
    prefill, the latest token for decode) and how many came before them.
    The KV cache itself lives on the device.
    """

    def __init__(self, config):
        self.token_ids = np.empty((1, 0), dtype=np.int64)
        self.num_preceding_tokens = 0


# Utilities
# ##########################################################################


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


def generate_token(config, forward_pass, state, sampler):
    """Run one forward pass and draw the next token from its last logits."""
    logits, state = forward_pass(config, state)
    return sampler(logits[0, -1]), state


def _log_softmax(logits):
    x = np.asarray(logits, dtype=np.float64).reshape(-1)
    x = x - x.max()
    return x - np.log(np.exp(x).sum())


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
        cand = _log_softmax(logits[0, -1])
        ref = _log_softmax(ref_logits[0, -1])
        kl = float(np.sum(np.exp(ref) * (ref - cand)))
        next_token = int(ref.argmax())
        top1 = int(cand.argmax()) == next_token
        results.append((kl, top1))
        print(f"step {step:3d}  KL {kl:.5f}  top-1 {'match' if top1 else 'MISMATCH'}")
        state.token_ids = np.array([[next_token]], dtype=np.int64)
        ref_state.token_ids = state.token_ids
    return results


def check_determinism(config, prompts, forward_pass, num_tokens, rounds):
    """Run each prompt `rounds` times, alternating, and compare logits bitwise.

    Each round prefills from a fresh state and decodes greedily. Alternating
    prompts with different text matters: a host write that never reaches the
    device then reads the other prompt's data, not a leftover copy of its own.
    Returns how many rounds differ from the first round of the same prompt.
    """
    first: list[np.ndarray | None] = [None] * len(prompts)
    n_differ = 0
    for r in range(rounds * len(prompts)):
        p = r % len(prompts)
        state = LlamaModelState(config)
        state.token_ids = prompts[p]
        logits = []
        for _ in range(num_tokens):
            out, state = forward_pass(config, state)
            logits.append(np.array(out[0, -1]))
            state.token_ids = out[:, -1:].argmax(axis=-1).astype(np.int64)
        # Bitwise, as 16-bit words: bf16 logits, NaNs and signed zeros included.
        logits = np.stack(logits).view(np.int16)
        if first[p] is None:
            first[p] = logits
            continue
        steps = np.flatnonzero((logits != first[p]).any(axis=1)).tolist()
        if steps:
            n_differ += 1
            print(f"round {r} (prompt {p}): logits differ at steps {steps}")
    return n_differ


def argument_parser(description="LLaMA 3.2 1B Inference Harness"):
    """The arguments every entry point takes; each adds its own."""
    parser = argparse.ArgumentParser(description=description)
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
        help="Length of the input prompt, in characters of prompt.txt (default: 2048)",
    )
    parser.add_argument(
        "--num-tokens",
        type=int,
        default=40,
        help="Number of tokens to generate (default: 40)",
    )
    return parser


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

    # Tokenize prompt
    prompt_token_ids = [config.special_tokens["<|begin_of_text|>"]]
    prompt_token_ids += config.tokenizer.encode(prompt)
    assert (
        len(prompt_token_ids) <= config.context_length
    ), f"Prompt length ({len(prompt_token_ids)} tokens) exceeds model context length ({config.context_length})"
    prompt_token_ids = np.array([prompt_token_ids], dtype=np.int64)

    state.token_ids = prompt_token_ids

    return config, state


def generate(config, state, forward_pass, num_tokens=100, seed=SEED):
    sampler = Sampler(config.temperature, config.top_k, np.random.default_rng(seed))
    # Generate tokens
    # First token (prefill)
    n_tokens_generated = 0
    t_prefill_start = time.perf_counter()
    first_token, state = generate_token(config, forward_pass, state, sampler)
    token_text = config.tokenizer.decode([first_token])
    n_tokens_generated += 1
    print(token_text, end="", flush=True)
    t_prefill_stop = time.perf_counter()

    # Remaining tokens (decode)
    state.token_ids = np.array([[first_token]], dtype=np.int64)
    t_decode_start = time.perf_counter()
    for _ in range(num_tokens - 1):
        next_token, state = generate_token(config, forward_pass, state, sampler)
        token_text = config.tokenizer.decode([next_token])
        n_tokens_generated += 1
        print(token_text, end="", flush=True)
        state.token_ids = np.array([[next_token]], dtype=np.int64)
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
