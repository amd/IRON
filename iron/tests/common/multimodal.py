# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.Multimodal``, device-free: its signature from its text model's
and towers', the versions a mixed call runs, and their references in turn,
a tower's soft tokens at their placeholders, against numpy.
"""

import numpy as np
import pytest
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

from iron.lm import Multimodal
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
