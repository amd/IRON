# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tune a model's profile on this NPU.

``python -m iron.lm.tune <application>`` times its calls' operators and
rewrites ``profiles/<device>.json`` with the fastest settings found;
review and commit the change with ``git diff``.
"""

import argparse
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from iron.common.declare import Profile
from iron.operators.sample import Sample
from iron.tune import cli as tune_cli
from iron.tune.autotune import Point, Shape, Timed
from iron.tune.fusions import NotBitIdentical

from .causal import CausalLM
from .cli import application_model, config_argument, parse_args, sampling_arguments
from .generation import Sampler
from .validate import validate

VERSIONS = ("decode", "prompt")


def contexts(low: int, high: int, count: int, unit: int) -> list[tuple[float, int]]:
    """Return ``count`` contexts from ``low`` to ``high``, each weighted, ascending.

    Every doubling counts alike: the span splits into ``count`` bands of equal
    log-width (small, medium and large for three), each timed at its geometric
    centre rounded to a multiple of ``unit`` and weighted by its share, so the
    weights sum to 1. Bands that round to one context share it.
    """
    found: dict[int, float] = {}
    for k in range(count):
        centre = low * (high / low) ** ((k + 0.5) / count)
        c = min(high, max(low, unit * max(1, round(centre / unit))))
        found[c] = found.get(c, 0.0) + 1 / count
    return [(w, c) for c, w in sorted(found.items())]


def arguments(parser: argparse.ArgumentParser) -> None:
    """Add the flags a decoder's ``calls`` follow from.

    The checkpoint whose header gives the weights' shapes, the contexts
    attention over the cache is timed at, and the sampling Sample is
    timed at.
    """
    parser.add_argument(
        "--checkpoint",
        type=Path,
        required=True,
        help="the checkpoint directory, as Model.load takes it, whose weights "
        "the calls are recorded on",
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
        default=None,
        help="the longest context a design whose work follows it is timed "
        "at, a multiple of the prompt chunk (default: the model's max_seq_len)",
    )
    parser.add_argument(
        "--points",
        type=int,
        default=3,
        help="how many contexts, every doubling up to --context counting alike, "
        "it is timed at: small, medium and large by default; their cost grows "
        "with it (default: 3)",
    )
    parser.add_argument(
        "--versions",
        nargs="+",
        choices=VERSIONS,
        default=list(VERSIONS),
        help="the versions whose calls are tuned; a profile entry only the "
        "others' shapes match is kept as it is (default: both)",
    )
    sampling_arguments(parser)
    config_argument(parser)


def calls(
    model: CausalLM,
    position: int,
    token: int,
    context: int,
    points: int,
    sampler: Sampler,
    sibling: CausalLM | None = None,
    versions: Sequence[str] = VERSIONS,
) -> list[Timed]:
    """Return the calls a decoder's designs are timed in.

    The decode step and the prompt chunk, each over ``contexts`` up to ``context``,
    ``points`` of them with every doubling counting alike (the decode step's from
    ``position``, the prompt chunk's from one chunk), and Sample on the draw rows
    ``sampler`` gives.

    Args:
        model: The decoder whose versions are timed.
        position: The decode position its designs are timed at; the decode
            step's shortest context is the one past it.
        token: The token the step embeds.
        context: The longest context a design whose work follows it is timed at.
        points: How many contexts up to ``context`` it is timed at.
        sampler: The sampling Sample is timed at.
        sibling: ``model`` at another ``max_seq_len``: a dimension whose
            value differs between their recordings is one a host's fitted
            context sizes (``Timed.varying``).
        versions: Which of ``VERSIONS`` to time.
    """
    L, C = model.config.max_seq_len, model.config.prefill_chunk
    decode_shapes, prompt_shapes = model.shapes()
    planned = [
        (
            "decode",
            decode_shapes,
            dict(position=position, token=token),
            [
                Point(w, dict(position=c - 1, token=token))
                for w, c in contexts(position + 1, context, points, 1)
            ],
        ),
        (
            "prompt",
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
                for w, c in contexts(C, context, points, C)
            ],
        ),
    ]
    out = []
    for label, shapes, values, timed in planned:
        if label not in versions:
            continue
        recording = model.record(**shapes)
        # Sample's work follows its draw row's temperature and top-k: measure
        # it at the rows generation writes, not at random words.
        [k_max] = {s.op.k_max for s in recording.steps if isinstance(s.op, Sample)}
        _, draws = recording.states[id(model.draws)]
        rows = sampler.rows(L, k_max)
        varying: dict[Any, frozenset[str]] = {}
        if sibling is not None:
            other = sibling.record(**shapes)
            assert len(other.steps) == len(recording.steps), "context sizes no step"
            for step, twin in zip(recording.steps, other.steps):
                here, there = Shape(step.op.resolved()), Shape(twin.op.resolved())
                moved = {n for n, v in here.dims.items() if there.dims.get(n) != v}
                varying[here.key] = varying.get(here.key, frozenset()) | moved
        out.append(Timed(recording, values, {draws.name: rows}, timed, varying))
    return out


def main(name: str, model: Any, argv: Sequence[str] | None = None) -> None:
    """Run the command line that tunes ``name``'s profile.

    The calls ``model`` plans (``tune_calls``, on the flags ``tune_arguments`` adds),
    into its profiles directory or ``--profiles``, recorded under each profile a stage
    hands on; what is saved passes the model's battery (``validate``) against the
    starting profile, bit-identical.
    """
    parser = tune_cli.parser(f"Tune {name}'s profile")
    if model.profile is None:
        parser.error(f"{name} has no profiles directory to tune into")
    model.tune_arguments(parser)
    parser.add_argument(
        "--profiles",
        type=Path,
        default=Path(model.profile),
        help="the profiles directory whose <device>.json the calls are "
        "recorded under and the tune starts from and rewrites; a copy of the "
        "model's own tunes from it without touching it (default: the "
        "model's own)",
    )
    args = parse_args(parser, argv)

    def record(profile: Profile) -> list[Timed]:
        model.profile = profile
        return model.tune_calls(parser, args)

    def battery(start: Profile, kept: Profile) -> dict:
        report = validate(model, args.checkpoint, kept, start, config=dict(args.config))
        if not report["bit_identical"]:
            raise NotBitIdentical(
                f"{name}: the tuned profile is not bit-identical to the starting "
                f"one; it stays in {args.profiles}/<device>.found.json"
            )
        return report

    tune_cli.tune(args, record, args.profiles, battery)


def cli() -> None:
    """``python -m iron.lm.tune <application>``: tune ``<application>``'s profile.

    Tunes with ``main``, its model found by ``application_model``;
    ``--help`` after ``<application>`` lists the rest of its flags.
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
