# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
from aie.utils.verify import Tolerance

from iron.common.testing import run_test, vectors
from iron.operators.flm.lm_head.op import LMHead


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("dim", [1536, 2560])
def test_projection_matches_reference(dim):
    """A softcap of 1000 keeps each tanh argument near zero, so the
    projection's bound alone holds; 1536 and 2560 are Gemma 4 E2B's and
    E4B's hidden sizes.
    """
    op = LMHead(dim=dim, vocab=4096, softcap=1000.0)
    errors = run_test(
        op,
        vectors(op, **op.test.draw(op)),
        tolerance=Tolerance.bounded(op.projection_error),
    )
    assert not errors, errors
