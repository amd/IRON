# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The graphs' references against the model's plain forward pass.

``Llama.forward`` is a stateless causal pass in torch, the oracle the NPU
application is judged against. ``PrefillGraph`` and ``DecodeGraph`` are the
same computation as graph functions, and ``GraphFunction.reference`` runs
each operator by operator through its ``reference()`` on host tensors, with
the per-call values modelled (the last prompt row selects the logits, the
cache offset moves the copy, the vector size masks the softmax) and the
caches as state. So the two can be compared without a device, from the
same prompt: that checks the graphs' wiring (layouts, reshapes, the scale,
the repeat, the transposes, the cache handoff between the phases) against
the model, leaving only the kernels' arithmetic for hardware.

The oracle needs no cache: the logits at position ``t`` of a causal pass
over ``t + 1`` tokens are what a cached decode produces at step ``t``. Both
sides compute in bfloat16 with different operation orders, so the logits
agree to bf16 tolerance and the argmax exactly.
"""

import pytest
import numpy as np
import torch
from ml_dtypes import bfloat16

from iron.applications.llama_3_2_1b import npu as llama_npu
from iron.applications.llama_3_2_1b.graphs import DecodeGraph, PrefillGraph
from iron.applications.llama_3_2_1b.harness import LlamaModelState
from iron.tests.common.llama_model import Config as _Config


def oracle(config, tokens):
    """The plain forward's logits at every position, in float."""
    return config.model(tokens, config.angles).float()


def _np(t):
    """A torch tensor as numpy, bf16 preserved: what a graph reference takes."""
    t = t.detach()
    if t.dtype is torch.bfloat16:
        return t.view(torch.uint16).numpy().view(bfloat16)
    return t.numpy()


def _embed(config, tokens):
    return _np(torch.nn.functional.embedding(tokens, config.model.out_head.weight))


def decode_graph(config):
    """The decode graph at the test's context length, four columns wide so the
    prefill graph's tiles divide the scaled model."""
    return DecodeGraph(config, config.context_length, num_aie_columns=4)


def graph_prefill(config, graph, prompt):
    """Run the prompt through the prefill graph's reference; the logits of its last token.

    The graph runs at the context length: the prompt fills the first rows
    of ``x`` and the rest are zero; ``last`` picks the last prompt row."""
    L, E = config.context_length, config.emb_dim
    n = prompt.shape[0]
    x = np.zeros((L, E), dtype=bfloat16)
    x[:n] = _embed(config, prompt)
    pre = PrefillGraph(config, graph, num_of_pipelines=1, tile_m=16)
    logits = pre.graph.reference(x, _np(config.angles)[:L], last=(n - 1) * E)
    return torch.from_numpy(logits.reshape(-1).astype(np.float32))


def graph_decode(config, graph, tokens, pos, *, vector_size=None):
    """Feed ``tokens`` one at a time through the decode graph's reference from
    position ``pos``, its caches as they are; the logits after each."""
    D = config.head_dim
    out = []
    for step, token in enumerate(tokens):
        x = _embed(config, token.reshape(1)).reshape(1, config.emb_dim)
        angles = _np(config.angles)[pos : pos + 1]
        n = pos + 1 if vector_size is None else vector_size(step, pos)
        logits = graph.graph.reference(x, angles, cache_offset=pos * D, vector_size=n)
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
    """The decode graph alone: the prompt fed one token at a time from an
    empty cache, then the generated tokens."""
    config, prompt, first, expected = cpu
    graph = decode_graph(config)
    over_prompt = graph_decode(config, graph, prompt, 0)
    _assert_close([over_prompt[-1]], [first])
    got = greedy(config, graph, over_prompt[-1], prompt.shape[0], len(expected))
    _assert_close(got, expected)


def test_prefill_matches_the_forward_and_hands_decode_its_caches(cpu):
    config, prompt, first, expected = cpu
    graph = decode_graph(config)
    got_first = graph_prefill(config, graph, prompt)
    _assert_close([got_first], [first])
    # Decode continues from the caches prefill wrote.
    got = greedy(config, graph, got_first, prompt.shape[0], len(expected))
    _assert_close(got, expected)


def test_the_cumulative_vector_size_is_not_the_context_length(cpu):
    """§18's first candidate. npu.py used to write the softmax's valid
    length as a running sum of context lengths, so from the second token on
    the softmax saw stale zero columns beyond the context as real keys.
    Modelled here: it drifts from the forward where the correct context
    length does not."""
    config, prompt, first, expected = cpu
    graph = decode_graph(config)
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


class _Image:
    """A compiled graph stood in by its reference: the application's view of one."""

    def __init__(self, graph):
        self.graph = graph

    def __call__(self, *tensors, **values):
        out = self.graph.reference(*tensors, **values)
        return type("Out", (), {"numpy": lambda _: out})()

    def read(self, state):
        return state.host.copy()

    def write(self, state, tensor):
        state.host = np.asarray(tensor).reshape(state.shape).astype(bfloat16)


def test_the_application_runs_both_phases_through_its_images(cpu, monkeypatch):
    """npu.py's own forward pass, its two images stood in by the graph
    references: the embedding, the prompt's padding and its last-row offset,
    the angles, the cache handoff and decode's values are the application's."""
    config, prompt, first, expected = cpu
    graph = decode_graph(config)
    prefill = PrefillGraph(config, graph, num_of_pipelines=1, tile_m=16)
    npu = llama_npu.AIELlama.__new__(llama_npu.AIELlama)
    npu.decode_graph = graph
    npu.decode, npu.prefill = _Image(graph.graph), _Image(prefill.graph)
    monkeypatch.setattr(llama_npu, "npu", npu)
    monkeypatch.setattr(llama_npu, "max_seq_len", config.context_length)

    state = LlamaModelState(config)
    state.token_ids = prompt.reshape(1, -1)
    logits, state = llama_npu.llama_forward_pass(config, state)
    assert logits.shape == (1, 1, config.vocab_size)

    # The images return numpy; llama_forward_pass hands the harness torch,
    # which it samples and scores in.
    assert isinstance(logits, torch.Tensor)
    _assert_close([logits[0, -1].float()], [first])
    got, token = [], int(logits[0, -1].argmax())
    for _ in range(len(expected)):
        state.token_ids = torch.tensor(token).reshape(1, 1)
        logits, state = llama_npu.llama_forward_pass(config, state)
        got.append(logits[0, -1].float())
        token = int(logits[0, -1].argmax())
    _assert_close(got, expected)
