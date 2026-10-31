# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a tune decides before it searches: the planner's seed, the
transforms whose legality is a fact of the graph and its weights rather
than a timing, checked end to end before the search starts from them; and
which searches the survey says pay.
"""

from __future__ import annotations

import dataclasses
from collections.abc import Callable, Hashable, Sequence

from iron.common.declare import Profile

from .autotune import Shape, Timed, coding_tunables, replacing
from .packings import MIN_SWITCH_SHARE
from .survey import Survey

# A fold search runs where the steps folds remove are this share of a
# version, or this long: an untuned version's share understates them.
FOLD_SHARE = 0.01
FOLD_US = 1000.0


def coded_seed(
    record: Callable[[Profile], Sequence[Timed]],
    dev,
    profile: Profile,
    log: Callable[[str], None] = print,
) -> Profile:
    """``profile`` with every input a tunable can code coded wherever its
    array codes whole: a shape is coded only where every array its steps
    share with other shapes (``array_key`` as ``profile`` runs them) holds
    shapes that all record coded and whose coded weights all fit their
    rows' capacity (``Recording.code_weights``). Coding part of an array
    would split it into a coded and a plain one, more cores than it fits.
    """
    calls = record(profile)
    resolved = [s.op.resolved(dev) for c in calls for s in c.recording.steps]
    shapes: dict[Hashable, Shape] = {}
    flags: dict[Hashable, set[str]] = {}
    arrays: dict[Hashable, set[Hashable]] = {}
    for call in calls:
        for step in call.recording.steps:
            names = coding_tunables(step.op)
            if not names:
                continue
            shape = Shape(step.op)
            shapes.setdefault(shape.key, shape)
            flags.setdefault(shape.key, set()).update(names)
            arrays.setdefault(step.op.resolved(dev).array_key(), set()).add(shape.key)

    def coded(keys) -> Profile:
        out, covering, held = replacing(profile, [shapes[k] for k in keys])
        for k in keys:
            given = {**held[k], **dict.fromkeys(flags[k], True)}
            dims = shapes[k].entry(covering[k], frozenset(), resolved)
            out.add(shapes[k].cls, **dims, **given)
        for fusion in profile.fusions():
            out.add_fusion(*fusion)
        for packing in profile.packings():
            out.add_packing(packing.members, packing.versions)
        return out

    legal = set()
    for key, shape in shapes.items():
        try:
            for call in record(coded([key])):
                for step in call.recording.steps:
                    if Shape(step.op).key == key:
                        step.op.resolved(dev)
        except (TypeError, ValueError) as e:
            log(f"coded: {shape} records only plain: {e}")
            continue
        legal.add(key)
    fits = set(legal)
    for call in record(coded(legal)):
        recording = call.recording
        recording.code_weights()
        refused = set(recording.read_plain)
        for step in recording.steps:
            if any(h.ref().root in refused for h in step.slots):
                fits.discard(Shape(step.op).key)
    for key in legal - fits:
        log(f"coded: {shapes[key]} has a weight past its rows' capacity")
    taken = set(fits)
    mixed = [m for m in arrays.values() if m & taken and not m <= taken]
    while mixed:
        for key in mixed[0] & taken:
            log(f"coded: {shapes[key]} shares an array with a shape kept plain")
        taken -= mixed[0]
        mixed = [m for m in arrays.values() if m & taken and not m <= taken]
    for key in taken:
        log(f"coded: {shapes[key]}")
    return coded(taken) if taken else profile


@dataclasses.dataclass(frozen=True)
class Search:
    """One search a tune may run, whether the plan runs it, and why."""

    name: str
    runs: bool
    why: str


def searches(surveys: Sequence[Survey], full_elf: bool) -> list[Search]:
    """Which searches pay for their device time, from each version's
    survey: packing where a version's switches cost ``MIN_SWITCH_SHARE`` of
    its steps; folds where the steps they remove are ``FOLD_SHARE`` of one,
    or ``FOLD_US``;
    fusions only on an xclbin per step, where a merge is the one way to run
    two steps as one dispatch (a full ELF's packing removes the switches
    they would, and a fusion splits the arrays a packing groups).
    """
    packing = [
        s.name
        for s in surveys
        if s.estimates["packing"].us >= MIN_SWITCH_SHARE * s.steps_us
    ]
    folds = [
        s.name
        for s in surveys
        if s.estimates["folds"].us
        >= min(FOLD_US, FOLD_SHARE * (s.steps_us + s.switch_us))
    ]
    return [
        Search(
            "packing",
            full_elf and bool(packing),
            (
                "an xclbin per step packs nothing"
                if not full_elf
                else f"switches cost at least {MIN_SWITCH_SHARE:.0%} of the steps "
                f"in {packing or 'no version'}"
            ),
        ),
        Search(
            "folds",
            bool(folds),
            f"removable steps are {FOLD_SHARE:.0%} or {FOLD_US / 1000:.0f} ms of "
            f"{folds or 'no version'}",
        ),
        Search(
            "fusions",
            not full_elf,
            (
                "a full ELF's packing removes the switches a fusion would"
                if full_elf
                else "a merge is an xclbin's one way to run steps as one dispatch"
            ),
        ),
    ]
