# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Image: what one run of a recorded graph builds and dispatches."""

from __future__ import annotations

import logging
from collections.abc import Hashable, Mapping, Sequence
from pathlib import Path
from typing import TYPE_CHECKING

import aie.utils as aie_utils
import numpy as np
from aie.utils import bfp
from aie.utils.npukernel import NPUKernel

from ..declare import Operator
from .allocator import ALIGNMENT, BANK, Allocation, ArenaPlan, LiveRange, Pool
from .artifacts import Artifacts, Design, Step
from .callable import BF16, FullELFCallable, ScratchArena, PerStepCallable
from .coresidence import AdjacentPacking
from .link import FullELF, PerStep
from .compose import ArgumentSizes
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
        full_elf: One full ELF, else one xclbin per design, a step at a
            time; ``None`` is a full ELF where the device dispatches one.
        check: The xclbin chain, each step checked against its reference
            on the NPU's inputs (``callable.check_step``).
        arena: A shared ``ArenaPlan`` to place the scratch buffers in. The
            full ELF places them all; a step at a time, each buffer is its
            own buffer object, so only the residents are placed there.
        residents: With ``arena``, the scratch buffers resident there, by
            storage key.
        shared_words: On the full ELF, design symbol -> the scratchpad word
            it shares with others that always hold the same number.
        coresident: Groups of operators whose designs share one device
            configuration in the full ELF, or an ``AdjacentPacking`` that
            chooses them.
        reconfigure: On the full ELF, configure the array at every call even
            where it runs one design, which the first call otherwise
            configures for all (``Composition.expands``).
        commands: On the full ELF, the steps that start a command of their
            own after the first's, each command a runtime sequence a call
            queues after the one before it.
    """

    def __init__(
        self,
        recording: Recording,
        full_elf: bool | None = None,
        check: bool = False,
        arena: ArenaPlan | None = None,
        residents: Mapping[str, Hashable] | None = None,
        shared_words: Mapping[str, str] | None = None,
        coresident: Sequence[Sequence[Operator]] | AdjacentPacking = (),
        reconfigure: bool = False,
        commands: Sequence[int] = (),
    ):
        if check:
            if full_elf:
                raise ValueError("check=True checks each step of an xclbin chain")
            full_elf = False
        if residents and arena is None:
            raise ValueError("residents are placed in an arena; pass arena= too")
        unbuilt = "check=True" if check else "full_elf=False"
        if recording.feedback and full_elf is False:
            raise ValueError(
                f"feedback arguments are an argument of the full ELF; "
                f"{unbuilt} has none"
            )
        if coresident and full_elf is False:
            raise ValueError(
                f"co-residence packs designs into one full-ELF device; "
                f"{unbuilt} builds none"
            )
        if reconfigure and full_elf is False:
            raise ValueError(
                f"reconfigure configures the full ELF at every call; "
                f"{unbuilt} builds none"
            )
        if commands and full_elf is False:
            raise ValueError(
                f"commands split the full ELF's sequence; {unbuilt} dispatches "
                f"every step on its own"
            )
        self.steps = [SequenceStep(s.op, s.refs()) for s in recording.steps]
        if isinstance(coresident, AdjacentPacking):
            self.coresident: tuple[tuple[Operator, ...], ...] | AdjacentPacking = (
                coresident
            )
        else:
            stepped = {id(s.op) for s in self.steps}
            strays = [
                type(op).__name__
                for group in coresident
                for op in group
                if id(op) not in stepped
            ]
            if strays:
                raise ValueError(f"coresident names operators no step runs: {strays}")
            self.coresident = tuple(tuple(group) for group in coresident)
        # The chain's kernel instances are named from this label.
        self.name = recording.name
        self.inputs = [h.name for h in recording.inputs]
        self.outputs = [h.name for h in recording.outputs]
        self.feedback = list(recording.feedback)
        self.pinned = dict(recording.pinned)
        self.reconfigure = reconfigure
        self.commands = tuple(commands)
        self.arena = arena
        self.residents = dict(residents or {})
        self.shared_words = dict(shared_words or {})
        self._arena_layout: dict[str, Allocation] | None = None
        self.full_elf = full_elf
        self.check = check
        self.layout: dict[str, tuple[str, int, int]] | None = None
        self._image = None
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

    def _pool_offsets(self, sizes: Mapping[str, int]) -> dict[str, int]:
        """Byte offsets letting intermediates with disjoint lifetimes overlap;
        a buffer the host addresses, or one a step names only in part, is
        never pooled.
        """
        held = {*self.inputs, *self.outputs, *self.feedback, *self.pinned}
        ranges = LiveRange.scan(self._uses(sizes), pinned=held)
        allocations, _ = Pool(ALIGNMENT).place(ranges, sizes)
        return {name: a.offset for name, a in allocations.items()}

    def _place_in_arena(self, sizes: Mapping[str, int]) -> dict[str, Allocation]:
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
        self._arena_layout = self.arena.place_image(
            self._uses(sizes), sizes, self.residents
        )
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

    def _layout(self) -> tuple[dict[str, tuple[str, int, int]], ArgumentSizes]:
        """Each buffer's ``(argument kind, byte offset, bytes)``, and the
        bytes of each argument.
        """
        sizes = self._sizes()
        layout: dict[str, tuple[str, int, int]] = {}

        def place(kind: str, roots: list[str]) -> int:
            if kind == "scratch" and self.arena is not None:
                stepwise = self.full_elf is False
                placed = self._place_in_arena(
                    {r: sizes[r] for r in roots if not stepwise or r in self.residents}
                )
                for root, a in placed.items():
                    layout[root] = (kind, a.offset, a.size)
                if not stepwise:
                    return max((a.end for a in placed.values()), default=0)
                roots = [r for r in roots if r not in placed]
            # The caller binds its own memory to the feedback argument: offsets are the contract.
            offsets = (
                self._pool_offsets({r: sizes[r] for r in roots})
                if kind != "feedback"
                else {}
            )
            # A host-visible kind is one buffer object, not banks.
            pool = Pool(ALIGNMENT, BANK if kind == "scratch" else None)
            cursor = end = 0
            pooled = []
            for root in roots:
                if root in offsets:
                    pooled.append(root)
                    continue
                cursor = pool.fit(cursor, sizes[root])
                layout[root] = (kind, cursor, sizes[root])
                end = cursor + sizes[root]
                cursor = pool.align(end)
            # The pool starts at zero, so it is rebased past the other
            # buffers, at a bank's start unless it fits the rest of this one.
            span = max((offsets[r] + sizes[r] for r in pooled), default=0)
            if pool.bank is not None and span > pool.bank - cursor % pool.bank:
                cursor = -(-cursor // pool.bank) * pool.bank
            for root in pooled:
                at = cursor + offsets[root]
                layout[root] = (kind, at, sizes[root])
                end = max(end, at + sizes[root])
            return end

        host = {*self.inputs, *self.outputs, *self.feedback}
        argument_sizes = ArgumentSizes(
            place("input", self.inputs),
            place("output", self.outputs),
            place("scratch", [r for r in sizes if r not in host]),
            place("feedback", self.feedback) if self.feedback else None,
        )
        return layout, argument_sizes

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
        """Settle the packaging and lay the buffers out, before anything is built."""
        dev = aie_utils.get_current_device()
        if self.full_elf is None:
            self.full_elf = dev is not None and dev.dispatches_full_elf
            if self.feedback and not self.full_elf:
                raise ValueError(
                    f"{self.name}: feedback arguments need the full ELF, which "
                    f"this device does not dispatch"
                )
            if self.coresident and not self.full_elf:
                raise ValueError(
                    f"{self.name}: co-residence packs designs into one full-ELF "
                    f"device, which this device does not dispatch"
                )
        # Resolved before unique_designs() takes identities, so operators that
        # resolve alike are one design.
        resolved: dict[int, Operator] = {}
        for s in self.steps:
            if id(s.op) not in resolved:
                resolved[id(s.op)] = s.op.resolved(dev)
        self.steps = [SequenceStep(resolved[id(s.op)], s.buffers) for s in self.steps]
        if not isinstance(self.coresident, AdjacentPacking):
            self.coresident = tuple(
                tuple(resolved[id(op)] for op in group) for group in self.coresident
            )
        # After the packaging check: a sequence that cannot run in its arena must
        # not place anything there.
        self.layout, self.buffer_sizes = self._layout()
        self._image = FullELF() if self.full_elf else PerStep()

    def compile(self):
        """Build the image ahead of time."""
        self.prepare()
        self.link()
        return self

    def link(self):
        """Build this sequence's image, once; sets ``self.image`` and ``artifacts``."""
        if self.layout is None:
            self.prepare()
        self.image = self._image.link(self)
        self._artifacts = self._record()
        return self.image

    def kernel(self, op: Operator) -> NPUKernel:
        """The kernel a step of ``op`` dispatches on the xclbin chain."""
        if not isinstance(self._image, PerStep) or self._image.image is None:
            raise RuntimeError(f"{self.name} is not linked as an xclbin chain")
        return self._image.links[id(op)].kernel

    @property
    def elf_path(self):
        """The full ELF, when that is this sequence's image."""
        return self.image if isinstance(self._image, FullELF) else None

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
        insts = None
        if isinstance(self._image, FullELF):
            assert self._image.design is not None, "link() built the image"
            entry = self._image.design.get_cache_entry()
            labels = [f"op{i}_{type(op).__name__}" for i, op in enumerate(designs)]
            records = tuple(
                Design(name=labels[i], operators=sharing[i])
                for i in range(len(designs))
            )
            image = self.image
        else:
            links = [self._image.links[id(op)] for op in designs]
            labels = [link.name for link in links]
            records = tuple(
                Design(
                    name=link.name,
                    operators=sharing[i],
                    entry=(
                        link.design
                        if link.configuration is None
                        else link.configuration
                    ).get_cache_entry(),
                    image=Path(link.kernel.xclbin_path),
                    insts=link.design.get_cache_entry().insts,
                )
                for i, link in enumerate(links)
            )
            entry = links[0].design.get_cache_entry()
            if len(links) == 1:
                insts = entry.insts
            image = self._image.image
        by_design = {id(op): labels[design_of[id(op)]] for op in operators}
        assert image is not None, "the image has been built"
        steps = tuple(
            Step(i, s.op.name, by_design[id(s.op)], s.buffers)
            for i, s in enumerate(self.steps)
        )
        return Artifacts(
            full_elf=self.full_elf,
            image=image,
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
        if not self.full_elf:
            return PerStepCallable(self, check=self.check, arena=arena)
        return FullELFCallable(self, arena=arena)
