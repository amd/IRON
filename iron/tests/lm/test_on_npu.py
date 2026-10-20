# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every model records, device-free, at its toy shape, every step of every
version a device operator: none of a model's call path hides host compute
behind a step the device never runs. A step that is not one fails with its
class, so a future graph that slips in a bare numpy op is caught here
rather than on hardware.

Each model is built the way its own tests already do: a real toy
``Checkpoint`` of its own tensor names and shapes (``names()`` beside its
toy config, most ported from ``tests/applications/<name>/reference/test.py``,
the one place several of these already proved right against transformers),
filled with drawn weights (``.tree("random")``) and loaded through the
model's own ``__init__`` and ``load_state_dict`` or ``load_layers``.
"""

import dataclasses

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.gemma3.model import Gemma3, Gemma3Config
from iron.applications.gemma4.model import Gemma4, Gemma4Config
from iron.applications.granite.model import Granite, GraniteConfig
from iron.applications.granite_hybrid.model import GraniteHybrid, GraniteHybridConfig
from iron.applications.idefics3.model import (
    SmolVLM,
    SmolVLMConfig,
    SmolVLMText,
    SmolVLMTextConfig,
)
from iron.applications.idefics3.vision.model import VisionConfig as SmolVLMVisionConfig
from iron.applications.idefics3.vision.model import VisionTower as SmolVLMVisionTower
from iron.applications.lfm2.model import Lfm2, Lfm2Config
from iron.applications.llama.model import Llama, LlamaConfig
from iron.applications.ministral3.model import Ministral3, Ministral3Config
from iron.applications.phi3.model import Phi4, Phi4Config
from iron.applications.qwen2.model import Qwen2, Qwen2Config
from iron.applications.qwen3.model import Qwen3
from iron.applications.qwen3_5.model import Qwen35, Qwen35Config
from iron.applications.qwen3_embedding.model import Qwen3Embedding
from iron.applications.qwen3_moe.model import Qwen3Moe, Qwen3MoeConfig
from iron.applications.resnet.model import ResNet, ResNetConfig
from iron.applications.smollm2.model import SmolLM2
from iron.applications.smollm3.model import SmolLM3, SmolLM3Config
from iron.applications.whisper.model import Whisper, WhisperConfig
from iron.applications.yolox.model import YOLOXNano
from iron.common.declare.operator import Operator
from iron.lm import DecoderConfig, Multimodal
from iron.tests.support.llama_model import checkpoint, shapes

pytestmark = pytest.mark.usefixtures("npu2")


def steps(model, calls: list[dict] | None = None) -> list[Operator]:
    """Every step's operator, over every version ``calls`` lists, or
    ``model.shapes()``'s for a ``Model`` with no single shape of its own.
    """
    out = []
    for call in calls if calls is not None else model.shapes():
        out += [step.op for step in model.record(**call).steps]
    return out


def assert_on_npu(model, calls: list[dict] | None = None) -> None:
    """Every step of every version of ``model`` is a device ``Operator``."""
    recorded = steps(model, calls)
    assert recorded, f"{type(model).__name__}: no steps recorded"
    not_device = [op for op in recorded if not isinstance(op, Operator)]
    assert not not_device, [
        f"{type(op).__module__}.{type(op).__name__}" for op in not_device
    ]


# ---------------------------------------------------------------------------
# Plain decoders: CausalLM subclasses with no tower or encoder of their own.
# Each config and names() is the toy its own reference test checks against
# transformers; only the accuracy-only bits (seeds, the golden) are dropped.


LLAMA = LlamaConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=16,
    num_key_value_heads=4,
    head_dim=64,
    intermediate_size=2048,
    rope_theta=500000.0,
    max_seq_len=256,
    prefill_chunk=256,
)

QWEN2 = Qwen2Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    intermediate_size=1024,
    rope_theta=1000000.0,
    max_seq_len=256,
    prefill_chunk=256,
)

QWEN3 = DecoderConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=1000000.0,
    max_seq_len=256,
    prefill_chunk=256,
)

GRANITE = GraniteConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    intermediate_size=1024,
    rope_theta=10000.0,
    max_seq_len=256,
    prefill_chunk=256,
    tie_word_embeddings=False,
    attention_multiplier=0.0625,
    residual_multiplier=0.22,
    embedding_multiplier=12.0,
    logits_scaling=8.0,
)

PHI3 = Phi4Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=64,
    intermediate_size=512,
    rope_theta=10000.0,
    max_seq_len=256,
    partial_rotary_factor=0.5,
    prefill_chunk=256,
)

MINISTRAL3 = Ministral3Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=1000000.0,
    max_seq_len=256,
    prefill_chunk=256,
)

SMOLLM3 = SmolLM3Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=8,
    num_key_value_heads=2,
    intermediate_size=1024,
    rope_theta=5000000.0,
    max_seq_len=256,
    prefill_chunk=256,
    no_rope_layers=(1, 1, 1, 0),
)

GEMMA3 = Gemma3Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=4,
    num_key_value_heads=1,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=1000000.0,
    # A prompt chunk's rows are flm.ProjectionGEMM's M, a multiple of 256;
    # the reference test's own 64-row chunk only ever runs through
    # graph.reference(), never record()'s real operators.
    max_seq_len=512,
    prefill_chunk=256,
    sliding_window=8,
    layer_types=("sliding_attention", "full_attention") * 2,
)

GEMMA4 = Gemma4Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=6,
    num_attention_heads=4,
    num_key_value_heads=1,
    head_dim=128,
    intermediate_size=512,
    rope_theta=10000.0,
    max_seq_len=512,
    prefill_chunk=256,
    sliding_window=8,
    layer_types=("sliding_attention", "full_attention") * 3,
    global_head_dim=256,
    num_kv_shared_layers=2,
    use_double_wide_mlp=True,
    ple_dim=128,
    final_logit_softcapping=5.0,
)

LFM2 = Lfm2Config(
    vocab_size=512,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=64,
    rope_theta=1e6,
    max_seq_len=1024,
    prefill_chunk=256,
    block_ff_dim=1024,
    full_attn_idxs=(1, 3),
)

QWEN3_MOE = Qwen3MoeConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=1000000.0,
    max_seq_len=256,
    prefill_chunk=256,
    # flm.ProjectionGEMM's N (the router's output width) is a multiple of 64.
    num_experts=64,
    num_experts_per_tok=2,
    moe_intermediate_size=256,
    norm_topk_prob=True,
)

QWEN3_5 = Qwen35Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=4,
    num_key_value_heads=1,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=10000000.0,
    max_seq_len=256,
    prefill_chunk=256,
    layer_types=("linear_attention", "full_attention") * 2,
    linear_conv_kernel_dim=4,
    linear_key_head_dim=64,
    linear_value_head_dim=64,
    linear_num_key_heads=2,
    # flm.ProjectionGEMM's N (in_proj_a/b's width, linear_num_value_heads)
    # is a multiple of 64.
    linear_num_value_heads=64,
)

GRANITE_HYBRID = GraniteHybridConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=8,
    num_key_value_heads=2,
    intermediate_size=256,
    max_seq_len=256,
    prefill_chunk=256,
    attention_multiplier=0.0625,
    residual_multiplier=0.22,
    embedding_multiplier=12.0,
    logits_scaling=8.0,
    tie_word_embeddings=False,
    layer_types=("mamba", "attention", "mamba", "mamba"),
    position_embedding_type="nope",
    shared_intermediate_size=512,
    # flm.ProjectionGEMM's N (the router's output width) is a multiple of 64.
    num_local_experts=64,
    num_experts_per_tok=2,
    # flm.ProjectionGEMM's N (dt's width, mamba_n_heads) is a multiple of 64.
    mamba_n_heads=64,
    mamba_d_head=64,
    mamba_d_state=64,
    mamba_n_groups=2,
)


def names_qwen2(c: Qwen2Config) -> dict[str, tuple[int, ...]]:
    Q, KV = c.num_attention_heads * c.head_dim, c.num_key_value_heads * c.head_dim
    out = shapes(c)
    for i in range(c.num_hidden_layers):
        a = f"model.layers.{i}.self_attn"
        out |= {
            f"{a}.q_proj.bias": (Q,),
            f"{a}.k_proj.bias": (KV,),
            f"{a}.v_proj.bias": (KV,),
        }
    return out


def names_qwen3(c: DecoderConfig) -> dict[str, tuple[int, ...]]:
    out = shapes(c)
    for i in range(c.num_hidden_layers):
        a = f"model.layers.{i}.self_attn"
        out |= {
            f"{a}.q_norm.weight": (c.head_dim,),
            f"{a}.k_norm.weight": (c.head_dim,),
        }
    return out


def names_granite(c: GraniteConfig) -> dict[str, tuple[int, ...]]:
    return shapes(c) | {"lm_head.weight": (c.vocab_size, c.hidden_size)}


def names_phi3(c: Phi4Config) -> dict[str, tuple[int, ...]]:
    E, F, V = c.hidden_size, c.intermediate_size, c.vocab_size
    Q, KV = c.num_attention_heads * c.head_dim, c.num_key_value_heads * c.head_dim
    out = {"model.embed_tokens.weight": (V, E), "model.norm.weight": (E,)}
    for i in range(c.num_hidden_layers):
        p = f"model.layers.{i}"
        out |= {
            f"{p}.input_layernorm.weight": (E,),
            f"{p}.self_attn.qkv_proj.weight": (Q + 2 * KV, E),
            f"{p}.self_attn.o_proj.weight": (E, Q),
            f"{p}.post_attention_layernorm.weight": (E,),
            f"{p}.mlp.gate_up_proj.weight": (2 * F, E),
            f"{p}.mlp.down_proj.weight": (E, F),
        }
    return out


def names_ministral3(c: Ministral3Config) -> dict[str, tuple[int, ...]]:
    return shapes(c) | {"lm_head.weight": (c.vocab_size, c.hidden_size)}


def names_gemma3(c: Gemma3Config) -> dict[str, tuple[int, ...]]:
    out = shapes(c)
    for i in range(c.num_hidden_layers):
        p = f"model.layers.{i}"
        out |= {
            f"{p}.self_attn.q_norm.weight": (c.head_dim,),
            f"{p}.self_attn.k_norm.weight": (c.head_dim,),
            f"{p}.pre_feedforward_layernorm.weight": (c.hidden_size,),
            f"{p}.post_feedforward_layernorm.weight": (c.hidden_size,),
        }
    return out


def names_gemma4(c: Gemma4Config) -> dict[str, tuple[int, ...]]:
    L, E, P, V = c.num_hidden_layers, c.hidden_size, c.ple_dim, c.vocab_size
    H, G = c.num_attention_heads, c.num_key_value_heads
    model = "model.language_model"
    out = {
        f"{model}.embed_tokens.weight": (V, E),
        f"{model}.norm.weight": (E,),
        f"{model}.embed_tokens_per_layer.weight": (V, L * P),
        f"{model}.per_layer_model_projection.weight": (L * P, E),
        f"{model}.per_layer_projection_norm.weight": (P,),
    }
    for i in range(L):
        D = c.global_head_dim if c.full(i) else c.head_dim
        I = c.intermediate_size * (2 if c.owner(i) != i else 1)
        layer = f"{model}.layers.{i}"
        out |= {
            f"{layer}.self_attn.q_proj.weight": (H * D, E),
            f"{layer}.self_attn.o_proj.weight": (E, H * D),
            f"{layer}.self_attn.q_norm.weight": (D,),
            f"{layer}.mlp.gate_proj.weight": (I, E),
            f"{layer}.mlp.up_proj.weight": (I, E),
            f"{layer}.mlp.down_proj.weight": (E, I),
            f"{layer}.per_layer_input_gate.weight": (P, E),
            f"{layer}.per_layer_projection.weight": (E, P),
            f"{layer}.layer_scalar": (1,),
            f"{layer}.self_attn.k_proj.weight": (G * D, E),
            f"{layer}.self_attn.v_proj.weight": (G * D, E),
            f"{layer}.self_attn.k_norm.weight": (D,),
        }
        out |= {
            f"{layer}.{norm}.weight": (E,)
            for norm in (
                "input_layernorm",
                "post_attention_layernorm",
                "pre_feedforward_layernorm",
                "post_feedforward_layernorm",
                "post_per_layer_input_norm",
            )
        }
    return out


def names_lfm2(c: Lfm2Config) -> dict[str, tuple[int, ...]]:
    E, F, D, K = c.hidden_size, c.intermediate_size, c.head_dim, c.conv_kernel
    Q, KV = c.num_attention_heads * D, c.num_key_value_heads * D
    out = {
        "model.embed_tokens.weight": (c.vocab_size, E),
        "model.embedding_norm.weight": (E,),
    }
    for i in range(c.num_hidden_layers):
        p = f"model.layers.{i}"
        out |= {
            f"{p}.operator_norm.weight": (E,),
            f"{p}.ffn_norm.weight": (E,),
            f"{p}.feed_forward.w1.weight": (F, E),
            f"{p}.feed_forward.w3.weight": (F, E),
            f"{p}.feed_forward.w2.weight": (E, F),
        }
        if i in c.full_attn_idxs:
            out |= {
                f"{p}.self_attn.q_proj.weight": (Q, E),
                f"{p}.self_attn.k_proj.weight": (KV, E),
                f"{p}.self_attn.v_proj.weight": (KV, E),
                f"{p}.self_attn.out_proj.weight": (E, Q),
                f"{p}.self_attn.q_layernorm.weight": (D,),
                f"{p}.self_attn.k_layernorm.weight": (D,),
            }
        else:
            out |= {
                f"{p}.conv.in_proj.weight": (3 * E, E),
                f"{p}.conv.conv.weight": (E, 1, K),
                f"{p}.conv.out_proj.weight": (E, E),
            }
    return out


def names_qwen3_moe(c: Qwen3MoeConfig) -> dict[str, tuple[int, ...]]:
    out = shapes(c)
    out["lm_head.weight"] = (c.vocab_size, c.hidden_size)
    E, M = c.hidden_size, c.moe_intermediate_size
    for i in range(c.num_hidden_layers):
        p = f"model.layers.{i}"
        out |= {
            f"{p}.self_attn.q_norm.weight": (c.head_dim,),
            f"{p}.self_attn.k_norm.weight": (c.head_dim,),
            f"{p}.mlp.gate.weight": (c.num_experts, E),
        }
        for name in ("gate_proj", "up_proj", "down_proj"):
            del out[f"{p}.mlp.{name}.weight"]
        for j in range(c.num_experts):
            expert = f"{p}.mlp.experts.{j}"
            out |= {
                f"{expert}.gate_proj.weight": (M, E),
                f"{expert}.up_proj.weight": (M, E),
                f"{expert}.down_proj.weight": (E, M),
            }
    return out


def names_qwen3_5(c: Qwen35Config) -> dict[str, tuple[int, ...]]:
    E, V, I = c.hidden_size, c.vocab_size, c.intermediate_size
    H, G, D = c.num_attention_heads, c.num_key_value_heads, c.head_dim
    Hv, Dv, C = c.linear_num_value_heads, c.linear_value_head_dim, c.conv_channels
    model = "model.language_model"
    out = {f"{model}.embed_tokens.weight": (V, E), f"{model}.norm.weight": (E,)}
    for i, kind in enumerate(c.layer_types):
        p = f"{model}.layers.{i}"
        out |= {
            f"{p}.input_layernorm.weight": (E,),
            f"{p}.post_attention_layernorm.weight": (E,),
            f"{p}.mlp.gate_proj.weight": (I, E),
            f"{p}.mlp.up_proj.weight": (I, E),
            f"{p}.mlp.down_proj.weight": (E, I),
        }
        if kind == "full_attention":
            a = f"{p}.self_attn"
            out |= {
                f"{a}.q_proj.weight": (2 * H * D, E),
                f"{a}.k_proj.weight": (G * D, E),
                f"{a}.v_proj.weight": (G * D, E),
                f"{a}.o_proj.weight": (E, H * D),
                f"{a}.q_norm.weight": (D,),
                f"{a}.k_norm.weight": (D,),
            }
        else:
            a = f"{p}.linear_attn"
            out |= {
                f"{a}.in_proj_qkv.weight": (C, E),
                f"{a}.in_proj_z.weight": (Hv * Dv, E),
                f"{a}.in_proj_b.weight": (Hv, E),
                f"{a}.in_proj_a.weight": (Hv, E),
                f"{a}.conv1d.weight": (C, 1, c.linear_conv_kernel_dim),
                f"{a}.dt_bias": (Hv,),
                f"{a}.A_log": (Hv,),
                f"{a}.norm.weight": (Dv,),
                f"{a}.out_proj.weight": (E, Hv * Dv),
            }
    return out


def names_granite_hybrid(c: GraniteHybridConfig) -> dict[str, tuple[int, ...]]:
    E, D = c.hidden_size, c.head_dim
    S, M = c.shared_intermediate_size, c.intermediate_size
    X, H, N = c.num_local_experts, c.mamba_n_heads, c.mamba_d_state
    I = H * c.mamba_d_head
    channels = I + 2 * c.mamba_n_groups * N
    out = {
        "model.embed_tokens.weight": (c.vocab_size, E),
        "model.norm.weight": (E,),
        "lm_head.weight": (c.vocab_size, E),
    }
    for i in range(c.num_hidden_layers):
        p = f"model.layers.{i}"
        out |= {
            f"{p}.input_layernorm.weight": (E,),
            f"{p}.post_attention_layernorm.weight": (E,),
            f"{p}.shared_mlp.input_linear.weight": (2 * S, E),
            f"{p}.shared_mlp.output_linear.weight": (E, S),
            f"{p}.block_sparse_moe.router.layer.weight": (X, E),
            f"{p}.block_sparse_moe.input_linear.weight": (X, 2 * M, E),
            f"{p}.block_sparse_moe.output_linear.weight": (X, E, M),
        }
        if c.attends(i):
            Q, KV = c.num_attention_heads * D, c.num_key_value_heads * D
            out |= {
                f"{p}.self_attn.q_proj.weight": (Q, E),
                f"{p}.self_attn.k_proj.weight": (KV, E),
                f"{p}.self_attn.v_proj.weight": (KV, E),
                f"{p}.self_attn.o_proj.weight": (E, Q),
            }
        else:
            m = f"{p}.mamba"
            out |= {
                f"{m}.in_proj.weight": (I + channels + H, E),
                f"{m}.conv1d.weight": (channels, 1, c.mamba_d_conv),
                f"{m}.conv1d.bias": (channels,),
                f"{m}.dt_bias": (H,),
                f"{m}.A_log": (H,),
                f"{m}.D": (H,),
                f"{m}.norm.weight": (I,),
                f"{m}.out_proj.weight": (E, I),
            }
    return out


DECODERS = [
    (Llama, LLAMA, shapes(LLAMA)),
    (Qwen2, QWEN2, names_qwen2(QWEN2)),
    (Qwen3, QWEN3, names_qwen3(QWEN3)),
    (SmolLM2, LLAMA, shapes(LLAMA)),
    (Granite, GRANITE, names_granite(GRANITE)),
    (Phi4, PHI3, names_phi3(PHI3)),
    (Ministral3, MINISTRAL3, names_ministral3(MINISTRAL3)),
    (SmolLM3, SMOLLM3, shapes(SMOLLM3)),
    (Gemma3, GEMMA3, names_gemma3(GEMMA3)),
    (Gemma4, GEMMA4, names_gemma4(GEMMA4)),
    (Lfm2, LFM2, names_lfm2(LFM2)),
    (Qwen3Moe, QWEN3_MOE, names_qwen3_moe(QWEN3_MOE)),
    (Qwen35, QWEN3_5, names_qwen3_5(QWEN3_5)),
    (GraniteHybrid, GRANITE_HYBRID, names_granite_hybrid(GRANITE_HYBRID)),
]


@pytest.mark.parametrize(
    "model_cls,config,named", DECODERS, ids=[cls.__name__ for cls, _, _ in DECODERS]
)
def test_decoder_is_on_npu(model_cls, config, named):
    weights = checkpoint(config, named).tree("random")
    assert_on_npu(model_cls(config, weights))


# ---------------------------------------------------------------------------
# Encoders with no tower of their own.


def test_qwen3_embedding_is_on_npu():
    named = {k.removeprefix("model."): v for k, v in names_qwen3(QWEN3).items()}
    weights = checkpoint(QWEN3, named).tree("random")
    assert_on_npu(Qwen3Embedding(QWEN3, weights))


RESNET = ResNetConfig(
    embedding_size=64,
    hidden_sizes=(256, 512, 1024, 2048),
    depths=(2, 1, 1, 1),
    image_size=96,
    num_labels=10,
)


def names_resnet(c: ResNetConfig) -> dict[str, tuple[int, ...]]:
    """Each float tensor of a ResNet checkpoint of ``c``'s shape, by name;
    every BatchNorm also holds an int64 ``num_batches_tracked``.
    """
    out = {}

    def conv(path, cin, cout, k=1):
        out[f"{path}.convolution.weight"] = (cout, cin, k, k)
        for name in ("weight", "bias", "running_mean", "running_var"):
            out[f"{path}.normalization.{name}"] = (cout,)

    conv("resnet.embedder.embedder", 3, c.embedding_size, 7)
    widths = (c.embedding_size, *c.hidden_sizes)
    for s, depth in enumerate(c.depths):
        for i in range(depth):
            p = f"resnet.encoder.stages.{s}.layers.{i}"
            cin, cout = widths[s + 1] if i else widths[s], widths[s + 1]
            if cin != cout or (s and not i):
                conv(f"{p}.shortcut", cin, cout)
            conv(f"{p}.layer.0", cin, cout // 4)
            conv(f"{p}.layer.1", cout // 4, cout // 4, 3)
            conv(f"{p}.layer.2", cout // 4, cout)
    out["classifier.1.weight"] = (c.num_labels, c.hidden_sizes[-1])
    out["classifier.1.bias"] = (c.num_labels,)
    return out


def test_resnet_is_on_npu():
    # ResNet is a plain Graph, not a Model: one shape, no shapes().
    named = names_resnet(RESNET)
    weights = checkpoint(RESNET, named).tree("random")
    for name in named:
        if name.endswith("normalization.weight"):
            node = weights
            for part in name.split(".")[:-1]:
                node = node[int(part)] if part.isdigit() else getattr(node, part)
            node.num_batches_tracked = np.zeros((), np.int64)
    model = ResNet(RESNET, weights)
    S = RESNET.image_size // 2 + 3
    assert_on_npu(model, [dict(image=((S, S * 16), bfloat16))])


def _base_conv(path, cin, cout, k=1, groups=1) -> dict[str, tuple[int, ...]]:
    # bn.num_batches_tracked (int64, scalar) is set directly on the loaded
    # tree below: filled("random")'s 0-d draw is a bare numpy scalar, not
    # an array, which param() refuses, and one checkpoint holds one dtype.
    return {
        f"{path}.conv.weight": (cout, cin // groups, k, k),
        f"{path}.bn.weight": (cout,),
        f"{path}.bn.bias": (cout,),
        f"{path}.bn.running_mean": (cout,),
        f"{path}.bn.running_var": (cout,),
    }


def _dwconv(path, cin, cout, k=3) -> dict[str, tuple[int, ...]]:
    return _base_conv(f"{path}.dconv", cin, cin, k, groups=cin) | _base_conv(
        f"{path}.pconv", cin, cout
    )


def _bottleneck(path, channels) -> dict[str, tuple[int, ...]]:
    return _base_conv(f"{path}.conv1", channels, channels) | _dwconv(
        f"{path}.conv2", channels, channels
    )


def _csp_layer(path, cin, cout, depth) -> dict[str, tuple[int, ...]]:
    hidden = cout // 2
    out = (
        _base_conv(f"{path}.conv1", cin, hidden)
        | _base_conv(f"{path}.conv2", cin, hidden)
        | _base_conv(f"{path}.conv3", 2 * hidden, cout)
    )
    for i in range(depth):
        out |= _bottleneck(f"{path}.m.{i}", hidden)
    return out


def _spp(path, channels) -> dict[str, tuple[int, ...]]:
    hidden = channels // 2
    return _base_conv(f"{path}.conv1", channels, hidden) | _base_conv(
        f"{path}.conv2", hidden * 4, channels
    )


def _prediction(path, cin, cout) -> dict[str, tuple[int, ...]]:
    return {f"{path}.weight": (cout, cin, 1, 1), f"{path}.bias": (cout,)}


def names_yolox() -> dict[str, tuple[int, ...]]:
    """Every tensor of YOLOX-Nano's own (fixed, no-config) checkpoint, by
    name: its backbone (``CSPDarknet``), neck (``PAFPN``) and head, mirrored
    from ``applications/yolox/model.py``'s own widths.
    """
    w = 16
    out = _base_conv("model.backbone.backbone.stem.conv", 12, w, 3)
    out |= _dwconv("model.backbone.backbone.dark2.0", w, 2 * w, 3)
    out |= _csp_layer("model.backbone.backbone.dark2.1", 2 * w, 2 * w, 1)
    out |= _dwconv("model.backbone.backbone.dark3.0", 2 * w, 4 * w, 3)
    out |= _csp_layer("model.backbone.backbone.dark3.1", 4 * w, 4 * w, 3)
    out |= _dwconv("model.backbone.backbone.dark4.0", 4 * w, 8 * w, 3)
    out |= _csp_layer("model.backbone.backbone.dark4.1", 8 * w, 8 * w, 3)
    out |= _dwconv("model.backbone.backbone.dark5.0", 8 * w, 16 * w, 3)
    out |= _spp("model.backbone.backbone.dark5.1", 16 * w)
    out |= _csp_layer("model.backbone.backbone.dark5.2", 16 * w, 16 * w, 1)
    n = 64
    out |= _base_conv("model.backbone.lateral_conv0", 4 * n, 2 * n)
    out |= _csp_layer("model.backbone.C3_p4", 4 * n, 2 * n, 1)
    out |= _base_conv("model.backbone.reduce_conv1", 2 * n, n)
    out |= _csp_layer("model.backbone.C3_p3", 2 * n, n, 1)
    out |= _dwconv("model.backbone.bu_conv2", n, n, 3)
    out |= _csp_layer("model.backbone.C3_n3", 2 * n, 2 * n, 1)
    out |= _dwconv("model.backbone.bu_conv1", 2 * n, 2 * n, 3)
    out |= _csp_layer("model.backbone.C3_n4", 4 * n, 4 * n, 1)
    widths, hidden, classes = (n, 2 * n, 4 * n), n, 80
    for i, width in enumerate(widths):
        out |= _base_conv(f"model.head.stems.{i}", width, hidden)
        for branch in ("cls_convs", "reg_convs"):
            for j in range(2):
                out |= _dwconv(f"model.head.{branch}.{i}.{j}", hidden, hidden)
        out |= _prediction(f"model.head.cls_preds.{i}", hidden, classes)
        out |= _prediction(f"model.head.reg_preds.{i}", hidden, 4)
        out |= _prediction(f"model.head.obj_preds.{i}", hidden, 1)
    return out


def test_yolox_is_on_npu():
    # YOLOX has no config: its checkpoint's shape is its own, fixed; the
    # config checkpoint() takes is unused but for named=None's fallback.
    named = names_yolox()
    weights = checkpoint(QWEN3, named).tree("random")
    for name in named:
        if name.endswith("bn.weight"):
            node = weights
            for part in name[: -len(".weight")].split("."):
                node = node[int(part)] if part.isdigit() else getattr(node, part)
            node.num_batches_tracked = np.zeros((), np.int64)
    model = YOLOXNano(weights)
    assert_on_npu(model, [dict(image=((416, 416 * 4), bfloat16))])


# ---------------------------------------------------------------------------
# Towers, standalone.


SMOLVLM_VISION = SmolVLMVisionConfig(
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    intermediate_size=512,
    patch_size=16,
    # side**2 (the patch rows a call takes) is flm.ProjectionGEMM's M, a
    # multiple of 256; the reference test's 128 only runs through reference().
    image_size=256,
    scale_factor=2,
    text_dim=256,
    image_token=511,
)
SMOLVLM_TEXT = SmolVLMTextConfig(
    vocab_size=512,
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    num_key_value_heads=2,
    head_dim=64,
    intermediate_size=512,
    rope_theta=1e5,
    max_seq_len=1024,
    prefill_chunk=256,
)


def names_smolvlm_vision(c: SmolVLMVisionConfig) -> dict[str, tuple[int, ...]]:
    E, F = c.hidden_size, c.intermediate_size
    v = "model.vision_model"
    out = {
        f"{v}.embeddings.patch_embedding.weight": (E, 3, c.patch_size, c.patch_size),
        f"{v}.embeddings.patch_embedding.bias": (E,),
        f"{v}.embeddings.position_embedding.weight": (c.side**2, E),
        f"{v}.post_layernorm.weight": (E,),
        f"{v}.post_layernorm.bias": (E,),
        "model.connector.modality_projection.proj.weight": (
            c.text_dim,
            E * c.scale_factor**2,
        ),
    }
    for i in range(c.num_hidden_layers):
        p = f"{v}.encoder.layers.{i}"
        for norm in ("layer_norm1", "layer_norm2"):
            out |= {f"{p}.{norm}.weight": (E,), f"{p}.{norm}.bias": (E,)}
        for proj in ("q_proj", "k_proj", "v_proj", "out_proj"):
            out |= {
                f"{p}.self_attn.{proj}.weight": (E, E),
                f"{p}.self_attn.{proj}.bias": (E,),
            }
        out |= {
            f"{p}.mlp.fc1.weight": (F, E),
            f"{p}.mlp.fc1.bias": (F,),
            f"{p}.mlp.fc2.weight": (E, F),
            f"{p}.mlp.fc2.bias": (E,),
        }
    return out


def names_smolvlm_text(c: SmolVLMTextConfig) -> dict[str, tuple[int, ...]]:
    text = {
        k.replace("model.", "model.text_model.", 1): v for k, v in shapes(c).items()
    }
    return text | {"lm_head.weight": (c.vocab_size, c.hidden_size)}


def test_smolvlm_vision_tower_is_on_npu():
    weights = checkpoint(SMOLVLM_TEXT, names_smolvlm_vision(SMOLVLM_VISION)).tree(
        "random"
    )
    assert_on_npu(SmolVLMVisionTower(SMOLVLM_VISION, weights))


# ---------------------------------------------------------------------------
# Whisper: an EncoderDecoder, its toy the device-free reference test's own
# (``tests/applications/whisper/test.py``), which builds both the encoder's
# and the decoder's tensors in one checkpoint, as Whisper's own __init__
# reads them.


WHISPER = WhisperConfig(
    vocab_size=512,
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    num_key_value_heads=4,
    intermediate_size=512,
    max_seq_len=448,
    hidden_act="gelu_pytorch_tanh",
    encoder_layers=2,
    encoder_attention_heads=4,
    encoder_ffn_dim=512,
    num_mel_bins=64,
    max_source_positions=200,
)


def names_whisper(c: WhisperConfig) -> dict[str, tuple[int, ...]]:
    E, V = c.hidden_size, c.vocab_size
    out = {
        "model.encoder.conv1.weight": (E, c.num_mel_bins, 3),
        "model.encoder.conv1.bias": (E,),
        "model.encoder.conv2.weight": (E, E, 3),
        "model.encoder.conv2.bias": (E,),
        "model.encoder.embed_positions.weight": (c.max_source_positions, E),
        "model.encoder.layer_norm.weight": (E,),
        "model.encoder.layer_norm.bias": (E,),
        "model.decoder.embed_tokens.weight": (V, E),
        "model.decoder.embed_positions.weight": (c.max_seq_len, E),
        "model.decoder.layer_norm.weight": (E,),
        "model.decoder.layer_norm.bias": (E,),
    }
    stacks = [
        ("model.encoder", c.encoder_layers, c.encoder_ffn_dim, ["self_attn"]),
        (
            "model.decoder",
            c.num_hidden_layers,
            c.intermediate_size,
            ["self_attn", "encoder_attn"],
        ),
    ]
    for stack, layers, F, attentions in stacks:
        for i in range(layers):
            p = f"{stack}.layers.{i}"
            for a in attentions:
                for proj in ("q_proj", "k_proj", "v_proj", "out_proj"):
                    out[f"{p}.{a}.{proj}.weight"] = (E, E)
                    if proj != "k_proj":
                        out[f"{p}.{a}.{proj}.bias"] = (E,)
                for part in ("weight", "bias"):
                    out[f"{p}.{a}_layer_norm.{part}"] = (E,)
            out |= {
                f"{p}.fc1.weight": (F, E),
                f"{p}.fc1.bias": (F,),
                f"{p}.fc2.weight": (E, F),
                f"{p}.fc2.bias": (E,),
                f"{p}.final_layer_norm.weight": (E,),
                f"{p}.final_layer_norm.bias": (E,),
            }
    return out


def test_whisper_is_on_npu():
    weights = checkpoint(WHISPER, names_whisper(WHISPER)).tree("random")
    assert_on_npu(Whisper(WHISPER, weights))


# ---------------------------------------------------------------------------
# Multimodal: a text model and a tower, as one iron.lm.Multimodal.


def test_smolvlm_is_on_npu():
    named = names_smolvlm_text(SMOLVLM_TEXT) | names_smolvlm_vision(SMOLVLM_VISION)
    weights = checkpoint(SMOLVLM_TEXT, named).tree("random")
    fields = {
        f.name: getattr(SMOLVLM_TEXT, f.name) for f in dataclasses.fields(SMOLVLM_TEXT)
    }
    config = SmolVLMConfig(**fields, vision=SMOLVLM_VISION)
    assert_on_npu(SmolVLM(config, weights))
