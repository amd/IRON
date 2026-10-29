# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A Resample over the right half of a wider resize reads the second half of
that resize's taps table: its headers name the wide columns, which
``first_chunk`` says. Host-only.
"""

import numpy as np
import pytest
from aie.iron.device import from_name

from iron.operators.resample.op import SIDE, Resample, ResampleTaps

HALF = 16  # width chunks a pass covers


def _ops(first_chunk):
    dev = from_name("npu2", n_cols=8)
    wide = Resample(
        height=37, width=53, out_height=96, out_width=2 * HALF * SIDE, dtype=np.uint8
    ).resolved(dev)
    half = Resample(
        height=37,
        width=53,
        out_height=96,
        out_width=HALF * SIDE,
        dtype=np.uint8,
        first_chunk=first_chunk,
    ).resolved(dev)
    image = np.random.default_rng(0).integers(
        0, 256, (wide.image_chunks, wide.chunk), dtype=np.uint8
    )
    taps_w = ResampleTaps(
        in_size=53,
        out_size=2 * HALF * SIDE,
        words=wide.words,
        slots=SIDE,
        chunks=2 * HALF,
    ).reference()
    taps_h = ResampleTaps(
        in_size=37,
        out_size=96,
        words=wide.words,
        slots=SIDE,
        chunks=wide.height_chunks,
    ).reference()
    return wide, half, image, taps_w, taps_h


def _pixels(op, written):
    return np.asarray(written).reshape(-1, op.pitch // 3, 3)[:96]


def test_the_second_half_of_a_table_resizes_the_right_half():
    wide, half, image, taps_w, taps_h = _ops(first_chunk=HALF)
    full = _pixels(wide, wide.reference(image, taps_w, taps_h))
    right = _pixels(half, half.reference(image, taps_w[HALF:], taps_h))
    assert np.array_equal(
        right[:, : HALF * SIDE], full[:, HALF * SIDE : 2 * HALF * SIDE]
    )


def test_a_slice_read_as_the_first_chunks_is_refused_as_the_kernel_refuses_it():
    _, half, image, taps_w, taps_h = _ops(first_chunk=0)
    with pytest.raises(ValueError, match="covers outputs from 256, not 0"):
        half.reference(image, taps_w[HALF:], taps_h)
