# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The devices the toolchain tests build for, each made current."""

import aie.utils as aie_utils
import pytest

from iron.tests.toolchain.tools import DEVICES


@pytest.fixture(params=sorted(DEVICES))
def device(request):
    """Each device width the gate builds for, made current."""
    previous = aie_utils.get_current_device()
    dev = DEVICES[request.param]()
    aie_utils.set_current_device(dev)
    yield dev
    aie_utils.set_current_device(previous)


@pytest.fixture
def npu2():
    previous = aie_utils.get_current_device()
    dev = DEVICES["npu2"]()
    aie_utils.set_current_device(dev)
    yield dev
    aie_utils.set_current_device(previous)
