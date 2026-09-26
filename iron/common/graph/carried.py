# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Carried values computed on the device, and a loop that never asks the host.

A full-ELF version of a graph with ``Carried`` values ends in an
:class:`~iron.operators.emit.Emit` step. Every version of the function shares
one ``carry`` state, ``(2, carried)`` int32: plane 0 holds the values a call
started from, plane 1 the elements it computed (the producers write there
directly). Emit evaluates a program over the two planes into

- the next call's parameter scratchpad image, drained to the run's feedback
  argument, and
- plane 0 for the next call.

The program depends on the image the words land in -- which slot is which
value, and whether it is shifted for a core read -- so it is composed on the
host once both images are built (:meth:`CompiledGraph.emit_to`), and is data,
not part of the design. :class:`CarriedLoop` binds runs so that each one's
Emit writes the scratchpad of the next.
"""

from __future__ import annotations

import dataclasses
from collections import deque
from collections.abc import Iterator, Mapping
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

from ...operators.emit import ROW, Emit
from .handle import Affine, Handle, State
from .trace import TracedGraph, TracedStep

if TYPE_CHECKING:
    from ..image.callable import FullELFRun
    from .compiled import CompiledGraph

# The runlist names of the buffers an Emit step adds.
CARRY, PROGRAM, IMAGE = "carry", "emit_program", "emit_image"


@dataclasses.dataclass(frozen=True)
class Parameter:
    """One entry of an image's ``params.txt``: a word of its scratchpad."""

    name: str
    index: int
    kind: str  # "core": the scratchpad holds it shifted left by 2; "addr": raw

    @property
    def shift(self) -> int:
        return 2 if self.kind == "core" else 0


def read_parameters(path: Path) -> list[Parameter]:
    """The per-call values an image's scratchpad holds, from its ``params.txt``."""
    count, *lines = path.read_text().split("\n")
    parameters = []
    for line in lines[: int(count)]:
        name, index, _, kind = line.split()
        parameters.append(Parameter(name, int(index), kind))
    return parameters


@dataclasses.dataclass(frozen=True)
class EmitSite:
    """What a version's Emit step reads and writes."""

    carried: tuple[str, ...]  # the function's carried values, in plane order
    carry: State  # (2, len(carried)), shared by every version
    program: State  # (slots + len(carried), ROW), this version's own
    slots: int  # the words of the scratchpad the image is written into


def attach_emit(
    traced: TracedGraph, carried: list[str], carry: State, slots: int
) -> EmitSite:
    """Append an Emit step to ``traced`` for a target of ``slots`` values.

    Each carried element the graph computes is moved into plane 1 of
    ``carry``: its producer writes there, and nothing else changes for
    whatever reads it.
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
    """Register ``state`` with the graph, as a closed-over one is."""
    handle = Handle(state.shape, state.dtype, state.name, "state")
    traced.states[id(state)] = (state, handle)
    traced.pinned[handle.name] = handle.nbytes
    return handle


def _move(traced: TracedGraph, handle: Handle, parent: Handle, start: int) -> None:
    """Make a computed element a view of ``parent`` at ``start``: the handle,
    and every other view of its buffer the steps hold."""
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
    symbols: list[tuple[Affine, str]],
    parameters: list[Parameter],
) -> np.ndarray:
    """The Emit program a version with ``site`` and ``next_values`` runs to
    start a call of the image with ``symbols`` and ``parameters``.

    Every word of the target's scratchpad must follow from a carried value:
    the device knows nothing else, and the host may not write a word the
    device writes.
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
        """(plane, index, scale, bias) of carried ``name``'s next value."""
        nxt = next_values[name]
        if isinstance(nxt, Handle):
            return 1, plane_of[name], 1, 0
        if nxt.value.name not in plane_of:
            raise ValueError(
                f"the next {name} is {nxt!r}, and {nxt.value.name} is not carried"
            )
        return 0, plane_of[nxt.value.name], nxt.scale, nxt.bias

    expressions = dict((symbol, expression) for expression, symbol in symbols)
    program = np.zeros(site.program.shape, dtype=np.int64)
    for p in parameters:
        expression = expressions.get(p.name)
        if expression is None:
            raise ValueError(f"{p.name} is not a value the graph binds")
        name = expression.value.name
        if name not in plane_of:
            raise ValueError(
                f"{p.name} is computed from {name}, which is not carried: the "
                f"device cannot know it"
            )
        plane, index, scale, bias = source(name)
        program[p.index] = (
            plane,
            index,
            expression.scale * scale,
            expression.scale * bias + expression.bias,
            p.shift,
        )
    for name, j in plane_of.items():
        program[site.slots + j] = (*source(name), 0)
    info = np.iinfo(np.int32)
    if program.min() < info.min or program.max() > info.max:
        raise OverflowError(f"an emit program word is outside int32:\n{program}")
    return program.astype(np.int32)


class CarriedLoop:
    """A graph's carried values, looped on the device.

    ``first`` runs once, with inputs and values from the host; then ``body``
    runs step after step, ``depth`` runs of it in flight. Each run's Emit
    writes the scratchpad of the run after it, so after ``first`` the host
    writes nothing: it waits on each step and restarts that run for the step
    ``depth`` later. ``first`` and ``body`` are full-ELF versions of one
    graph function (they share its arena and its carry), and ``body`` takes
    no tensor, since nothing would write one between its steps.
    """

    def __init__(self, first: CompiledGraph, body: CompiledGraph, depth: int = 2):
        for version in (first, body):
            if version.emit is None:
                raise ValueError(
                    f"{version.traced.name}: a full-ELF version with carried values "
                    f"loops; this one has no Emit step"
                )
        if first.arena is None or first.arena is not body.arena:
            raise ValueError("first and body are versions of one graph function")
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
        self._runs: list[FullELFRun] = [body.callable.new_run() for _ in range(depth)]
        for k, run in enumerate(self._runs):
            run.bind_feedback(self._runs[(k + 1) % depth].scratchpad_alias())
        self._first = first.callable.new_run()
        self._first.bind_feedback(self._runs[0].scratchpad_alias())

    def run(self, steps: int, /, *tensors, **values) -> Iterator[int]:
        """Run ``first`` on ``tensors`` and ``values``, then ``steps`` steps of
        ``body``; yield each step's index once it has completed.

        Closing the iterator early waits out the steps in flight.
        """
        self.start(*tensors, **values)
        yield from self.steps(steps)

    def start(self, *tensors, **values) -> None:
        """Run ``first`` on ``tensors`` and ``values``, and wait for it."""
        # Nothing stages the body's own call: its weights go up with first's.
        self.body.upload()
        self.first.start(self._first, *tensors, **values)
        self.first.callable.wait(self._first)

    def steps(self, steps: int) -> Iterator[int]:
        """Run ``steps`` steps of ``body`` from the carry :meth:`start` left;
        yield each step's index once it has completed.

        Closing the iterator early waits out the steps in flight.
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
