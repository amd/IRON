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

import aie.utils as aie_utils
from aie.iron.device import from_name

import iron
from iron.common.declare import Carried, Scratchpad
from iron.common.graph.carried import Parameter, attach_emit, compose
from iron.operators.emit import reference as emit_reference
from iron.operators.strided_copy import StridedCopy

N = 64
STEPS = 3 * N


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


def _element(buffer_in, buffer_out, **value):
    """An int32 copy of one element, at the per-call offset ``value`` names."""
    copy = StridedCopy(
        input_sizes=(1,),
        input_strides=(1,),
        input_offset=0,
        output_sizes=(1,),
        output_strides=(1,),
        output_offset=0,
        input_buffer_size=buffer_in,
        output_buffer_size=buffer_out,
        dtype=np.int32,
        num_aie_channels=1,
    )
    (name,) = value
    copy.use_value(name)
    return copy


def _walk(successor):
    """The graph, and the state it records the walk in."""
    trail = iron.state((STEPS + 1,), np.int32, name="trail")
    gather = _element(N, 1, in_offset=True)
    record = _element(1, STEPS + 1, out_offset=True)

    @iron.graph
    def walk(
        jump=None,
        *,
        node: Carried[np.int32],
        steps: Carried[np.int32],
        skip: Scratchpad[np.int32],
    ):
        if jump is None:
            nxt = gather(successor, in_offset=node)
        else:
            nxt = gather(jump, in_offset=skip)
        record(nxt, trail, out_offset=steps)
        return iron.carry(node=nxt, steps=steps + 1)

    return walk, trail


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
    walk, trail = _walk(successor)
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
        got = body.read(trail)
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
    assert body.read(trail)[7] == successor[want[-1]]


def test_the_emit_program_follows_the_target_parameters():
    """Each word of the target's scratchpad comes from a carried value, in
    the target's order and encoding; anything else is refused."""
    walk, _ = _walk(np.arange(N, dtype=np.int32))
    traced = walk.trace()
    assert traced.feedback == []  # tracing alone adds no Emit
    site = attach_emit(traced, walk.carried, walk._carry, slots=2)
    # The gathered node is computed into the carry's second plane.
    assert traced.runlist[0][-1] == "carry[8:12]"
    assert traced.runlist[-1][1:] == (
        "emit_program",
        "carry",
        "emit_image",
        "carry[0:8]",
    )
    assert traced.feedback == ["emit_image"] and traced.output_args == []

    symbols = [(b.expression, b.symbol) for b in traced.bindings]
    # A target laying the two out the other way, one as a core read.
    parameters = [
        Parameter(symbols[1][1], 0, "core"),
        Parameter(symbols[0][1], 1, "addr"),
    ]
    program = compose(site, traced.carry, symbols, parameters)
    assert program.tolist() == [
        [0, 1, 1, 1, 2],  # steps + 1, shifted for the core
        [1, 0, 1, 0, 0],  # the node the device gathered
        [1, 0, 1, 0, 0],  # the next node
        [0, 1, 1, 1, 0],  # the next step count
    ]
    image, state = emit_reference(program, np.array([[5, 9], [33, 0]]), slots=2)
    assert image.tolist() == [10 << 2, 33] and state.tolist() == [33, 10]

    with pytest.raises(ValueError, match="takes 1"):
        compose(site, traced.carry, symbols, parameters[:1])
    first = walk.trace(jump=((N,), np.int32))
    jumped = [(b.expression, b.symbol) for b in first.bindings]
    with pytest.raises(ValueError, match="skip, which is not carried"):
        compose(
            site,
            traced.carry,
            jumped,
            [Parameter(symbol, k, "addr") for k, (_, symbol) in enumerate(jumped)],
        )
