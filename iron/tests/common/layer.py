# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.Layer``, device-free: its oracle twin against hand-assembled
layers on fixed random inputs, and its graph's structure, traced, as the
checkpoint module it reads decides it.
"""

import dataclasses
from collections import Counter
from functools import partial
from types import SimpleNamespace

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.lm import Layer, Oracle, widen
from iron.applications.embedding_gemma2.config import AudioConfig
from iron.operators.mha import MHA
from iron.tests.common.llama_model import small

N, E, H, G, D, F = 4, 6, 2, 1, 4, 5


def oracle():
    return Oracle(AudioConfig(eps=1e-6))


def rms(x, w=np.float32(1)):
    return x / np.sqrt(np.mean(x * x, -1, keepdims=True) + 1e-6) * w


def shapes(E, H, G, D, F) -> dict[str, tuple[int, ...]]:
    """Each part of a layer module of that shape, by its Hugging Face name."""
    return {
        "input_layernorm": (E,),
        "post_attention_layernorm": (E,),
        "pre_feedforward_layernorm": (E,),
        "post_feedforward_layernorm": (E,),
        "self_attn.q_proj": (H * D, E),
        "self_attn.k_proj": (G * D, E),
        "self_attn.v_proj": (G * D, E),
        "self_attn.o_proj": (E, H * D),
        "self_attn.q_norm": (D,),
        "self_attn.k_norm": (D,),
        "mlp.gate_proj": (F, E),
        "mlp.up_proj": (F, E),
        "mlp.down_proj": (E, F),
        "mlp.fc1": (F, E),
        "mlp.fc2": (E, F),
        "self_attn_layer_norm": (E,),
        "self_attn.out_proj": (E, H * D),
        "encoder_attn_layer_norm": (E,),
        "encoder_attn.q_proj": (H * D, E),
        "encoder_attn.k_proj": (G * D, E),
        "encoder_attn.v_proj": (G * D, E),
        "encoder_attn.out_proj": (E, H * D),
        "final_layer_norm": (E,),
        "fc1": (F, E),
        "fc2": (E, F),
    }


def module(rng, shape, names, dtype=np.float32, bias=False, norm_bias=False, **parts):
    """A layer module of ``names`` at ``shape`` drawn from ``rng`` (a
    matrix's deviation ``1/sqrt(in)``), each projection with a bias if
    ``bias``, each norm if ``norm_bias``, then ``parts`` by name.
    """
    root = SimpleNamespace()
    drawn = {}
    for name in names:
        size = shape[name]
        weight = rng.standard_normal(size) / np.sqrt(size[-1] if len(size) == 2 else 1)
        part = SimpleNamespace(weight=weight.astype(dtype))
        if (bias and len(size) == 2) or (norm_bias and len(size) == 1):
            part.bias = (rng.standard_normal(size[0]) * 0.1).astype(dtype)
        drawn[name] = part
    for name, part in {**drawn, **parts}.items():
        *parents, leaf = name.split(".")
        node = root
        for key in parents:
            node = vars(node).setdefault(key, SimpleNamespace())
        vars(node)[leaf] = part
    return root


LLAMA = (
    "input_layernorm",
    "post_attention_layernorm",
    "self_attn.q_proj",
    "self_attn.k_proj",
    "self_attn.v_proj",
    "self_attn.o_proj",
    "mlp.gate_proj",
    "mlp.up_proj",
    "mlp.down_proj",
)
GEMMA = (
    *LLAMA,
    "pre_feedforward_layernorm",
    "post_feedforward_layernorm",
    "self_attn.q_norm",
    "self_attn.k_norm",
)


@pytest.mark.parametrize("scale, residual", [(None, 1.0), (0.3, 0.25)])
def test_the_oracle_is_a_pre_norm_swiglu_layer_with_biases(scale, residual):
    rng = np.random.default_rng(1)
    w = module(rng, shapes(E, H, G, D, F), LLAMA, bias=True)
    x = rng.standard_normal((N, E)).astype(np.float32)
    angles = rng.standard_normal((N, D)).astype(np.float32)
    o = oracle()
    layer = Layer(H, G, D, 1e-6, scale=scale, residual=residual)
    got = layer.oracle(o, w, x, partial(o.attend, causal=True), angles)

    a, m = w.self_attn, w.mlp
    h = rms(x, w.input_layernorm.weight)
    q = Oracle.rotate((h @ a.q_proj.weight.T + a.q_proj.bias).reshape(N, H, D), angles)
    k = Oracle.rotate((h @ a.k_proj.weight.T + a.k_proj.bias).reshape(N, G, D), angles)
    v = (h @ a.v_proj.weight.T + a.v_proj.bias).reshape(N, G, D)
    attended = o.attend(q, k, v, causal=True, scale=scale)
    x = x + residual * (attended @ a.o_proj.weight.T + a.o_proj.bias)
    h = rms(x, w.post_attention_layernorm.weight)
    gate = h @ m.gate_proj.weight.T + m.gate_proj.bias
    up = h @ m.up_proj.weight.T + m.up_proj.bias
    f = gate / (1 + np.exp(-gate)) * up
    want = x + residual * (f @ m.down_proj.weight.T + m.down_proj.bias)
    np.testing.assert_allclose(got, want, rtol=1e-5, atol=1e-6)


def test_the_oracle_is_a_sandwich_geglu_layer_with_qk_norms():
    rng = np.random.default_rng(5)
    w = module(rng, shapes(E, H, G, D, F), GEMMA)
    x = rng.standard_normal((N, E)).astype(np.float32)
    angles = rng.standard_normal((N, D)).astype(np.float32)
    o = oracle()
    layer = Layer(H, G, D, 1e-6, "gelu_pytorch_tanh", scale=1.0, v_norm=True)
    got = layer.oracle(o, w, x, o.attend, angles)

    a, m = w.self_attn, w.mlp
    h = rms(x, w.input_layernorm.weight)
    q = Oracle.rotate(
        rms((h @ a.q_proj.weight.T).reshape(N, H, D), a.q_norm.weight), angles
    )
    k = Oracle.rotate(
        rms((h @ a.k_proj.weight.T).reshape(N, G, D), a.k_norm.weight), angles
    )
    v = rms((h @ a.v_proj.weight.T).reshape(N, G, D))
    attended = o.attend(q, k, v, scale=1.0) @ a.o_proj.weight.T
    x2 = x + rms(attended, w.post_attention_layernorm.weight)
    h2 = rms(x2, w.pre_feedforward_layernorm.weight)
    gelu = Oracle.gelu_tanh(h2 @ m.gate_proj.weight.T)
    f = (gelu * (h2 @ m.up_proj.weight.T)) @ m.down_proj.weight.T
    want = x2 + rms(f, w.post_feedforward_layernorm.weight)
    np.testing.assert_allclose(got, want, rtol=1e-5, atol=1e-6)


def test_fused_and_wrapped_projections_read_as_their_parts():
    rng = np.random.default_rng(2)
    w = module(rng, shapes(E, H, G, D, F), LLAMA, bias=True)
    a, m = w.self_attn, w.mlp
    fused = SimpleNamespace(
        input_layernorm=w.input_layernorm,
        post_attention_layernorm=w.post_attention_layernorm,
        self_attn=SimpleNamespace(
            qkv_proj=SimpleNamespace(
                linear=SimpleNamespace(
                    weight=np.concatenate(
                        [p.weight for p in (a.q_proj, a.k_proj, a.v_proj)]
                    ),
                    bias=np.concatenate(
                        [p.bias for p in (a.q_proj, a.k_proj, a.v_proj)]
                    ),
                )
            ),
            o_proj=a.o_proj,
        ),
        mlp=SimpleNamespace(
            gate_up_proj=SimpleNamespace(
                weight=np.concatenate([m.gate_proj.weight, m.up_proj.weight]),
                bias=np.concatenate([m.gate_proj.bias, m.up_proj.bias]),
            ),
            down_proj=m.down_proj,
        ),
    )
    layer = Layer(H, G, D, 1e-6)
    pairs = [
        *zip(layer.projections(w.self_attn), layer.projections(fused.self_attn)),
        *zip(Layer.mlp(w), Layer.mlp(fused)),
    ]
    for (wa, ba), (wb, bb) in pairs:
        np.testing.assert_array_equal(wa, wb)
        np.testing.assert_array_equal(ba, bb)
    x = rng.standard_normal((N, E)).astype(np.float32)
    angles = rng.standard_normal((N, D)).astype(np.float32)
    o = oracle()
    attend = partial(o.attend, causal=True)
    np.testing.assert_array_equal(
        layer.oracle(o, w, x, attend, angles), layer.oracle(o, fused, x, attend, angles)
    )


def test_an_activation_with_no_operator_is_refused():
    with pytest.raises(ValueError, match="no operator for hidden_act 'gelu'"):
        Layer(H, G, D, 1e-6, "gelu")


def test_a_layer_norm_at_another_epsilon_than_its_kernels_is_refused():
    norm = SimpleNamespace(weight=np.ones(E, bfloat16), bias=np.zeros(E, bfloat16))
    with pytest.raises(ValueError, match="LayerNorm's kernel takes no epsilon"):
        Layer(H, G, D, 1e-6).norm(None, norm)


# A layer at a shape every operator in it traces at.
T, WIDTH, HEADS, GROUPS, HEAD, HIDDEN = 256, 512, 8, 2, 64, 1024


def traced(names, layer, turned=True, **parts):
    """The steps of ``layer`` on a module of ``names`` and ``parts``,
    traced at ``T`` rows, turned by RoPE if ``turned``.
    """
    rng = np.random.default_rng(3)
    shape = shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN)
    root = module(rng, shape, names, bfloat16, **parts)

    def attend(q, k, v, *, scale, window):
        o = MHA.step(
            q,
            k,
            v,
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
            window=window,
            scale=scale,
        )
        return o.reshape(T, HEADS * HEAD)

    class Model(iron.Graph):
        def __init__(self):
            self.weights = root
            self.angles = iron.weight(np.zeros((T, HEAD), bfloat16))

        def body(self, x):
            return layer.step(self.weights, x, attend, self.angles if turned else None)

    return Model().trace(x=(T, WIDTH))


def ops(t) -> Counter:
    return Counter(type(s.op).__name__ for s in t.steps)


@pytest.mark.usefixtures("npu2")
def test_the_module_and_the_config_decide_the_steps():
    layer = Layer(HEADS, GROUPS, HEAD, 1e-6, accurate=True)
    plain = traced(LLAMA, layer)
    assert ops(plain) == Counter(
        GEMM=7, RMSNorm=2, RoPE=2, MHA=1, ElementwiseAdd=2, SiLU=1, ElementwiseMul=1
    )
    gemma = traced(GEMMA, dataclasses.replace(layer, v_norm=True))
    # Sandwich norms, q and k norms and the v norm.
    assert ops(gemma) - ops(plain) == Counter(RMSNorm=5)
    bias = SimpleNamespace(
        weight=np.zeros((HEADS * HEAD, WIDTH), bfloat16),
        bias=np.zeros(HEADS * HEAD, bfloat16),
    )
    biased = traced(LLAMA, layer, **{"self_attn.q_proj": bias})
    assert ops(biased) - ops(plain) == Counter(RowwiseAdd=1)
    scaled = traced(LLAMA, dataclasses.replace(layer, residual=0.25))
    assert ops(plain) - ops(scaled) == Counter(ElementwiseAdd=2)
    assert ops(scaled) - ops(plain) == Counter(AXPY=2)


@pytest.mark.usefixtures("npu2")
def test_a_fused_projection_is_read_as_views_of_the_checkpoints_array():
    layer = Layer(HEADS, GROUPS, HEAD, 1e-6, accurate=True)
    Q, KV = HEADS * HEAD, GROUPS * HEAD
    qkv = SimpleNamespace(weight=np.zeros((Q + 2 * KV, WIDTH), bfloat16))
    names = [n for n in LLAMA if not n.endswith(("q_proj", "k_proj", "v_proj"))]
    t = traced(names, layer, **{"self_attn.qkv_proj": qkv})
    row = WIDTH * 2
    starts = [
        ref.start
        for s in t.steps
        for ref in s.refs()
        if ref.root == "weights.self_attn.qkv_proj.weight"
    ]
    assert starts == [0, Q * row, (Q + KV) * row]


def test_causal_attention_refuses_a_window():
    with pytest.raises(ValueError, match="window"):
        small().attend(None, 0, None, None, None, window=4)


PLAIN = (
    "input_layernorm",
    "post_attention_layernorm",
    "self_attn.q_proj",
    "self_attn.k_proj",
    "self_attn.v_proj",
    "self_attn.o_proj",
    "mlp.fc1",
    "mlp.fc2",
)


@pytest.mark.usefixtures("npu2")
def test_the_graph_through_its_operators_references_is_the_oracle():
    """A layer of affine LayerNorms, biases, a plain GELU feed-forward and a
    rotated prefix of each head, run through each operator's reference, is
    its oracle within bf16's rounding of each of its steps; an oracle that
    turns the whole head is not.
    """
    rng = np.random.default_rng(6)
    shape = shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN)
    w = module(rng, shape, PLAIN, bfloat16, bias=True, norm_bias=True)
    w.input_layernorm.weight += bfloat16(1)
    w.post_attention_layernorm.weight += bfloat16(1)
    rotary = HEAD // 2
    layer = Layer(
        HEADS, GROUPS, HEAD, 1e-5, "gelu_pytorch_tanh", rotary=rotary, accurate=True
    )
    positions = np.arange(T)[:, None] * np.float32(0.05) * np.arange(1, rotary // 2 + 1)
    angles = np.empty((T, rotary), np.float32)
    angles[:, ::2], angles[:, 1::2] = np.cos(positions), np.sin(positions)

    def attend(q, k, v, *, scale, window):
        o = MHA.step(q, k, v, heads_interleaved=True, kv_interleaved=True, causal=False)
        return o.reshape(T, HEADS * HEAD)

    class Model(iron.Graph):
        def __init__(self):
            self.weights = w
            self.angles = angles.astype(bfloat16)

        def body(self, x):
            return layer.step(self.weights, x, attend, self.angles)

    x = rng.standard_normal((T, WIDTH)).astype(bfloat16)
    got = np.asarray(Model().reference(x), np.float32)
    o = Oracle(AudioConfig(eps=1e-5))
    wide, xf = widen(w), np.asarray(x, np.float32)
    turned = np.asarray(angles.astype(bfloat16), np.float32)

    def error(oracle_layer, table):
        want = oracle_layer.oracle(o, wide, xf, o.attend, table)
        return np.linalg.norm(got - want) / np.linalg.norm(want)

    # About 20 steps, each rounded once to bf16 (2 ** -9 relative).
    assert error(layer, turned) < 20 * 2**-9
    # The same frequencies over the whole head, the rest turned by nothing.
    identity = np.tile(np.float32([1, 0]), (T, (HEAD - rotary) // 2))
    whole = np.concatenate([turned, identity], axis=-1)
    assert error(dataclasses.replace(layer, rotary=None), whole) > 20 * 2**-9


def same_parts(layer, w, other) -> bool:
    """Whether ``layer`` reads the same arrays and norm modules of ``w`` and
    ``other``, by identity.
    """
    parts = [
        *zip(layer.projections(w.self_attn), layer.projections(other.self_attn)),
        *zip(Layer.mlp(w), Layer.mlp(other)),
    ]
    return all(x is y for p, q in parts for x, y in zip(p, q)) and all(
        x is y
        for x, y in zip(
            (*Layer.norms(w), *Layer.qk_norms(w.self_attn)),
            (*Layer.norms(other), *Layer.qk_norms(other.self_attn)),
        )
    )


def renamed(w, family: str) -> SimpleNamespace:
    """``w``, a pre-norm layer of ``PLAIN``'s names, under ``family``'s:
    the same arrays.
    """
    a = w.self_attn
    attention = dict(q_proj=a.q_proj, k_proj=a.k_proj, v_proj=a.v_proj)
    if family == "siglip":
        return SimpleNamespace(
            layer_norm1=w.input_layernorm,
            layer_norm2=w.post_attention_layernorm,
            self_attn=SimpleNamespace(**attention, out_proj=a.o_proj),
            mlp=w.mlp,
        )
    return SimpleNamespace(
        self_attn_layer_norm=w.input_layernorm,
        final_layer_norm=w.post_attention_layernorm,
        self_attn=SimpleNamespace(**attention, out_proj=a.o_proj),
        fc1=w.mlp.fc1,
        fc2=w.mlp.fc2,
    )


@pytest.mark.usefixtures("npu2")
@pytest.mark.parametrize("family", ["siglip", "whisper"])
def test_a_family_s_names_read_as_their_llama_named_parts(family):
    rng = np.random.default_rng(7)
    shape = shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN)
    w = module(rng, shape, PLAIN, bfloat16, bias=True, norm_bias=True)
    other = renamed(w, family)
    layer = Layer(
        HEADS, GROUPS, HEAD, 1e-5, "gelu_pytorch_tanh", scale=1.0, accurate=True
    )
    assert same_parts(layer, w, other)
    o = Oracle(AudioConfig(eps=1e-5))
    x = rng.standard_normal((T, WIDTH)).astype(np.float32)
    angles = rng.standard_normal((T, HEAD)).astype(np.float32)
    np.testing.assert_array_equal(
        layer.oracle(o, widen(w), x, o.attend, angles),
        layer.oracle(o, widen(other), x, o.attend, angles),
    )
    steps = [
        (type(s.op), s.op.design_key()) for s in traced((), layer, **vars(w)).steps
    ]
    traced_other = traced((), layer, **vars(other))
    assert [(type(s.op), s.op.design_key()) for s in traced_other.steps] == steps


def test_a_module_with_no_family_of_norms_is_refused():
    with pytest.raises(ValueError, match="holds none of the norms"):
        Layer.norms(SimpleNamespace(norm=None))


@pytest.mark.usefixtures("npu2")
@pytest.mark.parametrize("residual", [1.0, 0.25])
def test_a_one_row_step_keeps_its_rows_through_the_residual(residual):
    """One row projects by GEMV, whose reference output is flat: the
    residual keeps the layer's input shape, scaled or not.
    """
    w = module(
        np.random.default_rng(8),
        shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN),
        LLAMA,
        bfloat16,
    )
    layer = Layer(HEADS, GROUPS, HEAD, 1e-6, residual=residual)

    def attend(q, k, v, *, scale, window):
        o = MHA.step(q, k, v, heads_interleaved=True, kv_interleaved=True, causal=False)
        return o.reshape(1, HEADS * HEAD)

    class Model(iron.Graph):
        def __init__(self):
            self.weights = w
            self.angles = np.zeros((1, HEAD), bfloat16)

        def body(self, x):
            return layer.step(self.weights, x, attend, self.angles)

    x = np.ones((1, WIDTH), bfloat16)
    assert np.asarray(Model().reference(x)).shape == (1, WIDTH)
    assert [tuple(h.shape) for h in Model().trace(x=(1, WIDTH)).outputs] == [(1, WIDTH)]


QK = (*LLAMA, "self_attn.q_norm", "self_attn.k_norm")


def lfm2(w) -> SimpleNamespace:
    """``w``, a pre-norm gated layer of ``QK``'s names, under LFM2's: the
    same arrays.
    """
    a, m = w.self_attn, w.mlp
    return SimpleNamespace(
        operator_norm=w.input_layernorm,
        ffn_norm=w.post_attention_layernorm,
        self_attn=SimpleNamespace(
            q_proj=a.q_proj,
            k_proj=a.k_proj,
            v_proj=a.v_proj,
            out_proj=a.o_proj,
            q_layernorm=a.q_norm,
            k_layernorm=a.k_norm,
        ),
        feed_forward=SimpleNamespace(w1=m.gate_proj, w3=m.up_proj, w2=m.down_proj),
    )


@pytest.mark.usefixtures("npu2")
def test_lfm2_s_names_read_as_their_llama_named_parts():
    rng = np.random.default_rng(9)
    w = module(rng, shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN), QK, bfloat16)
    other = lfm2(w)
    layer = Layer(HEADS, GROUPS, HEAD, 1e-5, accurate=True)
    assert same_parts(layer, w, other)
    o = Oracle(AudioConfig(eps=1e-5))
    x = rng.standard_normal((T, WIDTH)).astype(np.float32)
    angles = rng.standard_normal((T, HEAD)).astype(np.float32)
    attend = partial(o.attend, causal=True)
    np.testing.assert_array_equal(
        layer.oracle(o, widen(w), x, attend, angles),
        layer.oracle(o, widen(other), x, attend, angles),
    )
    steps = [
        (type(s.op), s.op.design_key()) for s in traced((), layer, **vars(w)).steps
    ]
    traced_other = traced((), layer, **vars(other))
    assert [(type(s.op), s.op.design_key()) for s in traced_other.steps] == steps


def test_a_module_with_no_feed_forward_is_refused():
    with pytest.raises(ValueError, match="holds no feed-forward"):
        Layer.mlp(SimpleNamespace(mlp=SimpleNamespace(proj=None)))


@pytest.mark.usefixtures("npu2")
def test_the_feed_forward_block_alone_is_its_oracle():
    """An LFM2 short-convolution layer's feed-forward, the module holding no
    attention: its oracle twin is a pre-norm SwiGLU and its residual, and its
    graph through its operators' references is that oracle within bf16's
    rounding of each of its steps.
    """
    rng = np.random.default_rng(10)
    w = lfm2(module(rng, shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN), QK, bfloat16))
    del w.self_attn
    w.ffn_norm.weight += bfloat16(1)
    layer = Layer(HEADS, GROUPS, HEAD, 1e-5, accurate=True)
    x = rng.standard_normal((T, WIDTH)).astype(bfloat16)
    o = Oracle(AudioConfig(eps=1e-5))
    wide, xf = widen(w), np.asarray(x, np.float32)
    want = layer.feed_forward_oracle(o, wide, xf)

    m = wide.feed_forward
    h = xf / np.sqrt(np.mean(xf * xf, -1, keepdims=True) + 1e-5) * wide.ffn_norm.weight
    gate = h @ m.w1.weight.T
    hand = xf + (gate / (1 + np.exp(-gate)) * (h @ m.w3.weight.T)) @ m.w2.weight.T
    np.testing.assert_allclose(want, hand, rtol=1e-4, atol=1e-5)

    class Model(iron.Graph):
        def __init__(self):
            self.weights = w

        def body(self, x):
            return layer.feed_forward(self.weights, x)

    graph = Model()
    assert ops(graph.trace(x=(T, WIDTH))) == Counter(
        RMSNorm=1, GEMM=3, SiLU=1, ElementwiseMul=1, ElementwiseAdd=1
    )
    got = np.asarray(graph.reference(x), np.float32)
    # Seven steps, each rounded once to bf16 (2 ** -9 relative).
    error = np.linalg.norm(got - want) / np.linalg.norm(want)
    assert error < 7 * 2**-9


WHISPER = (
    "self_attn_layer_norm",
    "self_attn.q_proj",
    "self_attn.k_proj",
    "self_attn.v_proj",
    "self_attn.out_proj",
    "encoder_attn_layer_norm",
    "encoder_attn.q_proj",
    "encoder_attn.k_proj",
    "encoder_attn.v_proj",
    "encoder_attn.out_proj",
    "final_layer_norm",
    "fc1",
    "fc2",
)


def decoder(rng, shape, dtype=np.float32):
    """A Whisper decoder layer module at ``shape``: affine LayerNorms about
    one, every projection biased but the keys', as Whisper's.
    """
    w = module(rng, shape, WHISPER, dtype, bias=True, norm_bias=True)
    for n in (w.self_attn_layer_norm, w.encoder_attn_layer_norm, w.final_layer_norm):
        n.weight += dtype(1)
    del w.self_attn.k_proj.bias, w.encoder_attn.k_proj.bias
    return w


def test_the_oracle_of_a_decoder_layer_attends_over_the_encoder():
    rng = np.random.default_rng(11)
    w = decoder(rng, shapes(E, H, H, D, F))
    x = rng.standard_normal((N, E)).astype(np.float32)
    memory = rng.standard_normal((N + 3, E)).astype(np.float32)
    o = Oracle(AudioConfig(eps=1e-5))
    layer = Layer(H, H, D, 1e-5, "gelu_pytorch_tanh")
    k, v = layer.cross_kv_oracle(o, w, memory)
    got = layer.oracle(
        o, w, x, partial(o.attend, causal=True), None, cross=partial(o.attend, k=k, v=v)
    )

    def ln(x, n):
        c = x - x.mean(-1, keepdims=True)
        return c / np.sqrt(np.mean(c * c, -1, keepdims=True) + 1e-5) * n.weight + n.bias

    def linear(x, p):
        return x @ p.weight.T + vars(p).get("bias", 0)

    a, c = w.self_attn, w.encoder_attn
    h = ln(x, w.self_attn_layer_norm)
    q, k, v = (linear(h, p).reshape(N, H, D) for p in (a.q_proj, a.k_proj, a.v_proj))
    x = x + linear(o.attend(q, k, v, causal=True), a.out_proj)
    q = linear(ln(x, w.encoder_attn_layer_norm), c.q_proj).reshape(N, H, D)
    k, v = (linear(memory, p).reshape(N + 3, H, D) for p in (c.k_proj, c.v_proj))
    x = x + linear(o.attend(q, k, v), c.out_proj)
    want = x + linear(Oracle.gelu_tanh(linear(ln(x, w.final_layer_norm), w.fc1)), w.fc2)
    np.testing.assert_allclose(got, want, rtol=1e-4, atol=1e-5)


@pytest.mark.usefixtures("npu2")
def test_no_angles_turn_nothing():
    rng = np.random.default_rng(12)
    w = module(rng, shapes(E, H, G, D, F), QK)
    x = rng.standard_normal((N, E)).astype(np.float32)
    identity = np.tile(np.float32([1, 0]), (N, D // 2))
    o = oracle()
    attend = partial(o.attend, causal=True)
    layer = Layer(H, G, D, 1e-6)
    np.testing.assert_array_equal(
        layer.oracle(o, w, x, attend, None), layer.oracle(o, w, x, attend, identity)
    )
    layer = Layer(HEADS, GROUPS, HEAD, 1e-6, accurate=True)
    turned, unturned = traced(LLAMA, layer), traced(LLAMA, layer, turned=False)
    assert ops(turned) - ops(unturned) == Counter(RoPE=2)
    assert not ops(unturned) - ops(turned)


# The encoder's output rows a decoder layer's cross-attention reads.
S = 512


class Decoder(iron.Graph):
    """``layer`` on the module ``w`` at ``T`` rows, attending over itself
    and, with ``cross``, over the keys and values ``cross_kv`` projects
    from ``memory``.
    """

    def __init__(self, layer, w, cross=True):
        self.layer, self.weights, self.cross = layer, w, cross

    def body(self, x, memory):
        layer = self.layer
        H, D = layer.heads, layer.head_dim

        def attend(q, k, v, *, scale, window):
            o = MHA.step(
                q, k, v, heads_interleaved=True, kv_interleaved=True, causal=False
            )
            return o.reshape(T, H * D)

        if not self.cross:
            return layer.step(self.weights, x, attend, None)
        keys, values = layer.cross_kv(self.weights, memory)

        def cross(q, *, scale):
            o = MHA.step(
                q,
                keys,
                values,
                heads_interleaved=True,
                kv_interleaved=True,
                causal=False,
                scale=scale,
            )
            return o.reshape(T, H * D)

        return layer.step(self.weights, x, attend, None, cross=cross)


@pytest.mark.usefixtures("npu2")
def test_a_decoder_layer_s_graph_through_its_operators_references_is_its_oracle():
    """A Whisper decoder layer, its keys and values over the encoder's output
    from ``cross_kv``, run through each operator's reference, is its oracle
    within bf16's rounding of each of its steps; an oracle missing the cross
    block is not.
    """
    rng = np.random.default_rng(13)
    w = decoder(rng, shapes(WIDTH, HEADS, HEADS, HEAD, HIDDEN), bfloat16)
    without = SimpleNamespace(**vars(w))
    del without.encoder_attn, without.encoder_attn_layer_norm
    layer = Layer(HEADS, HEADS, HEAD, 1e-5, "gelu_pytorch_tanh", accurate=True)
    graph = Decoder(layer, w)
    shape = dict(x=(T, WIDTH), memory=(S, WIDTH))
    # The cross block: its affine LayerNorm, q, k, v and o projected with
    # their biases but k's, the attention and the residual.
    extra = Counter(
        LayerNorm=1, RowwiseMul=1, RowwiseAdd=4, GEMM=4, MHA=1, ElementwiseAdd=1
    )
    plain = Decoder(layer, without, cross=False).trace(**shape)
    assert ops(graph.trace(**shape)) - ops(plain) == extra
    assert not ops(plain) - ops(graph.trace(**shape))

    x = rng.standard_normal((T, WIDTH)).astype(bfloat16)
    memory = rng.standard_normal((S, WIDTH)).astype(bfloat16)
    got = np.asarray(graph.reference(x, memory), np.float32)
    o = Oracle(AudioConfig(eps=1e-5))
    xf, mf = np.asarray(x, np.float32), np.asarray(memory, np.float32)
    k, v = layer.cross_kv_oracle(o, widen(w), mf)
    cross = partial(o.attend, k=k, v=v)

    def error(module):
        want = layer.oracle(o, widen(module), xf, o.attend, None, cross=cross)
        return np.linalg.norm(got - want) / np.linalg.norm(want)

    # Its 33 steps, each rounded once to bf16 (2 ** -9 relative).
    assert error(w) < 33 * 2**-9
    assert error(without) > 33 * 2**-9


@pytest.mark.usefixtures("npu2")
def test_a_decoder_layer_needs_its_cross_attention():
    shape = shapes(WIDTH, HEADS, HEADS, HEAD, HIDDEN)
    w = decoder(np.random.default_rng(14), shape, bfloat16)
    layer = Layer(HEADS, HEADS, HEAD, 1e-5, "gelu_pytorch_tanh")
    with pytest.raises(TypeError, match="encoder_attn needs cross="):
        Decoder(layer, w, cross=False).trace(x=(T, WIDTH), memory=(S, WIDTH))


# A per-layer input's width.
P = 4
# Gemma 4's per-layer input parts, held by its layer module itself.
PER_LAYER = {
    "per_layer_input_gate": (P, E),
    "per_layer_projection": (E, P),
    "post_per_layer_input_norm": (E,),
}


def gemma4(rng, width=E, heads=H, groups=G, head=D, hidden=F, ple=P, dtype=np.float32):
    """A Gemma 4 layer module: sandwich norms, q and k norms and its
    per-layer input's gate, projection and norm on the module itself.
    """
    shape = {
        **shapes(width, heads, groups, head, hidden),
        "per_layer_input_gate": (ple, width),
        "per_layer_projection": (width, ple),
        "post_per_layer_input_norm": (width,),
    }
    return module(rng, shape, (*GEMMA, *PER_LAYER), dtype)


def test_a_per_layer_input_on_the_module_reads_as_a_ple_block():
    """Gemma 4's per-layer input parts on the layer module are read as
    EmbeddingGemma 2's under ``ple_block``, and the oracle adds the gated
    input, scaled by ``ple_scale``, after the feed-forward.
    """
    rng = np.random.default_rng(15)
    w = gemma4(rng)
    block = SimpleNamespace(**{n: p for n, p in vars(w).items() if n not in PER_LAYER})
    block.ple_block = SimpleNamespace(**{n: vars(w)[n] for n in PER_LAYER})
    bare = SimpleNamespace(**{n: p for n, p in vars(w).items() if n not in PER_LAYER})
    x = rng.standard_normal((N, E)).astype(np.float32)
    ple = rng.standard_normal((N, P)).astype(np.float32)
    angles = rng.standard_normal((N, D)).astype(np.float32)
    o = oracle()
    attend = partial(o.attend, causal=True)
    c = 2**-0.5
    layer = Layer(H, G, D, 1e-6, "gelu_pytorch_tanh", scale=1.0, v_norm=True)
    layer = dataclasses.replace(layer, ple_scale=c)
    got = layer.oracle(o, w, x, attend, angles, ple=ple)
    np.testing.assert_array_equal(
        got, layer.oracle(o, block, x, attend, angles, ple=ple)
    )
    y = layer.oracle(o, bare, x, attend, angles)
    g = Oracle.gelu_tanh(y @ w.per_layer_input_gate.weight.T) * (ple * np.float32(c))
    want = y + rms(
        g @ w.per_layer_projection.weight.T, w.post_per_layer_input_norm.weight
    )
    np.testing.assert_allclose(got, want, rtol=1e-5, atol=1e-6)


def test_a_layer_sharing_keys_and_values_attends_over_the_earlier_layers():
    """A layer sharing an earlier layer's keys and values hands its
    attention none of its own; given the same keys and values, it is the
    layer that projects them and attends over the earlier layer's anyway.
    """
    rng = np.random.default_rng(16)
    w = module(rng, shapes(E, H, G, D, F), GEMMA)
    x = rng.standard_normal((N, E)).astype(np.float32)
    k, v = rng.standard_normal((2, N, G, D)).astype(np.float32)
    angles = rng.standard_normal((N, D)).astype(np.float32)
    o = oracle()
    given = []

    def earlier(q, keys, values, **kw):
        given.append((keys, values))
        return o.attend(q, k, v, causal=True, **kw)

    layer = Layer(H, G, D, 1e-6, "gelu_pytorch_tanh", scale=1.0, v_norm=True)
    shared = dataclasses.replace(layer, shares_kv=True)
    got = shared.oracle(o, w, x, earlier, angles)
    assert given == [(None, None)]
    np.testing.assert_array_equal(got, layer.oracle(o, w, x, earlier, angles))


class Sharing(iron.Graph):
    """``layer`` on the Gemma 4 module ``w`` at ``T`` rows and its per-layer
    input, turned by nothing, attending over a held cache where it shares an
    earlier layer's.
    """

    def __init__(self, layer, w):
        self.layer, self.weights = layer, w
        self.keys = iron.state((T, layer.groups, layer.head_dim))
        self.values = iron.state((T, layer.groups, layer.head_dim))
        turn = np.tile(np.float32([1, 0]), (T, layer.head_dim // 2))
        self.angles = iron.weight(turn.astype(bfloat16))

    def body(self, x, ple):
        layer = self.layer

        def attend(q, k, v, *, scale, window):
            o = MHA.step(
                q,
                self.keys if k is None else k,
                self.values if v is None else v,
                heads_interleaved=True,
                kv_interleaved=True,
                causal=False,
                scale=scale,
            )
            return o.reshape(T, layer.heads * layer.head_dim)

        return layer.step(self.weights, x, attend, self.angles, ple=ple)


@pytest.mark.usefixtures("npu2")
def test_a_layer_sharing_keys_and_values_projects_none():
    w = gemma4(
        np.random.default_rng(17), WIDTH, HEADS, GROUPS, HEAD, HIDDEN, 256, bfloat16
    )
    layer = Layer(
        HEADS,
        GROUPS,
        HEAD,
        1e-6,
        "gelu_pytorch_tanh",
        scale=1.0,
        v_norm=True,
        accurate=True,
    )
    shape = dict(x=(T, WIDTH), ple=(T, 256))
    own = ops(Sharing(layer, w).trace(**shape))
    shared = ops(Sharing(dataclasses.replace(layer, shares_kv=True), w).trace(**shape))
    # Its k and v projections, k's and v's norms and k's rotation.
    assert own - shared == Counter(GEMM=2, RMSNorm=2, RoPE=1)
    assert not shared - own


@pytest.mark.usefixtures("npu2")
def test_a_per_layer_input_s_graph_through_its_operators_references_is_its_oracle():
    """A Gemma 4 layer and its per-layer input over ``ple_scale``, folded
    into the input's norm, run through each operator's reference, is its
    oracle within bf16's rounding of each of its steps; an oracle without
    the per-layer input is not.
    """
    rng = np.random.default_rng(18)
    w = gemma4(rng, WIDTH, HEADS, GROUPS, HEAD, HIDDEN, 256, bfloat16)
    for n in ("pre_feedforward_layernorm", "post_per_layer_input_norm"):
        vars(w)[n].weight += bfloat16(1)
    bare = SimpleNamespace(**{n: p for n, p in vars(w).items() if n not in PER_LAYER})
    layer = Layer(
        HEADS,
        GROUPS,
        HEAD,
        1e-6,
        "gelu_pytorch_tanh",
        scale=1.0,
        v_norm=True,
        accurate=True,
        ple_scale=2**-0.5,
    )
    x = rng.standard_normal((T, WIDTH)).astype(bfloat16)
    ple = rng.standard_normal((T, 256)).astype(bfloat16)
    got = np.asarray(Sharing(layer, w).reference(x, ple), np.float32)
    o = oracle()
    xf, pf = np.asarray(x, np.float32), np.asarray(ple, np.float32)
    angles = np.tile(np.float32([1, 0]), (T, HEAD // 2))

    def error(module):
        want = layer.oracle(o, widen(module), xf, o.attend, angles, ple=pf)
        return np.linalg.norm(got - want) / np.linalg.norm(want)

    # About 30 steps, each rounded once to bf16 (2 ** -9 relative).
    assert error(w) < 30 * 2**-9
    assert error(bare) > 30 * 2**-9
