#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOX-Nano from its released checkpoint, on COCO photos: the oracle
finds what the photos hold, and the graph, by its own reference and on the
NPU, detects as the oracle does.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16
from PIL import Image

from iron.applications.yolox.model import (
    INPUT_SIZE,
    YOLOXNano,
    YOLOXNanoOracle,
    decode,
    preprocess,
)
from iron.lm import Checkpoint
from iron.lm.testing import Download, require, weights_dir

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
