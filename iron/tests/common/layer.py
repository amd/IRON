# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm``'s layer parts (``AttentionSpec``, ``MLPSpec``, ``Norm``,
``DecoderLayerSpec``), device-free: the steps each traces as it is configured,
and EmbeddingGemma 2's text layer, the parts at their fullest, through its
operators' references against Hugging Face's own Gemma 4 layer.
"""

from collections import Counter
from types import SimpleNamespace

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Precision
from iron.lm import AttentionSpec, DecoderLayerSpec, MLPSpec, Norm
from iron.applications.embedding_gemma2.blocks import SandwichLayer, TextLayer
from iron.operators.mha import MHA

pytestmark = pytest.mark.usefixtures("npu2")

# A layer at a shape every operator in it traces at.
T, WIDTH, HEADS, GROUPS, HEAD, HIDDEN = 256, 512, 8, 2, 64, 1024


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


def attending(rows):
    """Attention over every row, as an encoder's."""

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
        return o.reshape(rows, HEADS * HEAD)

    return attend


class Model(iron.Graph):
    """``layer`` on the module ``weights``, every row attending to every
    other, turned by zero angles.
    """

    def __init__(self, layer, weights, rows=T):
        self.part, self.weights, self.rows = layer, weights, rows
        self.angles = iron.weight(np.zeros((rows, HEAD), bfloat16))

    def body(self, x):
        return self.part(self.weights, x, attending(self.rows), self.angles)


def ops(layer, names, **parts) -> Counter:
    """The operators ``layer`` traces on a module of ``names`` and ``parts``."""
    rng = np.random.default_rng(3)
    shape = shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN)
    w = module(rng, shape, names, bfloat16, **parts)
    steps = Model(layer, w).trace(x=(T, WIDTH)).steps
    return Counter(type(s.op).__name__ for s in steps)


def llama(residual=1.0) -> DecoderLayerSpec:
    return DecoderLayerSpec(
        AttentionSpec(HEADS, GROUPS, HEAD, precision=Precision.HIGHEST),
        MLPSpec(precision=Precision.HIGHEST),
        Norm(1e-6),
        residual,
    )


def test_the_parts_decide_the_steps():
    plain = ops(llama(), LLAMA)
    assert plain == Counter(
        GEMM=7, RMSNorm=2, RoPE=2, MHA=1, ElementwiseAdd=2, SiLU=1, ElementwiseMul=1
    )
    gemma = SandwichLayer(
        AttentionSpec(
            HEADS,
            GROUPS,
            HEAD,
            1e-6,
            qk_norm=True,
            v_norm=True,
            precision=Precision.HIGHEST,
        ),
        MLPSpec(precision=Precision.HIGHEST),
        Norm(1e-6),
    )
    # Sandwich norms, q and k norms and the v norm.
    assert ops(gemma, GEMMA) - plain == Counter(RMSNorm=5)
    bias = SimpleNamespace(
        weight=np.zeros((HEADS * HEAD, WIDTH), bfloat16),
        bias=np.zeros(HEADS * HEAD, bfloat16),
    )
    biased = ops(llama(), LLAMA, **{"self_attn.q_proj": bias})
    assert biased - plain == Counter(RowwiseAdd=1)
    scaled = ops(llama(residual=0.25), LLAMA)
    assert plain - scaled == Counter(ElementwiseAdd=2)
    assert scaled - plain == Counter(AXPY=2)


@pytest.mark.parametrize("residual", [1.0, 0.25])
def test_a_one_row_step_keeps_its_rows_through_the_residual(residual):
    """One row projects by GEMV, whose reference output is flat: the
    residual keeps the layer's input shape, scaled or not.
    """
    rng = np.random.default_rng(8)
    w = module(rng, shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN), LLAMA, bfloat16)
    model = Model(llama(residual), w, rows=1)
    got = np.asarray(model.reference(np.ones((1, WIDTH), bfloat16)))
    assert got.shape == (1, WIDTH)
    assert [tuple(h.shape) for h in model.trace(x=(1, WIDTH)).outputs] == [(1, WIDTH)]


def test_an_activation_with_no_operator_is_refused():
    with pytest.raises(ValueError, match="no operator for hidden_act 'gelu'"):
        MLPSpec("gelu")


def test_a_layer_norm_at_another_epsilon_than_its_kernels_is_refused():
    norm = SimpleNamespace(weight=np.ones(WIDTH), bias=np.zeros(WIDTH))
    with pytest.raises(ValueError, match="the kernel takes no epsilon but"):
        Norm(1e-6, bias=True)(norm, SimpleNamespace(shape=(1, WIDTH)))


@pytest.mark.parametrize(
    "norm, steps",
    [
        (lambda x, w: F.rms_norm(x, x.shape[-1:], None, 1e-6), [("RMSNorm", False)]),
        (
            lambda x, w: F.layer_norm(x, x.shape[-1:], w, w),
            [("LayerNorm", True), ("RowwiseAdd", None)],
        ),
    ],
    ids=["rms_unweighted", "layer_weighted_biased"],
)
def test_a_norm_is_its_kernel_weighted_if_given_then_any_bias(norm, steps):
    class Normed(iron.Graph):
        def __init__(self):
            self.w = np.ones(WIDTH, bfloat16)

        def body(self, x):
            return norm(x, self.w)

    recorded = Normed().trace(x=(T, WIDTH)).steps
    assert [
        (type(s.op).__name__, getattr(s.op, "weighted", None)) for s in recorded
    ] == steps


