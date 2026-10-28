# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generation's EOS exits and rate accounting over a device loop, without an NPU."""

import math
from types import SimpleNamespace
from unittest.mock import Mock

import numpy as np
import pytest

from iron.lm.model import Model
from iron.lm.session import device_draws


@pytest.mark.parametrize("each", [False, True], ids=["generate", "stream"])
@pytest.mark.parametrize(
    "eos", [10, 12, None], ids=["first-eos", "later-eos", "no-eos"]
)
@pytest.mark.parametrize("max_tokens", [1, 6])
def test_device_generation_stops_only_before_undrawn_tokens(
    monkeypatch, each, eos, max_tokens
):
    clock = [0.0]
    monkeypatch.setattr("iron.lm.model.time.perf_counter", lambda: clock[0])

    def start(*args, **kwargs):
        clock[0] += 1.0

    def steps(n):
        for _ in range(n):
            clock[0] += 2.0
            yield None

    loop = SimpleNamespace(start=Mock(side_effect=start), steps=Mock(side_effect=steps))
    draws = np.arange(10, 16, dtype=np.int32)

    class DeviceModel(Model):
        draws_at_once = True

        def _draw(self, tokens, max_tokens, sampler, each, **inputs):
            chunks = [((tokens,), {"position": len(tokens) - 1})]
            yield from device_draws(self, chunks, len(tokens), max_tokens, each)

    model = DeviceModel()
    model.eos = set() if eos is None else {eos}
    model.prompt_chunk = object()
    model.drawn = object()
    model.decode_step = SimpleNamespace(read=lambda _: draws)
    model.loop = Mock(return_value=loop)
    tokens = (
        list(model.stream([1], max_tokens)) if each else model.generate([1], max_tokens)
    )
    end = max_tokens if eos is None else min(max_tokens, eos - 10 + 1)
    assert tokens == list(draws[:end])
    ran = end - 1 if each or eos == 10 else max_tokens - 1
    assert clock[0] == 1.0 + 2.0 * ran
    if eos == 10:
        loop.steps.assert_not_called()
    else:
        loop.steps.assert_called_once_with(max_tokens - 1)
    assert model.stats.ttft == 1.0
    if ran:
        assert model.stats.tokens_per_s == 0.5
    else:
        assert math.isnan(model.stats.tokens_per_s)
