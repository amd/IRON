# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The derived sequence, as the module spells it, without hardware.

Each operator generates its MLIR module on a bound NPU2 and the runtime
sequence is read back out of the text: the order, access patterns and waits
of the fills and drains the library derives, the resident writes before
them. Nothing is lowered or run; that is the toolchain's job and the
operator tests' job.
"""

import dataclasses
import re
from typing import NamedTuple

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.helpers.util import v8bfp16ebs8
from aie.iron import ObjectFifo, Worker
from aie.iron.device import NPU2, from_name

import iron.operators.flm.gemm.op as flm_op
from iron.common.declare import (
    DeclarationError,
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
    Xclbin,
)
from iron.common.external import LOCK_ADDRESS_BASE
from iron.common.tiling import Access
from iron.operators.flm.gemm.shipped import Shipped
from iron.operators.mem_copy import MemCopy
from iron.operators.mha.op import MHA

_TASK = re.compile(r"(%\w+) = aiex\.dma_configure_task_for @(\w+)")
_BD = re.compile(
    r"aie\.dma_bd\(%arg(\d+) : [^)]*?offset = (\d+) len = (\d+)"
    r"(?: sizes = \[([\d, ]+)\] strides = \[([\d, ]+)\])?"
)
_AWAIT = re.compile(r"aiex\.dma_await_task\((%\w+)\)")
_WRITE32 = re.compile(
    r"aiex\.npu\.write32\(%c(-?\d+)_i32\w*, %c(-?\d+)_i32\w*\) "
    r"\{column = (\d+) : i32, row = (\d+) : i32\}"
)
_RTP_WRITE = re.compile(r"aiex\.npu\.rtp_write\(@(\w+), (\d+), %c(-?\d+)_i32\w*\)")


class Task(NamedTuple):
    """One descriptor the sequence issues, as the module spells it."""

    verb: str  # "fill" or "drain", by the direction of the buffer it moves
    fifo: str  # the symbol it is issued on
    buffer: str
    offset: int
    sizes: tuple
    strides: tuple
    waited: bool  # issued with a token, which an await consumes


def _sequence(op):
    """The runtime sequence ``op`` generates on the bound device, in order.

    Transfers are :class:`Task`; an await is ``("await", i)`` with ``i`` the
    index of the task it waits on; a register write is ``("write32",
    address, value, col, row)`` and a runtime-parameter write ``("rtp_write",
    buffer, index, value)``.
    """
    text = op.generator()()
    body = text[text.index("aie.runtime_sequence") :]
    events, index, pending = [], {}, None
    for line in body.splitlines():
        if m := _TASK.search(line):
            pending = m[1], m[2]
        elif pending and (m := _BD.search(line)):
            bd = m
        elif pending and line.strip().startswith("}"):
            ssa, fifo = pending
            buf = op.buffers[int(bd[1])]
            sizes = (
                tuple(map(int, bd[4].split(","))) if bd[4] else (1, 1, 1, int(bd[3]))
            )
            strides = tuple(map(int, bd[5].split(","))) if bd[5] else (0, 0, 0, 1)
            index[ssa] = len(events)
            events.append(
                Task(
                    "fill" if buf.direction == "in" else "drain",
                    fifo,
                    buf.name,
                    int(bd[2]),
                    sizes,
                    strides,
                    "issue_token = true" in line,
                )
            )
            pending = None
        elif m := _AWAIT.search(line):
            events.append(("await", index[m[1]]))
        elif m := _WRITE32.search(line):
            events.append(("write32", *map(int, m.groups())))
        elif m := _RTP_WRITE.search(line):
            events.append(("rtp_write", m[1], int(m[2]), int(m[3])))
    return events


def _tasks(op):
    return [e for e in _sequence(op) if isinstance(e, Task)]


@pytest.fixture(autouse=True)
def device():
    """An eight-column NPU2: what the sequences below are generated for."""
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(NPU2())
    yield
    aie_utils.set_current_device(previous)


def _consume(*fifos):
    """A core that takes one object from each fifo and gives it back.

    No kernel, so a design built on it generates without the toolchain.
    """
    for f in fifos:
        f.acquire(1)
    for f in fifos:
        f.release(1)


def _consume_holding(fifo, rtp):
    """:func:`_consume`, on a core that also holds a runtime-parameter buffer."""
    _consume(fifo)


@operator
class UnaryOverlay(Overlay):
    tile: int = tunable(1024)
    cols: int = tunable(None)
    chans: int = tunable(2)

    x = StreamIn(tile, per=(cols, chans))
    y = StreamOut(tile, per=(cols, chans))

    def tuning(self, dev):
        return dataclasses.replace(self, cols=self.cols or dev.cols)


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

    def design(self, target) -> list:
        b = ObjectFifo(self.b.tile, name="b0")
        self.b.bind(b.prod())
        workers = []
        for col in range(self.cols):
            a = ObjectFifo(self.a.tile, name=f"a{col}")
            c = ObjectFifo(self.c.tile, name=f"c{col}")
            self.a[col].bind(a.prod())
            self.c[col].bind(c.cons())
            workers.append(Worker(_consume, [a.cons(), b.cons(), c.prod()]))
        return workers


@operator
class MV(Operator[MVOverlay]):
    M: int = dim()
    num_batches: int = dim(1)
    A = In(optional(num_batches), M, MVOverlay.K, to=MVOverlay.a)
    B = In(optional(num_batches), MVOverlay.K, to=MVOverlay.b)
    C = Out(optional(num_batches), M, from_=MVOverlay.c)


def test_plan_reproduces_the_channeled_unary_split():
    ov = UnaryOverlay().tuned(from_name("npu2", n_cols=4))
    op = Unary(ov, size=8192)
    order = op.order(op.A)
    assert order.stream is ov.x and len(order.slots) == 8  # 4 columns x 2 channels
    chunk = 8192 // 8
    for i, accesses in enumerate(order.slots):
        assert accesses == (Access(8192, chunk * i, (1, 1, 1, chunk), (0, 0, 0, 1)),)


def test_plan_batched_gemv_coalesces_and_broadcasts():
    ov = MVOverlay(K=128)
    op = MV(ov, M=256, num_batches=100)
    a_order = op.order(op.A)
    assert len(a_order.slots) == 2
    (acc,) = a_order[1]
    run = (256 // 2) * 128
    assert acc.offset == run and acc.sizes[1] == 100 and acc.strides[1] == 256 * 128
    b_order = op.order(op.B)
    assert b_order.stream is ov.b and b_order.slots == (
        (Access(100 * 128, 0, (1, 1, 1, 100 * 128), (0, 0, 0, 1)),),
    )


def test_derived_sequence_issues_fills_then_waited_drains():
    events = _sequence(MV(MVOverlay(K=128), M=256))
    assert [(t.verb, t.fifo, t.buffer, t.waited) for t in events[:5]] == [
        ("fill", "a0", "A", False),
        ("fill", "a1", "A", False),
        ("fill", "b0", "B", False),
        ("drain", "c0", "C", True),
        ("drain", "c1", "C", True),
    ]
    # Only the drains are awaited, after everything is issued.
    assert events[5:] == [("await", 3), ("await", 4)]


def test_derived_sequence_names_a_buffer_without_a_stream():
    @operator
    class NoStream(Operator[MVOverlay]):
        M: int = dim()
        A = In(M, MVOverlay.K)
        C = Out(M, from_=MVOverlay.c)

    op = NoStream(MVOverlay(K=128), M=256)
    with pytest.raises(ValueError, match="NoStream.A names no stream"):
        op.generator()()


def test_override_slices_and_issues_through_the_same_sequence():
    @operator
    class Custom(Operator[MVOverlay]):
        M: int = dim()
        A = In(M, MVOverlay.K, to=MVOverlay.a)
        B = In(MVOverlay.K, to=MVOverlay.b)
        C = Out(M, from_=MVOverlay.c)

        def design(self, rt):
            rows = self.M // self.ov.cols
            # One group for every transfer: upstream refuses a sequence
            # that mixes explicit groups with the default one.
            with rt.group():
                rt.fill(self.ov.b, self.B)
                for col in range(self.ov.cols):
                    rt.fill(self.ov.a[col], self.A[col * rows : (col + 1) * rows, :])
                    rt.drain(self.ov.c[col], self.C[col * rows : (col + 1) * rows])

    assert Custom.has_design_override() and not MV.has_design_override()
    tasks = _tasks(Custom(MVOverlay(K=128), M=256))
    assert [(t.verb, t.fifo, t.offset) for t in tasks] == [
        ("fill", "b0", 0),
        ("fill", "a0", 0),
        ("drain", "c0", 0),
        ("fill", "a1", 128 * 128),
        ("drain", "c1", 128),
    ]


@operator
class Counted(Overlay):
    tile: int = tunable(64)
    count = Resident(np.int32)
    s = StreamIn(tile)

    def design(self, target) -> list:
        s = ObjectFifo(self.s.tile, name="s0")
        self.s.bind(s.prod())
        rtps = [
            target.rtp(
                np.ndarray[(1,), np.dtype[np.int32]],
                name=f"rtp{i}",
                initial_value=np.zeros(1, dtype=np.int32),
            )
            for i in range(2)
        ]
        self.count.bind(rtps, 0)
        return [Worker(_consume_holding, [s.cons(), rtp]) for rtp in rtps]


def test_preamble_writes_residents_and_rejects_missing_ones():
    @operator
    class Op(Operator[Counted]):
        n: int = dim()
        A = In(n, to=Counted.s)

        def residents(self):
            return {"count": self.n // self.ov.tile}

    events = _sequence(Op(Counted(), n=640))
    # Every core's copy of the resident, before any transfer.
    assert events[:2] == [("rtp_write", "rtp0", 0, 10), ("rtp_write", "rtp1", 0, 10)]
    assert [type(e) for e in events[2:]] == [Task]

    @operator
    class Forgetful(Operator[Counted]):
        n: int = dim()
        A = In(n, to=Counted.s)

    with pytest.raises(ValueError, match="does not supply it"):
        Forgetful(Counted(), n=64).generator()()


def test_mha_sequence_is_one_descriptor_set_per_kv_group():
    # mha/op.py with eight pipelines: Q and O go through two shims, each
    # carrying four pipelines' (256-row) block. Per KV group, each shim's Q
    # is one pattern over the group's heads and every block, K and V are the
    # head's slab re-read once per (head, block) from the iteration slot, and
    # the O drains mirror the Q fills and wait.
    op = MHA(num_heads=2, seq_len=1000, d=64, num_KV_heads=1, num_of_pipelines=8)
    op = op.tuned(NPU2())
    ov = op.ov
    assert op.seq_pad == 1024 and ov.q_shims == 2 and ov.join_rows == 256
    assert op.residents() == {
        "q_blocks_per_pipeline": 2,
        "kv_blocks": 16,
        "s_q": 1000,
        "s_kv": 1000,
    }
    events = _sequence(op)
    # The residents first: each of the four words into every stage's
    # runtime-parameter buffer (eight pipelines, three stages).
    writes = [e for e in events if e[0] == "rtp_write"]
    assert events[: len(writes)] == writes and len(writes) == 8 * 3 * 4
    assert {(i, v) for _, _, i, v in writes} == {(0, 2), (1, 16), (2, 1000), (3, 1000)}
    n = len(writes)
    events = events[n:]

    head, block = 1024 * 64, 256 * 64
    # Q: (heads, blocks, rows, d), one per slot. K and V: the re-read in the
    # iteration slot, the head's 1024 rows factored for the d1 wrap.
    q = [((2, 2, 256, 64), (head, 2 * block, 64, 1), s * block) for s in range(2)]
    kv = ((4, 2, 512, 64), (0, 512 * 64, 64, 1), 0)
    assert [
        (t.verb, t.fifo, t.buffer, (t.sizes, t.strides, t.offset), t.waited)
        for t in events[:6]
    ] == [
        ("fill", "inQ", "Q", q[0], False),
        ("fill", "inQ2", "Q", q[1], False),
        ("fill", "inK", "K", kv, False),
        ("fill", "inV", "V", kv, False),
        ("drain", "memO", "O", q[0], True),
        ("drain", "memO2", "O", q[1], True),
    ]
    assert events[6:] == [("await", n + 4), ("await", n + 5)]


def test_mha_sequence_over_interleaved_heads_is_strided_the_same_way():
    # The (seq, heads, d) layout: a head's rows are strided by every head's
    # d, and the group's heads are d apart; the descriptor count is the same.
    op = MHA(
        num_heads=4,
        seq_len=1024,
        d=64,
        num_KV_heads=2,
        num_of_pipelines=8,
        heads_interleaved=True,
    )
    tasks = _tasks(op)
    assert [t.fifo for t in tasks] == ["inQ", "inQ2", "inK", "inV", "memO", "memO2"] * 2
    q0, q1, k0, *_ = tasks[:6]
    # Q: (heads 2 at stride d, blocks 2, rows 256 at stride 4d, d)
    assert q0.sizes == (2, 2, 256, 64) and q0.strides == (64, 2 * 256 * 256, 256, 1)
    assert q1.offset == q0.offset + 256 * 256
    # K: the head's 1024 rows at stride 2d, re-read 4 times, rows factored for d1.
    assert k0.sizes == (4, 2, 512, 64) and k0.strides == (0, 512 * 128, 128, 1)
    # The second group starts at its heads.
    assert tasks[6].offset == 2 * 64 and tasks[8].offset == 64


def test_mha_infers_the_padded_length_and_the_kv_head_count():
    op = MHA.from_operands((8, 128, 64), (2, 128, 64), (2, 128, 64))
    assert (op.num_heads, op.num_KV_heads, op.seq_len, op.seq_pad) == (8, 2, 128, 128)
    with pytest.raises(ValueError, match="seq_pad=100"):
        MHA(num_heads=1, seq_len=100, seq_pad=100, d=64)


# --------------------------------------------------------------------------
# flm/gemm: the configuration/shape split
# --------------------------------------------------------------------------


def test_flm_gemm_keyword_construction_tunes_from_the_device():
    # Keyword construction leaves every tunable to the overlay's tuning,
    # which reads the device alone; the operator's extent is checked against
    # the tuned overlay by compatible(), not folded into its defaults.
    assert flm_op.GEMM(M=512, K=1024, N=1024).ov.tile_n is None
    op = flm_op.GEMM(M=512, K=1024, N=1024).tuned(NPU2())
    ov = op.ov
    assert (ov.tile_n, ov.m_chunk, ov.rows, ov.cols, ov.bfp16_b) == (64, 1, 4, 8, True)
    # NPU2's core tiles: 64 KB of local memory, one memtile row.
    assert ov.tile_ma == flm_op._default_l1(64, 128, 9 / 8, 65536, 1)[0]
    # tile_n is tuning, not a function of K: the same on every shape.
    assert flm_op.GEMM(M=256, K=512, N=1024).tuned(NPU2()).ov.tile_n == 64
    assert (
        op.config_name == f"FLM_GEMM_tn64_ck128_ma{ov.tile_ma}_mc1_emf_conv_even_npu2"
    )
    assert op.name == op.config_name + "_M512_K1024_N1024"
    a, b, c = op.buffers
    assert a.shape == (512, 1024) and c.shape == (512, 1024)
    # B is declared in bfp16ebs8 blocks; the host holds the same bytes as uint8.
    assert b.shape == (1024 * 1024 // 8,) and b.dtype is v8bfp16ebs8
    assert b.host_shape == (flm_op.packed_b_size(1024, 1024, True),)
    assert b.host_dtype is np.uint8
    assert op.residents() == {
        "n_val": 1024,
        "m_row_blocks": 2,
        "k_iters": 2,
        "epilogue": 0,
        "clamp_min": int(np.float32(-np.inf).view(np.int32)),
        "clamp_max": int(np.float32(np.inf).view(np.int32)),
        "n_chunks": 2,
        "n_units": 2,
    }
    with pytest.raises(ValueError, match="multiple of 256"):
        flm_op.GEMM(M=100, K=1024, N=1024).tuned(NPU2())  # M tiles to the array's rows
    with pytest.raises(ValueError, match="not in epilogue_modes"):
        flm_op.GEMM(M=256, K=1024, N=1024, epilogue="gelu", epilogue_modes=("none",))


def test_flm_gemm_declared_overlay_tunes_from_the_device_only():
    ov = flm_op.FLMGEMMOverlay().tuned(NPU2())
    assert ov.tile_n == 64  # no K to look at: the general winner
    op = flm_op.GEMM(ov, M=256, K=512, N=512)
    assert op.ov.tile_n == 64
    untuned = flm_op.GEMM(flm_op.FLMGEMMOverlay(), M=256, K=512, N=512)
    with pytest.raises(flm_op.Incompatible, match="tuned overlay"):
        [b.shape for b in untuned.buffers]  # B's layout follows the device


def test_flm_gemm_unsplit_sequence_issues_c_then_a_then_b_per_block():
    tasks = _tasks(flm_op.GEMM(M=512, K=1024, N=1024))
    # Two column-blocks (N = 2 * 8 * 64): each drains C on eight columns,
    # then fills A on four rows and B on eight columns.
    block = ["C_L2L3"] * 8 + ["A_L3L2"] * 4 + ["B_L3L2"] * 8
    assert [t.fifo.rsplit("_", 1)[0] for t in tasks] == block * 2
    assert all(t.waited == (t.verb == "drain") for t in tasks)
    drains = [t for t in tasks if t.verb == "drain"]
    assert drains[1][1:5] == ("C_L2L3_1", "C", 64, (1, 2, 256, 64))
    assert drains[8][1:5] == ("C_L2L3_0", "C", 8 * 64, (1, 2, 256, 64))
    a_fills = [t for t in tasks if t.buffer == "A"]
    assert a_fills[1][1:5] == ("A_L3L2_1", "A", 64 * 1024, (2, 2, 64, 512))
    b_fills = [t for t in tasks if t.buffer == "B"]
    # B's offsets are in v8bfp16ebs8 elements: values // 8.
    assert b_fills[1][1:5] == (
        "B_L3L2_1",
        "B",
        64 * 1024 // 8,
        (2, 2, 1, 512 * 64 // 8),
    )


def test_flm_gemm_split_sequence_drains_one_row_block_at_a_time():
    # N = 10240 puts C's row-block stride past the 20-bit step: c_split.
    op = flm_op.GEMM(M=512, K=1024, N=10240).tuned(NPU2())
    assert op._c_split and not op._a_split
    drains = [t for t in _tasks(op) if t.verb == "drain"]
    assert len(drains) == 20 * 8 * 2  # blocks x columns x row-blocks
    assert all(t.sizes == (1, 1, 256, 64) for t in drains)


def test_mem_copy_sequence_pads_a_remainder_to_a_full_line():
    # mem_copy.py: whole partitions split evenly; the remainder is padded
    # to one line per core by re-reading copied data, in awaited groups of
    # four transfers on the last fifo.
    def run(size):
        op = MemCopy(
            size=size, num_cores=4, num_channels=1, bypass=False, tile_size=256
        )
        tasks = _tasks(op)
        moved = lambda verb: sum(  # noqa: E731
            t.sizes[0] * t.sizes[3] for t in tasks if t.verb == verb
        )
        return tasks, moved("fill"), moved("drain")

    tasks, filled, drained = run(1024)
    assert (filled, drained) == (1024, 1024)
    assert tasks[0][:5] == ("fill", "in0", "x", 0, (1, 1, 1, 256))
    assert tasks[-1][:5] == ("drain", "out3", "y", 768, (1, 1, 1, 256))
    assert tasks[-1].waited
    # 1000: one whole partition, then a 232-element tail re-reading 8 from
    # the copied prefix so the last core still consumes a full line.
    tasks, filled, drained = run(1000)
    assert (filled, drained) == (1024, 1024)
    assert tasks[-1][:5] == ("drain", "out3", "y", 768, (1, 1, 1, 232))
    assert tasks[-1].waited
    # 100: no whole partition, three idle cores, a 156-element pad.
    tasks, filled, drained = run(100)
    assert (filled, drained) == (256, 256)
    assert {t.fifo for t in tasks} == {"in3", "out3"}
    assert tasks[0][:5] == ("fill", "in3", "x", 0, (32, 1, 1, 4))
    assert tasks[0].waited


# --------------------------------------------------------------------------
# flm.gemm.Shipped: an external overlay's sequence
# --------------------------------------------------------------------------


def test_external_overlay_declares_its_pins_and_parameter_block():
    ov = Shipped()
    assert ov.external.filename == "flm_mm_f81eba71.xclbin"
    assert [(p.col, p.channel) for p in (ov.a.pin(r) for r in range(4))] == [
        (0, 0),
        (2, 0),
        (4, 0),
        (6, 0),
    ]
    assert (ov.b.pin(3).col, ov.b.pin(3).channel) == (3, 1)
    assert (ov.rtp.address, ov.rtp.lock) == (4096, 10)

    with pytest.raises(DeclarationError, match="pinned with via="):

        @operator
        class Unpinned(Overlay):
            image = Xclbin(url="u", sha256="s", filename="f")
            s = StreamIn(64)

    # Nothing designs a prebuilt overlay's array, so the declaration has to
    # say where the image is and what module drives it. flm's External mixin
    # answers both; an overlay without it is rejected at declaration.
    with pytest.raises(DeclarationError, match="must supply prebuilt"):

        @operator
        class Unhooked(Overlay):
            image = Xclbin(url="u", sha256="s", filename="f")


def test_shipped_sequence_writes_every_core_then_streams_in_consume_order():
    ov = Shipped()
    op = flm_op.GEMM(ov, M=256, K=1024, N=1152, epilogue="gelu", clamp=(-2.0, 2.0))
    # The port's residents are hidden; the image's block is laid out from
    # the operator's values.
    assert list(ov.residents) == ["rtp"]
    assert ov.resident_values(op) == {
        "rtp": [2, 256, 1152, 0, 1, 1, -1073741824, 1073741824]
    }
    events = _sequence(op)
    writes = [e for e in events if e[0] == "write32"]
    # 8 words on 32 cores, then one lock release per core, before any DMA.
    assert len(writes) == 32 * 8 + 32
    assert writes[0] == ("write32", 4096, 2, 0, 2)
    assert writes[7] == ("write32", 4124, 1073741824, 0, 2)
    assert writes[-1] == ("write32", LOCK_ADDRESS_BASE + 16 * 10, 1, 7, 5)
    assert events[: len(writes)] == writes
    tasks = [e for e in events if isinstance(e, Task)]
    # N = 9 column-blocks: one full sweep (4 A + 8 B + 8 C) and a trailing
    # block on column 0 alone, which still receives A on every row.
    assert len(tasks) == 20 + 6
    assert [t[1:] for t in tasks[:3]] == [
        ("a_0", "A", 0, (1, 2, 64, 512), (0, 512, 1024, 1), True),
        ("b_0", "B", 0, (1, 1, 1, 131072), (0, 0, 0, 1), True),
        ("c_0", "C", 0, (1, 1, 256, 128), (0, 0, 1152, 1), True),
    ]
    assert tasks[5][1:] == (
        "a_1",
        "A",
        64 * 1024,
        (1, 2, 64, 512),
        (0, 512, 1024, 1),
        True,
    )
    # Every task is awaited exactly once, the last ones by the trailing finish.
    awaited = [e[1] for e in events if e[0] == "await"]
    issued = [i for i, e in enumerate(events) if isinstance(e, Task)]
    assert sorted(awaited) == issued
