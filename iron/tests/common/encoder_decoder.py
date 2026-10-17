# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.EncoderDecoder``, device-free, on a tiny Whisper-shaped
decoder (tanh GELU, no RoPE, a learned position table, a tied head) over a
tower whose output is the rows it is given: its signature and versions,
what each traces, and each version's reference in turn, the encoder's keys
and values carried in states to the prompt chunks and the decode step,
against its oracle.
"""

from types import SimpleNamespace

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.lm import DecoderConfig, EncoderDecoder, EncoderDecoderOracle, widen
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.rope import RoPE
from iron.tests.common.layer import decoder, shapes
from iron.tests.common.llama_reference import _assert_close
from iron.tests.common.multimodal import Features

pytestmark = pytest.mark.usefixtures("npu2")

CONFIG = DecoderConfig(
    vocab_size=1024,
    emb_dim=512,
    n_layers=2,
    n_heads=8,
    n_kv_groups=8,
    head_dim=64,
    hidden_dim=1024,
    rope_base=None,
    max_seq_len=512,
    prefill_chunk=256,
    hidden_act="gelu_pytorch_tanh",
    eps=1e-5,
)
# The encoder's rows: as many as a prompt chunk's, the fewest its MHA takes.
SOURCE = 256


class Whisper(EncoderDecoder):
    """A Whisper-shaped decoder: its positions a learned table's rows, its
    head the final LayerNorm and the embedding.
    """

    def positions(self, x, step):
        c = self.config
        L, C, E = c.max_seq_len, c.prefill_chunk, c.emb_dim
        table = iron.weight(self.decoder.embed_positions.weight)
        if step.prompt:
            rows = Copy.step(table.reshape(L // C, C, E)[step.chunk, : step.rows])
        else:
            rows = Copy.step(table[step.position]).reshape(1, E)
        return ElementwiseAdd.step(x, rows)

    def head(self, x):
        h = self.config.layer(0).norm(x, self.decoder.layer_norm)
        return GEMV.step(self.decoder.embed_tokens.weight, h)


class WhisperOracle(EncoderDecoderOracle):
    def positions(self, x):
        return x + widen(self.decoder.embed_positions.weight[: x.shape[0]])

    def head(self, x):
        return self.normed(x, widen(self.decoder.layer_norm)) @ self.embedding.T


Whisper.oracle = WhisperOracle


def tree(seed: int):
    """A checkpoint tree of ``CONFIG``'s shape under ``model.decoder``, bf16."""
    rng = np.random.default_rng(seed)
    c = CONFIG
    E, V, L = c.emb_dim, c.vocab_size, c.max_seq_len
    shape = shapes(E, c.n_heads, c.n_kv_groups, c.head_dim, c.hidden_dim)
    layers = [decoder(rng, shape, bfloat16) for _ in range(c.n_layers)]
    norm = SimpleNamespace(
        weight=(1 + rng.standard_normal(E) / 8).astype(bfloat16),
        bias=(rng.standard_normal(E) / 8).astype(bfloat16),
    )
    return SimpleNamespace(
        model=SimpleNamespace(
            decoder=SimpleNamespace(
                embed_tokens=SimpleNamespace(
                    weight=(rng.standard_normal((V, E)) / 4).astype(bfloat16)
                ),
                embed_positions=SimpleNamespace(
                    weight=(rng.standard_normal((L, E)) / 4).astype(bfloat16)
                ),
                layers=layers,
                layer_norm=norm,
            )
        )
    )


@pytest.fixture(scope="module")
def whisper():
    """The model over a ``Features`` tower of ``SOURCE`` rows, its oracle,
    a clip of 200 encoder rows and 300 tokens, two prompt chunks.
    """
    weights = tree(0)
    encoder = Features(CONFIG.emb_dim, SOURCE)
    model = Whisper(CONFIG, weights, encoder, weights.model.decoder)
    oracle = Whisper.oracle(CONFIG, weights, weights.model.decoder)
    rng = np.random.default_rng(1)
    clip = (rng.standard_normal((200, CONFIG.emb_dim)) / 2).astype(bfloat16)
    tokens = rng.integers(0, CONFIG.vocab_size, 300)
    return model, oracle, clip, tokens


def test_its_signature_and_versions_are_the_decoder_s_and_the_encoder_s(whisper):
    model, *_ = whisper
    assert list(model.signature().parameters) == [
        "ids",
        "encoder_features",
        "token",
        "position",
        "chunk",
        "rows",
        "source",
        "encoder_n",
    ]
    assert [sorted(s) for s in model.shapes()] == [[], ["ids"], ["encoder_features"]]
    assert [s.shape for s in model.cross_keys] == [(SOURCE, 8, 64)] * 2


def test_the_encode_version_writes_each_layer_s_keys_and_values(whisper):
    model, *_ = whisper
    traced = model.trace(**model.shapes()[2])
    names = [type(s.op).__name__ for s in traced.steps]
    # The tower's copy, then per layer k and v projected and written.
    assert names.count("GEMM") == 4 and "MHA" not in names
    assert sorted(traced.reads) == ["encoder_n", "position", "source", "token"]


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


def test_each_version_s_reference_in_turn_is_the_oracle(whisper):
    """The encode version, then two prompt chunks and a decode step, each
    reference carrying its states to the next: the oracle's logits after
    the same clip and tokens, and not after another clip's; and the
    source rows bound the cross attention.
    """
    model, oracle, clip, tokens = whisper
    buffer, own = model.encoder.inputs(clip)
    source = model.encoder.soft(own)
    values = dict(token=0, position=0, chunk=0, rows=1, source=source)
    model.reference(None, buffer, **values, encoder_n=own["n"])
    logits, carry = prompt(model, tokens, source)
    assert carry["source"] == source
    oracle.encode(clip)
    got, want = np.asarray(logits, np.float32).reshape(-1), oracle.logits(tokens)
    _assert_close([got], [want])
    # Rows past the source move the logits further than the model's own
    # error does.
    past, _ = prompt(model, tokens, SOURCE)
    assert (
        np.abs(np.asarray(past, np.float32).reshape(-1) - got).max()
        > np.abs(got - want).max()
    )
    logits, carry = prompt(model, tokens, source)
    tokens = np.append(tokens, carry["token"])
    logits, _ = model.reference(chunk=0, rows=1, encoder_n=0, **carry)
    _assert_close([np.asarray(logits).reshape(-1)], [oracle.logits(tokens)])
    oracle.encode(clip[: source // 2])
    with pytest.raises(AssertionError):
        _assert_close([np.asarray(logits).reshape(-1)], [oracle.logits(tokens)])


def prompt(model, tokens, source: int):
    """Each prompt chunk's reference over ``tokens`` in turn, attending over
    ``source`` rows of the encoder's output: the last chunk's logits and
    carry.
    """
    C = CONFIG.prefill_chunk
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
        out = model.reference(model.prompt_ids(chunk), **values)
    return out
