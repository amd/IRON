# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pricing packings: a version's arrays grouped into shared device
configurations (``iron.tune.packings``). No NPU above ``# On the device``.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common.graph.compiled import apply_profile
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.relu import ReLU
from iron.operators.sigmoid import Sigmoid
from iron.operators.tanh import Tanh
from iron.tune.autotune import Timed
from iron.tune.costmodel import CostModel
from iron.tune.measure import Cache, Timing, platform
from iron.tune.packings import Packer, adjacent, price_packings, width_tunables

pytestmark = pytest.mark.usefixtures("npu2")

SIZE = 2048


class Alternating(iron.Graph):
    """ReLU and Tanh in turn, eight steps: every step a switch apart."""

    def body(self, x):
        for _ in range(4):
            x = Tanh.step(ReLU.step(x, num_aie_columns=8), num_aie_columns=8)
        return x


WIDE = 8192


class Wide(iron.Graph):
    """ReLU, Tanh and Sigmoid in turn at eight columns and two channels,
    twice: 16 cores each, 48 together, so packed only narrowed."""

    def body(self, x):
        for _ in range(2):
            for op in (ReLU, Tanh, Sigmoid):
                x = op.step(x, num_aie_columns=8, num_channels=2)
        return x


class Projections(iron.Graph):
    """One shape's GEMV twice, at two output tiles: two arrays, as q and o
    were with only q given half a head's tiles."""

    def body(self, w, x):
        y = GEMV.step(w, x, tile_size_output=32)
        return GEMV.step(w, y, tile_size_output=256)


def _packer(recording, dev, tmp_path):
    return Packer(
        Timed(recording),
        dev,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=None,
        fit_cache=tmp_path / "fit",
        log=lambda _: None,
        lock=False,
        model=CostModel(),
    )


def test_width_tunables_are_the_ones_counting_columns_channels_or_cores():
    assert width_tunables(GEMV(M=512, K=2048)) == ["num_aie_columns", "num_channels"]
    assert width_tunables(MHA(num_heads=32, num_KV_heads=8, d=64, seq_pad=1)) == [
        "num_pipelines"
    ]


def test_adjacent_counts_the_switches_a_merge_removes():
    order = ["a", "b", "a", "b", None, "c", "c", "a"]
    assert adjacent(order, {"a": 0, "b": 1, "c": 2}) == {(0, 1): 3, (0, 2): 1}
    assert adjacent(order, {"a": 0, "b": 0, "c": 2}) == {(0, 2): 1}


def test_a_packer_finds_each_array_and_its_narrower_widths(npu2, tmp_path):
    packer = _packer(Alternating().record(x=(SIZE,)), npu2, tmp_path)
    assert len(packer.shapes) == 2
    assert [k is not None for k in packer.order] == [True] * 8
    relu, tanh = packer.order[:2]
    assert packer.cores({relu: {}}) == 8
    narrow = {"num_aie_columns": 1, "num_channels": 1}
    assert narrow in packer.options(relu)
    assert packer.cores({relu: narrow, tanh: {}}) == 9


def test_one_shapes_two_arrays_are_one_unit_a_change_aligns(npu2, tmp_path):
    """A profile names shapes, so the two GEMVs of one shape are one unit,
    set as one; aligning it to one of its arrays' settings puts both on it.
    """
    packer = _packer(Projections().record(w=(2048, 2048), x=(2048,)), npu2, tmp_path)
    (unit,) = set(packer.order)
    assert len(packer.arrays(unit, {})) == 2
    aligned = [
        packer.cores({unit: s})
        for k, s in packer.changes({unit: {}})
        if len(packer.arrays(k, s)) == 1
    ]
    assert min(aligned) * 2 == packer.cores({unit: {}})


# ---------------------------------------------------------------------------
# On the device
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
def test_price_packings_packs_alternating_arrays_bit_identically(tmp_path):
    """Eight steps of two 8-column arrays, each step a switch: the packer
    narrows them to share one configuration and keeps it end to end; the
    packed graph computes what the unpacked one does."""
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    recording = Alternating().record(x=(SIZE,))
    profile = price_packings(
        [Timed(recording)],
        dev,
        iron.Profile(),
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=cache,
        fit_cache=tmp_path / "fit",
        log=print,
    )
    assert len(profile.packings()) == 1
    _, _, packing = apply_profile(recording, profile, dev)
    assert len(packing.groups) == 1 and len(packing.groups[0]) == 2

    packed_graph = Alternating()
    packed_graph.profile = profile
    packed = packed_graph.compile(x=(SIZE,))
    plain = Alternating().compile(x=(SIZE,))
    x = (np.random.default_rng(0).random(SIZE) * 4 - 2).astype(bfloat16)
    want = np.asarray(plain(x))
    got = np.asarray(packed(x))
    assert np.array_equal(want.view(np.uint16), got.view(np.uint16))
    reference = np.tanh(np.maximum(x.astype(np.float32), 0))
    for _ in range(3):
        reference = np.tanh(np.maximum(reference, 0))
    np.testing.assert_allclose(got.astype(np.float32), reference, atol=2e-2)


@pytest.mark.supported_devices("npu2")
def test_price_packings_narrows_what_does_not_co_reside(tmp_path):
    """Three arrays of 16 cores each take 48 of 32 at their own widths: the
    packer narrows the cheapest until they share one configuration, and the
    packed graph computes what the unpacked one does."""
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    recording = Wide().record(x=(WIDE,))
    logged = []
    profile = price_packings(
        [Timed(recording)],
        dev,
        iron.Profile(),
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=cache,
        fit_cache=tmp_path / "fit",
        log=logged.append,
    )
    print("\n".join(logged))
    (members,) = profile.packings()
    assert any(tunables for _, _, tunables in members), "nothing was narrowed"
    packed_graph = Wide()
    packed_graph.profile = profile
    packed = packed_graph.compile(x=(WIDE,))
    plain = Wide().compile(x=(WIDE,))
    x = (np.random.default_rng(0).random(WIDE) * 4 - 2).astype(bfloat16)
    assert np.array_equal(
        np.asarray(plain(x)).view(np.uint16), np.asarray(packed(x)).view(np.uint16)
    )
    reference = x.astype(np.float32)
    for _ in range(2):
        reference = 1 / (1 + np.exp(-np.tanh(np.maximum(reference, 0))))
    np.testing.assert_allclose(
        np.asarray(packed(x)).astype(np.float32), reference, atol=2e-2
    )
