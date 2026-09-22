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


class FakeGroup:
    """Upstream's TaskGroup refuses to exist outside a Runtime function."""

    def finish(self):
        pass


@pytest.fixture(autouse=True)
def fake_task_group(monkeypatch):
    import aie.iron

    monkeypatch.setattr(aie.iron, "TaskGroup", FakeGroup, raising=False)


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
        image = "elf"

    _preamble(Sequence(op, ov, {}), op, ov, FakeTarget())
    assert rtps == [{0: 10}, {0: 10}]

    @operator
    class Forgetful(Operator[Counted]):
        n: int = dim()
        A = In(n, to=Counted.s)

    with pytest.raises(ValueError, match="does not supply it"):
        _preamble(Sequence(op, ov, {}), Forgetful(ov, n=64), ov, FakeTarget())


def test_mha_sequence_is_one_descriptor_set_per_kv_group(monkeypatch):
    # mha/op.py with eight pipelines: Q and O go through two shims, each
    # carrying four pipelines' (256-row) block. Per KV group, each shim's Q
    # is one pattern over the group's heads and every block, K and V are the
    # head's slab re-read once per (head, block) from the iteration slot, and
    # the O drains mirror the Q fills and wait.
    from iron.operators.mha.op import MHA

    monkeypatch.setattr(Access, "tap", lambda self: self)

    class Dev:
        def resolve(self):
            class R:
                name = "npu2"

            return R()

    class Handle:
        def __init__(self, name, log):
            self.name, self.log = name, log

        def fill(self, data, tap, wait, group, offset_parameter):
            self.log.append(("fill", self.name, data, tap, wait))

        def drain(self, data, tap, wait, group, offset_parameter):
            self.log.append(("drain", self.name, data, tap, wait))

    op = MHA(num_heads=2, seq_len=1000, d=64, num_KV_heads=1, num_of_pipelines=8)
    op = op.tuned(Dev())
    ov = op.ov
    assert op.seq_pad == 1024 and ov.q_shims == 2 and ov.join_rows == 256
    assert op.residents() == {
        "q_blocks_per_pipeline": 2,
        "kv_blocks": 16,
        "s_q": 1000,
        "s_kv": 1000,
    }
    log = []
    for s in ov.streams.values():
        for i in range(s.count):
            s.bind(Handle(f"{s.name}{i}", log), i)
    op.design(Sequence(op, ov, {"Q": "dQ", "K": "dK", "V": "dV", "O": "dO"}))

    head, block = 1024 * 64, 256 * 64
    # Q: (heads, blocks, rows, d), one per slot. K and V: the re-read in the
    # iteration slot, the head's 1024 rows factored for the d1 wrap.
    q = {
        s: Access(2 * head, s * block, (2, 2, 256, 64), (head, 2 * block, 64, 1))
        for s in range(2)
    }
    kv = Access(head, 0, (4, 2, 512, 64), (0, 512 * 64, 64, 1))
    assert log == [
        ("fill", "q0", "dQ", q[0], False),
        ("fill", "q1", "dQ", q[1], False),
        ("fill", "k0", "dK", kv, False),
        ("fill", "v0", "dV", kv, False),
        ("drain", "o0", "dO", q[0], True),
        ("drain", "o1", "dO", q[1], True),
    ]


