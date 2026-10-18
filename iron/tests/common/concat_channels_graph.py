# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.ConcatChannels device-free: its reference, its operators', is
numpy's concatenation along the channels at each of its arities, and it
refuses what it cannot join; and ``F.cat`` of feature maps.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron.lm import ConcatChannels

pytestmark = pytest.mark.usefixtures("npu2")

ROWS, WIDTH = 5, 7


@pytest.mark.parametrize("channels", [(8, 16), (8, 2, 6), (4, 4, 4, 4)])
def test_the_reference_is_the_concatenation(channels):
    rng = np.random.default_rng(0)
    xs = [rng.standard_normal((ROWS, WIDTH * c)).astype(bfloat16) for c in channels]
    cat = ConcatChannels(rows=ROWS, width=WIDTH, channels=channels)
    want = np.concatenate(
        [x.reshape(ROWS, WIDTH, c) for x, c in zip(xs, channels)], axis=-1
    ).reshape(ROWS, -1)
    assert np.array_equal(np.asarray(cat.reference(*xs)), want)


@pytest.mark.parametrize("channels", [(8,), (2, 2, 2, 2, 2)])
def test_one_or_five_inputs_are_refused(channels):
    with pytest.raises(ValueError, match="two to four"):
        ConcatChannels(rows=ROWS, width=WIDTH, channels=channels)


def test_an_odd_channel_count_is_refused():
    with pytest.raises(ValueError, match="not all even"):
        ConcatChannels(rows=ROWS, width=WIDTH, channels=(4, 3))


def test_the_inputs_given_are_the_inputs_declared():
    cat = ConcatChannels(rows=ROWS, width=WIDTH, channels=(4, 4, 4))
    with pytest.raises(TypeError, match="2 inputs given, 3 declared"):
        cat.trace(x0=((ROWS, WIDTH * 4), bfloat16), x1=((ROWS, WIDTH * 4), bfloat16))


def test_functional_cat_joins_feature_maps_along_their_channels_only():
    rng = np.random.default_rng(0)
    a, b = (rng.standard_normal((ROWS, WIDTH, c)).astype(bfloat16) for c in (8, 2))

    class Cat(iron.Graph):
        def __init__(self, dim):
            self.dim = dim

        def body(self, a, b):
            return F.cat([a, b], self.dim)

    got = np.asarray(Cat(-1).reference(a, b)).reshape(ROWS, WIDTH, 10)
    assert np.array_equal(got, np.concatenate([a, b], -1))
    with pytest.raises(ValueError, match="only the channels"):
        Cat(0).trace(a=(a.shape, bfloat16), b=(b.shape, bfloat16))
