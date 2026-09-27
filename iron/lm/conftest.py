# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The model a model package's test module runs, loaded once for it."""

import aie.utils as aie_utils
import pytest


@pytest.fixture(scope="module")
def model(runner):
    """The module's ``runner``'s model, compiled and loaded once; the runtime
    is released after the module's last test, as ``npu_runtime`` does after
    each of the others.
    """
    yield runner.npu()
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()
