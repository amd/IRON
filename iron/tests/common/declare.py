# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The declaration layer, device-free.

Everything here runs without a device and without generating MLIR: what
class creation records and rejects, how bound members resolve on instances,
how inference binds fields from operand shapes, and how resolution behaves.
The design-generating half is ``iron/common/design/`` and needs the
toolchain.
"""

import contextlib
import dataclasses

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import (
    DeclarationError,
    DispatchTime,
    Extent,
    In,
    Incompatible,
    Operator,
    Out,
    Profile,
    Scratchpad,
    Shim,
    Unresolvable,
    Value,
    auto,
    from_spec,
    optional,
    param,
)
from iron.common.declare.field import DimRef
from iron.common.declare.infer import infer


class FakeDev:
    def __init__(self, cols=8):
        self.cols = cols

    def columns(self):
        return self.cols


# --------------------------------------------------------------------------
# A worked operator, close to GEMV
# --------------------------------------------------------------------------


class MV(Operator):
    M: int = param()
    K: int = param()
    num_batches: int = param(default=1)
    columns: int | None = auto()
    tile_out: int = auto(64)
    vec: int | None = auto(repr=False)
    epilogue: str = param(default="none", array=True)

    A = In(optional(num_batches), M, K, tile=(tile_out, K), per=columns)
    B = In(optional(num_batches), K, tile=(K,), broadcast=True)
    C = Out(optional(num_batches), M, tile=(tile_out,), per=columns)
    count = Value(np.int32, derive=lambda op: op.M // (op.columns * op.tile_out))
    start = Value(np.int32)  # per-call when a graph binds it, else unused

    def resolve(self, dev):
        cols = self.columns or dev.columns()
        vec = self.vec or next((w for w in (64, 32, 16) if self.K % w == 0), None)
        if vec is None:
            raise Unresolvable(f"K={self.K}: no vector width divides it")
        return dataclasses.replace(self, columns=cols, vec=vec)

    def compatible(self):
        assert self.columns is not None
        unit = self.columns * self.tile_out
        if self.M % unit:
            raise Incompatible(f"M={self.M} is not a multiple of {unit}")

    def uses_value(self, name):
        return name in self.used_values if name == "start" else super().uses_value(name)

    def array(self, target):
        return [self.K, self.columns, self.tile_out, self.epilogue]

    def reference(self, A, B):
        return A @ B


# --------------------------------------------------------------------------
# Class creation: names, order, re-attached fields
# --------------------------------------------------------------------------


def test_fields_are_reattached_as_dim_refs():
    assert isinstance(MV.K, DimRef) and MV.K.owner is MV
    assert MV.K.name == "K" and MV.K.tier == "param"
    assert isinstance(MV.tile_out, DimRef) and MV.tile_out.tier == "auto"


def test_members_keep_declaration_order_and_names():
    # An operand's own stream follows it, under its name.
    assert [m.name for m in MV._members] == [
        "A",
        "A",
        "B",
        "B",
        "C",
        "C",
        "count",
        "start",
    ]
    assert MV.A.direction == "in" and MV.C.direction == "out"
    assert MV.A.stream is not None and MV.A.stream.direction == "in"


def test_shapes_captured_bare_names_resolve_to_refs():
    # ``M`` and ``num_batches`` were Field objects in the class body; class
    # creation rewrote them to DimRefs on the class.
    dims = MV.A.dims
    assert dims[0].ref.name == "num_batches"
    assert dims[1] == MV.M and dims[2] is MV.K
    assert MV.A.stream is not None
    assert MV.A.stream.dims == (MV.tile_out, MV.K) and MV.A.stream.per == (MV.columns,)


def test_dataclass_constructor_is_typed_by_real_fields():
    assert [f.name for f in dataclasses.fields(MV)] == [
        "M",
        "K",
        "num_batches",
        "columns",
        "tile_out",
        "vec",
        "epilogue",
    ]


# --------------------------------------------------------------------------
# Rules rejected at class creation
# --------------------------------------------------------------------------


def test_a_knob_may_name_a_tile_but_not_a_buffer_shape():
    assert MV.A.stream is not None and MV.A.stream.dims[0] is MV.tile_out
    with pytest.raises(DeclarationError, match="host shape may not depend on tuning"):

        class Bad(Operator):
            M: int = param()
            t: int = auto(64)
            A = In(M, t)


def test_plain_defaulted_field_in_a_shape_is_its_literal():
    # A plain field with a default is bound to that default in the class
    # body, so a shape written against it captures the literal, not the
    # field. This is why anything a shape names must be declared with param().
    class Plain(Operator):
        n: int = 4
        x = In(n, tile=(n,))

    assert Plain.x.dims == (4,)
    assert Plain(n=8).x.shape == (4,)


def test_plain_field_reference_from_outside_is_rejected():
    class Plain(Operator):
        n: int = 4
        x = In(4)

    with pytest.raises(DeclarationError, match="not declared with param"):

        class Bad(Plain):
            M: int = param()
            A = In(M, Plain.n)


def test_expression_in_a_shape_is_rejected():
    with pytest.raises(DeclarationError, match="Expressions are not allowed"):

        class Bad(Operator):
            n: int = param()
            x = In("n // 2")


def test_annotated_member_is_rejected():
    with pytest.raises(DeclarationError, match="without an annotation"):

        class Bad(Operator):
            M: int = param()
            A: In = In(M)


def test_float_scratchpad_is_rejected():
    with pytest.raises(DeclarationError, match="floating point"):
        Scratchpad(np.float32)


def test_per_and_broadcast_are_exclusive():
    with pytest.raises(DeclarationError, match="either per"):

        class Bad(Operator):
            n: int = param()
            c: int = auto(2)
            x = In(n, tile=(4,), per=(c,), broadcast=True)


# --------------------------------------------------------------------------
# Bound members on instances
# --------------------------------------------------------------------------


def test_buffers_resolve_shape_dtype_and_direction():
    specs = MV(M=64, K=256, num_batches=2).buffers
    assert [(s.direction, s.shape) for s in specs] == [
        ("in", (2, 64, 256)),
        ("in", (2, 256)),
        ("out", (2, 64)),
    ]
    assert specs[0].dtype is bfloat16
    op = MV(M=1024, K=256)
    assert [b.name for b in op.inputs] == ["A", "B"]
    assert [b.name for b in op.outputs] == ["C"]


def test_an_optional_dim_is_omitted_when_one_and_may_sit_anywhere():
    assert MV(M=64, K=256).A.shape == (64, 256)
    assert MV(M=64, K=256, num_batches=3).C.shape == (3, 64)

    class Stack(Operator):
        rows: int = param()
        cols: int = param()
        seq: int = param(default=1)
        x = In(rows, optional(seq), cols)
        y = Out(rows, optional(seq), cols)

    assert infer(Stack, (8, 64)) == {"rows": 8, "cols": 64, "seq": 1}
    assert infer(Stack, (8, 16, 64)) == {"rows": 8, "cols": 64, "seq": 16}
    with pytest.raises(ValueError, match="rank 4"):
        infer(Stack, (8, 2, 16, 64))
    assert Stack(rows=8, cols=64).x.shape == (8, 64)
    assert Stack(rows=8, cols=64, seq=16).y.shape == (8, 16, 64)


class _RecordingRuntime:
    """What a sequence hands ``rt.fill``/``rt.drain``: ``(buffer name, descriptor)``."""

    def __init__(self) -> None:
        self.calls: list = []

    @contextlib.contextmanager
    def group(self):
        yield self

    def fill(self, buffer, tap, **_):
        self.calls.append(("fill", buffer.name, tap))

    def drain(self, buffer, tap, **_):
        self.calls.append(("drain", buffer.name, tap))


def test_a_stack_and_its_flat_spelling_move_the_same_descriptors():
    """``Repeat`` on the cache ``(G, L, D)`` is the repeat on ``(G, L * D)``:
    the same rows, the same row length, the same transfers.
    """
    from iron.operators.repeat import Repeat

    flat = Repeat(rows=8, cols=2048 * 64, repeat=4, tile_size=64)
    stack = Repeat(rows=8, seq=2048, cols=64, repeat=4)
    assert stack.x.shape == (8, 2048, 64) and stack.y.shape == (32, 2048, 64)
    taps = []
    for op in (flat, stack):
        rt = _RecordingRuntime()
        op.resolved(FakeDev(cols=8)).sequence(rt)
        taps.append(rt.calls)
    assert taps[0] == taps[1]
    assert stack.resolved(FakeDev(cols=8)).tile_size == 64  # the row's last axis


def test_explain_says_what_a_build_compiles_in_and_what_it_takes_per_call():
    op = MV(M=1024, K=128, columns=2)
    lines = op.explain().splitlines()
    assert lines[0].startswith("MV(") and lines[0].endswith("(unresolved)")
    assert lines[1] == (
        "  array, compiled into every core: K=128, columns=2, tile_out=64, "
        "epilogue='none'"
    )
    assert lines[2] == "  sequence, the host's alone: M=1024, num_batches=1, vec=None"
    assert lines[3] == "  count: written once per build"
    assert lines[4] == "  start: unused here"  # MV binds it only when a graph does
    resolved = op.resolved(FakeDev(cols=8)).explain().splitlines()
    assert resolved[0].endswith("(resolved)") and "vec=64" in resolved[2]
    assert resolved[3] == "  count: written once per build, 8 here"
    op.use_value("count")  # a graph binds them: per call from here on
    op.use_value("start")
    assert op.explain().splitlines()[3:] == [
        "  count: per call, a scratchpad word patched or read",
        "  start: per call, a scratchpad word patched or read",
    ]


def test_buffers_carry_the_declared_dtype_and_size():
    """The sizing contract: the sequence layout and the test harness allocate
    from ``b.dtype`` and ``b.nbytes`` of a declared buffer.
    """
    from iron.operators.repeat import Repeat

    x, y = Repeat(rows=8, cols=64, repeat=4, dtype=np.int32).buffers
    assert x.dtype == np.int32 and y.dtype == np.int32
    assert (x.direction, y.direction) == ("in", "out")
    assert y.nbytes == 8 * 64 * 4 * 4


def test_instance_values_shadow_dim_refs():
    op = MV(M=64, K=256, columns=2)
    assert op.K == 256 and op.columns == 2
    assert isinstance(MV.K, DimRef) and MV.K.name == "K"


def test_a_stream_is_bound_lane_by_lane():
    op = MV(M=1024, K=256, columns=2)
    op.A.lane(0).bind("h0")
    op.A.lane(1).bind("h1")
    op.B.bind("hb")
    assert op.A.handles == ["h0", "h1"]
    assert op.B.handle == "hb"
    with pytest.raises(ValueError, match="already bound"):
        op.A.lane(0).bind("again")
    with pytest.raises(ValueError, match="never bound"):
        op.C.handles
    with pytest.raises(ValueError, match="index it"):
        op.A.handle

    class NoTile(Operator):
        n: int = param()
        x = In(n)

    with pytest.raises(TypeError, match="without a tile"):
        NoTile(n=4).x.tile


def test_per_call_values_bind_on_the_operator():
    class Copy(Operator):
        n: int = param()
        src = In(n, tile=(n,))
        off = Scratchpad(np.int32)
        live = DispatchTime(np.int32)

    op = Copy(n=256)
    assert [v.name for v in op.values] == ["off", "live"]
    assert op.off.kind == "scratchpad" and op.live.kind == "dispatch"


def test_shim_pins_declare():
    class Pinned(Operator):
        n: int = param()
        c: int = auto(2)
        x = In(n, tile=(n,), via=Shim(col=1, channel=0))
        y = Out(n, tile=(n,), via=[Shim(col=c, channel=0) for c in range(2)], per=(c,))

    op = Pinned(n=2)
    pins = [op.x.lane().shim] + [op.y.lane(i).shim for i in range(2)]
    assert op.y.count == 2
    assert [p.col for p in pins if p is not None] == [1, 0, 1]


# --------------------------------------------------------------------------
# Inference
# --------------------------------------------------------------------------


def test_infer_reports_conflicts_naming_both_operands():
    with pytest.raises(
        ValueError, match=r"K is 128 from B.shape\[0\] but 256 from A.shape\[1\]"
    ):
        infer(MV, (1024, 256), (128,))
    with pytest.raises(ValueError, match="rank"):
        infer(MV, (1, 2, 3, 4), (256,))
    with pytest.raises(ValueError, match="K is 512 from A.shape"):
        infer(MV, (1024, 512), (512,), K=256)


def test_from_spec_builds_an_operator_from_literal_shapes():
    # swiglu_prefill_stream's escape: shapes from an exported graph, a
    # design that is not derived, an identity for sharing.
    Group = from_spec(
        "Group",
        inputs={"input": (64, 128), "w_gate": (128, 256)},
        outputs={"left": (64, 256)},
        key="abc123",
        params={"seq_len": 64, "k": 2},
        generator=lambda self, image="elf": "generator",
    )
    op = Group()
    assert [b.name for b in op.buffers] == ["input", "w_gate", "left"]
    assert [b.shape for b in op.buffers] == [(64, 128), (128, 256), (64, 256)]
    assert (op.seq_len, op.k) == (64, 2)
    assert op.design_key() == "abc123"
    assert op.generator() == "generator"
    # Literal shapes bind no field; inference only checks them.
    assert infer(Group, (64, 128), (128, 256)) == {}
    with pytest.raises(ValueError):
        infer(Group, (64, 128), (128, 512))


# --------------------------------------------------------------------------
# The array tier, resolution, identity
# --------------------------------------------------------------------------


def test_an_operand_with_a_tile_is_its_own_stream():
    op = MV(M=1024, K=128).resolved(FakeDev(cols=8))
    assert {k: (s.count, s.shape) for k, s in op.streams.items()} == {
        "A": (8, (64, 128)),
        "B": (1, (128,)),
        "C": (8, (64,)),
    }
    assert op.A.count == 8 and op.A.tile == np.ndarray[(64, 128), np.dtype[op.A.dtype]]
    assert op.A.shape == (1024, 128) and op.C.shape == (1024,)
    op.A.lane(3).bind("h3")
    assert op.A.lane(3).handle == "h3"
    op.B.bind("hb")
    assert op.B.handle == "hb"


def test_a_derived_value_is_written_once_per_build():
    op = MV(M=1024, K=128).resolved(FakeDev(cols=8))
    assert list(op.residents) == ["count"] and op.values == []
    assert op.resident_values() == {"count": 2}


def test_a_value_a_graph_binds_is_per_call_and_no_longer_a_resident():
    @iron.graph
    def g(a, b, *, pos: Scratchpad[np.int32], n: Scratchpad[np.int32]):
        # A per-call value at a call site is not a field a checker knows (yet).
        return MV(
            a, b, columns=8, start=pos, count=n
        )  # pyright: ignore[reportCallIssue]

    t = g.trace(a=(1024, 128), b=(128,))
    (op,) = t.operators
    assert op.uses_value("start") and op.uses_value("count")
    assert [v.name for v in op.values] == ["count", "start"] and op.residents == {}
    assert [b.member.name for b in t.bindings] == ["start", "count"]  # call order
    assert op.resident_values() == {}  # the preamble writes nothing for count
    # What an instance binds per call is part of its identity: an array
    # reading the value from the scratchpad is not the one reading a resident.
    assert op.design_key() != MV(M=1024, K=128, columns=8).design_key()


def test_identity_is_the_array_tier_for_sharing_and_every_field_for_a_build():
    a = MV(M=1024, K=128).resolved(FakeDev(cols=8))
    b = MV(M=2048, K=128).resolved(FakeDev(cols=8))
    assert a.array_key() == b.array_key()
    assert a.design_key() != b.design_key()
    assert a.array_key() == (
        "MV",
        ("K", 128),
        ("columns", 8),
        ("tile_out", 64),
        ("epilogue", "none"),
    )


def test_array_sees_the_array_tier_alone():
    class Leaky(MV):
        def array(self, target):
            return self.M

    op = MV(M=1024, K=128).resolved(FakeDev(cols=8))
    assert op.build_array(None) == [128, 8, 64, "none"]
    with pytest.raises(TypeError, match="reads M, which no tile names"):
        Leaky(M=1024, K=128).resolved(FakeDev(cols=8)).build_array(None)


def test_resolution_fills_every_knob_or_says_which_it_left():
    with pytest.raises(Unresolvable, match="no vector width"):
        MV(M=1024, K=24).resolved(FakeDev())
    with pytest.raises(Incompatible, match="not a multiple"):
        MV(M=1000, K=128).resolved(FakeDev(cols=8))
    ok = MV(M=1024, K=128, columns=2)
    assert not ok._resolved
    r = ok.resolved(FakeDev(cols=8))
    assert r._resolved and r.resolved(FakeDev()) is r and (r.columns, r.vec) == (2, 64)
    assert ok.columns == 2 and ok.vec is None  # the original is untouched


def test_a_profile_fills_the_knobs_a_call_leaves_open():
    p = Profile()
    p.add(MV, columns=4, tile_out=32)  # any MV: a declared default (64) counts as open
    p.add(MV, K=256, tile_out=16)  # more specific: its shape names K
    with p:
        assert (MV(M=1024, K=128).columns, MV(M=1024, K=128).tile_out) == (4, 32)
        assert MV(M=1024, K=256).tile_out == 16 and MV(M=1024, K=256).columns == 4
        assert MV(M=1024, K=256, tile_out=8).tile_out == 8  # what the call gives wins
        r = MV(M=1024, K=128).resolved(FakeDev(cols=8))
        assert (r.columns, r.tile_out, r.vec) == (4, 32, 64)  # resolve fills the rest
    assert MV(M=1024, K=128).columns is None and MV(M=1024, K=128).tile_out == 64
    assert p.lookup(MV(M=1024, K=256)) == {"columns": 4, "tile_out": 16}
    assert len(p) == 2


def test_a_profile_scope_is_per_thread():
    """One profile entered from several threads at once: each thread's scope
    is its own (the token lives in the context, not on the profile).
    """
    import threading

    p = Profile()
    p.add(MV, columns=2)
    seen, errors = [], []

    def work():
        try:
            for _ in range(50):
                with p:
                    seen.append(MV(M=64, K=64).columns)
                seen.append(MV(M=64, K=64).columns)
        except Exception as e:  # noqa: BLE001
            errors.append(e)

    threads = [threading.Thread(target=work) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert not errors and seen.count(2) == 200 and seen.count(None) == 200


def test_construction_is_by_keyword():
    with pytest.raises(TypeError, match="constructed by keyword"):
        MV(3, M=64, K=64)  # pyright: ignore[reportCallIssue]


def test_a_profile_is_checked_as_it_is_written_and_as_it_is_read():
    p = Profile()
    with pytest.raises(TypeError, match="declares no field"):
        p.add(MV, rows=4, columns=2)
    with pytest.raises(TypeError, match="must give a knob"):
        p.add(MV, M=1024)
    p.add(MV, M=1024, columns=2)
    p.add(MV, K=128, columns=8)  # as specific as the first: a clash for (1024, 128)
    with p:
        assert MV(M=512, K=128).columns == 8
        with pytest.raises(ValueError, match="ambiguous"):
            MV(M=1024, K=128)
        with Profile():  # an inner scope stands alone; the outer is back after
            assert MV(M=512, K=128).columns is None
        assert MV(M=512, K=128).columns == 8


def test_resolve_must_return_a_copy():
    class InPlace(MV):
        def resolve(self, dev):
            self.columns = 1
            return self

    op = InPlace(M=1024, K=128)
    with pytest.raises(TypeError, match="must return a copy"):
        op.resolved(FakeDev())
    assert not op._resolved


def test_overriding_an_inherited_field_needs_an_annotation():
    with pytest.raises(DeclarationError, match="tile_out: int = auto\\(32\\)"):

        class Pinned(MV):
            tile_out = 32  # dataclass would keep the base's 64 in silence

    class Annotated(MV):
        tile_out: int = auto(32)

    assert Annotated(M=64, K=64).tile_out == 32


def test_resolve_columns_is_the_count_given_or_the_most_that_fit():
    from aie.iron.device import from_name

    op = MV(M=96, K=64)
    dev = from_name("npu2", n_cols=8)  # the shim budget is the device's
    assert op.resolve_columns(dev, 2) == 2  # given, within the budget
    assert op.resolve_columns(dev, None) == 8  # the whole budget, nothing to fit
    assert op.resolve_columns(dev, None, fits=lambda c: 96 % (c * 32) == 0) == 3
    assert (
        op.resolve_columns(dev, None, fits=lambda c: False) == 1
    )  # compatible() will say why
    with pytest.raises(Unresolvable, match="none is bound and none was given"):
        op.resolve_columns(None, None)


def test_a_computed_default_is_inferred_from_a_shape_or_computed():
    class Rep(Operator):
        rows: int = param()
        repeat: int = param()
        out_rows: int = param(default=lambda op: op.rows * op.repeat)
        x = In(rows, 8)
        y = Out(out_rows, 8)

        def validate(self):
            self.check_derived("out_rows")  # a shape may bind it: it must agree

    assert Rep(rows=2, repeat=3).out_rows == 6  # computed
    assert Rep(rows=2, repeat=3, out_rows=6).out_rows == 6  # given, agrees
    with pytest.raises(ValueError, match="out_rows=5 is not what its other fields"):
        Rep(rows=2, repeat=3, out_rows=5)
    assert infer(Rep, (2, 8), outputs=[(6, 8)]) == {"rows": 2, "out_rows": 6}


def test_compatible_runs_at_construction_once_every_knob_is_known():
    with pytest.raises(Incompatible, match="not a multiple"):
        MV(M=1000, K=128, columns=8, tile_out=64, vec=64)  # nothing left to resolve
    MV(M=1000, K=128)  # a knob is open: compatible() waits for resolution


def test_inference_binds_the_fields_from_the_operands():
    op = MV.from_operands(
        (3, 1024, 128),
        (
            3,
            128,
        ),
    )
    assert (op.M, op.K, op.num_batches) == (1024, 128, 3)
    assert op.A.shape == (3, 1024, 128)
    assert MV.from_operands((1024, 128), (128,)).num_batches == 1


# --------------------------------------------------------------------------
# Two behaviours of declared shapes
# --------------------------------------------------------------------------


def test_gemm_layout_flags_transpose_rather_than_resize():
    from iron.operators.gemm.op import GEMM

    plain = GEMM(M=256, K=64, N=512).buffers
    b_major = GEMM(M=256, K=64, N=512, b_col_maj=True).buffers
    c_major = GEMM(M=256, K=64, N=512, c_col_maj=True).buffers
    assert plain[1].shape == (64, 512) and b_major[1].shape == (512, 64)
    assert plain[2].shape == (256, 512) and c_major[2].shape == (512, 256)
    # Transposing a layout must not change how many bytes move.
    assert plain[1].nbytes == b_major[1].nbytes
    assert plain[2].nbytes == c_major[2].nbytes


def test_mha_pads_the_sequence_and_groups_kv():
    from iron.operators.mha.op import MHA

    grouped = MHA(num_heads=8, seq_len=100, num_KV_heads=2).buffers
    plain = MHA(num_heads=8, seq_len=100).buffers
    # 100 rounds up to 128, so Q is 8 heads x 128 x 64.
    assert grouped[0].shape == (8, 128, 64)
    # Grouped K/V are narrower than Q; plain K/V are exactly as wide.
    assert grouped[1].shape == (2, 128, 64)
    assert plain[1].shape == plain[0].shape
    assert [spec.direction for spec in grouped] == ["in", "in", "in", "out"]


# --------------------------------------------------------------------------
# An extent a graph may bound per call
# --------------------------------------------------------------------------


class Rows(Operator):
    """Rows of ``cols`` elements over ``lanes`` lanes; ``rows`` may be bounded."""

    rows: int = param()
    cols: int = param()
    lanes: int = auto(2)
    valid = Extent(rows)
    count = Value(np.int32, derive=lambda op: op.valid // op.lanes)  # reads the extent
    width = Value(np.int32, derive=lambda op: op.cols)  # does not
    x = In(rows, cols, tile=(1, cols), per=(lanes,))
    y = Out(rows, cols, tile=(1, cols), per=(lanes,))

    def resolve(self, dev):
        return dataclasses.replace(self)

    def array(self, target):
        return []

    def reference(self, x):
        return x


def test_an_extent_reads_as_its_field_until_a_graph_bounds_it():
    op = Rows(rows=64, cols=8)
    assert op.valid == 64 and Rows.valid.field is Rows.rows
    assert not op.uses_value("valid") and not op.uses_value("count")
    assert op.resident_values() == {"count": 32, "width": 8}
    assert op.derived_at("count", valid=16) == 8 and op.valid == 64  # unchanged
    assert "valid: rows, unbounded" in op.explain()
    with pytest.raises(TypeError, match="no Extent \\['n'\\]"):
        op.derived_at("count", n=1)
    with pytest.raises(DeclarationError, match="must name a param"):

        class Bad(Operator):
            n: int = auto(4)
            valid = Extent(n)
            x = In(n)


def test_a_bounded_operand_binds_the_extent_and_what_derives_from_it(npu2):
    @iron.graph
    def g(x, *, n: Scratchpad[np.int32]):
        y = Rows(x[:n])  # bounds this instance
        return Rows(y)  # and, through its output, the next

    t = g.trace(x=(64, 8))
    a, b = t.operators
    for op in (a, b):
        assert op.bound_extents == {"valid": "n"}
        assert op.uses_value("valid") and op.uses_value("count")
        assert not op.uses_value("width")  # still written once per build
        assert set(op.residents) == {"width"}
        # The extent, what derives from it, and one word of tiles per lane
        # for each operand it sizes.
        assert [v.name for v in op.values] == ["valid", "count", "valid_x", "valid_y"]
        assert op.derived_at("valid_x", valid=16) == 8  # 16 rows over 2 lanes
    assert [(bd.member.name, bd.value.name) for bd in t.bindings] == [
        ("valid", "n"),
        ("valid", "n"),
    ]
    lines = a.explain().splitlines()
    assert "  valid: per call, bounds rows (graph value n)" in lines
    assert "  count: per call, derived from a bounded extent" in lines
    # Two instances alike in every field but one bounded are two designs.
    assert a.design_key() != Rows(rows=64, cols=8).design_key()
    assert a.design_key() == b.design_key()


def test_a_bound_is_refused_where_no_extent_takes_it():
    @iron.graph
    def g(x, *, n: Scratchpad[np.int32]):
        return MV(x[:n], x[0])  # M is not an Extent of MV

    with pytest.raises(TypeError, match="MV.A cannot be bounded per call on axis 0"):
        g.trace(x=(64, 128))

    @iron.graph
    def h(x, *, n: DispatchTime[np.int32]):
        return Rows(x[:n])

    with pytest.raises(ValueError, match="only a Scratchpad value can bound"):
        h.trace(x=(64, 8))

    @iron.graph
    def k(x, *, n: Scratchpad[np.int32]):
        return Rows(x[:, :n])  # cols is not an Extent

    with pytest.raises(TypeError, match="axis 1"):
        k.trace(x=(64, 8))
