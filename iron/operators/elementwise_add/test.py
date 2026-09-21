#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from iron.common.test_utils import binary_elementwise_cases, operator_test
from iron.operators.elementwise_add.op import ElementwiseAdd

test_elementwise_add = operator_test(
    ElementwiseAdd, binary_elementwise_cases([1024, 2048, 4096, 8192])
)
