# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``switch_cost`` on a real device.

A sane fit, and a cached call that dispatches nothing.
"""

import pytest

from iron.common.image.packaging import require_device
from iron.tune.measure import Cache, Timing, platform, pmode, switch_cost

pytestmark = pytest.mark.supported_devices("npu2")


def test_switch_cost_is_sane_and_a_second_call_hits_the_cache(npu2, tmp_path):
    dev = require_device()
    cache = Cache(platform()["Name"], pmode(), root=tmp_path)
    timing = Timing(rounds=4, calls=10)

    fixed_us, per_core_us = switch_cost(dev, timing=timing, cache=cache)
    assert 10.0 <= fixed_us <= 200.0
    assert 0.0 <= per_core_us <= 30.0
    assert cache.get_switch_cost(Cache.switch_cost_key(dev)) == (fixed_us, per_core_us)

    # A cache hit returns before ever measuring, so it never logs.
    logged = []
    again = switch_cost(dev, timing=timing, cache=cache, log=logged.append)
    assert again == (fixed_us, per_core_us)
    assert not logged
