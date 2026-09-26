# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B on the NPU: one graph function, one image per input shape.

The prompt and each decode step are calls of the one ``forward``
(:class:`.graphs.LlamaGraph`) at two shapes: a prompt runs padded to
``max_seq_len`` rows, a decode step at one row. Every version shares the function's scratch arena, so
the weights are uploaded once and the caches a prompt writes are the caches
decode reads.

Generation runs one of two ways. By default the host calls each step and
draws each token from the logits it returns. With ``--device-loop``
(:class:`DeviceGeneration`) the device draws them: the prompt starts the
first decode step and each step the next, the host only restarting runs, and
the text is the same token for token (``--compare-host`` checks it).

No torch: the weights are the mapped checkpoint, the prompt's embedding a
numpy gather (a decode step gathers its token's row on the device), the
logits numpy. The accuracy check, which needs the torch CPU
reference, is its own entry point (:mod:`.accuracy`).
"""

from __future__ import annotations

import dataclasses
import logging
import time
from collections.abc import Callable
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

import iron
from aie.iron.kernels.sample import ROW_WORDS
from iron.common.graph.compiled import CompiledGraph
from iron.common.graph.narrowing import CostTable, JointNarrowing

from . import harness
from .graphs import LlamaGraph
from .sampling import Sampler

MAX_SEQ_LEN = 2048


class AIELlama:
    """The model as one graph function called at the prompt's and a token's shape.

    ``forward_graph`` is that function -- a compiled
    :class:`~iron.common.graph.compiled.GraphFunction`, or anything called
    the same way and returning a buffer with ``numpy()``. :meth:`forward`
    is the ``forward_pass`` the harness calls.
    """

    def __init__(
        self,
        config,
        forward_graph: Callable,
        max_seq_len: int,
        device: DeviceGeneration | None = None,
    ):
        self.config = config
        self.forward_graph = forward_graph
        self.max_seq_len = max_seq_len
        # The same images, looped on the device; None where there is none.
        self.device = device

    @classmethod
    def compile(
        cls, config, max_seq_len=MAX_SEQ_LEN, cost_table: Path | None = None
    ) -> "AIELlama":
        """Trace, compile and load both versions, weights uploaded.

        Both before the first call, so the shared arena is made once at its
        final size. The checkpoint's pages are dropped a piece at a time as
        they reach the device, so the process holds at most one piece of it
        beside the buffers; the embedding's rows fault back in as it is read.
        With a ``cost_table`` the decode version's designs are narrowed and
        packed by it (:class:`~iron.common.graph.narrowing.JointNarrowing`).
        """
        model = LlamaGraph(config, max_seq_len)
        decode = model.compile(
            config,
            1,
            coresident=(
                None if cost_table is None else JointNarrowing(CostTable(cost_table))
            ),
        )
        if decode.tuning is not None:
            print("[Tuning] decode:\n" + decode.tuning.report(), flush=True)
        # A prompt's carried values start a decode step (see DeviceGeneration).
        prompt = model.compile(config, max_seq_len, feeds=decode)
        for version in (decode, prompt):
            version.load(release=config.weights.release)
        device = DeviceGeneration(config, model, prompt, decode)
        return cls(config, model.graph, max_seq_len, device)

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
        x = prompt_rows(config, token_ids, rows)
        # Every call passes every per-call value; a version reads the ones
        # its operators bind. A prompt reads the position of its last row,
        # whose logits are the only ones it computes.
        logits, _ = self.forward_graph(x, token=int(token_ids[-1]), position=n - 1)
        return logits.numpy()

    def _decode(self, token_id, position):
        assert position < self.max_seq_len
        # The graph derives the rest from the position: the cache row, and
        # the softmax's valid length, position + 1 (it used to be written as
        # a running sum of context lengths, which
        # iron/tests/common/llama_reference.py shows drifting from the CPU
        # reference from the second token on, §18). The token the device
        # drew, which the call also returns, is the host's to redraw.
        logits, _ = self.forward_graph(token=token_id, position=position)
        return logits.numpy()


def prompt_rows(config, token_ids, rows: int) -> np.ndarray:
    """A prompt's embedded tokens, ``(rows, emb_dim)``: the prompt fills the
    first rows and the rest are never read (attention is causal, and decode
    masks the cache's tail by its vector size)."""
    x = np.zeros((rows, config.emb_dim), dtype=bfloat16)
    x[: token_ids.shape[0]] = config.weights.embed(token_ids)
    return x


@dataclasses.dataclass(frozen=True)
class Generated:
    """What a generation produced: the token ids, and how long the prompt's
    first token and the rest took, in seconds."""

    tokens: list[int]
    t_prefill: float
    t_decode: float


class DeviceGeneration:
    """Generation with the host out of the loop.

    The prompt runs once, host-seeded; its carried values -- the token it
    drew and the position after it -- start the first decode step, and each
    step starts the next (:class:`~iron.common.graph.carried.CarriedLoop`).
    Every draw is the device's, from a row the host wrote before the prompt
    (:meth:`.sampling.Sampler.rows`), so a sampler seeded as the host loop's
    draws the same tokens from the same logits.
    """

    def __init__(
        self,
        config,
        model: LlamaGraph,
        prompt: CompiledGraph,
        decode: CompiledGraph,
        depth: int = 2,
    ):
        self.config = config
        self.model = model
        self.prompt = prompt
        self.decode = decode
        self.loop = iron.CarriedLoop(prompt, decode, depth)

    def generate(
        self, token_ids: np.ndarray, num_tokens: int, sampler: Sampler
    ) -> Generated:
        """``num_tokens`` tokens after the prompt ``token_ids`` (1-D)."""
        model, n = self.model, token_ids.shape[0]
        if n + num_tokens > model.max_seq_len + 1:
            raise ValueError(
                f"{n} prompt tokens and {num_tokens} generated exceed the "
                f"{model.max_seq_len} positions"
            )
        # The prompt draws at its last position, n - 1; step k at n + k.
        draws = np.zeros((model.max_seq_len, ROW_WORDS), dtype=np.int32)
        draws[n - 1 : n - 1 + num_tokens] = sampler.rows(num_tokens, model.k_max)
        self.decode.write(model.draws, draws)
        x = prompt_rows(self.config, token_ids, model.max_seq_len)
        t0 = time.perf_counter()
        self.loop.start(x, token=int(token_ids[-1]), position=n - 1)
        t1 = time.perf_counter()
        for _ in self.loop.steps(num_tokens - 1):
            pass
        t2 = time.perf_counter()
        tokens = self.decode.read(model.tokens)[n - 1 : n - 1 + num_tokens]
        return Generated([int(t) for t in tokens], t1 - t0, t2 - t1)


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
    return config, state, prompt, AIELlama.compile(config, cost_table=args.cost_table)


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
    parser.add_argument(
        "--device-loop",
        action="store_true",
        help="Draw every token on the device, each decode step started by the "
        "one before it, rather than on the host from the logits of each step",
    )
    parser.add_argument(
        "--compare-host",
        action="store_true",
        help="With --device-loop, then generate again on the host from the same "
        "seed and count the tokens that differ",
    )
    args = parser.parse_args()
    if args.compare_host and not args.device_loop:
        parser.error("--compare-host compares the --device-loop run")
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
    if not args.device_loop:
        harness.generate(config, state, npu.forward, num_tokens=args.num_tokens)
        return

    sampler = Sampler(
        config.temperature, config.top_k, np.random.default_rng(harness.SEED)
    )
    run = npu.device.generate(state.token_ids[0], args.num_tokens, sampler)
    print(config.tokenizer.decode(run.tokens), end="", flush=True)
    harness.report(run.t_prefill, run.t_decode, args.num_tokens)
    if args.compare_host:
        print("\n\n[Host loop]\n" + prompt, end="", flush=True)
        host = harness.generate(config, state, npu.forward, num_tokens=args.num_tokens)
        differ = sum(a != b for a, b in zip(run.tokens, host))
        print(
            f"\n[DeviceLoop] Tokens differing from the host loop: {differ}/{len(host)}"
        )


if __name__ == "__main__":
    main()
