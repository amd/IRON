# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The decode graph's reference against the model's own CPU reference.

``llama_cpu.py`` is the reference the NPU application is judged against: a
plain torch forward pass with a growing KV cache. ``DecodeGraph`` is the
same computation as a graph function, and ``GraphFunction.reference`` runs
it operator by operator through each operator's ``reference()`` on host
tensors, with the per-call values modelled (the cache offset moves the
copy, the vector size masks the softmax) and the caches as state. So the
two can be compared without a device, token by token, from the same
prompt: that checks the graph's wiring (layouts, reshapes, the scale, the
repeat, the transposes, the cache handoff) against the model, leaving only
the kernels' arithmetic for hardware.

Both sides compute in bfloat16 with different operation orders, so the
logits agree to bf16 tolerance and the argmax exactly.
"""

import math
import sys
from pathlib import Path

import pytest
import torch

APP = Path(__file__).resolve().parents[2] / "applications" / "llama_3.2_1b"
sys.path.insert(0, str(APP))

import llama_cpu  # noqa: E402
from decode_graph import DecodeGraph  # noqa: E402
from llama_inference_harness import LlamaModelState, compute_rope_angles  # noqa: E402


class _Param:
    def __init__(self, tensor):
        self.weight = tensor


class _Attn:
    pass


class _Block:
    def __init__(self, gen, E, H, G, D, F):
        w = lambda *shape, scale: _Param(  # noqa: E731
            (torch.randn(*shape, generator=gen) * scale).to(torch.bfloat16)
        )
        self.norm1, self.norm2 = w(E, scale=0.1) , w(E, scale=0.1)
        self.norm1.weight += 1
        self.norm2.weight += 1
        self.attn = _Attn()
        self.attn.q, self.attn.k = w(H * D, E, scale=E**-0.5), w(G * D, E, scale=E**-0.5)
        self.attn.v, self.attn.o = w(G * D, E, scale=E**-0.5), w(E, H * D, scale=(H * D) ** -0.5)
        self.ffn = _Attn()
        self.ffn.gate, self.ffn.up = w(F, E, scale=E**-0.5), w(F, E, scale=E**-0.5)
        self.ffn.down = w(E, F, scale=F**-0.5)


class _Model:
    def __init__(self, cfg, seed=0):
        gen = torch.Generator().manual_seed(seed)
        self.layers = [
            _Block(gen, cfg.emb_dim, cfg.n_heads, cfg.n_kv_groups, cfg.head_dim, cfg.hidden_dim)
            for _ in range(cfg.n_layers)
        ]
        self.norm = _Param((1 + 0.1 * torch.randn(cfg.emb_dim, generator=gen)).to(torch.bfloat16))
        self.out_head = _Param(
            (torch.randn(cfg.vocab_size, cfg.emb_dim, generator=gen) * cfg.emb_dim**-0.5).to(torch.bfloat16)
        )

    def named_parameters(self):
        for i, blk in enumerate(self.layers):
            for path in ("norm1", "norm2", "attn.q", "attn.k", "attn.v", "attn.o", "ffn.gate", "ffn.up", "ffn.down"):
                obj = blk
                for part in path.split("."):
                    obj = getattr(obj, part)
                yield f"layers.{i}.{path}.weight", obj.weight
        yield "norm.weight", self.norm.weight
        yield "out_head.weight", self.out_head.weight


class _Config:
    """Llama's shape at a size the reference runs in seconds; a real layout, small."""

    n_layers, n_heads, n_kv_groups, head_dim = 2, 16, 4, 64
    emb_dim, hidden_dim, vocab_size = 256, 512, 1024
    context_length = 64

    def __init__(self):
        self.model = _Model(self)
        self.angles = compute_rope_angles(self.head_dim, self.context_length).to(torch.bfloat16)


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


def graph_decode(config, prompt, n_tokens, first_logits_from_cpu, caches, *, vector_size):
    """Seed the caches from the CPU prefill and decode the same tokens through the graph's reference."""
    L, D = config.context_length, config.head_dim
    keys, values = caches
    graph = DecodeGraph(config, L, tensor=lambda a: torch.as_tensor(a).to(torch.bfloat16))
    for i in range(config.n_layers):
        for state, cache in ((graph.keys[i], keys[i]), (graph.values[i], values[i])):
            host = torch.zeros(state.shape, dtype=torch.bfloat16)
            P = cache.shape[2]
            host.view(config.n_kv_groups, L, D)[:, :P, :] = cache[0]
            state.host = host
    out, token = [], first_logits_from_cpu.argmax()
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


def test_the_graph_reference_matches_the_cpu_reference_token_by_token(cpu):
    config, prompt, n_tokens, expected, caches = cpu
    got = graph_decode(
        config, prompt, n_tokens, _first_logits(config, prompt), caches,
        vector_size=lambda step, pos: pos + 1,  # the context length: prompt + tokens so far
    )
    for step, (a, b) in enumerate(zip(got, expected)):
        scale = b.abs().max()
        err = (a - b).abs().max()
        assert err <= 0.05 * scale, f"step {step}: max |diff| {err:.4f} against |logits| {scale:.3f}"
        assert a.argmax() == b.argmax(), f"step {step}: argmax {a.argmax()} != {b.argmax()}"


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

    got = graph_decode(config, prompt, n_tokens, _first_logits(config, prompt), caches, vector_size=cumulative)
    # The first token is right (a sum of one term), later ones are not.
    assert torch.allclose(got[0], expected[0], atol=0.05 * expected[0].abs().max())
    drift = [(a - b).abs().max().item() for a, b in zip(got[1:], expected[1:])]
    assert max(drift) > 0.05 * expected[1].abs().max(), drift
