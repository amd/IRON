# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure the cost table Llama's decode step is tuned by, on this NPU.

``npu.py --cost-table TABLE`` narrows the decode step's designs and packs
them into shared device configurations by what each costs on the device
(:class:`~iron.common.graph.narrowing.JointNarrowing`). A table holds every
design's step time at each width it tunes to, and the configure cost
measured between a few pairs of designs. It is keyed by each design's
identity -- its code and parameters -- so a design that has changed since
is not in it, and the tuner leaves that design as written. This measures
one for the decode step as the graph is now: every design, each width.

``decode_costs_npu2.json`` beside this file is such a table, measured on a
Strix Halo NPU (8 columns) in turbo power mode. Designs already in the
table are kept unless ``--remeasure``; entries for designs the graph no
longer has are dropped.

Run with XRT sourced and the NPU otherwise idle::

    python -m iron.applications.llama_3_2_1b.tune model.safetensors tokenizer.model
"""

import argparse
import time
from pathlib import Path

import aie.utils as aie_utils

from iron.common.graph.narrowing import CostTable, Runlist, cost_key, variants
from iron.common.graph.probe import Timing, calibrate, measure_steps, pmode
from iron.common.graph.trace import TracedGraph

from .graphs import LlamaGraph
from .harness import LlamaConfig
from .npu import MAX_SEQ_LEN

DEFAULT_TABLE = Path(__file__).parent / "decode_costs_npu2.json"

# The configure cost is measured between small single-column designs, at
# their narrowest: one design's configure then costs least beside the fixed
# part the calibration isolates.
CALIBRATION_PAIRS = [
    ("ElementwiseAdd", "ElementwiseMul"),
    ("ElementwiseAdd", "SiLU"),
    ("SiLU", "ElementwiseMul"),
]


def per_call_values(traced: TracedGraph, op, graph_values: dict[str, int]):
    """The per-call values ``op`` is written in a call with ``graph_values``,
    by member name: what the probe measures it at."""
    return {
        b.member.name: b.expression.evaluate(graph_values)
        for b in traced.bindings
        if b.op is op
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("weights_path", type=str)
    parser.add_argument("tokenizer_path", type=str)
    parser.add_argument("--table", type=Path, default=DEFAULT_TABLE)
    parser.add_argument(
        "--position",
        type=int,
        default=256,
        help="the decode position designs are measured at: what their "
        "per-call values follow from (default: 256)",
    )
    parser.add_argument(
        "--token", type=int, default=0, help="the token the step embeds (default: 0)"
    )
    parser.add_argument("--rounds", type=int, default=8)
    parser.add_argument("--calls", type=int, default=50)
    parser.add_argument(
        "--repeats",
        type=int,
        default=9,
        help="steps per long run; a step's time is the long run's excess over "
        "a run of one, per extra step (default: 9)",
    )
    parser.add_argument(
        "--remeasure",
        action="store_true",
        help="measure designs and calibrations already in the table again",
    )
    args = parser.parse_args()

    dev = aie_utils.get_current_device()
    print(f"power mode: {pmode()}")
    config = LlamaConfig(args.weights_path, args.tokenizer_path)
    traced = LlamaGraph(config, MAX_SEQ_LEN).trace(config, 1)
    graph_values = dict(position=args.position, token=args.token)
    keys = [cost_key(s.op) for s in traced.steps]
    first = {}
    for key, step in zip(keys, traced.steps):
        first.setdefault(key, step.op)
    order = Runlist(keys).order
    found = {key: variants(first[key], dev) for key in order}

    table = CostTable(args.table)
    current = {v.key for vs in found.values() for v in vs}
    stale = [k for k in table.steps if k not in current]
    for k in stale:
        del table.steps[k]
    if stale:
        print(f"dropped {len(stale)} designs the graph no longer has")
    timing = Timing(args.rounds, args.calls)

    for i, key in enumerate(order):
        op = first[key]
        name = type(op).__name__
        if not args.remeasure and all(v.key in table.steps for v in found[key]):
            print(f"[{i}] {name}: in the table")
            continue
        values = per_call_values(traced, op, graph_values)
        start = time.time()
        costs = measure_steps(table, found[key], timing, args.repeats, values)
        table.save()
        print(f"[{i}] {name} ({time.time() - start:.0f}s) at {values}")
        for v in found[key]:
            c = costs[v.key]
            print(
                f"    {dict(v.widths)}: t_step {c.t_step_us:8.2f} us  "
                f"alone {c.alone_us:8.2f} us  exact {c.exact}"
            )

    # Each pair's first designs of those classes, at their narrowest.
    by_class = {}
    for key in order:
        by_class.setdefault(type(first[key]).__name__, found[key][-1])
    pairs = [(by_class[a], by_class[b]) for a, b in CALIBRATION_PAIRS]
    wanted = {f"{a.key}|{b.key}" for a, b in pairs}
    for k in [k for k in table.calibrations if k not in wanted]:
        del table.calibrations[k]
    for (a, b), (name_a, name_b) in zip(pairs, CALIBRATION_PAIRS):
        if not args.remeasure and f"{a.key}|{b.key}" in table.calibrations:
            print(f"calibration {name_a}/{name_b}: in the table")
            continue
        cal = calibrate(table, a.op, b.op, timing)
        table.save()
        print(
            f"calibration {name_a}/{name_b}: D0 {cal.dispatch_us:.1f}  "
            f"R {cal.reset_us:.1f}  base {cal.base_us:.1f}  "
            f"switch {cal.switch_us:.1f} us"
        )
    table.save()


if __name__ == "__main__":
    main()
