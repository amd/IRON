# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Static memory planning for a recorded runlist.

``LiveRange.scan`` gives each buffer the steps it must stay resident for;
``Pool.place`` gives each a byte offset, sharing bytes between buffers whose
lifetimes do not overlap (greedy by size, best fit: Algorithm 3 of Pisarchyk
& Lee, MLSys 2020). ``ArenaPlan`` shares one arena between the images of a
graph: residents (weights, states) keep one offset in every image, and each
image's transients are planned around them.
"""

from collections.abc import Hashable, Iterable, Mapping, Sequence
from dataclasses import dataclass

from aie.utils.hostruntime.tensor_class import COHERENCE_GRANULE

# Two buffers sharing a coherence granule cannot be synced independently
# (XRTTensor.subview refuses such a view); 64 bytes is also the shim's DDR burst.
ALIGNMENT = max(64, COHERENCE_GRANULE)


# (reads, writes) buffer names of one step, in execution order.
Steps = Sequence[tuple[Sequence[str], Sequence[str]]]


@dataclass(frozen=True)
class LiveRange:
    """Steps ``[begin, end]`` (inclusive) over which a buffer must be resident."""

    begin: int
    end: int

    def overlaps(self, other: "LiveRange") -> bool:
        return self.begin <= other.end and other.begin <= self.end

    @classmethod
    def scan(cls, steps: Steps, pinned=()) -> dict[str, "LiveRange"]:
        """Every poolable buffer's range, from its first write to its last read.

        A buffer read before it is written is an input and one never read is an
        output; like ``pinned``, neither is pooled.
        """
        first_write, last_read, first_read = {}, {}, {}
        for step, (reads, writes) in enumerate(steps):
            for n in reads:
                last_read[n] = step
                first_read.setdefault(n, step)
            for n in writes:
                first_write.setdefault(n, step)

        ranges = {}
        for name, begin in first_write.items():
            if name in pinned:
                continue
            if first_read.get(name, begin) < begin:
                continue
            if name not in last_read:
                continue
            ranges[name] = cls(begin, last_read[name])
        return ranges

    @classmethod
    def touching(cls, steps: Steps, names: Iterable[str]) -> dict[str, "LiveRange"]:
        """Each of ``names`` live from the first step that touches it to the last.

        For an arena whose host-visible buffers live elsewhere, so nothing in
        ``names`` is pinned. A name no step touches is live for the whole run.
        """
        wanted = set(names)
        first, last = {}, {}
        n_steps = 0
        for step, (reads, writes) in enumerate(steps):
            n_steps = step + 1
            for n in (*reads, *writes):
                if n in wanted:
                    first.setdefault(n, step)
                    last[n] = step
        whole = cls(0, max(n_steps - 1, 0))
        return {
            n: cls(first[n], last[n]) if n in first else whole for n in sorted(wanted)
        }

    @staticmethod
    def peak(ranges: Mapping[str, "LiveRange"], sizes: Mapping[str, int]) -> int:
        """Total bytes simultaneously live at the worst step: the lower bound."""
        if not ranges:
            return 0
        events = []
        for name, r in ranges.items():
            events.append((r.begin, sizes[name]))
            events.append((r.end + 1, -sizes[name]))
        peak = cur = 0
        for _, delta in sorted(events):
            cur += delta
            peak = max(peak, cur)
        return peak


@dataclass(frozen=True)
class Allocation:
    name: str
    offset: int
    size: int

    @property
    def end(self) -> int:
        return self.offset + self.size

    def overlaps(self, other: "Allocation") -> bool:
        return self.offset < other.end and other.offset < self.end


class Pool:
    """Byte offsets in one pool, each a multiple of ``alignment``."""

    def __init__(self, alignment: int = 64):
        self.alignment = alignment

    def align(self, x: int) -> int:
        return -(-x // self.alignment) * self.alignment

    def place(self, ranges, sizes, fixed: Iterable[Allocation] = ()):
        """Assign pool offsets, largest buffer first, each in the tightest gap
        that clears every placed buffer whose lifetime overlaps its own.

        Args:
            ranges: Each buffer's `LiveRange`.
            sizes: Each buffer's bytes.
            fixed: Allocations made earlier, occupied at every step.

        Returns:
            `(allocations, pool_bytes)`: each buffer's `Allocation`, and the
            highest byte any of them reaches (0 if there are none).
        """
        fixed = list(fixed)
        placed: list[tuple[Allocation, LiveRange]] = []
        order = sorted(ranges, key=lambda n: (-sizes[n], ranges[n].begin, n))

        for name in order:
            rng, size = ranges[name], sizes[name]
            obstacles = sorted(
                [*fixed, *(a for a, r in placed if r.overlaps(rng))],
                key=lambda a: a.offset,
            )
            cursor, best, best_gap = 0, None, None
            for ob in obstacles:
                gap = ob.offset - cursor
                if gap >= size and (best_gap is None or gap < best_gap):
                    best, best_gap = cursor, gap
                # A running max: a tall buffer can span several short ones.
                cursor = max(cursor, self.align(ob.end))
            offset = cursor if best is None else best
            placed.append((Allocation(name, offset, size), rng))

        allocations = {a.name: a for a, _ in placed}
        pool_bytes = max((a.end for a in allocations.values()), default=0)
        return allocations, pool_bytes


class ArenaPlan(Pool):
    """One scratch arena, shared by every image placed in it.

    A resident (keyed by its storage) has one offset in every image; a
    transient lives within one run of one image and may reuse another image's
    transients' bytes. An image bakes its offsets into its instruction
    stream, so nothing placed moves: a later image's new residents go above
    everything placed so far, and the arena only grows.
    """

    def __init__(self, alignment: int = 64):
        super().__init__(alignment)
        self._residents: dict[Hashable, Allocation] = {}
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    @property
    def residents(self) -> Mapping[Hashable, Allocation]:
        return dict(self._residents)

    def place_image(
        self,
        steps: Steps,
        sizes: Mapping[str, int],
        residents: Mapping[str, Hashable],
    ) -> dict[str, Allocation]:
        """Place one image's scratch buffers.

        Args:
            steps: The image's `(reads, writes)` per step.
            sizes: Every buffer the image keeps in the arena.
            residents: Which of them are residents, by storage key.

        Returns:
            Each buffer's `Allocation`.
        """
        unknown = set(residents) - set(sizes)
        if unknown:
            raise ValueError(f"residents {sorted(unknown)} have no size")
        result = {}
        for name, key in residents.items():
            size = sizes[name]
            held = self._residents.get(key)
            if held is None:
                held = Allocation(name, self.align(self._size), size)
                self._residents[key] = held
                self._size = held.end
            elif held.size != size:
                raise ValueError(
                    f"resident {name!r} is {size} bytes here, but its storage was "
                    f"placed as {held.name!r} with {held.size}; one storage is one "
                    f"size in every image"
                )
            result[name] = Allocation(name, held.offset, size)
        ranges = LiveRange.touching(steps, (n for n in sizes if n not in residents))
        transients, top = self.place(ranges, sizes, fixed=self._residents.values())
        self._size = max(self._size, top)
        result.update(transients)
        return result
