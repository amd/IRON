#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.common.test_utils import operator_test
from iron.operators.mem_copy.op import MemCopy


def cases():
    max_columns = aie_utils.get_current_device().cols
    out = []
    for size in [1024, 2048, 4096, 8192]:
        for num_cores in range(1, max_columns * 2 + 1):
            for channels in (1, 2):
                # A channel needs at least one core, and a core a shim channel.
                if not channels <= num_cores <= max_columns * channels:
                    continue
                for bypass in (False, True):
                    tile_size = min(size // num_cores, 8192)
                    if tile_size * num_cores != size:
                        continue
                    out.append(
                        pytest.param(
                            dict(
                                size=size,
                                num_cores=num_cores,
                                num_channels=channels,
                                bypass=bypass,
                                tile_size=tile_size,
                            ),
                            marks=(
                                []
                                if size == 2048 and not bypass
                                else [pytest.mark.extensive]
                            ),
                        )
                    )
    return out


# A copy that alters a value is a broken copy, so gate it exactly.
test_mem_copy = operator_test(MemCopy, cases(), rel_tol=0.0, abs_tol=0.0)
