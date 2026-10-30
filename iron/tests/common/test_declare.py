# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON's operator over mlir-aie's declaration, device-free.

Everything here runs without a device and without generating MLIR: how
bound operands and per-call values behave on instances, the key's
parameters a build reads, profiles, extents a graph bounds, and runtime
parameters. The declaration itself (class creation, inference, resolution,
identity) is mlir-aie's and tested there. The design-generating half is
``iron/common/design/`` and needs the toolchain.
"""

import numpy as np
import pytest
from aie.iron import In, ObjectFifo, Out, ScratchpadParameter
from aie.iron.device import from_name
from aie.utils import bfp
from aie.utils.compile.jit.params import Select, param, per_call, tunable, widths
from ml_dtypes import bfloat16

import iron
from iron import Profile, Scratchpad
from iron.common import Built, Operator, Rtp, Unresolvable, Value, Xclbin
from iron.common.declare.operand import active_runtime, axis_of
from iron.common.design import OperatorDesign, OperatorRuntime
from iron.operators.mha import MHA
from iron.tests.support.declare import Rows

NPU2 = from_name("npu2", n_cols=8)


def from_operands(cls, *operand_shapes, **overrides):
    """``cls`` constructed from operand shapes, an optional input's by keyword."""
    inputs, outputs, overrides = cls.call_operands(operand_shapes, overrides)
    return cls(**{**overrides, **cls.declaration.infer(inputs, outputs, **overrides)})


# --------------------------------------------------------------------------
# A worked operator, close to GEMV
# --------------------------------------------------------------------------


