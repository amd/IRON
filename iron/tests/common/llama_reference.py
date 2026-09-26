# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The graphs' references against the model's plain forward pass.

``Llama.forward`` is a stateless causal pass in torch, the oracle the NPU
application is judged against. ``LlamaGraph.graph`` is the same
computation as one graph function, called at a prompt's shape and at one
token's, and ``GraphFunction.reference`` runs it operator by operator
through each ``reference()`` on host tensors, with the per-call values
modelled (the last prompt row selects the logits, the cache offset moves the
copy, the vector size masks the softmax) and the caches as state. So the two
can be compared without a device, from the same prompt: that checks the
graph's wiring (layouts, reshapes, the scale, the repeat, the transposes,
the caches the prompt leaves for decode) against the model, leaving only
the kernels' arithmetic for hardware.

The oracle needs no cache: the logits at position ``t`` of a causal pass
over ``t + 1`` tokens are what a cached decode produces at step ``t``. Both
sides compute in bfloat16 with different operation orders, so the logits
agree to bf16 tolerance and the argmax exactly.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.llama_3_2_1b import harness
from iron.applications.llama_3_2_1b.graphs import LlamaGraph, prompt_rows
from iron.applications.llama_3_2_1b.harness import LlamaModelState
from iron.applications.llama_3_2_1b.npu import AIELlama
from iron.tests.common.llama_model import Config as _Config

# The oracle is torch; the graphs and the application are not.
torch = pytest.importorskip("torch")
model = pytest.importorskip("iron.applications.llama_3_2_1b.model")
reference = pytest.importorskip("iron.applications.llama_3_2_1b.reference")


def oracle(config, tokens):
    """The plain forward's logits at every position, in float."""
    tree = model.Llama.from_weights(config, config.weights)
    angles = torch.from_numpy(config.angles.view(np.uint16)).view(torch.bfloat16)
    return tree(tokens, angles).float()


def _embed(config, tokens):
    return config.weights.embed(tokens.numpy())


def llama_graph(config):
    """The graph at the test's context length; its profile fits the scaled model."""
    return LlamaGraph(config, config.context_length)


def graph_prefill(config, graph, prompt):
    """Run the prompt through the graph's reference; the logits of its last token.

    The graph runs at the context length: the prompt fills the first rows
    of ``x`` and the rest are zero; ``last`` picks the last prompt row.
    """
    rows = config.context_length
    E = config.emb_dim
    n = prompt.shape[0]
    x = np.zeros((rows, E), dtype=bfloat16)
    x[:n] = _embed(config, prompt)
    logits = graph.graph.reference(
        x,
        config.angles[:rows],
        rows=prompt_rows(n, rows),
        cache_offset=0,
        vector_size=n,
        last=n - 1,
    )
    return torch.from_numpy(logits.reshape(-1).astype(np.float32))


def graph_decode(config, graph, tokens, pos, *, vector_size=None):
    """Feed ``tokens`` one at a time through the graph's reference from
    position ``pos``, its caches as they are; the logits after each.
    """
    out = []
    for step, token in enumerate(tokens):
        x = _embed(config, token.reshape(1)).reshape(1, config.emb_dim)
        angles = config.angles[pos : pos + 1]
        n = pos + 1 if vector_size is None else vector_size(step, pos)
        logits = graph.graph.reference(
            x,
            angles,
            rows=1,
            cache_offset=pos,
            vector_size=n,
            last=0,
        )
        out.append(torch.from_numpy(logits.reshape(-1).astype(np.float32)))
        pos += 1
    return out


def greedy(config, graph, first_logits, pos, n_tokens):
    """Generate ``n_tokens`` greedily through the decode reference from ``pos``."""
    out, token = [], first_logits.argmax()
    for _ in range(n_tokens):
        (logits,) = graph_decode(config, graph, token.reshape(1), pos)
        out.append(logits)
        token = logits.argmax()
        pos += 1
    return out


@pytest.fixture(scope="module")
def cpu():
    """A prompt, the oracle's logits for it, and six greedy tokens' logits."""
    torch.manual_seed(1)
    config = _Config()
    prompt = torch.randint(0, config.vocab_size, (8,))
    n_tokens = 6
    tokens, expected = prompt, []
    first = oracle(config, tokens)[-1]
    logits = first
    for _ in range(n_tokens):
        tokens = torch.cat([tokens, logits.argmax().reshape(1)])
        logits = oracle(config, tokens)[-1]
        expected.append(logits)
    return config, prompt, first, expected


def _assert_close(got, expected):
    for step, (a, b) in enumerate(zip(got, expected)):
        scale = b.abs().max()
        err = (a - b).abs().max()
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
    config, prompt, first, expected = cpu
    graph = llama_graph(config)
    over_prompt = graph_decode(config, graph, prompt, 0)
    _assert_close([over_prompt[-1]], [first])
    got = greedy(config, graph, over_prompt[-1], prompt.shape[0], len(expected))
    _assert_close(got, expected)


