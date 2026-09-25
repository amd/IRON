# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import torch

from iron.operators.axpy.reference import reference


@pytest.mark.parametrize("scalar", [1.003, -1.003])
def test_reference_rounds_scalar_to_bf16(scalar):
    x = torch.tensor([1.0], dtype=torch.bfloat16)
    y = torch.tensor([-1.0 if scalar > 0 else 1.0], dtype=torch.bfloat16)

    unrounded = (torch.tensor(scalar, dtype=torch.float32) + y.float()).to(x.dtype)
    actual = reference(x, y, scalar)

    assert unrounded.item() != 0.0
    assert actual.dtype == x.dtype
    assert torch.equal(actual, torch.zeros_like(x))


def test_reference_does_not_round_intermediate_product():
    x = torch.tensor([1.0078125], dtype=torch.bfloat16)
    y = torch.tensor([-1.015625], dtype=torch.bfloat16)

    actual = reference(x, y, 1.0078125)

    assert torch.equal(actual, torch.tensor([2**-14], dtype=torch.bfloat16))
