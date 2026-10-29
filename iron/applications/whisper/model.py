# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper over ``iron.lm``: a bidirectional audio encoder (``WhisperEncoder``,
an ``iron.lm.Tower``) feeding a causal text decoder through cross attention
(``Whisper``, an ``iron.lm.EncoderDecoder``), judged by Hugging Face's own
model in float32 (``hugging_face.py``). Both are ``iron.lm``'s layer modules,
loaded from Whisper's renamed once at load (``RENAMES``); nothing rotates:
the encoder adds a fixed position table after its two convolutions, the
decoder a learned one after its embedding. The shape is read from the
checkpoint's ``config.json``.

The encoder takes a clip's samples and computes the feature extractor's
log-mel features from them (``iron.lm.LogMel``, Whisper's), a zero row
before them as its convolutions' padding.
"""

import argparse
import dataclasses
import functools
import json
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron import Precision, Scratchpad
from iron.lm import (
    MLP,
    Attention,
    CrossAttention,
    Config,
    Conv1d,
    CrossDecoderLayer,
    Decoder,
    DecoderConfig,
    Embedding,
    EncoderDecoder,
    EncoderLayer,
    LayerNorm,
    Linear,
    LogMel,
    Tower,
    activation,
    not_json,
    subtree,
)
from iron.lm.checkpoint import leaves, nest
from iron.lm.cli import parse_args
from iron.operators.copy import Copy

from .audio import load_wav

# The rows a GEMM's M and MHA's sequence come in whole blocks of.
BLOCK = 64


def bf16(weights):
    """``weights``, a checkpoint's tree, each float array (float16, as
    large-v3-turbo ships, or float32, as small ships) rounded once to bf16,
    the device's copy (the reference widens the checkpoint's own dtype
    itself); any other array as it is.
    """
    return nest(
        {
            name: w.astype(bfloat16) if np.issubdtype(w.dtype, np.floating) else w
            for name, w in leaves(weights)
        }
    )


#: Whisper's paths under the names ``iron.lm``'s modules read.
RENAMES = {
    "model.layer_norm": "model.norm",
    "self_attn_layer_norm": "input_layernorm",
    "self_attn.out_proj": "self_attn.o_proj",
    "encoder_attn.out_proj": "encoder_attn.o_proj",
    "final_layer_norm": "post_attention_layernorm",
    "fc1": "mlp.fc1",
    "fc2": "mlp.fc2",
}


@dataclasses.dataclass(frozen=True)
class WhisperEncoderConfig(Config):
    """The audio encoder's shape, built by ``WhisperConfig.encoder`` from
    the checkpoint's ``encoder_*`` keys; never read from or written to a
    ``config.json`` by itself.
    """

    # Every projection biased (``Attention``, ``MLP``).
    attention_bias = mlp_bias = True

    hidden_size: int
    num_hidden_layers: int
    num_attention_heads: int
    intermediate_size: int
    num_mel_bins: int
    positions: int
    hidden_act: str
    eps: float = dataclasses.field(default=1e-5, kw_only=True)
    # Every Whisper's feature extractor: samples per second, per hop and per frame.
    sample_rate: int = dataclasses.field(default=16000, kw_only=True)
    hop: int = dataclasses.field(default=160, kw_only=True)
    n_fft: int = dataclasses.field(default=400, kw_only=True)
    precision: Precision = not_json(Precision.MEDIUM, kw_only=True)

    @property
    def num_key_value_heads(self) -> int:
        return self.num_attention_heads

    @property
    def head_dim(self) -> int:
        return self.hidden_size // self.num_attention_heads

    @property
    def text_dim(self) -> int:
        """The width of the encoder's output, the decoder's."""
        return self.hidden_size

    @property
    def frames(self) -> int:
        """The log-mel frames of a clip, two a position."""
        return 2 * self.positions

    @property
    def samples(self) -> int:
        """The samples of a clip, a hop a frame: 30 s at large-v3-turbo's."""
        return self.frames * self.hop

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

    @property
    def conv1_channels(self) -> int:
        """``num_mel_bins`` rounded up to 64, the first convolution's GEMM's
        K (3 taps a channel) a whole tile of 64 at any mel count Whisper
        ships (80 or 128): the extra channels are zero-weighted, never read.
        """
        return -(-self.num_mel_bins // 64) * 64


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
    hidden_act: str = dataclasses.field(
        default="gelu", metadata={"json": "activation_function"}
    )
    eps: float = not_json(1e-5, kw_only=True)
    # Every feed-forward projection biased (``MLP``).
    mlp_bias: bool = not_json(True, kw_only=True)
    precision: Precision = not_json(Precision.MEDIUM, kw_only=True)
    encoder_layers: int = dataclasses.field(kw_only=True)
    encoder_attention_heads: int = dataclasses.field(kw_only=True)
    encoder_ffn_dim: int = dataclasses.field(kw_only=True)
    num_mel_bins: int = dataclasses.field(kw_only=True)
    max_source_positions: int = dataclasses.field(kw_only=True)
    # <|startoftranscript|>, every Whisper checkpoint's.
    decoder_start_token_id: int = dataclasses.field(default=50258, kw_only=True)
    # Decoding-time token ids a real checkpoint's generation_config.json
    # holds beside config.json (from_checkpoint merges the two); empty or
    # past vocab_size with no checkpoint (a toy's), so Whisper's draw()
    # suppresses nothing.
    suppress_tokens: tuple[int, ...] = dataclasses.field(
        default=(),
        kw_only=True,
        metadata={"json": "/suppress_tokens", "convert": tuple},
    )
    begin_suppress_tokens: tuple[int, ...] = dataclasses.field(
        default=(),
        kw_only=True,
        metadata={"json": "/begin_suppress_tokens", "convert": tuple},
    )
    # The first token of the task/language/timestamp block, from
    # task_to_id's smallest value: every text token and <|endoftext|> come
    # before it.
    first_special_token_id: int = dataclasses.field(
        default=1 << 30,
        kw_only=True,
        metadata={"json": "/task_to_id", "convert": lambda d: min(d.values())},
    )

    @classmethod
    def from_checkpoint(cls, path) -> "WhisperConfig":
        """``Config.from_checkpoint``, its ``config.json`` over the same
        directory's ``generation_config.json`` where one ships (every real
        Whisper checkpoint's): ``suppress_tokens`` and the rest above.
        """
        path = Path(path)
        if path.name != "config.json":
            path = (path if path.is_dir() else path.parent) / "config.json"
        generation = path.parent / "generation_config.json"
        data = json.loads(generation.read_text()) if generation.exists() else {}
        data |= json.loads(path.read_text())
        return cls.from_json(data, path)

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
            precision=self.precision,
        )


