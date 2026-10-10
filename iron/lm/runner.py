# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A model's checkpoint, tokenizer and config, the models built on them, and
the command line that runs them.
"""

import argparse
import dataclasses
from pathlib import Path

import numpy as np

import iron
from iron.common.graph.narrowing import CostTable, JointNarrowing

from .checkpoint import Checkpoint, Layout, load_weights, random_weights
from .decoder import CausalLM, Config, Oracle
from .generation import (
    SEED,
    Sampler,
    accuracy,
    determinism,
    generate,
    kl_stats,
)


class Runner:
    """A checkpoint, its tokenizer and ``config``, and the models on them.

    A subclass names the model: its ``config``; ``layout(config)``, where
    each weight is in the checkpoint (``checkpoint``); ``model``, the
    ``CausalLM`` on the NPU, whose ``oracle`` is the CPU model
    it is checked against; ``open_tokenizer(path)``, with ``encode`` and
    ``decode``; and ``bos``, the token every prompt starts with.

    The checkpoint is mapped, not read: ``npu`` uploads it a piece at a
    time and drops each piece's host pages once it is on the device.

    With no checkpoint the weights are drawn at ``seed``
    (``random_weights``), and with no tokenizer a prompt is random tokens:
    the model's speed, its accuracy against its oracle and its determinism
    are then measured on a host without the files.
    """

    config: Config
    model: type[CausalLM]
    bos: int

    @staticmethod
    def layout(config: Config) -> Layout:
        raise NotImplementedError

    @staticmethod
    def open_tokenizer(path):
        raise NotImplementedError

    def __init__(
        self,
        weights_path=None,
        tokenizer_path=None,
        config: Config | None = None,
        seed: int = 0,
    ):
        self.config = config or type(self).config
        self.seed = seed
        layout = self.layout(self.config)
        if weights_path is None:
            self.checkpoint = None
            self.weights = random_weights(layout, self.config.n_layers, seed)
        else:
            self.checkpoint = Checkpoint(weights_path)
            self.weights = load_weights(
                self.checkpoint.tensors, layout, self.config.n_layers
            )
        self.tokenizer = (
            None if tokenizer_path is None else self.open_tokenizer(tokenizer_path)
        )

    @staticmethod
    def add_arguments(parser: argparse.ArgumentParser) -> None:
        """The checkpoint and tokenizer arguments, or ``--random-weights``."""
        parser.add_argument(
            "weights_path", nargs="?", help="the .safetensors checkpoint"
        )
        parser.add_argument("tokenizer_path", nargs="?", help="the tokenizer's file")
        parser.add_argument(
            "--random-weights",
            type=int,
            metavar="SEED",
            help="in place of the checkpoint and the tokenizer, weights drawn "
            "at SEED and prompts of random tokens",
        )

    @classmethod
    def from_arguments(
        cls,
        parser: argparse.ArgumentParser,
        args: argparse.Namespace,
        config: Config | None = None,
    ) -> "Runner":
        """The runner ``add_arguments``'s arguments name."""
        given = [args.weights_path is not None, args.tokenizer_path is not None]
        if args.random_weights is None and not all(given):
            parser.error("give the checkpoint and the tokenizer, or --random-weights")
        if args.random_weights is not None and any(given):
            parser.error("--random-weights takes neither checkpoint nor tokenizer")
        if args.random_weights is None:
            return cls(args.weights_path, args.tokenizer_path, config)
        return cls(config=config, seed=args.random_weights)

    def npu(
        self, cost_table: Path | None = None, boundaries: str | None = None
    ) -> CausalLM:
        """The model compiled and loaded, weights uploaded. With a
        ``cost_table`` (``tune``) each version's designs are folded,
        narrowed and packed by it; ``boundaries`` are its decode step's
        (``CausalLM.load``).
        """
        model = self.model(self.config, self.weights)
        tuner = None if cost_table is None else JointNarrowing(CostTable(cost_table))
        release = None if self.checkpoint is None else self.checkpoint.release
        return model.load(release, tuner, boundaries)

    def cpu(self) -> Oracle:
        """The model's oracle, its weights widened (float32 is twice bf16)."""
        return self.model.oracle(self.config, self.weights)

    def encode(self, text: str) -> list[int]:
        return [self.bos, *self.tokenizer.encode(text)]

    def decode(self, tokens: list[int]) -> str:
        """``tokens`` as text, or as their numbers with no tokenizer."""
        if self.tokenizer is None:
            return "".join(f" {t}" for t in tokens)
        return self.tokenizer.decode(tokens)

    def prompt(self, chars: int, skip: int = 0) -> list[int]:
        """``chars`` characters of ``prompt.txt`` from ``skip`` on, encoded.

        With no tokenizer, ``chars // 3`` tokens drawn at ``seed`` and
        ``skip``: a little more than the text encodes to (Llama 3's
        tokenizer takes 3.7 characters a token), so a check sized in
        characters runs at about its size on the text.
        """
        if self.tokenizer is None:
            rng = np.random.default_rng((self.seed, skip))
            draw = rng.integers(0, self.config.vocab_size, chars // 3 - 1)
            return [self.bos, *draw]
        text = Path(__file__).with_name("prompt.txt").read_text()
        return self.encode(text[skip : skip + chars])


def main(runner: type[Runner], description: str):
    """The command line of ``runner``'s model: sample, or check it."""
    parser = argparse.ArgumentParser(description=description)
    runner.add_arguments(parser)
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
    parser.add_argument(
        "--max-seq-len",
        type=int,
        default=runner.config.max_seq_len,
        help="rows the caches hold, prompt and generated tokens together, a "
        f"multiple of {runner.config.prefill_chunk} "
        f"(default: {runner.config.max_seq_len})",
    )
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--top-k", type=int, default=50)
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
        "--device-loop",
        action="store_true",
        help="draw every token on the device, each decode step started by the "
        "one before it, rather than on the host from each step's logits",
    )
    parser.add_argument(
        "--compare-host",
        action="store_true",
        help="with --device-loop, then generate again on the host from the "
        "same seed and count the tokens that differ",
    )
    parser.add_argument(
        "--cost-table",
        type=Path,
        help="fold, narrow and pack the designs of the decode step and the "
        "prompt chunk by this measured cost table (iron.lm.tune); default: as "
        "the profile gives them",
    )
    parser.add_argument(
        "--each-step",
        action="store_true",
        help="dispatch every step of each version on its own from one xclbin, "
        "as NPU1 does",
    )
    args = parser.parse_args()
    if args.compare_host and not args.device_loop:
        parser.error("--compare-host compares the --device-loop run")
    if args.device_loop and args.each_step:
        parser.error("--device-loop needs a full-ELF decode step, not --each-step")

    try:
        config = dataclasses.replace(runner.config, max_seq_len=args.max_seq_len)
    except ValueError as e:
        parser.error(str(e))
    run = runner.from_arguments(parser, args, config)
    tokens = run.prompt(args.prompt_len)
    if len(tokens) + args.num_tokens > run.config.max_seq_len:
        parser.error(
            f"a {len(tokens)}-token prompt and {args.num_tokens} more exceed "
            f"{run.config.max_seq_len} rows"
        )
    model = run.npu(args.cost_table, iron.each_step if args.each_step else None)
    if args.device_loop and not model.device_loop:
        parser.error(
            "--device-loop needs a full-ELF decode step, which --each-step "
            "and NPU1 have not"
        )
    for name, tuning in model.tunings.items():
        print(f"[Tuning] {name}:\n" + tuning.report(), flush=True)

    if args.check_accuracy:
        results = accuracy(model, run.cpu(), tokens, args.num_tokens)
        worst = int(np.argmax([kl for kl, _ in results]))
        for stat, value in kl_stats(results).items():
            where = f" (step {worst})" if stat == "Max" else ""
            print(f"[Accuracy] {stat} KL: {value:.6f}{where}")
        print(f"[Accuracy] Top-1 mismatches: {sum(not t for _, t in results)}")
    elif args.check_determinism:
        # The second prompt is as much of the text as follows the first.
        prompts = [tokens, run.prompt(args.prompt_len, skip=args.prompt_len)]
        rounds = args.check_determinism
        n_differ = determinism(model, prompts, args.num_tokens, rounds)
        print(f"[Determinism] Differing runs: {n_differ}/{2 * (rounds - 1)}")
    else:

        def sampler():
            return Sampler(args.temperature, args.top_k, np.random.default_rng(SEED))

        pending: list[int] = []

        def show(token):
            pending.append(token)
            text = run.decode(pending)
            # A token can end partway through a character; the next completes it.
            if not text.endswith("\ufffd"):
                print(text, end="", flush=True)
                pending.clear()

        def report(first, later):
            print(f"\n\n[Prefill] Time to first token: {first:7.3f} s")
            if args.num_tokens > 1:
                print(f"[Decode]  Tokens per second:   {1 / later:7.3f}")

        print(run.decode(tokens[1:]), end="", flush=True)
        if not args.device_loop:
            timing = generate(model, tokens, args.num_tokens, sampler(), show)[1:]
            print(run.decode(pending), end="")
            report(*timing)
            return
        drawn, first, later = model.generate(tokens, args.num_tokens, sampler())
        print(run.decode(drawn), end="", flush=True)
        report(first, later)
        if args.compare_host:
            print("\n[Host loop]\n" + run.decode(tokens[1:]), end="")
            host, _, _ = generate(model, tokens, args.num_tokens, sampler(), show)
            print(run.decode(pending), end="")
            differ = sum(a != b for a, b in zip(drawn, host))
            print(
                f"\n[DeviceLoop] Tokens differing from the host loop: {differ}/{len(host)}"
            )
