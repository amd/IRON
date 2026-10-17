# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.Multimodal``, device-free: its signature from its text model's
and towers', the versions a mixed call runs, and their references in turn,
a tower's soft tokens at their placeholders, against numpy, over an encoder
and over a causal model's chunks.
"""

import dataclasses

import numpy as np
import pytest
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

from iron import Scratchpad
from iron.applications.llama.model import Llama
from iron.lm import Multimodal, Tower, widen
from iron.operators.copy import Copy
from iron.tests.common.llama_model import PROFILE, SMALL, checkpoint
from iron.tests.common.llama_reference import _assert_close
from iron.tests.common.encoder import (
    HEAD_DIM,
    HEADS,
    VOCAB,
    Rows,
    SelfAttention,
    attention,
)

pytestmark = pytest.mark.usefixtures("npu2")

PLACEHOLDER = VOCAB - 1
# The tower's layer, then the text's, each rounded once, in another order
# than numpy's: a rounding flip each.
TOLERANCE = Tolerance.bf16_ulps(2)


@pytest.fixture(scope="module")
def table():
    rng = np.random.default_rng(0)
    return (rng.standard_normal((VOCAB, HEADS * HEAD_DIM)) / 4).astype(bfloat16)


def test_its_signature_is_its_text_model_s_and_towers(table):
    model = Multimodal(SelfAttention(table, 1), {PLACEHOLDER: Rows()})
    assert list(model.signature().parameters) == [
        "ids",
        "rows",
        "placed",
        "n",
        "rows_n",
    ]
    assert [sorted(s) for s in model.shapes()] == [["ids"], ["rows"], ["placed"]]
    assert model.longest() == dict(n=128, rows_n=128)
    assert model.at == {PLACEHOLDER: 128}


def test_two_towers_on_one_input_name_are_refused(table):
    with pytest.raises(TypeError, match="repeat a name"):
        Multimodal(SelfAttention(table, 1), {PLACEHOLDER: Rows(), 0: Rows()})


@pytest.mark.parametrize("soft", [1, 5])
def test_a_mixed_call_places_the_soft_tokens_and_attends_over_them(table, soft):
    model = Multimodal(SelfAttention(table, 1), {PLACEHOLDER: Rows()})
    rng = np.random.default_rng(soft)
    rows = (rng.standard_normal((soft, HEADS * HEAD_DIM)) / 4).astype(bfloat16)
    tokens = np.array([3, *[PLACEHOLDER] * soft, 7, 9])
    calls, values = model.calls(tokens, {PLACEHOLDER: (rows,)})
    assert len(calls) == 2 and values == dict(n=tokens.size, rows_n=soft)
    for inputs in calls:
        got = model.reference(*inputs, **values)
    soft_tokens = attention(rows, HEAD_DIM**-0.5).astype(bfloat16)
    x = table[tokens].copy()
    x[1 : 1 + soft] = soft_tokens
    want = attention(x, 1.0)
    verdict = compare(np.asarray(got), want, TOLERANCE)
    assert verdict, verdict


def test_a_text_only_call_runs_the_text_model_s_version(table):
    model = Multimodal(SelfAttention(table, 1), {PLACEHOLDER: Rows()})
    tokens = np.array([3, 7, 9])
    calls, values = model.calls(tokens, {})
    assert len(calls) == 1 and values == dict(n=3, rows_n=0)
    got = model.reference(*calls[0], **values)
    verdict = compare(
        np.asarray(got), attention(table[tokens], 1.0), Tolerance.bf16_ulps(1)
    )
    assert verdict, verdict


def test_placeholders_that_are_not_the_soft_tokens_are_refused(table):
    model = Multimodal(SelfAttention(table, 1), {PLACEHOLDER: Rows()})
    rows = np.zeros((2, HEADS * HEAD_DIM), bfloat16)
    with pytest.raises(ValueError, match="1 placeholders"):
        model.calls([3, PLACEHOLDER, 7], {PLACEHOLDER: (rows,)})


@dataclasses.dataclass(frozen=True)
class Width:
    emb_dim: int
    text_dim: int


class Features(Tower):
    """A tower whose soft tokens are the rows it is given."""

    def __init__(self, width: int, rows: int):
        super().__init__(Width(width, width), [], rows, rows)

    def front(self, features, *, n):
        return Copy.step(features)[:n], None

    def head(self, x):
        return x

    def soft(self, values: dict) -> int:
        return values["n"]

    def inputs(self, features) -> tuple[np.ndarray, dict]:
        buffer = np.zeros((self.max_tokens, self.config.emb_dim), bfloat16)
        buffer[: len(features)] = features
        return buffer, dict(n=len(features))

    def shapes(self) -> list[dict]:
        return [dict(features=((self.max_tokens, self.config.emb_dim), bfloat16))]

    def body(self, features, *, n: Scratchpad[np.int32]):
        x, angles = self.front(features, n=n)
        return self.forward(x, n, angles)


IMAGE = SMALL.vocab_size - 1


@pytest.fixture(scope="module")
def causal():
    """A small Llama over chunks of 256 of 1024 positions, a tower on its
    image placeholder, its oracle, and a prompt whose run of 16 soft tokens
    crosses its first chunk's end.
    """
    config = dataclasses.replace(SMALL, max_seq_len=1024)
    weights = checkpoint(config).tree("random")
    text = Llama(config, weights)
    text.profile = PROFILE
    model = Multimodal(text, {IMAGE: Features(config.emb_dim, 64)})
    model.profile = PROFILE
    rng = np.random.default_rng(8)
    tokens = rng.integers(0, IMAGE, 300)
    tokens[250:266] = IMAGE
    soft = (rng.standard_normal((16, config.emb_dim)) / 8).astype(bfloat16)
    return model, Llama.oracle(config, weights), tokens, soft


def oracle_logits(oracle, tokens, soft) -> np.ndarray:
    """The oracle's logits after ``tokens``, the soft tokens at their placeholders."""
    x = oracle.embedding[tokens].copy()
    x[tokens == IMAGE] = soft.astype(np.float32)
    angles = oracle.angles[: tokens.size]
    for i, w in enumerate(oracle.layers):
        x = oracle.layer(i, angles, widen(w), x)
    return oracle.head(x[-1])


