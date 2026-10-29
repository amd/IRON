# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pricing on-chip chains: grouping the edges a tuner's calls admit, and
choosing among them cheapest first. No device below the line.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile
from iron.common.graph.chain import candidates
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.silu import SiLU
from iron.tests.support.graphs import Chain as ChainGraph
from iron.tests.support.llama_model import small
from iron.tune.autotune import Point, Timed, Trial
from iron.tune.chains import ChainGroup, chain_groups, price_chains, select_rewrites
from iron.tune.measure import Cache, Timing, platform

pytestmark = pytest.mark.usefixtures("npu2")

W = np.zeros(2048, bfloat16)


def _fused_graph():
    """A graph recording ``ElementwiseMul(SiLU(x), W)``, chainable at size=2048."""

    class Fused(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=2048, num_aie_columns=1)
            return ElementwiseMul.step(gate, W, tile_size=2048, num_aie_columns=1)

    return Fused()


def _group(dev, producer_at: int, rid: int = 0) -> ChainGroup:
    """A ``ChainGroup`` of SiLU -> ElementwiseMul, occurring once at
    ``producer_at`` of recording ``rid``: enough for ``select_rewrites``.
    """
    silu = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    mul = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    group = ChainGroup(silu, mul, "y", "a")
    group.occurrences = [(rid, producer_at)]
    return group


# ---------------------------------------------------------------------------
# chain_groups: grouping and weights
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def llama_recordings():
    model = small()
    decode_shapes, prompt_shapes = model.shapes()
    C = model.config.prefill_chunk
    decode = Timed(model.record(**decode_shapes))
    prompt = Timed(
        model.record(**prompt_shapes),
        values=dict(position=C - 1, token=0, start=0, rows=C, rope_start=0),
    )
    return decode, prompt


def test_chain_groups_merges_identical_shapes_across_llama_layers(llama_recordings):
    decode, prompt = llama_recordings
    dev = aie_utils.ensure_current_device()
    groups = chain_groups([decode, prompt], dev)

    def silu_group(recording):
        rid = id(recording)
        return next(
            g
            for g in groups
            if g.producer_shape.cls is SiLU
            and g.consumer_shape.cls is ElementwiseMul
            and g.occurrences[0][0] == rid
        )

    def silu_edges(recording):
        return [
            e
            for e in candidates(recording)
            if type(recording.steps[e.producer].op.resolved(dev)) is SiLU
            and type(recording.steps[e.producer + 1].op.resolved(dev)) is ElementwiseMul
        ]

    decode_group = silu_group(decode.recording)
    prompt_group = silu_group(prompt.recording)
    assert (
        len(decode_group.occurrences) == len(silu_edges(decode.recording)) == 2
    )  # per layer
    assert len(prompt_group.occurrences) == len(silu_edges(prompt.recording)) == 2
    # Every layer shares one identity: its points are not counted per layer.
    assert len(decode_group.points) == 1
    assert len(prompt_group.points) == 1


def test_chain_groups_merges_repeated_shapes_and_tracks_every_occurrence():
    dev = aie_utils.ensure_current_device()
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    groups = chain_groups([Timed(recording)], dev)
    assert len(groups) == 3

    add_to_silu = next(g for g in groups if g.producer_shape.cls is ElementwiseAdd)
    assert sorted(p for _, p in add_to_silu.occurrences) == [0, 3]
    assert len(add_to_silu.points) == 1  # both occurrences share one identity

    silu_to_mul = next(g for g in groups if g.consumer_shape.cls is ElementwiseMul)
    assert sorted(p for _, p in silu_to_mul.occurrences) == [1]

    mul_to_add = next(g for g in groups if g.producer_shape.cls is ElementwiseMul)
    assert sorted(p for _, p in mul_to_add.occurrences) == [2]


def test_chain_groups_carries_each_points_weight():
    dev = aie_utils.ensure_current_device()
    recording = _fused_graph().record(x=(2048,))
    calls = [Timed(recording, points=[Point(0.3, {}), Point(0.7, {})])]
    [group] = chain_groups(calls, dev)
    assert [weight for weight, _, _ in group.points] == [0.3, 0.7]


# ---------------------------------------------------------------------------
# select_rewrites: cheapest first, never two sharing a step
# ---------------------------------------------------------------------------


