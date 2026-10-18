#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper at a toy shape with tanh GELU, on drawn weights (no checkpoint),
against Hugging Face's own model in float32 over the same weights, its
logits recorded in ``goldens/``: device-free, the encoder over a clip's
features, then the decoder's prompt chunks and a decode step over its
output, each version's reference in turn; and the same on the NPU.
The real checkpoint waits on exact GELU (the pin group) and the gaps
``iron/applications/whisper/README.md`` lists.
"""

import dataclasses

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.whisper.hugging_face import HuggingFaceWhisper
from iron.applications.whisper.model import Whisper, WhisperConfig, WhisperEncoder
from iron.tests.common.llama_model import checkpoint

#: Whisper's proportions at toy size: 200 source positions, padded to 256,
#: as many as a prompt chunk's queries, the fewest its cross attention takes.
TOY = WhisperConfig(
    vocab_size=512,
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    num_key_value_heads=4,
    intermediate_size=512,
    max_seq_len=448,
    hidden_act="gelu_pytorch_tanh",
    encoder_layers=2,
    encoder_attention_heads=4,
    encoder_ffn_dim=512,
    num_mel_bins=64,
    max_source_positions=200,
)


def names(c: WhisperConfig) -> dict[str, tuple[int, ...]]:
    """Each tensor of a Whisper checkpoint of ``c``'s shape, by name."""
    E, V = c.hidden_size, c.vocab_size
    out = {
        "model.encoder.conv1.weight": (E, c.num_mel_bins, 3),
        "model.encoder.conv1.bias": (E,),
        "model.encoder.conv2.weight": (E, E, 3),
        "model.encoder.conv2.bias": (E,),
        "model.encoder.embed_positions.weight": (c.max_source_positions, E),
        "model.encoder.layer_norm.weight": (E,),
        "model.encoder.layer_norm.bias": (E,),
        "model.decoder.embed_tokens.weight": (V, E),
        "model.decoder.embed_positions.weight": (c.max_seq_len, E),
        "model.decoder.layer_norm.weight": (E,),
        "model.decoder.layer_norm.bias": (E,),
    }
    stacks = [
        ("model.encoder", c.encoder_layers, c.encoder_ffn_dim, ["self_attn"]),
        (
            "model.decoder",
            c.num_hidden_layers,
            c.intermediate_size,
            ["self_attn", "encoder_attn"],
        ),
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
    """The toy's weights and a clip's features, ``(num_mel_bins, frames)``."""
    weights = checkpoint(TOY, names(TOY)).tree("random")
    encoder = TOY.encoder()
    rng = np.random.default_rng(1)
    features = rng.uniform(-1, 1, (encoder.num_mel_bins, encoder.frames))
    return weights, features.astype(bfloat16).astype(np.float32)


@pytest.fixture(scope="module")
def reference(clip, golden):
    """Hugging Face's logits over the toy's weights after the clip."""
    weights, _ = clip
    return golden(
        "toy",
        lambda: HuggingFaceWhisper.build("whisper", TOY, weights, pad_token_id=None),
        TOY,
        weights,
    )


@pytest.mark.parametrize("version", [0, 1, 2], ids=["decode", "prompt", "encode"])
def test_each_version_resolves(clip, npu2, version):
    weights, _ = clip
    model = Whisper(TOY, weights)
    for op in model.trace(**model.shapes()[version]).operators:
        op.resolved(npu2)


class Encoder:
    """Hugging Face's encoder over the toy's weights, what records
    ``goldens/encoder.npz``: its output over a clip's features, rounded to bf16 to keep the file small, a hundredth of
    the bound it is held to.
    """

    def __init__(self, weights):
        self.encoder = HuggingFaceWhisper.build(
            "whisper", TOY, weights, pad_token_id=None
        ).model.model.encoder

    def logits(self, tokens, features):
        import torch

        features = torch.from_numpy(np.asarray(features, np.float32))[None]
        with torch.no_grad():
            out = self.encoder(features).last_hidden_state[0]
        return out.numpy().astype(bfloat16).astype(np.float32)


@pytest.mark.usefixtures("npu2")
def test_the_encoder_s_output_is_hugging_face_s(clip, golden):
    """The encoder judged alone: through the decoder, another clip moves
    the logits by less than the bound they are held to.
    """
    weights, features = clip
    encoder = WhisperEncoder(TOY.encoder(), weights)
    buffer, values = encoder.inputs(features)
    got = np.asarray(encoder.reference(buffer, **values), np.float32)
    want = golden("encoder", lambda: Encoder(weights), TOY, weights).logits(
        [], features
    )
    # 200 positions of the 256 rows the layers take.
    assert got.shape == want.shape == (TOY.max_source_positions, TOY.hidden_size)
    _assert_close(got, want, "the encoder's output")


@pytest.mark.usefixtures("npu2")
def test_the_decoder_attends_over_the_encoded_clip(clip, reference):
    """The encode version, then two prompt chunks and a decode step, each
    reference carrying its states to the next, against Hugging Face's
    logits after the same clip.
    """
    weights, features = clip
    model = Whisper(TOY, weights)
    buffer, own = model.encoder.inputs(features)
    source = model.encoder.soft(own)
    values = dict(token=0, position=0, start=0, rows=1, rope_start=0, source=source)
    model.reference(None, buffer, **values, encoder_rows=own["rows"])
    tokens = np.random.default_rng(2).integers(0, TOY.vocab_size, 300)
    C = TOY.prefill_chunk
    for begin in range(0, tokens.size, C):
        chunk = tokens[begin : begin + C]
        values = dict(
            token=int(chunk[-1]),
            position=begin + chunk.size - 1,
            start=begin,
            rope_start=begin,
            rows=chunk.size,
            source=source,
            encoder_rows=0,
        )
        logits, carry = model.reference(model.prompt_ids(chunk), **values)
    _assert_close(logits, reference.logits(tokens, features), "the prompt's logits")
    tokens = np.append(tokens, carry["token"])
    logits, _ = model.reference(start=0, rows=1, rope_start=0, encoder_rows=0, **carry)
    want = reference.logits(tokens, features)
    _assert_close(logits, want, "a decode step's logits")


def test_whisper_s_exact_gelu_is_refused_until_its_kernel():
    """The checkpoint's own ``gelu`` (exact): no operator yet."""
    exact = dataclasses.replace(TOY, hidden_act="gelu")
    with pytest.raises(ValueError, match="'gelu'"):
        Whisper(exact, checkpoint(TOY, names(TOY)).tree("random"))


@pytest.mark.supported_devices("npu2")
def test_whisper_toy_on_the_device(clip, reference):
    """The encode version, the prompt's two chunks and two decode steps,
    each within 5% of Hugging Face's largest logit, as the references are.
    """
    weights, features = clip
    model = Whisper(TOY, weights).load()
    model.encode(features)
    tokens = list(np.random.default_rng(2).integers(0, TOY.vocab_size, 300))
    for _ in range(3):
        want = reference.logits(tokens, features)
        _assert_close(model.logits(tokens), want, f"{len(tokens)} tokens")
        tokens.append(int(want.argmax()))


@pytest.mark.usefixtures("npu2")
def test_an_fp16_checkpoint_is_rounded_once_for_the_device(golden):
    """Whisper ships float16: the graph holds each weight rounded once to
    bf16 (``bf16``), Hugging Face's model the float16 itself, and the prompt's logits
    stay within the bound the bf16 checkpoint's are held to (0.66% of the
    largest logit, against 0.62% from a bf16 checkpoint).
    """
    weights = checkpoint(TOY, names(TOY), "F16").tree("random")
    assert weights.model.decoder.embed_tokens.weight.dtype == np.float16
    model = Whisper(TOY, weights)
    reference = golden(
        "toy_f16",
        lambda: HuggingFaceWhisper.build("whisper", TOY, weights, pad_token_id=None),
        TOY,
        weights,
    )
    assert model.decoder.embed_tokens.weight.dtype == bfloat16
    features = np.random.default_rng(1).uniform(
        -1, 1, (TOY.num_mel_bins, 2 * TOY.max_source_positions)
    )
    features = features.astype(bfloat16).astype(np.float32)
    buffer, own = model.encoder.inputs(features)
    source = model.encoder.soft(own)
    values = dict(token=0, position=0, start=0, rows=1, rope_start=0, source=source)
    model.reference(None, buffer, **values, encoder_rows=own["rows"])
    tokens = np.random.default_rng(2).integers(0, TOY.vocab_size, 100)
    logits, _ = model.reference(
        model.prompt_ids(tokens),
        token=int(tokens[-1]),
        position=99,
        start=0,
        rows=100,
        rope_start=0,
        source=source,
        encoder_rows=0,
    )
    _assert_close(logits, reference.logits(tokens, features), "the prompt's logits")
