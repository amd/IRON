#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A transposing Copy on several channels, on a device, against numpy.

The channels split the innermost axis of both sides; the output a copy
defaults to is rows as wide as its source's, so each channel's share of a
row lands in that row.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.operators.copy import Copy

N, G, D = 64, 8, 64

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
