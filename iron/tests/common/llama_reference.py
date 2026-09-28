# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The graph's reference against the model's plain forward pass.

``Llama.oracle`` (``LlamaOracle``) is a stateless causal pass in float32
numpy, the oracle the NPU application is judged against. ``Llama`` is the same
computation as one graph, called at a prompt's shape and at one token's,
and ``Graph.reference`` runs it operator by operator through each
``reference()`` on host tensors, with the per-call values modelled (the
chunk and the position move the cache writes and bound the attention, the
last prompt row selects the logits) and the caches as state. :class:`OnHost` is
the model with its images stood in by that reference, so the two can be
compared without a device, through the application's own ``logits``:
that checks the graph's wiring (layouts, reshapes, the scale, the repeat,
the transposes, the caches the prompt leaves for decode) against the model,
leaving only the kernels' arithmetic for hardware.

The oracle needs no cache: the logits at position ``t`` of a causal pass
over ``t + 1`` tokens are what a cached decode produces at step ``t``. The
graph computes in bfloat16 and the oracle in float32, so the logits agree
to bf16 tolerance and the argmax exactly.
"""

import dataclasses
from types import SimpleNamespace

import numpy as np
import pytest

from iron.lm import Config, Oracle, accuracy, determinism, greedy
from iron.lm.llama3.model import Llama
from iron.tests.common.llama_model import PROFILE, SMALL, random_weights


class _Output:
    """What an image returns: a buffer read with ``numpy()``."""

    def __init__(self, array):
        self.array = array

    def numpy(self):
        return self.array


class OnHost(Llama):
    """The model with its images stood in by its reference, which runs at
    whatever shape it is called with.
    """

    profile = PROFILE

    def __call__(self, *tensors, **values):
        return _Output(self.reference(*tensors, **values))


@dataclasses.dataclass
class Case:
    config: Config
    weights: SimpleNamespace
    oracle: Oracle
    prompt: np.ndarray
    first: np.ndarray
    expected: list


@pytest.fixture(scope="module")
def cpu():
    """The config, its weights, the oracle, a prompt, the oracle's logits
    for it and six greedy tokens' logits.
    """
    config = SMALL
    weights = random_weights(config)
    oracle = Llama.oracle(config, weights)
    prompt = np.random.default_rng(1).integers(0, config.vocab_size, 8)
    tokens, expected = prompt, []
    first = logits = oracle.logits(tokens)
    for _ in range(6):
        tokens = np.append(tokens, logits.argmax())
        logits = oracle.logits(tokens)
        expected.append(logits)
    return Case(config, weights, oracle, prompt, first, expected)


def _greedy(model, tokens, logits, n):
    """The logits of ``n`` greedy decode steps after ``tokens``, whose own
    are ``logits``.
    """
    history, out = list(tokens), []
    for _ in range(n):
        history.append(greedy(logits))
        logits = model.logits(history)
        out.append(logits)
    return out


def _assert_close(got, expected):
    for step, (a, b) in enumerate(zip(got, expected)):
        a = np.asarray(a, dtype=np.float32)
        scale = np.abs(b).max()
        err = np.abs(a - b).max()
        assert (
            err <= 0.05 * scale
        ), f"step {step}: max |diff| {err:.4f} against |logits| {scale:.3f}"
        assert (
            a.argmax() == b.argmax()
        ), f"step {step}: argmax {a.argmax()} != {b.argmax()}"


def test_decode_from_an_empty_cache_matches_the_forward_token_by_token(cpu):
    """One token at a time only: the prompt fed a token at a time from an
    empty cache, then the generated tokens.
    """
    model = OnHost(cpu.config, cpu.weights)
    last = model.logits(cpu.prompt[:1])
    for n in range(2, len(cpu.prompt) + 1):
        last = model.logits(cpu.prompt[:n])
    _assert_close([last], [cpu.first])
    got = _greedy(model, cpu.prompt, last, len(cpu.expected))
    _assert_close(got, cpu.expected)


def test_the_prompt_matches_the_forward_and_leaves_decode_its_caches(cpu):
    """The prompt at its own rows: the padding rows are masked and past the
    prompt in the caches, and decode continues from the caches it wrote.
    """
    model = OnHost(cpu.config, cpu.weights)
    first = model.logits(cpu.prompt)
    _assert_close([first], [cpu.first])
    got = _greedy(model, cpu.prompt, first, len(cpu.expected))
    _assert_close(got, cpu.expected)


def test_a_prompt_longer_than_a_chunk_runs_in_chunks(cpu):
    """A prompt of several chunks, each attending over the caches the ones
    before it wrote, then a decode step, then a turn of several tokens,
    which reruns only the chunk holding its first token onwards.
    """
    config = dataclasses.replace(cpu.config, max_seq_len=4 * cpu.config.prefill_chunk)
    model = OnHost(config, cpu.weights)
    oracle = Llama.oracle(config, cpu.weights)
    tokens = np.random.default_rng(3).integers(0, config.vocab_size, 150)
    first = oracle.logits(tokens)
    _assert_close([model.logits(tokens)], [first])
    tokens = np.append(tokens, first.argmax())
    _assert_close([model.logits(tokens)], [oracle.logits(tokens)])
    tokens = np.append(tokens, np.random.default_rng(4).integers(0, 1024, 30))
    _assert_close([model.logits(tokens)], [oracle.logits(tokens)])


def test_the_accuracy_check_scores_the_model_against_the_reference(cpu):
    """What ``--check-accuracy`` runs, the images stood in by the graph's
    reference: the model against the float32 reference, teacher-forced.
    """
    model = OnHost(cpu.config, cpu.weights)
    steps = len(cpu.expected) + 1
    results = accuracy(model, cpu.oracle, cpu.prompt, steps)
    assert all(top1 for _, top1 in results), results
    # bf16 graphs against a float32 forward: close, not equal.
    assert all(0 <= kl < 0.05 for kl, _ in results), results
    assert any(kl > 0 for kl, _ in results), results


def test_the_determinism_check_finds_the_reference_deterministic(cpu):
    """What ``--check-determinism`` runs: two prompts, alternated, each
    rerun from a prefill; no run differs from the first.
    """
    model = OnHost(cpu.config, cpu.weights)
    prompts = [cpu.prompt, cpu.prompt[::-1]]
    assert determinism(model, prompts, 3, 3) == 0


def test_a_short_prompt_runs_at_its_own_rows():
    """A context longer than a chunk: the prompt runs its own rows of one
    chunk, not the context, and its logits are the oracle's; decode
    continues from the caches it wrote.
    """
    config = dataclasses.replace(SMALL, max_seq_len=1024)
    weights = random_weights(config)
    model, oracle = OnHost(config, weights), Llama.oracle(config, weights)
    prompt = np.random.default_rng(2).integers(0, config.vocab_size, 8)
    first = oracle.logits(prompt)
    _assert_close([model.logits(prompt)], [first])
    tokens = np.append(prompt, first.argmax())
    _assert_close([model.logits(tokens)], [oracle.logits(tokens)])
