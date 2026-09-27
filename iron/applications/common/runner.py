# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A model's checkpoint, tokenizer and config, the models built on them, and
the command line that runs them.
"""

import argparse
from pathlib import Path

import numpy as np

from .checkpoint import Checkpoint, Layout, load_weights
from .generation import (
    SEED,
    Sampler,
    accuracy,
    determinism,
    generate,
    kl_stats,
)
from .model import CausalLM, Config, Oracle


class Runner:
    """A checkpoint, its tokenizer and ``config``, and the models on them.

    A subclass names the model: its ``config``; ``layout(config)``, where
    each weight is in the checkpoint (:mod:`.checkpoint`); ``model``, the
    :class:`~.model.CausalLM` on the NPU, whose ``oracle`` is the CPU model
    it is checked against; ``open_tokenizer(path)``, with ``encode`` and
    ``decode``; and ``bos``, the token every prompt starts with.

    The checkpoint is mapped, not read: :meth:`npu` uploads it a piece at a
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

    def npu(self) -> CausalLM:
        """The model compiled and loaded, weights uploaded."""
        model = self.model(self.config, self.weights)
        return model.load(self.checkpoint.release)

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
    args = parser.parse_args()

    run = runner(args.weights_path, args.tokenizer_path)
    tokens = run.prompt(args.prompt_len)
    if len(tokens) + args.num_tokens > run.config.max_seq_len:
        parser.error(
            f"a {len(tokens)}-token prompt and {args.num_tokens} more exceed "
            f"{run.config.max_seq_len} rows"
        )
    model = run.npu()

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
        sample = Sampler(args.temperature, args.top_k, np.random.default_rng(SEED))
        print(run.tokenizer.decode(tokens[1:]), end="", flush=True)

        def show(token):
            print(run.tokenizer.decode([token]), end="", flush=True)

        _, first, later = generate(model, tokens, args.num_tokens, sample, show)
        print(f"\n\n[Prefill] Time to first token: {first:7.3f} s")
        if args.num_tokens > 1:
            print(f"[Decode]  Tokens per second:   {1 / later:7.3f}")
