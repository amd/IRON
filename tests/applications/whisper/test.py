#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper at a toy shape with tanh GELU, on drawn weights (no checkpoint),
against Hugging Face's own model in float32 over the same weights, its
logits recorded in ``goldens/``: device-free, the encoder over a clip's
samples, then the decoder's prompt chunks and a decode step over its
output, each version's reference in turn; and the same on the NPU, with
tanh and exact GELU. Then large-v3-turbo from its checkpoint on the NPU
over a LibriSpeech clip, against transformers' logits recorded beside it.
"""

import dataclasses

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.whisper.model import Whisper, WhisperConfig, WhisperEncoder
from iron.lm.generation import divergence
from iron.lm.testing import LOGITS, assert_close, require, weights_dir
from iron.tests.support.llama_model import checkpoint
from iron.tests.support.librispeech import utterance
from iron.tests.support.llama_reference import prompt

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
#: The toy with Whisper's own GELU, the exact one.
EXACT = dataclasses.replace(TOY, hidden_act="gelu")

DIRECTORY = weights_dir("whisper-large-v3-turbo")
#: A LibriSpeech test-clean utterance, 7.3 s of speech.
SPEECH = "4446-2275-0016"


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


def drawn_audio(seconds: float) -> np.ndarray:
    """``seconds`` of a rising tone in noise at 16 kHz, float32."""
    t = np.arange(int(16000 * seconds)) / 16000
    rng = np.random.default_rng(1)
    tone = 0.3 * np.sin(2 * np.pi * (200 * t + 300 * t**2))
    return (tone + 0.05 * rng.standard_normal(t.size)).astype(np.float32)


@pytest.fixture(scope="module")
def clip():
    """The toy's weights and 3 s of audio, short of its 4 s clip."""
    weights = checkpoint(TOY, names(TOY)).tree("random")
    return weights, drawn_audio(3.0)


@pytest.fixture(scope="module", params=[TOY, EXACT], ids=["tanh_gelu", "exact_gelu"])
def toy(request):
    """The toy, with tanh GELU and with exact."""
    return request.param


@pytest.fixture(scope="module")
def reference(clip, golden, toy):
    """Hugging Face's logits over the toy's weights after the clip."""
    weights, _ = clip

    # transformers and torch, optional: only recording a golden imports them
    def record():
        from iron.applications.whisper.hugging_face import HuggingFaceWhisper

        return HuggingFaceWhisper.build("whisper", toy, weights, pad_token_id=None)

    return golden("toy" if toy is TOY else "toy_exact", record, toy, weights)


@pytest.mark.parametrize("version", [0, 1, 2], ids=["decode", "prompt", "encode"])
def test_each_version_resolves(clip, npu2, version):
    weights, _ = clip
    model = Whisper(TOY, weights)
    for op in model.record(**model.shapes()[version]).operators:
        op.resolved(npu2)


class Encoder:
    """Hugging Face's encoder over the toy's weights, what records
    ``goldens/encoder.npz``: its output over a clip's samples' features,
    rounded to bf16 to keep the file small, a hundredth of the bound it is
    held to.
    """

    def __init__(self, weights):
        from iron.applications.whisper.hugging_face import HuggingFaceWhisper

        self.whisper = HuggingFaceWhisper.build(
            "whisper", TOY, weights, pad_token_id=None
        )

    def logits(self, tokens, audio):
        import torch

        features = torch.from_numpy(self.whisper.features(audio))[None]
        with torch.no_grad():
            out = self.whisper.model.model.encoder(features).last_hidden_state[0]
        return out.numpy().astype(bfloat16).astype(np.float32)


@pytest.mark.usefixtures("npu2")
def test_the_encoder_s_output_is_hugging_face_s(clip, golden):
    """The encoder judged alone: through the decoder, another clip moves
    the logits by less than the bound they are held to.
    """
    weights, audio = clip
    encoder = WhisperEncoder(TOY.encoder(), weights)
    buffer, values = encoder.inputs(audio)
    got = np.asarray(encoder.reference(buffer, **values), np.float32)
    want = golden("encoder", lambda: Encoder(weights), TOY, weights).logits([], audio)
    # 200 positions of the 256 rows the layers take.
    assert got.shape == want.shape == (TOY.max_source_positions, TOY.hidden_size)
    # bf16 against float32, held as a decoder's logits are: measured 0.87%.
    err, scale = np.abs(got - want).max(), np.abs(want).max()
    assert err <= LOGITS * scale, f"|diff| {err:.4f} against {scale:.3f}"


