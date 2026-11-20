# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Applying a taken fusion's own per-step tunables (``Profile.add_fusion``, ``Profile.fusion_tunables``) to the steps it covers.

A profile matches a shape by its dims alone, so a step inside a fusion that needs
tunables different from the same shape unfused can only say so here, not by moving the
shape's own entry.
"""

from __future__ import annotations

import dataclasses
from collections.abc import Mapping, Sequence
from typing import Any

from aie.utils.compile.jit.params import OperatorParam

from ..declare import Operator, Profile
from ..image.step import Fusion
from .record import Recording


def apply(
    recording: Recording, profile: Profile, fused: Sequence[Fusion], dev
) -> Recording:
    """Return ``recording`` with each step inside a fusion in ``fused`` at its entry's tunables.

    The tunables are what the step's profile entry gives it (``Profile.fusion_tunables``,
    matched the way ``iron.common.graph.fusion.fusions`` matches a fusion itself); a
    step whose entry gives none, or whose fusion matches no entry, is untouched.
    """
    given: dict[int, Mapping[str, Any]] = {}
    version = recording.version
    for fusion in fused:
        ops = [recording.steps[i].op.resolved(dev) for i in fusion.steps]
        tunables = profile.fusion_tunables(
            fusion.kind, ops, fusion.local_edges, version, fusion.phased
        )
        if tunables is None:
            continue
        given.update((i, t) for i, t in zip(fusion.steps, tunables) if t)
    return rebuild(recording, given, dev)


def retuned(op: Operator, tunables: Mapping[str, Any], dev) -> Operator:
    """Return the recorded ``op`` rebuilt at ``tunables`` and resolved for ``dev``, the bound device where None.

    From the recorded operator, so a tunable resolved at its old widths resolves again
    at the new ones. A flag that reads an operand coded (``In(coded=)``) keeps its
    recorded value: the step's slot already holds the weight coded or plain
    (``Recording.code_weights``).
    """
    coding = {
        b.declared_coded.name
        for b in op.buffers
        if isinstance(b.declared_coded, OperatorParam)
    }
    return op._with_tunables(
        **{n: v for n, v in tunables.items() if n not in coding}
    ).resolved(dev)


def rebuild(
    recording: Recording, tunables: Mapping[int, Mapping[str, Any]], dev
) -> Recording:
    """Return ``recording`` with each step ``tunables`` names, by index, rebuilt at its tunables there (``retuned``).

    The per-call values bound to its operator bound to the rebuilt one.
    """
    steps = list(recording.steps)
    rebuilt: dict[int, list] = {}
    for i, t in tunables.items():
        narrowed = retuned(recording.steps[i].op, t, dev)
        rebuilt.setdefault(id(recording.steps[i].op), []).append(narrowed)
        steps[i] = dataclasses.replace(steps[i], op=narrowed)
    if not rebuilt:
        return recording
    result = dataclasses.replace(recording, steps=steps)
    result.rebind(rebuilt)
    return result