class WhisperAttention(Attention):
    """``Attention`` with q, v and o biased and k not, as Whisper's."""

    def projections(self, c) -> None:
        E, D = c.hidden_size, self.head_dim
        self.q_proj = Linear(E, self.heads * D, precision=c.precision)
        self.k_proj = Linear(E, self.groups * D, bias=False, precision=c.precision)
        self.v_proj = Linear(E, self.groups * D, precision=c.precision)


class WhisperCrossAttention(CrossAttention, WhisperAttention):
    """``CrossAttention`` biased as ``WhisperAttention``."""


class WhisperEncoderLayer(EncoderLayer):
    """``EncoderLayer`` on a ``WhisperAttention``."""

    def __init__(self, c: WhisperEncoderConfig, i: int):
        super().__init__(c, i, WhisperAttention(c, i, o_bias=True))


class WhisperDecoderLayer(CrossDecoderLayer):
    """``CrossDecoderLayer`` with each block after a ``LayerNorm``, a plain
    ``MLP`` biased, and ``WhisperAttention``s.
    """

    norm = LayerNorm

    def __init__(self, c: WhisperConfig, i: int):
        super().__init__(
            c,
            i,
            WhisperAttention(c, i, o_bias=True),
            MLP(c),
            WhisperCrossAttention(c, i, o_bias=True),
        )


