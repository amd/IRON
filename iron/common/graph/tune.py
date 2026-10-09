# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measuring costs on this NPU from the command line.

A graph's cost table is filled by a module of its own (``iron.lm.llama3.tune``):
it takes ``parser``, adds the arguments its calls follow from, builds each
version's calls (``probe.Call.admitted``) and passes them to ``measure``
with the directory its tables are in: one per device, ``costs_<device>.json``
for the packaging the device runs, ``costs_<device>_<dispatch>.json`` for
another.

One operator is measured at every setting it tunes to by this module's own
command line, its fields as a profile entry names them:

```bash
python -m iron.common.graph.tune GEMV M=2048 K=8192
python -m iron.common.graph.tune Softmax rows=32 cols=2048 --value valid_cols=1500
```

Run with XRT sourced and the NPU otherwise idle.
"""

import argparse
import functools
import json
import tempfile
from collections.abc import Sequence
from pathlib import Path

import aie.utils as aie_utils

from ... import operators
from ..image.packaging import full_elf
from .narrowing import DISPATCHES, CostTable, fitting, variants
from .probe import Call, Timing, cost_cache, measure_graph, pmode, search


def parser(description: str, tables: Path | None) -> argparse.ArgumentParser:
    """The arguments every measurement takes: the table to fill (by default
    the device's in ``tables``, ``table``; a scratch one if None) and how
    each figure is timed.
    """
    p = argparse.ArgumentParser(description=description)
    p.add_argument(
        "--table",
        type=Path,
        help="the table to fill (default: "
        + (
            f"costs_<device>[_<dispatch>].json in {tables}"
            if tables
            else "a scratch table"
        )
        + ")",
    )
    p.add_argument(
        "--dispatch",
        choices=DISPATCHES,
        help="the packaging measured under: fused (one full ELF) or separate "
        "(an xclbin dispatch per step); default: fused where the device runs "
        "a full ELF",
    )
    p.add_argument("--rounds", type=int, default=8)
    p.add_argument("--calls", type=int, default=50)
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
        help="measure designs and calibrations already in the table or the "
        "cost cache again",
    )
    return p


def dispatch(args: argparse.Namespace, dev) -> str:
    """The packaging ``args`` measures under on ``dev``."""
    if args.dispatch is not None:
        return args.dispatch
    return "fused" if full_elf(dev) else "separate"


def table(args: argparse.Namespace, dev, tables: Path) -> Path:
    """The table ``args`` fills on ``dev``: ``args.table``, else in
    ``tables`` ``costs_<device>.json``, or ``costs_<device>_<dispatch>.json``
    where ``args`` measures under a packaging other than the device's.
    """
    if args.table is not None:
        return args.table
    chosen = dispatch(args, dev)
    own = "fused" if full_elf(dev) else "separate"
    return tables / (
        f"costs_{dev.name}.json" if chosen == own else f"costs_{dev.name}_{chosen}.json"
    )


def measure(
    args: argparse.Namespace,
    calls: Sequence[Call],
    triangle: tuple[str, str, str],
    tables: Path,
) -> list[str]:
    """Fill the table ``args`` names in ``tables`` (``table``) with
    ``calls``' designs and the configure cost between each pair of
    ``triangle``'s operator classes (``measure_graph``), timed as ``args``
    says.
    """
    print(f"power mode: {pmode()}", flush=True)
    dev = aie_utils.ensure_current_device()
    return measure_graph(
        CostTable(
            table(args, dev, tables),
            dev.name,
            dispatch(args, dev),
            remeasure_stale=True,
        ),
        calls,
        triangle,
        Timing(args.rounds, args.calls, args.settle, args.cutoff),
        args.repeats,
        args.remeasure,
        # Hours long and usually redirected: each line lands as it is logged.
        log=functools.partial(print, flush=True),
    )


def main() -> None:
    """Measure one operator at each of its settings and print them."""
    p = parser("Measure one operator at every setting it tunes to", None)
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

    dev = aie_utils.ensure_current_device()
    op = getattr(operators, args.operator)(**fields)
    found, refused = fitting(variants(op.probed(), dev))
    print(f"power mode: {pmode()}; {len(found)} settings")
    for key, why in refused.items():
        first_line, _, _ = why.partition("\n")
        print(f"not measured, the placer refuses {key}: {first_line}")
    with tempfile.TemporaryDirectory() as scratch:
        costs = CostTable(
            args.table or Path(scratch) / "costs.json",
            dev.name,
            dispatch(args, dev),
            remeasure_stale=True,
        )
        search(
            costs,
            found,
            Timing(args.rounds, args.calls, args.settle, args.cutoff),
            args.repeats,
            values,
            None,
            cost_cache(),
            args.remeasure,
        )
        if args.table:
            costs.save()
        measured = [v for v in found if v.key in costs.steps]
        for v in sorted(measured, key=lambda v: costs.steps[v.key].t_step_us):
            c = costs.steps[v.key]
            print(
                f"{dict(v.tunables)}: t_step {c.t_step_us:8.2f} us  "
                f"alone {c.alone_us:8.2f} us  exact {c.exact}  accurate {c.accurate}"
                + ("  (default)" if v is found[0] else "")
            )


if __name__ == "__main__":
    main()
