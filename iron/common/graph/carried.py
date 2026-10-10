# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Carried values computed on the device, and a loop that never asks the host.

A full-ELF version with ``Carried`` values ends in an ``Emit`` step. The
versions share one ``carry`` state, ``(2, carried)`` int32: plane 0 the values
a call started from, plane 1 the elements it computed. Emit evaluates a
program over the planes into the next call's scratchpad image and plane 0.
The program depends on the target image's slots, so it is data composed once
both images are built (``CompiledGraph.emit_to()``).
"""

from __future__ import annotations

import dataclasses
from collections import deque
from collections.abc import Iterator, Mapping
from typing import TYPE_CHECKING

import numpy as np

from ...operators.emit import ROW, Emit
from ..image.artifacts import Parameter
from .handle import Affine, Handle, State
from .trace import TracedGraph, TracedStep

if TYPE_CHECKING:
    from ..image.callable import FullELFRun
    from .compiled import CompiledGraph, Word

CARRY, PROGRAM, IMAGE = "carry", "emit_program", "emit_image"


@dataclasses.dataclass(frozen=True)
class EmitSite:
    """What a version's Emit step reads and writes."""

    carried: tuple[str, ...]  # the graph's carried values, in plane order
    carry: State  # (2, len(carried)), shared by every version
    program: State  # (slots + len(carried), ROW), this version's own
    slots: int  # the words of the scratchpad the image is written into


def attach_emit(
    traced: TracedGraph, carried: list[str], carry: State, slots: int
) -> EmitSite:
    """Append an Emit step to ``traced`` for a target of ``slots`` values,
    each computed carried element moved into plane 1 of ``carry``.
    """
    if slots < 1:
        raise ValueError(
            f"{traced.name}: the image its carried values are emitted into takes "
            f"no per-call values"
        )
    taken = {h.name for s in traced.steps for h in s.slots} | set(traced.pinned)
    clash = taken & {CARRY, PROGRAM, IMAGE}
    if clash:
        raise ValueError(f"{traced.name}: buffer names {sorted(clash)} are the Emit's")
    n = len(carried)
    planes = _resident(traced, carry)
    for j, name in enumerate(carried):
        nxt = traced.carry[name]
        if isinstance(nxt, Handle):
            if any(nxt is h for h in traced.returned):
                raise NotImplementedError(
                    f"{traced.name}: {name} is carried and returned; on a full ELF "
                    f"it is computed into the carry, so read it from the Carry"
                )
            _move(traced, nxt, planes, n + j)
    program = State((slots + n, ROW), np.int32, PROGRAM)
    image = Handle((slots,), np.int32, IMAGE, "intermediate")
    current = Handle((n,), np.int32, CARRY, "slice", planes, 0)
    inputs = [_resident(traced, program), planes]
    traced.steps.append(
        TracedStep(
            Emit(slots=slots, carried=n),
            inputs + [image, current],
            inputs,
            [image, current],
        )
    )
    traced.feedback = [IMAGE]
    return EmitSite(tuple(carried), carry, program, slots)


def _resident(traced: TracedGraph, state: State) -> Handle:
    handle = Handle(state.shape, state.dtype, state.name, "state")
    traced.states[id(state)] = (state, handle)
    traced.pinned[handle.name] = handle.nbytes
    return handle


def _move(traced: TracedGraph, handle: Handle, parent: Handle, start: int) -> None:
    """Make a computed element, and every view of it, a slice of ``parent``."""
    old = handle.name
    views = [handle] + [h for s in traced.steps for h in s.slots + s.inputs + s.outputs]
    for view in views:
        if view.parent is not None and view.parent.name == old:
            raise NotImplementedError(
                f"{traced.name}: {view!r} slices the carried element {old!r}"
            )
        if view.parent is None and view.name == old:
            view.name, view.role, view.parent, view.start = (
                parent.name,
                "slice",
                parent,
                start,
            )
    traced.outputs = [h for h in traced.outputs if h.name != parent.name]


