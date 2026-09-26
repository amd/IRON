# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B on the NPU: the prefill and decode graphs as two fused images.

No torch: the weights are the mapped checkpoint, the embedding a numpy
gather, the logits numpy. The accuracy check, which needs the torch CPU
reference, is its own entry point (:mod:`.accuracy`).
"""

import logging

import numpy as np
from ml_dtypes import bfloat16

from . import harness
from .graphs import DecodeGraph, PrefillGraph

MAX_SEQ_LEN = 2048


class AIELlama:
    """Both phases as fused images over one set of weights and caches.

    The prefill image runs the prompt at ``max_seq_len`` and writes the
    caches in the layout the decode image reads; ``prefill_to_decode``
    hands them over. Each image owns a copy of the weights it reads.

    ``decode`` and ``prefill`` are the compiled images (:meth:`compile`
    builds them); :meth:`forward` is the ``forward_pass`` the harness calls.
    """

    def __init__(self, config, decode_graph, decode, prefill, max_seq_len):
        self.config = config
        self.decode_graph = decode_graph
        self.decode = decode
        self.prefill = prefill
        self.max_seq_len = max_seq_len

    @classmethod
    def compile(cls, config, max_seq_len=MAX_SEQ_LEN) -> "AIELlama":
        """Trace, compile and load both images, weights uploaded."""
        decode_graph = DecodeGraph(config, max_seq_len)
        decode = decode_graph.compile(config).load()
        prefill = PrefillGraph(config, decode_graph).compile(config).load()
        return cls(config, decode_graph, decode, prefill, max_seq_len)

    def prefill_to_decode(self):
        graph = self.decode_graph
        for cache in (*graph.keys, *graph.values):
            self.decode.write(cache, self.prefill.read(cache))

    # -- the forward pass ----------------------------------------------------

    def forward(self, config, state):
        """``state.token_ids`` through the model; the logits after the last, ``(1, 1, vocab)``."""
        batch, seq_len = state.token_ids.shape
        assert batch == 1
        if seq_len > 1:
            logits = self._prefill(state.token_ids[0])
            state.num_preceding_tokens = seq_len
        else:
            logits = self._decode(
                int(state.token_ids[0, 0]), state.num_preceding_tokens
            )
            state.num_preceding_tokens += 1
        # A copy: the image's output buffer is rewritten by the next call.
        return np.array(logits).reshape(1, 1, config.vocab_size), state

    def _prefill(self, token_ids):
        config, L = self.config, self.max_seq_len
        n = token_ids.shape[0]
        assert 0 < n <= L
        # The prompt fills the first rows; the rest are never read (attention is
        # causal, and decode masks the cache's tail by its vector size).
        x = np.zeros((L, config.emb_dim), dtype=bfloat16)
        x[:n] = config.weights.embed(token_ids)
        # The last prompt row's logits only, selected by its element offset.
        logits = self.prefill(
            x, config.angles[:L], last=(n - 1) * config.emb_dim
        ).numpy()
        self.prefill_to_decode()
        return logits

    def _decode(self, token_id, position):
        config = self.config
        assert position < self.max_seq_len
        # The softmax's valid row length is the context length: the kernel masks
        # every column from there on before the softmax, so the cache's unwritten
        # tail contributes nothing. It used to be written as a running sum of
        # context lengths, which iron/tests/common/llama_reference.py shows
        # drifting from the CPU reference from the second token on (§18).
        return self.decode(
            config.weights.embed([token_id]).reshape(1, config.emb_dim),
            config.angles[position : position + 1],
            cache_offset=position * config.head_dim,
            vector_size=position + 1,
        ).numpy()


# Main
# ##########################################################################


def setup(args):
    """The config, the prompt's state and the compiled model, from the arguments."""
    assert (
        MAX_SEQ_LEN >= args.prompt_len + args.num_tokens
    ), "MAX_SEQ_LEN must be at least prompt_len + num_tokens"
    prompt = harness.get_prompt(args.prompt_len)
    config, state = harness.init(args.weights_path, args.tokenizer_path, prompt=prompt)
    return config, state, prompt, AIELlama.compile(config)


def main():
    logging.basicConfig(level=logging.DEBUG)
    parser = harness.argument_parser()
    parser.add_argument(
        "--check-determinism",
        type=int,
        metavar="ROUNDS",
        help="Instead of sampling, run two prompts ROUNDS times each, alternating, "
        "and count the runs whose logits differ bitwise from the first run",
    )
    args = parser.parse_args()
    config, state, prompt, npu = setup(args)

    if args.check_determinism:
        # The second prompt is the same amount of the text that follows.
        other = harness.get_prompt(2 * args.prompt_len)[args.prompt_len :]
        other_ids = [config.special_tokens["<|begin_of_text|>"]]
        other_ids += config.tokenizer.encode(other)
        prompts = [state.token_ids, np.array([other_ids], dtype=np.int64)]
        n_differ = harness.check_determinism(
            config, prompts, npu.forward, args.num_tokens, args.check_determinism
        )
        n_compared = len(prompts) * (args.check_determinism - 1)
        print(f"[Determinism] Differing runs: {n_differ}/{n_compared}")
        return

    print(prompt, end="", flush=True)
    harness.generate(config, state, npu.forward, num_tokens=args.num_tokens)


if __name__ == "__main__":
    main()
