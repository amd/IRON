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
one for the decode step as the graph is now: every design, each width,
and every design a legal fold makes (:mod:`iron.common.graph.fold`), which
the tuner otherwise prices at the design it came from. Each packaging the
device runs is calibrated (:mod:`iron.common.image.packaging`).

``decode_costs_npu2.json`` beside this file is such a table, measured on a
Strix Halo NPU (8 columns) in turbo power mode. Designs already in the
table are kept unless ``--remeasure``; entries for designs the graph no
longer has are dropped.

Run with XRT sourced and the NPU otherwise idle::

    python -m iron.applications.llama_3_2_1b.tune model.safetensors tokenizer.model
"""

import argparse
import time
from collections.abc import Mapping
from pathlib import Path

import aie.utils as aie_utils
import numpy as np

from iron.common.graph.fold import FoldAll
from iron.common.graph.handle import Handle
from iron.common.graph.narrowing import CostTable, Runlist, cost_key, variants
from iron.common.graph.probe import (
    Timing,
    calibrate,
    calibrate_each_step,
    measure_each_step,
    measure_steps,
    pmode,
)
from iron.common.graph.trace import TracedGraph
from iron.common.image.packaging import EACH_STEP, FUSED, device_support, modes

from .graphs import LlamaGraph
from .harness import SEED, LlamaConfig
from .npu import MAX_SEQ_LEN
from .sampling import Sampler

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


def per_call_inputs(
    traced: TracedGraph, op, contents: Mapping[Handle, np.ndarray]
) -> dict[str, np.ndarray]:
    """What ``op``'s buffers hold in a call where the graph's buffers hold
    ``contents``, by buffer name: what the probe fills them with."""
    return {
        buf.name: contents[handle]
        for step in traced.steps
        if step.op is op
        for buf, handle in zip(op.buffers, step.slots)
        if handle in contents
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
        "--no-folds",
        action="store_true",
        help="measure only the graph as written; by default the designs every "
        "legal fold makes are measured too, so the tuner prices a fold measured "
        "rather than estimated (and a table kept without them drops them)",
    )
    parser.add_argument(
        "--remeasure",
        action="store_true",
        help="measure designs and calibrations already in the table again",
    )
    args = parser.parse_args()

    dev = aie_utils.ensure_current_device()
    print(f"power mode: {pmode()}")
    config = LlamaConfig(args.weights_path, args.tokenizer_path)
    graph = LlamaGraph(config, MAX_SEQ_LEN)
    traced = graph.trace(config, 1)
    graph_values = dict(position=args.position, token=args.token)
    # Sample's work follows its draw row's temperature and top-k: measure it
    # at the rows generation writes, not at random words.
    sampler = Sampler(config.temperature, config.top_k, np.random.default_rng(SEED))
    _, draws = traced.states[id(graph.draws)]
    contents = {draws: sampler.rows(MAX_SEQ_LEN, graph.k_max)}
    graphs = [traced] + ([] if args.no_folds else [FoldAll().fold(traced, dev)])
    # Each design, and the graph whose bindings and contents it is measured at.
    first: dict[str, tuple[TracedGraph, object]] = {}
    keys = []
    for g in graphs:
        for step in g.steps:
            key = cost_key(step.op)
            keys.append(key)
            first.setdefault(key, (g, step.op))
    order = Runlist(keys).order
    found = {key: variants(first[key][1], dev) for key in order}

    table = CostTable(args.table)
    current = {v.key for vs in found.values() for v in vs}
    stale = [k for k in table.steps if k not in current]
    for k in stale:
        del table.steps[k]
    if stale:
        print(f"dropped {len(stale)} designs the graph no longer has")
    timing = Timing(args.rounds, args.calls)

    for i, key in enumerate(order):
        g, op = first[key]
        name = type(op).__name__
        if not args.remeasure and all(v.key in table.steps for v in found[key]):
            print(f"[{i}] {name}: in the table")
            continue
        values = per_call_values(g, op, graph_values)
        inputs = per_call_inputs(g, op, contents)
        start = time.time()
        costs = measure_steps(table, found[key], timing, args.repeats, values, inputs)
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
        by_class.setdefault(type(first[key][1]).__name__, found[key][-1])
    pairs = [(by_class[a], by_class[b]) for a, b in CALIBRATION_PAIRS]
    # Every packaging the device runs has boundaries of its own to measure.
    allowed = modes(device_support(dev), traced)
    measure = {FUSED: calibrate, EACH_STEP: calibrate_each_step}
    wanted = {
        CostTable.calibration_key(mode, (a.key, b.key))
        for mode in allowed
        for a, b in pairs
    }
    for k in [k for k in table.calibrations if k not in wanted]:
        del table.calibrations[k]
    for mode in allowed:
        for (a, b), (name_a, name_b) in zip(pairs, CALIBRATION_PAIRS):
            key = CostTable.calibration_key(mode, (a.key, b.key))
            if not args.remeasure and key in table.calibrations:
                print(f"{mode.name} calibration {name_a}/{name_b}: in the table")
                continue
            cal = measure[mode](table, a.op, b.op, timing)
            table.save()
            print(
                f"{mode.name} calibration {name_a}/{name_b}: dispatch "
                f"{cal.dispatch_us:.1f}  R {cal.reset_us:.1f}  base "
                f"{cal.base_us:.1f}  switch {cal.switch_us:.1f} us"
            )
    # A step dispatched alone costs its array's configuration each time the
    # design changes, which grows with the array: measured per design, at the
    # width a per-step dispatch runs it (its default), against the first pair.
    if EACH_STEP in allowed:
        reference = (pairs[0][0].op, pairs[0][1].op)
        for i, key in enumerate(order):
            g, op = first[key]
            default = found[key][0]
            if not args.remeasure and table.steps[default.key].each_step_us is not None:
                continue
            values = per_call_values(g, op, graph_values)
            inputs = per_call_inputs(g, op, contents)
            got = measure_each_step(
                table, [default.op], reference, timing, values=values, inputs=inputs
            )
            table.save()
            print(f"[{i}] {type(op).__name__}: each_step {got[default.key]:8.1f} us")
    table.save()


if __name__ == "__main__":
    main()
