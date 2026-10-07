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
from aie.iron import ceildiv
from aie.iron.device import from_name
from ml_dtypes import bfloat16

import iron
from iron.common import Carried, DispatchTime, Profile, Scratchpad
from iron.common.design.build import device_symbol
from iron.common.graph import Handle, TracedGraph, Tracer
from iron.common.graph.carried import attach_emit, compose
from iron.common.graph.compiled import _words
from iron.common.graph.fold import folded
from iron.common.graph.handle import Affine, Value
from iron.common.image import OperatorSequence
from iron.common.image.artifacts import Parameter
from iron.lm.layers import SwiGLU
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.emit import reference as emit_reference
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV, Epilogue
from iron.operators.mha import MHA
from iron.operators.repeat import Repeat
from iron.operators.rms_norm import RMSNorm
from iron.operators.silu import SiLU
from iron.tests.common.declare import Rows
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
            h = RMSNorm(x, weight=norm_w)  # a bare tensor is a weight
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

    ffn = Ffn()

    refs: dict[str, Any] = dict(
        w_gate=w_gate, w_up=w_up, w_down=w_down, norm_w=norm_w, cache=cache
    )
    return ffn, refs


def test_tracing_records_the_runlist_with_names_from_roles():
    ffn, refs = _ffn()
    t = ffn.trace(x=(1, E))
    assert isinstance(t, TracedGraph)
    assert [(type(op).__name__, *names) for op, *names in t.runlist] == [
        ("RMSNorm", "x", "w0", "rmsnorm0"),
        ("GEMV", "w1", "rmsnorm0", "gemv1"),
        ("GEMV", "w2", "rmsnorm0", "gemv2"),
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


def test_a_name_the_tracer_makes_up_never_aliases_one_it_was_given():
    class Held(iron.Graph):
        def __init__(self):
            self.out = iron.state((E,))
            self.silu0 = iron.weight(z(E))

        def body(self, x):
            Copy(SiLU(x), self.out)
            return ElementwiseAdd(SiLU(x), self.silu0)

    t = Held().trace(x=(E,))
    assert [(type(op).__name__, *names) for op, *names in t.runlist] == [
        ("SiLU", "x", "silu0_1"),
        ("Copy", "silu0_1", "out"),
        ("SiLU", "x", "silu1"),
        ("ElementwiseAdd", "silu1", "silu0", "out_1"),
    ]
    assert t.output_args == ["out_1"] and t.pinned == {"out": E * 2, "silu0": E * 2}

    class Given(iron.Graph):
        def body(self, out):
            return SiLU(out)

    t = Given().trace(out=(E,))
    assert t.input_args == ["out"] and t.output_args == ["out_1"]


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


def test_an_input_read_only_through_slices_is_laid_out_whole():
    class Halves(iron.Graph):
        def body(self, x):
            return SiLU(x[E // 2 :]), SiLU(x[: E // 2])

    t = Halves().trace(x=(E,))
    assert t.pinned == {"x": E * 2}
    seq = t.sequence()
    seq.prepare()
    assert seq.subbuffer_layout["x"] == ("input", 0, E * 2)
    assert seq.slice_info == {
        f"x[{E}:{2 * E}]": ("x", E, 2 * E),
        f"x[0:{E}]": ("x", 0, E),
    }


def test_alike_instances_bound_to_different_values_are_different_designs():
    """Two copies alike in every field, one indexed by ``a`` and one by ``b``,
    write through two symbols and build twice; two bound to one value share.
    """
    c1, c2, c3 = (iron.state((4, 64, 16)) for _ in range(3))

    class F(iron.Graph):
        def body(self, x, *, a: Scratchpad[np.int32], b: Scratchpad[np.int32]):
            Copy(x, c1[:, a])
            Copy(x, c2[:, b])
            Copy(x, c3[:, a])

    f = F()

    t = f.trace(x=(4, 16))
    by_value = {b.expression.value.name: b for b in t.bindings}
    assert len(t.bindings) == 3 and set(by_value) == {"a", "b"}
    first, second, third = t.bindings
    assert first.expression == t.values[0] * 16  # an element offset: a rows of 16
    assert first.op.bound_values == {"out_offset": "a_x16"}
    assert first.op.design_key() != second.op.design_key()
    assert first.op.design_key() == third.op.design_key()
    symbols = [device_symbol(b.op, b.member) for b in t.bindings]
    assert symbols[0] != symbols[1] and symbols[0] == symbols[2]
    assert symbols[0].endswith("_out_offset_a_x16")
    assert symbols[1].endswith("_out_offset_b_x16")


def test_an_explicit_instance_checks_its_operands_shapes():
    q = GEMV(M=256, K=E, num_aie_columns=8, tile_size_input=4, tile_size_output=32)
    w_t = z(E, 256)  # the weight transposed: the same element count

    class Step(iron.Graph):
        def body(self, x):
            return q(w_t, x)

    step = Step()

    with pytest.raises(ValueError, match=r"GEMV.A is \(256, 2048\)"):
        step.trace(x=(E,))


def test_binding_two_handles_to_one_instance_is_an_error():
    copy = Copy(input_buffer_size=64, output_buffer_size=64)

    class Two(iron.Graph):
        def body(self, x, *, a: Scratchpad[np.int32], b: Scratchpad[np.int32]):
            y = copy(x, out_offset=a)
            return copy(y, out_offset=b)

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
            return GEMV(w_b, GEMV(w_a, x, tile_size_output=32))

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
            return q(w, x)

    step = Step()

    t = step.trace(x=(E,))
    assert t.runlist[0][0] is q and t.output_args == ["out"]
    with pytest.raises(TypeError, match="inside a graph's body"):
        q(w, z(E))


def test_shape_mismatch_and_rank_rules():
    w = z(256, E)

    class Bad(iron.Graph):
        def body(self, x):
            return GEMV(w, x)

    bad = Bad()

    with pytest.raises(ValueError, match=r"K is 1024 from B.shape\[0\] but 2048"):
        bad.trace(x=(E // 2,))
    add = ElementwiseAdd

    class Flat(iron.Graph):
        def body(self, x, y):
            return add(x, y)  # a flat operator takes any rank

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
            return SiLU(x)

    g = G()

    t = g.trace(x=(1024,))
    assert [(v.name, v.kind) for v in t.values] == [("n", "dispatch")]


def test_returning_an_input_or_a_slice_is_refused():
    class Ident(iron.Graph):
        def body(self, x):
            return x

    ident = Ident()

    with pytest.raises(TypeError, match="returns its input"):
        ident.trace(x=(64,))

    class Part(iron.Graph):
        def body(self, x):
            return SiLU(x)[:8]

    part = Part()

    with pytest.raises(TypeError, match="whole handles"):
        part.trace(x=(64,))


# --------------------------------------------------------------------------
# SwiGLU, as a graph
# --------------------------------------------------------------------------


def test_swiglu_one_token_shares_one_array_and_one_build_for_gate_and_up():

    ffn = SwiGLU(z(H, E), z(H, E), z(E, H))
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
    assert (gate.M, gate.K, down.M, down.K) == (H, E, E, H)
    assert t.input_args == ["x"] and t.output_args == ["out"]
    with pytest.raises(ValueError, match="do not agree"):
        SwiGLU(z(H, E), z(H, E), z(H, E))


def test_swiglu_folds_its_silu_into_the_gate_and_keeps_one_array(npu2):
    t = SwiGLU(z(H, E), z(H, E), z(E, H)).trace(x=(1, E))
    f, count = folded(t, npu2)
    assert [(str(fold), n) for fold, n in count.items()] == [("SiLU into GEMV", 1)]
    assert [type(op).__name__ for op, *_ in f.runlist] == [
        "GEMV",
        "GEMV",
        "ElementwiseMul",
        "GEMV",
    ]
    gate, up, mul, down = f.steps
    assert (gate.op.epilogue, up.op.epilogue) == (Epilogue.SILU, Epilogue.NONE)
    assert gate.op.resolved().array_key() == up.op.resolved().array_key()
    assert gate.op.design_key() != up.op.design_key()
    assert down.op.epilogues == (Epilogue.NONE,)
    silu = next(s for s in t.steps if type(s.op) is SiLU)
    assert gate.outputs[0].name == silu.outputs[0].name == mul.inputs[0].name
    assert f.input_args == t.input_args and f.output_args == t.output_args


class _Gate(iron.Graph):
    def __init__(self, use, rows=H, tile=H // 8):
        self.w, self.use, self.tile = z(rows, E), use, tile

    def body(self, x):
        gate = GEMV(self.w, x, num_aie_columns=8, tile_size_output=self.tile)
        act = SiLU(gate)
        if self.use == "returned":
            return act, gate
        if self.use == "read twice":
            return ElementwiseAdd(act, gate)
        return act


@pytest.mark.parametrize("use", ["returned", "read twice"])
def test_a_fold_needs_the_intermediate_to_itself(use, npu2):
    t = _Gate(use).trace(x=(E,))
    assert folded(t, npu2) == (t, {})
    assert folded(_Gate("once").trace(x=(E,)), npu2)[1].total() == 1


def test_a_fold_the_producer_cannot_resolve_is_left_alone(npu2):
    # An output tile of 8 rows: silu's 32 lanes do not divide it.
    t = _Gate("once", rows=512, tile=8).trace(x=(E,))
    gemv, silu = (s.op for s in t.steps)
    with pytest.raises(ValueError, match="silu epilogue"):
        gemv.fold(silu).resolved(npu2)
    assert folded(t, npu2) == (t, {})


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


def test_swiglu_over_a_sequence_reads_the_weights_column_major():

    t = SwiGLU(z(H, E), z(H, E), z(E, H)).trace(x=(256, E))
    gemms = [s.op for s in t.steps if type(s.op) is GEMM]
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
    t = model.trace(**model.shapes(1))
    # A token takes no tensor. It returns the logits and carries the token
    # it draws and the position after it.
    assert t.input_args == [] and t.output_args == ["out", "carry_token"]
    # One function, so every version takes every value; a token binds two.
    assert [v.name for v in t.values] == ["token", "position", "chunk", "rows"]
    token, position = t.values[0], t.values[1]
    assert t.carry["position"] == Affine(position, 1, 1)
    assert {b.expression.value.name for b in t.bindings} == {"token", "position"}
    by_op = {id(b.op): b for b in t.bindings}
    embedding, angles = t.steps[0].op, t.steps[1].op
    assert by_op[id(embedding)].expression == Affine(token, cfg.emb_dim)
    assert by_op[id(angles)].expression == Affine(position, cfg.head_dim)
    draw = {b.member.name: b.expression for b in t.bindings if b.op is t.steps[-1].op}
    assert draw == {"row": Affine(position, 4), "at": Affine(position)}
    # The weights are named from the model; the caches are pinned state.
    assert "layers.1.q" in t.pinned and "keys.0" in t.pinned
    assert t.pinned["keys.0"] == cfg.n_kv_groups * L * cfg.head_dim * 2
    # Every MHA attends over the keys up to the position, its one query
    # packed by its heads.
    mhas = [s.op for s in t.steps if type(s.op) is MHA]
    assert all(op.kv_interleaved for op in mhas)
    assert len(mhas) == cfg.n_layers
    assert all(op.bound_values == {"kv_valid": "position_p1"} for op in mhas)
    assert all(op.packed and op.kv_len == L for op in mhas)
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
    # projection, a pipeline per KV head, one core for the norm.
    E, D = cfg.emb_dim, cfg.head_dim
    gemvs = [s.op for s in t.steps if type(s.op) is GEMV]
    q, k, v, o, gate, up, down = gemvs[:7]
    assert (q.tile_size_output, k.tile_size_output, o.tile_size_output) == (
        D // 2,
        D // 2,
        E // 8,
    )
    assert (down.tile_size_input, gate.tile_size_output) == (1, cfg.hidden_dim // 8)
    assert mhas[0].num_pipelines == cfg.n_kv_groups
    assert (
        next(
            s.op for s in t.steps if type(s.op) is RMSNorm and s.op.weighted
        ).num_aie_columns
        == 1
    )


def test_llama_prompt_traces_over_the_same_caches():

    g = small()
    cfg = g.config
    t = g.trace(**g.shapes(cfg.prefill_chunk))
    assert t.input_args == ["x"] and t.output_args == ["out", "carry_token"]
    assert [v.name for v in t.values] == ["token", "position", "chunk", "rows"]
    # MHA attends over the caches up to the chunk's last token.
    mha = next(op for op, *_ in t.runlist if type(op).__name__ == "MHA")
    assert mha.bound_values == {"valid": "rows", "kv_valid": "position_p1"}
    # The caches are the states a token's version reads: the same objects,
    # so one arena holds them once for both.
    token = g.trace(**g.shapes(1))
    assert set(t.states) == set(token.states)
    assert t.residents["keys.0"] == token.residents["keys.0"]
    assert set(t.weights) == set(token.weights)
    # Every projection reads the (out, in) checkpoint layout through the
    # column-major flag, which the trace carries into shape inference.
    gemms = [op for op, *_ in t.runlist if type(op).__name__ == "GEMM"]
    assert all(op.b_col_maj for op in gemms)
    K = {op.K for op in gemms}
    assert K == {cfg.emb_dim, cfg.hidden_dim, cfg.n_heads * cfg.head_dim}
    for op in t.operators:
        op.resolved(aie_utils.get_current_device())


@pytest.mark.parametrize("step", ["decode", "prompt"])
def test_llama_does_not_grow_with_the_context(step):
    """``max_seq_len`` sizes the caches, the RoPE table and the draws a
    position each and nothing else a decode step or a prompt chunk runs: a
    chunk's one input is its embedded tokens (a step's token is a value),
    every activation and every array is the same at a four times longer
    context, and attention is the caches' two writes and MHA, the reshapes
    and transposes between them views the DMA walks.
    """

    def trace(max_seq_len):
        g = small(max_seq_len=max_seq_len)
        rows = 1 if step == "decode" else g.config.prefill_chunk
        return g.trace(**g.shapes(rows))

    short, long = trace(64), trace(256)
    assert short.input_args == long.input_args == ([] if step == "decode" else ["x"])
    grown = {name for name, n in long.pinned.items() if short.pinned[name] != n}
    caches = {"keys.0", "keys.1", "values.0", "values.1"}
    assert grown == {"rope", "draws", "drawn"} | caches

    def activations(t):
        return {
            h.buffer_name: h.nbytes
            for s in t.steps
            for h in s.inputs + s.outputs
            if h.role not in ("weight", "state")
        }

    assert activations(short) == activations(long)
    assert [op.array_key() for op in short.operators] == [
        op.array_key() for op in long.operators
    ]
    kinds = [type(op).__name__ for op, *_ in long.runlist]
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


def test_llama_names_only_the_tunables_that_matter(monkeypatch):
    """Every keyword the llama graph passes is a choice resolution would not
    have made in some setting the graph is written for: the model's real
    shape at the graph's own defaults, on NPU2 (MHA's) for a decode step and
    a prompt; and the scaled-down shape the host tests trace, with the
    parameters that shape needs.
    """
    npu2 = from_name("npu2", n_cols=8)
    real, scaled = llama_1b(n_layers=1), small()
    C, S = real.config.prefill_chunk, scaled.config.prefill_chunk
    settings = [
        (npu2, lambda: real.trace(**real.shapes(1))),
        (npu2, lambda: real.trace(**real.shapes(C))),
        (npu2, lambda: scaled.trace(**scaled.shapes(S))),
    ]
    _every_keyword_is_load_bearing(monkeypatch, settings)


def test_a_bound_value_survives_tuning():
    copy = Copy(input_buffer_size=64, output_buffer_size=64)

    class F(iron.Graph):
        def body(self, x, *, a: Scratchpad[np.int32]):
            return copy(x, out_offset=a)

    f = F()

    f.trace(x=(64,))
    assert [v.name for v in copy.resolved(aie_utils.get_current_device()).values] == [
        "out_offset"
    ]


# --------------------------------------------------------------------------
# A bound on a handle: the first n of an axis are the valid ones this call
# --------------------------------------------------------------------------


def test_a_bound_travels_through_reshape_and_transpose():

    n = Value("n", "scratchpad", np.int32)
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


def test_per_call_values_are_integer_expressions():
    """Integer arithmetic on a per-call value is an ``Affine`` of it,
    which a binding writes and names its word by.
    """
    p = Value("p", "scratchpad", np.int32)
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
    with pytest.raises(TypeError, match="not linear"):
        _ = cache[(p + 1) // 2]


def test_an_index_before_a_bound_keeps_the_bound_on_its_axis():
    """``cache.reshape(G, L // C, C, D)[:, chunk, :rows]`` drops the chunk
    axis: the bound is on axis 1 of the view, and the index an offset of
    whole chunks.
    """
    chunk = Value("chunk", "scratchpad", np.int32)
    rows = Value("rows", "scratchpad", np.int32)
    G, L, C, D = 2, 64, 16, 8
    cache = Handle((G, L // C, C, D), bfloat16, "cache", "state")
    v = cache[:, chunk, : rows + 1]
    assert v.shape == (G, C, D) and v.bounds == {1: rows + 1}
    assert v.index_by == chunk * (C * D)

    keys = iron.state((G, L, D), name="keys")

    class Chunked(iron.Graph):
        def body(self, x, *, chunk: Scratchpad[np.int32], rows: Scratchpad[np.int32]):
            k = x[:rows].reshape(C, G, D).transpose(1, 0, 2)
            Copy(k, keys.reshape(G, L // C, C, D)[:, chunk, :rows])

    t = Chunked().trace(x=(C, G * D))
    (copy,) = t.operators
    assert copy.dst_bound == 1 and copy.bound_values == {
        "src_valid": "rows",
        "out_offset": f"chunk_x{C * D}",
        "dst_valid": "rows",
    }


def test_a_bound_rounds_up_to_the_tiles_it_ends_in(npu2):
    """A bound ending inside a tile takes the tile: the words of tiles per
    lane and the trip counts derived from it round up, so ``p + 1`` rows
    reach their last row; at a whole number of tiles nothing changes.
    """

    class G(iron.Graph):
        def body(self, x, y, *, p: Scratchpad[np.int32]):
            return ElementwiseAdd(x[: p + 1], y[: p + 1])

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
            return ElementwiseMul(ElementwiseAdd(x[: p + 1], y[: p + 1]), y[: p + 1])

    t = G().trace(x=(64, 512), y=(64, 512))
    alone, _ = _words(t)
    words, shared = _words(t, share=True)
    assert len(words) == 4
    assert sorted(set(shared.values())) == [
        "graph_p_x1d4p1d4_int32",
        "graph_p_x512p512_int32",
    ]
    for p in range(64):
        mine = {w.symbol: w({"p": p}) for w in words}
        for w in alone:
            assert mine[shared.get(w.symbol, w.symbol)] == w({"p": p})


def test_the_reference_writes_a_given_output_of_an_operator_that_returns_one(npu2):
    """GEMM's reference takes its inputs and returns its result; given an
    output, the graph's reference writes that result into it.
    """

    class Into(iron.Graph):
        def body(self, x, a, b):
            y = ElementwiseAdd(x, x)
            GEMM(a, b, y[:256])
            return y

    rng = np.random.default_rng(0)
    x = rng.integers(-4, 4, (512, 256)).astype(bfloat16)
    a = rng.integers(-2, 2, (256, 256)).astype(bfloat16)
    b = rng.integers(-2, 2, (256, 256)).astype(bfloat16)
    y = np.asarray(Into().reference(x, a, b))
    f = np.float32
    np.testing.assert_array_equal(y[:256], (a.astype(f) @ b.astype(f)).astype(bfloat16))
    np.testing.assert_array_equal(y[256:], x[256:] * 2)


def test_the_reference_computes_the_expressions(npu2):
    """The reference runs the body on numbers: ``p + 1`` is the row the
    copy writes, as the device's offset word is.
    """
    keys = iron.state((2, 8, 4), name="keys")

    class Write(iron.Graph):
        def body(self, x, *, p: Scratchpad[np.int32]):
            Copy(x, keys[:, p + 1])

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
            return Rows(x[:n].reshape(64 * 8, 1))  # rows x 8 seen as rows*8 x 1

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
    """Sums, products and floor divisions by powers of two (so ``ceildiv``)
    of an expression are expressions that compute the same; anything else
    is refused.
    """
    x = Affine(Value("x", "scratchpad", np.int32), 3, -5)
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
        (lambda v: v // 3, TypeError),
        (lambda v: (v // 4) * 3 // 2, TypeError),
        (lambda v: v // 1 if v else 0, TypeError),
        (lambda v: v % 64, TypeError),
        (lambda v: v < 0, TypeError),
        (lambda v: v + x, TypeError),
    ]
    for f, error in cases:
        if error is not None:
            with pytest.raises(error):
                f(x)
            continue
        form = f(x)
        assert form.value is x.value
        for v in range(-300, 300):
            assert form.evaluate({"x": v}) == f(3 * v - 5), v


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
            o = MHA(
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
            return ElementwiseAdd(x[:n], y[:n])

    g = G()

    t = g.trace(x=(64, 512), y=(64, 512))
    (b,) = t.bindings
    assert (b.member.name, b.expression) == ("valid", t.values[0] * 512)


def test_words_that_always_hold_one_number_share_it(npu2):
    """On a full ELF, two designs bound to one graph value write one word
    for each ratio of it they read (their extents; the tiles per lane of
    each operand), and every symbol that shares a word reads its own value
    there. A derivation the library cannot see through (``count``) keeps
    its own word.
    """

    class G(iron.Graph):
        def body(self, x, y, *, n: Scratchpad[np.int32]):
            return ElementwiseMul(ElementwiseAdd(x[:n], y[:n]), y[:n])

    g = G()

    t = g.trace(x=(64, 512), y=(64, 512))
    alone, _ = _words(t)
    words, shared = _words(t, share=True)
    assert len(alone) == 10 and len(words) == 4
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
            Copy(k, keys[:, :n])
            return Repeat(keys[:, :c], repeat=2)

    g = Cached()

    t = g.trace(x=(L, G * D))
    copy, rep = t.operators
    assert copy.src_bound == 1 and copy.dst_bound == 1
    assert copy.bound_values == {"src_valid": "n", "dst_valid": "n"}
    assert rep.bound_extents == {"valid_seq": "c"}
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


def test_gemm_bounds_its_compute_and_mha_its_compute_and_kv_traffic(npu2):
    """A bound reaches GEMM through A's rows and MHA through Q's padded
    length and K's and V's (select shapes): GEMM derives the counts its
    cores compute per call and keeps every descriptor; MHA derives its
    counts and the first query block, and patches its K and V descriptors'
    block count.
    """

    class G(iron.Graph):
        def body(self, x, w, *, n: Scratchpad[np.int32]):
            h = GEMM(x[:n], w, b_col_maj=True)  # (512, 64) x (256, 64)^T
            return MHA(
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
    assert gemm.bound_extents == {"valid": "n"}
    assert mha.bound_extents == {"valid": "n", "kv_valid": "n"}
    gemm, mha = (op.resolved(aie_utils.get_current_device()) for op in (gemm, mha))
    assert [v.name for v in gemm.values] == ["valid", "n_tiles_valid"]
    assert gemm.derived_at("n_tiles_valid", valid=100) == 1 * (256 // gemm.mem_tile_n)
    at = dict(valid=100, kv_valid=100)
    assert mha.derived_at("s_q", **at) == mha.derived_at("s_kv", **at) == 100
    assert mha.derived_at("q_blocks_valid", **at) == 1  # 128 padded / (64 x 2)
    assert mha.derived_at("kv_blocks", **at) == 2  # ceil(100 / 64)
    assert mha.derived_at("q_start", **at) == 0
    assert mha.derived_at("q_start", valid=64, kv_valid=192) == 2  # a later chunk
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
        y = Copy(self.table[r])
        return y if x is None else ElementwiseAdd(x, y)


def test_an_optional_input_gives_a_version_without_it():
    table = np.arange(4 * 256, dtype=np.int32).astype(bfloat16).reshape(4, 256)
    g = _Gather(table)
    alone, added = g.trace(), g.trace(x=(256,))
    assert alone.input_args == [] and added.input_args == ["x"]
    assert g.trace(x=None).input_args == []
    # The row is a view of the one table, indexed per call.
    (copy,) = alone.operators
    assert list(alone.weights) == [id(g.table)]
    assert [(b.member.name, b.expression) for b in alone.bindings] == [
        ("in_offset", alone.values[0] * 256)
    ]
    assert copy.bound_values == {"in_offset": "r_x256"}
    x = np.full(256, 2, dtype=bfloat16)
    np.testing.assert_array_equal(g.reference(r=1), table[1])
    np.testing.assert_array_equal(g.reference(None, r=1), table[1])
    np.testing.assert_array_equal(g.reference(x, r=3), table[3] + x)


def test_only_none_may_default_an_input():
    with pytest.raises(TypeError, match="may only default to None"):

        class _Bad(iron.Graph):
            def body(self, x=0):
                return x

    with pytest.raises(TypeError, match=r"inputs \['x'\] missing"):
        _Ffn = _ffn()[0]
        _Ffn(pos=0)


# --------------------------------------------------------------------------
# Carried values: the graph computes them for its own next call
# --------------------------------------------------------------------------


class _Walk(iron.Graph):
    """Walks a linked list one node per call: the next node is gathered from
    the successor table on the device, the step count is an expression of
    the current one. It takes no tensor.
    """

    def __init__(self, successor):
        self.successor = iron.weight(successor)

    def body(self, *, node: Carried[np.int32], steps: Carried[np.int32]):
        nxt = Copy(self.successor[node], dtype=np.int32)
        return iron.carry(node=nxt, steps=steps + 1)


def test_a_graph_carries_its_next_values():
    successor = np.random.default_rng(0).permutation(16).astype(np.int32)
    walk = _Walk(successor)
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
    successor = iron.weight(np.arange(1, 9, dtype=np.int32) % 8)

    class Walk(iron.Graph):
        def body(self, *, node: Carried[np.int32]):
            nxt = Copy(successor[node], dtype=np.int32)
            return nxt, iron.carry(node=nxt)

    t = Walk().trace()
    assert t.output_args == ["out"] and t.carry["node"] is t.returned[0]
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
            return iron.carry(a=Copy(rows[a]))

    with pytest.raises(TypeError, match="one whole element"):
        CarriesARow().trace()

    class CarriesTheWrongDtype(iron.Graph):
        def body(self, *, a: Carried[np.int16]):
            return iron.carry(a=Copy(table[a], dtype=np.int32))

    with pytest.raises(TypeError, match="but a is int16"):
        CarriesTheWrongDtype().trace()

    class CarriesTwice(iron.Graph):
        def body(self, *, a: Carried[np.int32]):
            return iron.carry(a=a + 1), iron.carry(a=a + 2)

    with pytest.raises(TypeError, match="returned last"):
        CarriesTwice().trace()


class _Trail(iron.Graph):
    """Walks a linked list and records each node at the step count. The
    version with ``jump`` starts from a table the host gives, at a plain
    per-call value; the one without follows the list from ``node``.
    """

    def __init__(self, successor, steps: int):
        self.successor = iron.weight(successor)
        self.trail = iron.state((steps + 1,), np.int32, name="trail")

    def body(
        self,
        jump=None,
        *,
        node: Carried[np.int32],
        steps: Carried[np.int32],
        skip: Scratchpad[np.int32],
    ):
        if jump is None:
            nxt = Copy(self.successor[node], dtype=np.int32)
        else:
            nxt = Copy(jump[skip], dtype=np.int32)
        Copy(nxt, self.trail[steps], dtype=np.int32)
        return iron.carry(node=nxt, steps=steps + 1)


def test_the_emit_program_follows_the_target_parameters():
    """Each word of the target's scratchpad comes from a carried value, in
    the target's order and encoding; anything else is refused.
    """
    walk = _Trail(np.arange(16, dtype=np.int32), steps=8)
    traced = walk.trace()
    assert traced.feedback == []  # tracing alone adds no Emit
    assert walk._carry is not None
    site = attach_emit(traced, walk._carried, walk._carry, slots=2)
    # The gathered node is computed into the carry's second plane.
    assert traced.runlist[0][-1] == "carry[8:12]"
    assert traced.runlist[-1][1:] == (
        "emit_program",
        "carry",
        "emit_image",
        "carry[0:8]",
    )
    assert traced.feedback == ["emit_image"] and traced.output_args == []

    words, _ = _words(traced)
    # A target laying the two out the other way, one as a core read.
    by_value = {w.linear.value: w.symbol for w in words if w.linear is not None}
    parameters = [
        Parameter(by_value["steps"], 0, "i32", "core"),
        Parameter(by_value["node"], 1, "i32", "addr"),
    ]
    program = compose(site, traced.carry, words, parameters)
    assert program.tolist() == [
        [0, 1, 1, 1, 0, 1, 0, 2],  # steps + 1, shifted for the core
        [1, 0, 1, 0, 0, 1, 0, 0],  # the node the device gathered
        [1, 0, 1, 0, 0, 1, 0, 0],  # the next node
        [0, 1, 1, 1, 0, 1, 0, 0],  # the next step count
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
