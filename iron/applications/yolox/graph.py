#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOX-Nano on the NPU: the same architecture ``model.py``'s
``YOLOXNanoOracle`` computes in float32 numpy, as one ``iron.Graph``, bf16
throughout. Shares no code with the oracle (a CNN's device graph and its
host reference are built from entirely different primitives: ``Conv2d``,
``MaxPool2d``, ``project`` and channel-concat here, plain numpy windows
there), only the checkpoint loading (``model.fold_bn``/``model.plain``).

Device-only accommodations, all exact (zero-padding, never an
approximation): a channel count here is sometimes too narrow for a bf16
DMA transfer (whole 4-byte/2-element units), a kernel's own vector step
(32 elements), or ``flm.GEMM``'s own verified ``tile_n`` floor (16, no
smaller one is hardware-verified) --

- Focus's four corner slices are 3 channels each (RGB): the caller pads
  the image to 4 channels (one more, zero) before this graph's call, so
  each corner is even; the stem conv's own weight is padded to match (a
  zero input channel contributes nothing, exactly).
- The head's three predictions are 4 (box), 1 (objectness) and 80
  (class) channels: padded to 16, 32 and 96 respectively (a zero weight
  row per extra channel, always exactly zero) -- 16 for box regression's
  own ``flm.GEMM`` (``N`` below 16 has no verified tiling at all), 32 and
  96 so objectness and class scores' ``Sigmoid`` tile sizes divide evenly
  by a multiple of 32 at every one of this model's feature-map widths,
  including 13 (odd). The model's own caller drops the padding columns
  before reading the detections.
