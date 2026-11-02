#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper speech-to-text on the NPU (``iron.lm``).

``WhisperEncoder`` (convolutional stem and 12 bidirectional ``EncoderLayer``
blocks) and ``WhisperDecoder`` (causal self-attention ``KVCache``,
cross-attention ``MHA`` over the encoder's keys and values, and ``MLP``)
compiled as versions of one ``Whisper`` graph sharing a single arena.
"""

from __future__ import annotations

import argparse
import dataclasses
import re
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron.kernels import sample
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Carried, Precision, Scratchpad, lm
from iron.common.graph import CompiledGraph, Handle
from iron.lm import (
    MLP,
    Attention,
    Call,
    CausalLM,
    DecoderConfig,
    DecoderLayer,
    Embedding,
    Encoder,
    EncoderLayer,
    KVCache,
    LayerNorm,
    Linear,
    Model,
    NoCache,
    residual_add,
    subtree,
)
from iron.lm.blocks import LogMel
from iron.lm.checkpoint import renamed
from iron.lm.cli import parse_args
from iron.operators.copy import Copy
from iron.operators.gelu import GELU
from iron.operators.mha import MHA
from iron.operators.sample import Sample

from .audio import (
    FRAMES,
    HOP_LENGTH,
    N_FFT,
    N_SAMPLES,
    SAMPLE_RATE,
    load_wav,
    mel_filters,
)

PROFILES = Path(__file__).with_name("profiles")

# <|startoftranscript|> <|en|> <|transcribe|> <|notimestamps|>
PROMPT = (50258, 50259, 50359, 50363)
TIMESTAMP_PROMPT = PROMPT[:3]
EOS = 50257
FIRST_NON_TEXT_SPECIAL = 50358
# <|0.00|>; each following token adds 0.02 s (two 10 ms Mel frames).
TIMESTAMP_BEGIN = 50364
TIMESTAMP_SECONDS = 0.02
HOP_SECONDS = HOP_LENGTH / SAMPLE_RATE
INPUT_STRIDE = 2
MAX_INITIAL_TIMESTAMP = 50
TIMESTAMP_TOLERANCE = 5
MAX_NEW_TOKENS = 224
MAX_RANGES = 8
RENAMES = {
    "self_attn_layer_norm": "input_layernorm",
    "out_proj": "o_proj",
    "final_layer_norm": "post_attention_layernorm",
    "fc1": "mlp.fc1",
    "fc2": "mlp.fc2",
}


@dataclasses.dataclass(frozen=True)
class WhisperConfig(DecoderConfig):
    """Whisper's encoder and decoder shape from ``config.json``."""

    precision: Precision = lm.not_json(Precision.HIGHEST, kw_only=True)
    eps: float = lm.not_json(1e-5, kw_only=True)
    rope_theta: float | None = lm.not_json(None)
    prefill_chunk: int = lm.not_json(64)
    attention_bias: bool = lm.not_json(True, kw_only=True)
    mlp_bias: bool = lm.not_json(True, kw_only=True)

    hidden_size: int = dataclasses.field(default=768, metadata={"json": "d_model"})
    num_hidden_layers: int = dataclasses.field(
        default=12, metadata={"json": "decoder_layers"}
    )
    num_attention_heads: int = dataclasses.field(
        default=12, metadata={"json": "decoder_attention_heads"}
    )
    num_key_value_heads: int = dataclasses.field(
        default=12, metadata={"json": "decoder_attention_heads"}
    )
    intermediate_size: int = dataclasses.field(
        default=3072, metadata={"json": "decoder_ffn_dim"}
    )
    max_seq_len: int = dataclasses.field(
        default=448, metadata={"json": "max_target_positions"}
    )
    max_target_positions: int = 448
    hidden_act: str = dataclasses.field(
        default="gelu", metadata={"json": "activation_function"}
    )
    vocab_size: int = 51865
    encoder_layers: int = 12
    encoder_attention_heads: int = 12
    encoder_ffn_dim: int = 3072
    num_mel_bins: int = 80
    max_source_positions: int = 1500
    bos_token_id: int = 50257
    eos_token_id: int = 50257
    pad_token_id: int = 50257
    decoder_start_token_id: int = 50258
    suppress_tokens: tuple[int, ...] = dataclasses.field(
        default=(), metadata={"convert": tuple}
    )
    begin_suppress_tokens: tuple[int, ...] = dataclasses.field(
        default=(220, 50257), metadata={"convert": tuple}
    )

    @property
    def frames(self) -> int:
        """Return the valid Mel frames of one window."""
        return 2 * self.max_source_positions

    @property
    def source_pad(self) -> int:
        """Return ``max_source_positions`` padded to whole 64-row MHA blocks."""
        return -(-self.max_source_positions // 64) * 64

    @property
    def frames_pad(self) -> int:
        """Return the padded Mel frame count ``2 * source_pad``."""
        return 2 * self.source_pad

    @property
    def conv1_k(self) -> int:
        """Return ``3 * num_mel_bins`` padded to whole 64-element GEMM K tiles."""
        return -(-(3 * self.num_mel_bins) // 64) * 64

    @property
    def vocab_pad(self) -> int:
        """Return ``vocab_size`` padded to a multiple of 256 for 8-lane GEMV."""
        return -(-self.vocab_size // 256) * 256

    @property
    def encoder_config(self) -> WhisperConfig:
        """Return a copy with the encoder's layer, head and MLP counts."""
        return dataclasses.replace(
            self,
            num_hidden_layers=self.encoder_layers,
            num_attention_heads=self.encoder_attention_heads,
            num_key_value_heads=self.encoder_attention_heads,
            intermediate_size=self.encoder_ffn_dim,
        )


class TokenPolicy:
    """Whisper greedy-decoding logit filters and ``ApplyTimestampRules``.

    Without timestamps, all non-text special tokens are suppressed. With
    timestamps, timestamps come in pairs and never decrease, the initial
    timestamp is at most 1.0 s, and a timestamp is selected whenever the
    summed timestamp probability exceeds the top text token's.
    """

    def __init__(
        self,
        config: WhisperConfig,
        *,
        timestamps: bool = False,
        max_new_tokens: int = MAX_NEW_TOKENS,
    ):
        self.suppress = list(config.suppress_tokens)
        self.begin_suppress = list(config.begin_suppress_tokens)
        self.eos = config.eos_token_id
        self.timestamps = timestamps
        self.max_new_tokens = max_new_tokens

        self.vocab = config.vocab_size

    def ranges(self, generated: list[int]) -> list[tuple[int, int]]:
        """Return history-only suppression intervals in global vocabulary coordinates."""
        ranges = []
        if not generated and self.begin_suppress:
            ranges.extend((t, t + 1) for t in self.begin_suppress)
        if not self.timestamps:
            return [*ranges, (FIRST_NON_TEXT_SPECIAL, self.vocab)]

        ranges.append((FIRST_NON_TEXT_SPECIAL, TIMESTAMP_BEGIN))
        last = len(generated) >= 1 and generated[-1] >= TIMESTAMP_BEGIN
        penultimate = len(generated) < 2 or generated[-2] >= TIMESTAMP_BEGIN
        if last:
            if penultimate:
                ranges.append((TIMESTAMP_BEGIN, self.vocab))
            else:
                ranges.append((0, self.eos))

        stamps = [t for t in generated if t >= TIMESTAMP_BEGIN]
        if stamps:
            floor = stamps[-1] if last and not penultimate else stamps[-1] + 1
            ranges.append((TIMESTAMP_BEGIN, floor))
        if not generated:
            ranges.extend(
                [
                    (0, TIMESTAMP_BEGIN),
                    (TIMESTAMP_BEGIN + MAX_INITIAL_TIMESTAMP + 1, self.vocab),
                ]
            )
        return ranges

    def row(self, generated: list[int]) -> np.ndarray:
        """Pack one greedy draw, its ranges and the forced-timestamp split."""
        return np.concatenate(
            [
                sample.draw_row(0.0, 1, 0),
                sample.range_words(self.ranges(generated), MAX_RANGES),
                sample.split_word(TIMESTAMP_BEGIN if self.timestamps else self.vocab),
            ]
        ).reshape(1, -1)


class WhisperNoCache(NoCache):
    """Bidirectional encoder attention over ``seq_len`` valid rows of a padded buffer."""

    def __init__(self, seq_len: int):
        super().__init__(causal=False)
        self.seq_len = seq_len

    def attend(self, call, q, k, v, scale: float | None = None):
        """Attend ``q`` over ``k`` and ``v`` with ``seq_len`` valid positions."""
        n, H, D = q.shape
        o = MHA.step(
            q,
            k,
            v,
            seq_len=self.seq_len,
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
            scale=scale,
        )
        return o.reshape(n, H * D)


class WhisperAttention(Attention):
    """Whisper's attention: ``q_proj``, ``v_proj`` and ``o_proj`` biased, ``k_proj`` unbiased."""

    def __init__(self, c: WhisperConfig, i: int):
        super().__init__(c, i, o_bias=c.attention_bias)

    def projections(self, c) -> None:
        """Declare ``q_proj`` and ``v_proj`` with bias and ``k_proj`` without bias."""
        E, D = c.hidden_size, self.head_dim
        self.q_proj = Linear(
            E, self.heads * D, bias=c.attention_bias, precision=c.precision
        )
        self.k_proj = Linear(E, self.groups * D, bias=False, precision=c.precision)
        self.v_proj = Linear(
            E, self.groups * D, bias=c.attention_bias, precision=c.precision
        )


class WhisperCrossAttention(WhisperAttention):
    """Decoder cross-attention over the encoder's projected keys and values."""

    def __init__(self, c: WhisperConfig, i: int):
        super().__init__(c, i)
        self.keys = iron.state((c.source_pad, self.groups, self.head_dim))
        self.values = iron.state((c.source_pad, self.groups, self.head_dim))
        self.source_positions = c.max_source_positions

    def write_kv(self, hidden: Handle) -> None:
        """Project ``hidden`` into this layer's ``keys`` and ``values`` states."""
        S, G, D = self.keys.shape
        k = self.k_proj(hidden)
        v = self.v_proj(hidden)
        Copy.step(k.reshape(S, G, D), self.keys)
        Copy.step(v.reshape(S, G, D), self.values)

    def body(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, x: Handle
    ) -> Handle:
        """Attend ``x``'s queries over the encoder's fixed source positions."""
        n, H, D = x.shape[0], self.heads, self.head_dim
        tiles = dict(tile_size_output=D // 2) if n == 1 else {}
        q = F.linear(
            x,
            self.q_proj.weight,
            self.q_proj.bias,
            precision=self.q_proj.precision,
            **tiles,
        )
        # Keep whole DMA blocks in storage; 1500 rows alone do not tile.
        o = MHA.step(
            q.reshape(n, H, D),
            self.keys,
            self.values,
            kv_seq_len=self.source_positions,
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
            scale=self.scaling,
        )
        return self.output(o.reshape(n, H * D), x)


class WhisperEncoderLayer(EncoderLayer):
    """Layer ``i`` of Whisper's encoder."""

    def __init__(self, c: WhisperConfig, i: int):
        super().__init__(c, i, WhisperAttention(c, i))
        self.cache = WhisperNoCache(c.max_source_positions)


class WhisperEncoder(Encoder):
    """Whisper's audio encoder on the NPU: 2-layer Conv1d stem and ``EncoderLayer`` stack."""

    profile = PROFILES
    layer_class = WhisperEncoderLayer
    renames = RENAMES

    def __init__(self, config: WhisperConfig, weights: SimpleNamespace):
        c = config.encoder_config
        E, M, S = c.hidden_size, c.num_mel_bins, c.max_source_positions
        self.encoder = SimpleNamespace()
        super().__init__(c, c.source_pad)
        self.final_norm = LayerNorm(E, c.eps)
        self.encoder = SimpleNamespace(
            conv1=SimpleNamespace(weight=iron.param(E, M, 3), bias=iron.param(E)),
            conv2=SimpleNamespace(weight=iron.param(E, E, 3), bias=iron.param(E)),
            embed_positions=SimpleNamespace(weight=iron.param(S, E)),
            layers=self.layers,
            layer_norm=self.final_norm,
        )
        self.load_state_dict(
            renamed(subtree(weights, encoder=weights.model.encoder), self.renames)
        )
        w1 = np.zeros((E, c.conv1_k), bfloat16)
        w1[:, : 3 * M] = self.encoder.conv1.weight.transpose(0, 2, 1).reshape(E, 3 * M)
        self.w1 = iron.param(w1)
        w2 = self.encoder.conv2.weight.transpose(0, 2, 1).reshape(E, 3 * E)
        self.w2 = iron.param(np.ascontiguousarray(w2))
        pos = np.zeros((c.source_pad, E), bfloat16)
        pos[:S] = self.encoder.embed_positions.weight
        self.pos = iron.param(pos)
        self.conv1_out = iron.state((c.frames_pad + 2, E))
        self.zero_row = iron.param(np.zeros((1, E), bfloat16))

    def head(self, x):
        """Return the final-normed encoder rows unchanged."""
        return x

    def body(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, features: Handle
    ) -> Handle:
        """Run the Conv1d stem, position embeddings, encoder layers and final LayerNorm."""
        c = self.config
        F_pad, S_pad, M, E = c.frames_pad, c.source_pad, c.num_mel_bins, c.hidden_size
        win1 = TensorAccessPattern(
            features.shape, 0, [F_pad // 4, 4, c.conv1_k], [4 * M, M, 1]
        )
        a1 = Copy.step(features, src=win1).reshape(F_pad, c.conv1_k)
        h1 = F.linear(a1, self.w1, self.encoder.conv1.bias, precision=c.precision)
        GELU.step(h1, self.conv1_out[1 : F_pad + 1], approximate="none")
        self.conv1_out[c.frames + 1] = self.zero_row
        win2 = TensorAccessPattern(
            self.conv1_out.shape, 0, [S_pad // 4, 4, 3 * E], [8 * E, 2 * E, 1]
        )
        a2 = Copy.step(self.conv1_out, src=win2).reshape(S_pad, 3 * E)
        h2 = F.linear(a2, self.w2, self.encoder.conv2.bias, precision=c.precision)
        x = F.gelu(h2, approximate="none") + self.pos
        return self.forward(x, c.max_source_positions, None)

    def shapes(self) -> list[dict]:
        """Return the input shape of the encoder version."""
        c = self.config
        return [dict(features=((c.frames_pad + 4, c.num_mel_bins), bfloat16))]

    def inputs(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, mel: np.ndarray
    ) -> np.ndarray:
        """Pack ``mel`` ``(frames, num_mel_bins)`` into the padded input buffer."""
        c = self.config
        mel = np.asarray(mel)
        if mel.ndim != 2 or mel.shape[1] != c.num_mel_bins or mel.shape[0] > c.frames:
            raise ValueError(
                f"Expected mel shape (<= {c.frames}, {c.num_mel_bins}), got {mel.shape}"
            )
        buf = np.zeros((c.frames_pad + 4, c.num_mel_bins), bfloat16)
        buf[1 : 1 + mel.shape[0]] = mel.astype(bfloat16)
        return buf


class WhisperDecoderLayer(DecoderLayer):
    """Layer ``i`` of Whisper's decoder: self-attention, cross-attention and MLP."""

    norm = LayerNorm

    def __init__(self, c: WhisperConfig, i: int):
        super().__init__(c, i, WhisperAttention(c, i), MLP(c), KVCache(c, c.window))
        self.encoder_attn_layer_norm = LayerNorm(c.hidden_size, c.eps)
        self.encoder_attn = WhisperCrossAttention(c, i)

    def body(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, x: Handle, call
    ) -> Handle:
        """Run self-attention, cross-attention over the encoder and MLP."""
        x = residual_add(
            x, self.mix(self.input_layernorm(x), call), self.residual_multiplier
        )
        h = self.encoder_attn(self.encoder_attn_layer_norm(x))
        x = residual_add(x, h, self.residual_multiplier)
        h = self.mlp(self.post_attention_layernorm(x))
        return residual_add(x, h, self.residual_multiplier)


class WhisperDecoderModule(iron.Graph):
    """Whisper's ``model.decoder`` module tree."""

    def __init__(self, c: WhisperConfig, layer: type[WhisperDecoderLayer]):
        self.embed_tokens = Embedding(c.vocab_size, c.hidden_size)
        self.embed_positions = SimpleNamespace(
            weight=iron.param(c.max_target_positions, c.hidden_size)
        )
        self.layers = [layer(c, i) for i in range(c.num_hidden_layers)]
        self.norm = LayerNorm(c.hidden_size, c.eps)


class WhisperDecoder(CausalLM):
    """Whisper's decoder on ``CausalLM``."""

    config = WhisperConfig
    profile = PROFILES
    decoder_class = WhisperDecoderModule  # pyright: ignore[reportAssignmentType]
    layer_class = WhisperDecoderLayer
    model: WhisperDecoderModule
    renames = {**RENAMES, "layer_norm": "norm"}

    def __init__(self, config: WhisperConfig, weights: SimpleNamespace):
        super().__init__(config, subtree(weights, model=weights.model.decoder))
        c = config
        head = np.asarray(self.model.embed_tokens.weight)
        self.lm_head.weight = iron.param(
            np.pad(head, ((0, c.vocab_pad - c.vocab_size), (0, 0)))
        )
        pos = np.zeros((c.max_seq_len + c.prefill_chunk, c.hidden_size), bfloat16)
        pos[: c.max_seq_len] = self.model.embed_positions.weight[: c.max_seq_len]
        self.pos_table = iron.weight(pos)
        self.rules = iron.state(
            (1, sample.select_row_words(MAX_RANGES, True)), np.int32
        )
        self.selected = iron.state((1,), np.int32)
        bias = np.zeros(c.vocab_pad, bfloat16)
        bias[list(c.suppress_tokens)] = -np.inf
        bias[c.vocab_size :] = -np.inf
        self.suppress_bias = iron.param(bias)

    def draw(self, logits, call: Call):
        """Draw the next token from ``vocab_pad``-padded ``logits`` over ``vocab_size`` drawable tokens."""
        c = self.config
        _, drawn = Sample.step(
            logits.reshape(c.vocab_pad) + self.suppress_bias,
            self.rules,
            self.selected,
            drawable=c.vocab_size,
            max_ranges=MAX_RANGES,
            probability_rule=True,
        )
        return logits, iron.carry(token=drawn, position=call.position + 1)

    def positions(self, x, call: Call):
        """Add ``embed_positions`` for the prompt chunk's slice or the decode step's position."""
        C, E = self.config.prefill_chunk, self.config.hidden_size
        if call.prompt:
            pos = Copy.step(self.pos_table[call.start : call.start + C][: call.rows])
        else:
            pos = Copy.step(self.pos_table[call.position]).reshape(1, E)
        return x + pos


class Whisper(Model):
    """Whisper encoder-decoder speech-to-text model on the NPU.

    Compiles three versions sharing one arena:
    - ``decode_step`` (no input): single-token decoder step with ``KVCache`` and ``Sample``.
    - ``prompt_chunk`` (``ids``): decoder prompt prefill chunk.
    - ``encode`` (``features``): audio encoder + all decoder layers' cross-attention
      ``K`` and ``V`` projections into shared ``iron.state`` buffers.
    """

    config = WhisperConfig
    profile = PROFILES
    decoder_class = WhisperDecoder

    def __init__(self, config: WhisperConfig, weights: SimpleNamespace):
        self.config = config
        self.weights = weights
        self.encoder = WhisperEncoder(config, weights)
        self.decoder = self.decoder_class(config, weights)
        self.encode_version: CompiledGraph | None = None
        self._last_mel: np.ndarray | None = None
        self._frontends: dict[int, CompiledGraph] = {}

    @property
    def hugging_face(self):
        """Return ``HuggingFaceWhisper`` for golden recording and reference checks."""
        from .hugging_face import HuggingFaceWhisper

        return HuggingFaceWhisper

    @classmethod
    def fit(cls, config, weights_path, budget: int | None = None):
        """Return ``config`` at its fixed ``max_target_positions`` context."""
        return config

    def body(
        self,
        ids: Handle | None = None,
        features: Handle | None = None,
        *,
        token: Carried[np.int32],
        position: Carried[np.int32],
        start: Scratchpad[np.int32] = np.int32(0),
        rows: Scratchpad[np.int32] = np.int32(1),
        rope_start: Scratchpad[np.int32] = np.int32(0),
    ):
        """Record the encoder version when ``features`` is given, else the decoder."""
        if features is not None:
            hidden = self.encoder(features)
            for layer in self.decoder.layers:
                layer.encoder_attn.write_kv(hidden)
            carried: dict[str, Any] = {"token": token, "position": position}
            return hidden, iron.carry(**carried)
        return self.decoder.inline(
            self.decoder.body,
            ids,
            token=token,
            position=position,
            start=start,
            rows=rows,
            rope_start=rope_start,
        )

    def shapes(self) -> list[dict]:
        """Return the shapes of the decode step, prompt chunk and audio encoder."""
        return [*self.decoder.shapes(), *self.encoder.shapes()]

    def loaded(self, versions: list) -> None:
        """Bind the compiled decode step, prompt chunk and encoder versions."""
        decode_step, prompt_chunk, encode_version = versions
        self.decoder.use(decode_step, prompt_chunk)
        self.encode_version = encode_version
        self._last_mel = None

    def release(self) -> None:
        """Free the decoder's loops and all versions' device memory."""
        self.decoder.release()
        for frontend in self._frontends.values():
            frontend.release()
        self._frontends.clear()
        super().release()

    def encode(self, mel: np.ndarray) -> np.ndarray:
        """Run the audio encoder on ``mel`` ``(frames, num_mel_bins)`` and populate cross-attention K/V.

        Returns:
            ``(max_source_positions, hidden_size)`` float32 encoder hidden states.
        """
        c = self.config
        buf = self.encoder.inputs(mel)
        defaults = dict(
            token=0,
            position=0,
            start=0,
            rows=1,
            rope_start=0,
        )
        if self.encode_version is not None:
            out, _ = self.encode_version(buf, **defaults)
        else:
            out, _ = self(None, buf, **defaults)
        self._last_mel = np.array(mel, copy=True)
        self.decoder.forget(0)
        arr = np.asarray(out.numpy()).reshape(c.source_pad, c.hidden_size)
        return arr[: c.max_source_positions].astype(np.float32)

    def logits(self, tokens, mel: np.ndarray | None = None) -> np.ndarray:
        """Return the decoder logits after ``tokens``, encoding ``mel`` first when new."""
        if mel is not None and (
            self._last_mel is None or not np.array_equal(mel, self._last_mel)
        ):
            self.encode(mel)
        return self.decoder.logits(tokens)

    def window(
        self,
        mel: np.ndarray,
        prompt: list[int] | tuple[int, ...] = PROMPT,
        policy: TokenPolicy | None = None,
    ) -> tuple[list[int], np.ndarray]:
        """Encode one 30 s ``mel`` window and greedy-decode tokens under ``policy``."""
        if policy is None:
            policy = TokenPolicy(self.config, timestamps=False)
        if not (0 < len(prompt) <= self.config.prefill_chunk) or not (
            0 < policy.max_new_tokens <= self.config.max_seq_len - len(prompt) + 1
        ):
            raise ValueError(
                "Whisper: prompt and requested tokens do not fit the decoder"
            )
        if self.decoder.decode_step is None:
            raise RuntimeError("Whisper.window: load_versions() first")
        encoder_out = self.encode(mel)
        generated: list[int] = []
        while True:
            self.decoder.decode_step.write(self.decoder.rules, policy.row(generated))
            if not generated:
                _, carry = self.decoder(
                    self.decoder.session.prompt_ids(prompt),
                    token=0,
                    position=len(prompt) - 1,
                    start=0,
                    rows=len(prompt),
                )
            else:
                _, carry = self.decoder(
                    token=generated[-1],
                    position=len(prompt) + len(generated) - 1,
                )
            token = int(carry["token"])
            generated.append(token)
            if token == policy.eos or len(generated) >= policy.max_new_tokens:
                return generated, encoder_out

    def filters(self) -> np.ndarray:
        """Return the checkpoint's Mel filterbank, or the Slaney filterbank."""
        directory = (
            None if self.checkpoint is None else Path(self.checkpoint.path).parent
        )
        return mel_filters(
            directory, mels=self.config.num_mel_bins, sample_rate=SAMPLE_RATE
        )

    def log_mel(
        self, waveform: np.ndarray, *, long_form: bool = False
    ) -> tuple[np.ndarray, int]:
        """Extract and globally normalize log-Mel on the NPU; pad/reflect samples on the host."""
        samples = np.asarray(waveform, np.float32).reshape(-1)
        content = samples.size // HOP_LENGTH
        if long_form:
            samples = np.pad(samples, (0, N_SAMPLES))
        else:
            samples = np.pad(samples[:N_SAMPLES], (0, max(0, N_SAMPLES - samples.size)))
        frames = samples.size // HOP_LENGTH
        capacity = -(-frames // 64) * 64
        graph = LogMel(
            frame=N_FFT,
            fft=N_FFT,
            mels=self.config.num_mel_bins,
            mel_floor=1e-10,
            mel_scale="slaney",
            whisper=True,
        )
        length = (capacity - 1) * HOP_LENGTH + graph.span
        padded = np.pad(samples, (N_FFT // 2, N_FFT // 2), mode="reflect")
        wave = np.zeros(length, np.float32)
        wave[: min(length, padded.size)] = padded[:length]
        if capacity not in self._frontends:
            self._frontends[capacity] = graph.compile(wave=((length,), np.float32))
        # A reduction tile is eight padded Mel rows. Long-form's trailing
        # silence makes rounding to that tile harmless; a 30 s window is exact.
        out = self._frontends[capacity](wave, frames=-(-frames // 8) * 8)
        mel = out.numpy().reshape(capacity, self.config.num_mel_bins)
        return np.array(mel[:frames], np.float32), content

    def transcribe(
        self,
        waveform: np.ndarray,
        *,
        long_form: bool = False,
    ) -> dict[str, Any]:
        """Transcribe 16 kHz mono ``waveform`` on the NPU (single window or long-form)."""
        samples = np.asarray(waveform, dtype=np.float32).reshape(-1)
        duration = samples.size / SAMPLE_RATE
        use_long = long_form or duration > 30.0
        mel, content_frames = self.log_mel(samples, long_form=use_long)
        if not use_long:
            policy = TokenPolicy(self.config, timestamps=False)
            tokens, encoder_out = self.window(mel, list(PROMPT), policy)
            result = dict(encoder_out=encoder_out, segments=[])
        else:
            policy = TokenPolicy(self.config, timestamps=True)
            windows = transcribe_long(self, mel, content_frames, policy)
            tokens = [t for w in windows for t in w["tokens"]]
            result = dict(
                content_frames=content_frames,
                windows=windows,
                segments=(
                    segments_of(windows, self.tokenizer)
                    if self.tokenizer is not None
                    else []
                ),
            )
        text_ids = [t for t in tokens if t < EOS]
        text = (
            self.tokenizer.decode(text_ids).strip()
            if self.tokenizer is not None
            else ""
        )
        return {
            "text": text,
            "tokens": tokens,
            "long_form": use_long,
            "mel": mel,
            **result,
        }


def decode_window(
    backend,
    mel: np.ndarray,
    seek: int,
    content_frames: int,
    policy: TokenPolicy,
    frames: int = FRAMES,
) -> tuple[int, list[int]]:
    """Return the seek advance and completed tokens from one padded Mel window.

    When the next window rewinds to the last completed timestamp pair,
    discard unfinished speech that it will decode again.
    """
    size = min(frames, content_frames - seek)
    segment = np.zeros((frames, mel.shape[1]), dtype=np.float32)
    segment[:size] = mel[seek : seek + size]
    tokens, _ = backend.window(segment, list(TIMESTAMP_PROMPT), policy)
    text_end = [t for t in tokens if t != policy.eos]
    is_stamp = [t >= TIMESTAMP_BEGIN for t in text_end]
    pairs = [i + 1 for i in range(len(is_stamp) - 1) if is_stamp[i] and is_stamp[i + 1]]
    if pairs and is_stamp[-2:] != [False, True]:
        advance = (text_end[pairs[-1] - 1] - TIMESTAMP_BEGIN) * INPUT_STRIDE
        if advance > 0:
            return advance, text_end[: pairs[-1]]
    return size, tokens


def transcribe_long(
    backend,
    mel: np.ndarray,
    content_frames: int,
    policy: TokenPolicy,
    frames: int = FRAMES,
) -> list[dict[str, Any]]:
    """Run OpenAI Whisper's sequential long-form timestamp decoding over ``mel``."""
    seek = 0
    windows: list[dict[str, Any]] = []
    while seek < content_frames:
        size, tokens = decode_window(
            backend, mel, seek, content_frames, policy, frames=frames
        )
        windows.append({"seek": seek, "tokens": tokens})
        seek += size
    return windows


def windows_match(
    actual: list[int],
    expected: list[int],
    tokenizer=None,
    tolerance: int = TIMESTAMP_TOLERANCE,
) -> tuple[bool, int | None]:
    """Check whether ``actual`` and ``expected`` have matching words and timestamps within ``tolerance``."""
    actual_stamps = [t - TIMESTAMP_BEGIN for t in actual if t >= TIMESTAMP_BEGIN]
    expected_stamps = [t - TIMESTAMP_BEGIN for t in expected if t >= TIMESTAMP_BEGIN]
    if len(actual_stamps) != len(expected_stamps):
        return False, None
    worst = max((abs(a - e) for a, e in zip(actual_stamps, expected_stamps)), default=0)
    actual_text = [t for t in actual if t < EOS]
    expected_text = [t for t in expected if t < EOS]
    if tokenizer is not None:
        words_ok = normalize_words(tokenizer.decode(actual_text)) == normalize_words(
            tokenizer.decode(expected_text)
        )
    else:
        words_ok = actual_text == expected_text
    if not words_ok:
        return False, None
    return worst <= tolerance, worst


def segments_of(
    windows: list[dict[str, Any]], tokenizer
) -> list[tuple[float, float | None, str]]:
    """Return ``(start_s, end_s, text)`` for each timestamp-delimited segment."""
    result: list[tuple[float, float | None, str]] = []
    for window in windows:
        offset = window["seek"] * HOP_SECONDS
        start: float | None = None
        text: list[int] = []
        for token in window["tokens"]:
            if token >= TIMESTAMP_BEGIN:
                time_s = offset + (token - TIMESTAMP_BEGIN) * TIMESTAMP_SECONDS
                if start is None:
                    start = time_s
                elif text:
                    result.append((start, time_s, tokenizer.decode(text).strip()))
                    start, text = time_s, []
                else:
                    start = time_s
            elif token < EOS:
                text.append(token)
        if text:
            result.append((start or offset, None, tokenizer.decode(text).strip()))
    return result


def normalize_words(text: str) -> list[str]:
    """Normalize transcript text for word-error-rate comparison."""
    text = text.upper()
    for short, long in (("MR.", "MISTER"), ("MRS.", "MISSUS"), ("DR.", "DOCTOR")):
        text = text.replace(short, long)
    return re.sub(r"[^A-Z0-9' ]", " ", text).replace("'", "").split()


def word_error_rate(reference: str, hypothesis: str) -> float:
    """Return the word error rate between ``reference`` and ``hypothesis``."""
    ref, hyp = normalize_words(reference), normalize_words(hypothesis)
    row = list(range(len(hyp) + 1))
    for i, r in enumerate(ref, 1):
        prev, row[0] = row[0], i
        for j, h in enumerate(hyp, 1):
            prev, row[j] = row[j], min(row[j] + 1, row[j - 1] + 1, prev + (r != h))
    return row[-1] / max(len(ref), 1)


def nrmse(actual: np.ndarray, expected: np.ndarray) -> float:
    """Return ``||actual - expected|| / ||expected||`` in float32."""
    a = np.asarray(actual, dtype=np.float32)
    e = np.asarray(expected, dtype=np.float32)
    return float(np.linalg.norm(a - e) / np.linalg.norm(e))


def main(argv=None) -> None:
    """Run Whisper transcription from the command line."""
    parser = argparse.ArgumentParser(
        description="Transcribe 16 kHz mono audio with Whisper on the NPU"
    )
    parser.add_argument(
        "path",
        help="a directory holding config.json, model.safetensors and tokenizer.json, "
        "or a Hugging Face repository id",
    )
    parser.add_argument(
        "--wav",
        type=Path,
        required=True,
        help="16 kHz mono audio file to transcribe",
    )
    parser.add_argument(
        "--long-form",
        action="store_true",
        help="use timestamp-based long-form decoding even for audio up to 30 s",
    )
    parser.add_argument(
        "--reference-text",
        type=Path,
        help="optional transcript file to compute word error rate against",
    )
    parser.add_argument(
        "--check-reference",
        action="store_true",
        help="compare encoder output and decoded tokens against Hugging Face FP32",
    )
    parser.add_argument(
        "--full-elf",
        action=argparse.BooleanOptionalAction,
        help="package each version as one full ELF where supported",
    )
    args = parse_args(parser, argv)
    waveform = load_wav(args.wav)
    duration = waveform.size / SAMPLE_RATE
    model = Whisper.load(args.path, full_elf=args.full_elf)
    try:
        t0 = time.perf_counter()
        result = model.transcribe(waveform, long_form=args.long_form)
        elapsed = time.perf_counter() - t0
        for start_s, end_s, seg_text in result["segments"]:
            end = "   ?  " if end_s is None else f"{end_s:6.2f}"
            print(f"  [{start_s:6.2f} -> {end}] {seg_text}")
        print(f"Text: {result['text']}")
        print(
            f"[Whisper] {duration:.2f} s audio transcribed in {elapsed:.3f} s "
            f"(RTF {elapsed / max(duration, 1e-6):.3f})"
        )
        if args.reference_text is not None:
            truth = args.reference_text.read_text(encoding="utf-8")
            print(f"WER: {100.0 * word_error_rate(truth, result['text']):.1f}%")
        if args.check_reference:
            from .hugging_face import HuggingFaceWhisper

            assert model.checkpoint is not None
            hf = HuggingFaceWhisper.load(Path(model.checkpoint.path).parent)
            if not result["long_form"]:
                policy = TokenPolicy(model.config, timestamps=False)
                ref_tokens, ref_enc = hf.window(result["mel"], list(PROMPT), policy)
                enc_err = nrmse(result["encoder_out"], ref_enc)
                match = result["tokens"] == ref_tokens
                print(f"Encoder NRMSE vs FP32: {100.0 * enc_err:.3f}%")
                print(f"Exact CPU FP32 token match: {match}")
                if not match:
                    raise SystemExit("FAILED: token mismatch with CPU FP32 reference")
            else:
                policy = TokenPolicy(model.config, timestamps=True)
                match = True
                for w in result["windows"]:
                    _, expected = decode_window(
                        hf,
                        result["mel"],
                        w["seek"],
                        result["content_frames"],
                        policy,
                        frames=model.config.frames,
                    )
                    ok, _ = windows_match(
                        w["tokens"], expected, tokenizer=model.tokenizer
                    )
                    match = match and ok
                print(
                    f"CPU FP32 match (words exact, timestamps +-{TIMESTAMP_TOLERANCE}): {match}"
                )
                if not match:
                    raise SystemExit(
                        "FAILED: long-form mismatch with CPU FP32 reference"
                    )
    finally:
        model.release()
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()


if __name__ == "__main__":
    main()
