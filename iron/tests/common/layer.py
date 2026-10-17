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
from iron.lm import Layer, Oracle
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
    }


def module(rng, shape, names, dtype=np.float32, bias=False, **parts):
    """A layer module of ``names`` at ``shape`` drawn from ``rng``, each
    projection with a bias if ``bias``, then ``parts`` by name.
    """
    root = SimpleNamespace()
    drawn = {}
    for name in names:
        part = SimpleNamespace(weight=rng.standard_normal(shape[name]).astype(dtype))
        if bias and len(shape[name]) == 2:
            part.bias = rng.standard_normal(shape[name][0]).astype(dtype)
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


def test_the_oracle_is_a_pre_norm_swiglu_layer_with_biases():
    rng = np.random.default_rng(1)
    w = module(rng, shapes(E, H, G, D, F), LLAMA, bias=True)
    x = rng.standard_normal((N, E)).astype(np.float32)
    angles = rng.standard_normal((N, D)).astype(np.float32)
    o = oracle()
    got = Layer(H, G, D, 1e-6).oracle(o, w, x, partial(o.attend, causal=True), angles)

    a, m = w.self_attn, w.mlp
    h = rms(x, w.input_layernorm.weight)
    q = Oracle.rotate((h @ a.q_proj.weight.T + a.q_proj.bias).reshape(N, H, D), angles)
    k = Oracle.rotate((h @ a.k_proj.weight.T + a.k_proj.bias).reshape(N, G, D), angles)
    v = (h @ a.v_proj.weight.T + a.v_proj.bias).reshape(N, G, D)
    x = x + o.attend(q, k, v, causal=True) @ a.o_proj.weight.T + a.o_proj.bias
    h = rms(x, w.post_attention_layernorm.weight)
    gate = h @ m.gate_proj.weight.T + m.gate_proj.bias
    up = h @ m.up_proj.weight.T + m.up_proj.bias
    f = gate / (1 + np.exp(-gate)) * up
    want = x + f @ m.down_proj.weight.T + m.down_proj.bias
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
def test_the_module_decides_the_norms_and_the_biases():
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
