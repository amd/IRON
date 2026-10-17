#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A copy of a bounded view, by head, on a device.

``Copy(x[:n].reshape(T, H, D).transpose(1, 0, 2))`` moves the ``n`` valid
rows of each head: into a fresh output and into a cache given whole, both
bounded alike, so the drain ends where the fill does. A walk of a table by
a per-call repeat and length (``Handle.at``) moves the bands and blocks a
call names.
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
