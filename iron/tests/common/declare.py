# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The declaration layer, device-free.

Everything here runs without a device and without generating MLIR: what
class creation records and rejects, how bound members resolve on instances,
how inference binds fields from operand shapes, and how resolution behaves.
The design-generating half is ``iron/common/design/`` and needs the
toolchain.
"""

import dataclasses
from types import SimpleNamespace

import aie.utils as aie_utils
from aie.iron import CompileTime, DispatchTime, In, Out, ScratchpadParameter
import numpy as np
import pytest
from aie.iron.device import from_name
from aie.utils import bfp
from aie.utils.trace import TraceConfig
from ml_dtypes import bfloat16

import iron
from iron import Profile, Scratchpad
from iron.common import (
    Auto,
    Built,
    Divisors,
    Extent,
    Operator,
    Rtp,
    Select,
    Unresolvable,
    Value,
    Width,
    field,
)
from iron.common.declare.field import AutoSpec, ParamSpec
from iron.common.declare.operand import active_runtime
from iron.common.declare.value import DispatchValue
from iron.common.design import OperatorDesign
from iron.operators import ReLU as LibraryReLU
from iron.operators import Tanh

NPU2 = from_name("npu2", n_cols=8)


def from_operands(cls, *operand_shapes, **overrides):
    """``cls`` constructed from operand shapes, an optional input's by keyword."""
    inputs, outputs, overrides = cls.declaration.call_operands(
        operand_shapes, overrides
    )
    return cls(**{**overrides, **cls.declaration.infer(inputs, outputs, **overrides)})


# --------------------------------------------------------------------------
# A worked operator, close to GEMV
# --------------------------------------------------------------------------


