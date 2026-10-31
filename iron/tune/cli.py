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
import functools
import json
from collections.abc import Callable, Sequence
from pathlib import Path

import aie.utils as aie_utils

from iron import operators
from iron.common.declare import Profile
from iron.common.image.packaging import require_device
from .autotune import Shape, Timed, autotune, kernel_cycles, time_shape
from .fusions import price_fusions
from .costmodel import CostModel
from .failures import Ledger
from .packings import price_folds_before_packing
from .measure import Cache, Timing, pmode, switch_cost
from .plan import coded_seed
from .verify import entries, verify, write_report


def parser(description: str) -> argparse.ArgumentParser:
    """The arguments every tuning takes: how each setting is timed."""
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
        "--lock-in-process",
        action="store_true",
        help="take the device lock here, per measurement, instead of "
        "relying on coord/npu to hold it for this whole process's life: "
        "for a sweep run without that wrapper, so another agent's short "
        "run is never kept waiting behind it. Never pass this while also "
        "running under coord/npu (nesting the two deadlocks both)",
    )
    return p


def _timing(args: argparse.Namespace) -> dict:
    return dict(
        timing=Timing(args.rounds, args.calls, args.settle, args.cutoff),
        repeats=args.repeats,
        cache=Cache.here(),
        remeasure=args.remeasure,
        # Hours long and usually redirected: each line lands as it is logged.
        log=functools.partial(print, flush=True),
    )


def tune(
    args: argparse.Namespace,
    record: Callable[[Profile], Sequence[Timed]],
    profiles: Path,
    validate: Callable[[Profile, Profile], dict] | None = None,
) -> Path:
    """Rewrite ``profiles/<device>.json``: from the planner's seed
    (``coded_seed``, kept per version where it gains on the starting
    profile), time the settings the calls run fastest at (``autotune``),
    price the fusions their graphs admit (``price_fusions``), then fold what
    their arrays admit and group the result into shared device
    configurations (``price_folds_before_packing``); ``--fusions-only``
    skips the first search and ``--packings-only`` the first two. What the
    search finds goes to ``<device>.found.json`` as it goes; what is saved
    is what ``verify`` keeps of it against the seed and then the starting
    profile, once it passes ``validate`` where given, reported beside it
    (``write_report``). Timed as ``args`` says; return its path.

    Args:
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
    seed = coded_seed(record, dev, start, log=log)
    if entries(seed) != entries(start):
        seed, _ = verify(record, dev, start, seed, log=log, lock=args.lock_in_process)
        seed.save(found_path)
        print(f"wrote {found_path}, the seed")
    profile = seed
    if not args.packings_only:
        if not args.fusions_only:
            profile = autotune(
                record(profile),
                dev,
                profile,
                full_elf=full_elf,
                cycles=kernel_cycles(dev),
                core_mhz=aie_utils.DefaultNPURuntime.core_mhz,
                **_timing(args),
            )
            profile.save(found_path)
            print(f"wrote {found_path}")
        priced = price_fusions(
            record(profile),
            dev,
            profile,
            full_elf=full_elf,
            checkpoint=path.with_suffix(".progress.json"),
            max_price=args.max_price,
            lock=args.lock_in_process,
            **_timing(args),
        )
        if priced is None:
            print(f"{path}: priced a batch; some groups still unpriced, call again")
            return path
        profile = priced
        profile.save(found_path)
        print(f"wrote {found_path}")
    profile = _save_packings(args, record(profile), dev, profile, found_path, full_elf)
    if entries(seed) != entries(start):
        log("checking the search against its seed")
        profile, _ = verify(
            record, dev, seed, profile, log=log, lock=args.lock_in_process
        )
    kept, checks = verify(
        record, dev, start, profile, log=log, lock=args.lock_in_process
    )
    found = (
        {} if validate is None or not checks else {"validate": validate(start, kept)}
    )
    kept.save(path)
    write_report(path, start, kept, checks, **found)
    print(f"wrote {path} and its report")
    return path


def _save_packings(
    args, calls: Sequence[Timed], dev, profile: Profile, path: Path, full_elf: bool
) -> Profile:
    """``profile`` with the folds and packings ``price_folds_before_packing``
    finds, written to ``path``. On an xclbin per step nothing packs, so no
    switch is timed to calibrate a cost model, nor one written.
    """
    model = CostModel.load(dev.name) if full_elf else None
    if full_elf and model is None:
        model = CostModel.calibrated(
            *switch_cost(
                dev,
                cache=Cache.here(),
                log=functools.partial(print, flush=True),
                lock=args.lock_in_process,
            )
        )
    path.parent.mkdir(parents=True, exist_ok=True)

    def progress(found: Profile, fitted: CostModel) -> None:
        found.save(path)
        fitted.save(dev.name)
        print(f"wrote {path} and the cost model so far", flush=True)

    packed = price_folds_before_packing(
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
        lock=args.lock_in_process,
    )
    if model is not None:
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
        **_timing(args),
    )
    for t in sorted(tried, key=lambda t: t.delta_us):
        noise = "" if t.noise_us is None else f" ± {t.noise_us:.2f}"
        why = "" if t.refused is None else f"  refused: {t.refused}"
        mark = "  (recorded)" if t is tried[0] else ""
        print(f"{t.tunables}: {t.delta_us:+9.2f}{noise} us{mark}{why}")


if __name__ == "__main__":
    main()
