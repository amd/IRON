#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.ImagePatches on a device: one compile, called on two images of
different sizes, its pixels, xy and position ids each exactly its
reference's (the resize is torchvision's bit for bit).
"""

import numpy as np
import pytest

from iron.lm import ImagePatches

pytestmark = pytest.mark.supported_devices("npu1", "npu2")

# (height, width) of each image, and the size it is resized to.
IMAGES = {
    "small": ((37, 53), (96, 144)),
    "photo": ((480, 640), (672, 912)),
}


@pytest.fixture(scope="module")
def patches():
    graph = ImagePatches(2560, (480, 640))
    graph.compile(rgb=((graph.resample.image_chunks, graph.chunk), np.uint8))
    yield graph


@pytest.mark.parametrize("name", list(IMAGES))
def test_image_patches(patches, name):
    (h, w), (ho, wo) = IMAGES[name]
    image = np.random.default_rng(0).integers(0, 256, (h, w, 3), dtype=np.uint8)
    rgb, sizes = patches.pack(image, ho, wo)
    got = [np.asarray(a.numpy()).reshape(-1) for a in patches(rgb, **sizes)]
    want = [np.asarray(a).reshape(-1) for a in patches.reference(rgb, **sizes)]
    for label, g, r in zip(("pixels", "xy", "position_ids"), got, want):
        assert np.array_equal(g.view(np.uint8), r.view(np.uint8)), label
