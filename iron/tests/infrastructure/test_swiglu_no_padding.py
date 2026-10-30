# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A gated feed-forward does not pad.

A row count its inner GEMM cannot tile is an error at record time, and
an aligned one records with the extents it was given.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.operators.flm.gemm.op import ProjectionGEMM
from iron.tests.support.graphs import FeedForward

pytestmark = pytest.mark.usefixtures("npu2")


def _trace(rows, embedding_dim=2048, hidden_dim=2048):
    ffn = FeedForward(
        np.zeros((hidden_dim, embedding_dim), dtype=bfloat16),
        np.zeros((hidden_dim, embedding_dim), dtype=bfloat16),
        np.zeros((embedding_dim, hidden_dim), dtype=bfloat16),
    )
    return ffn.record(x=(rows, embedding_dim))


def test_non_aligned_row_count_raises_instead_of_being_padded():
    with pytest.raises(ValueError, match=r"M \(300\) must be a multiple of 256"):
        _trace(rows=300)


def test_aligned_row_count_records_with_the_given_extents():
    t = _trace(rows=512)
    gemms = [s.op for s in t.steps if type(s.op) is ProjectionGEMM]
    assert [(g.M, g.K, g.N) for g in gemms] == [
        (512, 2048, 2048),
        (512, 2048, 2048),
        (512, 2048, 2048),
    ]
    assert gemms[0].array_key() == gemms[1].array_key()  # gate and up share one array
