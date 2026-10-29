# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.ImagePatches device-free: called in a graph, its steps record into
the caller's, bound by the caller's sizes; its reference is the resize, the
patch order and the gather each computed on their own; and it refuses an
image a call does not hold. Through iron.lm.ImageResize, its pixels are
both resizes and the normalization computed on their own.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.device import from_name
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.lm import ImagePatches, ImageResize
from iron.operators.copy import Gather, GatherWords
from iron.operators.resample.op import PatchPositions, Resample, ResampleTaps
from iron.operators.resample.reference import Interpolation, resize

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


@pytest.mark.parametrize(
    "image,mid", [((300, 200), (512, 342)), ((37, 53), (358, 512))]
)
def test_patches_through_a_resized_image_are_both_resizes(image, mid):
    """SmolVLM's processing: Lanczos to ``mid``, a size no whole patches
    give, then to 256x256, normalized to ``[-1, 1]``, raster order.
    """
    lanczos = Interpolation.LANCZOS
    through = ImageResize((480, 640), (512, 512), lanczos)
    patches = ImagePatches(
        256,
        (512, 512),
        pool=1,
        chunk=through.pitch,
        interpolation=lanczos,
        mean=(0.5, 0.5, 0.5),
        std=(0.5, 0.5, 0.5),
        out=(256, 256),
    )
    pixels = np.random.default_rng(0).integers(0, 256, (*image, 3), dtype=np.uint8)
    rgb, sizes = through.pack(pixels, *mid)
    resized = np.asarray(through.reference(rgb, **sizes))
    got, _, _ = patches.reference(
        resized, height=mid[0], width=mid[1], out_height=256, out_width=256
    )
    out = resize(resize(pixels, *mid, lanczos), 256, 256, lanczos)
    want = ((out.astype(np.float32) - 127.5) / np.float32(127.5)).astype(bfloat16)
    want = want.reshape(16, 16, 16, 16, 3).transpose(0, 2, 1, 3, 4).reshape(256, -1)
    assert np.array_equal(np.asarray(got).view(np.uint16), want.view(np.uint16))


def test_a_resize_past_a_core_s_memory_splits_into_passes_that_resize_alike():
    """npu1's cores can't hold a 2048-wide resize's patch columns in one
    pass; two passes over halves of one taps table give the same image.
    """
    lanczos = Interpolation.LANCZOS
    pixels = np.random.default_rng(1).integers(0, 256, (900, 1000, 3), dtype=np.uint8)
    with aie_utils.set_current_device(from_name("npu1", n_cols=4)):
        split = ImageResize((1024, 1024), (2048, 2048), lanczos)
        rgb, sizes = split.pack(pixels, 2048, 2048)
        got = np.asarray(split.reference(rgb, **sizes))
    assert split.passes == 2
    assert ImageResize((1024, 1024), (2048, 2048), lanczos).passes == 1
    image = got.reshape(-1, split.pitch // 3, 3)[:2048, :2048]
    assert np.array_equal(image, resize(pixels, 2048, 2048, lanczos))
