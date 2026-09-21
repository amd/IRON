#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import torch
import aie.utils as aie_utils

from iron.common.test_utils import operator_test
from iron.operators.dequant.op import Dequant


def cases():
    max_aie_columns = aie_utils.get_current_device().cols
    out = []
    for size in [1024, 2048, 4096, 8192]:
        for cols in range(1, max_aie_columns + 1):
            for channels in (1, 2):
                tile_size = min(size // (cols * channels), 16384)
                if tile_size * cols * channels != size:
                    continue
                out.append(
                    pytest.param(
                        dict(
                            size=size,
                            num_aie_columns=cols,
                            num_channels=channels,
                            tile_size=tile_size,
                            group_size=32,
                        ),
                        marks=[] if size == 2048 else [pytest.mark.extensive],
                    )
                )
    return out


def packed(op):
    """Values in [0, 3.75) with scales in [1/3.75, 1) keep every quantized
    value inside int4's [0, 15]; the input is their packed form."""
    torch.manual_seed(42)
    values = torch.rand(op.size, dtype=torch.bfloat16) * 3.75
    scales = 1 / 3.75 + (1 - 1 / 3.75) * torch.rand(
        op.size // op.ov.group_size, dtype=torch.bfloat16
    )
    return dict(x=op.pack(values, scales))


test_dequant = operator_test(Dequant, cases(), rel_tol=0.01, draw=packed)
