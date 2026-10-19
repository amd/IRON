# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The norms and GELU ``F`` refuses, device-free, and EmbeddingGemma 2's
text layer (``SandwichLayer`` and ``PleLayer``, the shared blocks at their
fullest) through its operators' references against Hugging Face's own
Gemma 4 layer.
"""

from types import SimpleNamespace

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Precision
from iron.applications.embedding_gemma2.model import Config, EmbeddingGemma, TextLayer
from iron.lm import EncodeStep, blocks
from iron.lm.checkpoint import nest
from iron.tests.support.layer import shapes

pytestmark = pytest.mark.usefixtures("npu2")

# A layer at a shape every operator in it records at.
T, WIDTH, HEADS, GROUPS, HEAD, HIDDEN = 256, 512, 8, 2, 64, 1024


def module(rng, shape, names, dtype) -> SimpleNamespace:
    """A layer module of ``names`` at ``shape`` drawn from ``rng``, a
    matrix's deviation ``1/sqrt(in)``.
    """
    root = SimpleNamespace()
    for name in names:
        size = shape[name]
        weight = rng.standard_normal(size) / np.sqrt(size[-1] if len(size) == 2 else 1)
        *parents, leaf = name.split(".")
        node = root
        for key in parents:
            node = vars(node).setdefault(key, SimpleNamespace())
        vars(node)[leaf] = SimpleNamespace(weight=weight.astype(dtype))
    return root


# In the order the golden's weights were drawn.
GEMMA = (
    "input_layernorm",
    "post_attention_layernorm",
    "self_attn.q_proj",
    "self_attn.k_proj",
    "self_attn.v_proj",
    "self_attn.o_proj",
    "mlp.gate_proj",
    "mlp.up_proj",
    "mlp.down_proj",
    "pre_feedforward_layernorm",
    "post_feedforward_layernorm",
    "self_attn.q_norm",
    "self_attn.k_norm",
)


def test_an_activation_with_no_operator_is_refused():
    with pytest.raises(ValueError, match="no operator for hidden_act 'gelu'"):
        blocks.activation("gelu")


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

    recorded = Normed().record(x=(T, WIDTH)).steps
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


def test_layer_norm_refuses_an_eps_other_than_its_kernel_s():
    x = SimpleNamespace(shape=(4, WIDTH))
    with pytest.raises(ValueError, match="takes no epsilon"):
        F.layer_norm(x, WIDTH, eps=1e-6)


def test_gelu_refuses_the_exact_form_it_has_no_operator_for():
    with pytest.raises(ValueError, match="only approximate='tanh'"):
        F.gelu(None)


# The per-layer input's width, and the rows of the Gemma layer's test.
PLE, ROWS = 256, 64
# A Gemma text layer's per-layer input, its parts' shapes.
PER_LAYER = {
    "per_layer_input_gate": (PLE, WIDTH),
    "per_layer_projection": (WIDTH, PLE),
    "post_per_layer_input_norm": (WIDTH,),
}


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


class Text(iron.Graph):
    """EmbeddingGemma 2's text layer over the module ``w``, unrotated."""

    def __init__(self, w):
        config = Config(
            hidden_size=WIDTH,
            num_hidden_layers=1,
            num_attention_heads=HEADS,
            intermediate_size=HIDDEN,
            layer_types=("full_attention",),
            global_kv_groups=GROUPS,
            global_head_dim=HEAD,
            ple_dim=PLE,
        )
        self.layer = TextLayer(config, 0)
        self.layer.rope = None
        self.layer.load_state_dict(w)

    def body(self, x, ple):
        return self.layer(x, EncodeStep(ROWS, {}, x), ple)


def gemma_layer(rng) -> SimpleNamespace:
    """A Gemma text layer module drawn from ``rng``."""
    shape = shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN) | PER_LAYER
    w = module(rng, shape, (*GEMMA, *PER_LAYER), bfloat16)
    w.layer_scalar = np.array([0.75], bfloat16)
    return w


def test_gemma_s_text_layer_through_its_operators_references_is_hugging_face_s(
    golden,
):
    """EmbeddingGemma 2's text layer: sandwich norms, q, k and v norms,
    unscaled attention, its per-layer input and ``layer_scalar``, within
    bf16's rounding of each of its steps of Hugging Face's own layer.
    """
    rng = np.random.default_rng(12)
    w = gemma_layer(rng)
    x = rng.standard_normal((ROWS, WIDTH)).astype(bfloat16)
    ple = rng.standard_normal((ROWS, PLE)).astype(bfloat16)
    got = np.asarray(Text(w).reference(x, ple), np.float32)
    reference = golden("gemma_layer", lambda: HuggingFaceGemma(w, x, ple), w, ple)
    want = reference.logits(x.view(np.uint16))
    # Measured 0.013; 0.073 with the v norm left out.
    error = np.linalg.norm(got - want) / np.linalg.norm(want)
    assert error < 10 * 2**-9, error


def test_gemma_s_text_layer_projects_at_highest_precision():
    steps = (
        Text(gemma_layer(np.random.default_rng(0)))
        .record(x=(ROWS, WIDTH), ple=(ROWS, PLE))
        .steps
    )
    gemms = [s.op for s in steps if hasattr(s.op, "precision")]
    assert gemms and {op.precision for op in gemms} == {Precision.HIGHEST}


def test_embeddinggemma_2_loads_a_layer_s_per_layer_input_flat_or_nested():
    """Its per-layer input's weights as IRON's checkpoint names them, or
    under ``ple_block`` as transformers 5 saves them: the same encoder.
    """
    rng = np.random.default_rng(5)
    c = Config(
        vocab_size=64,
        hidden_size=WIDTH,
        num_hidden_layers=2,
        num_attention_heads=HEADS,
        intermediate_size=HIDDEN,
        num_key_value_heads=GROUPS,
        head_dim=HEAD,
        layer_types=("sliding_attention", "full_attention"),
        global_kv_groups=GROUPS,
        global_head_dim=HEAD,
        sliding_window=32,
        ple_dim=PLE,
        max_tokens=ROWS,
    )
    shape = shapes(WIDTH, HEADS, GROUPS, HEAD, HIDDEN)
    shape |= {f"ple_block.{n}": s for n, s in PER_LAYER.items()}
    named = {
        "embed_tokens.weight": (c.vocab_size, WIDTH),
        "embedding_projection.weight": (c.embedding_dim, WIDTH),
        "norm.weight": (WIDTH,),
        "ple.per_layer_model_projection.weight": (2 * PLE, WIDTH),
        "ple.per_layer_projection_norm.weight": (PLE,),
    }
    for i in range(2):
        named[f"layers.{i}.layer_scalar"] = (1,)
        for name in (*GEMMA, *(f"ple_block.{n}" for n in PER_LAYER)):
            named[f"layers.{i}.{name}.weight"] = shape[name]
    tensors = {
        f"language_model.{n}": (rng.standard_normal(s) * 0.05).astype(bfloat16)
        for n, s in sorted(named.items())
    }
    encoder = EmbeddingGemma(c, nest(tensors))
    ids, values = encoder.inputs(rng.integers(3, c.vocab_size, 9))
    got = np.asarray(encoder.reference(ids, **values), np.float32)
    assert np.isfinite(got).all()
    flat = {n.replace(".ple_block.", "."): t for n, t in tensors.items()}
    assert np.array_equal(got, EmbeddingGemma(c, nest(flat)).reference(ids, **values))
