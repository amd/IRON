# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pictures of a built image. A floorplan reads it: on each device, a
step's tiles are the cores its tunables ask for and a host stream per
operand per core, and every routed link joins neighbouring tiles or leaves
a shim for the host. An arena draws each scratch buffer over the steps
that touch it, at the offset the image placed it.
"""

import re

import iron
from iron.common.graph import CompiledGraph
from iron.common.graph.visualize import ArenaPicture, Floorplan
from iron.common.image.allocator import LiveRange
from iron.operators import ElementwiseAdd, SiLU
from iron.tests.toolchain.tools import requires
from iron.tune.narrowing import JointTuning, cost_key

pytestmark = requires("aiebu", "xclbinutil", "peano")

N = 4096


class TwoSteps(iron.Graph):
    def body(self, a, b):
        return SiLU.step(ElementwiseAdd.step(a, b))


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


def test_an_arena_draws_each_scratch_buffer_where_and_while_it_lives(device):
    version = TwoSteps().compile(a=(N,), b=(N,))
    plan = ArenaPicture(version)
    [between] = [h.name for h in version.traced.steps[0].outputs]
    assert set(plan.boxes) == {between}
    assert plan.ranges[between] == LiveRange(0, 1)
    _, offset, size = version.sequence.layout[between]
    assert plan.boxes[between] == (offset, size) and size == 2 * N
    assert (
        f"<title>{between}: {size} bytes at {offset}, steps 0 to 1</title>"
        in plan.svg()
    )


def test_a_chain_tuned_with_array_mates_draws_no_shared_device(npu1):
    built = TwoSteps().compile(a=(N,), b=(N,))
    keys = [cost_key(s.op) for s in built.traced.steps]
    # The tuner lists a chain's array mates as one device, as it does a pack's.
    tuning = JointTuning(
        chosen={},
        groups=(),
        devices=(tuple(keys),),
        configures=2,
        predicted_us=1.0,
        baseline_configures=2,
        baseline_us=1.0,
        unmeasured=(),
    )
    version = CompiledGraph(built.traced, built.plan, tuning=tuning)
    assert not version.plan.full_elf
    dot = version.dot()
    assert "one device" not in dot
    assert {"s0", "s1"} <= set(re.findall(r'^\s*"(s\d+)" \[', dot, re.M))
