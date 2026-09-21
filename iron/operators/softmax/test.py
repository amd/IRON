#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils

from iron.common.test_utils import operator_test
from iron.operators.softmax.op import Softmax


def columns_channels(total_cores):
    """The (columns, channels) split for a core count: 2x2 from four cores up
    (a 4x4 has placement issues on Phoenix), 1x2 for two, 1x1 for one."""
    return {1: (1, 1), 2: (1, 2)}.get(total_cores, (2, 2))


def cases():
    max_aie_columns = aie_utils.get_current_device().cols
    out = []
    for size, cols in [(32768, 1024), (32768, 512), (32768, 2048)]:
        columns, channels = columns_channels(size // cols)
        if columns > max_aie_columns:
            continue
        out.append(
            dict(
                rows=size // cols,
                cols=cols,
                num_aie_columns=columns,
                num_channels=channels,
            )
        )
    return out


test_softmax = operator_test(Softmax, cases())
