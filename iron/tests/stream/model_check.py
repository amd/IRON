#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the model check compares: stream's estimate of a run against the measured
latency, and the bits stream priced through a memory tile against the traced ones."""

import pytest

from iron.common.stream.model_check import (
    AIE_CLOCK_HZ,
    DMA_BITS_PER_CYCLE,
    TRACE_PORTS,
    _port_rows,
    points,
    predicted_us,
)

LATENCY = {"total": 1000, "per_iteration": 400, "overlap_between_iterations": 300}
MEMTILE = 1


def _estimate(**overrides):
    view = {"latency": LATENCY, "port_activity": []} | overrides
    return {
        "group_cycles": [1000.0],
        "dispatch_cycles": 50.0,
        "groups": {"group_0": view},
    }


def test_the_estimate_is_streams_cycles_on_top_of_a_dispatch():
    record = {"estimate": _estimate() | {"cycles": 3600.0}}
    assert predicted_us(record, 10.0) == pytest.approx(3600 / AIE_CLOCK_HZ * 1e6 + 10)


def test_a_design_two_groups_share_is_traced_over_both_runs():
    """Bits per run divide the traced cycles by every run of the design, and the
    iterations a run has come from its latency without the fill."""
    row = {
        "kind": "memory_port",
        "core_ids": [MEMTILE],
        "resource": "dma.s2mm",
        "bits_per_iteration": 640,
    }
    latency = LATENCY | {"total": 1000 + 77, "fill": 77}
    record = {
        "operator": "swiglu",
        "point": {"seq_len": 256},
        "candidate": {},
        "ports": TRACE_PORTS[0],
        "estimate": _estimate(latency=latency, port_activity=[row]),
        "traced": [
            {
                "groups": [0, 1],
                "tiles": {
                    "memtile_trace for tile1,0": {
                        "busy": {"PORT_RUNNING_0": 30, "PORT_RUNNING_5": 10},
                        "span": 4000,
                    }
                },
            }
        ],
    }
    (port,) = _port_rows([record])
    iterations = 1 + (1000 - 400) / (400 - 300)
    assert port["group"] == "0+1"
    assert port["modelled_bits"] == pytest.approx(640 * iterations)
    assert port["traced_bits"] == pytest.approx(40 * DMA_BITS_PER_CYCLE / 2)


def test_a_tile_stream_reports_no_port_for_is_left_out():
    record = {
        "operator": "swiglu",
        "point": {"seq_len": 256},
        "candidate": {},
        "ports": TRACE_PORTS[0],
        "estimate": _estimate(
            latency=LATENCY | {"overlap_between_iterations": 400}, port_activity=[]
        ),
        "traced": [
            {
                "groups": [0],
                "tiles": {
                    "memtile_trace for tile1,0": {
                        "busy": {"PORT_RUNNING_0": 30},
                        "span": 4000,
                    }
                },
            }
        ],
    }
    assert list(_port_rows([record])) == []


def test_an_operator_without_a_sweep_is_refused():
    with pytest.raises(ValueError, match="no sweep"):
        points("gemm")
