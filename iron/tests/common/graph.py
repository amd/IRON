# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graph functions, traced device-free.

A graph function run on handles produces a runlist, buffer names and
sizes, and value bindings; nothing here needs a toolchain. What is not
checked here is the image: that is OperatorSequence's job and the
hardware tests' job.
"""

import dataclasses
import inspect
from types import SimpleNamespace
from typing import Any

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron import DispatchTime, ceildiv
from aie.helpers.taplib import TensorAccessPattern
from aie.iron.device import from_name
from ml_dtypes import bfloat16

import iron
from iron import Carried, Precision, Profile, Scratchpad
from iron.common import Chain
from iron.common.graph import Handle
from iron.common.graph.trace import TracedGraph, Tracer
from iron.common.graph.carried import attach_emit, compose
from iron.common.graph.compiled import _words
from iron.common.declare import Unresolvable
from iron.common.graph.fold import Made, Place, Prologue, folded, replaced
from iron.common.graph.handle import Affine, PerCall
from iron.common.image.sequence import OperatorSequence
from iron.common.image.step import BufferRef, SequenceStep
from iron.common.image.artifacts import Parameter
from iron.common.image.packaging import Kind
import iron.functional as F
from iron.tests.common.graphs import FeedForward
from iron.operators.clamp import Clamp
from iron.operators.copy import Copy
from iron.tests.operators import copy_bounded_view
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.emit import UNCLAMPED, reference as emit_reference
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.gemm.op import GEMM as FLMGEMM
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.relu import ReLU
from iron.operators.repeat import Repeat
from iron.operators.rms_norm import RMSNorm
from iron.operators.silu import SiLU
from iron.operators.softmax import Softmax
from iron.tests.common.declare import Rows
from iron.tests.common.graphs import Trail, Walk
from iron.tests.common.llama_model import llama_1b, small

E, H = 2048, 8192


def z(*shape, dtype=bfloat16):
    return np.zeros(shape, dtype=dtype)


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _ffn():
    w_gate, w_up, w_down, norm_w = z(H, E), z(H, E), z(E, H), z(E)
    cache = iron.state((4, 1024, 64))

    class Ffn(iron.Graph):
        def body(self, x, *, pos: Scratchpad[np.int32]):
            h = RMSNorm.step(x, weight=norm_w)  # a bare tensor is a weight
            gate = GEMV.step(
                w_gate, h, num_aie_columns=8, tile_size_input=4, tile_size_output=H // 8
            )
            up = GEMV.step(
                w_up, h, num_aie_columns=8, tile_size_input=4, tile_size_output=H // 8
            )
            act = ElementwiseMul.step(SiLU.step(gate), up)
            Copy.step(
                act[:, : 4 * 64].reshape(4, 64), cache[:, pos]
            )  # writes state; returns nothing
            return GEMV.step(w_down, act, num_aie_columns=8, tile_size_output=E // 8)

    ffn = Ffn()

    refs: dict[str, Any] = dict(
        w_gate=w_gate, w_up=w_up, w_down=w_down, norm_w=norm_w, cache=cache
    )
    return ffn, refs


def test_tracing_records_the_runlist_with_names_from_roles():
    ffn, refs = _ffn()
    t = ffn.trace(x=(1, E))
    assert isinstance(t, TracedGraph)
    assert [(type(s.op).__name__, *map(str, s.refs())) for s in t.steps] == [
        ("RMSNorm", "x", "w0", "rmsnorm0"),
        ("GEMV", "w1", "rmsnorm0", "gemv1"),
        ("GEMV", "w2", "rmsnorm0", "gemv2"),
        ("SiLU", "gemv1", "silu3"),
        ("ElementwiseMul", "silu3", "gemv2", "elementwisemul4"),
        ("Copy", "elementwisemul4[0:512]", "state0"),
        ("GEMV", "w3", "elementwisemul4", "out"),
    ]
    assert [h.name for h in t.inputs] == ["x"] and [h.name for h in t.outputs] == [
        "out"
    ]
    # Weights, the state and a sliced intermediate keep private addresses.
    assert t.pinned == {
        "w0": E * 2,
        "w1": H * E * 2,
        "w2": H * E * 2,
        "w3": H * E * 2,
        "state0": 4 * 1024 * 64 * 2,
        "elementwisemul4": H * 2,
    }


def test_a_name_the_tracer_makes_up_never_aliases_one_it_was_given():
    class Held(iron.Graph):
        def __init__(self):
            self.out = iron.state((E,))
            self.silu0 = iron.weight(z(E))

        def body(self, x):
            Copy.step(SiLU.step(x), self.out)
            return ElementwiseAdd.step(SiLU.step(x), self.silu0)

    t = Held().trace(x=(E,))
    assert [(type(s.op).__name__, *map(str, s.refs())) for s in t.steps] == [
        ("SiLU", "x", "silu0_1"),
        ("Copy", "silu0_1", "out"),
        ("SiLU", "x", "silu1"),
        ("ElementwiseAdd", "silu1", "silu0", "out_1"),
    ]
    assert [h.name for h in t.outputs] == ["out_1"] and t.pinned == {
        "out": E * 2,
        "silu0": E * 2,
    }

    class Given(iron.Graph):
        def body(self, out):
            return SiLU.step(out)

    t = Given().trace(out=(E,))
    assert [h.name for h in t.inputs] == ["out"] and [h.name for h in t.outputs] == [
        "out_1"
    ]


def test_arrays_are_shared_by_array_key_and_extents_are_not():
    ffn, _ = _ffn()
    t = ffn.trace(x=(1, E))
    gate, up, down = (s.op for s in t.steps if type(s.op) is GEMV)
    assert (
        gate.array_key() == up.array_key() and gate is not up
    )  # one array, two operators
    assert down.array_key() != gate.array_key()  # a different K is a different array
    assert [type(o).__name__ for o in t.arrays] == [
        "RMSNorm",
        "GEMV",
        "SiLU",
        "ElementwiseMul",
        "Copy",
        "GEMV",
    ]
    assert (gate.M, gate.K, gate.num_batches) == (H, E, 1)


def test_per_call_values_bind_to_the_operator_and_enable_it():
    ffn, _ = _ffn()
    t = ffn.trace(x=(1, E))
    (binding,) = t.bindings
    op, value = binding.op, binding.expression.value
    assert type(op) is Copy and binding.member.name == "out_offset"
    assert value.name == "pos" and value.kind is Kind.SCRATCHPAD
    assert op.value("out_offset").per_call and not op.value("in_offset").per_call
    assert [v.name for v in op.values] == ["out_offset"]


def test_every_traced_operator_tunes_from_the_device_alone():
    ffn, _ = _ffn()
    t = ffn.trace(x=(1, E))
    for op in t.operators:
        op.resolved(
            aie_utils.get_current_device()
        )  # every default fills; every extent is compatible
    silu = next(s.op for s in t.steps if type(s.op) is SiLU).resolved(
        aie_utils.get_current_device()
    )
    assert (silu.num_aie_columns, silu.num_channels, silu.tile_size) == (8, 1, 256)
    norm = next(
        s.op for s in t.steps if type(s.op) is RMSNorm and s.op.weighted
    ).resolved(aie_utils.get_current_device())
    assert norm.num_aie_columns == 1  # one row: one core


def test_a_state_written_by_one_step_is_pinned_and_readable():
    ffn, refs = _ffn()
    t = ffn.trace(x=(1, E))
    state, handle = t.states[id(refs["cache"])]
    assert state is refs["cache"]
    assert handle.role == "state" and handle.name == "state0"
    assert refs["cache"].name == "state0"


def test_slices_are_views_into_the_parent_in_bytes():
    h = Handle((8, 64), bfloat16, "acts", "intermediate")
    part = h[2:4]
    assert part.shape == (2, 64) and part.ref() == BufferRef("acts", 256, 256)
    assert h[3].shape == (64,) and h[3].ref() == BufferRef("acts", 384, 128)
    with pytest.raises(TypeError, match="slicing a slice"):
        part[0]
    with pytest.raises(ValueError, match="unit steps"):
        h[::2]
    assert h.reshape(512).shape == (512,) and h.reshape(512).ref() == BufferRef("acts")
    assert part.reshape(128).ref() == BufferRef("acts", 256, 256)
    with pytest.raises(ValueError, match="cannot reshape"):
        h.reshape(3, 3)


def test_an_input_read_only_through_slices_is_laid_out_whole():
    class Halves(iron.Graph):
        def body(self, x):
            return SiLU.step(x[E // 2 :]), SiLU.step(x[: E // 2])

    t = Halves().trace(x=(E,))
    assert t.pinned == {"x": E * 2}
    seq = OperatorSequence(t)
    seq.prepare()
    assert seq.layout["x"] == ("input", 0, E * 2)
    assert [s.buffers[0] for s in seq.steps] == [
        BufferRef("x", E, E),
        BufferRef("x", 0, E),
    ]


def test_alike_instances_bound_to_different_values_are_different_designs():
    """Two copies alike in every field, one indexed by ``a`` and one by ``b``,
    write through two symbols and build twice; two bound to one value share.
    """
    c1, c2, c3 = (iron.state((4, 64, 16)) for _ in range(3))

    class F(iron.Graph):
        def body(self, x, *, a: Scratchpad[np.int32], b: Scratchpad[np.int32]):
            Copy.step(x, c1[:, a])
            Copy.step(x, c2[:, b])
            Copy.step(x, c3[:, a])

    f = F()

    t = f.trace(x=(4, 16))
    by_value = {b.expression.value.name: b for b in t.bindings}
    assert len(t.bindings) == 3 and set(by_value) == {"a", "b"}
    first, second, third = t.bindings
    assert first.expression == t.values[0] * 16  # an element offset: a rows of 16
    assert {k: e.name for k, e in first.op.bound_values.items()} == {
        "out_offset": "a_x16"
    }
    assert first.op.design_key() != second.op.design_key()
    assert first.op.design_key() == third.op.design_key()
    symbols = [b.member.symbol for b in t.bindings]
    assert symbols[0] != symbols[1] and symbols[0] == symbols[2]
    assert symbols[0].endswith("_out_offset_a_x16")
    assert symbols[1].endswith("_out_offset_b_x16")


def test_an_explicit_instance_checks_its_operands_shapes():
    q = GEMV(M=256, K=E, num_aie_columns=8, tile_size_input=4, tile_size_output=32)
    w_t = z(E, 256)  # the weight transposed: the same element count

    class Step(iron.Graph):
        def body(self, x):
            return q.apply(w_t, x)

    step = Step()

    with pytest.raises(ValueError, match=r"GEMV.A is \(256, 2048\)"):
        step.trace(x=(E,))


def test_binding_two_handles_to_one_instance_is_an_error():
    copy = Copy(input_buffer_size=64, output_buffer_size=64)

    class Two(iron.Graph):
        def body(self, x, *, a: Scratchpad[np.int32], b: Scratchpad[np.int32]):
            y = copy.apply(x, out_offset=a)
            return copy.apply(y, out_offset=b)

    two = Two()

    with pytest.raises(ValueError, match="bound to a at an earlier call site"):
        two.trace(x=(64,))


def test_a_graph_carries_its_profile():
    """A graph's profile reaches every run of the body: the
    trace and the host reference alike, with a call's own keyword kept.
    """
    profile = Profile()
    profile.add(GEMV, tile_size_input=4, tile_size_output=16)
    profile.add(GEMV, M=E, tile_size_output=E // 8)
    w_a, w_b = z(256, E), z(E, 256)

    class Two(iron.Graph):
        def body(self, x):
            return GEMV.step(w_b, GEMV.step(w_a, x, tile_size_output=32))

    two = Two()
    two.profile = profile

    a, b = (s.op for s in two.trace(x=(E,)).steps)
    assert (a.tile_size_input, a.tile_size_output) == (4, 32)  # the call's own
    assert (b.tile_size_input, b.tile_size_output) == (4, E // 8)  # the profile's
    assert two.reference(z(E)).shape == (E,)  # constructs under the profile too
    assert GEMV(M=E, K=256).tile_size_output is None  # nothing outside it


def test_an_explicit_instance_is_applied_like_the_class():
    q = GEMV(M=256, K=E, num_aie_columns=8, tile_size_input=4, tile_size_output=32)
    w = z(256, E)

    class Step(iron.Graph):
        def body(self, x):
            return q.apply(w, x)

    step = Step()

    t = step.trace(x=(E,))
    assert t.steps[0].op is q and [h.name for h in t.outputs] == ["out"]
    with pytest.raises(TypeError, match="outside a graph's body on device tensors"):
        q(w, z(E))


def test_shape_mismatch_and_rank_rules():
    w = z(256, E)

    class Bad(iron.Graph):
        def body(self, x):
            return GEMV.step(w, x)

    bad = Bad()

    with pytest.raises(ValueError, match=r"K is 1024 from B.shape\[0\] but 2048"):
        bad.trace(x=(E // 2,))
    add = ElementwiseAdd

    class Flat(iron.Graph):
        def body(self, x, y):
            return add.step(x, y)  # a flat operator takes any rank

    flat = Flat()

    t = flat.trace(x=(4, 512), y=(4, 512))
    assert t.steps[0].op.size == 2048 and t.outputs[0].shape == (4, 512)


def test_keyword_only_parameters_must_be_annotated_as_values():
    with pytest.raises(TypeError, match="annotated Scratchpad"):

        class F(iron.Graph):
            def body(self, x, *, n):
                return x

    class G(iron.Graph):
        def body(self, x, *, n: DispatchTime[np.int32]):
            return SiLU.step(x)

    g = G()

    t = g.trace(x=(1024,))
    assert [(v.name, v.kind) for v in t.values] == [("n", Kind.DISPATCH_TIME)]


def test_returning_an_input_or_a_slice_is_refused():
    class Ident(iron.Graph):
        def body(self, x):
            return x

    ident = Ident()

    with pytest.raises(TypeError, match="returns its input"):
        ident.trace(x=(64,))

    class Part(iron.Graph):
        def body(self, x):
            return SiLU.step(x)[:8]

    part = Part()

    with pytest.raises(TypeError, match="whole handles"):
        part.trace(x=(64,))


# --------------------------------------------------------------------------
# A gated feed-forward, as a graph
# --------------------------------------------------------------------------


def test_swiglu_one_token_shares_one_array_and_one_build_for_gate_and_up():

    ffn = FeedForward(z(H, E), z(H, E), z(E, H))
    t = ffn.trace(x=(1, E))
    assert [type(s.op).__name__ for s in t.steps] == [
        "GEMV",
        "GEMV",
        "SiLU",
        "ElementwiseMul",
        "GEMV",
    ]
    gate, up, down = (s.op for s in t.steps if type(s.op) is GEMV)
    assert gate.array_key() == up.array_key() and gate.design_key() == up.design_key()
    assert down.design_key() != gate.design_key()
    assert (gate.M, gate.K, down.M, down.K) == (H, E, E, H)
    assert [h.name for h in t.inputs] == ["x"] and [h.name for h in t.outputs] == [
        "out"
    ]


def test_swiglu_folds_its_silu_and_its_product_into_the_gate(npu2):
    t = FeedForward(z(H, E), z(H, E), z(E, H)).trace(x=(1, E))
    f, count = folded(t, npu2)
    assert [(str(fold), n) for fold, n in count.items()] == [
        ("SiLU into GEMV", 1),
        ("SiLU, then ElementwiseMul into GEMV", 1),
    ]
    assert [type(s.op).__name__ for s in f.steps] == ["GEMV", "GEMV", "GEMV"]
    up, gate, down = f.steps
    assert [type(link.op) for link in gate.op.finish] == [SiLU, ElementwiseMul]
    assert up.op.finish == down.op.finish == Chain()
    # The up projection rides the gate's matrix beside B, so the gate has an
    # array of its own.
    assert [b.name for b in gate.op.inputs if not b.streamed] == ["B", "finish1_b"]
    assert gate.op.resolved().array_key() != up.op.resolved().array_key()
    mul = next(s for s in t.steps if type(s.op) is ElementwiseMul)
    assert gate.inputs[2].name == up.outputs[0].name == mul.inputs[1].name
    assert gate.outputs[0].name == mul.outputs[0].name == down.inputs[1].name
    assert f.inputs == t.inputs and f.outputs == t.outputs


@pytest.mark.parametrize("device", ["npu1", "npu2"])
def test_a_prompt_swiglu_finishes_its_gate_with_its_silu(device, request):
    t = FeedForward(z(H, E), z(H, E), z(E, H)).trace(x=(256, E))
    f, count = folded(t, request.getfixturevalue(device))
    assert [(str(fold), n) for fold, n in count.items()] == [("SiLU into GEMM", 1)]
    gate, up, mul, down = (s.op for s in f.steps)
    assert (type(gate), type(mul)) == (FLMGEMM, ElementwiseMul)
    assert gate.activation is Epilogue.SILU
    assert gate.compiled_modes == (Epilogue.NONE, Epilogue.SILU)
    # The other projections run on the gate's array, without an activation.
    for op in (up, down):
        assert op.activation is Epilogue.NONE
        assert op.finish.shared == gate.finish.shared


def test_runs_sharing_what_they_made_fold_alike_with_the_same_operators(npu2):
    t = FeedForward(z(H, E), z(H, E), z(E, H)).trace(x=(1, E))
    made = Made(npu2)
    first, count = folded(t, npu2, made=made)
    again, recount = folded(t, npu2, made=made)
    alone, _ = folded(t, npu2)
    assert recount == count
    assert [s.op for s in again.steps] == [s.op for s in first.steps]
    assert [s.op.design_key() for s in alone.steps] == [
        s.op.design_key() for s in first.steps
    ]
    assert alone.steps[1].op is not first.steps[1].op


def test_each_folded_design_is_paired_with_the_one_whose_step_it_took(npu2):
    t = FeedForward(z(H, E), z(H, E), z(E, H)).trace(x=(1, E))
    f, _ = folded(t, npu2)
    # The gate took on the silu and the product; up kept its own.
    assert replaced(t, f) == [(t.steps[0].op, f.steps[1].op)]


class _Gate(iron.Graph):
    def __init__(self, use, rows=H, tile=H // 8):
        self.w, self.use, self.tile = z(rows, E), use, tile

    def body(self, x):
        gate = GEMV.step(self.w, x, num_aie_columns=8, tile_size_output=self.tile)
        act = SiLU.step(gate)
        if self.use == "returned":
            return act, gate
        if self.use == "read twice":
            return ElementwiseAdd.step(act, gate)
        return act


def test_a_fold_needs_the_intermediate_to_itself(npu2):
    t = _Gate("returned").trace(x=(E,))
    assert folded(t, npu2) == (t, {})
    # Read twice, the gate keeps its output; the sum takes it beside silu's.
    _, count = folded(_Gate("read twice").trace(x=(E,)), npu2)
    assert [str(fold) for fold in count] == ["ElementwiseAdd into SiLU"]
    assert folded(_Gate("once").trace(x=(E,)), npu2)[1].total() == 1


def test_a_fold_the_producer_cannot_resolve_is_left_alone(npu2):
    # An output tile of 8 rows: silu's 32 lanes do not divide it.
    t = _Gate("once", rows=512, tile=8).trace(x=(E,))
    gemv, silu = (s.op for s in t.steps)
    with pytest.raises(ValueError, match="not a multiple of the kernel"):
        gemv.fold(silu).resolved(npu2)
    assert folded(t, npu2) == (t, {})


class _Sums(iron.Graph):
    def __init__(self, consumer=SiLU):
        self.consumer = consumer.step if isinstance(consumer, type) else consumer

    def body(self, a, b):
        return self.consumer(ElementwiseAdd.step(a, b)), ElementwiseAdd.step(b, a)


def test_an_elementwise_step_finishes_its_consumer_in_its_own_cores(npu2):
    t = _Sums().trace(a=(E,), b=(E,))
    f, count = folded(t, npu2)
    assert [(str(fold), n) for fold, n in count.items()] == [
        ("SiLU into ElementwiseAdd", 1)
    ]
    finished, plain = (s.op.resolved(npu2) for s in f.steps)
    ((step, at),) = [(link.op, link.at) for link in finished.finish]
    assert (type(step), at, step.size, step.tile_size) == (SiLU, 0, 256, 256)
    # The other sum moved onto the finished one's array, choosing no step.
    assert finished.array_key() == plain.array_key()
    assert finished.design_key() != plain.design_key()
    assert finished.name != plain.name
    chains = [tuple(type(link.op) for link in c) for c in finished.finish.shared]
    assert chains[finished.residents["finish_chain"]] == (SiLU,)
    assert chains[plain.residents["finish_chain"]] == ()
    rng = np.random.default_rng(0)
    a, b = (rng.standard_normal(E).astype(bfloat16) for _ in range(2))
    (got,) = finished._call_reference({"a": a, "b": b}).values()
    np.testing.assert_array_equal(
        got, SiLU(size=E).reference(ElementwiseAdd(size=E).reference(a, b))
    )


def test_an_unfinished_operator_keeps_its_keys(npu2):
    add = ElementwiseAdd(size=E).resolved(npu2)
    assert "finish" not in repr((add.array_key(), add.design_key()))
    assert "finish_chain" not in add.residents


def test_an_operator_with_an_array_of_its_own_finishes_nothing(npu2):
    with pytest.raises(ValueError, match="finish no output"):
        Clamp(size=E, low=0, high=1).fold(SiLU(size=E)).resolved(npu2)
    with pytest.raises(ValueError, match="array of their own"):
        ElementwiseAdd(size=E).fold(Clamp(size=E, low=0, high=1)).resolved(npu2)
    t = _Sums(lambda y: Clamp.step(y, low=0.0, high=1.0)).trace(a=(E,), b=(E,))
    assert folded(t, npu2) == (t, {})


class _Chain(iron.Graph):
    def __init__(self, at=0, cols=4, channels=1):
        self.at, self.cols, self.channels = at, cols, channels

    def body(self, a, c):
        s = SiLU.step(
            ReLU.step(a, num_aie_columns=self.cols, num_channels=self.channels)
        )
        return ElementwiseMul.step(s, c) if self.at == 0 else ElementwiseMul.step(c, s)


@pytest.mark.parametrize("at", [0, 1])
def test_a_step_folds_with_its_other_input_streamed_beside(at, npu2):
    t = _Chain(at).trace(a=(E,), c=(E,))
    f, count = folded(t, npu2)
    mul = f"ElementwiseMul{' (input 1)' if at else ''}"
    assert [str(fold) for fold in count] == [
        "SiLU into ReLU",
        f"SiLU, then {mul} into ReLU",
    ]
    (step,) = f.steps
    fused = step.op.resolved(npu2)
    assert [(type(link.op), link.at) for link in fused.finish] == [
        (SiLU, 0),
        (ElementwiseMul, at),
    ]
    # A chain streaming an input of its own has an array of its own.
    assert fused.finish.shared == ()
    assert [b.name for b in fused.inputs] == ["x", f"finish1_{'ab'[1 - at]}"]
    assert [h.name for h in step.inputs] == ["a", "c"]
    assert replaced(t, f) == [(t.steps[0].op, step.op)]
    rng = np.random.default_rng(0)
    a, c = (rng.standard_normal(E).astype(bfloat16) for _ in range(2))
    s = SiLU(size=E).reference(ReLU(size=E).reference(a))
    want = ElementwiseMul(size=E).reference(*((s, c) if at == 0 else (c, s)))
    (got,) = fused._call_reference(
        dict(zip([i.name for i in fused.inputs], (a, c)))
    ).values()
    np.testing.assert_array_equal(got, want)
    # A fold of a chain brings the folds before it; the first comes alone.
    first, chain = count
    assert folded(t, npu2, (chain,))[1] == count
    assert list(folded(t, npu2, (first,))[1]) == [first]


class _GemvAdd(iron.Graph):
    def __init__(self):
        self.w = z(E, E)

    def body(self, x, r):
        return ElementwiseAdd.step(GEMV.step(self.w, x, num_aie_columns=8), r)


def test_a_fold_that_narrows_its_producer_is_refused(npu2):
    # Eight columns of two channels each, twice, are past the shim's sixteen.
    t = _Chain(cols=8, channels=2).trace(a=(2 * E,), c=(2 * E,))
    f, count = folded(t, npu2)
    assert [str(fold) for fold in count] == ["SiLU into ReLU"]


class _SumChain(iron.Graph):
    def body(self, a, b, c):
        return ElementwiseMul.step(
            SiLU.step(ElementwiseAdd.step(a, b, num_aie_columns=4)), c
        )


def test_a_fold_past_its_cores_input_channels_is_refused(npu2):
    # A sum's cores read two streams, and neither carries a product's input.
    t = _SumChain().trace(a=(E,), b=(E,), c=(E,))
    f, count = folded(t, npu2)
    assert [str(fold) for fold in count] == ["SiLU into ElementwiseAdd"]
    sum_ = next(s.op for s in f.steps if type(s.op) is ElementwiseAdd)
    mul = next(s.op for s in t.steps if type(s.op) is ElementwiseMul)
    with pytest.raises(Unresolvable, match="no input of its is declared feed=True"):
        sum_.fold(mul, 0).resolved()


def test_a_finish_input_rides_a_matvecs_matrix(npu2):
    gemv = _GemvAdd().trace(x=(E,), r=(E,))
    f, count = folded(gemv, npu2)
    assert [str(fold) for fold in count] == ["ElementwiseAdd into GEMV"]
    (step,) = f.steps
    op = step.op.resolved()
    assert [(b.name, b.streamed) for b in op.inputs] == [
        ("A", True),
        ("B", False),
        ("finish0_b", False),
    ]
    # Its tile is a column's share of rows, read twice to fill one of A's.
    assert (op.num_aie_columns, op.tile_size_input, op.tile_size_output) == (8, 2, 256)
    assert step.inputs[2].name == "r"


def test_a_finish_input_a_matvec_cannot_carry_is_refused(npu2):
    # A 32-row tile is read 128 times to fill one of A's, past a descriptor's 64.
    pinned = GEMV(M=256, K=1024, tile_size_input=4, tile_size_output=32)
    with pytest.raises(Unresolvable, match="in at most 64 whole reads"):
        pinned.fold(ElementwiseAdd(size=256), 0).resolved(npu2)
    # Four batches are eight transfers on each lane of A.
    batched = GEMV(M=256, K=128, num_batches=4)
    with pytest.raises(Unresolvable, match="8 transfers, .* past the 4 descriptors"):
        batched.fold(ElementwiseAdd(size=4 * 256), 0).resolved(npu2)
    # A repeat runs its batches in order, so each takes its own residual.
    repeated = GEMV(M=256, K=128, num_batches=2, repeat=2)
    repeated.fold(ElementwiseAdd(size=2 * 256), 0).resolved(npu2)
    # A matmul's cores hold its output's blocks out of order.
    gemm = GEMM(M=256, K=512, N=512).fold(ElementwiseAdd(size=256 * 512), 0)
    with pytest.raises(Unresolvable, match="in an order of their own"):
        gemm.resolved(npu2)


class _Bounded(iron.Graph):
    def __init__(self, gemm, other_bounded=True):
        self.w, self.gemm, self.other_bounded = z(256, 64), gemm, other_bounded

    def body(self, x, y, *, n: Scratchpad[np.int32]):
        if self.gemm:
            return SiLU.step(GEMM.step(x[:n], self.w, b_col_maj=True))
        other = y[:n] if self.other_bounded else y
        return ElementwiseMul.step(
            SiLU.step(ReLU.step(x[:n], num_aie_columns=4)), other
        )


def test_a_bounded_step_folds_under_its_producers_bound(npu2):
    t = _Bounded(gemm=True).trace(x=(512, 64), y=(512, 256))
    f, count = folded(t, npu2)
    assert [str(fold) for fold in count] == ["SiLU into GEMM"]
    (step,) = f.steps
    assert {k: e.name for k, e in step.op.bound_extents.items()} == {"valid": "n"}
    assert [(b.op, b.member.name) for b in f.bindings] == [(step.op, "valid")]

    t = _Bounded(gemm=False).trace(x=(512, 64), y=(512, 64))
    f, count = folded(t, npu2)
    assert [str(fold) for fold in count] == [
        "SiLU into ReLU",
        "SiLU, then ElementwiseMul into ReLU",
    ]
    (step,) = f.steps
    fused = step.op.resolved(npu2)
    assert {b.op for b in f.bindings} == {step.op}
    # The product's other input streams under the relu's bound.
    ((extent, _, _),) = (b.bounded for b in fused.finish_inputs)
    assert extent.name == "valid"


def test_a_fold_with_an_input_its_bound_does_not_reach_is_refused(npu2):
    t = _Bounded(gemm=False, other_bounded=False).trace(x=(512, 64), y=(512, 64))
    f, count = folded(t, npu2)
    assert [str(fold) for fold in count] == ["SiLU into ReLU"]
    assert {b.op for b in f.bindings} == {s.op for s in f.steps}


class _Late(iron.Graph):
    def __init__(self, overwrite):
        self.st = iron.state((E,))
        self.overwrite = overwrite

    def body(self, a, b):
        s = SiLU.step(self.st)
        if self.overwrite:
            Copy.step(a, self.st)
        return ElementwiseMul.step(s, ReLU.step(b))


def test_a_fold_runs_where_what_it_reads_is_written(npu2):
    # The product's other input is made after silu: the fold runs in its place.
    t = _Late(overwrite=False).trace(a=(E,), b=(E,))
    f, count = folded(t, npu2)
    assert [str(fold) for fold in count] == ["ElementwiseMul into SiLU"]
    assert [type(s.op).__name__ for s in f.steps] == ["ReLU", "SiLU"]
    # Moved past the copy, silu would read the state it overwrites, so the
    # product folds into the relu instead.
    t = _Late(overwrite=True).trace(a=(E,), b=(E,))
    f, count = folded(t, npu2)
    assert [str(fold) for fold in count] == ["ElementwiseMul (input 1) into ReLU"]
    assert [type(s.op).__name__ for s in f.steps] == ["SiLU", "Copy", "ReLU"]
    assert [h.name for h in f.steps[2].inputs] == ["b", f.steps[0].outputs[0].name]


class _Store(iron.Graph):
    def __init__(self, use="once", rows=512, length=8):
        self.w, self.use = z(rows, E), use
        self.cache = iron.state((length, rows))

    def body(self, x, *, pos: Scratchpad[np.int32]):
        y = GEMV.step(self.w, x, num_aie_columns=8)
        if self.use == "read between":
            out = ReLU.step(self.cache[0])
        Copy.step(y, self.cache[pos])
        if self.use == "returned":
            return y
        if self.use == "read between":
            return out
        return SiLU.step(x)


def test_a_copy_into_a_state_folds_into_its_producers_drain(npu2):
    t = _Store().trace(x=(E,))
    f, count = folded(t, npu2)
    assert [str(fold) for fold in count] == ["Copy into the drain of GEMV"]
    assert [type(s.op).__name__ for s in f.steps] == ["GEMV", "SiLU"]
    (slot,) = f.steps[0].outputs
    # It drains into the whole cache, at the run the copy's offset moves.
    assert slot.ref() == BufferRef("cache")
    assert f.steps[0].op.placements == (("C", 8 * 512, 0),)
    (binding,) = f.bindings
    assert binding.op is f.steps[0].op and binding.member.name == "C_offset"
    assert binding.expression == Affine(t.values[0], scale=512)
    assert folded(t, npu2, without=tuple(count)) == (t, {})


@pytest.mark.parametrize("use", ["returned", "read between"])
def test_a_copy_whose_input_or_output_another_step_names_stays(use, npu2):
    t = _Store(use).trace(x=(E,))
    assert folded(t, npu2) == (t, {})


class _Row(iron.Graph):
    def __init__(self, at):
        self.w, self.at = z(512, E), at
        self.cache = iron.state((8, 256))

    def body(self, x, *, pos: Scratchpad[np.int32]):
        y = GEMV.step(self.w, x, num_aie_columns=8)
        if self.at == "static":
            Copy.step(y.reshape(2, 256), self.cache[2:4])
        else:
            Copy.step(y.reshape(2, 256)[pos], self.cache[3])
        return SiLU.step(x)


def test_a_copy_to_a_fixed_run_folds_and_one_of_part_of_its_input_stays(npu2):
    f, count = folded(_Row("static").trace(x=(E,)), npu2)
    assert [str(fold) for fold in count] == ["Copy into the drain of GEMV"]
    assert f.steps[0].outputs[0].ref() == BufferRef("cache", 1024, 1024)
    assert f.steps[0].op.placements == (("C", 512, 0),)
    assert not f.bindings
    t = _Row("from pos").trace(x=(E,))
    assert not any(isinstance(fold, Place) for fold in folded(t, npu2)[1])


class _Project(iron.Graph):
    def __init__(self, heads=2, residual=False, shared=False):
        self.ws = [z(512, E) for _ in range(heads)]
        self.norm = z(E)
        self.residual, self.shared = residual, shared

    def body(self, x, r):
        s = ElementwiseAdd.step(x, r) if self.residual else x
        h = RMSNorm.step(s, weight=self.norm)
        ys = [GEMV.step(w, h, num_aie_columns=8) for w in self.ws]
        return (*ys, ElementwiseAdd.step(h, r)) if self.shared else tuple(ys)


def test_a_norm_folds_into_the_matvecs_that_read_it(npu2):
    t = _Project().trace(x=(1, E), r=(1, E))
    f, count = folded(t, npu2)
    assert [(str(fold), n) for fold, n in count.items()] == [
        ("RMSNorm into GEMV, GEMV", 1)
    ]
    assert [type(s.op).__name__ for s in f.steps] == ["GEMV", "GEMV"]
    # Each matvec reads the norm's input in place of its output, then its weight.
    for step, w in zip(f.steps, ("ws.0", "ws.1")):
        fused = step.op.resolved(npu2)
        assert [(type(link.op), link.at) for link in fused.prepare] == [(RMSNorm, 0)]
        assert [b.name for b in fused.inputs] == ["A", "B", "prepare0_weight"]
        assert [h.name for h in step.inputs] == [w, "x", "norm"]
    assert replaced(t, f) == [
        (t.steps[1].op, f.steps[0].op),
        (t.steps[2].op, f.steps[1].op),
    ]
    rng = np.random.default_rng(0)
    A = rng.standard_normal((512, E)).astype(bfloat16)
    x, w = (rng.standard_normal(E).astype(bfloat16) for _ in range(2))
    norm = RMSNorm(rows=1, tile_size=E, weighted=True)
    want = GEMV(M=512, K=E).reference(A, norm.reference(x.reshape(1, E), w).reshape(E))
    op = f.steps[0].op
    (got,) = op._call_reference({"A": A, "B": x, "prepare0_weight": w}).values()
    np.testing.assert_array_equal(got, want)


def test_a_norm_folds_with_its_input_as_the_tile_not_its_weight(npu2):
    # The weight is multiplied in after the first call has overwritten the tile.
    weighted = RMSNorm(rows=1, tile_size=E, weighted=True)
    with pytest.raises(ValueError, match="names weight, the line the first overwrites"):
        GEMV(M=512, K=E).prefold(weighted, at=1).resolved(npu2)
    t = _Project().trace(x=(1, E), r=(1, E))
    (fold,) = folded(t, npu2)[1]
    assert not folded(t, npu2, without=(fold,))[1]


def test_a_norm_read_beside_the_matvecs_stays(npu2):
    t = _Project(shared=True).trace(x=(1, E), r=(1, E))
    assert not any(isinstance(fold, Prologue) for fold in folded(t, npu2)[1])


def test_a_prologue_chains_through_the_step_before_it(npu2):
    t = _Project(heads=1, residual=True).trace(x=(1, E), r=(1, E))
    f, count = folded(t, npu2)
    first, chain = count
    assert [str(fold) for fold in count] == [
        "RMSNorm into GEMV",
        "ElementwiseAdd, then RMSNorm into GEMV",
    ]
    (step,) = f.steps
    fused = step.op.resolved(npu2)
    assert [type(link.op) for link in fused.prepare] == [ElementwiseAdd, RMSNorm]
    assert [h.name for h in step.inputs] == ["ws.0", "x", "r", "norm"]
    # A prologue of a chain brings the prologues after it; the last comes alone.
    assert folded(t, npu2, (chain,))[1] == count
    assert list(folded(t, npu2, (first,))[1]) == [first]
    rng = np.random.default_rng(0)
    A = rng.standard_normal((512, E)).astype(bfloat16)
    x, r, w = (rng.standard_normal(E).astype(bfloat16) for _ in range(3))
    s = ElementwiseAdd(size=E).reference(x, r)
    h = RMSNorm(rows=1, tile_size=E, weighted=True).reference(s.reshape(1, E), w)
    want = GEMV(M=512, K=E).reference(A, h.reshape(E))
    op = step.op
    (got,) = op._call_reference(
        dict(zip([i.name for i in op.inputs], (A, x, r, w)))
    ).values()
    np.testing.assert_array_equal(got, want)


def test_a_matvec_whose_columns_are_given_resolves_with_no_device():
    """What ``resolved()`` asks on a host with none bound: no memory to
    hold the cores to, so none is checked.
    """
    op = GEMV(M=256, K=64, num_aie_columns=1, num_channels=1, tile_size_output=32)
    assert op.resolve(None).tile_size_input == 2


def test_a_prologue_the_matvec_cannot_hold_is_refused(npu2):
    # A K of 8192: A's tiles, B's line and the prepared line fill L1.
    with pytest.raises(ValueError, match="past its 65536"):
        GEMV(M=2048, K=H).prefold(RMSNorm(rows=1, tile_size=H)).resolved(npu2)
    # Batched, a core takes a line per batch, beside which no weight streams.
    batched = GEMV(M=256, K=128, num_batches=4)
    batched.prefold(RMSNorm(rows=1, tile_size=128)).resolved(npu2)
    with pytest.raises(Unresolvable, match="inputs stream in beside one"):
        batched.prefold(RMSNorm(rows=1, tile_size=128, weighted=True)).resolved(npu2)
    # GEMM prepares no input.
    assert GEMM(M=256, K=E, N=512).prefold(RMSNorm(rows=256, tile_size=E)) is None


def test_two_spellings_of_one_array_are_one_design():
    """Identity is taken after resolution: a tunable left to resolve and the same
    tunable given its resolved value name one array, and a sequence builds it
    once. Every operator of a traced graph goes through the same point, so
    the design counts here are the gate on it.
    """
    a = GEMV(M=64, K=256, num_aie_columns=2, tile_size_input=2)
    b = GEMV(M=64, K=256, num_aie_columns=2, tile_size_input=2, tile_size_output=2)
    assert a.design_key() != b.design_key()  # as given
    seq = OperatorSequence(
        TracedGraph.of_steps(
            "two_spellings",
            [
                SequenceStep(a, (BufferRef("x"), BufferRef("w"), BufferRef("y"))),
                SequenceStep(b, (BufferRef("x2"), BufferRef("w"), BufferRef("z"))),
            ],
            ["x", "x2", "w"],
            ["z"],
        )
    )
    seq.prepare()
    designs, _ = seq.unique_designs()
    assert len(designs) == 1 and designs[0].tile_size_output == 2
    ffn, _ = _ffn()
    seq = OperatorSequence(ffn.trace(x=(1, E)))
    seq.prepare()
    assert len(seq.unique_designs()[0]) == 6


def test_swiglu_over_a_sequence_reads_the_weights_column_major():

    t = FeedForward(z(H, E), z(H, E), z(E, H)).trace(x=(256, E))
    gemms = [s.op for s in t.steps if type(s.op) is FLMGEMM]
    assert [(g.M, g.K, g.N) for g in gemms] == [(256, E, H), (256, E, H), (256, H, E)]
    assert all(g.b_col_maj for g in gemms)
    assert gemms[0].array_key() == gemms[1].array_key()
    silu = next(s.op for s in t.steps if type(s.op) is SiLU)
    assert silu.size == 256 * H


# --------------------------------------------------------------------------
# llama decode, traced at a scaled-down configuration
# --------------------------------------------------------------------------


def test_llama_decode_traces_and_tunes():

    L = 256
    model = small(max_seq_len=L)
    cfg = model.config
    t = model.trace(**model.shapes()[0])
    # A token takes no tensor. It returns the logits and carries the token
    # it draws and the position after it.
    assert t.inputs == [] and [h.name for h in t.outputs] == ["out", "carry_token"]
    # One function, so every version takes every value; a token binds two.
    assert [v.name for v in t.values] == [
        "token",
        "position",
        "start",
        "rows",
        "rope_start",
    ]
    token, position = t.values[0], t.values[1]
    assert t.carry["position"] == Affine(position, 1, 1)
    assert {b.expression.value.name for b in t.bindings} == {"token", "position"}
    by_op = {id(b.op): b for b in t.bindings}
    embedding, angles = t.steps[0].op, t.steps[1].op
    assert by_op[id(embedding)].expression == Affine(token, cfg.hidden_size)
    assert by_op[id(angles)].expression == Affine(position, cfg.head_dim)
    draw = {b.member.name: b.expression for b in t.bindings if b.op is t.steps[-1].op}
    assert draw == {"row": Affine(position, 4), "at": Affine(position)}
    # The weights are named by the checkpoint; the caches are pinned state.
    assert "weights.model.layers.1.self_attn.q_proj.weight" in t.pinned
    assert "keys.0" in t.pinned
    assert t.pinned["keys.0"] == cfg.num_key_value_heads * L * cfg.head_dim * 2
    # Every MHA attends over the keys up to the position, its one query
    # packed by its heads.
    mhas = [s.op for s in t.steps if type(s.op) is MHA]
    assert all(op.kv_interleaved for op in mhas)
    assert len(mhas) == cfg.num_hidden_layers
    assert all(
        {k: e.name for k, e in op.bound_values.items()} == {"kv_valid": "position_p1"}
        for op in mhas
    )
    assert all(op.packed and op.kv_len == L for op in mhas)
    # The same array serves every layer's like projections.
    q_arrays = {
        s.op.array_key()
        for s in t.steps
        if type(s.op) is GEMV
        and s.op.M == cfg.num_attention_heads * cfg.head_dim
        and s.op.K == cfg.hidden_size
    }
    assert len(q_arrays) == 1
    # Every operator tunes and is compatible on an 8-column device.
    for op in t.operators:
        op.resolved(aie_utils.get_current_device())
    # The profile gave the tiles decode was tuned with: half a head per
    # projection tile, a column's share of the row for the output
    # projection, a pipeline per KV head, one core for the norm.
    E, D = cfg.hidden_size, cfg.head_dim
    gemvs = [s.op for s in t.steps if type(s.op) is GEMV]
    q, k, v, o, gate, up, down = gemvs[:7]
    assert (q.tile_size_output, k.tile_size_output, o.tile_size_output) == (
        D // 2,
        D // 2,
        E // 8,
    )
    assert (down.tile_size_input, gate.tile_size_output) == (
        1,
        cfg.intermediate_size // 8,
    )
    assert mhas[0].num_pipelines == cfg.num_key_value_heads
    assert (
        next(
            s.op for s in t.steps if type(s.op) is RMSNorm and s.op.weighted
        ).num_aie_columns
        == 1
    )


def test_llama_decode_folds_its_norms_into_the_projections(npu2):
    model = small(max_seq_len=256)
    t = model.trace(**model.shapes()[0])
    f, count = folded(t, npu2)
    # Per layer: the attention norm into q, k and v, the feed-forward's into
    # gate and up, its product into down and the attention's residual into
    # o; the first layer's last residual into its down, the second's and
    # the final norm into the head; the rotated key and the value written
    # into their caches by the steps that make them.
    assert sorted((str(fold), n) for fold, n in count.items()) == [
        ("Copy into the drain of GEMV", 2),
        ("Copy into the drain of RoPE", 2),
        ("ElementwiseAdd (input 1) into GEMV", 1),
        ("ElementwiseAdd (input 1) into GEMV", 2),
        ("ElementwiseAdd, then RMSNorm into GEMV", 1),
        ("ElementwiseMul into GEMV", 2),
        ("RMSNorm into GEMV", 1),
        ("RMSNorm into GEMV, GEMV", 2),
        ("RMSNorm into GEMV, GEMV, GEMV", 2),
        ("SiLU, then ElementwiseMul into GEMV", 2),
    ]
    assert (len(t.steps), len(f.steps)) == (41, 24)
    assert not any(type(s.op) is RMSNorm for s in f.steps)
    row = model.config.num_key_value_heads * model.config.head_dim
    placed = {
        str(h.ref()): (
            s.op.placements,
            {k: e.name for k, e in s.op.bound_values.items()},
        )
        for s in f.steps
        for h in s.outputs
        if s.op.placements
    }
    rows = model.config.max_seq_len * row
    assert placed == {
        f"{cache}.{i}": (((name, rows, 0),), {f"{name}_offset": f"position_x{row}"})
        for i in range(2)
        for cache, name in (("keys", "y"), ("values", "C"))
    }


def test_llama_prompt_keeps_its_bounded_cache_writes(npu2):
    model = small(max_seq_len=256)
    t = model.trace(**model.shapes()[1])
    f, count = folded(t, npu2)
    assert not any(isinstance(fold, Place) for fold in count)
    assert sum(type(s.op) is Copy for s in f.steps) == sum(
        type(s.op) is Copy for s in t.steps
    )


def test_llama_prompt_traces_over_the_same_caches():

    g = small()
    cfg = g.config
    t = g.trace(**g.shapes()[1])
    assert [h.name for h in t.inputs] == ["ids"] and [h.name for h in t.outputs] == [
        "out",
        "carry_token",
    ]
    assert [v.name for v in t.values] == [
        "token",
        "position",
        "start",
        "rows",
        "rope_start",
    ]
    # MHA attends over the caches up to the chunk's last token.
    mha = next(s.op for s in t.steps if type(s.op).__name__ == "MHA")
    assert {k: e.name for k, e in mha.bound_values.items()} == {
        "valid": "rows",
        "kv_valid": "position_p1",
    }
    # The caches are the states a token's version reads: the same objects,
    # so one arena holds them once for both.
    token = g.trace(**g.shapes()[0])
    assert set(t.states) == set(token.states)
    assert t.residents["keys.0"] == token.residents["keys.0"]
    assert set(t.weights) == set(token.weights)
    # Every projection reads the (out, in) checkpoint layout through the
    # column-major flag, which the trace carries into shape inference.
    gemms = [s.op for s in t.steps if type(s.op) is FLMGEMM]
    assert all(op.b_col_maj for op in gemms)
    K = {op.K for op in gemms}
    assert K == {
        cfg.hidden_size,
        cfg.intermediate_size,
        cfg.num_attention_heads * cfg.head_dim,
    }
    for op in t.operators:
        op.resolved(aie_utils.get_current_device())


@pytest.mark.parametrize("device", ["npu1", "npu2"])
def test_llama_prompt_projects_with_flm_gemm(device, request):
    dev = request.getfixturevalue(device)
    g = llama_1b(num_hidden_layers=1)
    t = g.trace(**g.shapes()[1])
    ops = [s.op for s in t.steps]
    assert not any(type(op) is GEMM for op in ops)
    gemms = [op for op in ops if type(op) is FLMGEMM]
    assert len(gemms) == 7
    for op in gemms:
        assert op.b_col_maj and op.epilogue_modes == (Epilogue.NONE,)
        assert {k: e.name for k, e in op.bound_values.items()} == {"valid": "rows"}
        resolved = op.resolved(dev)
        assert resolved.B.shape == (op.N, op.K) and not resolved.bfp16_b


class Pointwise(iron.Graph):
    """A 1x1 convolution's pixels projected, K and N of 16."""

    def __init__(self, precision: Precision | None):
        self.precision = precision

    def body(self, x, w):
        return F.linear(x, w, k_tile=16, tile_n=16, precision=self.precision)


