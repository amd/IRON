# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A gather of a table's rows, ``Copy(table[ids])``, on a device.

With ``ids`` an array, the ids are known when the graph is recorded; each
row, or each run of rows whose ids step evenly, is one transfer of the
step's sequence. The table is a weight at EmbeddingGemma 2's size, or an
intermediate a step before produced. With ``ids`` an input of the graph,
each call names its rows, and the host encodes them as the addresses a
``Gather`` writes into the shim's descriptors; with ids a state or a step's
output, a core writes those addresses in a step before the gather. Either
runs in a full ELF or in an xclbin.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile, Scratchpad
from iron.operators import ElementwiseAdd
from iron.operators.copy import Copy, Gather

# EmbeddingGemma 2's per-layer embedding table.
VOCAB, WIDTH = 262144, 512


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
        self.ids = iron.param(ids)

    def body(self, x):
        rows = Copy.step(self.table[self.ids]).reshape(len(self.ids), WIDTH)
        return rows, ElementwiseAdd.step(rows, x)


class FromIntermediate(iron.Graph):
    def __init__(self, ids):
        self.ids = iron.param(ids)

    def body(self, table):
        table = Copy.step(table).reshape(table.shape)
        return Copy.step(table[self.ids]).reshape(len(self.ids), WIDTH)


class PerCall(iron.Graph):
    def __init__(self, table, feeds: int | None = None):
        self.table = iron.weight(table)
        self.profile = Profile()
        if feeds is not None:
            self.profile.add(Gather, feeds=feeds)

    def body(self, ids):
        return Copy.step(self.table[ids])


class Embedded(iron.Graph):
    """The rows an input names, and a step reading them."""

    def __init__(self, table):
        self.table = iron.weight(table)

    def body(self, ids, x):
        return ElementwiseAdd.step(Copy.step(self.table[ids]), x)


class Bounded(iron.Graph):
    """The first ``n`` rows a call's ids name, ``n`` per call."""

    def __init__(self, table, feeds: int | None = None):
        self.table = iron.weight(table)
        self.profile = Profile()
        if feeds is not None:
            self.profile.add(Gather, feeds=feeds)

    def body(self, ids, *, n: Scratchpad[np.int32]):
        return Copy.step(self.table[ids[:n]])


class FromDeviceIds(iron.Graph):
    """Two tables gathered by ids a step made, so no host encodes them."""

    def __init__(self, table, other, feeds: int | None = None):
        self.table = iron.weight(table)
        self.other = iron.weight(other)
        self.profile = Profile()
        if feeds is not None:
            self.profile.add(Gather, feeds=feeds)

    def body(self, ids):
        ids = Copy.step(ids, dtype=np.int32)
        return (
            Copy.step(self.table[ids]),
            Copy.step(self.other[ids]),
        )


class BoundedDeviceIds(iron.Graph):
    """The first ``n`` rows ids a step made name, ``n`` per call."""

    def __init__(self, table, feeds: int | None = None):
        self.table = iron.weight(table)
        self.profile = Profile()
        if feeds is not None:
            self.profile.add(Gather, feeds=feeds)

    def body(self, ids, *, n: Scratchpad[np.int32]):
        return Copy.step(self.table[Copy.step(ids, dtype=np.int32)[:n]])


class FromState(iron.Graph):
    def __init__(self, table, rows: int):
        self.table = iron.weight(table)
        self.ids = iron.state((rows,), np.int32)

    def body(self):
        return Copy.step(self.table[self.ids])


class ManyTables(iron.Graph):
    """Gather the first ``n`` rows a call's ids name, of each of three tables of their own widths.

    As Gemma 4's prompt chunk gathers its embedding and every layer's own
    table.
    """

    def __init__(self, *tables):
        self.tables = [iron.weight(t) for t in tables]

    def body(self, ids, *, n: Scratchpad[np.int32]):
        return tuple(Copy.step(t[ids[:n]]) for t in self.tables)


def many_tables(table) -> list[np.ndarray]:
    """``table`` and two narrower ones, of other heights."""
    rng = np.random.default_rng(3)
    return [
        table,
        rng.standard_normal((4096, 256)).astype(bfloat16),
        rng.standard_normal((1000, 128)).astype(bfloat16),
    ]


class Merged(iron.Graph):
    def __init__(self, table, rows: int, soft: int):
        self.table = iron.weight(table)
        self.at = rows
        self.merged = iron.state((rows + soft, WIDTH))

    def body(self, ids, soft, merge):
        x = Copy.step(self.table[ids])
        Copy.step(x, self.merged[: x.shape[0]])
        Copy.step(soft, self.merged[self.at : self.at + soft.shape[0]])
        return Copy.step(self.merged[merge])


