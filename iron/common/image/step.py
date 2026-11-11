# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A step of a sequence, and where its buffers are in the image's."""

from __future__ import annotations

import hashlib
from collections.abc import Iterator, Mapping, Sequence
from dataclasses import dataclass
from enum import Enum

from ..declare import Operator


@dataclass(frozen=True)
class BufferRef:
    """Where a step's buffer is.

    ``nbytes`` bytes of the image's buffer ``root`` from byte ``start``, or
    all of it where ``nbytes`` is None.
    """

    root: str
    start: int = 0
    nbytes: int | None = None

    def place(self, layout: Mapping[str, tuple[str, int, int]]) -> tuple[str, int, int]:
        """Return where this is, ``layout`` placing each buffer.

        Its ``(argument kind, byte offset, bytes)``.
        """
        kind, offset, nbytes = layout[self.root]
        return kind, offset + self.start, nbytes if self.nbytes is None else self.nbytes

    def __str__(self) -> str:
        if self.nbytes is None:
            return self.root
        return f"{self.root}[{self.start}:{self.start + self.nbytes}]"


class FusionKind(Enum):
    """How a fusion's steps run as one device configuration.

    ``STREAM`` (consecutive steps, each edge a fifo its lanes meet directly), ``STAGED``
    (as a stream, an edge whose lanes do not meet restaged through memtiles), ``PACK``
    (independent steps co-resident, issued concurrently), ``MERGE`` (consecutive steps
    sharing a configuration, run back to back with no edge), or ``FOLD`` (a consumer's
    kernel run in its producer's cores, applied to the recording before planning).
    """

    STREAM = "stream"
    STAGED = "staged"
    FOLD = "fold"
    PACK = "pack"
    MERGE = "merge"


@dataclass(frozen=True)
class Edge:
    """Step ``producer``'s output ``output`` streamed on-chip into step ``consumer``'s input ``input``.

    Both indices into one ``Fusion``'s ``steps``; several edges may share one
    ``(producer, output)``, fanning out to more than one consumer.
    """

    producer: int
    output: str
    consumer: int
    input: str


@dataclass(frozen=True)
class Fusion:
    """A set of steps that build and dispatch as one device configuration, with no host transfer between.

    ``kind`` how, ``steps`` its members (increasing, distinct indices into a sequence)
    and ``edges`` each on-chip hand-off among them. A ``phased`` stream or staged
    fusion runs one sequence per phase in its configuration, not one for all
    (``compose.fused_configuration``), so its phases take the shim's channels in
    turn, as a packing's members do.

    An edge between two steps that are not adjacent in ``steps`` is only
    valid where every step between them (by index) is also a member; a
    stream or staged fusion's edges run forward, producer before consumer.
    """

    kind: FusionKind
    steps: tuple[int, ...]
    edges: tuple[Edge, ...] = ()
    phased: bool = False

    def __post_init__(self) -> None:
        if len(self.steps) < 2:
            raise ValueError("a fusion needs at least two steps")
        if self.phased and self.kind not in (FusionKind.STREAM, FusionKind.STAGED):
            raise ValueError(f"a {self.kind.value} fusion has no phases to run apart")
        if list(self.steps) != sorted(set(self.steps)):
            raise ValueError(
                f"fusion steps {self.steps} must be increasing and distinct"
            )
        if self.kind in (FusionKind.PACK, FusionKind.MERGE) and self.edges:
            raise ValueError(f"a {self.kind.value} fusion takes no edges")
        members = set(self.steps)
        fed: set[tuple[int, str]] = set()
        for edge in self.edges:
            if edge.producer == edge.consumer:
                raise ValueError(f"{edge} feeds a step from itself")
            if (
                self.kind in (FusionKind.STREAM, FusionKind.STAGED)
                and edge.producer >= edge.consumer
            ):
                raise ValueError(
                    f"a {self.kind.value} fusion's edges run forward; {edge} does not"
                )
            if edge.producer not in members or edge.consumer not in members:
                raise ValueError(f"{edge} names a step outside {self.steps}")
            lo, hi = sorted((edge.producer, edge.consumer))
            if not set(range(lo, hi + 1)) <= members:
                raise ValueError(f"{edge} skips a step between {lo} and {hi} not in it")
            if (edge.consumer, edge.input) in fed:
                raise ValueError(
                    f"step {edge.consumer}'s input {edge.input!r} is fed twice"
                )
            fed.add((edge.consumer, edge.input))

    @property
    def local_edges(self) -> tuple[tuple[int, str, int, str], ...]:
        """Each edge as ``(producer, output, consumer, input)``, its steps by their place in ``steps``."""
        return tuple(
            (
                self.steps.index(e.producer),
                e.output,
                self.steps.index(e.consumer),
                e.input,
            )
            for e in self.edges
        )

    @staticmethod
    def dispatches(
        fusions: Sequence[Fusion], n: int
    ) -> Iterator[tuple[int, Fusion | None]]:
        """Each dispatch of ``n`` steps run with ``fusions``: its first step, and its fusion or None for a step alone."""
        starts = {fusion.steps[0]: fusion for fusion in fusions}
        i = 0
        while i < n:
            fusion = starts.get(i)
            yield i, fusion
            i = i + 1 if fusion is None else fusion.steps[-1] + 1

    def host_refs(self, steps: Sequence[SequenceStep]) -> tuple[BufferRef, ...]:
        """Its members' buffers in ``steps`` the host sees, in member order: all but those an edge feeds on-chip."""
        elided = {(e.producer, e.output) for e in self.edges} | {
            (e.consumer, e.input) for e in self.edges
        }
        return tuple(
            ref
            for j in self.steps
            for ref, b in zip(steps[j].buffers, steps[j].op.buffers)
            if (j, b.name) not in elided
        )

    def name(self, designs: Sequence[str]) -> str:
        """Return this fusion's device symbol, ``designs`` its members' design names.

        Content-named, so one hits the cache across processes, and distinct from any
        member's own, and a phased one's from its members unphased. Wiring is spelled by
        each member's place in the fusion, not in the sequence, so one recurring down a
        model shares a symbol.
        """
        wiring = ",".join(f"{p}:{o}>{c}:{i}" for p, o, c, i in self.local_edges)
        kind = f"{self.kind.value}/phased" if self.phased else self.kind.value
        digest = hashlib.sha256(
            f"{kind}[{'|'.join(designs)}]({wiring})".encode()
        ).hexdigest()[:8]
        return f"fusion{len(designs)}_{digest}"


@dataclass(frozen=True)
class SequenceStep:
    """One step: an operator, and where each of its declared buffers is."""

    op: Operator
    buffers: tuple[BufferRef, ...]

    def roots(self) -> tuple[list[str], list[str]]:
        """Return the buffer roots this step fills and those it drains, a root once per buffer naming it."""
        reads: list[str] = []
        writes: list[str] = []
        for ref, b in zip(self.buffers, self.op.buffers):
            if b.fills:
                reads.append(ref.root)
            if b.drains:
                writes.append(ref.root)
        return reads, writes
