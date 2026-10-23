# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.Conv2d device-free: its reference, its operators', is torch's
convolution in each of its forms (recorded in ``goldens/conv2d.npz``), a
caller's per-call rows bound it, and it refuses padding gathered patches do
not hold; and ``F.conv2d`` of a feature map in each of its forms.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
import iron.functional as F
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
    """torch's convolution of ``x`` by ``weight`` in float32, bordered, as
    ``conv`` lays its output out, rounded once to bfloat16 as the graph
    rounds it: ``logits``, as ``Golden`` reads it.
    """

    def __init__(self, conv: Conv2d, groups: int):
        self.conv, self.groups = conv, groups

    def logits(self, tokens, x, weight):
        import torch

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


# A 6 by 10 map: a 1x1 of pixels not whole row blocks, a depthwise 3x3 at
# stride 2 and a dense one, each inside a zero pixel a side.
MAPS = {
    "pointwise": ((64, 128, 1, 1), 128, dict()),
    "depthwise": ((32, 1, 3, 3), 32, dict(stride=2, padding=1, groups=32)),
    "dense": ((16, 64, 3, 3), 64, dict(padding=1)),
}


@pytest.mark.parametrize("case", list(MAPS))
def test_functional_conv2d_is_the_convolution(case):
    """Within its GEMM's bound, 2 units of 2^-8 of the convolution of |x| by
    |weight| plus |bias|.
    """
    shape, channels, kwargs = MAPS[case]
    stride, padding = kwargs.get("stride", 1), kwargs.get("padding", 0)
    groups = kwargs.get("groups", 1)
    rng = np.random.default_rng(0)
    weight = rng.standard_normal(shape).astype(bfloat16)
    bias = rng.standard_normal(shape[0]).astype(bfloat16)
    x = rng.standard_normal((6, 10, channels)).astype(bfloat16)

    class Map(iron.Graph):
        def body(self, x):
            return Copy.step(F.conv2d(x, weight, bias, **kwargs))

    def convolution(x, w, b):
        k = w.shape[-1]
        image = np.pad(x, ((padding, padding), (padding, padding), (0, 0)))
        windows = np.lib.stride_tricks.sliding_window_view(image, (k, k), (0, 1))
        windows = windows[::stride, ::stride]
        if groups > 1:
            return np.einsum("hwckl,ckl->hwc", windows, w[:, 0]) + b
        return np.einsum("hwckl,ockl->hwo", windows, w) + b

    f = [np.asarray(a, np.float32) for a in (x, weight, bias)]
    want = convolution(*f)
    bound = 2.0**-7 * convolution(*(np.abs(a) for a in f))
    got = np.asarray(Map().reference(x), np.float32).reshape(want.shape)
    assert (np.abs(got - want) <= bound).all()


class Apply(iron.Graph):
    def __init__(self, f):
        self.f = f

    def body(self, x):
        return self.f(x)


# A map's shape, the weight's, the keywords, and what the refusal says.
REFUSED = {
    "rank": ((6, 80), (16, 8, 3, 3), {}, "not a map"),
    "channels": ((6, 10, 8), (16, 4, 3, 3), {}, "8 channels"),
    "kernel": ((6, 10, 8), (16, 8, 1, 3), {}, "1x3"),
    "dilation": ((6, 10, 8), (16, 8, 3, 3), dict(dilation=2), "dilation 2"),
}


@pytest.mark.parametrize("case", list(REFUSED))
def test_functional_conv2d_refuses_what_it_does_not_compute(case):
    x, shape, kwargs, match = REFUSED[case]
    weight = np.zeros(shape, bfloat16)
    with pytest.raises(ValueError, match=match):
        Apply(lambda x: F.conv2d(x, weight, **kwargs)).record(x=(x, bfloat16))
