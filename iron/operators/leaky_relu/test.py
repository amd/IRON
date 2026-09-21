#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.common.test_utils import channeled_unary_cases, operator_test
from iron.operators.leaky_relu.op import LeakyReLU

# The shape sweep at the default alpha, then two more alphas on one small
# shape in the default suite, so that alpha is seen to reach the kernel.
CASES = channeled_unary_cases([1024, 2048, 4096, 8192], 4096, alpha=0.01) + [
    pytest.param(
        dict(size=2048, num_aie_columns=1, num_channels=1, tile_size=2048, alpha=a)
    )
    for a in (0.1, 0.25)
]

test_leaky_relu = operator_test(LeakyReLU, CASES, draw=dict(centered=("x",)))
