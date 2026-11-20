# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""DDR bandwidth: the device's read ceiling, each weight-bound toy's share of it, and a phased call's period, which waits on the device's measured rates."""

from __future__ import annotations

import dataclasses

import aie.utils as aie_utils
import pytest

from iron.common.declare.composition import Hold
from iron.common.graph.sdf import analyze
from iron.common.testing import run_test, vectors
from iron.tests.support import toys_dataflow as toys
from iron.tune.costmodel import CostModel
from iron.tune.ddr import Ceiling, read_gemv
from iron.tune.measure import platform

# (columns, channels) requested per nominal stream count; ``read_gemv`` takes
# the widest the device's shim DMAs admit, so the achieved count (read back
# off the resolved operator) is what is recorded against, never the request.
_REQUESTED = {1: (1, 1), 2: (2, 1), 4: (4, 1), 8: (8, 1), 16: (8, 2)}


def _timed(op) -> dict[str, float]:
    """Run ``op`` checked against its reference, then timed; return what the timing records."""
    timed: dict[str, float] = {}
    errors = run_test(
        op, vectors(op), tolerance=op.tolerance(), record=timed.__setitem__
    )
    assert not errors, {name: verdict.detail for name, verdict in errors.items()}
    return timed


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("nominal_streams", sorted(_REQUESTED))
def test_ddr_read_ceiling_against_stream_count(
    nominal_streams, record_property, device
):
    """The ceiling: a large weight-bound GEMV's achieved read bandwidth at each stream count the device supports."""
    columns, channels = _REQUESTED[nominal_streams]
    op = read_gemv(8192 // nominal_streams, columns, channels, device)
    record_property("Requested streams", nominal_streams)
    record_property("Achieved streams", op.num_aie_columns * op.num_channels)
    for name, value in _timed(op).items():
        record_property(name, value)


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("nominal_streams", [1, 4, 8])
def test_weight_bound_toy_reports_its_share_of_the_ceiling(
    nominal_streams, record_property, device
):
    """A smaller weight-bound GEMV, at the same stream count as a ceiling row, records its bandwidth as a fraction of that row's.

    The ceiling row runs first in this test (not shared across tests, so each
    is self-contained and free of ordering assumptions), then the toy; the
    ratio is recorded, never asserted, since it is a finding to attribute
    (IRON's access pattern, mlir-aie's defaults, or the hardware).
    """
    columns, channels = _REQUESTED[nominal_streams]
    ceiling = _timed(read_gemv(8192 // nominal_streams, columns, channels, device))
    toy = _timed(read_gemv(2048 // nominal_streams, columns, channels, device))
    record_property("Ceiling bandwidth GB/s", ceiling["Bandwidth"])
    record_property("Toy bandwidth GB/s", toy["Bandwidth"])
    record_property("Toy share of ceiling", toy["Bandwidth"] / ceiling["Bandwidth"])


def test_a_phased_period_waits_on_the_devices_measured_rates(device):
    """``add -> SiLU -> mul`` with an edge through host memory runs in two phases: without the device's DDR rates, its period names what it waits on."""
    add, silu, mul = toys.add_silu_mul(size=1 << 12, tile=128, cols=2)
    region = toys.add_silu_mul_region(add, silu, mul).held(0, Hold.DDR)
    recording = toys.add_silu_mul_recording("through_host", add, silu, mul)
    with pytest.raises(NotImplementedError, match="measured DDR rates"):
        analyze(region, recording, device).period


# npu2's: the part, power mode and clock are the attached NPU's.
@pytest.mark.supported_devices("npu2")
def test_a_stored_ceiling_is_read_only_on_the_part_and_clock_it_was_measured_on(
    tmp_path, device
):
    """Rates kept for the attached part in its power mode, at its core clock, are read; another part's, or at another clock, are not measured here."""
    report = platform()
    part, mode = report["Name"], report["Power Mode"]
    here = Ceiling(
        float(aie_utils.DefaultNPURuntime.core_mhz), {2: 4.0}, {256: 4.2}, {1: 7.3}
    )
    elsewhere = dataclasses.replace(here, core_mhz=here.core_mhz / 2)
    for kept, read in (
        ({part: {mode: here.as_json()}}, here),
        ({"NPU Elsewhere": {mode: here.as_json()}}, None),
        ({part: {mode: elsewhere.as_json()}}, None),
    ):
        CostModel(ddr=kept).save(device.name, tmp_path)
        assert Ceiling.stored(device.name, tmp_path) == read
