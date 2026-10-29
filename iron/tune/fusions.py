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
searches the members' settings for the fused form (``narrowings``) and
prices the fastest that co-resides against the members run apart at their
own; a member narrowed writes its own tunables into the fusion entry itself
(``FusionGroup.dims``, ``Profile.add_fusion``), applied only inside this
fusion (``iron.common.graph.fusion_tunables``), so the same shape running
unfused, or fused differently, elsewhere is untouched.
"""

from __future__ import annotations

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
from aie.iron import Program

from iron.common.declare import Operator, Profile
from iron.common.design import BuiltArray, OperatorDesign, configuration
from iron.common.graph.compiled import CompiledGraph, _step_words
from iron.common.graph.fusion import candidates
from iron.common.graph.fusion import fusions as graph_fusions
from iron.common.graph.fusion_tunables import apply as fusion_tunables_apply
from iron.common.image.compose import fused_configuration, places, unvalued
from iron.common.image.packaging import plan
from iron.common.image.step import Edge, Fusion, FusionKind
from .autotune import CONFIDENCE, FIT_CACHE, Shape, Timed, Trial, line, settings
from .measure import (
    Cache,
    Timing,
    _sample,
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
    round-trip to an equal one (an access pattern, which it cannot
    serialize at all; a tuple, which it gives back a list) left out: a
    profile entry still names what it can of a step whose shape is not
    wholly representable.
    """
    out = {}
    for k, v in dims.items():
        try:
            same = json.loads(json.dumps(v)) == v
        except TypeError:
            continue
        if same:
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

    def dims(
        self, combo: Sequence[Mapping[str, Any]] | None = None
    ) -> list[tuple[type, dict[str, Any], Mapping[str, Any] | None]]:
        """This fusion's steps as a profile entry names them
        (``Profile.add_fusion``), each with the tunables ``combo`` (a joint
        narrowing search's chosen setting, ``narrow_group``'s) gives it;
        None throughout where ``combo`` is, a group that needed no
        narrowing.
        """
        return [
            (type(op), _json_safe(shape.named(())), None if combo is None else combo[i])
            for i, (op, shape) in enumerate(zip(self.steps, self.shapes))
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


def _fed_widths(op: Operator, dev) -> list[dict[str, Any]]:
    """``op``'s settings (``_widths``), plus its settings with ``feed_b``
    held true: a member an edge feeds into its ``B`` may need it to admit
    the feed at all, a setting its own (unfused) width never tries since
    ``_widths`` holds every tunable but the column count closest to the
    member's own (``feed_b=False``, unfused).
    """
    if "feed_b" not in op.declaration.tunables:
        return _widths(op, dev)
    fed = op.replace(pinned=op.pinned | {"feed_b"}, feed_b=True)
    # feed_b is pinned on fed, so _widths leaves it out of what it found;
    # put it back so _with_tunables(**s) overrides it rather than keeping
    # op's own.
    return _widths(op, dev) + [{**s, "feed_b": True} for s in _widths(fed, dev)]


def _composed_module(
    designs: Mapping[str, OperatorDesign],
    kind: FusionKind | None = None,
    edges: Sequence[tuple[int, str, int, str]] = (),
) -> ir.Module:
    """The one module ``fits`` places ``designs`` as, built the same way it
    does: plain (``configuration``), or, given ``kind``, as ``kind``'s own
    fusion wires ``edges`` (``fused_configuration``, which also tells a
    pack's or a stream's own array per member, fuse=True, from a merge's
    shared one). Composing is cheap next to running the placement pipeline
    on the result, so a group-fit verdict's cache key is this module's own
    text: it reflects every code path composing takes (``configuration``,
    ``BuiltArray``, ...), not only ``compose.py``'s.
    """
    unvalued(designs)
    if kind is None:
        arrays = {n: BuiltArray(d) for n, d in designs.items()}
        configured = configuration(next(iter(arrays)), arrays)
    else:
        fusion = Fusion(
            kind,
            tuple(range(len(designs))),
            tuple(Edge(p, out, c, inp) for p, out, c, inp in edges),
        )
        configured, _ = fused_configuration("fused", fusion, list(designs.values()))
    return Program.compose([configured], entry=configured.runtimes[0]).resolve_program()


def group_fit_verdict(
    ops: Sequence[Operator],
    fit_cache: Path = FIT_CACHE,
    kind: FusionKind | None = None,
    edges: Sequence[tuple[int, str, int, str]] = (),
) -> str | None:
    """Why the placer refuses ``ops``' resolved designs sharing one device
    configuration (plain, or as ``kind``'s fusion wires ``edges``), or None
    if they co-reside; kept under ``fit_cache``, keyed on the composed
    module's own text (``_composed_module``) and each design's build
    (``artifact_hash``, as ``autotune.refusal`` keeps a single design's): a
    change to any code path composing takes invalidates it by construction,
    not only one to ``compose.py``'s own source.
    """
    designs = {str(i): OperatorDesign(op.resolved()) for i, op in enumerate(ops)}
    try:
        module = _composed_module(designs, kind, edges)
    except (ValueError, RuntimeError, ir.MLIRError) as e:
        return str(e)  # composing itself refused; no placement pass to cache
    key = hashlib.sha256(
        repr(
            (
                str(module),
                sorted(d.compilable().artifact_hash for d in designs.values()),
            )
        ).encode()
    ).hexdigest()[:24]
    record = fit_cache / key
    if record.exists():
        verdict = record.read_text()
    else:
        diagnostic = places(module)
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

    A member an edge feeds into its ``B`` searches ``feed_b`` true too
    (``_fed_widths``): the edge may only be admissible there, a setting its
    own (unfused) width never takes.
    """
    fed = {e[2] for e in group.edges if e[3] == "B"}
    per_member = [
        _fed_widths(op, dev) if i in fed else _widths(op, dev)
        for i, op in enumerate(group.steps)
    ]
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
                kind=group.kind,
                edges=group.edges,
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
    elif (
        group_fit_verdict(group.steps, fit_cache, kind=group.kind, edges=group.edges)
        is None
    ):
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
    combos: Mapping[FusionGroup, tuple[dict[str, Any], ...] | None],
    *,
    full_elf: bool,
    timing: Timing = Timing(rounds=3, calls=10),
    seed: int = 0,
    log: Callable[[str], None] = print,
) -> list[FusionGroup]:
    """``taken`` with a group dropped wherever the version it runs in does
    not gain from it beyond the noise: ``time_fusion_group`` prices a fusion
    against the steps it fuses alone, over one call; this times each
    recording's version with every group ``taken`` still holds fused
    (``combos``' narrowing, where it has one, applied via
    ``iron.common.graph.fusion_tunables`` the way a shipped profile would)
    against the same version unfused at its own, interleaved, and drops the
    smallest predicted gain (``priced``) among those active in a version
    that regresses, retrying it, until what is left gains or none is left
    to drop.

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
                trial_profile.add_fusion(
                    group.kind, group.dims(combos.get(group)), group.edges
                )
            fused = graph_fusions(recording, trial_profile)
            patched = (
                fusion_tunables_apply(recording, trial_profile, fused, dev)
                if fused
                else recording
            )
            plain_cg = CompiledGraph(recording, chosen, fusions=())
            fused_cg = CompiledGraph(patched, chosen, fusions=fused)
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

    A member narrowed to co-reside writes its own tunables into the fusion
    entry itself (``FusionGroup.dims``, ``Profile.add_fusion``), applied
    only to a step running inside this fusion
    (``iron.common.graph.fusion_tunables``): the same shape running unfused,
    or fused differently, elsewhere keeps what it already takes there.
    Fusion entries covering the shapes found are replaced; every tunable
    entry, and a fusion entry covering none of them, is kept as ``profile``
    has it.
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

    out = Profile()
    for cls, dims, tunables in profile or ():
        out.add(cls, **dims, **tunables)

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
            priced_dict,
            out,
            combos,
            full_elf=full_elf,
            timing=confirm_timing,
            log=log,
        )
    for group in taken:
        out.add_fusion(group.kind, group.dims(combos[group]), group.edges)
    return out