@pytest.mark.usefixtures("npu2")
def test_the_decoder_attends_over_the_encoded_clip(clip, toy, reference):
    """The encode version, then two prompt chunks and a decode step, each
    reference carrying its states to the next, against Hugging Face's
    logits after the same clip.
    """
    weights, audio = clip
    model = Whisper(toy, weights)
    buffer, own = model.encoder.inputs(audio)
    source = model.encoder.soft(own)
    values = dict(token=0, position=0, start=0, rows=1, rope_start=0, source=source)
    model.reference(None, buffer, **values, encoder_rows=own["rows"])
    tokens = np.random.default_rng(2).integers(0, TOY.vocab_size, 300)
    logits, carry = prompt(model, tokens, source=source, encoder_rows=0)
    assert_close(logits, reference.logits(tokens, audio), "the prompt's logits")
    tokens = np.append(tokens, carry["token"])
    logits, _ = model.reference(start=0, rows=1, rope_start=0, encoder_rows=0, **carry)
    want = reference.logits(tokens, audio)
    assert_close(logits, want, "a decode step's logits")


@pytest.mark.supported_devices("npu2")
def test_whisper_toy_on_the_device(clip, toy, reference):
    """The encode version, the prompt's two chunks and two decode steps,
    each within 5% of Hugging Face's largest logit, as the references are.
    """
    weights, audio = clip
    model = Whisper(toy, weights).load_versions()
    model.encode(audio)
    tokens = list(np.random.default_rng(2).integers(0, TOY.vocab_size, 300))
    for _ in range(3):
        want = reference.logits(tokens, audio)
        assert_close(model.logits(tokens), want, f"{len(tokens)} tokens")
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

    def record():
        from iron.applications.whisper.hugging_face import HuggingFaceWhisper

        return HuggingFaceWhisper.build("whisper", TOY, weights, pad_token_id=None)

    reference = golden("toy_f16", record, TOY, weights)
    assert model.model.embed_tokens.weight.dtype == bfloat16
    audio = drawn_audio(3.0)
    buffer, own = model.encoder.inputs(audio)
    source = model.encoder.soft(own)
    values = dict(token=0, position=0, start=0, rows=1, rope_start=0, source=source)
    model.reference(None, buffer, **values, encoder_rows=own["rows"])
    tokens = np.random.default_rng(2).integers(0, TOY.vocab_size, 100)
    logits, _ = prompt(model, tokens, source=source, encoder_rows=0)
    assert_close(logits, reference.logits(tokens, audio), "the prompt's logits")


# The bound on each step's KL(float32 forward || device).
MAX_KL = 0.05


@pytest.fixture(scope="module")
def large():
    """large-v3-turbo from its checkpoint, compiled and loaded once."""
    require(
        DIRECTORY / "model.safetensors",
        DIRECTORY / "config.json",
        DIRECTORY / "tokenizer.json",
        staged=False,
    )
    yield Whisper.load(DIRECTORY)
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


@pytest.mark.bench
@pytest.mark.supported_devices("npu2")
def test_whisper_large_v3_turbo_accuracy(large, record_property):
    """A LibriSpeech clip, then the transcript's preamble and three decode
    steps: each next-token distribution against transformers', teacher-forced.
    KL is held to its bound and a top-1 mismatch recorded.
    """
    audio = utterance(SPEECH)
    large.encode(audio)
    reference = large.cpu_reference()
    tokens = large.tokenizer("<|en|><|transcribe|><|notimestamps|>")
    results = []
    for _ in range(4):
        want = reference.logits(tokens, audio)
        results.append(divergence(want, large.logits(tokens)))
        tokens.append(int(want.argmax()))
    worst = max(kl for kl, _ in results)
    record_property("MaxKL", worst)
    record_property("Top1Mismatches", sum(not top1 for _, top1 in results))
    assert worst <= MAX_KL, f"KL {worst} > {MAX_KL}"
