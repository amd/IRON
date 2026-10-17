#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper over ``iron.lm``: a bidirectional audio encoder (``WhisperEncoder``,
an ``iron.lm.Tower``) feeding a causal text decoder through cross attention
(``Whisper``, an ``iron.lm.EncoderDecoder``), and their float32 twins
(``WhisperOracle``). Both are ``Layer``s on Whisper's names; nothing rotates:
the encoder adds a fixed position table after its two convolutions, the
decoder a learned one after its embedding. The shape is read from the
checkpoint's ``config.json``.

The encoder takes the feature extractor's log-mel features (``input_features``),
a zero row before them, as its convolutions' padding.
"""

import dataclasses
from types import SimpleNamespace

import numpy as np
from ml_dtypes import bfloat16
from tokenizers import Tokenizer as HFTokenizer

import iron
from iron import Scratchpad, lm
from iron.lm import (
    Config,
    Conv1d,
    DecoderConfig,
    Derived,
    EncoderDecoder,
    EncoderDecoderOracle,
    Layer,
    Oracle,
    Tower,
    widen,
)
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gelu import GELU
from iron.operators.gemv import GEMV

# The rows a GEMM's M and MHA's sequence come in whole blocks of.
BLOCK = 64


def bf16(weights):
    """``weights``, an array or a tree of namespaces and lists, each float16
    array rounded once to bf16, the device's copy of an fp16 checkpoint (the
    oracle widens the float16 itself); any other array as it is.
    """
    if isinstance(weights, np.ndarray):
        return weights.astype(bfloat16) if weights.dtype == np.float16 else weights
    if isinstance(weights, list):
        return [bf16(w) for w in weights]
    if isinstance(weights, SimpleNamespace):
        return SimpleNamespace(**{k: bf16(w) for k, w in vars(weights).items()})
    return weights


@dataclasses.dataclass(frozen=True)
class WhisperEncoderConfig(Config):
    """The audio encoder's shape (``WhisperConfig.encoder``)."""

    emb_dim: int
    n_layers: int
    n_heads: int
    hidden_dim: int
    mels: int
    positions: int
    hidden_act: str
    eps: float = dataclasses.field(default=1e-5, kw_only=True)

    @property
    def text_dim(self) -> int:
        """The width of the encoder's output, the decoder's."""
        return self.emb_dim

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

    def layer(self, i: int) -> Layer:
        H = self.n_heads
        return Layer(H, H, self.emb_dim // H, self.eps, self.hidden_act)


@dataclasses.dataclass(frozen=True)
class WhisperConfig(DecoderConfig):
    """Whisper's decoder's shape from its ``config.json``, and its encoder's
    (``encoder()``).
    """

    emb_dim: int = dataclasses.field(metadata={"json": "d_model"})
    n_layers: int = dataclasses.field(metadata={"json": "decoder_layers"})
    n_heads: int = dataclasses.field(metadata={"json": "decoder_attention_heads"})
    n_kv_groups: int = dataclasses.field(metadata={"json": "decoder_attention_heads"})
    hidden_dim: int = dataclasses.field(metadata={"json": "decoder_ffn_dim"})
    rope_base: float | None = dataclasses.field(default=None, kw_only=True)
    max_seq_len: int = dataclasses.field(metadata={"json": "max_target_positions"})
    prefill_chunk: int = 256
    # Whisper's own "gelu" is exact, which Layer refuses until the pin group
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

    def encoder(self) -> WhisperEncoderConfig:
        """The encoder's shape."""
        return WhisperEncoderConfig(
            self.emb_dim,
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
    table added, then each ``Layer`` and the final LayerNorm. Its rows are
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
        self.conv2 = Conv1d(e.conv2.weight, e.conv2.bias, c.emb_dim, stride=2)
        # The second convolution's input: a zero row, then the first's output.
        self.convolved = iron.state((2 * c.rows + 1, c.emb_dim))
        derived = Derived(weights)
        table = np.zeros((c.rows, c.emb_dim), e.embed_positions.weight.dtype)
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

    def norm(self, x):
        return self.config.layer(0).norm(x, self.whisper_encoder.layer_norm)

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


class WhisperEncoderOracle(Oracle):
    """``WhisperEncoder``'s float32 twin.

    Args:
        config: The encoder's shape.
        weights: The checkpoint's tree, as ``WhisperEncoder`` takes it.
    """

    def __init__(self, config: WhisperEncoderConfig, weights):
        super().__init__(config)
        self.whisper_encoder = widen(weights.model.encoder)

    def soft_tokens(self, features) -> np.ndarray:
        """The encoder's ``(positions, emb_dim)`` output over ``features``,
        ``(mels, frames)``.
        """
        c, e = self.config, self.whisper_encoder
        x = np.pad(np.asarray(features, np.float32).T, ((1, 1), (0, 0)))
        conv1 = Conv1d(e.conv1.weight, e.conv1.bias, c.mels)
        conv2 = Conv1d(e.conv2.weight, e.conv2.bias, c.emb_dim, stride=2)
        h = self.gelu_tanh(conv1.oracle(x, e.conv1.weight, e.conv1.bias))
        h = np.pad(h, ((1, 1), (0, 0)))
        h = self.gelu_tanh(conv2.oracle(h, e.conv2.weight, e.conv2.bias))
        x = h + e.embed_positions.weight
        for i, w in enumerate(e.layers):
            x = c.layer(i).oracle(self, w, x, self.attend, None)
        return self.normed(x, e.layer_norm)


class WhisperOracle(EncoderDecoderOracle):
    """Whisper's float32 forward pass on the host: ``encode`` the encoder's
    output, then ``logits``.
    """

    def __init__(self, config: WhisperConfig, weights):
        super().__init__(config, weights, weights.model.decoder)
        self.encoder = WhisperEncoderOracle(config.encoder(), weights)

    def positions(self, x):
        return x + widen(self.decoder.embed_positions.weight[: x.shape[0]])

    def head(self, x):
        return self.normed(x, widen(self.decoder.layer_norm)) @ self.embedding.T


class Whisper(EncoderDecoder):
    """Whisper on ``config``'s shape and a checkpoint's ``weights``: its
    encoder a ``WhisperEncoder``, its decoder under ``model.decoder``, the
    head tied to the embedding.
    """

    oracle = WhisperOracle

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
            rows = Copy.step(table[step.position]).reshape(1, c.emb_dim)
        return ElementwiseAdd.step(x, rows)

    def head(self, x):
        h = self.config.layer(0).norm(x, self.decoder.layer_norm)
        return GEMV.step(self.decoder.embed_tokens.weight, h)


def tokenizer(path) -> HFTokenizer:
    """Whisper's tokenizer, from its ``tokenizer.json``."""
    return HFTokenizer.from_file(str(path))


class Runner(lm.Runner):
    """Whisper, from its checkpoint and ``tokenizer.json``."""

    config = WhisperConfig
    model = Whisper
    open_tokenizer = staticmethod(tokenizer)
    #: ``<|startoftranscript|>``, every transcript's first token.
    bos = 50258