def assert_equal(got, expected, what):
    got = np.asarray(got, dtype=np.float32).reshape(expected.shape)
    wrong = np.argwhere(got != expected.astype(np.float32))
    assert not len(wrong), f"{what}: {len(wrong)} elements differ, first {wrong[:4]}"


@pytest.fixture(scope="module")
def table():
    rng = np.random.default_rng(0)
    return rng.standard_normal((VOCAB, WIDTH), dtype=np.float32).astype(bfloat16)


@pytest.mark.supported_devices("npu2")
def test_rows_of_a_weight_are_gathered(table):
    n_ids = 512
    ids = gathered_ids(VOCAB, n_ids)
    graph = FromWeight(table, ids)
    net = graph.compile(x=(n_ids, WIDTH))
    assert net.plan.full_elf
    x = np.random.default_rng(1).standard_normal((n_ids, WIDTH)).astype(bfloat16)
    rows, total = graph(x)
    assert_equal(rows, table[ids], "gathered")
    expected_rows, expected_total = graph.reference(x)
    assert_equal(expected_rows, table[ids], "reference")
    assert_equal(total, np.asarray(expected_total), "the step after")


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("full_elf", [True, False])
def test_one_input_s_ids_gather_from_each_of_three_tables(table, full_elf):
    """Check that one input's ids gather from each of three tables.

    Each table's words follow the last's in the input's buffer, each
    encoded per call from the same ids, bounded alike.
    """
    tables = many_tables(table)
    graph = ManyTables(*tables)
    graph.compile(ids=((256,), np.int32), full_elf=full_elf)
    rng = np.random.default_rng(4)
    for n in (1, 13, 256):
        ids = rng.integers(0, 1000, 256).astype(np.int32)
        ids[n:] = VOCAB  # past every table: a bounded call reads none of them
        for k, got in enumerate(graph(ids, n=n)):
            expected = np.take(tables[k], ids[:n], axis=0)
            got = np.asarray(got, dtype=np.float32).reshape(256, -1)[:n]
            assert_equal(got, expected, f"table {k}, {n} rows")


@pytest.mark.supported_devices("npu2")
def test_rows_of_an_intermediate_are_gathered():
    n_rows, n_ids = 4096, 512
    ids = gathered_ids(n_rows, n_ids)
    table = np.random.default_rng(2).standard_normal((n_rows, WIDTH)).astype(bfloat16)
    graph = FromIntermediate(ids)
    assert_equal(graph(table), table[ids], "gathered")
    assert_equal(graph.reference(table), table[ids], "reference")


