# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Runner``, a checkpoint, its tokenizer and config and the models on
them, and ``main``, a model's command line.
"""

import argparse
import dataclasses
import functools
import inspect
import json
import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

from iron.tune.autotune import Call

from .checkpoint import Checkpoint
from .config import Config, DecoderConfig
from .golden import Golden, HuggingFace
from .generation import Sampler, accuracy, determinism, generate_on_host, kl_stats
from .model import Model, OnHost

if TYPE_CHECKING:
    # causal imports Runner from here.
    from .causal import CausalLM


logger = logging.getLogger(__name__)


# What a host keeps beside a model's arena: the OS, Python and XRT, the
# checkpoint's pages as they upload, a test's host copies.
HOST_RESERVE = 8 << 30


def host_budget() -> int:
    """The bytes a model's arena may take here: physical memory, in which
    the NPU's buffers live, less ``HOST_RESERVE``.
    """
    return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") - HOST_RESERVE


def prompt_text(chars: int, skip: int = 0) -> str:
    """``chars`` characters of ``prompt.txt``, from ``skip`` on: the text every
    model's long inputs are drawn from.
    """
    return Path(__file__).with_name("prompt.txt").read_text()[skip : skip + chars]


#: The flags a runner's CLI and pytest's fixtures read alike
#: (``Runner.add_arguments``, ``Runner.from_options``), each a tuple of
#: ``add_argument``'s own flag strings and keywords.
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


class Tokenizer:
    """Text to a prompt's token ids, ``bos`` first, and token ids back to
    text, over ``encoding``: anything with ``encode`` and ``decode``, as
    ``Runner.open_tokenizer`` gives.
    """

    def __init__(self, encoding, bos: int):
        self.encoding, self.bos = encoding, bos

    def __call__(self, text: str) -> list[int]:
        return [self.bos, *self.encoding.encode(text)]

    def decode(self, tokens) -> str:
        return self.encoding.decode(list(tokens))


class _TokenizerJson:
    """A Hugging Face ``tokenizer.json``, over ``tokenizers`` (not
    ``transformers``): text to token ids without the special tokens its
    post-processor adds, since ``Tokenizer`` puts the BOS first, and back.
    """

    def __init__(self, path):
        import tokenizers

        self._tokenizer = tokenizers.Tokenizer.from_file(str(path))

    def encode(self, text: str) -> list[int]:
        return self._tokenizer.encode(text, add_special_tokens=False).ids

    def decode(self, tokens) -> str:
        return self._tokenizer.decode(tokens)


class Runner:
    """A checkpoint, its tokenizer and ``config``, and the models on them.

    A subclass names its ``config`` (a ``Config`` class read from the
    checkpoint's ``config.json``), ``model`` (the ``CausalLM``) and
    ``open_tokenizer`` and its ``tokenizer_file``, and becomes the model's
    ``runner``; ``tune_arguments`` and ``tune_calls`` are what
    ``iron.lm.tune`` tunes its profile by. Given a ``seed``, the weights are
    drawn in the checkpoint's shapes and a prompt with no tokenizer is
    random tokens, so speed, accuracy and determinism need neither.
    """

    config: Config | type[Config]
    model: "type[CausalLM]"
    # What loads the checkpoint into transformers to record its goldens.
    hugging_face: type = HuggingFace
    # The tokenizer's file in the model's Hugging Face repository.
    tokenizer_file = "tokenizer.json"

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # The first Runner naming a model is what ``CausalLM.load`` builds.
        if "model" in vars(cls) and "runner" not in vars(cls.model):
            cls.model.runner = cls

    @functools.cached_property
    def bos(self) -> int:
        """The token every prompt starts with: the checkpoint's
        ``config.json``'s ``bos_token_id``, unless a subclass names it.
        """
        path = Path(self.checkpoint.path).parent / "config.json"
        bos = json.loads(path.read_text()).get("bos_token_id")
        if bos is None:
            raise KeyError(f"{path} has no bos_token_id: name the runner's bos")
        return bos

    @staticmethod
    def open_tokenizer(path):
        """The tokenizer at ``path``: a Hugging Face ``tokenizer.json``."""
        return _TokenizerJson(path)

    @classmethod
    def default_config(cls, weights_path) -> Config:
        """``cls.config`` itself, if it is already one shape; else that
        class's own, built from ``weights_path``'s checkpoint directory
        (``Config.from_checkpoint``).
        """
        if isinstance(cls.config, type):
            return cls.config.from_checkpoint(weights_path)
        return cls.config

    @classmethod
    def tune_arguments(cls, parser: argparse.ArgumentParser) -> None:
        """The flags ``tune_calls`` follows from: the checkpoint whose header
        gives the weights' shapes, the decode step's position and token, the
        contexts attention over the cache is timed at, and the sampling
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

    @classmethod
    def tune_calls(
        cls, parser: argparse.ArgumentParser, args: argparse.Namespace
    ) -> list[Call]:
        """The calls the model's designs are timed in (``CausalLM.tune_calls``),
        on weights it never reads.
        """
        config = cls.default_config(args.checkpoint)
        if args.context > config.max_seq_len:
            parser.error(
                f"--context {args.context} is past max_seq_len {config.max_seq_len}"
            )
        model = cls.model(config, Checkpoint(args.checkpoint).tree("unread"))
        sample = Sampler(args.temperature, args.top_k)
        return model.tune_calls(
            sample, args.position, args.token, args.context, args.points
        )

    def __init__(
        self,
        weights_path,
        tokenizer_path=None,
        config: Config | None = None,
        seed: int | None = None,
    ):
        if config is None:
            config = type(self).fit(
                type(self).default_config(weights_path), weights_path
            )
        self.config = config
        self.seed = seed
        self.checkpoint = Checkpoint(weights_path)
        self.weights = (
            self.checkpoint.tree()
            if seed is None
            else self.checkpoint.tree("random", seed)
        )
        self.tokenizer = (
            None
            if tokenizer_path is None
            else Tokenizer(self.open_tokenizer(tokenizer_path), self.bos)
        )

    @classmethod
    def add_arguments(cls, parser: argparse.ArgumentParser) -> None:
        """The checkpoint and tokenizer, and ``FLAGS``: the same flags ``main()``'s CLI and the
        pytest fixtures read a runner's options by (``from_options``).
        """
        parser.add_argument(
            "weights_path",
            help="the .safetensors checkpoint, or a sharded one's "
            "model.safetensors.index.json",
        )
        parser.add_argument("tokenizer_path", nargs="?", help="the tokenizer's file")
        for flags, kwargs in FLAGS:
            parser.add_argument(*flags, **kwargs)

    @classmethod
    def from_arguments(
        cls,
        parser: argparse.ArgumentParser,
        args: argparse.Namespace,
        config: Config | None = None,
    ) -> "Runner":
        """The runner ``add_arguments``'s arguments name."""
        if args.random_weights is None and args.tokenizer_path is None:
            parser.error("give the tokenizer, or --random-weights")
        if args.random_weights is not None and args.tokenizer_path is not None:
            parser.error("--random-weights takes no tokenizer")
        return cls(args.weights_path, args.tokenizer_path, config, args.random_weights)

    @classmethod
    def from_options(
        cls,
        args: "list[str] | argparse.Namespace | None" = None,
        parser: argparse.ArgumentParser | None = None,
    ) -> "Runner":
        """A runner from ``args``, parsed or option strings: the checkpoint's
        config.json gives the shape, narrowed by ``--max-seq-len``, and ``from_arguments`` builds the runner.

        Args:
            args: The parsed namespace, or the option strings to parse
                (``sys.argv[1:]`` if ``None``).
            parser: The namespace's own parser, for ``from_arguments``'s
                errors; built here (and ``args`` parsed against it) when
                ``args`` is not already one.
        """
        if not isinstance(args, argparse.Namespace):
            parser = argparse.ArgumentParser()
            cls.add_arguments(parser)
            args = parser.parse_args(args)
        config = cls.default_config(args.weights_path)
        if args.max_seq_len is None:
            config = cls.fit(config, args.weights_path)
        elif args.max_seq_len > config.max_seq_len:
            parser.error(
                f"--max-seq-len {args.max_seq_len} is past the model's "
                f"{config.max_seq_len}"
            )
        else:
            config = dataclasses.replace(config, max_seq_len=args.max_seq_len)
        return cls.from_arguments(parser, args, config)

    @classmethod
    def fit(cls, config: Config, weights_path, budget: int | None = None) -> Config:
        """``config`` at its native context where the model's arena fits
        ``budget`` (``host_budget()`` by default), else at the longest whole
        number of prompt chunks that does, logged either way.

        The arena is what the model holds, weights and states, measured by
        tracing its decode step at one and two prompt chunks of context:
        what grows holds a row a position (``tests/applications/
        long_context``).
        """
        if not isinstance(config, DecoderConfig):
            return config
        native, C = config.max_seq_len, config.prefill_chunk
        if native < 2 * C:
            return config
        tree = Checkpoint(weights_path).tree("unread")
        held = []
        for length in (C, 2 * C):
            model = cls.model(dataclasses.replace(config, max_seq_len=length), tree)
            # What it holds does not follow its tunables, nor need a device.
            model.profile = None
            held.append(sum(model.trace(**model.shapes()[0]).pinned.values()))
        per_position = (held[1] - held[0]) / C
        fixed = held[0] - per_position * C
        budget = host_budget() if budget is None else budget
        need = fixed + per_position * native
        if need <= budget:
            logger.info(
                "max_seq_len %d, the model's native context: %.1f GiB of a %.1f GiB "
                "budget",
                native,
                need / 2**30,
                budget / 2**30,
            )
            return config
        fits = int((budget - fixed) // per_position) // C * C
        if fits < C:
            raise ValueError(
                f"{fixed / 2**30:.1f} GiB of weights and one {C}-position chunk "
                f"do not fit a {budget / 2**30:.1f} GiB budget"
            )
        logger.warning(
            "max_seq_len %d, not the native %d: the model would hold %.1f GiB "
            "there, past this host's %.1f GiB budget (physical memory less %.0f "
            "GiB); --max-seq-len asks for up to %d",
            fits,
            native,
            need / 2**30,
            budget / 2**30,
            HOST_RESERVE / 2**30,
            native,
        )
        return dataclasses.replace(config, max_seq_len=fits)

    def build(self) -> "Model":
        """The model on ``config`` and the weights, not yet loaded."""
        return self.model(self.config, self.weights)

    def npu(self, full_elf: bool | None = None) -> "Model":
        """``build()``'s model compiled and loaded, weights uploaded;
        ``full_elf`` is every version's packaging (``Model.load_versions``).
        """
        return self.build().load_versions(
            release=self.checkpoint.release, full_elf=full_elf
        )

    def reference(self):
        """What the model is judged by: with drawn weights, its own graph on
        the host (``OnHost``); else ``hugging_face``'s logits, recorded
        beside the checkpoint (``golden.npz``) from its ``config.json`` and
        its tensors (``Checkpoint.fingerprint``).
        """
        if self.seed is not None:

            class Host(OnHost, self.model):
                pass

            return Host(self.config, self.weights)
        directory = Path(self.checkpoint.path).parent
        return Golden(
            directory / "golden.npz",
            lambda: self.hugging_face.load(directory),
            ((directory / "config.json").read_text(), self.checkpoint.fingerprint()),
        )

    def decode(self, tokens: list[int]) -> str:
        """``tokens`` as text, or as their numbers with no tokenizer."""
        if self.tokenizer is None:
            return "".join(f" {t}" for t in tokens)
        return self.tokenizer.decode(tokens)

    def prompt(self, chars: int, skip: int = 0) -> list[int]:
        """``chars`` characters of ``prompt.txt`` from ``skip`` on, tokenized.

        With no tokenizer, ``chars // 3`` tokens drawn at ``seed`` and
        ``skip``: a little more than the text encodes to (Llama 3's
        tokenizer takes 3.7 characters a token), so a check sized in
        characters runs at about its size on the text.
        """
        if self.tokenizer is None:
            rng = np.random.default_rng((self.seed, skip))
            draw = rng.integers(0, self.config.vocab_size, chars // 3 - 1)
            return [self.bos, *draw]
        return self.tokenizer(prompt_text(chars, skip))


def sampling_arguments(parser: argparse.ArgumentParser) -> None:
    """``--temperature`` and ``--top-k``, a ``Sampler``'s, at its defaults."""
    defaults = inspect.signature(Sampler).parameters
    parser.add_argument(
        "--temperature", type=float, default=defaults["temperature"].default
    )
    parser.add_argument("--top-k", type=int, default=defaults["top_k"].default)


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
    run = runner.from_options(args, parser)
    tokens = run.prompt(args.prompt_len)
    if len(tokens) + args.num_tokens > run.config.max_seq_len:
        parser.error(
            f"a {len(tokens)}-token prompt and {args.num_tokens} more exceed "
            f"{run.config.max_seq_len} rows"
        )
    model = run.npu(args.full_elf)

    if args.check_accuracy:
        results = accuracy(model, run.reference(), tokens, args.num_tokens)
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
            return Sampler(args.temperature, args.top_k)

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
        drawn, first, later = model.generate(tokens, args.num_tokens, sampler())
        print(run.decode(drawn), end="", flush=True)
        report(first, later)
        if args.compare_host:
            print("\n[Host loop]\n" + run.decode(tokens[1:]), end="")
            host, _, _ = generate_on_host(
                model, tokens, args.num_tokens, sampler(), show
            )
            print(run.decode(pending), end="")
            differ = sum(a != b for a, b in zip(drawn, host))
            print(
                f"\n[Device] Tokens differing from the host loop: {differ}/{len(host)}"
            )
