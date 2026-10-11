#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.Conv1d on a device, at Whisper-large-v3-turbo's own encoder
front-end shapes: one compile each, called at two row counts, every output
row the call computes held to the float32 convolution within its GEMM's
bound, 2 units of 2^-8 of the convolution of |x| by |weight|.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.lm import Conv1d

pytestmark = pytest.mark.supported_devices("npu1", "npu2")

# (out, in) channels, kernel, stride, and input rows giving a 32-row-aligned
# output: Whisper's conv1 (padding folded into the input the caller holds)
# and conv2, padded from 1500 to the next 32-row block GEMM's tiling needs.
SHAPES = {
    "conv1": ((1280, 128), 3, 1, 1058),  # 1056 out rows
    "conv2": ((1280, 1280), 3, 2, 1059),  # 529 out rows -> pad to 544 by the caller
}


@pytest.fixture(scope="module", params=list(SHAPES))
def case(request, module_npu_runtime):
    (out, channels), kernel, stride, rows = SHAPES[request.param]
    rng = np.random.default_rng(0)
    weight = (rng.standard_normal((out, channels, kernel)) * 0.1).astype(bfloat16)
    bias = (rng.standard_normal((out,)) * 0.1).astype(bfloat16)
    conv = Conv1d(weight, bias, channels=channels, stride=stride)
    conv.compile(x=((rows, channels), bfloat16))
    x = rng.standard_normal((rows, channels)).astype(bfloat16)
    yield conv, weight.astype(np.float32), bias.astype(np.float32), x


@pytest.mark.parametrize("share", [0.25, 1.0])
def test_conv1d(case, share):
    conv, weight, bias, x = case
    out_rows = (x.shape[0] - conv.kernel) // conv.stride + 1
    rows = max(1, int(out_rows * share))
    got = conv(x, rows=rows).numpy().reshape(out_rows, conv.out_channels)[:rows]
    want = conv.exact(x, weight, bias)[:rows]
    # Two roundings (the GEMM's, then RowwiseAdd's own): a looser bound than
    # Conv2d's single-rounding 2^-7, not yet measured on real hardware.
    bound = (
        2.0**-6
        * conv.exact(np.abs(x.astype(np.float32)), np.abs(weight), np.abs(bias))[:rows]
    )
    assert (np.abs(got.astype(np.float32) - want) <= bound).all()
