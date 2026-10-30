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
import os
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
from iron.common.image.compose import fused_configuration, unvalued
from iron.common.image.packaging import plan
from iron.common.image.step import Edge, Fusion, FusionKind
from .failures import Kind, Ledger, first_error, place
from .autotune import CONFIDENCE, FIT_CACHE, Shape, Timed, Trial, line, settings
from .measure import (
    Cache,
    Timing,
    _sample,
    measure_fusion,
    npu_lock,
    standard_error,
    time_interleaved,
    write,
)

logger = logging.getLogger(__name__)

# What ``price_fusions`` prices: not ``MERGE``, consecutive steps in one
# configuration, which a profile's packings do for a whole version.
PRICED_KINDS = tuple(k for k in FusionKind if k is not FusionKind.MERGE)

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
    lock: bool = False,
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
            lock=lock,
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
    """``op``'s settings with ``feed_b`` held true, only: an edge into its
    ``B`` can only be fed there (an unfed ``B`` is not a streamed input at
    all, so ``feed_b=False`` never builds for this member), and a large
    group's exhaustive cap sorts combinations by column count alone, so
    keeping the never-buildable ``feed_b=False`` ones here would crowd the
    only combinations that can actually work out of it.
    """
    if "feed_b" not in op.declaration.tunables:
        return _widths(op, dev)
    fed = op.replace(pinned=op.pinned | {"feed_b"}, feed_b=True)
    # feed_b is pinned on fed, so _widths leaves it out of what it found;
    # put it back so _with_tunables(**s) overrides it rather than keeping
    # op's own.
    return [{**s, "feed_b": True} for s in _widths(fed, dev)]


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
    ledger: Ledger | None = None,
) -> str | None:
    """Why the placer refuses ``ops``' resolved designs sharing one device
    configuration (plain, or as ``kind``'s fusion wires ``edges``), or None
    if they co-reside; kept under ``fit_cache``, keyed on the composed
    module's own text (``_composed_module``) and each design's build
    (``artifact_hash``, as ``autotune.refusal`` keeps a single design's): a
    change to any code path composing takes invalidates it by construction,
    not only one to ``compose.py``'s own source. The placer runs in a
    process of its own (``failures.place``): a compiler crash refuses the
    group, recorded in ``ledger`` where one is given.
    """
    found = _fit_record(ops, fit_cache, kind, edges)
    if isinstance(found, str):
        return found  # composing itself refused; no placement pass to cache
    text, record = found
    if record.exists():
        verdict = record.read_text()
    else:
        outcome, diagnostic = place(text)
        if outcome == "crash":
            if ledger is not None:
                ledger.record(
                    Kind.CRASH,
                    ops[0].dev.name,
                    diagnostic or "",
                    "placing "
                    + ", ".join(type(op).__name__ for op in ops)
                    + " in one device",
                    module=text,
                )
            diagnostic = f"the compiler crashed: {first_error(diagnostic or '')}"
        verdict = "fits" if outcome == "fits" else f"refused: {diagnostic}"
        write(record, verdict)
    return None if verdict == "fits" else verdict.removeprefix("refused: ")


def refuse_group(
    ops: Sequence[Operator],
    reason: str,
    fit_cache: Path = FIT_CACHE,
    kind: FusionKind | None = None,
    edges: Sequence[tuple[int, str, int, str]] = (),
) -> None:
    """Record ``ops`` as refused to share one device for ``reason`` (a build,
    a run or a comparison that failed past placement), so
    ``group_fit_verdict`` answers it so until the toolchain changes.
    """
    found = _fit_record(ops, fit_cache, kind, edges)
    if not isinstance(found, str):
        write(found[1], f"refused: {reason}")


