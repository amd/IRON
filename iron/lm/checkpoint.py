# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A model's weights: ``Checkpoint.tree()``, the tensors by their own
names: ``model.layers.3.self_attn.q_proj.weight`` is
``weights.model.layers[3].self_attn.q_proj.weight``.
"""

import io
import json
import math
import mmap
import pickle
import struct
import zipfile
from collections import OrderedDict
from collections.abc import Callable, Iterator, Mapping
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Literal

import numpy as np
from ml_dtypes import bfloat16

from .golden import fingerprint


class _Shard:
    """One ``.safetensors`` file, or a PyTorch checkpoint (a ``.pth`` zip),
    mapped: ``tensors`` are read-only views of it, read only when touched,
    a PyTorch checkpoint's named by their dotted path from its root
    (``model.backbone.stem.conv.weight``). Parsed here: safetensors' own
    numpy loader has no bfloat16, and IRON reads PyTorch's without torch.
    """

    DTYPES = {"BF16": bfloat16, "F16": np.float16, "F32": np.float32}

    def __init__(self, path: Path):
        self.path = path
        with open(self.path, "rb") as f:
            # The mapping holds its own reference to the file.
            self._map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        data = np.frombuffer(self._map, dtype=np.uint8)
        self._address = data.ctypes.data
        if zipfile.is_zipfile(self.path):
            self.tensors = self._torch(data)
            return
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

    def _torch(self, data: np.ndarray) -> dict[str, np.ndarray]:
        """A PyTorch checkpoint's tensors, each a view of its storage's
        bytes, which PyTorch stores uncompressed.
        """
        archive = zipfile.ZipFile(self.path)
        root = archive.namelist()[0].split("/")[0]

        def storage(key: str) -> np.ndarray:
            info = archive.getinfo(f"{root}/data/{key}")
            if info.compress_type != zipfile.ZIP_STORED:
                raise ValueError(f"{self.path}: storage {key} is compressed")
            # The local header's name and extra field lengths, then the bytes.
            names = self._map[info.header_offset + 26 : info.header_offset + 30]
            begin = info.header_offset + 30 + sum(struct.unpack("<HH", names))
            return data[begin : begin + info.file_size]

        pickled = io.BytesIO(archive.read(f"{root}/data.pkl"))
        tensors = {}
        pending = [("", _TorchUnpickler(pickled, storage).load())]
        while pending:
            path, node = pending.pop()
            if isinstance(node, np.ndarray):
                tensors[path] = node
            elif isinstance(node, dict):
                pending += [(f"{path}.{k}" if path else k, v) for k, v in node.items()]
        return tensors

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


class _TorchUnpickler(pickle.Unpickler):
    """A PyTorch checkpoint's pickle, read as data: each tensor a numpy view
    of its storage, checked to lie inside it. ``GLOBALS`` is every global a
    state dict's pickle names, and nothing else resolves, so loading one
    runs no code of its own.
    """

    GLOBALS = {
        ("collections", "OrderedDict"): OrderedDict,
        ("torch._utils", "_rebuild_tensor_v2"): None,
        ("torch", "BFloat16Storage"): bfloat16,
        ("torch", "HalfStorage"): np.float16,
        ("torch", "FloatStorage"): np.float32,
        # A BatchNorm's num_batches_tracked.
        ("torch", "LongStorage"): np.int64,
    }

    def __init__(self, file, storage: Callable[[str], np.ndarray]):
        super().__init__(file)
        self.storage = storage

    def find_class(self, module: str, name: str):
        if (module, name) not in self.GLOBALS:
            raise pickle.UnpicklingError(f"a checkpoint may not load {module}.{name}")
        if (module, name) == ("torch._utils", "_rebuild_tensor_v2"):
            return self.rebuild
        return self.GLOBALS[module, name]

    def persistent_load(self, pid):
        """A storage, by its key, as its dtype: ``("storage", dtype, key,
        location, numel)``.

        Raises:
            pickle.UnpicklingError: Any other id, or a storage shorter
                than its ``numel``.
        """
        dtypes = [
            d for (_, name), d in self.GLOBALS.items() if name.endswith("Storage")
        ]
        if not (
            isinstance(pid, tuple)
            and len(pid) == 5
            and pid[0] == "storage"
            and any(pid[1] is d for d in dtypes)
            and isinstance(pid[2], str)
            and isinstance(pid[4], int)
        ):
            raise pickle.UnpicklingError(f"a checkpoint's storage id is {pid!r}")
        _, dtype, key, _, numel = pid
        data, size = self.storage(key), np.dtype(dtype).itemsize
        if not 0 <= numel * size <= data.size:
            raise pickle.UnpicklingError(
                f"storage {key} holds {data.size} bytes, not {numel} {np.dtype(dtype)}"
            )
        return data[: numel * size].view(dtype)

    @staticmethod
    def rebuild(storage, offset, size, stride, *_):
        """``torch._utils._rebuild_tensor_v2``'s tensor, a read-only view of
        ``storage``.

        Raises:
            pickle.UnpicklingError: It is not one, or reaches outside
                ``storage``.
        """
        if not (
            isinstance(storage, np.ndarray)
            and isinstance(size, tuple)
            and isinstance(stride, tuple)
            and len(size) == len(stride)
            and all(isinstance(n, int) and n >= 0 for n in (offset, *size, *stride))
        ):
            raise pickle.UnpicklingError("a checkpoint's tensor is not one")
        last = offset + sum((n - 1) * s for n, s in zip(size, stride) if n)
        if math.prod(size) and last >= storage.size:
            raise pickle.UnpicklingError(
                f"a tensor reaches element {last} of a {storage.size}-element storage"
            )
        return np.lib.stride_tricks.as_strided(
            storage[offset:],
            size,
            tuple(s * storage.itemsize for s in stride),
            writeable=False,
        )


class Checkpoint:
    """A ``.safetensors`` file or a PyTorch checkpoint, or, given its
    ``.safetensors.index.json``, every shard a sharded checkpoint splits
    across (``weight_map``, next to one another on disk), its tensors merged
    into one mapping, ``tensors``.
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

    def fingerprint(self) -> str:
        """A digest of each tensor's name, type and shape and of the first
        and last 4 KiB of its bytes: what tells a fine-tune from its base
        without reading either whole.
        """
        ends = []
        for name, t in self.tensors.items():
            n = 4096 // t.itemsize
            ends.append([name, f"{t.dtype}{t.shape}", t.flat[:n], t.flat[-n:]])
        return fingerprint(ends)

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
                anything of fewer than two axes normal with deviation 0.1,
                about zero if it is a bias and about one otherwise (a norm),
                so that swapping two changes the output. ``"unread"``: allocated
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

            def draw(name, t):
                x = rng.standard_normal(t.shape, dtype=np.float32)
                if t.ndim >= 2:
                    return (x / np.sqrt(math.prod(t.shape[1:]))).astype(t.dtype)
                return (x / 10 + (not name.endswith("bias"))).astype(t.dtype)

            tensors = {name: draw(name, t) for name, t in self.tensors.items()}
        elif fill == "unread":
            tensors = {
                name: (
                    np.zeros((), t.dtype) if t.ndim == 0 else np.empty(t.shape, t.dtype)
                )
                for name, t in self.tensors.items()
            }
        else:
            raise ValueError(f"fill is read, random or unread, not {fill!r}")
        return _nest(tensors, file=self.path)