@pytest.mark.parametrize("precision,macs", [(None, True), (Precision.HIGH, False)])
def test_project_asks_flm_gemm_for_bf16_macs(precision, macs, npu2):
    t = Pointwise(precision).trace(x=((256, 16), bfloat16), w=((16, 16), bfloat16))
    (op,) = [op for op in t.operators if type(op) is FLMGEMM]
    assert op.resolved(npu2).emulate_bf16_mmul_with_bfp16 is macs


class Projections(iron.Graph):
    """A projection at the profile's precision, one held at HIGHEST, and
    one instance applied."""

    def __init__(self):
        self.gemm = GEMM(M=256, K=256, N=256)

    def body(self, x, w):
        y = GEMM.step(x, w)
        y = GEMM.step(y, w, precision=Precision.HIGHEST)
        return self.gemm.apply(y, w)


@pytest.mark.parametrize(
    "floor, levels",
    [
        (None, ["medium", "highest", "medium"]),
        ("high", ["high", "highest", "high"]),
        ("highest", ["highest"] * 3),
    ],
)
def test_a_graph_s_precision_raises_every_step_that_rounds_more(floor, levels):
    graph = Projections()
    graph.precision = floor
    t = graph.trace(x=((256, 256), bfloat16), w=((256, 256), bfloat16))
    assert [s.op.precision for s in t.steps] == levels
    assert graph.gemm.precision == Precision.MEDIUM


