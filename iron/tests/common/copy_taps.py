# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The descriptors Copy issues for the copies llama makes, pinned.

Each copy is built, and every shim task of its runtime sequence recorded as
(lane, offset, sizes, strides), exactly: the copies written as views must
issue them.
"""

from typing import Any

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron.operators.copy import Copy
from iron.tests.common.build import generated_sequence

pytestmark = pytest.mark.usefixtures("npu2")

G, D, L, E, N = 8, 64, 128, 2048, 16  # kv groups, head dim, context, embed, rows


def _permuted(n, g, d) -> TensorAccessPattern:
    """An (n, g, d) buffer read as (g, n, d): ``x.transpose(1, 0, 2)``."""
    return TensorAccessPattern((n, g, d), 0, [g, n, d], [d, g * d, 1])


# One token's (G, D) keys into row `pos` of the (G, L, D) cache:
# Copy(k, keys[:, pos]), the row a per-call value.
ROW_INTO_CACHE = dict(
    src=TensorAccessPattern.full((G, D)),
    dst=TensorAccessPattern.full((G, L, D))[:, 0],
    input_buffer_size=G * D,
    output_buffer_size=G * L * D,
)
# N tokens' (N, G, D) keys, heads interleaved per token, into the first N
# rows: Copy(k.reshape(N, G, D).transpose(1, 0, 2), keys[:, :N]).
ROWS_INTO_CACHE = dict(
    src=_permuted(N, G, D),
    dst=TensorAccessPattern.full((G, L, D))[:, 0:N],
    input_buffer_size=N * G * D,
    output_buffer_size=G * L * D,
    tile_size=1024,
)
# The last prompt row of (4, E), selected by the per-call index `last`:
# Copy(x[last]).
LAST_ROW = dict(
    src=TensorAccessPattern.full((4, E))[0],
    input_buffer_size=4 * E,
    output_buffer_size=E,
)
# The same row at slot 5, on one channel and on two.
SLOT5 = dict(ROW_INTO_CACHE, dst=TensorAccessPattern.full((G, L, D))[:, 5])
SLOT5_TWO_CHANNELS = dict(SLOT5, num_channels=2)

PINNED: dict[str, tuple[dict[str, Any], list]] = {
    "row_into_cache": (
        ROW_INTO_CACHE,
        [
            ("fifo_in_0", 0, "1, 1, 8, 64", "0, 0, 64, 1"),
            ("fifo_out_0", 0, "1, 1, 8, 64", "0, 0, 8192, 1"),
        ],
    ),
    "rows_into_cache": (
        ROWS_INTO_CACHE,
        [
            ("fifo_in_0", 0, "1, 8, 16, 64", "0, 64, 512, 1"),
            ("fifo_out_0", 0, "1, 8, 16, 64", "0, 8192, 64, 1"),
        ],
    ),
    "last_row": (
        LAST_ROW,
        [
            ("fifo_in_0", 0, "1, 1, 1, 2048", "0, 0, 0, 1"),
            ("fifo_out_0", 0, "1, 1, 1, 2048", "0, 0, 0, 1"),
        ],
    ),
    "slot5": (
        SLOT5,
        [
            ("fifo_in_0", 0, "1, 1, 8, 64", "0, 0, 64, 1"),
            ("fifo_out_0", 320, "1, 1, 8, 64", "0, 0, 8192, 1"),
        ],
    ),
    "slot5_two_channels": (
        SLOT5_TWO_CHANNELS,
        [
            ("fifo_in_0", 0, "1, 1, 8, 32", "0, 0, 64, 1"),
            ("fifo_out_0", 320, "1, 1, 8, 32", "0, 0, 8192, 1"),
            ("fifo_in_1", 32, "1, 1, 8, 32", "0, 0, 64, 1"),
            ("fifo_out_1", 352, "1, 1, 8, 32", "0, 0, 8192, 1"),
        ],
    ),
}


def _bounded(op: Copy) -> Copy:
    """``op`` as a graph builds it, its per-call sizes bound."""
    op.use_value("src_valid")
    op.use_value("dst_valid")
    return op


@pytest.mark.parametrize("name", sorted(PINNED))
def test_copy_issues_these_descriptors(name):
    kwargs, tasks = PINNED[name]
    _, issued = generated_sequence(Copy(**kwargs))
    assert [(t.lane, t.offset, t.sizes, t.strides) for t in issued] == tasks


def test_a_bounded_axis_lands_on_d2_and_names_it():
    """A cache write of n rows, ``Copy(k.transpose(1, 0, 2), keys[:, :n])``:
    the bounded axis is one exact descriptor dimension per channel, D2 (the
    one a length patch bounds, with no wrap), the group axis iterating
    outside it; and the reference moves the bounded rows alone.
    """
    N, G, D, L = 16, 4, 8, 32
    op = Copy(
        src=_permuted(N, G, D),
        dst=TensorAccessPattern.full((G, L, D))[:, 0:N],
        src_bound=1,
        dst_bound=1,
        input_buffer_size=N * G * D,
        output_buffer_size=G * L * D,
    )
    _, (fill, drain) = generated_sequence(_bounded(op))
    assert (fill.sizes, fill.strides) == (f"{G}, {N}, 1, {D}", f"{D}, {G * D}, 0, 1")
    assert (drain.sizes, drain.strides) == (f"{G}, {N}, 1, {D}", f"{L * D}, {D}, 0, 1")
    assert fill.length_parameter.endswith("src_valid")
    assert drain.length_parameter.endswith("dst_valid")
    x = np.arange(N * G * D, dtype=np.float32).reshape(N, G, D)
    y = np.zeros((G, L, D), dtype=np.float32)
    op.reference(x, y, src_valid=5, dst_valid=5)
    assert (y[:, :5] == x[:5].transpose(1, 0, 2)).all() and not y[:, 5:].any()
    flat = Copy(
        src=TensorAccessPattern.full((N,)),
        src_bound=0,
        input_buffer_size=N,
        num_channels=2,
    )
    with pytest.raises(ValueError, match="channels split"):
        generated_sequence(_bounded(flat))


def test_a_bounded_axis_past_the_d1_wrap_still_packs():
    """Llama's prompt cache write, 2048 rows into a 2048-row cache: past
    D1's 1023 wrap, so the bounded axis packs only on D2.
    """
    N, G, D = 2048, 8, 64
    op = Copy(
        src=_permuted(N, G, D),
        dst=TensorAccessPattern.full((G, N, D))[:, 0:N],
        src_bound=1,
        dst_bound=1,
        input_buffer_size=N * G * D,
        output_buffer_size=G * N * D,
    )
    _, tasks = generated_sequence(_bounded(op))
    assert [t.sizes for t in tasks] == [f"{G}, {N}, 1, {D}"] * 2


# A gather of rows of a (V, W) table, ids known at trace time: Copy(table[ids]).
V, W = 64, 32


def _gather(ids, **kwargs) -> Copy:
    whole = TensorAccessPattern.full((V, W))
    return Copy(
        src=tuple(whole[int(i)] for i in ids), input_buffer_size=V * W, **kwargs
    )


GATHERS = {
    # Two runs of consecutive ids, of equal length: one pattern.
    "runs": (
        np.r_[5:9, 40:44],
        [
            ("fifo_out_0", 0, "1, 1, 8, 32", "0, 0, 32, 1"),
            ("fifo_in_0", 160, "1, 2, 4, 32", "0, 1120, 32, 1"),
        ],
    ),
    # A row repeated: a stride-0 iteration.
    "repeat": (
        np.full(6, 7),
        [
            ("fifo_out_0", 0, "1, 1, 6, 32", "0, 0, 32, 1"),
            ("fifo_in_0", 224, "6, 1, 1, 32", "0, 0, 0, 1"),
        ],
    ),
    # Out of order: a run down cannot merge, so every row is its own fill.
    "descending": (
        np.array([9, 8, 2]),
        [
            ("fifo_out_0", 0, "1, 1, 3, 32", "0, 0, 32, 1"),
            ("fifo_in_0", 288, "1, 1, 1, 32", "0, 0, 0, 1"),
            ("fifo_in_0", 256, "1, 1, 1, 32", "0, 0, 0, 1"),
            ("fifo_in_0", 64, "1, 1, 1, 32", "0, 0, 0, 1"),
        ],
    ),
}


@pytest.mark.parametrize("name", sorted(GATHERS))
def test_a_gather_merges_the_rows_it_can(name):
    ids, tasks = GATHERS[name]
    op = _gather(ids)
    text, issued = generated_sequence(op)
    assert [(t.lane, t.offset, t.sizes, t.strides) for t in issued] == tasks
    assert text.count("dma_await_task") == 1
    assert op.aiecc_flags == ("--reclaim-runtime-bds",)
    x = np.arange(V * W, dtype=np.float32).reshape(V, W)
    assert (op.reference(x).reshape(len(ids), W) == x[ids]).all()


def test_a_gathers_channels_split_each_row():
    ids = np.array([3, 3, 60, 1])
    op = _gather(ids, num_channels=2)
    text, issued = generated_sequence(op)
    assert {t.lane for t in issued} == {
        "fifo_in_0",
        "fifo_in_1",
        "fifo_out_0",
        "fifo_out_1",
    }
    assert text.count("dma_await_task") == 2
    x = np.arange(V * W, dtype=np.float32).reshape(V, W)
    assert (op.reference(x).reshape(len(ids), W) == x[ids]).all()


class _Gathers(iron.Graph):
    def __init__(self, ids):
        self.table = iron.weight(np.zeros((V, W), dtype=bfloat16))
        self.ids = ids

    def body(self, x):
        rows = Copy(self.table[self.ids])
        return Copy(Copy(x)[self.ids]), rows


def test_a_graph_gathers_from_a_weight_and_an_intermediate():
    ids = np.array([4, 0, 4, 63, -1])
    graph = _Gathers(ids)
    t = graph.trace(x=(V, W))
    gathers = [op for op, *_ in t.runlist if isinstance(op.src, tuple)]
    assert len(gathers) == 2
    whole = TensorAccessPattern.full((V, W))
    assert all(op.src == tuple(whole[i % V] for i in ids) for op in gathers)
    x = np.arange(V * W, dtype=np.float32).reshape(V, W).astype(bfloat16)
    from_x, from_table = graph.reference(x)
    assert (np.asarray(from_x).reshape(len(ids), W) == x[ids]).all()
    assert not np.asarray(from_table).any()


@pytest.mark.parametrize(
    "index, match",
    [
        (np.array([[0, 1]]), "1-D integer array"),
        (np.array([0.0, 1.0]), "1-D integer array"),
        (np.array([], dtype=np.int64), "gathering"),
        (np.array([0, V]), "gathering"),
        (np.array([-V - 1]), "gathering"),
        ((np.array([0, 1]), slice(0, 4)), "whole of every axis"),
    ],
)
def test_a_gather_refuses_what_it_cannot_lower(index, match):
    class Bad(iron.Graph):
        def body(self, x):
            return Copy(Copy(x)[index])

    with pytest.raises(IndexError, match=match):
        Bad().trace(x=(V, W))


@pytest.mark.parametrize("channels", [1, 2, 4])
def test_a_permuting_copy_keeps_its_order_on_every_channel_count(channels):
    """The channels split the innermost axis of both sides, so the default
    output is rows as wide as the source's: each channel's share of a source
    row lands in the same share of the output row.
    """
    op = Copy(
        src=_permuted(N, G, D), input_buffer_size=N * G * D, num_channels=channels
    )
    x = np.arange(N * G * D, dtype=np.float32).reshape(N, G, D)
    assert (op.reference(x).reshape(G, N, D) == x.transpose(1, 0, 2)).all()
