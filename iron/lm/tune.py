# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure the cost table a model's decode step is tuned by, on this NPU.

``--cost-table TABLE`` on a model's command line (:func:`.runner.main`)
narrows the decode step's designs and packs them into shared device
configurations by what each costs on the device
(:class:`~iron.common.graph.narrowing.JointNarrowing`). A table holds every
design's step time at each width it tunes to, and the configure cost
measured between a few pairs of designs. It is keyed by each design's
identity -- its fields -- so a design that has changed since is not in it,
and the tuner leaves that design as the profile gives it. :func:`measure`
fills one for the decode step as the graph is now: every design, each
width. Designs already in the table are kept unless ``remeasure``; entries
for designs the graph no longer has are dropped.

A model's ``tune`` module calls :func:`main` with its runner; run it with
XRT sourced and the NPU otherwise idle.
"""

import argparse
import time
from collections.abc import Callable, Mapping
from pathlib import Path

import aie.utils as aie_utils
import numpy as np

from iron.common.declare import Operator
from iron.common.graph.narrowing import CostTable, Runlist, cost_key, variants
from iron.common.graph.probe import Timing, calibrate, measure_steps, pmode
from iron.common.graph.trace import TracedGraph
from iron.operators.sample import Sample

from .decoder import CausalLM
from .generation import SEED, Sampler
from .runner import Runner

# The configure cost is measured between small single-column designs, at
# their narrowest: one design's configure then costs least beside the fixed
# part the calibration isolates.
CALIBRATION_PAIRS = [
    ("ElementwiseAdd", "ElementwiseMul"),
    ("ElementwiseAdd", "SiLU"),
    ("SiLU", "ElementwiseMul"),
]


def per_call_values(
    traced: TracedGraph, op: Operator, graph_values: Mapping[str, int]
) -> dict[str, int]:
    """The per-call values ``op`` is written in a call with ``graph_values``,
    by member name: what the probe measures it at.
    """
    return {
        b.member.name: b.expression.evaluate(graph_values)
        for b in traced.bindings
        if b.op is op
    }


def per_call_inputs(
    traced: TracedGraph, op: Operator, contents: Mapping[str, np.ndarray]
) -> dict[str, np.ndarray]:
    """What ``op``'s buffers hold in a call where the graph's buffers hold
    ``contents``, by graph buffer name; by ``op``'s buffer name: what the
    probe fills them with.
    """
    return {
        buf.name: contents[name]
        for step in traced.steps
        if step.op is op
        for buf, name in zip(op.buffers, step.names)
        if name in contents
    }


def measure(
    model: CausalLM,
    table: CostTable,
    sample: Sampler,
    position: int,
    token: int,
    timing: Timing = Timing(),
    repeats: int = 9,
    remeasure: bool = False,
    log: Callable[[str], None] = print,
) -> None:
    """Measure ``model``'s decode step into ``table``, saved as it goes: each
    design at ``position`` and ``token``, Sample on the draw rows ``sample``
    gives, and the configure cost between :data:`CALIBRATION_PAIRS`.
    """
    dev = aie_utils.ensure_current_device(required=True)
    traced = model.trace(**model.shapes(1))
    graph_values = dict(position=position, token=token)
    # Sample's work follows its draw row's temperature and top-k: measure it
    # at the rows generation writes, not at random words.
    [k_max] = {s.op.k_max for s in traced.steps if isinstance(s.op, Sample)}
    _, draws = traced.states[id(model.draws)]
    contents: dict[str, np.ndarray] = {
        draws.name: sample.rows(model.config.max_seq_len, k_max)
    }
    keys = [cost_key(s.op) for s in traced.steps]
    first: dict[str, Operator] = {}
    for key, step in zip(keys, traced.steps):
        first.setdefault(key, step.op)
    order = Runlist(keys).order
    found = {key: variants(first[key], dev) for key in order}

    current = {v.key for vs in found.values() for v in vs}
    stale = [k for k in table.steps if k not in current]
    for k in stale:
        del table.steps[k]
    if stale:
        log(f"dropped {len(stale)} designs the graph no longer has")

    for i, key in enumerate(order):
        op = first[key]
        name = type(op).__name__
        if not remeasure and all(v.key in table.steps for v in found[key]):
            log(f"[{i}] {name}: in the table")
            continue
        values = per_call_values(traced, op, graph_values)
        inputs = per_call_inputs(traced, op, contents)
        start = time.time()
        costs = measure_steps(table, found[key], timing, repeats, values, inputs)
        table.save()
        log(f"[{i}] {name} ({time.time() - start:.0f}s) at {values}")
        for v in found[key]:
            c = costs[v.key]
            log(
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
        if not remeasure and f"{a.key}|{b.key}" in table.calibrations:
            log(f"calibration {name_a}/{name_b}: in the table")
            continue
        cal = calibrate(table, a.op, b.op, timing)
        table.save()
        log(
            f"calibration {name_a}/{name_b}: D0 {cal.dispatch_us:.1f}  "
            f"R {cal.reset_us:.1f}  base {cal.base_us:.1f}  "
            f"switch {cal.switch_us:.1f} us"
        )
    table.save()


def main(runner: type[Runner], description: str, default_table: Path) -> None:
    """The command line that measures ``runner``'s model's cost table."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("weights_path", help="the .safetensors checkpoint")
    parser.add_argument("tokenizer_path", help="the tokenizer's file")
    parser.add_argument(
        "--table",
        type=Path,
        default=default_table,
        help=f"the table to fill (default: {default_table})",
    )
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
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--top-k", type=int, default=50)
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

    print(f"power mode: {pmode()}")
    run = runner(args.weights_path, args.tokenizer_path)
    measure(
        run.model(run.config, run.weights),
        CostTable(args.table),
        Sampler(args.temperature, args.top_k, np.random.default_rng(SEED)),
        args.position,
        args.token,
        Timing(args.rounds, args.calls),
        args.repeats,
        args.remeasure,
    )
