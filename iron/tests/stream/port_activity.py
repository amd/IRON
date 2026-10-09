#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A generated design records stream's estimate of it: cycles, and per group its latency and
port activity."""

import json
from types import SimpleNamespace

from iron.common.stream.runner import (
    ESTIMATE,
    PORT_REPORT,
    solve_options,
    write_estimate,
)

ROW = {
    "kind": "memory_port",
    "resource": "dma.s2mm",
    "core_ids": [2],
    "utilization": 0.9,
}
LATENCY = {"total": 100, "per_iteration": 40, "overlap_between_iterations": 20}


def test_the_estimate_keeps_the_cycles_and_each_groups_latency_and_rows(tmp_path):
    performance = {"latency": LATENCY, "memory_ports": [ROW]}
    estimate = SimpleNamespace(
        cycles=300.0,
        group_cycles=(100.0, 150.0),
        dispatch_cycles=50.0,
        context={"group_allocations": {1: None, 0: {"performance": performance}}},
    )
    write_estimate(str(tmp_path), estimate)
    assert json.loads((tmp_path / ESTIMATE).read_text()) == {
        "cycles": 300.0,
        "group_cycles": [100.0, 150.0],
        "dispatch_cycles": 50.0,
        "groups": {
            "group_0": {"latency": LATENCY, "port_activity": [ROW]},
            "group_1": {"latency": None, "port_activity": []},
        },
    }


def test_every_solve_asks_for_the_port_report(monkeypatch):
    from iron.common.stream import runner

    monkeypatch.setattr(runner, "array", lambda: SimpleNamespace(num_columns=8))
    monkeypatch.setattr(runner, "load_library", lambda: None)
    families = solve_options("npu2").families
    assert families.count(PORT_REPORT) == 1
    assert "memory_ports" not in families
    assert {
        "overlap": {"transfer_contention": False, "offchip_contention": False}
    } in families
