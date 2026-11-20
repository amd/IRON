# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the transformation tests share.

The marks for a type IRON does not build yet and for one that waits on a
kernel, and reaching a region by composing ``candidates``' edits.
"""

import itertools
from collections.abc import Sequence

import pytest
from aie.iron.device import Device

from iron.common.declare import Profile
from iron.common.declare.composition import Hold, Region
from iron.common.image.step import EdgeKind
from iron.tune.autotune import Timed
from iron.tune.search import AddEntry, DepthEdge, HoldEdge, candidates

unbuilt = pytest.mark.xfail(
    strict=True,
    raises=NotImplementedError,
    reason="not built yet: the composition contract's stubs raise",
)

waits_on_a_kernel = pytest.mark.xfail(
    strict=True,
    raises=ValueError,
    reason="waits on a kernel mlir-aie does not have yet (PLAN step 3): the "
    "operators refuse the shape or type it needs",
)


def _holds_reaching(start: Region, target: Region) -> list[tuple[int, Hold]]:
    """Return a hold for each edge, last first, that takes ``start`` to ``target`` (``Region.held``), skipping an edge whose hold changes nothing.

    Each edge's place is read off its namesake in ``target``: none there a
    ``MEMORY`` hold, a stream whose steps share a worker there ``L1``, a
    staged edge ``MEMTILE`` (or ``LATER_PHASE``, where ``target`` chooses
    phases), a DDR edge ``DDR``. Last first: a ``MEMORY`` hold drops
    its edge, moving those after it down.
    """
    at = {
        (e.producer, e.output, e.consumer, e.input): i
        for i, e in enumerate(target.edges)
    }
    options: list[tuple[Hold | None, ...]] = []
    for edge in start.edges:
        i = at.get((edge.producer, edge.output, edge.consumer, edge.input))
        if i is None:
            options.append((Hold.MEMORY,))
            continue
        kind = target.edges[i].kind
        if kind is EdgeKind.STREAM:
            options.append(
                (Hold.L1,)
                if any({edge.producer, edge.consumer} <= set(g) for g in target.workers)
                else (None,)
            )
        elif kind is EdgeKind.STAGED:
            options.append(
                (Hold.MEMTILE, Hold.LATER_PHASE)
                if target.phases is not None
                else (Hold.MEMTILE,)
            )
        elif kind is EdgeKind.DDR:
            options.append((Hold.DDR,))
        else:
            options.append((None,))
    for choice in itertools.product(*options):
        region, steps = start, []
        for index, place in reversed(list(enumerate(choice))):
            if place is not None and region.held(index, place) != region:
                region = region.held(index, place)
                steps.append((index, place))
        if region == target:
            return steps
    raise NotImplementedError(
        f"candidates proposes no holds taking {start} to {target}"
    )


def reached_by_candidates(
    region: Region, calls: Sequence[Timed], device: Device
) -> Profile:
    """Return the profile composing ``candidates``' edits reaches toward ``region``.

    First the plain region edit of ``region``'s members (no shared workers,
    one phase), every hand-off an edge of the analysis's kind; then one
    edge's hold at a time, then one edge's chosen depth at a time, each an
    edit ``candidates`` yields for the profile as it then stands.
    ``candidates`` raises where it yields no such edit.
    """
    reached = Profile()
    for edit in candidates(calls, reached, device):
        if (
            isinstance(edit, AddEntry)
            and isinstance(edit.entry.root, Region)
            and edit.entry.root.parts == region.parts
            and not edit.entry.root.workers
            and edit.entry.root.phases is None
        ):
            reached = edit.apply(reached)
            break
    (current,) = reached.entries()
    assert isinstance(current.root, Region)
    shallow = region
    for index in range(len(region.edges)):
        shallow = shallow.deepened(index, None)
    for index, place in _holds_reaching(current.root, shallow):
        for edit in candidates(calls, reached, device):
            if (
                isinstance(edit, HoldEdge)
                and edit.entry == current
                and (edit.index, edit.place) == (index, place)
            ):
                reached = edit.apply(reached)
                break
        (current,) = reached.entries()
    for index, edge in enumerate(region.edges):
        if edge.depth is None:
            continue
        for edit in candidates(calls, reached, device):
            if (
                isinstance(edit, DepthEdge)
                and edit.entry == current
                and (edit.index, edit.depth) == (index, edge.depth)
            ):
                reached = edit.apply(reached)
                break
        (current,) = reached.entries()
    return reached
