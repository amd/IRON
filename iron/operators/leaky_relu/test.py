#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.operators.leaky_relu.op import LeakyReLU
from iron.operators.leaky_relu.reference import generate_inputs
from iron.common.test_utils import (
    assert_matches_reference,
    make_channeled_unary_params,
)


def get_params():
    # Full shape sweep at the default alpha.
    params = [
        pytest.param(
            il, nac, nc, ts, 0.01, marks=[] if not ext else [pytest.mark.extensive]
        )
        for il, nac, nc, ts, ext in make_channeled_unary_params(
            [1024, 2048, 4096, 8192], 4096, [1, 2]
        )
    ]
    # Exercise additional alpha values on a small, device-independent shape so
    # the (non-extensive) suite verifies that alpha is actually plumbed through
    # to the kernel and honored, rather than ignored or hardcoded.
    params += [pytest.param(2048, 1, 1, 2048, alpha, marks=[]) for alpha in (0.1, 0.25)]
    return params


@pytest.mark.parametrize(
    "input_length,num_aie_columns,num_channels,tile_size,alpha", get_params()
)
@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
def test_leaky_relu(
    input_length, num_aie_columns, num_channels, tile_size, alpha, aie_context
):
    x = generate_inputs(input_length=input_length)

    operator = LeakyReLU(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        alpha=alpha,
        context=aie_context,
    )

    assert_matches_reference(operator, x)
