# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Each edge end's token size and element order, row vs column tiles."""

import pytest

from iron import Precision
from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Member, Region
from iron.common.graph.sdf import analyze
from iron.common.image.step import Edge, EdgeKind, HandOff
from iron.operators.gemm import GEMM
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import fit

pytestmark = pytest.mark.usefixtures("npu2")


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
def test_row_tiles_into_a_rowwise_consumer_fit_as_is():
    """``GEMM``'s row-major ``C`` (one tile a row) feeding ``RMSNorm`` directly: the analysis derives ``HandOff.EQUAL``, no restage, and it fits."""
    region, gemm, norm = _gemm_into_rows(b_col_maj=False, kind=EdgeKind.STREAM)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("rows", gemm, norm)
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert result.ok
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.hand_off[region.edges[0]] == HandOff.EQUAL


@unbuilt
def test_column_tiles_into_a_rowwise_consumer_are_restaged_by_layout():
    """``GEMM``'s column-major ``C`` feeding ``RMSNorm``, which reads rows, over a staged edge.

    The mismatched order is restaged through the memtile the staged edge
    allows, the analysis deriving ``HandOff.LAYOUT``, and it fits.
    """
    region, gemm, norm = _gemm_into_rows(b_col_maj=True, kind=EdgeKind.STAGED)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("cols", gemm, norm)
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert result.ok
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.hand_off[region.edges[0]] == HandOff.LAYOUT


@unbuilt
def test_column_tiles_with_no_restage_are_refused():
    """The same column-major ``C`` into ``RMSNorm``, over a plain stream edge.

    A stream edge's lanes meet directly, core to core, with no memtile
    to restage through: refused by ``fit`` at stage ``"counts"``, before
    any build, not silently transposed.
    """
    region, gemm, norm = _gemm_into_rows(b_col_maj=True, kind=EdgeKind.STREAM)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("cols-refused", gemm, norm)
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert not result.ok
    assert result.stage == "counts"


@unbuilt
def test_32_row_tiles_into_64_row_tiles_balance_at_their_lcm():
    """A 32-row GEMM tile feeding a 64-row GEMM tile.

    At ``M = 256`` both GEMMs resolve npu2's four core rows, so each
    firing really moves 128 and 256 rows; the edge's rate is ``128 : 256``
    rows a firing, no restage needed since 256 is a whole number of 128s,
    and it fits.
    """
    producer, consumer = toys.gemm_into_gemm(
        M=256, width=64, producer_tile=32, consumer_tile=64
    )
    assert producer.n_aie_rows == 4
    assert consumer.n_aie_rows == 4
    region = toys.gemm_into_gemm_region(producer, consumer)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_into_gemm_recording("32-64", producer, consumer)
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert result.ok
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.repetition == {0: 2, 1: 1}
