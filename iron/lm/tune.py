# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tune a model's profile on this NPU:

```bash
python -m iron.lm.tune llama --checkpoint /path/to/model.safetensors
python -m iron.lm.tune embedding_gemma2
```

The application's model class names the calls its operators are timed in
(``tune_calls``), and the fastest settings found rewrite its
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

from .model import Model


def application_model(name: str) -> type[Model]:
    """``name``'s model class: of those its package exports, the one that
    plans tuning calls (``tune_calls``), ``name`` dotted under
    ``iron.applications``.

    Raises:
        ValueError: ``name`` names no such application, or its package
            exports other than one such class.
    """
    try:
        package = importlib.import_module(f"iron.applications.{name}")
    except ImportError as e:
        raise ValueError(f"no application {name!r}: {e}") from e
    exported = [getattr(package, n) for n in getattr(package, "__all__", ())]
    found = [m for m in exported if hasattr(m, "tune_calls")]
    if len(found) != 1:
        raise ValueError(
            f"iron.applications.{name} exports {len(found)} models with "
            "tune_calls, not one"
        )
    return found[0]


def main(name: str, model: type[Model], argv: Sequence[str] | None = None) -> None:
    """The command line that tunes ``name``'s profile: the calls ``model``
    plans (``tune_calls``, on the flags ``tune_arguments`` adds), into its
    profiles directory.
    """
    parser = tune_cli.parser(f"Tune {name}'s profile")
    model.tune_arguments(parser)
    args = parser.parse_args(argv)
    tune_cli.tune(args, model.tune_calls(parser, args), Path(model.profile))


def cli() -> None:
    """``python -m iron.lm.tune <application>``: tune ``<application>``'s
    profile (``main``), its model found by ``application_model``.
    ``--help`` after ``<application>`` lists the rest of its flags; without
    one, only ``application`` is required, since the flags follow from it.
    """
    # No -h here: an unresolved --help passes through to main's parser,
    # which knows application's own flags.
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "application",
        help="dotted under iron.applications (e.g. llama, embedding_gemma2); "
        "the model its package exports is tuned",
    )
    args, rest = parser.parse_known_args()
    try:
        model = application_model(args.application)
    except ValueError as e:
        parser.error(str(e))
    main(args.application, model, rest)


if __name__ == "__main__":
    cli()
