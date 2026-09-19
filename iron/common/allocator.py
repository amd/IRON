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
2. :func:`plan` -- assign each a byte offset in one pool, letting buffers
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
"""

from dataclasses import dataclass


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


def plan(ranges, sizes, alignment=64):
    """Assign pool offsets. Returns ``(allocations, pool_bytes)``.

    Greedy by size descending; each buffer takes the lowest offset that clears
    every already-placed buffer whose lifetime overlaps its own (best fit --
    the tightest such gap). Buffers with disjoint lifetimes are invisible to
    one another, and that is exactly where the reuse comes from.
    """

    def align(x):
        return (x + alignment - 1) // alignment * alignment

    placed: list[tuple[Allocation, LiveRange]] = []
    order = sorted(ranges, key=lambda n: (-sizes[n], ranges[n].begin, n))

    for name in order:
        rng, size = ranges[name], sizes[name]
        obstacles = sorted(
            (a for a, r in placed if r.overlaps(rng)), key=lambda a: a.offset
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
            cursor = max(cursor, align(ob.offset + ob.size))
        offset = cursor if best is None else best
        placed.append((Allocation(name, offset, size), rng))

    allocations = {a.name: a for a, _ in placed}
    pool_bytes = max((a.offset + a.size for a in allocations.values()), default=0)
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
