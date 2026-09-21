# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The graphs' references against the model's own CPU reference.

``llama_cpu.py`` is the reference the NPU application is judged against: a
plain torch forward pass with a growing KV cache. ``PrefillGraph`` and
``DecodeGraph`` are the same computation as graph functions, and
``GraphFunction.reference`` runs each operator by operator through its
``reference()`` on host tensors, with the per-call values modelled (the
last prompt row selects the logits, the cache offset moves the copy, the
vector size masks the softmax) and the caches as state. So the two can be
compared without a device, from the same prompt: that checks the graphs'
wiring (layouts, reshapes, the scale, the repeat, the transposes, the
cache handoff between the phases) against the model, leaving only the
kernels' arithmetic for hardware.

Both sides compute in bfloat16 with different operation orders, so the
logits agree to bf16 tolerance and the argmax exactly.
"""

import sys
from pathlib import Path

import pytest
import torch

APP = Path(__file__).resolve().parents[2] / "applications" / "llama_3.2_1b"
sys.path.insert(0, str(APP))

import llama_cpu  # noqa: E402
from llama_graphs import DecodeGraph, PrefillGraph  # noqa: E402
from llama_inference_harness import LlamaModelState  # noqa: E402

from iron.tests.common.llama_model import Config as _Config  # noqa: E402


def _embed(config, token):
    return torch.nn.functional.embedding(token, config.model.out_head.weight)


def cpu_decode(config, prompt, n_tokens):
    """Prefill the prompt, then decode ``n_tokens`` greedily; logits per step and the caches."""
    state = LlamaModelState(config)
    state.token_ids = prompt
    logits, state = llama_cpu.llama_forward_pass(config, state)
    prefill_caches = (
        [c.clone() for c in state.attn_keys_caches],
        [c.clone() for c in state.attn_values_caches],
    )
    out, token = [], logits[0, -1].argmax()
    for _ in range(n_tokens):
        state.token_ids = token.reshape(1, 1)
        logits, state = llama_cpu.llama_forward_pass(config, state)
        out.append(logits[0, -1].float())
        token = logits[0, -1].argmax()
    return out, prefill_caches


def decode_graph(config):
    """The decode graph at the test's context length, four columns wide so the
    prefill graph's tiles divide the scaled model."""
    return DecodeGraph(
        config,
        config.context_length,
        num_aie_columns=4,
        tensor=lambda a: torch.as_tensor(a).to(torch.bfloat16),
    )


def seed_caches(config, graph, caches):
    """Write the CPU prefill's caches into the graph's states, in its layout."""
    L, D = config.context_length, config.head_dim
    keys, values = caches
    for i in range(config.n_layers):
        for state, cache in ((graph.keys[i], keys[i]), (graph.values[i], values[i])):
            host = torch.zeros(state.shape, dtype=torch.bfloat16)
            P = cache.shape[2]
            host.view(config.n_kv_groups, L, D)[:, :P, :] = cache[0]
            state.host = host


def graph_prefill(config, graph, prompt):
    """Run the prompt through the prefill graph's reference; the logits of its last token.

    The graph runs at the context length: the prompt fills the first rows
    of ``x`` and the rest are zero; ``last`` picks the last prompt row."""
    L, E = config.context_length, config.emb_dim
    n = prompt.shape[1]
    x = torch.zeros(L, E, dtype=torch.bfloat16)
    x[:n] = _embed(config, prompt).reshape(n, E)
    pre = PrefillGraph(config, graph, num_of_pipelines=1, tile_m=16)
    logits = pre.graph.reference(x, config.angles[:L], last=(n - 1) * E)
    return logits.reshape(-1).float()


