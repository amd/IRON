# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure the cost table a model's versions are tuned by, on this NPU:

```bash
python -m iron.lm.tune llama
python -m iron.lm.tune llama --dispatch separate
```

``<application>`` (``application_runner``), dotted under
``iron.applications`` (a tower names its own sub-package, e.g.
``embedding_gemma2.audio``), is read for a ``Runner`` in its ``model``
module; the table lands beside it, ``costs_<device>.json``.

``--cost-table TABLE`` on a model's own command line folds the steps of the
decode step and the prompt chunk into their producers, narrows their
designs and packs them into shared device configurations by what each
costs on the device (``JointNarrowing``). A table holds every design's step
time at each width it tunes to, and the configure cost measured between a
few pairs of designs. It is keyed by each design's identity -- its fields
-- so a design that has changed since is not in it, and the tuner leaves
that design as the profile gives it, unfolded. ``main`` fills one for both
versions as the graph is now (``calls``): every design, each setting, as
traced and with each fold it admits. Designs already in the table are kept
unless ``--remeasure``; entries for designs the graph no longer has are
dropped. A design another graph has had measured on this NPU is taken from
the cost cache (``iron.common.graph.costcache``) rather than run again.

A design whose work a per-call value changes (attention over the cache,
by the position) is also measured at a ladder of contexts up to
``--context`` (``contexts``) and priced at their weighted mean, the
contexts a generation of that length runs at equally often.

