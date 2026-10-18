# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.EncoderDecoder``, device-free, on a tiny Whisper-shaped
decoder (tanh GELU, no RoPE, a learned position table, a tied head) over a
tower whose output is the rows it is given: its signature and versions,
what each traces, and each version's reference in turn, the encoder's keys
and values carried in states to the prompt chunks and the decode step,
against Hugging Face's own Whisper decoder in float32 over the same
weights and encoder rows, its logits recorded in ``goldens/``.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron.applications.whisper.model import RENAMES, WhisperConfig
from iron.lm import EncoderDecoder
from iron.lm.golden import HuggingFace
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.rope import RoPE
from iron.tests.common.layer import WHISPER, shapes
from iron.tests.common.llama_model import checkpoint
from iron.lm.testing import assert_close
from iron.tests.common.llama_reference import prompt
from iron.tests.common.multimodal import Features

pytestmark = pytest.mark.usefixtures("npu2")


# The encoder's rows: as many as a prompt chunk's, the fewest its MHA takes.
SOURCE = 256
# Whisper's decoder; the encoder's fields only fill transformers' config.
CONFIG = WhisperConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=8,
    intermediate_size=1024,
    max_seq_len=512,
    hidden_act="gelu_pytorch_tanh",
    encoder_layers=0,
    encoder_attention_heads=8,
    encoder_ffn_dim=1024,
    num_mel_bins=80,
    max_source_positions=SOURCE,
)


class Whisper(EncoderDecoder):
    """A Whisper-shaped decoder: its positions a learned table's rows, its
    head the final LayerNorm and the embedding.
    """

    def positions(self, x, step):
        c = self.config
        C, E = c.prefill_chunk, c.hidden_size
        table = iron.weight(self.decoder.embed_positions.weight)
        if step.prompt:
            rows = Copy.step(table[step.start : step.start + C][: step.rows])
        else:
            rows = Copy.step(table[step.position]).reshape(1, E)
        return ElementwiseAdd.step(x, rows)

    renames = RENAMES

    def head(self, x):
        n = self.decoder.layer_norm
        h = F.layer_norm(x, x.shape[-1:], n.weight, n.bias, self.config.eps)
        return GEMV.step(self.decoder.embed_tokens.weight, h)


class HuggingFaceDecoder(HuggingFace):
    """transformers' Whisper decoder alone (``WhisperForCausalLM``), what
    records a golden: the logits after the tokens, attending over the
    encoder's output rows given beside them.
    """

    def logits(self, tokens, rows) -> np.ndarray:
        import torch

        with torch.no_grad():
            out = self.model(
                torch.tensor([list(tokens)]),
                encoder_outputs=(torch.from_numpy(np.asarray(rows, np.float32))[None],),
                use_cache=False,
            )
        return out.logits[0, -1].numpy()


def names(c: WhisperConfig) -> dict[str, tuple[int, ...]]:
    """Each tensor of a Whisper decoder of ``c``'s shape, by name: every
    projection biased but the keys', as Whisper's, every norm affine.
    """
    E, V = c.hidden_size, c.vocab_size
    H, D, F = c.num_attention_heads, c.head_dim, c.intermediate_size
    shape = shapes(E, H, H, D, F)
    d = "model.decoder"
    out = {
        f"{d}.embed_tokens.weight": (V, E),
        f"{d}.embed_positions.weight": (c.max_seq_len, E),
        f"{d}.layer_norm.weight": (E,),
        f"{d}.layer_norm.bias": (E,),
    }
    for i in range(c.num_hidden_layers):
        for name in WHISPER:
            out[f"{d}.layers.{i}.{name}.weight"] = shape[name]
            if not name.endswith("k_proj"):
                out[f"{d}.layers.{i}.{name}.bias"] = shape[name][:1]
    return out


def tree():
    """A random checkpoint tree of ``CONFIG``'s decoder, bf16."""
    return checkpoint(CONFIG, names(CONFIG)).tree("random")


