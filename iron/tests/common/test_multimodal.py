# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.Multimodal``, device-free: its signature from its text model's and towers'.

The versions a mixed call runs, and their references in turn, a tower's
soft tokens at their placeholders, against numpy over an encoder and
against Hugging Face's Llama (``goldens/``) over a causal model's chunks.
"""

import numpy as np
import pytest
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

from iron.lm import Multimodal
from iron.lm.testing import assert_close
from iron.tests.support.encoder import (
    HEAD_DIM,
    HEADS,
    VOCAB,
    Rows,
    SelfAttention,
    attention,
)
from iron.tests.support.llama_reference import prompt
from iron.tests.support.multimodal import IMAGE, small_causal

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
        "x",
        "placed",
        "rows",
        "x_rows",
    ]
    assert [sorted(s) for s in model.shapes()] == [["ids"], ["x"], ["placed"]]
    assert model.longest() == dict(rows=128, x_rows=128)
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
    calls = model.calls(tokens, {PLACEHOLDER: (rows,)})
    assert [values for _, values in calls] == [
        dict(rows=tokens.size, x_rows=soft),
        dict(rows=tokens.size, x_rows=0),
    ]
    for inputs, values in calls:
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
    ((inputs, values),) = model.calls(tokens, {})
    assert values == dict(rows=3, x_rows=0)
    got = model.reference(*inputs, **values)
    verdict = compare(
        np.asarray(got), attention(table[tokens], 1.0), Tolerance.bf16_ulps(1)
    )
    assert verdict, verdict


def test_placeholders_that_are_not_the_soft_tokens_are_refused(table):
    model = Multimodal(SelfAttention(table, 1), {PLACEHOLDER: Rows()})
    rows = np.zeros((2, HEADS * HEAD_DIM), bfloat16)
    with pytest.raises(ValueError, match="1 placeholders"):
        model.calls([3, PLACEHOLDER, 7], {PLACEHOLDER: (rows,)})


def test_a_causal_model_s_versions_and_signature(golden):
    model, *_ = small_causal(golden)
    assert list(model.signature().parameters) == [
        "ids",
        "features",
        "placed",
        "before",
        "token",
        "position",
        "start",
        "rows",
        "rope_start",
        "features_rows",
    ]
    assert [sorted(s) for s in model.shapes()] == [
        [],
        ["ids"],
        ["features"],
        ["before", "placed"],
    ]
    assert model.at == {IMAGE: 256}


def test_a_run_of_soft_tokens_crossing_a_chunk_is_placed_on_both_sides(golden):
    """Each version's reference in turn, its states carried from one to the next.

    The tower, then each chunk, one holding a placeholder through
    ``placed`` with the count before it, then a decode step.
    """
    model, reference, tokens, soft = small_causal(golden)
    C = model.text.config.prefill_chunk
    zero = dict(token=0, position=0, start=0, rows=1, rope_start=0)
    for inputs, values in model.tower_calls(tokens, {IMAGE: (soft,)}):
        model.reference(*inputs, **zero, **values)
    assert (tokens[:C] == IMAGE).any() and (tokens[C:] == IMAGE).any()
    logits, carry = prompt(model, tokens, **model.idle)
    assert_close(np.asarray(logits).reshape(-1), reference(tokens, soft))
    tokens = np.append(tokens, carry["token"])
    logits, _ = model.reference(start=0, rows=1, rope_start=0, **carry, **model.idle)
    assert_close(np.asarray(logits).reshape(-1), reference(tokens, soft))
