# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4 E2B's text decoder on the shared decoder (``iron.lm``), its
shape read from its checkpoint's ``config.json``, and the whole model,
the decoder with its vision and audio towers (``vision.py``, ``audio.py``)
as one ``iron.lm.Multimodal`` (``Gemma4Multimodal``). Run the text decoder
with ``python -m iron.applications.gemma4.model``.
"""

import dataclasses

import numpy as np
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Precision, lm
from iron.applications.gemma4.audio import AudioConfig, AudioTower
from iron.applications.gemma4.vision import VisionConfig, VisionTower
from iron.lm import (
    Attention,
    CausalLM,
    Decoder,
    DecoderConfig,
    Embedding,
    GatedMLP,
    KVCache,
    Linear,
    Multimodal,
    PleLayer,
    RMSNorm,
    Rope,
    subtree,
)
from iron.operators.copy import Copy
from iron.operators.tanh import Tanh


@dataclasses.dataclass(frozen=True)
class Gemma4Config(DecoderConfig):
    """``DecoderConfig`` under ``text_config``, the global layers' heads and
    RoPE, the shared caches, the per-layer inputs and the logits' cap.
    """

    precision: Precision = lm.not_json(Precision.MEDIUM, kw_only=True)
    json_prefix = "text_config."

    rope_theta: float = dataclasses.field(
        metadata={"json": "rope_parameters.sliding_attention.rope_theta"}
    )
    hidden_act: str = dataclasses.field(
        default="gelu_pytorch_tanh", metadata={"json": "hidden_activation"}
    )
    layer_types: tuple[str, ...] = dataclasses.field(
        kw_only=True, metadata={"convert": tuple}
    )
    global_head_dim: int = 512
    global_rope_theta: float = dataclasses.field(
        default=1000000.0,
        metadata={"json": "rope_parameters.full_attention.rope_theta"},
    )
    partial_rotary_factor: float = dataclasses.field(
        default=0.25,
        metadata={"json": "rope_parameters.full_attention.partial_rotary_factor"},
    )
    num_kv_shared_layers: int = 0
    use_double_wide_mlp: bool = False
    ple_dim: int = dataclasses.field(
        default=256, metadata={"json": "hidden_size_per_layer_input"}
    )
    final_logit_softcapping: float | None = None
    # The placeholders a tower's soft tokens replace, which the per-layer
    # inputs read as the padding token.
    pad_token_id: int = 0
    image_token_id: int | None = dataclasses.field(
        default=None, metadata={"json": "/image_token_id"}
    )
    audio_token_id: int | None = dataclasses.field(
        default=None, metadata={"json": "/audio_token_id"}
    )
    video_token_id: int | None = dataclasses.field(
        default=None, metadata={"json": "/video_token_id"}
    )

    @classmethod
    def from_json(cls, data: dict, source="config.json") -> "Gemma4Config":
        """``DecoderConfig.from_json``.

        Raises:
            ValueError: ``data`` asks for what is not built: keys equal to
                values, experts, an attention soft-cap, bidirectional text,
                a per-layer vocabulary other than the embedding's, or RoPE
                other than the sliding layers' default and the global ones'
                proportional.
        """
        text = dict(data.get("text_config", {}))
        for key in ("attention_k_eq_v", "enable_moe_block", "attn_logit_softcapping"):
            if text.get(key):
                raise ValueError(f"{source}: {key} {text[key]!r} is not built here")
        # "vision" makes only image tokens bidirectional; text has none.
        bidirectional = text.get("use_bidirectional_attention")
        if bidirectional not in (None, False, "vision"):
            raise ValueError(
                f"{source}: bidirectional attention {bidirectional!r} is not built here"
            )
        per_layer = text.get("vocab_size_per_layer_input", text.get("vocab_size"))
        if per_layer != text.get("vocab_size"):
            raise ValueError(
                f"{source}: vocab_size_per_layer_input {per_layer} other than "
                f"vocab_size {text.get('vocab_size')} is not built here"
            )
        rope = text.get("rope_parameters", {})
        for kind, built in (
            ("sliding_attention", "default"),
            ("full_attention", "proportional"),
        ):
            got = rope.get(kind, {}).get("rope_type", built)
            if got != built:
                raise ValueError(f"{source}: {kind} RoPE {got!r} is not built here")
        return super().from_json({**data, "text_config": text}, source)

    def full(self, i: int) -> bool:
        """Whether layer ``i`` is global."""
        return self.layer_types[i] == "full_attention"

    def owner(self, i: int) -> int:
        """The layer whose cache layer ``i`` attends over: its own, or for a
        shared layer the last one before the shared of its kind.
        """
        first = self.num_hidden_layers - self.num_kv_shared_layers
        if i < first:
            return i
        owners = [j for j in range(first) if self.full(j) == self.full(i)]
        if not owners:
            raise ValueError(
                f"Gemma4Config: shared layer {i} has no earlier layer of its kind"
            )
        return owners[-1]


class Gemma4Decoder(Decoder):
    """``Decoder`` and the per-layer inputs' token table, projection and
    norm.
    """

    def __init__(self, c: Gemma4Config, layer):
        super().__init__(c, layer)
        L, P, E = c.num_hidden_layers, c.ple_dim, c.hidden_size
        self.embed_tokens_per_layer = Embedding(c.vocab_size, L * P)
        self.per_layer_model_projection = Linear(E, L * P, False, precision=c.precision)
        self.per_layer_projection_norm = RMSNorm(P, c.eps)


class Gemma4Layer(PleLayer):
    """Layer ``i``: unscaled attention over normed q, k and v, its heads and
    whole context a global layer's where it is one, else within the window,
    and a double-wide MLP on a shared layer where ``use_double_wide_mlp``.
    """

    def __init__(self, c: Gemma4Config, i: int):
        heads = dataclasses.replace(c, head_dim=c.global_head_dim) if c.full(i) else c
        mlp = None
        if c.use_double_wide_mlp and c.owner(i) != i:
            mlp = GatedMLP(
                dataclasses.replace(c, intermediate_size=2 * c.intermediate_size)
            )
        attention = Attention(heads, i, norms="qkv")
        cache = KVCache(heads, None if c.full(i) else c.window)
        super().__init__(c, i, attention, mlp, cache)
        self.self_attn.scaling = 1.0


class Gemma4(CausalLM):
    """Gemma 4's text decoder on ``config``'s shape and a checkpoint's
    ``weights``, the decoder's under ``model.language_model`` (the towers'
    are ``Gemma4Multimodal``'s), from its checkpoint and ``tokenizer.json``.
    """

    config = Gemma4Config
    decoder_class = Gemma4Decoder
    layer_class = Gemma4Layer

    def __init__(self, config: Gemma4Config, weights):
        super().__init__(config, subtree(weights, model=weights.model.language_model))
        c = config
        turned = int(c.partial_rotary_factor * c.global_head_dim // 2)
        full = dataclasses.replace(
            c,
            head_dim=c.global_head_dim,
            rope_theta=c.global_rope_theta,
            # Proportional RoPE: the pairs past ``turned`` stand still.
            rope_scaling=lambda f: np.where(np.arange(f.size) < turned, f, 0),
        )
        rope = Rope(full)
        for i, layer in enumerate(self.layers):
            if c.full(i):
                layer.rope = rope
            if c.owner(i) != i:
                attention = layer.self_attn
                attention.k_proj = attention.v_proj = attention.k_norm = None
                layer.cache = self.layers[c.owner(i)].cache

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        c, m = self.config, self.model
        P, scale = c.ple_dim, np.float32(bfloat16(np.sqrt(c.ple_dim)))
        table = m.embed_tokens_per_layer.weight
        placeholders = [
            t
            for t in (c.image_token_id, c.audio_token_id, c.video_token_id)
            if t is not None
        ]
        for i, layer in enumerate(m.layers):
            # A layer's own columns, scaled, contiguous: one gather a layer.
            rows = table[:, i * P : (i + 1) * P].astype(np.float32) * scale
            rows[placeholders] = rows[c.pad_token_id]
            layer.per_layer_embedding = iron.param(rows.astype(bfloat16))
        m.embed_tokens_per_layer = None

    def lookup(self, ids):
        # The embedding times sqrt(hidden_size) in the weights' dtype.
        return super().lookup(ids) * float(bfloat16(np.sqrt(self.config.hidden_size)))

    def layer(self, call, i, w, x):
        """Layer ``i`` on ``x``, its input from the call's embeddings and
        ids.
        """
        c, m, P = self.config, self.model, self.config.ple_dim
        projection = m.per_layer_model_projection.weight[i * P : (i + 1) * P]
        ple = F.linear(call.embeddings, projection, precision=c.precision)
        # The projection's hidden_size ** -0.5 folded into the norm's
        # epsilon: RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        norm = m.per_layer_projection_norm.weight
        ple = F.rms_norm(ple, (P,), norm, c.eps * c.hidden_size)
        token = Copy.step(iron.weight(w.per_layer_embedding)[call.ids])
        return w(x, call, (ple + token.reshape(ple.shape)) * 2**-0.5)

    def head(self, x):
        """The tied head's logits, soft-capped where the config says."""
        logits, cap = super().head(x), self.config.final_logit_softcapping
        return logits if cap is None else Tanh.step(logits * (1 / cap)) * cap


