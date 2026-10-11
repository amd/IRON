# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What every model on IRON's operators shares: its shape (``Config``, and
``rope_angles``, the RoPE table it names), its weights, the float32
``Oracle`` it is judged by, ``Model``, a graph whose versions ``load()``
compiles up front in the packaging asked for, and ``Runner`` and ``main``,
a decoder's checkpoint, tokenizer and command line.

``Checkpoint`` maps a ``.safetensors`` file, or, given its
``.safetensors.index.json``, every shard a sharded checkpoint splits across.
``load_weights`` places its tensors in a tree by a model's *layout*: each
weight's path in the tree, its name in the checkpoint and its shape,
``{i}`` standing for a layer's index in both:

```python
{
    "embedding": ("model.embed_tokens.weight", (V, E)),
    "layers.{i}.q": ("model.layers.{i}.self_attn.q_proj.weight", (Q, E)),
    ...
}
```

makes ``weights.embedding`` and ``weights.layers[3].q``.
"""

import argparse
import dataclasses
import json
import math
import mmap
import struct
from collections.abc import Callable
from pathlib import Path
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron.common.graph.narrowing import CostTable, JointNarrowing, NarrowingKinds

from .generation import (
    SEED,
    Sampler,
    accuracy,
    determinism,
    generate,
    kl_stats,
)

if TYPE_CHECKING:
    # causal imports Config from here.
    from .causal import CausalLM

RopeScaling = Callable[[np.ndarray], np.ndarray]


def rope_angles(
    head_dim: int,
    context_length: int,
    rope_base: float = 500000.0,
    scaling: RopeScaling | None = None,
) -> np.ndarray:
    """The RoPE table, ``(context_length, head_dim)`` float32, cos and sin interleaved.

    Each transcendental is evaluated in float64 and rounded once.
    """
    exponents = np.arange(0, head_dim, 2, dtype=np.float32) / np.float32(head_dim)
    inv_freq = 1.0 / np.power(rope_base, exponents.astype(np.float64))
    if scaling is not None:
        inv_freq = scaling(inv_freq)
    inv_freq = inv_freq.astype(np.float32)
    freqs = np.outer(np.arange(context_length, dtype=np.float32), inv_freq)
    angles = np.empty((context_length, head_dim), dtype=np.float32)
    angles[:, ::2] = np.cos(freqs.astype(np.float64))
    angles[:, 1::2] = np.sin(freqs.astype(np.float64))
    return angles


@dataclasses.dataclass(frozen=True)
class Config:
    vocab_size: int
    emb_dim: int
    n_layers: int
    n_heads: int
    n_kv_groups: int
    head_dim: int
    hidden_dim: int
    max_seq_len: int
    rope_base: float
    rope_scaling: RopeScaling | None = None
    # The rotated prefix of head_dim (partial rotary, e.g. Phi's 0.75): None
    # rotates the whole head, as every full-rotary model does.
    rotary_dim: int | None = None
    # A post-trig scalar the whole angle table is multiplied by once at
    # build time (LongRoPE/YaRN's "mscale"): 1.0 leaves cos/sin as rotations.
    rope_attention_scaling: float = 1.0
    prefill_chunk: int = 2048

    def __post_init__(self):
        if self.max_seq_len % self.prefill_chunk:
            raise ValueError(
                f"prefill_chunk ({self.prefill_chunk}) must divide max_seq_len "
                f"({self.max_seq_len})"
            )

    @property
    def rope_width(self) -> int:
        """The angle table's own width: ``head_dim``, or ``rotary_dim`` under
        partial rotary.
        """
        return self.rotary_dim or self.head_dim

    def angles(self) -> np.ndarray:
        angles = rope_angles(
            self.rope_width, self.max_seq_len, self.rope_base, self.rope_scaling
        )
        if self.rope_attention_scaling != 1.0:
            angles = angles * np.float32(self.rope_attention_scaling)
        return angles


#: Each weight's path in the tree -> its checkpoint name and shape.
Layout = dict[str, tuple[str, tuple[int, ...]]]


class _Shard:
    """One ``.safetensors`` file, mapped: ``tensors`` are read-only views of
    it, read only when touched. The format is an 8-byte header length, a
    JSON header giving each tensor's dtype, shape and byte range, and the
    data. It is read here because safetensors' own numpy loader has no
    bfloat16.
    """

    DTYPES = {"BF16": bfloat16, "F16": np.float16, "F32": np.float32}

    def __init__(self, path: Path):
        self.path = path
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

    def release(self, array: np.ndarray) -> bool:
        """Drop the process's pages of ``array`` and report it was this
        shard's, if it is a view of this file; leave anything else alone and
        report so. It stays readable: a later read faults the bytes back in.
        What it saves is a weight counted twice, on the host and on the
        device.
        """
        begin = array.ctypes.data - self._address
        if not (array.flags.c_contiguous and 0 <= begin < len(self._map)):
            return False
        start = begin - begin % mmap.PAGESIZE
        self._map.madvise(mmap.MADV_DONTNEED, start, begin + array.nbytes - start)
        return True


class Checkpoint:
    """A ``.safetensors`` file, or, given its ``.safetensors.index.json``,
    every shard a sharded checkpoint splits across (``weight_map``, next to
    one another on disk), its tensors merged into one mapping, ``tensors``.
    """

    def __init__(self, path):
        self.path = Path(path)
        weight_map = self._weight_map(self.path)
        self._shards = [_Shard(p) for p in self._shard_paths(self.path, weight_map)]
        self.tensors: dict[str, np.ndarray] = {}
        for shard in self._shards:
            if weight_map is not None:
                named = {n for n, s in weight_map.items() if s == shard.path.name}
                if named != shard.tensors.keys():
                    raise ValueError(
                        f"{shard.path}: holds "
                        f"{sorted(shard.tensors.keys() - named)} the index does "
                        f"not name and lacks {sorted(named - shard.tensors.keys())}"
                    )
            overlap = sorted(self.tensors.keys() & shard.tensors.keys())
            if overlap:
                raise ValueError(f"{self.path}: {overlap} is in more than one shard")
            self.tensors.update(shard.tensors)

    @staticmethod
    def _weight_map(path: Path) -> dict[str, str] | None:
        """``path``'s own ``weight_map``, or ``None`` for a single file."""
        if path.suffix != ".json":
            return None
        return json.loads(path.read_text())["weight_map"]

    @staticmethod
    def _shard_paths(path: Path, weight_map: dict[str, str] | None) -> list[Path]:
        """``path`` itself, or, given its ``weight_map``, every shard it
        names, resolved beside it.
        """
        if weight_map is None:
            return [path]
        return [path.parent / name for name in sorted(set(weight_map.values()))]

    def release(self, array: np.ndarray) -> None:
        """Drop the process's pages of ``array`` if it is a view of one of
        the checkpoint's files; anything else is left alone.
        """
        for shard in self._shards:
            if shard.release(array):
                return


