# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.Experts``, device-free: a mixture of experts read by each family
of Hugging Face names, and its oracle twin against a row-by-row reference
written as Hugging Face's routers compute it.
"""

import json
from types import SimpleNamespace

import numpy as np
import pytest

from iron.applications.embedding_gemma2.config import AudioConfig
from iron.lm import DecoderConfig, Experts, Layer, Oracle

N, E, F, X, K, S = 9, 8, 6, 5, 2, 7


def drawn(seed: int) -> SimpleNamespace:
    """A mixture's arrays: router, stacked gate and up, down, and a shared
    expert's gate, up, down and gate projection.
    """
    rng = np.random.default_rng(seed)

    def normal(*shape):
        return (rng.standard_normal(shape) / np.sqrt(shape[-1])).astype(np.float32)

    return SimpleNamespace(
        router=normal(X, E) * 4,
        gate=normal(X, F, E),
        up=normal(X, F, E),
        down=normal(X, E, F),
        shared_gate=normal(S, E),
        shared_up=normal(S, E),
        shared_down=normal(E, S),
        shared_scale=normal(1, E),
        norm=np.ones(E, np.float32),
    )


def linear(weight) -> SimpleNamespace:
    return SimpleNamespace(weight=weight)


def layer(a: SimpleNamespace, family: str) -> SimpleNamespace:
    """A layer module holding the mixture ``a`` under ``family``'s names."""
    norms = dict(
        input_layernorm=linear(a.norm), post_attention_layernorm=linear(a.norm)
    )
    gate_up = np.concatenate([a.gate, a.up], axis=1)
    if family == "granite":
        moe = SimpleNamespace(
            router=SimpleNamespace(layer=linear(a.router)),
            input_linear=linear(gate_up),
            output_linear=linear(a.down),
        )
        return SimpleNamespace(**norms, block_sparse_moe=moe)
    if family == "stacked":
        moe = SimpleNamespace(
            router=linear(a.router),
            experts=SimpleNamespace(gate_up_proj=gate_up, down_proj=a.down),
        )
        return SimpleNamespace(**norms, block_sparse_moe=moe)
    if family == "mixtral":
        experts = [
            SimpleNamespace(w1=linear(g), w3=linear(u), w2=linear(d))
            for g, u, d in zip(a.gate, a.up, a.down)
        ]
        moe = SimpleNamespace(gate=linear(a.router), experts=experts)
        return SimpleNamespace(**norms, block_sparse_moe=moe)
    experts = [
        SimpleNamespace(gate_proj=linear(g), up_proj=linear(u), down_proj=linear(d))
        for g, u, d in zip(a.gate, a.up, a.down)
    ]
    return SimpleNamespace(
        **norms, mlp=SimpleNamespace(gate=linear(a.router), experts=experts)
    )


def silu(x):
    return x / (1 + np.exp(-x))


def by_row(a, h, k, normalize) -> np.ndarray:
    """The mixture row by row, as Hugging Face's routers write it: a softmax
    over every logit, the ``k`` largest, renormalized over those if
    ``normalize``, each chosen expert's output scaled by its weight.
    """
    out = np.zeros_like(h)
    for t, row in enumerate(h):
        logits = a.router @ row
        p = np.exp(logits - logits.max())
        p /= p.sum()
        ids = np.argsort(-p, kind="stable")[:k]
        w = p[ids] / p[ids].sum() if normalize else p[ids]
        for weight, e in zip(w, ids):
            out[t] += weight * (a.down[e] @ (silu(a.gate[e] @ row) * (a.up[e] @ row)))
    return out


def rows(seed: int) -> np.ndarray:
    return np.random.default_rng(seed).standard_normal((N, E)).astype(np.float32)


@pytest.mark.parametrize("normalize", [True, False])
def test_each_row_is_its_top_k_experts_weighted_as_its_router_says(normalize):
    a, h = drawn(1), rows(2)
    got = Experts(K, normalize).oracle(
        Oracle(AudioConfig()), layer(a, "granite"), h, "silu"
    )
    np.testing.assert_allclose(got, by_row(a, h, K, normalize), rtol=1e-5, atol=1e-6)


