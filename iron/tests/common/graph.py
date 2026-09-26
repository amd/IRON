# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graph functions, traced device-free.

A graph function run on handles produces a runlist, buffer names and
sizes, and value bindings; nothing here needs a toolchain. What is not
checked here is the image: that is OperatorSequence's job and the
hardware tests' job.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common.declare import Carried, DispatchTime, Scratchpad
from iron.common.graph import Affine, Handle, TracedGraph
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv.op import GEMV, GEMVOverlay
from iron.operators.rms_norm import RMSNorm, WeightedRMSNorm
from iron.operators.silu import SiLU
from iron.operators.strided_copy import StridedCopy
import aie.utils as aie_utils

E, H = 2048, 8192


def z(*shape, dtype=bfloat16):
    return np.zeros(shape, dtype=dtype)


@pytest.fixture(autouse=True)
def device():
    """Trace against a real eight-column NPU2.

    The shim budget these graphs size themselves from used to be faked at 16
    here, which is what eight columns of NPU2 actually offers; binding the
    device says the same thing without the stub, and an overlay that reads
    ``dev.cols`` gets an answer.
    """
    import aie.utils as aie_utils
    from aie.iron.device import from_name

    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


def _ffn():
    w_gate, w_up, w_down, norm_w = z(H, E), z(H, E), z(E, H), z(E)
    cache = iron.state((4, 1024 * 64))

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
        StridedCopy(  # writes state; returns nothing
            act[: 4 * 64],
            cache,
            input_sizes=(4, 64),
            input_strides=(64, 1),
            input_offset=0,
            output_sizes=(1, 4, 64),
            output_strides=(0, 1024 * 64, 1),
            output_offset=0,
            out_offset=pos,
        )
        return GEMV(w_down, act, num_aie_columns=8, tile_size_output=E // 8)

    return ffn, dict(
        w_gate=w_gate, w_up=w_up, w_down=w_down, norm_w=norm_w, cache=cache
    )


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
        ("StridedCopy", "elementwisemul4[0:512]", "state0"),
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


def test_overlays_are_shared_by_design_key_and_extents_are_not():
    ffn, _ = _ffn()
    t = ffn.trace(x=(1, E))
    gate, up, down = (s.op for s in t.steps if type(s.op) is GEMV)
    assert gate.ov is up.ov and gate is not up  # one array, two operators
    assert down.ov is not gate.ov  # a different K is a different array
    assert [type(o).__name__ for o in t.overlays] == [
        "WeightedRMSNormOverlay",
        "GEMVOverlay",
        "SiLUOverlay",
        "ElementwiseMulOverlay",
        "StridedCopyOverlay",
        "GEMVOverlay",
    ]
    assert (gate.M, gate.ov.K, gate.num_batches) == (H, E, 1)


def test_per_call_values_bind_to_the_operator_and_enable_it():
    ffn, _ = _ffn()
    t = ffn.trace(x=(1, E))
    (binding,) = t.bindings
    op, value = binding.op, binding.value
    assert type(op) is StridedCopy and binding.member.name == "out_offset"
    assert value.name == "pos" and value.kind == "scratchpad"
    assert op.uses_value("out_offset") and not op.uses_value("in_offset")
    assert [v.name for v in op.values] == ["out_offset"]


def test_every_traced_operator_tunes_from_the_device_alone():
    ffn, _ = _ffn()
    t = ffn.trace(x=(1, E))
    for op in t.operators:
        op.tuned(
            aie_utils.get_current_device()
        )  # every default fills; every extent is compatible
    silu = next(s.op for s in t.steps if type(s.op) is SiLU).tuned(
        aie_utils.get_current_device()
    )
    assert (silu.ov.num_aie_columns, silu.ov.num_channels, silu.ov.tile_size) == (
        8,
        1,
        256,
    )
    norm = next(s.op for s in t.steps if type(s.op) is WeightedRMSNorm).tuned(
        aie_utils.get_current_device()
    )
    assert norm.ov.num_aie_columns == 1  # one row: one core


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


def test_binding_two_handles_to_one_instance_is_an_error():
    copy = StridedCopy(
        input_sizes=(64,),
        input_strides=(1,),
        input_offset=0,
        output_sizes=(64,),
        output_strides=(1,),
        output_offset=0,
        input_buffer_size=64,
        output_buffer_size=64,
    )

    @iron.graph
    def two(x, *, a: Scratchpad[np.int32], b: Scratchpad[np.int32]):
        y = copy(x, out_offset=a)
        return copy(y, out_offset=b)

    with pytest.raises(ValueError, match=r"bound to Affine\(a\)"):
        two.trace(x=(64,))


def test_an_explicit_instance_is_applied_like_the_class():
    ov = GEMVOverlay(K=E, num_aie_columns=8, tile_size_input=4, tile_size_output=32)
    q = GEMV(ov, M=256)
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
    assert gate.ov is up.ov and gate.design_key() == up.design_key()
    assert down.design_key() != gate.design_key()
    assert (gate.ov.num_aie_columns, gate.ov.tile_size_output) == (8, H // 8)
    assert t.input_args == ["x"] and t.output_args == ["out"]
    with pytest.raises(ValueError, match="do not agree"):
        m.swiglu_decode(z(H, E), z(H, E), z(H, E))


def test_swiglu_prefill_traces_over_a_sequence():
    import iron.operators.swiglu_prefill.op as m
    from iron.operators.gemm.op import GEMM

    ffn = m.swiglu_prefill(z(E, H), z(E, H), z(H, E))
    t = ffn.trace(x=(256, E))
    gemms = [s.op for s in t.steps if type(s.op) is GEMM]
    assert [(g.M, g.K, g.N) for g in gemms] == [(256, E, H), (256, E, H), (256, H, E)]
    assert gemms[0].ov is gemms[1].ov
    silu = next(s.op for s in t.steps if type(s.op) is SiLU)
    assert silu.size == 256 * H


# --------------------------------------------------------------------------
# llama decode, traced at a scaled-down configuration
# --------------------------------------------------------------------------


def test_llama_decode_traces_and_tunes():
    from iron.tests.common.llama_model import Config as _Config

    from iron.applications.llama_3_2_1b.graphs import LlamaGraph

    cfg = _Config()
    L = 256
    t = LlamaGraph(cfg, L).trace(cfg, 1)
    kinds = [type(op).__name__ for op, *_ in t.runlist]
    gathers = ["StridedCopy", "StridedCopy"]  # the token's embedding, its angles
    per_block = [
        "WeightedRMSNorm",
        "GEMV",
        "GEMV",
        "GEMV",
        "RoPE",
        "RoPE",
        "StridedCopy",
        "StridedCopy",
        "Repeat",
        "Repeat",
        "GEMV",
        "ElementwiseMul",
        "DynamicSoftmax",
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
    assert kinds == gathers + per_block * cfg.n_layers + ["WeightedRMSNorm", "GEMV"]
    # A token takes no tensor: its rows are gathered from the tables.
    assert t.input_args == [] and t.output_args == ["out"]
    assert [v.name for v in t.values] == ["token", "position"]
    embedding, angles = t.steps[0].op, t.steps[1].op
    by_op = {id(b.op): b for b in t.bindings}
    assert by_op[id(embedding)].expression == Affine(t.values[0], cfg.emb_dim)
    assert by_op[id(angles)].expression == Affine(t.values[1], cfg.head_dim)
    assert embedding.ov is angles.ov  # one design, back to back
    # The weights are named from the model; the caches are pinned state.
    assert "layers.1.attn.q.weight" in t.pinned and "keys_cache_0" in t.pinned
    assert t.pinned["keys_cache_0"] == cfg.n_kv_groups * L * cfg.head_dim * 2
    # One strided copy instance per layer writes the row at the position, on
    # both of its call sites; every softmax sees position + 1 keys.
    position = t.values[1]
    copies = [b for b in t.bindings if b.member.name == "out_offset"]
    assert len(copies) == cfg.n_layers * 2
    assert {b.expression for b in copies} == {Affine(position, cfg.head_dim)}
    softmaxes = [b for b in t.bindings if b.member.name == "vector_size"]
    assert len(softmaxes) == cfg.n_layers
    assert {b.expression for b in softmaxes} == {Affine(position, 1, 1)}
    assert type(softmaxes[0].op.ov).__name__ == "DynamicSoftmaxOverlay"
    # The same array serves every layer's like projections.
    q_ovs = {
        id(s.op.ov)
        for s in t.steps
        if type(s.op) is GEMV
        and s.op.M == cfg.n_heads * cfg.head_dim
        and s.op.ov.K == cfg.emb_dim
    }
    assert len(q_ovs) == 1
    # Every operator tunes and is compatible on an 8-column device.
    for op in t.operators:
        op.tuned(aie_utils.get_current_device())


def test_llama_prompt_traces_over_the_same_caches():
    from iron.tests.common.llama_model import Config as _Config

    from iron.applications.llama_3_2_1b.graphs import LlamaGraph

    cfg = _Config()
    L = cfg.context_length
    g = LlamaGraph(cfg, L, num_aie_columns=4, num_of_pipelines=1, tile_m=16)
    t = g.trace(cfg, L)
    kinds = [type(op).__name__ for op, *_ in t.runlist]
    per_block = [
        "WeightedRMSNorm",
        "GEMM",
        "GEMM",
        "GEMM",
        "RoPE",
        "RoPE",
        "StridedCopy",
        "StridedCopy",
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
    tail = ["StridedCopy", "WeightedRMSNorm", "GEMV"]
    assert kinds == per_block * cfg.n_layers + tail
    assert t.input_args == ["x"] and t.output_args == ["out"]
    assert [v.name for v in t.values] == ["token", "position"]
    # The caches are the states a token's version reads: the same objects,
    # so one arena holds them once for both.
    token = g.trace(cfg, 1)
    assert set(t.states) == set(token.states)
    assert t.residents["keys_cache_0"] == token.residents["keys_cache_0"]
    # A prompt's MHA takes no scale table. Both versions read the same RoPE
    # table, and the embedding a token gathers from is the tied output head.
    assert set(t.weights) == set(token.weights) - {id(g.scale)}
    assert {id(g.rope), id(cfg.weights.embedding)} <= set(t.weights)
    # Every projection reads the (out, in) checkpoint layout through the
    # column-major flag, which the trace carries into shape inference.
    gemms = [op for op, *_ in t.runlist if type(op).__name__ == "GEMM"]
    assert all(op.ov.b_col_maj for op in gemms)
    K = {op.K for op in gemms}
    assert K == {cfg.emb_dim, cfg.hidden_dim, cfg.n_heads * cfg.head_dim}
    # The last-row copy is the one operator bound to a per-call value: the
    # position of the last prompt row, in elements.
    assert [(type(b.op).__name__, b.member.name) for b in t.bindings] == [
        ("StridedCopy", "in_offset")
    ]
    assert t.bindings[0].expression == Affine(t.values[1], cfg.emb_dim)
    for op in t.operators:
        op.tuned(aie_utils.get_current_device())


def test_a_bound_value_survives_tuning():
    copy = StridedCopy(
        input_sizes=(64,),
        input_strides=(1,),
        input_offset=0,
        output_sizes=(64,),
        output_strides=(1,),
        output_offset=0,
        input_buffer_size=64,
        output_buffer_size=64,
    )

    @iron.graph
    def f(x, *, a: Scratchpad[np.int32]):
        return copy(x, out_offset=a)

    f.trace(x=(64,))
    assert [v.name for v in copy.tuned(aie_utils.get_current_device()).values] == [
        "out_offset"
    ]


def _row_copy(n, rows):
    """A copy of one ``n``-element row out of a ``(rows, n)`` table."""
    return StridedCopy(
        input_sizes=(n,),
        input_strides=(1,),
        input_offset=0,
        output_sizes=(n,),
        output_strides=(1,),
        output_offset=0,
        input_buffer_size=rows * n,
        output_buffer_size=n,
    )


def test_integer_arithmetic_on_a_value_binds_an_expression():
    table = np.arange(4 * 64, dtype=np.int32).astype(bfloat16).reshape(4, 64)
    copy = _row_copy(64, 4)

    @iron.graph
    def row(*, r: Scratchpad[np.int32]):
        return copy(table, in_offset=(r + 1) * 64)

    t = row.trace()
    (binding,) = t.bindings
    assert binding.expression == Affine(t.values[0], 64, 64)
    assert binding.expression.evaluate({"r": 2}) == 192
    np.testing.assert_array_equal(row.reference(r=2), table[3])
    with pytest.raises(TypeError, match="unsupported operand"):
        t.values[0] * 0.5


def test_an_optional_input_gives_a_version_without_it():
    table = np.ones((4, 64), dtype=bfloat16)
    gather, add = _row_copy(64, 4), ElementwiseAdd(size=64)

    @iron.graph
    def f(x=None, *, r: Scratchpad[np.int32]):
        y = gather(table, in_offset=r * 64)
        return y if x is None else add(x, y)

    assert f.trace().input_args == []
    assert f.trace(x=(64,)).input_args == ["x"]
    x = np.full(64, 2, dtype=bfloat16)
    np.testing.assert_array_equal(f.reference(r=1), table[1])
    np.testing.assert_array_equal(f.reference(x, r=1), table[1] + x)


def _successor_walk(successor):
    """A graph that walks a linked list one node per call: the next node is
    gathered from the successor table on the device, the step count is an
    expression of the current one. It takes no tensor."""
    n = successor.shape[0]
    gather = StridedCopy(
        input_sizes=(1,),
        input_strides=(1,),
        input_offset=0,
        output_sizes=(1,),
        output_strides=(1,),
        output_offset=0,
        input_buffer_size=n,
        output_buffer_size=1,
        dtype=np.int32,
    )

    @iron.graph
    def walk(*, node: Carried[np.int32], steps: Carried[np.int32]):
        return iron.carry(node=gather(successor, in_offset=node), steps=steps + 1)

    return walk


def test_a_graph_carries_its_next_values():
    successor = np.random.default_rng(0).permutation(16).astype(np.int32)
    walk = _successor_walk(successor)
    t = walk.trace()
    assert [(v.name, v.carried) for v in t.values] == [
        ("node", True),
        ("steps", True),
    ]
    assert t.input_args == [] and t.returned == []
    # The gathered node is an output buffer, so the host can read it back.
    assert t.output_args == ["carry_node"] and t.carry["node"] is t.outputs[0]
    assert t.runlist[0][-1] == "carry_node"
    assert t.carry["steps"] == Affine(t.values[1], 1, 1)
    node, steps = 3, 0
    for _ in range(5):
        nxt = walk.reference(node=node, steps=steps)
        assert dict(nxt) == {"node": successor[node], "steps": steps + 1}
        node, steps = nxt["node"], nxt["steps"]


def test_a_carried_handle_may_also_be_returned():
    successor = np.arange(1, 9, dtype=np.int32) % 8
    gather = _successor_walk(successor).trace().steps[0].op

    @iron.graph
    def walk(*, node: Carried[np.int32]):
        nxt = gather(successor, in_offset=node)
        return nxt, iron.carry(node=nxt)

    t = walk.trace()
    assert t.output_args == ["out"] and t.carry["node"] is t.returned[0]
    out, nxt = walk.reference(node=7)
    assert out.reshape(-1)[0] == 0 and nxt["node"] == 0


def test_every_carried_value_is_carried_and_nothing_else():
    table = np.zeros(8, dtype=np.int32)
    gather = _successor_walk(table).trace().steps[0].op

    @iron.graph
    def forgets(*, a: Carried[np.int32], b: Carried[np.int32]):
        return iron.carry(a=a + 1)

    with pytest.raises(TypeError, match=r"return iron.carry\(b=\.\.\.\)"):
        forgets.trace()

    @iron.graph
    def carries_a_plain_value(*, a: Scratchpad[np.int32]):
        return iron.carry(a=a + 1)

    with pytest.raises(TypeError, match="Carried values are"):
        carries_a_plain_value.trace()

    @iron.graph
    def carries_a_constant(*, a: Carried[np.int32]):
        return iron.carry(a=5)

    with pytest.raises(TypeError, match="expression of the values"):
        carries_a_constant.trace()

    wide = _row_copy(64, 4)
    rows = np.zeros((4, 64), dtype=bfloat16)

    @iron.graph
    def carries_a_row(*, a: Carried[np.int32]):
        return iron.carry(a=wide(rows, in_offset=a * 64))

    with pytest.raises(TypeError, match="one whole element"):
        carries_a_row.trace()

    @iron.graph
    def carries_the_wrong_dtype(*, a: Carried[np.int16]):
        return iron.carry(a=gather(table, in_offset=a))

    with pytest.raises(TypeError, match="but a is int16"):
        carries_the_wrong_dtype.trace()
