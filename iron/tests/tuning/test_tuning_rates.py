# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The multi-rate family: single rate, multi-rate ``p : 1``, and rates that cannot balance."""

import math

import pytest
from aie.iron.trace import Scope

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Member, Refinement, Region
from iron.common.design import OperatorDesign
from iron.common.graph.fusion import composed
from iron.common.graph.record import Recording
from iron.common.graph.sdf import Derivation, analyze
from iron.common.image.compose import fused_configuration
from iron.common.image.step import Edge, EdgeKind
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemm import GEMM
from iron.operators.limbs import Limbs
from iron.tests.support import sequences, toys_edges
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.tools import DEVICES
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import _balanced_at, candidates, check, fit, search

pytestmark = pytest.mark.usefixtures("device")


def test_single_rate_edge_round_trips(device):
    """``add -> SiLU -> mul`` at an equal-width edge: the candidate generator proposes it unchanged among its own edits."""
    add, silu, mul = toys.add_silu_mul()
    region = toys.add_silu_mul_region(add, silu, mul)
    entry = Entry(root=region)
    recording = toys.add_silu_mul_recording("single-rate", add, silu, mul)
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, device)
    )


def test_gemm_tiles_into_rowwise_op_is_a_multi_rate_edge(device):
    """A GEMM's 64-row tile into a per-row op: one object a call into 64, and one object of buffer.

    The tile is the GEMM's whole 64-row output, so its lane moves one object
    a call; the memtile that restages it into the norm's rows takes that one
    object a round, so the producer's side of the edge holds one, not the
    ``64 + 1 - gcd(64, 1)`` rows a shared row-by-row buffer would.
    """
    gemm, norm = toys.gemm_rowwise(device, row_tile=64)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm)
    recording = toys.gemm_rowwise_recording("gemm-rows", gemm, norm)
    analysis = analyze(region, recording, device)
    assert analysis.consistent
    assert analysis.repetition == {0: 1, 1: 64}
    assert analysis.min_depth[region.edges[0]] == 1


def test_limbs_expansion_is_a_real_six_to_one_multi_rate_edge(device):
    """``Limbs`` writes six bf16 planes a row into a plane-sized consumer: one object a firing into six.

    ``Limbs`` fires once a row and writes one object of six planes; the
    consumer reads one plane an object, so it fires six times a ``Limbs``
    firing over the same 61,440 elements. A memtile re-chunks each six-plane
    object into planes, so the producer's side holds one object.
    """
    limbs = Limbs(rows=64, line=160, num_aie_columns=1)
    planes = 6 * limbs.rows
    consumer = ElementwiseAdd(
        size=planes * limbs.line, tile_size=limbs.line, num_aie_columns=1
    )
    edge = Edge(0, "y", 1, "a")
    region = Region(
        parts=(
            Member(cls=Limbs, dims={"rows": limbs.rows, "line": limbs.line}),
            Member(cls=ElementwiseAdd, dims={"size": consumer.size}),
        ),
        edges=(edge,),
    )
    steps = sequences.steps((limbs, "x", "mid"), (consumer, "mid", "w", "out"))
    recording = Recording.of_steps("limbs-expansion", steps, ["x", "w"], ["out"])
    analysis = analyze(region, recording, device)
    assert analysis.consistent
    assert analysis.repetition == {0: limbs.rows, 1: planes}
    assert analysis.tokens[edge] == ((1,), (1,))
    assert analysis.min_depth[edge] == 1


def test_per_call_bounded_token_count_is_a_valid_kv_length(device):
    """A GEMM over the first ``n`` of 48 rows (a valid KV length short of ``M``), each row then normalized.

    At ``n = 16`` with a 16-row tile, a call fires the GEMM once and the
    norm 16 times: the analysis is held to the call's own values, not the
    48 rows recorded.
    """
    recording = toys.BoundedRows(tile_m=16).record(a=(48, 64), b=(64, 64))
    region = Region(
        tuple(
            Member(cls=type(s.op), dims=Profile.dims(type(s.op), vars(s.op)))
            for s in recording.steps
        ),
        (Edge(0, "C", 1, "x"),),
    )
    analysis = analyze(region, recording, device, {"n": 16})
    assert analysis.consistent
    assert analysis.repetition == {0: 1, 1: 16}


