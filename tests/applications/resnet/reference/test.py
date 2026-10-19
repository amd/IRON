#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""ResNet's graph, by its own reference, against transformers'
ResNetForImageClassification in float32 over the same random weights at a
toy shape, its logits recorded in ``goldens/``, device-free.
"""

import dataclasses

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.resnet.model import ResNet, ResNetConfig
from iron.lm.golden import HuggingFace
from iron.lm.testing import assert_close
from iron.tests.support.llama_model import checkpoint

pytestmark = pytest.mark.usefixtures("npu2")

#: The logits' bound, a share of the largest: the toy measures under 1%,
#: and an average pool scaled by 1.03 moves them 3.1%.
RESNET = 0.02

#: ResNet-50's widths, its stages one bottleneck deep but the first, of
#: two, the second's shortcut the identity, on a 96-pixel image, so the
#: average pool takes a 3x3 map.
TOY = ResNetConfig(
    embedding_size=64,
    hidden_sizes=(256, 512, 1024, 2048),
    depths=(2, 1, 1, 1),
    image_size=96,
    num_labels=10,
)


class HuggingFaceResNet(HuggingFace):
    """transformers' ResNetForImageClassification: an image's logits."""

    model_class = "AutoModelForImageClassification"

    def logits(self, tokens, image) -> np.ndarray:
        import torch

        pixels = torch.from_numpy(image.astype(np.float32).transpose(2, 0, 1).copy())
        with torch.no_grad():
            return self.model(pixel_values=pixels[None]).logits[0].numpy()


def names(c: ResNetConfig) -> dict[str, tuple[int, ...]]:
    """Each float tensor of a ResNet checkpoint of ``c``'s shape, by name;
    every BatchNorm also holds an int64 ``num_batches_tracked``.
    """
    out = {}

    def conv(path, cin, cout, k=1):
        out[f"{path}.convolution.weight"] = (cout, cin, k, k)
        for name in ("weight", "bias", "running_mean", "running_var"):
            out[f"{path}.normalization.{name}"] = (cout,)

    conv("resnet.embedder.embedder", c.num_channels, c.embedding_size, 7)
    widths = (c.embedding_size, *c.hidden_sizes)
    for s, depth in enumerate(c.depths):
        for i in range(depth):
            p = f"resnet.encoder.stages.{s}.layers.{i}"
            cin, cout = widths[s + 1] if i else widths[s], widths[s + 1]
            if cin != cout or (s and not i):
                conv(f"{p}.shortcut", cin, cout)
            conv(f"{p}.layer.0", cin, cout // 4)
            conv(f"{p}.layer.1", cout // 4, cout // 4, 3)
            conv(f"{p}.layer.2", cout // 4, cout)
    out["classifier.1.weight"] = (c.num_labels, c.hidden_sizes[-1])
    out["classifier.1.bias"] = (c.num_labels,)
    return out


def tree(c: ResNetConfig, dtype: str = "BF16"):
    """Random ``dtype`` weights of ``c``'s shape, each BatchNorm's running mean about
    zero rather than the draw's one, which would leave every ReLU of a
    random net dead, its running variance log-uniform down to 1e-4, where
    its epsilon counts, and its count of batches beside them.
    """
    named = names(c)
    weights = checkpoint(c, named, dtype).tree("random")
    rng = np.random.default_rng(1)
    for name in named:
        if name.endswith("normalization.weight"):
            node = weights
            for part in name.split(".")[:-1]:
                node = node[int(part)] if part.isdigit() else getattr(node, part)
            node.running_mean -= 1
            var = np.exp(rng.uniform(np.log(1e-4), 0, node.running_var.shape))
            node.running_var[:] = var
            node.num_batches_tracked = np.zeros((), np.int64)
    return weights


@pytest.fixture(scope="module")
def toy(golden):
    weights = tree(TOY)
    reference = golden(
        "toy",
        lambda: HuggingFaceResNet.build("resnet", TOY, weights, num_labels=10),
        TOY,
        weights,
    )
    return weights, reference


def test_the_graph_classifies_as_transformers(toy):
    weights, reference = toy
    model = ResNet(TOY, weights)
    S = TOY.image_size
    for seed in range(2):
        image = np.random.default_rng(seed).standard_normal((S, S, 3))
        image = image.astype(bfloat16)
        got = model.reference(model.inputs(image))
        assert_close(got, reference.logits((), image), share=RESNET)


def test_a_float32_conv_weight_rounds_only_after_its_fold():
    weights = tree(TOY, "F32")
    layer = ResNet(TOY, weights).resnet.encoder.stages[0].layers[0].layer[0]
    w = weights.resnet.encoder.stages[0].layers[0].layer[0]
    bn = {k: np.asarray(v, np.float64) for k, v in vars(w.normalization).items()}
    scale = bn["weight"] / np.sqrt(bn["running_var"] + layer.normalization.eps)
    want = np.asarray(w.convolution.weight, np.float64) * scale[:, None, None, None]
    # float32's rounding, where a bf16 weight before the fold is 2^-9 off.
    np.testing.assert_allclose(layer.weight, want, rtol=1e-6)


@pytest.mark.parametrize("size", [64, 224])
def test_every_step_of_resnet50_resolves(size, npu2):
    """Each step's operator at ResNet-50's depths takes a shape npu2 builds."""
    c = dataclasses.replace(TOY, depths=(3, 4, 6, 3), image_size=size)
    S = size // 2 + 3
    recording = ResNet(c, tree(c)).record(image=((S, S * 16), bfloat16))
    for step in recording.steps:
        step.op.resolved(npu2)


def test_another_bottleneck_or_activation_is_refused():
    with pytest.raises(ValueError, match="only ResNet-50's bottleneck"):
        dataclasses.replace(TOY, layer_type="basic")
