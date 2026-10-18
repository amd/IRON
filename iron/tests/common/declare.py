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

import aie.iron
import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.device import from_name
from aie.utils import bfp
from aie.utils.trace import TraceConfig
from ml_dtypes import bfloat16

import iron
from iron import Profile, Scratchpad
from iron.common import (
    DispatchTime,
    Extent,
    In,
    Operator,
    Out,
    Select,
    Unresolvable,
    Value,
    Auto,
    Param,
    Built,
)
from iron.common.declare.field import AutoSpec, ParamSpec
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
    M: int = Param()
    K: int = Param()
    num_batches: int | None = Param(default=None)
    columns: int | None = Auto()
    tile_out: int = Auto(default=64)
    vec: int | None = Auto(repr=False)
    epilogue: str = Param(default="none")

    A = In(num_batches, M, K, obj_type=(tile_out, K), per=columns)
    B = In(num_batches, K, obj_type=(K,), broadcast=True)
    C = Out(num_batches, M, obj_type=(tile_out,), per=columns)
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
        K: int
        columns: int
        tile_out: int
        epilogue: str

        def build(self) -> Built:
            return Built([self.K, self.columns, self.tile_out, self.epilogue])

    def reference(self, A, B):
        return A @ B


# --------------------------------------------------------------------------
# Class creation: names, order, re-attached fields
# --------------------------------------------------------------------------


def test_fields_are_their_own_references():
    fields = {f.name: f for f in dataclasses.fields(MV)}
    assert MV.K is fields["K"] and MV.K.name == "K"
    assert type(ParamSpec.of(MV.K)) is ParamSpec
    assert MV.tile_out is fields["tile_out"]
    assert isinstance(ParamSpec.of(MV.tile_out), AutoSpec)


def test_members_keep_declaration_order_and_names():
    assert [m.name for m in MV.declaration.members] == ["A", "B", "C", "count", "start"]
    assert isinstance(MV.A, In) and isinstance(MV.C, Out)


def test_shapes_captured_bare_names_resolve_to_refs():
    # ``M`` and ``num_batches`` were the fields themselves in the class body.
    dims = MV.A.dims.dims
    assert dims[0].name == "num_batches"
    assert dims[1] is MV.M and dims[2] is MV.K
    assert MV.A.obj_dims.dims == (MV.tile_out, MV.K)
    assert MV.A.per.dims == (MV.columns,)


