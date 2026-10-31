# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``main``, a model's command line."""

import argparse
import importlib
import inspect
import json
import logging
from typing import Any

import numpy as np

from .generation import Sampler, accuracy, determinism, generate_on_host, kl_stats
from .model import Model, prompt_text

#: The flags ``main()``'s CLI and pytest's fixtures read alike, each a
#: tuple of ``add_argument``'s own flag strings and keywords.
FLAGS: tuple[tuple[tuple[str, ...], dict[str, Any]], ...] = (
    (
        ("--random-weights",),
        dict(
            type=int,
            default=None,
            metavar="SEED",
            help="in place of the checkpoint's weights and the tokenizer, "
            "weights drawn at SEED in its shapes (only its header is read) "
            "and prompts of random tokens",
        ),
    ),
    (
        ("--max-seq-len",),
        dict(
            type=int,
            default=None,
            help="the longest context served, prompt and generated tokens "
            "together (default: the checkpoint's max_position_embeddings)",
        ),
    ),
)


def exports(package: str, names):
    """Build a model package's ``__getattr__``, each of ``names`` from its model module.

    Imported on first use, so ``python -m <package>.model`` runs that
    module once.
    """

    def __getattr__(name):
        if name in names:
            return getattr(importlib.import_module(f"{package}.model"), name)
        raise AttributeError(f"module {package!r} has no attribute {name!r}")

    return __getattr__


def sampling_arguments(parser: argparse.ArgumentParser) -> None:
    """``--temperature`` and ``--top-k``, a ``Sampler``'s, at its defaults."""
    defaults = inspect.signature(Sampler).parameters
    parser.add_argument(
        "--temperature", type=float, default=defaults["temperature"].default
    )
    parser.add_argument("--top-k", type=int, default=defaults["top_k"].default)


def config_argument(parser: argparse.ArgumentParser) -> None:
    """``--config NAME=VALUE``, repeated: fields of the model's config given
    other values (JSON, else a bare string), as ``Model.from_checkpoint``'s
    ``config`` takes them; ``num_hidden_layers=2`` is a model a tuner's own
    changes run against in minutes, every design still the full model's.
    """

    def field(text: str) -> tuple[str, Any]:
        name, sep, value = text.partition("=")
        if not sep or not name:
            raise argparse.ArgumentTypeError(f"{text!r} is not NAME=VALUE")
        try:
            return name, json.loads(value)
        except json.JSONDecodeError:
            return name, value

    parser.add_argument(
        "--config",
        type=field,
        action="append",
        default=[],
        metavar="NAME=VALUE",
        help="a field of the model's config, given another value (repeat for "
        "more): num_hidden_layers=2 is a shallow model of the same designs",
    )


def parse_args(parser: argparse.ArgumentParser, args=None) -> argparse.Namespace:
    """``parser``'s arguments with ``-v``, which logs iron's INFO lines.

    Such as each compile's.
    """
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="log iron's INFO lines"
    )
    args = parser.parse_args(args)
    if args.verbose:
        logging.basicConfig()
        logging.getLogger("iron").setLevel(logging.INFO)
    return args


