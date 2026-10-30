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
from iron import Scratchpad
from iron.common.graph.compiled import apply_profile
from iron.common.graph.packing import apply as apply_packings
from iron.lm.generation import Sampler
from iron.lm.tune import calls
from iron.tests.support.llama_model import small
from iron.operators.copy import Copy
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.relu import ReLU
from iron.operators.sigmoid import Sigmoid
from iron.operators.tanh import Tanh
from iron.tune.autotune import Point, Timed
from iron.tune.costmodel import CostModel
from iron.tune.measure import Cache, Timing, platform
from iron.tune.packings import (
    Packer,
    _end_to_end,
    adjacent,
    price_packings,
    widen_packings,
    width_tunables,
)

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


LONG = 2**24


class Runs(iron.Graph):
    """Four ReLUs then four Tanhs over a long vector: one switch among eight
    long steps."""

    def body(self, x):
        for op in (ReLU, Tanh):
            for _ in range(4):
                x = op.step(x, num_aie_columns=8)
        return x


class BoundedReLUs(iron.Graph):
    """Two ReLUs over a call's first ``n`` elements."""

    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU.step(ReLU.step(x[:n]))


ROUND = 2**22


class Rounds(iron.Graph):
    """ReLU, Tanh and Sigmoid in turn over a call's first ``n`` elements,
    twice, at eight columns; given ``other``, a second version over the same
    arrays (it copies ``other`` too). A short call is switch-bound and a long
    one bound by the arrays' own time, as a decode step and a prompt chunk
    are."""

    def body(self, x, other=None, *, n: Scratchpad[np.int32]):
        x = x[:n]
        for _ in range(2):
            for op in (ReLU, Tanh, Sigmoid):
                x = op.step(x, num_aie_columns=8)
        if other is None:
            return x
        return x, Copy.step(other)


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


def test_a_packing_names_no_dimension_a_hosts_context_sizes(npu2, tmp_path):
    """A host fits its own context, which sizes the decode step's KV cache
    and so MHA and the cache copies: a packing found at one context names
    none of those dimensions, so the model fitted to another packs the same
    designs together."""
    model, sibling = small(), small(max_seq_len=512)
    decode, _ = calls(model, 0, 0, 256, 1, Sampler(0.7, 50), sibling)
    assert any("kv_len" in v for v in decode.varying.values())
    packer = Packer(
        decode,
        npu2,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=None,
        fit_cache=tmp_path / "fit",
        log=lambda _: None,
        lock=False,
        model=CostModel(),
    )
    members = packer.members({k: {} for k in packer.shapes})
    assert not any("kv_len" in dims for cls, dims, _ in members if cls is MHA)
    profile = iron.Profile()
    profile.add_packing(members)
    sizes = []
    for m in (model, sibling):
        _, packing = apply_packings(m.record(**m.shapes()[0]), profile, [], npu2)
        sizes.append([len(g) for g in packing.groups])
    assert sizes[0] == sizes[1] and sizes[0], sizes


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
    kept = []
    profile = price_packings(
        [Timed(recording)],
        dev,
        iron.Profile(),
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=cache,
        fit_cache=tmp_path / "fit",
        progress=lambda found, model: kept.append(found),
        log=print,
    )
    assert len(profile.packings()) == 1
    assert [len(p.packings()) for p in kept] == [1], "the version's find, kept"
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
def test_price_packings_skips_a_version_its_switches_cannot_pay(tmp_path):
    """One switch beside eight long steps: no grouping could gain the
    share packing is worth searching for, so the version is not searched."""
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    logged = []
    profile = price_packings(
        [Timed(Runs().record(x=(LONG,)))],
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
    assert not profile.packings()
    assert any(line.endswith("not searched") for line in logged)
    assert not any("grouped" in line for line in logged)


@pytest.mark.supported_devices("npu2")
def test_end_to_end_runs_a_call_at_each_of_its_points():
    """A point bounding past the graph's input is a call it refuses: the
    end-to-end check runs the call at each of its points, not only at its
    own values."""
    dev = aie_utils.ensure_current_device()
    recording = BoundedReLUs().record(x=(SIZE,))
    profile = iron.Profile()
    timing = Timing(rounds=1, calls=2)
    own = Timed(recording, values=dict(n=SIZE))
    delta, _ = _end_to_end(own, dev, profile, profile, timing, print, False)
    assert np.isfinite(delta)
    past = Timed(
        recording,
        values=dict(n=SIZE),
        points=[Point(0.5, dict(n=SIZE)), Point(0.5, dict(n=2 * SIZE))],
    )
    with pytest.raises(IndexError):
        _end_to_end(past, dev, profile, profile, timing, print, False)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("rows, applies", [(2048, True), (ROUND, False)])
def test_widen_packings_applies_an_entry_only_where_it_pays(rows, applies):
    """An entry found in one version narrows its arrays to one column. In
    the other version, at short calls it removes switches and applies
    there too; at long calls the narrowed arrays cost more than the switches
    it removes, so it keeps to the version it names rather than being
    dropped."""
    dev = aie_utils.ensure_current_device()
    first = Rounds().record(x=(ROUND,))
    second = Rounds().record(x=(ROUND,), other=(64,))
    narrow = {"num_aie_columns": 1, "num_channels": 1}
    profile = iron.Profile()
    profile.add_packing(
        [(op, {"size": ROUND}, narrow) for op in (ReLU, Tanh, Sigmoid)],
        versions=[first.version],
    )
    logged = []
    widened = widen_packings(
        [Timed(first, values=dict(n=2048)), Timed(second, values=dict(n=rows))],
        dev,
        profile,
        timing=Timing(rounds=2, calls=5),
        log=logged.append,
    )
    print("\n".join(logged))
    (entry,) = widened.packings()
    want = {first.version, second.version} if applies else {first.version}
    assert entry.versions == want, logged
    _, _, packing = apply_profile(second, widened, dev)
    assert bool(packing.groups) == applies


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
    (entry,) = profile.packings()
    assert entry.versions == {recording.version}
    assert any(tunables for _, _, tunables in entry.members), "nothing was narrowed"
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
