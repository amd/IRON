# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tune a model's profile on this NPU:

```bash
python -m iron.lm.tune llama --checkpoint /path/to/model.safetensors
python -m iron.lm.tune embedding_gemma2
```

The application's ``Runner`` names the calls its operators are timed in
(``tune_calls``), and the fastest settings found rewrite its model's
``profiles/<device>.json`` (``iron.tune.autotune``): review the change with
``git diff`` and commit it. Times the cost cache holds are kept unless
``--remeasure``; an operator a per-call value moves is also timed at
contexts up to ``--context``. The model is built on weights it never
reads, since a step's time does not follow them. Run with the NPU
otherwise idle.
"""

import argparse
import importlib
from collections.abc import Sequence
from pathlib import Path

from iron.tune import cli as tune_cli

from .runner import Runner


def application_runner(name: str) -> type[Runner]:
    """``name``'s ``Runner``, read from its ``model`` module: ``name``
    dotted under ``iron.applications``.

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
    return vars(module)["Runner"]


def main(name: str, runner: type[Runner], argv: Sequence[str] | None = None) -> None:
    """The command line that tunes ``name``'s profile: the calls ``runner``
    plans (``Runner.tune_calls``, on the flags ``Runner.tune_arguments``
    adds), into its model's profiles directory.
    """
    parser = tune_cli.parser(f"Tune {name}'s profile")
    runner.tune_arguments(parser)
    args = parser.parse_args(argv)
    tune_cli.tune(args, runner.tune_calls(parser, args), Path(runner.model.profile))


def cli() -> None:
    """``python -m iron.lm.tune <application>``: tune ``<application>``'s
    profile (``main``), its ``Runner`` found by ``application_runner``.
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
        runner = application_runner(args.application)
    except ValueError as e:
        parser.error(str(e))
    main(args.application, runner, rest)


if __name__ == "__main__":
    cli()