class WhisperDecoder(Decoder):
    """``Decoder`` with a learned position table, ``embed_positions``, and
    a ``LayerNorm`` its final norm.
    """

    def __init__(self, c: WhisperConfig, layer):
        super().__init__(c, layer)
        self.embed_positions = Embedding(c.max_seq_len, c.hidden_size)
        self.norm = LayerNorm(c.hidden_size)


def decoder_weights(weights):
    """The decoder's modules of a Whisper checkpoint's tree, as ``model``."""
    return subtree(weights, model=weights.model.decoder)


class WhisperEncoder(Tower):
    """Whisper's audio encoder over one clip: its log-mel features, as the
    feature extractor computes them (``LogMel``), then two convolutions,
    each then a GELU, the second at stride 2, the position table added, then
    each layer and the final LayerNorm. Its rows are ``config.rows``,
    bounded per call to ``rows``, the clip's positions.

    Args:
        config: The encoder's shape.
        weights: The checkpoint's tree, bf16 (``bf16``); ``model.encoder`` is
            read.
    """

    layer_class = WhisperEncoderLayer
    renames = RENAMES

    def __init__(self, config: WhisperEncoderConfig, weights):
        c, e = config, weights.model.encoder
        super().__init__(c, c.rows, c.rows)
        self.final_norm = LayerNorm(c.hidden_size)
        self.load_layers(weights, "model.encoder.layers.", "model.encoder.layer_norm.")
        self.log_mel = LogMel(
            c.n_fft,
            c.hop,
            c.n_fft,
            c.num_mel_bins,
            c.sample_rate,
            mel_floor=1e-10,
            mel_scale="slaney",
            norm="slaney",
            power=2,
            decades=8.0,
        )
        # The first convolution's input: a zero row, the features, zero rows.
        self.features = iron.state((c.conv_rows + 2, c.num_mel_bins))
        # At 80 mels (every Whisper but large), conv1's channels are padded
        # to conv1_channels so its GEMM's K (3 taps a channel) is a whole
        # tile; the pad columns are never read, since conv1's padded weight
        # rows are zero. Log10Clamp needs a contiguous destination, so
        # features is copied in rather than written there directly.
        if c.conv1_channels == c.num_mel_bins:
            self.conv1_input, conv1_weight = None, e.conv1.weight
        else:
            self.conv1_input = iron.state((c.conv_rows + 2, c.conv1_channels))
            conv1_weight = np.pad(
                np.asarray(e.conv1.weight),
                ((0, 0), (0, c.conv1_channels - c.num_mel_bins), (0, 0)),
            )
        self.conv1 = Conv1d(conv1_weight, e.conv1.bias, c.conv1_channels)
        self.conv2 = Conv1d(e.conv2.weight, e.conv2.bias, c.hidden_size, stride=2)
        # The convolutions' GELU is the layers' hidden_act.
        self.act = activation(c.hidden_act)
        # The second convolution's input: a zero row, then the first's output.
        self.convolved = iron.state((2 * c.rows + 1, c.hidden_size))
        # The position table padded to the rows.
        self.embed_positions = iron.param(
            np.zeros((c.rows, c.hidden_size), e.embed_positions.weight.dtype)
        )
        self.embed_positions[: c.positions] = e.embed_positions.weight

    @property
    def wave_samples(self) -> int:
        """The samples a call takes: those of the clip's frames in whole
        128-row blocks, ``LogMel``'s GEMMs'.
        """
        c = self.config
        return (-(-c.frames // 128) * 128 - 1) * c.hop + self.log_mel.span

    def front(self, wave, *, rows):
        """The clip's ``rows`` positions after the convolutions, with their
        position embeddings.
        """
        c = self.config
        self.log_mel(wave, self.features[1 : c.frames + 1], frames=c.frames)
        if self.conv1_input is None:
            conv1_in = self.features
        else:
            Copy.step(self.features, self.conv1_input[:, : c.num_mel_bins])
            conv1_in = self.conv1_input
        h = self.act(self.conv1(conv1_in, rows=c.conv_rows))
        self.convolved[1 : c.frames + 1] = h[: c.frames]
        h = self.act(self.conv2(self.convolved, rows=rows))
        table = iron.weight(self.embed_positions)
        return h + table[:rows], None

    def head(self, x):
        return x

    def body(self, wave, *, rows: Scratchpad[np.int32]):
        """The encoder's output over a clip's ``wave``, ``inputs``'."""
        x, angles = self.front(wave, rows=rows)
        return self.forward(x, rows, angles)

    def shapes(self) -> list[dict]:
        return [dict(wave=((self.wave_samples,), np.float32))]

    def longest(self) -> dict:
        return dict(rows=self.config.positions)

    def inputs(self, audio) -> tuple[np.ndarray, dict]:
        """A call's buffer for ``audio``, float32 samples at ``sample_rate``,
        and its ``rows``: as the feature extractor takes them, padded with
        zeros or cut to the clip's samples, then mirrored ``n_fft // 2``
        samples at each end (``torch.stft``'s centring), zero past.

        Raises:
            ValueError: ``audio`` is not one channel of samples.
        """
        c = self.config
        audio = np.asarray(audio, np.float32)
        if audio.ndim != 1:
            raise ValueError(
                f"WhisperEncoder: audio {audio.shape} is not one channel of samples"
            )
        clip = np.zeros(c.samples, np.float32)
        clip[: min(audio.size, c.samples)] = audio[: c.samples]
        padded = np.pad(clip, c.n_fft // 2, mode="reflect")[: self.wave_samples]
        buffer = np.zeros(self.wave_samples, np.float32)
        buffer[: padded.size] = padded
        return buffer, dict(rows=c.positions)


class Whisper(EncoderDecoder):
    """Whisper on ``config``'s shape and a checkpoint's ``weights``: its
    encoder a ``WhisperEncoder``, its decoder under ``model.decoder``, the
    head tied to the embedding. From its checkpoint and ``tokenizer.json``,
    a prompt starts at ``<|startoftranscript|>``.
    """

    config = WhisperConfig
    decoder_class = WhisperDecoder
    layer_class = WhisperDecoderLayer
    renames = RENAMES
    profile = Path(__file__).with_name("profiles")

    def __init__(self, config: WhisperConfig, weights):
        weights = bf16(weights)
        encoder = WhisperEncoder(config.encoder(), weights)
        super().__init__(config, decoder_weights(weights), encoder)
        # Added to the head's logits before Sample draws: -inf at every
        # token generation_config.json holds unspeakable (empty, and so a
        # no-op, with no checkpoint: a toy's). begin_suppress_bias is the
        # prompt chunk's own, which draws the first generated token;
        # suppress_bias every call after.
        v = config.vocab_size + config.vocab_size % 2
        bias = np.zeros(v, bfloat16)
        bias[list(config.suppress_tokens)] = -np.inf
        bias[config.first_special_token_id :] = -np.inf
        self.suppress_bias = iron.param(bias)
        begin_bias = bias.copy()
        begin_bias[list(config.begin_suppress_tokens)] = -np.inf
        self.begin_suppress_bias = iron.param(begin_bias)

    @functools.cached_property
    def bos(self) -> int:
        """``<|startoftranscript|>``, the decoder's first token."""
        return self.config.decoder_start_token_id

    @property
    def hugging_face(self):
        """transformers' Whisper, imported only where a golden is recorded."""
        from .hugging_face import HuggingFaceWhisper

        return HuggingFaceWhisper

    def special(self, token: str) -> int:
        """The id of ``token`` (``<|transcribe|>``, a language), by the
        checkpoint's own tokenizer.

        Raises:
            RuntimeError: Drawn weights loaded no tokenizer.
            KeyError: The checkpoint's tokenizer has no such token.
        """
        if self.tokenizer is None:
            raise RuntimeError(f"{type(self).__name__}: no tokenizer; drawn weights")
        id = self.tokenizer.token_to_id(token)
        if id is None:
            raise KeyError(f"{type(self).__name__}: no token {token!r}")
        return id

    def prompt_tokens(
        self, language: str = "en", task: str = "transcribe"
    ) -> list[int]:
        """``<|startoftranscript|> <|language|> <|task|> <|notimestamps|>``:
        one 30 s window decoded without timestamps. ``transcribe_long``'s
        windows leave ``<|notimestamps|>`` off instead.
        """
        return [
            self.bos,
            self.special(f"<|{language}|>"),
            self.special(f"<|{task}|>"),
            self.special("<|notimestamps|>"),
        ]

    def sampled(self, logits, call):
        """``logits`` plus this call's suppression bias: ``begin_suppress_bias``
        for the prompt chunk, which draws the first generated token,
        ``suppress_bias`` after. ``logits`` itself, the call's own return
        value, is never suppressed.
        """
        bias = self.begin_suppress_bias if call.prompt else self.suppress_bias
        return logits + iron.weight(bias)

    def positions(self, x, call):
        c = self.config
        table = iron.weight(self.model.embed_positions.weight)
        if call.prompt:
            C = c.prefill_chunk
            rows = Copy.step(table[call.start : call.start + C][: call.rows])
        else:
            rows = Copy.step(table[call.position]).reshape(1, c.hidden_size)
        return x + rows

    def transcribe(
        self,
        audio,
        *,
        language: str = "en",
        task: str = "transcribe",
        max_tokens: int = 224,
    ) -> tuple[list[int], str]:
        """One window's transcript of ``audio``, 16 kHz mono float32 samples
        no longer than the checkpoint's own clip (30 s at large-v3-turbo's):
        its generated token ids, greedy, and their decoded text.

        Raises:
            ValueError: ``audio`` is longer than one window: long-form audio
                needs timestamp-aware decoding, ``transcribe_long`` (not yet
                built).
        """
        c = self.config.encoder()
        if audio.size > c.samples:
            raise ValueError(
                f"{audio.size / c.sample_rate:.1f} s is longer than one "
                f"{c.samples / c.sample_rate:.0f} s window; long-form audio "
                "needs timestamp-aware decoding (transcribe_long), not yet built"
            )
        self.encode(audio)
        prompt = self.prompt_tokens(language=language, task=task)
        generated = self.generate(prompt, max_tokens=max_tokens)
        # Every text token is below the first special token after it
        # (<|endoftext|>, the lowest of self.eos); suppressed on the device,
        # a stray one would still decode to nothing a listener reads as text.
        boundary = min(self.eos)
        text = self.tokenizer.decode([t for t in generated if t < boundary]).strip()
        return generated, text


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe 16 kHz mono PCM16 audio with Whisper on the NPU."
    )
    parser.add_argument(
        "path",
        help="a directory holding config.json, the checkpoint and the "
        "tokenizer, or a Hugging Face repository's id",
    )
    parser.add_argument(
        "--wav", required=True, type=Path, help="the audio to transcribe"
    )
    parser.add_argument("--language", default="en", help="the audio's language code")
    parser.add_argument(
        "--task", default="transcribe", choices=["transcribe", "translate"]
    )
    parser.add_argument(
        "--max-tokens", type=int, default=224, help="generated tokens per window"
    )
    args = parse_args(parser)

    model = Whisper.load(args.path)
    audio = load_wav(args.wav)
    generated, text = model.transcribe(
        audio, language=args.language, task=args.task, max_tokens=args.max_tokens
    )
    print(f"Token IDs: {generated}")
    print(f"Text: {text}")
    stats = model.stats
    assert stats is not None, "set once the last token is drawn"
    print(f"Time to first token: {stats.ttft:.3f} s")
    print(f"Tokens per second:   {stats.tokens_per_s:.3f}")


if __name__ == "__main__":
    main()
