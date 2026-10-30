# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A weight a graph streams as coded rows (``aie.utils.coded``): the buffer
derived from it, which every coded operand reading the weight shares.
"""

from __future__ import annotations

import os
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor

import numpy as np
from aie.utils import coded
from ml_dtypes import bfloat16


class CodedWeight:
    """``array``'s coded rows at ``capacity``: the weight a coded operand
    reads in its place, encoded once for every version of a graph.

    Attributes:
        array: The bf16 weight.
        name: The weight's buffer in the graph.
        capacity: The exceptions a coded row holds.
        rows: The coded rows, once ``encode()`` has run.
    """

    def __init__(self, array: np.ndarray, name: str, capacity: int) -> None:
        self.array = array
        self.name = name
        self.capacity = capacity
        self.rows: np.ndarray | None = None

    @property
    def shape(self) -> tuple[int, ...]:
        """The coded rows' shape, ``(..., M, R)``."""
        *lead, K = self.array.shape
        return (*lead, coded.row_bytes(K, self.capacity))

    def encode(self) -> np.ndarray:
        """The coded rows, encoded on the first call.

        Raises:
            ValueError: A row holds more exceptions than ``capacity``.
        """
        if self.rows is None:
            self.rows = coded.encode_rows(
                np.asarray(self.array, bfloat16), self.capacity
            )
        return self.rows


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
