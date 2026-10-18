#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils.verify import Tolerance

from iron.common.testing import run_test, vectors
from iron.operators.flm.lm_head.op import LMHead

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.mark.parametrize("dim", [1536, 2560])
def test_projection_matches_reference(dim):
    """A softcap of 1000 keeps each tanh argument near zero, so the
    projection's bound alone holds.

    1536 and 2560 are Gemma 4 E2B's and E4B's hidden sizes.
    """
    op = LMHead(dim=dim, vocab=4096, softcap=1000.0)
    errors = run_test(
        op,
        vectors(op, **op.test.draw(op)),
        tolerance=Tolerance(bound=op.projection_error),
    )
    assert not errors, errors


def test_softcap_bounds_the_logits():
    """A softcap of 5 saturates most logits. No logit may exceed the softcap."""
    op = LMHead(dim=1536, vocab=1024, softcap=5.0)
    v = vectors(op, **op.test.draw(op))
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    y, w, x = (
        tensor(v[b.name]) if b.fills else tensor(b.host_shape, dtype=b.host_dtype)
        for b in op.buffers
    )
    op(y, w, x)
    assert np.abs(y.numpy().astype(np.float64)).max() <= 5.0
