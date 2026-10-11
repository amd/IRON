#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Resample's patch rows, padded past the cores of the device it runs on.

Host-only: the reference is what the cores write, row for row, so its
shape is the buffer's wherever the default sizes it.
"""

import pytest

from iron.common.harness import vectors
from iron.operators.resample.op import Resample


@pytest.mark.parametrize("device", ["npu1", "npu2"])
@pytest.mark.parametrize("out_width", [144, 256])
def test_the_default_patch_rows_are_the_rows_the_cores_write(
    device, out_width, request
):
    dev = request.getfixturevalue(device)
    op = Resample(height=37, width=53, out_height=96, out_width=out_width)
    op = op.resolved(dev)
    written = op.cores * op.residents["patch_count"]
    assert op.patch_rows == written
    patches = vectors(op, **Resample.test.draw(op)).outputs["patches"]
    assert patches.shape == (written, 16 * 16 * 3)
