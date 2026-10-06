#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A gather of a table's rows, ``Copy(table[ids])``, on a device.

The ids are known when the graph is traced; each row, or each run of rows
whose ids step evenly, is one transfer of the step's sequence. The table is
a weight at EmbeddingGemma 2's size, or an intermediate a step before
produced.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.operators import ElementwiseAdd
from iron.operators.copy import Copy

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
