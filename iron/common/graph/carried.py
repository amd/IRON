# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Carried values computed on the device, and a loop that never asks the host.

A full-ELF version with ``Carried`` values ends in an ``Emit`` step, whose
program (``CompiledGraph.emit_to()``) turns the shared ``carry``, ``(2, carried)``
int32 (start values, computed ones), into the next call's scratchpad and start.
"""

from __future__ import annotations

import dataclasses
from collections import deque
from collections.abc import Iterator, Mapping
from typing import TYPE_CHECKING

import numpy as np
from aie.helpers.taplib import Affine

from ...operators.emit import ROW, UNCLAMPED, Emit
from ..image.artifacts import Parameter
from ..image.callable import FullELFCallable
from .handle import Dense, Handle, State
from .record import Recording, Step

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
    recording: Recording, carried: list[str], carry: State, slots: int
) -> EmitSite:
    """Append an Emit step to ``recording`` for a target of ``slots`` values.

    Each computed carried element is moved into plane 1 of ``carry``.
    """
    if slots < 1:
        raise ValueError(
            f"{recording.name}: the image its carried values are emitted into takes "
            f"no per-call values"
        )
    taken = {h.name for s in recording.steps for h in s.slots} | set(recording.pinned)
    clash = taken & {CARRY, PROGRAM, IMAGE}
    if clash:
        raise ValueError(
            f"{recording.name}: buffer names {sorted(clash)} are the Emit's"
        )
    n = len(carried)
    planes = _resident(recording, carry)
    for j, name in enumerate(carried):
        nxt = recording.carry[name]
        if isinstance(nxt, Handle):
            if any(nxt is h for h in recording.returned):
                raise NotImplementedError(
                    f"{recording.name}: {name} is carried and returned; on a full ELF "
                    f"it is computed into the carry, so read it from the Carry"
                )
            _move(recording, nxt, planes, n + j)
    program = State((slots + n, ROW), np.int32, PROGRAM)
    image = Handle.whole((slots,), np.int32, IMAGE, "intermediate")
    current = Handle(planes.buffer, (n,), np.int32, {}, Dense(0))
    inputs = [_resident(recording, program), planes]
    recording.steps.append(
        Step(
            Emit(slots=slots, carried=n),
            inputs + [image, current],
            inputs,
            [image, current],
        )
    )
    recording.feedback = [IMAGE]
    return EmitSite(tuple(carried), carry, program, slots)


def _resident(recording: Recording, state: State) -> Handle:
    assert state.name is not None, "the carry and the program are named"
    handle = Handle.whole(state.shape, state.dtype, state.name, "state")
    recording.states[id(state)] = (state, handle)
    recording.pinned[handle.name] = handle.nbytes
    return handle


def _move(recording: Recording, handle: Handle, planes: Handle, start: int) -> None:
    """Put ``handle``'s buffer, a carried element, at element ``start`` of ``planes``'s.

    In every step and in the carry.
    """
    old = handle.buffer

    def moved(h):
        if not isinstance(h, Handle) or h.buffer is not old:
            return h
        if h.layout != Dense():
            raise NotImplementedError(
                f"{recording.name}: {h!r} slices the carried element {old.name!r}"
            )
        return dataclasses.replace(h, buffer=planes.buffer, layout=Dense(start))

    for s in recording.steps:
        s.slots, s.inputs, s.outputs = (
            [moved(h) for h in hs] for hs in (s.slots, s.inputs, s.outputs)
        )
    recording.carry = {k: moved(v) for k, v in recording.carry.items()}
    recording.outputs = [h for h in recording.outputs if h.buffer is not old]


def compose(
    site: EmitSite,
    next_values: Mapping[str, Handle | Affine],
    words: list[Word],
    parameters: list[Parameter],
) -> np.ndarray:
    """Return the Emit program that starts a call of the image with ``words`` and ``parameters``.

    Every word of it must follow from a carried value.
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
            UNCLAMPED[0] if form.lo is None else form.lo,
            UNCLAMPED[1] if form.hi is None else form.hi,
            -1 if form.mod is None else form.mod - 1,
            p.shift,
        )
    for name, j in plane_of.items():
        program[site.slots + j] = (*source(name), 0, 1, 0, *UNCLAMPED, -1, 0)
    info = np.iinfo(np.int32)
    if program.min() < info.min or program.max() > info.max:
        raise OverflowError(f"an emit program word is outside int32:\n{program}")
    return program.astype(np.int32)


