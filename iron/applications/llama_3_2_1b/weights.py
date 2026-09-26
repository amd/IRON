# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2's parameters and RoPE table as numpy, with no torch in the path.

:class:`SafetensorsFile` maps a checkpoint read-only and hands out each
tensor as a zero-copy view of the mapping, so nothing is read from disk
until a byte is touched -- uploading a weight into a device buffer is the
one copy it ever gets. :class:`LlamaWeights` arranges those views into the
model's tree under the names :mod:`.model` gives them, which are the names
the graphs' weight buffers carry.

Every matrix is ``(out, in)``, exactly as the checkpoint ships it and as
:mod:`.graphs` reads it today: decode's GEMV takes it as ``(M, K)`` and
prefill's GEMM as a column-major B (``b_col_maj=True``). Nothing here
transposes, casts or copies.
"""

from __future__ import annotations

import json
import mmap
import re
import struct
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

import ml_dtypes
import numpy as np

# Safetensors dtype names -> numpy dtypes.
_DTYPES: dict[str, np.dtype] = {
    "BOOL": np.dtype(np.bool_),
    "U8": np.dtype(np.uint8),
    "I8": np.dtype(np.int8),
    "U16": np.dtype(np.uint16),
    "I16": np.dtype(np.int16),
    "U32": np.dtype(np.uint32),
    "I32": np.dtype(np.int32),
    "U64": np.dtype(np.uint64),
    "I64": np.dtype(np.int64),
    "F16": np.dtype(np.float16),
    "BF16": np.dtype(ml_dtypes.bfloat16),
    "F32": np.dtype(np.float32),
    "F64": np.dtype(np.float64),
    "F8_E4M3": np.dtype(ml_dtypes.float8_e4m3fn),
    "F8_E5M2": np.dtype(ml_dtypes.float8_e5m2),
}


@dataclass(frozen=True)
class TensorInfo:
    """Where one tensor lives in the file's data section."""

    dtype: np.dtype
    shape: tuple[int, ...]
    begin: int  # byte offsets, relative to the start of the data section
    end: int


class SafetensorsFile:
    """A ``.safetensors`` file, mapped read-only.

    The format is an 8-byte little-endian header length, a JSON header naming
    each tensor's dtype, shape and byte range, and the data. ``self[name]``
    is a read-only view of the mapping; the mapping stays alive for as long
    as any view does.
    """

    def __init__(self, path: str | Path):
        self.path = Path(path)
        with open(self.path, "rb") as f:
            (header_len,) = struct.unpack("<Q", f.read(8))
            header = json.loads(f.read(header_len))
            # The mapping holds its own reference to the file; closing ours
            # does not unmap it.
            self._map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # Where the mapping starts in memory, to tell a view's place in it.
        self._address = np.frombuffer(self._map, dtype=np.uint8).ctypes.data
        self._data_start = 8 + header_len
        self.metadata: dict[str, str] = header.pop("__metadata__", None) or {}
        data_len = len(self._map) - self._data_start
        self._tensors: dict[str, TensorInfo] = {}
        for name, entry in header.items():
            if entry["dtype"] not in _DTYPES:
                raise ValueError(
                    f"{self.path}: {name} has unsupported dtype {entry['dtype']}"
                )
            info = TensorInfo(
                dtype=_DTYPES[entry["dtype"]],
                shape=tuple(entry["shape"]),
                begin=entry["data_offsets"][0],
                end=entry["data_offsets"][1],
            )
            nbytes = int(np.prod(info.shape, dtype=np.int64)) * info.dtype.itemsize
            if (
                info.end - info.begin != nbytes
                or not 0 <= info.begin <= info.end <= data_len
            ):
                raise ValueError(
                    f"{self.path}: {name} claims bytes [{info.begin}, {info.end}) "
                    f"for {nbytes} bytes of {entry['dtype']}{list(info.shape)}, in a "
                    f"{data_len}-byte data section"
                )
            self._tensors[name] = info

    def keys(self) -> list[str]:
        """The tensor names, in header order."""
        return list(self._tensors)

    def info(self, name: str) -> TensorInfo:
        return self._tensors[name]

    def __contains__(self, name: str) -> bool:
        return name in self._tensors

    def __len__(self) -> int:
        return len(self._tensors)

    def __getitem__(self, name: str) -> np.ndarray:
        """``name`` as a read-only view of the mapped file; no bytes are copied."""
        info = self._tensors[name]
        count = (info.end - info.begin) // info.dtype.itemsize
        flat = np.frombuffer(
            self._map,
            dtype=info.dtype,
            count=count,
            offset=self._data_start + info.begin,
        )
        return flat.reshape(info.shape)

    def holds(self, array: np.ndarray) -> bool:
        """Whether ``array``'s bytes lie in this mapping's data section."""
        begin = array.ctypes.data - self._address
        return self._data_start <= begin and begin + array.nbytes <= len(self._map)

    def release(self, view: np.ndarray) -> None:
        """Drop this process's pages of ``view``, a view of this mapping.

        Nothing is lost: the mapping is of the file, read-only, so a later
        read faults the bytes back in, from the page cache or the disk. What
        it saves is resident memory -- a weight read once, to upload it,
        need not stay counted against the process. Pages the view shares
        with its neighbours are dropped too, as harmlessly.
        """
        if not (view.flags.c_contiguous and self.holds(view)):
            raise ValueError(f"not a contiguous view of {self.path}")
        begin = view.ctypes.data - self._address
        start = begin - begin % mmap.PAGESIZE
        self._map.madvise(mmap.MADV_DONTNEED, start, begin + view.nbytes - start)