def test_a_profile_gives_a_precision_the_tuner_does_not_search(tmp_path, npu2):
    path = tmp_path / "npu2.json"
    path.write_text(
        '{"entries": [{"operator": "flm.GEMM", "K": 512, "precision": "high"}]}'
    )
    op = Profile.load(path).make(FLMGEMM, M=256, K=512, N=256)
    assert op.precision is Precision.HIGH
    assert not op.resolved(npu2).emulate_bf16_mmul_with_bfp16
    assert "precision" not in op.resolved(npu2)._domains(npu2)


def test_llama_prompt_bounds_every_flm_gemm_by_its_rows(npu2):
    """Each projection of a prompt chunk derives two per-call words from its
    rows, the 256-row units they reach and that less one, A's repeat count,
    and every projection shares them.
    """
    g = llama_1b(num_hidden_layers=2)
    t = g.trace(**g.shapes()[1])
    words, shared = _words(t, share=True)
    assert len(words) <= 32
    gemms = [op.resolved(npu2) for op in t.operators if type(op) is FLMGEMM]
    names = {"units_valid", "units_repeat"}
    symbols = set()
    for op in gemms:
        assert {v.name for v in op.values} == names | {"valid"}
        for name in names:
            symbol = op.value(name).symbol
            symbols.add(shared.get(symbol, symbol))
        for rows, reached in ((1, 1), (15, 1), (256, 1), (257, 2), (2048, 8)):
            assert op.derived_at("units_valid", valid=rows) == reached
            assert op.derived_at("units_repeat", valid=rows) == reached - 1
    assert len(symbols) == len(names)


