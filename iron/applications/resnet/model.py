#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""ResNet-50, an image classifier: one graph from an image to its class
logits (``ResNet``), its shape read from Hugging Face's ``resnet``
checkpoint's ``config.json`` and its weights by that checkpoint's names.

A 7x7 stride-2 stem and a 3x3 stride-2 max pool, then four stages of
bottlenecks (a 1x1 conv narrowing the channels by four, a 3x3 conv at the
stage's stride, a 1x1 conv widening them again, added to the input or to
its 1x1 projection, then ReLU), a global average pool and a linear
classifier. Every conv is bias-free, then BatchNorm, which folds into the
conv's weight and bias as it loads, then ReLU but the last of a
bottleneck. Channels-last throughout, as ``iron.functional``'s feature
maps; the image is ImageNet-normalized before the graph, and laid out in
2x2 blocks for the stem (``ResNet.inputs``).
"""

import dataclasses

import numpy as np
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron.lm import Linear
from iron.lm.config import Config, not_json
from iron.operators.relu import ReLU

#: nn.BatchNorm2d's default, which transformers' ResNet keeps.
BN_EPS = 1e-5
#: An image pixel's channels as the graph takes them: RGB and a zero.
PIXEL = 4


@dataclasses.dataclass(frozen=True)
class ResNetConfig(Config):
    """ResNet's shape as ``config.json`` names it: bottleneck stages of
    ``depths`` layers, each ``hidden_sizes`` wide, after an
    ``embedding_size``-wide stem. ``image_size`` is the square image the
    graph takes, the classifier's ``num_labels`` ImageNet's.
    """

    embedding_size: int
    hidden_sizes: tuple[int, ...] = dataclasses.field(metadata={"convert": tuple})
    depths: tuple[int, ...] = dataclasses.field(metadata={"convert": tuple})
    num_channels: int = 3
    layer_type: str = "bottleneck"
    hidden_act: str = "relu"
    downsample_in_first_stage: bool = False
    downsample_in_bottleneck: bool = False
    image_size: int = not_json(224)
    num_labels: int = not_json(1000)

    def __post_init__(self):
        given = (self.layer_type, self.hidden_act, self.downsample_in_bottleneck)
        if given != ("bottleneck", "relu", False):
            raise ValueError(
                f"ResNetConfig: only ResNet-50's bottleneck of ReLUs, downsampled "
                f"in its 3x3 conv, is built here, not {given}"
            )
        if self.image_size % 32:
            raise ValueError(
                f"ResNetConfig: a {self.image_size}-pixel image does not halve "
                "five times"
            )


class Convolution(iron.Graph):
    """A bias-free conv's float32 weight, as the checkpoint holds it, for
    its BatchNorm to fold into before it rounds.
    """

    def __init__(self, *shape: int):
        self.weight = iron.param(*shape, dtype=np.float32)


class BatchNorm(iron.Graph):
    """A BatchNorm's affine weights and running statistics, float32."""

    def __init__(self, channels: int):
        for name in ("weight", "bias", "running_mean", "running_var"):
            setattr(self, name, iron.param(channels, dtype=np.float32))
        self.num_batches_tracked = iron.param(dtype=np.int64)


