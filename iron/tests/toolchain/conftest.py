# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One build per case.

The repo-wide ``--iterations`` (default 5) repeats every test for timing
statistics. A lowering or a full-ELF build is deterministic and minutes
long, and its cache would make the repeats no-ops in any case, so only the
first iteration of each toolchain test is kept.
"""

import pytest

aie = pytest.importorskip("aie")
import aie.utils as aie_utils  # noqa: E402
from aie.iron.device import NPU2  # noqa: E402

from iron.tests.toolchain.tools import DEVICES  # noqa: E402


def pytest_collection_modifyitems(config, items):
    keep, dropped = [], []
    for item in items:
        params = getattr(getattr(item, "callspec", None), "params", {})
        (dropped if params.get("_iteration", 0) else keep).append(item)
    if dropped:
        config.hook.pytest_deselected(items=dropped)
        items[:] = keep


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
    aie_utils.set_current_device(NPU2())
    yield
    aie_utils.set_current_device(previous)
