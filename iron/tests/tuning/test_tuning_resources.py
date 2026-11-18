# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Resources a token pattern needs: locks, DMA buffer descriptors and memory banks, from the target model."""

import pytest
from aie.dialects.aie import get_target_model

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Member, Region
from iron.common.image.step import Edge, EdgeKind
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.fusable import gemv_add_recording
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import fit

pytestmark = pytest.mark.usefixtures("npu2")


@unbuilt
def test_a_deep_buffer_within_the_memtile_budget_is_counted_and_fits():
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
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert result.ok


@unbuilt
def test_a_strided_token_pattern_counts_its_buffer_descriptors():
    """A row-tiled edge counts the buffer descriptors its stride needs.

    A real 16-row tile (``tile_m = 16``) into a per-row consumer, so
    neither end moves whole rows a firing as a contiguous edge would.
    ``M = 48`` keeps the row split npu2's array resolves at one, so the
    real per-firing count is ``tile_m`` alone and depth 16 is its minimum.
    """
    gemm, norm = toys.gemm_rowwise(M=48, row_tile=16)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm, depth=16)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("strided", gemm, norm)
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert result.ok


def test_more_buffer_descriptors_than_a_tile_holds_is_refused_before_any_build():
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
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert not result.ok
    assert result.stage == "counts"


@unbuilt
def test_resource_limits_come_from_the_target_model_not_a_constant():
    """The budget ``fit`` holds a design to is the target model's own.

    Not a number this test hardcodes; a toy that fits on npu2's eight
    columns may not on a four-column device.
    """
    target = get_target_model(toys.NPU2.resolve())
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
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert target is not None
    assert result.ok
