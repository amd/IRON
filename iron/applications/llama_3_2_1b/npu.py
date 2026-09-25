# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B on the NPU: the prefill and decode graphs as two fused images."""

import logging

import numpy as np
import torch
from ml_dtypes import bfloat16

from . import harness
from .graphs import DecodeGraph, PrefillGraph, _np, _torch

max_seq_len = 2048

npu = None


class AIELlama:
    """Both phases as fused images over one set of weights and caches.

    The prefill image runs the prompt at ``max_seq_len`` and writes the
    caches in the layout the decode image reads; ``prefill_to_decode``
    hands them over. Each image owns a copy of the weights it reads.
    """

    def __init__(self, config):
        self.decode_graph = DecodeGraph(config, max_seq_len)
        self.decode = self.decode_graph.compile(config).load()
        self.prefill_graph = PrefillGraph(config, self.decode_graph)
        self.prefill = self.prefill_graph.compile(config).load()

    def prefill_to_decode(self, config):
        graph = self.decode_graph
        for i in range(config.n_layers):
            for cache in (graph.keys[i], graph.values[i]):
                self.decode.write(cache, self.prefill.read(cache))


# Prefill
# ##########################################################################


def llama_forward_pass_prefill(config, state):
    batch, seq_len = state.token_ids.shape
    assert batch == 1 and 0 < seq_len <= max_seq_len
    # The prompt fills the first rows; the rest are never read (attention is
    # causal, and decode masks the cache's tail by its vector size).
    x = np.zeros((max_seq_len, config.emb_dim), dtype=bfloat16)
    x[:seq_len] = _np(
        torch.nn.functional.embedding(state.token_ids, config.model.out_head.weight)
    ).reshape(seq_len, config.emb_dim)
    # The last prompt row's logits only, selected by its element offset. The
    # harness samples and scores in torch, so the logits cross over here.
    logits = _torch(
        npu.prefill(
            x,
            _np(config.angles)[:max_seq_len],
            last=(seq_len - 1) * config.emb_dim,
        ).numpy()
    ).reshape(1, 1, config.vocab_size)
    npu.prefill_to_decode(config)
    return logits, state


# Decode
# ##########################################################################


def llama_forward_pass_decode(config, state):
    batch, seq_len = state.token_ids.shape
    assert seq_len == 1
    assert state.num_preceding_tokens < max_seq_len

    context_len = state.num_preceding_tokens + 1
    cache_offset = state.num_preceding_tokens * config.head_dim
    # The softmax's valid row length is the context length: the kernel masks
    # every column from there on before the softmax, so the cache's unwritten
    # tail contributes nothing. It used to be written as a running sum of
    # context lengths, which iron/tests/common/llama_reference.py shows
    # drifting from the CPU reference from the second token on (§18).

    angles = _np(config.angles)[
        state.num_preceding_tokens : state.num_preceding_tokens + seq_len
    ]
    # Token embedding (on CPU)
    x = _np(
        torch.nn.functional.embedding(state.token_ids, config.model.out_head.weight)
    )

    logits = _torch(
        npu.decode(
            x.reshape(1, config.emb_dim),
            angles.reshape(1, config.head_dim),
            cache_offset=cache_offset,
            vector_size=context_len,
        ).numpy()
    ).reshape(1, 1, config.vocab_size)
    return logits, state


# Main
# ##########################################################################


def llama_forward_pass(config, state):
    batch, seq_len = state.token_ids.shape
    if seq_len > 1:
        ret = llama_forward_pass_prefill(config, state)
        state.num_preceding_tokens = state.token_ids.shape[1]
        return ret
    else:
        ret = llama_forward_pass_decode(config, state)
        state.num_preceding_tokens += 1
        return ret


def main():
    global npu
    logging.basicConfig(level=logging.DEBUG)
    args = harness.parse_args()

    assert (
        max_seq_len >= args.prompt_len + args.num_tokens
    ), "max_seq_len must be at least prompt_len + num_tokens"

    prompt = harness.get_prompt(args.prompt_len)

    config, state = harness.init(args.weights_path, args.tokenizer_path, prompt=prompt)

    npu = AIELlama(config)

    if args.check_accuracy:
        results = harness.check_accuracy(
            config,
            state,
            llama_forward_pass,
            config,
            harness.LlamaModelState(config),
            harness.ReferenceForward(config),
            args.num_tokens,
        )
        kl = [k for k, _ in results]
        print(f"[Accuracy] Prefill KL: {kl[0]:.6f}")
        if len(kl) > 1:
            print(f"[Accuracy] Decode max KL: {max(kl[1:]):.6f}")
        print(f"[Accuracy] Top-1 mismatches: {sum(not t for _, t in results)}")
        return

    if args.check_determinism:
        # The second prompt is the same amount of the text that follows.
        other = harness.get_prompt(2 * args.prompt_len)[args.prompt_len :]
        other_ids = [config.special_tokens["<|begin_of_text|>"]]
        other_ids += config.tokenizer.encode(other)
        prompts = [state.token_ids, torch.tensor([other_ids], dtype=torch.long)]
        n_differ = harness.check_determinism(
            config, prompts, llama_forward_pass, args.num_tokens, args.check_determinism
        )
        n_compared = len(prompts) * (args.check_determinism - 1)
        print(f"[Determinism] Differing runs: {n_differ}/{n_compared}")
        return

    print(prompt, end="", flush=True)
    harness.generate(config, state, llama_forward_pass, num_tokens=args.num_tokens)


if __name__ == "__main__":
    main()
