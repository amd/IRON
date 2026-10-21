#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOX-Nano from its released checkpoint, on COCO photos: the oracle
finds what the photos hold, and the graph, by its own reference and on the
NPU, detects as the oracle does.
"""

import aie.utils as aie_utils
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import pytest
from ml_dtypes import bfloat16

from iron.applications.yolox.model import (
    BN_EPS,
    INPUT_SIZE,
    POOLS,
    YOLOXNano,
    decode,
    preprocess,
    sigmoid,
)
from iron.lm import Checkpoint
from iron.lm.testing import Download, require, weights_dir


def silu(x):
    return x * sigmoid(x)


def conv2d(x, weight, bias, stride=1, depthwise=False):
    """``x`` ``(H, W, C)`` by ``weight`` ``(out, in / groups, k, k)``, same
    padding, plus ``bias``.
    """
    out_channels, _, k, _ = weight.shape
    pad = (k - 1) // 2
    padded = np.pad(x, ((pad, pad), (pad, pad), (0, 0)))
    windows = sliding_window_view(padded, (k, k), axis=(0, 1))[::stride, ::stride]
    if depthwise:
        out = np.einsum("hwckl,ckl->hwc", windows, weight[:, 0])
    else:
        taps = weight.transpose(1, 2, 3, 0).reshape(-1, out_channels)
        out = windows.reshape(*windows.shape[:2], -1) @ taps
    return out + bias


def max_pool2d(x, kernel):
    """Same-padded max pooling at stride 1, padded with ``-inf``."""
    pad = kernel // 2
    padded = np.pad(x, ((pad, pad), (pad, pad), (0, 0)), constant_values=-np.inf)
    windows = sliding_window_view(padded, (kernel, kernel), axis=(0, 1))
    return windows.max(axis=(-2, -1))


def upsample2x(x):
    """Nearest 2x: each pixel a 2x2 block."""
    return np.repeat(np.repeat(x, 2, axis=0), 2, axis=1)


class YOLOXNanoOracle:
    """YOLOX-Nano's forward pass in float32 on the host, from a
    preprocessed ``(416, 416, 3)`` image to its three scales' predictions,
    ``(52, 52, 85)``, ``(26, 26, 85)`` and ``(13, 13, 85)``, the
    objectness and class scores through their sigmoid.

    Args:
        weights: The checkpoint's ``model`` (``Checkpoint.tree().model``).
    """

    def __init__(self, weights):
        self.weights = weights

    def conv(self, m, x, stride=1, depthwise=False):
        """A ``BaseConv``: the conv, then its BatchNorm, then SiLU."""
        bn = m.bn
        y = conv2d(x, m.conv.weight, 0, stride, depthwise)
        y = (y - bn.running_mean) / np.sqrt(bn.running_var + BN_EPS)
        return silu(y * bn.weight + bn.bias)

    def dwconv(self, m, x, stride=1):
        """A depthwise 3x3 then a pointwise 1x1, each a ``BaseConv``."""
        return self.conv(m.pconv, self.conv(m.dconv, x, stride, depthwise=True))

    def csp(self, m, x, shortcut):
        """A CSP block: its bottlenecks after a 1x1, beside another 1x1,
        joined and projected.
        """
        y = self.conv(m.conv1, x)
        for b in m.m:
            z = self.dwconv(b.conv2, self.conv(b.conv1, y))
            y = z + y if shortcut else z
        return self.conv(m.conv3, np.concatenate([y, self.conv(m.conv2, x)], -1))

    def backbone(self, x):
        """CSPDarknet's dark3, dark4 and dark5."""
        b = self.weights.backbone.backbone
        corners = [x[0::2, 0::2], x[1::2, 0::2], x[0::2, 1::2], x[1::2, 1::2]]
        x = self.conv(b.stem.conv, np.concatenate(corners, -1))
        x = self.csp(b.dark2[1], self.dwconv(b.dark2[0], x, 2), True)
        dark3 = self.csp(b.dark3[1], self.dwconv(b.dark3[0], x, 2), True)
        dark4 = self.csp(b.dark4[1], self.dwconv(b.dark4[0], dark3, 2), True)
        x = self.conv(b.dark5[1].conv1, self.dwconv(b.dark5[0], dark4, 2))
        pooled = [x] + [max_pool2d(x, k) for k in POOLS]
        x = self.conv(b.dark5[1].conv2, np.concatenate(pooled, -1))
        return dark3, dark4, self.csp(b.dark5[2], x, False)

    def neck(self, dark3, dark4, dark5):
        """PAFPN's three outputs, finest first."""
        n = self.weights.backbone
        top0 = self.conv(n.lateral_conv0, dark5)
        x = self.csp(n.C3_p4, np.concatenate([upsample2x(top0), dark4], -1), False)
        top1 = self.conv(n.reduce_conv1, x)
        out3 = self.csp(n.C3_p3, np.concatenate([upsample2x(top1), dark3], -1), False)
        x = np.concatenate([self.dwconv(n.bu_conv2, out3, 2), top1], -1)
        out4 = self.csp(n.C3_n3, x, False)
        x = np.concatenate([self.dwconv(n.bu_conv1, out4, 2), top0], -1)
        return out3, out4, self.csp(n.C3_n4, x, False)

    def head(self, i, x):
        """Scale ``i``'s box, objectness and class scores."""
        h = self.weights.head
        x = self.conv(h.stems[i], x)
        cls, reg = x, x
        for j in range(2):
            cls = self.dwconv(h.cls_convs[i][j], cls)
            reg = self.dwconv(h.reg_convs[i][j], reg)
        box = conv2d(reg, h.reg_preds[i].weight, h.reg_preds[i].bias)
        obj = conv2d(reg, h.obj_preds[i].weight, h.obj_preds[i].bias)
        scores = conv2d(cls, h.cls_preds[i].weight, h.cls_preds[i].bias)
        return np.concatenate([box, sigmoid(obj), sigmoid(scores)], -1)

    def __call__(self, image):
        scales = self.neck(*self.backbone(image))
        return [self.head(i, x) for i, x in enumerate(scales)]


