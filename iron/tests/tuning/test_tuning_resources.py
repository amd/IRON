# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Resources a token pattern needs: locks, DMA buffer descriptors and memory banks, from the target model."""

import pytest
from aie.dialects.aie import get_target_model

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Member, Refinement, Region
from iron.common.graph.record import Recording
from iron.common.image.step import Edge, EdgeKind
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU
from iron.tests.support import sequences
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.fusable import gemv_add_recording
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import member
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import check, fit

pytestmark = pytest.mark.usefixtures("device")

# Where GEMM composes beside another operator on the device: npu1's runs wait to
# be checked on an npu1 host (they compile and fit here).
_GEMM_BESIDE = [
    pytest.param(name, id=f"device_{name}", marks=() if name == "npu2" else unbuilt)
    for name in sorted(DEVICES)
]


def test_a_deep_buffer_within_the_memtile_budget_is_counted_and_fits(device):
    """A staged edge held a few objects deep, well inside the memtile banks the target model reports: ``fit`` counts it and does not refuse it."""
    gemv = GEMV(M=256, K=256, tile_size_input=4, tile_size_output=256)
    add = ElementwiseAdd(size=256, tile_size=256)
    region = Region(
        parts=(
            Member(cls=GEMV, dims={"M": gemv.M, "K": gemv.K}),
            Member(cls=ElementwiseAdd, dims={"size": add.size}),
        ),
        edges=(Edge(0, "C", 1, "b", kind=EdgeKind.STAGED, depth=4),),
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = gemv_add_recording("fits", gemv, add)
    result = fit(profile, [Timed(recording)], device)
    assert result.ok


def test_a_staged_edge_counts_the_rounds_its_memtile_pools(device):
    """GEMV's two-element objects into an add's 256-element tile, held a call's 128 objects deep, fit.

    The memtile pools the add's 256-element rounds, a buffer descriptor
    each, not the GEMV's objects: 128 of them are one round, well inside a
    memtile's descriptors.
    """
    gemv = GEMV(M=256, K=256, num_aie_columns=1)
    add = ElementwiseAdd(size=256, tile_size=256)
    region = Region(
        parts=(
            Member(cls=GEMV, dims={"M": gemv.M, "K": gemv.K}),
            Member(cls=ElementwiseAdd, dims={"size": add.size}),
        ),
        edges=(Edge(0, "C", 1, "b", kind=EdgeKind.STAGED, depth=128),),
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = gemv_add_recording("rounds", gemv, add)
    result = fit(profile, [Timed(recording)], device)
    assert result.ok, result.why


def test_a_strided_token_pattern_counts_its_buffer_descriptors(device):
    """A row-tiled edge counts the buffer descriptors its stride needs, with the rest of its core's.

    A real 16-row tile (``tile_m = 16``) into a per-row consumer, so
    neither end moves whole rows a firing as a contiguous edge would.
    ``M = 48`` keeps the row split each device's array resolves at one, so the
    real per-firing count is ``tile_m`` alone. At depth 16 the norm's core
    holds a whole tile, a row an object and a buffer descriptor each, read
    from GEMM's memtile, and drains its own rows past them: past a core
    tile's descriptors, refused before any build.
    """
    gemm, norm = toys.gemm_rowwise(device, M=48, row_tile=16)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm, depth=16)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("strided", gemm, norm)
    result = fit(profile, [Timed(recording)], device)
    target = get_target_model(device.resolve())
    assert target is not None
    core_row = next(r for r in range(target.rows()) if target.is_core_tile(0, r))
    assert not result.ok
    assert result.stage == "counts"
    assert "step 1 (RMSNorm)'s core 0 moves" in result.why
    assert f"a core tile has {target.get_num_bds(0, core_row)}" in result.why


@pytest.mark.parametrize("device", _GEMM_BESIDE, indirect=True)
@pytest.mark.supported_devices("npu1", "npu2")
def test_a_core_using_every_buffer_descriptor_is_bit_identical(device):
    """The strided edge at the deepest its norm's core holds fits, and one object deeper is refused at the counts.

    The count is the placer's own: at the deepest depth ``fit`` takes, the
    norm's core uses every buffer descriptor a core tile has, and the fused
    build runs bit-identical to the steps apart.
    """
    target = get_target_model(device.resolve())
    assert target is not None
    core_row = next(r for r in range(target.rows()) if target.is_core_tile(0, r))
    bds = target.get_num_bds(0, core_row)
    gemm, norm = toys.gemm_rowwise(device, M=48, row_tile=16)
    recording = toys.gemm_rowwise_recording("every-descriptor", gemm, norm)
    profiles = {}
    for depth in range(bds, 0, -1):
        profiles[depth] = Profile()
        profiles[depth].add_entry(
            Entry(root=toys.gemm_rowwise_region(gemm, norm, depth=depth))
        )
        if fit(profiles[depth], [Timed(recording)], device).ok:
            break
    refused = fit(profiles[depth + 1], [Timed(recording)], device)
    assert not refused.ok
    assert refused.stage == "counts"
    assert f"moves {bds + 1} objects by DMA" in refused.why
    result = check(
        profiles[depth], Profile(), [Timed(recording)], device, Refinement.EXACT
    )
    assert result.ok, result.why


@pytest.mark.parametrize("columns", [(2, 1), (1, 2)], ids=["join", "split"])
def test_a_staged_round_past_one_buffer_descriptor_fits_as_a_descriptor_chain(
    columns, device
):
    """Two columns' contiguous halves restaged to or from one column: the only round in the lanes' order is the whole call.

    At ``1 << 18`` bfloat16 a memtile holds that round, but one buffer
    descriptor moves less than all of it. A join reads each half into the
    memtile as a descriptor of its own; a split takes the whole round in as
    one object, which the memtile moves as a chain of descriptors under one
    lock. Both fit, the placer's verdict included.
    """
    size = 1 << 18
    first = SiLU(size=size, tile_size=128, num_aie_columns=columns[0])
    second = SiLU(size=size, tile_size=128, num_aie_columns=columns[1])
    recording = Recording.of_steps(
        "past-a-descriptor",
        sequences.steps((first, "x", "h"), (second, "h", "y")),
        ["x"],
        ["y"],
    )
    region = Region(
        parts=(member(first), member(second)),
        edges=(Edge(0, "y", 1, "x", kind=EdgeKind.STAGED),),
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], device)
    assert result.ok, result.why