def compose(
    site: EmitSite,
    next_values: Mapping[str, Handle | Affine],
    words: list[Word],
    parameters: list[Parameter],
) -> np.ndarray:
    """The Emit program that starts a call of the image with ``words`` and
    ``parameters``; every word of it must follow from a carried value.
    """
    plane_of = {name: j for j, name in enumerate(site.carried)}
    if len(parameters) != site.slots:
        raise ValueError(
            f"the Emit writes {site.slots} scratchpad words, and the image it "
            f"starts takes {len(parameters)}; compile with feeds= that image"
        )
    if sorted(p.index for p in parameters) != list(range(site.slots)):
        raise ValueError(f"scratchpad indices {[p.index for p in parameters]}")

    def source(name: str) -> tuple[int, int, int, int]:
        nxt = next_values[name]
        if isinstance(nxt, Handle):
            return 1, plane_of[name], 1, 0
        if nxt.value.name not in plane_of:
            raise ValueError(
                f"the next {name} is {nxt}, and {nxt.value.name} is not carried"
            )
        return 0, plane_of[nxt.value.name], nxt.scale, nxt.bias

    by_symbol = {w.symbol: w for w in words}
    program = np.zeros(site.program.shape, dtype=np.int64)
    for p in parameters:
        word = by_symbol.get(p.name)
        if word is None:
            raise ValueError(f"{p.name} is not a word the graph writes")
        form = word.form
        if form is None:
            raise ValueError(
                f"{p.name} has no Emit form (an Affine of one graph value): "
                f"the device cannot compute it"
            )
        if form.value.name not in plane_of:
            raise ValueError(
                f"{p.name} is computed from {form.value.name}, which is not carried: "
                f"the device cannot know it"
            )
        plane, index, scale, bias = source(form.value.name)
        program[p.index] = (
            plane,
            index,
            form.scale * scale,
            form.scale * bias + form.bias,
            form.down,
            form.mul,
            form.add,
            p.shift,
        )
    for name, j in plane_of.items():
        program[site.slots + j] = (*source(name), 0, 1, 0, 0)
    info = np.iinfo(np.int32)
    if program.min() < info.min or program.max() > info.max:
        raise OverflowError(f"an emit program word is outside int32:\n{program}")
    return program.astype(np.int32)


class CarriedLoop:
    """A graph's carried values, looped on the device.

    ``first`` runs once from the host; then ``body`` (taking no tensor) runs
    with ``depth`` runs in flight, each run's Emit writing the next's
    scratchpad, so the host only waits and restarts.
    """

    def __init__(self, first: CompiledGraph, body: CompiledGraph, depth: int = 2):
        for version in (first, body):
            if version.emit is None:
                raise ValueError(
                    f"{version.traced.name}: a full-ELF version with carried values "
                    f"loops; this one has no Emit step (compile one that takes a "
                    f"tensor with feeds= the version it starts)"
                )
        if first.arena is None or first.arena is not body.arena:
            raise ValueError("first and body are versions of one graph")
        if body.traced.inputs:
            raise ValueError(
                f"{body.traced.name}: the looped version takes no tensor, got "
                f"{body.traced.input_args}"
            )
        if depth < 1:
            raise ValueError(f"depth is at least 1, got {depth}")
        self.first, self.body, self.depth = first, body, depth
        first.emit_to(body)
        body.emit_to(body)
        # Each run holds a copy of its ELF's control code in the device heap,
        # 64 MB on older amdxdna, so the loop reuses each version's own run.
        self._runs: list[FullELFRun] = [body.callable.run]
        self._runs += [body.callable.new_run() for _ in range(depth - 1)]
        for k, run in enumerate(self._runs):
            run.bind_feedback(self._runs[(k + 1) % depth].scratchpad_alias())
        self._first = first.callable.run
        self._first.bind_feedback(self._runs[0].scratchpad_alias())

    def run(self, steps: int, /, *tensors, **values) -> Iterator[int]:
        """``start``, then ``steps``."""
        self.start(*tensors, **values)
        yield from self.steps(steps)

    def start(self, *tensors, **values) -> None:
        """Run ``first`` on ``tensors`` and ``values``, and wait for it."""
        self.body.upload()
        self.first.start(self._first, *tensors, **values)
        self.first.callable.wait(self._first)

    def steps(self, steps: int) -> Iterator[int]:
        """Run ``steps`` steps of ``body``, yielding each index once complete;
        closing early waits out the steps in flight.
        """
        in_flight: deque[int] = deque()
        for k in range(min(self.depth, steps)):
            self._runs[k].start()
            in_flight.append(k)
        try:
            for k in range(steps):
                run = self._runs[k % self.depth]
                self.body.callable.wait(run)
                in_flight.popleft()
                if k + self.depth < steps:
                    run.start()
                    in_flight.append(k + self.depth)
                yield k
        finally:
            self.body.callable.wait(*(self._runs[k % self.depth] for k in in_flight))
