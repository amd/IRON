# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a tune saves, checked end to end against the profile it started from.

Each version it changes is built under both and compared (``compare_graphs``); a version
that does not gain takes the starting profile's entries back, and the result is checked
again, so every gain a tune reports is one of a profile it built.
"""

from __future__ import annotations

import dataclasses
import json
from collections.abc import Callable, Hashable, Sequence
from pathlib import Path
from typing import Any

from iron.common.declare import Profile
from iron.common.declare.profile import PackingEntry, Version
from iron.common.graph.compiled import apply_profile
from iron.common.graph.fold import chosen_folds
from iron.common.graph.fusion import fusions as graph_fusions
from iron.common.graph.record import Recording
from iron.common.image.step import FusionKind

from .autotune import CONFIDENCE, Timed, _identity
from .fusions import built, compare_graphs
from .measure import Timing


@dataclasses.dataclass(frozen=True)
class Check:
    """One version built under a candidate profile against its base.

    Attributes:
        name: The recording's name and its inputs' shapes.
        delta_us: How much longer the candidate takes, weighted over the
            call's points; negative is faster.
        noise_us: The standard error of `delta_us`; None from one round.
    """

    name: str
    delta_us: float
    noise_us: float | None

    @property
    def gains(self) -> bool:
        return self.noise_us is not None and self.delta_us < -CONFIDENCE * self.noise_us


def fingerprint(call: Timed, profile: Profile, dev) -> Hashable:
    """Return what ``call``'s version builds under ``profile``.

    Its steps' designs, fusions and packing; two profiles giving one fingerprint build
    one image.
    """
    recording, fused, packing = apply_profile(call.recording, profile, dev)
    return tuple(_identity(s.op, dev) for s in recording.steps), fused, packing


def touches(kind: str, entry: Any, recording: Recording) -> bool:
    """Whether a profile entry applies to a step of ``recording``.

    ``kind`` ``"tunable"`` (``(cls, dims, tunables)``), ``"fusion"``
    (``Profile.fusions``'s) or ``"packing"`` (a ``PackingEntry``).
    """
    version = recording.version
    if kind == "tunable":
        cls, dims, _ = entry
        return any(
            isinstance(s.op, cls)
            and Profile.matches(dims, Profile.dims(type(s.op), vars(s.op)))
            for s in recording.steps
        )
    probe = Profile()
    if kind == "fusion":
        fusion_kind, steps, edges, versions = entry
        if versions is not None and version not in versions:
            return False
        probe.add_fusion(fusion_kind, steps, edges)
        found = (
            chosen_folds(recording, probe)
            if fusion_kind is FusionKind.FOLD
            else graph_fusions(recording, probe)
        )
        return bool(found)
    if entry.versions is not None and version not in entry.versions:
        return False
    probe.add_packing(entry.members)
    return any(probe.packings_of(s.op.resolved(), version) for s in recording.steps)


def narrowed(
    base: Profile,
    candidate: Profile,
    losers: set[Version],
    recordings: Sequence[Recording],
) -> Profile:
    """``candidate`` with ``base``'s entries wherever they touch a version in ``losers``.

    A scoped fusion or packing loses those versions, an unscoped one or a tunable entry
    is ``base``'s as a whole.
    """
    lost = [r for r in recordings if r.version in losers]
    out = Profile()
    for entry in candidate:
        if not any(touches("tunable", entry, r) for r in lost):
            out.add(entry[0], **entry[1], **entry[2])
    for entry in base:
        if any(touches("tunable", entry, r) for r in lost):
            out.add(entry[0], **entry[1], **entry[2])
    fusions: list = []
    for kind, steps, edges, versions in candidate.fusions():
        if versions is not None:
            versions = versions - losers
        elif any(touches("fusion", (kind, steps, edges, None), r) for r in lost):
            continue
        if versions is None or versions:
            fusions.append((kind, steps, edges, versions))
    for kind, steps, edges, versions in base.fusions():
        if any(touches("fusion", (kind, steps, edges, versions), r) for r in lost):
            scope = None if versions is None else versions & losers
            if (kind, steps, edges, scope) not in fusions:
                fusions.append((kind, steps, edges, scope))
    for fusion in fusions:
        out.add_fusion(*fusion)
    packings: list[PackingEntry] = []
    for entry in candidate.packings():
        if entry.versions is not None:
            if rest := entry.versions - losers:
                packings.append(PackingEntry(entry.members, frozenset(rest)))
        elif not any(touches("packing", entry, r) for r in lost):
            packings.append(entry)
    for entry in base.packings():
        if any(touches("packing", entry, r) for r in lost):
            scope = None if entry.versions is None else entry.versions & losers
            if (own := PackingEntry(entry.members, scope)) not in packings:
                packings.append(own)
    for entry in packings:
        out.add_packing(entry.members, entry.versions)
    return out


def verify(
    record: Callable[[Profile], Sequence[Timed]],
    dev,
    base: Profile,
    candidate: Profile,
    *,
    timing: Timing = Timing(rounds=3, calls=10),
    log: Callable[[str], None] = print,
    lock: bool = False,
    memo: dict[tuple[Hashable, Hashable], Check] | None = None,
) -> tuple[Profile, dict[Version, Check]]:
    """``candidate`` where each version it builds differently from ``base`` gains on it end to end beyond the noise.

    ``base``'s entries elsewhere (``narrowed``), and each changed version's last check.

    Args:
        dev: The device the versions run on.
        base: The profile each version is checked against.
        candidate: The profile checked.
        timing: How each version is timed end to end.
        log: Where each version's verdict is logged.
        lock: Take the device lock per check, not under ``coord/npu``.
        record: The calls, recorded under a profile.
        memo: Checks by the two builds' fingerprints, read and added to: a
            tune's checks against its seed and then its start share it, so
            a version the search left as the seed is not built and timed
            twice.
    """
    memo = {} if memo is None else memo
    old = {c.recording.version: c for c in record(base)}
    plain = {v: fingerprint(c, base, dev) for v, c in old.items()}
    chosen, losers = candidate, set()
    checks: dict[Version, Check] = {}
    measured: dict[Version, Hashable] = {}
    while True:
        calls = record(chosen)
        fresh = set()
        for call in calls:
            version = call.recording.version
            built_as = fingerprint(call, chosen, dev)
            if built_as == plain[version]:
                checks.pop(version, None)
                continue
            if measured.get(version) == built_as:
                continue
            measured[version] = built_as
            if (pair := (plain[version], built_as)) in memo:
                check = checks[version] = memo[pair]
                log(f"verify {check.name}: as checked before, {check.delta_us:+.1f} us")
                if not check.gains:
                    fresh.add(version)
                continue
            delta, noise = compare_graphs(
                old[version],
                built(old[version], base, dev),
                built(call, chosen, dev),
                timing=timing,
                log=log,
                lock=lock,
            )
            inputs = ", ".join(f"{n}{list(s)}" for n, s, _ in version) or "no inputs"
            check = Check(f"{call.recording.name} ({inputs})", delta, noise)
            checks[version] = memo[pair] = check
            noise_s = "?" if noise is None else f"{noise:.1f}"
            verdict = "kept" if check.gains else "reverted to the base's entries"
            log(
                f"verify {check.name}: {delta:+.1f} ± {noise_s} us end to end, {verdict}"
            )
            if not check.gains:
                fresh.add(version)
        if not fresh:
            return chosen, checks
        if fresh <= losers:
            log(
                "verify: a version that does not gain cannot be narrowed back; base kept"
            )
            return base, {}
        losers |= fresh
        chosen = narrowed(base, chosen, losers, [c.recording for c in calls])


def entries(profile: Profile) -> set[str]:
    """``profile``'s entries, one line each, for a report's diff."""

    def step(cls, dims, tunables) -> str:
        named = " ".join(f"{k}={v}" for k, v in dims.items())
        given = "" if not tunables else f" {json.dumps(tunables, sort_keys=True)}"
        return f"{cls.__name__} {named}".strip() + given

    def scope(versions) -> str:
        if versions is None:
            return ""
        return " in " + "; ".join(
            sorted(", ".join(f"{n}{list(s)}" for n, s, _ in v) for v in versions)
        )

    out = {f"tunables {step(cls, d, t)}" for cls, d, t in profile}
    out |= {
        f"{kind.value} " + " + ".join(step(*s) for s in steps) + scope(versions)
        for kind, steps, _, versions in profile.fusions()
    }
    out |= {
        "packing " + " + ".join(step(*m) for m in p.members) + scope(p.versions)
        for p in profile.packings()
    }
    return out


def write_report(
    path: Path,
    start: Profile,
    saved: Profile,
    checks: dict[Version, Check],
    **found: Any,
) -> None:
    """Write the tune's report beside ``path`` (``.report.json`` and ``.report.txt``).

    What ``saved`` adds to and drops from ``start``, each changed version's check
    against ``start``, and ``found``, anything else a caller measured.
    """
    before, after = entries(start), entries(saved)
    report = {
        "profile": str(path),
        "added": sorted(after - before),
        "dropped": sorted(before - after),
        "versions": [dataclasses.asdict(c) for c in checks.values()],
        **found,
    }
    path.with_suffix(".report.json").write_text(json.dumps(report, indent=2) + "\n")
    lines = [f"tune of {path}", "", "added:"]
    lines += [f"  {e}" for e in report["added"]] or ["  nothing"]
    lines += ["dropped:"] + ([f"  {e}" for e in report["dropped"]] or ["  nothing"])
    lines += ["end to end against the starting profile:"]
    lines += [
        f"  {c.name}: {c.delta_us:+.1f} ± "
        + ("?" if c.noise_us is None else f"{c.noise_us:.1f}")
        + " us"
        for c in checks.values()
    ] or ["  no version changed"]
    for key, value in found.items():
        lines += [f"{key}:", f"  {json.dumps(value, indent=2, default=str)}"]
    path.with_suffix(".report.txt").write_text("\n".join(lines) + "\n")
