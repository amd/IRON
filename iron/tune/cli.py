# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tuning on this NPU from the command line.

A model's profile is tuned by a module built on this one: it takes
``parser``, adds the arguments its calls follow from, records the calls
(``autotune.Timed``) and passes them to ``tune`` with its profiles'
directory, whose ``<device>.json`` it rewrites. A model's is ``iron.lm.tune``
(``python -m iron.lm.tune <application>``).

One operator is timed at every setting it tunes to by this module's own
command line, its fields as a profile entry names them:

```bash
python -m iron.tune.cli GEMV M=2048 K=8192
python -m iron.tune.cli Softmax rows=32 cols=2048 --value valid_cols=1500
```

Run with XRT sourced and the NPU otherwise idle.
"""

import argparse
import dataclasses
import functools
import json
import math
from collections.abc import Callable, Hashable, Sequence
from pathlib import Path

import aie.utils as aie_utils
from aie.utils.benchmark import other_npu_users

from iron import operators
from iron.common.declare import Profile
from iron.common.image.packaging import require_device

from .autotune import (
    SHAPE_SHARE,
    Point,
    Shape,
    Timed,
    autotune,
    coding_tunables,
    kernel_cycles,
    shapes,
    time_shape,
)
from .costmodel import CostModel
from .failures import Ledger
from .fusions import price_fusions
from .measure import Budget, Cache, NpuLock, Timing, measure, pmode, switch_cost
from .packings import price_folds_before_packing, price_packings
from .plan import coded_seed, searches
from .survey import Survey, step_points, step_times, survey
from .verify import Phases, entries, verify, write_report

# Where amdxdna keeps its parameters, its command timeout among them.
WATCHDOG = Path("/sys/module/amdxdna/parameters")

# The watchdog must allow this many times the longest command a tune times at
# the starting profile: a narrowed setting runs slower.
WATCHDOG_HEADROOM = 2.0


def parser(description: str) -> argparse.ArgumentParser:
    """Build the arguments every tuning takes: how each setting is timed."""
    p = argparse.ArgumentParser(description=description)
    p.add_argument("--rounds", type=int, default=Timing.rounds)
    p.add_argument("--calls", type=int, default=Timing.calls)
    p.add_argument(
        "--cutoff",
        type=float,
        default=Timing.cutoff,
        help="a setting this many times the fastest's run time is timed no "
        f"further after --settle rounds; inf times every round (default: "
        f"{Timing.cutoff})",
    )
    p.add_argument("--settle", type=int, default=Timing.settle)
    p.add_argument(
        "--first-cutoff",
        type=float,
        default=Timing.first_cutoff,
        help="a setting whose step takes this many times the fastest's in the "
        f"first round, the fastest at least {Timing.first_floor_us:.0f} us, is "
        f"timed no further; inf times it on (default: {Timing.first_cutoff})",
    )
    p.add_argument(
        "--repeats",
        type=int,
        default=9,
        help="steps per long run; a step's time is the long run's excess over "
        "a run of one, per extra step (default: 9)",
    )
    p.add_argument(
        "--remeasure",
        action="store_true",
        help="time settings the cache already holds again",
    )
    p.add_argument(
        "--fusions-only",
        action="store_true",
        help="price only the fusions a graph admits against the profile as "
        "it stands, skipping the (hours-long) tunable search",
    )
    p.add_argument(
        "--packings-only",
        action="store_true",
        help="fold what a graph's arrays admit and group the result into "
        "shared device configurations against the profile as it stands "
        "(price_folds_before_packing), skipping the tunable search and the "
        "fusions",
    )
    p.add_argument(
        "--hold",
        action="append",
        default=[],
        choices=sorted(operators.CATALOG),
        metavar="OPERATOR",
        help="an operator class whose shapes the tunable search leaves at the "
        "profile's settings (repeatable), as while its design is still changing",
    )
    p.add_argument(
        "--budget",
        type=float,
        metavar="SECONDS",
        help="the tune's wall-clock time: past the first round of each search, "
        "a search stops once the time left is under the share kept back to "
        "finish (measure.RESERVE_SHARE), keeping what it found, which the tune "
        "then checks, verifies and validates (default: no limit)",
    )
    p.add_argument(
        "--record-failures",
        action="store_true",
        help="keep each failure tuning hits (a compiler crash, a build, a "
        "hang, a version not bit-identical) in this machine's ledger, with "
        "a repro (python -m iron.tune.failures lists and rechecks them)",
    )
    p.add_argument(
        "--max-price",
        type=int,
        default=None,
        help="price at most this many fusion groups this call, then stop "
        "without selecting, confirming or saving (a caller holding the "
        "device lock for one call, not a whole multi-hour sweep, calls "
        "again for the rest)",
    )
    p.add_argument(
        "--npu-lock",
        type=NpuLock,
        metavar="PATH",
        help="flock PATH around each measurement, so another process taking "
        "the same lock never dispatches while this one's images are loaded "
        "(default: no lock); never one a wrapper of this process already holds",
    )
    return p


def _timing(args: argparse.Namespace) -> dict:
    return dict(
        timing=Timing(
            args.rounds, args.calls, args.settle, args.cutoff, args.first_cutoff
        ),
        repeats=args.repeats,
        cache=Cache.here(),
        remeasure=args.remeasure,
        lock=args.npu_lock,
        # Hours long and usually redirected: each line lands as it is logged.
        log=functools.partial(print, flush=True),
    )


def tune(
    args: argparse.Namespace,
    record: Callable[[Profile], Sequence[Timed]],
    profiles: Path,
    validate: Callable[[Profile, Profile], dict] | None = None,
) -> Path:
    """Rewrite ``profiles/<device>.json``, and return its path.

    From the planner's seed (``coded_seed``), times the calls' fastest settings
    (``autotune``), prices the fusions their graphs admit (``price_fusions``), then
    folds and packs what their arrays admit (``price_folds_before_packing``);
    ``--fusions-only`` skips the first search and ``--packings-only`` the first two.
    Saves what ``verify`` keeps against the seed and the starting profile, once it
    passes ``validate`` where given, with a report of each phase's seconds and gain
    (``write_report``).

    Args:
        args: The command line: how settings are timed, and which searches it skips.
        profiles: The directory whose ``<device>.json`` the tune starts from and
            rewrites.
        record: The calls, recorded under a profile: each stage records
            them under the profile the last one found.
        validate: The model's own battery, the starting profile against the
            one to save, returning its report; it raises where the profile
            must not be saved.
    """
    print(f"power mode: {pmode()}", flush=True)
    dev = require_device()
    path = profiles / f"{dev.name}.json"
    start = Profile.load(path) if path.exists() else Profile()
    found_path = path.with_suffix(".found.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    full_elf = dev.can_dispatch_full_elf
    log = functools.partial(print, flush=True)
    preflight(
        record,
        start,
        dev,
        timing=_timing(args)["timing"],
        repeats=args.repeats,
        cache=Cache.here(),
        log=log,
        lock=args.npu_lock,
    )
    budget = Budget(args.budget, log)
    lock = args.npu_lock
    cycles = kernel_cycles(dev)
    core_mhz = aie_utils.DefaultNPURuntime.core_mhz
    model = _cost_model(args, dev)
    # Every end-to-end check's figures by pair of builds and point: the search's,
    # the phases' and the final verify's, so a pair is timed once a point.
    memo: dict = {}
    # A phase is checked at each call's shortest point, the final verify at every
    # point: a deep context's call takes seconds before attention is tuned.

    def first_point(profile: Profile) -> list[Timed]:
        return [c.shortest() for c in record(profile)]

    checks_at = dict(log=log, lock=lock, memo=memo, cap_s=budget.check_s)
    with Phases(first_point, dev, start, **checks_at) as phases:
        seed = coded_seed(record, dev, start, log=log)
        if entries(seed) != entries(start):
            seed, _ = verify(first_point, dev, start, seed, **checks_at)
            seed.save(found_path)
            print(f"wrote {found_path}, the seed")
        phases.end("seed", seed)
        coded_shapes = {
            Shape(s.op).key
            for c in record(seed)
            for s in c.recording.steps
            if any(vars(s.op)[n] for n in coding_tunables(s.op))
        }
        surveys = _surveys(
            args, record, start, dev, model, coded_shapes, cycles, core_mhz, log
        )
        plan = {s.name: s for s in searches(surveys)}
        for planned in plan.values():
            log(
                f"{planned.name}: {'searched' if planned.runs else 'skipped'}, "
                f"{planned.why}"
            )
        phases.end("survey", seed)
        profile = seed
        if not args.packings_only and not args.fusions_only:
            # A shape's share is of the version as it stands: once the costliest
            # are tuned, the rest weigh more, so survey again until none newly
            # reaches SHAPE_SHARE.
            searched: set[Hashable] = set()
            while not (searched and budget.ends("the tunable search")):
                # A read-bound shape is held to the fastest read any version shows.
                rate = max(s.read_rate for s in surveys)
                shares: dict[Hashable, float] = {}
                for surveyed in surveys:
                    for key, share in surveyed.shares(rate).items():
                        shares[key] = max(shares.get(key, 0.0), share)
                held = {
                    s.key
                    for s in shapes(record(profile), dev)
                    if issubclass(s.cls, tuple(operators.CATALOG[n] for n in args.hold))
                }
                fresh = {
                    k: v
                    for k, v in shares.items()
                    if v >= SHAPE_SHARE and k not in searched and k not in held
                }
                if held:
                    log(f"{len(held)} shape(s) of {', '.join(args.hold)} held")
                if not fresh:
                    break
                profile = autotune(
                    record(profile),
                    dev,
                    profile,
                    full_elf=full_elf,
                    cycles=cycles,
                    core_mhz=core_mhz,
                    shares=fresh,
                    ledger=Ledger() if args.record_failures else None,
                    **_timing(args),
                )
                searched |= fresh.keys()
                profile.save(found_path)
                print(f"wrote {found_path}")
                surveys = _surveys(
                    args,
                    record,
                    profile,
                    dev,
                    model,
                    coded_shapes,
                    cycles,
                    core_mhz,
                    log,
                )
                phases.end(f"autotune of {len(fresh)} shape(s)", profile)
        if plan["packing"].runs or plan["folds"].runs:
            profile = _save_packings(
                args,
                record(profile),
                dev,
                profile,
                found_path,
                full_elf,
                model,
                folds=plan["folds"].runs,
                budget=budget,
                memo=memo,
            )
            phases.end(
                "folds and packing" if plan["folds"].runs else "packing", profile
            )
        # Fusions are priced on the packed versions: one that splits what a
        # packing groups is dropped where the packed version does not gain.
        if (
            not args.packings_only
            and plan["fusions"].runs
            and not budget.ends("the fusion search")
        ):
            priced = price_fusions(
                record(profile),
                dev,
                profile,
                full_elf=full_elf,
                checkpoint=path.with_suffix(".progress.json"),
                max_price=args.max_price,
                budget=budget,
                **_timing(args),
            )
            if priced is None:
                print(f"{path}: priced a batch; some groups still unpriced, call again")
                return path
            profile = priced
            profile.save(found_path)
            print(f"wrote {found_path}")
            phases.end("fusions", profile)
        if entries(seed) != entries(start):
            log("checking the search against its seed")
            # At each call's shortest point, as a phase: the final verify, against the
            # starting profile, times every point.
            profile, _ = verify(first_point, dev, seed, profile, **checks_at)
        kept, checks = verify(record, dev, start, profile, **checks_at)
        phases.end("verify", kept)
        battery = (
            {}
            if validate is None or not checks
            else {"validate": validate(start, kept)}
        )
        phases.end("validate", kept)
    kept.save(path)
    write_report(
        path,
        start,
        kept,
        checks,
        phases=phases.done,
        survey=[s.lines() for s in surveys],
        plan=[dataclasses.asdict(s) for s in plan.values()],
        **battery,
        **(
            {}
            if args.budget is None
            else {"budget": {"seconds": args.budget, "stopped": budget.stopped}}
        ),
    )
    print(f"wrote {path} and its report")
    return path


def watchdog_s(directory: Path = WATCHDOG) -> float | None:
    """Return the driver's command timeout in ``directory``, seconds; None where it is not readable.

    amdxdna's ``tdr_timeout_ms`` on newer drivers, ``timeout_in_sec`` on older.
    """
    for name, seconds in (("tdr_timeout_ms", 1e-3), ("timeout_in_sec", 1.0)):
        try:
            return int((directory / name).read_text()) * seconds
        except (OSError, ValueError):
            continue
    return None


def preflight(
    record: Callable[[Profile], Sequence[Timed]],
    profile: Profile,
    dev,
    *,
    timing: Timing,
    repeats: int,
    cache: Cache | None,
    log: Callable[[str], None] = print,
    lock: NpuLock | None = None,
    watchdog: Path = WATCHDOG,
) -> None:
    """Refuse, before any search, a tune this host cannot finish.

    The calls must record under ``profile`` (a model sizes them to hold two builds
    in memory, and raises where even one prompt chunk does not fit), the NPU must be
    idle (``other_npu_users``), and the driver's watchdog (``watchdog_s``)
    must allow ``WATCHDOG_HEADROOM`` times the longest command a call issues at its
    last point: on a full ELF the whole call, else its longest step, each step's
    standalone time (``measure``, cached for the tune).

    Raises:
        SystemExit: Naming what to change.
    """
    try:
        calls = record(profile)
    except ValueError as e:
        raise SystemExit(
            f"pre-flight: the calls, sized to hold the two builds a tune checks, do "
            f"not record on this host: {e}"
        ) from e
    held = other_npu_users()
    if held:
        raise SystemExit(
            f"pre-flight: pid {sorted(held)} holds the NPU; tune with it otherwise idle"
        )
    full_elf = dev.can_dispatch_full_elf
    longest_us = 0.0
    for call in calls:
        last = [Point(1.0, call.points[-1].values)] if call.points else []
        at = dataclasses.replace(call, points=last)
        steps = [
            measure(
                [op],
                full_elf=full_elf,
                timing=timing,
                repeats=repeats,
                values=values,
                inputs=inputs,
                cache=cache,
                log=log,
                lock=lock,
            )[0].t_step_us
            for op, points, inputs in step_points(at, profile, dev)
            for _, values in points
        ]
        longest_us = max(longest_us, sum(steps) if full_elf else max(steps))
    limit = watchdog_s(watchdog)
    longest = (
        f"the longest command this tune issues takes about {longest_us / 1e6:.2f} s"
    )
    if limit is None:
        log(f"pre-flight: {watchdog} holds no readable watchdog; {longest}")
        return
    if limit < WATCHDOG_HEADROOM * longest_us / 1e6:
        raise SystemExit(
            f"pre-flight: the driver's watchdog is {limit:g} s and {longest}, "
            f"under {WATCHDOG_HEADROOM:g}x it; raise it (as root: echo "
            f"{math.ceil(WATCHDOG_HEADROOM * longest_us / 1e3)} > "
            f"{watchdog / 'tdr_timeout_ms'}, or timeout_in_sec on an older driver)"
        )
    log(f"pre-flight: watchdog {limit:g} s; {longest}")


def _surveys(
    args, record, profile: Profile, dev, model, coded_shapes, cycles, core_mhz, log
) -> list[Survey]:
    """Survey each version of the calls as ``profile`` builds it (``survey``), logged."""
    out = []
    for call in record(profile):
        times = step_times(
            call,
            profile,
            dev,
            full_elf=dev.can_dispatch_full_elf,
            timing=_timing(args)["timing"],
            repeats=args.repeats,
            cache=Cache.here(),
            log=log,
            lock=args.npu_lock,
        )
        found = survey(
            call,
            profile,
            dev,
            times,
            model,
            coded_shapes,
            cycles,
            core_mhz,
        )
        out.append(found)
        log("\n".join(found.lines()))
    return out


def _cost_model(args, dev) -> CostModel:
    """``dev``'s cost model, calibrated on a timed switch where none is kept."""
    model = CostModel.load(dev.name)
    if model is None:
        model = CostModel.calibrated(
            *switch_cost(
                dev,
                cache=Cache.here(),
                log=functools.partial(print, flush=True),
                lock=args.npu_lock,
            )
        )
    return model


