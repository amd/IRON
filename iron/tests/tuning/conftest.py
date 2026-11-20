# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every tuning test runs once per device it applies to.

A test takes ``device``, the device bound as current for it, once per
``DEVICES`` entry. Device-free, it runs for each. Marked
``supported_devices``, it runs only for the devices the marker names, each
only on that NPU: a design built for one device runs on no other.
"""

import aie.utils as aie_utils
import pytest

from iron.tests.support.tools import DEVICES


@pytest.fixture(params=sorted(DEVICES))
def device(request):
    """Return the device ``request.param`` names, bound as current for the test."""
    dev = DEVICES[request.param]()
    with aie_utils.set_current_device(dev):
        yield dev


def pytest_collection_modifyitems(config, items):
    """Keep a device test only for the devices it names, each run only on its own NPU."""
    kept, dropped = [], []
    for item in items:
        callspec = vars(item).get("callspec")
        marker = item.get_closest_marker("supported_devices")
        if callspec is None or "device" not in callspec.params or marker is None:
            kept.append(item)
            continue
        name = callspec.params["device"]
        if name in marker.args:
            item.add_marker(pytest.mark.supported_devices(name), append=False)
            kept.append(item)
        else:
            dropped.append(item)
    if dropped:
        config.hook.pytest_deselected(items=dropped)
        items[:] = kept