def main(model_class: type[Model]):
    """Run the command line of ``model_class``, loaded as ``Model.load`` loads it.

    Sample, or check it.
    """
    parser = argparse.ArgumentParser(description=f"{model_class.__name__} on the NPU")
    parser.add_argument(
        "path",
        help="a directory holding config.json, the checkpoint and the "
        "tokenizer, or a Hugging Face repository's id",
    )
    for flags, kwargs in FLAGS:
        parser.add_argument(*flags, **kwargs)
    parser.add_argument("--prompt", metavar="TEXT", help="the text to continue")
    parser.add_argument(
        "--prompt-len",
        type=int,
        default=2048,
        help="without --prompt, characters of prompt.txt to prompt with, or "
        "with --random-weights a third as many random tokens (default: 2048)",
    )
    parser.add_argument(
        "--num-tokens", type=int, default=40, help="tokens to generate (default: 40)"
    )
    sampling_arguments(parser)
    check = parser.add_mutually_exclusive_group()
    check.add_argument(
        "--check-accuracy",
        action="store_true",
        help="instead of sampling, compare each step's logits with the CPU "
        "reference's, feeding both the reference's greedy token",
    )
    check.add_argument(
        "--check-determinism",
        type=int,
        metavar="ROUNDS",
        help="instead of sampling, run two prompts ROUNDS times each, "
        "alternating, and count the runs whose logits differ bitwise",
    )
    parser.add_argument(
        "--compare-host",
        action="store_true",
        help="after drawing on the device, generate again drawing on the host "
        "from the same seed and count the tokens that differ",
    )
    parser.add_argument(
        "--full-elf",
        action=argparse.BooleanOptionalAction,
        help="package each version as one full ELF, or with --no-full-elf "
        "dispatch every step on its own from one xclbin, as NPU1 does "
        "(default: a full ELF where the device runs one)",
    )
    args = parse_args(parser)
    if args.check_determinism is not None and args.check_determinism < 2:
        parser.error("--check-determinism compares rounds: give 2 or more")
    try:
        model = model_class.from_checkpoint(
            args.path, random_weights=args.random_weights, max_seq_len=args.max_seq_len
        )
    except ValueError as e:
        parser.error(str(e))
    if args.prompt is None:
        text, tokens = prompt_text(args.prompt_len), model.prompt(args.prompt_len)
    elif model.tokenizer is None:
        parser.error("--prompt takes the checkpoint's tokenizer: no --random-weights")
    else:
        text, tokens = args.prompt, model.tokenizer(args.prompt)
    if len(tokens) + args.num_tokens > model.config.max_seq_len:
        parser.error(
            f"a {len(tokens)}-token prompt and {args.num_tokens} more exceed "
            f"{model.config.max_seq_len} rows"
        )
    assert model.checkpoint is not None, "from_checkpoint gives it one"
    model.load_versions(release=model.checkpoint.release, full_elf=args.full_elf)

    if args.check_accuracy:
        results = accuracy(model, model.cpu_reference(), tokens, args.num_tokens)
        worst = int(np.argmax([kl for kl, _ in results]))
        for stat, value in kl_stats(results).items():
            where = f" (step {worst})" if stat == "Max" else ""
            print(f"[Accuracy] {stat} KL: {value:.6f}{where}")
        print(f"[Accuracy] Top-1 mismatches: {sum(not t for _, t in results)}")
    elif args.check_determinism is not None:
        # The second prompt is as much of the text as follows the first.
        prompts = [tokens, model.prompt(args.prompt_len, skip=args.prompt_len)]
        rounds = args.check_determinism
        n_differ = determinism(model, prompts, args.num_tokens, rounds)
        print(f"[Determinism] Differing runs: {n_differ}/{2 * (rounds - 1)}")
    else:

        def sampler():
            return Sampler(args.temperature, args.top_k)

        # The text, where there is a tokenizer to read it, else the ids.
        ids = model.tokenizer is None
        prompt = tokens if ids else text
        for piece in model.stream(prompt, args.num_tokens, sampler()):
            print(f" {piece}" if ids else piece, end="", flush=True)
        stats = model.stats
        assert stats is not None, "set once the last token is drawn"
        print(f"\n\n[Prefill] Time to first token: {stats.ttft:7.3f} s")
        if args.num_tokens > 1:
            print(f"[Decode]  Tokens per second:   {stats.tokens_per_s:7.3f}")
        if args.compare_host:
            drawn = model.generate(tokens, args.num_tokens, sampler())
            host = generate_on_host(model, tokens, args.num_tokens, sampler())
            differ = sum(a != b for a, b in zip(drawn, host))
            print(f"[Device] Tokens differing from the host loop: {differ}/{len(host)}")


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
    exported = [getattr(package, n) for n in vars(package).get("__all__", ())]
    found = [
        m
        for m in exported
        if isinstance(m, type) and any("tune_calls" in vars(k) for k in m.__mro__)
    ]
    if len(found) != 1:
        raise ValueError(
            f"iron.applications.{name} exports {len(found)} models to tune, not one"
        )
    return found[0]
