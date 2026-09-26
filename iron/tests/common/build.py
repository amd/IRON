# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The derived sequence, device-free.

Streams are bound to fake fifo handles that record what is issued, so the
order and access patterns of the fills and drains the library derives can be
checked without generating MLIR. What cannot be checked here is that the
recorded calls are what upstream's ObjectFifoHandle.fill/drain accept; that
is the toolchain's job and the operator tests' job.
"""

from typing import Any, cast

import numpy as np
import pytest
from aie.helpers.util import v8bfp16ebs8

from iron.common import In, Operator, Out, Shim, Value, auto, optional, param
from iron.common.design import Sequence, transfers
from iron.common.tiling import Access


class FakeGroup:
    """Upstream's TaskGroup refuses to exist outside a Runtime function."""

    def finish(self):
        pass


@pytest.fixture(autouse=True)
def fake_task_group(monkeypatch):
    # Patched where it is looked up, not where it is defined: runtime.py
    # imports the name, so rebinding aie.iron's attribute would not reach it.
    from iron.common.design import runtime

    monkeypatch.setattr(runtime, "TaskGroup", FakeGroup)


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


class Unary(Operator):
    size: int = param()
    tile: int = auto(1024)
    cols: int = auto()
    chans: int = auto(2)
    A = In(size, tile=(tile,), per=(cols, chans))
    B = Out(size, tile=(tile,), per=(cols, chans))

    def resolve(self, dev):
        import dataclasses

        return dataclasses.replace(self, cols=self.cols or dev.columns())


class MV(Operator):
    M: int = param()
    K: int = param()
    num_batches: int = param(default=1)
    cols: int = auto(2)
    tile_out: int = auto(64)
    A = In(optional(num_batches), M, K, tile=(tile_out, K), per=(cols,))
    B = In(optional(num_batches), K, tile=(K,), broadcast=True)
    C = Out(optional(num_batches), M, tile=(tile_out,), per=(cols,))


def _bind_all(op, log):
    for s in op.streams.values():
        for i in range(s.count):
            s.bind(FakeHandle(f"{s.name}{i}", log), i)


def test_plan_reproduces_the_channeled_unary_split():
    op = Unary(size=8192).resolved(FakeDev())
    p = transfers(op.A, op.streams["A"])
    assert len(p) == 8  # 4 columns x 2 channels
    chunk = 8192 // 8
    for i, (slot, accesses) in enumerate(p):
        assert slot.index == i
        assert accesses == [Access(8192, chunk * i, (1, 1, 1, chunk), (0, 0, 0, 1))]


