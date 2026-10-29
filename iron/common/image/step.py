# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A step of a sequence, and where its buffers are in the image's."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from enum import Enum

from ..declare import Operator


@dataclass(frozen=True)
class BufferRef:
    """Where a step's buffer is: ``nbytes`` bytes of the image's buffer
    ``root`` from byte ``start``, or all of it where ``nbytes`` is None.
    """

    root: str
    start: int = 0
    nbytes: int | None = None

    def place(self, layout: Mapping[str, tuple[str, int, int]]) -> tuple[str, int, int]:
        """Where this is, ``layout`` placing each buffer: its ``(argument
        kind, byte offset, bytes)``.
        """
        kind, offset, nbytes = layout[self.root]
        return kind, offset + self.start, nbytes if self.nbytes is None else self.nbytes

    def __str__(self) -> str:
        if self.nbytes is None:
            return self.root
        return f"{self.root}[{self.start}:{self.start + self.nbytes}]"


class FusionKind(Enum):
    """How a fusion's steps run as one device configuration. ``STREAM``
    (consecutive steps, each edge a fifo its lanes meet directly),
    ``STAGED`` (as a stream, an edge whose lanes do not meet restaged
    through memtiles), ``PACK`` (independent steps co-resident, issued
    concurrently) and ``MERGE`` (consecutive steps sharing a configuration,
    run back to back with no edge) build today; ``FOLD`` (an in-core fold)
    is not yet built.
    """

    STREAM = "stream"
    STAGED = "staged"
    FOLD = "fold"
    PACK = "pack"
    MERGE = "merge"


@dataclass(frozen=True)
class Edge:
    """Step ``producer``'s output ``output`` streamed on-chip into step
    ``consumer``'s input ``input``, both indices into one ``Fusion``'s
    ``steps``; several edges may share one ``(producer, output)``, fanning
    out to more than one consumer.
    """

    producer: int
    output: str
    consumer: int
    input: str


@dataclass(frozen=True)
class Fusion:
    """A set of steps that build and dispatch as one device configuration,
    with no host transfer between: ``kind`` how, ``steps`` its members
    (increasing, distinct indices into a sequence) and ``edges`` each
    on-chip hand-off among them.

    An edge between two steps that are not adjacent in ``steps`` is only
    valid where every step between them (by index) is also a member; a
    stream or staged fusion's edges run forward, producer before consumer.
    """

    kind: FusionKind
    steps: tuple[int, ...]
    edges: tuple[Edge, ...] = ()

    def __post_init__(self) -> None:
        if len(self.steps) < 2:
            raise ValueError("a fusion needs at least two steps")
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


@dataclass(frozen=True)
class SequenceStep:
    """One step: an operator, and where each of its declared buffers is."""

    op: Operator
    buffers: tuple[BufferRef, ...]
