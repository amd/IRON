# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The declaration layer, device-free.

Everything here runs without a device and without generating MLIR: it checks
what ``@operator`` records and rejects at class creation, how bound members
resolve on instances, how inference binds fields from operand shapes, and how
tuning and specialisation behave. The design-generating half is
``iron/common/build.py`` and needs the toolchain.
"""

import dataclasses

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common.declare import (
    DeclarationError,
    DimRef,
    DispatchTime,
    In,
    Incompatible,
    InOut,
    Operator,
    Out,
    Overlay,
    Resident,
    Scratchpad,
    Shim,
    StreamIn,
    StreamOut,
    Untunable,
    dim,
    operator,
    optional,
    tunable,
)


class FakeDev:
    def __init__(self, cols=8):
        self.cols = cols

    def columns(self):
        return self.cols


# --------------------------------------------------------------------------
# A worked pair, close to GEMV
# --------------------------------------------------------------------------


@operator
class MVOverlay(Overlay):
    K: int = dim()
    num_aie_columns: int = tunable(None)
    tile_size_output: int = tunable(64)
    vec: int = tunable(None, repr=False)

    a = StreamIn(tile_size_output, K, per=num_aie_columns)
    b = StreamIn(K, broadcast=True)
    c = StreamOut(tile_size_output, per=num_aie_columns)
    count = Resident(np.int32)

    def tuning(self, dev):
        cols = self.num_aie_columns or dev.columns()
        vec = self.vec or next(
            (w for w in (64, 32, 16) if self.K % w == 0 and self.K >= 2 * w), None
        )
        if vec is None:
            raise Untunable(f"K={self.K}: no vector width divides it")
        return dataclasses.replace(self, num_aie_columns=cols, vec=vec)


@operator
class MV(Operator[MVOverlay]):
    M: int = dim()
    num_batches: int = dim(1)

    A = In(optional(num_batches), M, MVOverlay.K, to=MVOverlay.a)
    B = In(optional(num_batches), MVOverlay.K, to=MVOverlay.b)
    C = Out(optional(num_batches), M, from_=MVOverlay.c)

    def compatible(self):
        unit = self.ov.num_aie_columns * self.ov.tile_size_output
        if self.M % unit:
            raise Incompatible(f"M={self.M} is not a multiple of {unit}")

    def reference(self, A, B):
        return A @ B


# --------------------------------------------------------------------------
# Class creation: names, order, re-attached fields
# --------------------------------------------------------------------------


def test_fields_are_reattached_as_dim_refs():
    assert isinstance(MVOverlay.K, DimRef)
    assert MVOverlay.K.name == "K" and MVOverlay.K.tier == "dim"
    assert MVOverlay.tile_size_output.tier == "tunable"
    assert isinstance(MV.M, DimRef) and MV.M.owner is MV


def test_members_keep_declaration_order_and_names():
    assert [m.name for m in MVOverlay._members] == ["a", "b", "c", "count"]
    assert [m.name for m in MV._members] == ["A", "B", "C"]
    assert MV.A.direction == "in" and MV.C.direction == "out"


def test_shapes_captured_bare_names_resolve_to_refs():
    # ``M`` and ``num_batches`` were Field objects in the class body; the
    # decorator rewrote them to DimRefs on the class.
    dims = MV.A.dims
    assert dims[0].ref.name == "num_batches"
    assert dims[1] == MV.M
    assert dims[2] is MVOverlay.K


def test_dataclass_constructor_is_typed_by_real_fields():
    params = list(dataclasses.fields(MV))
    assert [p.name for p in params] == ["ov", "M", "num_batches"]
    assert dataclasses.fields(MVOverlay)[0].name == "K"


# --------------------------------------------------------------------------
# Rules rejected at class creation
# --------------------------------------------------------------------------


def test_tunable_in_a_buffer_shape_is_rejected():
    with pytest.raises(DeclarationError, match="host shape may not depend on tuning"):

        @operator
        class Bad(Operator[MVOverlay]):
            M: int = dim()
            A = In(M, MVOverlay.tile_size_output, to=MVOverlay.a)


def test_tunable_in_a_stream_tile_is_allowed():
    assert MVOverlay.a.dims[0] is MVOverlay.tile_size_output


def test_plain_defaulted_field_in_a_shape_is_its_literal():
    # A plain field with a default is bound to that default in the class
    # body, so a shape written against it captures the literal, not the
    # field. This is why anything a shape names must be declared with dim().
    @operator
    class Plain(Overlay):
        n: int = 4
        s = StreamIn(n)

    assert Plain.s.dims == (4,)
    assert Plain(n=8).s.shape == (4,)


def test_plain_field_reference_from_outside_is_rejected():
    @operator
    class Plain(Overlay):
        n: int = 4
        s = StreamIn(4)

    with pytest.raises(DeclarationError, match="not declared with dim"):

        @operator
        class Bad(Operator[Plain]):
            M: int = dim()
            A = In(M, Plain.n, to=Plain.s)


def test_expression_in_a_shape_is_rejected():
    with pytest.raises(DeclarationError, match="Expressions are not allowed"):

        @operator
        class Bad(Overlay):
            n: int = dim()
            s = StreamIn("n // 2")


def test_annotated_member_is_rejected():
    with pytest.raises(DeclarationError, match="without an annotation"):

        @operator
        class Bad(Operator[MVOverlay]):
            M: int = dim()
            A: In = In(M, to=MVOverlay.a)


def test_buffers_on_an_overlay_are_rejected():
    with pytest.raises(
        DeclarationError, match="buffers and DispatchTime values belong"
    ):

        @operator
        class Bad(Overlay):
            n: int = dim()
            x = In(n)


def test_streams_on_an_operator_are_rejected():
    with pytest.raises(DeclarationError, match="streams and residents belong"):

        @operator
        class Bad(Operator[MVOverlay]):
            n: int = dim()
            s = StreamIn(n)


def test_stream_of_another_overlay_is_rejected():
    @operator
    class Other(Overlay):
        n: int = dim()
        s = StreamIn(n)

    with pytest.raises(DeclarationError, match="belongs to Other"):

        @operator
        class Bad(Operator[MVOverlay]):
            M: int = dim()
            A = In(M, to=Other.s)


def test_wrong_stream_direction_is_rejected():
    with pytest.raises(DeclarationError, match="to= must be a StreamIn"):

        @operator
        class Bad(Operator[MVOverlay]):
            M: int = dim()
            A = In(M, to=MVOverlay.c)


def test_float_scratchpad_is_rejected():
    with pytest.raises(DeclarationError, match="floating point"):
        Scratchpad(np.float32)


def test_per_and_broadcast_are_exclusive():
    with pytest.raises(DeclarationError, match="either per"):
        StreamIn(4, per=MVOverlay.num_aie_columns, broadcast=True)


# --------------------------------------------------------------------------
# Bound members on instances
# --------------------------------------------------------------------------


def test_overlay_streams_resolve_shape_count_and_tile():
    ov = MVOverlay(K=256, num_aie_columns=4)
    assert ov.a.shape == (64, 256) and ov.a.count == 4
    assert ov.b.shape == (256,) and ov.b.count == 1 and ov.b.broadcast
    assert ov.c.direction == "out"
    assert ov.a.tile == np.ndarray[(64, 256), np.dtype[bfloat16]]
    assert ov.a.elements == 64 * 256
    assert ov.count.dtype is np.int32


def test_operator_buffers_resolve_across_the_seam():
    ov = MVOverlay(K=256, num_aie_columns=4)
    op = MV(ov, M=1024)
    assert op.A.shape == (1024, 256)
    assert op.B.shape == (256,)
    assert op.C.shape == (1024,)
    assert op.A.stream(ov) is ov.a
    assert [b.name for b in op.inputs] == ["A", "B"]
    assert [b.name for b in op.outputs] == ["C"]


def test_optional_leading_dim_is_omitted_when_one():
    ov = MVOverlay(K=256)
    assert MV(ov, M=64).A.shape == (64, 256)
    assert MV(ov, M=64, num_batches=3).A.shape == (3, 64, 256)
    assert MV(ov, M=64, num_batches=3).C.shape == (3, 64)


def test_buffers_carry_direction_shape_and_dtype():
    ov = MVOverlay(K=256)
    specs = MV(ov, M=64, num_batches=2).buffers
    assert [(s.direction, s.shape) for s in specs] == [
        ("in", (2, 64, 256)),
        ("in", (2, 256)),
        ("out", (2, 64)),
    ]
    assert specs[0].dtype is bfloat16


def test_buffers_carry_the_declared_dtype_and_size():
    """The sizing contract: the sequence layout and the test harness allocate
    from ``b.dtype`` and ``b.nbytes`` of a declared buffer."""
    from iron.operators.repeat import Repeat

    x, y = Repeat(rows=8, cols=64, repeat=4, dtype=np.int32).buffers
    assert x.dtype == np.int32 and y.dtype == np.int32
    assert (x.direction, y.direction) == ("in", "out")
    assert y.nbytes == 8 * 64 * 4 * 4


def test_instance_values_shadow_dim_refs():
    ov = MVOverlay(K=256, num_aie_columns=2)
    assert ov.K == 256 and ov.num_aie_columns == 2
    assert MVOverlay.K.name == "K"


def test_stream_binding_slots():
    ov = MVOverlay(K=256, num_aie_columns=2)
    ov.a[0].bind("h0")
    ov.a[1].bind("h1")
    ov.b.bind("hb")
    assert ov.a.handles == ["h0", "h1"]
    assert ov.b.handle == "hb"
    with pytest.raises(ValueError, match="already bound"):
        ov.a[0].bind("again")
    with pytest.raises(ValueError, match="never bound"):
        ov.c.handles
    with pytest.raises(ValueError, match="index it"):
        ov.a.handle


def test_per_call_values_bind_on_the_operator():
    @operator
    class Copy(Operator[MVOverlay]):
        n: int = dim()
        src = In(n, to=MVOverlay.b)
        off = Scratchpad(np.int32)
        live = DispatchTime(np.int32)

    op = Copy(MVOverlay(K=256), n=256)
    assert [v.name for v in op.values] == ["off", "live"]
    assert op.off.kind == "scratchpad" and op.live.kind == "dispatch"


# --------------------------------------------------------------------------
# Tuning and specialisation
# --------------------------------------------------------------------------


def test_tuning_fills_tunables_from_the_device_only():
    ov = MVOverlay(K=256).tuned(FakeDev(cols=8))
    assert ov.num_aie_columns == 8 and ov.vec == 64
    assert ov.a.count == 8
    assert ov.tuned(FakeDev(cols=4)) is ov  # idempotent once tuned


def test_untunable_is_raised_not_defaulted():
    with pytest.raises(Untunable, match="K=24"):
        MVOverlay(K=24).tuned(FakeDev())


def test_tuning_that_leaves_a_tunable_unset_is_an_error():
    @operator
    class Lazy(Overlay):
        n: int = dim()
        t: int = tunable(None)
        s = StreamIn(n)

    with pytest.raises(Untunable, match=r"left \['t'\] unset"):
        Lazy(n=4).tuned(FakeDev())


def test_for_extent_is_a_distinct_specialised_overlay():
    base = MVOverlay(K=256).tuned(FakeDev())
    spec = base.for_extent(tile_size_output=32)
    assert spec.specialised and not base.specialised
    assert spec != base and hash(spec) != hash(base)
    assert MVOverlay(K=256).tuned(FakeDev()) == base  # equal by design_key
    with pytest.raises(TypeError, match="non-tunable"):
        base.for_extent(K=128)


def test_operator_tuned_runs_compatible():
    op = MV(MVOverlay(K=256, tile_size_output=64), M=1000)
    with pytest.raises(Incompatible, match="M=1000"):
        op.tuned(FakeDev(cols=8))
    ok = MV(MVOverlay(K=256, tile_size_output=64), M=1024).tuned(FakeDev(cols=8))
    assert ok.ov.num_aie_columns == 8


# --------------------------------------------------------------------------
# Inference
# --------------------------------------------------------------------------


def test_infer_binds_both_layers_from_operands():
    assert MV.infer((1024, 256), (256,)) == {"M": 1024, "K": 256, "num_batches": 1}
    assert MV.infer((3, 1024, 256), (3, 256)) == {"num_batches": 3, "M": 1024, "K": 256}


def test_infer_reports_conflicts_naming_both_operands():
    with pytest.raises(
        ValueError, match=r"K is 128 from B.shape\[0\] but 256 from A.shape\[1\]"
    ):
        MV.infer((1024, 256), (128,))
    with pytest.raises(ValueError, match="rank"):
        MV.infer((1, 2, 3, 4), (256,))
    with pytest.raises(ValueError, match="K is 512 from A.shape"):
        MV.infer((1024, 512), (512,), K=256)


def test_from_operands_constructs_overlay_and_operator():
    op = MV.from_operands((1024, 256), (256,), num_aie_columns=2)
    assert isinstance(op.ov, MVOverlay)
    assert (op.ov.K, op.ov.num_aie_columns, op.M, op.num_batches) == (256, 2, 1024, 1)


def test_classic_construction_splits_overlay_fields():
    op = MV(M=1024, K=256, num_aie_columns=2, tile_size_output=32)
    assert op.ov == MVOverlay(K=256, num_aie_columns=2, tile_size_output=32)
    assert op.M == 1024
    op2 = MV(op.ov, M=64)
    assert op2.ov is op.ov


def test_wrong_overlay_type_is_rejected():
    @operator
    class Other(Overlay):
        n: int = dim()
        s = StreamIn(n)

    with pytest.raises(TypeError, match="declared against MVOverlay"):
        MV(Other(n=4), M=64)


def test_inout_and_shim_pins_declare():
    @operator
    class Pinned(Overlay):
        n: int = dim()
        s = StreamIn(n, via=Shim(col=1, channel=0))
        d = StreamOut(n, via=[Shim(col=c, channel=0) for c in range(2)], per=n)

    @operator
    class Inplace(Operator[Pinned]):
        n: int = dim()
        x = InOut(n, to=Pinned.s, from_=Pinned.d)

    ov = Pinned(n=2)
    assert ov.s.via.col == 1 and len(ov.d.via) == 2 and ov.d.count == 2
    op = Inplace(ov, n=2)
    assert op.x.direction == "inout" and op.inputs == op.outputs


def test_from_spec_builds_an_operator_from_literal_shapes():
    # swiglu_prefill_stream's escape: shapes from an exported graph, a
    # design that is not derived, an identity for sharing.
    Group = Operator.from_spec(
        "Group",
        inputs={"input": (64, 128), "w_gate": (128, 256)},
        outputs={"left": (64, 256)},
        key="abc123",
        params={"seq_len": 64, "k": 2},
        generator=lambda self, image="elf": "generator",
    )
    op = Group(Group._overlay_class())
    assert [b.name for b in op.buffers] == ["input", "w_gate", "left"]
    assert [b.shape for b in op.buffers] == [(64, 128), (128, 256), (64, 256)]
    assert (op.seq_len, op.k) == (64, 2)
    assert op.design_key() == "abc123"
    assert op.generator() == "generator"
    # Literal shapes bind no field; inference only checks them.
    assert Group.infer((64, 128), (128, 256)) == {}
    with pytest.raises(ValueError):
        Group.infer((64, 128), (128, 512))


# --------------------------------------------------------------------------
# Two behaviours the old shape functions existed to express, now declared
# --------------------------------------------------------------------------


def test_gemm_layout_flags_transpose_rather_than_resize():
    from iron.operators.gemm.op import GEMM, GEMMOverlay

    plain = GEMM(GEMMOverlay(), M=256, K=64, N=512).buffers
    b_major = GEMM(GEMMOverlay(b_col_maj=True), M=256, K=64, N=512).buffers
    c_major = GEMM(GEMMOverlay(c_col_maj=True), M=256, K=64, N=512).buffers
    assert plain[1].shape == (64, 512) and b_major[1].shape == (512, 64)
    assert plain[2].shape == (256, 512) and c_major[2].shape == (512, 256)
    # Transposing a layout must not change how many bytes move.
    assert plain[1].nbytes == b_major[1].nbytes
    assert plain[2].nbytes == c_major[2].nbytes


def test_mha_pads_the_sequence_and_groups_kv():
    from iron.operators.mha.op import MHA, MHAOverlay

    grouped = MHA(MHAOverlay(), num_heads=8, seq_len=100, num_KV_heads=2).buffers
    plain = MHA(MHAOverlay(), num_heads=8, seq_len=100).buffers
    # 100 rounds up to 128, so Q is 8 heads x 128 x 64.
    assert grouped[0].shape == (8, 128, 64)
    # Grouped K/V are narrower than Q; plain K/V are exactly as wide.
    assert grouped[1].shape == (2, 128, 64)
    assert plain[1].shape == plain[0].shape
    assert [spec.direction for spec in grouped] == ["in", "in", "in", "out"]
