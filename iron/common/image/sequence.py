# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Image: what one run of a recorded graph builds and dispatches."""

from __future__ import annotations

import logging
from collections.abc import Hashable, Mapping, Sequence
from typing import TYPE_CHECKING

import aie.utils as aie_utils
import numpy as np
from aie.utils import bfp

from ..declare import Operand, Operator
from .allocator import Allocation, ArenaPlan, lay_out
from .artifacts import Artifacts, Step
from .callable import BF16, FullELFCallable, PerStepCallable, ScratchArena
from .link import FullELF, PerStep
from .step import BufferRef, Fusion, SequenceStep

if TYPE_CHECKING:
    from ..graph.record import Recording

logger = logging.getLogger(__name__)


def _signature(op):
    """Return the runtime arguments an operator takes: direction, shape and dtype each."""
    return [
        (b.role.__name__, tuple(b.shape), bfp.dtype_name(b.dtype)) for b in op.buffers
    ]


class Image:
    """A recorded graph's steps, built and dispatched as one image.

    ``residents``, by storage key, keep one place in the shared ``arena``
    across images.
    """

    def __init__(
        self,
        recording: Recording,
        packaging: FullELF | PerStep,
        arena: ArenaPlan | None = None,
        residents: Mapping[str, Hashable] | None = None,
        fusions: Sequence[Fusion] = (),
    ):
        if residents and arena is None:
            raise ValueError("residents are placed in an arena; pass arena= too")
        self.steps = [SequenceStep(s.op, s.refs()) for s in recording.steps]
        # A fusion's kernel instances are named from this label.
        self.name = recording.name
        self.inputs = [h.name for h in recording.inputs]
        self.outputs = [h.name for h in recording.outputs]
        self.feedback = list(recording.feedback)
        self.pinned = dict(recording.pinned)
        self.packaging = packaging
        self.arena = arena
        self.residents = dict(residents or {})
        self.fusions = tuple(fusions)
        if self.fusions and isinstance(packaging, PerStep) and packaging.check:
            raise ValueError(
                "fusions need their own single dispatch; check=True checks "
                "each step on its own, against its reference"
            )
        self._validate_fusions()
        self._arena_layout: dict[str, Allocation] | None = None
        self.layout: dict[str, tuple[str, int, int]] | None = None
        self._artifacts: Artifacts | None = None

    def _validate_fusions(self) -> None:
        """Each ``Fusion``'s steps are real steps, no step in two fusions, and
        each of its edges names a real hand-off: the producer's drained
        output and the consumer's filled input, both the whole of one buffer.

        Raises:
            ValueError: Any of the above does not hold.
        """
        claimed: set[int] = set()
        for fusion in self.fusions:
            for s in fusion.steps:
                if not 0 <= s < len(self.steps):
                    raise ValueError(
                        f"fusion step {s} names no step ({len(self.steps)} steps)"
                    )
                if s in claimed:
                    raise ValueError(f"step {s} is in two fusions")
            claimed |= set(fusion.steps)
            for edge in fusion.edges:
                producer, consumer = (
                    self.steps[edge.producer],
                    self.steps[edge.consumer],
                )
                out = next(
                    (
                        ref
                        for ref, b in zip(producer.buffers, producer.op.buffers)
                        if b.name == edge.output and b.drains
                    ),
                    None,
                )
                if out is None:
                    raise ValueError(
                        f"step {edge.producer} ({type(producer.op).__name__}) has "
                        f"no drained buffer {edge.output!r}"
                    )
                in_ = next(
                    (
                        ref
                        for ref, b in zip(consumer.buffers, consumer.op.buffers)
                        if b.name == edge.input and b.fills
                    ),
                    None,
                )
                if in_ is None:
                    raise ValueError(
                        f"step {edge.consumer} ({type(consumer.op).__name__}) has "
                        f"no filled buffer {edge.input!r}"
                    )
                if (
                    out.nbytes is not None
                    or in_.nbytes is not None
                    or out.root != in_.root
                ):
                    raise ValueError(
                        f"edge {edge.producer}->{edge.consumer}: {edge.output!r} "
                        f"({out}) and {edge.input!r} ({in_}) do not name one "
                        f"whole buffer"
                    )

    @property
    def traced(self) -> bool:
        """Whether any step's operator is built with a ``trace``."""
        return any(s.op.trace is not None for s in self.steps)

    def unique_operators(self):
        """Operators in step order, de-duplicated by identity."""
        seen = {}
        for s in self.steps:
            seen.setdefault(id(s.op), s.op)
        return list(seen.values())

    def unique_designs(self):
        """Return the designs to build, and which each operator uses.

        Operators reporting one ``design_key`` share a design, built and
        configured once.
        """
        designs = []
        design_of = {}
        first_with_key = {}
        for op in self.unique_operators():
            key = op.design_key()
            if key in first_with_key:
                shared = designs[first_with_key[key]]
                if _signature(op) != _signature(shared):
                    raise ValueError(
                        f"{op.name} and {shared.name} report the same design_key but "
                        "different runtime arguments, so the design cannot be shared"
                    )
                design_of[id(op)] = first_with_key[key]
                continue
            first_with_key[key] = len(designs)
            design_of[id(op)] = len(designs)
            designs.append(op)
        return designs, design_of

    def _uses(self, roots) -> list[tuple[list[str], list[str]]]:
        """Return each step's reads and writes among ``roots``.

        A part of a buffer is its use.
        """
        uses = []
        for s in self.steps:
            reads, writes = [], []
            for ref, b in zip(s.buffers, s.op.buffers):
                if ref.root not in roots:
                    continue
                if b.fills:
                    reads.append(ref.root)
                if b.drains:
                    writes.append(ref.root)
            uses.append((reads, writes))
        return uses

    def _place_in_arena(self, uses, sizes: Mapping[str, int]) -> dict[str, Allocation]:
        """Place this sequence's scratch buffers in the shared arena, once.

        A part's use is a use of its buffer.
        """
        if self._arena_layout is not None:
            return self._arena_layout
        missing = set(self.residents) - set(sizes)
        if missing:
            raise ValueError(
                f"residents {sorted(missing)} are not scratch buffers of {self.name}"
            )
        assert self.arena is not None, "placed in an arena plan"
        self._arena_layout = self.arena.place_image(uses, sizes, self.residents)
        return self._arena_layout

    def _layout(self):
        """Return each buffer's ``(argument kind, byte offset, bytes)`` and each argument's bytes.

        ``pinned`` sizes a buffer over what the steps naming it whole
        declare.
        """
        sizes: dict[str, int] = {}
        declared: dict[str, Operand] = {}
        parts = []
        for s in self.steps:
            if len(s.buffers) != len(s.op.buffers):
                raise ValueError(
                    f"{s.op!r} declares {len(s.op.buffers)} buffers, but its step "
                    f"names {len(s.buffers)}"
                )
            for ref, b in zip(s.buffers, s.op.buffers):
                if ref.nbytes is not None:
                    parts.append(ref)
                    continue
                seen = declared.setdefault(ref.root, b)
                if seen.nbytes != b.nbytes:
                    raise ValueError(
                        f"Buffer {ref.root!r} has conflicting sizes between "
                        f"operators: {seen.shape} {bfp.dtype_name(seen.dtype)} vs "
                        f"{b.shape} {bfp.dtype_name(b.dtype)}"
                    )
                sizes.setdefault(ref.root, self.pinned.get(ref.root, b.nbytes))
        for root, nbytes in self.pinned.items():
            sizes.setdefault(root, nbytes)
        for ref in parts:
            if ref.root not in sizes:
                raise ValueError(f"{ref} is part of {ref.root!r}, which has no size")
        for kind, roots in (
            ("Input", self.inputs),
            ("Output", self.outputs),
            ("Feedback", self.feedback),
        ):
            for root in roots:
                if root not in sizes:
                    raise ValueError(f"{kind} buffer {root!r} is no step's buffer")
        both = set(self.feedback) & {*self.inputs, *self.outputs}
        if both:
            raise ValueError(f"Feedback buffers {sorted(both)} are inputs or outputs")
        uses = self._uses(sizes)
        arena = {}
        if self.arena is not None:
            hosted = {*self.inputs, *self.outputs, *self.feedback}
            scratch = [r for r in sizes if r not in hosted]
            placed = self.packaging.in_arena(scratch, self.residents)
            arena = self._place_in_arena(uses, {r: sizes[r] for r in placed})
        host = (self.inputs, self.outputs, self.feedback)
        return lay_out(sizes, uses, host, self.pinned, arena)

    def buffer_dtype(self, ref: BufferRef) -> np.dtype:
        """Return the host dtype ``ref`` is viewed as.

        What the first step naming it declares, else a whole buffer's
        parts' if they agree (bytes if not), or bf16.
        """
        parts = set()
        for s in self.steps:
            for r, b in zip(s.buffers, s.op.buffers):
                if r == ref:
                    return np.dtype(b.host_dtype)
                if ref.nbytes is None and r.root == ref.root:
                    parts.add(np.dtype(b.host_dtype))
        if len(parts) == 1:
            return parts.pop()
        return np.dtype(np.uint8) if parts else BF16

    def _prepare(self):
        """Resolve the operators and lay the buffers out, before anything is built."""
        dev = aie_utils.get_current_device()
        # Resolved before unique_designs() takes identities, so operators that
        # resolve alike are one design.
        resolved: dict[int, Operator] = {}
        for s in self.steps:
            if id(s.op) not in resolved:
                resolved[id(s.op)] = s.op.resolved(dev)
        self.steps = [SequenceStep(resolved[id(s.op)], s.buffers) for s in self.steps]
        self.layout, self.buffer_sizes = self._layout()

    def compile(self):
        """Build the image ahead of time."""
        self._prepare()
        self._link()
        return self

    def _link(self):
        """Build this sequence's image, once; sets ``self.image`` and ``artifacts``."""
        self.image = self.packaging.link(self)
        self._artifacts = self._record()
        return self.image

    @property
    def artifacts(self) -> Artifacts:
        """The record of what ``compile`` produced."""
        if self._artifacts is None:
            raise RuntimeError(f"{self.name} is not linked; compile() first")
        return self._artifacts

    def _record(self):
        """Record what this image consists of: its designs, its steps, its buffers."""
        assert self.layout is not None, "_prepare() ran before _link()"
        designs, design_of = self.unique_designs()
        operators = list(self.unique_operators())
        sharing = [
            tuple(op.name for op in operators if design_of[id(op)] == i)
            for i in range(len(designs))
        ]
        records, entry, insts = self.packaging.record(designs, sharing)
        labels = [d.name for d in records]
        by_design = {id(op): labels[design_of[id(op)]] for op in operators}
        # A fusion's steps are one design in the composed module: all of its
        # members report one label, not their separate standalone ones.
        for fusion in self.fusions:
            paired = "+".join(by_design[id(self.steps[j].op)] for j in fusion.steps)
            for j in fusion.steps:
                by_design[id(self.steps[j].op)] = paired
        steps = tuple(
            Step(i, s.op.name, by_design[id(s.op)], s.buffers)
            for i, s in enumerate(self.steps)
        )
        return Artifacts(
            full_elf=isinstance(self.packaging, FullELF),
            image=self.image,
            insts=insts,
            entry=entry,
            designs=records,
            steps=steps,
            buffers=dict(self.layout),
        )

    def get_callable(
        self, arena: ScratchArena | None = None
    ) -> FullELFCallable | PerStepCallable:
        """Return the callable of this sequence's image, compiling first if needed.

        Runs in ``arena`` what it placed in an arena plan (a new arena if
        not given).
        """
        if self.layout is None:
            self._prepare()
        self._link()
        if self.arena is not None and arena is None:
            arena = ScratchArena(self.arena)
        return self.packaging.callable(self, arena)
