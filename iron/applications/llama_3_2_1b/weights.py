# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2's weights in numpy, mapped from the safetensors checkpoint.

:class:`LlamaWeights` is the checkpoint as the model's tree, under the names
the graphs' weight buffers carry. Every matrix is ``(out, in)``, exactly as
the checkpoint ships it and as :mod:`.npu` reads it: decode's GEMV takes
it as ``(M, K)`` and prefill's GEMM as a column-major B (``b_col_maj=True``).
Nothing here transposes, casts or copies.

"""

from __future__ import annotations

import mmap
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

import ml_dtypes
import numpy as np
from safetensors import safe_open

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


class SafetensorsFile:
    """A ``.safetensors`` file, its tensors read-only views of one mapping.

    The safetensors library reads the header and holds the file to its
    format: each tensor's bytes agree with its dtype and shape, and the
    tensors tile the data section, in offset order, with no gap and nothing
    after. What it does not do is hand out a view: ``get_tensor`` copies,
    and a copied checkpoint is 2.5 GB resident beside the device's own copy.
    So the bytes are read from a mapping of the file, at the offsets that
    tiling implies. Nothing is read until touched, and :meth:`release` drops
    a weight's pages once it is on the device.
    """

    def __init__(self, path: str | Path):
        self.path = Path(path)
        with safe_open(self.path, framework="numpy") as f:
            self.metadata: dict[str, str] = f.metadata() or {}
            specs = [
                (name, f.get_slice(name).get_dtype(), f.get_slice(name).get_shape())
                for name in f.offset_keys()
            ]
        for name, dtype, _ in specs:
            if dtype not in _DTYPES:
                raise ValueError(f"{self.path}: {name} has unsupported dtype {dtype}")
        with open(self.path, "rb") as file:
            # The mapping holds its own reference to the file; closing ours
            # does not unmap it.
            self._map = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        # Where the mapping starts in memory, to tell a view's place in it.
        self._address = np.frombuffer(self._map, dtype=np.uint8).ctypes.data
        self._tensors: dict[str, tuple[np.dtype, tuple[int, ...], int]] = {}
        sizes = [
            int(np.prod(shape, dtype=np.int64)) * _DTYPES[dtype].itemsize
            for _, dtype, shape in specs
        ]
        offset = len(self._map) - sum(sizes)
        for (name, dtype, shape), size in zip(specs, sizes):
            self._tensors[name] = (_DTYPES[dtype], tuple(shape), offset)
            offset += size

    def keys(self) -> list[str]:
        """The tensor names, in the order of their bytes."""
        return list(self._tensors)

    def __contains__(self, name: str) -> bool:
        return name in self._tensors

    def __getitem__(self, name: str) -> np.ndarray:
        """``name`` as a read-only view of the mapped file; no bytes are copied."""
        dtype, shape, offset = self._tensors[name]
        count = int(np.prod(shape, dtype=np.int64))
        flat = np.frombuffer(self._map, dtype=dtype, count=count, offset=offset)
        return flat.reshape(shape)

    def holds(self, array: np.ndarray) -> bool:
        """Whether ``array``'s bytes lie in this mapping."""
        begin = array.ctypes.data - self._address
        return 0 <= begin and begin + array.nbytes <= len(self._map)

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

    Field ``f`` is named ``layers.{i}.<_LAYER_NAMES[f][1]>`` in the graphs:
    ``norm1`` is ``layers.{i}.norm1.weight``, ``q`` is
    ``layers.{i}.attn.q.weight`` and ``gate`` is ``layers.{i}.ffn.gate.weight``.
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


# LayerWeights field -> (checkpoint suffix, graph name suffix), per layer.
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
_LAYER_KEY = re.compile(r"model\.layers\.(\d+)\.")


@dataclass(frozen=True)
class LlamaWeights:
    """Every weight Llama 3.2 has, as views of the checkpoint.

    Llama 3.2 ties the output head to the token embedding: ``out_head`` is
    ``embedding``, the same array, so it is one buffer on the device and one
    name, ``out_head.weight``.

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
    def dims(self) -> dict[str, int]:
        """What every shape is made of, read off the embedding and layer 0.

        ``q`` is ``n_heads * head_dim`` and ``kv`` ``n_kv_groups * head_dim``.
        """
        first = self.layers[0]
        return {
            "n_layers": len(self.layers),
            "vocab": self.embedding.shape[0],
            "emb": self.embedding.shape[1],
            "q": first.q.shape[0],
            "kv": first.k.shape[0],
            "hidden": first.gate.shape[0],
        }

    @classmethod
    def load(cls, path: str | Path) -> LlamaWeights:
        """Map a Hugging Face Llama checkpoint; nothing is read until touched.

        Strict both ways: a missing key and a key this tree has no place for
        (an untied ``lm_head.weight``, say) both raise, and every array must
        have the shape :attr:`dims` says.
        """
        return cls.from_file(SafetensorsFile(path))

    @classmethod
    def from_file(cls, file: SafetensorsFile) -> LlamaWeights:
        # As many layers as the highest-numbered key says, at least one;
        # every one of them whole.
        numbers = [int(m[1]) for k in file.keys() if (m := _LAYER_KEY.match(k))]
        layer_keys = [
            {f: f"model.layers.{i}.{hf}" for f, (hf, _) in _LAYER_NAMES.items()}
            for i in range(max(numbers, default=0) + 1)
        ]
        expected = [_EMBEDDING, _NORM, *(k for ks in layer_keys for k in ks.values())]
        missing = [k for k in expected if k not in file]
        unknown = sorted(set(file.keys()) - set(expected))
        if missing or unknown:
            raise ValueError(
                f"{file.path}: missing {missing}; no place in the tree for {unknown}"
            )
        weights = cls(
            embedding=file[_EMBEDDING],
            norm=file[_NORM],
            layers=tuple(
                LayerWeights(**{f: file[k] for f, k in ks.items()}) for ks in layer_keys
            ),
            file=file,
        )
        weights._check_shapes()
        return weights

    def _check_shapes(self) -> None:
        d = self.dims
        E, Q, KV, F = d["emb"], d["q"], d["kv"], d["hidden"]
        expected = {
            "norm1": (E,),
            "q": (Q, E),
            "k": (KV, E),
            "v": (KV, E),
            "o": (E, Q),
            "norm2": (E,),
            "gate": (F, E),
            "up": (F, E),
            "down": (E, F),
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
        """``(name, array)`` under the graphs' names; what ``iron.graph(names_from=...)`` reads."""
        for i, layer in enumerate(self.layers):
            for name, array in layer.arrays().items():
                yield f"layers.{i}.{_LAYER_NAMES[name][1]}", array
        yield "norm.weight", self.norm
        yield "out_head.weight", self.out_head

    def embed(self, token_ids) -> np.ndarray:
        """Token embeddings, ``(*token_ids.shape, emb_dim)``: rows of the table, copied."""
        return self.embedding[np.asarray(token_ids, dtype=np.int64)]
