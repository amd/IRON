# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""RoPE on one core under a row bound, one angle row turning every row (as
Qwen3.5's multimodal RoPE turns an image's walked rows by its first
position's angles): the transfers move the rows the call bounds, which the
core turns, not the angle row's every row, which it never takes.
"""

import numpy as np
import pytest
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.operators.rope import RoPE

ROWS, COLS = 256, 64

pytestmark = pytest.mark.usefixtures("npu2")


class Turn(iron.Graph):
    def body(self, x, angle, *, n: Scratchpad[np.int32]):
        return RoPE.step(x[:n], angle, two_halves=False)


def inputs():
    rng = np.random.default_rng(0)
    x = rng.standard_normal((ROWS, COLS)).astype(bfloat16)
    theta = rng.uniform(-np.pi, np.pi, COLS // 2)
    angle = np.empty((1, COLS), np.float32)
    angle[0, ::2], angle[0, 1::2] = np.cos(theta), np.sin(theta)
    return x, angle.astype(bfloat16)


@pytest.mark.parametrize("n", [1, 40, ROWS])
def test_the_bound_rows_are_what_moves(n):
    x, angle = inputs()
    (step,) = Turn().record(x=x.shape, angle=angle.shape).steps
    op = step.op.resolved()
    tiles = op.derived_at("valid_x", valid=n)
    assert op.num_aie_columns == 1
    assert tiles * op.x.extent_unit(0) == n


@pytest.mark.supported_devices("npu2")
def test_the_bound_rows_turn_on_the_device():
    x, angle = inputs()
    turn = Turn()
    net = turn.compile(x=x.shape, angle=angle.shape)
    for n in (1, 40, ROWS):
        out = np.asarray(net(x, angle, n=n), np.float32).reshape(ROWS, COLS)[:n]
        want = np.asarray(turn.reference(x, angle, n=n), np.float32).reshape(n, COLS)
        verdict = compare(out, want, Tolerance.relative(0.05))
        assert verdict, f"{n=}: {verdict.detail}"
