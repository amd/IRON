# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.ImagePatches device-free: called in a graph, its steps record into
the caller's, bound by the caller's sizes; its reference is the resize, the
patch order and the gather each computed on their own; and it refuses an
image a call does not hold.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.lm import ImagePatches
from iron.operators.copy import Gather, GatherWords
from iron.operators.resample.op import PatchPositions, Resample, ResampleTaps

pytestmark = pytest.mark.usefixtures("npu2")


class Tower(iron.Graph):
    def __init__(self):
        self.processor = ImagePatches(256, (480, 640))

    def body(
        self,
        rgb,
        *,
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
    ):
        pixels, _, _ = self.processor(
            rgb,
            height=height,
            width=width,
            out_height=out_height,
            out_width=out_width,
        )
        return pixels


def test_a_caller_records_and_bounds_it():
    tower = Tower()
    rgb = tower.processor.resample.image_chunks, tower.processor.chunk
    recording = tower.record(rgb=(rgb, np.uint8))
    assert [type(s.op) for s in recording.steps] == [
        ResampleTaps,
        ResampleTaps,
        Resample,
        PatchPositions,
        GatherWords,
        Gather,
    ]
    named = {b.expression.value.name for b in recording.bindings}
    assert {"height", "width", "out_height", "out_width"} <= named
    assert {h.name for _, h in recording.states.values()} == {"processor.raster"}


def test_the_reference_is_its_parts_on_their_own():
    patches = ImagePatches(256, (480, 640))
    image = np.random.default_rng(0).integers(0, 256, (37, 53, 3), dtype=np.uint8)
    rgb, sizes = patches.pack(image, 96, 144)
    pixels, xy, ids = (np.asarray(a) for a in patches.reference(rgb, **sizes))
    h, w, ho, wo = (
        sizes["height"],
        sizes["width"],
        sizes["out_height"],
        sizes["out_width"],
    )
    taps_w = patches.taps_w.reference(in_samples=w, out_samples=wo)
    taps_h = patches.taps_h.reference(in_samples=h, out_samples=ho)
    raster = np.zeros(patches.raster.shape, pixels.dtype)
    patches.resample.reference(
        rgb,
        taps_w,
        taps_h,
        rows=h,
        columns=w,
        out_rows=ho,
        out_columns=wo,
        patches=raster,
    )
    want_xy, want_ids, order = patches.patch_positions.reference(
        out_rows=ho, out_columns=wo
    )
    assert np.array_equal(pixels.view(np.uint16), raster[order].view(np.uint16))
    assert np.array_equal(xy, want_xy.reshape(-1))
    assert np.array_equal(ids, want_ids.reshape(-1))


def test_an_image_a_call_does_not_hold_is_refused():
    patches = ImagePatches(256, (480, 640))
    with pytest.raises(ValueError, match="does not fit"):
        patches.pack(np.zeros((700, 800, 3), np.uint8), 96, 144)
