# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The graph's reference against the model's plain forward pass.

``Llama.oracle`` (``LlamaOracle``) is a stateless causal pass in float32
numpy, the oracle the NPU application is judged against. ``Llama`` is the same
computation as one graph, called at a prompt's shape and at one token's,
and ``Graph.reference`` runs it operator by operator through each
``reference()`` on host tensors, with the per-call values modelled (the
chunk and the position move the cache writes and bound the attention, the
last prompt row selects the logits, a decode step gathers its token's row)
and the caches as state. ``OnHost`` is
the model with its images stood in by that reference, so the two can be
compared without a device, through the application's own ``logits``:
that checks the graph's wiring (layouts, reshapes, the head grouping,
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
from ml_dtypes import bfloat16

import iron
from iron.lm import (
    DecoderConfig,
    Oracle,
    Sampler,
    accuracy,
    determinism,
    generate_on_host,
)
from iron.lm.generation import greedy
from iron.applications.llama.model import Llama, LlamaOracle
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.rope import RoPE
from iron.tests.common.llama_model import PROFILE, SMALL, checkpoint

pytestmark = pytest.mark.usefixtures("npu2")  # MHA decode on any host


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
        logits, carry = self.reference(*tensors, **values)
        return _Output(logits), carry


@dataclasses.dataclass
class Case:
    config: DecoderConfig
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
    weights = checkpoint(config).tree("random")
    oracle = Llama.oracle(config, weights)
    # No greedy step of this prompt has a top-2 gap within bf16's resolution.
    prompt = np.random.default_rng(7).integers(0, config.vocab_size, 8)
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


@pytest.mark.parametrize("outside", [-1, SMALL.vocab_size])
def test_a_token_outside_the_vocabulary_is_refused_before_any_dispatch(cpu, outside):
    """A prompt that differs from the history in its first chunk and holds
    an id no row embeds in its second: refused whole, the caches and the
    history as the last call left them.
    """
    config = dataclasses.replace(cpu.config, prefill_chunk=64)
    model = OnHost(config, cpu.weights)
    tokens = np.random.default_rng(6).integers(0, config.vocab_size, 100)
    model.logits(tokens)
    broken = tokens.copy()
    broken[3] = (broken[3] + 1) % config.vocab_size
    broken[70] = outside
    with pytest.raises(IndexError, match=rf"\[{outside}\] are outside"):
        model.logits(broken)
    np.testing.assert_array_equal(model._seen, tokens)
    fresh = OnHost(config, cpu.weights).logits(tokens)
    np.testing.assert_array_equal(model.logits(tokens), fresh)


def test_a_model_runs_only_the_versions_it_loaded(cpu):
    """Before ``load()`` a call compiles nothing on its own: that would build
    an untuned version past the tuner and packaging ``load`` is given.
    """
    model = Llama(cpu.config, cpu.weights)
    with pytest.raises(RuntimeError, match=r"load\(\) first"):
        model.logits(cpu.prompt)
    with pytest.raises(RuntimeError, match=r"load\(\) first"):
        model(chunk=0, rows=1, token=0, position=0)
    assert not model._versions


def test_the_oracle_carries_nothing_from_call_to_call(cpu):
    """Its buffers outlive a call: a shorter prompt after a longer one, and
    each longer one after, gives a fresh oracle's logits bit for bit.
    """
    tokens = np.random.default_rng(5).integers(0, cpu.config.vocab_size, 40)
    for n in (20, 8, 21, 40):
        fresh = Llama.oracle(cpu.config, cpu.weights).logits(tokens[:n])
        assert np.array_equal(cpu.oracle.logits(tokens[:n]), fresh), n


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
    weights = checkpoint(config).tree("random")
    model, oracle = OnHost(config, weights), Llama.oracle(config, weights)
    prompt = np.random.default_rng(2).integers(0, config.vocab_size, 8)
    first = oracle.logits(prompt)
    _assert_close([model.logits(prompt)], [first])
    tokens = np.append(prompt, first.argmax())
    _assert_close([model.logits(tokens)], [oracle.logits(tokens)])


@pytest.mark.parametrize("temperature", [0.0, 0.7])
def test_the_carried_draws_are_the_host_loop_s_tokens(cpu, temperature):
    """What ``generate_on_host`` loops on the device, each call started from
    the last one's carry: from the same seed, the host loop's tokens. Every
    draw is the graph's own, from the rows the sampler gives it.
    """
    config, n, count = cpu.config, len(cpu.prompt), 6
    host = OnHost(config, cpu.weights)
    expected, _, _ = generate_on_host(
        host, cpu.prompt, count, Sampler(temperature, 40, np.random.default_rng(5))
    )
    model = OnHost(config, cpu.weights)
    draws = np.zeros(model.draws.shape, dtype=np.int32)
    sampler = Sampler(temperature, 40, np.random.default_rng(5))
    draws[n - 1 : n - 1 + count] = sampler.rows(count, k_max=64)
    model.draws.host = draws
    ((inputs, values),) = model._chunks(np.asarray(cpu.prompt), 0)
    _, carry = model(*inputs, **values)
    drawn = [carry["token"]]
    for _ in range(count - 1):
        _, carry = model(chunk=0, rows=1, **carry)
        drawn.append(carry["token"])
    assert drawn == expected


class Placed(OnHost):
    """``OnHost`` with no RoPE, its positions a held table's rows added to
    the embedding's.
    """

    def __init__(self, config, weights, table):
        super().__init__(config, weights)
        self.table = iron.weight(table)

    def positions(self, x, step):
        c = self.config
        L, C, E = c.max_seq_len, c.prefill_chunk, c.emb_dim
        if step.prompt:
            rows = Copy.step(self.table.reshape(L // C, C, E)[step.chunk, : step.rows])
        else:
            rows = Copy.step(self.table[step.position]).reshape(1, E)
        return ElementwiseAdd.step(x, rows)


class PlacedOracle(LlamaOracle):
    """``Placed``'s oracle."""

    def __init__(self, config, weights, table):
        super().__init__(config, weights)
        self.table = np.asarray(table, np.float32)

    def positions(self, x):
        return x + self.table[: x.shape[0]]


def test_a_decoder_without_rope_places_its_positions_through_the_hook(cpu):
    """No ``rope_base``: no table is held and nothing turns q and k; a
    model's ``positions`` adds its own rows instead, in each prompt chunk at
    the chunk's positions and in a decode step at its one, as its oracle's
    ``positions`` does.
    """
    config = dataclasses.replace(
        cpu.config, rope_base=None, max_seq_len=2 * cpu.config.prefill_chunk
    )
    assert config.angles() is None
    table = np.random.default_rng(9).standard_normal(
        (config.max_seq_len, config.emb_dim)
    )
    table = (table / 2).astype(bfloat16)
    model = Placed(config, cpu.weights, table)
    assert model.rope is None
    for shapes in model.shapes():
        steps = model.trace(**shapes).steps
        assert not any(isinstance(s.op, RoPE) for s in steps)
    oracle = PlacedOracle(config, cpu.weights, table)
    tokens = np.random.default_rng(10).integers(0, config.vocab_size, 300)
    first = oracle.logits(tokens)
    _assert_close([model.logits(tokens)], [first])
    tokens = np.append(tokens, first.argmax())
    _assert_close([model.logits(tokens)], [oracle.logits(tokens)])
    with pytest.raises(AssertionError):
        _assert_close(
            [model.logits(tokens)], [LlamaOracle(config, cpu.weights).logits(tokens)]
        )


def test_a_decoder_nested_in_its_checkpoint_is_read_where_it_is(cpu):
    """A checkpoint holding its decoder's embedding and layers under
    ``model.decoder``: ``decoder=`` reads them there, in the model and its
    oracle, and both give the flat checkpoint's logits bit for bit.
    """
    m = cpu.weights.model
    decoder = SimpleNamespace(embed_tokens=m.embed_tokens, layers=m.layers)
    nested = SimpleNamespace(
        model=SimpleNamespace(norm=m.norm, embed_tokens=m.embed_tokens, decoder=decoder)
    )
    model = OnHost(cpu.config, nested, decoder)
    assert model.layers is m.layers and model.decoder is decoder
    np.testing.assert_array_equal(
        model.logits(cpu.prompt), OnHost(cpu.config, cpu.weights).logits(cpu.prompt)
    )
    oracle = LlamaOracle(cpu.config, nested, decoder)
    np.testing.assert_array_equal(oracle.logits(cpu.prompt), cpu.first)


def test_a_context_no_chunk_divides_runs_to_its_last_position():
    """300 positions in 256-row chunks: a prompt whose second chunk is 43
    rows, then the decode step at the last position, 299, each the oracle's
    logits; the caches are 300 rows, exactly.
    """
    config = dataclasses.replace(SMALL, max_seq_len=300)
    weights = checkpoint(config).tree("random")
    model, oracle = OnHost(config, weights), Llama.oracle(config, weights)
    tokens = np.random.default_rng(8).integers(0, config.vocab_size, 300)
    _assert_close([model.logits(tokens[:299])], [oracle.logits(tokens[:299])])
    _assert_close([model.logits(tokens)], [oracle.logits(tokens)])
    with pytest.raises(IndexError, match="rows to 301 of 300"):
        model(model.prompt_ids(tokens[256:]), token=0, position=300, chunk=1, rows=45)
