# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A weight a graph streams as coded rows (``aie.utils.coded``): the buffer
derived from it, which every coded operand reading the weight shares, and
the cache that keeps it from being encoded on every load.
"""

from __future__ import annotations

import dataclasses
import hashlib
import os
from collections.abc import Callable, Iterable
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import BinaryIO

import numpy as np
from aie.utils import coded
from aie.utils.compile import NPU_CACHE_HOME
from ml_dtypes import bfloat16

CACHE = Path(NPU_CACHE_HOME) / "iron" / "coded"


@dataclasses.dataclass(frozen=True)
class Source:
    """Where a weight's bytes are in a file: the file as it was when read
    (its path, size and modification time) and the tensor's byte offset.
    """

    path: str
    size: int
    mtime_ns: int
    offset: int


class CodedWeight:
    """``array``'s coded rows at ``capacity``: the weight a coded operand
    reads in place of ``array``, encoded once for every version of a graph.
    A weight read from a file (``source``) is cached under ``cache``, keyed
    by the file, the tensor, the format and the capacity; one that is not
    is encoded every time.

    Attributes:
        array: The bf16 weight.
        name: The weight's buffer in the graph.
        capacity: The exceptions a coded row holds.
        source: Where ``array`` was read from, or None.
        rows: The coded rows, once ``encode()`` has run.
        from_cache: Whether ``rows`` were read from the cache.
    """

    def __init__(
        self,
        array: np.ndarray,
        name: str,
        capacity: int,
        source: Source | None = None,
        cache: Path = CACHE,
    ) -> None:
        self.array = array
        self.name = name
        self.capacity = capacity
        self.source = source
        self.cache = cache
        self.rows: np.ndarray | None = None
        self.from_cache = False

    @property
    def shape(self) -> tuple[int, ...]:
        """The coded rows' shape, ``(..., M, R)``."""
        *lead, K = self.array.shape
        return (*lead, coded.row_bytes(K, self.capacity))

    @property
    def cached(self) -> Path | None:
        """The cache file the rows are kept in, or None without a source."""
        if self.source is None:
            return None
        key = repr(
            (
                coded.FORMAT,
                self.capacity,
                tuple(self.array.shape),
                dataclasses.astuple(self.source),
            )
        )
        return self.cache / f"{hashlib.sha256(key.encode()).hexdigest()}.npy"

    def encode(self) -> np.ndarray:
        """The coded rows: on the first call read from the cache, else
        encoded and, with a source, written to it. A refusal is cached too.

        Raises:
            ValueError: A row holds more exceptions than ``capacity``.
        """
        if self.rows is not None:
            return self.rows
        cached = self.cached
        refusal = None if cached is None else cached.with_suffix(".refused")
        if cached is not None and cached.exists():
            self.rows = np.load(cached, mmap_mode="r")
            self.from_cache = True
            return self.rows
        if refusal is not None and refusal.exists():
            raise ValueError(refusal.read_text())
        try:
            rows = coded.encode_rows(np.asarray(self.array, bfloat16), self.capacity)
        except ValueError as refused:
            if refusal is not None:
                _publish(refusal, lambda f: f.write(str(refused).encode()))
            raise
        if cached is not None:
            _publish(cached, lambda f: np.save(f, rows))
        self.rows = rows
        return rows


def _publish(path: Path, write: Callable[[BinaryIO], object]) -> None:
    """Write ``path`` whole or not at all: a reader racing the writer finds
    either no file or every byte of it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_name(f"{path.name}.{os.getpid()}.partial")
    with open(partial, "wb") as f:
        write(f)
    os.replace(partial, path)


def encode_all(weights: Iterable[CodedWeight]) -> dict[CodedWeight, ValueError]:
    """Encode ``weights``, a thread a weight; return each one that a row's
    exceptions refuse, with why.
    """
    pending = [w for w in weights if w.rows is None]

    def attempt(w: CodedWeight) -> ValueError | None:
        try:
            w.encode()
        except ValueError as refused:
            return refused
        return None

    with ThreadPoolExecutor(
        max_workers=min(len(pending), os.cpu_count() or 1) or 1
    ) as pool:
        results = list(pool.map(attempt, pending))
    return {w: e for w, e in zip(pending, results) if e is not None}