def checkpoint_shapes(layout: Layout, n_layers: int) -> dict[str, tuple[int, ...]]:
    """Every tensor a checkpoint of ``layout`` over ``n_layers`` holds, by name."""
    return {name: shape for name, (_, shape) in _expand(layout, n_layers).items()}


def random_weights(layout: Layout, n_layers: int, seed: int = 0) -> SimpleNamespace:
    """The tree of ``layout`` over ``n_layers``, drawn at ``seed`` in place of
    a checkpoint: each matrix normal with deviation ``1/sqrt(in)`` (an
    embedding's ``in`` its width), each norm weight one.
    """
    rng = np.random.default_rng(seed)
    tensors = {
        name: (
            np.ones(shape, dtype=bfloat16)
            if len(shape) == 1
            else (
                rng.standard_normal(shape, dtype=np.float32) / np.sqrt(shape[1])
            ).astype(bfloat16)
        )
        for name, shape in checkpoint_shapes(layout, n_layers).items()
    }
    return load_weights(tensors, layout, n_layers)


def unread_weights(layout: Layout, n_layers: int) -> SimpleNamespace:
    """The tree of ``layout`` over ``n_layers``, its arrays allocated and
    never written: for tracing, building and measuring a model, none of
    which reads a weight. The pages are reserved, not touched.
    """
    tensors = {
        name: np.empty(shape, dtype=bfloat16)
        for name, shape in checkpoint_shapes(layout, n_layers).items()
    }
    return load_weights(tensors, layout, n_layers)