@pytest.mark.parametrize("step", ["decode", "prompt"])
def test_llama_does_not_grow_with_the_context(step):
    """``max_seq_len`` sizes the caches, the RoPE table and the draws a
    position each and nothing else a decode step or a prompt chunk runs: a
    chunk's one input is its token ids (a step's token is a value),
    every activation and every array is the same at a four times longer
    context, and attention is the caches' two writes and MHA, the reshapes
    and transposes between them views the DMA walks.
    """

    def trace(max_seq_len):
        g = small(max_seq_len=max_seq_len)
        return g.trace(**g.shapes()[0 if step == "decode" else 1])

    short, long = trace(256), trace(1024)
    assert (
        [h.name for h in short.inputs]
        == [h.name for h in long.inputs]
        == ([] if step == "decode" else ["ids"])
    )
    grown = {name for name, n in long.pinned.items() if short.pinned[name] != n}
    caches = {"keys.0", "keys.1", "values.0", "values.1"}
    assert grown == {"rope", "draws", "drawn"} | caches

    def activations(t):
        return {
            h.ref(): h.nbytes
            for s in t.steps
            for h in s.inputs + s.outputs
            if h.role not in ("weight", "state")
        }

    assert activations(short) == activations(long)
    assert [op.array_key() for op in short.operators] == [
        op.array_key() for op in long.operators
    ]
    kinds = [type(s.op).__name__ for s in long.steps]
    rotations = [i for i, kind in enumerate(kinds) if kind == "RoPE"][1::2]
    mhas = [i for i, kind in enumerate(kinds) if kind == "MHA"]
    assert len(rotations) == len(mhas) == 2
    for rope, mha in zip(rotations, mhas):
        assert kinds[rope + 1 : mha + 1] == ["Copy", "Copy", "MHA"]


def _resolved_fields(settings):
    """Every field of every step of every setting, resolved for its device.

    A setting is ``(device, trace)``: ``trace`` builds the graph with that
    device current and traces it. The device is restored afterwards.
    """
    out = []
    for dev, trace in settings:
        with aie_utils.set_current_device(dev):
            out.append(
                [
                    tuple((f.name, vars(op)[f.name]) for f in dataclasses.fields(op))
                    + (op.design_key(),)
                    for s in trace().steps
                    for op in [s.op.resolved(dev)]
                ]
            )
    return out


def _every_keyword_is_load_bearing(monkeypatch, settings):
    """Drop each keyword the graphs pass, one (class, name) at a time; each
    must change some resolved step, or fail, in some setting. A keyword that
    resolution would have picked anyway is noise a reader has to disprove.
    """
    construct = Tracer._construct
    passed = set()

    def recording(self, cls, inputs, outputs, kwargs):
        passed.update((cls, name) for name in kwargs)
        return construct(self, cls, inputs, outputs, kwargs)

    monkeypatch.setattr(Tracer, "_construct", recording)
    baseline = _resolved_fields(settings)
    redundant = []
    for cls, name in sorted(passed, key=lambda k: (k[0].__name__, k[1])):

        def dropping(self, kls, inputs, outputs, kwargs, cls=cls, name=name):
            if kls is cls:
                kwargs = {k: v for k, v in kwargs.items() if k != name}
            return construct(self, kls, inputs, outputs, kwargs)

        monkeypatch.setattr(Tracer, "_construct", dropping)
        try:
            same = _resolved_fields(settings) == baseline
        except Exception:
            continue
        if same:
            redundant.append(f"{cls.__name__}({name}=)")
    assert not redundant, f"resolution picks these anyway: {redundant}"


def test_llama_names_only_the_tunables_that_matter(monkeypatch):
    """Every keyword the llama graph passes is a choice resolution would not
    have made in some setting the graph is written for: the model's real
    shape at the graph's own defaults, on NPU2 (MHA's) for a decode step and
    a prompt; and the scaled-down shape the host tests trace, with the
    parameters that shape needs.
    """
    npu2 = from_name("npu2", n_cols=8)
    real, scaled = llama_1b(num_hidden_layers=1), small()
    settings = [
        (npu2, lambda: real.trace(**real.shapes()[0])),
        (npu2, lambda: real.trace(**real.shapes()[1])),
        (npu2, lambda: scaled.trace(**scaled.shapes()[1])),
    ]
    _every_keyword_is_load_bearing(monkeypatch, settings)


def test_a_bound_value_survives_tuning():
    copy = Copy(input_buffer_size=64, output_buffer_size=64)

    class F(iron.Graph):
        def body(self, x, *, a: Scratchpad[np.int32]):
            return copy.apply(x, out_offset=a)

    f = F()

    f.trace(x=(64,))
    assert [v.name for v in copy.resolved(aie_utils.get_current_device()).values] == [
        "out_offset"
    ]


# --------------------------------------------------------------------------
# A bound on a handle: the first n of an axis are the valid ones this call
# --------------------------------------------------------------------------


def test_a_bound_travels_through_reshape_and_transpose():

    n = PerCall("n", Kind.SCRATCHPAD, np.int32)
    x = Handle((64, 8, 4), bfloat16, "x", "input")
    b = x[:n]
    assert b.shape == x.shape and b.bounds == {0: n.affine()} and b.tap is None
    assert b.reshape(512, 4).bounds == {0: n * 8}  # merged with the axis after it
    assert b.reshape(64 * 8 * 4).bounds == {0: n * 32}
    assert b.reshape(512, 4).reshape(64, 8, 4).bounds == {0: n.affine()}  # split back
    assert b.transpose(1, 0, 2).bounds == {1: n.affine()}
    with pytest.raises(ValueError, match="does not divide"):
        b.reshape(32, 16, 4)  # a leading axis no run of the others makes
    assert b[0].bounds == {} and b[0].shape == (8, 4)  # one row: no bound
    with pytest.raises(TypeError, match="bounded per call on axis 0"):
        b[0:2]
    with pytest.raises(ValueError, match="from its start"):
        x[2:n]
    v = b[:, 2:6]  # all of the bounded axis: the bound stays on it
    assert v.shape == (64, 4, 4) and v.bounds == {0: n.affine()}
    assert b[:, 3].bounds == {0: n.affine()} and b[:, 3].shape == (64, 4)


