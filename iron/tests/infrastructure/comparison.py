#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the tolerances in verify_buffer are required to mean.

An operator that does no arithmetic (transpose, mem_copy) should be gated on exact
equality, not on a tolerance that would also accept a wrong answer. That is
rel_tol=abs_tol=0, so the zero case has to behave -- and it is the case a
threshold comparison is easiest to get backwards, since the threshold is then the
same value as the difference between two identical buffers.
"""

import numpy as np
import pytest
import torch

from iron.common.test_utils import verify_buffer


@pytest.mark.parametrize("dtype", [torch.float32, torch.bfloat16])
def test_zero_tolerance_accepts_an_identical_buffer(dtype):
    buf = (torch.arange(64, dtype=torch.float32) / 8).to(dtype)

    assert verify_buffer(buf, "out", buf.clone(), rel_tol=0.0, abs_tol=0.0) == []


@pytest.mark.parametrize("rel_tol,abs_tol", [(0.0, 0.0), (0.04, 1e-6)])
def test_a_single_wrong_element_is_reported_alone(rel_tol, abs_tol):
    reference = torch.arange(64, dtype=torch.float32)
    output = reference.clone()
    output[
        17
    ] += 10.0  # past the 4% relative tolerance at this magnitude, not just past 0

    assert verify_buffer(output, "out", reference, rel_tol, abs_tol) == [17]


def test_zero_tolerance_still_rejects_a_one_ulp_error():
    """The point of the zero case is that it is exact, not that it is lenient."""
    reference = torch.full((32,), 1.0, dtype=torch.float32)
    output = reference.clone()
    output[5] = float(np.nextafter(np.float32(1.0), np.float32(2.0)))

    assert verify_buffer(output, "out", reference, rel_tol=0.0, abs_tol=0.0) == [5]
    # The default tolerance is meant to absorb exactly this.
    assert verify_buffer(output, "out", reference) == []
