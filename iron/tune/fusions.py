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

A ``PACK`` or ``MERGE`` group often co-resides only at narrower tunables
than its members' own standalone best (fewer columns, say): ``narrow_group``
searches the members' settings for the fused form (``narrowings``), prices
the fastest that co-resides against the members run apart at their own, and
``_resolve_narrowing`` decides, for a member whose shape also runs unfused or
fused differently elsewhere, whether narrowing it everywhere (the only way a
profile, matching by shape alone, can say it) still gains once what it costs
there is priced too.
"""

from __future__ import annotations

import dataclasses
import hashlib
import itertools
import json
import logging
import math
import statistics
from collections.abc import Callable, Hashable, Mapping, Sequence
from pathlib import Path
from typing import Any, Protocol, TypeVar

import numpy as np
from aie import ir

from iron.common.declare import Operator, Profile
from iron.common.design import OperatorDesign
from iron.common.graph.compiled import CompiledGraph, _step_words
from iron.common.graph.fusion import candidates
from iron.common.graph.fusion import fusions as graph_fusions
from iron.common.graph.record import Recording
from iron.common.image.compose import fits
from iron.common.image.packaging import plan
from iron.common.image.step import FusionKind
from .autotune import (
    CONFIDENCE,
    FIT_CACHE,
    Shape,
    Timed,
    Trial,
    line,
    replacing,
    settings,
)
from .autotune import shapes as autotune_shapes
from .measure import (
    Cache,
    Timing,
    _sample,
    measure,
    measure_fusion,
    standard_error,
    time_interleaved,
    write,
)

logger = logging.getLogger(__name__)

# Past this many combinations of the members' widths, only the ones using
# the most columns overall are checked for fit: a member is never faster
# narrower than at the width ``autotune`` already found it alone, only
# sometimes narrower is what lets it co-reside.
NARROWING_EXHAUSTIVE = 32


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


def fusion_groups(
    calls: Sequence[Timed], dev, kinds: Sequence[FusionKind] = tuple(FusionKind)
) -> list[FusionGroup]:
    """The fusions of ``kinds`` ``calls``' recordings admit (``candidates``),
    grouped by kind, steps' shapes and wiring, in the order first seen. A
    shape's points and inputs are taken from its first distinct identity
    alone, as ``autotune.shapes`` takes an operator's; every occurrence is
    kept, so a fusion sharing a step with another is seen regardless of how
    many times either recurs. Every kind by default, so a kind
    ``iron.common.graph.fusion`` adds later is priced the same way without a
    change here.
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
        for fusion in candidates(call.recording, kinds=kinds):
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
    fused: Sequence[Operator] | None = None,
    log: Callable[[str], None] = print,
) -> Trial:
    """``group`` priced as a whole: ``measure_fusion`` at each of its points,
    weighted as ``autotune._time`` weighs an operator's; refused where any
    point's fusion is. ``fused``, a joint narrowing search's on-chip
    combination of the members' tunables (``narrow_group``), prices them
    fused at that setting against ``group.steps`` run apart at their own;
    defaults to ``group.steps`` themselves.
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
            kind=group.kind,
            fused_steps=fused,
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


def _widths(op: Operator, dev) -> list[dict[str, Any]]:
    """``op``'s settings (``autotune.settings``), one per value of
    ``num_aie_columns`` it resolves at, each the setting otherwise closest
    to its own (``autotune.line``), widest first: ``autotune`` already timed
    every member alone and took its fastest, so narrowing a member only ever
    trades its own speed for co-residence, never gains either.
    """
    found = settings(op, dev, op.pinned)
    if "num_aie_columns" not in found[0]:
        return [found[0]]
    return sorted(
        line(found, found[0], "num_aie_columns"),
        key=lambda s: -s["num_aie_columns"],
    )


def group_fit_verdict(
    ops: Sequence[Operator], fit_cache: Path = FIT_CACHE
) -> str | None:
    """Why the placer refuses ``ops``' resolved designs sharing one device
    configuration, or None if they co-reside (``fits``); kept under
    ``fit_cache``, keyed on their recipes, as ``autotune.refusal`` keeps a
    single design's.
    """
    designs = {str(i): OperatorDesign(op.resolved()) for i, op in enumerate(ops)}
    key = hashlib.sha256(
        repr(sorted(d.compilable().recipe_hash for d in designs.values())).encode()
    ).hexdigest()[:24]
    record = fit_cache / key
    if record.exists():
        verdict = record.read_text()
    else:
        diagnostic = fits(designs)
        verdict = "fits" if diagnostic is None else f"refused: {diagnostic}"
        write(record, verdict)
    return None if verdict == "fits" else verdict.removeprefix("refused: ")


def _dominates(a: Sequence[Mapping[str, Any]], b: Sequence[Mapping[str, Any]]) -> bool:
    """Whether combination ``a`` is at least as wide as ``b`` in every
    member, strictly in one: ``b`` can then never be faster than ``a`` and
    so, narrower, can never be the fastest combination that fits.
    """
    cols_a = [s.get("num_aie_columns") for s in a]
    cols_b = [s.get("num_aie_columns") for s in b]
    return all(
        x is None or y is None or x >= y for x, y in zip(cols_a, cols_b)
    ) and any(x is not None and y is not None and x > y for x, y in zip(cols_a, cols_b))


def narrowings(
    group: FusionGroup,
    dev,
    fit_cache: Path = FIT_CACHE,
    exhaustive: int = NARROWING_EXHAUSTIVE,
) -> list[tuple[dict[str, Any], ...]]:
    """Every combination of the group's members' widths (``_widths``), the
    ones no feasible combination dominates in every member (``_dominates``),
    most columns overall first: a member is never faster narrower than
    ``autotune`` already found it alone, so the fastest fitting combination
    is among these.

    A pack's or a merge's co-resides where ``group_fit_verdict`` says so; an
    edge's own feed (a stream, a staged one, a fan-out) shares its buffer
    rather than needing one of its own per member, which
    ``group_fit_verdict``'s generic placement check does not model (nor
    whether a feed's lanes meet, broadcast or not), so every combination is
    a candidate, left to ``narrow_group``'s own build to refuse one that
    does not.

    Past ``exhaustive`` combinations, only the ones using the most columns
    overall are checked for fit, since those are the likeliest to dominate.
    """
    per_member = [_widths(op, dev) for op in group.steps]
    combos = list(itertools.product(*per_member))
    if len(combos) > exhaustive:
        combos = sorted(
            combos, key=lambda c: -sum(s.get("num_aie_columns", 0) for s in c)
        )[:exhaustive]
    feasible = (
        combos
        if group.edges
        else [
            c
            for c in combos
            if group_fit_verdict(
                [op._with_tunables(**s).resolved(dev) for op, s in zip(group.steps, c)],
                fit_cache,
            )
            is None
        ]
    )
    maximal = [
        c for c in feasible if not any(_dominates(o, c) for o in feasible if o is not c)
    ]
    return sorted(maximal, key=lambda c: -sum(s.get("num_aie_columns", 0) for s in c))


def narrow_group(
    group: FusionGroup,
    dev,
    *,
    full_elf: bool,
    timing: Timing = Timing(),
    repeats: int = 9,
    cache: Cache | None = None,
    remeasure: bool = False,
    fit_cache: Path = FIT_CACHE,
    exhaustive: int = NARROWING_EXHAUSTIVE,
    log: Callable[[str], None] = print,
) -> tuple[Trial, tuple[dict[str, Any], ...] | None]:
    """``group`` priced at the fastest setting of its members that
    co-resides, against ``group.steps`` run apart at their own: its own (as
    recorded) setting where that already co-resides, so a group that
    already fits is never searched or narrowed; otherwise each
    Pareto-maximal combination ``narrowings`` finds, widest first, timed
    (``time_fusion_group``) until one is not refused, the fastest of those
    kept.

    A fusion with edges (a stream, a staged one, a fan-out) shares its
    buffer rather than needing one of its own per member, so it takes less
    of a device than ``group.steps`` co-resident without a feed between
    them would (``group_fit_verdict``'s generic placement check does not
    see this); its own width is tried first, by building it, and taken
    without a search where that builds (a plain stream's usually does,
    ``iron.common.graph.fusion`` having already found it fused at its
    members' own width, ``_admits``, when it was proposed; a fan-out's may
    not, its several consumers sharing a shim budget the search then
    narrows to fit).

    Returns:
        The trial, and the settings taken for each of the group's members in
        order, or None where its own setting already co-resides or builds,
        or none of its members' widths co-reside (or build fused) at all
        (refused).
    """
    if group.edges:
        try:
            own = time_fusion_group(
                group,
                full_elf=full_elf,
                timing=timing,
                repeats=repeats,
                cache=cache,
                remeasure=remeasure,
                log=log,
            )
        except (ValueError, RuntimeError, ir.MLIRError) as e:
            log(f"  {group}: does not build at its own width: {e}")
        else:
            if own.refused is None:
                return own, None
    elif group_fit_verdict(group.steps, fit_cache) is None:
        return (
            time_fusion_group(
                group,
                full_elf=full_elf,
                timing=timing,
                repeats=repeats,
                cache=cache,
                remeasure=remeasure,
                log=log,
            ),
            None,
        )
    combos = narrowings(group, dev, fit_cache, exhaustive)
    if not combos:
        return (
            Trial({}, 0.0, None, refused="no setting of its members co-resides"),
            None,
        )
    best: Trial | None = None
    best_combo: tuple[dict[str, Any], ...] | None = None
    for combo in combos:
        fused = tuple(
            op._with_tunables(**s).resolved(dev) for op, s in zip(group.steps, combo)
        )
        cols = [s.get("num_aie_columns") for s in combo]
        try:
            trial = time_fusion_group(
                group,
                full_elf=full_elf,
                timing=timing,
                repeats=repeats,
                cache=cache,
                remeasure=remeasure,
                fused=fused,
                log=log,
            )
        except (ValueError, RuntimeError, ir.MLIRError) as e:
            # fits() places each design alone; narrowed together they may
            # still not build (a feed's lanes, say).
            log(f"  {group} narrowed to {cols}: does not build: {e}")
            continue
        noise = "?" if trial.noise_us is None else f"{trial.noise_us:.1f}"
        log(f"  {group} narrowed to {cols}: {trial.delta_us:+.1f} ± {noise} us")
        if trial.refused is None and (best is None or trial.delta_us < best.delta_us):
            best, best_combo = trial, combo
    if best is None:
        return (
            Trial(
                {},
                0.0,
                None,
                refused="no narrowing of its members both co-resides "
                "and matches the steps run apart",
            ),
            None,
        )
    return best, best_combo


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


def _shape_key(op: Operator, dev) -> Hashable:
    """``op``'s identity as a profile entry matches it (``Shape.key``),
    resolved for ``dev`` so a derived dimension reads its real value, not an
    unresolved placeholder.
    """
    return Shape(op.resolved(dev)).key


def _shape_occurrences(calls: Sequence[Timed], dev, key: Hashable) -> int:
    """How many steps across ``calls``' recordings are shape ``key``
    (``_shape_key``): every physical occurrence, not folded to one identity
    as ``autotune.shapes`` keeps.
    """
    return sum(
        1
        for call in calls
        for step in call.recording.steps
        if _shape_key(step.op, dev) == key
    )


def _claimed_occurrences(group: FusionGroup, dev, key: Hashable) -> int:
    """How many of shape ``key``'s physical occurrences ``group`` accounts
    for: its own occurrences, times how many of its members are that shape.
    """
    matches = sum(1 for op in group.steps if _shape_key(op, dev) == key)
    return matches * len(group.occurrences)


def _collateral_us(
    shape: Shape,
    tunables: Mapping[str, Any],
    *,
    full_elf: bool,
    timing: Timing,
    repeats: int,
    cache: Cache | None,
    remeasure: bool,
    log: Callable[[str], None],
) -> float:
    """How much slower ``shape`` runs at ``tunables`` than at its own,
    weighted over its points as ``autotune._time`` weighs an operator's:
    what forcing the profile's entry for it to a fusion's narrower setting
    would cost the occurrence the fusion itself does not narrow.
    """
    op, points, inputs = shape.members[0]
    ops = [op.resolved(), op._with_tunables(**tunables).resolved()]
    total = 0.0
    for weight, values in points:
        ran = measure(
            ops,
            full_elf=full_elf,
            timing=timing,
            repeats=repeats,
            values=values,
            inputs=inputs,
            cache=cache,
            remeasure=remeasure,
            log=log,
        )
        if 1 not in ran:
            return math.inf
        delta, _ = ran[1].against_default()
        total += weight * delta
    return total


def _resolve_narrowing(
    taken: Sequence[FusionGroup],
    combos: Mapping[FusionGroup, tuple[dict[str, Any], ...] | None],
    priced: Mapping[FusionGroup, Trial],
    calls: Sequence[Timed],
    dev,
    *,
    full_elf: bool,
    timing: Timing,
    repeats: int,
    cache: Cache | None,
    remeasure: bool,
    log: Callable[[str], None],
) -> tuple[list[FusionGroup], dict[Hashable, tuple[Shape, dict[str, Any]]]]:
    """``taken``, with a group dropped wherever narrowing a member whose
    shape also runs unfused, or fused differently, elsewhere
    (``_shape_occurrences``, ``_claimed_occurrences``) costs more there
    (``_collateral_us``) than the group gains: a profile matches a shape by
    its dims alone, not where it runs, so narrowing one member narrows every
    occurrence of its shape, and a narrowing only pays where the net still
    gains. The tunable settings the kept groups' narrowings need, by
    ``_shape_key`` (``price_fusions`` writes a profile entry for each); a
    shape no kept group narrows is untouched here, left to the profile it
    already has.

    ``taken`` cheapest first (its own order out of ``select_rewrites``), so
    a shape two groups would narrow differently is decided by whichever
    gains more; the later one either matches it or is dropped.
    """
    kept: list[FusionGroup] = []
    locked: dict[Hashable, dict[str, Any]] = {}
    entries: dict[Hashable, tuple[Shape, dict[str, Any]]] = {}
    for group in taken:
        combo = combos[group]
        if combo is None:
            kept.append(group)
            continue
        trial = priced[group]
        changes: list[tuple[Hashable, Shape, dict[str, Any]]] = []
        collateral = 0.0
        ok = True
        for op, tunables in zip(group.steps, combo):
            recorded = {n: vars(op.resolved(dev))[n] for n in tunables}
            if tunables == recorded:
                continue
            shape = Shape(op.resolved(dev))
            key = shape.key
            if key in locked:
                if locked[key] != tunables:
                    ok = False
                    log(
                        f"  {group}: dropped, {shape} is already narrowed to "
                        f"{locked[key]} for another fusion"
                    )
                    break
                continue
            total = _shape_occurrences(calls, dev, key)
            claimed = _claimed_occurrences(group, dev, key)
            if claimed < total:
                cost = _collateral_us(
                    shape,
                    tunables,
                    full_elf=full_elf,
                    timing=timing,
                    repeats=repeats,
                    cache=cache,
                    remeasure=remeasure,
                    log=log,
                )
                log(f"  {group}: narrowing {shape} elsewhere costs {cost:+.1f} us")
                collateral += cost
            changes.append((key, shape, tunables))
        if not ok:
            continue
        if collateral and -trial.delta_us <= collateral:
            log(
                f"  {group}: dropped, narrowing its members costs "
                f"{collateral:.1f} us elsewhere, past its {-trial.delta_us:.1f} us gain"
            )
            continue
        for key, shape, tunables in changes:
            locked[key] = tunables
            entries[key] = (shape, tunables)
        kept.append(group)
    return kept, entries


def _apply_tunables(
    recording: Recording, narrowed: Mapping[Hashable, Mapping[str, Any]], dev
) -> Recording:
    """``recording`` with every step whose shape (``_shape_key``) is in
    ``narrowed`` rebuilt at its tunables: the profile entries a joint
    narrowing search wrote, applied everywhere that shape runs, fused or
    not, as they will be once the profile ships (``confirm_fusions``).
    """
    if not narrowed:
        return recording
    steps = list(recording.steps)
    changed = False
    for i, step in enumerate(steps):
        tunables = narrowed.get(_shape_key(step.op, dev))
        if tunables is None:
            continue
        steps[i] = dataclasses.replace(
            step, op=step.op._with_tunables(**tunables).resolved(dev)
        )
        changed = True
    return dataclasses.replace(recording, steps=steps) if changed else recording


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
    narrowed: Mapping[Hashable, Mapping[str, Any]] | None = None,
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

    Args:
        narrowed: A joint narrowing search's chosen tunables, by
            ``_shape_key``, applied to every step of that shape in a
            version, fused or not (``_apply_tunables``): the profile being
            confirmed runs it everywhere that shape occurs, not only inside
            the fusions that needed it narrower.

    Raises:
        RuntimeError: A version's fused output is not bit-identical to its
            unfused one.
    """
    remaining = list(taken)
    narrowed = narrowed or {}
    for call in calls:
        active = [g for g in remaining if g.occurs_in(call.recording)]
        if not active:
            continue
        recording = _apply_tunables(call.recording, narrowed, dev)
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
            log(f"  {worst}: dropped, {recording.name} does not gain from it")
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
    fit_cache: Path = FIT_CACHE,
    exhaustive: int = NARROWING_EXHAUSTIVE,
    log: Callable[[str], None] = print,
) -> Profile:
    """``profile`` with a fusion entry for each fusion ``calls``' graphs
    admit that gains beyond the noise, each priced at the fastest setting of
    its members that co-resides (``narrow_group``) and, unless ``confirm``
    is False, still gains each version it runs in end to end
    (``confirm_fusions``), taken cheapest first, skipping one that would
    share a step with a fusion already taken (``select_rewrites``).

    A member narrowed to co-reside writes its own tunable entry too
    (``_resolve_narrowing``): dropped instead where its shape also runs
    unfused, or fused differently, elsewhere and costs more there than the
    fusion gains, since a profile narrows every occurrence of a shape, not
    only the one a fusion needed narrower. Fusion entries covering the
    shapes found, and tunable entries covering a shape narrowed, are
    replaced; the rest is kept as ``profile`` has it.
    """
    found = fusion_groups(calls, dev)

    priced: list[tuple[FusionGroup, Trial]] = []
    combos: dict[FusionGroup, tuple[dict[str, Any], ...] | None] = {}
    for group in found:
        trial, combo = narrow_group(
            group,
            dev,
            full_elf=full_elf,
            timing=timing,
            repeats=repeats,
            cache=cache,
            remeasure=remeasure,
            fit_cache=fit_cache,
            exhaustive=exhaustive,
            log=log,
        )
        noise = "?" if trial.noise_us is None else f"{trial.noise_us:.1f}"
        why = "" if trial.refused is None else f"  refused: {trial.refused}"
        log(f"{group}: {trial.delta_us:+.1f} ± {noise} us{why}")
        priced.append((group, trial))
        combos[group] = combo

    taken = select_rewrites(priced, log)
    priced_dict = dict(priced)
    taken, narrowed_entries = _resolve_narrowing(
        taken,
        combos,
        priced_dict,
        calls,
        dev,
        full_elf=full_elf,
        timing=timing,
        repeats=repeats,
        cache=cache,
        remeasure=remeasure,
        log=log,
    )

    out, covering, held = replacing(profile, [s for s, _ in narrowed_entries.values()])
    for shape, tunables in narrowed_entries.values():
        out.add(
            shape.cls,
            **shape.named(covering[shape.key]),
            **{**held[shape.key], **tunables},
        )

    existing = profile.fusions() if profile is not None else []
    for kind, steps, edges in existing:
        probe = Profile()
        probe.add_fusion(kind, steps, edges)
        if not any(probe.fused(g.kind, g.steps, g.edges) for g in found):
            out.add_fusion(kind, steps, edges)

    if confirm:
        narrowed_tunables = {key: t for key, (_, t) in narrowed_entries.items()}
        taken = confirm_fusions(
            calls,
            dev,
            taken,
            priced_dict,
            out,
            full_elf=full_elf,
            timing=confirm_timing,
            narrowed=narrowed_tunables,
            log=log,
        )
    for group in taken:
        out.add_fusion(group.kind, group.dims(), group.edges)
    return out