@pytest.fixture(scope="module")
def reference(golden):
    """Hugging Face's logits over ``tree()`` after tokens and encoder rows."""
    weights = tree()
    return golden(
        "encoder_decoder",
        lambda: HuggingFaceDecoder.build("whisper", CONFIG, weights, pad_token_id=None),
        CONFIG,
        weights,
    )


@pytest.fixture(scope="module")
def whisper(reference):
    """The model over a ``Features`` tower of ``SOURCE`` rows, a clip of 200
    encoder rows, Hugging Face's logits, and 300 tokens, two prompt chunks.
    """
    weights = tree()
    encoder = Features(CONFIG.hidden_size, SOURCE)
    model = Whisper(CONFIG, weights, encoder, weights.model.decoder)
    rng = np.random.default_rng(1)
    clip = (rng.standard_normal((200, CONFIG.hidden_size)) / 2).astype(bfloat16)
    tokens = rng.integers(0, CONFIG.vocab_size, 300)
    return model, clip, reference, tokens


def test_its_signature_and_versions_are_the_decoder_s_and_the_encoder_s(whisper):
    model, *_ = whisper
    assert list(model.signature().parameters) == [
        "ids",
        "encoder_features",
        "token",
        "position",
        "start",
        "rows",
        "rope_start",
        "source",
        "encoder_rows",
    ]
    assert [sorted(s) for s in model.shapes()] == [[], ["ids"], ["encoder_features"]]
    assert [s.shape for s in model.cross_keys] == [(SOURCE, 8, 64)] * 2


def test_the_encode_version_writes_each_layer_s_keys_and_values(whisper):
    model, *_ = whisper
    traced = model.trace(**model.shapes()[2])
    names = [type(s.op).__name__ for s in traced.steps]
    # The tower's copy, then per layer k and v projected and written.
    assert names.count("ProjectionGEMM") == 4 and "MHA" not in names
    assert sorted(traced.reads) == ["encoder_rows", "position", "source", "token"]


@pytest.mark.parametrize("version", [0, 1])
def test_a_decoder_version_attends_over_the_source_rows_it_carries(whisper, version):
    model, *_ = whisper
    traced = model.trace(**model.shapes()[version])
    dev = aie_utils.get_current_device()
    for s in traced.steps:
        s.op.resolved(dev)
    attention = [s.op for s in traced.steps if isinstance(s.op, MHA)]
    # Per layer, the causal attention over the caches, then the cross.
    assert [op.causal for op in attention] == [True, False] * 2
    assert not any(isinstance(s.op, RoPE) for s in traced.steps)
    assert "source" in traced.reads


def test_each_version_s_reference_in_turn_is_hugging_face_s(whisper):
    """The encode version, then two prompt chunks and a decode step, each
    reference carrying its states to the next: Hugging Face's logits after
    the same clip and tokens, and not after another clip's; and the
    source rows bound the cross attention.
    """
    model, clip, reference, tokens = whisper
    buffer, own = model.encoder.inputs(clip)
    source = model.encoder.soft(own)
    values = dict(token=0, position=0, start=0, rows=1, rope_start=0, source=source)
    model.reference(None, buffer, **values, encoder_rows=own["rows"])
    logits, carry = prompt(model, tokens, source=source, encoder_rows=0)
    assert carry["source"] == source
    got = np.asarray(logits, np.float32).reshape(-1)
    want = reference.logits(tokens, clip)
    assert_close(got, want)
    # Rows past the source move the logits further than the model's own
    # error does.
    past, _ = prompt(model, tokens, source=SOURCE, encoder_rows=0)
    assert (
        np.abs(np.asarray(past, np.float32).reshape(-1) - got).max()
        > np.abs(got - want).max()
    )
    logits, carry = prompt(model, tokens, source=source, encoder_rows=0)
    tokens = np.append(tokens, carry["token"])
    logits, _ = model.reference(start=0, rows=1, rope_start=0, encoder_rows=0, **carry)
    got = np.asarray(logits).reshape(-1)
    assert_close(got, reference.logits(tokens, clip))
    with pytest.raises(AssertionError):
        assert_close(got, reference.logits(tokens, clip[:100]))