def test_more_buffer_descriptors_than_a_tile_holds_is_refused_before_any_build(device):
    """A buffer descriptor count past the target model's per-tile limit.

    An implausibly deep, implausibly strided edge: refused by ``fit`` at
    stage ``"counts"``, before any build.
    """
    gemv = GEMV(M=2048, K=2048, tile_size_input=4, tile_size_output=256)
    add = ElementwiseAdd(size=2048, tile_size=256)
    region = Region(
        parts=(
            Member(cls=GEMV, dims={"M": gemv.M, "K": gemv.K}),
            Member(cls=ElementwiseAdd, dims={"size": add.size}),
        ),
        edges=(Edge(0, "C", 1, "b", kind=EdgeKind.STAGED, depth=1 << 16),),
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = gemv_add_recording("too-many-bds", gemv, add)
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"


def test_resource_limits_come_from_the_target_model_not_a_constant(device):
    """The budget ``fit`` holds a design to is the target model's own.

    Not a number this test hardcodes; a toy that fits on npu2's eight
    columns may not on a four-column device.
    """
    target = get_target_model(device.resolve())
    gemv = GEMV(M=256, K=256, tile_size_input=4, tile_size_output=256)
    add = ElementwiseAdd(size=256, tile_size=256)
    region = Region(
        parts=(
            Member(cls=GEMV, dims={"M": gemv.M, "K": gemv.K}),
            Member(cls=ElementwiseAdd, dims={"size": add.size}),
        ),
        edges=(Edge(0, "C", 1, "b", kind=EdgeKind.STAGED, depth=4),),
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = gemv_add_recording("model-derived", gemv, add)
    result = fit(profile, [Timed(recording)], device)
    assert target is not None
    assert result.ok
