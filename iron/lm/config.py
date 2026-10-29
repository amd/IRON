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
from typing import Any

import numpy as np

from iron.common.declare.precision import Precision

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


def unscaled(rope_scaling: dict) -> None:
    """A checkpoint's ``rope_scaling`` that leaves RoPE as it is: None.

    Raises:
        ValueError: It scales RoPE, which this config builds no table for.
    """
    kind = rope_scaling.get("rope_type", rope_scaling.get("type"))
    if kind != "default":
        raise ValueError(f"rope_scaling {rope_scaling}: no RoPE table here builds it")


def not_json(default, **kwargs) -> Any:
    """A field ``config.json`` does not set, an IRON choice: kept at
    ``default`` by ``from_checkpoint`` and left out by ``to_json``.
    """
    return dataclasses.field(default=default, metadata={"json": None}, **kwargs)


@dataclasses.dataclass(frozen=True)
class Config:
    """A model's shape, built from a checkpoint's ``config.json``
    (``from_checkpoint``); ``precision`` is every projection's, chosen per
    application on its measured accuracy, with no default here.
    """

    # Unbiased projections, RoPE over whole heads, unless a model says.
    attention_bias = mlp_bias = False
    rotary_dim = None
    # The object of config.json the fields are read from ("text_config."
    # for a model nested there); a ``metadata["json"]`` path after "/" is
    # from the file's root.
    json_prefix = ""

    eps: float = dataclasses.field(
        default=1e-6, kw_only=True, metadata={"json": "rms_norm_eps"}
    )
    precision: Precision = dataclasses.field(kw_only=True, metadata={"json": None})

    @classmethod
    def from_checkpoint(cls, path) -> "Config":
        """``cls``'s fields read from ``path``'s own ``config.json``, each
        at its ``metadata["json"]`` path (under ``json_prefix``), converted
        by ``metadata["convert"]`` if it names one.

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
        return cls.from_json(json.loads(path.read_text()), path)

    @classmethod
    def from_json(cls, data: dict, source: str | Path = "config.json") -> "Config":
        """``from_checkpoint`` on ``data``, a ``config.json`` already
        parsed; ``source`` names it in an error.

        Raises:
            ValueError: ``data`` lacks a field that has no default, or
                ``cls`` states no default for a field ``config.json`` does
                not set (an application's choice, as ``precision``).
        """
        kwargs, missing = {}, []
        for f in dataclasses.fields(cls):
            key = cls.json_key(f)
            if key is None:
                required = dataclasses.MISSING
                if f.default is required and f.default_factory is required:
                    raise ValueError(f"{cls.__name__} states no {f.name}")
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
            raise ValueError(f"{source} lacks {missing}")
        return cls(**kwargs)

    @classmethod
    def json_key(cls, f: dataclasses.Field) -> str | None:
        """Where ``config.json`` holds field ``f``; None: nowhere."""
        key = f.metadata.get("json", f.name)
        if key is None or key.startswith("/"):
            return None if key is None else key[1:]
        return cls.json_prefix + key

    def to_json(self) -> dict:
        """The fields as ``config.json`` names them, ``from_checkpoint``'s
        inverse: a nested ``Config`` gives its own ``to_json()``, another
        dataclass its fields. A ``not_json`` field, or one that is None or
        not JSON, is left out.
        """
        out = {}
        for f in dataclasses.fields(self):
            key = self.json_key(f)
            value = getattr(self, f.name)
            if isinstance(value, Config):
                value = value.to_json()
            elif dataclasses.is_dataclass(value) and not isinstance(value, type):
                value = dataclasses.asdict(value)
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


@dataclasses.dataclass(frozen=True)
class DecoderConfig(Config):
    """A decoder's shape, named as a Hugging Face checkpoint's own
    ``config.json`` does where it has one; ``max_seq_len`` is the
    checkpoint's native context unless a caller lowers it.
    """

    vocab_size: int
    hidden_size: int
    num_hidden_layers: int
    num_attention_heads: int
    num_key_value_heads: int
    # None where the checkpoint's config.json has no head_dim: __post_init__
    # derives it.
    head_dim: int | None = dataclasses.field(default=None, kw_only=True)
    intermediate_size: int
    # None: no RoPE, a decoder of absolute positions (``positions``).
    rope_theta: float | None
    max_seq_len: int = dataclasses.field(metadata={"json": "max_position_embeddings"})
    rope_scaling: RopeScaling | None = dataclasses.field(
        default=None, metadata={"convert": unscaled}
    )
    # The rotated prefix of head_dim (partial rotary, e.g. Phi's 0.75): None
    # rotates the whole head, as every full-rotary model does.
    rotary_dim: int | None = not_json(None)
    # A post-trig scalar the whole angle table is multiplied by once at
    # build time (LongRoPE/YaRN's "mscale"): 1.0 leaves cos/sin as rotations.
    rope_attention_scaling: float = not_json(1.0)
    prefill_chunk: int = not_json(2048)
    hidden_act: str = "silu"
    # Whether the output head is the input embedding.
    tie_word_embeddings: bool = True
    # Whether attention's projections (o where its layer says) and every
    # feed-forward projection add a bias.
    attention_bias: bool = dataclasses.field(default=False, kw_only=True)
    mlp_bias: bool = dataclasses.field(default=False, kw_only=True)
    # The positions each layer attends to, its own included, where under
    # max_seq_len. A checkpoint gating it by use_sliding_window (Qwen's,
    # SmolLM3's) picks its layers per model, so there it must be false.
    sliding_window: int | None = dataclasses.field(default=None, kw_only=True)
    use_sliding_window: bool | None = dataclasses.field(default=None, kw_only=True)

    def __post_init__(self):
        if self.head_dim is None:
            object.__setattr__(
                self, "head_dim", self.hidden_size // self.num_attention_heads
            )
        if self.prefill_chunk > self.max_seq_len:
            object.__setattr__(self, "prefill_chunk", self.max_seq_len)
        if self.use_sliding_window and self.window is not None:
            raise ValueError(
                f"{type(self).__name__}: use_sliding_window with sliding_window "
                f"{self.sliding_window} windows only some layers; none here does"
            )

    @property
    def window(self) -> int | None:
        """The positions before a query each layer attends to (``KVCache``'s
        ``window``), ``sliding_window`` less the query's own; None is all.
        """
        if self.use_sliding_window is False or self.sliding_window is None:
            return None
        if self.sliding_window >= self.max_seq_len:
            return None
        return self.sliding_window - 1

    @property
    def rope_width(self) -> int:
        """The angle table's own width: ``head_dim``, or ``rotary_dim`` under
        partial rotary.
        """
        assert self.head_dim is not None, "__post_init__ sets it"
        return self.rotary_dim or self.head_dim

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