def test_the_prompt_matches_the_forward_and_leaves_decode_its_caches(cpu):
    config, prompt, first, expected = cpu
    graph = llama_graph(config)
    got_first = graph_prefill(config, graph, prompt)
    _assert_close([got_first], [first])
    # Decode continues from the caches the prompt wrote: the same states.
    got = greedy(config, graph, got_first, prompt.shape[0], len(expected))
    _assert_close(got, expected)


def test_the_cumulative_vector_size_is_not_the_context_length(cpu):
    """A softmax valid length written as a running sum of context lengths
    makes the softmax treat stale zero columns beyond the context as real
    keys from the second token on. Modelled here: it drifts from the forward
    where the correct context length does not.
    """
    config, prompt, first, expected = cpu
    graph = llama_graph(config)
    graph_prefill(config, graph, prompt)
    cum = {"total": 0}

    def cumulative(step, pos):
        cum["total"] += pos + 1
        return min(cum["total"], config.context_length)

    tokens = torch.stack([first.argmax()] + [e.argmax() for e in expected[:-1]])
    got = graph_decode(config, graph, tokens, prompt.shape[0], vector_size=cumulative)
    # The first token is right (a sum of one term), later ones are not.
    _assert_close(got[:1], expected[:1])
    drift = [(a - b).abs().max().item() for a, b in zip(got[1:], expected[1:])]
    assert max(drift) > 0.05 * expected[1].abs().max(), drift


class _Output:
    """What an image returns: a buffer read with ``numpy()``."""

    def __init__(self, array):
        self.array = array

    def numpy(self):
        return self.array


def application(config):
    """npu.py's AIELlama with its graph function stood in by its reference,
    which runs at whatever shape it is called with.
    """
    graph = llama_graph(config)

    def forward(*tensors, **values):
        return _Output(graph.graph.reference(*tensors, **values))

    return AIELlama(config, forward, config.context_length)


def test_the_application_runs_both_phases_through_its_images(cpu):
    """npu.py's own forward pass, its graph stood in by the reference: the
    embedding, the prompt's padding and its last-row offset, the angles and
    decode's values are the application's.
    """
    config, prompt, first, expected = cpu
    npu = application(config)

    state = LlamaModelState(config)
    state.token_ids = prompt.numpy().reshape(1, -1)
    logits, state = npu.forward(config, state)
    assert logits.shape == (1, 1, config.vocab_size)

    # The images return numpy, and so does the forward pass: the harness
    # samples and scores in numpy.
    assert isinstance(logits, np.ndarray)

    def as_torch(a):
        return torch.from_numpy(a[0, -1].astype(np.float32))

    _assert_close([as_torch(logits)], [first])
    got, token = [], int(logits[0, -1].argmax())
    for _ in range(len(expected)):
        state.token_ids = np.array([[token]], dtype=np.int64)
        logits, state = npu.forward(config, state)
        got.append(as_torch(logits))
        token = int(logits[0, -1].argmax())
    _assert_close(got, expected)


def test_the_accuracy_check_scores_the_application_against_the_reference(cpu):
    """What ``python -m iron.applications.llama_3_2_1b.accuracy`` runs, with
    the graph references for the images: the numpy harness against the
    float32 torch reference, teacher-forced.
    """
    config, prompt, _, expected = cpu
    npu = application(config)
    state = LlamaModelState(config)
    state.token_ids = prompt.numpy().reshape(1, -1)
    results = harness.check_accuracy(
        config,
        state,
        npu.forward,
        config,
        LlamaModelState(config),
        reference.ReferenceForward(config),
        len(expected) + 1,
    )
    assert all(top1 for _, top1 in results), results
    # bf16 graphs against a float32 forward: close, not equal.
    assert all(0 <= kl < 0.05 for kl, _ in results), results
    assert any(kl > 0 for kl, _ in results), results


def test_the_determinism_check_finds_the_references_deterministic(cpu):
    """What ``--check-determinism`` runs: two prompts, alternated, through
    the application's forward pass; no run differs from the first.
    """
    config, prompt, _, _ = cpu
    npu = application(config)
    prompts = [prompt.numpy().reshape(1, -1), prompt.numpy()[::-1].reshape(1, -1)]
    assert harness.check_determinism(config, prompts, npu.forward, 3, 3) == 0


def test_a_short_prompt_runs_at_its_own_rows():
    """A context longer than a prompt's row block: the prompt runs at its
    rows (``prompt_rows``), not the context, and its logits are the oracle's;
    decode continues from the caches it wrote.
    """

    class Longer(_Config):
        context_length = 1024

    torch.manual_seed(2)
    config = Longer()
    prompt = torch.randint(0, config.vocab_size, (8,))
    assert prompt_rows(8, config.context_length) == 512 < config.context_length
    graph = llama_graph(config)
    first = oracle(config, prompt)[-1]
    got_first = graph_prefill(config, graph, prompt)
    _assert_close([got_first], [first])
    token = first.argmax().reshape(1)
    (got_next,) = graph_decode(config, graph, token, 8)
    _assert_close([got_next], [oracle(config, torch.cat([prompt, token]))[-1]])
