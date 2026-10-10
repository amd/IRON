#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SwiGLU does not pad: a row count its inner GEMM cannot tile is an error
at trace time, and an aligned one traces with the extents it was given.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.lm.layers import SwiGLU
from iron.operators.flm.gemm.op import GEMM as FLMGEMM

pytestmark = pytest.mark.usefixtures("npu2")


def _trace(rows, embedding_dim=2048, hidden_dim=2048):
    z = lambda *s: np.zeros(s, dtype=bfloat16)
    ffn = SwiGLU(
        z(hidden_dim, embedding_dim),
        z(hidden_dim, embedding_dim),
        z(embedding_dim, hidden_dim),
    )
    return ffn.trace(x=(rows, embedding_dim))


def test_non_aligned_row_count_raises_instead_of_being_padded():
    with pytest.raises(ValueError, match=r"M \(300\) must be a multiple of 256"):
        _trace(rows=300)


def test_aligned_row_count_traces_with_the_given_extents():
    t = _trace(rows=512)
    gemms = [s.op for s in t.steps if type(s.op) is FLMGEMM]
    assert [(g.M, g.K, g.N) for g in gemms] == [
        (512, 2048, 2048),
        (512, 2048, 2048),
        (512, 2048, 2048),
    ]
    assert gemms[0].array_key() == gemms[1].array_key()  # gate and up share one array