class ConvLayer(iron.Graph):
    """A ``k``-square conv at ``stride``, same padding, its BatchNorm
    folded in as it loads, then ReLU where ``relu``.
    """

    def __init__(self, cin, cout, k=1, stride=1, relu=True):
        self.convolution = Convolution(cout, cin, k, k)
        self.normalization = BatchNorm(cout)
        self.stride, self.relu = stride, relu

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        bn = self.normalization
        self.weight, bias = F.fuse_conv_bn_weights(
            self.convolution.weight,
            None,
            bn.running_mean,
            bn.running_var,
            BN_EPS,
            bn.weight,
            bn.bias,
        )
        self.bias = bias.astype(bfloat16)

    def body(self, x):
        k = self.weight.shape[-1]
        y = F.conv2d(x, self.weight, self.bias, self.stride, k // 2)
        return ReLU.step(y) if self.relu else y


class Bottleneck(iron.Graph):
    """A bottleneck from ``cin`` channels to ``cout`` at ``stride``, its
    input projected (``shortcut``) where either changes.
    """

    def __init__(self, cin, cout, stride=1):
        mid = cout // 4
        self.shortcut = None
        if cin != cout or stride != 1:
            self.shortcut = ConvLayer(cin, cout, 1, stride, relu=False)
        self.layer = [
            ConvLayer(cin, mid),
            ConvLayer(mid, mid, 3, stride),
            ConvLayer(mid, cout, relu=False),
        ]

    def body(self, x):
        y = x
        for conv in self.layer:
            y = conv(y)
        residual = x if self.shortcut is None else self.shortcut(x)
        return ReLU.step(y + residual)


class Stage(iron.Graph):
    def __init__(self, cin, cout, depth, stride):
        self.layers = [Bottleneck(cin, cout, stride)]
        self.layers += [Bottleneck(cout, cout) for _ in range(depth - 1)]

    def body(self, x):
        for layer in self.layers:
            x = layer(x)
        return x


class Stem(ConvLayer):
    """The 7x7 stride-2 stem as a 4x4 conv at stride 1 over the image's
    2x2 space-to-depth (``ResNet.inputs``): its kernel zero-padded to 8x8
    (a tap before its first), each 2x2 block of taps one tap of the
    block's sixteen channels, so its patches are whole 64-element runs.
    """

    def __init__(self, c: ResNetConfig):
        super().__init__(c.num_channels, c.embedding_size, 7, 2)

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        out, channels = self.weight.shape[:2]
        w = np.zeros((out, PIXEL, 8, 8), np.float32)
        w[:, :channels, 1:, 1:] = self.weight
        # (out, c, u, p, v, q) to (out, p, q, c, u, v): channel (p, q, c).
        w = w.reshape(out, PIXEL, 4, 2, 4, 2).transpose(0, 3, 5, 1, 2, 4)
        self.weight = w.reshape(out, 4 * PIXEL, 4, 4)

    def body(self, x):
        y = F.conv2d(x, self.weight, self.bias)
        return ReLU.step(y)


class Embedder(iron.Graph):
    """The stem and its 3x3 stride-2 max pool."""

    def __init__(self, c: ResNetConfig):
        self.embedder = Stem(c)

    def body(self, x):
        return F.max_pool2d(self.embedder(x), 3, 2, 1)


class Encoder(iron.Graph):
    def __init__(self, c: ResNetConfig):
        widths = (c.embedding_size, *c.hidden_sizes)
        self.stages = [
            Stage(
                widths[i],
                widths[i + 1],
                depth,
                2 if i or c.downsample_in_first_stage else 1,
            )
            for i, depth in enumerate(c.depths)
        ]

    def body(self, x):
        for stage in self.stages:
            x = stage(x)
        return x


class Backbone(iron.Graph):
    def __init__(self, c: ResNetConfig):
        self.embedder = Embedder(c)
        self.encoder = Encoder(c)

    def body(self, x):
        return self.encoder(self.embedder(x))


class ResNet(iron.Graph):
    """ResNet on ``config``'s shape and a checkpoint's ``weights``, by its
    names: from an image as ``inputs`` lays it out to its ``num_labels``
    logits. The global average pool is a depthwise conv of the final map's
    size, every tap its mean's.
    """

    def __init__(self, config: ResNetConfig, weights):
        self.config = config
        self.resnet = Backbone(config)
        # transformers' classifier is a flatten, then the linear.
        self.classifier = [
            None,
            Linear(config.hidden_sizes[-1], config.num_labels),
        ]
        self.load_state_dict(weights)

    def inputs(self, image: np.ndarray) -> np.ndarray:
        """An ImageNet-normalized ``(size, size, 3)`` image as the graph
        takes it: a zero channel after RGB, zero-padded four pixels before
        and two after, and each 2x2 block of pixels one pixel of their
        sixteen channels, ``(S, S * 16)`` with ``S = size / 2 + 3``.
        """
        size = self.config.image_size
        padded = np.zeros((size + 6, size + 6, PIXEL), bfloat16)
        padded[4 : size + 4, 4 : size + 4, :3] = image
        S = size // 2 + 3
        blocks = padded.reshape(S, 2, S, 2, PIXEL).transpose(0, 2, 1, 3, 4)
        return np.ascontiguousarray(blocks).reshape(S, S * 4 * PIXEL)

    def body(self, image):
        S = image.shape[0]
        x = self.resnet(image.reshape(S, S, 4 * PIXEL))
        H, W, C = x.shape
        mean = np.full((C, 1, H, W), 1 / (H * W), np.float32)
        pooled = F.conv2d(x, mean, groups=C).reshape(1, C)
        return self.classifier[1](pooled)
