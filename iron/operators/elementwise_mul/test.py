#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from iron.common.test_utils import binary_elementwise_cases, operator_test
from iron.operators.elementwise_mul.op import ElementwiseMul

test_elementwise_mul = operator_test(
    ElementwiseMul, binary_elementwise_cases([1024, 2048, 4096, 8192], 4096)
)