def load_weights(tensors: dict, layout: Layout, n_layers: int) -> SimpleNamespace:
    """The tree of ``layout`` over ``n_layers``, from ``tensors`` by
    checkpoint name. The arrays are used as they are. Strict: a missing
    name, one with no place in the layout (an untied ``lm_head.weight``, say)
    and a shape other than the layout's all raise.
    """
    expected = _expand(layout, n_layers)
    missing = sorted(expected.keys() - tensors.keys())
    unknown = sorted(tensors.keys() - expected.keys())
    wrong = [
        f"{name} is {tensors[name].shape}, expected {shape}"
        for name, (_, shape) in expected.items()
        if name in tensors and tuple(tensors[name].shape) != shape
    ]
    if missing or unknown or wrong:
        raise ValueError(
            f"the checkpoint is not the model's: missing {missing}, "
            f"no place for {unknown}, {wrong}"
        )
    nested: dict = {}
    for name, (path, _) in expected.items():
        *parents, leaf = path.split(".")
        node = nested
        for key in parents:
            node = node.setdefault(key, {})
        node[leaf] = tensors[name]
    return _tree(nested)


def _expand(layout: Layout, n_layers: int) -> dict[str, tuple[str, tuple]]:
    """Checkpoint name -> (path, shape), ``{i}`` expanded over the layers:
    the model's own tensors, then each layer's, in the layout's order.
    """
    each = [entry for entry in layout.items() if "{i}" not in entry[0]]
    per_layer = [entry for entry in layout.items() if "{i}" in entry[0]]
    out = {name: (path, tuple(shape)) for path, (name, shape) in each}
    for i in range(n_layers):
        for path, (name, shape) in per_layer:
            out[name.format(i=i)] = (path.format(i=i), tuple(shape))
    return out


def _tree(node) -> Any:
    """Nested dicts as namespaces, those keyed ``0..n-1`` as lists."""
    if not isinstance(node, dict):
        return node
    items = {key: _tree(child) for key, child in node.items()}
    if all(key.isdigit() for key in items):
        return [items[str(i)] for i in range(len(items))]
    return SimpleNamespace(**items)


