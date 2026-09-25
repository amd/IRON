#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.operators.elementwise_mul.op import ElementwiseMul
from iron.operators.elementwise_mul.reference import generate_inputs
from iron.common.test_utils import (
    assert_matches_reference,
    make_binary_elementwise_params,
)


def get_params():
    return [
        pytest.param(il, nac, ts, marks=[] if not ext else [pytest.mark.extensive])
        for il, nac, ts, ext in make_binary_elementwise_params(
            [1024, 2048, 4096, 8192], 4096
        )
    ]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_aie_columns,tile_size",
    get_params(),
)
def test_elementwise_mul(input_length, num_aie_columns, tile_size, aie_context):
    a, b = generate_inputs(input_length=input_length)

    operator = ElementwiseMul(
        size=input_length,
        tile_size=tile_size,
        num_aie_columns=num_aie_columns,
        context=aie_context,
    )

    assert_matches_reference(operator, a, b)
