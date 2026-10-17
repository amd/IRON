#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A copy of a bounded view, by head, on a device.

``Copy(x[:n].reshape(T, H, D).transpose(1, 0, 2))`` moves the ``n`` valid
rows of each head: into a fresh output and into a cache given whole, both
bounded alike, so the drain ends where the fill does. A walk of a table by
a per-call repeat and length (``Handle.at``) moves the bands and blocks a
call names, and cut into groups of bands, each group walked in turn by a
repeat of its own.
"""

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.operators.copy import Copy
from iron.operators.relu import ReLU

T, H, D = 256, 4, 64

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


@pytest.mark.supported_devices("npu2")
def test_a_copy_moves_the_valid_rows_of_each_head():
    cache = iron.state((H, T, D), name="cache")

    class ByHead(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            k = ReLU.step(x[:n]).reshape(T, H, D).transpose(1, 0, 2)
            Copy.step(k, cache)
            return Copy.step(k)

    step = ByHead()
    net = step.compile(x=(T, H * D))
    rng = np.random.default_rng(0)
    for n in (1, 50, 129, T):
        x = rng.standard_normal((T, H * D)).astype(bfloat16)
        net.write(cache, np.zeros((H, T, D), dtype=np.float32))
        out = np.asarray(net(x, n=n), dtype=np.float32).reshape(H, T, D)
        want = np.maximum(x[:n].astype(np.float32), 0).astype(bfloat16)
        want = want.astype(np.float32).reshape(n, H, D).transpose(1, 0, 2)
        assert np.array_equal(out[:, :n], want), f"{n=}: the output's valid rows"
        got = np.asarray(net.read(cache), dtype=np.float32).reshape(H, T, D)
        assert np.array_equal(got[:, :n], want), f"{n=}: the cache's valid rows"
        assert not got[:, n:].any(), f"{n=}: a row past the bound was written"


# A table of blocks walked band by band: `wk` blocks of K2 rows a band, `hk`
# bands a call, each band the same blocks (stride 0) or the next ones.
HK, WK, K2, E = 8, 6, 9, 64


class Walk(iron.Graph):
    def __init__(self, table, band_stride: int):
        self.table = iron.weight(table)
        self.band_stride = band_stride

    def body(
        self,
        *,
        hk: Scratchpad[np.int32],
        wk: Scratchpad[np.int32],
        n: Scratchpad[np.int32],
    ):
        tap = TensorAccessPattern(
            self.table.shape,
            0,
            [HK, WK, K2, E],
            [self.band_stride * K2 * E, K2 * E, E, 1],
        )
        rows = self.table.at(
            tap, (HK * WK * K2, E), bounds={0: n}, repeat=hk, length=wk
        )
        return Copy.step(rows)


def walked(table, band_stride: int, hk: int, wk: int) -> np.ndarray:
    """The rows `hk` bands of `wk` blocks walk, band `b` from block `b * band_stride`."""
    starts = [b * band_stride * K2 for b in range(hk)]
    return np.concatenate([table[s : s + wk * K2] for s in starts])


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("full_elf", [True, False], ids=["full_elf", "xclbin"])
@pytest.mark.parametrize("band_stride", [0, 1])
def test_a_walk_repeats_and_bounds_per_call(full_elf, band_stride):
    rng = np.random.default_rng(band_stride)
    table = rng.standard_normal((HK * WK * K2, E)).astype(bfloat16)
    graph = Walk(table, band_stride)
    net = graph.compile(full_elf=full_elf)
    assert net.plan.full_elf == full_elf
    for hk, wk in ((3, 4), (HK, WK), (1, 1), (5, 2)):
        n = hk * wk * K2
        got = np.asarray(net(hk=hk, wk=wk, n=n), dtype=np.float32).reshape(-1, E)
        want = walked(table, band_stride, hk, wk).astype(np.float32)
        assert np.array_equal(got[:n], want), f"{hk=} {wk=}"


# `Walk`'s bands in groups, (first band, bands): each walked in turn.
GROUPS = ((0, 2), (2, 2), (4, 4))


class Walks(iron.Graph):
    def __init__(self, table, band_stride: int):
        self.table = iron.weight(table)
        self.band_stride = band_stride

    def body(
        self,
        *,
        r0: Scratchpad[np.int32],
        r1: Scratchpad[np.int32],
        r2: Scratchpad[np.int32],
        wk: Scratchpad[np.int32],
        n: Scratchpad[np.int32],
    ):
        taps = tuple(
            TensorAccessPattern(
                self.table.shape,
                first * self.band_stride * K2 * E,
                [bands, WK, K2, E],
                [self.band_stride * K2 * E, K2 * E, E, 1],
            )
            for first, bands in GROUPS
        )
        rows = self.table.at(
            taps, (HK * WK * K2, E), bounds={0: n}, repeat=(r0, r1, r2), length=wk
        )
        return Copy.step(rows)


def walks_values(hk: int, wk: int) -> dict:
    """A call's values: each group's repeat, at least one, and the rows moved."""
    repeats = [min(max(hk - first, 1), bands) for first, bands in GROUPS]
    n = sum(repeats) * wk * K2
    return dict(zip(("r0", "r1", "r2"), repeats), wk=wk, n=n)


def walks_walked(table, band_stride: int, hk: int, wk: int) -> np.ndarray:
    """The rows `Walks` moves: each group's bands, past the image a group's first."""
    values = walks_values(hk, wk)
    return np.concatenate(
        [
            walked(table[first * band_stride * K2 :], band_stride, values[r], wk)
            for (first, _), r in zip(GROUPS, ("r0", "r1", "r2"))
        ]
    )


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("full_elf", [True, False], ids=["full_elf", "xclbin"])
@pytest.mark.parametrize("band_stride", [0, 1])
def test_walks_in_turn_repeat_each_per_call(full_elf, band_stride):
    rng = np.random.default_rng(band_stride)
    table = rng.standard_normal((HK * WK * K2, E)).astype(bfloat16)
    net = Walks(table, band_stride).compile(full_elf=full_elf)
    assert net.plan.full_elf == full_elf
    for hk, wk in ((3, 4), (HK, WK), (1, 1), (5, 2)):
        values = walks_values(hk, wk)
        n = values["n"]
        got = np.asarray(net(**values), dtype=np.float32).reshape(-1, E)
        want = walks_walked(table, band_stride, hk, wk).astype(np.float32)
        assert np.array_equal(got[:n], want), f"{hk=} {wk=}"


# Rows past D1's 1023 wrap, bounded per call, into either half of a state's rows.
ROWS, HALF = 2048, 32


class Halves(iron.Graph):
    def __init__(self):
        self.rows = iron.state((ROWS, 2 * HALF), name="rows")

    def body(self, x, y, *, n: Scratchpad[np.int32]):
        Copy.step(x[:n], self.rows[:n, :HALF])
        Copy.step(y[:n], self.rows[:n, HALF:])
        return Copy.step(self.rows[:n])


@pytest.mark.supported_devices("npu2")
def test_bounded_rows_past_a_wrap_fill_either_half():
    net = Halves().compile(x=(ROWS, HALF), y=(ROWS, HALF))
    rng = np.random.default_rng(0)
    for n in (1, 1024, ROWS):
        x, y = (rng.standard_normal((ROWS, HALF)).astype(bfloat16) for _ in range(2))
        got = np.asarray(net(x, y, n=n), dtype=np.float32).reshape(ROWS, 2 * HALF)
        want = np.concatenate([x[:n], y[:n]], axis=1).astype(np.float32)
        assert np.array_equal(got[:n], want), f"{n=}"