A design's time follows its shapes, per-call values and Sample's draw
rows, not the weights, so no checkpoint is read: the model is built on
weights it never touches. Run with XRT sourced and the NPU otherwise idle.
"""

import argparse
import importlib
from collections.abc import Sequence
from pathlib import Path

import aie.utils as aie_utils
import numpy as np

from iron.common.graph import tune as graph_tune
from iron.common.graph.probe import Call, Point
from iron.operators import ElementwiseAdd, ElementwiseMul, SiLU
from iron.operators.sample import Sample

from .base import Runner, unread_weights
from .causal import CausalLM
from .generation import SEED, Sampler

# The configure cost is measured between small single-column designs, at
# their narrowest: one design's configure then costs least beside the fixed
# part the calibration isolates.
CALIBRATION_TRIANGLE = (ElementwiseAdd, SiLU, ElementwiseMul)


def contexts(top: int, count: int, unit: int) -> list[tuple[float, int]]:
    """At most ``count`` contexts halving down from ``top``, multiples of
    ``unit``, ascending, each weighted by the share of a uniform context in
    ``(0, top]`` nearest it (the trapezoid rule): the weights sum to 1.

    Raises:
        ValueError: ``top`` is not a positive multiple of ``unit``.
    """
    if top < unit or top % unit:
        raise ValueError(f"the context {top} is not a multiple of {unit}")
    found = [top]
    while len(found) < count and found[-1] // 2 >= unit and found[-1] // 2 % unit == 0:
        found.append(found[-1] // 2)
    found.reverse()
    edges = [0] + [(a + b) / 2 for a, b in zip(found, found[1:])] + [top]
    return [((hi - lo) / top, c) for lo, hi, c in zip(edges, edges[1:], found)]


def calls(
    model: CausalLM,
    sample: Sampler,
    position: int,
    token: int,
    context: int,
    count: int,
) -> list[Call]:
    """The calls ``model``'s designs are measured in on the current device:
    the decode step at ``position`` and ``token``, and the prompt chunk at
    a whole first chunk, each as traced and with each fold it admits, Sample on the
    draw rows ``sample`` gives. Each is priced over ``contexts`` up to ``context``,
    ``count`` of them: the decode step at their last position, the prompt
    chunk as the whole chunk ending there.
    """
    dev = aie_utils.ensure_current_device()
    C = model.config.prefill_chunk
    versions = [
        (
            model.shapes(1),
            dict(position=position, token=token),
            [
                Point(w, dict(position=c - 1, token=token))
                for w, c in contexts(context, count, 1)
            ],
        ),
        (
            model.shapes(C),
            dict(position=C - 1, token=token, chunk=0, rows=C),
            [
                Point(w, dict(position=c - 1, token=token, chunk=c // C - 1, rows=C))
                for w, c in contexts(context, count, C)
            ],
        ),
    ]
    out = []
    for shapes, values, points in versions:
        traced = model.trace(**shapes)
        # Sample's work follows its draw row's temperature and top-k: measure
        # it at the rows generation writes, not at random words.
        [k_max] = {s.op.k_max for s in traced.steps if isinstance(s.op, Sample)}
        _, draws = traced.states[id(model.draws)]
        rows = sample.rows(model.config.max_seq_len, k_max)
        out += Call.admitted(traced, dev, values, {draws.name: rows}, points)
    return out


def application_runner(name: str) -> tuple[type[Runner], Path]:
    """``name``'s ``Runner``, read from its ``model`` module, and the
    directory its cost table lands in (that module's own): ``name`` dotted
    under ``iron.applications``, a tower naming its own sub-package
    (``embedding_gemma2.audio``).

    Raises:
        ValueError: ``name`` names no such application, or its ``model``
            module exports no ``Runner``.
    """
    try:
        module = importlib.import_module(f"iron.applications.{name}.model")
    except ImportError as e:
        raise ValueError(f"no application {name!r}: {e}") from e
    if "Runner" not in vars(module):
        raise ValueError(f"iron.applications.{name}.model exports no Runner")
    return vars(module)["Runner"], Path(module.__file__).parent


def main(
    name: str, runner: type[Runner], tables: Path, argv: Sequence[str] | None = None
) -> None:
    """The command line that measures ``name``'s ``runner``'s model's cost
    table in ``tables`` (``graph_tune.table``): its ``calls``, and the
    configure cost between each pair of ``CALIBRATION_TRIANGLE``.
    """
    parser = graph_tune.parser(
        f"Measure {name}'s cost table, its decode step and prompt chunk", tables
    )
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
    parser.add_argument(
        "--context",
        type=int,
        default=8192,
        help="the longest context a design whose work follows it is priced "
        "at, a multiple of the prompt chunk (default: 8192)",
    )
    parser.add_argument(
        "--points",
        type=int,
        default=6,
        help="how many contexts up to --context it is priced at, each "
        "measured per setting: their cost grows with it (default: 6)",
    )
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--top-k", type=int, default=50)
    args = parser.parse_args(argv)

    config = runner.config
    model = runner.model(config, unread_weights(runner.layout(config), config.n_layers))
    sample = Sampler(args.temperature, args.top_k, np.random.default_rng(SEED))
    if args.context > config.max_seq_len:
        parser.error(
            f"--context {args.context} is past max_seq_len {config.max_seq_len}"
        )
    graph_tune.measure(
        args,
        calls(
            model,
            sample,
            args.position,
            args.token,
            args.context,
            args.points,
        ),
        CALIBRATION_TRIANGLE,
        tables,
    )


def cli() -> None:
    """``python -m iron.lm.tune <application>``: measure ``<application>``'s
    cost table (``main``), its ``Runner`` found by ``application_runner``.
    ``--help`` after ``<application>`` lists the rest of its flags; without
    one, only ``application`` is required, since the flags follow from it.
    """
    # No -h here: an unresolved --help passes through to main's parser,
    # which knows application's own flags.
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "application",
        help="dotted under iron.applications, a tower naming its own "
        "sub-package (e.g. embedding_gemma2.audio); its model module's "
        "Runner is tuned",
    )
    args, rest = parser.parse_known_args()
    try:
        runner, tables = application_runner(args.application)
    except ValueError as e:
        parser.error(str(e))
    main(args.application, runner, tables, rest)


if __name__ == "__main__":
    cli()
