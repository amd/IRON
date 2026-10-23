# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.Conv2d on a device, at EmbeddingGemma 2's subsampling shapes
and two depthwise ones, the second's 13 output rows not whole GEMM row
blocks: one compile each, called at two row counts, every output row the
call computes held to its reference (the convolution, as
``iron/tests/common/test_conv2d_graph.py`` judges it against torch's) within its
GEMM's bound, 2 units of 2^-8 of the convolution of |x| by |weight|.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.lm import Conv2d

pytestmark = pytest.mark.supported_devices("npu1", "npu2")

# (out, channels_per_group) channels, input rows, pixels a row, and the
# convolution's own; ``groups`` (depthwise only) gives the true input
# channel count, else it is ``channels_per_group``.
SHAPES = {
    "band": ((128, 1), 3074, 128, dict(stride=2, padding=1, border=1)),
    "patches": ((32, 128), 1538, 66, dict(stride=2)),
    "depthwise": ((64, 1), 514, 64, dict(stride=2, groups=64)),
    "depthwise_13_rows": ((64, 1), 27, 26, dict(stride=2, padding=1, groups=64)),
}


@pytest.fixture(scope="module", params=list(SHAPES))
def case(request):
    (out, channels_per_group), rows, width, kwargs = SHAPES[request.param]
    in_channels = kwargs.get("groups", channels_per_group)
    rng = np.random.default_rng(0)
    weight = rng.standard_normal((out, channels_per_group, 3, 3)).astype(bfloat16)
    conv = Conv2d(weight, width, **kwargs)
    conv.compile(x=((rows, width * in_channels), bfloat16))
    x = rng.standard_normal((rows, width * in_channels)).astype(bfloat16)
    # Every output row on the host, each call's rows the first of them.
    out_rows = (rows - 3) // 2 + 1
    want = np.asarray(conv.reference(x, rows=out_rows), np.float32)
    magnitude = Conv2d(np.abs(weight.astype(np.float32)), width, **kwargs)
    bound = 2.0**-7 * np.asarray(magnitude.reference(np.abs(x), rows=out_rows))
    yield conv, x, want, bound.astype(np.float32)


@pytest.mark.parametrize("share", [0.25, 1.0])
def test_conv2d(case, share):
    conv, x, want, bound = case
    rows = int(len(want) * share)
    got = conv(x, rows=rows).numpy().reshape(-1, conv.out_line)[:rows]
    assert (np.abs(got.astype(np.float32) - want[:rows]) <= bound[:rows]).all()
