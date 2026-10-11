#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOX-Nano: a CNN object detector (Megvii-BaseDetection/YOLOX,
Apache-2.0), the one non-transformer model this skill covers. Its
checkpoint ships as a raw PyTorch ``.pth`` (no HF/safetensors release), so
loading it needs torch, unlike every other model here -- the only run path
this touches, not the device graph, which is numpy/bf16 throughout.

Architecture, confirmed against the real checkpoint's own tensor names and
shapes (``torch.load(..., weights_only=False)['model']``), not assumed from
the training config: a CSPDarknet backbone (a ``Focus`` stem -- 2x2
space-to-depth, then a 3x3 conv; four stride-2 stages, each a
depthwise-separable downsample then a CSP ("C3") block of 1x1 convs around
a stack of bottlenecks; the last stage's bottleneck block follows an SPP --
three parallel max-pools, kernel 5/9/13, concatenated with the input), a
PAFPN neck (top-down then bottom-up, nearest-neighbor 2x upsamples and
channel concatenation, more CSP blocks) and a decoupled head (three
scales/strides, each a shared 1x1 stem then separate two-conv classification
and regression branches). Every conv is bias-free, BatchNorm, SiLU
("BaseConv"); depthwise convs are what makes it "Nano" rather than a
regular-conv variant.

