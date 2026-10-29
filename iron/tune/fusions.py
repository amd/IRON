# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Choosing which on-chip fusions to take.

A graph admits more fusions (``iron.common.graph.fusion.candidates``) than a
profile should name: fusing one may cost more than it saves, or two may
overlap at one step. ``price_fusions`` times each fusion the calls' graphs
admit, as a whole, against the same steps run apart (``measure_fusion``), and
keeps those that gain beyond the noise, cheapest first, skipping one that
would share a step with a fusion already taken (``select_rewrites``, kept
kind-agnostic: a fold or a pack prices and selects the same way, over its
own ``Candidate``).
"""

from __future__ import annotations

import json
import logging
import math
import statistics
from collections.abc import Callable, Hashable, Mapping, Sequence
from typing import Any, Protocol, TypeVar

import numpy as np

from iron.common.declare import Operator, Profile
from iron.common.design import OperatorDesign
from iron.common.graph.compiled import CompiledGraph, _step_words
from iron.common.graph.fusion import candidates
from iron.common.graph.fusion import fusions as graph_fusions
from iron.common.image.packaging import plan
from iron.common.image.step import FusionKind
from .autotune import CONFIDENCE, Shape, Timed, Trial
from .measure import (
    Cache,
    Timing,
    _sample,
    measure_fusion,
    standard_error,
    time_interleaved,
)

logger = logging.getLogger(__name__)


def _json_safe(dims: Mapping[str, Any]) -> dict[str, Any]:
    """``dims`` (a ``Shape.named`` result) with any value JSON cannot
    round-trip (an access pattern, say) left out: a profile entry still
    names what it can of a step whose shape is not wholly representable.
    """
    out = {}
    for k, v in dims.items():
        try:
            json.dumps(v)
        except TypeError:
            continue
        out[k] = v
    return out


class FusionGroup:
    """Every occurrence of one fusion shape - its steps' shapes, in order,
    and the edges wiring them - across a tuner's calls: what
    ``time_fusion_group`` prices as a whole, and one fusion entry covers
    (``Profile.add_fusion``).
    """

    def __init__(
        self,
        kind: FusionKind,
        steps: Sequence[Operator],
        edges: Sequence[tuple[int, str, int, str]],
    ):
        self.kind = kind
        self.steps = list(steps)
        self.shapes = [Shape(op) for op in steps]
        self.edges = tuple(edges)
        # Each distinct identity's weighted points: every step's per-call
        # values, as an operator's own time is weighed (``Timed.op_points``).
        self.points: list[tuple[float, list[dict[str, int]]]] = []
        self.inputs: list[dict[str, np.ndarray]] = [{} for _ in steps]
        # (recording id, first step's index): every occurrence of this
        # fusion, so a group sharing a step with one taken first is seen to.
        self.occurrences: list[tuple[int, int]] = []

    @property
    def key(self) -> Hashable:
        return (self.kind, tuple(s.key for s in self.shapes), self.edges)

    def claims(self) -> set[tuple[int, int]]:
        """The (recording, step) pairs this fusion's steps occupy, in every
        recording it runs in.
        """
        out: set[tuple[int, int]] = set()
        for rid, first in self.occurrences:
            out.update((rid, first + i) for i in range(len(self.steps)))
        return out

    def occurs_in(self, recording) -> bool:
        """Whether this fusion runs in ``recording``."""
        rid = id(recording)
        return any(r == rid for r, _ in self.occurrences)

    def dims(self) -> list[tuple[type, dict[str, Any]]]:
        """This fusion's steps as a profile entry names them (``Profile.add_fusion``)."""
        return [
            (type(op), _json_safe(shape.named(())))
            for op, shape in zip(self.steps, self.shapes)
        ]

    def __str__(self) -> str:
        return " -> ".join(str(s) for s in self.shapes)


