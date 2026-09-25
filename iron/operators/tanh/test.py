#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
from aie.utils.verify import Tolerance

from iron.operators.tanh.op import Tanh
from iron.operators.tanh.reference import generate_inputs
from iron.common.test_utils import (
    assert_matches_reference,
    make_channeled_unary_params,
)


def get_params():
    return [
        pytest.param(il, nac, nc, ts, marks=[] if not ext else [pytest.mark.extensive])
        for il, nac, nc, ts, ext in make_channeled_unary_params(
            [1024, 2048, 4096, 8192], 4096, [1, 2]
        )
    ]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_aie_columns,num_channels,tile_size",
    get_params(),
)
def test_tanh(input_length, num_aie_columns, num_channels, tile_size, aie_context):
    x = generate_inputs(input_length=input_length)

    operator = Tanh(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        context=aie_context,
    )

    # The torch reference at this test's tolerance, tighter than the kernel
    # contract's.
    assert_matches_reference(operator, x, tolerance=Tolerance.relative(0.04, 1e-6))
