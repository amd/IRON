#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Phi-4-mini-instruct's graph against Hugging Face's Phi-3 in float32 over
the same random weights, its logits recorded in ``goldens/``, device-free
(no checkpoint, no NPU): its partial rotary and fused qkv_proj and
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

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.phi3.model import LongRope, Phi4, Phi4Config
from iron.lm import Checkpoint, OnHost as Host, accuracy, determinism
from iron.lm.golden import HuggingFace
from iron.lm.testing import LOGITS, assert_close

pytestmark = pytest.mark.usefixtures("npu2")

#: Phi-4-mini-instruct's proportions at toy size: GQA, a fused qkv/gate_up,
#: partial rotary (half of each head).
TOY = Phi4Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=64,
    intermediate_size=512,
    rope_theta=10000.0,
    max_seq_len=256,
    partial_rotary_factor=0.5,
    prefill_chunk=256,
)


def _shapes(c: Phi4Config) -> dict[str, tuple[int, ...]]:
    E, F, V = c.hidden_size, c.intermediate_size, c.vocab_size
    Q, KV = c.num_attention_heads * c.head_dim, c.num_key_value_heads * c.head_dim
    out = {"model.embed_tokens.weight": (V, E), "model.norm.weight": (E,)}
    for i in range(c.num_hidden_layers):
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


class OnHost(Host, Phi4):
    profile = None


def _hugging_face(config, weights):
    """Hugging Face's Phi-3 on ``config`` and ``weights``; its default
    padding token lies past the toy vocabulary.
    """
    return HuggingFace.build("phi3", config, weights, pad_token_id=None)


@pytest.fixture(scope="module")
def cpu(golden):
    config = TOY
    weights = _toy_weights(config)
    reference = golden("toy", lambda: _hugging_face(config, weights), config, weights)
    prompt = np.random.default_rng(7).integers(0, config.vocab_size, 8)
    tokens, expected = prompt, []
    first = logits = reference.logits(tokens)
    for _ in range(6):
        tokens = np.append(tokens, logits.argmax())
        logits = reference.logits(tokens)
        expected.append(logits)
    return config, weights, reference, prompt, first, expected


def test_decode_from_an_empty_cache_matches_the_forward_token_by_token(cpu):
    config, weights, reference, prompt, first, expected = cpu
    model = OnHost(config, weights)
    last = model.logits(prompt[:1])
    for n in range(2, len(prompt) + 1):
        last = model.logits(prompt[:n])
    assert_close(last, first)


def test_the_prompt_matches_the_forward_and_leaves_decode_its_caches(cpu):
    config, weights, reference, prompt, first, expected = cpu
    model = OnHost(config, weights)
    got = model.logits(prompt)
    assert_close(got, first)
    history = list(prompt)
    out = []
    logits = got
    for _ in range(len(expected)):
        history.append(int(logits.argmax()))
        logits = model.logits(history)
        out.append(logits)
    for step, (a, b) in enumerate(zip(out, expected)):
        assert_close(a, b, f"step {step}")


def test_a_prompt_longer_than_a_chunk_runs_in_chunks(cpu):
    config, weights, reference, *_ = cpu
    config = dataclasses.replace(config, max_seq_len=4 * config.prefill_chunk)
    model = OnHost(config, weights)
    tokens = np.random.default_rng(3).integers(0, config.vocab_size, 150)
    first = reference.logits(tokens)
    assert_close(model.logits(tokens), first)
    tokens = np.append(tokens, first.argmax())
    assert_close(model.logits(tokens), reference.logits(tokens))
    tokens = np.append(tokens, np.random.default_rng(4).integers(0, 1024, 30))
    assert_close(model.logits(tokens), reference.logits(tokens))


def test_the_accuracy_check_scores_the_model_against_the_reference(cpu):
    config, weights, reference, prompt, first, expected = cpu
    model = OnHost(config, weights)
    results = accuracy(model, reference, prompt, len(expected) + 1)
    assert all(top1 for _, top1 in results), results
    # The toys measure at most 8e-5: a bound ten times that.
    assert all(0 <= kl < 1e-3 for kl, _ in results), results


def test_the_determinism_check_finds_the_reference_deterministic(cpu):
    config, weights, reference, prompt, first, expected = cpu
    model = OnHost(config, weights)
    assert determinism(model, [prompt, prompt[::-1]], 3, 3) == 0


#: LongRoPE at toy size: a 128-position original context, served to 512.
LONG = dataclasses.replace(
    TOY,
    max_seq_len=512,
    prefill_chunk=128,
    original_max_position_embeddings=128,
    longrope=LongRope(
        short_factor=(1.0,) * 16,
        long_factor=tuple(float(f) for f in np.geomspace(1, 32, 16)),
    ),
)


def test_a_turn_past_the_original_context_rotates_only_its_own_rows_long(golden):
    """Decision 35 on decision 50: a prompt within 128 positions rotates
    short and a first turn passing 128 long throughout, both Hugging
    Face's; a second turn passing 128 runs from its first new token, its
    own rows rotated long, the cached ones as they were written, so it
    differs from a first turn over the same tokens, and a decode step past
    128 then reads the long rows as a turn over it does. Hugging Face's
    logits are a whole forward call's, so no golden judges the second turn.
    """
    weights = _toy_weights(LONG)
    reference = golden("long", lambda: _hugging_face(LONG, weights), LONG, weights)
    model = OnHost(LONG, weights)
    tokens = np.random.default_rng(5).integers(0, LONG.vocab_size, 301)
    assert_close(model.logits(tokens[:100]), reference.logits(tokens[:100]))
    got = np.asarray(model.logits(tokens[:300]), np.float32)
    whole = reference.logits(tokens[:300])
    # Measured 64%: past twice LOGITS, so no rounding passes for it.
    assert np.abs(got - whole).max() > 2 * LOGITS * np.abs(whole).max()
    turned = OnHost(LONG, weights)
    turned.logits(tokens[:100])
    assert_close(model.logits(tokens), turned.logits(tokens))
    assert_close(OnHost(LONG, weights).logits(tokens), reference.logits(tokens))