# The model tree
# ##########################################################################


@dataclass(frozen=True)
class LayerWeights:
    """One transformer block's parameters; every matrix ``(out, in)``.

    Field ``f`` is :mod:`.model`'s ``layers.{i}.<_TREE_NAMES[f]>``, i.e.
    ``blk.norm1.weight`` is ``norm1``, ``blk.attn.q.weight`` is ``q`` and
    ``blk.ffn.gate.weight`` is ``gate``.
    """

    norm1: np.ndarray  # (emb_dim,)
    q: np.ndarray  # (n_heads * head_dim, emb_dim)
    k: np.ndarray  # (n_kv_groups * head_dim, emb_dim)
    v: np.ndarray  # (n_kv_groups * head_dim, emb_dim)
    o: np.ndarray  # (emb_dim, n_heads * head_dim)
    norm2: np.ndarray  # (emb_dim,)
    gate: np.ndarray  # (hidden_dim, emb_dim)
    up: np.ndarray  # (hidden_dim, emb_dim)
    down: np.ndarray  # (emb_dim, hidden_dim)

    def arrays(self) -> dict[str, np.ndarray]:
        """Field name -> array, in declaration order."""
        return {
            "norm1": self.norm1,
            "q": self.q,
            "k": self.k,
            "v": self.v,
            "o": self.o,
            "norm2": self.norm2,
            "gate": self.gate,
            "up": self.up,
            "down": self.down,
        }


# LayerWeights field -> (checkpoint suffix, :mod:`.model` suffix), per layer.
_LAYER_NAMES: dict[str, tuple[str, str]] = {
    "norm1": ("input_layernorm.weight", "norm1.weight"),
    "q": ("self_attn.q_proj.weight", "attn.q.weight"),
    "k": ("self_attn.k_proj.weight", "attn.k.weight"),
    "v": ("self_attn.v_proj.weight", "attn.v.weight"),
    "o": ("self_attn.o_proj.weight", "attn.o.weight"),
    "norm2": ("post_attention_layernorm.weight", "norm2.weight"),
    "gate": ("mlp.gate_proj.weight", "ffn.gate.weight"),
    "up": ("mlp.up_proj.weight", "ffn.up.weight"),
    "down": ("mlp.down_proj.weight", "ffn.down.weight"),
}
_EMBEDDING = "model.embed_tokens.weight"
_NORM = "model.norm.weight"
_LAYER_KEY = re.compile(r"model\.layers\.(\d+)\.(.+)")


