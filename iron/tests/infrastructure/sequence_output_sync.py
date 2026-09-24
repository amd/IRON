#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Device-free tests for the per-buffer output sync.

A dispatch writes its output buffers on the device, which the host-side coherence
map does not observe. ``to("cpu")`` transfers only the ranges the map holds as
device-resident, so a range left marked ``cpu`` by an earlier read is skipped and
the next dispatch hands back the previous one's output.
"""

import pytest

from aie.utils.hostruntime.coherence import _CoherenceMap

from iron.common.sequence import SequenceXclbinCallable


def test_a_pull_is_skipped_while_the_range_reads_as_host_resident():
    """The hazard the output sync has to defeat, at the layer that decides it."""
    coherence = _CoherenceMap(64, _CoherenceMap.DEVICE)
    assert coherence.ranges(0, 64, _CoherenceMap.DEVICE) == [(0, 64)]

    coherence.set(0, 64, _CoherenceMap.HOST)
    assert coherence.ranges(0, 64, _CoherenceMap.DEVICE) == []

    coherence.set(0, 64, _CoherenceMap.DEVICE)
    assert coherence.ranges(0, 64, _CoherenceMap.DEVICE) == [(0, 64)]


class _RecordingBuffer:
    def __init__(self):
        self.calls = []
        self._device = "cpu"

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, value):
        self._device = value
        self.calls.append(("device", value))

    def to(self, target):
        self._device = target
        self.calls.append(("to", target))


class _Op:
    def __init__(self, names, inputs):
        self.subbuffer_layout = {n: (None, None, 8) for n in names}
        self.input_args = set(inputs)


def _callable(names, inputs):
    """A SequenceXclbinCallable with recording buffers and no XRT behind it."""
    call = object.__new__(SequenceXclbinCallable)
    call.op = _Op(names, inputs)
    call._buffers = {n: _RecordingBuffer() for n in names}
    return call


def test_output_sync_claims_the_device_before_pulling():
    call = _callable(["a", "out"], inputs=["a"])
    call._sync_outputs()
    assert call._buffers["out"].calls == [("device", "npu"), ("to", "cpu")]


@pytest.mark.parametrize("reps", [2, 3])
def test_every_dispatch_pulls_again(reps):
    call = _callable(["out"], inputs=[])
    for _ in range(reps):
        call._sync_outputs()
    assert call._buffers["out"].calls.count(("to", "cpu")) == reps
    assert call._buffers["out"].calls.count(("device", "npu")) == reps


def test_inputs_are_left_alone():
    call = _callable(["a", "out"], inputs=["a"])
    call._sync_outputs()
    assert call._buffers["a"].calls == []
