# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Each edge end's token size and element order, row vs column tiles."""

import dataclasses

import pytest
from aie.dialects.aie import get_target_model

from iron import Precision
from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Member, Region
from iron.common.graph.record import Recording
from iron.common.graph.sdf import analyze
from iron.common.image.step import Edge, EdgeKind, HandOff
from iron.operators.gemm import GEMM
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import toys_dataflow as toys
from iron.tests.support import toys_edges
from iron.tests.support.tools import DEVICES
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import fit

pytestmark = pytest.mark.usefixtures("device")


def _gemm_into_rows(b_col_maj: bool, kind: EdgeKind) -> tuple[Region, GEMM, RMSNorm]:
    gemm = GEMM(
        M=64,
        K=64,
        N=64,
        precision=Precision.MEDIUM,
        b_col_maj=b_col_maj,
        num_aie_columns=1,
    )
    norm = RMSNorm(rows=64, tile_size=64, num_aie_columns=1)
    region = Region(
        parts=(
            Member(
                cls=GEMM,
                dims={"M": gemm.M, "K": gemm.K, "N": gemm.N, "b_col_maj": b_col_maj},
            ),
            Member(cls=RMSNorm, dims={"rows": norm.rows}),
        ),
        edges=(Edge(0, "C", 1, "x", kind=kind),),
    )
    return region, gemm, norm


@unbuilt
def test_row_tiles_into_a_rowwise_consumer_fit_as_is(device):
    """``GEMM``'s row-major ``C`` (one tile a row) feeding ``RMSNorm`` directly: the analysis derives ``HandOff.EQUAL``, no restage, and it fits."""
    region, gemm, norm = _gemm_into_rows(b_col_maj=False, kind=EdgeKind.STREAM)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("rows", gemm, norm)
    result = fit(profile, [Timed(recording)], device)
    assert result.ok
    analysis = analyze(region, recording, device)
    assert analysis.hand_off[region.edges[0]] == HandOff.EQUAL


def _tiles_into_rows(kind: EdgeKind) -> tuple[Recording, Region]:
    recording, region = toys_edges.layout_transpose()
    (edge,) = region.edges
    return recording, dataclasses.replace(
        region, edges=(dataclasses.replace(edge, kind=kind),)
    )


# Where the tiles' restage fits. npu1 builds GEMM on an array narrower than the
# device, which a configuration beside another operator's does not take.
_LAYOUT_FITS = [
    pytest.param(name, id=f"device_{name}", marks=() if name == "npu2" else unbuilt)
    for name in sorted(DEVICES)
]


@pytest.mark.parametrize("device", _LAYOUT_FITS, indirect=True)
def test_column_tiles_into_a_rowwise_consumer_are_restaged_by_layout(device):
    """``GEMM``'s 32x32 ``C`` tiles feeding ``RMSNorm``, which reads whole rows, over a staged edge.

    A tile narrower than a row is restaged through the memtile the staged
    edge allows, the analysis deriving ``HandOff.LAYOUT``, and it fits.
    """
    recording, region = _tiles_into_rows(EdgeKind.STAGED)
    analysis = analyze(region, recording, device)
    assert analysis.hand_off[region.edges[0]] == HandOff.LAYOUT
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], device)
    assert result.ok, result.why


def test_column_tiles_with_no_restage_are_refused(device):
    """The same tiles into ``RMSNorm``, over a plain stream edge.

    A stream edge's lanes meet as they are, core to core, with no memtile
    to restage through: the analysis derives the layout hand-off, so
    ``fit`` refuses it at stage ``"analysis"``, before any build, not
    silently transposed.
    """
    recording, region = _tiles_into_rows(EdgeKind.STREAM)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "layout" in (result.why or "")


@unbuilt
def test_32_row_tiles_into_64_row_tiles_balance_at_their_lcm(device):
    """A 32-row GEMM tile feeding a 64-row GEMM tile.

    At ``M = 256`` both GEMMs resolve every core row of a column (four,
    on npu1 and npu2), so each
    firing really moves 128 and 256 rows; the edge's rate is ``128 : 256``
    rows a firing, no restage needed since 256 is a whole number of 128s,
    and it fits.
    """
    producer, consumer = toys.gemm_into_gemm(
        device, M=256, width=64, producer_tile=32, consumer_tile=64
    )
    model = get_target_model(device.resolve())
    rows = sum(model.is_core_tile(0, row) for row in range(model.rows()))
    assert producer.n_aie_rows == rows
    assert consumer.n_aie_rows == rows
    region = toys.gemm_into_gemm_region(producer, consumer)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_into_gemm_recording("32-64", producer, consumer)
    result = fit(profile, [Timed(recording)], device)
    assert result.ok
    analysis = analyze(region, recording, device)
    assert analysis.repetition == {0: 2, 1: 1}