def fusion_groups(calls: Sequence[Timed], dev) -> list[FusionGroup]:
    """The stream fusions ``calls``' recordings admit (``candidates``),
    grouped by kind, steps' shapes and wiring, in the order first seen. A
    shape's points and inputs are taken from its first distinct identity
    alone, as ``autotune.shapes`` takes an operator's; every occurrence is
    kept, so a fusion sharing a step with another is seen regardless of how
    many times either recurs.
    """
    found: dict[Hashable, FusionGroup] = {}
    seen: set[tuple[str, ...]] = set()
    for call in calls:
        rid = id(call.recording)
        points = (
            [(1.0, call.values)]
            if not call.points
            else [(p.weight, p.values) for p in call.points]
        )
        for fusion in candidates(call.recording):
            # op_values/op_inputs match a binding's op by identity: the
            # recording's own (unresolved) op, not a resolved copy of it.
            raw_steps = [call.recording.steps[i].op for i in fusion.steps]
            resolved = [op.resolved(dev) for op in raw_steps]
            local = {step: i for i, step in enumerate(fusion.steps)}
            edges = tuple(
                (local[e.producer], e.output, local[e.consumer], e.input)
                for e in fusion.edges
            )
            group = FusionGroup(fusion.kind, resolved, edges)
            group = found.setdefault(group.key, group)
            group.occurrences.append((rid, fusion.steps[0]))
            identity = tuple(OperatorDesign(op).identity for op in resolved)
            if identity in seen:
                continue
            seen.add(identity)
            group.inputs = [call.op_inputs(op) for op in raw_steps]
            for weight, point_values in points:
                group.points.append(
                    (weight, [call.op_values(op, point_values) for op in raw_steps])
                )
    return list(found.values())


def time_fusion_group(
    group: FusionGroup,
    *,
    full_elf: bool,
    timing: Timing = Timing(),
    repeats: int = 9,
    cache: Cache | None = None,
    remeasure: bool = False,
    log: Callable[[str], None] = print,
) -> Trial:
    """``group`` priced as a whole: ``measure_fusion`` at each of its points,
    weighted as ``autotune._time`` weighs an operator's; refused where any
    point's fusion is.
    """
    delta = 0.0
    variance: float | None = 0.0
    refused: str | None = None
    for weight, values in group.points:
        m = measure_fusion(
            group.steps,
            group.edges,
            full_elf=full_elf,
            timing=timing,
            repeats=repeats,
            values=values,
            inputs=group.inputs,
            cache=cache,
            remeasure=remeasure,
            log=log,
        )
        if m.refused is not None:
            refused = refused or m.refused
            continue
        d, noise = m.difference()
        delta += weight * d
        variance = (
            None
            if variance is None or noise is None
            else variance + (weight * noise) ** 2
        )
    noise_us = None if variance is None else math.sqrt(variance)
    return Trial({}, delta, noise_us, refused)


class Candidate(Protocol):
    """What ``select_rewrites`` needs of a priced rewrite, a fusion or
    otherwise: the steps it would claim, by (recording, step index).
    """

    def claims(self) -> set[tuple[int, int]]: ...

    def __str__(self) -> str: ...


CandidateT = TypeVar("CandidateT", bound=Candidate)


def select_rewrites(
    priced: Sequence[tuple[CandidateT, Trial]], log: Callable[[str], None] = print
) -> list[CandidateT]:
    """Of ``priced`` candidates and their trials, those that gain beyond the
    noise (``Trial.gains``), cheapest first, skipping one whose steps
    overlap a candidate already taken. Kind-agnostic: a fusion, a fold or a
    pack is a ``Candidate`` the same way.
    """
    taken: list[CandidateT] = []
    claimed: set[tuple[int, int]] = set()
    for candidate, trial in sorted(
        (ct for ct in priced if ct[1].gains), key=lambda ct: ct[1].delta_us
    ):
        if candidate.claims() & claimed:
            log(f"  {candidate}: skipped, overlaps an edge already taken")
            continue
        taken.append(candidate)
        claimed |= candidate.claims()
        log(f"  {candidate}: taken")
    return taken


def _random_tensor(handle, rng: np.random.Generator) -> np.ndarray:
    """``handle``'s shape and dtype, filled with ``rng``'s bytes: an end to
    end confirmation only compares a fused version's output to the same
    recording's unfused one, not a numpy reference, so the content need not
    be representative.
    """
    sampled = _sample(handle.dtype, handle.nbytes, rng)
    return sampled.view(handle.dtype).reshape(handle.shape)


