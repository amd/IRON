# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B on the NPU: one graph function, one image per input shape.

The prompt and each decode step are calls of the one ``forward``
(:class:`.graphs.LlamaGraph`) at two shapes: a prompt in the
``max_seq_len``-row version, bounded per call to the rows it needs, a
decode step at one row. Every version shares the function's scratch arena,
so the weights are uploaded once and the caches a prompt writes are the
caches decode reads.

No torch: the weights are the mapped checkpoint, the embedding a numpy
gather, the logits numpy. The accuracy check, which needs the torch CPU
reference, is its own entry point (:mod:`.accuracy`).
"""

import logging
from collections.abc import Callable

import numpy as np
from ml_dtypes import bfloat16

from . import harness
from .graphs import LlamaGraph, prompt_rows

MAX_SEQ_LEN = 2048


class AIELlama:
    """The model as one graph function called at the prompt's and a token's shape.

    ``forward_graph`` is that function -- a compiled
    :class:`~iron.common.graph.compiled.GraphFunction`, or anything called
    the same way and returning a buffer with ``numpy()``. :meth:`forward`
    is the ``forward_pass`` the harness calls.
    """

    def __init__(self, config, forward_graph: Callable, max_seq_len: int):
        self.config = config
        self.forward_graph = forward_graph
        self.max_seq_len = max_seq_len
        # The RoPE table as the images read it, as far as they reach. A
        # float32 table would be another input signature, and so another
        # compile.
        self.angles = config.angles[:max_seq_len].astype(bfloat16)

    @classmethod
    def compile(cls, config, max_seq_len=MAX_SEQ_LEN) -> "AIELlama":
        """Trace, compile and load both versions, weights uploaded.

        Both before the first call, so the shared arena is made once at its
        final size. The checkpoint's pages are dropped a piece at a time as
        they reach the device, so the process holds at most one piece of it
        beside the buffers; the embedding's rows fault back in as it is read.
        """
        model = LlamaGraph(config, max_seq_len)
        for rows in (1, max_seq_len):
            model.compile(config, rows)
        for version in model.graph.versions.values():
            version.load(release=config.weights.release)
        return cls(config, model.graph, max_seq_len)

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
        config, rows = self.config, self.max_seq_len
        n = token_ids.shape[0]
        assert 0 < n <= rows
        # The prompt fills the first rows; the rest are never read (attention is
        # causal, and decode masks the cache's tail by its vector size).
        x = np.zeros((rows, config.emb_dim), dtype=bfloat16)
        x[:n] = config.weights.embed(token_ids)
        # Every call passes every per-call value; a version reads the ones
        # its operators bind. Here: the rows the prompt runs at, its true
        # length for the masks, and the last prompt row's logits, selected
        # by its row.
        return self.forward_graph(
            x,
            self.angles[:rows],
            rows=prompt_rows(n, rows),
            cache_offset=0,
            vector_size=n,
            last=n - 1,
        ).numpy()

    def _decode(self, token_id, position):
        config = self.config
        assert position < self.max_seq_len
        # The softmax's valid row length is the context length: the kernel masks
        # every column from there on before the softmax, so the cache's unwritten
        # tail contributes nothing. A running sum of context lengths is wrong
        # here: iron/tests/common/llama_reference.py shows it drifting from
        # the CPU reference from the second token on.
        return self.forward_graph(
            config.weights.embed([token_id]).reshape(1, config.emb_dim),
            self.angles[position : position + 1],
            rows=1,
            cache_offset=position,
            vector_size=position + 1,
            last=0,
        ).numpy()


# Main
# ##########################################################################


def setup(args):
    """The config, the prompt's state and the compiled model, from the arguments."""
    prompt = harness.get_prompt(args.prompt_len)
    config, state = harness.init(args.weights_path, args.tokenizer_path, prompt=prompt)
    # --prompt-len counts characters; the rows are tokens, known only now.
    n_prompt = state.token_ids.shape[1]
    if n_prompt + args.num_tokens > MAX_SEQ_LEN:
        raise ValueError(
            f"a {n_prompt}-token prompt and {args.num_tokens} generated tokens "
            f"exceed the model's {MAX_SEQ_LEN} rows"
        )
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
