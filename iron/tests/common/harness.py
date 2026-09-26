# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``vectors()`` and ``verify_buffer()``: the device test's two halves, host-side."""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common.harness import vectors, verify_buffer
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.relu import ReLU

pytestmark = pytest.mark.usefixtures("npu2")


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
    assert vectors(op, x=(32,))["x"].shape == (32,)
    plain, centred = vectors(op)["x"], vectors(op, centered=("x",))["x"]
    assert plain.dtype == centred.dtype == bfloat16
    assert 0 <= plain.min() and plain.max() < 4.0 and not (plain == plain.round()).all()
    assert (centred < 0).any() and (centred > 0).any()  # both signs, as ReLU asks
    with pytest.raises(ValueError, match=r"has no input \['z'\]"):
        vectors(op, z=given)


def test_verify_buffer_returns_the_indices_outside_tolerance():
    ref = np.arange(8, dtype=np.float32)
    assert verify_buffer(ref.copy(), "y", ref) == []
    out = ref.copy()
    out[3] += 1.0
    out[5] += 0.001
    assert verify_buffer(out, "y", ref, rel_tol=0.04, abs_tol=1e-6) == [3]
    assert verify_buffer(out, "y", ref, rel_tol=0.0, abs_tol=0.0) == [3, 5]
    assert verify_buffer(ref[:6].copy(), "y", ref) == [6, 7]  # short: the rest