def leaves(tree, prefix: str = "") -> Iterator[tuple[str, Any]]:
    """Each leaf of ``tree``, a ``Checkpoint.tree()``'s namespaces and
    lists, by its dotted name: ``_nest``'s inverse.
    """
    if isinstance(tree, (list, SimpleNamespace)):
        items = enumerate(tree) if isinstance(tree, list) else vars(tree).items()
        for name, value in items:
            yield from leaves(value, f"{prefix}{name}.")
    else:
        yield prefix[:-1], tree


# What a missing name's error calls the file of a tree that names none.
_FILE = "the checkpoint"


def _nest(named: Mapping[str, Any], path: str = "", file=_FILE) -> SimpleNamespace:
    """Values by dotted name, nested as ``Checkpoint.tree()`` nests them,
    under ``path`` (a dotted prefix) of ``file``, which a missing name
    names.
    """
    nested: dict = {}
    for name, value in named.items():
        *parents, leaf = name.split(".")
        node = nested
        for key in parents:
            node = node.setdefault(key, {})
        node[leaf] = value
    return _tree(nested, path, file)


def _tree(node, path: str, file) -> Any:
    """Nested dicts as ``_Module``s, those keyed by indices as ``_Layers``.

    Raises:
        ValueError: A run of indices skips one.
    """
    if not isinstance(node, dict):
        return node
    items = {key: _tree(child, f"{path}{key}.", file) for key, child in node.items()}
    if items and all(key.isdigit() for key in items):
        indices = range(max(map(int, items)) + 1)
        missing = sorted(set(indices) - {int(key) for key in items})
        if missing:
            raise ValueError(
                f"{path[:-1]} in {file}: indices {sorted(map(int, items))} "
                f"skip {missing}"
            )
        tree = _Layers(items[str(i)] for i in indices)
    else:
        tree = _Module(**items)
    tree._path, tree._file = path, file
    return tree


class _Module(SimpleNamespace):
    """A module of a ``Checkpoint.tree()``, its tensors and submodules by
    name; a name it lacks raises an ``AttributeError`` naming its dotted
    path, the file and the names it has.
    """

    __slots__ = ("_path", "_file")

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(name)
        raise AttributeError(
            f"{self._path}{name} is not in {self._file} "
            f"(it has {', '.join(vars(self))})"
        )


class _Layers(list):
    """A run of a ``Checkpoint.tree()``'s modules by index; an index past
    the end raises an ``IndexError`` naming its dotted path, the file and
    how many there are.
    """

    __slots__ = ("_path", "_file")

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            raise IndexError(
                f"{self._path}{index} is not in {self._file} (it has {len(self)})"
            ) from None


def renamed(tree, renames: Mapping[str, str]):
    """A copy of ``tree`` with each leaf under a dotted path among
    ``renames``' keys moved to the path its value names, the rest where
    they are: its namespaces new, so a ``sanitize`` may change them.
    """

    def moved(path):
        for old, new in renames.items():
            if path == old or path.startswith(old + "."):
                return new + path[len(old) :]
        return path

    return _nest(
        {moved(path): value for path, value in leaves(tree)},
        getattr(tree, "_path", ""),
        getattr(tree, "_file", _FILE),
    )
