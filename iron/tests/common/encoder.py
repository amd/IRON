# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm``'s ``Encoder`` and ``Tower``, device-free: a call's inputs, the
bounded gather a body traces, each kind's reference, the operators' own,
against numpy attention over the valid rows, and the default layer, its
config's ``DecoderLayer`` attending both ways.
"""

import dataclasses

import numpy as np
import pytest
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

import iron
from iron import Precision, Scratchpad
from iron.lm import MLP, Attention, DecoderLayer, Encoder, Norm, Tower, rope_angles
from iron.operators.copy import Copy, Gather
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.mha import MHA
from iron.tests.common.layer import LLAMA, module, shapes

pytestmark = pytest.mark.usefixtures("npu2")

ROWS, VOCAB, HEADS, HEAD_DIM = 128, 32, 2, 64
# The references compute in float32 and round each layer's rows once, as the
# numpy below does in another order: a rounding flip a layer.
LAYERS = 2
TOLERANCE = Tolerance.bf16_ulps(LAYERS)


@dataclasses.dataclass(frozen=True)
class Shape:
    vocab_size: int = VOCAB
    hidden_size: int = HEADS * HEAD_DIM
    text_dim: int = HEADS * HEAD_DIM


@dataclasses.dataclass(frozen=True)
class Windowed(Shape):
    """A Llama-shaped layer each, at HIGHEST precision, the first unscaled within 64
    positions."""

    def layer(self, i: int) -> DecoderLayer:
        first = i == 0
        attention = Attention(
            HEADS,
            1,
            HEAD_DIM,
            scale=1.0 if first else None,
            window=64 if first else None,
            precision=Precision.HIGHEST,
        )
        return DecoderLayer(attention, MLP(precision=Precision.HIGHEST), Norm(1e-6))


class Layers(Encoder):
    """The default layer over Llama-shaped modules, rotated from the first
    position."""

    def __init__(self, table, layers: list):
        self.table = table
        self.modules = layers
        angles = rope_angles(HEAD_DIM, ROWS, 10000.0).astype(bfloat16)
        self.rope = iron.weight(angles)
        super().__init__(Windowed(), layers, ROWS)

    def lookup(self, ids):
        return Copy.step(iron.weight(self.table)[ids])

    def angles(self, n):
        return self.rope[:n]

    def head(self, x):
        return x


class SelfAttention(Encoder):
    """Each layer the rows attending to themselves, unscaled, within
    ``window`` positions."""

    def __init__(self, table, layers: int, window: int | None = None):
        self.table = table
        self.window = window
        super().__init__(Shape(), [None] * layers, ROWS)

    def lookup(self, ids):
        return Copy.step(iron.weight(self.table)[ids])

    def layer(self, step, i, weights, x):
        q = x.reshape(x.shape[0], HEADS, HEAD_DIM)
        return self.attend(step, i, q, q, q, scale=1.0, window=self.window)

    def head(self, x):
        return x


class Rows(Tower):
    """A tower whose front end is the rows it is given, one soft token each."""

    def __init__(self):
        super().__init__(Shape(), [None], ROWS, ROWS)

    def front(self, x, *, rows):
        return Copy.step(x)[:rows], None

    def layer(self, step, i, weights, x):
        q = x.reshape(x.shape[0], HEADS, HEAD_DIM)
        return self.attend(step, i, q, q, q)

    def head(self, x):
        return x

    def inputs(self, rows) -> tuple[np.ndarray, dict]:
        buffer = np.zeros((ROWS, HEADS * HEAD_DIM), bfloat16)
        buffer[: len(rows)] = rows
        return buffer, dict(rows=len(rows))

    def shapes(self) -> list[dict]:
        return [dict(x=((ROWS, HEADS * HEAD_DIM), bfloat16))]

    def body(self, x, *, rows: Scratchpad[np.int32]):
        x, angles = self.front(x, rows=rows)
        return self.forward(x, rows, angles)


def attention(x, scale: float, window: int | None = None) -> np.ndarray:
    """Every row of ``x`` over the rows within ``window`` of it, per head."""
    n = x.shape[0]
    h = x.astype(np.float32).reshape(n, HEADS, HEAD_DIM).transpose(1, 0, 2)
    logits = h @ h.transpose(0, 2, 1) * np.float32(scale)
    if window is not None:
        at = np.arange(n)
        logits[:, np.abs(at[:, None] - at[None, :]) > window] = -np.inf
    p = np.exp(logits - logits.max(axis=-1, keepdims=True))
    p /= p.sum(axis=-1, keepdims=True)
    return (p @ h).transpose(1, 0, 2).reshape(n, HEADS * HEAD_DIM)


@pytest.fixture(scope="module")
def table():
    rng = np.random.default_rng(0)
    return (rng.standard_normal((VOCAB, HEADS * HEAD_DIM)) / 4).astype(bfloat16)


def test_inputs_pad_with_zero_and_give_rows(table):
    ids, values = SelfAttention(table, 1).inputs([5, VOCAB - 1, 7])
    assert values == dict(rows=3)
    assert ids.dtype == np.int32 and ids.shape == (ROWS,)
    np.testing.assert_array_equal(ids[:3], [5, VOCAB - 1, 7])
    assert not ids[3:].any()


@pytest.mark.parametrize(
    "tokens, error",
    [
        ([], ValueError),
        ([1] * (ROWS + 1), ValueError),
        ([VOCAB], IndexError),
        ([-1], IndexError),
    ],
)
def test_inputs_refuse_what_no_call_takes(table, tokens, error):
    with pytest.raises(error):
        SelfAttention(table, 1).inputs(tokens)


def test_the_gather_reads_only_the_rows_a_call_bounds(table):
    graph = SelfAttention(table, 1)
    traced = graph.trace(**graph.shapes()[0])
    assert [type(s.op).__name__ for s in traced.steps] == ["Gather", "MHA"]
    (gather,) = [s.op for s in traced.steps if isinstance(s.op, Gather)]
    assert "valid_rows" in gather.bound_extents
    assert gather.table_rows == VOCAB


@pytest.mark.parametrize("window", [None, 64])
@pytest.mark.parametrize("n", [1, ROWS])
def test_an_encoder_attends_its_valid_rows_both_ways(table, window, n):
    graph = SelfAttention(table, LAYERS, window)
    tokens = np.random.default_rng(n).integers(0, VOCAB, n)
    ids, values = graph.inputs(tokens)
    got = graph.reference(ids, **values)
    x = table[tokens].astype(np.float32)
    for _ in graph.layers:
        x = attention(x, 1.0, window).astype(bfloat16).astype(np.float32)
    assert np.shape(got) == (n, HEADS * HEAD_DIM)
    verdict = compare(np.asarray(got), x, TOLERANCE)
    assert verdict, verdict


def test_a_tower_runs_its_front_end_s_rows():
    tower = Rows()
    rows = (np.random.default_rng(1).standard_normal((9, 128)) / 4).astype(bfloat16)
    buffer, values = tower.inputs(rows)
    assert tower.soft(values) == 9
    got = tower.reference(buffer, **values)
    want = attention(rows, HEAD_DIM**-0.5)
    verdict = compare(np.asarray(got), want, Tolerance.bf16_ulps(1))
    assert verdict, verdict


def test_a_tower_takes_no_ids():
    with pytest.raises(NotImplementedError, match="Rows defines no lookup"):
        Rows().lookup(None)


def test_the_default_layer_is_the_config_s_attending_both_ways(table):
    rng = np.random.default_rng(2)
    shape = shapes(HEADS * HEAD_DIM, HEADS, 1, HEAD_DIM, 256)
    graph = Layers(table, [module(rng, shape, LLAMA, bfloat16) for _ in range(2)])
    traced = graph.trace(**graph.shapes()[0])
    attention = [s.op for s in traced.steps if isinstance(s.op, MHA)]
    assert [(op.causal, op.window, op.scale) for op in attention] == [
        (False, 64, 1.0),
        (False, None, HEAD_DIM**-0.5),
    ]
    ids, values = graph.inputs(np.arange(9))
    assert np.shape(graph.reference(ids, **values)) == (9, HEADS * HEAD_DIM)


class Positioned(SelfAttention):
    """One layer of ``SelfAttention`` over rows placed by a held table of
    absolute positions."""

    def __init__(self, table, positions):
        super().__init__(table, 1)
        self.position_table = iron.weight(positions)

    def positions(self, x, step):
        return ElementwiseAdd.step(x, Copy.step(self.position_table[: step.rows]))


@pytest.mark.parametrize("n", [9, ROWS])
def test_an_encoder_places_its_positions_through_the_hook(table, n):
    rng = np.random.default_rng(n)
    positions = (rng.standard_normal((ROWS, HEADS * HEAD_DIM)) / 4).astype(bfloat16)
    graph = Positioned(table, positions)
    tokens = rng.integers(0, VOCAB, n)
    ids, values = graph.inputs(tokens)
    got = graph.reference(ids, **values)
    x = (table[tokens].astype(np.float32) + positions[:n]).astype(bfloat16)
    verdict = compare(np.asarray(got), attention(x, 1.0), TOLERANCE)
    assert verdict, verdict
    unplaced = attention(table[tokens], 1.0)
    assert not compare(np.asarray(got), unplaced, TOLERANCE)