@dataclasses.dataclass(frozen=True)
class Gemma4MultimodalConfig(Gemma4Config):
    """``Gemma4Config``, its towers' shapes, ``vision`` and ``audio``, and
    the markers either side of a run of an image's or a clip's placeholders.
    """

    boi_token_id: int = dataclasses.field(
        default=255999, metadata={"json": "/boi_token_id"}
    )
    eoi_token_id: int = dataclasses.field(
        default=258882, metadata={"json": "/eoi_token_id"}
    )
    boa_token_id: int = dataclasses.field(
        default=256000, metadata={"json": "/boa_token_id"}
    )
    eoa_token_id: int = dataclasses.field(
        default=258883, metadata={"json": "/eoa_token_id"}
    )
    vision: VisionConfig | None = lm.not_json(None, kw_only=True)
    audio: AudioConfig | None = lm.not_json(None, kw_only=True)

    @classmethod
    def from_checkpoint(cls, path) -> "Gemma4MultimodalConfig":
        text = super().from_checkpoint(path)
        return dataclasses.replace(
            text,
            vision=VisionConfig.from_checkpoint(path),
            audio=AudioConfig.from_checkpoint(path),
        )

    def expand(self, tokens, raw: dict[int, tuple]) -> list[int]:
        """``tokens`` with each placeholder of ``raw`` a run of its tower's
        soft tokens between its markers, as ``Gemma4Processor`` lays it out.
        """
        vision, audio = self.vision, self.audio
        assert vision is not None and audio is not None
        runs = {}
        if self.image_token_id in raw:
            image, max_tokens = raw[self.image_token_id]
            run = [self.image_token_id] * vision.tokens(
                *np.shape(image)[:2], max_tokens
            )
            runs[self.image_token_id] = [self.boi_token_id, *run, self.eoi_token_id]
        if self.audio_token_id in raw:
            (wave,) = raw[self.audio_token_id]
            run = [self.audio_token_id] * audio.tokens(audio.frames(np.size(wave)))
            runs[self.audio_token_id] = [self.boa_token_id, *run, self.eoa_token_id]
        out = []
        for t in tokens:
            out += runs.get(int(t), [int(t)])
        return out


class Gemma4Multimodal(Multimodal):
    """Gemma 4 whole: its text decoder (``Gemma4``) with its vision and audio
    towers' soft tokens at their placeholders. A call takes an image as
    ``(image, max_soft_tokens)`` and a clip as ``(waveform,)``, by placeholder.
    """

    config = Gemma4MultimodalConfig

    def __init__(self, config: Gemma4MultimodalConfig, weights):
        assert config.vision is not None and config.audio is not None
        assert config.image_token_id is not None and config.audio_token_id is not None
        self.config, self.weights = config, weights
        towers = {
            config.image_token_id: VisionTower(config.vision, weights.model),
            config.audio_token_id: AudioTower(config.audio, weights.model),
        }
        super().__init__(Gemma4(config, weights), towers)

    @property
    def hugging_face(self):
        """transformers' Gemma 4, imported only where a golden is recorded."""
        from .hugging_face import HuggingFaceGemma4

        return HuggingFaceGemma4


if __name__ == "__main__":
    lm.main(Gemma4)