def test_mha_sequence_over_interleaved_heads_is_strided_the_same_way(monkeypatch):
    # The (seq, heads, d) layout: a head's rows are strided by every head's
    # d, and the group's heads are d apart; the descriptor count is the same.
    from iron.operators.mha.op import MHA

    monkeypatch.setattr(Access, "tap", lambda self: self)

    class Dev:
        def resolve(self):
            class R:
                name = "npu2"

            return R()

    class Handle:
        def __init__(self, name, log):
            self.name, self.log = name, log

        def fill(self, data, tap, wait, group, offset_parameter):
            self.log.append((self.name, tap))

        def drain(self, data, tap, wait, group, offset_parameter):
            self.log.append((self.name, tap))

    op = MHA(
        num_heads=4,
        seq_len=1024,
        d=64,
        num_KV_heads=2,
        num_of_pipelines=8,
        heads_interleaved=True,
    ).tuned(Dev())
    ov = op.ov
    log = []
    for s in ov.streams.values():
        for i in range(s.count):
            s.bind(Handle(f"{s.name}{i}", log), i)
    op.design(Sequence(op, ov, {"Q": "dQ", "K": "dK", "V": "dV", "O": "dO"}))
    assert [name for name, _ in log] == ["q0", "q1", "k0", "v0", "o0", "o1"] * 2
    q0, q1, k0, *_ = [tap for _, tap in log[:6]]
    # Q: (heads 2 at stride d, blocks 2, rows 256 at stride 4d, d)
    assert q0.sizes == (2, 2, 256, 64) and q0.strides == (64, 2 * 256 * 256, 256, 1)
    assert q1.offset == q0.offset + 256 * 256
    # K: the head's 1024 rows at stride 2d, re-read 4 times, rows factored for d1.
    assert k0.sizes == (4, 2, 512, 64) and k0.strides == (0, 512 * 128, 128, 1)
    # The second group starts at its heads.
    assert log[6][1].offset == 2 * 64 and log[8][1].offset == 64


def test_mha_infers_the_padded_length_and_the_kv_head_count():
    from iron.operators.mha.op import MHA

    op = MHA.from_operands((8, 128, 64), (2, 128, 64), (2, 128, 64))
    assert (op.num_heads, op.num_KV_heads, op.seq_len, op.seq_pad) == (8, 2, 128, 128)
    with pytest.raises(ValueError, match="seq_pad=100"):
        MHA(num_heads=1, seq_len=100, seq_pad=100, d=64)


# --------------------------------------------------------------------------
# flm/gemm: the configuration/shape split, device-free
# --------------------------------------------------------------------------


class _Arch:
    AIE2p = "aie2p"
    AIE2 = "aie2"


class _NPU2:
    cols = 8
    arch = _Arch.AIE2p

    def resolve(self):
        class R:
            name = "npu2"

        return R()


class _TargetModel:
    def rows(self):
        return 6

    def get_num_mem_tile_rows(self):
        return 1

    def get_local_memory_size(self):
        return 65536

    def get_num_bds(self, col, row):
        return 16


@pytest.fixture
def flm(monkeypatch):
    import iron.operators.flm.gemm.op as flm

    monkeypatch.setattr(flm, "AIEArch", _Arch)
    monkeypatch.setattr(flm, "get_target_model", lambda dev: _TargetModel())
    monkeypatch.setattr(flm.aie_utils, "get_current_device", lambda: _NPU2())
    import iron.operators.flm.gemm.design as design

    monkeypatch.setattr(design, "get_target_model", lambda dev: _TargetModel())
    monkeypatch.setattr(Access, "tap", lambda self: self)
    return flm


class _Recorder:
    def __init__(self, name, log):
        self.name, self.log = name, log

    def fill(self, data, tap, wait, group, offset_parameter):
        self.log.append(("fill", self.name, tap.offset, tap.sizes, wait))

    def drain(self, data, tap, wait, group, offset_parameter):
        self.log.append(("drain", self.name, tap.offset, tap.sizes, wait))


def _record(ov):
    log = []
    for s in ov.streams.values():
        for i in range(s.count):
            s.bind(_Recorder(f"{s.name}{i}", log), i)
    return log


def test_flm_gemm_keyword_construction_tunes_from_the_device(flm):
    # Keyword construction leaves every tunable to the overlay's tuning,
    # which reads the device alone; the operator's extent is checked against
    # the tuned overlay by compatible(), not folded into its defaults.
    assert flm.GEMM(M=512, K=1024, N=1024).ov.tile_n is None
    op = flm.GEMM(M=512, K=1024, N=1024).tuned(_NPU2())
    ov = op.ov
    assert (ov.tile_n, ov.m_chunk, ov.rows, ov.cols, ov.bfp16_b) == (64, 1, 4, 8, True)
    assert ov.tile_ma == flm._default_l1(64, 128, 9 / 8, 65536, 1)[0]
    # tile_n is tuning, not a function of K: the same on every shape.
    assert flm.GEMM(M=256, K=512, N=1024).tuned(_NPU2()).ov.tile_n == 64
    assert (
        op.config_name == f"FLM_GEMM_tn64_ck128_ma{ov.tile_ma}_mc1_emf_conv_even_npu2"
    )
    assert op.name == op.config_name + "_M512_K1024_N1024"
    a, b, c = op.buffers
    assert a.shape == (512, 1024) and c.shape == (512, 1024)
    assert b.shape == (flm.packed_b_size(1024, 1024, True),) and b.dtype is np.uint8
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
        flm.GEMM(M=100, K=1024, N=1024).tuned(_NPU2())  # M tiles to the array's rows
    with pytest.raises(ValueError, match="not in epilogue_modes"):
        flm.GEMM(M=256, K=1024, N=1024, epilogue="gelu", epilogue_modes=("none",))