class CarriedLoop:
    """A graph's carried values looped on the device.

    ``first`` runs once from the host, then ``body`` (no tensor) with
    ``depth`` runs in flight, each run's Emit writing the next's
    scratchpad, so the host only waits and restarts.
    """

    def __init__(self, first: CompiledGraph, body: CompiledGraph, depth: int = 2):
        for version in (first, body):
            if version.emit is None:
                raise ValueError(
                    f"{version.recording.name}: a full-ELF version with carried values "
                    f"loops; this one has no Emit step (compile one that takes a "
                    f"tensor with feeds= the version it starts)"
                )
        if first.arena is None or first.arena is not body.arena:
            raise ValueError("first and body are versions of one graph")
        if body.recording.inputs:
            raise ValueError(
                f"{body.recording.name}: the looped version takes no tensor, got "
                f"{[h.name for h in body.recording.inputs]}"
            )
        if depth < 1:
            raise ValueError(f"depth is at least 1, got {depth}")
        self.first, self.body, self.depth = first, body, depth
        first.emit_to(body)
        body.emit_to(body)
        # Each run holds a copy of its ELF's control code in the device heap,
        # 64 MB on older amdxdna, so the loop reuses each version's own run.
        first_call, body_call = first.callable, body.callable
        # Only a full ELF has an Emit step.
        assert isinstance(first_call, FullELFCallable)
        assert isinstance(body_call, FullELFCallable)
        self._first_call, self._body_call = first_call, body_call
        # Built on the first start(): first runs once and, where it is not
        # body itself, is dead after, so the heap holds first's ctrlcode and
        # body's first copy, then body's depth copies, never 1 + depth.
        self._runs: list[FullELFRun] | None = None

    def run(self, steps: int, /, *tensors, **values) -> Iterator[int]:
        """``start`` now, then ``steps``, each index yielded once complete."""
        self.start(*tensors, **values)
        return self.steps(steps)

    def start(self, *tensors, **values) -> None:
        """Run ``first`` on ``tensors`` and ``values``, and wait for it."""
        self.body.upload()
        first_run = self._first_call.run
        runs = self._runs or [self._body_call.run]
        first_run.bind_feedback(runs[0].scratchpad_alias())
        self.first.start(first_run, *tensors, **values)
        self._first_call.wait(first_run)
        if self._first_call is not self._body_call:
            # first never runs again: free its ctrlcode heap copy, as any
            # other callable's idle run is (FullELFCallable.release()), not
            # just when a later new_run() happens to need the room.
            first_run.wired = False
            self._first_call.release()
        # pyxrt frees a run's ctrlcode only once nothing references the run.
        del first_run
        if self._runs is None:
            runs += [self._body_call.new_run() for _ in range(self.depth - 1)]
            for k, run in enumerate(runs):
                run.bind_feedback(runs[(k + 1) % self.depth].scratchpad_alias())
            self._runs = runs

    def steps(self, steps: int) -> Iterator[int]:
        """Run ``steps`` steps of ``body``, yielding each index once complete.

        Closing early waits out the steps in flight.
        """
        assert self._runs is not None, "start() builds body's runs first"
        in_flight: deque[int] = deque()
        for k in range(min(self.depth, steps)):
            self._runs[k].start()
            in_flight.append(k)
        try:
            for k in range(steps):
                run = self._runs[k % self.depth]
                self._body_call.wait(run)
                in_flight.popleft()
                if k + self.depth < steps:
                    run.start()
                    in_flight.append(k + self.depth)
                yield k
        finally:
            self._body_call.wait(*(self._runs[k % self.depth] for k in in_flight))
