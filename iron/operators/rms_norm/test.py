#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.common.test_utils import operator_test
from iron.common.utils import get_shim_dma_limit
from iron.operators.rms_norm.op import RMSNorm, WeightedRMSNorm


def cases(weighted):
    dev = aie_utils.get_current_device()
    shim_dma_limit = get_shim_dma_limit(dev)
    tile_cap = 4096 if weighted else 8192
    out = []
    for size in [1024, 2048, 4096, 8192]:
        for cols in range(1, dev.cols + 1):
            for channels in (1, 2):
                if cols * channels > shim_dma_limit:
                    continue
                # The weight row is one fifo per channel shared across the
                # columns: the ShimDMA budget is channels * (columns + 1).
                if weighted and channels * (cols + 1) > shim_dma_limit:
                    continue
                tile_size = min(size // (cols * channels), tile_cap)
                if tile_size * cols * channels != size:
                    continue
                out.append(
                    pytest.param(
                        dict(
                            rows=size // tile_size,
                            num_aie_columns=cols,
                            num_channels=channels,
                            tile_size=tile_size,
                        ),
                        marks=[] if size == 2048 else [pytest.mark.extensive],
                    )
                )
    return out


test_rms_norm = operator_test(RMSNorm, cases(weighted=False))
test_weighted_rms_norm = operator_test(WeightedRMSNorm, cases(weighted=True))
