#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from iron.common.test_utils import channeled_unary_cases, operator_test
from iron.operators.tanh.op import Tanh

test_tanh = operator_test(Tanh, channeled_unary_cases([1024, 2048, 4096, 8192], 4096))
