# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Static memory planning for a recorded runlist.

A recorded graph names every intermediate it produces, so a model that runs
the same block 16 times asks for 16 copies of each scratch buffer. Sized for
Llama-3.2-1B that is over 100 MB of duplicates. Today the model author avoids
it by hand: reusing one pinned name per scratch slot, everywhere, forever.

That is a register allocator written by hand, so write the allocator instead.
Two passes over the runlist:

1. :func:`live_ranges` -- one linear scan giving each buffer the half-open
   step interval ``[first_write, last_read]`` it must stay resident for.
2. :func:`place` -- assign each a byte offset in one pool, letting buffers
   whose lifetimes do not overlap share addresses.

This is Dynamic Storage Allocation: rectangles of fixed width (lifetime) and
height (bytes), slid vertically only, packed into a minimum-height strip. It
is NP-complete (Garey & Johnson, problem SR2; Stockmeyer 1976), and the best
known general approximation is (2+eps) of peak-liveness (Buchsbaum, Karloff,
Kenyon, Reingold & Thorup, STOC 2003) -- who also show a family forcing a 25%
gap, so matching the bound is not always possible.

In practice the simple heuristic is excellent. Greedy-by-size with best-fit
placement is Algorithm 3 of Pisarchyk & Lee, "Efficient Memory Management for
Deep Neural Net Inference" (MLSys 2020, arXiv:2001.03288), which they measured
hitting the lower bound *exactly* on five of six production networks. It is
what TensorFlow Lite ships (``SimpleMemoryArena::Allocate``) and what
TorchInductor's pooled planner approximates (``allocate_groups`` sorts
intermediates largest-first).

Buffers the host addresses by name -- weights, KV caches, the sequence's own
inputs and outputs -- are *pinned*: they need private, stable addresses, so
they are never pooled. TorchInductor keeps the same exclusion list in
``can_reuse``: graph inputs, constants, and explicitly never-reused buffers.

:class:`ArenaPlan` carries this across images. One graph function compiled
for several input shapes is several images, and one runs at a time, so they
can share a single scratch arena: *residents* (weights, states) get one
offset, the same in every image, and each image's *transients* are planned
around them, free to reuse the bytes of any other image's transients.
"""

from collections.abc import Hashable, Iterable, Mapping, Sequence
from dataclasses import dataclass

# (reads, writes) buffer names of one step, in execution order.
Steps = Sequence[tuple[Sequence[str], Sequence[str]]]


def align_up(x: int, alignment: int) -> int:
    return (x + alignment - 1) // alignment * alignment


@dataclass(frozen=True)
class LiveRange:
    """Steps ``[begin, end]`` (inclusive) over which a buffer must be resident."""

    begin: int
    end: int

    def overlaps(self, other: "LiveRange") -> bool:
        return self.begin <= other.end and other.begin <= self.end


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


def live_ranges(steps, pinned=()):
    """Map every poolable buffer to the step interval it must stay live for.

    ``steps`` is an iterable of ``(reads, writes)`` buffer names, in execution
    order. One linear scan suffices because that order is already total -- the
    same reason TorchInductor computes last-use with a single reverse scan in
    ``Scheduler.compute_last_usage`` rather than building a conflict graph.

    A buffer is live from its first write to its last read; a
    buffer that is read before it is ever written is an input, and one never
    read again is an output -- both are treated as pinned, since their
    contents outlive the sequence.
    """
    first_write, last_read, first_read = {}, {}, {}
    for step, (reads, writes) in enumerate(steps):
        for n in reads:
            last_read.setdefault(n, step)
            last_read[n] = step
            first_read.setdefault(n, step)
        for n in writes:
            first_write.setdefault(n, step)

    ranges = {}
    for name, begin in first_write.items():
        if name in pinned:
            continue
        # Read before ever written -> supplied by the host; not ours to pool.
        if first_read.get(name, begin) < begin:
            continue
        # Never read again -> an output the host reads back.
        if name not in last_read:
            continue
        ranges[name] = LiveRange(begin, last_read[name])
    return ranges


def touch_ranges(steps: Steps, names: Iterable[str]) -> dict[str, LiveRange]:
    """Each of ``names`` live from the first step that touches it to the last.

    The planning rule for an arena whose host-visible buffers live elsewhere:
    nothing in ``names`` outlives the run, so none is pinned for being read
    first or never read. A write nobody reads still needs its bytes for the
    step that writes it; a read before any write sees whatever was there, and
    is only kept from being overwritten during its own span. A name no step
    touches is resident for the whole run -- it has a size but no uses, and
    the conservative reading of that is "always".
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
    whole = LiveRange(0, max(n_steps - 1, 0))
    return {
        n: LiveRange(first[n], last[n]) if n in first else whole for n in sorted(wanted)
    }


