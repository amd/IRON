#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B on the NPU: the prefill and decode graphs as two fused images."""

import logging
import sys
from pathlib import Path

import torch

import llama_inference_harness as harness

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))

from iron.common.context import AIEContext  # noqa: E402
from iron.models.llama_graphs import DecodeGraph, PrefillGraph  # noqa: E402

max_seq_len = 2048

npu = None


class AIELlama:
    """Both phases as fused images over one set of weights and caches.

    The prefill image runs the prompt at ``max_seq_len`` and writes the
    caches in the layout the decode image reads; ``prefill_to_decode``
    hands them over. Each image owns a copy of the weights it reads.
    """

    def __init__(self, config):
        context = AIEContext(build_dir="build_elf")
        self.decode_graph = DecodeGraph(config, max_seq_len)
        self.decode = self.decode_graph.compile(config, context=context)
        self.prefill_graph = PrefillGraph(config, self.decode_graph)
        self.prefill = self.prefill_graph.compile(config, context=context)

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
    x = torch.zeros(max_seq_len, config.emb_dim, dtype=torch.bfloat16)
    x[:seq_len] = torch.nn.functional.embedding(
        state.token_ids, config.model.out_head.weight
    ).reshape(seq_len, config.emb_dim)
    # The last prompt row's logits only, selected by its element offset.
    logits = (
        npu.prefill(
            x,
            config.angles[:max_seq_len],
            last=(seq_len - 1) * config.emb_dim,
        )
        .to_torch()
        .view(1, 1, config.vocab_size)
    )
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

    angles = config.angles[
        state.num_preceding_tokens : state.num_preceding_tokens + seq_len
    ]
    # Token embedding (on CPU)
    x = torch.nn.functional.embedding(state.token_ids, config.model.out_head.weight)

    logits = (
        npu.decode(
            x.reshape(1, config.emb_dim),
            angles.reshape(1, config.head_dim),
            cache_offset=cache_offset,
            vector_size=context_len,
        )
        .to_torch()
        .view(1, 1, config.vocab_size)
    )
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

    assert max_seq_len >= args.prompt_len + args.num_tokens, (
        "max_seq_len must be at least prompt_len + num_tokens"
    )

    prompt = harness.get_prompt(args.prompt_len)

    config, state = harness.init(args.weights_path, args.tokenizer_path, prompt=prompt)

    npu = AIELlama(config)

    print(prompt, end="", flush=True)
    harness.generate(config, state, llama_forward_pass, num_tokens=args.num_tokens)


if __name__ == "__main__":
    main()
