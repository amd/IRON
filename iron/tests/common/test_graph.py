# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graph functions, recorded device-free.

A graph function run on handles produces a runlist, buffer names and
sizes, and value bindings; nothing here needs a toolchain.
"""

import inspect
from types import SimpleNamespace
from typing import Any

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron import ceildiv
from aie.helpers.taplib import Affine, PerCall, TensorAccessPattern
from aie.iron.device import from_name
from ml_dtypes import bfloat16

import iron
from iron import Carried, Precision, Profile, Scratchpad
from iron.common.graph import Handle
from iron.common.graph.handle import Dense
from iron.common.graph.record import Recording, Recorder
from iron.common.graph.carried import attach_emit, compose
from iron.common.graph.compiled import CompiledGraph, _words
from iron.common.image.link import PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, SequenceStep
from iron.common.image.artifacts import Parameter
from iron.common.image.packaging import Kind, require_device
import iron.functional as F
from iron.tests.support.graphs import FeedForward
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.emit import UNCLAMPED, reference as emit_reference
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.gemm.op import ProjectionGEMM
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.relu import ReLU
from iron.operators.rms_norm import RMSNorm
from iron.operators.silu import SiLU
from iron.operators.softmax import Softmax
from iron.tests.support.declare import Rows
from iron.tests.support.graphs import Trail, Walk
from iron.tests.support.llama_model import llama_1b, small

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
    t = ffn.record(x=(1, E))
    assert isinstance(t, Recording)
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

    t = Held().record(x=(E,))
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

    t = Given().record(out=(E,))
    assert [h.name for h in t.inputs] == ["out"] and [h.name for h in t.outputs] == [
        "out_1"
    ]


def test_arrays_are_shared_by_array_key_and_extents_are_not():
    ffn, _ = _ffn()
    t = ffn.record(x=(1, E))
    gate, up, down = (s.op for s in t.steps if type(s.op) is GEMV)
    assert (
        gate.array_key() == up.array_key() and gate is not up
    )  # one array, two operators
    assert gate.design_key() == up.design_key()
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
    t = ffn.record(x=(1, E))
    (binding,) = t.bindings
    op, value = binding.op, binding.expression.value
    assert type(op) is Copy and binding.member.name == "out_offset"
    assert value.name == "pos" and value.marker is Kind.SCRATCHPAD
    assert op.value("out_offset").per_call and not op.value("in_offset").per_call
    assert [v.name for v in op.values] == ["out_offset"]


def test_every_recorded_operator_tunes_from_the_device_alone():
    ffn, _ = _ffn()
    t = ffn.record(x=(1, E))
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
    t = ffn.record(x=(1, E))
    state, handle = t.states[id(refs["cache"])]
    assert state is refs["cache"]
    assert handle.role == "state" and handle.name == "state0"
    assert refs["cache"].name == "state0"


def test_slices_are_views_into_the_parent_in_bytes():
    h = Handle.whole((8, 64), bfloat16, "acts", "intermediate")
    part = h[2:4]
    assert part.shape == (2, 64) and part.ref() == BufferRef("acts", 256, 256)
    assert h[3].shape == (64,) and h[3].ref() == BufferRef("acts", 384, 128)
    assert part[1].ref() == BufferRef("acts", 384, 128)
    assert part[1, 2:6].ref() == BufferRef("acts", 388, 8)
    with pytest.raises(TypeError, match="a view, which only a copy takes"):
        h.transpose(1, 0)[0]
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

    t = Halves().record(x=(E,))
    assert t.pinned == {"x": E * 2}
    seq = Image(t, PerStep())
    seq._prepare()
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

    t = f.record(x=(4, 16))
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


def test_binding_two_handles_to_one_instance_is_an_error():
    copy = Copy(input_buffer_size=64, output_buffer_size=64)

    class Two(iron.Graph):
        def body(self, x, *, a: Scratchpad[np.int32], b: Scratchpad[np.int32]):
            y = copy(x, out_offset=a)
            return copy(y, out_offset=b)

    two = Two()

    with pytest.raises(ValueError, match="bound to a at an earlier call site"):
        two.record(x=(64,))


def test_a_graph_carries_its_profile():
    """A graph's profile reaches every run of the body: the
    record and the host reference alike, with a call's own keyword kept.
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

    a, b = (s.op for s in two.record(x=(E,)).steps)
    assert (a.tile_size_input, a.tile_size_output) == (4, 32)  # the call's own
    assert (b.tile_size_input, b.tile_size_output) == (4, E // 8)  # the profile's
    assert two.reference(z(E)).shape == (E,)  # constructs under the profile too
    assert GEMV(M=E, K=256).tile_size_output is None  # nothing outside it


def test_a_graph_reads_as_its_name_and_recorded_shapes():
    w = z(256, E)

    class Project(iron.Graph):
        def body(self, x):
            return GEMV.step(w, x)

    project = Project()
    project.reference(z(E))
    assert repr(project).startswith(f"Project(x=({E},) ")
    assert "weights" not in repr(project.record(x=(E,)))


def test_an_explicit_instance_is_applied_like_the_class():
    q = GEMV(M=256, K=E, num_aie_columns=8, tile_size_input=4, tile_size_output=32)

    class Step(iron.Graph):
        def __init__(self, w):
            self.w = iron.param(w)

        def body(self, x):
            return q(self.w, x)

    w = z(256, E)
    t = Step(w).record(x=(E,))
    assert t.steps[0].op is q and [h.name for h in t.outputs] == ["out"]
    with pytest.raises(TypeError, match="outside a graph's body on device tensors"):
        q(w, z(E))
    # The weight transposed: the same element count, refused by its shape.
    with pytest.raises(ValueError, match=r"M is 2048 from A.shape\[0\] but 256"):
        Step(z(E, 256)).record(x=(E,))


def test_shape_mismatch_and_rank_rules():
    w = z(256, E)

    class Bad(iron.Graph):
        def body(self, x):
            return GEMV.step(w, x)

    bad = Bad()

    with pytest.raises(ValueError, match=r"K is 1024 from B.shape\[0\] but 2048"):
        bad.record(x=(E // 2,))
    add = ElementwiseAdd

    class Flat(iron.Graph):
        def body(self, x, y):
            return add.step(x, y)  # a flat operator takes any rank

    flat = Flat()

    t = flat.record(x=(4, 512), y=(4, 512))
    assert t.steps[0].op.size == 2048 and t.outputs[0].shape == (4, 512)


def test_no_npu_says_how_to_compile_without_one(monkeypatch):
    monkeypatch.setattr(aie_utils, "ensure_current_device", lambda: None)
    monkeypatch.delenv("NPU_RUNTIME", raising=False)
    with pytest.raises(
        RuntimeError,
        match=r"no NPU found \(NPU_RUNTIME unset; is the driver loaded\? .*"
        r"pass dev=NPU2\(\) \(aie\.iron\.device\) or bind one",
    ):
        require_device()
    monkeypatch.setenv("NPU_RUNTIME", "xrt")
    with pytest.raises(RuntimeError, match=r"\(NPU_RUNTIME=xrt; "):
        require_device()


def test_keyword_only_parameters_must_be_annotated_as_values():
    with pytest.raises(TypeError, match="annotated Scratchpad"):

        class F(iron.Graph):
            def body(self, x, *, n):
                return x


def test_returning_an_input_or_a_slice_is_refused():
    class Ident(iron.Graph):
        def body(self, x):
            return x

    ident = Ident()

    with pytest.raises(TypeError, match="returns its input"):
        ident.record(x=(64,))

    class Part(iron.Graph):
        def body(self, x):
            return SiLU.step(x)[:8]

    part = Part()

    with pytest.raises(TypeError, match="whole handles"):
        part.record(x=(64,))


# --------------------------------------------------------------------------
# A gated feed-forward, as a graph
# --------------------------------------------------------------------------


def test_a_matvec_whose_columns_are_given_resolves_with_no_device():
    """What ``resolved()`` asks on a host with none bound: no memory to
    hold the cores to, so none is checked.
    """
    op = GEMV(M=256, K=64, num_aie_columns=1, num_channels=1, tile_size_output=32)
    assert op.resolve(None).tile_size_input == 2


def test_two_spellings_of_one_array_are_one_design():
    """Identity is taken after resolution: a tunable left to resolve and the same
    tunable given its resolved value name one array, and a sequence builds it
    once. Every operator of a recorded graph goes through the same point, so
    the design counts here are the gate on it.
    """
    a = GEMV(M=64, K=256, num_aie_columns=2, tile_size_input=2)
    b = GEMV(M=64, K=256, num_aie_columns=2, tile_size_input=2, tile_size_output=2)
    assert a.design_key() != b.design_key()  # as given
    seq = Image(
        Recording.of_steps(
            "two_spellings",
            [
                SequenceStep(a, (BufferRef("x"), BufferRef("w"), BufferRef("y"))),
                SequenceStep(b, (BufferRef("x2"), BufferRef("w"), BufferRef("z"))),
            ],
            ["x", "x2", "w"],
            ["z"],
        ),
        PerStep(),
    )
    seq._prepare()
    designs, _ = seq.unique_designs()
    assert len(designs) == 1 and designs[0].tile_size_output == 2
    ffn, _ = _ffn()
    seq = Image(ffn.record(x=(1, E)), PerStep())
    seq._prepare()
    assert len(seq.unique_designs()[0]) == 6


def test_swiglu_over_a_sequence_reads_the_weights_column_major():

    t = FeedForward(z(H, E), z(H, E), z(E, H)).record(x=(256, E))
    gemms = [s.op for s in t.steps if type(s.op) is ProjectionGEMM]
    assert [(g.M, g.K, g.N) for g in gemms] == [(256, E, H), (256, E, H), (256, H, E)]
    assert all(g.b_col_maj for g in gemms)
    assert gemms[0].array_key() == gemms[1].array_key()
    silu = next(s.op for s in t.steps if type(s.op) is SiLU)
    assert silu.size == 256 * H


# --------------------------------------------------------------------------
# llama decode, recorded at a scaled-down configuration
# --------------------------------------------------------------------------


def test_llama_decode_records_and_tunes():

    L = 256
    model = small(max_seq_len=L)
    cfg = model.config
    t = model.record(**model.shapes()[0])
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
    # The weights are pinned, and so are the caches, as state.
    layers = model.model.layers
    assert id(layers[1].self_attn.q_proj.weight) in t.weights
    _, keys = t.states[id(layers[0].cache.keys)]
    assert t.pinned[keys.name] == cfg.num_key_value_heads * L * cfg.head_dim * 2
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


def test_llama_prompt_records_over_the_same_caches():

    g = small()
    cfg = g.config
    t = g.record(**g.shapes()[1])
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
    token = g.record(**g.shapes()[0])
    assert set(t.states) == set(token.states)
    keys = "model.layers.0.cache.keys"
    assert t.residents[keys] == token.residents[keys]
    assert set(t.weights) == set(token.weights)
    # Every projection reads the (out, in) checkpoint layout through the
    # column-major flag, which the recording carries into shape inference.
    gemms = [s.op for s in t.steps if type(s.op) is ProjectionGEMM]
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
    t = g.record(**g.shapes()[1])
    ops = [s.op for s in t.steps]
    assert not any(type(op) is GEMM for op in ops)
    gemms = [op for op in ops if type(op) is ProjectionGEMM]
    assert len(gemms) == 7
    for op in gemms:
        assert op.b_col_maj and op.epilogue_modes == (Epilogue.NONE,)
        assert {k: e.name for k, e in op.bound_values.items()} == {"valid": "rows"}
        resolved = op.resolved(dev)
        assert resolved.B.shape == (op.N, op.K) and not resolved.bfp16_b


class Pointwise(iron.Graph):
    """A 1x1 convolution's pixels projected."""

    def __init__(self, precision: Precision | None):
        self.precision = precision

    def body(self, x, w):
        return F.linear(x, w, precision=self.precision)


@pytest.mark.parametrize("precision,macs", [(None, True), (Precision.HIGH, False)])
def test_project_asks_flm_gemm_for_bf16_macs(precision, macs, npu2):
    t = Pointwise(precision).record(x=((256, 128), bfloat16), w=((128, 128), bfloat16))
    (op,) = [op for op in t.operators if type(op) is ProjectionGEMM]
    assert op.resolved(npu2).emulate_bf16_mmul_with_bfp16 is macs


def test_llama_prompt_bounds_every_flm_gemm_by_its_rows(npu2):
    """Each projection of a prompt chunk derives five per-call words from its
    rows: the 256-row units they reach and that less one, A's repeat count,
    which every projection shares; where the second half of the core rows
    starts in A and in C, the units' first 128 rows of K and of N, which
    every projection as wide shares; and B's memtile ring passes less one,
    A's repeat count where B is resident, and where it streams (down's)
    the units' k tiles over the ring's slots.
    """
    g = llama_1b(num_hidden_layers=2)
    t = g.record(**g.shapes()[1])
    words, shared = _words(t, share=True)
    assert len(words) <= 32
    gemms = [op.resolved(npu2) for op in t.operators if type(op) is ProjectionGEMM]
    names = {"units_valid", "units_repeat", "a_half", "c_half", "b_passes_repeat"}
    symbols, widths, passes = set(), set(), set()
    for op in gemms:
        assert {v.name for v in op.values} == names | {"valid"}
        widths |= {op.K, op.N}
        unit_passes = op._k_iters // op._b_ring
        passes |= {unit_passes} - {1}
        for name in names:
            symbol = op.value(name).symbol
            symbols.add(shared.get(symbol, symbol))
        for rows, reached in ((1, 1), (15, 1), (256, 1), (257, 2), (2048, 8)):
            assert op.derived_at("units_valid", valid=rows) == reached
            assert op.derived_at("units_repeat", valid=rows) == reached - 1
            assert op.derived_at("a_half", valid=rows) == reached * 128 * op.K
            assert op.derived_at("c_half", valid=rows) == reached * 128 * op.N
            assert (
                op.derived_at("b_passes_repeat", valid=rows)
                == reached * unit_passes - 1
            )
    assert passes == {4}
    assert len(symbols) == 2 + len(widths) + len(passes)


@pytest.mark.parametrize("step", ["decode", "prompt"])
def test_llama_does_not_grow_with_the_context(step):
    """``max_seq_len`` sizes the caches, the RoPE table and the draws a
    position each and nothing else a decode step or a prompt chunk runs: a
    chunk's one input is its token ids (a step's token is a value),
    every activation and every array is the same at a four times longer
    context, and attention is the caches' two writes and MHA, the reshapes
    and transposes between them views the DMA walks.
    """

    def record(max_seq_len):
        g = small(max_seq_len=max_seq_len)
        return g.record(**g.shapes()[0 if step == "decode" else 1])

    short, long = record(256), record(1024)
    assert (
        [h.name for h in short.inputs]
        == [h.name for h in long.inputs]
        == ([] if step == "decode" else ["ids"])
    )
    grown = {name for name, n in long.pinned.items() if short.pinned[name] != n}
    caches = {
        f"model.layers.{i}.cache.{kv}" for i in (0, 1) for kv in ("keys", "values")
    }
    assert grown == {"rotary_emb.table", "draws", "drawn"} | caches

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

    A setting is ``(device, record)``: ``record`` builds the graph with that
    device current and records it. The device is restored afterwards.
    """
    out = []
    for dev, record in settings:
        with aie_utils.set_current_device(dev):
            out.append(
                [
                    tuple((n, vars(op)[n]) for n in op.declaration.params)
                    + (op.design_key(),)
                    for s in record().steps
                    for op in [s.op.resolved(dev)]
                ]
            )
    return out


def _every_tunable_is_load_bearing(monkeypatch, settings):
    """Drop each tunable the graphs pass, one (class, name) at a time; each
    must change some resolved step, or fail, in some setting. A tunable that
    resolution would have picked anyway is noise a reader has to disprove.
    """
    construct = Recorder._construct
    passed = set()

    def recording(self, cls, inputs, outputs, kwargs):
        passed.update((cls, n) for n in kwargs if n in cls.declaration.tunables)
        return construct(self, cls, inputs, outputs, kwargs)

    monkeypatch.setattr(Recorder, "_construct", recording)
    baseline = _resolved_fields(settings)
    redundant = []
    for cls, name in sorted(passed, key=lambda k: (k[0].__name__, k[1])):

        def dropping(self, kls, inputs, outputs, kwargs, cls=cls, name=name):
            if kls is cls:
                kwargs = {k: v for k, v in kwargs.items() if k != name}
            return construct(self, kls, inputs, outputs, kwargs)

        monkeypatch.setattr(Recorder, "_construct", dropping)
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
    a prompt; and the scaled-down shape the host tests record, with the
    parameters that shape needs.
    """
    npu2 = from_name("npu2", n_cols=8)
    real, scaled = llama_1b(num_hidden_layers=1), small()
    settings = [
        (npu2, lambda: real.record(**real.shapes()[0])),
        (npu2, lambda: real.record(**real.shapes()[1])),
        (npu2, lambda: scaled.record(**scaled.shapes()[1])),
    ]
    _every_tunable_is_load_bearing(monkeypatch, settings)


def test_a_bound_value_survives_tuning():
    copy = Copy(input_buffer_size=64, output_buffer_size=64)

    class F(iron.Graph):
        def body(self, x, *, a: Scratchpad[np.int32]):
            return copy(x, out_offset=a)

    f = F()

    f.record(x=(64,))
    assert [v.name for v in copy.resolved(aie_utils.get_current_device()).values] == [
        "out_offset"
    ]


# --------------------------------------------------------------------------
# A bound on a handle: the first n of an axis are the valid ones this call
# --------------------------------------------------------------------------


def test_a_bound_travels_through_reshape_and_transpose():

    n = PerCall("n", Kind.SCRATCHPAD, np.int32)
    x = Handle.whole((64, 8, 4), bfloat16, "x", "input")
    b = x[:n]
    assert b.shape == x.shape and b.valid == {0: n.affine()} and b.layout == Dense()
    assert b.reshape(512, 4).valid == {0: n * 8}  # merged with the axis after it
    assert b.reshape(64 * 8 * 4).valid == {0: n * 32}
    assert b.reshape(512, 4).reshape(64, 8, 4).valid == {0: n.affine()}  # split back
    assert b.transpose(1, 0, 2).valid == {1: n.affine()}
    with pytest.raises(ValueError, match="does not divide"):
        b.reshape(32, 16, 4)  # a leading axis no run of the others makes
    assert b[0].valid == {} and b[0].shape == (8, 4)  # one row: no bound
    with pytest.raises(TypeError, match="bounded per call on axis 0"):
        b[0:2]
    with pytest.raises(ValueError, match="from its start"):
        x[2:n]
    v = b[:, 2:6]  # all of the bounded axis: the bound stays on it
    assert v.shape == (64, 4, 4) and v.valid == {0: n.affine()}
    assert b[:, 3].valid == {0: n.affine()} and b[:, 3].shape == (64, 4)


def test_an_index_may_floor_and_a_bound_may_only_clamp():
    """A bound patches a length, so it is linear or clamped (a window's
    ``min(p + 1, 8)``); an index may floor.
    """
    p = PerCall("p", Kind.SCRATCHPAD, np.int32)
    cache = Handle.whole((8, 4), bfloat16, "cache", "state")
    assert cache[(p + 1) // 2].layout.offset == (p + 1) // 2 * 4
    with pytest.raises(TypeError, match="not linear"):
        _ = cache[: (p + 1) // 2]
    start = iron.clamp(p - 3, lo=0)
    assert start == (p - 3).clamp(lo=0) and cache[start].layout.offset == start * 4
    assert cache[: (p + 1).clamp(hi=8)].valid == {0: (p + 1).clamp(hi=8)}


def test_a_per_call_value_cannot_steer_the_record():
    """A body is recorded once for every call, so a branch on a per-call value
    would take one side for all of them: a comparison or a truth test raises.
    """

    class Branches(iron.Graph):
        def __init__(self, test):
            self.test = test

        def body(self, x, *, pos: Scratchpad[np.int32]):
            if self.test(pos):
                return ReLU.step(x)
            return ElementwiseAdd.step(x, x)

    for test in (lambda p: p == 0, lambda p: p * 2 != np.float32(2), bool):
        with pytest.raises(TypeError, match="per call"):
            Branches(test).record(x=(64,))


def test_an_index_before_a_bound_keeps_the_bound_on_its_axis():
    """``cache.reshape(G, L // C, C, D)[:, chunk, :rows]`` drops the chunk
    axis: the bound is on axis 1 of the view, and the index an offset of
    whole chunks.
    """
    chunk = PerCall("chunk", Kind.SCRATCHPAD, np.int32)
    rows = PerCall("rows", Kind.SCRATCHPAD, np.int32)
    G, L, C, D = 2, 64, 16, 8
    cache = Handle.whole((G, L // C, C, D), bfloat16, "cache", "state")
    v = cache[:, chunk, : rows + 1]
    assert v.shape == (G, C, D) and v.valid == {1: rows + 1}
    assert v.layout.offset == chunk * (C * D)

    keys = iron.state((G, L, D), name="keys")

    class Chunked(iron.Graph):
        def body(self, x, *, chunk: Scratchpad[np.int32], rows: Scratchpad[np.int32]):
            k = x[:rows].reshape(C, G, D).transpose(1, 0, 2)
            Copy.step(k, keys.reshape(G, L // C, C, D)[:, chunk, :rows])

    t = Chunked().record(x=(C, G * D))
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
    cache = Handle.whole((64, 2, 8), bfloat16, "cache", "state")
    a = cache[chunk * 16 : chunk * 16 + 16][:rows]
    b = cache.reshape(4, 16, 2, 8)[chunk, :rows]
    assert (a.shape, a.valid, a.layout.offset, a.ref()) == (
        b.shape,
        b.valid,
        b.layout.offset,
        b.ref(),
    )
    assert (a.layout.tap.offset, a.layout.tap.sizes, a.layout.tap.strides) == (
        b.layout.tap.offset,
        b.layout.tap.sizes,
        b.layout.tap.strides,
    )


def test_a_run_from_a_per_call_start_takes_any_start_on_any_axis():
    """A start that is no block's (``pos``), floored (``pos // 64 * 64``), on
    a leading or an inner axis: a view offset by the start's rows, its width
    fixed, bounded on the same axis.
    """
    pos = PerCall("pos", Kind.SCRATCHPAD, np.int32)
    rows = PerCall("rows", Kind.SCRATCHPAD, np.int32)
    cache = Handle.whole((100, 2, 8), bfloat16, "cache", "state")
    v = cache[pos : pos + 16][:rows]
    assert v.shape == (16, 2, 8) and v.valid == {0: rows.affine()}
    assert v.layout.offset == pos * 16
    floored = pos // 64 * 64
    assert cache[floored : floored + 64].layout.offset == floored * 16
    keys = Handle.whole((2, 100, 8), bfloat16, "keys", "state")
    w = keys[:, pos : pos + 16][:, :rows]
    assert w.shape == (2, 16, 8) and w.valid == {1: rows.affine()}
    assert w.layout.offset == pos * 8


def test_a_run_as_wide_as_its_axis_keeps_its_start_under_a_bound():
    """``x[:n][:, s : s + W]`` with ``W`` the whole axis is still offset by
    ``s`` each call, and still bounded by ``n``.
    """
    s = PerCall("s", Kind.SCRATCHPAD, np.int32)
    n = PerCall("n", Kind.SCRATCHPAD, np.int32)
    v = Handle.whole((8, 256), bfloat16, "x", "state")[:n][:, s : s + 256]
    assert v.layout.offset == s.affine() and v.valid == {0: n.affine()}


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
    cache = Handle.whole((100, 100), bfloat16, "cache", "state")
    with pytest.raises((IndexError, ValueError), match=error):
        cache[key(pos, n)]


def test_a_run_is_bounded_from_its_start_on_its_own_axis():
    pos = PerCall("pos", Kind.SCRATCHPAD, np.int32)
    rows = PerCall("rows", Kind.SCRATCHPAD, np.int32)
    run = Handle.whole((100, 2, 8), bfloat16, "cache", "state")[pos : pos + 16]
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

    t = Bounded().record(x=(100, 16))
    assert inside(t, pos=96, rows=4) and inside(t, pos=0, rows=16)
    assert not inside(t, pos=96, rows=5) and not inside(t, pos=-1, rows=1)
    assert not inside(t, pos=0, rows=17)
    t = Whole().record(x=(100, 16))
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
    with pytest.raises(IndexError, match=r"^Write: start \+ rows is 101, outside"):
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

    t = Chunked().record(x=(C, G * D))
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

    t = G().record(x=(64, 512), y=(64, 512))
    (op,) = t.operators
    op = op.resolved(aie_utils.get_current_device())
    per_word = op.cores * op.tile_size  # elements one word of tiles covers
    words = {w.symbol: w for w in _words(t)[0]}
    for p in range(64):
        elements = (p + 1) * 512
        tiles = -(-elements // per_word)
        assert words[op.value("valid").symbol]({"p": p}) == elements
        assert words[op.value("count").symbol]({"p": p}) == tiles
        assert words[op.value("valid_a").symbol]({"p": p}) == tiles
        assert tiles * per_word >= elements and tiles * per_word <= 64 * 512


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

    t = G().record()
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
    """``RMSNorm(x, w)`` gives the weight as RMSNorm's output: a recording and
    the reference refuse it, naming the keyword, whatever view of it, and
    the reference leaves the weight as it was.
    """
    w = np.arange(E).astype(bfloat16)

    class Norm(iron.Graph):
        def __init__(self):
            self.w = iron.param(w)

        def body(self, x):
            return RMSNorm.step(x, self.w.reshape(1, E) if view else self.w)

    x = np.ones((1, E), dtype=bfloat16)
    kept = w.copy()
    with pytest.raises(TypeError, match=r"graph weight or a view of one.*\(weight=\)"):
        Norm().record(x=(1, E))
    with pytest.raises(TypeError, match=r"graph weight or a view of one.*\(weight=\)"):
        Norm().reference(x)
    np.testing.assert_array_equal(w, kept)


def test_an_input_given_as_an_output_is_refused():
    class Over(iron.Graph):
        def body(self, x, y):
            ReLU.step(x, y[1:])
            return y

    with pytest.raises(TypeError, match="graph input or a view of one"):
        Over().record(x=(E - 1,), y=(E,))
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
            gemm(a, b, y)
            return y

    with pytest.raises(ValueError, match="operand C has rank 1"):
        Flat().record(a=(256, 256), b=(256, 256))


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
            return GEMM.step(a, b, output_dtype=np.float32, tile_m=32)

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
    t = g.record(x=(2, 4))
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

    t = g.record(x=(64, 8))
    (op,) = t.operators
    words = {w.symbol: w for w in _words(t)[0]}
    symbol = {v: op.value(v).symbol for v in ("valid", "count", "valid_x", "valid_y")}
    assert set(words) == set(symbol.values())
    assert symbol["valid"] == f"{op.name}_valid_n_x8"
    assert symbol["count"] == f"{op.name}_n_x8_count"
    call = {"n": 16}
    assert words[symbol["valid"]](call) == 16 * 8  # the reshape's scale
    assert words[symbol["count"]](call) == 16 * 8 // 2  # derived: valid // lanes
    assert words[symbol["valid_x"]](call) == 16 * 8 // 2  # tiles per lane
    # A full ELF's designs read the bound only through what they derive.
    elf = {w.symbol for w in _words(t, extents=False)[0]}
    assert elf == set(words) - {symbol["valid"]}
    for w in words.values():  # and each is what its Emit row computes
        assert w.form is not None and w.form.evaluate(call) == w(call)


def test_one_operator_bound_to_two_values_derives_a_word_from_each(npu2):
    """Two steps of one operator, each bounded by its own value, derive
    their words each from its own: a derived word is named by the values
    bound to its step, not shared as two steps bound alike share it.
    """

    class G(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32], m: Scratchpad[np.int32]):
            a = Rows.step(x[:n].reshape(64 * 8, 1))
            return a, Rows.step(x[:m].reshape(64 * 8, 1))

    t = G().record(x=(64, 8))
    first, second = t.operators
    assert first.value("count").symbol != second.value("count").symbol
    words = {w.symbol: w for w in _words(t)[0]}
    call = {"n": 16, "m": 32}
    for op, rows in ((first, 16), (second, 32)):
        assert words[op.value("count").symbol](call) == rows * 8 // 2


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

    words, _ = _words(G().record(q=(32, 64)), extents=False)
    assert words
    for w in words:
        assert w.form is not None and w.form.value.name == "position", w.symbol
        for position in range(2048):
            at = {"position": position}
            assert w.form.evaluate(at) == w(at), w.symbol


@pytest.mark.parametrize(
    "bound, names",
    [
        (lambda n: n, ["graph_n_x1d4_int32", "graph_n_x512_int32"]),
        (lambda n: n + 1, ["graph_n_x1d4p1d4_int32", "graph_n_x512p512_int32"]),
    ],
    ids=["n", "n+1"],
)
def test_words_that_always_hold_one_number_share_it(npu2, bound, names):
    """On a full ELF, two designs bound to one graph value write one word
    for each ratio and offset of it they read (their extents; the tiles per
    lane of each operand), and every symbol that shares a word reads its own
    value there. A derivation the library sees through (``count``, a ceiling
    division) shares the word of the ratio it computes.
    """

    class G(iron.Graph):
        def body(self, x, y, *, n: Scratchpad[np.int32]):
            rows = bound(n)
            return ElementwiseMul.step(
                ElementwiseAdd.step(x[:rows], y[:rows]), y[:rows]
            )

    t = G().record(x=(64, 512), y=(64, 512))
    alone, _ = _words(t)
    words, shared = _words(t, share=True)
    assert len(alone) == 10 and len(words) == 2
    assert sorted(set(shared.values())) == names
    for n in (0, 15, 63):
        mine = {w.symbol: w({"n": n}) for w in words}
        for w in alone:
            assert mine[shared.get(w.symbol, w.symbol)] == w({"n": n})


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

    t = ByHead().record(x=(L, G * D))
    (n,) = t.values
    for copy in t.operators:
        assert copy.src_bound == 1 and copy.dst_bound == 1
        assert {k: e.name for k, e in copy.bound_values.items()} == {
            "src_valid": "n",
            "dst_valid": "n",
        }
    assert (
        sorted(b.member.name for b in t.bindings)
        == ["dst_valid"] * 2 + ["src_valid"] * 2
    )
    assert all(b.expression == n.affine() for b in t.bindings)
    assert list(t.operators[1].dst.sizes) == [G, L, D]
    (out,) = t.outputs
    assert out.shape == (G, L, D) and out.valid == {1: n.affine()}

    class Flat(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            Copy.step(x[:n].reshape(L, G, D).transpose(1, 0, 2), keys.reshape(G * L, D))

    with pytest.raises(ValueError, match="bound it alike"):
        Flat().record(x=(L, G * D))


def test_the_reference_copies_a_bounded_call_into_the_rows_it_covers(npu2):
    """The recording bounds a given view alike (above); the reference, which runs
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

    t = g.record(x=(512, 64), w=(256, 64))
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
    # A call from mid-block: the block holding its first query, and the rows into it.
    at = dict(valid=40, kv_valid=310)
    assert [mha.derived_at(v, **at) for v in ("q_start", "q_offset")] == [4, 14]
    # Bound alike, the queries start at 0 on every call: written once.
    assert mha.residents["q_start"] == mha.residents["q_offset"] == 0
    assert mha.value("s_q").per_call
    (out,) = t.outputs
    assert out.valid == {0: t.values[0].affine()}  # O is bounded like Q


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
    alone, added = g.record(), g.record(x=(256,))
    assert alone.inputs == [] and [h.name for h in added.inputs] == ["x"]
    assert g.record(x=None).inputs == []
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


def test_a_held_array_that_is_no_param_is_refused():
    class Plain(iron.Graph):
        def __init__(self):
            self.w = z(256, E)

        def body(self, x):
            return GEMV.step(self.w, x)

    with pytest.raises(TypeError, match=r"Plain: w is an array.*iron\.param"):
        Plain().record(x=(E,))


def test_a_held_array_is_viewed_in_the_body_under_its_own_path():
    table = np.arange(8 * 256, dtype=np.int32).astype(bfloat16).reshape(8, 256)
    table = iron.param(table)
    g = _Held(table)
    t = g.record(x=(512,))
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


def test_a_call_refuses_an_input_numpy_would_not_cast_to_its_dtype():
    """Float ids are refused, not truncated; int64 ids cast to int32."""
    g = small()
    C = g.config.prefill_chunk

    class Staged(Exception):
        pass

    def upload():
        raise Staged

    version = SimpleNamespace(recording=g.record(**g.shapes()[1]), upload=upload)
    values = dict(position=C - 1, token=0, start=0, rows=C, rope_start=0)
    with pytest.raises(
        TypeError,
        match=r"input ids is int32, got float64; pass ids\.astype\(np\.int32\)",
    ):
        CompiledGraph._stage(version, [np.zeros(C)], values)
    with pytest.raises(Staged):
        CompiledGraph._stage(version, [np.zeros(C, np.int64)], values)


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
    t = walk.record()
    assert [(v.name, v.marker) for v in t.values] == [
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

    t = Walk().record()
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
        Forgets().record()

    class CarriesAPlainValue(iron.Graph):
        def body(self, *, a: Scratchpad[np.int32]):
            return iron.carry(a=a + 1)

    with pytest.raises(TypeError, match="Carried values are"):
        CarriesAPlainValue().record()

    class CarriesAConstant(iron.Graph):
        def body(self, *, a: Carried[np.int32]):
            return iron.carry(a=5)

    with pytest.raises(TypeError, match="expression of the values"):
        CarriesAConstant().record()

    class CarriesARow(iron.Graph):
        def body(self, *, a: Carried[np.int32]):
            return iron.carry(a=Copy.step(rows[a]))

    with pytest.raises(TypeError, match="one whole element"):
        CarriesARow().record()

    class CarriesTheWrongDtype(iron.Graph):
        def body(self, *, a: Carried[np.int16]):
            return iron.carry(a=Copy.step(table[a], dtype=np.int32))

    with pytest.raises(TypeError, match="but a is int16"):
        CarriesTheWrongDtype().record()

    class CarriesTwice(iron.Graph):
        def body(self, *, a: Carried[np.int32]):
            return iron.carry(a=a + 1), iron.carry(a=a + 2)

    with pytest.raises(TypeError, match="returned last"):
        CarriesTwice().record()


def test_the_emit_program_follows_the_target_parameters():
    """Each word of the target's scratchpad comes from a carried value, in
    the target's order and encoding; anything else is refused.
    """
    walk = Trail(np.arange(16, dtype=np.int32), steps=8)
    recording = walk.record()
    assert recording.feedback == []  # recording alone adds no Emit
    assert walk._carry is not None
    site = attach_emit(recording, walk._parameters.carried, walk._carry, slots=2)
    # The gathered node is computed into the carry's second plane.
    assert recording.steps[0].refs()[-1] == BufferRef("carry", 8, 4)
    assert recording.steps[-1].refs() == (
        BufferRef("emit_program"),
        BufferRef("carry"),
        BufferRef("emit_image"),
        BufferRef("carry", 0, 8),
    )
    assert recording.feedback == ["emit_image"] and recording.outputs == []

    words, _ = _words(recording)
    # A target laying the two out the other way, one as a core read.
    by_value = {w.linear.value: w.symbol for w in words if w.linear is not None}
    parameters = [
        Parameter(by_value["steps"], 0, "i32", "core"),
        Parameter(by_value["node"], 1, "i32", "addr"),
    ]
    program = compose(site, recording.carry, words, parameters)
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
        compose(site, recording.carry, words, parameters[:1])
    jumped, _ = _words(walk.record(jump=((16,), np.int32)))
    with pytest.raises(ValueError, match="skip, which is not carried"):
        compose(
            site,
            recording.carry,
            jumped,
            [Parameter(w.symbol, k, "i32", "addr") for k, w in enumerate(jumped)],
        )


def _emitted(graph, positions):
    """The words a carried ``position`` writes after each of ``positions``,
    each as the Emit program the device runs between calls computes it.
    """
    recording = graph.record()
    words, _ = _words(recording)
    assert all(w.linear is None for w in words)
    site = attach_emit(
        recording, graph._parameters.carried, graph._carry, slots=len(words)
    )
    parameters = [Parameter(w.symbol, k, "i32", "addr") for k, w in enumerate(words)]
    program = compose(site, recording.carry, words, parameters)
    out = []
    for p in positions:
        image, state = emit_reference(program, np.array([[p], [0]]), slots=len(words))
        want = [w(dict(position=p + 1)) for w in words]
        assert image.tolist() == want and state.tolist() == [p + 1]
        out.append(want)
    return out


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
    floored = [b.expression for b in graph.record().bindings]
    assert [e.down for e in floored] == [2, 2]
    assert len({e.name for e in floored}) == 2
    assert _emitted(graph, range(10)) == [
        [(p + 1) // 4 * 32, ((p + 2) // 4 + 1) * 32] for p in range(10)
    ]

    slots = np.arange(8 * 32, dtype=np.int32).reshape(8, 32)
    graph.slots.host = slots.copy()
    graph.reference(position=6)
    assert (graph.slots.host[2] == slots[1]).all()

    class Bounded(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return Copy.step(x[: n // 4])

    with pytest.raises(TypeError, match="not linear"):
        Bounded().record(x=((64, 32), bfloat16))


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
    assert _emitted(graph, range(40)) == [
        [max(p - 2, 0) % 8 * 32, (p + 1) % 8 * 32] for p in range(40)
    ]

    rows = np.arange(8 * 32, dtype=np.int32).reshape(8, 32)
    for position, read, written in ((1, 0, 1), (10, 7, 2), (21, 2, 5)):
        graph.rows.host = rows.copy()
        graph.reference(position=position)
        assert (graph.rows.host[written] == rows[read]).all()


def test_an_extent_bounded_by_a_clamped_carried_count_stays_clamped(npu2):
    """A ReLU over ``min(position + 1, 40)`` rows: its tiles per lane follow
    the clamp, growing up to the bound and then holding, and take no linear
    form, which would drop it.
    """

    class Window(iron.Graph):
        def __init__(self):
            self.rows = iron.state((64, 64), bfloat16)

        def body(self, *, position: Carried[np.int32]):
            n = iron.clamp(position + 1, hi=40)
            ReLU.step(Copy.step(self.rows[:n]))
            return iron.carry(position=position + 1)

    words, _ = _words(Window().record())
    tiles = [w for w in words if w.symbol.endswith(("valid_x", "valid_y"))]
    assert tiles and all(w.linear is None for w in tiles)
    for w in tiles:
        assert [w(dict(position=p)) for p in (0, 39, 50)] == [1, 2, 2]


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
    assert _emitted(graph, range(20)) == [
        [max(p - 2, 0) * 32, min((p + 2) // 2, 7) * 32] for p in range(20)
    ]

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
    tables = iron.param(tables.reshape(2, 8, 256))
    g = _HeldStack(tables)
    t = g.record(ids=((4,), np.int32))
    assert [h.name for _, h in t.weights.values()] == ["weights.embed.weight"]
    (gather,) = t.steps
    assert gather.refs()[0] == BufferRef("weights.embed.weight")
    ids = np.array([15, 0, 8, 7], np.int32)
    np.testing.assert_array_equal(g.reference(ids), tables.reshape(16, 256)[ids])


def test_only_a_copy_takes_the_rows_an_input_names():
    class Relu(iron.Graph):
        def body(self, ids):
            table = np.zeros((8, 256), bfloat16)
            return ReLU.step(iron.weight(table)[ids])

    with pytest.raises(TypeError, match=r"only a Copy of it alone does"):
        Relu().record(ids=((4,), np.int32))


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
    t = g.record(**shapes)
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
    assert g.record(x=(8, 256)).reads == {"n"}
    assert g.record(y=(8, 256)).reads == {"m"}
    assert [v.name for v in g.record(x=(8, 256)).values] == ["n", "m"]


def test_inline_records_only_into_a_body():
    with pytest.raises(TypeError, match="records into a graph's body"):
        _Summed(2).inline(_Summed(2).body)


class _DeviceIds(iron.Graph):
    """A gather by ids a step made, whose table address the image writes."""

    def __init__(self, table):
        self.table = iron.weight(table)

    def body(self, ids, *, n: Scratchpad[np.int32], m: Scratchpad[np.int32]):
        return Copy.step(self.table[Copy.step(ids, dtype=np.int32)[:n]])


def test_a_version_reads_none_of_the_words_its_image_writes():
    table = np.zeros((300, 64), dtype=bfloat16)
    recording = _DeviceIds(table).record(ids=((64,), np.int32))
    assert recording.addresses, "the gather's table address is a word the image writes"
    assert recording.reads == {"n"}


class _StateRows(iron.Graph):
    """A state's rows, bounded per call, added to an input's."""

    def __init__(self):
        self.rows = iron.state((64, 64))

    def body(self, x, *, n: Scratchpad[np.int32]):
        Copy.step(x[:n], self.rows[:n])
        rows = self.rows.at(TensorAccessPattern.full((64, 64)), (64, 64), bounds={0: n})
        return ElementwiseAdd.step(x[:n], rows)


def test_a_bounded_view_of_a_state_is_its_rows_this_call():
    """In a reference, a state viewed by ``at`` is its host rows to the bound."""
    x = np.arange(64 * 64, dtype=np.float32).reshape(64, 64).astype(bfloat16)
    got = np.asarray(_StateRows().reference(x, n=40), dtype=np.float32)
    want = (2 * x[:40].astype(np.float32)).astype(bfloat16).astype(np.float32)
    np.testing.assert_array_equal(got, want)


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
        _BadWalk(sizes, strides, bounded).record()


class _UnpairedWalks(iron.Graph):
    """``taps`` patterns walked in turn with ``repeats`` repeats."""

    def __init__(self, taps: int, repeats: int):
        self.table = iron.weight(np.zeros((64, 64), dtype=bfloat16))
        self.taps, self.repeats = taps, repeats

    def body(self, *, k: Scratchpad[np.int32]):
        tap = TensorAccessPattern(self.table.shape, 0, [4, 4, 4, 64], [0, 256, 64, 1])
        taps = (tap,) * self.taps if self.taps > 1 else tap
        repeat = (k,) * self.repeats if self.repeats > 1 else k
        rows = self.table.at(taps, (128, 64), bounds={0: k}, repeat=repeat)
        return Copy.step(rows)


@pytest.mark.parametrize("taps, repeats", [(2, 1), (1, 2)])
def test_walks_take_a_repeat_each(taps, repeats):
    with pytest.raises(ValueError, match="take a repeat each"):
        _UnpairedWalks(taps, repeats).record()


def test_a_handle_adds_and_multiplies_by_elementwise_and_rowwise_steps():
    """A row times a matrix is rowwise either way round, the row a held
    vector, a handle or a row of one, the matrix a handle or held.
    """
    w, m = z(E), z(4, E)

    class Arithmetic(iron.Graph):
        def __init__(self):
            self.w, self.m = iron.param(w), iron.param(m)

        def body(self, x, y, row):
            return (x + y) * self.w + x, row * x, x * row, x[0] * self.m

    t = Arithmetic().record(x=(2, E), y=(2, E), row=(E,))
    assert [type(s.op).__name__ for s in t.steps] == [
        "ElementwiseAdd",
        "RowwiseMul",
        "ElementwiseAdd",
    ] + ["RowwiseMul"] * 3
    with pytest.raises(TypeError, match="a row of"):
        Arithmetic().record(x=(2, E), y=(2, E // 2), row=(E,))


@pytest.mark.parametrize(
    "rows, keywords, steps",
    [
        (1, dict(precision=Precision.MEDIUM), ["GEMV"]),
        (4, dict(tile_size_output=32), None),
    ],
    ids=["gemv", "gemm"],
)
def test_linear_takes_a_precision_for_any_rows_and_gemv_tunables_for_one(
    rows, keywords, steps
):
    class Linear(iron.Graph):
        def __init__(self):
            self.w = iron.weight(z(E, E))

        def body(self, x):
            return F.linear(x, self.w, **keywords)

    if steps is None:
        with pytest.raises(ValueError, match="take no GEMV"):
            Linear().record(x=(rows, E))
    else:
        t = Linear().record(x=(rows, E))
        assert [type(s.op).__name__ for s in t.steps] == steps


def test_highest_runs_the_gemm_that_rounds_once():
    class Asked(iron.Graph):
        def body(self, x, w):
            return F.linear(x, w, precision=Precision.HIGHEST)

    shapes = dict(x=((128, 256), bfloat16), w=((256, 256), bfloat16))
    assert [type(s.op) for s in Asked().record(**shapes).steps] == [GEMM]
    # The GEMM takes its own profile entry.
    tuned = Asked()
    tuned.profile = Profile()
    tuned.profile.add(GEMM, tile_n=32)
    assert [s.op.tile_n for s in tuned.record(**shapes).steps] == [32]


def test_linear_takes_one_row_or_several():
    class Batched(iron.Graph):
        def body(self, x, w):
            return F.linear(x, w)

    with pytest.raises(
        ValueError, match=r"x \(2, 4, 256\) is not \(in,\) or \(rows, in\)"
    ):
        Batched().record(x=((2, 4, 256), bfloat16), w=((256, 256), bfloat16))


def test_the_reference_runs_the_trace_so_held_state_takes_arithmetic():
    """The reference interprets the recorded steps: a view of a state times a
    row, plus an input, is what its operators' references compute, and a
    state the body writes keeps that write for the next call.
    """
    held = iron.state((8, 64), name="held")
    row = np.full(64, 2, bfloat16)

    class Scaled(iron.Graph):
        def body(self, x):
            Copy.step(x, held[0:4])
            return held.reshape(2, 4, 64)[0] * row + x

    x = (np.arange(4 * 64) % 16).reshape(4, 64).astype(bfloat16)
    got = np.asarray(Scaled().reference(x), np.float32)
    np.testing.assert_array_equal(got, 3 * x.astype(np.float32))
    np.testing.assert_array_equal(held.host[:4], x)


def test_causal_conv1d_carries_its_tail_from_a_prompt_chunk_to_decode_steps():
    """A bounded chunk then two single rows, each row the taps over it and
    the rows before it, the first chunk's from zeros, each step's from the
    tail before it.
    """
    K, C, n = 3, 8, 5
    carried, tail = iron.state((K - 1, 64)), iron.state((K - 1, 64))
    window = iron.state((2, C, 64))
    taps = (np.arange(K * 64) % 5 + 1).reshape(K, 64).astype(bfloat16)
    state = F.ConvState(carried, carried, window, tail)

    class Prompt(iron.Graph):
        def body(self, x, *, rows: Scratchpad[np.int32]):
            return F.causal_conv1d(x[:rows], taps, state)

    class Decode(iron.Graph):
        def body(self, x):
            return F.causal_conv1d(x, taps, state)

    x = (np.arange((C + 2) * 64) % 7).reshape(C + 2, 64).astype(bfloat16)
    decode = Decode()
    got = np.concatenate(
        [
            Prompt().reference(x[:C], rows=n),
            decode.reference(x[C : C + 1]),
            decode.reference(x[C + 1 :]),
        ]
    ).astype(np.float32)
    rows = np.concatenate([np.zeros((K - 1, 64)), x[:n], x[C:]])
    t = taps.astype(np.float32)
    want = [sum(t[k] * rows[i + k] for k in range(K)) for i in range(n + 2)]
    np.testing.assert_array_equal(got, want)


@pytest.mark.parametrize(
    "keywords, doubles",
    [
        (dict(scale_factor=2), True),
        (dict(size=(6, 10)), True),
        (dict(size=6), False),
        (dict(scale_factor=2, mode="bilinear"), False),
        (dict(scale_factor=2, align_corners=False), False),
    ],
    ids=["scale", "size", "square_size", "bilinear", "align_corners"],
)
def test_interpolate_is_the_exact_2x_nearest_upsampling_only(keywords, doubles):
    class Upsample(iron.Graph):
        def body(self, x):
            return F.interpolate(x, **keywords)

    x = (np.arange(3 * 5 * 4) % 11).reshape(3, 5, 4).astype(bfloat16)
    if not doubles:
        with pytest.raises(ValueError, match="only the exact 2x nearest"):
            Upsample().record(x=(x.shape, bfloat16))
        return
    got = np.asarray(Upsample().reference(x)).reshape(6, 10, 4)
    np.testing.assert_array_equal(got, x.repeat(2, 0).repeat(2, 1))
    with pytest.raises(ValueError, match="not a map"):
        Upsample().record(x=((3, 20), bfloat16))


def _steps(t) -> list[str]:
    return [type(s.op).__name__ for s in t.steps]


def test_a_number_on_either_side_is_a_row_of_it():
    """``x * c``, ``c * x``, ``x + c``, ``-x``, ``x / c``: a rowwise step on
    one constant row per number, the same in the reference.
    """

    class Scalars(iron.Graph):
        def body(self, x):
            return 0.5 * x + 1, x * 0.5, -x, x / 4

    t = Scalars().record(x=(2, 64))
    assert _steps(t) == ["RowwiseMul", "RowwiseAdd"] + ["RowwiseMul"] * 3
    assert len(t.weights) == 4  # 0.5, 1, -1, 0.25: 0.5 once
    x = (np.arange(128) % 8).reshape(2, 64).astype(bfloat16)
    got = [np.asarray(y, np.float32) for y in Scalars().reference(x)]
    f = x.astype(np.float32)
    for y, want in zip(got, (0.5 * f + 1, 0.5 * f, -f, f / 4)):
        np.testing.assert_array_equal(y, want)


def test_one_row_times_a_number_is_elementwise():
    """A single row's row is the whole operand: streamed, not held in one
    core, as Gemma 4's 262144-wide soft-capped logits need.
    """

    class Capped(iron.Graph):
        def body(self, x):
            return x * (1 / 30) + 1

    t = Capped().record(x=(1, 262144))
    assert _steps(t) == ["ElementwiseMul", "ElementwiseAdd"]
    x = (np.arange(262144) % 8).reshape(1, 262144).astype(bfloat16)
    (got,) = [np.asarray(Capped().reference(x), np.float32)]
    want = x.astype(np.float32) * np.float32(bfloat16(1 / 30)) + 1
    np.testing.assert_array_equal(got, want.astype(bfloat16).astype(np.float32))


def test_one_row_a_core_holds_is_still_rowwise():
    """ResNet's classifier bias: one row of ten, which no elementwise line
    divides, is a row a core holds.
    """

    class Biased(iron.Graph):
        def __init__(self):
            self.bias = iron.param(np.arange(10).astype(bfloat16))

        def body(self, x):
            return x + self.bias

    t = Biased().record(x=(1, 10))
    assert _steps(t) == ["RowwiseAdd"]
    for step in t.steps:
        step.op.resolved()


def test_a_difference_is_one_axpy_and_a_number_less_a_handle_two_steps():
    class Differences(iron.Graph):
        def body(self, x, y):
            return x - y, 3 - x

    t = Differences().record(x=(2, 64), y=(2, 64))
    assert _steps(t) == ["AXPY", "RowwiseMul", "RowwiseAdd"]
    x = (np.arange(128) % 8).reshape(2, 64).astype(bfloat16)
    y = np.ones((2, 64), bfloat16)
    d, r = (np.asarray(v, np.float32) for v in Differences().reference(x, y))
    np.testing.assert_array_equal(d, x.astype(np.float32) - 1)
    np.testing.assert_array_equal(r, 3 - x.astype(np.float32))


def test_a_state_is_subtracted_as_it_is_added():
    class LessState(iron.Graph):
        def __init__(self):
            self.s = iron.state((2, 64))

        def body(self, x):
            return x - self.s

    graph = LessState()
    assert _steps(graph.record(x=(2, 64))) == ["AXPY"]
    x = (np.arange(128) % 8).reshape(2, 64).astype(bfloat16)
    graph.s.host = np.ones((2, 64), bfloat16)
    got = np.asarray(graph.reference(x), np.float32)
    np.testing.assert_array_equal(got, x.astype(np.float32) - 1)


def test_a_handle_is_divided_by_a_number_alone():
    class Divide(iron.Graph):
        def body(self, x, y):
            return x / y

    with pytest.raises(TypeError, match="divided by a number"):
        Divide().record(x=(64,), y=(64,))


@pytest.mark.parametrize(
    "rows, op, held",
    [
        (1, "GEMV", iron.param),
        (256, "ProjectionGEMM", iron.param),
        (256, "ProjectionGEMM", iron.weight),
        (256, "ProjectionGEMM", lambda w: iron.state(w.shape)),
    ],
    ids=["gemv", "gemm", "weight", "state"],
)
def test_matmul_by_a_weight_s_transpose_is_linear(rows, op, held):
    """``x @ W.T`` of a bare array, a weight or a state; a handle's ``.T``
    is its transpose.
    """

    class Project(iron.Graph):
        def __init__(self):
            self.w = held(z(128, E))

        def body(self, x, v):
            assert v.T.shape == (E, 128) and v.T.layout == v.transpose(1, 0).layout
            return x @ self.w.T

    assert _steps(Project().record(x=(rows, E), v=(128, E))) == [op]


def test_a_weight_times_a_row_is_linear_and_a_plain_matrix_is_refused():
    w = z(128, E)

    class Left(iron.Graph):
        def __init__(self):
            self.w = iron.param(w)

        def body(self, x):
            return self.w @ x

    class Plain(iron.Graph):
        def __init__(self):
            self.w = iron.param(w)

        def body(self, x):
            return x @ self.w

    assert _steps(Left().record(x=(E,))) == ["GEMV"]
    with pytest.raises(TypeError, match=r"x @ W.T with W \(out, in\)"):
        Plain().record(x=(1, 128))


def test_a_numpy_function_on_a_handle_says_what_to_call():
    class Exp(iron.Graph):
        def body(self, x):
            return np.exp(x)

    with pytest.raises(TypeError, match="numpy's exp cannot compute"):
        Exp().record(x=(64,))


def test_an_assignment_into_a_view_is_the_copy_into_it():
    """``cache[pos] = x`` records the step ``Copy.step(x, cache[pos])`` does,
    recorded and in the reference; a handle's slice takes one too.
    """
    cache = iron.state((8, 64), name="cache")

    class Store(iron.Graph):
        def body(self, x, *, pos: Scratchpad[np.int32]):
            cache[pos] = x
            y = Copy.step(x).reshape(2, 32)
            y[1] = x[0:32]
            return y

    class Spelled(iron.Graph):
        def body(self, x, *, pos: Scratchpad[np.int32]):
            Copy.step(x, cache[pos])
            y = Copy.step(x).reshape(2, 32)
            Copy.step(x[0:32], y[1])
            return y

    a, b = (g().record(x=(64,)) for g in (Store, Spelled))
    assert _steps(a) == _steps(b) == ["Copy"] * 3
    assert [s.refs() for s in a.steps] == [s.refs() for s in b.steps]
    x = (np.arange(64) % 16).astype(bfloat16)
    y = Store().reference(x, pos=3)
    np.testing.assert_array_equal(cache.host[3], x)
    np.testing.assert_array_equal(np.asarray(y)[1], x[:32])


def test_a_refused_step_names_the_graph_the_operator_and_the_held_path():
    class Project(iron.Graph):
        def __init__(self):
            self.layers = [SimpleNamespace(w=iron.param(z(256, 512)))]

        def body(self, x):
            return GEMV.step(self.layers[0].w, x)

    with pytest.raises(ValueError, match=r"^Project: GEMV\(layers\.0\.w, x\): GEMV"):
        Project().record(x=(256,))


def test_a_refused_step_shows_an_unheld_param_as_an_array_of_its_shape():
    class Project(iron.Graph):
        def body(self, x):
            return GEMV.step(iron.param(z(256, 512)), x)

    with pytest.raises(ValueError, match=r"^Project: GEMV\(ndarray \[256, 512\], x\)"):
        Project().record(x=(256,))


def test_reference_without_a_device_names_how_to_bind_one(monkeypatch):
    class Doubled(iron.Graph):
        def body(self, x):
            return x + x

    x = np.ones((4, 64), dtype=bfloat16)
    np.testing.assert_array_equal(Doubled().reference(x, dev=from_name("npu1")), x + x)
    monkeypatch.setattr(aie_utils, "ensure_current_device", lambda: None)
    with pytest.raises(RuntimeError, match="set_current_device"):
        Doubled().reference(x)


def test_a_per_call_value_s_default_is_given_when_left_out():
    class Defaulted(iron.Graph):
        def body(self, x, *, n: iron.Scratchpad[np.int32] = 1):
            return x + x

    x = np.ones((4, 64), dtype=bfloat16)
    np.testing.assert_array_equal(Defaulted().reference(x), x + x)
    with pytest.raises(TypeError, match=r"\['m'\] unknown"):
        Defaulted().reference(x, m=2)
