# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure the cost table a model's versions are tuned by, on this NPU:

```bash
python -m iron.lm.tune llama --checkpoint /path/to/model.safetensors
python -m iron.lm.tune embedding_gemma2
```

The application's ``Runner`` names what is measured (``tune_calls``,
``calibration_triangle``) and where ``costs_<device>.json`` lands
(``tables``, else beside its module); ``--cost-table`` on the model's own
command line tunes by it (``JointNarrowing``). The table is keyed by each
design's fields, so a design changed since is left as the profile gives
it. Designs the table or the cost cache hold are kept unless
``--remeasure``; a design a per-call value moves is also measured at
contexts up to ``--context``. The model is built on weights it never
reads, since a step's time does not follow them. Run with the NPU
otherwise idle.
"""

import argparse
import importlib
from collections.abc import Sequence
from pathlib import Path

from iron.tune import cli as tune_cli

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
    (``tune_cli.table``): the calls ``runner`` plans (``Runner.tune_calls``,
    on the flags ``Runner.tune_arguments`` adds), and the configure cost
    between each pair of its ``calibration_triangle``.
    """
    parser = tune_cli.parser(f"Measure {name}'s cost table", tables)
    runner.tune_arguments(parser)
    args = parser.parse_args(argv)
    tune_cli.measure(
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
