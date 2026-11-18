# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Toys the tuning transformation tests build: coded weights, a per-call range and shared state."""

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron import Precision, Scratchpad
from iron.common.graph.record import Recording
from iron.operators.copy import Copy
from iron.operators.decode import Decode
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.tests.support import sequences


def coded_consumer(M: int, K: int, rows: int = 1, num_aie_columns: int = 1):
    """Return a ``Decode`` of ``rows`` rows a call and the ``GEMV`` its plain weight feeds.

    ``Decode``'s coded rows in, bf16 weight out; the ``GEMV`` reads that weight as its
    ``A``, both on ``num_aie_columns`` columns, a pair a ``Region`` may share one worker
    between.
    """
    decode = Decode(M=M, K=K, rows=rows, num_aie_columns=num_aie_columns)
    gemv = GEMV(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=1,
        tile_size_output=M // num_aie_columns,
    )
    return decode, gemv


def coded_consumer_recording(name: str, decode: Decode, gemv: GEMV) -> Recording:
    """Return ``decode`` then ``gemv``, ``decode``'s plain weight and ``gemv``'s ``A`` both ``w``."""
    steps = sequences.steps((decode, "coded", "w"), (gemv, "w", "x", "out"))
    return Recording.of_steps(name, steps, ["coded", "x"], ["out"])


def small_integer_weight(shape: tuple[int, ...], seed: int) -> np.ndarray:
    """Return small integers as bf16 at ``shape``, whose coded form is always well inside capacity."""
    rng = np.random.default_rng(seed)
    return rng.integers(-8, 8, size=shape).astype(bfloat16)


def coded_consumer_recording_with_weight(
    rows: int,
    num_aie_columns: int,
    weight: np.ndarray,
    num_batches: int | None = None,
) -> Recording:
    """Record a real ``Decode`` reading ``weight``, into the ``GEMV`` it feeds.

    ``weight`` is a graph weight (``iron.param``), so the recording carries it for real:
    an overflowing row shows up in ``recording.weights`` as a real ``CodedWeight``, not
    only in the shapes ``Decode`` and ``GEMV`` are built at. ``num_batches`` batches
    ``x``, amortizing the one decoded weight over more of the ``GEMV``'s compute; None
    for the single row a decode step reads a call.
    """
    M, K = weight.shape
    cols = num_aie_columns

    class CodedConsumer(iron.Graph):
        def __init__(self, w):
            self.w = iron.param(w)

        def body(self, x):
            decoded = Decode.step(self.w, rows=rows, num_aie_columns=cols)
            return GEMV.step(
                decoded,
                x,
                num_aie_columns=cols,
                tile_size_input=1,
                tile_size_output=M // cols,
                num_batches=num_batches,
            )

    shape = (K,) if num_batches is None else (num_batches, K)
    return CodedConsumer(weight).record(x=shape)


class RangedPair(iron.Graph):
    """A projection over the first ``rows`` of ``x``, and a copy of the first ``valid`` rows of eight of ``y``.

    Two per-call values in one call, a 2-D per-call range: ``rows`` bounds the
    projection's input rows, ``valid`` the copy's length, independently of each other.
    The copy moves rows of eight bf16s: a per-call length counts whole 16-byte units.
    """

    def __init__(self, K: int, N: int):
        self.K, self.N = K, N

    def body(self, x, w, y, *, rows: Scratchpad[np.int32], valid: Scratchpad[np.int32]):
        projected = GEMM.step(x[:rows], w, b_col_maj=True, precision=Precision.MEDIUM)
        copied = Copy.step(y.reshape(y.shape[0] // 8, 8)[:valid])
        return projected, copied


def shared_kv_state(size: int = 256, tile: int = 64):
    """Return a graph whose prefill-sized call writes a persistent ``kv`` and whose decode-sized call reads it.

    One real ``iron.state`` buffer, shared by both versions of one graph (as
    ``iron/tests/infrastructure/test_graph_versions.py``'s own function does): the
    prefill-shaped call adds a bias row into ``kv`` and returns it; the decode-shaped
    call multiplies ``kv`` by its own first ``size`` elements.
    """
    bias = small_integer_weight((size,), 1)
    kv = iron.state((size,), name="kv")

    class SharedKVState(iron.Graph):
        def body(self, x):
            if x.shape[0] == size:
                ElementwiseAdd.step(x, bias, kv, tile_size=tile)
                return ElementwiseAdd.step(kv, bias, tile_size=tile)
            return ElementwiseMul.step(kv, x[:size], tile_size=tile)

    return SharedKVState()