def _save_packings(
    args,
    calls: Sequence[Timed],
    dev,
    profile: Profile,
    path: Path,
    full_elf: bool,
    model: CostModel,
    folds: bool = True,
    budget: Budget | None = None,
    memo: dict | None = None,
) -> Profile:
    """``profile`` with the packings ``price_packings`` finds within ``budget``.

    And with ``folds`` the folds ``price_folds_before_packing`` keeps, written to
    ``path`` with ``model`` as it refits it; its end-to-end checks read and add to
    ``memo``.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    def progress(found: Profile, fitted: CostModel) -> None:
        found.save(path)
        fitted.save(dev.name)
        print(f"wrote {path} and the cost model so far", flush=True)

    search = price_folds_before_packing if folds else price_packings
    packed = search(
        calls,
        dev,
        profile,
        full_elf=full_elf,
        timing=_timing(args)["timing"],
        repeats=args.repeats,
        cache=Cache.here(),
        model=model,
        ledger=Ledger() if args.record_failures else None,
        cycles=kernel_cycles(dev),
        core_mhz=aie_utils.DefaultNPURuntime.core_mhz,
        progress=progress,
        log=functools.partial(print, flush=True),
        lock=args.npu_lock,
        budget=budget,
        memo=memo,
    )
    print(f"wrote {model.save(dev.name)}")
    packed.save(path)
    print(f"wrote {path}")
    return packed


def main() -> None:
    """Time one operator at each of its settings and print them."""
    p = parser("Time one operator at every setting it tunes to")
    p.add_argument("operator", choices=operators.CATALOG)
    p.add_argument(
        "fields",
        nargs="*",
        metavar="NAME=VALUE",
        help="what the operator is made with, each value JSON or a bare "
        "string; a tunable given here is held, not searched",
    )
    p.add_argument(
        "--value",
        action="append",
        default=[],
        metavar="NAME=INT",
        help="a per-call value the operator is written at",
    )
    args = p.parse_args()
    fields = {}
    for item in args.fields:
        name, _, text = item.partition("=")
        try:
            fields[name] = json.loads(text)
        except json.JSONDecodeError:
            fields[name] = text
    values = {
        name: int(text) for name, _, text in (v.partition("=") for v in args.value)
    }

    cls = operators.CATALOG[args.operator]
    dev = require_device()
    op = cls(**fields)
    shape = Shape(op)
    shape.members.append((op, [(1.0, values)], {}))
    print(f"power mode: {pmode()}")
    tried = time_shape(
        shape,
        dev,
        full_elf=dev.can_dispatch_full_elf,
        cycles=kernel_cycles(dev),
        core_mhz=aie_utils.DefaultNPURuntime.core_mhz,
        ledger=Ledger() if args.record_failures else None,
        **_timing(args),
    )
    for t in sorted(tried, key=lambda t: t.delta_us):
        noise = "" if t.noise_us is None else f" ± {t.noise_us:.2f}"
        why = "" if t.refused is None else f"  refused: {t.refused}"
        mark = "  (recorded)" if t is tried[0] else ""
        print(f"{t.tunables}: {t.delta_us:+9.2f}{noise} us{mark}{why}")


if __name__ == "__main__":
    main()
