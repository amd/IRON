# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The devices the toolchain tests build for, each made current."""

import pytest

from iron.tests.toolchain.tools import DEVICES


@pytest.fixture(params=sorted(DEVICES))
def device(request):
    """Each device width the gate builds for, made current by the root
    conftest's fixture of that name.
    """
    return request.getfixturevalue(request.param)
