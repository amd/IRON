#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from iron.common.test_utils import channeled_unary_cases, operator_test
from iron.operators.relu.op import ReLU

test_relu = operator_test(
    ReLU,
    channeled_unary_cases([1024, 2048, 4096, 8192], 4096),
    draw=dict(centered=("x",)),  # both signs
)
