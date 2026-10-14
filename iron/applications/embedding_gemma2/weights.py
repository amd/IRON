# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Where EmbeddingGemma 2's checkpoint keeps each weight: a layout per part
(``iron.lm.Layout``), the text encoder's, the audio tower's and the vision
tower's, and ``Weights``, the trees ``load_weights`` makes of them.
"""

import dataclasses
from pathlib import Path
from types import SimpleNamespace

from iron.lm import Checkpoint, Layout, load_weights, unread_weights

from .config import AudioConfig, Config, VisionConfig


def text_layout(config: Config) -> Layout:
    """The text encoder's weights. A global layer's attention is wider than
    a sliding one's, so the attention weights are listed layer by layer.
    """
    c = config
    E, F, P, V = c.emb_dim, c.hidden_dim, c.ple_dim, c.vocab_size
    model = "language_model"
    layer = f"{model}.layers.{{i}}"
    out = {
        "embedding": (f"{model}.embed_tokens.weight", (V, E)),
        "norm": (f"{model}.norm.weight", (E,)),
        "projection": (f"{model}.embedding_projection.weight", (c.out_dim, E)),
        "ple": (f"{model}.ple.per_layer_model_projection.weight", (c.n_layers * P, E)),
        "ple_norm": (f"{model}.ple.per_layer_projection_norm.weight", (P,)),
        "layers.{i}.norm1": (f"{layer}.input_layernorm.weight", (E,)),
        "layers.{i}.norm2": (f"{layer}.post_attention_layernorm.weight", (E,)),
        "layers.{i}.norm3": (f"{layer}.pre_feedforward_layernorm.weight", (E,)),
        "layers.{i}.norm4": (f"{layer}.post_feedforward_layernorm.weight", (E,)),
        "layers.{i}.scalar": (f"{layer}.layer_scalar", (1,)),
        "layers.{i}.gate": (f"{layer}.mlp.gate_proj.weight", (F, E)),
        "layers.{i}.up": (f"{layer}.mlp.up_proj.weight", (F, E)),
        "layers.{i}.down": (f"{layer}.mlp.down_proj.weight", (E, F)),
        "layers.{i}.ple_gate": (
            f"{layer}.ple_block.per_layer_input_gate.weight",
            (P, E),
        ),
        "layers.{i}.ple_proj": (
            f"{layer}.ple_block.per_layer_projection.weight",
            (E, P),
        ),
        "layers.{i}.ple_norm": (
            f"{layer}.ple_block.post_per_layer_input_norm.weight",
            (E,),
        ),
    }
    for i in range(c.n_layers):
        G, D, _ = c.heads(i)
        attn = f"{model}.layers.{i}.self_attn"
        out |= {
            f"layers.{i}.q": (f"{attn}.q_proj.weight", (c.n_heads * D, E)),
            f"layers.{i}.k": (f"{attn}.k_proj.weight", (G * D, E)),
            f"layers.{i}.v": (f"{attn}.v_proj.weight", (G * D, E)),
            f"layers.{i}.o": (f"{attn}.o_proj.weight", (E, c.n_heads * D)),
            f"layers.{i}.q_norm": (f"{attn}.q_norm.weight", (D,)),
            f"layers.{i}.k_norm": (f"{attn}.k_norm.weight", (D,)),
        }
    return out


def audio_layout(config: AudioConfig) -> Layout:
    """The audio tower's weights and its projection into the text model's
    space. A clipped linear is a namespace of its `weight` and the scalar
    bounds its input and output are clamped to.
    """
    c = config
    E, F, (C0, C1) = c.emb_dim, c.hidden_dim, c.channels
    tower = "audio_tower"
    sub = f"{tower}.subsample_conv_projection"
    layer = f"{tower}.layers.{{i}}"
    out = {
        "conv0": (f"{sub}.layer0.conv.weight", (C0, 1, 3, 3)),
        "norm0": (f"{sub}.layer0.norm.weight", (C0,)),
        "conv1": (f"{sub}.layer1.conv.weight", (C1, C0, 3, 3)),
        "norm1": (f"{sub}.layer1.norm.weight", (C1,)),
        "input_proj": (f"{sub}.input_proj_linear.weight", (E, C1 * c.mels // 4)),
        "output_proj": (f"{tower}.output_proj.weight", (c.output_dim, E)),
        "output_bias": (f"{tower}.output_proj.bias", (c.output_dim,)),
        "projection": (
            "embed_audio.embedding_projection.weight",
            (c.text_dim, c.output_dim),
        ),
        "layers.{i}.norm_pre_attn": (f"{layer}.norm_pre_attn.weight", (E,)),
        "layers.{i}.norm_post_attn": (f"{layer}.norm_post_attn.weight", (E,)),
        "layers.{i}.norm_out": (f"{layer}.norm_out.weight", (E,)),
        "layers.{i}.attn.relative": (
            f"{layer}.self_attn.relative_k_proj.weight",
            (E, E),
        ),
        "layers.{i}.attn.per_dim_scale": (
            f"{layer}.self_attn.per_dim_scale",
            (c.head_dim,),
        ),
        "layers.{i}.conv.depthwise": (
            f"{layer}.lconv1d.depthwise_conv1d.weight",
            (E, 1, c.conv_kernel),
        ),
        "layers.{i}.conv.pre": (f"{layer}.lconv1d.pre_layer_norm.weight", (E,)),
        "layers.{i}.conv.norm": (f"{layer}.lconv1d.conv_norm.weight", (E,)),
    }
    clipped = {
        "conv.start": ("lconv1d.linear_start", (2 * E, E)),
        "conv.end": ("lconv1d.linear_end", (E, E)),
        "attn.q": ("self_attn.q_proj", (E, E)),
        "attn.k": ("self_attn.k_proj", (E, E)),
        "attn.v": ("self_attn.v_proj", (E, E)),
        "attn.post": ("self_attn.post", (E, E)),
    }
    for j in (1, 2):
        ff = f"feed_forward{j}"
        out[f"layers.{{i}}.ff{j}.pre"] = (f"{layer}.{ff}.pre_layer_norm.weight", (E,))
        out[f"layers.{{i}}.ff{j}.post"] = (
            f"{layer}.{ff}.post_layer_norm.weight",
            (E,),
        )
        clipped[f"ff{j}.up"] = (f"{ff}.ffw_layer_1", (F, E))
        clipped[f"ff{j}.down"] = (f"{ff}.ffw_layer_2", (E, F))
    for path, (name, shape) in clipped.items():
        out[f"layers.{{i}}.{path}.weight"] = (f"{layer}.{name}.linear.weight", shape)
        for bound in ("input_min", "input_max", "output_min", "output_max"):
            out[f"layers.{{i}}.{path}.{bound}"] = (f"{layer}.{name}.{bound}", ())
    return out


def vision_layout(config: VisionConfig) -> Layout:
    """The vision tower's weights and its projection into the text model's
    space.
    """
    c = config
    E, F, D = c.emb_dim, c.hidden_dim, c.head_dim
    tower = "vision_tower"
    layer = f"{tower}.encoder.layers.{{i}}"
    out = {
        "patch": (f"{tower}.patch_embedder.input_proj.weight", (E, 3 * c.patch**2)),
        "position": (
            f"{tower}.patch_embedder.position_embedding_table",
            (2, c.positions, E),
        ),
        "projection": ("embed_vision.embedding_projection.weight", (c.text_dim, E)),
        "layers.{i}.norm1": (f"{layer}.input_layernorm.weight", (E,)),
        "layers.{i}.norm2": (f"{layer}.post_attention_layernorm.weight", (E,)),
        "layers.{i}.norm3": (f"{layer}.pre_feedforward_layernorm.weight", (E,)),
        "layers.{i}.norm4": (f"{layer}.post_feedforward_layernorm.weight", (E,)),
        "layers.{i}.gate": (f"{layer}.mlp.gate_proj.linear.weight", (F, E)),
        "layers.{i}.up": (f"{layer}.mlp.up_proj.linear.weight", (F, E)),
        "layers.{i}.down": (f"{layer}.mlp.down_proj.linear.weight", (E, F)),
    }
    for name in "qkvo":
        out[f"layers.{{i}}.{name}"] = (
            f"{layer}.self_attn.{name}_proj.linear.weight",
            (E, E),
        )
    for name in "qk":
        out[f"layers.{{i}}.{name}_norm"] = (
            f"{layer}.self_attn.{name}_norm.weight",
            (D,),
        )
    return out


@dataclasses.dataclass(frozen=True)
class Weights:
    """EmbeddingGemma 2's weights, a tree per part (``load_weights``): the
    text encoder's, the audio tower's and the vision tower's, each tower's
    with its projection into the text model's space.
    """

    text: SimpleNamespace
    audio: SimpleNamespace
    vision: SimpleNamespace

    @classmethod
    def read(
        cls,
        directory,
        config: Config = Config(),
        audio: AudioConfig = AudioConfig(),
        vision: VisionConfig = VisionConfig(),
    ) -> "Weights":
        """The weights of the checkpoint in `directory`, mapped, not read:
        a part's arrays are views of `model.safetensors`.
        """
        tensors = Checkpoint(Path(directory) / "model.safetensors").tensors
        parts = {
            "language_model.": (text_layout(config), config.n_layers),
            ("audio_tower.", "embed_audio."): (audio_layout(audio), audio.n_layers),
            ("vision_tower.", "embed_vision."): (
                vision_layout(vision),
                vision.n_layers,
            ),
        }
        return cls(
            *(
                load_weights(
                    {k: v for k, v in tensors.items() if k.startswith(prefix)},
                    layout,
                    n_layers,
                )
                for prefix, (layout, n_layers) in parts.items()
            )
        )

    @classmethod
    def unread(
        cls,
        config: Config = Config(),
        audio: AudioConfig = AudioConfig(),
        vision: VisionConfig = VisionConfig(),
    ) -> "Weights":
        """The trees `unread_weights` gives, for tracing, building and
        measuring the graphs, none of which reads a weight.
        """
        return cls(
            unread_weights(text_layout(config), config.n_layers),
            unread_weights(audio_layout(audio), audio.n_layers),
            unread_weights(vision_layout(vision), vision.n_layers),
        )
