# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The tuner's probe over a graph that gathers by ids the device made.

Such a graph holds per-call values no caller gives (the table's address its
word step reads), and a ``Gather`` whose control words name device
addresses; run alone, a gather must stream words for its own table, not
random bytes.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Carried
from iron.tune.autotune import Timed
from iron.tune.measure import Standalone, Timing, measure
from iron.common.image.step import BufferRef
from iron.operators.copy import APERTURE, Copy, Gather, GatherWords

ROWS, WIDTH = 4096, 512

pytestmark = pytest.mark.usefixtures("npu2")


class DeviceIds(iron.Graph):
    def __init__(self, table):
        self.table = iron.weight(table)

    def body(self, ids):
        return Copy.step(self.table[Copy.step(ids, dtype=np.int32)])


class Walk(iron.Graph):
    def __init__(self, table, rows: int):
        self.table = iron.weight(table)
        self.ids = iron.state((rows,), np.int32)
        self.rows = iron.state((rows, WIDTH))

    def body(self, *, steps: Carried[np.int32]):
        Copy.step(Copy.step(self.table[self.ids]), self.rows)
        return iron.carry(steps=steps + 1)


@pytest.fixture(scope="module")
def table():
    rng = np.random.default_rng(0)
    return rng.standard_normal((ROWS, WIDTH), dtype=np.float32).astype(bfloat16)


def test_a_call_gives_the_address_a_word_step_reads(table):
    traced = DeviceIds(table).trace(ids=((15,), np.int32))
    call = Timed(traced)
    words = next(s.op for s in traced.steps if isinstance(s.op, GatherWords))
    assert call.op_values(words) == {"base_lo": 0, "base_hi": 0}


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("rows", [15, 256])
def test_a_gather_alone_reads_the_rows_its_words_name(table, rows):
    traced = DeviceIds(table).trace(ids=((rows,), np.int32))
    gather = next(s.op for s in traced.steps if isinstance(s.op, Gather))
    alone = Standalone(f"probe_gather{rows}", [gather])
    words = (
        alone.callable.get_buffer(BufferRef("s0_control")).numpy_view().view(np.uint32)
    )
    _, slots = gather.template
    addresses = words[slots].astype(np.int64) | words[slots + 2].astype(np.int64) << 32
    offsets = addresses - (alone.address("s0_table") + APERTURE)
    row_bytes = WIDTH * np.dtype(bfloat16).itemsize
    assert not (offsets % row_bytes).any()
    ids = offsets // row_bytes
    assert ((ids >= 0) & (ids < ROWS)).all()
    stored = (
        alone.callable.get_buffer(BufferRef("s0_table")).numpy_view().view(np.uint16)
    )
    expected = stored[: ROWS * WIDTH].reshape(ROWS, WIDTH)[ids]
    alone.callable()
    [got] = alone.written().values()
    got = got.view(np.uint16).reshape(rows, WIDTH)
    np.testing.assert_array_equal(got, expected)


@pytest.mark.extensive
@pytest.mark.supported_devices("npu2")
def test_a_graph_gathering_by_device_ids_is_timed(table):
    traced = DeviceIds(table).trace(ids=((15,), np.int32))
    call = Timed(traced)
    assert {type(s.op) for s in traced.steps} == {Copy, GatherWords, Gather}
    for step in traced.steps:
        ran = measure(
            [step.op.resolved()],
            full_elf=True,
            timing=Timing(rounds=1, calls=5),
            repeats=2,
            values=call.op_values(step.op),
            log=lambda _: None,
        )
        assert 0 in ran, type(step.op).__name__


@pytest.mark.supported_devices("npu2")
def test_an_emit_cannot_start_a_gather_by_device_ids(table):
    walk = Walk(table, 15)
    body = walk.compile()
    with pytest.raises(ValueError, match=r"an Emit cannot start it.*\['table'\]"):
        body.emit_to(body)
