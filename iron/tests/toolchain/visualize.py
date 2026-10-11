# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A floorplan reads the built image: on each device, a step's tiles are
the cores its tunables ask for and a host stream per operand per core, and
every routed link joins neighbouring tiles or leaves a shim for the host.
"""

import iron
from iron.common.graph.visualize import Floorplan
from iron.operators import ElementwiseAdd, SiLU
from iron.tests.toolchain.tools import requires

pytestmark = requires("aiebu", "xclbinutil", "peano")

N = 4096


class TwoSteps(iron.Graph):
    def body(self, a, b):
        return SiLU(ElementwiseAdd(a, b))


def test_a_floorplan_holds_the_cores_and_streams_the_step_asks_for(device):
    version = TwoSteps().compile(a=(N,), b=(N,))
    assert len(version.traced.steps) == 2
    for i, step in enumerate(version.traced.steps):
        op = step.op.resolved()
        plan = Floorplan(version, i)
        lanes = op.num_aie_columns * op.num_channels
        assert len(plan.cores) == lanes
        assert sum(plan.shims.values()) == len(op.buffers) * lanes
        assert all(col < device.cols for col, _ in plan.tiles)
        for (a, b), count in plan.links.items():
            assert count > 0
            assert abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1, (a, b)
            assert b in plan.tiles or (a[1] == 0 and b[1] == -1), (a, b)
        svg = plan.svg(columns=device.cols)
        assert svg.count("<title>tile (") == device.cols * (
            1 + max(r for _, r in plan.tiles)
        )
