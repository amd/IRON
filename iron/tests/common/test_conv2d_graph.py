# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.Conv2d device-free.

Its reference, its operators', is torch's convolution in each of its
forms (recorded in ``goldens/conv2d.npz``), a caller's per-call rows
bound it, and it refuses padding gathered patches do not hold.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.lm import Conv2d
from iron.operators.copy import Copy
from iron.operators.gemm import GEMM
from iron.operators.relu import ReLU

pytestmark = pytest.mark.usefixtures("npu2")

# EmbeddingGemma 2's subsampling convolutions at a few of their rows:
# one channel to 128 as a band over half the width, padded and bordered,
# and 128 to 32 by gathered patches; and a depthwise one, every output
# channel its own input channel, at stride 2, its 13 output rows not whole
# GEMM row blocks.
CASES = {
    "band": ((128, 1), 34, 64, dict(stride=2, padding=1, border=1)),
    "patches": ((32, 128), 66, 18, dict(stride=2)),
    "depthwise": ((16, 1), 34, 16, dict(stride=2, groups=16)),
    "depthwise_13_rows": ((64, 1), 27, 26, dict(stride=2, padding=1, groups=64)),
}


def draw(case):
    (out, channels), rows, width, kwargs = CASES[case]
    in_channels = kwargs.get("groups", channels)
    rng = np.random.default_rng(0)
    weight = rng.standard_normal((out, channels, 3, 3)).astype(np.float32)
    x = rng.standard_normal((rows, width * in_channels)).astype(bfloat16)
    return Conv2d(weight, width, **kwargs), weight, x


class Convolution:
    """torch's convolution of ``x`` by ``weight`` in float32, bordered.

    As ``conv`` lays its output out, rounded once to bfloat16 as the
    graph rounds it: ``logits``, as ``Golden`` reads it.
    """

    def __init__(self, conv: Conv2d, groups: int):
        self.conv, self.groups = conv, groups

    def logits(self, tokens, x, weight):
        import torch  # records a golden only: not a requirement

        c = self.conv
        image = np.asarray(x, np.float32).reshape(-1, c.width, c.channels)
        out = torch.nn.functional.conv2d(
            torch.from_numpy(image.transpose(2, 0, 1).copy())[None],
            torch.from_numpy(weight.astype(np.float32)),
            stride=c.stride,
            padding=(0, c.padding),
            groups=self.groups,
        )
        out = out[0].numpy().transpose(1, 2, 0)
        out = np.pad(out, ((0, 0), (c.border, c.border), (0, 0)))
        return out.reshape(out.shape[0], c.out_line).astype(bfloat16)


@pytest.mark.parametrize("case", list(CASES))
def test_the_reference_is_the_convolution(case, golden):
    """Keyed in ``goldens/conv2d.npz`` by the input and the weight."""
    conv, weight, x = draw(case)
    rows = (x.shape[0] - 3) // 2 + 1
    got = np.asarray(conv.reference(x, rows=rows), np.float32)
    groups = CASES[case][3].get("groups", 1)
    reference = golden("conv2d", lambda: Convolution(conv, groups), CASES)
    want = reference.logits((), x, weight.astype(bfloat16))
    ulp = 2.0 ** (np.floor(np.log2(np.abs(want).clip(1e-30))) - 7)
    assert (np.abs(got - want) <= ulp).all()


class Subsample(iron.Graph):
    def __init__(self, conv: Conv2d):
        self.conv = conv

    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU.step(self.conv(x, rows=n))


def test_a_caller_bounds_its_rows():
    conv, _, x = draw("band")
    recording = Subsample(conv).record(x=(x.shape, bfloat16))
    assert [type(s.op) for s in recording.steps] == [Copy, GEMM, ReLU]
    bound = {type(b.op) for b in recording.bindings if b.expression.value.name == "n"}
    assert ReLU in bound
    assert {h.name for _, h in recording.weights.values()} == {"conv.matrix"}


def test_an_unaligned_gather_computes_whole_blocks():
    conv, _, x = draw("depthwise_13_rows")
    recording = Subsample(conv).record(x=(x.shape, bfloat16))
    gemm = next(s.op for s in recording.steps if isinstance(s.op, GEMM))
    assert gemm.M == 16


class Into(iron.Graph):
    def __init__(self, conv: Conv2d, rows: int):
        self.conv = conv
        self.out = iron.state((rows, conv.out_line))

    def body(self, x, *, n: Scratchpad[np.int32]):
        self.conv(x, self.out, rows=n)


def test_an_unaligned_gather_writes_no_callers_output():
    conv, _, x = draw("depthwise_13_rows")
    with pytest.raises(ValueError, match="not whole 16-row blocks"):
        Into(conv, 13).record(x=(x.shape, bfloat16))


def test_patches_short_of_a_tile_compute_a_whole_one():
    # 3 rows of 8 pixels: 24 patches, 40 more of the first.
    conv = Conv2d(np.zeros((32, 128, 3, 3), np.float32), 18, stride=2)
    x = (7, 18 * 128)
    recording = Subsample(conv).record(x=(x, bfloat16))
    gemm = next(s.op for s in recording.steps if isinstance(s.op, GEMM))
    assert gemm.N == 64
    with pytest.raises(ValueError, match="not whole 64-pixel tiles"):
        Into(conv, 3).record(x=(x, bfloat16))


def test_gathered_patches_hold_no_padding():
    with pytest.raises(ValueError, match="hold no zero padding"):
        Conv2d(np.zeros((32, 128, 3, 3), np.float32), 18, stride=2, padding=1)
