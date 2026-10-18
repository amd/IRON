# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A model's shape: ``Config``, read from a checkpoint's own
``config.json``, and a decoder's, ``DecoderConfig``, with its RoPE table
(``rope_angles``).
"""

import dataclasses
import json
from collections.abc import Callable
from pathlib import Path

import numpy as np

from .blocks import Attention, DecoderLayer, MLP, Norm

RopeScaling = Callable[[np.ndarray], np.ndarray]


def rope_angles(
    head_dim: int,
    context_length: int,
    rope_theta: float = 500000.0,
    scaling: RopeScaling | None = None,
) -> np.ndarray:
    """The RoPE table, ``(context_length, head_dim)`` float32, cos and sin interleaved.

    Each transcendental is evaluated in float64 and rounded once.
    """
    exponents = np.arange(0, head_dim, 2, dtype=np.float32) / np.float32(head_dim)
    inv_freq = 1.0 / np.power(rope_theta, exponents.astype(np.float64))
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
            ValueError: The file lacks a field that has no default.
        """
        path = Path(path)
        if path.name != "config.json":
            path = (path if path.is_dir() else path.parent) / "config.json"
        data = json.loads(path.read_text())
        kwargs, missing = {}, []
        for f in dataclasses.fields(cls):
            key = f.metadata.get("json")
            if key is None:
                continue
            value = _dotted(data, key)
            # Hugging Face writes an unset option as null.
            if value is _MISSING or value is None:
                required = dataclasses.MISSING
                if f.default is required and f.default_factory is required:
                    missing.append(key)
                continue
            convert = f.metadata.get("convert")
            kwargs[f.name] = convert(value) if convert else value
        if missing:
            raise ValueError(f"{path} lacks {missing}")
        return cls(**kwargs)

    def to_json(self) -> dict:
        """The fields as ``config.json`` names them, ``from_checkpoint``'s
        inverse: a value its ``convert`` built gives its own ``to_json()``.
        A field that is None or not JSON is left out.
        """
        out = {}
        for f in dataclasses.fields(self):
            key, value = f.metadata.get("json"), getattr(self, f.name)
            if hasattr(value, "to_json"):
                value = value.to_json()
            if key is None or not isinstance(
                value, (bool, int, float, str, tuple, dict)
            ):
                continue
            *path, leaf = key.split(".")
            node = out
            for part in path:
                node = node.setdefault(part, {})
            node[leaf] = list(value) if isinstance(value, tuple) else value
        return out

    def norm(self) -> Norm:
        """Every norm's kind: RMS at ``eps``."""
        return Norm(self.eps)

    def layer(self, i: int) -> DecoderLayer:
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
    hidden_size: int = dataclasses.field(metadata={"json": "hidden_size"})
    num_hidden_layers: int = dataclasses.field(metadata={"json": "num_hidden_layers"})
    num_attention_heads: int = dataclasses.field(
        metadata={"json": "num_attention_heads"}
    )
    num_key_value_heads: int = dataclasses.field(
        metadata={"json": "num_key_value_heads"}
    )
    # None where the checkpoint's own config.json has no head_dim (Qwen 2.5,
    # Granite, LFM2, Phi-4-mini-instruct): __post_init__ derives it.
    head_dim: int | None = dataclasses.field(
        default=None, kw_only=True, metadata={"json": "head_dim"}
    )
    intermediate_size: int = dataclasses.field(metadata={"json": "intermediate_size"})
    # None turns nothing: a decoder of absolute positions (``positions``).
    rope_theta: float | None = dataclasses.field(metadata={"json": "rope_theta"})
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
    # Whether the output head is the input embedding.
    tie_word_embeddings: bool = dataclasses.field(
        default=True, metadata={"json": "tie_word_embeddings"}
    )

    def __post_init__(self):
        if self.head_dim is None:
            object.__setattr__(
                self, "head_dim", self.hidden_size // self.num_attention_heads
            )

    @property
    def rope_width(self) -> int:
        """The angle table's own width: ``head_dim``, or ``rotary_dim`` under
        partial rotary.
        """
        return self.rotary_dim or self.head_dim

    def long_angles(self) -> tuple[int, np.ndarray] | None:
        """The position a prompt's sequence must pass to take a second RoPE
        table, and that table (LongRoPE's long one); None by default.
        """
        return None

    def angles(self) -> np.ndarray | None:
        """The RoPE table, a row per position; None with no ``rope_theta``."""
        if self.rope_theta is None:
            return None
        angles = rope_angles(
            self.rope_width, self.max_seq_len, self.rope_theta, self.rope_scaling
        )
        if self.rope_attention_scaling != 1.0:
            angles = angles * np.float32(self.rope_attention_scaling)
        return angles

    def attention(self, i: int) -> Attention:
        """Layer ``i``'s attention: Llama's."""
        return Attention(
            self.num_attention_heads,
            self.num_key_value_heads,
            self.head_dim,
            self.eps,
            rotary=self.rotary_dim,
        )

    def layer(self, i: int) -> DecoderLayer:
        """Layer ``i``: Llama's, ``attention(i)`` and a gated feed-forward,
        each after its RMS norm.
        """
        return DecoderLayer(self.attention(i), MLP(self.hidden_act), self.norm())