def test_plan_batched_gemv_coalesces_and_broadcasts():
    op = MV(M=256, K=128, num_batches=100)
    a_transfers = transfers(op.A, op.streams["A"])
    assert [slot.index for slot, _ in a_transfers] == [0, 1]
    (acc,) = a_transfers[1][1]
    run = (256 // 2) * 128
    assert acc.offset == run and acc.sizes[1] == 100 and acc.strides[1] == 256 * 128
    b_slot, b_accesses = transfers(op.B, op.streams["B"])[0]
    assert b_slot is op.streams["B"] and b_accesses == [
        Access(100 * 128, 0, (1, 1, 1, 100 * 128), (0, 0, 0, 1))
    ]


def test_derived_sequence_issues_fills_then_waited_drains():
    log = []
    op = MV(M=256, K=128)
    _bind_all(op, log)
    rt = Sequence(op, {"A": "dA", "B": "dB", "C": "dC"})
    rt._derived()
    assert log == [
        ("fill", "A0", "dA", False),
        ("fill", "A1", "dA", False),
        ("fill", "B0", "dB", False),
        ("drain", "C0", "dC", True),
        ("drain", "C1", "dC", True),
    ]


def test_derived_sequence_names_a_buffer_without_a_stream():
    class NoStream(Operator):
        M: int = param()
        K: int = param()
        A = In(M, K)
        C = Out(M, tile=(64,))

    log = []
    op = NoStream(M=256, K=128)
    _bind_all(op, log)
    with pytest.raises(ValueError, match="NoStream.A has no tile="):
        Sequence(op, {"A": "dA", "C": "dC"})._derived()


def test_override_slices_and_issues_through_the_same_sequence():
    class Custom(MV):
        def sequence(self, rt):
            rows = self.M // self.cols
            rt.fill(self.B, self.B)
            with rt.group():
                for col in range(self.cols):
                    rt.fill(self.A.lane(col), self.A[col * rows : (col + 1) * rows, :])
                    rt.drain(self.C.lane(col), self.C[col * rows : (col + 1) * rows])

    log = []
    op = Custom(M=256, K=128)
    _bind_all(op, log)
    assert Custom.has_sequence_override() and not MV.has_sequence_override()
    op.sequence(Sequence(op, {"A": "dA", "B": "dB", "C": "dC"}))
    assert [(v, h) for v, h, _, _ in log] == [
        ("fill", "B0"),
        ("fill", "A0"),
        ("drain", "C0"),
        ("fill", "A1"),
        ("drain", "C1"),
    ]


def test_preamble_writes_residents_and_rejects_unbound_ones():
    class Op(Operator):
        n: int = param()
        tile: int = auto(64)
        A = In(n, tile=(tile,))
        count = Value(np.int32, derive=lambda op: op.n // op.tile)

    class FakeRTP(dict):
        pass

    rtps = [FakeRTP(), FakeRTP()]
    op = Op(n=640)
    op.count.bind(rtps)

    class FakeTarget:
        barriers = []
        image = "elf"

    target: Any = FakeTarget()
    Sequence(op, {}).preamble(target)
    assert rtps == [{0: 10}, {0: 10}]

    with pytest.raises(ValueError, match="never bound this value"):
        Sequence(Op(n=64), {}).preamble(target)


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

    op = MHA(num_heads=2, seq_len=1000, d=64, num_KV_heads=1, num_pipelines=8)
    op = op.resolved(Dev())
    assert op.seq_pad == 1024 and op.q_shims == 2 and op.join_rows == 256
    assert op.resident_values() == {
        "q_blocks_per_pipeline": 2,
        "kv_blocks": 16,
        "s_q": 1000,
        "s_kv": 1000,
        # Read only under a bound; the preamble skips them unbound.
        "q_blocks_valid": 2,
        "kv_blocks_valid": 16,
    }
    log = []
    for s in op.streams.values():
        for i in range(s.count):
            s.bind(Handle(f"{s.name}{i}", log), i)
    op.sequence(Sequence(op, {"Q": "dQ", "K": "dK", "V": "dV", "O": "dO"}))

    head, block = 1024 * 64, 256 * 64
    # Q: (heads, blocks, rows, d), one per slot. K and V: the re-read in the
    # iteration slot, the head's 1024 rows factored for the d1 wrap.
    q = {
        s: Access(2 * head, s * block, (2, 2, 256, 64), (head, 2 * block, 64, 1))
        for s in range(2)
    }
    kv = Access(head, 0, (4, 2, 512, 64), (0, 512 * 64, 64, 1))
    assert log == [
        ("fill", "Q0", "dQ", q[0], False),
        ("fill", "Q1", "dQ", q[1], False),
        ("fill", "K0", "dK", kv, False),
        ("fill", "V0", "dV", kv, False),
        ("drain", "O0", "dO", q[0], True),
        ("drain", "O1", "dO", q[1], True),
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
        num_pipelines=8,
        heads_interleaved=True,
    ).resolved(Dev())
    log = []
    for s in op.streams.values():
        for i in range(s.count):
            s.bind(Handle(f"{s.name}{i}", log), i)
    op.sequence(Sequence(op, {"Q": "dQ", "K": "dK", "V": "dV", "O": "dO"}))
    assert [name for name, _ in log] == ["Q0", "Q1", "K0", "V0", "O0", "O1"] * 2
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
    import iron.exports.flm.gemm.op as flm

    monkeypatch.setattr(flm, "AIEArch", _Arch)
    monkeypatch.setattr(flm, "get_target_model", lambda dev: _TargetModel())
    import iron.common.device as device

    monkeypatch.setattr(device.aie_utils, "ensure_current_device", lambda: _NPU2())
    import iron.exports.flm.gemm.design as design

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


def _record(op):
    log = []
    for s in op.streams.values():
        for i in range(s.count):
            s.bind(_Recorder(f"{s.name}{i}", log), i)
    return log


def test_flm_gemm_keyword_construction_tunes_from_the_device(flm):
    # Keyword construction leaves every knob to resolution, which reads the
    # device alone; the operator's extent is checked against the resolved
    # knobs by compatible(), not folded into its defaults.
    assert flm.GEMM(M=512, K=1024, N=1024).tile_n is None
    op = flm.GEMM(M=512, K=1024, N=1024).resolved(_NPU2())
    assert (op.tile_n, op.m_chunk, op.rows, op.cols, op.bfp16_b) == (64, 1, 4, 8, True)
    assert op.tile_ma == flm._default_l1(64, 128, 9 / 8, 65536, 1)[0]
    # tile_n is resolution, not a function of K: the same on every shape.
    assert flm.GEMM(M=256, K=512, N=1024).resolved(_NPU2()).tile_n == 64
    assert (
        op.config_name == f"FLM_GEMM_tn64_ck128_ma{op.tile_ma}_mc1_emf_conv_even_npu2"
    )
    assert op.name == op.config_name + "_M512_K1024_N1024"
    a, b, c = op.buffers
    assert a.shape == (512, 1024) and c.shape == (512, 1024)
    # B is declared in bfp16ebs8 blocks; the host holds the same bytes as uint8.
    assert b.shape == (1024 * 1024 // 8,) and b.dtype is v8bfp16ebs8
    assert b.host_shape == (flm.packed_b_size(1024, 1024, True),)
    assert b.host_dtype is np.uint8
    assert op.resident_values() == {
        "n_val": 1024,
        "m_row_blocks": 2,
        "k_iters": 2,
        "mode": 0,
        "clamp_min": int(np.float32(-np.inf).view(np.int32)),
        "clamp_max": int(np.float32(np.inf).view(np.int32)),
        "n_chunks": 2,
        "n_units": 2,
    }
    with pytest.raises(ValueError, match="multiple of 256"):
        flm.GEMM(M=100, K=1024, N=1024).resolved(_NPU2())  # M tiles to the array's rows
    with pytest.raises(ValueError, match="not in epilogue_modes"):
        flm.GEMM(M=256, K=1024, N=1024, epilogue="gelu", epilogue_modes=("none",))


def test_flm_gemm_layout_of_b_follows_the_device(flm):
    untuned = flm.GEMM(M=256, K=512, N=512)
    with pytest.raises(flm.Incompatible):
        [b.shape for b in untuned.buffers]  # B's layout follows the device
    assert untuned.resolved(_NPU2()).B.shape == (512 * 512 // 8,)


def test_flm_gemm_unsplit_sequence_issues_c_then_a_then_b_per_block(flm):
    op = flm.GEMM(M=512, K=1024, N=1024).resolved(_NPU2())
    log = _record(op)
    op.sequence(Sequence(op, {"A": "dA", "B": "dB", "C": "dC"}))
    verbs = [v for v, *_ in log]
    # Two column-blocks (N = 2 * 8 * 64): each drains C on eight columns,
    # then fills A on four rows and B on eight columns.
    block = ["drain"] * 8 + ["fill"] * 4 + ["fill"] * 8
    assert verbs == block * 2
    drains = [e for e in log if e[0] == "drain"]
    assert drains[1] == ("drain", "C1", 64, (1, 2, 256, 64), True)
    assert drains[8] == ("drain", "C0", 8 * 64, (1, 2, 256, 64), True)
    a_fills = [e for e in log if e[1].startswith("A")]
    assert a_fills[1] == ("fill", "A1", 64 * 1024, (2, 2, 64, 512), False)
    b_fills = [e for e in log if e[1].startswith("B")]
    # B's offsets are in v8bfp16ebs8 elements: values // 8.
    assert b_fills[1] == ("fill", "B1", 64 * 1024 // 8, (2, 2, 1, 512 * 64 // 8), False)


def test_flm_gemm_split_sequence_drains_one_row_block_at_a_time(flm):
    # N = 10240 puts C's row-block stride past the 20-bit step: c_split.
    op = flm.GEMM(M=512, K=1024, N=10240).resolved(_NPU2())
    assert op._c_split and not op._a_split
    log = _record(op)
    op.sequence(Sequence(op, {"A": "dA", "B": "dB", "C": "dC"}))
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
        ).resolved(Dev())
        log = _record(op)
        op.sequence(Sequence(op, {"x": "dx", "y": "dy"}))

        def moved(verb):
            return sum(s[0] * s[3] for v, _, _, s, _ in log if v == verb)

        return log, moved("fill"), moved("drain")

    log, filled, drained = run(1024)
    assert (filled, drained) == (1024, 1024)
    assert log[0] == ("fill", "x0", 0, (1, 1, 1, 256), False)
    assert log[-1] == ("drain", "y3", 768, (1, 1, 1, 256), True)
    # 1000: one whole partition, then a 232-element tail re-reading 8 from
    # the copied prefix so the last core still consumes a full line.
    log, filled, drained = run(1000)
    assert (filled, drained) == (1024, 1024)
    assert log[-1] == ("drain", "y3", 768, (1, 1, 1, 232), True)
    # 100: no whole partition, three idle cores, a 156-element pad.
    log, filled, drained = run(100)
    assert (filled, drained) == (256, 256)
    assert {name for _, name, *_ in log} == {"x3", "y3"}
    assert log[0] == ("fill", "x3", 0, (32, 1, 1, 4), True)


# --------------------------------------------------------------------------
# flm.gemm.Shipped: the sequence for a shipped image, device-free
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


def test_a_shipped_image_declares_its_pins_and_parameter_block():
    from iron.common import DeclarationError, Value, Xclbin
    from iron.exports.flm.gemm.shipped import Shipped

    op = Shipped(M=256, K=1024, N=1152)
    assert op.external.filename == "flm_mm_f81eba71.xclbin"
    pins = [op.A.lane(r).shim for r in range(4)] + [op.B.lane(3).shim]
    assert [(p.col, p.channel) for p in pins if p is not None] == [
        (0, 0),
        (2, 0),
        (4, 0),
        (6, 0),
        (3, 1),
    ]
    assert (op.rtp.address, op.rtp.lock) == (4096, 10)

    image = Xclbin(url="u", sha256="s", filename="f")
    # Nothing builds a shipped image's array, so the declaration has to say
    # where every stream enters and every value lives, and may not build.
    with pytest.raises(DeclarationError, match="pinned with via="):

        class Unpinned(Operator, image=image):
            n: int = param()
            x = In(n, tile=(64,))

    with pytest.raises(DeclarationError, match="needs an address"):

        class Unplaced(Operator, image=image):
            n: int = param()
            x = In(n, tile=(64,), via=Shim(0))
            count = Value(np.int32, derive=lambda op: op.n)

    with pytest.raises(DeclarationError, match="nothing builds its array"):

        class Built(Operator, image=image):
            n: int = param()
            x = In(n, tile=(64,), via=Shim(0))

            def array(self, target):
                return []


def test_shipped_sequence_writes_every_core_then_streams_in_consume_order():
    from iron.common.external import LOCK_ADDRESS_BASE, run_sequence
    from iron.exports.flm.gemm.shipped import Shipped

    op = Shipped(M=256, K=1024, N=1152, epilogue="gelu", clamp=(-2.0, 2.0))
    # The port's values are hidden; the image's block is laid out from the
    # operator's fields.
    assert list(op.residents) == ["rtp"]
    assert op.resident_values() == {
        "rtp": [2, 256, 1152, 0, 1, 1, -1073741824, 1073741824]
    }
    rec = _ForeignRecorder()
    cores = [(c, r) for r in range(2, 6) for c in range(8)]
    run_sequence(op, {"A": "dA", "B": "dB", "C": "dC"}, cores, rec)
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
        ("start", ("A", 0), "dA", 0, (1, 2, 64, 512), (0, 512, 1024, 1)),
        ("start", ("B", 0), "dB", 0, (1, 1, 1, 131072), (0, 0, 0, 1)),
        ("start", ("C", 0), "dC", 0, (1, 1, 256, 128), (0, 0, 1152, 1)),
    ]
    assert starts[5] == (
        "start",
        ("A", 1),
        "dA",
        64 * 1024,
        (1, 2, 64, 512),
        (0, 512, 1024, 1),
    )
    # Every task is awaited exactly once, the last ones by the trailing finish.
    awaited = [e[1] for e in rec.log if e[0] == "await"]
    assert sorted(awaited) == sorted((k, n) for n, (_, k, *_) in enumerate(starts, 1))


# --------------------------------------------------------------------------
# A per-call size in a transfer
# --------------------------------------------------------------------------


class _SizedHandle:
    """A fifo handle whose fill takes the assumed size-kind parameter."""

    def __init__(self, log):
        self.log = log

    def fill(self, data, tap, wait, group, offset_parameter, size_parameters=None):
        self.log.append(("fill", data, offset_parameter, size_parameters))

    def drain(self, data, tap, wait, group, offset_parameter, size_parameters=None):
        self.log.append(("drain", data, offset_parameter, size_parameters))


class _DynamicHandle:
    """A fifo handle on the dispatch path: sizes and offsets are scalars."""

    def __init__(self, log):
        self.log = log

    def fill(self, data, *, sizes, strides, offset, transfer_len, wait, group):
        self.log.append(("fill", data, sizes, offset))


def _bounded_unary():
    from iron.tests.common.declare import Rows

    op = Rows(rows=64, cols=8).resolved(FakeDev())
    op.use_value("valid", "n")  # what a graph does for x[:n]
    for name in ("valid", "count"):
        op.value(name).param = f"<{name}>"
    return op


def test_a_size_patch_names_the_dimension_and_the_word():
    log = []
    op = _bounded_unary()
    op.streams["x"].bind(_SizedHandle(log), 0)
    rt = Sequence(op, {"x": "dx", "y": "dy"})
    acc = Access(64 * 8, 0, (1, 1, 32, 8), (0, 0, 16, 1))
    rt.fill(op.x.lane(0), acc, size_by={2: op.value("count")})
    assert log == [("fill", "dx", None, {2: "<count>"})]
    with pytest.raises(ValueError, match="dimensions 0..3"):
        rt.fill(op.x.lane(0), acc, size_by={4: op.value("count")})
    with pytest.raises(TypeError, match="value member's word"):
        rt.fill(op.x.lane(0), acc, size_by={2: 32})  # a number, not a word


def test_a_size_patch_needs_the_toolchain_kind_or_the_dispatch_path():
    log = []
    op = _bounded_unary()
    op.streams["x"].bind(FakeHandle("x0", log), 0)  # no size_parameters= upstream
    rt = Sequence(op, {"x": "dx", "y": "dy"})
    acc = Access(64 * 8, 0, (1, 1, 32, 8), (0, 0, 16, 1))
    with pytest.raises(NotImplementedError, match="size-kind scratchpad parameter"):
        rt.fill(op.x.lane(0), acc, size_by={2: op.value("count")})
    # On the dispatch path the scalar stands in for the size itself.
    op = _bounded_unary()
    op.streams["x"].bind(_DynamicHandle(log), 0)
    op.value("count").ssa = cast(Any, "<n>")
    rt = Sequence(op, {"x": "dx", "y": "dy"})
    rt.fill(op.x.lane(0), acc, size_by={2: op.value("count")})
    assert log == [("fill", "dx", [1, 1, "<n>", 8], 0)]


def test_a_bounded_operand_goes_round_robin_over_the_lanes():
    """Under a bound each lane reads every ``lanes``-th tile from a fixed
    offset, so one patched count serves every lane; the descriptor is built
    for the full extent.
    """
    from iron.common.design.runtime import bounded_transfers
    from iron.tests.common.declare import Rows

    op = Rows(rows=64, cols=8).resolved(FakeDev())
    plan = bounded_transfers(op.x, op.streams["x"], 0)
    assert [(slot.index, acc, dim) for slot, acc, dim in plan] == [
        (0, Access(512, 0, (1, 32, 1, 8), (0, 16, 0, 1)), 1),
        (1, Access(512, 8, (1, 32, 1, 8), (0, 16, 0, 1)), 1),
    ]
    # A leading batch axis is the outer repeat; the tile count keeps its slot.
    batched = MV(M=256, K=128, num_batches=3).resolved(FakeDev())
    (slot, acc, dim), *_ = bounded_transfers(batched.A, batched.streams["A"], 1)
    # The 64 x 128 tile is a run past one wrap, so it takes the two inner
    # slots as 8 x 1024; the tile count sits above them.
    assert acc == Access(
        3 * 256 * 128, 0, (3, 2, 8, 1024), (256 * 128, 2 * 64 * 128, 1024, 1)
    )
    assert dim == 1 and (batched.M // (2 * 64)) == 2


def test_the_derived_sequence_patches_a_bounded_operand():
    log = []
    op = _bounded_unary()
    for name in ("valid_x", "valid_y"):
        op.value(name).param = f"<{name}>"
    for s in op.streams.values():
        for i in range(s.count):
            s.bind(_SizedHandle(log), i)
    rt = Sequence(op, {"x": "dx", "y": "dy"})
    rt._derived()
    assert log == [
        ("fill", "dx", None, {1: "<valid_x>"}),
        ("fill", "dx", None, {1: "<valid_x>"}),
        ("drain", "dy", None, {1: "<valid_y>"}),
        ("drain", "dy", None, {1: "<valid_y>"}),
    ]
    assert op.derived_at("valid_x", valid=16) == 8  # the word: 16 rows over 2 lanes


def test_a_bounded_gemv_moves_a_and_c_in_output_tiles_round_robin(npu2):
    """Under a bound on M, B goes whole as ever, then each column takes A in
    output tiles (two input tiles each here) and C in the same tiles, both
    patched by the tile count the core also reads.
    """
    from aie.iron.device import from_name

    from iron.operators.gemv.op import GEMV

    op = GEMV(M=256, K=64, num_aie_columns=2, tile_size_input=2, tile_size_output=4)
    op.use_value("valid", "n")
    op = op.resolved(from_name("npu2", n_cols=8))
    assert [v.name for v in op.values] == ["valid", "tiles", "valid_A", "valid_C"]
    assert op.derived_at("tiles", valid=64) == 64 // (2 * 4)
    assert op.derived_at("valid_A", valid=64) == 64 // (2 * 4)  # unit: output tiles
    log = []
    for name in ("valid_A", "valid_C"):
        op.value(name).param = f"<{name}>"
    for s in op.streams.values():
        for i in range(s.count):
            s.bind(_SizedHandle(log), i)
    Sequence(op, {"A": "dA", "B": "dB", "C": "dC"}).run()
    assert log == [
        ("fill", "dB", None, None),
        ("fill", "dB", None, None),
        ("fill", "dA", None, {1: "<valid_A>"}),
        ("fill", "dA", None, {1: "<valid_A>"}),
        ("drain", "dC", None, {1: "<valid_C>"}),
        ("drain", "dC", None, {1: "<valid_C>"}),
    ]


def test_a_bounded_repeat_patches_the_stack_axis():
    from iron.operators.repeat import Repeat

    op = Repeat(rows=4, cols=8, seq=32, repeat=2).resolved(FakeDev())
    op.use_value("valid_seq", "c")
    log = []
    for name in ("valid_seq_x", "valid_seq_y"):
        op.value(name).param = f"<{name}>"
    for s in op.streams.values():
        s.bind(_SizedHandle(log))
    Sequence(op, {"x": "dx", "y": "dy"}).run()
    assert log == [
        ("fill", "dx", None, {2: "<valid_seq_x>"}),
        ("drain", "dy", None, {2: "<valid_seq_y>"}),
    ]
