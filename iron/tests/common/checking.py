# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Check mode's judging, device-free: each step of a traced graph held to its
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
from iron.operators import GEMV, ElementwiseAdd, SiLU

K, M = 2048, 256


class Project(iron.Graph):
    """x + x, projected by ``w``, then SiLU: three steps, the second weighted."""

    def __init__(self, w):
        self.w = w

    def body(self, x):
        return SiLU(GEMV(self.w, ElementwiseAdd(x, x)))


def _run(traced, x, wrong: dict[int, np.ndarray]):
    """Each step on the host as check mode sees it: its inputs as the buffers
    hold them, what it wrote (its reference, or with ``wrong[i]`` in place of
    step ``i``'s weight, what that weight computes) and its reference.
    """
    held = {traced.input_args[0]: x}
    held |= {h.name: np.asarray(t) for t, h in traced.weights.values()}
    weights = {h.name for _, h in traced.weights.values()}
    for index, (op, *names) in enumerate(traced.runlist):
        op = op.resolved()
        by_name = dict(zip((b.name for b in op.buffers), names))
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
    traced = Project(w).trace(x=(K,))
    assert [type(op).__name__ for op, *_ in traced.runlist] == [
        "ElementwiseAdd",
        "GEMV",
        "SiLU",
    ]
    _run(traced, x, {})
    wrong = w.copy()
    wrong[: M // 2] = -wrong[: M // 2]
    with pytest.raises(RuntimeError, match=r"\[check step 1\] GEMV .*deviates"):
        _run(traced, x, {1: wrong})
