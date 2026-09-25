#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
from aie.utils.verify import Tolerance
import aie.utils as aie_utils

from iron.operators.mem_copy.op import MemCopy
from iron.operators.mem_copy.reference import generate_inputs
from iron.common.test_utils import assert_matches_reference


def get_params():
    max_columns = aie_utils.get_current_device().cols

    input_lengths = [1024, 2048, 4096, 8192]
    bypass_modes = [False, True]

    params = []

    for input_length in input_lengths:
        for num_cores in range(1, max_columns * 2 + 1):  # Up to MAX_COLUMNS * 2 cores
            for num_channels in range(1, 3):  # 1 or 2 channels
                for bypass in bypass_modes:
                    # Calculate the maximum cores that can be utilized with 1 or 2 shim channels
                    max_cores = max_columns * num_channels  # MAX_COLUMNS * num_channels

                    if max_cores >= num_cores and num_cores >= num_channels:
                        tile_size = input_length // num_cores

                        # Cap tile_size at 8192
                        if tile_size > 8192:
                            tile_size = 8192

                        # Only proceed if tile_size * num_cores == input_length (exact division)
                        if tile_size * num_cores == input_length:
                            is_regular = input_length == 2048 and bypass == False
                            marks = [] if is_regular else [pytest.mark.extensive]

                            params.append(
                                pytest.param(
                                    input_length,
                                    num_cores,
                                    num_channels,
                                    bypass,
                                    tile_size,
                                    marks=marks,
                                )
                            )

    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_cores,num_channels,bypass,tile_size",
    get_params(),
)
def test_mem_copy(
    input_length, num_cores, num_channels, bypass, tile_size, aie_context
):
    x = generate_inputs(input_length=input_length)

    # num_cores >= num_channels is required: each channel must have at least one core assigned
    operator = MemCopy(
        size=input_length,
        num_cores=num_cores,
        num_channels=num_channels,
        bypass=bypass,
        tile_size=tile_size,
        context=aie_context,
    )

    # A copy that alters a value is a broken copy, so gate it exactly.
    assert_matches_reference(operator, x, tolerance=Tolerance.exact())
