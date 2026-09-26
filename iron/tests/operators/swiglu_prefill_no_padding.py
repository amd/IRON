#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""swiglu_prefill does not pad: a seq_len its inner GEMM cannot tile is an
error at trace time, and an aligned one traces with the extents it was given.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.operators.gemm.op import GEMM
from iron.operators.swiglu_prefill.op import swiglu_prefill

pytestmark = pytest.mark.usefixtures("npu2")


def _trace(seq_len, embedding_dim=2048, hidden_dim=2048):
    z = lambda *s: np.zeros(s, dtype=bfloat16)  # noqa: E731
    ffn = swiglu_prefill(
        z(embedding_dim, hidden_dim),
        z(embedding_dim, hidden_dim),
        z(hidden_dim, embedding_dim),
    )
    return ffn.trace(x=(seq_len, embedding_dim))


def test_non_aligned_seq_len_raises_instead_of_being_padded():
    with pytest.raises(ValueError, match=r"M \(300\) must be a multiple of 256"):
        _trace(seq_len=300)


def test_aligned_seq_len_traces_with_the_given_extents():
    t = _trace(seq_len=512)
    gemms = [s.op for s in t.steps if type(s.op) is GEMM]
    assert [(g.M, g.K, g.N) for g in gemms] == [
        (512, 2048, 2048),
        (512, 2048, 2048),
        (512, 2048, 2048),
    ]
    assert gemms[0].array_key() == gemms[1].array_key()  # gate and up share one array
