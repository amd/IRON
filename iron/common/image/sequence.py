# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Image: what one run of a recorded graph builds and dispatches."""

from __future__ import annotations

import logging
from collections.abc import Hashable, Mapping
from typing import TYPE_CHECKING

import aie.utils as aie_utils
import numpy as np
from aie.utils import bfp

from ..declare import Operator
from .allocator import Allocation, ArenaPlan, lay_out
from .artifacts import Artifacts, Step
from .callable import BF16, ScratchArena
from .link import FullELF, PerStep
from .step import BufferRef, SequenceStep

if TYPE_CHECKING:
    from ..graph.record import Recording

logger = logging.getLogger(__name__)


def _signature(op):
    """The runtime arguments an operator takes: direction, shape and dtype each."""
    return [
        (b.role.__name__, tuple(b.shape), bfp.dtype_name(b.dtype)) for b in op.buffers
    ]


class Image:
    """A recorded graph's steps, built and dispatched as one image.

    Args:
        recording: The graph: its steps, inputs, outputs, the sizes of the
            buffers a step names only in part (``pinned``) and the buffers
            of its feedback argument.
        packaging: One full ELF, or an xclbin per step, as
            ``packaging.plan`` picks.
        arena: A shared ``ArenaPlan`` to place the scratch buffers in. The
            full ELF places them all; a step at a time, each buffer is its
            own buffer object, so only the residents are placed there.
        residents: With ``arena``, the scratch buffers resident there, by
            storage key.
    """

    def __init__(
        self,
        recording: Recording,
        packaging: FullELF | PerStep,
        arena: ArenaPlan | None = None,
        residents: Mapping[str, Hashable] | None = None,
    ):
        if residents and arena is None:
            raise ValueError("residents are placed in an arena; pass arena= too")
        self.steps = [SequenceStep(s.op, s.refs()) for s in recording.steps]
        # The chain's kernel instances are named from this label.
        self.name = recording.name
        self.inputs = [h.name for h in recording.inputs]
        self.outputs = [h.name for h in recording.outputs]
        self.feedback = list(recording.feedback)
        self.pinned = dict(recording.pinned)
        self.packaging = packaging
        self.arena = arena
        self.residents = dict(residents or {})
        self._arena_layout: dict[str, Allocation] | None = None
        self.layout: dict[str, tuple[str, int, int]] | None = None
        self._artifacts: Artifacts | None = None

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
        """The designs to build, and which design each operator uses.

        Operators reporting the same ``design_key`` collapse onto one design,
        so it is built, prefixed and configured once.
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
        """Each step's reads and writes among ``roots``, a part of a buffer
        its use.
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
        """This sequence's scratch buffers placed in the shared arena, once; a
        part's use is a use of its buffer.
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

    def _sizes(self) -> dict[str, int]:
        """Each buffer's bytes: those steps name whole first, in first-use
        order, by what they declare unless ``pinned`` sizes them, then the
        rest of ``pinned``.
        """
        sizes: dict[str, int] = {}
        declared: dict[str, object] = {}
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
        return sizes

    def _layout(self):
        """Each buffer's ``(argument kind, byte offset, bytes)``, and the
        bytes of each argument.
        """
        sizes = self._sizes()
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
        """The host dtype ``ref`` is viewed as: what the first step naming it
        declares, else, for a whole buffer, its parts' dtype if they agree
        (bytes if not), else bf16.
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

    def prepare(self):
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
        self.prepare()
        self.link()
        return self

    def link(self):
        """Build this sequence's image, once; sets ``self.image`` and ``artifacts``."""
        if self.layout is None:
            self.prepare()
        self.image = self.packaging.link(self)
        self._artifacts = self._record()
        return self.image

    @property
    def artifacts(self) -> Artifacts:
        """The record of what ``link`` produced."""
        if self._artifacts is None:
            raise RuntimeError(f"{self.name} is not linked; compile() first")
        return self._artifacts

    def _record(self):
        """What this image consists of: its designs, its steps, its buffers."""
        designs, design_of = self.unique_designs()
        operators = list(self.unique_operators())
        sharing = [
            tuple(op.name for op in operators if design_of[id(op)] == i)
            for i in range(len(designs))
        ]
        records, entry, insts = self.packaging.record(designs, sharing)
        labels = [d.name for d in records]
        by_design = {id(op): labels[design_of[id(op)]] for op in operators}
        steps = tuple(
            Step(i, s.op.name, by_design[id(s.op)], s.buffers)
            for i, s in enumerate(self.steps)
        )
        return Artifacts(
            full_elf=self.packaging.full_elf,
            image=self.image,
            insts=insts,
            entry=entry,
            designs=records,
            steps=steps,
            buffers=dict(self.layout),
        )

    def get_callable(self, arena: ScratchArena | None = None):
        """The runtime callable of this sequence's image, compiling first if
        needed. A sequence placed in an arena plan runs what it placed there
        in ``arena``, made here if not given.
        """
        if self.layout is None:
            self.compile()
        self.link()
        if self.arena is not None and arena is None:
            arena = ScratchArena(self.arena)
        return self.packaging.callable(self, arena)