``YOLOXNanoOracle`` is the float32 forward pass on the host, channels-last
(HWC, this library's convention throughout, not torch's NCHW): BatchNorm is
folded into its preceding conv's weight and bias exactly, once, at load
time (``fold_bn``), not a separate device step. Verified against the real
upstream source (vendored, not reimplemented from memory, in
``/scratch/ehunhoff/iron-next/scratch/yolox_src/yolox_ref.py`` -- Apache-2.0,
fetched from Megvii-BaseDetection/YOLOX, not part of this tree) loading the
same real checkpoint: 0 missing/unexpected keys, and on a random image,
``YOLOXNanoOracle`` matches the vendored torch reference's final (decoded)
output to a max relative error of 2.4e-4 (mean absolute error 5.4e-6). One
real finding along the way: the training exp config
(``exps/default/yolox_nano.py``) sets BatchNorm's momentum and implies
``eps=1e-3``, but the released checkpoint's own modules report
``eps=1e-5`` (``nn.BatchNorm2d``'s default) -- confirmed from the live
torch model, not the config file, which does not actually override it at
the module level for this release.

The NPU graph (``iron.lm.blocks``' ``Conv2d``, ``MaxPool2d``, ``project``)
is not yet wired; this module is the oracle alone, the gate step 6.1 asks
for before any device work.
"""

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

#: The real checkpoint's own BatchNorm eps (``nn.BatchNorm2d``'s default),
#: confirmed from the live torch modules, not the training exp config's
#: (misleading) 1e-3.
BN_EPS = 1e-5

INPUT_SIZE = 416
NUM_CLASSES = 80
STRIDES = (8, 16, 32)
BASE_CHANNELS = 16  # int(0.25 * 64), YOLOX-Nano's width multiplier
BASE_DEPTH = 1  # max(round(0.33 * 3), 1), YOLOX-Nano's depth multiplier


def silu(x):
    return x / (1.0 + np.exp(-x))


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def conv2d(x, weight, bias, stride=1, groups=1):
    """``x`` ``(H, W, Cin)``, ``weight`` ``(Cout, Cin / groups, k, k)``
    (the checkpoint's own, torch layout), same padding
    (``(k - 1) // 2``), ``bias`` ``(Cout,)`` or ``None``.
    """
    Cout, Cin_g, k, _ = weight.shape
    pad = (k - 1) // 2
    xp = np.pad(x, ((pad, pad), (pad, pad), (0, 0)))
    if groups == 1:
        # sliding_window_view gives (Hout, Wout, Cin, k, k); move Cin after
        # the window axes so the flatten order matches weight's (k, k, Cin).
        windows = sliding_window_view(xp, (k, k), axis=(0, 1))[::stride, ::stride]
        windows = np.moveaxis(windows, 2, -1)  # (Hout, Wout, k, k, Cin)
        w = weight.transpose(2, 3, 1, 0).reshape(k * k * Cin_g, Cout)
        out = windows.reshape(*windows.shape[:2], -1) @ w
    else:
        # Depthwise: groups == Cout == Cin, Cin_g == 1; no cross-channel
        # mixing, so the natural (Hout, Wout, C, k, k) window needs no move.
        windows = sliding_window_view(xp, (k, k), axis=(0, 1))[::stride, ::stride]
        w = weight[:, 0]  # (C, k, k)
        out = np.einsum("hwckl,ckl->hwc", windows, w)
    if bias is not None:
        out = out + bias
    return out


def max_pool2d(x, kernel):
    """ "Same"-padded max pooling, stride 1, ``-inf`` the pad value: a real
    input (post-SiLU) can be slightly negative, so zero would not be the
    reduction's identity.
    """
    pad = kernel // 2
    xp = np.pad(x, ((pad, pad), (pad, pad), (0, 0)), constant_values=-np.inf)
    windows = sliding_window_view(xp, (kernel, kernel), axis=(0, 1))
    return windows.max(axis=(-1, -2))


def upsample2x(x):
    """Nearest-neighbor 2x upsample, each pixel repeated into a 2x2 block."""
    return np.repeat(np.repeat(x, 2, axis=0), 2, axis=1)


def fold_bn(sd, prefix, eps=BN_EPS):
    """A ``BaseConv``'s folded ``(weight, bias)``: the preceding conv's
    weight times BatchNorm's scale, and BatchNorm's own shift, exact in
    float32 (one rounding, same as every other model's weight loading).
    """
    w = np.asarray(sd[f"{prefix}.conv.weight"], np.float32)
    gamma = np.asarray(sd[f"{prefix}.bn.weight"], np.float32)
    beta = np.asarray(sd[f"{prefix}.bn.bias"], np.float32)
    mean = np.asarray(sd[f"{prefix}.bn.running_mean"], np.float32)
    var = np.asarray(sd[f"{prefix}.bn.running_var"], np.float32)
    scale = gamma / np.sqrt(var + eps)
    weight = w * scale[:, None, None, None]
    bias = beta - mean * scale
    return weight, bias


def plain(sd, prefix):
    """A head prediction conv's own ``(weight, bias)``: a real bias, no
    BatchNorm (``nn.Conv2d`` directly, not ``BaseConv``).
    """
    return (
        np.asarray(sd[f"{prefix}.weight"], np.float32),
        np.asarray(sd[f"{prefix}.bias"], np.float32),
    )


class BaseConv:
    """Conv, BatchNorm (folded), SiLU: every conv in the backbone and neck,
    and the head's shared stem and branches, bar the final predictions.
    """

    def __init__(self, sd, prefix, stride, groups=1):
        self.weight, self.bias = fold_bn(sd, prefix)
        self.stride, self.groups = stride, groups

    def __call__(self, x):
        return silu(conv2d(x, self.weight, self.bias, self.stride, self.groups))


class DWConv:
    """Depthwise-separable conv: a depthwise 3x3 (one filter a channel, no
    cross-channel mixing) then a pointwise 1x1, each its own BaseConv.
    """

    def __init__(self, sd, prefix, stride):
        channels = sd[f"{prefix}.dconv.conv.weight"].shape[0]
        self.dconv = BaseConv(sd, f"{prefix}.dconv", stride, groups=channels)
        self.pconv = BaseConv(sd, f"{prefix}.pconv", 1)

    def __call__(self, x):
        return self.pconv(self.dconv(x))


class Bottleneck:
    """A CSP block's inner residual unit: 1x1 then a depthwise-separable
    3x3, added back to its input when the shapes agree (always, inside a
    CSPLayer, whose bottlenecks keep the hidden width both ends).
    """

    def __init__(self, sd, prefix, in_channels, out_channels, shortcut=True):
        self.conv1 = BaseConv(sd, f"{prefix}.conv1", 1)
        self.conv2 = DWConv(sd, f"{prefix}.conv2", 1)
        self.use_add = shortcut and in_channels == out_channels

    def __call__(self, x):
        y = self.conv2(self.conv1(x))
        return y + x if self.use_add else y


class CSPLayer:
    """ "C3": a 1x1 conv run through ``n`` bottlenecks, beside a second 1x1
    conv of the same input taken whole, concatenated and projected by a
    third 1x1 conv.
    """

    def __init__(self, sd, prefix, out_channels, n, shortcut=True):
        self.conv1 = BaseConv(sd, f"{prefix}.conv1", 1)
        self.conv2 = BaseConv(sd, f"{prefix}.conv2", 1)
        self.conv3 = BaseConv(sd, f"{prefix}.conv3", 1)
        hidden = out_channels // 2
        self.m = [
            Bottleneck(sd, f"{prefix}.m.{i}", hidden, hidden, shortcut)
            for i in range(n)
        ]

    def __call__(self, x):
        x1 = self.conv1(x)
        for b in self.m:
            x1 = b(x1)
        x2 = self.conv2(x)
        return self.conv3(np.concatenate([x1, x2], axis=-1))


class Focus:
    """The backbone's stem: 2x2 space-to-depth (four interleaved corners,
    top-left/bottom-left/top-right/bottom-right, the real source's own
    concat order) into the channel axis, then a 3x3 BaseConv.
    """

    def __init__(self, sd, prefix):
        self.conv = BaseConv(sd, f"{prefix}.conv", 1)

    def __call__(self, x):
        tl, tr = x[0::2, 0::2], x[0::2, 1::2]
        bl, br = x[1::2, 0::2], x[1::2, 1::2]
        return self.conv(np.concatenate([tl, bl, tr, br], axis=-1))


class SPPBottleneck:
    """Spatial pyramid pooling: a 1x1 conv, three parallel same-padded max
    pools (kernel 5, 9, 13, stride 1) over its output concatenated with it,
    then a second 1x1 conv back down.
    """

    def __init__(self, sd, prefix, kernel_sizes=(5, 9, 13)):
        self.conv1 = BaseConv(sd, f"{prefix}.conv1", 1)
        self.conv2 = BaseConv(sd, f"{prefix}.conv2", 1)
        self.kernel_sizes = kernel_sizes

    def __call__(self, x):
        x = self.conv1(x)
        pooled = [x] + [max_pool2d(x, k) for k in self.kernel_sizes]
        return self.conv2(np.concatenate(pooled, axis=-1))


class CSPDarknet:
    """The backbone: the stem, then four stride-2 stages (dark2-dark5),
    each a depthwise-separable downsample into a CSP block; dark5's block
    follows an SPP. Returns dark3, dark4, dark5 (the neck's three inputs).
    """

    def __init__(self, sd, prefix="backbone.backbone", bc=BASE_CHANNELS, bd=BASE_DEPTH):
        self.stem = Focus(sd, f"{prefix}.stem")
        self.dark2_down = DWConv(sd, f"{prefix}.dark2.0", 2)
        self.dark2_csp = CSPLayer(sd, f"{prefix}.dark2.1", bc * 2, bd)
        self.dark3_down = DWConv(sd, f"{prefix}.dark3.0", 2)
        self.dark3_csp = CSPLayer(sd, f"{prefix}.dark3.1", bc * 4, bd * 3)
        self.dark4_down = DWConv(sd, f"{prefix}.dark4.0", 2)
        self.dark4_csp = CSPLayer(sd, f"{prefix}.dark4.1", bc * 8, bd * 3)
        self.dark5_down = DWConv(sd, f"{prefix}.dark5.0", 2)
        self.dark5_spp = SPPBottleneck(sd, f"{prefix}.dark5.1")
        self.dark5_csp = CSPLayer(sd, f"{prefix}.dark5.2", bc * 16, bd, shortcut=False)

    def __call__(self, x):
        x = self.stem(x)
        x = self.dark2_csp(self.dark2_down(x))
        dark3 = self.dark3_csp(self.dark3_down(x))
        dark4 = self.dark4_csp(self.dark4_down(dark3))
        dark5 = self.dark5_csp(self.dark5_spp(self.dark5_down(dark4)))
        return dark3, dark4, dark5


class YOLOPAFPN:
    """The neck: top-down (lateral 1x1 convs, 2x upsample, concat, CSP
    block) then bottom-up (depthwise-separable downsample, concat, CSP
    block), over the backbone's three feature maps.
    """

    def __init__(self, sd, prefix="backbone", bc=BASE_CHANNELS, bd=BASE_DEPTH):
        self.backbone = CSPDarknet(sd, f"{prefix}.backbone", bc, bd)
        self.lateral_conv0 = BaseConv(sd, f"{prefix}.lateral_conv0", 1)
        self.C3_p4 = CSPLayer(sd, f"{prefix}.C3_p4", bc * 8, bd, shortcut=False)
        self.reduce_conv1 = BaseConv(sd, f"{prefix}.reduce_conv1", 1)
        self.C3_p3 = CSPLayer(sd, f"{prefix}.C3_p3", bc * 4, bd, shortcut=False)
        self.bu_conv2 = DWConv(sd, f"{prefix}.bu_conv2", 2)
        self.C3_n3 = CSPLayer(sd, f"{prefix}.C3_n3", bc * 8, bd, shortcut=False)
        self.bu_conv1 = DWConv(sd, f"{prefix}.bu_conv1", 2)
        self.C3_n4 = CSPLayer(sd, f"{prefix}.C3_n4", bc * 16, bd, shortcut=False)

    def __call__(self, x):
        x2, x1, x0 = self.backbone(x)

        fpn_out0 = self.lateral_conv0(x0)
        f_out0 = self.C3_p4(np.concatenate([upsample2x(fpn_out0), x1], axis=-1))

        fpn_out1 = self.reduce_conv1(f_out0)
        pan_out2 = self.C3_p3(np.concatenate([upsample2x(fpn_out1), x2], axis=-1))

        p_out1 = np.concatenate([self.bu_conv2(pan_out2), fpn_out1], axis=-1)
        pan_out1 = self.C3_n3(p_out1)

        p_out0 = np.concatenate([self.bu_conv1(pan_out1), fpn_out0], axis=-1)
        pan_out0 = self.C3_n4(p_out0)

        return pan_out2, pan_out1, pan_out0


class YOLOXHead:
    """The decoupled head: one shared 1x1 stem per scale, then separate
    two-conv classification and regression branches, 1x1 predictions
    (object score folded into the regression branch's features), and the
    grid/stride box decode.
    """

    def __init__(self, sd, prefix="head", num_classes=NUM_CLASSES, strides=STRIDES):
        self.stems = [BaseConv(sd, f"{prefix}.stems.{i}", 1) for i in range(3)]
        self.cls_convs = [
            [DWConv(sd, f"{prefix}.cls_convs.{i}.{j}", 1) for j in range(2)]
            for i in range(3)
        ]
        self.reg_convs = [
            [DWConv(sd, f"{prefix}.reg_convs.{i}.{j}", 1) for j in range(2)]
            for i in range(3)
        ]
        self.cls_preds = [plain(sd, f"{prefix}.cls_preds.{i}") for i in range(3)]
        self.reg_preds = [plain(sd, f"{prefix}.reg_preds.{i}") for i in range(3)]
        self.obj_preds = [plain(sd, f"{prefix}.obj_preds.{i}") for i in range(3)]
        self.strides = strides

    def __call__(self, feats):
        outputs = []
        for i, x in enumerate(feats):
            x = self.stems[i](x)
            cls_feat = x
            for c in self.cls_convs[i]:
                cls_feat = c(cls_feat)
            reg_feat = x
            for c in self.reg_convs[i]:
                reg_feat = c(reg_feat)
            cw, cb = self.cls_preds[i]
            rw, rb = self.reg_preds[i]
            ow, ob = self.obj_preds[i]
            cls_out = conv2d(cls_feat, cw, cb)
            reg_out = conv2d(reg_feat, rw, rb)
            obj_out = conv2d(reg_feat, ow, ob)
            outputs.append(
                np.concatenate([reg_out, sigmoid(obj_out), sigmoid(cls_out)], axis=-1)
            )
        return self.decode_outputs(outputs)

    def decode_outputs(self, outputs):
        """Each scale's ``(x, y)`` offset by its own grid and ``(w, h)``
        exponentiated, both times the scale's stride: pure arithmetic over
        the raw predictions, no learned weights, so it runs on the host
        either side of the device (the LM ports' tokenizer decode is the
        same kind of step).
        """
        flat, grids, strides = [], [], []
        for out, stride in zip(outputs, self.strides):
            h, w, c = out.shape
            flat.append(out.reshape(h * w, c))
            yv, xv = np.meshgrid(np.arange(h), np.arange(w), indexing="ij")
            grids.append(np.stack([xv, yv], axis=-1).reshape(h * w, 2))
            strides.append(np.full((h * w, 1), stride, np.float32))
        flat = np.concatenate(flat, axis=0)
        grids = np.concatenate(grids, axis=0).astype(np.float32)
        strides = np.concatenate(strides, axis=0)
        xy = (flat[:, 0:2] + grids) * strides
        wh = np.exp(flat[:, 2:4]) * strides
        return np.concatenate([xy, wh, flat[:, 4:]], axis=-1)


class YOLOXNanoOracle:
    """YOLOX-Nano's forward pass in float32, from a channels-last
    ``(416, 416, 3)`` image to ``(3549, 85)`` detections (52**2 + 26**2 +
    13**2 anchors; ``xywh`` then objectness then 80 class scores).
    """

    def __init__(self, sd):
        self.pafpn = YOLOPAFPN(sd)
        self.head = YOLOXHead(sd)

    def __call__(self, image_hwc):
        return self.head(self.pafpn(image_hwc))


def load_checkpoint(path):
    """The real checkpoint's tensors as numpy, by their own (torch) names:
    this is the one place a YOLOX-Nano run path needs torch, since the
    upstream release ships a raw ``.pth``, not a HF/safetensors checkpoint.
    """
    import torch

    checkpoint = torch.load(path, map_location="cpu", weights_only=False)
    return {k: v.numpy() for k, v in checkpoint["model"].items()}
