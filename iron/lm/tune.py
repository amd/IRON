# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure the cost table a model's versions are tuned by, on this NPU:

```bash
python -m iron.lm.tune llama --checkpoint /path/to/model.safetensors
python -m iron.lm.tune llama --checkpoint /path/to/model.safetensors --dispatch separate
python -m iron.lm.tune embedding_gemma2
```

``<application>`` (``application_runner``), dotted under
``iron.applications``, is read for a ``Runner`` in its ``model`` module;
the table, ``costs_<device>.json``, lands in the Runner's ``tables``, else
beside that module. What is measured is the Runner's plan: its
``tune_calls`` on the flags its ``tune_arguments`` adds, and the configure
cost between its ``calibration_triangle``. A decoder's is the base
``Runner``'s, ``CausalLM.tune_calls``; a model of another kind gives its
own (EmbeddingGemma 2's, every version of its multimodal graph).

``--cost-table TABLE`` on a model's own command line folds the steps of the
decode step and the prompt chunk into their producers, narrows their
designs and packs them into shared device configurations by what each
costs on the device (``JointNarrowing``). A table holds every design's step
time at each width it tunes to, and the configure cost measured between a
few pairs of designs. It is keyed by each design's identity -- its fields
-- so a design that has changed since is not in it, and the tuner leaves
that design as the profile gives it, unfolded. ``main`` fills one for the
versions the plan names, as the graph is now: every design, each setting,
as traced and with each fold it admits. Designs already in the table are kept
unless ``--remeasure``; entries for designs the graph no longer has are
dropped. A design another graph has had measured on this NPU is taken from
the cost cache (``iron.common.graph.costcache``) rather than run again.

In a decoder's plan, a design whose work a per-call value changes
(attention over the cache, by the position) is also measured at a ladder
of contexts up to ``--context`` (``iron.lm.causal.contexts``) and priced at
their weighted mean, the contexts a generation of that length runs at
equally often.

A design's time follows its shapes, per-call values and Sample's draw
rows, not the weights, so the model is built on weights it never reads,
in the shapes its checkpoint's header gives. Run with XRT sourced and the
NPU otherwise idle.
"""

import argparse
import importlib
from collections.abc import Sequence
from pathlib import Path

from iron.common.graph import tune as graph_tune

from .base import Runner


def application_runner(name: str) -> tuple[type[Runner], Path]:
    """``name``'s ``Runner``, read from its ``model`` module, and the
    directory its cost table lands in (its ``tables``, else that module's
    own): ``name`` dotted under ``iron.applications``.

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
    runner = vars(module)["Runner"]
    if runner.tables is not None:
        return runner, runner.tables
    return runner, Path(module.__file__).parent


def main(
    name: str, runner: type[Runner], tables: Path, argv: Sequence[str] | None = None
) -> None:
    """The command line that measures ``name``'s cost table in ``tables``
    (``graph_tune.table``): the calls ``runner`` plans (``Runner.tune_calls``,
    on the flags ``Runner.tune_arguments`` adds), and the configure cost
    between each pair of its ``calibration_triangle``.
    """
    parser = graph_tune.parser(f"Measure {name}'s cost table", tables)
    runner.tune_arguments(parser)
    args = parser.parse_args(argv)
    graph_tune.measure(
        args, runner.tune_calls(parser, args), runner.calibration_triangle, tables
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
        help="dotted under iron.applications (e.g. llama, embedding_gemma2); "
        "its model module's Runner is tuned",
    )
    args, rest = parser.parse_known_args()
    try:
        runner, tables = application_runner(args.application)
    except ValueError as e:
        parser.error(str(e))
    main(args.application, runner, tables, rest)


if __name__ == "__main__":
    cli()
