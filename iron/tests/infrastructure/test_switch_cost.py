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


def test_a_teardown_switch_is_kept_apart_and_saves_the_reset(npu2, tmp_path):
    dev = require_device()
    cache = Cache(platform()["Name"], pmode(), root=tmp_path)
    timing = Timing(rounds=4, calls=10)

    reset = switch_cost(dev, timing=timing, cache=cache)
    torn = switch_cost(dev, timing=timing, cache=cache, teardown=True)
    assert Cache.switch_cost_key(dev, teardown=True) != Cache.switch_cost_key(dev)
    assert cache.get_switch_cost(Cache.switch_cost_key(dev, teardown=True)) == torn
    # The reset before each configuration is most of a switch's fixed part on npu2
    # (about 36 of 39 us into one core); undoing only what was configured is not.
    assert torn[0] < reset[0] / 2
