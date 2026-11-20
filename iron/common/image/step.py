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


class EdgeKind(Enum):
    """The path an edge's objects take: a core-to-core ``STREAM``, ``STAGED`` through memtiles, ``DDR``, or the ``CASCADE``."""

    STREAM = "stream"
    STAGED = "staged"
    DDR = "ddr"
    CASCADE = "cascade"


class HandOff(Enum):
    """How a producer's lanes map onto a consumer's, as the dataflow analysis derives it."""

    EQUAL = "equal"
    JOIN = "join"
    SPLIT = "split"
    RATIO = "ratio"
    BROADCAST = "broadcast"
    SLICES = "slices"
    LAYOUT = "layout"


@dataclass(frozen=True)
class Edge:
    """Step ``producer``'s output ``output`` fed on-chip into step ``consumer``'s input ``input``.

    Indices name a region's steps depth-first through its nested regions, so
    an edge may join steps of different nested regions; it sits in the
    innermost region holding both. Several edges may share one
    ``(producer, output)``, fanning out to more than one consumer. An edge
    names only choices: the tokens, lanes, type and initial values it
    carries are the operators' and the recording's, which the dataflow
    analysis derives.

    Attributes:
        producer: The producing step.
        output: The producer's output.
        consumer: The consuming step.
        input: The consumer's input.
        kind: The path the objects take.
        depth: Objects in flight; None for the dataflow analysis's minimum.
    """

    producer: int
    output: str
    consumer: int
    input: str
    kind: EdgeKind = EdgeKind.STREAM
    depth: int | None = None

    @property
    def across_calls(self) -> bool:
        """Whether it carries what its producer writes into its consumer's next call: a self-loop, or a consumer earlier than its producer."""
        return self.consumer <= self.producer


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
    ``kept`` names each edge's ``(producer, output)`` whose buffer a step
    past the fusion or the host also reads: its drain to host is kept beside
    its on-chip readers (a tee). ``waits`` names each ``(producer, consumer)``
    of members where the consumer reads, in host memory, what the producer
    writes there (a DDR edge): a phased fusion runs the consumer a phase or
    more after the producer. ``workers`` names each group of members whose
    cores are one, in firing order: each lane's core runs the group's
    members' bodies in turn, the edges among them fifos within its tile.
    ``packets`` True sends its members' host fills as packet flows, sharing
    the shim's sending channels; False keeps them circuits; None leaves it to
    the placer: packets only where circuits run the channels short and packets
    place (``compose.transported``). ``drains`` above one joins each run of
    that many lanes of a member's output drained only to the host in a
    memtile into one host lane, taking fewer of the shim's receiving
    channels; 1 drains each lane on its own; None leaves it to the placer,
    as ``packets``.
    ``phases`` names each member's phase, in ``steps``' order, where they are
    chosen rather than derived (``compose.phases``).
    """

    kind: FusionKind
    steps: tuple[int, ...]
    edges: tuple[Edge, ...] = ()
    phased: bool = False
    kept: tuple[tuple[int, str], ...] = ()
    waits: tuple[tuple[int, int], ...] = ()
    workers: tuple[tuple[int, ...], ...] = ()
    packets: bool | None = None
    phases: tuple[int, ...] | None = None
    drains: int | None = None

    def __post_init__(self) -> None:
        if len(self.steps) < 2:
            raise ValueError("a fusion needs at least two steps")
        if self.phases is not None and (
            not self.phased or len(self.phases) != len(self.steps)
        ):
            raise ValueError(
                f"fusion {self.steps}: chosen phases {self.phases} name a phase "
                f"for each member of a phased fusion"
            )
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
        if self.drains is not None and self.drains < 1:
            raise ValueError(
                f"fusion {self.steps} joins drains in runs of {self.drains}; a run "
                f"is a lane or more"
            )
        if self.waits and not self.phased:
            raise ValueError(
                f"fusion {self.steps} waits on host memory, which only a phased "
                f"fusion's later phase can"
            )
        for producer, consumer in self.waits:
            if not (
                producer in members and consumer in members and producer < consumer
            ):
                raise ValueError(
                    f"wait ({producer}, {consumer}) is no forward pair of {self.steps}"
                )
        grouped = [s for group in self.workers for s in group]
        if self.workers and (
            self.kind is not FusionKind.STREAM
            or len(grouped) != len(set(grouped))
            or not set(grouped) <= members
            or any(len(group) < 2 for group in self.workers)
        ):
            raise ValueError(
                f"fusion {self.steps}: workers {self.workers} are not disjoint "
                f"groups of two or more of its members, in a stream fusion"
            )
        made = {(e.producer, e.output) for e in self.edges}
        for producer, output in self.kept:
            if (producer, output) not in made:
                raise ValueError(
                    f"kept ({producer}, {output!r}) is no edge's producer output"
                )

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
        """Its members' buffers in ``steps`` the host sees, in member order: all but those an edge feeds on-chip, a kept output included."""
        elided = {(e.producer, e.output) for e in self.edges} - set(self.kept) | {
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
        wiring += "".join(f"+{self.steps.index(p)}:{o}" for p, o in self.kept)
        wiring += "".join(
            f"#{self.steps.index(e.producer)}:{e.output}={e.depth}"
            for e in self.edges
            if e.depth is not None
        )
        wiring += "".join(
            f"~{self.steps.index(p)}>{self.steps.index(c)}" for p, c in self.waits
        )
        wiring += "".join(
            "@" + "+".join(str(self.steps.index(s)) for s in group)
            for group in self.workers
        )
        if self.phases is not None:
            wiring += "%" + ",".join(map(str, self.phases))
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