@pytest.mark.parametrize("family", ["stacked", "mixtral", "qwen"])
def test_every_family_s_names_read_as_the_same_mixture(family):
    a, h, o = drawn(3), rows(4), Oracle(AudioConfig())
    mine, theirs = layer(a, "granite"), layer(a, family)
    for p, q in zip(
        Experts.experts(Experts.mixture(mine)), Experts.experts(Experts.mixture(theirs))
    ):
        np.testing.assert_array_equal(np.stack(list(p)), np.stack(list(q)))
    experts = Experts(K)
    np.testing.assert_array_equal(
        experts.oracle(o, mine, h, "silu"), experts.oracle(o, theirs, h, "silu")
    )


def test_a_tie_at_the_k_th_logit_goes_to_the_lower_expert():
    a, h, o = drawn(5), rows(6), Oracle(AudioConfig())
    # Experts 2 and 3 route alike and compute differently.
    a.router[3] = a.router[2]
    a.router[[0, 1, 4]] = -a.router[2]
    a.gate[3] = -a.gate[2]
    got = Experts(1).oracle(o, layer(a, "granite"), h, "silu")
    for e, want in ((2, True), (3, False)):
        one = a.down[e] @ (silu(a.gate[e] @ h.T) * (a.up[e] @ h.T))
        top = np.argmax(h @ a.router.T, axis=-1) == 2
        assert top.any()
        assert np.allclose(got[top], one.T[top], rtol=1e-5, atol=1e-6) == want


@pytest.mark.parametrize("family", ["granite", "qwen"])
def test_a_shared_expert_is_added_scaled_by_its_gate_where_it_has_one(family):
    a, h, o = drawn(7), rows(8), Oracle(AudioConfig())
    w = layer(a, family)
    if family == "granite":
        w.shared_mlp = SimpleNamespace(
            input_linear=linear(np.concatenate([a.shared_gate, a.shared_up])),
            output_linear=linear(a.shared_down),
        )
        scale = np.ones((N, 1), np.float32)
    else:
        w.mlp.shared_expert = SimpleNamespace(
            gate_proj=linear(a.shared_gate),
            up_proj=linear(a.shared_up),
            down_proj=linear(a.shared_down),
        )
        w.mlp.shared_expert_gate = linear(a.shared_scale)
        scale = 1 / (1 + np.exp(-(h @ a.shared_scale.T)))
    shared = (silu(h @ a.shared_gate.T) * (h @ a.shared_up.T)) @ a.shared_down.T
    want = by_row(a, h, K, True) + scale * shared
    np.testing.assert_allclose(
        Experts(K).oracle(o, w, h, "silu"), want, rtol=1e-5, atol=1e-6
    )


def test_the_feed_forward_block_is_the_mixture_and_its_residual():
    a, x, o = drawn(9), rows(10), Oracle(AudioConfig(eps=1e-6))
    a.norm = np.random.default_rng(11).uniform(0.5, 1.5, E).astype(np.float32)
    layer_ = Layer(2, 1, 4, 1e-6, residual=0.22, experts=Experts(K))
    got = layer_.feed_forward_oracle(o, layer(a, "granite"), x)
    h = x / np.sqrt(np.mean(x * x, -1, keepdims=True) + 1e-6) * a.norm
    np.testing.assert_allclose(
        got, x + np.float32(0.22) * by_row(a, h, K, True), rtol=1e-5, atol=1e-6
    )


def test_a_mixture_the_config_routes_no_rows_of_is_refused():
    with pytest.raises(ValueError, match="routes none"):
        Layer(2, 1, 4, 1e-6).feed_forward_oracle(
            Oracle(AudioConfig()), layer(drawn(12), "granite"), rows(13)
        )


@pytest.mark.parametrize(
    "fields, routed",
    [
        ({}, None),
        ({"num_experts_per_tok": 8}, Experts(8)),
        ({"num_experts_per_tok": 4, "norm_topk_prob": False}, Experts(4, False)),
    ],
)
def test_the_config_json_routes_each_layer(tmp_path, fields, routed):
    shape = dict(
        vocab_size=16,
        hidden_size=8,
        num_hidden_layers=2,
        num_attention_heads=2,
        num_key_value_heads=1,
        head_dim=4,
        intermediate_size=6,
        rope_theta=10000.0,
    )
    (tmp_path / "config.json").write_text(json.dumps({**shape, **fields}))
    config = DecoderConfig.from_checkpoint(tmp_path)
    assert config.layer(1).experts == routed