# A feed count left out resolves, to one feed for 15 rows and four past 48.
FEEDS = [(None, 15), (4, 71), (1, 512)]


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("feeds,n_ids", FEEDS)
def test_rows_each_call_names_are_gathered(table, feeds, n_ids):
    graph = PerCall(table, feeds)
    net = graph.compile(ids=((n_ids,), np.int32))
    assert net.plan.full_elf
    (gather,) = [s.op for s in net.recording.steps if isinstance(s.op, Gather)]
    assert gather.resolved().feeds == (feeds or (1 if n_ids <= 16 else 4))
    rng = np.random.default_rng(n_ids)
    for call in range(3):
        ids = rng.integers(-VOCAB, VOCAB, n_ids).astype(np.int32)
        ids[:2] = (-VOCAB, VOCAB - 1)
        expected = np.take(table, ids, axis=0)
        assert_equal(graph(ids), expected, f"call {call}")
        assert_equal(graph.reference(ids), expected, f"reference {call}")


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("feeds,n_ids", FEEDS)
def test_the_rows_a_call_bounds_are_gathered(table, feeds, n_ids):
    graph = Bounded(table, feeds)
    net = graph.compile(ids=((n_ids,), np.int32))
    assert net.plan.full_elf
    rng = np.random.default_rng(n_ids)
    for n in sorted({1, 9, n_ids // 2, n_ids - 1, n_ids} - {0}):
        ids = rng.integers(-VOCAB, VOCAB, n_ids).astype(np.int32)
        ids[n:] = VOCAB  # past the table: a bounded call reads none of them
        expected = np.take(table, ids[:n], axis=0)
        got = np.asarray(graph(ids, n=n), dtype=np.float32).reshape(-1, WIDTH)[:n]
        assert_equal(got, expected, f"{n} of {n_ids}")
        assert_equal(graph.reference(ids, n=n), expected, f"reference {n}")


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("feeds,n_ids", [(None, 1), *FEEDS])
def test_rows_ids_the_device_made_name_are_gathered(table, feeds, n_ids):
    other = np.random.default_rng(4).standard_normal((3000, 256)).astype(bfloat16)
    graph = FromDeviceIds(table, other, feeds)
    net = graph.compile(ids=((n_ids,), np.int32))
    assert net.plan.full_elf
    assert not net.recording.encoders
    resolved = {
        s.op.resolved().feeds for s in net.recording.steps if isinstance(s.op, Gather)
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
@pytest.mark.parametrize("feeds,n_ids", FEEDS)
def test_the_rows_a_call_bounds_by_ids_the_device_made_are_gathered(
    table, feeds, n_ids
):
    """Check that the rows a call bounds by ids the device made are gathered.

    The word step writes each row's length too: a whole row for the
    first ``n``, a unit for each other, as the bounded drains take them.
    """
    graph = BoundedDeviceIds(table, feeds)
    net = graph.compile(ids=((n_ids,), np.int32))
    assert net.plan.full_elf
    assert not net.recording.encoders
    rng = np.random.default_rng(n_ids)
    for n in sorted({1, 9, n_ids // 2, n_ids - 1, n_ids} - {0}):
        ids = rng.integers(-VOCAB, VOCAB, n_ids).astype(np.int32)
        ids[n:] = VOCAB  # past the table: clipped, and a unit of it moved
        expected = np.take(table, ids[:n], axis=0)
        got = np.asarray(graph(ids, n=n), dtype=np.float32).reshape(-1, WIDTH)[:n]
        assert_equal(got, expected, f"{n} of {n_ids}")
        assert_equal(graph.reference(ids, n=n), expected, f"reference {n}")


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("n_ids", [1, 256])
def test_rows_a_state_names_are_gathered(table, n_ids):
    graph = FromState(table, n_ids)
    net = graph.compile()
    rng = np.random.default_rng(n_ids)
    for call in range(3):
        ids = rng.integers(0, VOCAB, n_ids).astype(np.int32)
        net.write(graph.ids, ids)
        assert_equal(graph(), table[ids], f"call {call}")


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("full_elf", [None, False], ids=["full_elf", "xclbin"])
def test_a_graph_gathers_twice_from_a_weight_and_a_state(full_elf):
    n_rows, rows, soft = 4096, 64, 64
    rng = np.random.default_rng(3)
    table = rng.standard_normal((n_rows, WIDTH)).astype(bfloat16)
    graph = Merged(table, rows, soft)
    net = graph.compile(
        ids=((rows,), np.int32),
        soft=((soft, WIDTH), bfloat16),
        merge=((rows,), np.int32),
        full_elf=full_elf,
    )
    assert net.plan.full_elf == (full_elf is None)
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
def test_ids_past_the_table_are_refused(table, outside):
    graph = PerCall(table)
    ids = np.arange(15, dtype=np.int32)
    ids[7] = outside
    with pytest.raises(IndexError):
        graph(ids)
    with pytest.raises(IndexError):
        graph.reference(ids)


@pytest.mark.supported_devices("npu1", "npu2")
def test_each_step_gathers_the_rows_an_input_names(table):
    """Check that each step gathers the rows an input names.

    Each step its own xclbin, as NPU1 runs: the host encodes the ids
    against the table's address as a full ELF's do, and the step after
    reads the rows.
    """
    graph = Embedded(table)
    net = graph.compile(ids=((256,), np.int32), x=(256, WIDTH), full_elf=False)
    assert not net.plan.full_elf
    steps = [type(s.op).__name__ for s in net.recording.steps]
    assert steps == ["Gather", "ElementwiseAdd"]
    x = np.zeros((256, WIDTH), bfloat16)
    rng = np.random.default_rng(5)
    for call in range(3):
        ids = rng.integers(-VOCAB, VOCAB, 256).astype(np.int32)
        expected = np.take(table, ids, axis=0)
        assert_equal(graph(ids, x), expected, f"call {call}")
        assert_equal(graph.reference(ids, x), expected, f"reference {call}")


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("n_ids", [15, 256])
def test_each_step_gathers_the_rows_a_call_bounds(table, n_ids):
    """Check that each step gathers the rows a call bounds.

    Each step its own xclbin, as NPU1 runs a prompt chunk's embedding
    rows: the first ``n`` rows a call's ids name, the drains' lengths
    generated per call.
    """
    graph = Bounded(table)
    net = graph.compile(ids=((n_ids,), np.int32), full_elf=False)
    assert not net.plan.full_elf
    rng = np.random.default_rng(n_ids)
    for n in sorted({1, 9, n_ids // 2, n_ids}):
        ids = rng.integers(-VOCAB, VOCAB, n_ids).astype(np.int32)
        ids[n:] = VOCAB  # past the table: a bounded call reads none of them
        expected = np.take(table, ids[:n], axis=0)
        got = np.asarray(graph(ids, n=n), dtype=np.float32).reshape(-1, WIDTH)[:n]
        assert_equal(got, expected, f"{n} of {n_ids}")
        assert_equal(graph.reference(ids, n=n), expected, f"reference {n}")


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("n_ids", [15, 512])
def test_each_step_gathers_by_ids_the_device_made(table, n_ids):
    """Check that each step gathers by ids the device made.

    An xclbin's word step reads the table's address from its runtime
    parameters, which the sequence writes each call.
    """
    other = np.random.default_rng(4).standard_normal((3000, 256)).astype(bfloat16)
    graph = FromDeviceIds(table, other)
    net = graph.compile(ids=((n_ids,), np.int32), full_elf=False)
    assert not net.plan.full_elf
    rng = np.random.default_rng(n_ids)
    for call in range(3):
        ids = rng.integers(-len(other), len(other), n_ids).astype(np.int32)
        rows, others = graph(ids)
        assert_equal(rows, np.take(table, ids, axis=0), f"call {call}")
        assert_equal(others, other[ids], f"call {call}")


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("n_ids", [15, 256])
def test_each_step_gathers_the_rows_a_call_bounds_by_ids_the_device_made(table, n_ids):
    """Check that each step gathers the rows a call bounds by ids the device made.

    An xclbin's word step reads the bound from its runtime parameters,
    which the sequence writes each call.
    """
    graph = BoundedDeviceIds(table)
    net = graph.compile(ids=((n_ids,), np.int32), full_elf=False)
    assert not net.plan.full_elf
    rng = np.random.default_rng(n_ids)
    for n in sorted({1, 9, n_ids // 2, n_ids}):
        ids = rng.integers(-VOCAB, VOCAB, n_ids).astype(np.int32)
        ids[n:] = VOCAB
        expected = np.take(table, ids[:n], axis=0)
        got = np.asarray(graph(ids, n=n), dtype=np.float32).reshape(-1, WIDTH)[:n]
        assert_equal(got, expected, f"{n} of {n_ids}")


def _moved(gather: Gather, valid: int) -> np.ndarray:
    """Return the bytes each row's descriptor moves.

    Read from the control words a call with ``valid`` rows writes.
    """
    words = gather.control_words(np.arange(gather.rows), 0, valid)
    return words[gather.template[1] - 1].astype(np.int64) * 4


def test_a_bounded_gather_moves_its_rows_and_a_unit_for_each_other():
    for rows, feeds in ((1, 1), (15, 1), (71, 4), (512, 4), (2048, 4)):
        gather = Gather(rows=rows, table_rows=VOCAB, row=WIDTH, feeds=feeds)
        row_bytes = WIDTH * 2
        for valid in sorted(
            {0, 1, 13, rows // 2, rows - 1, rows} & set(range(rows + 1))
        ):
            moved = _moved(gather, valid)
            assert (moved[:valid] == row_bytes).all()
            assert (moved[valid:] == Gather.pad_bytes).all()
            # Each feed drains what its rows' descriptors moved.
            for k, run in enumerate(gather.runs):
                span = moved[run.start * Gather.chain : run.stop * Gather.chain]
                drained = gather.derived_at(f"drained{k}", valid_rows=valid)
                assert drained * 16 == span.sum(), (rows, valid, k)
        assert _moved(gather, None).sum() == rows * row_bytes


def test_a_bounded_prompt_chunk_moves_13_rows_not_2048():
    """Llama 3.2 1B's chunk: 2048 rows of 4096 bytes from 128256."""
    gather = Gather(rows=2048, table_rows=128256, row=2048, feeds=4)
    assert _moved(gather, None).sum() == 8 * 1024 * 1024
    assert _moved(gather, 13).sum() == 13 * 4096 + 2035 * 16 == 85808


def test_an_input_gathers_from_a_table_once(npu2, table):
    class Twice(iron.Graph):
        def __init__(self):
            self.table = iron.weight(table)

        def body(self, ids):
            return Copy.step(self.table[ids]), Copy.step(self.table[ids])

    with pytest.raises(ValueError, match="gathers from 'table' once"):
        Twice().record(ids=((16,), np.int32))