"""

from pathlib import Path

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron.lm.blocks import Concat2, Concat3, Concat4, Conv2d, MaxPool2d, project
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd, RowwiseAdd
from iron.operators.flm.gemm.design import M_TILE, compute_rows
from iron.operators.sigmoid import Sigmoid
from iron.operators.silu import SiLU

from .model import BN_EPS, INPUT_SIZE, NUM_CLASSES, STRIDES, fold_bn, plain


def pad_stem_weight(weight):
    """``(16, 12, 3, 3)`` with a zero input channel after each of the
    Focus's four 3-channel corners: ``(16, 16, 3, 3)``, exact.
    """
    cout, cin, kh, kw = weight.shape
    assert cin == 12
    grouped = weight.reshape(cout, 4, 3, kh, kw)
    padded = np.zeros((cout, 4, 4, kh, kw), weight.dtype)
    padded[:, :, :3] = grouped
    return padded.reshape(cout, 16, kh, kw)


REG_PRED_CHANNELS = 16
OBJ_PRED_CHANNELS = 32
CLS_PRED_CHANNELS = 96


def pad_pred_channels(weight, bias, out_channels):
    """A conv's ``(weight, bias)`` padded with extra all-zero output
    channels, exact. For box regression (``flm.GEMM``'s ``N`` floor: no
    verified ``tile_n`` below 16), and for objectness and class scores
    (``Sigmoid``'s 32-element vector step: ``width * channels`` must
    itself be a multiple of 32 at every one of this model's three
    feature-map widths -- 13, 26, 52 -- and only channels contributes
    that factor at 13, odd). The caller drops the padding columns before
    reading real predictions.
    """
    n = weight.shape[0]
    out_w = np.zeros((out_channels, *weight.shape[1:]), weight.dtype)
    out_w[:n] = weight
    out_b = np.zeros((out_channels,), bias.dtype)
    out_b[:n] = bias
    return out_w, out_b


def sigmoid_tile_size(width, channels, cap=4096):
    """A whole number of rows' worth of ``width * channels`` elements,
    halved until it fits a single core's tile (``Sigmoid.tile_cap``).
    """
    tile = width * channels
    while tile > cap:
        assert tile % 2 == 0, f"sigmoid_tile_size: {tile} has no even half below {cap}"
        tile //= 2
    return tile


def tiled_bias(bias, width):
    """``bias`` (``Cout``,), repeated once a width position: the row
    ``RowwiseAdd`` holds beside a channels-last line.
    """
    return np.tile(np.asarray(bias, np.float32), width).astype(bfloat16)


class _RowPad:
    """``padding`` zero rows either side, physically written: ``Conv2d``'s
    own ``padding`` only reaches the width dimension (a band matrix's zero
    weight entries); the row dimension is "rows the input holds, so a
    producer writes past them in place" (its own docstring) -- every
    depthwise/single-channel 3x3 conv in this model needs this (the dense
    stem conv needs both dimensions physically padded instead, ``_SpatialPad``).
    """

    def __init__(self, rows: int, width: int, channels: int, padding: int):
        self.rows, self.width, self.channels, self.padding = (
            rows,
            width,
            channels,
            padding,
        )
        self.padded_rows = rows + 2 * padding
        self.border = np.zeros((self.padded_rows, width * channels), bfloat16)
        self.padded = iron.state((self.padded_rows, width * channels))

    def __call__(self, x):
        p, w, c = self.padding, self.width, self.channels
        Copy(self.border, self.padded)
        interior = TensorAccessPattern(
            (self.padded_rows, w * c), p * w * c, [self.rows, w * c], [w * c, 1]
        )
        Copy(x, self.padded, dst=interior)
        return Copy(self.padded[:])


class ConvBlock:
    """``BaseConv``: a 1x1 conv is ``project`` (no spatial gather at all);
    wider or depthwise is ``Conv2d``. Either way, BatchNorm folds into the
    conv's own ``(weight, bias)``, and ``SiLU`` follows.
    """

    def __init__(
        self,
        sd,
        prefix,
        width,
        rows=None,
        stride=1,
        groups=1,
        weight_bias=None,
        padding=None,
    ):
        weight, bias = (
            weight_bias if weight_bias is not None else fold_bn(sd, prefix, BN_EPS)
        )
        kernel = weight.shape[-1]
        self.out_channels = weight.shape[0]
        if kernel == 1 and stride == 1 and groups == 1:
            self.conv = None
            self.weight2d = weight[:, :, 0, 0].astype(bfloat16)
            self.bias = np.asarray(bias, np.float32).astype(bfloat16)
            self.out_width = width
            # project() is one pixel a row (GEMM's own convention, a
            # token's); every other op here is channels-last image rows
            # (one row, many pixels), so a 1x1 conv reshapes to pixel rows
            # around the projection and back.
            self.rows = rows if rows is not None else width
            self.in_channels = weight.shape[1]
            self._init_proj_pad()
        else:
            if padding is None:
                padding = (kernel - 1) // 2  # "same" padding, every BaseConv's own
            self.row_pad = None
            if padding > 0 and groups > 1:
                # Depthwise (banded): Conv2d's own padding covers the width
                # band; the rows must still be physically pre-padded.
                rows = rows if rows is not None else width
                channels_in = weight.shape[1] * groups
                self.row_pad = _RowPad(rows, width, channels_in, padding)
            self.conv = Conv2d(
                weight, width, stride=stride, padding=padding, groups=groups
            )
            self.bias_row = tiled_bias(bias, self.conv.out_width)
            self.out_width = self.conv.out_width

    def _init_proj_pad(self):
        """``flm.GEMM`` needs its pixel-row count (M) to be a whole multiple
        of ``M_TILE * compute_rows(dev)`` (256 on this device); none of this
        model's feature maps (104x104 down to 13x13) naturally are. Pad rows
        up to that multiple here, project, then slice back in `_project` --
        the padding rows' own output is never read, so padding with zero
        (written once, not per call) is exact, not approximate.
        """
        dev = aie_utils.ensure_current_device()
        unit = M_TILE * compute_rows(dev)
        self.real_rows = self.rows * self.out_width
        pad = (-self.real_rows) % unit
        self.pad_rows = self.real_rows + pad
        if pad:
            self.proj_border = np.zeros((self.pad_rows, self.in_channels), bfloat16)
            self.proj_padded = iron.state((self.pad_rows, self.in_channels))
        else:
            self.proj_padded = None

    def _project(self, pixels):
        if self.proj_padded is None:
            x = pixels
        else:
            Copy(self.proj_border, self.proj_padded)
            dst = TensorAccessPattern(
                (self.pad_rows, self.in_channels),
                0,
                [self.real_rows, self.in_channels],
                [self.in_channels, 1],
            )
            Copy(pixels, self.proj_padded, dst=dst)
            x = Copy(self.proj_padded[:])
        y = project(x, self.weight2d, bias=self.bias, small=True)
        return y if self.proj_padded is None else y[: self.real_rows]

    def __call__(self, x):
        # A feature map's width (13 at dark5's scale) is prime, so an
        # auto-resolved tile_size can fail to divide rows * width *
        # channels; a whole row (width * channels) always does, and is a
        # multiple of the kernel's own 32-element vector step for every
        # shape this model has (channels alone is too, past the stem's 16).
        if self.conv is None:
            pixels = x.reshape(self.rows * self.out_width, self.in_channels)
            y = self._project(pixels)
            out = SiLU(y, tile_size=self.out_width * self.out_channels)
            return out.reshape(self.rows, self.out_width * self.out_channels)
        if self.row_pad is not None:
            x = self.row_pad(x)
        # Every feature map in this model is square (rows == width), so
        # the output row bound Conv2d's own per-call `rows` needs is the
        # same number as out_width, computed from the same formula.
        y = RowwiseAdd(self.conv(x, rows=self.conv.out_width), self.bias_row)
        return SiLU(y, tile_size=self.out_width * self.out_channels)


class DWBlock:
    """``DWConv``: a depthwise 3x3 (``ConvBlock`` with ``groups=channels``)
    then a pointwise 1x1, each its own ``ConvBlock``.
    """

    def __init__(self, sd, prefix, width, stride, channels):
        self.dconv = ConvBlock(
            sd, f"{prefix}.dconv", width, stride=stride, groups=channels
        )
        self.pconv = ConvBlock(sd, f"{prefix}.pconv", self.dconv.out_width)
        self.out_width = self.pconv.out_width

    def __call__(self, x):
        return self.pconv(self.dconv(x))


class BottleneckBlock:
    """1x1 then a depthwise-separable 3x3, added back to its input when
    the caller says the shapes agree (always, inside a ``CSPBlock``).
    """

    def __init__(self, sd, prefix, width, channels, shortcut):
        self.conv1 = ConvBlock(sd, f"{prefix}.conv1", width)
        self.conv2 = DWBlock(sd, f"{prefix}.conv2", self.conv1.out_width, 1, channels)
        self.use_add = shortcut
        self.channels = channels
        self.out_width = self.conv2.out_width

    def __call__(self, x):
        y = self.conv2(self.conv1(x))
        tile = self.out_width * self.channels
        return ElementwiseAdd(y, x, tile_size=tile) if self.use_add else y


class CSPBlock:
    """ "C3": a 1x1 conv run through ``n`` bottlenecks, beside a second 1x1
    conv of the same input, concatenated (``Concat2``) and projected by a
    third 1x1 conv.
    """

    def __init__(self, sd, prefix, width, rows, out_channels, n, shortcut=True):
        self.conv1 = ConvBlock(sd, f"{prefix}.conv1", width)
        self.conv2 = ConvBlock(sd, f"{prefix}.conv2", width)
        hidden = out_channels // 2
        self.m = []
        for i in range(n):
            self.m.append(
                BottleneckBlock(
                    sd, f"{prefix}.m.{i}", self.conv1.out_width, hidden, shortcut
                )
            )
        self.cat = Concat2(rows=rows, width=width, channels=(hidden, hidden))
        self.conv3 = ConvBlock(sd, f"{prefix}.conv3", width)
        self.out_width = self.conv3.out_width

    def __call__(self, x):
        x1 = self.conv1(x)
        for b in self.m:
            x1 = b(x1)
        x2 = self.conv2(x)
        return self.conv3(self.cat(x1, x2))


class _SpatialPad:
    """One zero pixel's border, physically written: ``Conv2d``'s dense
    (not depthwise) multi-channel path holds no padding of its own,
    unlike the single-channel/depthwise band (every other 3x3 conv in
    this model), so its one caller (the stem conv, the one regular,
    non-depthwise 3x3) pre-pads here instead.
    """

    def __init__(self, rows: int, width: int, channels: int):
        self.rows, self.width, self.channels = rows, width, channels
        padded_rows, padded_width = rows + 2, width + 2
        self.padded_rows, self.padded_width = padded_rows, padded_width
        self.border = np.zeros((padded_rows, padded_width * channels), bfloat16)
        self.padded = iron.state((padded_rows, padded_width * channels))

    def __call__(self, x):
        pw, c = self.padded_width, self.channels
        Copy(self.border, self.padded)
        interior = TensorAccessPattern(
            (self.padded_rows, pw * c),
            pw * c + c,
            [self.rows, self.width * c],
            [pw * c, 1],
        )
        Copy(x, self.padded, dst=interior)
        return Copy(self.padded[:])


class FocusBlock:
    """The backbone's stem: 2x2 space-to-depth (the real source's own
    corner order, top-left/bottom-left/top-right/bottom-right) into the
    channel axis, then a 3x3 ``ConvBlock``. The caller's image is already
    padded to 4 channels (one more than RGB, zero); the stem conv's own
    weight is padded to match (``pad_stem_weight``), so every corner slice
    is an even (4) channel count, the DMA's own requirement. The
    concatenated 16-channel plane is also padded a pixel either side
    first (``_SpatialPad``): the stem conv is the one regular (not
    depthwise), multi-channel 3x3 in this model, and that path holds no
    padding of its own.
    """

    def __init__(self, sd, prefix, size):
        self.size = size
        self.half = size // 2
        weight, bias = fold_bn(sd, f"{prefix}.conv", BN_EPS)
        padded = pad_stem_weight(weight)
        self.cat = Concat4(rows=self.half, width=self.half, channels=(4, 4, 4, 4))
        self.spatial_pad = _SpatialPad(self.half, self.half, 16)
        self.conv = ConvBlock(
            sd, None, self.half + 2, weight_bias=(padded, bias), padding=0
        )
        self.out_width = self.conv.out_width

    def _corner(self, x, row0, col0):
        size, half = self.size, self.half
        view = TensorAccessPattern(
            (size, size * 4),
            row0 * size * 4 + col0 * 4,
            [half, half, 4],
            [2 * size * 4, 2 * 4, 1],
        )
        return Copy(x, src=view).reshape(half, half * 4)

    def __call__(self, x):
        tl = self._corner(x, 0, 0)
        bl = self._corner(x, 1, 0)
        tr = self._corner(x, 0, 1)
        br = self._corner(x, 1, 1)
        return self.conv(self.spatial_pad(self.cat(tl, bl, tr, br)))


class SPPBlock:
    """Spatial pyramid pooling: a 1x1 conv, three parallel same-padded max
    pools (kernel 5, 9, 13, stride 1) over its output, joined with it
    (``Concat4``), then a second 1x1 conv back down.
    """

    def __init__(self, sd, prefix, width, rows, kernel_sizes=(5, 9, 13)):
        self.conv1 = ConvBlock(sd, f"{prefix}.conv1", width)
        c = self.conv1.out_channels
        self.pools = [
            MaxPool2d(rows=rows, width=width, channels=c, kernel=k)
            for k in kernel_sizes
        ]
        self.cat = Concat4(rows=rows, width=width, channels=(c, c, c, c))
        self.conv2 = ConvBlock(sd, f"{prefix}.conv2", width)
        self.out_width = self.conv2.out_width

    def __call__(self, x):
        x = self.conv1(x)
        pooled = [pool(x) for pool in self.pools]
        return self.conv2(self.cat(x, *pooled))


class CSPDarknetGraph:
    """The backbone: the stem, then four stride-2 stages (dark2-dark5),
    each a depthwise-separable downsample into a CSP block; dark5's block
    follows an SPP. Returns dark3, dark4, dark5 (the neck's three inputs).
    """

    def __init__(self, sd, prefix="backbone.backbone", bc=16, bd=1, size=INPUT_SIZE):
        self.stem = FocusBlock(sd, f"{prefix}.stem", size)
        w = self.stem.out_width
        rows = w

        self.dark2_down = DWBlock(sd, f"{prefix}.dark2.0", w, 2, bc)
        w2, rows2 = self.dark2_down.out_width, rows // 2
        self.dark2_csp = CSPBlock(sd, f"{prefix}.dark2.1", w2, rows2, bc * 2, bd)

        self.dark3_down = DWBlock(sd, f"{prefix}.dark3.0", w2, 2, bc * 2)
        w3, rows3 = self.dark3_down.out_width, rows2 // 2
        self.dark3_csp = CSPBlock(sd, f"{prefix}.dark3.1", w3, rows3, bc * 4, bd * 3)

        self.dark4_down = DWBlock(sd, f"{prefix}.dark4.0", w3, 2, bc * 4)
        w4, rows4 = self.dark4_down.out_width, rows3 // 2
        self.dark4_csp = CSPBlock(sd, f"{prefix}.dark4.1", w4, rows4, bc * 8, bd * 3)

        self.dark5_down = DWBlock(sd, f"{prefix}.dark5.0", w4, 2, bc * 8)
        w5, rows5 = self.dark5_down.out_width, rows4 // 2
        self.dark5_spp = SPPBlock(sd, f"{prefix}.dark5.1", w5, rows5)
        self.dark5_csp = CSPBlock(
            sd, f"{prefix}.dark5.2", w5, rows5, bc * 16, bd, shortcut=False
        )

        self.widths = {
            "dark3": (rows3, w3, bc * 4),
            "dark4": (rows4, w4, bc * 8),
            "dark5": (rows5, w5, bc * 16),
        }

    def __call__(self, x):
        x = self.stem(x)
        x = self.dark2_csp(self.dark2_down(x))
        dark3 = self.dark3_csp(self.dark3_down(x))
        dark4 = self.dark4_csp(self.dark4_down(dark3))
        dark5 = self.dark5_csp(self.dark5_spp(self.dark5_down(dark4)))
        return dark3, dark4, dark5


class Upsample2x:
    """Nearest-neighbor 2x upsample: each pixel repeated into a 2x2 block,
    channels-last, so a column run repeats too.

    A single 5-dimensional gather (row-repeat and column-repeat both a
    stride-0 source dim) traces and references fine but aiecc's real
    ``aie.dma_bd`` lowering refuses it ("has 5 dimensions, and no split
    into at most 1024 descriptors of 4 fits this tile") -- a device-free
    blind spot, caught only by compiling the real model. Row-repeat (one
    stride-0 dim, 3 total) lowers fine split out on its own; a 4-dim
    gather with a stride-0 dim in this position does not ("Stride 1 must
    be a positive integer"). Column-repeat instead writes the row-doubled
    buffer twice, into interleaved even/odd destination column slots (no
    stride-0 dimension at all) -- the same idiom
    ``_ConcatChannelsBase`` already uses for its own interleaved writes.
    """

    def __init__(self, rows: int, width: int, channels: int):
        self.rows, self.width, self.channels = rows, width, channels
        self.row_doubled = iron.state((rows * 2, width * channels))
        self.out = iron.state((rows * 2, width * 2 * channels))

    def __call__(self, x):
        line = self.width * self.channels
        out_line = self.width * 2 * self.channels
        rows_view = TensorAccessPattern(
            (self.rows, line), 0, [self.rows, 2, line], [line, 0, 1]
        )
        Copy(x, self.row_doubled, src=rows_view)
        for col_offset in (0, self.channels):
            dst = TensorAccessPattern(
                (self.rows * 2, out_line),
                col_offset,
                [self.rows * 2, self.width, self.channels],
                [out_line, 2 * self.channels, 1],
            )
            Copy(self.row_doubled[:], self.out, dst=dst)
        return Copy(self.out[:])


class YOLOPAFPNGraph:
    """The neck: top-down (lateral 1x1 convs, 2x upsample, concat, CSP
    block) then bottom-up (depthwise-separable downsample, concat, CSP
    block), over the backbone's three feature maps.
    """

    def __init__(self, sd, prefix="backbone", bc=16, bd=1, size=INPUT_SIZE):
        self.backbone = CSPDarknetGraph(sd, f"{prefix}.backbone", bc, bd, size)
        rows3, w3, c3 = self.backbone.widths["dark3"]
        rows4, w4, c4 = self.backbone.widths["dark4"]
        rows5, w5, c5 = self.backbone.widths["dark5"]

        self.lateral_conv0 = ConvBlock(sd, f"{prefix}.lateral_conv0", w5)
        self.up0 = Upsample2x(rows5, w5, c4)
        self.cat_p4 = Concat2(rows=rows4, width=w4, channels=(c4, c4))
        self.C3_p4 = CSPBlock(
            sd, f"{prefix}.C3_p4", w4, rows4, bc * 8, bd, shortcut=False
        )

        self.reduce_conv1 = ConvBlock(sd, f"{prefix}.reduce_conv1", w4)
        self.up1 = Upsample2x(rows4, w4, c3)
        self.cat_p3 = Concat2(rows=rows3, width=w3, channels=(c3, c3))
        self.C3_p3 = CSPBlock(
            sd, f"{prefix}.C3_p3", w3, rows3, bc * 4, bd, shortcut=False
        )

        self.bu_conv2 = DWBlock(sd, f"{prefix}.bu_conv2", w3, 2, bc * 4)
        self.cat_n3 = Concat2(rows=rows4, width=w4, channels=(bc * 4, bc * 4))
        self.C3_n3 = CSPBlock(
            sd, f"{prefix}.C3_n3", w4, rows4, bc * 8, bd, shortcut=False
        )

        self.bu_conv1 = DWBlock(sd, f"{prefix}.bu_conv1", w4, 2, bc * 8)
        self.cat_n4 = Concat2(rows=rows5, width=w5, channels=(bc * 8, bc * 8))
        self.C3_n4 = CSPBlock(
            sd, f"{prefix}.C3_n4", w5, rows5, bc * 16, bd, shortcut=False
        )

        self.scales = [(rows3, w3, bc * 4), (rows4, w4, bc * 8), (rows5, w5, bc * 16)]

    def __call__(self, x):
        x2, x1, x0 = self.backbone(x)
        rows3, w3, c3 = self.scales[0]
        rows4, w4, c4 = self.scales[1]
        rows5, w5, c5 = self.scales[2]

        fpn_out0 = self.lateral_conv0(x0)
        up0 = self.up0(fpn_out0)
        f_out0 = self.C3_p4(self.cat_p4(up0, x1))

        fpn_out1 = self.reduce_conv1(f_out0)
        up1 = self.up1(fpn_out1)
        pan_out2 = self.C3_p3(self.cat_p3(up1, x2))

        p_out1 = self.cat_n3(self.bu_conv2(pan_out2), fpn_out1)
        pan_out1 = self.C3_n3(p_out1)

        p_out0 = self.cat_n4(self.bu_conv1(pan_out1), fpn_out0)
        pan_out0 = self.C3_n4(p_out0)

        return pan_out2, pan_out1, pan_out0


class YOLOXHeadGraph:
    """The decoupled head: one shared 1x1 stem per scale, separate
    two-conv classification and regression branches, 1x1 predictions.
    Objectness (1 real channel) and class scores (``num_classes`` real
    channels) are both zero-padded to a multiple of 32 so that the
    Sigmoid applied to each divides evenly into the kernel's 32-element
    vector step at every feature-map width this model uses, including
    13 (odd); see ``pad_pred_channels``. The caller drops the padding
    columns before reading real predictions.
    """

    def __init__(self, sd, prefix, scales, num_classes=NUM_CLASSES):
        self.stems, self.cls_convs, self.reg_convs = [], [], []
        self.cls_preds, self.reg_preds, self.obj_preds = [], [], []
        self.cats = []
        self.w2s = []
        self.rows_widths = scales
        for i, (rows, width, channels) in enumerate(scales):
            stem = ConvBlock(sd, f"{prefix}.stems.{i}", width)
            w = stem.out_width
            cls = [
                DWBlock(sd, f"{prefix}.cls_convs.{i}.{j}", w, 1, 64) for j in range(2)
            ]
            reg = [
                DWBlock(sd, f"{prefix}.reg_convs.{i}.{j}", w, 1, 64) for j in range(2)
            ]
            w2 = cls[-1].out_width
            cls_w, cls_b = plain(sd, f"{prefix}.cls_preds.{i}")
            reg_w, reg_b = plain(sd, f"{prefix}.reg_preds.{i}")
            obj_w, obj_b = plain(sd, f"{prefix}.obj_preds.{i}")
            reg_w, reg_b = pad_pred_channels(reg_w, reg_b, REG_PRED_CHANNELS)
            obj_w, obj_b = pad_pred_channels(obj_w, obj_b, OBJ_PRED_CHANNELS)
            cls_w, cls_b = pad_pred_channels(cls_w, cls_b, CLS_PRED_CHANNELS)
            # plain() already reads the checkpoint's own 4D conv weight
            # (Cout, Cin, 1, 1); ConvBlock's project path reduces it to
            # 2D itself.
            cls_pred = ConvBlock(sd, None, w2, weight_bias=(cls_w, cls_b))
            reg_pred = ConvBlock(sd, None, w2, weight_bias=(reg_w, reg_b))
            obj_pred = ConvBlock(sd, None, w2, weight_bias=(obj_w, obj_b))
            self.stems.append(stem)
            self.cls_convs.append(cls)
            self.reg_convs.append(reg)
            self.cls_preds.append(cls_pred)
            self.reg_preds.append(reg_pred)
            self.obj_preds.append(obj_pred)
            self.cats.append(
                Concat3(
                    rows=rows,
                    width=w2,
                    channels=(REG_PRED_CHANNELS, OBJ_PRED_CHANNELS, CLS_PRED_CHANNELS),
                )
            )
            self.w2s.append(w2)
        self.strides = STRIDES

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
            # cls_pred/reg_pred/obj_pred are plain 1x1 convs with a real
            # bias (no BatchNorm, no SiLU): skip ConvBlock's own silu() by
            # calling its pieces directly.
            cls_out = _plain_conv(self.cls_preds[i], cls_feat)
            reg_out = _plain_conv(self.reg_preds[i], reg_feat)
            obj_out = _plain_conv(self.obj_preds[i], reg_feat)
            w2 = self.w2s[i]
            # Detection confidence (objectness, class scores) is read
            # directly by the caller's threshold/NMS, not fed through
            # further learned weights: the LUT's tighter tolerance is
            # worth its extra cycles here, unlike the backbone's SiLUs.
            obj_sig = Sigmoid(
                obj_out,
                tile_size=sigmoid_tile_size(w2, OBJ_PRED_CHANNELS),
                use_lut=True,
            )
            cls_sig = Sigmoid(
                cls_out,
                tile_size=sigmoid_tile_size(w2, CLS_PRED_CHANNELS),
                use_lut=True,
            )
            outputs.append(self.cats[i](reg_out, obj_sig, cls_sig))
        return outputs


def _plain_conv(block, x):
    """A prediction conv's own output, no BatchNorm fold, no activation:
    ``ConvBlock`` built it with a real (weight, bias) and kernel 1, so its
    ``conv`` is always ``None`` (``project`` path); bypass its ``SiLU``,
    reshaping to and from pixel rows the same way ``ConvBlock`` itself does.
    """
    pixels = x.reshape(block.rows * block.out_width, block.in_channels)
    y = block._project(pixels)
    return y.reshape(block.rows, block.out_width * block.out_channels)


class YOLOXNanoGraph(iron.Graph):
    """YOLOX-Nano on the NPU: a ``(416, 416, 4)`` image (RGB padded to 4
    channels, zero) in, the three scales' raw ``(reg, obj_padded, cls)``
    feature maps out -- the grid/stride box decode is pure arithmetic over
    the raw predictions, no learned weights, so it runs on the host, like
    every other model's sampling or tokenizer decode.
    """

    profile = Path(__file__).with_name("profiles")

    def __init__(self, sd, num_classes=NUM_CLASSES, size=INPUT_SIZE):
        self.pafpn = YOLOPAFPNGraph(sd, size=size)
        self.head = YOLOXHeadGraph(sd, "head", self.pafpn.scales, num_classes)

    def body(self, pixels):
        feats = self.pafpn(pixels)
        return self.head(feats)