def test_dataclass_constructor_is_typed_by_real_fields():
    # trace, bound_values, pinned, the finish, the prologue and the
    # placements are every operator's, from the base.
    assert [f.name for f in dataclasses.fields(MV)] == [
        "trace",
        "bound_values",
        "pinned",
        "finish",
        "prepare",
        "placements",
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


def test_a_tunable_may_name_a_tile_but_not_a_buffer_shape():
    assert MV.A.obj_dims.dims[0] is MV.tile_out
    with pytest.raises(TypeError, match="host shape may not depend on tuning"):

        class Bad(Operator):
            M: int = Param()
            t: int = Auto(default=64)
            A = In(M, t)


def test_plain_defaulted_field_in_a_shape_is_its_literal():
    # A plain field with a default is bound to that default in the class
    # body, so a shape written against it captures the literal, not the
    # field. This is why anything a shape names must be declared with Param().
    class Plain(Operator):
        n: int = 4
        x = In(n, obj_type=(n,))

    assert Plain.x.dims.dims == (4,)
    assert Plain(n=8).x.shape == (4,)


def test_plain_field_reference_from_outside_is_rejected():
    class Plain(Operator):
        n: int = 4
        x = In(4)

    with pytest.raises(TypeError, match="not declared with Param"):

        class Bad(Plain):
            M: int = Param()
            A = In(M, Plain.n)


def test_expression_in_a_shape_is_rejected():
    with pytest.raises(TypeError, match="Expressions are not allowed"):

        class Bad(Operator):
            n: int = Param()
            x = In("n // 2")


def test_annotated_member_is_rejected():
    with pytest.raises(TypeError, match="without an annotation"):

        class Bad(Operator):
            M: int = Param()
            A: In = In(M)


def test_a_member_hiding_the_operators_own_attribute_is_rejected():
    with pytest.raises(TypeError, match="hides Operator.values"):

        class Bad(Operator):
            n: int = Param()
            values = In(n)


def test_a_field_hiding_the_operators_own_attribute_is_rejected():
    with pytest.raises(TypeError, match="hides Operator.inputs"):

        class Bad(Operator):
            inputs: int = Param()

    with pytest.raises(TypeError, match="hides Operator.name"):

        class Worse(Operator):
            name: str = Param()


def test_a_field_may_replace_an_operator_bases_own_attribute():
    class Base(Operator):
        window = None

    class Windowed(Base):
        window: int = Param(default=512)

    assert Windowed().window == 512


def test_float_value_is_rejected():
    with pytest.raises(TypeError, match="floating point"):
        Value(dtype=np.float32)


def test_float_scratchpad_annotation_is_rejected():
    with pytest.raises(TypeError, match="floating point"):

        class Bad(iron.Graph):
            def body(self, x, *, scale: Scratchpad[np.float32]):
                return x


def test_per_and_broadcast_are_exclusive():
    with pytest.raises(TypeError, match="either per"):

        class Bad(Operator):
            n: int = Param()
            c: int = Auto(default=2)
            x = In(n, obj_type=(4,), per=(c,), broadcast=True)


def test_a_probe_may_not_be_on_a_field_the_array_reads():
    with pytest.raises(TypeError, match="probe= on an array field"):

        class Baked(Operator):
            n: int = Param()
            alpha: float = Param(probe=1.0)
            x = In(n)

            class Array(Operator.Array):
                alpha: float

    with pytest.raises(TypeError, match="probe= on an array field"):

        class Tiled(Operator):
            n: int = Param()
            t: int = Param(probe=16)
            x = In(n, obj_type=(t,))

            class Array(Operator.Array):
                t: int


def test_a_probe_may_not_be_on_a_field_the_transfers_follow():
    with pytest.raises(TypeError, match="probe= on a field an operand's shape"):

        class Shaped(Operator):
            n: int = Param(probe=1024)
            x = In(n)

    with pytest.raises(TypeError, match="probe= on a field an operand's shape"):

        class Present(Operator):
            n: int = Param()
            gated: bool = Param(default=False, probe=False)
            x = In(n)
            w = In(n, when=gated)


def test_a_probe_may_not_be_on_a_field_the_constructor_cannot_set():
    with pytest.raises(TypeError, match="probe= on an init=False field"):

        class Fixed(Operator):
            n: int = Param()
            low: float = Param(default=0.0, init=False, probe=0.0)
            x = In(n)


def test_probed_sets_each_probe_field_and_nothing_else():
    class Bounded(Operator):
        n: int = Param()
        low: float = Param(probe=-np.inf)
        cap: tuple | None = Param(default=None, probe=None)
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


def test_buffers_resolve_shape_dtype_and_direction():
    specs = MV(M=64, K=256, num_batches=2).buffers
    assert [(type(s), s.shape) for s in specs] == [
        (In, (2, 64, 256)),
        (In, (2, 256)),
        (Out, (2, 64)),
    ]
    assert specs[0].dtype is bfloat16
    op = MV(M=1024, K=256)
    assert [b.name for b in op.inputs] == ["A", "B"]
    assert [b.name for b in op.outputs] == ["C"]


def test_a_t_or_none_dim_is_omitted_when_none_and_may_sit_anywhere():
    assert MV(M=64, K=256).A.shape == (64, 256)
    assert MV(M=64, K=256, num_batches=3).C.shape == (3, 64)

    class Stack(Operator):
        rows: int = Param()
        cols: int = Param()
        seq: int | None = Param(default=None)
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
        n: int = Param()
        t: int = Auto()
        x = In(n, obj_type=(t,))

        class Array(Operator.Array):
            t: int

    with pytest.raises(ValueError, match="t is None.*Resolve the operator first"):
        Tiled(n=64).x.obj_type


def test_a_block_float_tile_is_sized_by_its_blocks(npu2):
    class Blocks(Operator):
        n: int = Param()
        x = In(n, dtype=bfp.v8bfp16ebs8, obj_type=(4096,))

        class Array(Operator.Array):
            pass

    # 4096 blocks of 9 bytes: past half a core memory bank, so one deep.
    assert Blocks(n=4096).x.l1_depth == 1


def test_buffers_carry_the_declared_dtype_and_size(npu2):
    """The sizing contract: the sequence layout and the test harness allocate
    from ``b.dtype`` and ``b.nbytes`` of a declared buffer.
    """
    from iron.operators.copy import Copy

    x, y = Copy(input_buffer_size=512, dtype=np.int32).buffers
    assert x.dtype == np.int32 and y.dtype == np.int32
    assert (type(x), type(y)) == (In, Out)
    assert y.nbytes == 512 * 4


def test_instance_values_shadow_the_fields():
    op = MV(M=64, K=256, columns=2)
    assert op.K == 256 and op.columns == 2
    assert ParamSpec.of(MV.K) is not None and MV.K.name == "K"


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
        n: int = Param()
        x = In(n)

    with pytest.raises(TypeError, match="without an obj_type"):
        NoObjType(n=4).x.obj_type


def test_an_operand_fills_only_inside_its_operators_sequence():
    op = MV(M=1024, K=256, columns=2)
    with pytest.raises(ValueError, match="run in the operator's sequence"):
        op.A.fill(lane=0)


def test_per_call_values_bind_on_the_operator():
    class Copy(Operator):
        n: int = Param()
        src = In(n, obj_type=(n,))
        off = Value()
        live = DispatchTime()

        class Array(Operator.Array):
            n: int

    op = Copy(n=256)
    assert [v.name for v in op.values] == ["off", "live"]
    assert type(op.off) is Value and op.off.op is op
    assert isinstance(op.live, DispatchTime) and op.live is not Copy.live


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
        n: int = Param()
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
    op.A.bind([f"h{k}" for k in range(8)])
    assert op.A.handles[3] == "h3"
    op.B.bind("hb")
    assert op.B.handles == ["hb"]


class Scaled(Operator):
    """``x`` times a scale row when ``scaled``, else a copy of it."""

    N: int = Param()
    scaled: bool = Param(default=False)

    x = In(N, obj_type=(N,))
    s = In(N, obj_type=(N,), when=scaled)
    y = Out(N, obj_type=(N,))

    class Array(Operator.Array):
        N: int
        scaled: bool

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
    with pytest.raises(TypeError, match="must be a Param"):

        class Bad(Operator):
            N: int = Param()
            flag: bool = Auto(default=False)
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


def test_an_array_lists_what_names_its_streams_and_nothing_else():
    with pytest.raises(TypeError, match=r"\['tile_out'\] configure the array"):

        class Untiled(MV):
            class Array(Operator.Array):
                K: int
                columns: int

    with pytest.raises(TypeError, match=r"lists \['work'\], which are neither"):

        class Stray(MV):
            class Array(MV.Array):
                work: int


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


def test_profile_make_has_no_shared_state():
    """``profile.make()`` touches no global state, so concurrent calls from
    different threads cannot see each other's tunables.
    """
    import threading

    p = Profile()
    p.add(MV, columns=2)
    seen, errors = [], []

    def work():
        try:
            for _ in range(50):
                seen.append(p.make(MV, M=64, K=64).columns)
        except Exception as e:
            errors.append(e)

    threads = [threading.Thread(target=work) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert not errors and seen.count(2) == 200


def test_construction_is_by_keyword():
    with pytest.raises(TypeError, match="positional argument"):
        MV(3, M=64, K=64)


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
    assert MV(M=512, K=128).columns is None  # plain construction reads no profile


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
    with pytest.raises(TypeError, match="tile_out: int = Auto\\(default=32\\)"):

        class Pinned(MV):
            tile_out = 32  # dataclass would keep the base's 64 in silence

    class Annotated(MV):
        tile_out: int = Auto(default=32)

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
        scale = In(MV.M, obj_type=(MV.tile_out,), per=MV.columns)

    # 16 input channels: A's and scale's lanes per column, B once.
    assert MV.declaration.shim_columns(NPU2) == 8
    assert (
        Scaled.declaration.shim_columns(NPU2)
        == (NPU2.shim_dma_channels_in - 1) // 2
        == 7
    )


def test_a_broadcast_stream_is_paid_once_in_the_shim_budget():
    # 16 input channels: B once, then A's two channels a column.
    assert MV.declaration.shim_columns(NPU2, num_channels=2) == (16 - 1) // 2


def test_a_computed_default_is_inferred_from_a_shape_or_computed():
    class Rep(Operator):
        rows: int = Param()
        repeat: int = Param()
        out_rows: int = Param(derive=lambda op: op.rows * op.repeat)
        x = In(rows, 8)
        y = Out(out_rows, 8)

        def validate(self):
            self.check_derived("out_rows")  # a shape may bind it: it must agree

    assert Rep(rows=2, repeat=3).out_rows == 6  # computed
    assert Rep(rows=2, repeat=3, out_rows=6).out_rows == 6  # given, agrees
    with pytest.raises(ValueError, match="out_rows=5 is not what its other fields"):
        Rep(rows=2, repeat=3, out_rows=5)
    assert Rep.declaration.infer({"x": (2, 8)}, [(6, 8)]) == {"rows": 2, "out_rows": 6}


def test_a_select_picks_a_layout_within_a_storage():
    class Weights(Operator):
        K: int = Param()
        N: int = Param()
        blocks: int = Param(default=0)
        packed: bool = Param(default=False)
        transposed: bool = Param(default=False)
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
    assert [type(spec) for spec in grouped] == [In] * 3 + [Out]


# --------------------------------------------------------------------------
# An extent a graph may bound per call
# --------------------------------------------------------------------------


class Rows(Operator):
    """Rows of ``cols`` elements over ``lanes`` lanes; ``rows`` may be bounded."""

    rows: int = Param()
    cols: int = Param()
    lanes: int = Auto(default=2)
    valid = Extent(rows)
    count = Value(derive=lambda op: op.valid // op.lanes)  # reads the extent
    width = Value(derive=lambda op: op.cols)  # does not
    x = In(rows, cols, obj_type=(1, cols), per=(lanes,))
    y = Out(rows, cols, obj_type=(1, cols), per=(lanes,))

    def resolve(self, dev):
        return dataclasses.replace(self)

    class Array(Operator.Array):
        cols: int
        lanes: int

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
    with pytest.raises(TypeError, match="must name a Param"):

        class Bad(Operator):
            n: int = Auto(default=4)
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
        def body(self, x, *, n: aie.iron.DispatchTime[np.int32]):
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
