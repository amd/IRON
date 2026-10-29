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

from ..common.graph.compiled import param
from ..common.graph.fill import filled
from .golden import fingerprint


class _Shard:
    """One ``.safetensors`` file, or a PyTorch checkpoint (a ``.pth`` zip),
    mapped so ``tensors`` are lazy read-only views, parsed here since
    safetensors' numpy loader has no bfloat16 and IRON reads PyTorch
    without torch.
    """

    # I64: a BatchNorm's num_batches_tracked.
    DTYPES = {"BF16": bfloat16, "F16": np.float16, "F32": np.float32, "I64": np.int64}

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
            if t.get("dtype") not in self.DTYPES:
                raise ValueError(f"{self.path}: {name} is {t.get('dtype')}")
            if len(t.get("data_offsets", ())) != 2 or "shape" not in t:
                raise ValueError(f"{self.path}: {name} has no data_offsets or shape")
            begin, end = (8 + length + o for o in t["data_offsets"])
            dtype = np.dtype(self.DTYPES[t["dtype"]])
            if (
                end - begin != dtype.itemsize * math.prod(t["shape"])
                or begin < 8 + length
                or end > data.size
            ):
                raise ValueError(
                    f"{self.path}: {name} spans bytes {begin} to {end}, not "
                    f"{t['dtype']} {t['shape']} within the file"
                )
            view = data[begin:end].view(dtype)
            self.tensors[name] = view.reshape(t["shape"])

    def _torch(self, data: np.ndarray) -> dict[str, np.ndarray]:
        """A PyTorch checkpoint's tensors, each a view of its storage's
        bytes, which PyTorch stores uncompressed.
        """
        archive = zipfile.ZipFile(self.path)
        if not archive.namelist():
            raise ValueError(f"{self.path}: an empty archive, not a checkpoint")
        root = archive.namelist()[0].split("/")[0]

        def storage(key: str) -> np.ndarray:
            info = archive.getinfo(f"{root}/data/{key}")
            if info.compress_type != zipfile.ZIP_STORED:
                raise ValueError(f"{self.path}: storage {key} is compressed")
            # A ZIP local file header is 30 bytes, its name's and extra
            # field's lengths at 26; the name, the field, then the bytes.
            header, lengths = info.header_offset + 30, info.header_offset + 26
            names = self._map[lengths:header]
            begin = header + sum(struct.unpack("<HH", names))
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
    of its storage, checked to lie inside it. ``GLOBALS`` names every
    global a state dict's pickle may use, so loading one runs no code of
    its own.
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


def weights_file(directory) -> Path:
    """A checkpoint directory's weights: a sharded checkpoint's
    ``model.safetensors.index.json``, else ``model.safetensors``.
    """
    index = Path(directory) / "model.safetensors.index.json"
    return index if index.exists() else index.with_name("model.safetensors")


class Checkpoint:
    """A ``.safetensors`` file or a PyTorch checkpoint, or, given its
    ``.safetensors.index.json``, every shard a sharded checkpoint splits
    across, its tensors merged into one mapping, ``tensors``.
    """

    def __init__(self, path):
        self.path = Path(path)
        weight_map = None
        paths = [self.path]
        if self.path.suffix == ".json":
            weight_map = json.loads(self.path.read_text())["weight_map"]
            names = sorted(set(weight_map.values()))
            for n in names:
                if Path(n).name != n:
                    raise ValueError(f"{self.path}: {n} is not a file beside the index")
            paths = [self.path.parent / n for n in names]
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
        """Return the checkpoint's tensors as a tree of ``param``, split at
        the dots (``model.layers.3.weight`` becomes
        ``tree.model.layers[3].weight``).

        Args:
            fill: What the arrays hold: ``"read"`` the tensors (lazy views);
                ``"random"`` or ``"unread"`` ``filled``'s, which reads
                nothing past the header.
            seed: The seed ``"random"`` draws at.

        Raises:
            ValueError: ``fill`` is none of these.
        """
        if fill not in ("read", "random", "unread"):
            raise ValueError(f"fill is read, random or unread, not {fill!r}")
        tensors = self.tensors
        if fill != "read":
            named = {n: (t.shape, t.dtype) for n, t in tensors.items()}
            tensors = filled(fill, named, seed)
        return nest({n: param(t) for n, t in tensors.items()}, file=self.path)


def leaves(tree, prefix: str = "") -> Iterator[tuple[str, Any]]:
    """Each leaf of ``tree``, a ``Checkpoint.tree()``'s namespaces and
    lists, by its dotted name: ``nest``'s inverse.
    """
    if isinstance(tree, (list, SimpleNamespace)):
        items = enumerate(tree) if isinstance(tree, list) else vars(tree).items()
        for name, value in items:
            yield from leaves(value, f"{prefix}{name}.")
    else:
        yield prefix[:-1], tree


# What a missing name's error calls the file of a tree that names none.
_FILE = "the checkpoint"


def nest(
    named: Mapping[str, Any], path: str = "", file: str | Path = _FILE
) -> SimpleNamespace:
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
    """Nested dicts as ``_Module``s, those keyed by indices as ``_Layers``,
    an empty ``_Module`` at a skipped index.
    """
    if not isinstance(node, dict):
        return node
    items = {key: _tree(child, f"{path}{key}.", file) for key, child in node.items()}
    if items and all(key.isdigit() for key in items):
        top = max(map(int, items))
        # A skipped index is a module with no weights (an activation in a
        # Sequential), never most of them: a name can't make the host
        # build millions.
        if top >= 4 * len(items) + 4:
            raise ValueError(f"{file}: {path}{top} is past its {len(items)} layers")
        indices = range(top + 1)
        tree = _Layers(
            items[str(i)] if str(i) in items else _tree({}, f"{path}{i}.", file)
            for i in indices
        )
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
            f"(it has {', '.join(vars(self)) or 'nothing'})"
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


def subtree(tree, **modules):
    """A tree of ``modules``, each a module of ``tree``, at their names: a
    checkpoint's part as a model loads it (a text decoder of a
    vision-language checkpoint), a missing name naming ``tree``'s file.
    """
    file = tree._file if isinstance(tree, (_Module, _Layers)) else _FILE
    return _tree(modules, "", file)


def renamed(tree, renames: Mapping[str, str]):
    """A copy of ``tree`` with each leaf under a run of whole dotted names
    among ``renames``' keys moved to the run its value names, the rest
    where they are; its namespaces are new, so a caller may change them
    and leave ``tree`` as it was.
    """

    def moved(path):
        for old, new in renames.items():
            at = f".{path}.".find(f".{old}.")
            if at >= 0:
                return path[:at] + new + path[at + len(old) :]
        return path

    held = isinstance(tree, (_Module, _Layers))
    return nest(
        {moved(path): value for path, value in leaves(tree)},
        tree._path if held else "",
        tree._file if held else _FILE,
    )
