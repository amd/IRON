# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A host step (``iron.on_host``) between a graph's steps: recorded, planned,
run in the reference, and on the device between a full ELF's commands or an
xclbin's steps.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.common.image.callable import FullELFCallable
from iron.common.image.packaging import plan
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd

R, C = 16, 256


class Reversed(iron.Graph):
    """``x + x`` on the first ``rows`` rows; the host writes those rows of
    it, reversed, into ``staged`` (zero below); then ``x + staged``.
    """

    def __init__(self):
        self.staged = iron.state((R, C))
        self.calls = 0

    def body(self, x, *, rows: Scratchpad[np.int32]):
        y = ElementwiseAdd.step(x[:rows], x[:rows])
        iron.on_host(self.reverse, y, writes=(self.staged,))
        return ElementwiseAdd.step(x, self.staged)

    def reverse(self, y, staged):
        self.calls += 1
        staged[: len(y)] = y[::-1]
        staged[len(y) :] = 0


def expected(x, rows):
    staged = np.zeros_like(x, dtype=np.float32)
    staged[:rows] = (2 * x[:rows].astype(np.float32))[::-1]
    return (x.astype(np.float32) + staged).astype(bfloat16)


def drawn(seed=0):
    return np.random.default_rng(seed).integers(-8, 8, (R, C)).astype(bfloat16)


def test_a_host_step_is_recorded_before_the_next_step(npu2):
    g = Reversed()
    recording = g.record(x=(R, C))
    (step,) = recording.host
    assert step.at == 1 and len(recording.steps) == 2
    (read,) = step.reads
    assert read is recording.steps[0].outputs[0]
    assert set(read.valid) == {0}, "read cut to the rows the call bounds"
    (write,) = step.writes
    assert write.role == "state" and write.name == g.staged.name
    assert "rows" in recording.reads


def test_a_full_elf_ends_a_command_at_a_host_step(npu2):
    recording = Reversed().record(x=(R, C))
    chosen = plan(npu2, recording, full_elf=True)
    assert chosen.commands == (1,)
    assert any("host step" in r for r in chosen.reasons), chosen.reasons


def test_a_version_with_no_tensor_splits_at_a_host_step_too(npu2):
    """A version taking no tensor stays one command so a loop can drain into
    it; one with a host step has no loop, so it splits there.
    """
    x = iron.state((R, C))
    out = iron.state((R, C))

    def copy(y, o):
        o[:] = y

    class NoInput(iron.Graph):
        def body(self):
            y = ElementwiseAdd.step(x, x)
            iron.on_host(copy, y, writes=(out,))
            return ElementwiseAdd.step(y, out)

    chosen = plan(npu2, NoInput().record(), full_elf=True)
    assert chosen.commands == (1,)


@pytest.mark.parametrize("rows", [R, 5])
def test_the_reference_runs_the_host_step_on_the_rows_the_call_bounds(npu2, rows):
    g, x = Reversed(), drawn()
    y = np.asarray(g.reference(x, rows=rows))
    np.testing.assert_array_equal(y, expected(x, rows))
    assert g.calls == 1


def test_on_host_outside_a_body_is_refused():
    with pytest.raises(TypeError, match="records into a graph's body"):
        iron.on_host(print, np.zeros(4))


def test_a_host_write_to_other_than_a_state_is_refused(npu2):
    class Into(iron.Graph):
        def body(self, x):
            y = ElementwiseAdd.step(x, x)
            iron.on_host(print, x, writes=(y,))
            return y

    with pytest.raises(TypeError, match="writes contiguous parts of states"):
        Into().record(x=(R, C))


def test_a_host_write_to_a_state_a_step_writes_is_refused(npu2):
    cache = iron.state((R, C))

    class Both(iron.Graph):
        def body(self, x):
            Copy.step(x, cache[:])
            iron.on_host(print, x, writes=(cache,))
            return ElementwiseAdd.step(x, cache)

    with pytest.raises(ValueError, match="which a step writes too"):
        Both().record(x=(R, C))


@pytest.mark.parametrize(
    "full_elf",
    [
        pytest.param(True, marks=pytest.mark.supported_devices("npu2")),
        pytest.param(False, marks=pytest.mark.supported_devices("npu1", "npu2")),
    ],
    ids=["full_elf", "each_step"],
)
def test_a_host_step_runs_between_the_device_s_steps(full_elf):
    """Each call reads what the first step wrote, cut to its rows, and the
    second step reads what the host wrote: numpy's, exactly, call after call.
    """
    g = Reversed()
    version = g.compile(x=(R, C), full_elf=full_elf)
    assert version.plan.full_elf is full_elf
    assert version.emit is None
    for k, rows in enumerate([R, 5, 1, R]):
        x = drawn(k)
        y = version(x, rows=np.int32(rows))
        got = np.asarray(y.numpy()).reshape(R, C)
        np.testing.assert_array_equal(got, expected(x, rows))
    assert g.calls == 4
    call = version.callable
    if isinstance(call, FullELFCallable):
        with pytest.raises(ValueError, match="host step runs between its commands"):
            version.start(call.run, drawn(), rows=np.int32(R))
