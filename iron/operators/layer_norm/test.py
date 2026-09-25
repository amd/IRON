#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
from aie.utils.verify import Tolerance

from iron.operators.layer_norm.op import LayerNorm
from iron.operators.layer_norm.reference import generate_inputs
from iron.common.test_utils import (
    assert_matches_reference,
    make_channeled_unary_params,
)


def get_params():
    return [
        pytest.param(il, nac, nc, ts, marks=[] if not ext else [pytest.mark.extensive])
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
def test_layer_norm(
    input_length, num_aie_columns, num_channels, tile_size, aie_context
):
    x = generate_inputs(rows=input_length // tile_size, cols=tile_size)

    operator = LayerNorm(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        context=aie_context,
    )

    assert_matches_reference(
        operator,
        x,
        # The tighter of this test's former rel_tol (0.1) and the kernel
        # contract's atol (0.05).
        tolerance=Tolerance.relative(0.1, 0.05),
    )