def test_a_causal_model_s_versions_and_signature(causal):
    model, *_ = causal
    assert list(model.signature().parameters) == [
        "ids",
        "features",
        "placed",
        "before",
        "token",
        "position",
        "chunk",
        "rows",
        "features_n",
    ]
    assert [sorted(s) for s in model.shapes()] == [
        [],
        ["ids"],
        ["features"],
        ["before", "placed"],
    ]
    assert model.at == {IMAGE: 256}


def test_a_run_of_soft_tokens_crossing_a_chunk_is_placed_on_both_sides(causal):
    """Each version's reference in turn, its states carried from one to the
    next: the tower, then each chunk, one holding a placeholder through
    ``placed`` with the count before it, then a decode step.
    """
    model, oracle, tokens, soft = causal
    C = model.text.config.prefill_chunk
    calls, towers = model.tower_calls(tokens, {IMAGE: (soft,)})
    zero = dict(token=0, position=0, chunk=0, rows=1)
    for inputs in calls:
        model.reference(*inputs, **zero, **towers)
    placed = []
    for begin in range(0, tokens.size, C):
        chunk = tokens[begin : begin + C]
        ids = model.text.prompt_ids(chunk)
        values = dict(
            token=int(chunk[-1]),
            position=begin + chunk.size - 1,
            chunk=begin // C,
            rows=chunk.size,
            **towers,
        )
        if (chunk == IMAGE).any():
            before = np.array([np.count_nonzero(tokens[:begin] == IMAGE)], np.int32)
            placed.append(int(before[0]))
            logits, carry = model.reference(None, None, ids, before, **values)
        else:
            logits, carry = model.reference(ids, **values)
    assert placed == [0, 6]
    _assert_close(
        [np.asarray(logits).reshape(-1)], [oracle_logits(oracle, tokens, soft)]
    )
    tokens = np.append(tokens, carry["token"])
    logits, _ = model.reference(chunk=0, rows=1, **carry, **towers)
    _assert_close(
        [np.asarray(logits).reshape(-1)], [oracle_logits(oracle, tokens, soft)]
    )
