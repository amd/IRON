# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Bounded reductions ignore the inactive capacity suffix."""

import numpy as np
import pytest

from iron.operators.reduce_max import ReduceMax


@pytest.mark.parametrize("valid, expected", [(1024, 3.0), (2048, 100.0)])
def test_reference_reduces_only_valid_prefix(npu2, valid, expected):
    op = ReduceMax(size=2048, tile_size=1024).resolved(npu2)
    x = np.full(2048, 3.0, np.float32)
    x[1024:] = 100.0
    result = op._call_reference({"x": x}, values={"valid": valid})
    np.testing.assert_array_equal(result["y"], [expected])
    if valid == op.size:
        np.testing.assert_array_equal(op.reference(x), [expected])
