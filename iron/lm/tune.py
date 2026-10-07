# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure the cost table a model's versions are tuned by, on this NPU.

``--cost-table TABLE`` on a model's command line (``main``)
folds the steps of the decode step and the prompt chunk into their
producers, narrows their designs and packs them into shared device
configurations by what each costs on the device (``JointNarrowing``). A
table holds every design's step time at each width it tunes to, and the
configure cost measured between a few pairs of designs. It is keyed by
each design's identity -- its fields -- so a design that has changed since
is not in it, and the tuner leaves that design as the profile gives it,
unfolded. ``main`` fills one for both versions as the graph is now
(``calls``): every design, each setting, as traced and with each fold it
admits. Designs already in the table are kept unless ``--remeasure``; entries
for designs the graph no longer has are dropped. A design another graph has
had measured on this NPU is taken from the cost cache
(``iron.common.graph.costcache``) rather than run again.

A design's time follows its shapes, per-call values and Sample's draw
rows, not the weights, so no checkpoint is read: the model is built on
weights it never touches. A model's ``tune`` module calls ``main`` with
its runner; run it with XRT sourced and the NPU otherwise idle.
"""

from pathlib import Path

import aie.utils as aie_utils
import numpy as np

from iron.common.graph import tune as graph_tune
from iron.common.graph.probe import Call
from iron.operators.sample import Sample

from .checkpoint import unread_weights
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


def calls(model: CausalLM, sample: Sampler, position: int, token: int) -> list[Call]:
    """The calls ``model``'s designs are measured in on the current device:
    the decode step at ``position`` and ``token``, the prompt chunk at a
    whole first chunk, each as traced and with each fold it admits, Sample
    on the draw rows ``sample`` gives.
    """
    dev = aie_utils.ensure_current_device()
    C = model.config.prefill_chunk
    versions = [
        (model.shapes(1), dict(position=position, token=token)),
        (model.shapes(C), dict(position=C - 1, token=token, chunk=0, rows=C)),
    ]
    out = []
    for shapes, values in versions:
        traced = model.trace(**shapes)
        # Sample's work follows its draw row's temperature and top-k: measure
        # it at the rows generation writes, not at random words.
        [k_max] = {s.op.k_max for s in traced.steps if isinstance(s.op, Sample)}
        _, draws = traced.states[id(model.draws)]
        rows = sample.rows(model.config.max_seq_len, k_max)
        out += Call.admitted(traced, dev, values, {draws.name: rows})
    return out


def main(runner: type[Runner], description: str, default_table: Path) -> None:
    """The command line that measures ``runner``'s model's cost table: its
    ``calls``, and the configure cost between ``CALIBRATION_PAIRS``.
    """
    parser = graph_tune.parser(description, default_table)
    parser.add_argument(
        "--position",
        type=int,
        default=256,
        help="the decode position the decode step's designs are measured at: "
        "what their per-call values follow from (default: 256)",
    )
    parser.add_argument(
        "--token", type=int, default=0, help="the token the step embeds (default: 0)"
    )
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--top-k", type=int, default=50)
    args = parser.parse_args()

    config = runner.config
    model = runner.model(config, unread_weights(runner.layout(config), config.n_layers))
    sample = Sampler(args.temperature, args.top_k, np.random.default_rng(SEED))
    graph_tune.measure(
        args, calls(model, sample, args.position, args.token), CALIBRATION_PAIRS
    )
