#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper over ``iron.lm``: a bidirectional audio encoder (``WhisperEncoder``,
an ``iron.lm.Tower``) feeding a causal text decoder through cross attention
(``Whisper``, an ``iron.lm.EncoderDecoder``), judged by Hugging Face's own
model in float32 (``Reference``). Both are ``iron.lm``'s layer parts over
Whisper's modules renamed once at load (``sanitize``); nothing rotates:
the encoder adds a fixed position table after its two convolutions, the
decoder a learned one after its embedding. The shape is read from the
checkpoint's ``config.json``.

The encoder takes the feature extractor's log-mel features (``input_features``),
a zero row before them, as its convolutions' padding.
"""

import dataclasses
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad, lm
import iron.functional as F
from iron.lm import (
    MLP,
    Attention,
    Config,
    Conv1d,
    CrossDecoderLayer,
    DecoderConfig,
    DecoderLayer,
    Derived,
    EncoderDecoder,
    Norm,
    Tower,
)
from iron.lm.golden import Golden, flat, config_json
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gelu import GELU
from iron.operators.gemv import GEMV

# The rows a GEMM's M and MHA's sequence come in whole blocks of.
BLOCK = 64


def bf16(weights):
    """``weights``, an array or a tree of namespaces and lists, each float16
    array rounded once to bf16, the device's copy of an fp16 checkpoint (the
    reference widens the float16 itself); any other array as it is.
    """
    if isinstance(weights, np.ndarray):
        return weights.astype(bfloat16) if weights.dtype == np.float16 else weights
    if isinstance(weights, list):
        return [bf16(w) for w in weights]
    if isinstance(weights, SimpleNamespace):
        return SimpleNamespace(**{k: bf16(w) for k, w in vars(weights).items()})
    return weights


def sanitize(w):
    """A Whisper layer module under the names ``iron.lm``'s parts read."""

    def attention(a):
        return SimpleNamespace(
            q_proj=a.q_proj, k_proj=a.k_proj, v_proj=a.v_proj, o_proj=a.out_proj
        )

    out = SimpleNamespace(
        input_layernorm=w.self_attn_layer_norm,
        self_attn=attention(w.self_attn),
        post_attention_layernorm=w.final_layer_norm,
        mlp=SimpleNamespace(fc1=w.fc1, fc2=w.fc2),
    )
    if "encoder_attn" in vars(w):
        out.encoder_attn = attention(w.encoder_attn)
        out.encoder_attn_layer_norm = w.encoder_attn_layer_norm
    return out