class MV(Operator):
    M: CompileTime[int] = field()
    K: CompileTime[int] = field()
    num_batches: CompileTime[int | None] = field(default=None)
    columns: CompileTime[int | None] = Auto()
    tile_out: CompileTime[int] = Auto(default=64)
    vec: CompileTime[int | None] = Auto(repr=False)
    epilogue: CompileTime[str] = field(default="none", array=True)

    A = In(num_batches, M, K, obj_shape=(tile_out, K), per=columns)
    B = In(num_batches, K, obj_shape=(K,))
    C = Out(num_batches, M, obj_shape=(tile_out,), per=columns)
    count = Value(derive=lambda op: op.M // (op.columns * op.tile_out))
    start = Value(derive=lambda op: 0)  # per call when a graph binds it

    def resolve(self, dev):
        cols = self.columns or dev.cols
        vec = self.vec or next((w for w in (64, 32, 16) if self.K % w == 0), None)
        if vec is None:
            raise Unresolvable(f"K={self.K}: no vector width divides it")
        return dataclasses.replace(self, columns=cols, vec=vec)

    def compatible(self):
        assert self.columns is not None
        unit = self.columns * self.tile_out
        if self.M % unit:
            raise ValueError(f"M={self.M} is not a multiple of {unit}")

    class Array(Operator.Array):
        def build(self) -> Built:
            return Built([self.K, self.columns, self.tile_out, self.epilogue])

    def reference(self, A, B):
        return A @ B


# --------------------------------------------------------------------------
# Class creation: names, order, re-attached fields
# --------------------------------------------------------------------------


def test_fields_are_their_own_references_and_instances_shadow_them():
    fields = {f.name: f for f in dataclasses.fields(MV)}
    assert MV.K is fields["K"] and MV.K.name == "K"
    assert type(ParamSpec.of(MV.K)) is ParamSpec
    assert MV.tile_out is fields["tile_out"]
    assert isinstance(ParamSpec.of(MV.tile_out), AutoSpec)
    op = MV(M=64, K=256, columns=2)
    assert op.K == 256 and op.columns == 2 and MV.K is fields["K"]


def test_a_declaration_prints_what_it_inferred():
    assert repr(MV.declaration) == "\n".join(
        [
            "MV",
            "  fields:   M, K, num_batches, epilogue",
            "  derived:  -",
            "  tunables: columns, tile_out, vec",
            "  resolved: -",
            "  In        A [num_batches, M, K] per [columns]",
            "  In        B [num_batches, K]",
            "  Out       C [num_batches, M] per [columns]",
            "  Value     count",
            "  Value     start",
            "  array:    (K, columns, tile_out, epilogue)",
        ]
    )


def test_every_catalog_operator_s_declaration_prints():
    import iron.operators as catalog
    import iron.operators.flm as flm

    for name in catalog._OPERATOR_MODULES:
        cls = (
            getattr(flm, name[4:])
            if name.startswith("flm.")
            else getattr(catalog, name)
        )
        assert repr(cls.declaration).startswith(cls.__name__)


def test_members_keep_declaration_order_and_names():
    assert [m.name for m in MV.declaration.members] == ["A", "B", "C", "count", "start"]
    assert MV.A.role is In and MV.C.role is Out


def test_shapes_captured_bare_names_resolve_to_refs():
    # ``M`` and ``num_batches`` were the fields themselves in the class body.
    dims = MV.A.dims.dims
    assert dims[0].name == "num_batches"
    assert dims[1] is MV.M and dims[2] is MV.K
    assert MV.A.obj_dims.dims == (MV.tile_out, MV.K)
    assert MV.A.per.dims == (MV.columns,)


def test_an_elementwise_operand_is_split_over_every_core_unless_it_says():
    from iron.operators import RMSNorm

    def per(operand):
        return [d.name for d in operand.per.dims]

    assert per(Tanh.x) == per(RMSNorm.x) == ["num_aie_columns", "num_channels"]
    assert per(RMSNorm.weight) == ["num_channels"]


# --------------------------------------------------------------------------
# Rules rejected at class creation
# --------------------------------------------------------------------------


def test_a_tunable_may_name_a_tile_but_not_a_buffer_shape():
    assert MV.A.obj_dims.dims[0] is MV.tile_out
    with pytest.raises(TypeError, match="host shape may not depend on tuning"):

        class Bad(Operator):
            M: CompileTime[int] = field()
            t: CompileTime[int] = Auto(default=64)
            A = In(M, t)


def test_a_field_without_a_marker_is_rejected():
    with pytest.raises(
        TypeError,
        match=r"Bad\.n: annotated <class 'int'>; a field is annotated "
        r"aie\.iron's CompileTime\[T\] or DispatchTime\[T\]",
    ):

        class Bad(Operator):
            n: int = field()


def test_a_marked_field_not_declared_with_field_is_rejected():
    # A plain default would be the literal a shape in the body captures.
    with pytest.raises(TypeError, match="Bad.n: declare a CompileTime field"):

        class Bad(Operator):
            n: CompileTime[int] = 4

    with pytest.raises(TypeError, match="Unset.n: declare a DispatchTime value"):

        class Unset(Operator):
            n: DispatchTime[np.int32]


def test_a_marker_inside_a_union_is_rejected():
    # CompileTime[int] | None would read as int and lose the None.
    with pytest.raises(TypeError, match=r"Bad\.n: .*CompileTime\[int \| None\]"):

        class Bad(Operator):
            n: CompileTime[int] | None = field(default=None)


@pytest.mark.parametrize(
    "options",
    [
        {},
        {"init": False, "default": 1},
        {"init": False, "array": True},
        {"init": False, "probe": 0},
    ],
)
def test_a_dispatch_value_takes_no_field_option(options):
    with pytest.raises(TypeError, match="Bad.n: declare a DispatchTime value"):

        class Bad(Operator):
            n: DispatchTime[np.int32] = field(**options)


def test_expression_in_a_shape_is_rejected():
    with pytest.raises(TypeError, match="Expressions are not allowed"):

        class Bad(Operator):
            n: CompileTime[int] = field()
            x = In("n // 2")


def test_annotated_member_is_rejected():
    with pytest.raises(TypeError, match="without an annotation"):

        class Bad(Operator):
            M: CompileTime[int] = field()
            A: In = In(M)


def test_a_member_hiding_the_operators_own_attribute_is_rejected():
    with pytest.raises(TypeError, match="hides Operator.values"):

        class Bad(Operator):
            n: CompileTime[int] = field()
            values = In(n)


def test_a_field_hiding_the_operators_own_attribute_is_rejected():
    with pytest.raises(TypeError, match="hides Operator.inputs"):

        class Bad(Operator):
            inputs: CompileTime[int] = field()

    with pytest.raises(TypeError, match="hides Operator.name"):

        class Worse(Operator):
            name: CompileTime[str] = field()


def test_a_field_may_replace_an_operator_bases_own_attribute():
    class Base(Operator):
        window = None

    class Windowed(Base):
        window: CompileTime[int] = field(default=512)

    assert Windowed().window == 512


def test_float_value_is_rejected():
    with pytest.raises(TypeError, match="floating point"):
        Value(dtype=np.float32)


def test_float_scratchpad_annotation_is_rejected():
    with pytest.raises(TypeError, match="floating point"):

        class Bad(iron.Graph):
            def body(self, x, *, scale: Scratchpad[np.float32]):
                return x


def test_a_probe_may_not_be_on_a_field_the_array_reads():
    with pytest.raises(TypeError, match="probe= on an array field"):

        class Baked(Operator):
            n: CompileTime[int] = field()
            alpha: CompileTime[float] = field(probe=1.0, array=True)
            x = In(n)

    with pytest.raises(TypeError, match="probe= on an array field"):

        class Tiled(Operator):
            n: CompileTime[int] = field()
            t: CompileTime[int] = field(probe=16)
            x = In(n, obj_shape=(t,))


def test_a_probe_may_not_be_on_a_field_the_transfers_follow():
    with pytest.raises(TypeError, match="probe= on a field an operand's shape"):

        class Shaped(Operator):
            n: CompileTime[int] = field(probe=1024)
            x = In(n)

    with pytest.raises(TypeError, match="probe= on a field an operand's shape"):

        class Present(Operator):
            n: CompileTime[int] = field()
            gated: CompileTime[bool] = field(default=False, probe=False)
            x = In(n)
            w = In(n, when=gated)


def test_a_probe_may_not_be_on_a_field_the_constructor_cannot_set():
    with pytest.raises(TypeError, match="probe= on an init=False field"):

        class Fixed(Operator):
            n: CompileTime[int] = field()
            low: CompileTime[float] = field(default=0.0, init=False, probe=0.0)
            x = In(n)


def test_probed_sets_each_probe_field_and_nothing_else():
    class Bounded(Operator):
        n: CompileTime[int] = field()
        low: CompileTime[float] = field(probe=-np.inf)
        cap: CompileTime[tuple | None] = field(default=None, probe=None)
        x = In(n)

    assert Bounded.declaration.probes == {"low": -np.inf, "cap": None}
    at = Bounded(n=64, low=-np.inf)
    assert at._probed() is at
    off = Bounded(n=64, low=0.5, cap=(0.0, 1.0))
    probe = off._probed()
    assert (probe.n, probe.low, probe.cap) == (64, -np.inf, None)
    assert (off.low, off.cap) == (0.5, (0.0, 1.0))
    assert probe.design_key() == at.design_key() != off.design_key()
    assert MV.declaration.probes == {}
    plain = MV(M=64, K=256)
    assert plain._probed() is plain


# --------------------------------------------------------------------------
# Bound members on instances
# --------------------------------------------------------------------------


def test_buffers_resolve_shape_dtype_and_direction(npu2):
    specs = MV(M=64, K=256, num_batches=2).buffers
    assert [(s.role, s.shape) for s in specs] == [
        (In, (2, 64, 256)),
        (In, (2, 256)),
        (Out, (2, 64)),
    ]
    assert specs[0].dtype is bfloat16
    op = MV(M=1024, K=256)
    assert [b.name for b in op.inputs] == ["A", "B"]
    assert [b.name for b in op.outputs] == ["C"]
    # The layout and the harness allocate from a buffer's dtype and nbytes.
    from iron.operators.copy import Copy

    x, y = Copy(input_buffer_size=512, dtype=np.int32).buffers
    assert x.dtype == y.dtype == np.int32 and y.nbytes == 512 * 4


def test_a_t_or_none_dim_is_omitted_when_none_and_may_sit_anywhere():
    assert MV(M=64, K=256).A.shape == (64, 256)
    assert MV(M=64, K=256, num_batches=3).C.shape == (3, 64)

    class Stack(Operator):
        rows: CompileTime[int] = field()
        cols: CompileTime[int] = field()
        seq: CompileTime[int | None] = field(default=None)
        x = In(rows, seq, cols)
        y = Out(rows, seq, cols)

    assert Stack.declaration.infer({"x": (8, 64)}) == {
        "rows": 8,
        "cols": 64,
        "seq": None,
    }
    assert Stack.declaration.infer({"x": (8, 16, 64)}) == {
        "rows": 8,
        "cols": 64,
        "seq": 16,
    }
    with pytest.raises(ValueError, match="rank 4"):
        Stack.declaration.infer({"x": (8, 2, 16, 64)})
    assert Stack(rows=8, cols=64).x.shape == (8, 64)
    assert Stack(rows=8, cols=64, seq=16).y.shape == (8, 16, 64)


def test_an_unresolved_tile_dimension_refuses_to_resolve():
    class Tiled(Operator):
        n: CompileTime[int] = field()
        t: CompileTime[int] = Auto()
        x = In(n, obj_shape=(t,))

    with pytest.raises(ValueError, match="t is None.*Resolve the operator first"):
        Tiled(n=64).x.obj_type


def test_a_block_float_tile_is_sized_by_its_blocks(npu2):
    class Blocks(Operator):
        n: CompileTime[int] = field()
        x = In(n, dtype=bfp.v8bfp16ebs8, obj_shape=(4096,))

    # 4096 blocks of 9 bytes: past half a core memory bank, so one deep.
    assert Blocks(n=4096).x.l1_depth == 1


def test_a_stream_binds_a_handle_per_lane():
    op = MV(M=1024, K=256, columns=2)
    op.A.bind(["h0", "h1"])
    op.B.bind("hb")
    assert op.A.handles == ["h0", "h1"]
    assert op.B.handles == ["hb"]
    with pytest.raises(ValueError, match="already bound"):
        op.A.bind(["again", "again"])
    with pytest.raises(ValueError, match="never bound"):
        op.C.handles
    with pytest.raises(ValueError, match="has 2 lanes"):
        MV(M=1024, K=256, columns=2).A.bind("h")

    class NoObjType(Operator):
        n: CompileTime[int] = field()
        x = In(n)

    with pytest.raises(TypeError, match="without an obj_shape"):
        NoObjType(n=4).x.obj_type


def test_an_operand_fills_only_inside_its_operators_sequence():
    op = MV(M=1024, K=256, columns=2)
    with pytest.raises(ValueError, match="run in the operator's sequence"):
        op.A.fill(lane=0)
    # Nor inside another operator's.
    token = active_runtime.set(SimpleNamespace(op=MV(M=1024, K=256, columns=2)))
    try:
        with pytest.raises(ValueError, match="run in the operator's sequence"):
            op.A.fill(lane=0)
    finally:
        active_runtime.reset(token)


def test_per_call_values_bind_on_the_operator():
    class Copy(Operator):
        n: CompileTime[int] = field()
        src = In(n, obj_shape=(n,))
        off = Value()
        live: DispatchTime[np.int32] = field(init=False)

    op = Copy(n=256)
    assert [v.name for v in op.values] == ["off", "live"]
    assert type(op.off) is Value and op.off.op is op
    assert isinstance(op.live, DispatchValue) and op.live is not Copy.live


# --------------------------------------------------------------------------
# Inference
# --------------------------------------------------------------------------


def test_infer_reports_conflicts_naming_both_operands():
    with pytest.raises(
        ValueError, match=r"K is 128 from B.shape\[0\] but 256 from A.shape\[1\]"
    ):
        MV.declaration.infer({"A": (1024, 256), "B": (128,)})
    with pytest.raises(ValueError, match="rank"):
        MV.declaration.infer({"A": (1, 2, 3, 4), "B": (256,)})
    with pytest.raises(ValueError, match="K is 512 from A.shape"):
        MV.declaration.infer({"A": (1024, 512), "B": (512,)}, K=256)


def test_an_exported_design_replaces_the_derived_one():
    # The design is another tool's text; the operands are declared as any
    # operator's are.
    class Exported(Operator):
        n: CompileTime[int] = field()
        x = In(n)
        y = Out(n)

        def exported_design(self):
            return lambda: "module {}"

    op = Exported(n=64)
    assert [b.shape for b in op.buffers] == [(64,), (64,)]
    assert OperatorDesign(op).build() == "module {}"
    assert op.xclbin_operator() is op


# --------------------------------------------------------------------------
# The array tier, resolution, identity
# --------------------------------------------------------------------------


def test_an_operand_with_a_tile_is_its_own_stream():
    op = MV(M=1024, K=128).resolved(NPU2)
    assert {b.name: (b.lanes, b.obj_shape) for b in op.buffers} == {
        "A": (8, (64, 128)),
        "B": (1, (128,)),
        "C": (8, (64,)),
    }
    assert (
        op.A.lanes == 8 and op.A.obj_type == np.ndarray[(64, 128), np.dtype[op.A.dtype]]
    )
    assert op.A.shape == (1024, 128) and op.C.shape == (1024,)


class Scaled(Operator):
    """``x`` times a scale row when ``scaled``, else a copy of it."""

    N: CompileTime[int] = field()
    scaled: CompileTime[bool] = field(default=False)

    x = In(N, obj_shape=(N,))
    s = In(N, obj_shape=(N,), when=scaled)
    y = Out(N, obj_shape=(N,))

    class Array(Operator.Array):
        def build(self) -> Built:
            return Built([self.scaled])


def test_an_operand_declared_when_a_flag_exists_only_where_it_is_true():
    plain, scaled = Scaled(N=64), Scaled(N=64, scaled=True)
    assert [b.name for b in plain.buffers if b.streamed] == ["x", "y"]
    assert [b.name for b in scaled.buffers if b.streamed] == ["x", "s", "y"]
    assert scaled.s.shape == (64,)
    with pytest.raises(AttributeError, match="declared when=scaled"):
        plain.s
    # The flag decides the streams, so it is of the array tier.
    assert "scaled" in Scaled.declaration.array
    assert plain.array_key() != scaled.array_key()
    # A call gives the optional input by keyword, which sets its flag.
    assert not from_operands(Scaled, (64,)).scaled
    assert from_operands(Scaled, (64,), s=(64,)).scaled
    assert from_operands(Scaled, (64,), s=(64,), scaled=True).scaled
    with pytest.raises(TypeError, match="only where scaled is true"):
        from_operands(Scaled, (64,), s=(64,), scaled=False)
    with pytest.raises(TypeError, match=r"Scaled\(scaled=True\) takes s="):
        from_operands(Scaled, (64,), scaled=True)


def test_a_positional_operand_past_the_inputs_is_an_output_not_an_optional_one():
    class G(iron.Graph):
        def __init__(self):
            self.y = iron.state((64,))

        def body(self, x):
            Scaled.step(x, self.y)  # y is written: an output, never the scale

    (step,) = G().trace(x=(64,)).steps
    assert not step.op.scaled
    assert [b.name for b in step.op.buffers] == ["x", "y"]

    class H(G):
        def body(self, x, s):
            Scaled.step(x, self.y, s=s)

    (step,) = H().trace(x=(64,), s=(64,)).steps
    assert step.op.scaled
    assert [b.name for b in step.op.buffers] == ["x", "s", "y"]


def test_when_names_a_param():
    with pytest.raises(TypeError, match=r"must be a field\(\)"):

        class Bad(Operator):
            N: CompileTime[int] = field()
            flag: CompileTime[bool] = Auto(default=False)
            s = In(N, when=flag)


def test_a_derived_value_is_written_once_per_build():
    op = MV(M=1024, K=128).resolved(NPU2)
    assert op.residents == {"count": 2, "start": 0} and op.values == []


def test_a_value_a_graph_binds_is_per_call_and_no_longer_a_resident():
    class G(iron.Graph):
        def body(self, a, b, *, pos: Scratchpad[np.int32], n: Scratchpad[np.int32]):
            return MV.step(a, b, columns=8, start=pos, count=n)

    g = G()

    t = g.trace(a=(1024, 128), b=(128,))
    (op,) = t.operators
    assert op.value("start").per_call and op.value("count").per_call
    assert [v.name for v in op.values] == ["count", "start"]
    assert [b.member.name for b in t.bindings] == ["start", "count"]  # call order
    assert op.residents == {}  # the preamble writes nothing for count
    # What an instance binds per call is part of its identity: an array
    # reading the value from the scratchpad is not the one reading a resident.
    assert op.design_key() != MV(M=1024, K=128, columns=8).design_key()


def test_identity_is_the_array_tier_for_sharing_and_every_field_for_a_build():
    a = MV(M=1024, K=128).resolved(NPU2)
    b = MV(M=2048, K=128).resolved(NPU2)
    assert a.array_key() == b.array_key()
    assert a.design_key() != b.design_key()
    assert a.array_key() == (
        MV,
        ("K", 128),
        ("columns", 8),
        ("tile_out", 64),
        ("epilogue", "none"),
    )


class ReLU(Tanh):
    """A ReLU of this module's own, which runs tanh."""


def test_two_operators_of_one_name_are_two_designs():
    given = dict(size=4096, num_aie_columns=1, num_channels=1, tile_size=1024)
    ours, theirs = ReLU(**given), LibraryReLU(**given)
    assert ours.array_key() != theirs.array_key()
    assert ours.design_key() != theirs.design_key()


def test_a_traced_operator_is_not_the_untraced_ones_array():
    given = dict(size=4096, num_aie_columns=1, num_channels=1, tile_size=1024)
    traced = Tanh(**given, trace=TraceConfig(trace_size=8192))
    assert traced.array_key() != Tanh(**given).array_key()


def test_array_sees_the_array_tier_alone():
    class Leaky(MV):
        class Array(MV.Array):
            def build(self) -> Built:
                return Built([self.M // self.tile_out])

    op = MV(M=1024, K=128).resolved(NPU2)
    assert MV.declaration.array == ("K", "columns", "tile_out", "epilogue")
    assert op.array_config().build() == Built([128, 8, 64, "none"])
    with pytest.raises(AttributeError, match="'M'"):
        Leaky(M=1024, K=128).resolved(NPU2).array_config().build()


def test_an_array_reads_what_names_its_streams_and_nothing_else():
    # Generated: the fields a stream names, those declared array=True, and
    # every member, with no annotation of its own.
    fields = [f.name for f in dataclasses.fields(MV.Array)]
    assert fields == [
        "K",
        "columns",
        "tile_out",
        "epilogue",
        "A",
        "B",
        "C",
        "count",
        "start",
    ]

    # By hand it annotates only the library's views: a field, a member or
    # anything else is refused.
    for name in ("K", "A", "work"):
        with pytest.raises(TypeError, match=rf"annotates \['{name}'\], but"):
            type(
                "Listed",
                (MV,),
                {"Array": type("Array", (MV.Array,), {"__annotations__": {name: int}})},
            )


def test_resolution_fills_every_tunable_or_says_which_it_left():
    with pytest.raises(Unresolvable, match="no vector width"):
        MV(M=1024, K=24).resolved(NPU2)
    with pytest.raises(ValueError, match="not a multiple"):
        MV(M=1000, K=128).resolved(NPU2)
    ok = MV(M=1024, K=128, columns=2)
    assert not ok._resolved
    r = ok.resolved(NPU2)
    assert r._resolved and r.resolved(NPU2) is r and (r.columns, r.vec) == (2, 64)
    assert ok.columns == 2 and ok.vec is None  # the original is untouched


def test_resolving_for_a_device_binds_it_while_it_resolves():
    seen = []

    class Reads(MV):
        def resolve(self, dev):
            seen.append(self.dev)
            return super().resolve(dev)

    with aie_utils.set_current_device(None):
        Reads(M=1024, K=128).resolved(NPU2)
        assert (
            seen == [NPU2] and aie_utils.get_current_device(probe_runtime=False) is None
        )


def test_a_field_resolve_computes_is_kept_by_copies_and_checked_once_known():
    class Derived(MV):
        half: CompileTime[int] = Auto(init=False)

        def resolve(self, dev):
            new = super().resolve(dev)
            return new.replace(half=new.tile_out // 2)

        def compatible(self):
            super().compatible()
            if self.half is not None and self.half > 16:
                raise ValueError(f"half={self.half} is past 16")

    assert "half" not in Derived.declaration.tunables
    r = Derived(M=1024, K=128, tile_out=32).resolved(NPU2)
    assert r.half == 16 and r.copy().half == 16
    with pytest.raises(ValueError, match="half=32 is past 16"):
        Derived(M=1024, K=128).resolved(NPU2)


def test_a_profile_fills_the_tunables_a_call_leaves_open():
    p = Profile()
    p.add(MV, columns=4, tile_out=32)  # any MV: a declared default (64) counts as open
    p.add(MV, K=256, tile_out=16)  # more specific: its shape names K
    assert (p.make(MV, M=1024, K=128).columns, p.make(MV, M=1024, K=128).tile_out) == (
        4,
        32,
    )
    assert (
        p.make(MV, M=1024, K=256).tile_out == 16
        and p.make(MV, M=1024, K=256).columns == 4
    )
    # what the call gives wins
    assert p.make(MV, M=1024, K=256, tile_out=8).tile_out == 8
    r = p.make(MV, M=1024, K=128).resolved(NPU2)
    assert (r.columns, r.tile_out, r.vec) == (4, 32, 64)  # resolve fills the rest
    # plain construction reads no profile
    assert MV(M=1024, K=128).columns is None and MV(M=1024, K=128).tile_out == 64
    assert p.tunables_for(MV, dict(M=1024, K=256)) == {"columns": 4, "tile_out": 16}
    assert len(p) == 2


def test_a_profile_reads_as_its_operators():
    p = Profile()
    p.add(MV, columns=4)
    p.add(MV, K=256, tile_out=16)
    assert repr(p) == "Profile(MV)"


def test_a_profile_is_checked_as_it_is_written_and_as_it_is_read():
    p = Profile()
    with pytest.raises(TypeError, match="declares no field"):
        p.add(MV, rows=4, columns=2)
    with pytest.raises(TypeError, match="must give a tunable"):
        p.add(MV, M=1024)
    p.add(MV, M=1024, columns=2)
    p.add(MV, K=128, columns=8)  # as specific as the first: a clash for (1024, 128)
    assert p.make(MV, M=512, K=128).columns == 8
    with pytest.raises(ValueError, match="ambiguous"):
        p.make(MV, M=1024, K=128)


def test_resolve_must_return_a_copy():
    class InPlace(MV):
        def resolve(self, dev):
            self.columns = 1
            return self

    op = InPlace(M=1024, K=128)
    with pytest.raises(TypeError, match="must return a copy"):
        op.resolved(NPU2)
    assert not op._resolved


def test_overriding_an_inherited_field_needs_an_annotation():
    with pytest.raises(
        TypeError, match=r"tile_out: CompileTime\[int\] = Auto\(default=32\)"
    ):

        class Pinned(MV):
            tile_out = 32  # dataclass would keep the base's 64 in silence

    class Annotated(MV):
        tile_out: CompileTime[int] = Auto(default=32)

    assert Annotated(M=64, K=64).tile_out == 32


def test_resolve_columns_is_the_count_given_or_the_most_that_fit():
    op = MV(M=96, K=64)
    dev = NPU2  # the shim budget is the device's
    assert op.resolve_columns(dev, 2) == 2  # given, within the budget
    assert op.resolve_columns(dev, None) == 8  # the whole budget, nothing to fit
    assert op.resolve_columns(dev, None, fits=lambda c: 96 % (c * 32) == 0) == 3
    assert (
        op.resolve_columns(dev, None, fits=lambda c: False) == 1
    )  # compatible() will say why
    with pytest.raises(Unresolvable, match="none is bound and none was given"):
        op.resolve_columns(None, None)


def test_a_stream_with_no_lanes_is_paid_once_in_the_shim_budget():
    class Scaled(MV):
        scale = In(MV.M, obj_shape=(MV.tile_out,), per=MV.columns)

    # 16 input channels: A's and scale's lanes per column (or A's two
    # channels a column), B once.
    assert MV.declaration.shim_columns(NPU2) == 8
    assert NPU2.shim_dma_channels_in == 16
    assert Scaled.declaration.shim_columns(NPU2) == (16 - 1) // 2
    assert MV.declaration.shim_columns(NPU2, num_channels=2) == (16 - 1) // 2


def test_a_computed_default_is_inferred_from_a_shape_or_computed():
    class Rep(Operator):
        rows: CompileTime[int] = field()
        repeat: CompileTime[int] = field()
        out_rows: CompileTime[int] = field(derive=lambda op: op.rows * op.repeat)
        cap: CompileTime[int] = field(derive=lambda op: op.out_rows, held=False)
        x = In(rows, 8)
        y = Out(out_rows, 8)

    assert Rep(rows=2, repeat=3).out_rows == 6  # computed
    assert Rep(rows=2, repeat=3, out_rows=6).out_rows == 6  # given, agrees
    with pytest.raises(ValueError, match=r"out_rows \(5\) must be 6"):
        Rep(rows=2, repeat=3, out_rows=5)  # a derived field is held to its formula
    assert Rep.declaration.infer({"x": (2, 8)}, [(6, 8)]) == {"rows": 2, "out_rows": 6}
    # held=False: computed after the fields before it, or given and kept.
    assert Rep(rows=2, repeat=3).cap == 6
    assert Rep(rows=2, repeat=3, cap=8).cap == 8
    # replace computes a held field again from the fields it changes.
    assert Rep(rows=2, repeat=3).replace(repeat=4).out_rows == 8
    assert Rep(rows=2, repeat=3, cap=8).replace(repeat=4).cap == 8


def test_a_computed_default_of_none_must_be_given():
    class Unknown(Operator):
        n: CompileTime[int] = field(derive=lambda op: None, held=False)

    with pytest.raises(ValueError, match=r"n \(None\) must be given"):
        Unknown()
    assert Unknown(n=2).n == 2


def test_a_field_gives_a_default_or_a_derive_not_both_and_holds_only_a_derive():
    with pytest.raises(TypeError, match="give one, not both"):
        field(default=1, derive=lambda op: 1)
    with pytest.raises(TypeError, match=r"only a derive= field is held"):
        field(held=False)


def test_a_select_picks_a_layout_within_a_storage():
    class Weights(Operator):
        K: CompileTime[int] = field()
        N: CompileTime[int] = field()
        blocks: CompileTime[int] = field(default=0)
        packed: CompileTime[bool] = field(default=False)
        transposed: CompileTime[bool] = field(default=False)
        w = In(Select(packed, (blocks,), (Select(transposed, (N, K), (K, N)),)))

    assert Weights.declaration.infer({"w": (64, 32)}, transposed=True) == {
        "transposed": True,
        "N": 64,
        "K": 32,
    }
    assert Weights.declaration.infer({"w": (64, 32)}) == {"K": 64, "N": 32}
    assert Weights(K=32, N=64, transposed=True).buffers[0].shape == (64, 32)
    assert Weights(K=32, N=64, blocks=8, packed=True).buffers[0].shape == (8,)


def test_compatible_runs_at_construction_once_every_tunable_is_known():
    with pytest.raises(ValueError, match="not a multiple"):
        MV(M=1000, K=128, columns=8, tile_out=64, vec=64)  # nothing left to resolve
    MV(M=1000, K=128)  # a tunable is open: compatible() waits for resolution


def test_inference_binds_the_fields_from_the_operands():
    op = from_operands(
        MV,
        (3, 1024, 128),
        (
            3,
            128,
        ),
    )
    assert (op.M, op.K, op.num_batches) == (1024, 128, 3)
    assert op.A.shape == (3, 1024, 128)
    assert from_operands(MV, (1024, 128), (128,)).num_batches is None


# --------------------------------------------------------------------------
# Two behaviours of declared shapes
# --------------------------------------------------------------------------


def test_gemm_layout_flags_transpose_rather_than_resize():
    from iron.operators.gemm import GEMM

    plain = GEMM(M=256, K=64, N=512).buffers
    b_major = GEMM(M=256, K=64, N=512, b_col_maj=True).buffers
    c_major = GEMM(M=256, K=64, N=512, c_col_maj=True).buffers
    assert plain[1].shape == (64, 512) and b_major[1].shape == (512, 64)
    assert plain[2].shape == (256, 512) and c_major[2].shape == (512, 256)
    # Transposing a layout must not change how many bytes move.
    assert plain[1].nbytes == b_major[1].nbytes
    assert plain[2].nbytes == c_major[2].nbytes


def test_mha_pads_the_sequence_and_groups_kv():
    from iron.operators.mha import MHA

    grouped = MHA(num_heads=8, seq_len=100, num_KV_heads=2).buffers
    plain = MHA(num_heads=8, seq_len=100).buffers
    # 100 rounds up to 128, so Q is 8 heads x 128 x 64.
    assert grouped[0].shape == (8, 128, 64)
    # Grouped K/V are narrower than Q; plain K/V are exactly as wide.
    assert grouped[1].shape == (2, 128, 64)
    assert plain[1].shape == plain[0].shape
    assert [spec.role for spec in grouped] == [In] * 3 + [Out]
    inputs, _, _ = MHA.declaration.call_operands(
        ((8, 128, 64), (2, 128, 64), (2, 128, 64)), {}
    )
    op = MHA(**MHA.declaration.infer(inputs))
    assert (op.num_heads, op.num_KV_heads, op.seq_len, op.seq_pad) == (8, 2, 128, 128)
    with pytest.raises(ValueError, match=r"seq_pad \(100\)"):
        MHA(num_heads=1, seq_len=100, seq_pad=100, d=64)


# --------------------------------------------------------------------------
# An extent a graph may bound per call
# --------------------------------------------------------------------------


class Rows(Operator):
    """Rows of ``cols`` elements over ``lanes`` lanes; ``rows`` may be bounded."""

    rows: CompileTime[int] = field()
    cols: CompileTime[int] = field()
    lanes: CompileTime[int] = Auto(default=2)
    valid = Extent(rows)
    count = Value(derive=lambda op: op.valid // op.lanes)  # reads the extent
    width = Value(derive=lambda op: op.cols)  # does not
    x = In(rows, cols, obj_shape=(1, cols), per=(lanes,))
    y = Out(rows, cols, obj_shape=(1, cols), per=(lanes,))

    def resolve(self, dev):
        return dataclasses.replace(self)

    class Array(Operator.Array):
        def build(self) -> Built:
            return Built([])

    def reference(self, x):
        return x


def test_an_extent_reads_as_its_field_until_a_graph_bounds_it():
    op = Rows(rows=64, cols=8)
    assert op.valid == 64 and Rows.valid.field is Rows.rows
    assert not op.value("valid").per_call and not op.value("count").per_call
    assert op.residents == {"count": 32, "width": 8}
    assert op.derived_at("count", valid=16) == 8 and op.valid == 64  # unchanged
    with pytest.raises(TypeError, match="no Extent \\['n'\\]"):
        op.derived_at("count", n=1)
    with pytest.raises(TypeError, match=r"must name a field\(\)"):

        class Bad(Operator):
            n: CompileTime[int] = Auto(default=4)
            valid = Extent(n)
            x = In(n)


def test_a_bounded_operand_binds_the_extent_and_what_derives_from_it(npu2):
    class G(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            y = Rows.step(x[:n])  # bounds this instance
            return Rows.step(y)  # and, through its output, the next

    g = G()

    t = g.trace(x=(64, 8))
    a, b = t.operators
    for op in (a, b):
        assert {k: e.name for k, e in op.bound_extents.items()} == {"valid": "n"}
        assert op.value("valid").per_call and op.value("count").per_call
        assert not op.value("width").per_call  # still written once per build
        assert set(op.residents) == {"width"}
        # The extent, what derives from it, and one word of tiles per lane
        # for each operand it sizes.
        assert [v.name for v in op.values] == ["valid", "count", "valid_x", "valid_y"]
        assert op.derived_at("valid_x", valid=16) == 8  # 16 rows over 2 lanes
    assert [(bd.member.name, bd.expression.name) for bd in t.bindings] == [
        ("valid", "n"),
        ("valid", "n"),
    ]
    # Two instances alike in every field but one bounded are two designs.
    assert a.design_key() != Rows(rows=64, cols=8).design_key()
    assert a.design_key() == b.design_key()


def test_what_a_bound_makes_per_call_is_worked_out_once_per_binding():
    calls = []

    class Counted(Rows):
        count = Value(derive=lambda op: calls.append(1) or op.valid // op.lanes)

    op = Counted(rows=64, cols=8)
    op.use_value("valid")
    assert op.value("count").per_call
    once = len(calls)
    op.values, op.values
    assert len(calls) == once
    op.use_value("count")  # a new binding asks again
    op.values
    assert len(calls) > once


def test_a_derive_that_fails_for_another_reason_than_resolution_raises():
    class Buggy(Rows):
        count = Value(derive=lambda op: op.valid and {}["typo"])

    op = Buggy(rows=64, cols=8)
    op.use_value("valid")
    with pytest.raises(KeyError, match="typo"):
        op.values


def test_a_bound_is_refused_where_no_extent_takes_it():
    class G(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return MV.step(x[:n], x[0])  # M is not an Extent of MV

    g = G()

    with pytest.raises(TypeError, match="MV.A cannot be bounded per call on axis 0"):
        g.trace(x=(64, 128))

    class H(iron.Graph):
        def body(self, x, *, n: DispatchTime[np.int32]):
            return Rows.step(x[:n])

    h = H()

    with pytest.raises(ValueError, match="only a Scratchpad value can bound"):
        h.trace(x=(64, 8))

    class K(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return Rows.step(x[:, :n])  # cols is not an Extent

    k = K()

    with pytest.raises(TypeError, match="axis 1"):
        k.trace(x=(64, 8))


# --------------------------------------------------------------------------
# Tuning domains, runtime parameters and shapes through a Select
# --------------------------------------------------------------------------


def test_a_width_is_the_value_and_every_power_of_two_up_to_the_columns():
    assert Width().values(None, NPU2, 3) == (8, 4, 3, 2, 1)
    assert Width().values(None, NPU2, 8) == (8, 4, 2, 1)


@pytest.mark.parametrize(
    "domain,expected",
    [
        (Divisors(of=64), (64, 32, 16, 8, 4, 2, 1)),
        (Divisors(of=64, cap=16), (16, 8, 4, 2, 1)),  # the cap bounds above
        (Divisors(of=64, step=4), (64, 32, 16, 8, 4)),  # the step bounds below
        (Divisors(of=64, span=1), (16, 8, 4)),  # one octave either side
        (Divisors(of=24), (8, 4, 2, 1)),  # 16 does not divide 24
        (Divisors(of=lambda op, dev: dev.cols * 4), (32, 16, 8, 4, 2, 1)),
    ],
    ids=["plain", "cap", "step", "span", "not_dividing", "callable"],
)
def test_divisors_are_the_value_times_powers_of_two_within_the_bounds(domain, expected):
    assert domain.values(None, NPU2, 8) == expected


def test_divisors_read_a_field_off_the_operator():
    op = MV(M=1024, K=256)
    assert Divisors(of=MV.K, cap=64).values(op, NPU2, 32) == (64, 32, 16, 8, 4, 2, 1)


def _value(name, **kw):
    value = Value(**kw)
    value.name = name
    return value


def test_runtime_parameters_lay_out_the_buffer_words_and_skip_scratchpad_ones():
    one, block, scratch = _value("one"), _value("block", words=3), _value("s")
    scratch.param = ScratchpadParameter("s", np.int32)
    rtp = Rtp([block, one, scratch])
    assert rtp.slots == {block: 0, one: 3}
    assert rtp.buffer is not None and rtp[-1] is scratch.param
    with pytest.raises(ValueError, match="block holds 3 words; it was given 2"):
        rtp.write({"block": [1, 2], "one": 1})


def test_a_scratchpad_parameter_holds_one_word():
    block = _value("block", words=2)
    block.param = ScratchpadParameter("block", np.int32)
    with pytest.raises(ValueError, match="block is 2 words"):
        Rtp([block])


def test_an_axis_is_found_through_the_branch_a_select_takes():
    class Laid(Operator):
        rows: CompileTime[int] = field()
        cols: CompileTime[int] = field()
        flip: CompileTime[bool] = field(default=False)
        x = In(Select(flip, (cols, rows), (rows, cols)))

    assert Laid.x.dims.axis_of("rows", Laid(rows=4, cols=8)) == 0
    assert Laid.x.dims.axis_of("rows", Laid(rows=4, cols=8, flip=True)) == 1
    assert Laid(rows=4, cols=8, flip=True).x.shape == (8, 4)


class Doubled(Operator):
    """Doubles its input, with a reference and no kernel."""

    reference_only = True
    rows: CompileTime[int] = field()
    x = In(rows, 8)
    y = Out(rows, 8)

    def reference(self, x):
        return x * 2


def test_a_reference_only_operator_runs_its_reference_and_does_not_compile(npu2):
    class Twice(iron.Graph):
        def body(self, x):
            return Doubled.step(x)

    x = np.arange(32).reshape(4, 8).astype(bfloat16)
    np.testing.assert_array_equal(np.asarray(Twice().reference(x)), x * 2)
    with pytest.raises(TypeError, match="Doubled is reference-only: it has no kernel"):
        Doubled(rows=4).compile()


def test_a_reference_only_operator_takes_no_build():
    with pytest.raises(TypeError, match="Builds is reference-only, so it takes no"):

        class Builds(Doubled):
            class Array(Operator.Array):
                def build(self) -> Built:
                    return Built([])
