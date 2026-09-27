#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Running Llama 3.2: the config, the checkpoint, the tokenizer, sampling,
and the loops that generate and check, over any model.

A model is anything with ``logits(tokens)``: the logits after the last of
``tokens``, the whole history so far, as ``(vocab_size,)``. The NPU's
(:class:`.npu.Llama3_2_1b`) and the CPU's (:class:`.cpu.Reference`) are
built alike from a :class:`Config` and the weights :func:`load_weights`
reads; :class:`Runner` does both from a checkpoint and a tokenizer.
:func:`generate`, :func:`accuracy` and :func:`determinism` take models.

Run it with ``python -m iron.applications.llama_3_2_1b.runner``.
"""

import argparse
import json
import mmap
import struct
import time
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import tiktoken
import tiktoken.load
from ml_dtypes import bfloat16

from iron.operators.rope.op import LLAMA_3_2, Llama3RopeScaling, rope_angles

from .cpu import Reference
from .npu import Llama3_2_1b

#: Seeds the sampler, so a run's text is reproducible.
SEED = 1608560892


@dataclass(frozen=True)
class Config:
    """Llama 3.2's shape: 1B's unless given. ``max_seq_len`` is the rows
    the caches hold, prompt and generated tokens together.
    """

    vocab_size: int = 128256
    emb_dim: int = 2048
    n_layers: int = 16
    n_heads: int = 32
    n_kv_groups: int = 8
    head_dim: int = 64
    hidden_dim: int = 8192
    max_seq_len: int = 2048
    rope_base: float = 500000.0
    rope_scaling: Llama3RopeScaling | None = LLAMA_3_2

    def angles(self) -> np.ndarray:
        """The RoPE table, ``(max_seq_len, head_dim)`` float32."""
        return rope_angles(
            self.head_dim, self.max_seq_len, self.rope_base, self.rope_scaling
        )


# The weights
# ##########################################################################

# Each layer's weights, by the checkpoint's name for them.
LAYER = {
    "norm1": "input_layernorm",
    "q": "self_attn.q_proj",
    "k": "self_attn.k_proj",
    "v": "self_attn.v_proj",
    "o": "self_attn.o_proj",
    "norm2": "post_attention_layernorm",
    "gate": "mlp.gate_proj",
    "up": "mlp.up_proj",
    "down": "mlp.down_proj",
}


def checkpoint_shapes(config: Config) -> dict[str, tuple[int, ...]]:
    """Every tensor a checkpoint of ``config``'s shape holds, by name: each
    matrix ``(out, in)``. The output head is the embedding, tied.
    """
    E, F, V = config.emb_dim, config.hidden_dim, config.vocab_size
    Q, KV = config.n_heads * config.head_dim, config.n_kv_groups * config.head_dim
    layer = dict(
        norm1=(E,), q=(Q, E), k=(KV, E), v=(KV, E), o=(E, Q),
        norm2=(E,), gate=(F, E), up=(F, E), down=(E, F),
    )  # fmt: skip
    shapes = {"model.embed_tokens.weight": (V, E), "model.norm.weight": (E,)}
    for i in range(config.n_layers):
        for field, name in LAYER.items():
            shapes[f"model.layers.{i}.{name}.weight"] = layer[field]
    return shapes


def load_weights(tensors: dict, config: Config) -> SimpleNamespace:
    """The model's weights, ``embedding``, ``norm`` and ``layers[i].<field>``
    of :data:`LAYER`, from ``tensors`` by checkpoint name. The arrays are
    used as they are. Strict: a missing name, one with no place here (an
    untied ``lm_head.weight``, say) and a shape other than ``config``'s all
    raise.
    """
    expected = checkpoint_shapes(config)
    missing = sorted(expected.keys() - tensors.keys())
    unknown = sorted(tensors.keys() - expected.keys())
    wrong = [
        f"{name} is {tensors[name].shape}, expected {shape}"
        for name, shape in expected.items()
        if name in tensors and tuple(tensors[name].shape) != shape
    ]
    if missing or unknown or wrong:
        raise ValueError(
            f"the checkpoint is not {config}: missing {missing}, "
            f"no place for {unknown}, {wrong}"
        )
    return SimpleNamespace(
        embedding=tensors["model.embed_tokens.weight"],
        norm=tensors["model.norm.weight"],
        layers=[
            SimpleNamespace(
                **{f: tensors[f"model.layers.{i}.{n}.weight"] for f, n in LAYER.items()}
            )
            for i in range(config.n_layers)
        ],
    )


class Checkpoint:
    """A ``.safetensors`` file, mapped: ``tensors`` are read-only views of
    it, read only when touched. The format is an 8-byte header length, a
    JSON header giving each tensor's dtype, shape and byte range, and the
    data.
    """

    DTYPES = {"BF16": bfloat16, "F16": np.float16, "F32": np.float32}

    def __init__(self, path):
        self.path = Path(path)
        with open(self.path, "rb") as f:
            # The mapping holds its own reference to the file.
            self._map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        data = np.frombuffer(self._map, dtype=np.uint8)
        self._address = data.ctypes.data
        (length,) = struct.unpack("<Q", self._map[:8])
        header = json.loads(self._map[8 : 8 + length])
        header.pop("__metadata__", None)
        self.tensors = {}
        for name, t in header.items():
            if t["dtype"] not in self.DTYPES:
                raise ValueError(f"{self.path}: {name} is {t['dtype']}")
            begin, end = (8 + length + o for o in t["data_offsets"])
            view = data[begin:end].view(self.DTYPES[t["dtype"]])
            self.tensors[name] = view.reshape(t["shape"])

    def release(self, array: np.ndarray) -> None:
        """Drop the process's pages of ``array`` if it is a view of the file;
        anything else is left alone. It stays readable: a later read faults
        the bytes back in. What it saves is a weight counted twice, on the
        host and on the device.
        """
        begin = array.ctypes.data - self._address
        if not (array.flags.c_contiguous and 0 <= begin < len(self._map)):
            return
        start = begin - begin % mmap.PAGESIZE
        self._map.madvise(mmap.MADV_DONTNEED, start, begin + array.nbytes - start)


# The tokenizer and sampling
# ##########################################################################

SPECIAL_TOKENS = {
    "<|begin_of_text|>": 128000,
    "<|end_of_text|>": 128001,
    "<|start_header_id|>": 128006,
    "<|end_header_id|>": 128007,
    "<|eot_id|>": 128009,
    **{
        f"<|reserved_{i}|>": i for i in [*range(128002, 128006), *range(128009, 128256)]
    },
}


def tokenizer(path) -> tiktoken.Encoding:
    return tiktoken.Encoding(
        name="llama3.2-1b",
        pat_str=r"(?i:'s|'t|'re|'ve|'m|'ll|'d)"
        r"|[^\r\n\p{L}\p{N}]?\p{L}+"
        r"|\p{N}{1,3}"
        r"| ?[^\s\p{L}\p{N}]+[\r\n]*"
        r"|\s*[\r\n]+"
        r"|\s+(?!\S)"
        r"|\s+",
        mergeable_ranks=tiktoken.load.load_tiktoken_bpe(str(path)),
        special_tokens=SPECIAL_TOKENS,
    )


class Sampler:
    """Temperature, then top-k, then a draw from the softmax.

    Logits are divided by the temperature, every logit below the
    ``top_k``-th largest is dropped (ties with it are kept), and a token is
    drawn from the softmax of what is left. The arithmetic is float32 over
    the (bf16) logits and the draw float64; a temperature of 0 is greedy
    (the argmax). The draw comes from ``rng``, so a seeded generator makes
    it reproducible.
    """

    def __init__(
        self,
        temperature: float,
        top_k: int | None,
        rng: np.random.Generator,
    ):
        if temperature < 0:
            raise ValueError(f"temperature {temperature} is negative")
        if top_k is not None and top_k < 1:
            raise ValueError(f"top_k {top_k} keeps no token")
        self.temperature = temperature
        self.top_k = top_k
        self.rng = rng

    def probabilities(self, logits: np.ndarray) -> np.ndarray:
        """The distribution a token is drawn from, float64, over ``logits`` (1-D)."""
        x = np.asarray(logits, dtype=np.float32).reshape(-1)
        x = x / np.float32(self.temperature)
        if self.top_k is not None and self.top_k < x.size:
            kth = np.partition(x, -self.top_k)[-self.top_k]
            x = np.where(x < kth, -np.inf, x)
        e = np.exp((x - x.max()).astype(np.float64))
        return e / e.sum()

    def __call__(self, logits: np.ndarray) -> int:
        """One token id drawn from a row of logits (any shape of one row)."""
        if self.temperature == 0:
            return greedy(logits)
        probs = self.probabilities(logits)
        cdf = np.cumsum(probs)
        # The first token whose cumulative mass exceeds the draw; a zero-mass
        # token never exceeds its predecessor, so it is never picked.
        token = int(np.searchsorted(cdf, self.rng.random() * cdf[-1], side="right"))
        # A draw just under 1 can round up to the total, past every token;
        # it belongs to the last one with any mass.
        return token if token < cdf.size else int(np.flatnonzero(probs)[-1])


def greedy(logits: np.ndarray) -> int:
    return int(np.argmax(np.asarray(logits, dtype=np.float32).reshape(-1)))


# Generating and checking
# ##########################################################################


def generate(model, tokens, num_tokens, sample, show=None):
    """Draw ``num_tokens`` after ``tokens``, each passed to ``show``.

    Returns the tokens drawn, the seconds to the first and the mean seconds
    per token after it (NaN for one token).
    """
    history, seconds = [int(t) for t in tokens], []
    for _ in range(num_tokens):
        start = time.perf_counter()
        history.append(sample(model.logits(history)))
        seconds.append(time.perf_counter() - start)
        if show is not None:
            show(history[-1])
    later = np.mean(seconds[1:]) if num_tokens > 1 else float("nan")
    return history[-num_tokens:], seconds[0], float(later)


def _log_softmax(logits):
    x = np.asarray(logits, dtype=np.float64).reshape(-1)
    x = x - x.max()
    return x - np.log(np.exp(x).sum())


def accuracy(model, reference, tokens, num_tokens) -> list[tuple[float, bool]]:
    """``model``'s next-token distributions against ``reference``'s, over
    ``num_tokens`` steps from ``tokens``.

    Teacher-forced: both are fed the reference's greedy token, so a
    divergence at a step is the model's own error there rather than the
    consequence of an earlier different choice. One ``(kl, top1)`` per step:
    KL(reference || model), and whether both rank the same token first.
    """
    history, results = [int(t) for t in tokens], []
    for step in range(num_tokens):
        got = _log_softmax(model.logits(history))
        ref = _log_softmax(reference.logits(history))
        kl = float(np.sum(np.exp(ref) * (ref - got)))
        top1 = int(got.argmax()) == int(ref.argmax())
        results.append((kl, top1))
        print(f"step {step:3d}  KL {kl:.5f}  top-1 {'match' if top1 else 'MISMATCH'}")
        history.append(int(ref.argmax()))
    return results


def determinism(model, prompts, num_tokens, rounds) -> int:
    """How many runs' logits differ bitwise from the first of their prompt.

    Each prompt runs ``rounds`` times, alternating, ``num_tokens`` greedy
    tokens each. Alternating prompts with different text matters: a host
    write that never reaches the device then reads the other prompt's data,
    not a leftover copy of its own.
    """
    first: list = [None] * len(prompts)
    differ = 0
    for r in range(rounds * len(prompts)):
        p = r % len(prompts)
        history, rows = [int(t) for t in prompts[p]], []
        for _ in range(num_tokens):
            logits = model.logits(history)
            rows.append(logits.view(np.uint8))  # NaNs and signed zeros too
            history.append(greedy(logits))
        run = np.stack(rows)
        if first[p] is None:
            first[p] = run
            continue
        steps = np.flatnonzero((run != first[p]).any(axis=1)).tolist()
        if steps:
            differ += 1
            print(f"round {r} (prompt {p}): logits differ at steps {steps}")
    return differ


# The application
# ##########################################################################


class Runner:
    """A checkpoint, its tokenizer and ``config``, and the models on them.

    The checkpoint is mapped, not read: :meth:`npu` uploads it a piece at a
    time and drops each piece's host pages once it is on the device.
    """

    def __init__(self, weights_path, tokenizer_path, config: Config = Config()):
        self.config = config
        self.checkpoint = Checkpoint(weights_path)
        self.weights = load_weights(self.checkpoint.tensors, config)
        self.tokenizer = tokenizer(tokenizer_path)

    def npu(self) -> Llama3_2_1b:
        """The model compiled and loaded, weights uploaded."""
        return Llama3_2_1b(self.config, self.weights).load(self.checkpoint.release)

    def cpu(self) -> Reference:
        """The float32 reference: 5 GB for 1B, widened on the spot."""
        return Reference(self.config, self.weights)

    def encode(self, text: str) -> list[int]:
        return [SPECIAL_TOKENS["<|begin_of_text|>"], *self.tokenizer.encode(text)]

    def prompt(self, chars: int, skip: int = 0) -> list[int]:
        """``chars`` characters of ``prompt.txt`` from ``skip`` on, encoded."""
        text = Path(__file__).with_name("prompt.txt").read_text()
        return self.encode(text[skip : skip + chars])


def main():
    parser = argparse.ArgumentParser(description="Llama 3.2 1B on the NPU")
    parser.add_argument("weights_path", help="model.safetensors")
    parser.add_argument("tokenizer_path", help="tokenizer.model (tiktoken)")
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
        help="instead of sampling, compare each step's logits with the float32 "
        "CPU reference's, feeding both the reference's greedy token",
    )
    check.add_argument(
        "--check-determinism",
        type=int,
        metavar="ROUNDS",
        help="instead of sampling, run two prompts ROUNDS times each, "
        "alternating, and count the runs whose logits differ bitwise",
    )
    args = parser.parse_args()

    runner = Runner(args.weights_path, args.tokenizer_path)
    tokens = runner.prompt(args.prompt_len)
    if len(tokens) + args.num_tokens > runner.config.max_seq_len:
        parser.error(
            f"a {len(tokens)}-token prompt and {args.num_tokens} more exceed "
            f"{runner.config.max_seq_len} rows"
        )
    model = runner.npu()

    if args.check_accuracy:
        # Over every step, prefill and decode alike: one step's KL depends as
        # much on how confident the reference is at that position as on the NPU.
        results = accuracy(model, runner.cpu(), tokens, args.num_tokens)
        kl = np.array([k for k, _ in results])
        print(f"[Accuracy] Mean KL: {kl.mean():.6f}")
        print(f"[Accuracy] P90 KL: {np.percentile(kl, 90):.6f}")
        print(f"[Accuracy] Max KL: {kl.max():.6f} (step {kl.argmax()})")
        print(f"[Accuracy] Top-1 mismatches: {sum(not t for _, t in results)}")
    elif args.check_determinism:
        # The second prompt is as much of the text as follows the first.
        prompts = [tokens, runner.prompt(args.prompt_len, skip=args.prompt_len)]
        rounds = args.check_determinism
        n_differ = determinism(model, prompts, args.num_tokens, rounds)
        print(f"[Determinism] Differing runs: {n_differ}/{2 * (rounds - 1)}")
    else:
        sample = Sampler(args.temperature, args.top_k, np.random.default_rng(SEED))
        print(runner.tokenizer.decode(tokens[1:]), end="", flush=True)

        def show(token):
            print(runner.tokenizer.decode([token]), end="", flush=True)

        _, first, later = generate(model, tokens, args.num_tokens, sample, show)
        print(f"\n\n[Prefill] Time to first token: {first:7.3f} s")
        if args.num_tokens > 1:
            print(f"[Decode]  Tokens per second:   {1 / later:7.3f}")


if __name__ == "__main__":
    main()
