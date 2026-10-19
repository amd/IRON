# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tune a model's profile on this NPU:

```bash
python -m iron.lm.tune llama --checkpoint /path/to/model.safetensors
python -m iron.lm.tune embedding_gemma2
```

A model names the calls its operators are timed in (``tune_calls``): a
decoder's are its decode step and its prompt chunk (``calls``).
The fastest settings found rewrite the application's
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

from iron.operators.sample import Sample
from iron.tune import cli as tune_cli
from iron.tune.autotune import Point, Timed

from .causal import CausalLM
from .cli import parse_args, sampling_arguments
from .generation import Sampler
from .model import Model


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


def arguments(parser: argparse.ArgumentParser) -> None:
    """The flags a decoder's ``calls`` follow from: the checkpoint whose
    header gives the weights' shapes, the decode step's position and token,
    the contexts attention over the cache is timed at, and the sampling
    Sample is timed at.
    """
    parser.add_argument(
        "--checkpoint",
        type=Path,
        required=True,
        help="the .safetensors checkpoint, or a sharded one's "
        "model.safetensors.index.json, of which only the header is read",
    )
    parser.add_argument(
        "--position",
        type=int,
        default=256,
        help="the decode position the decode step's designs are timed at: "
        "what their per-call values follow from (default: 256)",
    )
    parser.add_argument(
        "--token",
        type=int,
        default=0,
        help="the token the step embeds (default: 0)",
    )
    parser.add_argument(
        "--context",
        type=int,
        default=8192,
        help="the longest context a design whose work follows it is timed "
        "at, a multiple of the prompt chunk (default: 8192)",
    )
    parser.add_argument(
        "--points",
        type=int,
        default=6,
        help="how many contexts up to --context it is timed at, each "
        "timed per setting: their cost grows with it (default: 6)",
    )
    sampling_arguments(parser)


def calls(
    model: CausalLM,
    position: int,
    token: int,
    context: int,
    points: int,
    sampler: Sampler,
) -> list[Timed]:
    """The calls a decoder's designs are timed in: the decode step at
    ``position`` and ``token``, and the prompt chunk at a whole first chunk,
    Sample on the draw rows ``sampler`` gives. Each is timed over
    ``contexts`` up to ``context``, ``points`` of them: the decode step at
    their last position, the prompt chunk as the whole chunk ending there.

    Raises:
        ValueError: ``context`` is past the model's ``max_seq_len``.
    """
    L, C = model.config.max_seq_len, model.config.prefill_chunk
    if context > L:
        raise ValueError(f"context {context} is past max_seq_len {L}")
    decode_shapes, prompt_shapes = model.shapes()
    versions = [
        (
            decode_shapes,
            dict(position=position, token=token),
            [
                Point(w, dict(position=c - 1, token=token))
                for w, c in contexts(context, points, 1)
            ],
        ),
        (
            prompt_shapes,
            dict(
                position=C - 1,
                token=token,
                start=0,
                rows=C,
                rope_start=model.rope_row(C, 0),
            ),
            [
                Point(
                    w,
                    dict(
                        position=c - 1,
                        token=token,
                        start=c - C,
                        rows=C,
                        rope_start=model.rope_row(c, c - C),
                    ),
                )
                for w, c in contexts(context, points, C)
            ],
        ),
    ]
    out = []
    for shapes, values, timed in versions:
        recording = model.record(**shapes)
        # Sample's work follows its draw row's temperature and top-k: measure
        # it at the rows generation writes, not at random words.
        [k_max] = {s.op.k_max for s in recording.steps if isinstance(s.op, Sample)}
        _, draws = recording.states[id(model.draws)]
        rows = sampler.rows(L, k_max)
        out.append(Timed(recording, values, {draws.name: rows}, timed))
    return out


def application_model(name: str) -> type[Model]:
    """``name``'s model class: of those its package exports, the one that
    names its calls (``tune_calls``), ``name`` dotted under
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
            f"iron.applications.{name} exports {len(found)} models to tune, not one"
        )
    return found[0]


def main(name: str, model: type[Model], argv: Sequence[str] | None = None) -> None:
    """The command line that tunes ``name``'s profile: the calls ``model``
    plans (``tune_calls``, on the flags ``tune_arguments`` adds), into its
    profiles directory.
    """
    parser = tune_cli.parser(f"Tune {name}'s profile")
    if model.profile is None:
        parser.error(f"{name} has no profiles directory to tune into")
    model.tune_arguments(parser)
    args = parse_args(parser, argv)
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
