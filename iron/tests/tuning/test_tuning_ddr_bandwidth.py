# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""DDR bandwidth: the device's read ceiling, each weight-bound toy's share of it, and a phased call's period at the device's host streams."""

from __future__ import annotations

import dataclasses
from fractions import Fraction

import pytest

from iron.common.declare.composition import Hold
from iron.common.graph.sdf import Ceiling, analyze
from iron.common.testing import run_test, vectors
from iron.tests.support import toys_dataflow as toys
from iron.tune.ddr import read_gemv

# A ceiling shaped as npu2's (Strix Halo) measures: flat to eight streams,
# shared past them, small objects moving faster.
CEILING = Ceiling(
    core_mhz=1800.0,
    mixed={2: 4.0, 8: 4.0, 16: 3.0},
    mixed_object=8192,
    objects={256: 4.4, 8192: 4.0, 32768: 4.0},
    read={1: 7.3},
    boundary=3600.0,
)

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


def _through_host(size: int, edges: int):
    """Return ``add -> SiLU -> mul`` on two columns with its first ``edges`` edges through host memory, a phase boundary each, and its recording."""
    add, silu, mul = toys.add_silu_mul(size=size, tile=128, cols=2)
    region = toys.add_silu_mul_region(add, silu, mul)
    for index in range(edges):
        region = region.held(index, Hold.DDR)
    return region, toys.add_silu_mul_recording(f"through_host_{edges}", add, silu, mul)


def test_a_phased_period_waits_on_the_measurement_it_lacks(device):
    """Without the device's measured rates, or with them but no phase boundary, a phased call's period names the measurement it waits on."""
    region, recording = _through_host(1 << 12, 1)
    with pytest.raises(NotImplementedError, match="measured DDR rates"):
        analyze(region, recording, device).period
    unbounded = dataclasses.replace(CEILING, boundary=None)
    with pytest.raises(NotImplementedError, match="measured phase boundary"):
        analyze(region, recording, device, ceiling=unbounded).period


# npu1's waits on host 203.
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("edges", [1, 2])
def test_each_boundary_adds_its_measured_cost_to_the_phased_period(edges, device):
    """A chain with one or two edges through host memory runs two or three phases: each boundary between them adds the ceiling's ``boundary``."""
    region, recording = _through_host(1 << 17, edges)
    free = dataclasses.replace(CEILING, boundary=0.0)
    paid = analyze(region, recording, device, ceiling=CEILING).period
    assert paid - analyze(region, recording, device, ceiling=free).period == (
        edges * Fraction(CEILING.boundary)
    )


# npu2's: its kernels are traced on it.
@pytest.mark.supported_devices("npu2")
def test_host_streams_move_their_fifos_objects_at_the_objects_curves_rate(device):
    """Each host fill and drain moves its fifo's 256-byte objects; at a ceiling where those move faster than ``mixed``'s, the phased period is shorter."""
    region, recording = _through_host(1 << 17, 1)
    analysis = analyze(region, recording, device, ceiling=CEILING)
    assert set(analysis.transfers.values()) == {128 * 2}
    flat = dataclasses.replace(CEILING, objects={CEILING.mixed_object: 4.0})
    assert analysis.period < analyze(region, recording, device, ceiling=flat).period
