# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``vectors()`` and ``verify_buffer()``: the device test's two halves, host-side."""

import numpy as np
import pytest
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common.harness import vectors, verify_buffer
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.relu import ReLU
from iron.operators.rope import RoPE

pytestmark = pytest.mark.usefixtures("npu2")

RELATIVE = Tolerance.relative(0.04, 1e-6)


def test_vectors_draws_each_input_and_runs_the_reference_on_the_draw():
    op = ElementwiseAdd(size=64, num_aie_columns=1, tile_size=64)
    v = vectors(op, seed=1)
    assert set(v.inputs) == {"a", "b"} and set(v.outputs) == {"y"}
    assert v["a"].shape == (64,) and v["a"].dtype == bfloat16
    np.testing.assert_array_equal(v["y"], v["a"] + v["b"])
    assert np.array_equal(vectors(op, seed=1)["a"], v["a"])  # seeded
    assert not np.array_equal(vectors(op, seed=2)["a"], v["a"])


def test_vectors_takes_a_given_array_a_shape_or_a_centred_draw():
    op = ReLU(size=64, num_aie_columns=1, tile_size=64)
    given = np.arange(64, dtype=bfloat16)
    assert vectors(op, x=given)["x"] is given
    assert vectors(op, x=(2, 32))["x"].shape == (2, 32)  # the declared 64, as given
    plain, centred = vectors(op)["x"], vectors(op, centered=("x",))["x"]
    assert plain.dtype == centred.dtype == bfloat16
    assert 0 <= plain.min() and plain.max() < 4.0 and not (plain == plain.round()).all()
    assert (centred < 0).any() and (centred > 0).any()  # both signs, as ReLU asks
    with pytest.raises(ValueError, match=r"has no input \['z'\]"):
        vectors(op, z=given)


def test_gate_is_the_declared_tolerance_else_the_contract():
    rope = RoPE(rows=8, cols=64)
    assert rope.gate() is RoPE.test.tolerance
    relu = ReLU(size=64, num_aie_columns=1, tile_size=64)
    assert relu.gate() == relu.resolved().tolerance() is not None


def test_verify_buffer_returns_the_verdict_of_compare():
    ref = np.arange(8, dtype=np.float32)
    assert verify_buffer(ref.copy(), "y", ref, RELATIVE)
    out = ref.copy()
    out[3] += 1.0
    out[5] += 0.001
    relative = verify_buffer(out, "y", ref, RELATIVE)
    assert (relative.n_mismatch, relative.first_bad_index) == (1, 3)
    exact = verify_buffer(out, "y", ref, Tolerance.exact())
    assert (exact.n_mismatch, exact.first_bad_index) == (2, 3)
    short = verify_buffer(ref[:6].copy(), "y", ref, RELATIVE)
    assert not short and "shape mismatch" in short.detail


def test_verify_buffer_judges_a_bound_tolerance_by_its_evaluated_limit():
    ref = np.arange(8, dtype=np.float32)
    out = ref + np.float32(0.25)

    def eighth(x):
        return np.abs(x) / 8

    judge = Tolerance.bounded(eighth)
    limit = eighth(ref)  # 0.25 from x = 2 on
    verdict = verify_buffer(out, "y", ref, judge, bound=limit)
    assert (verdict.n_mismatch, verdict.first_bad_index) == (2, 0)
    with pytest.raises(ValueError, match="needs its bound="):
        verify_buffer(out, "y", ref, judge)
