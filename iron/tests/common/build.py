# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The derived sequence, device-free.

Streams are bound to fake fifo handles that record what is issued, so the
order and access patterns of the fills and drains the library derives can be
checked without generating MLIR. What cannot be checked here is that the
recorded calls are what upstream's ObjectFifoHandle.fill/drain accept; that
is the toolchain's job and the operator tests' job.
"""

import numpy as np
import pytest

from iron.common.build import Sequence, _derived, _preamble, plan
from iron.common.declare import (
    In,
    Operator,
    Out,
    Overlay,
    Resident,
    StreamIn,
    StreamOut,
    dim,
    operator,
    optional,
    tunable,
)
from iron.common.tiling import Access


class FakeHandle:
    def __init__(self, name, log):
        self.name, self.log = name, log

    def fill(self, data, tap, wait, group, offset_parameter):
        self.log.append(("fill", self.name, data, wait))

    def drain(self, data, tap, wait, group, offset_parameter):
        self.log.append(("drain", self.name, data, wait))


class FakeDev:
    def columns(self):
        return 4


@operator
class UnaryOverlay(Overlay):
    tile: int = tunable(1024)
    cols: int = tunable(None)
    chans: int = tunable(2)

    x = StreamIn(tile, per=(cols, chans))
    y = StreamOut(tile, per=(cols, chans))

    def tuning(self, dev):
        import dataclasses

        return dataclasses.replace(self, cols=self.cols or dev.columns())


@operator
class Unary(Operator[UnaryOverlay]):
    size: int = dim()
    A = In(size, to=UnaryOverlay.x)
    B = Out(size, from_=UnaryOverlay.y)


@operator
class MVOverlay(Overlay):
    K: int = dim()
    cols: int = tunable(2)
    tile_out: int = tunable(64)
    a = StreamIn(tile_out, K, per=cols)
    b = StreamIn(K, broadcast=True)
    c = StreamOut(tile_out, per=cols)


@operator
class MV(Operator[MVOverlay]):
    M: int = dim()
    num_batches: int = dim(1)
    A = In(optional(num_batches), M, MVOverlay.K, to=MVOverlay.a)
    B = In(optional(num_batches), MVOverlay.K, to=MVOverlay.b)
    C = Out(optional(num_batches), M, from_=MVOverlay.c)


def _bind_all(ov, log):
    for s in ov.streams.values():
        for i in range(s.count):
            s.bind(FakeHandle(f"{s.name}{i}", log), i)


def test_plan_reproduces_the_channeled_unary_split():
    ov = UnaryOverlay().tuned(FakeDev())
    op = Unary(ov, size=8192)
    (x,) = [s for s in ov.streams.values() if s.name == "x"]
    p = plan(op.A, x)
    assert len(p) == 8  # 4 columns x 2 channels
    chunk = 8192 // 8
    for i, (slot, accesses) in enumerate(p):
        assert slot.index == i
        assert accesses == [Access(8192, chunk * i, (1, 1, 1, chunk), (0, 0, 0, 1))]


def test_plan_batched_gemv_coalesces_and_broadcasts():
    ov = MVOverlay(K=128)
    op = MV(ov, M=256, num_batches=100)
    a_plan = plan(op.A, ov.a)
    assert [slot.index for slot, _ in a_plan] == [0, 1]
    (acc,) = a_plan[1][1]
    run = (256 // 2) * 128
    assert acc.offset == run and acc.sizes[1] == 100 and acc.strides[1] == 256 * 128
    b_slot, b_accesses = plan(op.B, ov.b)[0]
    assert b_slot is ov.b and b_accesses == [
        Access(100 * 128, 0, (1, 1, 1, 100 * 128), (0, 0, 0, 1))
    ]


def test_derived_sequence_issues_fills_then_waited_drains():
    log = []
    ov = MVOverlay(K=128)
    _bind_all(ov, log)
    op = MV(ov, M=256)
    rt = Sequence(op, ov, {"A": "dA", "B": "dB", "C": "dC"})
    _derived(rt, op, ov)
    assert log == [
        ("fill", "a0", "dA", False),
        ("fill", "a1", "dA", False),
        ("fill", "b0", "dB", False),
        ("drain", "c0", "dC", True),
        ("drain", "c1", "dC", True),
    ]


def test_derived_sequence_names_a_buffer_without_a_stream():
    @operator
    class NoStream(Operator[MVOverlay]):
        M: int = dim()
        A = In(M, MVOverlay.K)
        C = Out(M, from_=MVOverlay.c)

    log = []
    ov = MVOverlay(K=128)
    _bind_all(ov, log)
    op = NoStream(ov, M=256)
    with pytest.raises(ValueError, match="NoStream.A names no stream"):
        _derived(op and Sequence(op, ov, {"A": "dA", "C": "dC"}), op, ov)


def test_override_slices_and_issues_through_the_same_sequence():
    @operator
    class Custom(Operator[MVOverlay]):
        M: int = dim()
        A = In(M, MVOverlay.K, to=MVOverlay.a)
        B = In(MVOverlay.K, to=MVOverlay.b)
        C = Out(M, from_=MVOverlay.c)

        def design(self, rt):
            rows = self.M // self.ov.cols
            rt.fill(self.ov.b, self.B)
            with rt.group():
                for col in range(self.ov.cols):
                    rt.fill(self.ov.a[col], self.A[col * rows : (col + 1) * rows, :])
                    rt.drain(self.ov.c[col], self.C[col * rows : (col + 1) * rows])

    log = []
    ov = MVOverlay(K=128)
    _bind_all(ov, log)
    op = Custom(ov, M=256)
    assert Custom.has_design_override() and not MV.has_design_override()
    op.design(Sequence(op, ov, {"A": "dA", "B": "dB", "C": "dC"}))
    assert [(v, h) for v, h, _, _ in log] == [
        ("fill", "b0"),
        ("fill", "a0"),
        ("drain", "c0"),
        ("fill", "a1"),
        ("drain", "c1"),
    ]


def test_preamble_writes_residents_and_rejects_missing_ones():
    @operator
    class Counted(Overlay):
        tile: int = tunable(64)
        count = Resident(np.int32)
        s = StreamIn(tile)

    @operator
    class Op(Operator[Counted]):
        n: int = dim()
        A = In(n, to=Counted.s)

        def residents(self):
            return {"count": self.n // self.ov.tile}

    class FakeRTP(dict):
        pass

    ov = Counted()
    rtps = [FakeRTP(), FakeRTP()]
    ov.count.bind(rtps)
    op = Op(ov, n=640)

    class FakeTarget:
        barriers = []

    _preamble(Sequence(op, ov, {}), op, ov, FakeTarget())
    assert rtps == [{0: 10}, {0: 10}]

    @operator
    class Forgetful(Operator[Counted]):
        n: int = dim()
        A = In(n, to=Counted.s)

    with pytest.raises(ValueError, match="does not supply it"):
        _preamble(Sequence(op, ov, {}), Forgetful(ov, n=64), ov, FakeTarget())
