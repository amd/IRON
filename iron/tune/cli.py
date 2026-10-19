# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tuning on this NPU from the command line.

A model's profile is tuned by a module built on this one: it takes
``parser``, adds the arguments its calls follow from, traces the calls
(``autotune.Call``) and passes them to ``tune`` with its profiles'
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
from collections.abc import Sequence
from pathlib import Path

from iron import operators
from iron.common.declare import Profile
from iron.common.image.packaging import dispatches_full_elf, require_device
from .autotune import Call, Shape, autotune, kernel_cycles, time_shape
from .measure import Cache, Timing, pmode


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


def tune(args: argparse.Namespace, calls: Sequence[Call], profiles: Path) -> Path:
    """Rewrite ``profiles/<device>.json`` with the settings ``calls`` time
    fastest at (``autotune``), timed as ``args`` says; return its path.
    """
    print(f"power mode: {pmode()}", flush=True)
    dev = require_device()
    path = profiles / f"{dev.name}.json"
    profile = Profile.load(path) if path.exists() else None
    tuned = autotune(
        calls,
        dev,
        profile,
        full_elf=dispatches_full_elf(dev),
        cycles=kernel_cycles(dev),
        **_timing(args),
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    tuned.save(path)
    print(f"wrote {path}")
    return path


def main() -> None:
    """Time one operator at each of its settings and print them."""
    p = parser("Time one operator at every setting it tunes to")
    p.add_argument("operator", choices=operators.__all__)
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

    cls = getattr(operators, args.operator)
    dev = require_device()
    op = cls(**fields)
    shape = Shape(op)
    shape.members.append((op, [(1.0, values)], {}))
    print(f"power mode: {pmode()}")
    tried = time_shape(
        shape,
        dev,
        full_elf=dispatches_full_elf(dev),
        cycles=kernel_cycles(dev),
        **_timing(args),
    )
    for t in sorted(tried, key=lambda t: t.delta_us):
        noise = "" if t.noise_us is None else f" ± {t.noise_us:.2f}"
        why = "" if t.refused is None else f"  refused: {t.refused}"
        mark = "  (traced)" if t is tried[0] else ""
        print(f"{t.tunables}: {t.delta_us:+9.2f}{noise} us{mark}{why}")


if __name__ == "__main__":
    main()