def test_a_decoder_call_before_any_encode_is_refused(whisper):
    model, *_ = whisper
    with pytest.raises(RuntimeError, match=r"encode\(\) first"):
        model.call_values()


class Attending(Features):
    """A ``Features`` tower whose one layer attends its rows to themselves,
    bounded to its ``rows``."""

    def __init__(self, width: int, rows: int):
        super().__init__(width, rows)
        self.layers = [None]

    def layer(self, step, i, weights, x):
        q = x.reshape(x.shape[0], CONFIG.num_attention_heads, CONFIG.head_dim)
        return self.attend(step, i, q, q, q)


def attended(rows) -> np.ndarray:
    """``rows`` attended to themselves per head in float32, as ``Attending``'s
    layer does, rounded once to bf16.
    """
    H, D = CONFIG.num_attention_heads, CONFIG.head_dim
    h = np.asarray(rows, np.float32).reshape(-1, H, D).transpose(1, 0, 2)
    p = h @ h.transpose(0, 2, 1) * np.float32(D**-0.5)
    p = np.exp(p - p.max(-1, keepdims=True))
    p /= p.sum(-1, keepdims=True)
    out = (p @ h).transpose(1, 0, 2).reshape(rows.shape[0], H * D)
    return out.astype(bfloat16)


def run(model, buffer, n: int, source: int, tokens) -> np.ndarray:
    """The encode version's reference on ``buffer``, ``n`` of its rows
    valid, then the prompt chunks' over ``tokens`` reading ``source`` rows:
    the last chunk's logits.
    """
    values = dict(token=0, position=0, start=0, rows=1, rope_start=0, source=source)
    model.reference(None, buffer, **values, encoder_rows=n)
    logits, _ = prompt(model, tokens, source=source, encoder_rows=0)
    return np.asarray(logits, np.float32).reshape(-1)


def test_padded_encoder_rows_reach_neither_attention(reference):
    """A clip of 200 rows padded to 256 with rows far from any real one, and
    a longer clip's rows left in the cross states past them: the encoder's
    self-attention (bounded by its ``rows``) and the decoder's cross attention
    (by ``source``) read neither, so the logits are a zero-padded clip's on
    a fresh model bit for bit, and Hugging Face's over the 200 rows. Bounded
    to all 256 rows, they are not.
    """
    weights = tree()
    rng = np.random.default_rng(2)
    clip = (rng.standard_normal((200, CONFIG.hidden_size)) / 2).astype(bfloat16)
    tokens = rng.integers(0, CONFIG.vocab_size, 300)
    garbage = (rng.standard_normal((SOURCE, CONFIG.hidden_size)) * 4).astype(bfloat16)

    def model():
        return Whisper(
            CONFIG,
            weights,
            Attending(CONFIG.hidden_size, SOURCE),
            weights.model.decoder,
        )

    fresh = model()
    buffer, own = fresh.encoder.inputs(clip)
    n = fresh.encoder.soft(own)
    clean = run(fresh, buffer, n, n, tokens)

    stale = model()
    run(stale, garbage, SOURCE, SOURCE, tokens)
    padded = buffer.copy()
    padded[n:] = garbage[n:]
    np.testing.assert_array_equal(run(stale, padded, n, n, tokens), clean)

    want = reference.logits(tokens, attended(clip))
    assert_close(clean, want)
    leaked = run(model(), padded, SOURCE, SOURCE, tokens)
    assert np.abs(leaked - clean).max() > np.abs(clean - want).max()


def test_an_encoder_shorter_than_a_prompt_chunk_is_refused():
    """MHA takes a chunk's queries as the last rows of the keys, so a cross
    attention over fewer rows has none to compile.
    """
    weights = tree()
    with pytest.raises(ValueError, match="fewer than a 256-row prompt chunk"):
        Whisper(
            CONFIG, weights, Features(CONFIG.hidden_size, 128), weights.model.decoder
        )
