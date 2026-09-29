# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A model's weights: the checkpoint file, and the tree a model reads.

``Checkpoint`` maps a ``.safetensors`` file. ``load_weights``
places its tensors in a tree by a model's *layout*: each weight's path in
the tree, its name in the checkpoint and its shape, ``{i}`` standing for a
layer's index in both:

```python
{
    "embedding": ("model.embed_tokens.weight", (V, E)),
    "layers.{i}.q": ("model.layers.{i}.self_attn.q_proj.weight", (Q, E)),
    ...
}
```

makes ``weights.embedding`` and ``weights.layers[3].q``.
"""

import json
import mmap
import struct
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import numpy as np
from ml_dtypes import bfloat16

#: Each weight's path in the tree -> its checkpoint name and shape.
Layout = dict[str, tuple[str, tuple[int, ...]]]


class Checkpoint:
    """A ``.safetensors`` file, mapped: ``tensors`` are read-only views of
    it, read only when touched. The format is an 8-byte header length, a
    JSON header giving each tensor's dtype, shape and byte range, and the
    data. It is read here because safetensors' own numpy loader has no
    bfloat16.
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


def checkpoint_shapes(layout: Layout, n_layers: int) -> dict[str, tuple[int, ...]]:
    """Every tensor a checkpoint of ``layout`` over ``n_layers`` holds, by name."""
    return {name: shape for name, (_, shape) in _expand(layout, n_layers).items()}


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
