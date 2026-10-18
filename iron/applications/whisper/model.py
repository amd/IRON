#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper over ``iron.lm``: a bidirectional audio encoder (``WhisperEncoder``,
an ``iron.lm.Tower``) feeding a causal text decoder through cross attention
(``Whisper``, an ``iron.lm.EncoderDecoder``), judged by Hugging Face's own
model in float32 (``hugging_face.py``). Both are ``iron.lm``'s layer parts over
Whisper's modules renamed once at load (``RENAMES``); nothing rotates:
the encoder adds a fixed position table after its two convolutions, the
decoder a learned one after its embedding. The shape is read from the
checkpoint's ``config.json``.

The encoder takes the feature extractor's log-mel features (``input_features``),
a zero row before them, as its convolutions' padding.
"""

import dataclasses

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.lm import (
    MLP,
    Attention,
    Config,
    Conv1d,
    CrossDecoderLayer,
    DecoderConfig,
    DecoderLayer,
    EncoderDecoder,
    Norm,
    Tower,
    not_json,
)
from iron.lm.checkpoint import _nest, leaves
from iron.operators.copy import Copy

# The rows a GEMM's M and MHA's sequence come in whole blocks of.
BLOCK = 64


def bf16(weights):
    """``weights``, a checkpoint's tree, each float16 array rounded once to
    bf16, the device's copy of an fp16 checkpoint (the reference widens the
    float16 itself); any other array as it is.
    """
    return _nest(
        {
            name: w.astype(bfloat16) if w.dtype == np.float16 else w
            for name, w in leaves(weights)
        }
    )


#: A Whisper layer's paths under the names ``iron.lm``'s parts read.
RENAMES = {
    "self_attn_layer_norm": "input_layernorm",
    "self_attn.out_proj": "self_attn.o_proj",
    "encoder_attn.out_proj": "encoder_attn.o_proj",
    "final_layer_norm": "post_attention_layernorm",
    "fc1": "mlp.fc1",
    "fc2": "mlp.fc2",
}


@dataclasses.dataclass(frozen=True)
class WhisperEncoderConfig(Config):
    """The audio encoder's shape (``WhisperConfig.encoder``)."""

    hidden_size: int
    num_hidden_layers: int
    num_attention_heads: int
    intermediate_size: int
    num_mel_bins: int
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

    def norm(self) -> Norm:
        return Norm(self.eps, bias=True)

    def layer(self, i: int) -> DecoderLayer:
        H = self.num_attention_heads
        return DecoderLayer(
            Attention(H, H, self.hidden_size // H),
            MLP(self.hidden_act, gated=False),
            self.norm(),
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
    rope_theta: float | None = not_json(None, kw_only=True)
    max_seq_len: int = dataclasses.field(metadata={"json": "max_target_positions"})
    prefill_chunk: int = not_json(256)
    # Whisper's own "gelu" is exact, which MLP refuses: no operator computes
    # it. A checkpoint at "gelu_pytorch_tanh" runs.
    hidden_act: str = dataclasses.field(
        default="gelu", metadata={"json": "activation_function"}
    )
    eps: float = not_json(1e-5, kw_only=True)
    encoder_layers: int = dataclasses.field(kw_only=True)
    encoder_attention_heads: int = dataclasses.field(kw_only=True)
    encoder_ffn_dim: int = dataclasses.field(kw_only=True)
    num_mel_bins: int = dataclasses.field(kw_only=True)
    max_source_positions: int = dataclasses.field(kw_only=True)

    def norm(self) -> Norm:
        return Norm(self.eps, bias=True)

    def layer(self, i: int) -> CrossDecoderLayer:
        H = self.num_attention_heads
        return CrossDecoderLayer(
            Attention(H, H, self.head_dim),
            MLP(self.hidden_act, gated=False),
            self.norm(),
        )

    def encoder(self) -> WhisperEncoderConfig:
        """The encoder's shape."""
        return WhisperEncoderConfig(
            self.hidden_size,
            self.encoder_layers,
            self.encoder_attention_heads,
            self.encoder_ffn_dim,
            self.num_mel_bins,
            self.max_source_positions,
            self.hidden_act,
            eps=self.eps,
        )


class WhisperEncoder(Tower):
    """Whisper's audio encoder over one clip's log-mel features: two
    convolutions, each then a GELU, the second at stride 2, the position
    table added, then each layer and the final LayerNorm. Its rows are
    ``config.rows``, bounded per call to ``rows``, the clip's positions.

    Args:
        config: The encoder's shape.
        weights: The checkpoint's tree, bf16 (``bf16``); ``model.encoder`` is
            read.
    """

    def __init__(self, config: WhisperEncoderConfig, weights):
        c, e = config, weights.model.encoder
        super().__init__(c, e.layers, c.rows, c.rows)
        self.final_norm = e.layer_norm
        self.conv1 = Conv1d(e.conv1.weight, e.conv1.bias, c.num_mel_bins)
        self.conv2 = Conv1d(e.conv2.weight, e.conv2.bias, c.hidden_size, stride=2)
        # The convolutions' GELU is the layers' hidden_act.
        self.act = MLP(c.hidden_act).act
        # The second convolution's input: a zero row, then the first's output.
        self.convolved = iron.state((2 * c.rows + 1, c.hidden_size))
        # The position table padded to the rows.
        self.embed_positions = np.zeros(
            (c.rows, c.hidden_size), e.embed_positions.weight.dtype
        )
        self.embed_positions[: c.positions] = e.embed_positions.weight

    def front(self, features, *, rows):
        """The clip's ``rows`` positions after the convolutions, with their
        position embeddings.
        """
        c = self.config
        h = self.act(self.conv1(features, rows=c.conv_rows))
        self.convolved[1 : c.frames + 1] = h[: c.frames]
        h = self.act(self.conv2(self.convolved, rows=rows))
        table = iron.weight(self.embed_positions)
        return h + table[:rows], None

    renames = RENAMES

    def head(self, x):
        return x

    def body(self, features, *, rows: Scratchpad[np.int32]):
        """The encoder's output over a clip's ``features``, ``(conv_rows +
        2, num_mel_bins)``: a zero row, the frames, zero rows after.
        """
        x, angles = self.front(features, rows=rows)
        return self.forward(x, rows, angles)

    def shapes(self) -> list[dict]:
        c = self.config
        return [dict(features=((c.conv_rows + 2, c.num_mel_bins), bfloat16))]

    def longest(self) -> dict:
        return dict(rows=self.config.positions)

    def inputs(self, features) -> tuple[np.ndarray, dict]:
        """A call's buffer for ``features``, ``(num_mel_bins, frames)`` as the
        feature extractor gives them, and its ``rows``.

        Raises:
            ValueError: ``features`` is not ``(num_mel_bins, frames)``.
        """
        c = self.config
        features = np.asarray(features)
        if features.shape != (c.num_mel_bins, c.frames):
            raise ValueError(
                f"WhisperEncoder: features {features.shape} are not "
                f"{(c.num_mel_bins, c.frames)}"
            )
        buffer = np.zeros((c.conv_rows + 2, c.num_mel_bins), bfloat16)
        buffer[1 : c.frames + 1] = features.T
        return buffer, dict(rows=c.positions)


class Whisper(EncoderDecoder):
    """Whisper on ``config``'s shape and a checkpoint's ``weights``: its
    encoder a ``WhisperEncoder``, its decoder under ``model.decoder``, the
    head tied to the embedding.
    """

    def __init__(self, config: WhisperConfig, weights):
        weights = bf16(weights)
        encoder = WhisperEncoder(config.encoder(), weights)
        super().__init__(config, weights, encoder, weights.model.decoder)
        self.final_norm = self.decoder.layer_norm

    def positions(self, x, step):
        c = self.config
        table = iron.weight(self.decoder.embed_positions.weight)
        if step.prompt:
            C = c.prefill_chunk
            rows = Copy.step(table[step.start : step.start + C][: step.rows])
        else:
            rows = Copy.step(table[step.position]).reshape(1, c.hidden_size)
        return x + rows

    renames = RENAMES
