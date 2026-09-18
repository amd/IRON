#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``AIERuntimeArgSpec``'s read/write predicates and the shared shape helpers.

``direction`` is a string, and every caller that wanted to know whether a step
touches a buffer compared it against a set inline. That is fine until
``"inout"`` shows up: it has to answer yes to *both* questions, and a caller
that partitions arguments into inputs and outputs will count it once and place
it wrong. The liveness analysis that memory planning depends on is exactly such
a caller, so the predicates are pinned here rather than left implicit.

The shape helpers exist because an operator's *spec* and its *design* are
separable. A ReLU and a transpose share nothing in their generated MLIR, but
both declare one input and one output of identical shape -- so the shape rule
is a function anything can call, not a base class you have to inherit.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common import AIERuntimeArgSpec, same_shape_binary, same_shape_unary


@pytest.mark.parametrize(
    "direction, reads, writes",
    [("in", True, False), ("out", False, True), ("inout", True, True)],
)
def test_direction_predicates(direction, reads, writes):
    spec = AIERuntimeArgSpec(direction, (16,))
    assert spec.reads is reads
    assert spec.writes is writes


def test_inout_is_both_not_either():
    """The case the string comparison gets wrong."""
    spec = AIERuntimeArgSpec("inout", (16,))
    assert spec.reads and spec.writes


def test_invalid_direction_is_rejected():
    with pytest.raises(ValueError, match="Invalid direction"):
        AIERuntimeArgSpec("sideways", (16,))


@pytest.mark.parametrize(
    "dtype, itemsize", [(bfloat16, 2), (np.float32, 4), (np.int8, 1)]
)
def test_nbytes_follows_dtype(dtype, itemsize):
    assert AIERuntimeArgSpec("in", (4, 8), dtype=dtype).nbytes() == 4 * 8 * itemsize


def test_nbytes_of_a_scalar_shape():
    """An empty shape is one element, not zero bytes."""
    assert AIERuntimeArgSpec("in", (), dtype=np.float32).nbytes() == 4


def test_same_shape_unary_from_an_int():
    specs = same_shape_unary(1024)
    assert [s.direction for s in specs] == ["in", "out"]
    assert all(s.shape == (1024,) for s in specs)


def test_same_shape_unary_from_a_tuple():
    """Multi-dimensional shapes pass through unchanged.

    Transpose relies on this: it declares a flat ``(M*N,)`` buffer, optionally
    with a leading batch dimension, and the helper must not flatten or reorder
    what it is handed.
    """
    specs = same_shape_unary((4, 1024))
    assert all(s.shape == (4, 1024) for s in specs)


def test_same_shape_binary_shapes_and_directions():
    specs = same_shape_binary(256)
    assert [s.direction for s in specs] == ["in", "in", "out"]
    assert all(s.shape == (256,) for s in specs)


@pytest.mark.parametrize("helper", [same_shape_unary, same_shape_binary])
def test_helpers_default_to_bfloat16(helper):
    assert all(s.dtype is bfloat16 for s in helper(64))


@pytest.mark.parametrize("helper", [same_shape_unary, same_shape_binary])
def test_helpers_propagate_dtype(helper):
    """A helper that dropped the dtype would silently hand back the default.

    That is the bug arg_spec_dtype.py already guards for hand-written specs;
    routing operators through a shared helper must not reintroduce it.
    """
    specs = helper(64, dtype=np.float32)
    assert all(s.dtype is np.float32 for s in specs)
    assert all(s.nbytes() == 64 * 4 for s in specs)
