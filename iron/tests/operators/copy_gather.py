#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A gather of a table's rows, ``Copy(table[ids])``, on a device.

With ``ids`` an array, the ids are known when the graph is traced; each
row, or each run of rows whose ids step evenly, is one transfer of the
step's sequence. The table is a weight at EmbeddingGemma 2's size, or an
intermediate a step before produced. With ``ids`` an input of the graph,
each call names its rows, and the host encodes them as the addresses a
``Gather`` writes into the shim's descriptors; with ids a state or a step's
output, a core writes those addresses in a step before the gather.
"""

import numpy as np
import pytest
from aie.iron.device import from_name
from ml_dtypes import bfloat16

import iron
from iron.common import Profile
from iron.operators import ElementwiseAdd
from iron.operators.copy import Copy, Gather

# EmbeddingGemma 2's per-layer embedding table.
VOCAB, WIDTH = 262144, 512

pytestmark = pytest.mark.usefixtures("npu2")


def gathered_ids(n_rows: int, n_ids: int) -> np.ndarray:
    """Random ids, out of order, with repeats, a run and a reversed run."""
    rng = np.random.default_rng(n_ids)
    ids = rng.integers(0, n_rows, n_ids)
    ids[::9] = ids[4]
    ids[10:42] = np.arange(1000, 1032)
    ids[50:66] = np.arange(80, 64, -1)
    ids[70:78] = n_rows - 1
    return ids


class FromWeight(iron.Graph):
    def __init__(self, table, ids):
        self.table = iron.weight(table)
        self.ids = ids

    def body(self, x):
        rows = Copy(self.table[self.ids]).reshape(len(self.ids), WIDTH)
        return rows, ElementwiseAdd(rows, x)


class FromIntermediate(iron.Graph):
    def __init__(self, ids):
        self.ids = ids

    def body(self, table):
        table = Copy(table).reshape(table.shape)
        return Copy(table[self.ids]).reshape(len(self.ids), WIDTH)


class PerCall(iron.Graph):
    def __init__(self, table, feeds: int | None = None):
        self.table = iron.weight(table)
        self.profile = Profile()
        if feeds is not None:
            self.profile.add(Gather, feeds=feeds)

    def body(self, ids):
        return Copy(self.table[ids])


class FromDeviceIds(iron.Graph):
    """Two tables gathered by ids a step made, so no host encodes them."""

    def __init__(self, table, other, feeds: int | None = None):
        self.table = iron.weight(table)
        self.other = iron.weight(other)
        self.profile = Profile()
        if feeds is not None:
            self.profile.add(Gather, feeds=feeds)

    def body(self, ids):
        ids = Copy(ids, dtype=np.int32)
        return Copy(self.table[ids]), Copy(self.other[ids])


class FromState(iron.Graph):
    def __init__(self, table, rows: int):
        self.table = iron.weight(table)
        self.ids = iron.state((rows,), np.int32)

    def body(self):
        return Copy(self.table[self.ids])


class Merged(iron.Graph):
    def __init__(self, table, rows: int, soft: int):
        self.table = iron.weight(table)
        self.at = rows
        self.merged = iron.state((rows + soft, WIDTH))

    def body(self, ids, soft, merge):
        x = Copy(self.table[ids])
        Copy(x, self.merged[: x.shape[0]])
        Copy(soft, self.merged[self.at : self.at + soft.shape[0]])
        return Copy(self.merged[merge])


def assert_equal(got, expected, what):
    got = np.asarray(got, dtype=np.float32).reshape(expected.shape)
    wrong = np.argwhere(got != expected.astype(np.float32))
    assert not len(wrong), f"{what}: {len(wrong)} elements differ, first {wrong[:4]}"


@pytest.fixture(scope="module")
def table():
    rng = np.random.default_rng(0)
    return rng.standard_normal((VOCAB, WIDTH), dtype=np.float32).astype(bfloat16)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("n_ids", [256, 512])
def test_rows_of_a_weight_are_gathered(npu_runtime, table, n_ids):
    ids = gathered_ids(VOCAB, n_ids)
    graph = FromWeight(table, ids)
    net = graph.compile(x=(n_ids, WIDTH))
    assert net.plan.image == "elf"
    x = np.random.default_rng(1).standard_normal((n_ids, WIDTH)).astype(bfloat16)
    rows, total = graph(x)
    assert_equal(rows, table[ids], "gathered")
    expected_rows, expected_total = graph.reference(x)
    assert_equal(expected_rows, table[ids], "reference")
    assert_equal(total, np.asarray(expected_total), "the step after")


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("n_ids", [256, 512])
def test_rows_of_an_intermediate_are_gathered(npu_runtime, n_ids):
    n_rows = 4096
    ids = gathered_ids(n_rows, n_ids)
    table = np.random.default_rng(2).standard_normal((n_rows, WIDTH)).astype(bfloat16)
    graph = FromIntermediate(ids)
    assert_equal(graph(table), table[ids], "gathered")
    assert_equal(graph.reference(table), table[ids], "reference")


# A feed count left out resolves, to one feed for 15 rows and four past 48.
FEEDS = [(None, 15), (None, 256), (1, 71), (4, 71), (1, 512), (4, 512)]


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("feeds,n_ids", FEEDS)
def test_rows_each_call_names_are_gathered(npu_runtime, table, feeds, n_ids):
    graph = PerCall(table, feeds)
    net = graph.compile(ids=((n_ids,), np.int32))
    assert net.plan.image == "elf"
    (gather,) = [s.op for s in net.traced.steps if isinstance(s.op, Gather)]
    assert gather.resolved().feeds == (feeds or (1 if n_ids <= 16 else 4))
    rng = np.random.default_rng(n_ids)
    for call in range(3):
        ids = rng.integers(-VOCAB, VOCAB, n_ids).astype(np.int32)
        ids[:2] = (-VOCAB, VOCAB - 1)
        expected = np.take(table, ids, axis=0)
        assert_equal(graph(ids), expected, f"call {call}")
        assert_equal(graph.reference(ids), expected, f"reference {call}")


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("feeds,n_ids", [(None, 1), *FEEDS])
def test_rows_ids_the_device_made_name_are_gathered(npu_runtime, table, feeds, n_ids):
    other = np.random.default_rng(4).standard_normal((3000, 256)).astype(bfloat16)
    graph = FromDeviceIds(table, other, feeds)
    net = graph.compile(ids=((n_ids,), np.int32))
    assert net.plan.image == "elf"
    assert not net.traced.encoders
    resolved = {
        s.op.resolved().feeds for s in net.traced.steps if isinstance(s.op, Gather)
    }
    assert resolved == {feeds or (1 if n_ids <= 16 else 4)}
    rng = np.random.default_rng(n_ids)
    for call in range(3):
        ids = rng.integers(-VOCAB, VOCAB, n_ids).astype(np.int32)
        ids[1::2] = rng.integers(-len(other), len(other), n_ids // 2)
        ids[:2] = (-VOCAB, VOCAB - 1)[:n_ids]
        rows, others = graph(ids)
        assert_equal(rows, np.take(table, ids, axis=0), f"call {call}")
        # Past the table an id is clipped to its first or last row.
        clipped = np.clip(ids, -len(other), len(other) - 1)
        assert_equal(others, other[clipped], f"call {call}")


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("n_ids", [1, 256])
def test_rows_a_state_names_are_gathered(npu_runtime, table, n_ids):
    graph = FromState(table, n_ids)
    net = graph.compile()
    rng = np.random.default_rng(n_ids)
    for call in range(3):
        ids = rng.integers(0, VOCAB, n_ids).astype(np.int32)
        net.write(graph.ids, ids)
        assert_equal(graph(), table[ids], f"call {call}")


@pytest.mark.supported_devices("npu2")
def test_a_graph_gathers_twice_from_a_weight_and_a_state(npu_runtime):
    n_rows, rows, soft = 4096, 64, 64
    rng = np.random.default_rng(3)
    table = rng.standard_normal((n_rows, WIDTH)).astype(bfloat16)
    graph = Merged(table, rows, soft)
    net = graph.compile(
        ids=((rows,), np.int32),
        soft=((soft, WIDTH), bfloat16),
        merge=((rows,), np.int32),
    )
    assert net.plan.image == "elf"
    for call in range(3):
        ids = rng.integers(0, n_rows, rows).astype(np.int32)
        x = rng.standard_normal((soft, WIDTH)).astype(bfloat16)
        k = int(rng.integers(1, rows))
        start = int(rng.integers(0, rows - k + 1))
        merge = np.arange(rows, dtype=np.int32)
        merge[start : start + k] = rows + np.arange(k)
        expected = np.take(table, ids, axis=0)
        expected[start : start + k] = x[:k]
        assert_equal(graph(ids, x, merge), expected, f"call {call}")


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("outside", [VOCAB, -VOCAB - 1])
def test_ids_past_the_table_are_refused(npu_runtime, table, outside):
    graph = PerCall(table)
    ids = np.arange(15, dtype=np.int32)
    ids[7] = outside
    with pytest.raises(IndexError):
        graph(ids)
    with pytest.raises(IndexError):
        graph.reference(ids)


def test_a_per_call_gather_needs_a_full_elf(table):
    graph = PerCall(table)
    with pytest.raises(ValueError, match="full ELF"):
        graph.compile(ids=((15,), np.int32), boundaries=iron.each_step)


def test_the_control_words_are_counted():
    for rows in (1, 7, 8, 15, 256, 512):
        gather = Gather(rows=rows, table_rows=VOCAB, row=WIDTH)
        ids = np.arange(rows, dtype=np.int32)
        assert gather.control_words(ids, 0).size == gather.words


def test_a_core_writes_the_words_the_host_would():
    for rows in (1, 7, 8, 15, 256, 512):
        gather = Gather(rows=rows, table_rows=VOCAB, row=WIDTH)
        _, slots = gather.template
        written = np.concatenate(
            [tap.gather(np.arange(gather.words)) for tap in gather.word_source().taps()]
        )
        np.testing.assert_array_equal(written, np.stack([slots, slots + 1], -1).ravel())


def test_a_gather_feeds_from_as_many_shim_pairs_as_the_device_has():
    for name, cols, rows, feeds in (
        ("npu1", 4, 512, 2),
        ("npu2", 8, 512, 4),
        ("npu2", 8, 33, 3),
        ("npu2", 8, 16, 1),
        ("npu2", 8, 1, 1),
    ):
        gather = Gather(rows=rows, table_rows=VOCAB, row=WIDTH)
        assert gather.resolved(from_name(name, n_cols=cols)).feeds == feeds


def test_the_feeds_stream_runs_of_whole_pairs_that_cover_the_batches_once():
    for rows in (17, 33, 71, 512, 5120):
        for feeds in range(1, min(4, -(-rows // 16)) + 1):
            gather = Gather(rows=rows, table_rows=VOCAB, row=WIDTH, feeds=feeds)
            runs = gather.runs
            assert [j for run in runs for j in run] == list(range(len(gather.batches)))
            assert all(len(run) and run.start % 2 == 0 for run in runs)


def test_the_control_words_are_one_layout_for_every_feed_count():
    ids = gathered_ids(VOCAB, 512)
    words = {
        feeds: Gather(rows=512, table_rows=VOCAB, row=WIDTH, feeds=feeds).control_words(
            ids, 0x40000
        )
        for feeds in (1, 2, 3, 4)
    }
    for feeds in (2, 3, 4):
        np.testing.assert_array_equal(words[feeds], words[1])


def test_ids_the_device_made_take_a_word_step(table):
    other = np.zeros((3000, 256), dtype=bfloat16)
    traced = FromDeviceIds(table, other).trace(ids=((15,), np.int32))
    steps = [type(s.op).__name__ for s in traced.steps]
    assert steps == ["Copy", "GatherWords", "Gather", "GatherWords", "Gather"]
    assert not traced.encoders
    assert sorted((buffer, word) for buffer, _, word in traced.addresses.values()) == [
        ("other", "base_hi"),
        ("other", "base_lo"),
        ("table", "base_hi"),
        ("table", "base_lo"),
    ]
