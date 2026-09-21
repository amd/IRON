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
from iron.common.declare import DispatchTime, Scratchpad
from iron.common.graph import Handle, State, TracedGraph
from iron.operators.elementwise_add.op import ElementwiseAdd
from iron.operators.elementwise_mul.op import ElementwiseMul
from iron.operators.gemv.op import GEMV, GEMVOverlay
from iron.operators.rms_norm.op import RMSNorm, WeightedRMSNorm
from iron.operators.silu.op import SiLU
from iron.operators.strided_copy.op import StridedCopy

E, H = 2048, 8192


def z(*shape, dtype=bfloat16):
    return np.zeros(shape, dtype=dtype)


class Dev:
    cols = 8

    def resolve(self):
        class R:
            name = "npu2"

        return R()


@pytest.fixture(autouse=True)
def shim_limit(monkeypatch):
    import iron.common.operator_bases as bases
    import iron.operators.rms_norm.op as rms

    monkeypatch.setattr(bases, "get_shim_dma_limit", lambda dev: 16)
    monkeypatch.setattr(rms, "get_shim_dma_limit", lambda dev: 16)


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
    ((op, member, value),) = t.bindings
    assert type(op) is StridedCopy and member == "out_offset"
    assert value.name == "pos" and value.kind == "scratchpad"
    assert op.uses_value("out_offset") and not op.uses_value("in_offset")
    assert [v.name for v in op.values] == ["out_offset"]


def test_every_traced_operator_tunes_from_the_device_alone():
    ffn, _ = _ffn()
    t = ffn.trace(x=(1, E))
    for op in t.operators:
        op.tuned(Dev())  # every default fills; every extent is compatible
    silu = next(s.op for s in t.steps if type(s.op) is SiLU).tuned(Dev())
    assert (silu.ov.num_aie_columns, silu.ov.num_channels, silu.ov.tile_size) == (
        8,
        1,
        256,
    )
    norm = next(s.op for s in t.steps if type(s.op) is WeightedRMSNorm).tuned(Dev())
    assert norm.ov.num_aie_columns == 1  # one row: one core


def test_a_state_written_by_one_step_is_pinned_and_readable():
    ffn, refs = _ffn()
    t = ffn.trace(x=(1, E))
    handle = t.states[id(refs["cache"])]
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

    with pytest.raises(ValueError, match="bound to Value\\('a'"):
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


def test_swiglu_decode_shares_one_array_and_one_build_for_gate_and_up(monkeypatch):
    import iron.operators.swiglu_decode.op as m

    monkeypatch.setattr(m, "get_shim_dma_limit", lambda dev: 16)
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


def test_swiglu_prefill_traces_over_a_sequence(monkeypatch):
    import iron.operators.swiglu_prefill.op as m
    from iron.operators.gemm.op import GEMM

    monkeypatch.setattr(m, "get_shim_dma_limit", lambda dev: 16)
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


class _Param:
    def __init__(self, shape):
        self.weight = z(*shape)


class _Block:
    def __init__(self, E, H, G, D, F):
        self.norm1, self.norm2 = _Param((E,)), _Param((E,))
        self.attn = type("attn", (), {})()
        self.attn.q, self.attn.k = _Param((H * D, E)), _Param((G * D, E))
        self.attn.v, self.attn.o = _Param((G * D, E)), _Param((E, H * D))
        self.ffn = type("ffn", (), {})()
        self.ffn.gate, self.ffn.up = _Param((F, E)), _Param((F, E))
        self.ffn.down = _Param((E, F))


class _Model:
    def __init__(self, cfg):
        self.layers = [
            _Block(
                cfg.emb_dim, cfg.n_heads, cfg.n_kv_groups, cfg.head_dim, cfg.hidden_dim
            )
            for _ in range(cfg.n_layers)
        ]
        self.norm = _Param((cfg.emb_dim,))
        self.out_head = _Param((cfg.vocab_size, cfg.emb_dim))

    def named_parameters(self):
        for i, blk in enumerate(self.layers):
            for path in (
                "norm1",
                "norm2",
                "attn.q",
                "attn.k",
                "attn.v",
                "attn.o",
                "ffn.gate",
                "ffn.up",
                "ffn.down",
            ):
                obj = blk
                for part in path.split("."):
                    obj = getattr(obj, part)
                yield f"layers.{i}.{path}.weight", obj.weight
        yield "norm.weight", self.norm.weight
        yield "out_head.weight", self.out_head.weight


class _Config:
    n_layers, n_heads, n_kv_groups, head_dim = 2, 16, 4, 64
    emb_dim, hidden_dim, vocab_size = 256, 512, 1024

    def __init__(self):
        self.model = _Model(self)


def test_llama_decode_traces_and_tunes(monkeypatch):
    import sys

    sys.path.insert(0, "iron/applications/llama_3.2_1b")
    from decode_graph import DecodeGraph

    cfg = _Config()
    L = 256
    dg = DecodeGraph(cfg, L)
    t = dg.trace(cfg)
    kinds = [type(op).__name__ for op, *_ in t.runlist]
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
    assert [v.name for v in t.values] == ["cache_offset", "vector_size"]
    # The weights are named from the model; the caches are pinned state.
    assert "layers.1.attn.q.weight" in t.pinned and "keys_cache_0" in t.pinned
    assert t.pinned["keys_cache_0"] == cfg.n_kv_groups * L * cfg.head_dim * 2
    # One strided copy instance per layer is bound to cache_offset on both of
    # its call sites; every softmax binds vector_size on its overlay.
    copies = [(op, n) for op, n, v in t.bindings if v.name == "cache_offset"]
    assert len(copies) == cfg.n_layers * 2 and all(n == "out_offset" for _, n in copies)
    softmaxes = [op for op, n, v in t.bindings if v.name == "vector_size"]
    assert len(softmaxes) == cfg.n_layers
    assert type(softmaxes[0].ov).__name__ == "DynamicSoftmaxOverlay"
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
        op.tuned(Dev())


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
    assert [v.name for v in copy.tuned(Dev()).values] == ["out_offset"]
