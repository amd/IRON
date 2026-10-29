# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Applying a taken fusion's own per-step tunables (``Profile.add_fusion``,
``Profile.fusion_tunables``) to the steps it covers: a profile matches a
shape by its dims alone, so a step inside a fusion that needs tunables
different from the same shape unfused can only say so here, not by moving
the shape's own entry.
"""

from __future__ import annotations

import dataclasses
from collections.abc import Mapping, Sequence
from typing import Any

from ..declare import Profile
from ..image.step import Fusion
from .record import Recording


def apply(
    recording: Recording, profile: Profile, fused: Sequence[Fusion], dev
) -> Recording:
    """``recording`` with every step inside a fusion in ``fused`` rebuilt at
    the tunables its profile entry gives it (``Profile.fusion_tunables``,
    matched the way ``iron.common.graph.fusion.fusions`` matches a fusion
    itself); a step whose entry gives none, or whose fusion matches no
    entry, is untouched.
    """
    given: dict[int, Mapping[str, Any]] = {}
    for fusion in fused:
        ops = [recording.steps[i].op.resolved(dev) for i in fusion.steps]
        local = {step: i for i, step in enumerate(fusion.steps)}
        edges = tuple(
            (local[e.producer], e.output, local[e.consumer], e.input)
            for e in fusion.edges
        )
        tunables = profile.fusion_tunables(fusion.kind, ops, edges)
        if tunables is None:
            continue
        given.update((i, t) for i, t in zip(fusion.steps, tunables) if t)
    return rebuild(recording, given, dev)


def rebuild(
    recording: Recording, tunables: Mapping[int, Mapping[str, Any]], dev
) -> Recording:
    """``recording`` with each step ``tunables`` names, by index, rebuilt at
    its tunables there, the per-call values bound to its operator bound to
    the rebuilt one.
    """
    steps = list(recording.steps)
    rebuilt: dict[int, list] = {}
    for i, t in tunables.items():
        op = recording.steps[i].op.resolved(dev)
        narrowed = op._with_tunables(**t).resolved(dev)
        rebuilt.setdefault(id(recording.steps[i].op), []).append(narrowed)
        steps[i] = dataclasses.replace(steps[i], op=narrowed)
    if not rebuilt:
        return recording
    # A narrowed design reads its own value symbols, so each per-call value
    # bound to the step's operator is bound to its narrowed one instead.
    kept = {id(s.op) for s in steps}
    bindings = []
    for b in recording.bindings:
        if id(b.op) in kept:
            bindings.append(b)
        for narrowed in rebuilt.get(id(b.op), ()):
            bindings.append(
                dataclasses.replace(
                    b, op=narrowed, member=narrowed.value(b.member.name)
                )
            )
    return dataclasses.replace(recording, steps=steps, bindings=bindings)
