#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.common.test_utils import operator_test
from iron.operators.axpy.op import AXPY


def cases():
    max_aie_columns = aie_utils.get_current_device().cols
    out = []
    for size in [1024, 2048, 4096, 8192]:
        for cols in range(1, max_aie_columns + 1):
            tile_size = size // cols
            if tile_size * cols != size:
                continue
            for scalar in (3.0, 10.0):
                regular = size == 2048 and scalar == 3.0
                out.append(
                    pytest.param(
                        dict(
                            size=size,
                            num_aie_columns=cols,
                            tile_size=tile_size,
                            scalar_factor=scalar,
                        ),
                        marks=[] if regular else [pytest.mark.extensive],
                    )
                )
    return out


test_axpy = operator_test(AXPY, cases())
