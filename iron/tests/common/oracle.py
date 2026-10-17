# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.Oracle``'s shared primitives (``rms_norm``, ``gelu_tanh``,
``attend``, ``rotate``), against independent reference formulas on fixed
random inputs, and that ``LlamaOracle`` (a decoder's own subclass) still
traces the same math through them. No NPU.
"""

import dataclasses

import numpy as np
import pytest

from iron.lm import Oracle
from iron.applications.embedding_gemma2.config import AudioConfig
from iron.applications.llama.model import Llama
from iron.tests.common.llama_model import SMALL, checkpoint


def _rng(seed):
    return np.random.default_rng(seed)


def test_rms_norm_matches_the_formula():
    rng = _rng(0)
    x = rng.standard_normal((5, 8)).astype(np.float32)
    w = rng.standard_normal(8).astype(np.float32)
    o = Oracle(AudioConfig())
    got = o.rms_norm(x, w)
    want = x / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + 1e-6) * w
    np.testing.assert_allclose(got, want, rtol=1e-6, atol=0)
    # The default weight is 1: unweighted RMS normalization.
    np.testing.assert_allclose(
        o.rms_norm(x),
        x / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + 1e-6),
        rtol=1e-6,
        atol=0,
    )


def test_gelu_tanh_matches_the_formula():
    x = np.linspace(-4, 4, 33, dtype=np.float32)
    c = np.sqrt(2 / np.pi).astype(np.float32)
    want = 0.5 * x * (1 + np.tanh(c * (x + 0.044715 * x**3)))
    np.testing.assert_allclose(Oracle.gelu_tanh(x), want, rtol=1e-6, atol=0)


def test_rotate_single_table_matches_the_rope_formula():
    rng = _rng(1)
    n, heads, D = 6, 3, 8
    x = rng.standard_normal((n, heads, D)).astype(np.float32)
    angles = rng.standard_normal((n, D)).astype(np.float32)
    got = Oracle.rotate(x, angles)
    cos, sin = angles[:, None, ::2], angles[:, None, 1::2]
    x1, x2 = np.split(x, 2, axis=-1)
    want = np.concatenate([x1 * cos - x2 * sin, x1 * sin + x2 * cos], axis=-1)
    np.testing.assert_array_equal(got, want)


def test_rotate_a_list_of_tables_rotates_each_part_of_the_head_by_its_own():
    rng = _rng(2)
    n, heads, D = 5, 2, 8
    x = rng.standard_normal((n, heads, D)).astype(np.float32)
    tables = [rng.standard_normal((n, 4)).astype(np.float32) for _ in range(2)]
    got = Oracle.rotate(x, tables)
    parts = np.split(x, 2, axis=-1)
    want = np.concatenate([Oracle.rotate(p, a) for p, a in zip(parts, tables)], axis=-1)
    np.testing.assert_array_equal(got, want)
    assert got.shape == x.shape


def test_attend_causal_matches_scaled_masked_softmax():
    rng = _rng(3)
    n, H, G, D = 5, 4, 2, 8
    q = rng.standard_normal((n, H, D)).astype(np.float32)
    k = rng.standard_normal((n, G, D)).astype(np.float32)
    v = rng.standard_normal((n, G, D)).astype(np.float32)
    o = Oracle(AudioConfig())
    got = o.attend(q, k, v, causal=True)

    kr, vr = (np.repeat(a, H // G, axis=1) for a in (k, v))
    p = np.einsum("qhd,khd->hqk", q, kr) / np.sqrt(D)
    mask = np.triu(np.full((n, n), -np.inf, np.float32), k=1)
    p = p + mask
    p = p - p.max(axis=-1, keepdims=True)
    p = np.exp(p)
    p = p / p.sum(axis=-1, keepdims=True)
    want = np.einsum("hqk,khd->qhd", p, vr).reshape(n, H * D)
    np.testing.assert_allclose(got, want, rtol=1e-5, atol=1e-6)


def test_attend_bidirectional_at_scale_one_is_unscaled_and_windowed():
    rng = _rng(4)
    n, H, G, D = 6, 4, 2, 8
    q = rng.standard_normal((n, H, D)).astype(np.float32)
    k = rng.standard_normal((n, G, D)).astype(np.float32)
    v = rng.standard_normal((n, G, D)).astype(np.float32)
    window = 2
    o = Oracle(AudioConfig())
    got = o.attend(q, k, v, window=window, scale=1.0)

    kr, vr = (np.repeat(a, H // G, axis=1) for a in (k, v))
    p = np.einsum("qhd,khd->hqk", q, kr)  # unscaled
    pos = np.arange(n)
    banded = np.abs(pos[:, None] - pos[None, :]) <= window
    p = np.where(banded[None], p, -np.inf)
    p = p - p.max(axis=-1, keepdims=True)
    p = np.exp(p)
    p = p / p.sum(axis=-1, keepdims=True)
    want = np.einsum("hqk,khd->qhd", p, vr).reshape(n, H * D)
    np.testing.assert_allclose(got, want, rtol=1e-5, atol=1e-6)


def test_attend_refuses_causal_and_window_together():
    o = Oracle(AudioConfig())
    q = k = v = np.zeros((2, 2, 4), np.float32)
    with pytest.raises(ValueError):
        o.attend(q, k, v, causal=True, window=1)


def test_llama_oracle_still_runs_and_is_deterministic():
    """Two oracles of the same weights, each through ``Layer.oracle``, give
    bitwise-identical logits.
    """
    config = SMALL
    weights = checkpoint(config).tree("random", seed=7)
    a = Llama.oracle(config, weights)
    b = Llama.oracle(config, weights)
    tokens = np.array([1, 2, 3, 4], np.int64)
    logits_a, logits_b = a.logits(tokens), b.logits(tokens)
    assert np.array_equal(logits_a, logits_b)
    assert np.isfinite(logits_a).all()


def test_llama_oracle_head_uses_the_configs_eps():
    config = dataclasses.replace(SMALL, eps=1e-3)
    weights = checkpoint(config).tree("random", seed=8)
    oracle = Llama.oracle(config, weights)
    x = np.random.default_rng(9).standard_normal((1, config.emb_dim)).astype(np.float32)
    norm = np.asarray(weights.model.norm.weight, np.float32)
    got = oracle.head(x)
    want = (x / np.sqrt(np.mean(x * x, -1, keepdims=True) + 1e-3) * norm) @ np.asarray(
        oracle.embedding, np.float32
    ).T
    np.testing.assert_allclose(got, want, rtol=1e-5, atol=1e-6)