def test_select_rewrites_takes_every_non_overlapping_gain():
    dev = aie_utils.ensure_current_device()
    a, b = _group(dev, 0), _group(dev, 4)
    priced = [(a, Trial({}, -10.0, 1.0)), (b, Trial({}, -5.0, 1.0))]
    assert set(select_rewrites(priced, log=lambda _: None)) == {a, b}


def test_select_rewrites_prefers_the_cheaper_of_two_overlapping_gains():
    dev = aie_utils.ensure_current_device()
    costlier, cheaper = _group(dev, 0), _group(dev, 0)
    # The cheaper is priced second: cost, not discovery order, decides.
    priced = [
        (costlier, Trial({}, -5.0, 1.0)),
        (cheaper, Trial({}, -20.0, 1.0)),
    ]
    assert select_rewrites(priced, log=lambda _: None) == [cheaper]


def test_select_rewrites_excludes_a_trial_that_does_not_gain():
    dev = aie_utils.ensure_current_device()
    gains, flat = _group(dev, 0), _group(dev, 4)
    priced = [(gains, Trial({}, -10.0, 1.0)), (flat, Trial({}, 2.0, 1.0))]
    assert select_rewrites(priced, log=lambda _: None) == [gains]


def test_select_rewrites_excludes_a_refused_trial():
    dev = aie_utils.ensure_current_device()
    group = _group(dev, 0)
    priced = [(group, Trial({}, -10.0, 1.0, refused="not bit-identical"))]
    assert select_rewrites(priced, log=lambda _: None) == []


# ---------------------------------------------------------------------------
# price_chains: the profile it returns
# ---------------------------------------------------------------------------


def test_price_chains_with_no_candidates_keeps_tunables_and_chain_entries():
    dev = aie_utils.ensure_current_device()
    profile = Profile()
    profile.add(SiLU, num_aie_columns=1)
    profile.add_chain(
        SiLU,
        ElementwiseMul,
        "a",
        producer_dims=dict(size=4096),
        consumer_dims=dict(size=4096),
    )
    out = price_chains([], dev, profile, full_elf=True, log=lambda _: None)
    assert out.tunables_for(SiLU, {}) == {"num_aie_columns": 1}
    gate = SiLU(size=4096, tile_size=4096, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=4096, tile_size=4096, num_aie_columns=1).resolved()
    assert out.chained(gate, up, "a")


# ---------------------------------------------------------------------------
# On the device: a gaining chain is written and runs bit-identically.
# ---------------------------------------------------------------------------

CHAIN_SIZE, CHAIN_TILE, CHAIN_COLS = 2**22, 4096, 8
W_BIG = np.zeros(CHAIN_SIZE, bfloat16)


def _big_fused_graph():
    class Fused(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=CHAIN_TILE, num_aie_columns=CHAIN_COLS)
            return ElementwiseMul.step(
                gate, W_BIG, tile_size=CHAIN_TILE, num_aie_columns=CHAIN_COLS
            )

    return Fused()


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_pricing_a_gaining_chain_writes_an_entry_that_runs_bit_identically(tmp_path):
    recording = _big_fused_graph().record(x=(CHAIN_SIZE,))
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    profile = price_chains(
        [Timed(recording)],
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        cache=cache,
        log=lambda _: None,
    )
    gate = SiLU(
        size=CHAIN_SIZE, tile_size=CHAIN_TILE, num_aie_columns=CHAIN_COLS
    ).resolved()
    up = ElementwiseMul(
        size=CHAIN_SIZE, tile_size=CHAIN_TILE, num_aie_columns=CHAIN_COLS
    ).resolved()
    assert profile.chained(gate, up, "a")

    chained_graph = _big_fused_graph()
    chained_graph.profile = profile
    chained = chained_graph.compile(full_elf=True, x=(CHAIN_SIZE,))
    plain = _big_fused_graph().compile(full_elf=True, x=(CHAIN_SIZE,))

    rng = np.random.default_rng(0)
    x = (rng.random(CHAIN_SIZE) * 4 - 2).astype(bfloat16)
    want = np.array(plain(x).numpy()[:CHAIN_SIZE])
    got = np.array(chained(x).numpy()[:CHAIN_SIZE])
    assert want.view(np.uint16).tolist() == got.view(np.uint16).tolist()
