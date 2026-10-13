#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.ConcatChannels on a device, at two to four inputs: one compile
each, its output exactly numpy's concatenation along the channels.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.lm import ConcatChannels

pytestmark = pytest.mark.supported_devices("npu1", "npu2")

ROWS, WIDTH = 13, 13


@pytest.mark.parametrize("channels", [(128, 128), (64, 32, 64), (4, 4, 4, 4)])
def test_concat_channels(channels, module_npu_runtime):
    rng = np.random.default_rng(0)
    xs = [rng.standard_normal((ROWS, WIDTH * c)).astype(bfloat16) for c in channels]
    cat = ConcatChannels(rows=ROWS, width=WIDTH, channels=channels)
    cat.compile(**{f"x{i}": (x.shape, bfloat16) for i, x in enumerate(xs)})
    got = np.asarray(cat(*xs).numpy()).reshape(ROWS, -1)
    want = np.concatenate(
        [x.reshape(ROWS, WIDTH, c) for x, c in zip(xs, channels)], axis=-1
    ).reshape(ROWS, -1)
    assert np.array_equal(got, want)
