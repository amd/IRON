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

from .checkpoint import Checkpoint, Layout, load_weights
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

    def __init__(self, weights_path, tokenizer_path, config: Config | None = None):
        self.config = config or type(self).config
        self.checkpoint = Checkpoint(weights_path)
        layout = self.layout(self.config)
        self.weights = load_weights(
            self.checkpoint.tensors, layout, self.config.n_layers
        )
        self.tokenizer = self.open_tokenizer(tokenizer_path)

    def npu(
        self, cost_table: Path | None = None, boundaries: str | None = None
    ) -> CausalLM:
        """The model compiled and loaded, weights uploaded. With a
        ``cost_table`` (``tune``) its decode step's designs are folded,
        narrowed and packed by it; ``boundaries`` are its decode step's
        (``CausalLM.load``).
        """
        model = self.model(self.config, self.weights)
        tuner = None if cost_table is None else JointNarrowing(CostTable(cost_table))
        return model.load(self.checkpoint.release, tuner, boundaries)

    def cpu(self) -> Oracle:
        """The model's oracle, its weights widened (float32 is twice bf16)."""
        return self.model.oracle(self.config, self.weights)

    def encode(self, text: str) -> list[int]:
        return [self.bos, *self.tokenizer.encode(text)]

    def prompt(self, chars: int, skip: int = 0) -> list[int]:
        """``chars`` characters of ``prompt.txt`` from ``skip`` on, encoded."""
        text = Path(__file__).with_name("prompt.txt").read_text()
        return self.encode(text[skip : skip + chars])


def main(runner: type[Runner], description: str):
    """The command line of ``runner``'s model: sample, or check it."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("weights_path", help="the .safetensors checkpoint")
    parser.add_argument("tokenizer_path", help="the tokenizer's file")
    parser.add_argument(
        "--prompt-len",
        type=int,
        default=2048,
        help="characters of prompt.txt to prompt with (default: 2048)",
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
        help="fold, narrow and pack the decode step's designs by this measured "
        "cost table (iron.lm.tune); default: as the profile gives them",
    )
    parser.add_argument(
        "--each-step",
        action="store_true",
        help="dispatch every step of a decode step on its own from one xclbin, "
        "as NPU1 does; the prompt then runs a token at a time",
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
    run = runner(args.weights_path, args.tokenizer_path, config)
    tokens = run.prompt(args.prompt_len)
    if len(tokens) + args.num_tokens > run.config.max_seq_len:
        parser.error(
            f"a {len(tokens)}-token prompt and {args.num_tokens} more exceed "
            f"{run.config.max_seq_len} rows"
        )
    model = run.npu(args.cost_table, iron.each_step if args.each_step else None)
    if args.device_loop and not model.full_elf:
        parser.error(
            "--device-loop needs a full-ELF decode step, which this device "
            "(NPU1) has not"
        )
    if model.tuning is not None:
        print("[Tuning] decode:\n" + model.tuning.report(), flush=True)

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

        def show(token):
            print(run.tokenizer.decode([token]), end="", flush=True)

        def report(first, later):
            print(f"\n\n[Prefill] Time to first token: {first:7.3f} s")
            if args.num_tokens > 1:
                print(f"[Decode]  Tokens per second:   {1 / later:7.3f}")

        print(run.tokenizer.decode(tokens[1:]), end="", flush=True)
        if not args.device_loop:
            report(*generate(model, tokens, args.num_tokens, sampler(), show)[1:])
            return
        drawn, first, later = model.generate(tokens, args.num_tokens, sampler())
        print(run.tokenizer.decode(drawn), end="", flush=True)
        report(first, later)
        if args.compare_host:
            print("\n[Host loop]\n" + run.tokenizer.decode(tokens[1:]), end="")
            host, _, _ = generate(model, tokens, args.num_tokens, sampler(), show)
            differ = sum(a != b for a, b in zip(drawn, host))
            print(
                f"\n[DeviceLoop] Tokens differing from the host loop: {differ}/{len(host)}"
            )
