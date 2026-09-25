#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
from aie.utils.verify import Tolerance

from iron.operators.gelu.op import GELU
from iron.operators.gelu.reference import generate_inputs
from iron.common.test_utils import (
    assert_matches_reference,
    make_channeled_unary_params,
)


def get_params():
    def _marks(ext):
        return [pytest.mark.extensive] if ext else []

    return [
        pytest.param(il, nac, nc, ts, marks=_marks(ext))
        for il, nac, nc, ts, ext in make_channeled_unary_params(
            [1024, 2048, 4096, 8192], 8192, [1, 2]
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
def test_gelu(input_length, num_aie_columns, num_channels, tile_size, aie_context):
    x = generate_inputs(input_length=input_length)

    operator = GELU(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        context=aie_context,
    )

    # The torch reference at this test's tolerance, tighter than the kernel
    # contract's.
    assert_matches_reference(operator, x, tolerance=Tolerance.relative(0.04, 1e-6))