@pytest.mark.parametrize("norm", [F.rms_norm, F.layer_norm], ids=["rms", "layer"])
def test_a_norm_over_another_axis_than_the_last_is_refused(norm):
    x = SimpleNamespace(shape=(4, WIDTH))
    with pytest.raises(
        ValueError, match=rf"\[4\] is not the last axis of input \[4, {WIDTH}\]"
    ):
        norm(x, 4)


def test_a_q_k_or_v_norm_needs_its_epsilon():
    with pytest.raises(ValueError, match="needs its eps"):
        AttentionSpec(HEADS, GROUPS, HEAD, qk_norm=True)


def test_gelu_refuses_the_exact_form_it_has_no_operator_for():
    with pytest.raises(ValueError, match="only approximate='tanh'"):
        F.gelu(None)


# The per-layer input's width, and the rows of the Gemma layer's test.
PLE, ROWS = 256, 64


class HuggingFaceGemma:
    """transformers' Gemma 4 text layer in float32 over the module ``w``:
    its output on ``x`` and the per-layer input ``ple``, every row
    attending to every other, unrotated.
    """

    def __init__(self, w, x, ple):
        import torch
        from transformers.models.gemma4 import modeling_gemma4 as gemma4

        from iron.lm.golden import flat

        config = gemma4.Gemma4TextConfig(
            hidden_size=WIDTH,
            num_attention_heads=HEADS,
            num_key_value_heads=GROUPS,
            head_dim=HEAD,
            intermediate_size=HIDDEN,
            hidden_size_per_layer_input=PLE,
            hidden_activation="gelu_pytorch_tanh",
            rms_norm_eps=1e-6,
            global_head_dim=HEAD,
            layer_types=["full_attention"],
            num_hidden_layers=1,
        )
        config._attn_implementation = "eager"
        layer = gemma4.Gemma4TextDecoderLayer(config, 0).eval()
        state = {k: torch.from_numpy(v) for k, v in flat(w)}
        missing, _ = layer.load_state_dict(state, strict=False)
        assert not missing, missing
        self.layer, self.x, self.ple = layer, x, ple

    def logits(self, _):
        import torch

        x = torch.from_numpy(np.asarray(self.x, np.float32))[None]
        ple = torch.from_numpy(np.asarray(self.ple, np.float32))[None]
        unturned = (torch.ones(1, ROWS, HEAD), torch.zeros(1, ROWS, HEAD))
        with torch.no_grad():
            y = self.layer(
                x,
                per_layer_input=ple,
                position_embeddings=unturned,
                shared_kv_states={},
            )
        return (y[0] if isinstance(y, tuple) else y)[0].numpy()


def test_gemma_s_text_layer_through_its_operators_references_is_hugging_face_s(
    golden,
):
    """EmbeddingGemma 2's text layer: sandwich norms, q, k and v norms,
    unscaled attention, its per-layer input and ``layer_scalar``, within
    bf16's rounding of each of its steps of Hugging Face's own layer.
    """
    rng = np.random.default_rng(12)
    per_layer = {
        "per_layer_input_gate": (PLE, WIDTH),
        "per_layer_projection": (WIDTH, PLE),
        "post_per_layer_input_norm": (WIDTH,),
    }
    shape = shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN) | per_layer
    w = module(rng, shape, (*GEMMA, *per_layer), bfloat16)
    w.layer_scalar = np.array([0.75], bfloat16)
    x = rng.standard_normal((ROWS, WIDTH)).astype(bfloat16)
    ple = rng.standard_normal((ROWS, PLE)).astype(bfloat16)
    layer = TextLayer(
        AttentionSpec(
            HEADS,
            GROUPS,
            HEAD,
            1e-6,
            qk_norm=True,
            v_norm=True,
            scale=1.0,
            precision=Precision.HIGHEST,
        ),
        MLPSpec("gelu_pytorch_tanh", precision=Precision.HIGHEST),
        Norm(1e-6),
    )

    class Text(iron.Graph):
        def __init__(self):
            self.weights = w
            self.scale = np.full(WIDTH, w.layer_scalar[0], bfloat16)

        def body(self, x, ple):
            attend = attending(ROWS)
            return layer(self.weights, x, attend, None, ple=ple, scale=self.scale)

    got = np.asarray(Text().reference(x, ple), np.float32)
    reference = golden("gemma_layer", lambda: HuggingFaceGemma(w, x, ple), w, ple)
    want = reference.logits(x.view(np.uint16))
    # Measured 0.013; 0.073 with the v norm left out.
    error = np.linalg.norm(got - want) / np.linalg.norm(want)
    assert error < 10 * 2**-9, error