def _fit_record(
    ops: Sequence[Operator],
    fit_cache: Path,
    kind: FusionKind | None,
    edges: Sequence[tuple[int, str, int, str]],
) -> tuple[str, Path] | str:
    """``ops`` composed into one module, its text and its verdict's file
    under ``fit_cache``; or why composing them refused.
    """
    designs = {str(i): OperatorDesign(op.resolved()) for i, op in enumerate(ops)}
    try:
        module = _composed_module(designs, kind, edges)
    except (ValueError, RuntimeError, ir.MLIRError) as e:
        return str(e)
    text = str(module)
    key = hashlib.sha256(
        repr(
            (text, sorted(d.compilable().artifact_hash for d in designs.values()))
        ).encode()
    ).hexdigest()[:24]
    return text, fit_cache / key


def _device_timeout(e: Exception) -> bool:
    """Whether ``e`` is the driver's own command timeout
    (``ert_cmd_state.ERT_CMD_STATE_TIMEOUT``, ``iron.common.image.callable``
    ``.wait``'s), not a build or placement failure: a hang, which another
    setting of the same group may share, so a caller refuses the group
    outright rather than trying one.
    """
    return "ERT_CMD_STATE_TIMEOUT" in str(e)


def _refused_key(group: FusionGroup) -> str:
    """``group``'s content-hash identity among refused groups: stable
    across a restart, unlike ``id(group)``, and over ``group.key`` alone so
    a progress file holds it as a plain string.
    """
    return hashlib.sha256(repr(group.key).encode()).hexdigest()[:32]


def _load_refused(path: Path) -> dict[str, str]:
    """A hung group never retried, by ``_refused_key``, with why: empty
    where ``path`` holds none yet.
    """
    return json.loads(path.read_text()) if path.exists() else {}


