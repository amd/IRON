# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A graph called in another graph's body, device-free: its steps trace into
the caller's, its weights take the caller's path to it, and the caller's
reference runs it.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import Carried, Scratchpad
from iron.lm import SwiGLU, swiglu
from iron.operators.relu import ReLU

pytestmark = pytest.mark.usefixtures("npu2")

E, H = 512, 1024


def weight(rng, rows, cols):
    return (rng.standard_normal((rows, cols)) / np.sqrt(cols)).astype(bfloat16)


class Block(iron.Graph):
    """A feed-forward held as a graph and called in this one's body."""

    def __init__(self):
        rng = np.random.default_rng(0)
        self.ffn = SwiGLU(weight(rng, H, E), weight(rng, H, E), weight(rng, E, H))

    def body(self, x):
        return ReLU(self.ffn(x))


class Inline(iron.Graph):
    """The same feed-forward written into the body."""

    def __init__(self, ffn: SwiGLU):
        self.ffn = ffn

    def body(self, x):
        f = self.ffn
        return ReLU(swiglu(x, f.w_gate, f.w_up, f.w_down))


def test_a_called_graph_traces_into_its_caller():
    block = Block()
    called = block.trace(x=((256, E), bfloat16))
    inline = Inline(block.ffn).trace(x=((256, E), bfloat16))
    assert [s.op.design_key() for s in called.steps] == [
        s.op.design_key() for s in inline.steps
    ]
    names = {h.name for _, h in called.weights.values()}
    assert names == {"ffn.w_gate", "ffn.w_up", "ffn.w_down"}


def test_the_callers_reference_runs_the_called_graph():
    block = Block()
    x = np.random.default_rng(1).standard_normal((256, E)).astype(bfloat16)
    got = np.asarray(block.reference(x))
    want = np.maximum(np.asarray(block.ffn.reference(x)).astype(np.float32), 0)
    assert np.array_equal(
        got.astype(np.float32), want.astype(bfloat16).astype(np.float32)
    )


class Counter(iron.Graph):
    def body(self, x, *, step: Carried[np.int32]):
        return ReLU(x), iron.carry(step=step + 1)


class CallsCounter(iron.Graph):
    def __init__(self):
        self.counter = Counter()

    def body(self, x, *, step: Scratchpad[np.int32]):
        return self.counter(x, step=step)[0]


class Rows(iron.Graph):
    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU(x[:n])


class CallsWithoutValue(iron.Graph):
    def __init__(self):
        self.rows = Rows()

    def body(self, x):
        return self.rows(x)


def test_a_called_graph_takes_every_value_and_carries_none():
    with pytest.raises(TypeError, match="carries no values"):
        CallsCounter().trace(x=((256, E), bfloat16))
    with pytest.raises(TypeError, match="per-call values"):
        CallsWithoutValue().trace(x=((256, E), bfloat16))