def test_flm_gemm_declared_overlay_tunes_from_the_device_only(flm):
    ov = flm.FLMGEMMOverlay().tuned(_NPU2())
    assert ov.tile_n == 64  # no K to look at: the general winner
    op = flm.GEMM(ov, M=256, K=512, N=512)
    assert op.ov.tile_n == 64
    untuned = flm.GEMM(flm.FLMGEMMOverlay(), M=256, K=512, N=512)
    with pytest.raises(flm.Incompatible, match="tuned overlay"):
        [b.shape for b in untuned.buffers]  # B's layout follows the device


def test_flm_gemm_unsplit_sequence_issues_c_then_a_then_b_per_block(flm):
    op = flm.GEMM(M=512, K=1024, N=1024).tuned(_NPU2())
    ov = op.ov
    log = _record(ov)
    op.design(Sequence(op, ov, {"A": "dA", "B": "dB", "C": "dC"}))
    verbs = [v for v, *_ in log]
    # Two column-blocks (N = 2 * 8 * 64): each drains C on eight columns,
    # then fills A on four rows and B on eight columns.
    block = ["drain"] * 8 + ["fill"] * 4 + ["fill"] * 8
    assert verbs == block * 2
    drains = [e for e in log if e[0] == "drain"]
    assert drains[1] == ("drain", "c1", 64, (1, 2, 256, 64), True)
    assert drains[8] == ("drain", "c0", 8 * 64, (1, 2, 256, 64), True)
    a_fills = [e for e in log if e[1].startswith("a")]
    assert a_fills[1] == ("fill", "a1", 64 * 1024, (2, 2, 64, 512), False)
    b_fills = [e for e in log if e[1].startswith("b")]
    # B's offsets are in v8bfp16ebs8 elements: values // 8.
    assert b_fills[1] == ("fill", "b1", 64 * 1024 // 8, (2, 2, 1, 512 * 64 // 8), False)


def test_flm_gemm_split_sequence_drains_one_row_block_at_a_time(flm):
    # N = 10240 puts C's row-block stride past the 20-bit step: c_split.
    op = flm.GEMM(M=512, K=1024, N=10240).tuned(_NPU2())
    assert op._c_split and not op._a_split
    ov = op.ov
    log = _record(ov)
    op.design(Sequence(op, ov, {"A": "dA", "B": "dB", "C": "dC"}))
    drains = [e for e in log if e[0] == "drain"]
    assert len(drains) == 20 * 8 * 2  # blocks x columns x row-blocks
    assert all(sizes == (1, 1, 256, 64) for _, _, _, sizes, _ in drains)


def test_mem_copy_sequence_pads_a_remainder_to_a_full_line(monkeypatch):
    # mem_copy/op.py: whole partitions split evenly; the remainder is padded
    # to one line per core by re-reading copied data, in awaited groups of
    # four transfers on the last fifo.
    from iron.operators.mem_copy import MemCopy

    monkeypatch.setattr(Access, "tap", lambda self: self)

    class Dev:
        def resolve(self):
            class R:
                name = "npu2"

            return R()

    def run(size):
        op = MemCopy(
            size=size, num_cores=4, num_channels=1, bypass=False, tile_size=256
        ).tuned(Dev())
        log = _record(op.ov)
        op.design(Sequence(op, op.ov, {"x": "dx", "y": "dy"}))
        moved = lambda verb: sum(s[0] * s[3] for v, _, _, s, _ in log if v == verb)  # noqa: E731
        return log, moved("fill"), moved("drain")

    log, filled, drained = run(1024)
    assert (filled, drained) == (1024, 1024)
    assert log[0] == ("fill", "s0", 0, (1, 1, 1, 256), False)
    assert log[-1] == ("drain", "d3", 768, (1, 1, 1, 256), True)
    # 1000: one whole partition, then a 232-element tail re-reading 8 from
    # the copied prefix so the last core still consumes a full line.
    log, filled, drained = run(1000)
    assert (filled, drained) == (1024, 1024)
    assert log[-1] == ("drain", "d3", 768, (1, 1, 1, 232), True)
    # 100: no whole partition, three idle cores, a 156-element pad.
    log, filled, drained = run(100)
    assert (filled, drained) == (256, 256)
    assert {name for _, name, *_ in log} == {"s3", "d3"}
    assert log[0] == ("fill", "s3", 0, (32, 1, 1, 4), True)


# --------------------------------------------------------------------------
# flm.gemm.Shipped: an external overlay's sequence, device-free
# --------------------------------------------------------------------------


class _ForeignRecorder:
    def __init__(self):
        self.log, self.n = [], 0

    def write32(self, address, value, col, row):
        self.log.append(("w", address, value, col, row))

    def start(self, key, buffer, offset, sizes, strides):
        self.n += 1
        self.log.append(("start", key, buffer, offset, tuple(sizes), tuple(strides)))
        return (key, self.n)

    def await_(self, task):
        self.log.append(("await", task))


def test_external_overlay_declares_its_pins_and_parameter_block():
    from iron.common.declare import DeclarationError, Xclbin
    from iron.operators.flm.gemm.shipped import Shipped

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
    from iron.common.external import LOCK_ADDRESS_BASE, run_sequence
    from iron.operators.flm.gemm.op import GEMM
    from iron.operators.flm.gemm.shipped import Shipped

    ov = Shipped()
    op = GEMM(ov, M=256, K=1024, N=1152, epilogue="gelu", clamp=(-2.0, 2.0))
    # The port's residents are hidden; the image's block is laid out from
    # the operator's values.
    assert list(ov.residents) == ["rtp"]
    assert ov.resident_values(op) == {
        "rtp": [2, 256, 1152, 0, 1, 1, -1073741824, 1073741824]
    }
    rec = _ForeignRecorder()
    cores = [(c, r) for r in range(2, 6) for c in range(8)]
    run_sequence(op, ov, {"A": "dA", "B": "dB", "C": "dC"}, cores, rec)
    writes = [e for e in rec.log if e[0] == "w"]
    # 8 words on 32 cores, then one lock release per core, before any DMA.
    assert len(writes) == 32 * 8 + 32
    assert writes[0] == ("w", 4096, 2, 0, 2) and writes[7] == (
        "w",
        4124,
        1073741824,
        0,
        2,
    )
    assert writes[-1] == ("w", LOCK_ADDRESS_BASE + 16 * 10, 1, 7, 5)
    assert rec.log.index(writes[-1]) < rec.log.index(
        next(e for e in rec.log if e[0] == "start")
    )
    starts = [e for e in rec.log if e[0] == "start"]
    # N = 9 column-blocks: one full sweep (4 A + 8 B + 8 C) and a trailing
    # block on column 0 alone, which still receives A on every row.
    assert len(starts) == 20 + 6
    assert starts[:3] == [
        ("start", ("a", 0), "dA", 0, (1, 2, 64, 512), (0, 512, 1024, 1)),
        ("start", ("b", 0), "dB", 0, (1, 1, 1, 131072), (0, 0, 0, 1)),
        ("start", ("c", 0), "dC", 0, (1, 1, 256, 128), (0, 0, 1152, 1)),
    ]
    assert starts[5] == (
        "start",
        ("a", 1),
        "dA",
        64 * 1024,
        (1, 2, 64, 512),
        (0, 512, 1024, 1),
    )
    # Every task is awaited exactly once, the last ones by the trailing finish.
    awaited = [e[1] for e in rec.log if e[0] == "await"]
    assert sorted(awaited) == sorted((k, n) for n, (_, k, *_) in enumerate(starts, 1))
