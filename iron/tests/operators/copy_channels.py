#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A transposing Copy on several channels, on a device, against numpy.

The channels split the innermost axis of both sides; the output a copy
defaults to is rows as wide as its source's, so each channel's share of a
row lands in that row.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron.common.image import OperatorImage
from iron.operators.copy import Copy

N, G, D = 64, 8, 64
T, H, W = 64, 4, 256

pytestmark = pytest.mark.usefixtures("npu2")


class _Permute(iron.Graph):
    def __init__(self, channels):
        self.channels = channels

    def body(self, x):
        return Copy(x.reshape(N, G, D).transpose(1, 0, 2), num_channels=self.channels)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("channels", [1, 2, 4])
def test_a_transposing_copy_on_any_channel_count(npu_runtime, channels):
    x = np.random.default_rng(channels).standard_normal((N, G * D)).astype(bfloat16)
    permute = _Permute(channels)
    got = permute(x).numpy().reshape(G, N, D)
    want = x.reshape(N, G, D).transpose(1, 0, 2)
    wrong = np.argwhere(got != want)
    assert not len(wrong), f"{len(wrong)} elements differ, first {wrong[:4]}"


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("channels", [1, 2, 4])
@pytest.mark.parametrize("rows", [T * H * W, T * W], ids=["flat", "head_rows"])
def test_a_transpose_into_wider_rows_on_any_channel_count(npu_runtime, channels, rows):
    """Each element's bits are its index in the source, so a misplaced one
    names where it came from.
    """
    op = Copy(
        src=TensorAccessPattern((T, H, W), 0, [H, T, W], [W, H * W, 1]),
        dst=TensorAccessPattern.full((T * H * W // rows, rows)),
        input_buffer_size=T * H * W,
        num_channels=channels,
    )
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    x = np.arange(T * H * W, dtype=np.uint16).reshape(T, H, W)
    y = tensor(np.full(T * H * W, 0xFFFF, dtype=np.uint16).view(bfloat16))
    OperatorImage(op)(tensor(x.reshape(-1).view(bfloat16)), y)
    got = y.numpy().view(np.uint16).reshape(H, T, W)
    wrong = np.argwhere(got != x.transpose(1, 0, 2))
    assert not len(wrong), f"{len(wrong)} elements differ, first {wrong[:4]}"
