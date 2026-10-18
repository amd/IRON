# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.Multimodal``, device-free: its signature from its text model's
and towers', the versions a mixed call runs, and their references in turn,
a tower's soft tokens at their placeholders, against numpy over an encoder
and against Hugging Face's Llama (``goldens/``) over a causal model's chunks.
"""

import dataclasses

import numpy as np
import pytest
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

from iron import Scratchpad
from iron.applications.llama.model import Llama
from iron.lm import Multimodal, Tower
from iron.lm.golden import HuggingFace
from iron.operators.copy import Copy
from iron.tests.common.llama_model import PROFILE, SMALL, checkpoint
from iron.lm.testing import assert_close
from iron.tests.common.llama_reference import prompt
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
    calls, values = model.calls(tokens, {PLACEHOLDER: (rows,)})
    assert len(calls) == 2 and values == dict(rows=tokens.size, x_rows=soft)
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
    assert len(calls) == 1 and values == dict(rows=3, x_rows=0)
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
    hidden_size: int
    text_dim: int


class Features(Tower):
    """A tower whose soft tokens are the rows it is given."""

    def __init__(self, width: int, rows: int):
        super().__init__(Width(width, width), [], rows, rows)

    def front(self, features, *, rows):
        return Copy.step(features)[:rows], None

    def head(self, x):
        return x

    def inputs(self, features) -> tuple[np.ndarray, dict]:
        buffer = np.zeros((self.max_tokens, self.config.hidden_size), bfloat16)
        buffer[: len(features)] = features
        return buffer, dict(rows=len(features))

    def shapes(self) -> list[dict]:
        return [dict(features=((self.max_tokens, self.config.hidden_size), bfloat16))]

    def body(self, features, *, rows: Scratchpad[np.int32]):
        x, angles = self.front(features, rows=rows)
        return self.forward(x, rows, angles)


IMAGE = SMALL.vocab_size - 1


class Placed(HuggingFace):
    """Hugging Face's Llama with ``soft`` at its image placeholders: the
    logits after a sequence's tokens.
    """

    def logits(self, tokens, soft) -> np.ndarray:
        import torch

        tokens = torch.from_numpy(np.asarray(tokens))
        with torch.no_grad():
            x = self.model.model.embed_tokens(tokens)
            x[tokens == IMAGE] = torch.from_numpy(soft.astype(np.float32))
            out = self.model(inputs_embeds=x[None], use_cache=False)
        return out.logits[0, -1].numpy()


@pytest.fixture(scope="module")
def causal(golden):
    """A small Llama over chunks of 256 of 1024 positions, a tower on its
    image placeholder, Hugging Face's logits for it (``reference(tokens,
    soft)``, from ``goldens/multimodal.npz``), and a prompt whose run of 16
    soft tokens crosses its first chunk's end.
    """
    config = dataclasses.replace(SMALL, max_seq_len=1024)
    weights = checkpoint(config).tree("random")
    text = Llama(config, weights)
    text.profile = PROFILE
    model = Multimodal(text, {IMAGE: Features(config.hidden_size, 64)})
    model.profile = PROFILE
    rng = np.random.default_rng(8)
    tokens = rng.integers(0, IMAGE, 300)
    tokens[250:266] = IMAGE
    soft = (rng.standard_normal((16, config.hidden_size)) / 8).astype(bfloat16)

    hf = golden(
        "multimodal", lambda: Placed.build("llama", config, weights), config, weights
    )
    return model, hf.logits, tokens, soft


def test_a_causal_model_s_versions_and_signature(causal):
    model, *_ = causal
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


def test_a_run_of_soft_tokens_crossing_a_chunk_is_placed_on_both_sides(causal):
    """Each version's reference in turn, its states carried from one to the
    next: the tower, then each chunk, one holding a placeholder through
    ``placed`` with the count before it, then a decode step.
    """
    model, reference, tokens, soft = causal
    C = model.text.config.prefill_chunk
    calls, towers = model.tower_calls(tokens, {IMAGE: (soft,)})
    zero = dict(token=0, position=0, start=0, rows=1, rope_start=0)
    for inputs in calls:
        model.reference(*inputs, **zero, **towers)
    assert (tokens[:C] == IMAGE).any() and (tokens[C:] == IMAGE).any()
    logits, carry = prompt(model, tokens, **towers)
    assert_close(np.asarray(logits).reshape(-1), reference(tokens, soft))
    tokens = np.append(tokens, carry["token"])
    logits, _ = model.reference(start=0, rows=1, rope_start=0, **carry, **towers)
    assert_close(np.asarray(logits).reshape(-1), reference(tokens, soft))
