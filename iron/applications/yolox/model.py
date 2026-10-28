# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOX-Nano (Megvii-BaseDetection/YOLOX, Apache-2.0), a CNN object
detector: one graph from an image to its three scales' predictions on the
NPU (``YOLOXNano``), read from the release's PyTorch checkpoint by its
own names, and the image preprocessing and box decode around it. Its tests
check it against a float32 forward pass on the host (``YOLOXNanoOracle``
in its ``test.py``).

A CSPDarknet backbone (a ``Focus`` stem, 2x2 space-to-depth then a 3x3
conv; four stride-2 stages, each a depthwise-separable downsample into a
CSP block of 1x1 convs around depthwise bottlenecks, the last after an SPP
of three max pools), a PAFPN neck (top-down then bottom-up, nearest 2x
upsamples and channel concatenation) and a decoupled head (per scale, a
1x1 stem, then two-conv classification and regression branches and their
1x1 predictions). Every conv but the predictions is bias-free, then
BatchNorm, then SiLU (``BaseConv``); BatchNorm folds into the conv's
weight and bias. Channels-last throughout, as ``iron.functional``'s
feature maps.

Every BatchNorm's epsilon is 1e-3: upstream's ``exp.get_model()`` sets it
(``init_yolo``) on modules built with ``nn.BatchNorm2d``'s default 1e-5,
so a model built without it detects umbrellas in a photo of two cats.
"""

from pathlib import Path
from types import SimpleNamespace

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron.lm import BatchNorm2d, subtree
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.sigmoid import Sigmoid
from iron.operators.silu import SiLU

BN_EPS = 1e-3
INPUT_SIZE = 416
STRIDES = (8, 16, 32)
POOLS = (5, 9, 13)
# The value upstream's preprocessing pads a letterboxed image with.
PAD_VALUE = 114
# The predictions' channels on the NPU, each zero-padded: the box's 4 to
# flm.ProjectionGEMM's narrowest tile, objectness's 1 and the 80 class scores to
# whole 32-element vectors of Sigmoid's in a 13-pixel row.
BOX, OBJECTNESS, CLASSES = 16, 32, 96


def preprocess(image: np.ndarray, size: int = INPUT_SIZE) -> np.ndarray:
    """An RGB ``uint8`` image as YOLOX takes it: BGR, resized to fit
    ``size`` square keeping its aspect (OpenCV's bilinear, half-pixel
    centres, rounded to ``uint8``), top-left, the rest ``PAD_VALUE``;
    ``(size, size, 3)`` float32.
    """
    h, w = image.shape[:2]
    r = min(size / h, size / w)
    out_h, out_w = int(h * r), int(w * r)
    source = image[..., ::-1].astype(np.float32)
    ys = np.clip((np.arange(out_h) + 0.5) / r - 0.5, 0, h - 1)
    xs = np.clip((np.arange(out_w) + 0.5) / r - 0.5, 0, w - 1)
    y0, x0 = np.floor(ys).astype(int), np.floor(xs).astype(int)
    y1, x1 = np.minimum(y0 + 1, h - 1), np.minimum(x0 + 1, w - 1)
    fy, fx = (ys - y0)[:, None, None], (xs - x0)[None, :, None]
    top = source[y0][:, x0] * (1 - fx) + source[y0][:, x1] * fx
    bottom = source[y1][:, x0] * (1 - fx) + source[y1][:, x1] * fx
    resized = np.rint(top * (1 - fy) + bottom * fy)
    out = np.full((size, size, 3), PAD_VALUE, np.float32)
    out[:out_h, :out_w] = resized
    return out


def decode(scales: list[np.ndarray]) -> np.ndarray:
    """The three scales' predictions ``(H, W, 85)`` (box, objectness, 80
    class scores) as ``(anchors, 85)`` detections: each box's centre
    offset by its grid cell and its size exponentiated, both times its
    scale's stride.
    """
    rows = []
    for out, stride in zip(scales, STRIDES):
        h, w, c = out.shape
        y, x = np.meshgrid(np.arange(h), np.arange(w), indexing="ij")
        grid = np.stack([x, y], axis=-1).reshape(h * w, 2).astype(np.float32)
        flat = out.reshape(h * w, c).astype(np.float32)
        xy = (flat[:, :2] + grid) * stride
        wh = np.exp(flat[:, 2:4]) * stride
        rows.append(np.concatenate([xy, wh, flat[:, 4:]], axis=-1))
    return np.concatenate(rows)


def _row(x) -> int:
    """A feature map's elements a row."""
    return x.shape[1] * x.shape[2]