@dataclasses.dataclass(frozen=True)
class WhisperEncoderConfig(Config):
    """The audio encoder's shape (``WhisperConfig.encoder``)."""

    hidden_size: int
    num_hidden_layers: int
    num_attention_heads: int
    intermediate_size: int
    mels: int
    positions: int
    hidden_act: str
    eps: float = dataclasses.field(default=1e-5, kw_only=True)

    @property
    def text_dim(self) -> int:
        """The width of the encoder's output, the decoder's."""
        return self.hidden_size

    @property
    def frames(self) -> int:
        """The log-mel frames of a clip, two a position."""
        return 2 * self.positions

    @property
    def rows(self) -> int:
        """The positions rounded up to whole blocks: the rows every layer
        takes, bounded per call to ``positions``.
        """
        return -(-self.positions // BLOCK) * BLOCK

    @property
    def conv_rows(self) -> int:
        """The frames rounded up to whole blocks: the first convolution's
        output rows.
        """
        return -(-self.frames // BLOCK) * BLOCK

    def layer(self, i: int) -> DecoderLayer:
        H = self.num_attention_heads
        return DecoderLayer(
            Attention(H, H, self.hidden_size // H),
            MLP(self.hidden_act, gated=False),
            Norm(self.eps, bias=True),
        )


@dataclasses.dataclass(frozen=True)
class WhisperConfig(DecoderConfig):
    """Whisper's decoder's shape from its ``config.json``, and its encoder's
    (``encoder()``).
    """

    hidden_size: int = dataclasses.field(metadata={"json": "d_model"})
    num_hidden_layers: int = dataclasses.field(metadata={"json": "decoder_layers"})
    num_attention_heads: int = dataclasses.field(
        metadata={"json": "decoder_attention_heads"}
    )
    num_key_value_heads: int = dataclasses.field(
        metadata={"json": "decoder_attention_heads"}
    )
    intermediate_size: int = dataclasses.field(metadata={"json": "decoder_ffn_dim"})
    rope_theta: float | None = dataclasses.field(default=None, kw_only=True)
    max_seq_len: int = dataclasses.field(metadata={"json": "max_target_positions"})
    prefill_chunk: int = 256
    # Whisper's own "gelu" is exact, which MLP refuses until the pin group
    # brings the kernel; a checkpoint at "gelu_pytorch_tanh" runs.
    hidden_act: str = dataclasses.field(
        default="gelu", metadata={"json": "activation_function"}
    )
    eps: float = dataclasses.field(default=1e-5, kw_only=True)
    encoder_layers: int = dataclasses.field(
        kw_only=True, metadata={"json": "encoder_layers"}
    )
    encoder_heads: int = dataclasses.field(
        kw_only=True, metadata={"json": "encoder_attention_heads"}
    )
    encoder_hidden_dim: int = dataclasses.field(
        kw_only=True, metadata={"json": "encoder_ffn_dim"}
    )
    mels: int = dataclasses.field(kw_only=True, metadata={"json": "num_mel_bins"})
    source_positions: int = dataclasses.field(
        kw_only=True, metadata={"json": "max_source_positions"}
    )

    def layer(self, i: int) -> CrossDecoderLayer:
        H = self.num_attention_heads
        return CrossDecoderLayer(
            Attention(H, H, self.head_dim),
            MLP(self.hidden_act, gated=False),
            Norm(self.eps, bias=True),
        )

    def encoder(self) -> WhisperEncoderConfig:
        """The encoder's shape."""
        return WhisperEncoderConfig(
            self.hidden_size,
            self.encoder_layers,
            self.encoder_heads,
            self.encoder_hidden_dim,
            self.mels,
            self.source_positions,
            self.hidden_act,
            eps=self.eps,
        )


class WhisperEncoder(Tower):
    """Whisper's audio encoder over one clip's log-mel features: two
    convolutions, each then a GELU, the second at stride 2, the position
    table added, then each layer and the final LayerNorm. Its rows are
    ``rows``, bounded per call to ``n``, the clip's positions.

    Args:
        config: The encoder's shape.
        weights: The checkpoint's tree; ``model.encoder`` is read.
    """

    def __init__(self, config: WhisperEncoderConfig, weights):
        c, weights = config, bf16(weights)
        self.whisper_encoder = e = weights.model.encoder
        super().__init__(c, e.layers, c.rows, c.rows)
        if c.hidden_act != "gelu_pytorch_tanh":
            # TODO(pin group): exact GELU, the checkpoint's own "gelu".
            raise ValueError(
                f"WhisperEncoder: no operator for activation {c.hidden_act!r} yet"
            )
        self.conv1 = Conv1d(e.conv1.weight, e.conv1.bias, c.mels)
        self.conv2 = Conv1d(e.conv2.weight, e.conv2.bias, c.hidden_size, stride=2)
        # The second convolution's input: a zero row, then the first's output.
        self.convolved = iron.state((2 * c.rows + 1, c.hidden_size))
        derived = Derived(weights)
        table = np.zeros((c.rows, c.hidden_size), e.embed_positions.weight.dtype)
        table[: c.positions] = e.embed_positions.weight
        derived.put(e.embed_positions, padded=table)
        self.derived = derived.tree()

    def front(self, features, *, n):
        """The clip's ``n`` positions after the convolutions, with their
        position embeddings.
        """
        c = self.config
        h = GELU.step(self.conv1(features, rows=c.conv_rows))
        Copy.step(h[: c.frames], self.convolved[1 : c.frames + 1])
        h = GELU.step(self.conv2(self.convolved, rows=n))
        table = self.derived.model.encoder.embed_positions.padded
        return ElementwiseAdd.step(h, iron.weight(table)[:n]), None

    def sanitize(self, w):
        return sanitize(w)

    def norm(self, x):
        n = self.whisper_encoder.layer_norm
        return F.layer_norm(x, n.weight, n.bias, self.config.eps)

    def head(self, x):
        return x

    # TODO(whole-clip max reduction): the log-mel features on the device
    # (LogMel with a power spectrum, log10 and the per-clip clamp).
    def body(self, features, *, n: Scratchpad[np.int32]):
        """The encoder's output over a clip's ``features``, ``(conv_rows +
        2, mels)``: a zero row, the frames, zero rows after.
        """
        x, angles = self.front(features, n=n)
        return self.forward(x, n, angles)

    def soft(self, values: dict) -> int:
        return values["n"]

    def shapes(self) -> list[dict]:
        c = self.config
        return [dict(features=((c.conv_rows + 2, c.mels), bfloat16))]

    def longest(self) -> dict:
        return dict(n=self.config.positions)

    def inputs(self, features) -> tuple[np.ndarray, dict]:
        """A call's buffer for ``features``, ``(mels, frames)`` as the
        feature extractor gives them, and its ``n``.

        Raises:
            ValueError: ``features`` is not ``(mels, frames)``.
        """
        c = self.config
        features = np.asarray(features)
        if features.shape != (c.mels, c.frames):
            raise ValueError(
                f"WhisperEncoder: features {features.shape} are not "
                f"{(c.mels, c.frames)}"
            )
        buffer = np.zeros((c.conv_rows + 2, c.mels), bfloat16)
        buffer[1 : c.frames + 1] = features.T
        return buffer, dict(n=c.positions)


class Whisper(EncoderDecoder):
    """Whisper on ``config``'s shape and a checkpoint's ``weights``: its
    encoder a ``WhisperEncoder``, its decoder under ``model.decoder``, the
    head tied to the embedding.
    """

    def __init__(self, config: WhisperConfig, weights):
        weights = bf16(weights)
        encoder = WhisperEncoder(config.encoder(), weights)
        super().__init__(config, weights, encoder, weights.model.decoder)

    def positions(self, x, step):
        c = self.config
        table = iron.weight(self.decoder.embed_positions.weight)
        if step.prompt:
            C = c.prefill_chunk
            rows = Copy.step(table[step.start : step.start + C][: step.rows])
        else:
            rows = Copy.step(table[step.position]).reshape(1, c.hidden_size)
        return ElementwiseAdd.step(x, rows)

    def sanitize(self, w):
        return sanitize(w)

    def head(self, x):
        n = self.decoder.layer_norm
        h = F.layer_norm(x, n.weight, n.bias, self.config.eps)
        return GEMV.step(self.decoder.embed_tokens.weight, h)


class Runner(lm.Runner):
    """Whisper, from its checkpoint and ``tokenizer.json``."""

    config = WhisperConfig
    model = Whisper
    #: ``<|startoftranscript|>``, every transcript's first token.
    bos = 50258

    def reference(self):
        """With drawn weights, the model's own graph on the host; else
        Hugging Face's logits (``Reference``), recorded beside the
        checkpoint (``golden.npz``).
        """
        if self.seed is not None:
            return super().reference()
        directory = Path(self.checkpoint.path).parent
        load = lambda: HuggingFaceWhisper.load(directory)  # noqa: E731
        return Reference(Golden(directory / "golden.npz", load))


class Reference:
    """What Whisper is judged by: ``golden``'s logits after a clip and the
    decoder's tokens, keyed on both. ``encode`` the clip's features,
    ``(mels, frames)``, then ``logits``, as ``Whisper`` takes them.
    """

    def __init__(self, golden: Golden):
        self.golden = golden

    def encode(self, features) -> None:
        self.features = np.asarray(features, np.float32).view(np.int32).reshape(-1)

    def logits(self, tokens) -> np.ndarray:
        return self.golden.logits(np.append(self.features, tokens))


class HuggingFaceWhisper:
    """transformers' ``WhisperForConditionalGeneration`` in float32, what
    records a ``Reference``'s golden: the logits after a key of a clip's
    features (their float32 bits), then the decoder's tokens.
    """

    def __init__(self, model):
        self.model = model.eval()

    @classmethod
    def load(cls, directory) -> "HuggingFaceWhisper":
        import torch
        import transformers

        return cls(
            transformers.WhisperForConditionalGeneration.from_pretrained(
                directory, dtype=torch.float32
            )
        )

    @classmethod
    def build(cls, config: WhisperConfig, weights) -> "HuggingFaceWhisper":
        """The model on ``config``'s shape over ``weights``."""
        import torch
        import transformers

        # A toy vocabulary holds no Whisper padding token.
        hf = transformers.WhisperConfig(**config_json(config), pad_token_id=None)
        model = transformers.WhisperForConditionalGeneration(hf)
        state = {k: torch.from_numpy(v) for k, v in flat(weights)}
        model.load_state_dict(state, strict=False)
        return cls(model)

    def logits(self, key) -> np.ndarray:
        import torch

        c = self.model.config
        n = c.num_mel_bins * 2 * c.max_source_positions
        features = np.asarray(key[:n], np.int32).view(np.float32)
        with torch.no_grad():
            out = self.model(
                input_features=torch.from_numpy(features).reshape(
                    1, c.num_mel_bins, -1
                ),
                decoder_input_ids=torch.tensor([list(key[n:])]),
                use_cache=False,
            )
        return out.logits[0, -1].numpy()
