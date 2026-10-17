# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What every model on IRON's operators shares: its shape, its weights
(``Checkpoint.tree()``, the tensors by their own names:
``model.layers.3.self_attn.q_proj.weight`` is
``weights.model.layers[3].self_attn.q_proj.weight``; ``Derived``, those
computed from them), the float32 ``Oracle`` it is judged by, ``Model``,
and ``Runner`` and ``main``.
"""

import argparse
import dataclasses
import json
import logging
import math
import mmap
import os
import struct
from collections.abc import Callable, Mapping
from functools import partial
from pathlib import Path
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any, Literal

import aie.utils as aie_utils
import numpy as np
from ml_dtypes import bfloat16

import iron
from iron.common.graph.tuner import Tuner
from iron.operators import ElementwiseAdd, ElementwiseMul, SiLU
from iron.tune.narrowing import CostTable, JointNarrowing, NarrowingKinds
from iron.tune.probe import Call

from .blocks import Layer
from .generation import (
    SEED,
    Sampler,
    accuracy,
    determinism,
    generate_on_host,
    kl_stats,
)

if TYPE_CHECKING:
    # causal imports Config from here.
    from .causal import CausalLM

RopeScaling = Callable[[np.ndarray], np.ndarray]

logger = logging.getLogger(__name__)

# What a host keeps beside a model's arena: the OS, Python and XRT, the
# checkpoint's pages as they upload, a test's host copies.
HOST_RESERVE = 8 << 30


def host_budget() -> int:
    """The bytes a model's arena may take here: physical memory, in which
    the NPU's buffers live, less ``HOST_RESERVE``.
    """
    return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") - HOST_RESERVE


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


_MISSING = object()


def _dotted(data: dict, path: str):
    node = data
    for key in path.split("."):
        if not isinstance(node, dict) or key not in node:
            return _MISSING
        node = node[key]
    return node


@dataclasses.dataclass(frozen=True)
class Config:
    """A model's shape: a decoder's (``DecoderConfig``) and EmbeddingGemma
    2's own subclass it, for the one field every model judges its RMS norms
    by and the one way every model is built from a checkpoint's own
    ``config.json``.
    """

    eps: float = dataclasses.field(
        default=1e-6, kw_only=True, metadata={"json": "rms_norm_eps"}
    )

    @classmethod
    def from_checkpoint(cls, path) -> "Config":
        """``cls``'s fields named in ``path``'s own ``config.json``: each
        field's own ``metadata["json"]``, a dot-separated path from the
        file's root, converted by its ``metadata["convert"]`` if it names
        one; a field with no ``"json"`` entry is an IRON choice, not the
        checkpoint's, and keeps its default, as does one the file leaves
        null.

        Args:
            path: A ``config.json``, or a checkpoint's directory or file
                (its directory's ``config.json`` is read).

        Raises:
            FileNotFoundError: No ``config.json`` is there.
        """
        path = Path(path)
        if path.name != "config.json":
            path = (path if path.is_dir() else path.parent) / "config.json"
        data = json.loads(path.read_text())
        kwargs = {}
        for f in dataclasses.fields(cls):
            key = f.metadata.get("json")
            if key is None:
                continue
            value = _dotted(data, key)
            # Hugging Face writes an unset option as null.
            if value is _MISSING or value is None:
                continue
            convert = f.metadata.get("convert")
            kwargs[f.name] = convert(value) if convert else value
        return cls(**kwargs)

    def layer(self, i: int) -> Layer:
        """Layer ``i`` as the config describes it."""
        raise NotImplementedError(f"{type(self).__name__} describes no layer")


@dataclasses.dataclass(frozen=True)
class DecoderConfig(Config):
    """A decoder's shape, named as a Hugging Face checkpoint's own
    ``config.json`` does where it has one. ``max_seq_len``, the longest
    context served, is the checkpoint's native ``max_position_embeddings``
    unless a caller lowers it; ``prefill_chunk`` is IRON's own prompt
    chunking.
    """

    vocab_size: int = dataclasses.field(metadata={"json": "vocab_size"})
    emb_dim: int = dataclasses.field(metadata={"json": "hidden_size"})
    n_layers: int = dataclasses.field(metadata={"json": "num_hidden_layers"})
    n_heads: int = dataclasses.field(metadata={"json": "num_attention_heads"})
    n_kv_groups: int = dataclasses.field(metadata={"json": "num_key_value_heads"})
    # None where the checkpoint's own config.json has no head_dim (Qwen 2.5,
    # Granite, LFM2, Phi-4-mini-instruct): __post_init__ derives it.
    head_dim: int | None = dataclasses.field(
        default=None, kw_only=True, metadata={"json": "head_dim"}
    )
    hidden_dim: int = dataclasses.field(metadata={"json": "intermediate_size"})
    # None turns nothing: a decoder of absolute positions (``positions``).
    rope_base: float | None = dataclasses.field(metadata={"json": "rope_theta"})
    max_seq_len: int = dataclasses.field(metadata={"json": "max_position_embeddings"})
    rope_scaling: RopeScaling | None = None
    # The rotated prefix of head_dim (partial rotary, e.g. Phi's 0.75): None
    # rotates the whole head, as every full-rotary model does.
    rotary_dim: int | None = None
    # A post-trig scalar the whole angle table is multiplied by once at
    # build time (LongRoPE/YaRN's "mscale"): 1.0 leaves cos/sin as rotations.
    rope_attention_scaling: float = 1.0
    prefill_chunk: int = 2048
    hidden_act: str = dataclasses.field(default="silu", metadata={"json": "hidden_act"})

    def __post_init__(self):
        if self.head_dim is None:
            object.__setattr__(self, "head_dim", self.emb_dim // self.n_heads)

    @property
    def rope_width(self) -> int:
        """The angle table's own width: ``head_dim``, or ``rotary_dim`` under
        partial rotary.
        """
        return self.rotary_dim or self.head_dim

    def angles(self) -> np.ndarray | None:
        """The RoPE table, a row per position; None with no ``rope_base``."""
        if self.rope_base is None:
            return None
        angles = rope_angles(
            self.rope_width, self.max_seq_len, self.rope_base, self.rope_scaling
        )
        if self.rope_attention_scaling != 1.0:
            angles = angles * np.float32(self.rope_attention_scaling)
        return angles

    def layer(self, i: int) -> Layer:
        """Layer ``i``: every layer of a decoder is alike."""
        return Layer(
            heads=self.n_heads,
            groups=self.n_kv_groups,
            head_dim=self.head_dim,
            eps=self.eps,
            activation=self.hidden_act,
            rotary=self.rotary_dim,
        )


def prompt_text(chars: int, skip: int = 0) -> str:
    """``chars`` characters of ``prompt.txt``, from ``skip`` on: the text every
    model's long inputs are drawn from.
    """
    return Path(__file__).with_name("prompt.txt").read_text()[skip : skip + chars]


class _Shard:
    """One ``.safetensors`` file, mapped: ``tensors`` are read-only views of
    it, read only when touched. Parsed here: safetensors' own numpy loader
    has no bfloat16.
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
        """Drop the process's pages of ``array`` if it is a view of this
        file, and report whether it was; it stays readable, a later read
        faulting the bytes back in.
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
        weight_map = None
        paths = [self.path]
        if self.path.suffix == ".json":
            weight_map = json.loads(self.path.read_text())["weight_map"]
            paths = [self.path.parent / n for n in sorted(set(weight_map.values()))]
        self._shards = [_Shard(p) for p in paths]
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

    def release(self, array: np.ndarray) -> None:
        """Drop the process's pages of ``array`` if it is a view of one of
        the checkpoint's files; anything else is left alone.
        """
        for shard in self._shards:
            if shard.release(array):
                return

    def tree(
        self, fill: Literal["read", "random", "unread"] = "read", seed: int = 0
    ) -> SimpleNamespace:
        """The checkpoint as a tree of its tensors' names, each split at its
        dots: ``model.layers.3.self_attn.q_proj.weight`` is
        ``tree.model.layers[3].self_attn.q_proj.weight``, a run of indices a
        list.

        Args:
            fill: What the arrays hold. ``"read"``: the tensors, views of the
                mapped file read only when touched. ``"random"``: drawn at
                ``seed`` in the file's order, each matrix normal with
                deviation ``1/sqrt(in)`` (an embedding's ``in`` its width),
                anything of fewer than two axes one. ``"unread"``: allocated
                and never written, for tracing, building and measuring a
                model, none of which reads a weight; the pages are reserved,
                not touched, and a scalar is zero, since a graph may read one
                as it is built (a clamp's bounds). Only ``"read"`` reads past
                the header.
            seed: The seed ``"random"`` draws at.

        Raises:
            ValueError: ``fill`` is none of these, or a run of indices skips
                one.
        """
        if fill == "read":
            tensors = self.tensors
        elif fill == "random":
            rng = np.random.default_rng(seed)
            tensors = {
                name: (
                    np.ones(t.shape, t.dtype)
                    if t.ndim < 2
                    else (
                        rng.standard_normal(t.shape, dtype=np.float32)
                        / np.sqrt(math.prod(t.shape[1:]))
                    ).astype(t.dtype)
                )
                for name, t in self.tensors.items()
            }
        elif fill == "unread":
            tensors = {
                name: (
                    np.zeros((), t.dtype) if t.ndim == 0 else np.empty(t.shape, t.dtype)
                )
                for name, t in self.tensors.items()
            }
        else:
            raise ValueError(f"fill is read, random or unread, not {fill!r}")
        return _nest(tensors)


class Derived:
    """Weights a model computes once from its checkpoint, each put on the
    module it belongs to. Held as ``self.derived = derived.tree()``, a
    leaf's graph path is ``derived.<module>.<leaf>``.

    Args:
        weights: The checkpoint tree (``Checkpoint.tree()``).
    """

    def __init__(self, weights: SimpleNamespace) -> None:
        self._paths: dict[int, str] = {}
        pending: list[tuple[Any, str]] = [(weights, "")]
        while pending:
            node, path = pending.pop()
            if isinstance(node, SimpleNamespace):
                self._paths[id(node)] = path
                pending += [
                    (child, f"{path}.{key}" if path else key)
                    for key, child in vars(node).items()
                ]
            elif isinstance(node, list):
                pending += [(child, f"{path}.{i}") for i, child in enumerate(node)]
        self._tensors: dict[str, np.ndarray] = {}

    def put(self, module: SimpleNamespace, **tensors: np.ndarray) -> None:
        """Put ``tensors`` on ``module``, each under its keyword.

        Raises:
            ValueError: ``module`` is not in the tree, or a leaf is a
                checkpoint name or already put.
        """
        path = self._paths.get(id(module))
        if path is None:
            raise ValueError("Derived.put: the module is not in the checkpoint tree")
        for leaf, tensor in tensors.items():
            name = f"{path}.{leaf}" if path else leaf
            if leaf in vars(module) or name in self._tensors:
                raise ValueError(
                    f"Derived.put: {name} is a checkpoint name or derived already"
                )
            self._tensors[name] = tensor

    def tree(self) -> SimpleNamespace:
        """The derived weights, nested as the checkpoint tree is; a list's
        module that nothing was put on, as on a layer of a kind only some
        layers are, is an empty namespace.
        """
        return _nest(self._tensors, sparse=True)


def _nest(named: Mapping[str, Any], sparse: bool = False) -> SimpleNamespace:
    """Values by dotted name, nested as ``Checkpoint.tree()`` nests them."""
    nested: dict = {}
    for name, value in named.items():
        *parents, leaf = name.split(".")
        node = nested
        for key in parents:
            node = node.setdefault(key, {})
        node[leaf] = value
    return _tree(nested, sparse)


def _tree(node, sparse: bool) -> Any:
    """Nested dicts as namespaces, those keyed by indices as lists up to
    the largest; with ``sparse`` an index none holds is an empty namespace.

    Raises:
        ValueError: A run of indices skips one, not ``sparse``.
    """
    if not isinstance(node, dict):
        return node
    items = {key: _tree(child, sparse) for key, child in node.items()}
    if items and all(key.isdigit() for key in items):
        indices = range(max(map(int, items)) + 1)
        missing = sorted(set(indices) - {int(key) for key in items})
        if missing and not sparse:
            raise ValueError(f"indices {sorted(map(int, items))} skip {missing}")
        return [items.get(str(i), SimpleNamespace()) for i in indices]
    return SimpleNamespace(**items)


class Oracle:
    """A model's float32 forward pass on the host, the oracle it is judged
    by: a decoder's (``weights`` given) or EmbeddingGemma 2's own (built
    from its own weights tree by the subclass, ``weights`` left out).

    It is numpy, not composed from the operators' references, so it catches
    a wiring mistake the graph's own reference would repeat. A decoder's
    weights are widened to float32 as the pass reaches them, so beside the
    checkpoint it holds in float32 one layer's and the embedding, not all
    of them.

    Args:
        config: The model's shape; its ``eps`` is every RMS norm's.
        weights: A decoder's checkpoint tree (``Checkpoint.tree``). Left
            out, the subclass builds its own state from its own weights
            tree.
        decoder: The decoder's module of ``weights``, whose
            ``embed_tokens`` and ``layers`` are read here, the rest by the
            subclass; None is ``weights.model``.
    """

    def __init__(self, config: Config, weights=None, decoder=None):
        self.config = config
        self.buffers: dict[str, np.ndarray] = {}
        if weights is None:
            return
        self.weights = weights
        self.decoder = weights.model if decoder is None else decoder
        self.embedding = widen(self.decoder.embed_tokens.weight)
        self.layers = self.decoder.layers
        self.angles = config.angles()

    def layer(self, i: int, angles, w, x):
        """Layer ``i`` on ``x``, ``config.layer(i)``'s twin, attending causally."""
        attend = partial(self.attend, causal=True)
        return self.config.layer(i).oracle(self, w, x, attend, angles)

    def head(self, x):
        raise NotImplementedError(f"{type(self).__name__} defines no head()")

    def embed(self, x):
        return x

    def positions(self, x):
        """``x``, its rows at positions from 0, with the model's absolute
        positions placed; unchanged by default.
        """
        return x

    def logits(self, tokens) -> np.ndarray:
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        angles = None if self.angles is None else self.angles[: tokens.size]
        x = self.positions(self.embed(self.embedding[tokens]))
        for i, w in enumerate(self.layers):
            x = self.layer(i, angles, widen(w), x)
        return self.head(x[-1])

    def rms_norm(self, x, w=np.float32(1)):
        """`x` over the RMS of its last axis, times `w`, by `config.eps`."""
        eps = np.float32(self.config.eps)
        mean = np.mean(x * x, axis=-1, keepdims=True)
        return x * np.power(mean + eps, np.float32(-0.5)) * w

    def layer_norm(self, x, w, b):
        """`x` less its mean over the RMS of that, by `config.eps`, times `w`, plus `b`."""
        x = x - np.mean(x, axis=-1, keepdims=True)
        return self.rms_norm(x, w) + b

    def normed(self, x, n):
        """`x` normed by the norm module `n`: an affine LayerNorm where it holds
        a bias, else its RMS norm.
        """
        if "bias" in vars(n):
            return self.layer_norm(x, n.weight, n.bias)
        return self.rms_norm(x, n.weight)

    @staticmethod
    def linear(x, weight, bias=None):
        """``x @ weight.T``, plus ``bias`` if given."""
        y = x @ weight.T
        return y if bias is None else y + bias

    @staticmethod
    def silu(x):
        """SiLU, with the sigmoid as a tanh, which does not overflow."""
        half = x * np.float32(0.5)
        return (np.tanh(half) + 1) * half

    @staticmethod
    def gelu_tanh(x):
        c = np.float32(np.sqrt(2 / np.pi))
        return (
            np.float32(0.5) * x * (1 + np.tanh(c * (x + np.float32(0.044715) * x**3)))
        )

    @staticmethod
    def softplus(x):
        """``log(1 + exp(x))``, which does not overflow."""
        return np.logaddexp(np.float32(0), x)

    @staticmethod
    def causal_conv(x, weight, bias):
        """Each channel of ``x`` ``(n, channels)`` convolved over its rows by
        its own taps, ``weight`` ``(channels, taps)``, from zero rows before
        the first, plus ``bias`` if given.
        """
        n, taps = x.shape[0], weight.shape[1]
        padded = np.concatenate([np.zeros((taps - 1, x.shape[1]), np.float32), x])
        out = np.zeros_like(x, dtype=np.float32)
        if bias is not None:
            out += bias
        for k in range(taps):
            out += weight[:, k] * padded[k : k + n]
        return out

    @staticmethod
    def ssd(x, dt, A, B, C, block: int, state=None) -> tuple[np.ndarray, np.ndarray]:
        """Mamba-2's chunked scan, as Hugging Face's ``mamba2_chunk_scan``
        computes it: blocks of ``block`` positions, each a decay-masked
        product within it and its incoming state's share, the state carried
        block to block.

        Args:
            x: ``(n, heads, head_dim)``.
            dt: ``(n, heads)``, after its softplus.
            A: ``(heads,)``, negative.
            B: ``(n, groups, state)``.
            C: ``(n, groups, state)``.
            block: The positions a block holds.
            state: ``(heads, head_dim, state)`` before the first position;
                None is zero.

        Returns:
            ``y`` ``(n, heads, head_dim)``, without the skip ``D * x``, and
            the state after the last position.
        """
        n, H, P = x.shape
        B, C = (np.repeat(t, H // t.shape[1], axis=1) for t in (B, C))
        N = B.shape[-1]
        S = np.zeros((H, P, N), np.float32) if state is None else state
        y = np.empty((n, H, P), np.float32)
        later = np.tril(np.ones((block, block), bool), -1)[..., None]
        for start in range(0, n, block):
            s = slice(start, min(start + block, n))
            q = s.stop - start
            xd = x[s] * dt[s][..., None]
            a = A * dt[s]
            acs = np.cumsum(a, axis=0)
            # Each segment's sum from its own cumulative sum, as Hugging Face's
            # segment_sum: the decay from s to l, for s <= l.
            segments = np.cumsum(np.where(later[:q, :q], a[:, None], 0), axis=0)
            segments[~np.tril(np.ones((q, q), bool))] = -np.inf
            mask = np.exp(segments)
            G = np.einsum("lhn,shn->lsh", C[s], B[s])
            y[s] = np.einsum("lsh,shp->lhp", G * mask, xd)
            y[s] += np.einsum("lhn,hpn->lhp", C[s], S) * np.exp(acs)[..., None]
            decay = np.exp(acs[-1] - acs)
            S = S * np.exp(acs[-1])[:, None, None] + np.einsum(
                "lhn,lhp->hpn", B[s] * decay[..., None], xd
            )
        return y, S

    @staticmethod
    def rotate(x, angles):
        """`x` `(n, heads, D)` under RoPE, one table (`angles`, a row a
        position) or, a list of tables, `D` split evenly across them
        (Gemma's partial multi-band rotation), each part its own table.
        """
        if isinstance(angles, list):
            parts = np.split(x, len(angles), axis=-1)
            return np.concatenate(
                [Oracle.rotate(p, a) for p, a in zip(parts, angles)], axis=-1
            )
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

    def attend(
        self,
        q,
        k,
        v,
        *,
        causal: bool = False,
        window: int | None = None,
        scale: float | None = None,
    ):
        """Attention of `q` `(n, H, D)` over `k`, `v` `(n, G, D)`, each KV
        group's rows repeated to its heads, the logits scaled by `scale`
        (`1 / sqrt(D)` if None): bidirectional by default, with `window` a
        key at most that many positions away; `causal` masks a key past its
        query and reuses one buffer for the growing decode length.

        Raises:
            ValueError: both `causal` and `window` are given.
        """
        if causal and window is not None:
            raise ValueError("attend: causal and window do not combine")
        n, H, D = q.shape
        k, v = (np.repeat(a, H // a.shape[1], axis=1) for a in (k, v))
        if causal:
            # Batched matmuls, not einsum: BLAS is 10x faster at 3k.
            p = np.matmul(
                q.transpose(1, 0, 2),
                k.transpose(1, 2, 0),
                out=self.buffer("scores", (H, n, n)),
            )
            p *= np.float32(1 / np.sqrt(D) if scale is None else scale)
            p += np.triu(np.full((n, n), -np.inf, dtype=np.float32), k=1)
        else:
            p = q.transpose(1, 0, 2) @ k.transpose(1, 2, 0)
            p *= np.float32(1 / np.sqrt(D) if scale is None else scale)
            if window is not None:
                pos = np.arange(n)
                p[:, np.abs(pos[:, None] - pos[None, :]) > window] = -np.inf
        p -= p.max(axis=-1, keepdims=True)
        np.exp(p, out=p)
        p /= p.sum(axis=-1, keepdims=True)
        return (p @ v.transpose(1, 0, 2)).transpose(1, 0, 2).reshape(n, H * D)


def widen(value):
    """``value``, an array or a weight tree of namespaces and lists, in float32."""
    if isinstance(value, np.ndarray):
        return value.astype(np.float32)
    if isinstance(value, list):
        return [widen(v) for v in value]
    if isinstance(value, SimpleNamespace):
        return SimpleNamespace(**{k: widen(v) for k, v in vars(value).items()})
    return value


class Model(iron.Graph):
    """A model's graph, every version ``shapes()`` names compiled and
    loaded by ``load()`` before the first call, so the arena is made once:
    a version after the first feeds off the one before it, a full ELF's
    Emit starting there. ``versions`` (``Graph``'s own), in ``shapes()``'s
    order, is every version ``load()`` compiled.
    """

    def shapes(self) -> list[dict]:
        """The input shapes of each version."""
        raise NotImplementedError(f"{type(self).__name__} defines no shapes()")

    def load(
        self,
        *,
        release: Callable[[np.ndarray], None] | None = None,
        tuner: Tuner | None = None,
        full_elf: bool | None = None,
        dev=None,
    ) -> "Model":
        """Compile and load every version before the first call.

        Args:
            release: Given each piece of each weight once it is on the device.
            tuner: Folds, narrows and packs each version's designs by cost.
            full_elf: Each version's packaging (``Graph.compile``).
            dev: The device every version compiles for, else the current one.
        """
        if dev is None:
            dev = aie_utils.ensure_current_device()
        feeds = None
        for shapes in self.shapes():
            version = self.compile(
                dev=dev, feeds=feeds, tuner=tuner, full_elf=full_elf, **shapes
            )
            version.load(release=release)
            feeds = version if version.emit is not None else None
        return self


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


class Runner:
    """A checkpoint, its tokenizer and ``config``, and the models on them.

    A subclass names its ``config`` (a ``Config`` class read from the
    checkpoint's ``config.json``), ``model`` (the ``CausalLM``, whose
    ``oracle`` it is checked against), ``open_tokenizer`` and ``bos``, and
    any ``sizes`` ``--size`` picks among; ``tune_arguments``,
    ``tune_calls``, ``calibration_triangle`` and ``tables`` are what
    ``iron.lm.tune`` measures it by. Given a ``seed``, the weights are drawn
    in the checkpoint's shapes and a prompt with no tokenizer is random
    tokens, so speed, accuracy and determinism need neither.
    """

    config: Config | type[Config]
    sizes: dict[str, Config] = {}
    model: "type[CausalLM]"
    bos: int
    # The configure cost is measured between small single-column designs, at
    # their narrowest: one design's configure then costs least beside the
    # fixed part the calibration isolates.
    calibration_triangle: tuple[type, ...] = (ElementwiseAdd, SiLU, ElementwiseMul)
    tables: Path | None = None

    @staticmethod
    def open_tokenizer(path):
        raise NotImplementedError

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
        contexts attention over the cache is priced at, and the sampling
        Sample is measured at.
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
            help="the decode position the decode step's designs are measured at: "
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
            help="the longest context a design whose work follows it is priced "
            "at, a multiple of the prompt chunk (default: 8192)",
        )
        parser.add_argument(
            "--points",
            type=int,
            default=6,
            help="how many contexts up to --context it is priced at, each "
            "measured per setting: their cost grows with it (default: 6)",
        )
        parser.add_argument("--temperature", type=float, default=0.7)
        parser.add_argument("--top-k", type=int, default=50)

    @classmethod
    def tune_calls(
        cls, parser: argparse.ArgumentParser, args: argparse.Namespace
    ) -> list[Call]:
        """The calls the model's designs are measured in (``CausalLM.tune_calls``),
        on weights it never reads.
        """
        config = cls.default_config(args.checkpoint)
        if args.context > config.max_seq_len:
            parser.error(
                f"--context {args.context} is past max_seq_len {config.max_seq_len}"
            )
        model = cls.model(config, Checkpoint(args.checkpoint).tree("unread"))
        sample = Sampler(args.temperature, args.top_k, np.random.default_rng(SEED))
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
            None if tokenizer_path is None else self.open_tokenizer(tokenizer_path)
        )

    @classmethod
    def add_arguments(cls, parser: argparse.ArgumentParser) -> None:
        """The checkpoint and tokenizer, a model with several ``sizes``'
        ``--size``, and ``FLAGS``: the same flags ``main()``'s CLI and the
        pytest fixtures read a runner's options by (``from_options``).
        """
        parser.add_argument(
            "weights_path",
            help="the .safetensors checkpoint, or a sharded one's "
            "model.safetensors.index.json",
        )
        parser.add_argument("tokenizer_path", nargs="?", help="the tokenizer's file")
        if cls.sizes:
            parser.add_argument(
                "--size",
                choices=cls.sizes,
                default=next(n for n, c in cls.sizes.items() if c == cls.config),
                help="the model's size (default: %(default)s)",
            )
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
        config.json gives the shape, narrowed by ``--size`` or
        ``--max-seq-len``, and ``from_arguments`` builds the runner.

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
        config = (
            cls.sizes[args.size] if cls.sizes else cls.default_config(args.weights_path)
        )
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

    def npu(
        self,
        cost_table: Path | None = None,
        full_elf: bool | None = None,
        kinds: NarrowingKinds | None = None,
    ) -> "CausalLM":
        """The model compiled and loaded, weights uploaded. With a
        ``cost_table`` (``tune``) each version's designs are folded,
        narrowed and packed by it, restricted to ``kinds`` if given;
        ``full_elf`` is both versions' packaging (``CausalLM.load``).
        """
        model = self.model(self.config, self.weights)
        tuner = (
            None
            if cost_table is None
            else JointNarrowing(CostTable(cost_table), kinds=kinds or NarrowingKinds())
        )
        return model.load(
            release=self.checkpoint.release, tuner=tuner, full_elf=full_elf
        )

    def oracle(self) -> Oracle:
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
        return self.encode(prompt_text(chars, skip))


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
    model = run.npu(args.cost_table, args.full_elf)
    for name, tuning in model.tunings.items():
        print(f"[Tuning] {name}:\n" + tuning.report(), flush=True)

    if args.check_accuracy:
        results = accuracy(model, run.oracle(), tokens, args.num_tokens)
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
            host, _, _ = generate_on_host(
                model, tokens, args.num_tokens, sampler(), show
            )
            print(run.decode(pending), end="")
            differ = sum(a != b for a, b in zip(drawn, host))
            print(
                f"\n[Device] Tokens differing from the host loop: {differ}/{len(host)}"
            )
