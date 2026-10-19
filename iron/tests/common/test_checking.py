# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Check mode's judging, device-free: each step of a recorded graph held to its
reference on its own inputs by its ``tolerance()`` (``check_step``, what
``Graph.compile(check=True)`` runs after every dispatch). The oracle's own
step outputs pass; a step computed from a real wrong weight is caught at
that step, and the steps before it pass.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common.image.callable import check_step
from iron.common.image.step import BufferRef
from iron.operators import GEMV, ElementwiseAdd, SiLU

K, M = 2048, 256


class Project(iron.Graph):
    """x + x, projected by ``w``, then SiLU: three steps, the second weighted."""

    def __init__(self, w):
        self.w = w

    def body(self, x):
        return SiLU.step(GEMV.step(self.w, ElementwiseAdd.step(x, x)))


def _run(recording, x, wrong: dict[int, np.ndarray]):
    """Each step on the host as check mode sees it: its inputs as the buffers
    hold them, what it wrote (its reference, or with ``wrong[i]`` in place of
    step ``i``'s weight, what that weight computes) and its reference.
    """
    held = {BufferRef(recording.inputs[0].name): x}
    held |= {h.ref(): np.asarray(t) for t, h in recording.weights.values()}
    weights = {h.ref() for _, h in recording.weights.values()}
    for index, step in enumerate(recording.steps):
        op = step.op.resolved()
        by_name = dict(zip((b.name for b in op.buffers), step.refs()))
        inputs = {b.name: held[by_name[b.name]] for b in op.inputs}
        expected = op._call_reference(inputs)
        computed = {
            name: wrong[index] if by_name[name] in weights and index in wrong else t
            for name, t in inputs.items()
        }
        written = op._call_reference(computed)
        check_step(index, op, by_name, inputs, written, expected)
        held |= {by_name[b.name]: written[b.name] for b in op.outputs}


def test_the_oracles_steps_pass_and_a_wrong_weight_is_caught_at_its_step(npu2):
    rng = np.random.default_rng(0)
    w = (rng.standard_normal((M, K)) * 0.05).astype(bfloat16)
    x = (rng.random(K) * 2 - 1).astype(bfloat16)
    recording = Project(w).record(x=(K,))
    assert [type(s.op).__name__ for s in recording.steps] == [
        "ElementwiseAdd",
        "GEMV",
        "SiLU",
    ]
    _run(recording, x, {})
    wrong = w.copy()
    wrong[: M // 2] = -wrong[: M // 2]
    with pytest.raises(RuntimeError, match=r"\[check step 1\] GEMV .*deviates"):
        _run(recording, x, {1: wrong})