def place(ranges, sizes, alignment=64, fixed: Iterable[Allocation] = ()):
    """Assign pool offsets. Returns ``(allocations, pool_bytes)``.

    Greedy by size descending; each buffer takes the lowest offset that clears
    every already-placed buffer whose lifetime overlaps its own (best fit --
    the tightest such gap). Buffers with disjoint lifetimes are invisible to
    one another, and that is exactly where the reuse comes from.

    Every offset is a multiple of ``alignment``. ``fixed`` are allocations
    made earlier that stay where they are and occupy their bytes at every
    step; nothing is placed over them. ``pool_bytes`` is the highest byte any
    allocation of this call reaches, zero if there are none.
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
            # Placed buffers nest, so the skyline is a running max, not an
            # assignment: a tall buffer can span several short ones. Getting
            # this wrong is the classic bug -- cf. TFLite's arena planner and
            # TFLM's GreedyMemoryPlanner, which both take the max here.
            cursor = max(cursor, align_up(ob.end, alignment))
        offset = cursor if best is None else best
        placed.append((Allocation(name, offset, size), rng))

    allocations = {a.name: a for a, _ in placed}
    pool_bytes = max((a.end for a in allocations.values()), default=0)
    return allocations, pool_bytes


def peak_live_bytes(ranges, sizes):
    """Total bytes simultaneously live at the worst step: the lower bound.

    Known as LOAD in the Dynamic Storage Allocation literature (max weighted
    clique of the interval graph). No allocator can beat it, and greedy-by-size
    usually matches it, so it is the number to check a plan against. Computed
    as a difference array plus prefix sum, as TorchInductor's
    ``estimate_peak_memory`` does.
    """
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


class ArenaPlan:
    """One scratch arena, shared by every image placed in it.

    An image is one compiled version of a graph: the same function traced at
    another input shape is another image over the same weights and states.
    Only one image runs at a time, so they can share one arena:

    * A *resident* -- a weight, a state, anything the host addresses by what
      it is rather than by image -- is keyed by its storage and gets one
      offset for the life of the arena, the same in every image. It is
      uploaded once, and a state one image writes is where the next reads it.
    * A *transient* lives within one run of one image. Transients are planned
      per image around the residents, and may reuse the bytes of any other
      image's transients: those are dead whenever this image runs.

    Nothing placed ever moves, because an image bakes its offsets into its
    instruction stream. So an image added later puts its new residents above
    everything placed so far -- below, a transient of an earlier image could
    overwrite them -- and the arena only grows. Offsets are multiples of
    ``alignment``.
    """

    def __init__(self, alignment: int = 64):
        self.alignment = alignment
        self._residents: dict[Hashable, Allocation] = {}
        self._size = 0

    @property
    def size(self) -> int:
        """Bytes the arena needs to hold every image placed so far."""
        return self._size

    @property
    def residents(self) -> Mapping[Hashable, Allocation]:
        """Every resident placed so far, by storage key."""
        return dict(self._residents)

    def place_image(
        self,
        steps: Steps,
        sizes: Mapping[str, int],
        residents: Mapping[str, Hashable],
    ) -> dict[str, Allocation]:
        """Place one image's scratch buffers; return each one's allocation.

        ``sizes`` names every buffer the image keeps in the arena and
        ``residents`` which of them are residents, by storage key; the rest
        are transients, live over the steps (``(reads, writes)`` names each)
        that touch them.
        """
        unknown = set(residents) - set(sizes)
        if unknown:
            raise ValueError(f"residents {sorted(unknown)} have no size")
        result = {}
        for name, key in residents.items():
            size = sizes[name]
            held = self._residents.get(key)
            if held is None:
                held = Allocation(name, align_up(self._size, self.alignment), size)
                self._residents[key] = held
                self._size = held.end
            elif held.size != size:
                raise ValueError(
                    f"resident {name!r} is {size} bytes here, but its storage was "
                    f"placed as {held.name!r} with {held.size}; one storage is one "
                    f"size in every image"
                )
            result[name] = Allocation(name, held.offset, size)
        ranges = touch_ranges(steps, (n for n in sizes if n not in residents))
        transients, top = place(
            ranges, sizes, self.alignment, fixed=self._residents.values()
        )
        self._size = max(self._size, top)
        result.update(transients)
        return result