def sigmoid(x):
    """The logistic function as a tanh, which does not overflow."""
    return (np.tanh(x / 2) + 1) / 2


class BaseConv(iron.Graph):
    """A bias-free ``k``-square conv at ``stride``, depthwise over
    ``groups``, same padding, its BatchNorm folded in as it loads, then
    SiLU.
    """

    def __init__(self, cin: int, cout: int, k: int = 1, stride: int = 1, groups=1):
        shape = (cout, cin // groups, k, k)
        self.conv = SimpleNamespace(weight=iron.param(*shape, dtype=np.float32))
        self.bn = BatchNorm2d(cout, BN_EPS)
        self.stride, self.groups = stride, groups

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        self.weight, self.bias = map(iron.param, self.bn.fold(self.conv.weight))

    def body(self, x):
        k = self.weight.shape[-1]
        bias = self.bias.astype(bfloat16)
        y = F.conv2d(x, self.weight, bias, self.stride, k // 2, groups=self.groups)
        return SiLU.step(y, tile_size=_row(y))


class DWConv(iron.Graph):
    """A depthwise ``k``-square ``BaseConv`` at ``stride``, then a 1x1."""

    def __init__(self, cin: int, cout: int, k: int = 3, stride: int = 1):
        self.dconv = BaseConv(cin, cin, k, stride, groups=cin)
        self.pconv = BaseConv(cin, cout)

    def body(self, x):
        return self.pconv(self.dconv(x))


class Bottleneck(iron.Graph):
    """A 1x1 ``BaseConv`` then a ``DWConv``, added to its input where
    ``shortcut``.
    """

    def __init__(self, channels: int, shortcut: bool):
        self.conv1 = BaseConv(channels, channels)
        self.conv2 = DWConv(channels, channels)
        self.shortcut = shortcut

    def body(self, x):
        y = self.conv2(self.conv1(x))
        return ElementwiseAdd.step(y, x, tile_size=_row(x)) if self.shortcut else y


class CSPLayer(iron.Graph):
    """A CSP block: ``m``'s bottlenecks over half the channels, each added
    to its input where ``shortcut``, beside a 1x1 of the input, then a
    1x1 of both.
    """

    def __init__(self, cin: int, cout: int, depth: int, shortcut: bool = True):
        hidden = cout // 2
        self.conv1 = BaseConv(cin, hidden)
        self.conv2 = BaseConv(cin, hidden)
        self.conv3 = BaseConv(2 * hidden, cout)
        self.m = [Bottleneck(hidden, shortcut) for _ in range(depth)]

    def body(self, x):
        y = self.conv1(x)
        for b in self.m:
            y = b(y)
        return self.conv3(F.cat([y, self.conv2(x)], dim=-1))


class SPPBottleneck(iron.Graph):
    """A 1x1 conv, its max pools of each of ``POOLS`` beside it, then a
    1x1 of all four.
    """

    def __init__(self, channels: int):
        hidden = channels // 2
        self.conv1 = BaseConv(channels, hidden)
        self.conv2 = BaseConv(hidden * (len(POOLS) + 1), channels)

    def body(self, x):
        x = self.conv1(x)
        pooled = [F.max_pool2d(x, k, 1, k // 2) for k in POOLS]
        return self.conv2(F.cat([x, *pooled], dim=-1))


class Prediction(iron.Graph):
    """A head's 1x1 prediction conv, its ``cout`` output channels
    zero-padded to ``width`` as it loads, bfloat16.
    """

    def __init__(self, cin: int, cout: int, width: int):
        self.weight = iron.param(cout, cin, 1, 1, dtype=np.float32)
        self.bias = iron.param(cout, dtype=np.float32)
        self.width = width

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        out, channels = self.weight.shape[:2]
        weight = np.zeros((self.width, channels, 1, 1), bfloat16)
        bias = np.zeros(self.width, bfloat16)
        weight[:out], bias[:out] = self.weight, self.bias
        self.weight, self.bias = iron.param(weight), iron.param(bias)

    def body(self, x):
        return F.conv2d(x, self.weight, self.bias)


class Focus(iron.Graph):
    """The stem: a ``BaseConv`` over the image's 2x2 space-to-depth, its
    four corners each taking a zero channel after BGR's three.
    """

    def __init__(self, cout: int):
        self.conv = BaseConv(4 * 3, cout, 3)

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        weight = self.conv.weight.reshape(-1, 4, 3, 3, 3)
        weight = np.pad(weight, ((0, 0), (0, 0), (0, 1), (0, 0), (0, 0)))
        self.conv.weight = iron.param(weight.reshape(-1, 16, 3, 3))


class CSPDarknet(iron.Graph):
    """YOLOX-Nano's backbone (``dark2`` to ``dark5`` after the stem), 16
    channels from the stem.
    """

    def __init__(self):
        w = 16
        self.stem = Focus(w)
        self.dark2 = [DWConv(w, 2 * w, 3, 2), CSPLayer(2 * w, 2 * w, 1)]
        self.dark3 = [DWConv(2 * w, 4 * w, 3, 2), CSPLayer(4 * w, 4 * w, 3)]
        self.dark4 = [DWConv(4 * w, 8 * w, 3, 2), CSPLayer(8 * w, 8 * w, 3)]
        self.dark5 = [
            DWConv(8 * w, 16 * w, 3, 2),
            SPPBottleneck(16 * w),
            CSPLayer(16 * w, 16 * w, 1, shortcut=False),
        ]


class PAFPN(iron.Graph):
    """The backbone, then the neck: top-down then bottom-up over its last
    three maps, 64 channels at the finest.
    """

    def __init__(self):
        w = 64
        self.backbone = CSPDarknet()
        self.lateral_conv0 = BaseConv(4 * w, 2 * w)
        self.C3_p4 = CSPLayer(4 * w, 2 * w, 1, shortcut=False)
        self.reduce_conv1 = BaseConv(2 * w, w)
        self.C3_p3 = CSPLayer(2 * w, w, 1, shortcut=False)
        self.bu_conv2 = DWConv(w, w, 3, 2)
        self.C3_n3 = CSPLayer(2 * w, 2 * w, 1, shortcut=False)
        self.bu_conv1 = DWConv(2 * w, 2 * w, 3, 2)
        self.C3_n4 = CSPLayer(4 * w, 4 * w, 1, shortcut=False)


class Head(iron.Graph):
    """The decoupled head over the neck's maps of 64, 128 and 256
    channels: per scale a 1x1 stem to 64, two-conv classification and
    regression branches, and their 1x1 predictions of 80 classes, the box
    and objectness.
    """

    def __init__(self):
        widths, hidden, classes = (64, 128, 256), 64, 80
        self.stems = [BaseConv(w, hidden) for w in widths]
        self.cls_convs = [[DWConv(hidden, hidden) for _ in "ab"] for _ in widths]
        self.reg_convs = [[DWConv(hidden, hidden) for _ in "ab"] for _ in widths]
        self.cls_preds = [Prediction(hidden, classes, CLASSES) for _ in widths]
        self.reg_preds = [Prediction(hidden, 4, BOX) for _ in widths]
        self.obj_preds = [Prediction(hidden, 1, OBJECTNESS) for _ in widths]


class YOLOX(iron.Graph):
    """The checkpoint's ``model``: the neck over its backbone, then the
    head.
    """

    def __init__(self):
        self.backbone = PAFPN()
        self.head = Head()


class YOLOXNano(iron.Graph):
    """YOLOX-Nano on the NPU, from a preprocessed image's rows, ``(416,
    416 * 4)``, BGR and a zero channel so each corner the stem gathers is
    whole 4-byte units, to each scale's predictions, ``(H, W, 144)``: the
    box, objectness and class scores, each zero-padded (``BOX``,
    ``OBJECTNESS``, ``CLASSES``), the last two through their sigmoid.

    Every ``BaseConv``'s BatchNorm folds into its weight and bias as it
    loads, and so do the stem's zero channels and the predictions' zero
    padding. A map's elementwise steps each take one of its rows a tile.

    Args:
        weights: The checkpoint (``Checkpoint.tree()``), its ``model`` read.
    """

    profile = Path(__file__).with_name("profiles")

    def __init__(self, weights):
        self.model = YOLOX()
        self.load_state_dict(subtree(weights, model=weights.model))

    def backbone(self, image):
        b = self.model.backbone.backbone
        S, line = INPUT_SIZE // 2, INPUT_SIZE * 4
        corners = [
            Copy.step(
                image,
                src=TensorAccessPattern(
                    image.shape, r * line + c * 4, [S, S, 4], [2 * line, 8, 1]
                ),
            ).reshape(S, S, 4)
            for r, c in ((0, 0), (1, 0), (0, 1), (1, 1))
        ]
        x = b.stem.conv(F.cat(corners, dim=-1))
        x = b.dark2[1](b.dark2[0](x))
        dark3 = b.dark3[1](b.dark3[0](x))
        dark4 = b.dark4[1](b.dark4[0](dark3))
        x = b.dark5[1](b.dark5[0](dark4))
        return dark3, dark4, b.dark5[2](x)

    def neck(self, dark3, dark4, dark5):
        n = self.model.backbone
        top0 = n.lateral_conv0(dark5)
        x = F.cat([F.interpolate(top0, scale_factor=2), dark4], dim=-1)
        top1 = n.reduce_conv1(n.C3_p4(x))
        x = F.cat([F.interpolate(top1, scale_factor=2), dark3], dim=-1)
        out3 = n.C3_p3(x)
        out4 = n.C3_n3(F.cat([n.bu_conv2(out3), top1], dim=-1))
        x = F.cat([n.bu_conv1(out4), top0], dim=-1)
        return out3, out4, n.C3_n4(x)

    def head(self, i, x):
        h = self.model.head
        cls = reg = h.stems[i](x)
        for j in range(2):
            cls = h.cls_convs[i][j](cls)
            reg = h.reg_convs[i][j](reg)
        box, obj, scores = h.reg_preds[i](reg), h.obj_preds[i](reg), h.cls_preds[i](cls)
        obj, scores = (
            Sigmoid.step(y, tile_size=_row(y) // (2 if _row(y) > 4096 else 1))
            for y in (obj, scores)
        )
        return F.cat([box, obj, scores], dim=-1)

    def body(self, image):
        scales = self.neck(*self.backbone(image))
        return tuple(self.head(i, x) for i, x in enumerate(scales))

    def inputs(self, image: np.ndarray) -> np.ndarray:
        """A preprocessed ``(416, 416, 3)`` image as the graph takes it."""
        rows = np.zeros((INPUT_SIZE, INPUT_SIZE, 4), bfloat16)
        rows[..., :3] = image
        return rows.reshape(INPUT_SIZE, INPUT_SIZE * 4)

    @staticmethod
    def predictions(scales) -> list[np.ndarray]:
        """The graph's outputs as the oracle's: each scale ``(H, W, 85)``
        float32, its padding dropped. A device returns each flat.
        """
        out = []
        for y, stride in zip(scales, STRIDES):
            size = INPUT_SIZE // stride
            y = np.asarray(y, np.float32).reshape(size, size, -1)
            box, obj = y[..., :4], y[..., BOX : BOX + 1]
            scores = y[..., BOX + OBJECTNESS : BOX + OBJECTNESS + 80]
            out.append(np.concatenate([box, obj, scores], -1))
        return out