class MV(Operator):
    M: int = param()
    K: int = param()
    num_batches: int | None = param(default=None)
    columns: int | None = tunable(domain=widths)
    tile_out: int = tunable(default=64)
    vec: int | None = tunable(repr=False)
    epilogue: str = param(default="none", array=True)

    A = In(num_batches, M, K, obj_shape=(tile_out, K), per=columns)
    B = In(num_batches, K, obj_shape=(K,))
    C = Out(num_batches, M, obj_shape=(tile_out,), per=columns)
    count = per_call(derive=lambda op: op.M // (op.columns * op.tile_out))
    start = per_call(derive=lambda op: 0)  # per call when a graph binds it

    def resolve(self, dev):
        cols = self.columns or dev.cols
        vec = self.vec or next((w for w in (64, 32, 16) if self.K % w == 0), None)
        if vec is None:
            raise Unresolvable(f"K={self.K}: no vector width divides it")
        return self.replace(columns=cols, vec=vec)

    def compatible(self):
        assert self.columns is not None
        unit = self.columns * self.tile_out
        if self.M % unit:
            raise ValueError(f"M={self.M} is not a multiple of {unit}")

    def build(self) -> Built:
        return Built([self.K, self.columns, self.tile_out, self.epilogue])

    def reference(self, A, B):
        return A @ B


def test_float_scratchpad_annotation_is_rejected():
    # Unvalidated, a float's bits reinterpreted as the scratchpad's integer
    # encoding would silently zero its top bits rather than fail loudly.
    with pytest.raises(TypeError, match="floating point"):

        class Bad(iron.Graph):
            def body(self, x, *, scale: Scratchpad[np.float32]):
                return x


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
        rows: int = param()
        cols: int = param()
        seq: int | None = param(default=None)
        x = In(rows, seq, cols)
        y = Out(rows, seq, cols)

    assert Stack(rows=8, cols=64).x.shape == (8, 64)
    assert Stack(rows=8, cols=64, seq=16).y.shape == (8, 16, 64)


def test_a_block_float_tile_is_sized_by_its_blocks(npu2):
    class Blocks(Operator):
        n: int = param()
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


def test_an_operand_fills_only_inside_its_operators_sequence(npu2):
    op = MV(M=1024, K=256, columns=2)
    with pytest.raises(ValueError, match="run in the operator's sequence"):
        op.A.fill(lane=0)
    # Nor inside another operator's.
    other = Rows(rows=8, cols=16).resolved()
    fifos = [ObjectFifo(np.ndarray[(16,), np.dtype[bfloat16]]) for _ in range(4)]
    other.x.bind([fifos[0].prod(), fifos[1].prod()])
    other.y.bind([fifos[2].cons(), fifos[3].cons()])
    token = active_runtime.set(OperatorRuntime(other, other.build()))
    try:
        with pytest.raises(ValueError, match="run in the operator's sequence"):
            op.A.fill(lane=0)
    finally:
        active_runtime.reset(token)


def test_per_call_values_bind_on_the_operator():
    class Copy(Operator):
        n: int = param()
        src = In(n, obj_shape=(n,))
        off = per_call()

        def exported_design(self):
            return None if self.n < 512 else (lambda: "module {}")

    op = Copy(n=256)
    assert [v.name for v in op.values] == ["off"]
    assert type(op.off) is Value and op.off.op is op and op.off is not Copy.off
    # A value every call gives regenerates an exported design's stream.
    assert not op.off.dispatch and Copy(n=512).off.dispatch


def test_an_exported_design_replaces_the_derived_one():
    # The design is another tool's text; the operands are declared as any
    # operator's are.
    class Exported(Operator):
        n: int = param()
        x = In(n)
        y = Out(n)

        def exported_design(self):
            return lambda: "module {}"

    op = Exported(n=64)
    assert [b.shape for b in op.buffers] == [(64,), (64,)]
    assert OperatorDesign(op).build() == "module {}"
    assert op.xclbin_operator() is op


# --------------------------------------------------------------------------
# The key's parameters, resolution, identity
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

    N: int = param()
    scaled: bool = param(default=False)

    x = In(N, obj_shape=(N,))
    s = In(N, obj_shape=(N,), when=scaled)
    y = Out(N, obj_shape=(N,))

    def build(self) -> Built:
        return Built([self.scaled])


def test_an_operand_declared_when_a_flag_exists_only_where_it_is_true():
    plain, scaled = Scaled(N=64), Scaled(N=64, scaled=True)
    assert [b.name for b in plain.buffers if b.streamed] == ["x", "y"]
    assert [b.name for b in scaled.buffers if b.streamed] == ["x", "s", "y"]
    assert scaled.s.shape == (64,)
    with pytest.raises(AttributeError, match="declared when=scaled"):
        plain.s
    # The flag decides the streams, so it is one of the key's parameters.
    assert "scaled" in Scaled.declaration.key
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

    (step,) = G().record(x=(64,)).steps
    assert not step.op.scaled
    assert [b.name for b in step.op.buffers] == ["x", "y"]

    class H(G):
        def body(self, x, s):
            Scaled.step(x, self.y, s=s)

    (step,) = H().record(x=(64,), s=(64,)).steps
    assert step.op.scaled
    assert [b.name for b in step.op.buffers] == ["x", "s", "y"]


def test_a_bound_value_is_its_member_on_the_instance():
    op = MV(M=1024, K=128)
    value, member = op.value("count"), MV.count
    assert type(value) is Value and value is not member and value.op is op
    assert (value.name, value.dtype, value.derive, value.words) == (
        member.name,
        member.dtype,
        member.derive,
        1,
    )


def test_a_derived_value_is_written_once_per_build():
    op = MV(M=1024, K=128).resolved(NPU2)
    assert op.residents == {"count": 2, "start": 0} and op.values == []


def test_a_value_a_graph_binds_is_per_call_and_no_longer_a_resident():
    class G(iron.Graph):
        def body(self, a, b, *, pos: Scratchpad[np.int32], n: Scratchpad[np.int32]):
            return MV.step(a, b, columns=8, start=pos, count=n)

    g = G()

    t = g.record(a=(1024, 128), b=(128,))
    (op,) = t.operators
    assert op.value("start").per_call and op.value("count").per_call
    assert [v.name for v in op.values] == ["count", "start"]
    assert [b.member.name for b in t.bindings] == ["start", "count"]  # call order
    assert op.residents == {}  # the preamble writes nothing for count
    # What an instance binds per call is part of its identity: an array
    # reading the value from the scratchpad is not the one reading a resident.
    assert op.design_key() != MV(M=1024, K=128, columns=8).design_key()


def test_array_sees_the_array_tier_alone():
    class Leaky(MV):
        def build(self) -> Built:
            return Built([self.M // self.tile_out])

    op = MV(M=1024, K=128).resolved(NPU2)
    assert MV.declaration.key == ("K", "columns", "tile_out", "vec", "epilogue")
    assert op.layout().build() == Built([128, 8, 64, "none"])
    with pytest.raises(AttributeError, match="reads M, which is not in the"):
        Leaky(M=1024, K=128).resolved(NPU2).layout().build()
    view = op.layout()
    assert view.A.op is view and view.A.obj_shape == (64, 128)
    with pytest.raises(AttributeError, match="reads num_batches, which is not in"):
        view.A.shape


def test_a_field_resolve_computes_is_kept_by_copies_and_checked_once_known():
    class Derived(MV):
        half: int = tunable(init=False)

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


def test_a_tunable_given_as_none_is_left_to_the_profile():
    p = Profile()
    p.add(MV, columns=4, tile_out=32)
    op = p.make(MV, M=1024, K=128, columns=None, tile_out=None)
    assert (op.columns, op.tile_out, op.pinned) == (4, 32, frozenset())


def test_saving_an_operator_outside_the_catalog_names_it(tmp_path):
    p = Profile()
    p.add(MV, columns=4)
    with pytest.raises(ValueError, match="MV is not in iron.operators.CATALOG"):
        p.save(tmp_path / "profile.json")


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


def test_no_column_count_resolves_when_one_column_overruns_the_shim():
    # NPU2 has 16 shim input channels; one column needs 17: A's 16 and B's one.
    with pytest.raises(Unresolvable, match="one column's streams exceed"):
        MV(M=96, K=64).resolve_columns(NPU2, None, num_channels=16)


def test_a_stream_with_no_lanes_is_paid_once_in_the_shim_budget():
    class Scaled(MV):
        scale = In(MV.M, obj_shape=(MV.tile_out,), per=MV.columns)

    # NPU2 has 16 shim input channels: B takes one, and each column two
    # more (A's and scale's, or A's two channels).
    assert MV.shim_columns(NPU2) == 8
    assert NPU2.shim_dma_channels_in == 16
    assert Scaled.shim_columns(NPU2) == (16 - 1) // 2
    assert MV.shim_columns(NPU2, num_channels=2) == (16 - 1) // 2


def test_compatible_runs_at_construction_once_every_tunable_is_known():
    with pytest.raises(ValueError, match="not a multiple"):
        MV(M=1000, K=128, columns=8, tile_out=64, vec=64)  # nothing left to resolve
    MV(M=1000, K=128)  # a tunable is open: compatible() waits for resolution


def test_mha_refuses_a_sequence_pad_of_no_whole_blocks():
    with pytest.raises(ValueError, match=r"seq_pad \(100\)"):
        MHA(num_heads=1, seq_len=100, seq_pad=100, d=64)


# --------------------------------------------------------------------------
# An extent a graph may bound per call
# --------------------------------------------------------------------------


def test_an_extent_reads_as_its_field_until_a_graph_bounds_it():
    op = Rows(rows=64, cols=8)
    assert op.valid == 64 and Rows.valid.bounds is Rows.rows
    assert not op.value("valid").per_call and not op.value("count").per_call
    assert op.residents == {"count": 32, "width": 8}
    assert op.derived_at("count", valid=16) == 8 and op.valid == 64  # unchanged
    with pytest.raises(TypeError, match="no extent \\['n'\\]"):
        op.derived_at("count", n=1)


def test_a_bounded_operand_binds_the_extent_and_what_derives_from_it(npu2):
    class G(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            y = Rows.step(x[:n])  # bounds this instance
            return Rows.step(y)  # and, through its output, the next

    g = G()

    t = g.record(x=(64, 8))
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
        count = per_call(derive=lambda op: calls.append(1) or op.valid // op.lanes)

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
        count = per_call(derive=lambda op: op.valid and {}["typo"])

    op = Buggy(rows=64, cols=8)
    op.use_value("valid")
    with pytest.raises(KeyError, match="typo"):
        op.values


def test_a_bound_is_refused_where_no_extent_takes_it():
    class G(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return MV.step(x[:n], x[0])  # M bounds no per-call value of MV

    g = G()

    with pytest.raises(TypeError, match="MV.A cannot be bounded"):
        g.record(x=(64, 128))

    class K(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return Rows.step(x[:, :n])  # nothing bounds cols

    k = K()

    with pytest.raises(TypeError, match="axis 1"):
        k.record(x=(64, 8))


# --------------------------------------------------------------------------
# Runtime parameters and shapes through a Select
# --------------------------------------------------------------------------


def _value(name, **kw):
    return Value(None, name, **kw)


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
        rows: int = param()
        cols: int = param()
        flip: bool = param(default=False)
        x = In(Select(flip, (cols, rows), (rows, cols)))

    assert axis_of(Laid.x.dims, "rows", Laid(rows=4, cols=8)) == 0
    assert axis_of(Laid.x.dims, "rows", Laid(rows=4, cols=8, flip=True)) == 1
    assert Laid(rows=4, cols=8, flip=True).x.shape == (8, 4)


class Doubled(Operator):
    """Doubles its input, with a reference and no kernel."""

    reference_only = True
    rows: int = param()
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
    with pytest.raises(TypeError, match="Doubled is reference-only"):
        Doubled(rows=4).compile()


def test_a_reference_only_operator_takes_no_image():
    with pytest.raises(TypeError, match="Shipped is reference-only"):

        class Shipped(Doubled, image=Xclbin(url="u", sha256="0" * 64, filename="f")):
            pass
