# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``main``, a model's command line."""

import argparse
import inspect

import numpy as np

from .generation import Sampler, accuracy, determinism, generate_on_host, kl_stats
from .model import Model

#: The flags ``main()``'s CLI and pytest's fixtures read alike, each a
#: tuple of ``add_argument``'s own flag strings and keywords.
FLAGS = (
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


def sampling_arguments(parser: argparse.ArgumentParser) -> None:
    """``--temperature`` and ``--top-k``, a ``Sampler``'s, at its defaults."""
    defaults = inspect.signature(Sampler).parameters
    parser.add_argument(
        "--temperature", type=float, default=defaults["temperature"].default
    )
    parser.add_argument("--top-k", type=int, default=defaults["top_k"].default)


def main(model: type[Model]):
    """The command line of ``model``, loaded as ``Model.load`` loads it:
    sample, or check it.
    """
    parser = argparse.ArgumentParser(description=f"{model.__name__} on the NPU")
    parser.add_argument(
        "path",
        help="a directory holding config.json, the checkpoint and the "
        "tokenizer, or a Hugging Face repository's id",
    )
    for flags, kwargs in FLAGS:
        parser.add_argument(*flags, **kwargs)
    parser.add_argument(
        "--prompt-len",
        type=int,
        default=2048,
        help="characters of prompt.txt to prompt with, or with --random-weights "
        "a third as many random tokens (default: 2048)",
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
    args = parser.parse_args()
    try:
        model = model.from_checkpoint(
            args.path, seed=args.random_weights, max_seq_len=args.max_seq_len
        )
    except ValueError as e:
        parser.error(str(e))
    tokens = model.prompt(args.prompt_len)
    if len(tokens) + args.num_tokens > model.config.max_seq_len:
        parser.error(
            f"a {len(tokens)}-token prompt and {args.num_tokens} more exceed "
            f"{model.config.max_seq_len} rows"
        )
    model.load_versions(release=model.checkpoint.release, full_elf=args.full_elf)

    if args.check_accuracy:
        results = accuracy(model, model.cpu_reference(), tokens, args.num_tokens)
        worst = int(np.argmax([kl for kl, _ in results]))
        for stat, value in kl_stats(results).items():
            where = f" (step {worst})" if stat == "Max" else ""
            print(f"[Accuracy] {stat} KL: {value:.6f}{where}")
        print(f"[Accuracy] Top-1 mismatches: {sum(not t for _, t in results)}")
    elif args.check_determinism:
        # The second prompt is as much of the text as follows the first.
        prompts = [tokens, model.prompt(args.prompt_len, skip=args.prompt_len)]
        rounds = args.check_determinism
        n_differ = determinism(model, prompts, args.num_tokens, rounds)
        print(f"[Determinism] Differing runs: {n_differ}/{2 * (rounds - 1)}")
    else:

        def decode(tokens: list[int]) -> str:
            """``tokens`` as text, or as their numbers with no tokenizer."""
            if model.tokenizer is None:
                return "".join(f" {t}" for t in tokens)
            return model.tokenizer.decode(tokens)

        def sampler():
            return Sampler(args.temperature, args.top_k)

        pending: list[int] = []

        def show(token):
            pending.append(token)
            text = decode(pending)
            # A token can end partway through a character; the next completes it.
            if not text.endswith("\ufffd"):
                print(text, end="", flush=True)
                pending.clear()

        def report(first, later):
            print(f"\n\n[Prefill] Time to first token: {first:7.3f} s")
            if args.num_tokens > 1:
                print(f"[Decode]  Tokens per second:   {1 / later:7.3f}")

        print(decode(tokens[1:]), end="", flush=True)
        drawn, first, later = model.generate(tokens, args.num_tokens, sampler())
        print(decode(drawn), end="", flush=True)
        report(first, later)
        if args.compare_host:
            print("\n[Host loop]\n" + decode(tokens[1:]), end="")
            host, _, _ = generate_on_host(
                model, tokens, args.num_tokens, sampler(), show
            )
            print(decode(pending), end="")
            differ = sum(a != b for a, b in zip(drawn, host))
            print(
                f"\n[Device] Tokens differing from the host loop: {differ}/{len(host)}"
            )