@pytest.mark.parametrize("n", [0, 16, 20, 32, 48])
def test_a_bounded_gemms_loops_are_read_off_its_words(n, device):
    """A GEMM over the first ``n`` of 48 rows: its loops' trips are the words its program reads at the call, not solved from the objects it moves.

    Its row blocks, column tiles and K tiles each, then the padding tiles
    and their K tiles, which object counts alone settle more than one way.
    """
    recording = toys.BoundedRows(tile_m=16).record(a=(48, 64), b=(64, 64))
    gemm = recording.steps[0].op
    region = Region(
        (Member(cls=GEMM, dims=Profile.dims(GEMM, vars(gemm))),),
    )
    derivation = Derivation(region, recording, device, {"n": n})
    (core,) = derivation.recorded[0][1].cores
    loops = []
    nested = [core]
    while nested:
        scope = nested.pop()
        if scope is not core:
            loops.append(derivation.read[id(scope)])
        nested += reversed([s for s in scope.body if isinstance(s, Scope)])
    blocks = -(-n // 16)
    assert loops == [blocks, 1, 1, 3 - blocks, 1]


def _bounded_rows_region(columns: int, kind: EdgeKind) -> tuple[Recording, Region]:
    """Return ``BoundedRows`` over 48 rows of ``columns`` columns, a 16-row tile, and its region over a ``kind`` edge."""
    recording = toys.BoundedRows(tile_m=16).record(a=(48, 64), b=(64, columns))
    region = Region(
        tuple(
            Member(cls=type(s.op), dims=Profile.dims(type(s.op), vars(s.op)))
            for s in recording.steps
        ),
        (Edge(0, "C", 1, "x", kind=kind),),
    )
    return recording, region


def test_a_bounded_gemm_draining_every_tile_into_valid_rows_is_refused(device):
    """A bounded GEMM draining every tile, its padding too, into a norm over only the valid rows: refused at the analysis.

    Its lanes each hold two column tiles. Each lane's C walk then takes every descriptor dimension, so no per-call
    length sizes its row blocks: at ``n = 16`` it writes 48 rows, and the
    norm reads 16.
    """
    recording, region = _bounded_rows_region(128, EdgeKind.STREAM)
    assert not recording.steps[0].op.resolved(device).drains_bounded
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording, {"n": 16})], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "objects written a call" in result.why


def test_a_valid_kv_length_streamed_into_its_rows_is_refused_past_whole_tiles(device):
    """``BoundedRows``' GEMM streamed into its norm a row at a time: refused at the analysis, for every call it serves.

    Its C drains the 16-row blocks a call computes, the norm the call's
    ``n`` rows: at ``n = 16, 32, 48`` they balance, but at ``n = 1`` one
    block, 16 rows, meets one row read, the other 15 left for the next
    call. One image serves every ``n`` the recording admits.
    """
    recording, region = _bounded_rows_region(64, EdgeKind.STREAM)
    assert recording.steps[0].op.resolved(device).drains_bounded
    profile = Profile()
    profile.add_entry(Entry(root=region))
    for n in (16, 48):
        result = fit(profile, [Timed(recording, {"n": n})], device)
        assert not result.ok
        assert result.stage == "analysis"
        assert "at n = 1," in result.why
        assert "objects written a call" in result.why


# Where GEMM composes beside another operator on the device: npu1's runs wait to
# be checked on an npu1 host (they compile and fit here).
_GEMM_BESIDE = [
    pytest.param(name, id=f"device_{name}", marks=() if name == "npu2" else unbuilt)
    for name in sorted(DEVICES)
]


@pytest.mark.parametrize("device", _GEMM_BESIDE, indirect=True)
@pytest.mark.parametrize("row_tile", [16, 64])
@pytest.mark.supported_devices("npu1", "npu2")
def test_gemm_tiles_delivered_a_row_at_a_time_are_bit_identical(row_tile, device):
    """A GEMM's ``row_tile``-row tile delivered to a per-row norm a row at a time over one stream (an asymmetric fifo): bit-identical to the steps run apart."""
    gemm, norm = toys.gemm_rowwise(device, M=row_tile, row_tile=row_tile)
    assert gemm.n_aie_rows == 1
    profile = Profile()
    profile.add_entry(Entry(root=toys.gemm_rowwise_region(gemm, norm)))
    recording = toys.gemm_rowwise_recording("delivered-rows", gemm, norm)
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


def test_buffer_below_the_computed_minimum_is_refused(device):
    """A multi-rate stream (``16 : 1`` rows) one object short of its minimum buffer is refused by ``fit`` at stage ``"analysis"``, before any build.

    The GEMM's 16-row tile is delivered to the norm a row at a time (one
    asymmetric fifo). Its minimum buffer is ``p + c - gcd(p, c)`` elements,
    ``1024 + 64 - 64``: one of the producer's objects, the unit an edge's
    depth counts. At it, the region fits.
    """
    gemm, norm = toys.gemm_rowwise(device, M=16, K=64, N=64, row_tile=16)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm)
    recording = toys.gemm_rowwise_recording("below-minimum", gemm, norm)
    analysis = analyze(region, recording, device)
    (edge,) = region.edges
    produced, consumed = 16 * 64, 64
    least = produced + consumed - math.gcd(produced, consumed)
    assert analysis.min_depth[edge] * produced == least
    for depth, fits in ((analysis.min_depth[edge], True), (0, False)):
        profile = Profile()
        profile.add_entry(Entry(root=toys.gemm_rowwise_region(gemm, norm, depth=depth)))
        result = fit(profile, [Timed(recording)], device)
        assert result.ok is fits, result.why
        if not fits:
            assert result.stage == "analysis"
            assert "deadlock" in result.why


