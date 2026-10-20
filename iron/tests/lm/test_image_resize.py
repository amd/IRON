#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.ImageResize feeding iron.lm.ImagePatches on a device, as SmolVLM
processes an image: Lanczos through a size of no whole patches, then to a
square, normalized. One compile, called on images of three sizes, its
pixels each exactly its reference's (each resize is torchvision's bit for
bit).
"""

import numpy as np
import pytest

import iron
from iron import Scratchpad
from iron.lm import ImagePatches, ImageResize
from iron.operators.resample.reference import Interpolation

pytestmark = pytest.mark.supported_devices("npu2")

# (height, width) of each image, and the size it is first resized to.
IMAGES = {
    "portrait": ((300, 200), (512, 342)),
    "small": ((37, 53), (358, 512)),
    "largest": ((480, 640), (384, 512)),
}


class Processor(iron.Graph):
    def __init__(self):
        lanczos = Interpolation.LANCZOS
        self.resize = ImageResize((480, 640), (512, 512), lanczos)
        self.patches = ImagePatches(
            256,
            (512, 512),
            pool=1,
            chunk=self.resize.pitch,
            interpolation=lanczos,
            mean=(0.5, 0.5, 0.5),
            std=(0.5, 0.5, 0.5),
            out=(256, 256),
        )

    def body(
        self,
        rgb,
        *,
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        mid_height: Scratchpad[np.int32],
        mid_width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
    ):
        mid = self.resize(
            rgb, height=height, width=width, out_height=mid_height, out_width=mid_width
        )
        pixels, _, _ = self.patches(
            mid,
            height=mid_height,
            width=mid_width,
            out_height=out_height,
            out_width=out_width,
        )
        return pixels


@pytest.fixture(scope="module")
def processor():
    graph = Processor()
    graph.compile(
        rgb=((graph.resize.resample.image_chunks, graph.resize.chunk), np.uint8)
    )
    yield graph


@pytest.mark.parametrize("name", list(IMAGES))
def test_image_resize_then_patches(processor, name):
    (h, w), (mh, mw) = IMAGES[name]
    image = np.random.default_rng(0).integers(0, 256, (h, w, 3), dtype=np.uint8)
    rgb, _ = processor.resize.pack(image, mh, mw)
    values = dict(
        height=h, width=w, mid_height=mh, mid_width=mw, out_height=256, out_width=256
    )
    got = np.asarray(processor(rgb, **values).numpy()).reshape(-1)
    want = np.asarray(processor.reference(rgb, **values)).reshape(-1)
    assert np.array_equal(got.view(np.uint16), want.view(np.uint16))
