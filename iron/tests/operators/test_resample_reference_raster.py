# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Resample.reference given a raster larger than one image fills, as a graph gives it a state.

It writes the image's rows over its leading ones, as the device does,
and keeps the rest. Host-only.
"""

import numpy as np
from aie.iron.device import from_name
from ml_dtypes import bfloat16

from iron.operators.resample.op import Resample, ResampleTaps


def test_a_given_raster_keeps_the_rows_past_the_image():
    op = Resample(height=37, width=53, out_height=96, out_width=144)
    op = op.resolved(from_name("npu2", n_cols=8))
    image = np.random.default_rng(0).integers(
        0, 256, (op.image_chunks, op.chunk), dtype=np.uint8
    )
    taps = [
        ResampleTaps(
            in_size=n_in, out_size=n_out, words=op.words, slots=16, chunks=chunks
        ).reference()
        for n_in, n_out, chunks in (
            (53, 144, op.width_chunks),
            (37, 96, op.height_chunks),
        )
    ]
    alone = op.reference(image, *taps)
    raster = np.full((alone.shape[0] + 64, alone.shape[1]), 7, bfloat16)
    written = op.reference(image, *taps, patches=raster)
    assert written is raster
    assert np.array_equal(
        raster[: alone.shape[0]].view(np.uint16), alone.view(np.uint16)
    )
    assert (raster[alone.shape[0] :].astype(np.float32) == 7).all()
