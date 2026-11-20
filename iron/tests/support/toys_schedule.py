# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Toy graphs and recordings for the schedule, configuration, width, transport and across-call tuning tests."""

from __future__ import annotations

import iron
from iron.common.graph.record import Recording
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import sequences


def skip() -> tuple[ElementwiseAdd, RMSNorm, GEMV, ElementwiseAdd]:
    """Return a residual add held past RMSNorm and a GEMV, joined by a second add."""
    add = ElementwiseAdd(size=2048, num_aie_columns=2, tile_size=256)
    norm = RMSNorm(rows=1, tile_size=2048)
    proj = GEMV(M=2048, K=2048, feed_b=True, num_aie_columns=2)
    add2 = ElementwiseAdd(size=2048, num_aie_columns=2, tile_size=256)
    return add, norm, proj, add2


def skip_recording(name, add, norm, proj, add2) -> Recording:
    steps = sequences.steps(
        (add, "a", "b", "h"),
        (norm, "h", "n"),
        (proj, "W", "n", "g"),
        (add2, "g", "h", "out"),
    )
    return Recording.of_steps(name, steps, ["a", "b", "W"], ["out"])


def two_gemv_window(columns=4, channels=2) -> tuple[RMSNorm, GEMV, GEMV]:
    """Return decode's ``RMSNorm -> gate, up`` pair (HEADROOM.md's E2): a norm feeding two equal GEMVs streaming their weights at once."""
    norm = RMSNorm(rows=1, tile_size=2048)
    gate = GEMV(
        M=8192, K=2048, feed_b=True, num_aie_columns=columns, num_channels=channels
    )
    up = GEMV(
        M=8192, K=2048, feed_b=True, num_aie_columns=columns, num_channels=channels
    )
    return norm, gate, up


def two_gemv_window_recording(name, norm, gate, up) -> Recording:
    steps = sequences.steps(
        (norm, "x", "n"), (gate, "Wg", "n", "g"), (up, "Wu", "n", "u")
    )
    return Recording.of_steps(name, steps, ["x", "Wg", "Wu"], ["g", "u"])


class Alternating(iron.Graph):
    """ReLU and Tanh in turn, eight steps at ``columns`` columns: every step a switch apart (ported from ``test_tune_packings.py``).

    Args:
        columns: Each step's columns, the array's width on the device tuned.
    """

    def __init__(self, columns: int) -> None:
        self.columns = columns

    def body(self, x):
        from iron.operators.relu import ReLU
        from iron.operators.tanh import Tanh

        for _ in range(4):
            x = Tanh.step(
                ReLU.step(x, num_aie_columns=self.columns),
                num_aie_columns=self.columns,
            )
        return x


class Wide(iron.Graph):
    """ReLU, Tanh and Sigmoid at ``columns`` columns and two channels, twice: six cores a column, so packed only narrowed.

    Ported from ``test_tune_packings.py``.

    Args:
        columns: Each step's columns, the array's width on the device tuned.
    """

    def __init__(self, columns: int) -> None:
        self.columns = columns

    def body(self, x):
        from iron.operators.relu import ReLU
        from iron.operators.sigmoid import Sigmoid
        from iron.operators.tanh import Tanh

        for _ in range(2):
            for op in (ReLU, Tanh, Sigmoid):
                x = op.step(x, num_aie_columns=self.columns, num_channels=2)
        return x


def decode_step(add_cols=2) -> tuple[GEMV, ElementwiseAdd]:
    """Return one decode step a call-schedule toy repeats: a projection and its residual add."""
    gemv = GEMV(M=2048, K=2048, tile_size_input=4, tile_size_output=256)
    add = ElementwiseAdd(size=2048, num_aie_columns=add_cols, tile_size=256)
    return gemv, add


def decode_step_recording(name, gemv, add) -> Recording:
    steps = sequences.steps((gemv, "A", "x", "mid"), (add, "r", "mid", "out"))
    return Recording.of_steps(name, steps, ["A", "x", "r"], ["out"])


def projection_step(size=1024) -> GEMV:
    """Return one call a call-schedule toy repeats: a projection alone, which no region joins and no merge takes.

    Its call is short enough that a dispatch is much of it.
    """
    return GEMV(M=size, K=size, tile_size_input=4, tile_size_output=32)


def projection_step_recording(name, gemv) -> Recording:
    return Recording.of_steps(
        name, sequences.steps((gemv, "A", "x", "y")), ["A", "x"], ["y"]
    )


def residual_step(cols=2) -> tuple[ElementwiseAdd, ElementwiseMul]:
    """Return a step merged calls stack: elementwise throughout, so ``k`` calls are one call at ``k`` times the size."""
    add = ElementwiseAdd(size=2048, num_aie_columns=cols, tile_size=256)
    mul = ElementwiseMul(size=2048, num_aie_columns=cols, tile_size=256)
    return add, mul


def residual_step_recording(name, add, mul) -> Recording:
    steps = sequences.steps((add, "x", "r", "h"), (mul, "h", "g", "out"))
    return Recording.of_steps(name, steps, ["x", "r", "g"], ["out"])


def kv_write_read(width=64) -> tuple[Copy, Copy]:
    """Return a KV-cache-like write then read through one shared buffer, a row's worth of words each."""
    write = Copy(input_buffer_size=width, output_buffer_size=width)
    read = Copy(input_buffer_size=width, output_buffer_size=width)
    return write, read


def kv_write_read_recording(name, write, read) -> Recording:
    steps = sequences.steps((write, "k", "cache"), (read, "cache", "out"))
    return Recording.of_steps(name, steps, ["k", "cache"], ["out"])
