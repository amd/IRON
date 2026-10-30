# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""MHA's declared buffers do not follow a device-free tuner's tunable.

A tunable a device-free tuner chooses does not change them without
rebuilding the array.
"""

import pytest

from iron.operators.mha import MHA

pytestmark = pytest.mark.usefixtures("npu2")


def test_buffers_do_not_follow_the_pipeline_count():
    """A tuner choosing ``num_pipelines`` leaves the host's buffers as they are."""
    shapes = {
        tuple(
            b.shape
            for b in MHA(num_heads=8, seq_len=500, num_pipelines=p).resolved().buffers
        )
        for p in (1, 2, 4, 8)
    }
    assert shapes == {((8, 512, 64),) * 4}