def _save_refused(refused: Mapping[str, str], path: Path) -> None:
    """``refused`` written atomically, as ``_checkpoint`` writes a profile:
    another process may be reading ``path``.
    """
    partial = path.with_suffix(f".{os.getpid()}")
    partial.write_text(json.dumps(refused))
    partial.replace(path)


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
    """Every combination of the group's members' widths (``_widths``), most
    columns overall first: a member is never faster narrower than
    ``autotune`` already found it alone, so the fastest fitting combination
    is among these.

    A pack's or a merge's co-resides where ``group_fit_verdict`` says so,
    which lets dominance prune one combination no feasible one can ever beat
    (``_dominates``): among combinations that already co-reside, a member
    is never faster narrower, so one no feasible combination dominates in
    every member is never worse than the one dominating it, and the search
    need not try it.

    An edge's own feed (a stream, a staged one, a fan-out) shares its buffer
    rather than needing one of its own per member, which
    ``group_fit_verdict``'s generic placement check does not model (nor
    whether a feed's lanes meet, broadcast or not), so every combination is
    a candidate, left to ``narrow_group``'s own build to refuse one that
    does not: with no feasibility check to back it, dominance does not
    prune here (every width list's own-widest entry co-occurs in the
    all-widest combination, which would always dominate every other one,
    collapsing the search to that single, usually non-co-resident
    combination alone) — every one of these (up to ``exhaustive``) is tried.

    Past ``exhaustive`` combinations, only the ones using the most columns
    overall are checked for fit, since those are the likeliest to dominate
    (a pack or a merge) or fastest if they do build (an edge).

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
    if group.edges:
        return sorted(
            combos, key=lambda c: -sum(s.get("num_aie_columns", 0) for s in c)
        )
    feasible = [
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
    lock: bool = False,
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

    A device command timeout (the driver's own, not a build or placement
    failure) refuses the group outright, without trying another setting:
    a hang is a property of actually running it, which another setting may
    share, so retrying risks hanging the NPU again rather than finding one
    that works. It is never caught past here, so one run never retries a
    group it has already hung on.
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
                lock=lock,
            )
        except (ValueError, RuntimeError, ir.MLIRError) as e:
            if _device_timeout(e):
                return Trial({}, 0.0, None, refused=f"hung on the device: {e}"), None
            log(f"  {group}: does not build at its own width: {e}")
        else:
            if own.refused is None:
                return own, None
            log(f"  {group}: refused at its own width: {own.refused}")
    elif (
        group_fit_verdict(group.steps, fit_cache, kind=group.kind, edges=group.edges)
        is None
    ):
        try:
            return (
                time_fusion_group(
                    group,
                    full_elf=full_elf,
                    timing=timing,
                    repeats=repeats,
                    cache=cache,
                    remeasure=remeasure,
                    log=log,
                    lock=lock,
                ),
                None,
            )
        except (ValueError, RuntimeError, ir.MLIRError) as e:
            if _device_timeout(e):
                return Trial({}, 0.0, None, refused=f"hung on the device: {e}"), None
            log(f"  {group}: does not build at its own (fitting) width: {e}")
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
                lock=lock,
            )
        except (ValueError, RuntimeError, ir.MLIRError) as e:
            if _device_timeout(e):
                return Trial({}, 0.0, None, refused=f"hung on the device: {e}"), None
            # fits() places each design alone; narrowed together they may
            # still not build (a feed's lanes, say).
            log(f"  {group} narrowed to {cols}: does not build: {e}")
            continue
        noise = "?" if trial.noise_us is None else f"{trial.noise_us:.1f}"
        if trial.refused is not None:
            log(f"  {group} narrowed to {cols}: refused: {trial.refused}")
            continue
        log(f"  {group} narrowed to {cols}: {trial.delta_us:+.1f} ± {noise} us")
        if best is None or trial.delta_us < best.delta_us:
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


def _gather_table_rows(recording) -> dict[str, int]:
    """An input ids handle's buffer name to the table row count a ``Gather``
    holds it to: random bytes are not valid ids (``Gather.control_words``
    raises past the table), so these need drawing in range instead. Keyed
    by name, not identity: the handle a step's ``gather`` holds is its own
    view, a different object from ``recording.inputs``' of the same buffer.
    """
    return {
        step.gather.name: step.op.table_rows
        for step in recording.steps
        if step.gather is not None and step.gather.role == "input"
    }


def _bound_points(recording, values: Mapping[str, int]) -> list[dict[str, int]]:
    """``values`` with each per-call value that bounds an extent halved, one
    at a time, where the recording's limits allow it and every bounded
    operator derives its per-call words there: a design reading a bound
    wrongly agrees with the right one when every bound is at its largest,
    as it is in a full prompt chunk.
    """
    bounded = [b for b in recording.bindings if b.member.bounds is not None]
    bounding = sorted({b.expression.value.name for b in bounded if b.expression.linear})
    points = []
    for name in bounding:
        if values.get(name, 0) < 2:
            continue
        point = {**values, name: values[name] // 2}
        try:
            recording.check_limits(point)
            for op in {id(b.op): b.op for b in bounded}.values():
                extents = {
                    b.member.name: b.expression.evaluate(point)
                    for b in bounded
                    if b.op is op
                }
                resolved = op.resolved()
                for word in resolved._per_call_derived() - resolved.bound_values.keys():
                    resolved.derived_at(word, **extents)
        except (IndexError, ValueError):
            continue
        points.append(point)
    return points


def compare_graphs(
    call: Timed,
    before: CompiledGraph,
    after: CompiledGraph,
    *,
    timing: Timing,
    seed: int = 0,
    log: Callable[[str], None] = print,
    lock: bool = False,
) -> tuple[float, float | None]:
    """How much longer ``after`` takes than ``before``, two builds of
    ``call``'s recording, run interleaved on the same seeded inputs and
    states at each of the call's points (its own values where it has none),
    weighted, and that difference's standard error; both are released after.

    Raises:
        RuntimeError: ``after``'s outputs are not bit-identical to
            ``before``'s at a point, the call's values or one of its bounds
            halved (``_bound_points``); a device timeout propagates as it is
            raised.
    """
    recording = call.recording
    rng = np.random.default_rng(seed)
    table_rows = _gather_table_rows(recording)
    inputs = [
        (
            rng.integers(0, table_rows[h.name], h.shape).astype(h.dtype)
            if h.name in table_rows
            else _random_tensor(h, rng)
        )
        for h in recording.inputs
    ]
    states = [(s, h, _random_tensor(h, rng)) for s, h in recording.states.values()]
    timed = [(p.weight, {**call.values, **p.values}) for p in call.points] or [
        (1.0, dict(call.values))
    ]
    # A timed point right after it is staged: timing dispatches what was
    # staged last.
    staged = [(None, v) for v in _bound_points(recording, call.values)] + timed
    delta = 0.0
    variance: float | None = 0.0
    # Held from the first dispatch (each graph's context created lazily on
    # it) through the release below, not just around a dispatch: both
    # graphs' contexts stay loaded past their own call otherwise, past the
    # window another process holding this lock is kept out of.
    with npu_lock(lock):
        try:
            for weight, values in staged:
                for state, _, content in states:
                    before.write(state, content)
                    after.write(state, content)
                before(*inputs, **values)
                after(*inputs, **values)
                if not all(
                    np.array_equal(before.read(h), after.read(h))
                    for h in recording.returned
                ):
                    raise RuntimeError(
                        f"{recording.name}: not bit-identical to it as before at "
                        f"{values}"
                    )
                if weight is None:
                    continue
                times = time_interleaved(
                    [before.callable, after.callable], timing, log=log, lock=lock
                )
                paired = [
                    a - b for b, a in zip(times[0].samples_us, times[1].samples_us)
                ]
                delta += weight * statistics.median(paired)
                noise = standard_error(paired)
                variance = (
                    None
                    if variance is None or noise is None
                    else variance + (weight * noise) ** 2
                )
        finally:
            before.release()
            after.release()
    return delta, None if variance is None else math.sqrt(variance)


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
    refused: dict[str, str] | None = None,
    log: Callable[[str], None] = print,
    lock: bool = False,
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

    Args:
        refused: A hang's reason recorded here, by ``_refused_key``, for
            every group dropped on it: a caller persists this so the group
            is never retried past this run either.
        lock: Take ``NPU_LOCK_PATH`` from each version's first dispatch
            through releasing its graphs' contexts, not just under
            ``coord/npu``.

    Raises:
        RuntimeError: A version's fused output is not bit-identical to its
            unfused one, at the call's values or at one of its bounds
            halved (``_bound_points``).
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
            try:
                plain_cg = CompiledGraph(recording, chosen, fusions=())
                narrowed = plan(
                    dev,
                    patched,
                    full_elf,
                    False,
                    step_words=_step_words(patched),
                    fusions=fused,
                )
                fused_cg = CompiledGraph(patched, narrowed, fusions=fused)
            except (ValueError, RuntimeError, ir.MLIRError) as e:
                # A build failure is a property of this version (this
                # particular combination of active groups' fusions), not of
                # any one group alone; drop the one predicted to gain least
                # and retry, as for a version that regresses once run.
                worst = max(active, key=lambda g: priced[g].delta_us)
                log(f"  {worst}: dropped, {recording.name} does not build fused: {e}")
                remaining.remove(worst)
                active.remove(worst)
                continue
            try:
                delta, noise = compare_graphs(
                    call,
                    plain_cg,
                    fused_cg,
                    timing=timing,
                    seed=seed,
                    log=log,
                    lock=lock,
                )
            except (RuntimeError, ir.MLIRError) as e:
                if not _device_timeout(e):
                    raise
                # A hang is a property of this version running at all,
                # which dropping only one of several active groups may not
                # fix; none of them is retried in this run.
                names = ", ".join(str(g) for g in active)
                log(f"  {names}: dropped, {recording.name} hung on the device: {e}")
                for g in active:
                    remaining.remove(g)
                    if refused is not None:
                        refused[_refused_key(g)] = f"hung on the device: {e}"
                break
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


def _checkpoint(
    profile: Profile | None,
    priced: Sequence[tuple[FusionGroup, Trial]],
    combos: Mapping[FusionGroup, tuple[dict[str, Any], ...] | None],
    checkpoint: Path,
) -> None:
    """``profile`` with a fusion entry for each group ``priced`` so far
    gains beyond the noise (``select_rewrites``, not yet confirmed end to
    end, which needs its own device time this does not spend), written
    atomically: a restart after a run dies partway at least starts from
    every group already priced (``price_fusions``'s own cache does that
    regardless), and whoever is waiting on it can see the decisions so far.
    """
    out = Profile()
    for cls, dims, tunables in profile or ():
        out.add(cls, **dims, **tunables)
    for group in select_rewrites(priced, log=lambda _: None):
        out.add_fusion(group.kind, group.dims(combos.get(group)), group.edges)
    # Profile.save() writes in place; another process reading checkpoint
    # must never see a half-written file, so write beside it and rename.
    partial = checkpoint.with_suffix(f".{os.getpid()}")
    out.save(partial)
    partial.replace(checkpoint)


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
    checkpoint: Path | None = None,
    max_price: int | None = None,
    kinds: Sequence[FusionKind] = PRICED_KINDS,
    log: Callable[[str], None] = print,
    lock: bool = False,
) -> Profile | None:
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

    Args:
        kinds: The kinds priced (``PRICED_KINDS``).
        checkpoint: Where to write the decisions so far (``_checkpoint``)
            after every group is priced, so a run that dies partway still
            leaves something behind beyond the cache alone. A group a device
            timeout refused is written beside it (``_refused_key``,
            ``checkpoint.with_suffix(".refused.json")``) and loaded back
            here first, so a later call, batched or a restart after one,
            never retries it.
        max_price: Price at most this many of the found groups in this
            call (already-cached ones cost little to recheck); where that
            leaves any unpriced, return None without selecting, confirming
            or saving. A caller holding the device lock for this call
            alone, and calling again (fresh lock, so another agent's own
            short run is never kept waiting behind a whole multi-hour
            sweep) until it gets a profile back, never holds the lock past
            one batch.
        lock: Take ``NPU_LOCK_PATH`` for each measurement's own lifetime (a
            caller running this whole sweep without the ``coord/npu``
            wrapper, which takes it for the wrapped command's whole life
            instead).

    Returns:
        The profile, or None where ``max_price`` left groups unpriced.
    """
    refused_path = (
        None if checkpoint is None else checkpoint.with_suffix(".refused.json")
    )
    refused = {} if refused_path is None else _load_refused(refused_path)

    all_found = fusion_groups(calls, dev, kinds)
    found = []
    for group in all_found:
        why = refused.get(_refused_key(group))
        if why is None:
            found.append(group)
        else:
            log(f"{group}: skipped, refused earlier: {why}")
    if max_price is not None and max_price < len(found):
        found_now, rest = found[:max_price], found[max_price:]
    else:
        found_now, rest = found, []

    priced: list[tuple[FusionGroup, Trial]] = []
    combos: dict[FusionGroup, tuple[dict[str, Any], ...] | None] = {}
    for group in found_now:
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
            lock=lock,
        )
        noise = "?" if trial.noise_us is None else f"{trial.noise_us:.1f}"
        why = "" if trial.refused is None else f"  refused: {trial.refused}"
        log(f"{group}: {trial.delta_us:+.1f} ± {noise} us{why}")
        priced.append((group, trial))
        combos[group] = combo
        if trial.refused is not None and trial.refused.startswith("hung on the device"):
            refused[_refused_key(group)] = trial.refused
            if refused_path is not None:
                _save_refused(refused, refused_path)
        if checkpoint is not None:
            _checkpoint(profile, priced, combos, checkpoint)

    if rest:
        log(f"{len(rest)} group(s) left unpriced this batch; call again for them")
        return None

    taken = select_rewrites(priced, log)
    priced_dict = dict(priced)

    out = Profile()
    for cls, dims, tunables in profile or ():
        out.add(cls, **dims, **tunables)

    existing = profile.fusions() if profile is not None else []
    for kind, steps, edges in existing:
        probe = Profile()
        probe.add_fusion(kind, steps, edges)
        if not any(probe.fused(g.kind, g.steps, g.edges) for g in all_found):
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
            refused=refused,
            log=log,
            lock=lock,
        )
        if refused_path is not None:
            _save_refused(refused, refused_path)
    for group in taken:
        out.add_fusion(group.kind, group.dims(combos[group]), group.edges)
    return out
