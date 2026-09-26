# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.operators.axpy import AXPY


def _reference(x, y, scalar):
    return AXPY(size=x.size, scalar_factor=scalar).reference(x, y)


@pytest.mark.parametrize("scalar", [1.003, -1.003])
def test_reference_rounds_scalar_to_bf16(scalar):
    x = np.array([1.0], dtype=bfloat16)
    y = np.array([-1.0 if scalar > 0 else 1.0], dtype=bfloat16)

    unrounded = (np.float32(scalar) + y.astype(np.float32)).astype(bfloat16)
    actual = _reference(x, y, scalar)

    assert unrounded.item() != 0.0
    assert actual.dtype == x.dtype
    np.testing.assert_array_equal(actual, np.zeros_like(x))


def test_reference_does_not_round_intermediate_product():
    x = np.array([1.0078125], dtype=bfloat16)
    y = np.array([-1.015625], dtype=bfloat16)

    actual = _reference(x, y, 1.0078125)

    np.testing.assert_array_equal(actual, np.array([2**-14], dtype=bfloat16))