@pytest.mark.extensive
@pytest.mark.parametrize("device", _GEMM_BESIDE, indirect=True)
@pytest.mark.supported_devices("npu1", "npu2")
def test_tuner_picks_token_sizes_that_pay(device):
    """``search``, run on the multi-rate toy alone, keeps a depth at or past the analysis's minimum and passes ``check`` against the start, exact.

    An edge with no chosen depth builds at the analysis's minimum.
    """
    gemm, norm = toys.gemm_rowwise(device, M=48, row_tile=16)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("searched-rates", gemm, norm)
    calls = [Timed(recording)]
    tuned = search(calls, profile, device)
    verdict = check(tuned, profile, calls, device, Refinement.EXACT)
    assert verdict.ok, verdict.why
    tuned_entry = tuned.entries()[0]
    tuned_edge = tuned_entry.root.edges[0]
    analysis = analyze(tuned_entry.root, recording, device)
    least = analysis.min_depth[tuned_edge]
    assert (least if tuned_edge.depth is None else tuned_edge.depth) >= least


def _skip_into_larger_objects(depth: int) -> tuple[Recording, Region]:
    """Return the skip toy, its GEMV's two-element objects delivered to the second add 256 at a time, that edge ``depth`` deep."""
    recording, members, _ = toys_edges.skip_add_gemv_add()
    return recording, Region(
        members,
        (
            Edge(0, "y", 1, "B"),
            Edge(1, "C", 2, "a", depth=depth),
            toys_edges.skip_add_gemv_add_edge(depth=4),
        ),
    )


def _delivered(device, reader: str, depth: int | None):
    """Compose the delivered stream ``reader`` names at ``depth`` as the build does; return the region and its producer's output operand."""
    if reader == "smaller":
        gemm, norm = toys.gemm_rowwise(device, M=16, row_tile=16)
        recording = toys.gemm_rowwise_recording("delivered-depth", gemm, norm)
        region = toys.gemm_rowwise_region(gemm, norm, depth=depth)
        step = 0
    else:
        recording, region = _skip_into_larger_objects(depth)
        step = 1
    profile = Profile()
    profile.add_entry(Entry(root=region))
    assert fit(profile, [Timed(recording)], device).ok
    _, (fusion,) = composed(recording, profile)
    designs = [
        OperatorDesign(recording.steps[s].op.resolved(device)) for s in fusion.steps
    ]
    _, arrays = fused_configuration("delivered", fusion, designs)
    (made,) = [b for b in arrays[fusion.steps.index(step)].op.buffers if b.name == "C"]
    assert made.delivers is not None
    return made


def test_balance_is_held_at_three_of_every_residue_of_the_bounds_period(device):
    """``BoundedRows`` over 1024 rows: fit analyses three values of each of ``n``'s 64 classes.

    What a call moves repeats every 64 of ``n`` (a block of 16-row tiles,
    one a core row, four rows). The first 64 values, 64 from the middle and the last 64: a count the
    two ends move differs on each class by a polynomial of degree two at
    most, so three roots make it zero on every admitted value. The region
    is refused at the first unbalanced one.
    """
    recording = toys.BoundedRows(tile_m=16).record(a=(1024, 64), b=(64, 64))
    region = Region(
        tuple(
            Member(cls=type(s.op), dims=Profile.dims(type(s.op), vars(s.op)))
            for s in recording.steps
        ),
        (Edge(0, "C", 1, "x"),),
    )
    points = _balanced_at(
        Derivation(region, recording, device), recording, "n", 0, 1024
    )
    assert points == [*range(64), *range(512, 576), *range(961, 1025)]
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert "at n = 1," in result.why


@pytest.mark.parametrize(
    ("device", "reader"),
    [
        pytest.param(name, reader, id=f"device_{name}-reader_{reader}")
        for name in sorted(DEVICES)
        for reader in ("smaller", "larger")
    ],
    indirect=["device"],
)
def test_a_delivered_streams_chosen_depth_counts_its_producers_objects(reader, device):
    """A stream whose ends take objects of other sizes, at a chosen depth: its producer's end that many of its own objects deep.

    As the analysis and fit count it. GEMM's 16-row tile delivered a row at a time to a norm (its reader's
    objects smaller), and GEMV's two-element objects delivered 256 at a time
    to an add (its reader's larger). Its reader's end keeps the depth it has
    with no depth chosen.
    """
    made = _delivered(device, reader, 3)
    own = _delivered(device, reader, None)
    assert [f.depth for f in made.lane_fifos] == [3] * made.lanes
    assert [h.depth for h in made.lane_handles] == [h.depth for h in own.lane_handles]
