#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.common.test_utils import operator_test
from iron.operators.transpose.op import Transpose


def cases():
    max_aie_columns = aie_utils.get_current_device().cols
    m = n = 64
    out = []
    for M in (64, 2048):
        for N in (64, 128, 256, 512):
            for cols in range(1, max_aie_columns + 1):
                for channels in (1, 2):
                    if (M // channels) % m or (N // cols) % n:
                        continue
                    if (M // channels) * (N // cols) * channels * cols != M * N:
                        continue
                    out.append(
                        pytest.param(
                            dict(
                                M=M,
                                N=N,
                                num_aie_columns=cols,
                                num_channels=channels,
                                m=m,
                                n=n,
                                s=8,
                                num_batches=1,
                            ),
                            marks=(
                                [] if (M, N) == (2048, 64) else [pytest.mark.extensive]
                            ),
                        )
                    )
    # num_batches > 1: independent same-shape transposes in one dispatch, on
    # the regular shape; two batches in the default suite, four extensive.
    for nb in (2, 4):
        out.append(
            pytest.param(
                dict(
                    M=2048,
                    N=64,
                    num_aie_columns=1,
                    num_channels=1,
                    m=m,
                    n=n,
                    s=8,
                    num_batches=nb,
                ),
                marks=[] if nb == 2 else [pytest.mark.extensive],
            )
        )
    return out


# A transpose is a permutation. Any tolerance here also accepts some class of
# wrong permutation, so gate it exactly.
test_transpose = operator_test(Transpose, cases(), rel_tol=0.0, abs_tol=0.0)
