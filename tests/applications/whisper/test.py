#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper at a toy shape with tanh GELU, on drawn weights (no checkpoint),
against its own float32 forward pass: device-free, the encoder over a
clip's features, then the decoder's prompt chunks and a decode step over
its output, each version's reference in turn; and the same on the NPU.
The real checkpoint waits on exact GELU (the pin group) and the gaps
``iron/applications/whisper/README.md`` lists.
"""

import dataclasses

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.whisper.model import (
    Whisper,
    WhisperConfig,
    WhisperEncoder,
    WhisperEncoderOracle,
)
from iron.tests.common.llama_model import drawn

#: Whisper's proportions at toy size: 200 source positions, padded to 256,
#: as many as a prompt chunk's queries, the fewest its cross attention takes.
TOY = WhisperConfig(
    vocab_size=512,
    emb_dim=256,
    n_layers=2,
    n_heads=4,
    n_kv_groups=4,
    hidden_dim=512,
    max_seq_len=448,
    hidden_act="gelu_pytorch_tanh",
    encoder_layers=2,
    encoder_heads=4,
    encoder_hidden_dim=512,
    mels=64,
    source_positions=200,
)


def names(c: WhisperConfig) -> dict[str, tuple[int, ...]]:
    """Each tensor of a Whisper checkpoint of ``c``'s shape, by name."""
    E, V = c.emb_dim, c.vocab_size
    out = {
        "model.encoder.conv1.weight": (E, c.mels, 3),
        "model.encoder.conv1.bias": (E,),
        "model.encoder.conv2.weight": (E, E, 3),
        "model.encoder.conv2.bias": (E,),
        "model.encoder.embed_positions.weight": (c.source_positions, E),
        "model.encoder.layer_norm.weight": (E,),
        "model.encoder.layer_norm.bias": (E,),
        "model.decoder.embed_tokens.weight": (V, E),
        "model.decoder.embed_positions.weight": (c.max_seq_len, E),
        "model.decoder.layer_norm.weight": (E,),
        "model.decoder.layer_norm.bias": (E,),
    }
    stacks = [
        ("model.encoder", c.encoder_layers, c.encoder_hidden_dim, ["self_attn"]),
        ("model.decoder", c.n_layers, c.hidden_dim, ["self_attn", "encoder_attn"]),
    ]
    for stack, layers, F, attentions in stacks:
        for i in range(layers):
            p = f"{stack}.layers.{i}"
            for a in attentions:
                for proj in ("q_proj", "k_proj", "v_proj", "out_proj"):
                    out[f"{p}.{a}.{proj}.weight"] = (E, E)
                    if proj != "k_proj":
                        out[f"{p}.{a}.{proj}.bias"] = (E,)
                for part in ("weight", "bias"):
                    out[f"{p}.{a}_layer_norm.{part}"] = (E,)
            out |= {
                f"{p}.fc1.weight": (F, E),
                f"{p}.fc1.bias": (F,),
                f"{p}.fc2.weight": (E, F),
                f"{p}.fc2.bias": (E,),
                f"{p}.final_layer_norm.weight": (E,),
                f"{p}.final_layer_norm.bias": (E,),
            }
    return out


def _assert_close(got, want, what: str):
    """bf16 against float32, so within 5% of the largest value, as a
    decoder's logits are held.
    """
    got = np.asarray(got, np.float32).reshape(want.shape)
    err, scale = np.abs(got - want).max(), np.abs(want).max()
    assert err <= 0.05 * scale, f"{what}: |diff| {err:.4f} against {scale:.3f}"


@pytest.fixture(scope="module")
def clip():
    """The toy's weights and a clip's features, ``(mels, frames)``."""
    weights = drawn(TOY, names(TOY), 0)
    encoder = TOY.encoder()
    rng = np.random.default_rng(1)
    features = rng.uniform(-1, 1, (encoder.mels, encoder.frames))
    return weights, features.astype(bfloat16).astype(np.float32)


@pytest.mark.parametrize("version", [0, 1, 2], ids=["decode", "prompt", "encode"])
def test_each_version_resolves(clip, npu2, version):
    weights, _ = clip
    model = Whisper(TOY, weights)
    for op in model.trace(**model.shapes()[version]).operators:
        op.resolved(npu2)


@pytest.mark.usefixtures("npu2")
def test_the_encoder_s_output_matches_its_oracle(clip):
    weights, features = clip
    encoder = WhisperEncoder(TOY.encoder(), weights)
    buffer, values = encoder.inputs(features)
    got = np.asarray(encoder.reference(buffer, **values), np.float32)
    want = WhisperEncoderOracle(TOY.encoder(), weights).soft_tokens(features)
    # 200 positions of the 256 rows the layers take.
    assert got.shape == want.shape == (TOY.source_positions, TOY.emb_dim)
    _assert_close(got, want, "the encoder's output")


@pytest.mark.usefixtures("npu2")
def test_the_decoder_attends_over_the_encoded_clip(clip):
    """The encode version, then two prompt chunks and a decode step, each
    reference carrying its states to the next, against the oracle encoded
    with the same clip.
    """
    weights, features = clip
    model, oracle = Whisper(TOY, weights), Whisper.oracle(TOY, weights)
    buffer, own = model.encoder.inputs(features)
    source = model.encoder.soft(own)
    values = dict(token=0, position=0, chunk=0, rows=1, source=source)
    model.reference(None, buffer, **values, encoder_n=own["n"])
    oracle.encode(oracle.encoder.soft_tokens(features))
    tokens = np.random.default_rng(2).integers(0, TOY.vocab_size, 300)
    C = TOY.prefill_chunk
    for begin in range(0, tokens.size, C):
        chunk = tokens[begin : begin + C]
        values = dict(
            token=int(chunk[-1]),
            position=begin + chunk.size - 1,
            chunk=begin // C,
            rows=chunk.size,
            source=source,
            encoder_n=0,
        )
        logits, carry = model.reference(model.prompt_ids(chunk), **values)
    _assert_close(logits, oracle.logits(tokens), "the prompt's logits")
    tokens = np.append(tokens, carry["token"])
    logits, _ = model.reference(chunk=0, rows=1, encoder_n=0, **carry)
    _assert_close(logits, oracle.logits(tokens), "a decode step's logits")


def test_whisper_s_exact_gelu_is_refused_until_its_kernel():
    """The checkpoint's own ``gelu`` (exact): no operator yet."""
    exact = dataclasses.replace(TOY, hidden_act="gelu")
    with pytest.raises(ValueError, match="'gelu'"):
        Whisper(exact, drawn(TOY, names(TOY), 0))


@pytest.mark.supported_devices("npu2")
def test_whisper_toy_on_the_device(clip):
    """The encode version, the prompt's two chunks and two decode steps,
    each within 5% of the oracle's largest logit, as the references are.
    """
    weights, features = clip
    model = Whisper(TOY, weights).load()
    oracle = Whisper.oracle(TOY, weights)
    model.encode(features)
    oracle.encode(oracle.encoder.soft_tokens(features))
    tokens = list(np.random.default_rng(2).integers(0, TOY.vocab_size, 300))
    for _ in range(3):
        want = oracle.logits(tokens)
        _assert_close(model.logits(tokens), want, f"{len(tokens)} tokens")
        tokens.append(int(want.argmax()))