def graph_decode(config, graph, prompt, n_tokens, first_logits, *, vector_size):
    """Decode ``n_tokens`` through the graph's reference from its seeded caches."""
    D = config.head_dim
    out, token = [], first_logits.argmax()
    pos = prompt.shape[1]
    for step in range(n_tokens):
        x = _embed(config, token.reshape(1, 1)).reshape(1, config.emb_dim)
        angles = config.angles[pos : pos + 1]
        logits = graph.graph.reference(
            x, angles, cache_offset=pos * D, vector_size=vector_size(step, pos)
        )
        logits = logits.reshape(-1).float()
        out.append(logits)
        token = logits.argmax()
        pos += 1
    return out


@pytest.fixture(scope="module")
def cpu():
    torch.manual_seed(1)
    config = _Config()
    prompt = torch.randint(0, config.vocab_size, (1, 8))
    n_tokens = 6
    logits, caches = cpu_decode(config, prompt, n_tokens)
    return config, prompt, n_tokens, logits, caches


def _first_logits(config, prompt):
    state = LlamaModelState(config)
    state.token_ids = prompt
    logits, _ = llama_cpu.llama_forward_pass(config, state)
    return logits[0, -1]


def _context_length(step, pos):
    return pos + 1  # prompt + tokens so far


def _assert_close(got, expected):
    for step, (a, b) in enumerate(zip(got, expected)):
        scale = b.abs().max()
        err = (a - b).abs().max()
        assert err <= 0.05 * scale, (
            f"step {step}: max |diff| {err:.4f} against |logits| {scale:.3f}"
        )
        assert a.argmax() == b.argmax(), (
            f"step {step}: argmax {a.argmax()} != {b.argmax()}"
        )


def test_the_decode_reference_matches_the_cpu_reference_token_by_token(cpu):
    config, prompt, n_tokens, expected, caches = cpu
    graph = decode_graph(config)
    seed_caches(config, graph, caches)
    first = _first_logits(config, prompt)
    got = graph_decode(
        config, graph, prompt, n_tokens, first, vector_size=_context_length
    )
    _assert_close(got, expected)


def test_the_prefill_reference_matches_the_cpu_prefill_and_hands_decode_its_caches(
    cpu,
):
    config, prompt, n_tokens, expected, caches = cpu
    graph = decode_graph(config)
    first = graph_prefill(config, graph, prompt)
    _assert_close([first], [_first_logits(config, prompt).float()])
    # The caches hold the prompt's keys and values in decode's layout.
    L, D, n = config.context_length, config.head_dim, prompt.shape[1]
    keys, values = caches
    for i in range(config.n_layers):
        for state, cache in ((graph.keys[i], keys[i]), (graph.values[i], values[i])):
            got = state.host.view(config.n_kv_groups, L, D)[:, :n, :].float()
            want = cache[0].float()
            assert (got - want).abs().max() <= 0.05 * want.abs().max(), (i, state)
    # Decode continues from them, without the CPU's caches.
    got = graph_decode(
        config, graph, prompt, n_tokens, first, vector_size=_context_length
    )
    _assert_close(got, expected)


def test_the_cumulative_vector_size_is_not_the_context_length(cpu):
    """§18's first candidate. llama_npu.py writes the softmax's valid length
    as a running sum of context lengths, so from the second token on the
    softmax sees stale zero columns beyond the context as real keys.
    Modelled here: it drifts from the CPU reference where the correct
    context length does not."""
    config, prompt, n_tokens, expected, caches = cpu
    cum = {"total": 0}

    def cumulative(step, pos):
        cum["total"] += pos + 1
        return min(cum["total"], config.context_length)

    graph = decode_graph(config)
    seed_caches(config, graph, caches)
    got = graph_decode(
        config,
        graph,
        prompt,
        n_tokens,
        _first_logits(config, prompt),
        vector_size=cumulative,
    )
    # The first token is right (a sum of one term), later ones are not.
    assert torch.allclose(got[0], expected[0], atol=0.05 * expected[0].abs().max())
    drift = [(a - b).abs().max().item() for a, b in zip(got[1:], expected[1:])]
    assert max(drift) > 0.05 * expected[1].abs().max(), drift
