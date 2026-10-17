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
    for (wa, ba), (wb, bb) in zip(layer.projections(w), layer.projections(fused)):
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


def traced(names, layer, **parts):
    """The steps of ``layer`` on a module of ``names`` and ``parts``,
    traced at ``T`` rows.
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
            return layer.step(self.weights, x, attend, self.angles)

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
    assert all(
        x is y
        for p, q in zip(layer.projections(w), layer.projections(other))
        for x, y in zip(p, q)
    )
    assert all(x is y for x, y in zip(Layer.norms(w), Layer.norms(other)))
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
