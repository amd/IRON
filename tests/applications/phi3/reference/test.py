#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Phi-4-mini-instruct's graph against its own plain forward pass, device-free
(no checkpoint, no NPU): Layer's partial rotary and fused qkv_proj and
gate_up_proj, through the shared decoder's caches, independent of whether
the real checkpoint or hardware is at hand.
"""

import dataclasses
import hashlib
import json
import math
import struct
import tempfile
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.device import from_name
from ml_dtypes import bfloat16

from iron.applications.phi3.model import Phi4, Phi4Config
from iron.lm import Checkpoint, accuracy, determinism


@pytest.fixture(autouse=True)
def _npu2():
    """``npu2``, bound explicitly rather than through the shared fixture:
    its ``get_current_device()`` falls back to probing the real runtime
    when nothing is bound yet, which on a host with no live NPU retries
    against hardware instead of just failing. ``probe_runtime=False``
    here never does that.
    """
    previous = aie_utils.get_current_device(probe_runtime=False)
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


#: Phi-4-mini-instruct's proportions at toy size: GQA, a fused qkv/gate_up,
#: partial rotary (half of each head), LongRoPE's amplitude scale.
TOY = Phi4Config(
    vocab_size=1024,
    emb_dim=256,
    n_layers=2,
    n_heads=8,
    n_kv_groups=2,
    head_dim=64,
    hidden_dim=512,
    rope_base=10000.0,
    max_seq_len=256,
    rotary_dim=32,
    prefill_chunk=256,
)


def _shapes(c: Phi4Config) -> dict[str, tuple[int, ...]]:
    E, F, V = c.emb_dim, c.hidden_dim, c.vocab_size
    Q, KV = c.n_heads * c.head_dim, c.n_kv_groups * c.head_dim
    out = {"model.embed_tokens.weight": (V, E), "model.norm.weight": (E,)}
    for i in range(c.n_layers):
        layer = f"model.layers.{i}"
        out |= {
            f"{layer}.input_layernorm.weight": (E,),
            f"{layer}.self_attn.qkv_proj.weight": (Q + 2 * KV, E),
            f"{layer}.self_attn.o_proj.weight": (E, Q),
            f"{layer}.post_attention_layernorm.weight": (E,),
            f"{layer}.mlp.gate_up_proj.weight": (2 * F, E),
            f"{layer}.mlp.down_proj.weight": (E, F),
        }
    return out


def _checkpoint(c: Phi4Config) -> Checkpoint:
    named = _shapes(c)
    tmp = tempfile.TemporaryDirectory(prefix="iron-phi4-reference-")
    digest = hashlib.sha256(json.dumps(named).encode()).hexdigest()[:16]
    path = Path(tmp.name) / f"{digest}.safetensors"
    header, end = {}, 0
    for name, shape in named.items():
        size = math.prod(shape) * np.dtype(bfloat16).itemsize
        header[name] = {
            "dtype": "BF16",
            "shape": shape,
            "data_offsets": [end, end + size],
        }
        end += size
    blob = json.dumps(header).encode()
    blob += b" " * (-len(blob) % 8)
    with open(path, "wb") as f:
        f.write(struct.pack("<Q", len(blob)) + blob)
        f.truncate(8 + len(blob) + end)
    checkpoint = Checkpoint(path)
    checkpoint._tmp = tmp
    return checkpoint


def _toy_weights(config: Phi4Config, seed: int = 0):
    return _checkpoint(config).tree("random", seed)


class _Output:
    def __init__(self, array):
        self.array = array

    def numpy(self):
        return self.array


class OnHost(Phi4):
    """The model with its images stood in by its reference, which runs at
    whatever shape it is called with.
    """

    profile = None

    def __call__(self, *tensors, **values):
        logits, carry = self.reference(*tensors, **values)
        return _Output(logits), carry


def _assert_close(got, expected):
    for step, (a, b) in enumerate(zip(got, expected)):
        a = np.asarray(a, dtype=np.float32)
        scale = np.abs(b).max()
        err = np.abs(a - b).max()
        assert (
            err <= 0.05 * scale
        ), f"step {step}: |diff| {err:.4f} vs |logits| {scale:.3f}"
        assert (
            a.argmax() == b.argmax()
        ), f"step {step}: argmax {a.argmax()} != {b.argmax()}"


@pytest.fixture(scope="module")
def cpu():
    config = TOY
    weights = _toy_weights(config)
    oracle = Phi4.oracle(config, weights)
    prompt = np.random.default_rng(7).integers(0, config.vocab_size, 8)
    tokens, expected = prompt, []
    first = logits = oracle.logits(tokens)
    for _ in range(6):
        tokens = np.append(tokens, logits.argmax())
        logits = oracle.logits(tokens)
        expected.append(logits)
    return config, weights, oracle, prompt, first, expected


def test_decode_from_an_empty_cache_matches_the_forward_token_by_token(cpu):
    config, weights, oracle, prompt, first, expected = cpu
    model = OnHost(config, weights)
    last = model.logits(prompt[:1])
    for n in range(2, len(prompt) + 1):
        last = model.logits(prompt[:n])
    _assert_close([last], [first])


def test_the_prompt_matches_the_forward_and_leaves_decode_its_caches(cpu):
    config, weights, oracle, prompt, first, expected = cpu
    model = OnHost(config, weights)
    got = model.logits(prompt)
    _assert_close([got], [first])
    history = list(prompt)
    out = []
    logits = got
    for _ in range(len(expected)):
        history.append(int(logits.argmax()))
        logits = model.logits(history)
        out.append(logits)
    _assert_close(out, expected)


def test_a_prompt_longer_than_a_chunk_runs_in_chunks():
    config = dataclasses.replace(TOY, max_seq_len=4 * TOY.prefill_chunk)
    weights = _toy_weights(config)
    model, oracle = OnHost(config, weights), Phi4.oracle(config, weights)
    tokens = np.random.default_rng(3).integers(0, config.vocab_size, 150)
    first = oracle.logits(tokens)
    _assert_close([model.logits(tokens)], [first])
    tokens = np.append(tokens, first.argmax())
    _assert_close([model.logits(tokens)], [oracle.logits(tokens)])
    tokens = np.append(tokens, np.random.default_rng(4).integers(0, 1024, 30))
    _assert_close([model.logits(tokens)], [oracle.logits(tokens)])


def test_the_accuracy_check_scores_the_model_against_the_reference(cpu):
    config, weights, oracle, prompt, first, expected = cpu
    model = OnHost(config, weights)
    results = accuracy(model, oracle, prompt, len(expected) + 1)
    assert all(top1 for _, top1 in results), results
    assert all(0 <= kl < 0.05 for kl, _ in results), results


def test_the_determinism_check_finds_the_reference_deterministic(cpu):
    config, weights, oracle, prompt, first, expected = cpu
    model = OnHost(config, weights)
    assert determinism(model, [prompt, prompt[::-1]], 3, 3) == 0
