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

Shapes themselves are declared on each operator (``In``/``Out`` members in
:mod:`iron.common.declare`); only the vocabulary is pinned here.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common import AIERuntimeArgSpec


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
