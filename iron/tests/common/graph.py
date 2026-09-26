# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graph functions, traced device-free.

A graph function run on handles produces a runlist, buffer names and
sizes, and value bindings; nothing here needs a toolchain. What is not
checked here is the image: that is OperatorSequence's job and the
hardware tests' job.
"""

import dataclasses
from typing import Any

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import DispatchTime, Profile, Scratchpad
from iron.common.graph import Handle, TracedGraph, Tracer
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv.op import GEMV
from iron.operators.rms_norm import RMSNorm, WeightedRMSNorm
from iron.operators.silu import SiLU
from iron.operators.transpose import Transpose

E, H = 2048, 8192


def z(*shape, dtype=bfloat16):
    return np.zeros(shape, dtype=dtype)


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _ffn():
    w_gate, w_up, w_down, norm_w = z(H, E), z(H, E), z(E, H), z(E)
    cache = iron.state((4, 1024, 64))

    @iron.graph
    def ffn(x, *, pos: Scratchpad[np.int32]):
        h = RMSNorm(x, norm_w)  # a bare tensor is a weight
        gate = GEMV(
            w_gate, h, num_aie_columns=8, tile_size_input=4, tile_size_output=H // 8
        )
        up = GEMV(
            w_up, h, num_aie_columns=8, tile_size_input=4, tile_size_output=H // 8
        )
        act = ElementwiseMul(SiLU(gate), up)
        Copy(
            act[: 4 * 64].reshape(4, 64), cache[:, pos]
        )  # writes state; returns nothing
        return GEMV(w_down, act, num_aie_columns=8, tile_size_output=E // 8)

    refs: dict[str, Any] = dict(
        w_gate=w_gate, w_up=w_up, w_down=w_down, norm_w=norm_w, cache=cache
    )
    return ffn, refs


def test_tracing_records_the_runlist_with_names_from_roles():
    ffn, refs = _ffn()
    t = ffn.trace(x=(1, E))
    assert isinstance(t, TracedGraph)
    assert [(type(op).__name__, *names) for op, *names in t.runlist] == [
        ("WeightedRMSNorm", "x", "w0", "weightedrmsnorm0"),
        ("GEMV", "w1", "weightedrmsnorm0", "gemv1"),
        ("GEMV", "w2", "weightedrmsnorm0", "gemv2"),
        ("SiLU", "gemv1", "silu3"),
        ("ElementwiseMul", "silu3", "gemv2", "elementwisemul4"),
        ("Copy", "elementwisemul4[0:512]", "state0"),
        ("GEMV", "w3", "elementwisemul4", "out"),
    ]
    assert t.input_args == ["x"] and t.output_args == ["out"]
    # Weights, the state and a sliced intermediate keep private addresses.
    assert t.pinned == {
        "w0": E * 2,
        "w1": H * E * 2,
        "w2": H * E * 2,
        "w3": H * E * 2,
        "state0": 4 * 1024 * 64 * 2,
        "elementwisemul4": H * 2,
    }


def test_arrays_are_shared_by_array_key_and_extents_are_not():
    ffn, _ = _ffn()
    t = ffn.trace(x=(1, E))
    gate, up, down = (s.op for s in t.steps if type(s.op) is GEMV)
    assert (
        gate.array_key() == up.array_key() and gate is not up
    )  # one array, two operators
    assert down.array_key() != gate.array_key()  # a different K is a different array
    assert [type(o).__name__ for o in t.arrays] == [
        "WeightedRMSNorm",
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
    op, value = binding.op, binding.value
    assert type(op) is Copy and binding.member.name == "out_offset"
    assert value.name == "pos" and value.kind == "scratchpad"
    assert op.uses_value("out_offset") and not op.uses_value("in_offset")
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
    norm = next(s.op for s in t.steps if type(s.op) is WeightedRMSNorm).resolved(
        aie_utils.get_current_device()
    )
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
    assert part.shape == (2, 64) and part.buffer_name == "acts[256:512]"
    assert h[3].shape == (64,) and h[3].buffer_name == "acts[384:512]"
    with pytest.raises(TypeError, match="slicing a slice"):
        part[0]
    with pytest.raises(ValueError, match="unit steps"):
        h[::2]
    assert h.reshape(512).shape == (512,) and h.reshape(512).buffer_name == "acts"
    assert part.reshape(128).buffer_name == "acts[256:512]"
    with pytest.raises(ValueError, match="cannot reshape"):
        h.reshape(3, 3)


def test_alike_instances_bound_to_different_values_are_different_designs():
    """Two copies alike in every field, one indexed by ``a`` and one by ``b``,
    write through two symbols and build twice; two bound to one value share.
    """
    from iron.common.design.build import device_symbol

    c1, c2, c3 = (iron.state((4, 64, 16)) for _ in range(3))

    @iron.graph
    def f(x, *, a: Scratchpad[np.int32], b: Scratchpad[np.int32]):
        Copy(x, c1[:, a])
        Copy(x, c2[:, b])
        Copy(x, c3[:, a])

    t = f.trace(x=(4, 16))
    by_value = {b.value.name: b for b in t.bindings}
    assert len(t.bindings) == 3 and set(by_value) == {"a", "b"}
    first, second, third = t.bindings
    assert first.op.bound_values == {"out_offset": "a"}
    assert first.op.design_key() != second.op.design_key()
    assert first.op.design_key() == third.op.design_key()
    symbols = [device_symbol(b.op, b.member) for b in t.bindings]
    assert symbols[0] != symbols[1] and symbols[0] == symbols[2]
    assert symbols[0].endswith("_out_offset_a") and symbols[1].endswith("_out_offset_b")


def test_an_explicit_instance_checks_its_operands_shapes():
    q = GEMV(M=256, K=E, num_aie_columns=8, tile_size_input=4, tile_size_output=32)
    w_t = z(E, 256)  # the weight transposed: the same element count

    @iron.graph
    def step(x):
        return q(w_t, x)

    with pytest.raises(ValueError, match=r"GEMV.A is \(256, 2048\)"):
        step.trace(x=(E,))


def test_binding_two_handles_to_one_instance_is_an_error():
    copy = Copy(input_buffer_size=64, output_buffer_size=64)

    @iron.graph
    def two(x, *, a: Scratchpad[np.int32], b: Scratchpad[np.int32]):
        y = copy(x, out_offset=a)
        return copy(y, out_offset=b)

    with pytest.raises(ValueError, match="bound to Value\\('a'"):
        two.trace(x=(64,))


def test_a_graph_function_carries_its_profile():
    """A profile given to ``iron.graph`` reaches every run of the body: the
    trace and the host reference alike, with a call's own keyword kept.
    """
    profile = Profile()
    profile.add(GEMV, tile_size_input=4, tile_size_output=16)
    profile.add(GEMV, M=E, tile_size_output=E // 8)
    w_a, w_b = z(256, E), z(E, 256)

    @iron.graph(profile=profile)
    def two(x):
        return GEMV(w_b, GEMV(w_a, x, tile_size_output=32))

    a, b = (s.op for s in two.trace(x=(E,)).steps)
    assert (a.tile_size_input, a.tile_size_output) == (4, 32)  # the call's own
    assert (b.tile_size_input, b.tile_size_output) == (4, E // 8)  # the profile's
    assert two.reference(z(E)).shape == (E,)  # constructs under the profile too
    assert GEMV(M=E, K=256).tile_size_output is None  # nothing outside it


def test_an_explicit_instance_is_applied_like_the_class():
    q = GEMV(M=256, K=E, num_aie_columns=8, tile_size_input=4, tile_size_output=32)
    w = z(256, E)

    @iron.graph
    def step(x):
        return q(w, x)

    t = step.trace(x=(E,))
    assert t.runlist[0][0] is q and t.output_args == ["out"]
    with pytest.raises(TypeError, match="inside an @iron.graph function"):
        q(w, z(E))


def test_shape_mismatch_and_rank_rules():
    w = z(256, E)

    @iron.graph
    def bad(x):
        return GEMV(w, x)

    with pytest.raises(ValueError, match=r"K is 1024 from B.shape\[0\] but 2048"):
        bad.trace(x=(E // 2,))
    add = ElementwiseAdd

    @iron.graph
    def flat(x, y):
        return add(x, y)  # a flat operator takes any rank

    t = flat.trace(x=(4, 512), y=(4, 512))
    assert t.steps[0].op.size == 2048 and t.outputs[0].shape == (4, 512)


def test_keyword_only_parameters_must_be_annotated_as_values():
    with pytest.raises(TypeError, match="annotated Scratchpad"):

        @iron.graph
        def f(x, *, n):
            return x

    @iron.graph
    def g(x, *, n: DispatchTime[np.int32]):
        return SiLU(x)

    t = g.trace(x=(1024,))
    assert [(v.name, v.kind) for v in t.values] == [("n", "dispatch")]


def test_returning_an_input_or_a_slice_is_refused():
    @iron.graph
    def ident(x):
        return x

    with pytest.raises(TypeError, match="returns its input"):
        ident.trace(x=(64,))

    @iron.graph
    def part(x):
        return SiLU(x)[:8]

    with pytest.raises(TypeError, match="whole handles"):
        part.trace(x=(64,))


# --------------------------------------------------------------------------
# The two swiglu composites, as graph functions
# --------------------------------------------------------------------------


def test_swiglu_decode_shares_one_array_and_one_build_for_gate_and_up():
    import iron.operators.swiglu_decode.op as m

    ffn = m.swiglu_decode(z(H, E), z(H, E), z(E, H))
    t = ffn.trace(x=(1, E))
    assert [type(op).__name__ for op, *_ in t.runlist] == [
        "GEMV",
        "GEMV",
        "SiLU",
        "ElementwiseMul",
        "GEMV",
    ]
    gate, up, down = (s.op for s in t.steps if type(s.op) is GEMV)
    assert gate.array_key() == up.array_key() and gate.design_key() == up.design_key()
    assert down.design_key() != gate.design_key()
    assert (gate.num_aie_columns, gate.tile_size_output) == (8, H // 8)
    assert t.input_args == ["x"] and t.output_args == ["out"]
    with pytest.raises(ValueError, match="do not agree"):
        m.swiglu_decode(z(H, E), z(H, E), z(H, E))


def test_two_spellings_of_one_array_are_one_design():
    """Identity is taken after resolution: a knob left to resolve and the same
    knob given its resolved value name one array, and a sequence builds it
    once. Every operator of a traced graph goes through the same point, so
    the design counts here are the gate on it.
    """
    from iron.common.image import OperatorSequence

    a = GEMV(M=64, K=256, num_aie_columns=2, tile_size_input=2)
    b = GEMV(M=64, K=256, num_aie_columns=2, tile_size_input=2, tile_size_output=2)
    assert a.design_key() != b.design_key()  # as given
    seq = OperatorSequence(
        "two_spellings",
        [(a, "x", "w", "y"), (b, "x2", "w", "z")],
        input_args=["x", "x2", "w"],
        output_args=["z"],
        share_designs=True,
    )
    seq.prepare()
    designs, _ = seq.unique_designs()
    assert len(designs) == 1 and designs[0].tile_size_output == 2
    ffn, _ = _ffn()
    seq = ffn.trace(x=(1, E)).sequence()
    seq.prepare()
    assert len(seq.unique_designs()[0]) == 6


def test_swiglu_prefill_traces_over_a_sequence():
    import iron.operators.swiglu_prefill.op as m
    from iron.operators.gemm.op import GEMM

    ffn = m.swiglu_prefill(z(E, H), z(E, H), z(H, E))
    t = ffn.trace(x=(256, E))
    gemms = [s.op for s in t.steps if type(s.op) is GEMM]
    assert [(g.M, g.K, g.N) for g in gemms] == [(256, E, H), (256, E, H), (256, H, E)]
    assert gemms[0].array_key() == gemms[1].array_key()
    silu = next(s.op for s in t.steps if type(s.op) is SiLU)
    assert silu.size == 256 * H


# --------------------------------------------------------------------------
# llama decode, traced at a scaled-down configuration
# --------------------------------------------------------------------------


def test_llama_decode_traces_and_tunes():
    from iron.applications.llama_3_2_1b.graphs import LlamaGraph
    from iron.tests.common.llama_model import Config as _Config

    cfg = _Config()
    L = 256
    t = LlamaGraph(cfg, L).trace(cfg, 1)
    kinds = [type(op).__name__ for op, *_ in t.runlist]
    per_block = [
        "WeightedRMSNorm",
        "GEMV",
        "GEMV",
        "GEMV",
        "RoPE",
        "RoPE",
        "Copy",
        "Copy",
        "Repeat",
        "Repeat",
        "GEMV",
        "ElementwiseMul",
        "Softmax",
        "Transpose",
        "GEMV",
        "GEMV",
        "ElementwiseAdd",
        "WeightedRMSNorm",
        "GEMV",
        "GEMV",
        "SiLU",
        "ElementwiseMul",
        "GEMV",
        "ElementwiseAdd",
    ]
    assert kinds == per_block * cfg.n_layers + ["WeightedRMSNorm", "GEMV"]
    assert t.input_args == ["x", "angles"] and t.output_args == ["out"]
    # One function, so every version takes every value; one token binds two.
    assert [v.name for v in t.values] == ["rows", "cache_offset", "vector_size", "last"]
    assert {b.value.name for b in t.bindings} == {"cache_offset", "vector_size"}
    # The weights are named from the model; the caches are pinned state.
    assert "layers.1.attn.q.weight" in t.pinned and "keys_cache_0" in t.pinned
    assert t.pinned["keys_cache_0"] == cfg.n_kv_groups * L * cfg.head_dim * 2
    # One strided copy instance per layer is bound to cache_offset on both of
    # its call sites; every softmax binds vector_size.
    copies = [
        (b.op, b.member.name) for b in t.bindings if b.value.name == "cache_offset"
    ]
    assert len(copies) == cfg.n_layers * 2 and all(n == "out_offset" for _, n in copies)
    softmaxes = [b.op for b in t.bindings if b.value.name == "vector_size"]
    assert len(softmaxes) == cfg.n_layers
    assert all(s.uses_value("vector_size") for s in softmaxes)
    # The same array serves every layer's like projections.
    q_arrays = {
        s.op.array_key()
        for s in t.steps
        if type(s.op) is GEMV
        and s.op.M == cfg.n_heads * cfg.head_dim
        and s.op.K == cfg.emb_dim
    }
    assert len(q_arrays) == 1
    # Every operator tunes and is compatible on an 8-column device.
    for op in t.operators:
        op.resolved(aie_utils.get_current_device())
    # The profile gave the tiles decode was tuned with: half a head per
    # projection tile, a column's share of the row for the output
    # projection, two columns for the transpose, one core for the norm.
    E, D = cfg.emb_dim, cfg.head_dim
    gemvs = [s.op for s in t.steps if type(s.op) is GEMV]
    q, k, v, scores, ctx, o, gate, up, down = gemvs[:9]
    assert (q.tile_size_output, k.tile_size_output, o.tile_size_output) == (
        D // 2,
        D // 2,
        E // 8,
    )
    assert (down.tile_size_input, gate.tile_size_output) == (1, cfg.hidden_dim // 8)
    transpose = next(s.op for s in t.steps if type(s.op) is Transpose)
    assert (transpose.num_aie_columns, transpose.m, transpose.n) == (2, 256, 32)
    assert (
        next(s.op for s in t.steps if type(s.op) is WeightedRMSNorm).num_aie_columns
        == 1
    )


def test_llama_prompt_traces_over_the_same_caches():
    from iron.applications.llama_3_2_1b.graphs import LlamaGraph
    from iron.tests.common.llama_model import Config as _Config

    cfg = _Config()
    L = cfg.context_length
    g = LlamaGraph(cfg, L)
    t = g.trace(cfg, L)
    kinds = [type(op).__name__ for op, *_ in t.runlist]
    per_block = [
        "WeightedRMSNorm",
        "GEMM",
        "GEMM",
        "GEMM",
        "RoPE",
        "RoPE",
        "Copy",
        "Copy",
        "MHA",
        "GEMM",
        "ElementwiseAdd",
        "WeightedRMSNorm",
        "GEMM",
        "GEMM",
        "SiLU",
        "ElementwiseMul",
        "GEMM",
        "ElementwiseAdd",
    ]
    tail = ["Copy", "WeightedRMSNorm", "GEMV"]
    assert kinds == per_block * cfg.n_layers + tail
    assert t.input_args == ["x", "angles"] and t.output_args == ["out"]
    assert [v.name for v in t.values] == ["rows", "cache_offset", "vector_size", "last"]
    # One slice at the top bounds every operator of every block by the rows
    # the call runs; the tail (the last row's copy, the norm and the head)
    # runs one row and is not.
    by_rows = [op for op, *_ in t.runlist if "rows" in op.bound_values.values()]
    assert len(by_rows) == len(per_block) * cfg.n_layers
    mha = next(op for op, *_ in t.runlist if type(op).__name__ == "MHA")
    assert mha.bound_values == {
        "valid": "rows",
        "s_q": "vector_size",
        "s_kv": "vector_size",
    }
    # The caches are the states a token's version reads: the same objects,
    # so one arena holds them once for both.
    token = g.trace(cfg, 1)
    assert set(t.states) == set(token.states)
    assert t.residents["keys_cache_0"] == token.residents["keys_cache_0"]
    assert set(t.weights) == set(token.weights) - {id(g.scale)}
    # Every projection reads the (out, in) checkpoint layout through the
    # column-major flag, which the trace carries into shape inference.
    gemms = [op for op, *_ in t.runlist if type(op).__name__ == "GEMM"]
    assert all(op.b_col_maj for op in gemms)
    K = {op.K for op in gemms}
    assert K == {cfg.emb_dim, cfg.hidden_dim, cfg.n_heads * cfg.head_dim}
    # The last-row copy is the one operator bound to the per-call offset.
    offsets = [
        (type(b.op).__name__, b.member.name)
        for b in t.bindings
        if b.member.name.endswith("_offset")
    ]
    assert offsets == [("Copy", "in_offset")]
    for op in t.operators:
        op.resolved(aie_utils.get_current_device())


def _resolved_fields(settings):
    """Every field of every step of every setting, resolved for its device.

    A setting is ``(device, trace)``: ``trace`` builds the graph with that
    device current and traces it. The device is restored afterwards.
    """
    previous = aie_utils.get_current_device()
    try:
        out = []
        for dev, trace in settings:
            aie_utils.set_current_device(dev)
            out.append(
                [
                    tuple((f.name, getattr(op, f.name)) for f in dataclasses.fields(op))
                    + (op.design_key(),)
                    for op, *_ in trace().runlist
                    for op in [op.resolved(dev)]
                ]
            )
        return out
    finally:
        aie_utils.set_current_device(previous)


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


def test_llama_names_only_the_knobs_that_matter(monkeypatch):
    """Every keyword the llama graph passes is a choice resolution would not
    have made in some setting the graph is written for: the model's real
    shape at the graph's own defaults, on either NPU generation for a decode
    step and on NPU2 (MHA's) for a prompt; and the scaled-down shape the
    host tests trace, with the parameters that shape needs.
    """
    from aie.iron.device import from_name

    from iron.applications.llama_3_2_1b.graphs import LlamaGraph
    from iron.tests.common.llama_model import Config as _Config
    from iron.tests.common.llama_model import Llama1B

    npu2, npu1 = from_name("npu2", n_cols=8), from_name("npu1", n_cols=4)
    real, small = Llama1B(n_layers=1), _Config()
    L = small.context_length
    settings = [
        (npu2, lambda: LlamaGraph(real, 512).trace(real, 1)),
        (npu1, lambda: LlamaGraph(real, 512).trace(real, 1)),
        (npu2, lambda: LlamaGraph(real, 512).trace(real, 512)),
        (
            npu2,
            lambda: LlamaGraph(small, L).trace(small, L),
        ),
    ]
    _every_keyword_is_load_bearing(monkeypatch, settings)


def test_a_bound_value_survives_tuning():
    copy = Copy(input_buffer_size=64, output_buffer_size=64)

    @iron.graph
    def f(x, *, a: Scratchpad[np.int32]):
        return copy(x, out_offset=a)

    f.trace(x=(64,))
    assert [v.name for v in copy.resolved(aie_utils.get_current_device()).values] == [
        "out_offset"
    ]


# --------------------------------------------------------------------------
# A bound on a handle: the first n of an axis are the valid ones this call
# --------------------------------------------------------------------------


def test_a_bound_travels_through_reshape_and_transpose():
    from iron.common.graph.handle import Value

    n = Value("n", "scratchpad", np.int32)
    x = Handle((64, 8, 4), bfloat16, "x", "input")
    b = x[:n]
    assert b.shape == x.shape and b.bounds == {0: (n, 1)} and b.walk is None
    assert b.reshape(512, 4).bounds == {0: (n, 8)}  # merged with the axis after it
    assert b.reshape(64 * 8 * 4).bounds == {0: (n, 32)}
    assert b.reshape(512, 4).reshape(64, 8, 4).bounds == {0: (n, 1)}  # split back
    assert b.transpose(1, 0, 2).bounds == {1: (n, 1)}
    with pytest.raises(ValueError, match="does not divide"):
        b.reshape(32, 16, 4)  # a leading axis no run of the others makes
    assert b[0].bounds == {} and b[0].shape == (8, 4)  # one row: no bound
    with pytest.raises(TypeError, match="bounded per call on axis 0"):
        b[0:2]
    with pytest.raises(ValueError, match="from its start"):
        x[2:n]


def test_the_words_a_call_writes_come_from_the_bound(npu2):
    """Each bound value is a word, and so is every value an operator derives
    from a bounded extent, computed by the operator from the call's bound.
    """
    from iron.common.graph.compiled import _words
    from iron.tests.common.declare import Rows

    @iron.graph
    def g(x, *, n: Scratchpad[np.int32]):
        return Rows(x[:n].reshape(64 * 8, 1))  # rows x 8 seen as rows*8 x 1

    t = g.trace(x=(64, 8))
    (op,) = t.operators
    words = {symbol: word for symbol, _, word in _words(t)}
    assert set(words) == {
        f"{op.name}_{w}" for w in ("valid_n", "count", "valid_x", "valid_y")
    }
    call = {"n": 16}
    assert words[f"{op.name}_valid_n"](call) == 16 * 8  # the reshape's scale
    assert words[f"{op.name}_count"](call) == 16 * 8 // 2  # derived: valid // lanes
    assert words[f"{op.name}_valid_x"](call) == 16 * 8 // 2  # tiles per lane


def test_a_bound_reaches_a_copy_and_a_repeat_through_their_views(npu2):
    """``x[:n]`` reshaped and transposed lands on axis 1 of the copy's source
    walk; ``keys[:, :n]`` on axis 1 of its destination; ``keys[:, :c]`` on the
    stack axis of a Repeat, whose output carries the bound on.
    """
    from iron.operators.copy import Copy
    from iron.operators.repeat import Repeat

    G, D, L = 4, 8, 32  # traced at the cache's full length, as a prompt is
    keys = iron.state((G, L, D), name="keys")

    @iron.graph
    def g(x, *, n: Scratchpad[np.int32], c: Scratchpad[np.int32]):
        k = x[:n].reshape(L, G, D).transpose(1, 0, 2)
        Copy(k, keys[:, :n])
        return Repeat(keys[:, :c], repeat=2)

    t = g.trace(x=(L, G * D))
    copy, rep = t.operators
    assert copy.src.bounded == 1 and copy.dst.bounded == 1
    assert copy.bound_values == {"src_valid": "n", "dst_valid": "n"}
    assert rep.bound_extents == {"valid_seq": "c"}
    assert [(b.member.name, b.value.name, b.scale) for b in t.bindings] == [
        ("src_valid", "n", 1),
        ("dst_valid", "n", 1),
        ("valid_seq", "c", 1),
    ]
    (out,) = t.outputs
    assert out.shape == (2 * G, L, D) and out.bounds == {1: (t.values[1], 1)}
    rep = rep.resolved(aie_utils.get_current_device())
    assert rep.derived_at("valid_seq_x", valid_seq=12) == 12  # the stack axis itself


def test_gemm_and_mha_bound_their_compute_not_their_traffic(npu2):
    """A bound reaches GEMM through A's rows and MHA through Q's padded
    length (a select shape): each derives the counts its cores compute per
    call, makes no word of tiles per lane, and keeps every descriptor.
    """
    from iron.operators.gemm.op import GEMM
    from iron.operators.mha.op import MHA

    @iron.graph
    def g(x, w, *, n: Scratchpad[np.int32]):
        h = GEMM(x[:n], w, b_col_maj=True)  # (512, 64) x (256, 64)^T
        return MHA(
            h.reshape(512, 4, 64),
            h.reshape(512, 4, 64),
            h.reshape(512, 4, 64),
            heads_interleaved=True,
            num_pipelines=2,
        )

    t = g.trace(x=(512, 64), w=(256, 64))
    gemm, mha = t.operators
    assert gemm.bound_extents == {"valid": "n"} and mha.bound_extents == {"valid": "n"}
    gemm, mha = (op.resolved(aie_utils.get_current_device()) for op in (gemm, mha))
    assert [v.name for v in gemm.values] == ["valid", "n_tiles_valid"]
    assert gemm.derived_at("n_tiles_valid", valid=100) == 1 * (256 // gemm.mem_tile_n)
    assert [v.name for v in mha.values] == [
        "valid",
        "s_q",
        "s_kv",
        "q_blocks_valid",
        "kv_blocks_valid",
    ]
    assert mha.derived_at("s_q", valid=100) == 100
    assert mha.derived_at("q_blocks_valid", valid=100) == 1  # 128 padded / (64 x 2)
    assert mha.derived_at("kv_blocks_valid", valid=100) == 2  # ceil(100 / 64)
    (out,) = t.outputs
    assert out.bounds == {0: (t.values[0], 1)}  # O is bounded like Q
