# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One build per case, and the toolchain kind this branch assumes.

The repo-wide ``--iterations`` (default 5) repeats every test for timing
statistics. A lowering or a full-ELF build is deterministic and minutes
long, and its cache would make the repeats no-ops in any case, so only the
first iteration of each toolchain test is kept.

A build that patches a descriptor's size per call needs mlir-aie's
size-kind scratchpad parameter (LENGTH_FREE_PLAN.md). Until the toolchain
has it, a test that reaches that point is a skip naming it, not a failure:
everything before it (the arrays, the words, the other descriptors) ran.
"""

import pytest

aie = pytest.importorskip("aie")
import aie.utils as aie_utils  # noqa: E402

from iron.tests.toolchain.tools import DEVICES  # noqa: E402


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
    aie_utils.set_current_device(DEVICES["npu2"]())
    yield
    aie_utils.set_current_device(previous)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    outcome = yield
    try:
        outcome.get_result()
    except NotImplementedError as e:
        if "size-kind scratchpad parameter" in str(e):
            # The build stopped mid-generation: the kernels it declared stay
            # registered, which compile() would have cleared.
            from aie.iron import ExternalFunction

            ExternalFunction._instances.clear()
            outcome.force_exception(pytest.skip.Exception(str(e)))
