# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measuring costs on this NPU from the command line.

A graph's cost table is filled by a module of its own (``iron.lm.llama3.tune``):
it takes ``parser``, adds the arguments its calls follow from, builds each
version's calls (``probe.Call.admitted``) and passes them to ``measure``.

One operator is measured at every setting it tunes to by this module's own
command line, its fields as a profile entry names them:

```bash
python -m iron.common.graph.tune GEMV M=2048 K=8192
python -m iron.common.graph.tune Softmax rows=32 cols=2048 --value valid_cols=1500
```

Run with XRT sourced and the NPU otherwise idle.
"""

import argparse
import json
import tempfile
from collections.abc import Sequence
from pathlib import Path

import aie.utils as aie_utils

from ... import operators
from .narrowing import CostTable, fitting, variants
from .probe import Call, Timing, cost_cache, measure_graph, pmode, search


def parser(description: str, table: Path | None) -> argparse.ArgumentParser:
    """The arguments every measurement takes: the table to fill (``table``
    by default; a scratch one if None) and how each figure is timed.
    """
    p = argparse.ArgumentParser(description=description)
    p.add_argument(
        "--table",
        type=Path,
        default=table,
        help=f"the table to fill (default: {table or 'a scratch table'})",
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


def measure(
    args: argparse.Namespace, calls: Sequence[Call], pairs: Sequence[tuple[str, str]]
) -> list[str]:
    """Fill ``args.table`` with ``calls``' designs and the configure cost
    between ``pairs`` (``measure_graph``), timed as ``args`` says.
    """
    print(f"power mode: {pmode()}")
    return measure_graph(
        CostTable(args.table),
        calls,
        pairs,
        Timing(args.rounds, args.calls, args.settle, args.cutoff),
        args.repeats,
        args.remeasure,
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
        table = CostTable(args.table or Path(scratch) / "costs.json")
        search(
            table,
            found,
            Timing(args.rounds, args.calls, args.settle, args.cutoff),
            args.repeats,
            values,
            None,
            cost_cache(),
            args.remeasure,
        )
        if args.table:
            table.save()
        measured = [v for v in found if v.key in table.steps]
        for v in sorted(measured, key=lambda v: table.steps[v.key].t_step_us):
            c = table.steps[v.key]
            print(
                f"{dict(v.tunables)}: t_step {c.t_step_us:8.2f} us  "
                f"alone {c.alone_us:8.2f} us  exact {c.exact}  accurate {c.accurate}"
                + ("  (default)" if v is found[0] else "")
            )


if __name__ == "__main__":
    main()