class Oracle:
    """A decoder's float32 forward pass on the host, the oracle the model is judged by.

    It is numpy, not composed from the operators' references, so it catches
    a wiring mistake the graph's own reference would repeat. A layer's
    weights are widened to float32 as the pass reaches it, so beside the
    checkpoint it holds in float32 one layer's and the model's own (the
    embedding, the final norm), not all of them.
    """

    embedding: np.ndarray
    layers: list

    def __init__(self, config: Config, weights):
        self.config = config
        vars(self).update(
            {k: v if k == "layers" else _widen(v) for k, v in vars(weights).items()}
        )
        self.angles = config.angles()
        self.buffers: dict[str, np.ndarray] = {}

    def layer(self, angles, w, x):
        raise NotImplementedError(f"{type(self).__name__} defines no layer()")

    def head(self, x):
        raise NotImplementedError(f"{type(self).__name__} defines no head()")

    def embed(self, x, pixel_values=None):
        return x

    def logits(self, tokens, pixel_values=None) -> np.ndarray:
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        angles = self.angles[: tokens.size]
        x = self.embed(self.embedding[tokens], pixel_values)
        for w in self.layers:
            x = self.layer(angles, _widen(w), x)
        return self.head(x[-1])

    @staticmethod
    def rotate(x, angles):
        cos, sin = angles[:, None, ::2], angles[:, None, 1::2]
        x1, x2 = np.split(x, 2, axis=-1)
        return np.concatenate([x1 * cos - x2 * sin, x1 * sin + x2 * cos], axis=-1)

    def buffer(self, name: str, shape: tuple[int, ...]) -> np.ndarray:
        """A float32 array of `shape` that `name` reuses from call to call.

        A temporary past glibc's mmap threshold is mapped afresh and faulted
        in page by page, which under memory pressure costs more than the
        arithmetic.

        Args:
            name: What the array holds; one array per name.
            shape: Its shape this time.

        Returns:
            A view of the array, its contents undefined.
        """
        size = math.prod(shape)
        held = self.buffers.get(name)
        if held is None or held.size < size:
            # Headroom, so a history growing a token a step seldom reallocates.
            held = np.empty(
                size if held is None else max(size, held.size * 5 // 4), np.float32
            )
            self.buffers[name] = held
        return held[:size].reshape(shape)

    def attend(self, q, k, v):
        n, H, D = q.shape
        k, v = (np.repeat(a, H // self.config.n_kv_groups, axis=1) for a in (k, v))
        # Batched matmuls, not einsum: BLAS is 10x faster at 3k.
        p = np.matmul(
            q.transpose(1, 0, 2),
            k.transpose(1, 2, 0),
            out=self.buffer("scores", (H, n, n)),
        )
        p *= np.float32(1 / np.sqrt(D))
        p += np.triu(np.full((n, n), -np.inf, dtype=np.float32), k=1)
        p -= p.max(axis=-1, keepdims=True)
        np.exp(p, out=p)
        p /= p.sum(axis=-1, keepdims=True)
        return (p @ v.transpose(1, 0, 2)).transpose(1, 0, 2).reshape(n, H * D)


def _widen(value):
    if isinstance(value, np.ndarray):
        return value.astype(np.float32)
    if isinstance(value, list):
        return [_widen(v) for v in value]
    if isinstance(value, SimpleNamespace):
        return SimpleNamespace(**{k: _widen(v) for k, v in vars(value).items()})
    return value


class Model(iron.Graph):
    """A model's graph, every version ``shapes()`` names compiled by
    ``load()`` before the first call, so the arena is made once. A
    decoder's two versions feed one another, so ``CausalLM`` loads its own.
    """

    def shapes(self) -> list[dict]:
        """The input shapes of each version."""
        raise NotImplementedError(f"{type(self).__name__} defines no shapes()")

    def load(
        self, tuner: JointNarrowing | None = None, boundaries: str | None = None
    ) -> "Model":
        """Compile every version.

        Args:
            tuner: Narrows and packs each version's designs by cost.
            boundaries: Each version's packaging; NPU1 derives its own.
        """
        for shapes in self.shapes():
            self.compile(coresident=tuner, boundaries=boundaries, **shapes)
        return self


class Runner:
    """A checkpoint, its tokenizer and ``config``, and the models on them.

    A subclass names the model: its ``config``; ``layout(config)``, where
    each weight is in the checkpoint; ``model``, the ``CausalLM`` on the
    NPU, whose ``oracle`` is the CPU model it is checked against;
    ``open_tokenizer(path)``, with ``encode`` and ``decode``; and ``bos``,
    the token every prompt starts with. A model that comes in several sizes
    names them in ``sizes``, ``config`` among them, and ``--size`` picks one.

    The checkpoint is mapped, not read: ``npu`` uploads it a piece at a
    time and drops each piece's host pages once it is on the device.

    With no checkpoint the weights are drawn at ``seed``
    (``random_weights``), and with no tokenizer a prompt is random tokens:
    the model's speed, its accuracy against its oracle and its determinism
    are then measured on a host without the files.
    """

    config: Config
    sizes: dict[str, Config] = {}
    model: "type[CausalLM]"
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
            "weights_path",
            nargs="?",
            help="the .safetensors checkpoint, or a sharded one's "
            "model.safetensors.index.json",
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
        self,
        cost_table: Path | None = None,
        boundaries: str | None = None,
        kinds: NarrowingKinds | None = None,
    ) -> "CausalLM":
        """The model compiled and loaded, weights uploaded. With a
        ``cost_table`` (``tune``) each version's designs are folded,
        narrowed and packed by it, restricted to ``kinds`` if given
        (``NarrowingKinds()``, every kind, if not: today's plan);
        ``boundaries`` are its decode step's (``CausalLM.load``).
        """
        model = self.model(self.config, self.weights)
        tuner = (
            None
            if cost_table is None
            else JointNarrowing(CostTable(cost_table), kinds=kinds or NarrowingKinds())
        )
        release = None if self.checkpoint is None else self.checkpoint.release
        return model.load(release, tuner, boundaries)

    def cpu(self) -> Oracle:
        """The model's oracle over the same weights, widened a layer at a time."""
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
    if runner.sizes:
        parser.add_argument(
            "--size",
            choices=runner.sizes,
            default=next(n for n, c in runner.sizes.items() if c == runner.config),
            help="the model's size (default: %(default)s)",
        )
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
        help="rows the caches hold, prompt and generated tokens together, a "
        f"multiple of {runner.config.prefill_chunk} "
        "(default: the size's own)",
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
        "--compare-host",
        action="store_true",
        help="after drawing on the device, generate again drawing on the host "
        "from the same seed and count the tokens that differ",
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

    config = runner.sizes[args.size] if runner.sizes else runner.config
    if args.max_seq_len is not None:
        try:
            config = dataclasses.replace(config, max_seq_len=args.max_seq_len)
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
        drawn, first, later = model.generate(tokens, args.num_tokens, sampler())
        print(run.decode(drawn), end="", flush=True)
        report(first, later)
        if args.compare_host:
            print("\n[Host loop]\n" + run.decode(tokens[1:]), end="")
            host, _, _ = generate(model, tokens, args.num_tokens, sampler(), show)
            print(run.decode(pending), end="")
            differ = sum(a != b for a, b in zip(drawn, host))
            print(
                f"\n[Device] Tokens differing from the host loop: {differ}/{len(host)}"
            )