def test_per_call_values_are_integer_expressions():
    """Integer arithmetic on a per-call value is an ``Affine`` of it,
    which a binding writes and names its word by.
    """
    p = PerCall("p", Kind.SCRATCHPAD, np.int32)
    assert (p + 1) * 64 == Affine(p, 64, 64) == 64 * (1 + p)
    assert (p - 1).evaluate({"p": 5}) == 4 and (p * 3 + 2).evaluate({"p": 5}) == 17
    assert [e.name for e in (p.affine(), p * 64, (p + 1) * 64, p - 1)] == [
        "p",
        "p_x64",
        "p_x64_p64",
        "p_m1",
    ]
    assert str((p + 1) * 64) == "p * 64 + 64"
    with pytest.raises(TypeError):
        _ = p * 0.5
    cache = Handle((8, 4), bfloat16, "cache", "state")
    # An index may floor; a bound, which patches a length, may not.
    assert cache[(p + 1) // 2].index_by == (p + 1) // 2 * 4
    with pytest.raises(TypeError, match="not linear"):
        _ = cache[: (p + 1) // 2]
    assert 10 - p == Affine(p, -1, 10) and -p == Affine(p, -1)
    assert (p * 4) // 2 == p // 1 * 2 and p // 2 == Affine(p, 1, 0, 1)
    arithmetic = {"__add__", "__sub__", "__mul__", "__radd__", "__rmul__"}
    arithmetic |= {"__rsub__", "__neg__", "__floordiv__"}
    assert arithmetic <= set(vars(Affine)) and arithmetic <= set(vars(PerCall))


def test_a_clamped_expression_carries_its_range_through_integer_arithmetic():
    """``clamp`` holds an expression to a range; a sum, a product (a negative
    one swapping the bounds) and a floor division by a power of two carry
    it, each as numpy computes it at every value tried. An index may be
    clamped; a bound, which patches a length, may not."""
    p = PerCall("p", Kind.SCRATCHPAD, np.int32)
    start = (p - 3).clamp(lo=0)
    assert start.name == "p_m3_lo0" and str(start) == "clamp(p - 3, 0, None)"
    cases = {
        start: lambda v: max(v - 3, 0),
        start + 5: lambda v: max(v - 3, 0) + 5,
        start * -2: lambda v: -2 * max(v - 3, 0),
        (p + 1).clamp(hi=9) // 4: lambda v: min(v + 1, 9) // 4,
        ((p * 3 + 1) // 2).clamp(lo=-4, hi=20) * 3
        + 1: lambda v: 3 * min(max((3 * v + 1) // 2, -4), 20)
        + 1,
        (p - 3).clamp(lo=0).clamp(lo=-5, hi=6): lambda v: min(max(v - 3, 0), 6),
    }
    for e, want in cases.items():
        assert [e.evaluate({"p": v}) for v in range(-20, 21)] == [
            want(v) for v in range(-20, 21)
        ], e
    with pytest.raises(TypeError, match="not linear"):
        start.affine()
    with pytest.raises(TypeError):
        _ = start + start
    with pytest.raises(TypeError):
        _ = start // 3
    with pytest.raises(ValueError, match="holds no value"):
        (p + 0).clamp(lo=5, hi=2)
    # A reference call gives the number itself.
    assert [iron.clamp(v, lo=0, hi=4) for v in (-2, 3, 9)] == [0, 3, 4]
    assert iron.clamp(p - 3, lo=0) == start
    cache = Handle((8, 4), bfloat16, "cache", "state")
    assert cache[start].index_by == start * 4
    with pytest.raises(TypeError, match="not linear"):
        _ = cache[: (p + 1).clamp(hi=8)]


def test_a_per_call_value_cannot_steer_the_trace():
    """A body is traced once for every call, so a branch on a per-call value
    would take one side for all of them: a comparison or a truth test raises.
    """

    class Branches(iron.Graph):
        def __init__(self, test):
            self.test = test

        def body(self, x, *, pos: Scratchpad[np.int32]):
            if self.test(pos):
                return ReLU.step(x)
            return ElementwiseAdd.step(x, x)

    for test in (
        lambda p: p == 0,
        lambda p: p + 1 == 1,
        lambda p: p + 1 == 1.0,
        lambda p: p * 2 != np.float32(2),
        bool,
        lambda p: p != 3,
    ):
        with pytest.raises(TypeError, match="per call"):
            Branches(test).trace(x=(64,))
    p = PerCall("p", Kind.SCRATCHPAD, np.int32)
    assert p == p and p != PerCall("p", Kind.SCRATCHPAD, np.int32) and p + 1 == p + 1
    assert len({p, p}) == 1 and len({p + 1, 1 + p}) == 1
    with pytest.raises(TypeError, match="not a number"):
        int(p)


def test_an_index_before_a_bound_keeps_the_bound_on_its_axis():
    """``cache.reshape(G, L // C, C, D)[:, chunk, :rows]`` drops the chunk
    axis: the bound is on axis 1 of the view, and the index an offset of
    whole chunks.
    """
    chunk = PerCall("chunk", Kind.SCRATCHPAD, np.int32)
    rows = PerCall("rows", Kind.SCRATCHPAD, np.int32)
    G, L, C, D = 2, 64, 16, 8
    cache = Handle((G, L // C, C, D), bfloat16, "cache", "state")
    v = cache[:, chunk, : rows + 1]
    assert v.shape == (G, C, D) and v.bounds == {1: rows + 1}
    assert v.index_by == chunk * (C * D)

    keys = iron.state((G, L, D), name="keys")

    class Chunked(iron.Graph):
        def body(self, x, *, chunk: Scratchpad[np.int32], rows: Scratchpad[np.int32]):
            k = x[:rows].reshape(C, G, D).transpose(1, 0, 2)
            Copy.step(k, keys.reshape(G, L // C, C, D)[:, chunk, :rows])

    t = Chunked().trace(x=(C, G * D))
    (copy,) = t.operators
    assert copy.dst_bound == 1 and {
        k: e.name for k, e in copy.bound_values.items()
    } == {
        "src_valid": "rows",
        "out_offset": f"chunk_x{C * D}",
        "dst_valid": "rows",
    }


def test_a_run_from_a_per_call_start_is_its_whole_chunk_s_view():
    """``x[c * 16 : c * 16 + 16][:rows]`` is the view of block ``c`` of
    ``x.reshape(4, 16, ...)[c, :rows]``: the same offset, pattern and bound.
    """
    chunk = PerCall("chunk", Kind.SCRATCHPAD, np.int32)
    rows = PerCall("rows", Kind.SCRATCHPAD, np.int32)
    cache = Handle((64, 2, 8), bfloat16, "cache", "state")
    a = cache[chunk * 16 : chunk * 16 + 16][:rows]
    b = cache.reshape(4, 16, 2, 8)[chunk, :rows]
    assert (a.shape, a.bounds, a.index_by, a.ref()) == (
        b.shape,
        b.bounds,
        b.index_by,
        b.ref(),
    )
    assert (a.tap.offset, a.tap.sizes, a.tap.strides) == (
        b.tap.offset,
        b.tap.sizes,
        b.tap.strides,
    )


def test_a_run_from_a_per_call_start_takes_any_start_on_any_axis():
    """A start that is no block's (``pos``), floored (``pos // 64 * 64``), on
    a leading or an inner axis: a view offset by the start's rows, its width
    fixed, bounded on the same axis.
    """
    pos = PerCall("pos", Kind.SCRATCHPAD, np.int32)
    rows = PerCall("rows", Kind.SCRATCHPAD, np.int32)
    cache = Handle((100, 2, 8), bfloat16, "cache", "state")
    v = cache[pos : pos + 16][:rows]
    assert v.shape == (16, 2, 8) and v.bounds == {0: rows.affine()}
    assert v.index_by == pos * 16
    floored = pos // 64 * 64
    assert cache[floored : floored + 64].index_by == floored * 16
    keys = Handle((2, 100, 8), bfloat16, "keys", "state")
    w = keys[:, pos : pos + 16][:, :rows]
    assert w.shape == (2, 16, 8) and w.bounds == {1: rows.affine()}
    assert w.index_by == pos * 8


@pytest.mark.parametrize(
    "key,error",
    [
        (lambda p, n: np.s_[p:], "fixed width"),
        (lambda p, n: np.s_[p : p + 101], "fixed width"),
        (lambda p, n: np.s_[p : n + 4], "fixed width"),
        (lambda p, n: (p, np.s_[p : p + 4]), "one axis at most"),
    ],
    ids=["no_stop", "wider_than_the_axis", "another_value", "two_per_call"],
)
def test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start(key, error):
    pos = PerCall("pos", Kind.SCRATCHPAD, np.int32)
    n = PerCall("n", Kind.SCRATCHPAD, np.int32)
    cache = Handle((100, 100), bfloat16, "cache", "state")
    with pytest.raises((IndexError, ValueError), match=error):
        cache[key(pos, n)]


def test_a_run_is_bounded_from_its_start_on_its_own_axis():
    pos = PerCall("pos", Kind.SCRATCHPAD, np.int32)
    rows = PerCall("rows", Kind.SCRATCHPAD, np.int32)
    run = Handle((100, 2, 8), bfloat16, "cache", "state")[pos : pos + 16]
    for key in (np.s_[2:rows], np.s_[:4], np.s_[:, :rows]):
        with pytest.raises(IndexError, match="bound its axis 0"):
            run[key]


def test_a_run_past_the_buffer_s_end_is_kept_inside_by_each_call():
    """100 rows, runs of 16: a call's start plus its bound, or with no bound
    the run's width, is checked to end within the buffer; so is the start.
    """

    class Bounded(iron.Graph):
        def body(self, x, *, pos: Scratchpad[np.int32], rows: Scratchpad[np.int32]):
            return Copy.step(x[pos : pos + 16][:rows])

    class Whole(iron.Graph):
        def body(self, x, *, pos: Scratchpad[np.int32]):
            return Copy.step(x[pos : pos + 16])

    def inside(t, **at):
        return all(m.lo <= m.evaluate(at) < m.hi for m in t.limits)

    t = Bounded().trace(x=(100, 16))
    assert inside(t, pos=96, rows=4) and inside(t, pos=0, rows=16)
    assert not inside(t, pos=96, rows=5) and not inside(t, pos=-1, rows=1)
    assert not inside(t, pos=0, rows=17)
    t = Whole().trace(x=(100, 16))
    assert inside(t, pos=84) and not inside(t, pos=85)


def test_a_run_from_a_per_call_start_is_written_and_read_as_numpy_does():
    """The reference of a write of ``rows`` rows from ``start`` and a read of
    them back, at starts no chunk's, one with its run past the end; and a
    bound past the end refused.
    """
    L, C, W = 100, 16, 8
    cache = iron.state((L, W), name="cache")

    class Write(iron.Graph):
        def body(self, x, *, start: Scratchpad[np.int32], rows: Scratchpad[np.int32]):
            Copy.step(x[:rows], cache[start : start + C][:rows])
            return Copy.step(cache[start : start + C][:rows])

    write = Write()
    expected = np.zeros((L, W), bfloat16)
    rng = np.random.default_rng(0)
    for start, rows in ((5, 16), (37, 3), (90, 10), (99, 1)):
        x = rng.standard_normal((C, W)).astype(bfloat16)
        expected[start : start + rows] = x[:rows]
        got = write.reference(x, start=start, rows=rows)
        np.testing.assert_array_equal(np.asarray(got), x[:rows])
        np.testing.assert_array_equal(cache.host, expected)
    with pytest.raises(IndexError, match="rows to 101 of 100"):
        write.reference(x, start=90, rows=11)


def test_the_trace_records_the_range_each_per_call_index_and_bound_holds():
    """A call checks these before it reaches the device, where an index past
    its view moves a transfer onto another buffer.
    """
    G, L, C, D = 2, 64, 16, 8
    keys = iron.state((G, L, D), name="keys")
    table = iron.state((L, D), name="table")

    class Chunked(iron.Graph):
        def body(
            self,
            x,
            *,
            chunk: Scratchpad[np.int32],
            rows: Scratchpad[np.int32],
            pos: Scratchpad[np.int32],
        ):
            k = x[:rows].reshape(C, G, D).transpose(1, 0, 2)
            Copy.step(k, keys.reshape(G, L // C, C, D)[:, chunk, :rows])
            return Copy.step(table[pos + 1]).reshape(1, D)

    t = Chunked().trace(x=(C, G * D))
    got = {(str(m.expression), m.lo, m.hi) for m in t.limits}
    assert got == {("rows", 0, C + 1), ("chunk", 0, L // C), ("pos + 1", 0, L)}
    for m in t.limits:
        assert m.expression.evaluate(dict(chunk=3, rows=C, pos=L - 2)) < m.hi
    (outside,) = [m for m in t.limits if str(m.expression) == "pos + 1"]
    assert outside.expression.evaluate(dict(pos=L - 1)) == outside.hi


def test_a_bound_rounds_up_to_the_tiles_it_ends_in(npu2):
    """A bound ending inside a tile takes the tile: the words of tiles per
    lane and the trip counts derived from it round up, so ``p + 1`` rows
    reach their last row; at a whole number of tiles nothing changes.
    """

    class G(iron.Graph):
        def body(self, x, y, *, p: Scratchpad[np.int32]):
            return ElementwiseAdd.step(x[: p + 1], y[: p + 1])

    t = G().trace(x=(64, 512), y=(64, 512))
    (op,) = t.operators
    op = op.resolved(aie_utils.get_current_device())
    per_word = op.cores * op.tile_size  # elements one word of tiles covers
    words = {w.symbol: w for w in _words(t)[0]}
    for p in range(64):
        elements = (p + 1) * 512
        tiles = -(-elements // per_word)
        assert words[f"{op.name}_valid_p_x512_p512"]({"p": p}) == elements
        assert words[f"{op.name}_count"]({"p": p}) == tiles
        assert words[f"{op.name}_valid_a"]({"p": p}) == tiles
        assert tiles * per_word >= elements and tiles * per_word <= 64 * 512


def test_words_with_an_offset_share_by_ratio_and_offset(npu2):
    """Symbols share a word when they are one ratio and one offset of a
    graph value; the word, rounded up, is each one's own number.
    """

    class G(iron.Graph):
        def body(self, x, y, *, p: Scratchpad[np.int32]):
            return ElementwiseMul.step(
                ElementwiseAdd.step(x[: p + 1], y[: p + 1]), y[: p + 1]
            )

    t = G().trace(x=(64, 512), y=(64, 512))
    alone, _ = _words(t)
    words, shared = _words(t, share=True)
    assert len(words) == 2
    assert sorted(set(shared.values())) == [
        "graph_p_x1d4p1d4_int32",
        "graph_p_x512p512_int32",
    ]
    for p in range(64):
        mine = {w.symbol: w({"p": p}) for w in words}
        for w in alone:
            assert mine[shared.get(w.symbol, w.symbol)] == w({"p": p})


def test_words_of_one_clamped_expression_share_it(npu2):
    """Two designs indexed by one clamped expression of a value share its
    word; rows of another width are another expression, their own word.
    """

    class G(iron.Graph):
        def __init__(self):
            self.a = iron.state((8, 32), np.int32)
            self.c = iron.state((8, 64), np.int32)

        def body(self, *, p: Scratchpad[np.int32]):
            row = iron.clamp(p - 3, lo=0)
            return tuple(
                Copy.step(view, dtype=np.int32)
                for view in (self.a[row], self.a[row, :16], self.c[row])
            )

    t = G().trace()
    alone, _ = _words(t)
    words, shared = _words(t, share=True)
    assert (len(alone), len(words)) == (3, 2)
    assert sorted(set(shared.values())) == ["graph_p_x32_m96_lo0_int32"]
    for p in range(8):
        mine = {w.symbol: w({"p": p}) for w in words}
        for w in alone:
            assert mine[shared.get(w.symbol, w.symbol)] == w({"p": p})


def test_the_reference_writes_a_given_output_of_an_operator_that_returns_one(npu2):
    """GEMM's reference takes its inputs and returns its result; given an
    output, the graph's reference writes that result into it.
    """

    class Into(iron.Graph):
        def body(self, x, a, b):
            y = ElementwiseAdd.step(x, x)
            GEMM.step(a, b, y[:256])
            return y

    rng = np.random.default_rng(0)
    x = rng.integers(-4, 4, (512, 256)).astype(bfloat16)
    a = rng.integers(-2, 2, (256, 256)).astype(bfloat16)
    b = rng.integers(-2, 2, (256, 256)).astype(bfloat16)
    y = np.asarray(Into().reference(x, a, b))
    f = np.float32
    np.testing.assert_array_equal(y[:256], (a.astype(f) @ b.astype(f)).astype(bfloat16))
    np.testing.assert_array_equal(y[256:], x[256:] * 2)


@pytest.mark.parametrize("view", [False, True])
def test_a_weight_given_where_an_optional_input_was_meant_is_refused(view):
    """``RMSNorm(x, w)`` gives the weight as RMSNorm's output: a trace and
    the reference refuse it, naming the keyword, whatever view of it, and
    the reference leaves the weight as it was.
    """
    w = np.arange(E).astype(bfloat16)

    class Norm(iron.Graph):
        def __init__(self):
            self.w = w

        def body(self, x):
            return RMSNorm.step(x, self.w.reshape(1, E) if view else self.w)

    x = np.ones((1, E), dtype=bfloat16)
    kept = w.copy()
    with pytest.raises(TypeError, match=r"graph weight or a view of one.*\(weight=\)"):
        Norm().trace(x=(1, E))
    with pytest.raises(TypeError, match=r"graph weight or a view of one.*\(weight=\)"):
        Norm().reference(x)
    np.testing.assert_array_equal(w, kept)


def test_an_input_given_as_an_output_is_refused():
    class Over(iron.Graph):
        def body(self, x, y):
            ReLU.step(x, y[1:])
            return y

    with pytest.raises(TypeError, match="graph input or a view of one"):
        Over().trace(x=(E - 1,), y=(E,))
    y = np.ones(E, dtype=bfloat16)
    with pytest.raises(TypeError, match="graph input or a view of one"):
        Over().reference(np.ones(E - 1, dtype=bfloat16), y)
    assert (y == 1).all()


def test_a_given_output_of_another_rank_is_refused_unless_declared_flat():
    """A class call infers from the ranks and refuses; a built operator's
    call is checked as it records.
    """
    gemm = GEMM(M=256, K=256, N=256)

    class Flat(iron.Graph):
        def body(self, a, b):
            y = ElementwiseAdd.step(a.reshape(256 * 256), a.reshape(256 * 256))
            gemm.apply(a, b, y)
            return y

    with pytest.raises(ValueError, match=r"GEMM.C is \(256, 256\)"):
        Flat().trace(a=(256, 256), b=(256, 256))


def test_a_column_major_product_is_read_as_stored_by_the_next_reference(npu2):
    """A ``c_col_maj`` GEMM's C is ``(N, M)`` as stored, which an elementwise
    operator's reference takes as lines of its own length.
    """

    class Transposed(iron.Graph):
        def body(self, a, b):
            return ReLU.step(GEMM.step(a, b, b_col_maj=True, c_col_maj=True))

    rng = np.random.default_rng(0)
    a = rng.integers(-2, 2, (32, 256)).astype(bfloat16)
    b = rng.integers(-2, 2, (2048, 256)).astype(bfloat16)
    y = np.asarray(Transposed().reference(a, b), np.float32)
    c = b.astype(np.float32) @ a.astype(np.float32).T
    np.testing.assert_array_equal(y, np.maximum(c, 0))


def test_a_float32_product_is_not_rounded_to_its_inputs_dtype(npu2):
    class Wide(iron.Graph):
        def body(self, a, b):
            return GEMM.step(a, b, dtype_out=np.float32, tile_m=32)

    rng = np.random.default_rng(0)
    a = rng.standard_normal((256, 256)).astype(bfloat16)
    b = rng.standard_normal((256, 512)).astype(bfloat16)
    y = np.asarray(Wide().reference(a, b))
    c = a.astype(np.float32) @ b.astype(np.float32)
    assert y.dtype == np.float32
    np.testing.assert_array_equal(y, c)
    assert (c != c.astype(bfloat16).astype(np.float32)).any()


def test_the_reference_computes_the_expressions(npu2):
    """The reference runs the body on numbers: ``p + 1`` is the row the
    copy writes, as the device's offset word is.
    """
    keys = iron.state((2, 8, 4), name="keys")

    class Write(iron.Graph):
        def body(self, x, *, p: Scratchpad[np.int32]):
            Copy.step(x, keys[:, p + 1])

    g = Write()
    t = g.trace(x=(2, 4))
    (b,) = t.bindings
    assert b.expression == (t.values[0] + 1) * 4  # a row of the cache is 4 long
    x = np.arange(8, dtype=np.float32).astype(bfloat16).reshape(2, 4)
    g.reference(x, p=2)
    assert keys.host is not None
    assert (keys.host[:, 3] == x).all() and not keys.host[:, :3].any()


def test_the_words_a_call_writes_come_from_the_bound(npu2):
    """Each bound value is a word, and so is every value an operator derives
    from a bounded extent, computed by the operator from the call's bound.
    """

    class G(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return Rows.step(x[:n].reshape(64 * 8, 1))  # rows x 8 seen as rows*8 x 1

    g = G()

    t = g.trace(x=(64, 8))
    (op,) = t.operators
    words = {w.symbol: w for w in _words(t)[0]}
    assert set(words) == {
        f"{op.name}_{w}" for w in ("valid_n_x8", "count", "valid_x", "valid_y")
    }
    call = {"n": 16}
    assert words[f"{op.name}_valid_n_x8"](call) == 16 * 8  # the reshape's scale
    assert words[f"{op.name}_count"](call) == 16 * 8 // 2  # derived: valid // lanes
    assert words[f"{op.name}_valid_x"](call) == 16 * 8 // 2  # tiles per lane
    # A full ELF's designs read the bound only through what they derive.
    elf = {w.symbol for w in _words(t, extents=False)[0]}
    assert elf == set(words) - {f"{op.name}_valid_n_x8"}
    for w in words.values():  # and each is what its Emit row computes
        assert w.form is not None and w.form.evaluate(call) == w(call)


def test_integer_arithmetic_on_an_expression_is_an_expression():
    """Sums, products, floor divisions and remainders by powers of two (so
    ``ceildiv``) of an expression are expressions that compute the same, and
    so are sums of two linear ones in its value; anything else is refused.
    """
    x = Affine(PerCall("x", Kind.SCRATCHPAD, np.int32), 3, -5)
    y = Affine(PerCall("y", Kind.SCRATCHPAD, np.int32))
    cases = [
        (lambda v: v + 7, None),
        (lambda v: 2 - v, None),
        (lambda v: v * -4, None),
        (lambda v: v // 8, None),
        (lambda v: v // -4, None),
        (lambda v: ceildiv(v, 64), None),
        (lambda v: (ceildiv(v, 64) + 1) * 32, None),
        (lambda v: (v // 4 + 3) // 16, None),  # nested floors fold into one
        (lambda v: (v // 4) * 8 // 2 - 1, None),  # an exact division
        (lambda v: (v * 512) // 512, None),  # linear again
        (lambda v: ceildiv(v * 4, 256), None),
        (lambda v: v * 3 + v + 1, None),
        (lambda v: v * 4 - v, None),
        (lambda v: v - v, None),  # the value cancels: a number
        (lambda v: (v * 4) // v, None),
        (lambda v: v // 3, TypeError),
        (lambda v: (v // 4) * 3 // 2, TypeError),
        (lambda v: v // 1 if v else 0, TypeError),
        (lambda v: v % 64, None),  # a power of two: a ring's row
        (lambda v: v % 48, TypeError),
        (lambda v: v < 0, TypeError),
        (lambda v: v + y, TypeError),
        (lambda v: v // 4 + v, TypeError),
        (lambda v: (v + 1) // v, TypeError),
        (lambda v: v // (v * 2), TypeError),
    ]
    for f, error in cases:
        if error is not None:
            with pytest.raises(error):
                f(x)
            continue
        form = f(x)
        for v in range(-300, 300):
            u = 3 * v - 5
            if isinstance(form, int):
                assert f(u) == form, v
                continue
            assert form.value is x.value
            assert form.evaluate({"x": v}) == f(u), v


def test_the_packed_decode_words_of_mha_have_emit_forms(npu2):
    """One query attending over a span of the cache: every word the full
    ELF's MHA reads, ``ceildiv``s of the span among them, is an Emit row.
    """

    class G(iron.Graph):
        def __init__(self):
            self.keys = iron.state((8, 2048, 64))
            self.values = iron.state((8, 2048, 64))

        def body(self, q, *, position: Scratchpad[np.int32]):
            span = np.s_[:, : position + 1]
            o = MHA.step(
                q.reshape(1, 32, 64),
                self.keys[span],
                self.values[span],
                heads_interleaved=True,
            )
            return o.reshape(1, 32 * 64)

    words, _ = _words(G().trace(q=(32, 64)), extents=False)
    assert words
    for w in words:
        assert w.form is not None and w.form.value.name == "position", w.symbol
        for position in range(2048):
            at = {"position": position}
            assert w.form.evaluate(at) == w(at), w.symbol


def test_a_bound_on_rows_reaches_a_flat_buffer_in_elements(npu2):
    """``x[:n]`` of a (64, 512) handle into a flat elementwise buffer bounds
    it to ``n * 512`` elements, not ``n``.
    """

    class G(iron.Graph):
        def body(self, x, y, *, n: Scratchpad[np.int32]):
            return ElementwiseAdd.step(x[:n], y[:n])

    g = G()

    t = g.trace(x=(64, 512), y=(64, 512))
    (b,) = t.bindings
    assert (b.member.name, b.expression) == ("valid", t.values[0] * 512)


def test_words_that_always_hold_one_number_share_it(npu2):
    """On a full ELF, two designs bound to one graph value write one word
    for each ratio of it they read (their extents; the tiles per lane of
    each operand), and every symbol that shares a word reads its own value
    there. A derivation the library sees through (``count``, a ceiling
    division) shares the word of the ratio it computes.
    """

    class G(iron.Graph):
        def body(self, x, y, *, n: Scratchpad[np.int32]):
            return ElementwiseMul.step(ElementwiseAdd.step(x[:n], y[:n]), y[:n])

    g = G()

    t = g.trace(x=(64, 512), y=(64, 512))
    alone, _ = _words(t)
    words, shared = _words(t, share=True)
    assert len(alone) == 10 and len(words) == 2
    assert sorted(set(shared.values())) == ["graph_n_x1d4_int32", "graph_n_x512_int32"]
    for n in (1, 16, 64):
        mine = {w.symbol: w({"n": n}) for w in words}
        for w in alone:
            assert mine[shared.get(w.symbol, w.symbol)] == w({"n": n})


def test_a_bound_reaches_a_copy_and_a_repeat_through_their_views(npu2):
    """``x[:n]`` reshaped and transposed lands on axis 1 of the copy's source
    walk; ``keys[:, :n]`` on axis 1 of its destination; ``keys[:, :c]`` on the
    stack axis of a Repeat, whose output carries the bound on.
    """
    G, D, L = 4, 8, 32  # traced at the cache's full length, as a prompt is
    keys = iron.state((G, L, D), name="keys")

    class Cached(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32], c: Scratchpad[np.int32]):
            k = x[:n].reshape(L, G, D).transpose(1, 0, 2)
            Copy.step(k, keys[:, :n])
            return Repeat.step(keys[:, :c], repeat=2)

    g = Cached()

    t = g.trace(x=(L, G * D))
    copy, rep = t.operators
    assert copy.src_bound == 1 and copy.dst_bound == 1
    assert {k: e.name for k, e in copy.bound_values.items()} == {
        "src_valid": "n",
        "dst_valid": "n",
    }
    assert {k: e.name for k, e in rep.bound_extents.items()} == {"valid_seq": "c"}
    n, c = t.values
    assert [(b.member.name, b.expression) for b in t.bindings] == [
        ("src_valid", n.affine()),
        ("dst_valid", n.affine()),
        ("valid_seq", c.affine()),
    ]
    (out,) = t.outputs
    assert out.shape == (2 * G, L, D) and out.bounds == {1: t.values[1].affine()}
    rep = rep.resolved(aie_utils.get_current_device())
    assert rep.derived_at("valid_seq_x", valid_seq=12) == 12  # the stack axis itself


def test_a_bound_on_one_side_of_a_copy_holds_the_other(npu2):
    """A copy of ``x[:n]`` by head makes an output of the view's shape bounded
    alike, and into a given view of that shape bounds it on the same axis; a
    side moving every row would wait on rows the other never moves. A given
    view of another shape cannot follow the bound, and is refused.
    """
    G, D, L = 4, 8, 32
    keys = iron.state((G, L, D), name="keys")

    class ByHead(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            k = x[:n].reshape(L, G, D).transpose(1, 0, 2)
            Copy.step(k, keys)
            return Copy.step(k)

    t = ByHead().trace(x=(L, G * D))
    (n,) = t.values
    for copy in t.operators:
        assert copy.src_bound == 1 and copy.dst_bound == 1
        assert {k: e.name for k, e in copy.bound_values.items()} == {
            "src_valid": "n",
            "dst_valid": "n",
        }
    assert list(t.operators[1].dst.sizes) == [G, L, D]
    (out,) = t.outputs
    assert out.shape == (G, L, D) and out.bounds == {1: n.affine()}

    class Flat(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            Copy.step(x[:n].reshape(L, G, D).transpose(1, 0, 2), keys.reshape(G * L, D))

    with pytest.raises(ValueError, match="bound it alike"):
        Flat().trace(x=(L, G * D))


def test_the_reference_copies_a_bounded_call_into_the_rows_it_covers(npu2):
    """The trace bounds a given view alike (above); the reference, which runs
    a bounded call on the rows it covers, writes those of the view and
    leaves the rest.
    """
    R, L, C = 16, 4, 256
    cache = iron.state((R, L, C), name="cache")

    class G(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32], pos: Scratchpad[np.int32]):
            y = Softmax.step(x[:, :n])
            Copy.step(y, cache[:, pos])
            return y

    rng = np.random.default_rng(0)
    x = rng.standard_normal((R, C)).astype(bfloat16)
    cache.host = rng.standard_normal((R, L, C)).astype(bfloat16)
    want = cache.host.copy()
    y = np.asarray(G().reference(x, n=100, pos=2))
    want[:, 2, :100] = y
    assert y.shape == (R, 100)
    assert np.array_equal(cache.host.view(np.uint16), want.view(np.uint16))


def test_gemm_bounds_its_compute_and_mha_its_compute_and_kv_traffic(npu2):
    """A bound reaches GEMM through A's rows and MHA through Q's padded
    length and K's and V's (select shapes): GEMM derives the counts its
    cores compute per call and keeps every descriptor; MHA derives its
    counts and the first query block, and patches its K and V descriptors'
    block count.
    """

    class G(iron.Graph):
        def body(self, x, w, *, n: Scratchpad[np.int32]):
            h = GEMM.step(x[:n], w, b_col_maj=True)  # (512, 64) x (256, 64)^T
            return MHA.step(
                h.reshape(512, 4, 64),
                h.reshape(512, 4, 64),
                h.reshape(512, 4, 64),
                heads_interleaved=True,
                kv_interleaved=True,
                num_pipelines=2,
            )

    g = G()

    t = g.trace(x=(512, 64), w=(256, 64))
    gemm, mha = t.operators
    assert {k: e.name for k, e in gemm.bound_extents.items()} == {"valid": "n"}
    assert {k: e.name for k, e in mha.bound_extents.items()} == {
        "valid": "n",
        "kv_valid": "n",
    }
    gemm, mha = (op.resolved(aie_utils.get_current_device()) for op in (gemm, mha))
    assert [v.name for v in gemm.values] == ["valid", "row_blocks_valid"]
    assert gemm.derived_at("row_blocks_valid", valid=100) == 1
    assert gemm.residents["col_tiles"] == 256 // gemm.mem_tile_n
    at = dict(valid=100, kv_valid=100)
    assert mha.derived_at("s_q", **at) == mha.derived_at("s_kv", **at) == 100
    assert mha.derived_at("q_blocks_valid", **at) == 1  # 128 padded / (64 x 2)
    assert mha.derived_at("kv_blocks", **at) == 2  # ceil(100 / 64)
    assert mha.derived_at("q_start", **at) == 0
    assert mha.derived_at("q_start", valid=64, kv_valid=192) == 2  # a later chunk
    # Bound alike, the queries start at 0 on every call: written once.
    assert mha.residents["q_start"] == 0 and mha.value("s_q").per_call
    (out,) = t.outputs
    assert out.bounds == {0: t.values[0].affine()}  # O is bounded like Q


# --------------------------------------------------------------------------
# Optional inputs
# --------------------------------------------------------------------------


class _Gather(iron.Graph):
    """A row of a held table, gathered by a per-call index, plus ``x`` if given."""

    def __init__(self, table):
        self.table = iron.weight(table)

    def body(self, x=None, *, r: Scratchpad[np.int32]):
        y = Copy.step(self.table[r])
        return y if x is None else ElementwiseAdd.step(x, y)


def test_an_optional_input_gives_a_version_without_it():
    table = np.arange(4 * 256, dtype=np.int32).astype(bfloat16).reshape(4, 256)
    g = _Gather(table)
    alone, added = g.trace(), g.trace(x=(256,))
    assert alone.inputs == [] and [h.name for h in added.inputs] == ["x"]
    assert g.trace(x=None).inputs == []
    # The row is a view of the one table, indexed per call.
    (copy,) = alone.operators
    assert list(alone.weights) == [id(g.table.array)]
    assert [(b.member.name, b.expression) for b in alone.bindings] == [
        ("in_offset", alone.values[0] * 256)
    ]
    assert {k: e.name for k, e in copy.bound_values.items()} == {"in_offset": "r_x256"}
    x = np.full(256, 2, dtype=bfloat16)
    np.testing.assert_array_equal(g.reference(r=1), table[1])
    np.testing.assert_array_equal(g.reference(None, r=1), table[1])
    np.testing.assert_array_equal(g.reference(x, r=3), table[3] + x)


class _Held(iron.Graph):
    """A checkpoint-held table gathered, sliced and transposed in the body."""

    def __init__(self, table):
        self.weights = SimpleNamespace(embed=SimpleNamespace(weight=table))

    def body(self, x, *, r: Scratchpad[np.int32]):
        table = self.weights.embed.weight
        row = Copy.step(iron.weight(table)[r])
        half = ElementwiseAdd.step(x, table[2:4].reshape(512))
        return row, half, Copy.step(table.T)


def test_a_held_array_is_viewed_in_the_body_under_its_own_path():
    table = np.arange(8 * 256, dtype=np.int32).astype(bfloat16).reshape(8, 256)
    g = _Held(table)
    t = g.trace(x=(512,))
    assert [h.name for _, h in t.weights.values()] == ["weights.embed.weight"]
    assert list(t.weights) == [id(table)]
    whole = BufferRef("weights.embed.weight")
    gather, add, transpose = t.steps
    assert gather.refs()[0] == transpose.refs()[0] == whole
    assert add.refs()[1] == BufferRef("weights.embed.weight", 1024, 1024)
    x = np.full(512, 2, dtype=bfloat16)
    row, half, flipped = g.reference(x, r=5)
    np.testing.assert_array_equal(row, table[5])
    np.testing.assert_array_equal(half, table[2:4].reshape(512) + x)
    np.testing.assert_array_equal(flipped, table.T)


def test_only_none_may_default_an_input():
    with pytest.raises(TypeError, match="may only default to None"):

        class _Bad(iron.Graph):
            def body(self, x=0):
                return x

    with pytest.raises(TypeError, match=r"inputs \['x'\] missing"):
        _Ffn = _ffn()[0]
        _Ffn(pos=0)


def test_an_input_named_as_a_compile_keyword_is_refused():
    with pytest.raises(TypeError, match=r"inputs \['full_elf'\] are named as compile"):

        class _Bad(iron.Graph):
            def body(self, x, full_elf):
                return x


def test_the_reference_refuses_what_a_call_refuses():
    ffn, _ = _ffn()
    x = z(1, E)
    with pytest.raises(TypeError, match=r"inputs \['x'\] missing"):
        ffn.reference(pos=0)
    with pytest.raises(TypeError, match=r"per-call values \['pos'\] missing"):
        ffn.reference(x)
    with pytest.raises(TypeError, match=r"\['position'\] unknown"):
        ffn.reference(x, pos=0, position=0)


def test_a_call_refuses_its_values_before_it_compiles():
    ffn, _ = _ffn()
    with pytest.raises(TypeError, match=r"\['position'\] unknown"):
        ffn(z(1, E), pos=0, position=0)
    assert not ffn._versions


def test_a_refused_compile_restores_the_device_it_was_given_over(npu2):
    ffn, _ = _ffn()
    with pytest.raises(TypeError, match=r"\['nope'\] are not inputs"):
        ffn.compile(dev=from_name("npu1"), x=(1, E), nope=(1,))
    assert aie_utils.get_current_device(probe_runtime=False) is npu2


# --------------------------------------------------------------------------
# Carried values: the graph computes them for its own next call
# --------------------------------------------------------------------------


def test_a_graph_carries_its_next_values():
    successor = np.random.default_rng(0).permutation(16).astype(np.int32)
    walk = Walk(successor)
    t = walk.trace()
    assert [(v.name, v.kind) for v in t.values] == [
        ("node", Kind.CARRIED),
        ("steps", Kind.CARRIED),
    ]
    assert t.inputs == [] and t.returned == []
    # The gathered node is an output buffer, so the host can read it back.
    assert [h.name for h in t.outputs] == ["carry_node"] and t.carry[
        "node"
    ] is t.outputs[0]
    assert t.steps[0].refs()[-1] == BufferRef("carry_node")
    assert t.carry["steps"] == Affine(t.values[1], 1, 1)
    node, steps = 3, 0
    for _ in range(5):
        nxt = walk.reference(node=node, steps=steps)
        assert dict(nxt) == {"node": successor[node], "steps": steps + 1}
        node, steps = nxt["node"], nxt["steps"]


def test_a_carried_handle_may_also_be_returned():
    successor = iron.weight(np.arange(1, 9, dtype=np.int32) % 8)

    class Walk(iron.Graph):
        def body(self, *, node: Carried[np.int32]):
            nxt = Copy.step(successor[node], dtype=np.int32)
            return nxt, iron.carry(node=nxt)

    t = Walk().trace()
    assert [h.name for h in t.outputs] == ["out"] and t.carry["node"] is t.returned[0]
    out, nxt = Walk().reference(node=7)
    assert out.reshape(-1)[0] == 0 and nxt["node"] == 0


def test_every_carried_value_is_carried_and_nothing_else():
    table = iron.weight(np.zeros(8, dtype=np.int32))
    rows = iron.weight(np.zeros((4, 64), dtype=bfloat16))

    class Forgets(iron.Graph):
        def body(self, *, a: Carried[np.int32], b: Carried[np.int32]):
            return iron.carry(a=a + 1)

    with pytest.raises(TypeError, match=r"return iron.carry\(b=\.\.\.\)"):
        Forgets().trace()

    class CarriesAPlainValue(iron.Graph):
        def body(self, *, a: Scratchpad[np.int32]):
            return iron.carry(a=a + 1)

    with pytest.raises(TypeError, match="Carried values are"):
        CarriesAPlainValue().trace()

    class CarriesAConstant(iron.Graph):
        def body(self, *, a: Carried[np.int32]):
            return iron.carry(a=5)

    with pytest.raises(TypeError, match="expression of the values"):
        CarriesAConstant().trace()

    class CarriesARow(iron.Graph):
        def body(self, *, a: Carried[np.int32]):
            return iron.carry(a=Copy.step(rows[a]))

    with pytest.raises(TypeError, match="one whole element"):
        CarriesARow().trace()

    class CarriesTheWrongDtype(iron.Graph):
        def body(self, *, a: Carried[np.int16]):
            return iron.carry(a=Copy.step(table[a], dtype=np.int32))

    with pytest.raises(TypeError, match="but a is int16"):
        CarriesTheWrongDtype().trace()

    class CarriesTwice(iron.Graph):
        def body(self, *, a: Carried[np.int32]):
            return iron.carry(a=a + 1), iron.carry(a=a + 2)

    with pytest.raises(TypeError, match="returned last"):
        CarriesTwice().trace()


def test_the_emit_program_follows_the_target_parameters():
    """Each word of the target's scratchpad comes from a carried value, in
    the target's order and encoding; anything else is refused.
    """
    walk = Trail(np.arange(16, dtype=np.int32), steps=8)
    traced = walk.trace()
    assert traced.feedback == []  # tracing alone adds no Emit
    assert walk._carry is not None
    site = attach_emit(traced, walk._carried, walk._carry, slots=2)
    # The gathered node is computed into the carry's second plane.
    assert traced.steps[0].refs()[-1] == BufferRef("carry", 8, 4)
    assert traced.steps[-1].refs() == (
        BufferRef("emit_program"),
        BufferRef("carry"),
        BufferRef("emit_image"),
        BufferRef("carry", 0, 8),
    )
    assert traced.feedback == ["emit_image"] and traced.outputs == []

    words, _ = _words(traced)
    # A target laying the two out the other way, one as a core read.
    by_value = {w.linear.value: w.symbol for w in words if w.linear is not None}
    parameters = [
        Parameter(by_value["steps"], 0, "i32", "core"),
        Parameter(by_value["node"], 1, "i32", "addr"),
    ]
    program = compose(site, traced.carry, words, parameters)
    lo, hi = UNCLAMPED
    assert program.tolist() == [
        [0, 1, 1, 1, 0, 1, 0, lo, hi, -1, 2],  # steps + 1, shifted for the core
        [1, 0, 1, 0, 0, 1, 0, lo, hi, -1, 0],  # the node the device gathered
        [1, 0, 1, 0, 0, 1, 0, lo, hi, -1, 0],  # the next node
        [0, 1, 1, 1, 0, 1, 0, lo, hi, -1, 0],  # the next step count
    ]
    image, state = emit_reference(program, np.array([[5, 9], [33, 0]]), slots=2)
    assert image.tolist() == [10 << 2, 33] and state.tolist() == [33, 10]

    with pytest.raises(ValueError, match="takes 1"):
        compose(site, traced.carry, words, parameters[:1])
    jumped, _ = _words(walk.trace(jump=((16,), np.int32)))
    with pytest.raises(ValueError, match="skip, which is not carried"):
        compose(
            site,
            traced.carry,
            jumped,
            [Parameter(w.symbol, k, "i32", "addr") for k, w in enumerate(jumped)],
        )


def test_a_state_is_indexed_by_a_floored_carried_value(npu2):
    """``position // 4`` indexes a state's slot: its word floors on the host,
    in the reference and in the Emit program the device runs between calls;
    a bound, which patches a length, stays linear.
    """

    class Slots(iron.Graph):
        def __init__(self):
            self.slots = iron.state((8, 32), np.int32)

        def body(self, *, position: Carried[np.int32]):
            row = Copy.step(self.slots[position // 4], dtype=np.int32)
            Copy.step(row, self.slots[(position + 1) // 4 + 1], dtype=np.int32)
            return iron.carry(position=position + 1)

    graph = Slots()
    traced = graph.trace()
    floored = [b.expression for b in traced.bindings]
    assert [e.down for e in floored] == [2, 2]
    assert len({e.name for e in floored}) == 2
    words, _ = _words(traced)
    assert all(w.linear is None for w in words)
    site = attach_emit(traced, graph._carried, graph._carry, slots=len(words))
    parameters = [Parameter(w.symbol, k, "i32", "addr") for k, w in enumerate(words)]
    program = compose(site, traced.carry, words, parameters)
    for p in range(10):
        image, state = emit_reference(program, np.array([[p], [0]]), slots=len(words))
        want = [w(dict(position=p + 1)) for w in words]
        assert image.tolist() == want == [(p + 1) // 4 * 32, ((p + 2) // 4 + 1) * 32]
        assert state.tolist() == [p + 1]

    slots = np.arange(8 * 32, dtype=np.int32).reshape(8, 32)
    graph.slots.host = slots.copy()
    graph.reference(position=6)
    assert (graph.slots.host[2] == slots[1]).all()

    class Bounded(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return Copy.step(x[: n // 4])

    with pytest.raises(TypeError, match="not linear"):
        Bounded().trace(x=((64, 32), bfloat16))


def test_a_wrapped_expression_is_a_ring_row_and_its_elements():
    """``% m`` (a power of two) wraps after the clamp, and a positive power of
    two times a wrapped expression wraps its elements, at every value tried;
    nothing else follows a wrap."""
    p = PerCall("p", Kind.SCRATCHPAD, np.int32)
    ring = p % 16
    assert ring.name == "p_mod16" and str(ring) == "(p) % 16"
    cases = {
        ring: lambda v: v % 16,
        ring * 64: lambda v: v % 16 * 64,
        iron.clamp(p - 5, lo=0) % 8: lambda v: max(v - 5, 0) % 8,
        iron.clamp(p - 5, lo=0) % 8 * 4: lambda v: max(v - 5, 0) % 8 * 4,
        (p * 3 + 1) // 2 % 32: lambda v: (3 * v + 1) // 2 % 32,
        ring % 4: lambda v: v % 4,
    }
    for e, want in cases.items():
        assert [e.evaluate({"p": v}) for v in range(-40, 41)] == [
            want(v) for v in range(-40, 41)
        ], e
    for bad in (lambda: p % 12, lambda: ring % 32, lambda: ring * 3, lambda: ring * -2):
        with pytest.raises(TypeError):
            bad()
    for bad in (lambda: ring + 1, lambda: ring // 2, lambda: ring.clamp(lo=0)):
        with pytest.raises(TypeError):
            bad()
    with pytest.raises(TypeError, match="not linear"):
        ring.affine()


def test_a_state_is_written_at_a_wrapped_carried_value(npu2):
    """A ring of 8 rows written at ``position % 8`` and read from
    ``max(0, position - 3) % 8``: each word wraps on the host and in the
    Emit program the device runs between calls, past several wraps."""

    class Ring(iron.Graph):
        def __init__(self):
            self.rows = iron.state((8, 32), np.int32)

        def body(self, *, position: Carried[np.int32]):
            row = Copy.step(
                self.rows[iron.clamp(position - 3, lo=0) % 8], dtype=np.int32
            )
            Copy.step(row, self.rows[position % 8], dtype=np.int32)
            return iron.carry(position=position + 1)

    graph = Ring()
    traced = graph.trace()
    words, _ = _words(traced)
    assert all(w.linear is None for w in words)
    site = attach_emit(traced, graph._carried, graph._carry, slots=len(words))
    parameters = [Parameter(w.symbol, k, "i32", "addr") for k, w in enumerate(words)]
    program = compose(site, traced.carry, words, parameters)
    for p in range(40):
        image, state = emit_reference(program, np.array([[p], [0]]), slots=len(words))
        want = [w(dict(position=p + 1)) for w in words]
        assert image.tolist() == want
        assert want == [max(p - 2, 0) % 8 * 32, (p + 1) % 8 * 32]
        assert state.tolist() == [p + 1]

    rows = np.arange(8 * 32, dtype=np.int32).reshape(8, 32)
    for position, read, written in ((1, 0, 1), (10, 7, 2), (21, 2, 5)):
        graph.rows.host = rows.copy()
        graph.reference(position=position)
        assert (graph.rows.host[written] == rows[read]).all()


def test_a_state_is_indexed_by_a_clamped_carried_value(npu2):
    """``max(0, position - 3)`` and ``min((position + 1) // 2, 7)`` index a
    state's rows: each word is clamped on the host and in the Emit program
    the device runs between calls, at positions on both sides of a bound.
    """

    class Rows(iron.Graph):
        def __init__(self):
            self.rows = iron.state((8, 32), np.int32)

        def body(self, *, position: Carried[np.int32]):
            row = Copy.step(self.rows[iron.clamp(position - 3, lo=0)], dtype=np.int32)
            later = iron.clamp((position + 1) // 2, hi=7)
            Copy.step(row, self.rows[later], dtype=np.int32)
            return iron.carry(position=position + 1)

    graph = Rows()
    traced = graph.trace()
    words, _ = _words(traced)
    assert all(w.linear is None for w in words)
    site = attach_emit(traced, graph._carried, graph._carry, slots=len(words))
    parameters = [Parameter(w.symbol, k, "i32", "addr") for k, w in enumerate(words)]
    program = compose(site, traced.carry, words, parameters)
    for p in range(20):
        image, state = emit_reference(program, np.array([[p], [0]]), slots=len(words))
        want = [w(dict(position=p + 1)) for w in words]
        assert image.tolist() == want
        assert want == [max(p - 2, 0) * 32, min((p + 2) // 2, 7) * 32]
        assert state.tolist() == [p + 1]

    rows = np.arange(8 * 32, dtype=np.int32).reshape(8, 32)
    for position, read, written in ((1, 0, 1), (9, 6, 5), (10, 7, 5)):
        graph.rows.host = rows.copy()
        graph.reference(position=position)
        assert (graph.rows.host[written] == rows[read]).all()


class _HeldStack(iron.Graph):
    """A checkpoint-held stack of two tables gathered as one, by the ids an
    input names."""

    def __init__(self, tables):
        self.weights = SimpleNamespace(embed=SimpleNamespace(weight=tables))

    def body(self, ids):
        tables = self.weights.embed.weight
        return Copy.step(iron.weight(tables.reshape(-1, tables.shape[-1]))[ids])


def test_a_whole_reshape_of_a_held_array_is_gathered_under_its_own_path():
    tables = np.arange(2 * 8 * 256, dtype=np.int32).astype(bfloat16)
    tables = tables.reshape(2, 8, 256)
    g = _HeldStack(tables)
    t = g.trace(ids=((4,), np.int32))
    assert [h.name for _, h in t.weights.values()] == ["weights.embed.weight"]
    (gather,) = t.steps
    assert gather.refs()[0] == BufferRef("weights.embed.weight")
    ids = np.array([15, 0, 8, 7], np.int32)
    np.testing.assert_array_equal(g.reference(ids), tables.reshape(16, 256)[ids])


class _Summed(iron.Graph):
    """The sum of the first ``n`` rows of as many inputs as it is made with."""

    def __init__(self, count: int):
        self.count = count

    def signature(self) -> inspect.Signature:
        P = inspect.Parameter
        inputs = [P(f"x{i}", P.POSITIONAL_OR_KEYWORD) for i in range(self.count)]
        n = P("n", P.KEYWORD_ONLY, annotation=Scratchpad[np.int32])
        return inspect.Signature([*inputs, n])

    def body(self, *inputs, **values):
        n = values["n"]
        total = inputs[0][:n]
        for x in inputs[1:]:
            total = ElementwiseAdd.step(total, x[:n])
        return total


@pytest.mark.parametrize("count", [2, 3])
def test_a_graph_names_its_inputs_and_values_in_signature(count):
    g = _Summed(count)
    shapes = {f"x{i}": (8, 256) for i in range(count)}
    t = g.trace(**shapes)
    assert [h.name for h in t.inputs] == list(shapes)
    assert [v.name for v in t.values] == ["n"]
    assert len(t.steps) == count - 1
    xs = [np.full((8, 256), i + 1, bfloat16) for i in range(count)]
    got = g.reference(*xs, n=3)
    np.testing.assert_array_equal(got, np.full((3, 256), sum(range(1, count + 1))))
    with pytest.raises(TypeError, match="per-call value"):
        g.reference(*xs)


def test_a_body_of_args_with_no_signature_is_refused_as_its_class_is_made():
    with pytest.raises(TypeError, match="not traceable"):

        class _Bad(iron.Graph):
            def body(self, *inputs):
                return inputs


class _TwoBounds(iron.Graph):
    """Two per-call values, of which a version reads one."""

    def body(self, x=None, y=None, *, n: Scratchpad[np.int32], m: Scratchpad[np.int32]):
        if x is not None:
            return ElementwiseAdd.step(x[:n], x[:n])
        return ElementwiseAdd.step(y[:m], y[:m])


def test_a_version_reads_only_the_values_its_steps_read():
    g = _TwoBounds()
    assert g.trace(x=(8, 256)).reads == {"n"}
    assert g.trace(y=(8, 256)).reads == {"m"}
    assert [v.name for v in g.trace(x=(8, 256)).values] == ["n", "m"]


def test_inline_traces_only_into_a_body():
    with pytest.raises(TypeError, match="traces into a graph's body"):
        _Summed(2).inline(_Summed(2).body)


class _DeviceIds(iron.Graph):
    """A gather by ids a step made, whose table address the image writes."""

    def __init__(self, table):
        self.table = iron.weight(table)

    def body(self, ids, *, n: Scratchpad[np.int32], m: Scratchpad[np.int32]):
        return Copy.step(self.table[Copy.step(ids, dtype=np.int32)[:n]])


def test_a_version_reads_none_of_the_words_its_image_writes():
    table = np.zeros((300, 64), dtype=bfloat16)
    traced = _DeviceIds(table).trace(ids=((64,), np.int32))
    assert traced.addresses, "the gather's table address is a word the image writes"
    assert traced.reads == {"n"}


@pytest.mark.parametrize("band_stride", [0, 1])
def test_a_walk_by_a_per_call_repeat_and_length_is_its_reference(band_stride):
    walk = copy_bounded_view
    table = np.arange(walk.HK * walk.WK * walk.K2 * walk.E, dtype=np.float32)
    table = table.astype(bfloat16).reshape(-1, walk.E)
    graph = walk.Walk(table, band_stride)
    (step,) = graph.trace().steps
    assert (step.op.src_repeat, step.op.src_bound, step.op.dst_bound) == (True, 1, 0)
    for hk, wk in ((3, 4), (1, 1)):
        n = hk * wk * walk.K2
        got = np.asarray(graph.reference(hk=hk, wk=wk, n=n), dtype=np.float32)
        want = walk.walked(table, band_stride, hk, wk).astype(np.float32)
        np.testing.assert_array_equal(got, want)


@pytest.mark.parametrize("band_stride", [0, 1])
def test_walks_in_turn_are_their_reference(band_stride):
    walk = copy_bounded_view
    table = np.arange(walk.HK * walk.WK * walk.K2 * walk.E, dtype=np.float32)
    table = table.astype(bfloat16).reshape(-1, walk.E)
    graph = walk.Walks(table, band_stride)
    (step,) = graph.trace().steps
    assert (len(step.op.src), step.op.src_repeat, step.op.src_bound) == (3, True, 1)
    for hk, wk in ((3, 4), (walk.HK, walk.WK), (1, 1)):
        values = walk.walks_values(hk, wk)
        got = np.asarray(graph.reference(**values), dtype=np.float32)
        want = walk.walks_walked(table, band_stride, hk, wk).astype(np.float32)
        np.testing.assert_array_equal(got[: values["n"]], want)
        real = walk.walked(table, band_stride, hk, wk).astype(np.float32)
        np.testing.assert_array_equal(got[: real.shape[0]], real)


class _StateRows(iron.Graph):
    """A state's rows, bounded per call, added to an input's."""

    def __init__(self):
        self.rows = iron.state((64, 64))

    def body(self, x, *, n: Scratchpad[np.int32]):
        Copy.step(x[:n], self.rows[:n])
        rows = self.rows.at(TensorAccessPattern.full((64, 64)), (64, 64), {0: n})
        return ElementwiseAdd.step(x[:n], rows)


def test_a_bounded_view_of_a_state_is_its_rows_this_call():
    """In a reference, a state viewed by ``at`` is its host rows to the bound."""
    x = np.arange(64 * 64, dtype=np.float32).reshape(64, 64).astype(bfloat16)
    got = np.asarray(_StateRows().reference(x, n=40), dtype=np.float32)
    want = (2 * x[:40].astype(np.float32)).astype(bfloat16).astype(np.float32)
    np.testing.assert_array_equal(got, want)


def test_bounded_rows_past_a_wrap_halve_the_run():
    """A bound of more rows than D1 wraps takes D2, the run's halves D1."""
    graph = copy_bounded_view.Halves()
    traced = graph.trace(x=(copy_bounded_view.ROWS, 32), y=(copy_bounded_view.ROWS, 32))
    into = [s.op for s in traced.steps][:2]
    for op in into:
        ((tap, unit),) = op._taps(op.dst, op.dst_bound, op.y)
        assert (list(tap.sizes), unit) == ([1, copy_bounded_view.ROWS, 2, 16], 32)
    x = np.arange(copy_bounded_view.ROWS * 32, dtype=np.float32).reshape(-1, 32)
    x, y = x.astype(bfloat16), (x + 0.5).astype(bfloat16)
    got = np.asarray(graph.reference(x, y, n=1500), dtype=np.float32)
    want = np.concatenate([x[:1500], y[:1500]], axis=1).astype(np.float32)
    np.testing.assert_array_equal(got[:1500], want)


class _BadWalk(iron.Graph):
    """A walk ``Handle.at`` refuses."""

    def __init__(self, sizes, strides, bounded: bool):
        self.table = iron.weight(np.zeros((64, 4096), dtype=bfloat16))
        self.sizes, self.strides, self.bounded = sizes, strides, bounded

    def body(self, *, k: Scratchpad[np.int32]):
        tap = TensorAccessPattern(self.table.shape, 0, self.sizes, self.strides)
        bounds = {0: k} if self.bounded else None
        return Copy.step(self.table.at(tap, (64, 4096), bounds=bounds, repeat=k))


@pytest.mark.parametrize(
    "sizes, strides, bounded, match",
    [
        ([64, 4096], [4096, 1], True, "one shim"),  # not four dimensions
        # Rows of 1024 words, past a descriptor's innermost wrap, with gaps.
        ([2, 2, 8, 2048], [0, 65536, 4096, 1], True, "one shim"),
        ([4, 4, 4, 1024], [0, 4096, 1024, 1], False, "give bounds"),
    ],
)
def test_a_walk_one_descriptor_cannot_hold_is_refused(sizes, strides, bounded, match):
    with pytest.raises(ValueError, match=match):
        _BadWalk(sizes, strides, bounded).trace()


class _UnpairedWalks(iron.Graph):
    """Two patterns walked in turn with one repeat between them."""

    def __init__(self):
        self.table = iron.weight(np.zeros((64, 64), dtype=bfloat16))

    def body(self, *, k: Scratchpad[np.int32]):
        tap = TensorAccessPattern(self.table.shape, 0, [4, 4, 4, 64], [0, 256, 64, 1])
        rows = self.table.at((tap, tap), (128, 64), bounds={0: k}, repeat=k)
        return Copy.step(rows)


def test_walks_in_turn_take_a_repeat_each():
    with pytest.raises(ValueError, match="take a repeat each"):
        _UnpairedWalks().trace()


def test_a_handle_adds_and_multiplies_by_elementwise_and_rowwise_steps():
    w = z(E)

    class Arithmetic(iron.Graph):
        def __init__(self):
            self.w = w

        def body(self, x, y):
            return (x + y) * self.w + x

    t = Arithmetic().trace(x=(2, E), y=(2, E))
    assert [type(s.op).__name__ for s in t.steps] == [
        "ElementwiseAdd",
        "RowwiseMul",
        "ElementwiseAdd",
    ]
    with pytest.raises(TypeError, match="a row of"):
        Arithmetic().trace(x=(2, E), y=(2, E // 2))


@pytest.mark.parametrize(
    "rows, keywords",
    [(1, dict(k_tile=64)), (4, dict(tile_size_output=32))],
    ids=["gemv", "gemm"],
)
def test_linear_refuses_a_tunable_its_rows_do_not_choose(rows, keywords):
    class Linear(iron.Graph):
        def __init__(self):
            self.w = iron.weight(z(E, E))

        def body(self, x):
            return F.linear(x, self.w, **keywords)

    with pytest.raises(ValueError, match="no (GEMV|flm.GEMM)"):
        Linear().trace(x=(rows, E))


def test_a_row_times_a_matrix_is_rowwise_either_way_round():
    class Scale(iron.Graph):
        def body(self, x, row):
            return row * x, x * row

    t = Scale().trace(x=(4, E), row=(E,))
    assert [type(s.op).__name__ for s in t.steps] == ["RowwiseMul", "RowwiseMul"]


def test_an_operand_neither_of_its_shape_nor_a_row_is_refused():
    class Add(iron.Graph):
        def body(self, x, y):
            return x + y

    with pytest.raises(TypeError, match="takes an operand of its shape or a row"):
        Add().trace(x=(4, E), y=(4, E // 2))