@dataclass(frozen=True)
class LlamaWeights:
    """Every weight Llama 3.2 has, as views of the checkpoint.

    Llama 3.2 ties the output head to the token embedding: ``out_head`` is
    ``embedding``, the same array, so it is one buffer on the device and one
    name, ``out_head.weight``, as :mod:`.model` calls it.

    Each array is created once and kept: the graph tracer names and pins a
    weight by the identity of the array a graph closed over, so a field must
    return the same object on every read (a frozen dataclass does).
    """

    embedding: np.ndarray  # (vocab_size, emb_dim)
    norm: np.ndarray  # (emb_dim,)
    layers: tuple[LayerWeights, ...]
    # The mapped checkpoint the arrays view, if they came from one.
    file: SafetensorsFile | None = field(default=None, repr=False, compare=False)

    def release(self, array: np.ndarray) -> None:
        """Drop the host pages of ``array`` if it is a view of the mapped
        checkpoint; anything else is left alone. It stays readable.
        """
        if self.file is not None and self.file.holds(array):
            self.file.release(array)

    @property
    def out_head(self) -> np.ndarray:
        """The output projection, ``(vocab_size, emb_dim)``: the embedding, tied."""
        return self.embedding

    @property
    def emb_dim(self) -> int:
        return self.embedding.shape[1]

    @property
    def vocab_size(self) -> int:
        return self.embedding.shape[0]

    @classmethod
    def load(cls, path: str | Path) -> LlamaWeights:
        """Map a Hugging Face Llama checkpoint; nothing is read until touched.

        Strict both ways: a missing key and a key this tree has no place for
        (an untied ``lm_head.weight``, say) both raise, and every layer must
        have the first layer's shapes, over the embedding's width.
        """
        return cls.from_file(SafetensorsFile(path))

    @classmethod
    def from_file(cls, file: SafetensorsFile) -> LlamaWeights:
        by_layer: dict[int, dict[str, np.ndarray]] = {}
        suffixes = {hf: field for field, (hf, _) in _LAYER_NAMES.items()}
        unknown = []
        for key in file.keys():
            match = _LAYER_KEY.fullmatch(key)
            if key in (_EMBEDDING, _NORM):
                continue
            if match is None or match.group(2) not in suffixes:
                unknown.append(key)
                continue
            by_layer.setdefault(int(match.group(1)), {})[suffixes[match.group(2)]] = (
                file[key]
            )
        if unknown:
            raise ValueError(
                f"{file.path}: keys with no place in the tree: {sorted(unknown)}"
            )
        missing = [k for k in (_EMBEDDING, _NORM) if k not in file]
        if not by_layer:
            missing.append("every layer")
        elif sorted(by_layer) != list(range(len(by_layer))):
            gaps = sorted(set(range(max(by_layer) + 1)) - set(by_layer))
            missing.append(f"layers {gaps}")
        for i, found in sorted(by_layer.items()):
            missing += [
                f"model.layers.{i}.{_LAYER_NAMES[f][0]}"
                for f in _LAYER_NAMES
                if f not in found
            ]
        if missing:
            raise ValueError(f"{file.path}: missing {missing}")

        weights = cls(
            embedding=file[_EMBEDDING],
            norm=file[_NORM],
            layers=tuple(LayerWeights(**by_layer[i]) for i in range(len(by_layer))),
            file=file,
        )
        weights._check_shapes()
        return weights

    def _check_shapes(self) -> None:
        E = self.emb_dim
        first = self.layers[0]
        expected = {
            "norm1": (E,),
            "norm2": (E,),
            "q": (first.q.shape[0], E),
            "k": (first.k.shape[0], E),
            "v": first.k.shape,
            "o": (E, first.q.shape[0]),
            "gate": (first.gate.shape[0], E),
            "up": first.gate.shape,
            "down": (E, first.gate.shape[0]),
        }
        if self.norm.shape != (E,):
            raise ValueError(f"norm is {self.norm.shape}, not ({E},)")
        for i, layer in enumerate(self.layers):
            for name, array in layer.arrays().items():
                if array.shape != expected[name]:
                    raise ValueError(
                        f"layer {i} {name} is {array.shape}, expected {expected[name]}"
                    )

    def named_parameters(self) -> Iterator[tuple[str, np.ndarray]]:
        """``(name, array)`` under :mod:`.model`'s names; what ``iron.graph(names_from=...)`` reads."""
        for i, layer in enumerate(self.layers):
            for name, array in layer.arrays().items():
                yield f"layers.{i}.{_LAYER_NAMES[name][1]}", array
        yield "norm.weight", self.norm
        yield "out_head.weight", self.out_head

    def embed(self, token_ids) -> np.ndarray:
        """Token embeddings, ``(*token_ids.shape, emb_dim)``: rows of the table, copied."""
        return self.embedding[np.asarray(token_ids, dtype=np.int64)]


# RoPE
# ##########################################################################


@dataclass(frozen=True)
class Llama3RopeScaling:
    """Llama 3's RoPE frequency scaling (``"rope_type": "llama3"``).

    How Llama 3.1 and later stretch a model trained at
    ``original_max_position_embeddings`` to a longer context, by frequency:
    one whose wavelength is under ``original / high_freq_factor`` positions
    is kept, one over ``original / low_freq_factor`` is divided by
    ``factor``, and one between is interpolated between the two by where its
    wavelength falls. The fields are the checkpoint's ``rope_scaling``.
    """

    factor: float
    low_freq_factor: float
    high_freq_factor: float
    original_max_position_embeddings: int

    def __call__(self, inv_freq: np.ndarray) -> np.ndarray:
        """``inv_freq`` (radians per position, per frequency), scaled."""
        original = self.original_max_position_embeddings
        wavelen = 2 * np.pi / inv_freq
        smooth = (original / wavelen - self.low_freq_factor) / (
            self.high_freq_factor - self.low_freq_factor
        )
        between = (1 - smooth) * inv_freq / self.factor + smooth * inv_freq
        return np.where(
            wavelen < original / self.high_freq_factor,
            inv_freq,
            np.where(
                wavelen > original / self.low_freq_factor,
                inv_freq / self.factor,
                between,
            ),
        )


def rope_angles(
    head_dim: int,
    context_length: int,
    rope_base: float = 500000.0,
    scaling: Llama3RopeScaling | None = None,
) -> np.ndarray:
    """The RoPE table, ``(context_length, head_dim)`` float32: cos and sin
    interleaved per frequency, as the device kernel reads it.

    ``scaling``, if given, is applied to the frequencies in float64, before
    their one rounding to float32.

    The formula is :func:`.model.rope_angles`' in float32 -- ``inv_freq`` and
    each ``position * inv_freq`` are rounded to float32 at the same points --
    but each transcendental is evaluated in float64 and rounded once, so
    every entry is the correctly rounded float32 of that formula. torch
    evaluates ``pow``, ``cos`` and ``sin`` through its own vectorised
    routines, which are not correctly rounded, so the two tables are not
    bitwise equal. This one is the nearer to exact; in the first 2048 rows,
    0.28% of entries round to a different bf16, by at most 2**-8.
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