WEIGHTS = weights_dir("yolox-nano") / "yolox_nano.pth"

VAL2017 = "https://s3.amazonaws.com/images.cocodataset.org/val2017"

# COCO val2017 photos, fetched into IRON's cache, and the COCO class each
# holds: two cats on a sofa, and a stop sign.
COCO = {
    "cats": (
        Download(
            f"{VAL2017}/000000039769.jpg",
            "dea9e7ef97386345f7cff32f9055da4982da5471c48d575146c796ab4563b04e",
        ),
        15,
    ),
    "stop_sign": (
        Download(
            f"{VAL2017}/000000000724.jpg",
            "5c0e559c75d3969c8e3e297b61f61063f78045c9d4802b526ba616361f3823fd",
        ),
        11,
    ),
}

# The graph in bf16 against the float32 oracle, at every anchor the oracle
# scores at least SCORE: the same class, its centre within CENTRE pixels,
# its size within a factor of exp(SIZE) and its score within SCORE_ERROR.
# The graph's reference over four COCO photos measured at most 2.9 px, 0.04
# and 0.19 (the cats' sofa, near a tie), the bounds about 1.5x that.
SCORE = 0.25
CENTRE, SIZE, SCORE_ERROR = 4.5, 0.06, 0.3


def image(name: str) -> np.ndarray:
    from PIL import Image

    with Image.open(COCO[name][0].fetch()) as photo:
        return preprocess(np.asarray(photo.convert("RGB")))


def check_detections(got: list[np.ndarray], want: list[np.ndarray]):
    a, b = decode(got), decode(want)
    keep = b[:, 4] * b[:, 5:].max(-1) >= SCORE
    assert keep.any()
    a, b = a[keep], b[keep]
    np.testing.assert_array_equal(a[:, 5:].argmax(-1), b[:, 5:].argmax(-1))
    assert np.abs(a[:, :2] - b[:, :2]).max() <= CENTRE
    assert np.abs(np.log(a[:, 2:4] / b[:, 2:4])).max() <= SIZE
    assert np.abs(a[:, 4:] - b[:, 4:]).max() <= SCORE_ERROR


@pytest.fixture(scope="module")
def weights():
    require(WEIGHTS)
    return Checkpoint(WEIGHTS).tree()


@pytest.mark.parametrize("name", list(COCO))
def test_the_oracle_finds_what_the_photo_holds(weights, name):
    """The most confident anchor is the photo's class; in the cats', both
    cats, a cat at each side.
    """
    d = decode(YOLOXNanoOracle(weights.model)(image(name)))
    score = d[:, 4] * d[:, 5:].max(-1)
    assert d[np.argmax(score), 5:].argmax() == COCO[name][1]
    if name == "cats":
        cats = d[(score >= 0.5) & (d[:, 5:].argmax(-1) == 15)]
        assert cats[:, 0].min() < INPUT_SIZE / 2 < cats[:, 0].max()


def test_the_graph_reference_detects_as_the_oracle(weights, npu2):
    """The graph, each operator's reference on host tensors in bf16."""
    x = image("cats")
    model = YOLOXNano(weights)
    got = YOLOXNano.predictions(model.reference(model.inputs(x)))
    check_detections(got, YOLOXNanoOracle(weights.model)(x))


@pytest.mark.supported_devices("npu2")
def test_yolox_nano_detects_as_the_oracle(weights):
    x = image("cats")
    model = YOLOXNano(weights)
    model.compile(image=((INPUT_SIZE, INPUT_SIZE * 4), bfloat16))
    rows = aie_utils.DEFAULT_TENSOR_CLASS(model.inputs(x))
    got = YOLOXNano.predictions(np.array(y.numpy()) for y in model(rows))
    check_detections(got, YOLOXNanoOracle(weights.model)(x))
