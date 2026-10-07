# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure the cost table a model's decode step is tuned by, on this NPU.

``--cost-table TABLE`` on a model's command line (``main``)
narrows the decode step's designs and packs them into shared device
configurations by what each costs on the device
(``JointNarrowing``). A table holds every
design's step time at each width it tunes to, and the configure cost
measured between a few pairs of designs. It is keyed by each design's
identity -- its fields -- so a design that has changed since is not in it,
and the tuner leaves that design as the profile gives it. ``measure``
fills one for the decode step as the graph is now: every design, each
width. Designs already in the table are kept unless ``remeasure``; entries
for designs the graph no longer has are dropped. A design another graph has
had measured on this NPU is taken from the cost cache
(``iron.common.graph.costcache``) rather than run again.

A model's ``tune`` module calls ``main`` with its runner; run it with
XRT sourced and the NPU otherwise idle.
"""

import argparse
from collections.abc import Callable
from pathlib import Path

import aie.utils as aie_utils
import numpy as np

from iron.common.graph.fold import folded
from iron.common.graph.narrowing import CostTable
from iron.common.graph.probe import Call, Timing, measure_graph, pmode
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
    """Measure ``model``'s decode step into ``table`` (``measure_graph``):
    each design at ``position`` and ``token``, Sample on the draw rows
    ``sample`` gives, and the configure cost between ``CALIBRATION_PAIRS``.
    """
    # The decode step as ``CausalLM.load`` compiles it, folded.
    traced, _ = folded(
        model.trace(**model.shapes(1)), aie_utils.ensure_current_device()
    )
    # Sample's work follows its draw row's temperature and top-k: measure it
    # at the rows generation writes, not at random words.
    [k_max] = {s.op.k_max for s in traced.steps if isinstance(s.op, Sample)}
    _, draws = traced.states[id(model.draws)]
    call = Call(
        traced,
        dict(position=position, token=token),
        {draws.name: sample.rows(model.config.max_seq_len, k_max)},
    )
    measure_graph(table, [call], CALIBRATION_PAIRS, timing, repeats, remeasure, log)


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
        help="measure designs and calibrations already in the table or the "
        "cost cache again",
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
