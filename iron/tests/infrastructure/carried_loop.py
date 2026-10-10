#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Carried values, on a device, with no host between the steps.

The graph walks a linked list and records each node in a state at the step
count. Its first version is seeded by the host: it jumps into the list
through a table it takes as input, at a plain per-call value. Every later
step is the body version, which takes nothing from the host: its Emit writes
the next run's scratchpad from the node it gathered and the step count it
started from. A step that read a stale or misplaced word leaves the cycle or
records at the wrong index, and the trail shows where.
"""

import time

import numpy as np
import pytest

import iron
from iron.common import Carried, Scratchpad
from iron.operators.copy import Copy

N = 64
STEPS = 3 * N


class Trail(iron.Graph):
    def __init__(self, successor):
        self.successor = iron.weight(successor)
        self.trail = iron.state((STEPS + 1,), np.int32, name="trail")

    def body(
        self,
        jump=None,
        *,
        node: Carried[np.int32],
        steps: Carried[np.int32],
        skip: Scratchpad[np.int32],
    ):
        if jump is None:
            nxt = Copy(self.successor[node], dtype=np.int32)
        else:
            nxt = Copy(jump[skip], dtype=np.int32)
        Copy(nxt, self.trail[steps], dtype=np.int32)
        return iron.carry(node=nxt, steps=steps + 1)


def _expected(successor, start):
    trail = [start]
    for _ in range(STEPS):
        trail.append(successor[trail[-1]])
    return np.array(trail, dtype=np.int32)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("depth", [1, 2, 3])
def test_a_carried_loop_walks_a_linked_list_on_the_device(npu_runtime, depth):
    rng = np.random.default_rng(depth)
    successor = rng.permutation(N).astype(np.int32)
    jump = rng.permutation(N).astype(np.int32)
    walk = Trail(successor)
    body = walk.compile()
    first = walk.compile(jump=((N,), np.int32), feeds=body)
    assert body.plan.image == first.plan.image == "elf"
    assert [p.kind for p in body.parameters] == ["addr", "addr"]

    loop = iron.CarriedLoop(first, body, depth=depth)
    for skip in (5, 40):
        t0 = time.perf_counter()
        done = list(loop.run(STEPS, jump, node=0, steps=0, skip=skip))
        elapsed = time.perf_counter() - t0
        assert done == list(range(STEPS))
        got = body.read(walk.trail)
        want = _expected(successor, jump[skip])
        wrong = np.flatnonzero(got != want)
        assert not wrong.size, f"skip {skip}: first wrong step {wrong[0]}: {got[:8]}"
        # The carry holds what a next step would start from: the last node.
        planes = body.read(walk._carry)
        assert planes[0].tolist() == [want[-1], STEPS + 1], planes
        print(f"depth {depth}: {elapsed / (STEPS + 1) * 1e6:.1f} us/step")

    # The host path of the same versions still works, carry and all.
    nxt = body(node=int(want[-1]), steps=7, skip=0)
    assert dict(nxt) == {"node": successor[want[-1]], "steps": 8}
    assert body.read(walk.trail)[7] == successor[want[-1]]
