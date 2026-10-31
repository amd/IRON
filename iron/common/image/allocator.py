# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Static memory planning for a recorded runlist.

``Pool.place`` shares bytes between buffers whose ``LiveRange``s do not overlap
(greedy by size, best fit: Algorithm 3 of Pisarchyk & Lee, MLSys 2020), in
``BANK``-byte banks no buffer crosses; ``ArenaPlan`` shares an arena across images.
"""

from collections.abc import Hashable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from typing import NamedTuple

from aie.utils.hostruntime.tensor_class import COHERENCE_GRANULE

# Two buffers sharing a coherence granule cannot be synced independently
# (XRTTensor.subview refuses such a view); 64 bytes is also the shim's DDR burst.
ALIGNMENT = max(64, COHERENCE_GRANULE)

# 3.5 GiB: under a 4 GB `ulimit -l` and the addend's 4 GiB.
BANK = 7 << 29


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
        """Return every poolable buffer's range, from its first write to its last read.

        Not ``pinned``, nor read before written (an input), nor never
        read (an output).
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
        """Return each of ``names`` live from the first step that touches it to the last.

        Or the whole run if none does; for an arena, so none is pinned.
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
    """Byte offsets in one pool, each a multiple of ``alignment``.

    Each buffer is within one bank of ``bank`` bytes (with ``None``,
    one bank).
    """

    def __init__(self, alignment: int = 64, bank: int | None = BANK):
        self.alignment = alignment
        self.bank = bank

    def align(self, x: int) -> int:
        return -(-x // self.alignment) * self.alignment

    def fit(self, offset: int, size: int) -> int:
        """Return the first aligned offset from ``offset`` at which ``size`` bytes stay in one bank.

        A ``size`` over a bank raises ``ValueError``.
        """
        offset = self.align(offset)
        if self.bank is None:
            return offset
        if size > self.bank:
            raise ValueError(f"{size} bytes do not fit a {self.bank}-byte bank")
        if offset // self.bank != (offset + size - 1) // self.bank:
            return -(-offset // self.bank) * self.bank
        return offset

    def place(self, ranges, sizes, fixed: Iterable[Allocation] = ()):
        """Place each of ``ranges`` largest first, in the tightest gap clear of ``fixed``.

        Clear too of the buffers it is live with; returns them and the
        top byte.
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
                at = self.fit(cursor, size)
                gap = ob.offset - at
                if gap >= size and (best_gap is None or gap < best_gap):
                    best, best_gap = at, gap
                # A running max: a tall buffer can span several short ones.
                cursor = max(cursor, self.align(ob.end))
            offset = self.fit(cursor, size) if best is None else best
            placed.append((Allocation(name, offset, size), rng))

        allocations = {a.name: a for a, _ in placed}
        pool_bytes = max((a.end for a in allocations.values()), default=0)
        return allocations, pool_bytes


class ArenaPlan(Pool):
    """One scratch arena shared by images.

    A resident keeps one offset in all of them, a transient may reuse
    other images' transients, and nothing placed moves.
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
        """Place one image's arena buffers, ``sizes``.

        ``residents`` maps those that are residents to their storage key.
        """
        unknown = set(residents) - set(sizes)
        if unknown:
            raise ValueError(f"residents {sorted(unknown)} have no size")
        result = {}
        for name, key in residents.items():
            size = sizes[name]
            held = self._residents.get(key)
            if held is None:
                held = Allocation(name, self.fit(self._size, size), size)
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


class ArgumentSizes(NamedTuple):
    """Bytes of each runtime-sequence argument of a full ELF.

    ``feedback`` is None where there is none; the scratch arena is
    passed as one argument per bank.
    """

    input: int
    output: int
    scratch: int
    feedback: int | None = None

    @property
    def bank_kinds(self) -> list[str]:
        """Return the scratch arena's arguments, a bank each.

        ``scratch``, then ``scratch_1`` on.
        """
        banks = max(1, -(-self.scratch // BANK))
        return ["scratch", *(f"scratch_{k}" for k in range(1, banks))]

    def arguments(self) -> dict[str, int]:
        """Size by kind, in argument order."""
        kinds = self.bank_kinds
        banks = [min(BANK, self.scratch - k * BANK) for k in range(len(kinds))]
        sizes = {"input": self.input, "output": self.output, "scratch": banks[0]}
        if self.feedback is not None:
            sizes["feedback"] = self.feedback
        sizes.update(zip(kinds[1:], banks[1:]))
        return sizes

    def scratch_argument(self, offset: int, length: int) -> tuple[str, int]:
        """Return the bank argument a scratch buffer of ``length`` bytes at ``offset`` is in.

        And its offset there; one crossing banks raises ``ValueError``.
        """
        k = offset // BANK
        if length and (offset + length - 1) // BANK != k:
            raise ValueError(
                f"a scratch buffer of {length} bytes at {offset} crosses from "
                f"bank {k} into the next, of {BANK} bytes each"
            )
        return self.bank_kinds[k], offset - k * BANK


def lay_out(
    sizes: Mapping[str, int],
    steps: Steps,
    host: tuple[Sequence[str], Sequence[str], Sequence[str]],
    pinned: Iterable[str],
    arena: Mapping[str, Allocation],
) -> tuple[dict[str, tuple[str, int, int]], ArgumentSizes]:
    """Return each buffer's ``(argument kind, byte offset, bytes)`` and each argument's bytes.

    Intermediates share bytes, ``host`` and ``pinned`` buffers never do.
    """
    inputs, outputs, feedback = host
    held = {*inputs, *outputs, *feedback, *pinned}
    ranges = LiveRange.scan(steps, pinned=held)
    layout: dict[str, tuple[str, int, int]] = {}

    def place(kind: str, roots: Sequence[str]) -> int:
        end = 0
        for root, a in arena.items():
            if root in roots:
                layout[root] = (kind, a.offset, a.size)
                end = max(end, a.end)
        roots = [r for r in roots if r not in arena]
        # The caller binds its own memory to the feedback argument: offsets are the contract.
        offsets = {}
        if kind != "feedback":
            mine = {r: ranges[r] for r in roots if r in ranges}
            allocations, _ = Pool(ALIGNMENT).place(mine, sizes)
            offsets = {name: a.offset for name, a in allocations.items()}
        # A host-visible kind is one buffer object, not banks.
        pool = Pool(ALIGNMENT, BANK if kind == "scratch" else None)
        cursor = 0
        pooled = []
        for root in roots:
            if root in offsets:
                pooled.append(root)
                continue
            cursor = pool.fit(cursor, sizes[root])
            layout[root] = (kind, cursor, sizes[root])
            end = max(end, cursor + sizes[root])
            cursor = pool.align(cursor + sizes[root])
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

    hosted = {*inputs, *outputs, *feedback}
    return layout, ArgumentSizes(
        place("input", inputs),
        place("output", outputs),
        place("scratch", [r for r in sizes if r not in hosted]),
        place("feedback", feedback) if feedback else None,
    )