def confirm_fusions(
    calls: Sequence[Timed],
    dev,
    taken: Sequence[FusionGroup],
    priced: Mapping[FusionGroup, Trial],
    profile: Profile,
    *,
    full_elf: bool,
    timing: Timing = Timing(rounds=3, calls=10),
    seed: int = 0,
    log: Callable[[str], None] = print,
) -> list[FusionGroup]:
    """``taken`` with a group dropped wherever the version it runs in does
    not gain from it beyond the noise: ``time_fusion_group`` prices a fusion
    against the steps it fuses alone, over one call; this times each
    recording's version with every group ``taken`` still holds fused against
    the same version unfused, interleaved, and drops the smallest predicted
    gain (``priced``) among those active in a version that regresses,
    retrying it, until what is left gains or none is left to drop.

    Raises:
        RuntimeError: A version's fused output is not bit-identical to its
            unfused one.
    """
    remaining = list(taken)
    for call in calls:
        recording = call.recording
        active = [g for g in remaining if g.occurs_in(recording)]
        if not active:
            continue
        chosen = plan(
            dev, recording, full_elf, False, step_words=_step_words(recording)
        )
        rng = np.random.default_rng(seed)
        inputs = [_random_tensor(h, rng) for h in recording.inputs]
        states = [(s, h, _random_tensor(h, rng)) for s, h in recording.states.values()]
        while active:
            trial_profile = Profile()
            for cls, dims, tunables in profile:
                trial_profile.add(cls, **dims, **tunables)
            for kind, steps, edges in profile.fusions():
                trial_profile.add_fusion(kind, steps, edges)
            for group in remaining:
                trial_profile.add_fusion(group.kind, group.dims(), group.edges)
            fused = graph_fusions(recording, trial_profile)
            plain_cg = CompiledGraph(recording, chosen, fusions=())
            fused_cg = CompiledGraph(recording, chosen, fusions=fused)
            for state, _, content in states:
                plain_cg.write(state, content)
                fused_cg.write(state, content)
            plain_cg(*inputs, **call.values)
            fused_cg(*inputs, **call.values)
            plain_out = [plain_cg.read(h) for h in recording.returned]
            fused_out = [fused_cg.read(h) for h in recording.returned]
            if not all(np.array_equal(p, f) for p, f in zip(plain_out, fused_out)):
                names = ", ".join(str(g) for g in active)
                raise RuntimeError(
                    f"{recording.name}: fused ({names}) is not bit-identical to "
                    f"it unfused"
                )
            times = time_interleaved(
                [plain_cg.callable, fused_cg.callable], timing, log=log
            )
            paired = list(zip(times[0].samples_us, times[1].samples_us))
            delta = statistics.median(f - p for p, f in paired)
            noise = standard_error([f - p for p, f in paired])
            noise_s = "?" if noise is None else f"{noise:.1f}"
            log(
                f"{recording.name}: [{', '.join(str(g) for g in active)}] "
                f"{delta:+.1f} ± {noise_s} us end to end"
            )
            if noise is not None and delta < -CONFIDENCE * noise:
                break
            worst = max(active, key=lambda g: priced[g].delta_us)
            log(f"  {worst}: dropped, does not gain {recording.name} end to end")
            remaining.remove(worst)
            active.remove(worst)
    return remaining


def price_fusions(
    calls: Sequence[Timed],
    dev,
    profile: Profile | None = None,
    *,
    full_elf: bool,
    timing: Timing = Timing(),
    repeats: int = 9,
    cache: Cache | None = None,
    remeasure: bool = False,
    confirm: bool = True,
    confirm_timing: Timing = Timing(rounds=3, calls=10),
    log: Callable[[str], None] = print,
) -> Profile:
    """``profile`` with a fusion entry for each stream fusion ``calls``'
    graphs admit that gains beyond the noise (``time_fusion_group``,
    ``select_rewrites``) and, unless ``confirm`` is False, still gains each
    version it runs in end to end (``confirm_fusions``), taken cheapest
    first, skipping one that would share a step with a fusion already taken.
    Fusion entries covering the shapes found are replaced; every tunable
    entry, and a fusion entry covering none of them, is kept as ``profile``
    has it.
    """
    found = fusion_groups(calls, dev)
    out = Profile()
    for cls, dims, tunables in profile or ():
        out.add(cls, **dims, **tunables)

    priced = []
    for group in found:
        trial = time_fusion_group(
            group,
            full_elf=full_elf,
            timing=timing,
            repeats=repeats,
            cache=cache,
            remeasure=remeasure,
            log=log,
        )
        noise = "?" if trial.noise_us is None else f"{trial.noise_us:.1f}"
        why = "" if trial.refused is None else f"  refused: {trial.refused}"
        log(f"{group}: {trial.delta_us:+.1f} ± {noise} us{why}")
        priced.append((group, trial))

    taken = select_rewrites(priced, log)

    existing = profile.fusions() if profile is not None else []
    for kind, steps, edges in existing:
        probe = Profile()
        probe.add_fusion(kind, steps, edges)
        if not any(probe.fused(g.kind, g.steps, g.edges) for g in found):
            out.add_fusion(kind, steps, edges)

    if confirm:
        taken = confirm_fusions(
            calls,
            dev,
            taken,
            dict(priced),
            out,
            full_elf=full_elf,
            timing=confirm_timing,
            log=log,
        )
    for group in taken:
        out.add_fusion(group.kind, group.dims(), group.edges)
    return out
