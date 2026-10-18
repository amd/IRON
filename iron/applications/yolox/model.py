#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOX-Nano (Megvii-BaseDetection/YOLOX, Apache-2.0), a CNN object
detector: one graph from an image to its three scales' predictions on the
NPU (``YOLOXNano``), its float32 forward pass on the host
(``YOLOXNanoOracle``), both read from the release's PyTorch checkpoint by
its own names, and the image preprocessing and box decode around them.

A CSPDarknet backbone (a ``Focus`` stem, 2x2 space-to-depth then a 3x3
conv; four stride-2 stages, each a depthwise-separable downsample into a
CSP block of 1x1 convs around depthwise bottlenecks, the last after an SPP
of three max pools), a PAFPN neck (top-down then bottom-up, nearest 2x
upsamples and channel concatenation) and a decoupled head (per scale, a
1x1 stem, then two-conv classification and regression branches and their
1x1 predictions). Every conv but the predictions is bias-free, then
BatchNorm, then SiLU (``BaseConv``); BatchNorm folds into the conv's
weight and bias. Channels-last throughout: an image is ``(H, W, C)``, and
on the NPU its rows, ``(H, W * C)``.

Every BatchNorm's epsilon is 1e-3: upstream's ``exp.get_model()`` sets it
(``init_yolo``) on modules built with ``nn.BatchNorm2d``'s default 1e-5,
so a model built without it detects umbrellas in a photo of two cats.
"""

from pathlib import Path
from types import SimpleNamespace

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16
from numpy.lib.stride_tricks import sliding_window_view

import iron
import iron.functional as F
from iron.lm import ConcatChannels, Conv2d, MaxPool2d
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.flm.gemm.design import M_TILE, compute_rows
from iron.operators.sigmoid import Sigmoid
from iron.operators.silu import SiLU

BN_EPS = 1e-3
INPUT_SIZE = 416
STRIDES = (8, 16, 32)
POOLS = (5, 9, 13)
# The value upstream's preprocessing pads a letterboxed image with.
PAD_VALUE = 114
# The predictions' channels on the NPU, each zero-padded: the box's 4 to
# flm.GEMM's narrowest tile, objectness's 1 and the 80 class scores to
# whole 32-element vectors of Sigmoid's in a 13-pixel row.
BOX, OBJECTNESS, CLASSES = 16, 32, 96


def folded(m) -> tuple[np.ndarray, np.ndarray]:
    """A ``BaseConv`` module's conv weight and bias with its BatchNorm
    folded in, float32.
    """
    bn = m.bn
    scale = bn.weight / np.sqrt(bn.running_var + np.float32(BN_EPS))
    weight = m.conv.weight * scale[:, None, None, None]
    return weight.astype(np.float32), (bn.bias - bn.running_mean * scale)


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


def sigmoid(x):
    """The logistic function as a tanh, which does not overflow."""
    return (np.tanh(x / 2) + 1) / 2


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
        """A ``BaseConv``: the conv, BatchNorm folded, then SiLU."""
        return silu(conv2d(x, *folded(m), stride, depthwise))

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


class Pointwise(iron.Graph):
    """A 1x1 conv of a ``size``-square feature map by ``weight`` ``(out,
    in)``, plus ``bias``, then SiLU if ``act``: a projection of its pixels.
    flm.GEMM takes them in whole blocks of rows, so a map of another count
    is first copied into a held one of whole blocks, whose rows past the
    map are computed and dropped.
    """

    def __init__(self, weight, bias, size: int, act: bool = True):
        self.weight, self.bias, self.size, self.act = weight, bias, size, act
        unit = M_TILE * compute_rows(aie_utils.ensure_current_device())
        pixels = size * size
        self.padded = None
        if pixels % unit:
            self.padded = iron.state((-(-pixels // unit) * unit, weight.shape[1]))

    def body(self, x):
        out, channels = self.weight.shape
        n = self.size * self.size
        pixels = x.reshape(n, channels)
        if self.padded is not None:
            self.padded[:n] = pixels
            pixels = self.padded
        y = F.linear(pixels, self.weight, self.bias, precision=iron.Precision.HIGH)[:n]
        if self.act:
            y = SiLU.step(y, tile_size=self.size * out)
        return y.reshape(self.size, self.size * out)


class Spatial(iron.Graph):
    """A 3x3 conv of a ``size``-square feature map by ``weight`` ``(out,
    in / groups, 3, 3)`` at ``stride``, plus ``bias``, then SiLU: depthwise,
    its input copied between two held zero rows (``Conv2d`` pads the width
    itself), or dense, inside a held zero border a pixel wide.
    """

    def __init__(self, weight, bias, size: int, stride: int = 1):
        out, per_group, k, _ = weight.shape
        self.depthwise = per_group == 1
        self.size, self.bias = size, bias
        channels = out if self.depthwise else per_group
        if self.depthwise:
            self.conv = Conv2d(weight, size, stride, padding=1, groups=out)
            shape = (size + 2, size * channels)
        else:
            self.conv = Conv2d(weight, size + 2, stride)
            shape = (size + 2, (size + 2) * channels)
        self.padded = iron.state(shape)
        self.zeros = np.zeros(shape, bfloat16)
        self.out_rows = (size + 2 - k) // stride + 1

    def body(self, x):
        line = self.padded.shape[1]
        channels = x.shape[1] // self.size
        Copy.step(self.zeros, self.padded)
        offset = line + (0 if self.depthwise else channels)
        interior = TensorAccessPattern(
            self.padded.shape, offset, [self.size, x.shape[1]], [line, 1]
        )
        Copy.step(x, self.padded, dst=interior)
        y = self.conv(self.padded, rows=self.out_rows)
        out, width = self.conv.out_channels, self.conv.out_width
        y = y.reshape(self.out_rows * width, out) + self.bias
        y = SiLU.step(y, tile_size=width * out)
        return y.reshape(self.out_rows, width * out)


class Upsample(iron.Graph):
    """Nearest 2x upsampling of a ``size``-square map of ``channels``: each
    row read twice into a held buffer, which is then written twice, into
    the even and the odd pixels.
    """

    def __init__(self, size: int, channels: int):
        self.size, self.channels = size, channels
        self.doubled = iron.state((2 * size, size * channels))
        self.out = iron.state((2 * size, 2 * size * channels))

    def body(self, x):
        S, C = self.size, self.channels
        twice = TensorAccessPattern((S, S * C), 0, [S, 2, S * C], [S * C, 0, 1])
        Copy.step(x, self.doubled, src=twice)
        for column in (0, C):
            dst = TensorAccessPattern(
                self.out.shape, column, [2 * S, S, C], [2 * S * C, 2 * C, 1]
            )
            Copy.step(self.doubled[:], self.out, dst=dst)
        return Copy.step(self.out[:])


class YOLOXNano(iron.Graph):
    """YOLOX-Nano on the NPU, from a preprocessed image's rows, ``(416,
    416 * 4)``, BGR and a zero channel so each corner the stem gathers is
    whole 4-byte units, to each scale's predictions, ``(H, W * 144)``: the
    box, objectness and class scores, each zero-padded (``BOX``,
    ``OBJECTNESS``, ``CLASSES``), the last two through their sigmoid.

    Every ``BaseConv``'s BatchNorm folds into its weight and bias once, and
    so do the predictions' zero padding, each by its module's path. The
    blocks are built along the forward pass, each keyed by its module's
    checkpoint path.

    Args:
        weights: The checkpoint (``Checkpoint.tree()``).
    """

    profile = Path(__file__).with_name("profiles")

    def __init__(self, weights):
        self.weights = weights
        m = weights.model
        self._paths, convs = {}, []
        pending = [(m, "model")]
        while pending:
            node, path = pending.pop()
            self._paths[id(node)] = path
            if isinstance(node, list):
                pending += [(c, f"{path}.{i}") for i, c in enumerate(node)]
                continue
            if "bn" in vars(node):
                convs.append(node)
            pending += [
                (c, f"{path}.{k}")
                for k, c in vars(node).items()
                if not isinstance(c, np.ndarray)
            ]
        self.derived, self._spatial = {}, {}
        for node in convs:
            weight, bias = folded(node)
            d = self.derived[self._paths[id(node)]] = SimpleNamespace(
                bias=bias.astype(bfloat16)
            )
            if weight.shape[-1] == 1:
                d.weight = weight[:, :, 0, 0].astype(bfloat16)
            else:
                self._spatial[id(node)] = weight
        # The stem's four corners each take a zero channel after BGR's three.
        stem = m.backbone.backbone.stem.conv
        weight = self._spatial[id(stem)].reshape(-1, 4, 3, 3, 3)
        self._spatial[id(stem)] = np.pad(
            weight, ((0, 0), (0, 0), (0, 1), (0, 0), (0, 0))
        ).reshape(-1, 16, 3, 3)
        h = m.head
        for i in range(len(STRIDES)):
            for p, width in (
                (h.reg_preds[i], BOX),
                (h.obj_preds[i], OBJECTNESS),
                (h.cls_preds[i], CLASSES),
            ):
                out, channels = p.weight.shape[:2]
                w = np.zeros((width, channels), bfloat16)
                b = np.zeros(width, bfloat16)
                w[:out], b[:out] = p.weight[:, :, 0, 0], p.bias
                self.derived[self._paths[id(p)]] = SimpleNamespace(
                    padded_weight=w, padded_bias=b
                )
        self.blocks = {}
        self.build(m)

    def derive(self, m):
        """What ``m`` folds into."""
        return self.derived[self._paths[id(m)]]

    def build_conv(self, m, size: int, stride: int = 1) -> int:
        """The block of ``BaseConv`` ``m`` on a ``size``-square map; returns
        the size it gives.
        """
        d = self.derive(m)
        if id(m) in self._spatial:
            block = Spatial(self._spatial[id(m)], d.bias, size, stride)
            size = block.conv.out_width
        else:
            block = Pointwise(d.weight, d.bias, size)
        self.blocks[self._paths[id(m)]] = block
        return size

    def build_dwconv(self, m, size: int, stride: int = 1) -> int:
        return self.build_conv(m.pconv, self.build_conv(m.dconv, size, stride))

    def build_csp(self, m, size: int):
        for c in (m.conv1, m.conv2, m.conv3):
            self.build_conv(c, size)
        for b in m.m:
            self.build_dwconv(b.conv2, self.build_conv(b.conv1, size))
        hidden = m.conv1.conv.weight.shape[0]
        self.blocks[f"{self._paths[id(m)]}.join"] = ConcatChannels(
            size, size, (hidden, hidden)
        )

    def build(self, m):
        """Every block, along the forward pass, its maps' sizes as they go."""
        b, n, h = m.backbone.backbone, m.backbone, m.head
        size = INPUT_SIZE // 2
        self.blocks["model.backbone.backbone.stem.corners"] = ConcatChannels(
            size, size, (4, 4, 4, 4)
        )
        size = self.build_conv(b.stem.conv, size)
        sizes = {}
        for stage in (b.dark2, b.dark3, b.dark4, b.dark5):
            size = self.build_dwconv(stage[0], size, 2)
            sizes[id(stage)] = size
        for stage in (b.dark2, b.dark3, b.dark4):
            self.build_csp(stage[1], sizes[id(stage)])
        spp = b.dark5[1]
        self.build_conv(spp.conv1, size)
        self.build_conv(spp.conv2, size)
        hidden = spp.conv1.conv.weight.shape[0]
        for k in POOLS:
            self.blocks[f"{self._paths[id(spp)]}.pool{k}"] = MaxPool2d(
                size, size, hidden, k
            )
        self.blocks[f"{self._paths[id(spp)]}.join"] = ConcatChannels(
            size, size, (hidden,) * (len(POOLS) + 1)
        )
        self.build_csp(b.dark5[2], size)
        s3, s4, s5 = (sizes[id(stage)] for stage in (b.dark3, b.dark4, b.dark5))
        c4, c5 = (c.conv3.conv.weight.shape[0] for c in (b.dark4[1], b.dark5[2]))
        self.build_conv(n.lateral_conv0, s5)
        top0 = n.lateral_conv0.conv.weight.shape[0]
        self.blocks["model.backbone.up0"] = Upsample(s5, top0)
        self.blocks["model.backbone.join_p4"] = ConcatChannels(s4, s4, (top0, c4))
        self.build_csp(n.C3_p4, s4)
        self.build_conv(n.reduce_conv1, s4)
        top1 = n.reduce_conv1.conv.weight.shape[0]
        c3 = b.dark3[1].conv3.conv.weight.shape[0]
        self.blocks["model.backbone.up1"] = Upsample(s4, top1)
        self.blocks["model.backbone.join_p3"] = ConcatChannels(s3, s3, (top1, c3))
        self.build_csp(n.C3_p3, s3)
        self.build_dwconv(n.bu_conv2, s3, 2)
        down = n.bu_conv2.pconv.conv.weight.shape[0]
        self.blocks["model.backbone.join_n3"] = ConcatChannels(s4, s4, (down, top1))
        self.build_csp(n.C3_n3, s4)
        self.build_dwconv(n.bu_conv1, s4, 2)
        down = n.bu_conv1.pconv.conv.weight.shape[0]
        self.blocks["model.backbone.join_n4"] = ConcatChannels(s5, s5, (down, top0))
        self.build_csp(n.C3_n4, s5)
        for i, size in enumerate((s3, s4, s5)):
            self.build_conv(h.stems[i], size)
            for j in range(2):
                self.build_dwconv(h.cls_convs[i][j], size)
                self.build_dwconv(h.reg_convs[i][j], size)
            for p in (h.reg_preds[i], h.obj_preds[i], h.cls_preds[i]):
                d = self.derive(p)
                self.blocks[self._paths[id(p)]] = Pointwise(
                    d.padded_weight, d.padded_bias, size, act=False
                )
            self.blocks[f"model.head.join{i}"] = ConcatChannels(
                size, size, (BOX, OBJECTNESS, CLASSES)
            )

    def conv(self, m, x):
        return self.blocks[self._paths[id(m)]](x)

    def dwconv(self, m, x):
        return self.conv(m.pconv, self.conv(m.dconv, x))

    def csp(self, m, x, shortcut: bool):
        """A CSP block, as the oracle's."""
        y = self.conv(m.conv1, x)
        for b in m.m:
            z = self.dwconv(b.conv2, self.conv(b.conv1, y))
            y = ElementwiseAdd.step(z, y, tile_size=y.shape[1]) if shortcut else z
        join = self.blocks[f"{self._paths[id(m)]}.join"]
        return self.conv(m.conv3, join(y, self.conv(m.conv2, x)))

    def backbone(self, image):
        b = self.weights.model.backbone.backbone
        S, line = INPUT_SIZE // 2, INPUT_SIZE * 4
        corners = [
            Copy.step(
                image,
                src=TensorAccessPattern(
                    image.shape, r * line + c * 4, [S, S, 4], [2 * line, 8, 1]
                ),
            ).reshape(S, S * 4)
            for r, c in ((0, 0), (1, 0), (0, 1), (1, 1))
        ]
        x = self.conv(
            b.stem.conv, self.blocks["model.backbone.backbone.stem.corners"](*corners)
        )
        x = self.csp(b.dark2[1], self.dwconv(b.dark2[0], x), True)
        dark3 = self.csp(b.dark3[1], self.dwconv(b.dark3[0], x), True)
        dark4 = self.csp(b.dark4[1], self.dwconv(b.dark4[0], dark3), True)
        spp = b.dark5[1]
        x = self.conv(spp.conv1, self.dwconv(b.dark5[0], dark4))
        path = self._paths[id(spp)]
        pooled = [self.blocks[f"{path}.pool{k}"](x) for k in POOLS]
        x = self.conv(spp.conv2, self.blocks[f"{path}.join"](x, *pooled))
        return dark3, dark4, self.csp(b.dark5[2], x, False)

    def neck(self, dark3, dark4, dark5):
        n, blocks = self.weights.model.backbone, self.blocks
        top0 = self.conv(n.lateral_conv0, dark5)
        x = blocks["model.backbone.join_p4"](blocks["model.backbone.up0"](top0), dark4)
        x = self.csp(n.C3_p4, x, False)
        top1 = self.conv(n.reduce_conv1, x)
        x = blocks["model.backbone.join_p3"](blocks["model.backbone.up1"](top1), dark3)
        out3 = self.csp(n.C3_p3, x, False)
        x = blocks["model.backbone.join_n3"](self.dwconv(n.bu_conv2, out3), top1)
        out4 = self.csp(n.C3_n3, x, False)
        x = blocks["model.backbone.join_n4"](self.dwconv(n.bu_conv1, out4), top0)
        return out3, out4, self.csp(n.C3_n4, x, False)

    def head(self, i, x):
        h = self.weights.model.head
        x = self.conv(h.stems[i], x)
        cls, reg = x, x
        for j in range(2):
            cls = self.dwconv(h.cls_convs[i][j], cls)
            reg = self.dwconv(h.reg_convs[i][j], reg)
        box = self.conv(h.reg_preds[i], reg)
        obj, scores = (
            Sigmoid.step(y, tile_size=y.shape[1] // (2 if y.shape[1] > 4096 else 1))
            for y in (self.conv(h.obj_preds[i], reg), self.conv(h.cls_preds[i], cls))
        )
        return self.blocks[f"model.head.join{i}"](box, obj, scores)

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
        float32, its padding dropped.
        """
        out = []
        for y in scales:
            y = np.asarray(y, np.float32)
            y = y.reshape(y.shape[0], y.shape[0], BOX + OBJECTNESS + CLASSES)
            box, obj = y[..., :4], y[..., BOX : BOX + 1]
            scores = y[..., BOX + OBJECTNESS : BOX + OBJECTNESS + 80]
            out.append(np.concatenate([box, obj, scores], -1))
        return out
