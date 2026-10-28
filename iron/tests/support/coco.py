# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""COCO val2017 photos, the images the vision models' tests see."""

import numpy as np

from iron.lm.testing import Download

VAL2017 = "https://s3.amazonaws.com/images.cocodataset.org/val2017"

# COCO val2017 photos (CC BY 4.0), as COCO's own host serves them, fetched
# once into IRON's cache.
COCO = {
    # 640x480.
    "cats": Download(
        f"{VAL2017}/000000039769.jpg",
        "dea9e7ef97386345f7cff32f9055da4982da5471c48d575146c796ab4563b04e",
    ),
    # 375x500, portrait.
    "stop_sign": Download(
        f"{VAL2017}/000000000724.jpg",
        "5c0e559c75d3969c8e3e297b61f61063f78045c9d4802b526ba616361f3823fd",
    ),
    # 640x426.
    "living_room": Download(
        f"{VAL2017}/000000000139.jpg",
        "ffe0f0cec3b2e27aab1967229cdf0a0d7751dcdd5800322f0b8ac0dffb3b8a8d",
    ),
    # 621x640.
    "baseball": Download(
        f"{VAL2017}/000000000872.jpg",
        "c2aa138ee3a59b057a7ba6fc5a6a18e62af531aa7dab78a7bfd33c1cd7e55eb6",
    ),
}


def photo(name: str) -> np.ndarray:
    """`COCO[name]`, fetched into IRON's cache and decoded:
    `(height, width, 3)` uint8.
    """
    # Pillow is a test requirement (requirements_examples.txt), not IRON's.
    from PIL import Image

    with Image.open(COCO[name].fetch()) as image:
        return np.array(image.convert("RGB"))
