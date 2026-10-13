#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper-large-v3-turbo, encoder-decoder, on the NPU: a 32-layer
bidirectional audio encoder (log-mel in, 1500 soft positions out) feeding
a 4-layer causal text decoder through cross-attention.

Both towers are a plain pre-norm transformer (``LayerNorm`` with a learned
weight and bias, a GELU feed-forward -- no RMSNorm, no SwiGLU gating, no
RoPE: the encoder's position embedding is a fixed sinusoidal table and the
decoder's a learned one, both added once, not rotated per layer). Every
projection but ``k_proj`` carries a bias (``project(..., bias=)``).

Cross-attention needs no new operator: a decoder layer's own
``encoder_attn.k_proj``/``v_proj`` project the encoder's final hidden state
once per clip (by ``WhisperEncoder``, alongside the hidden state itself),
and every decode step or prompt-chunk call attends over that *static* K/V
with plain ``MHA(causal=False)`` -- the same "bidirectional over a fixed
cache" shape EmbeddingGemma 2's sliding/global layers already exercise. The
static cross K/V crosses from the encoder's compiled graph to the
decoder's own (two separate images, run at different times) through one
host round-trip of already-computed bf16 arrays per audio clip, not per
decode step -- ``WhisperDecoder.encode`` reads the encoder's output back
and ``write()``s it into the decoder's own per-layer state, the same
mechanism ``CausalLM.generate`` already uses to seed its draws.

The feature extraction (log-mel) is Hugging Face's ``WhisperFeatureExtractor``
exactly: a Slaney mel scale (not EmbeddingGemma 2's HTK), a power spectrum
(not a magnitude one), ``log10`` (not natural log), and a per-clip clamp to
``log_spec.max() - 8`` before an affine ``(x + 4) / 4``. The rfft, the power
and the mel filterbank are on the device (``WhisperLogMel``, the same
GEMM-as-DFT mechanism ``iron.lm.LogMel`` uses, with Whisper's own filters and
framing); the per-clip *global* max and the clamp/affine step are not yet --
there is no on-device reduction over a whole tensor in this library today,
only per-row ones (``RMSNorm``, ``Softmax``). ``WhisperEncoder.encode``
therefore reads the device's pre-clamp log-mel back, finds its max and
clamps/affines it on the host (one read-back and one cheap numpy pass per
clip, not per decode step) before re-uploading it to the device for conv1.
This is the one exception to "everything on the NPU" in this port; closing
it needs a new on-device global-reduction operator (a row-max pass, then a
second row-max pass over the row-maxes reshaped into one row), noted in
this port's skill-gaps.md rather than silently worked around.
"""

import dataclasses
import math
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import aie.utils as aie_utils
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron.common import Carried, Scratchpad
from iron.lm import (
    CausalLM,
    Checkpoint,
    Conv1d,
    Layout,
    Step,
    checkpoint_shapes,
    load_weights,
    project,
    random_weights,
)
from iron.lm import Config as DecoderConfig
from aie.iron.kernels.sample import ROW_WORDS
from iron.operators import (
    GELU,
    GEMV,
    MHA,
    Clamp,
    Copy,
    ElementwiseAdd,
    ElementwiseMul,
    LayerNorm,
    Log,
    Magnitude,
    RowwiseAdd,
    Sample,
    RowwiseMul,
)
from iron.operators.gemm import GEMM
from iron.operators.limbs import Limbs, stacked

# Each product's float32 sum rounded once: the rfft and the mel filterbank.
ACCURATE = dict(prio_accuracy=True, emulate_bf16_mmul_with_bfp16=False)


def slaney_mel(num_freq_bins: int, num_mels: int, sample_rate: int) -> np.ndarray:
    """The ``(num_freq_bins, num_mels)`` Slaney mel filterbank Hugging
    Face's ``WhisperFeatureExtractor`` uses, 0 Hz to ``sample_rate // 2``,
    float64 (matches its own ``mel_filters`` to the bit at float32).
    """

    def to_mel(freq):
        low_hz, low_mel, logstep = 1000.0, 15.0, 27.0 / math.log(6.4)
        freq = np.asarray(freq, np.float64)
        linear = 3.0 * freq / 200.0
        return np.where(
            freq >= low_hz,
            low_mel + np.log(np.maximum(freq, 1e-10) / low_hz) * logstep,
            linear,
        )

    def to_hz(mel):
        low_hz, low_mel, logstep = 1000.0, 15.0, math.log(6.4) / 27.0
        linear = 200.0 * mel / 3.0
        return np.where(
            mel >= low_mel, low_hz * np.exp(logstep * (mel - low_mel)), linear
        )

    mel_min, mel_max = to_mel(0.0), to_mel(sample_rate / 2)
    mel_freqs = np.linspace(mel_min, mel_max, num_mels + 2)
    filter_freqs = to_hz(mel_freqs)
    fft_freqs = np.linspace(0, sample_rate / 2, num_freq_bins)
    diff = np.diff(filter_freqs)
    slopes = filter_freqs[None, :] - fft_freqs[:, None]
    down, up = -slopes[:, :-2] / diff[:-1], slopes[:, 2:] / diff[1:]
    filters = np.maximum(0, np.minimum(down, up))
    return filters * (2.0 / (filter_freqs[2:] - filter_freqs[:-2]))[None, :]


@dataclasses.dataclass(frozen=True)
class EncoderConfig:
    d_model: int = 1280
    n_layers: int = 32
    n_heads: int = 20
    ffn_dim: int = 5120
    mels: int = 128
    max_source_positions: int = 1500
    eps: float = 1e-5
    sample_rate: int = 16000
    n_fft: int = 400
    hop: int = 160
    n_samples: int = 480000

    @property
    def head_dim(self) -> int:
        return self.d_model // self.n_heads

    @property
    def frames(self) -> int:
        return self.n_samples // self.hop  # 3000

    @property
    def conv1_rows(self) -> int:
        # conv1: kernel 3, stride 1, padding 1 -> same length; the caller's
        # buffer holds the one zero row of padding either side.
        return self.frames + 2

    @property
    def hidden_rows(self) -> int:
        # max_source_positions (1500) has no factor of 8: GEMM's M needs a
        # multiple of 32 and MHA's own Q buffer a multiple of 64 (its own
        # seq_pad granularity); 64 covers both, so both conv2's own static
        # output and every GEMM/MHA through the encoder stack run at this
        # width instead. Rows 1500:hidden_rows are real, computed values
        # (never left undefined), just unread past MHA's own `valid` bound.
        return -(-self.max_source_positions // 64) * 64

    @property
    def conv2_rows(self) -> int:
        # conv2: kernel 3, stride 2, padding 1, over conv1's padded output,
        # inverted so its static output is exactly hidden_rows: one zero row
        # of real padding, hidden_rows * 2 - 1 more (conv1's valid 3000 plus
        # harmless tail rows, zeroed for hygiene, past the first 3000).
        return 2 * self.hidden_rows + 1


ENCODER = EncoderConfig()


#: 51866 does not split evenly (into an even slice) over Sample's 4 cores;
#: padded to 51872, the checkpoint's own tokens (never past 51866) and 6
#: dummy rows, zeroed at load (WhisperDecoder.from_checkpoint), never
#: produced as a draw in practice -- not yet proven never, see skill-gaps.md.
VOCAB_SIZE = -(-51866 // 8) * 8

DECODER = DecoderConfig(
    vocab_size=VOCAB_SIZE,
    emb_dim=1280,
    n_layers=4,
    n_heads=20,
    n_kv_groups=20,
    head_dim=64,
    hidden_dim=5120,
    max_seq_len=448,
    rope_base=10000.0,  # unused: this decoder has no RoPE, see WhisperDecoder
    prefill_chunk=448,
)


def encoder_tensors(tensors: dict) -> dict:
    """The encoder's tensors of the full checkpoint."""
    return {k: v for k, v in tensors.items() if k.startswith("model.encoder.")}


def decoder_tensors(tensors: dict) -> dict:
    """The decoder's tensors of the full checkpoint."""
    return {k: v for k, v in tensors.items() if k.startswith("model.decoder.")}


def encoder_layout(config: EncoderConfig) -> Layout:
    E, F = config.d_model, config.ffn_dim
    layer = "model.encoder.layers.{i}"
    out = {
        "conv1.weight": ("model.encoder.conv1.weight", (E, config.mels, 3)),
        "conv1.bias": ("model.encoder.conv1.bias", (E,)),
        "conv2.weight": ("model.encoder.conv2.weight", (E, E, 3)),
        "conv2.bias": ("model.encoder.conv2.bias", (E,)),
        "pos_embedding": (
            "model.encoder.embed_positions.weight",
            (config.max_source_positions, E),
        ),
        "norm.weight": ("model.encoder.layer_norm.weight", (E,)),
        "norm.bias": ("model.encoder.layer_norm.bias", (E,)),
    }
    linear = {
        "attn.q": ("self_attn.q_proj", True),
        "attn.k": ("self_attn.k_proj", False),
        "attn.v": ("self_attn.v_proj", True),
        "attn.out": ("self_attn.out_proj", True),
        "fc1": ("fc1", True),
        "fc2": ("fc2", True),
    }
    for path, (name, bias) in linear.items():
        shape = (F, E) if path == "fc1" else (E, F) if path == "fc2" else (E, E)
        out[f"layers.{{i}}.{path}.weight"] = (f"{layer}.{name}.weight", shape)
        if bias:
            out_dim = shape[0]
            out[f"layers.{{i}}.{path}.bias"] = (f"{layer}.{name}.bias", (out_dim,))
    for norm in ("self_attn_layer_norm", "final_layer_norm"):
        key = "norm1" if norm == "self_attn_layer_norm" else "norm2"
        out[f"layers.{{i}}.{key}.weight"] = (f"{layer}.{norm}.weight", (E,))
        out[f"layers.{{i}}.{key}.bias"] = (f"{layer}.{norm}.bias", (E,))
    return out


def decoder_layout(config: DecoderConfig) -> Layout:
    E, F = config.emb_dim, config.hidden_dim
    layer = "model.decoder.layers.{i}"
    out = {
        "embedding": ("model.decoder.embed_tokens.weight", (config.vocab_size, E)),
        "pos_embedding": (
            "model.decoder.embed_positions.weight",
            (config.max_seq_len, E),
        ),
        "norm.weight": ("model.decoder.layer_norm.weight", (E,)),
        "norm.bias": ("model.decoder.layer_norm.bias", (E,)),
    }
    linear = {
        "self_attn.q": ("self_attn.q_proj", True),
        "self_attn.k": ("self_attn.k_proj", False),
        "self_attn.v": ("self_attn.v_proj", True),
        "self_attn.out": ("self_attn.out_proj", True),
        "cross_attn.q": ("encoder_attn.q_proj", True),
        "cross_attn.k": ("encoder_attn.k_proj", False),
        "cross_attn.v": ("encoder_attn.v_proj", True),
        "cross_attn.out": ("encoder_attn.out_proj", True),
        "fc1": ("fc1", True),
        "fc2": ("fc2", True),
    }
    for path, (name, bias) in linear.items():
        shape = (F, E) if path == "fc1" else (E, F) if path == "fc2" else (E, E)
        out[f"layers.{{i}}.{path}.weight"] = (f"{layer}.{name}.weight", shape)
        if bias:
            out_dim = shape[0]
            out[f"layers.{{i}}.{path}.bias"] = (f"{layer}.{name}.bias", (out_dim,))
    for norm, key in (
        ("self_attn_layer_norm", "norm1"),
        ("encoder_attn_layer_norm", "norm2"),
        ("final_layer_norm", "norm3"),
    ):
        out[f"layers.{{i}}.{key}.weight"] = (f"{layer}.{norm}.weight", (E,))
        out[f"layers.{{i}}.{key}.bias"] = (f"{layer}.{norm}.bias", (E,))
    return out


def affine_norm(x, weight, bias):
    """``LayerNorm`` (gamma 1, beta 0, a hardcoded ``eps=1e-5`` -- Whisper's
    own config carries no ``layer_norm_eps`` of its own, so this is exactly
    its default) times ``weight`` plus ``bias``: the library's norm composed
    with the existing ``RowwiseMul``/``RowwiseAdd``, not a fused chain of
    its own (see ``LIBRARY.md``: this model's norms are not its cost, the
    32-layer encoder's attention is).
    """
    return RowwiseAdd(RowwiseMul(LayerNorm(x), weight), bias)


def feed_forward(x, w, norm_key: str):
    """The GELU feed-forward, its residual included. ``ffn_dim`` (5120)
    exceeds ``RowwiseAdd``'s 4096-element ``tile_cap`` for fc1's bias:
    split into whole pieces here, each its own ``project()``+``GELU``+
    ``project()`` with no fold past the cap, their partial outputs summed.
    The split is of the plain numpy weight arrays, before either ever
    becomes a device operand (`w.fc1`/`w.fc2` are read straight from
    `load_weights`, not yet `iron.weight`-wrapped), so each piece is its
    own ordinary contiguous constant -- no scratch state, no aliasing risk.
    """
    norm = getattr(w, norm_key)
    h = affine_norm(x, norm.weight, norm.bias)
    ffn_dim = w.fc1.bias.shape[0]
    if ffn_dim <= 4096:
        g = GELU(project(h, w.fc1.weight, bias=w.fc1.bias, k_tile=256))
        out = project(g, w.fc2.weight, bias=w.fc2.bias, k_tile=256)
        return ElementwiseAdd(x, out)
    pieces = -(-ffn_dim // 4096)
    piece = next(
        p for p in range(-(-ffn_dim // pieces), ffn_dim + 1) if ffn_dim % p == 0
    )
    out = None
    for start in range(0, ffn_dim, piece):
        end = start + piece
        g = GELU(
            project(h, w.fc1.weight[start:end], bias=w.fc1.bias[start:end], k_tile=256)
        )
        partial = project(g, w.fc2.weight[:, start:end], k_tile=256)
        out = partial if out is None else ElementwiseAdd(out, partial)
    # emb_dim (fc2's own output width) is always <= 4096: one plain fold.
    # A decode step's GEVM path gives a flat vector, not a (rows, emb_dim)
    # 2-D shape; reshape the same way project()'s own bias fold does.
    out_shape = out.shape
    emb_dim = w.fc2.bias.shape[0]
    rows = math.prod(out_shape) // emb_dim
    out = RowwiseAdd(out.reshape(rows, emb_dim), w.fc2.bias).reshape(out_shape)
    return ElementwiseAdd(x, out)


class WhisperLogMel(iron.Graph):
    """Hugging Face's ``WhisperFeatureExtractor`` through ``log10``, on the
    device: the Slaney mel filterbank and a power (not magnitude) spectrum,
    Whisper's own ``n_fft``/``hop``, the rfft as an exact GEMM (``Limbs``,
    the window folded into the DFT matrix, as ``iron.lm.LogMel`` does for
    EmbeddingGemma 2). The one piece left for the caller: the per-clip
    ``log_spec.max()`` clamp and the ``(x + 4) / 4`` affine, which need a
    reduction over the *whole* feature matrix this library has no on-device
    primitive for yet (every reduction here is per-row: ``RMSNorm``,
    ``Softmax``). ``exact()`` is Hugging Face's full formula, clamp and
    affine included, the host oracle this graph's own output (before the
    clamp) is judged against up to that point.

    Args:
        config: ``EncoderConfig``, for ``n_fft``/``hop``/``mels``/``sample_rate``.
    """

    def __init__(self, config: EncoderConfig):
        c = self.config = config
        # Limbs needs a whole 32-element line: pad the gathered frame's width
        # past n_fft (400) with extra, harmless raw samples (the next hop's
        # overlap) and zero the dft matrix's rows past n_fft so they carry
        # no weight -- the product is the exact n_fft-point transform either way.
        self.k_pad = -(-c.n_fft // 32) * 32
        self.window = np.hanning(c.n_fft + 1)[:-1].astype(np.float64)
        bins = c.n_fft // 2 + 1
        width = -(-bins // 64) * 64
        angle = 2 * np.pi * np.arange(c.n_fft)[:, None] * np.arange(bins) / c.n_fft
        dft = np.zeros((self.k_pad, 2 * width))
        dft[: c.n_fft, :bins] = self.window[:, None] * np.cos(angle)
        dft[: c.n_fft, width : width + bins] = -self.window[:, None] * np.sin(angle)
        self.dft = stacked(dft)
        self.filters = slaney_mel(bins, c.mels, c.sample_rate)
        # Plain bf16, not Limbs/stacked: power is already a deliberate single
        # bf16 rounding (below), so the filterbank GEMM needs no further
        # float32 preservation past that point.
        self.filterbank = np.pad(self.filters, ((0, width - bins), (0, 0))).astype(
            bfloat16
        )
        # An exact (one-rounding) float32 -> bf16 cast of the magnitude,
        # via Limbs/GEMM like every other step here: magnitude @ I is exact,
        # so the only rounding is dtype_out's, not a second approximate one.
        self.identity = stacked(np.eye(width))

    def body(self, wave):
        """``wave``, ``(frames + n_fft - hop,)`` float32 reflect-padded
        samples (``n_fft // 2`` either side of the real ``n_samples``), to
        ``(frames, mels)`` float32 ``log10`` mel energies, pre-clamp.
        """
        c = self.config
        frames, k_pad = c.frames, self.k_pad
        windows = TensorAccessPattern(wave.shape, 0, [frames, k_pad], [c.hop, 1])
        a = Copy(wave, src=windows, dtype=np.float32).reshape(frames, k_pad)
        exact = dict(dtype_out=np.float32, emulate_bf16_mmul_with_bfp16=False)
        spectrum = GEMM(Limbs(a), self.dft, **exact)
        magnitude = Magnitude(spectrum)
        cast = GEMM(
            Limbs(magnitude),
            self.identity,
            dtype_out=bfloat16,
            **{k: v for k, v in exact.items() if k != "dtype_out"},
        )
        # power = magnitude ** 2, the one bf16 rounding of this cast; the
        # filterbank GEMM is plain bf16 from here, not Limbs/exact. filters
        # is (bins, mels), the same (K, N) row-major layout Conv1d's weight
        # matrix uses, not a checkpoint's (out, in).
        power = ElementwiseMul(cast, cast)
        energy = GEMM(
            power,
            self.filterbank,
            dtype_out=np.float32,
            emulate_bf16_mmul_with_bfp16=False,
        )
        # Natural log, rounded once to bf16 (Log's own contract); the
        # caller scales by 1 / ln(10) for log10, the clamp and the affine.
        return Log(energy, offset=1e-10)

    def exact(self, waveform: np.ndarray) -> np.ndarray:
        """Hugging Face's ``WhisperFeatureExtractor`` formula exactly, in
        float64 rounded once to float32: ``(frames, mels)``, the clamp and
        affine both included (unlike ``body()``, which stops at ``log10``).
        """
        c = self.config
        audio = np.asarray(waveform, np.float64)[: c.n_samples]
        if audio.size < c.n_samples:
            audio = np.pad(audio, (0, c.n_samples - audio.size))
        pad = c.n_fft // 2
        padded = np.pad(audio, (pad, pad), mode="reflect")
        starts = np.arange(c.frames) * c.hop
        frames = padded[starts[:, None] + np.arange(c.n_fft)]
        spectrum = np.fft.rfft(frames * self.window, n=c.n_fft, axis=-1)
        power = np.abs(spectrum) ** 2
        mel = power @ self.filters
        log_spec = np.log10(np.clip(mel, 1e-10, None))
        log_spec = np.maximum(log_spec, log_spec.max() - 8.0)
        return ((log_spec + 4.0) / 4.0).astype(np.float32)

    def pack(self, waveform: np.ndarray) -> np.ndarray:
        """``waveform`` (mono, ``sample_rate``), padded and reflected into
        the ``(frames - 1) * hop + k_pad`` float32 samples ``body()`` reads:
        ``n_fft // 2`` reflected either side of the real, truncated-or-
        zero-padded ``n_samples``, then whatever extra raw samples
        ``k_pad``'s Limbs alignment needs past the last real frame
        (harmless: the dft matrix's rows past ``n_fft`` are zero, see
        ``__init__``).
        """
        c = self.config
        audio = np.asarray(waveform, np.float32)[: c.n_samples]
        if audio.size < c.n_samples:
            audio = np.pad(audio, (0, c.n_samples - audio.size))
        pad = c.n_fft // 2
        padded = np.pad(audio, (pad, pad), mode="reflect")
        length = (c.frames - 1) * c.hop + self.k_pad
        if padded.size < length:
            padded = np.pad(padded, (0, length - padded.size))
        return padded[:length]

    def conv1_input(self, waveform: np.ndarray) -> np.ndarray:
        """``waveform`` through this graph on the device, then the one
        step left off ``body()``: the per-clip ``log_spec.max() - 8``
        clamp and the ``(x + 4) / 4`` affine, on the host (one read-back
        and one cheap numpy pass a clip, not a decode step -- this
        library has no whole-tensor reduction yet, see skill-gaps.md), and
        packed into ``WhisperEncoder``'s own ``conv1`` input shape
        (``conv1_rows``, ``mels``: one zero row of padding either side of
        the ``frames`` valid ones).
        """
        c = self.config
        raw = np.asarray(self(self.pack(waveform)).numpy(), np.float32).reshape(
            c.frames, c.mels
        )
        log10 = raw / math.log(10.0)
        log10 = np.maximum(log10, log10.max() - 8.0)
        affine = (log10 + 4.0) / 4.0
        x = np.zeros((c.conv1_rows, c.mels), bfloat16)
        x[1 : c.frames + 1] = affine.astype(bfloat16)
        return x


def self_attention(w, x, n_heads: int, head_dim: int, valid: int, causal: bool):
    """One tower's bidirectional or causal self-attention over its own,
    freshly projected q/k/v (``k`` with no bias), the output projected
    back. ``valid`` is documentation only for now (see the KNOWN GAP
    below): every one of ``x``'s rows, real or tile padding, is both a
    query and a key.
    """
    H, D = n_heads, head_dim
    # Project every row (flm.GEMM's own M tiling wants the full, already
    # 256-row-aligned width). KNOWN GAP (skill-gaps.md): MHA's kv_len must
    # itself be a whole 64-row block at least seq_pad long, so the
    # hidden_rows - max_source_positions padding rows (36 of 1536, <2.4%)
    # are not yet excluded as keys here, only as queries (their output is
    # simply never read) -- closing this needs either a per-call bound
    # Extent proven to reach MHA's kv_valid from a *literal* (never
    # varying) slice, or giving MHA a real mask, neither attempted yet.
    q = project(x, w.q.weight, bias=w.q.bias, k_tile=256)
    k = project(x, w.k.weight, k_tile=256)
    v = project(x, w.v.weight, bias=w.v.bias, k_tile=256)
    o = MHA(
        q.reshape(q.shape[0], H, D),
        k.reshape(k.shape[0], H, D),
        v.reshape(v.shape[0], H, D),
        causal=causal,
        heads_interleaved=True,
        kv_interleaved=True,
    )
    return project(
        o.reshape(o.shape[0], H * D), w.out.weight, bias=w.out.bias, k_tile=256
    )


def cross_attention(w, q_x, k, v, n_heads: int, head_dim: int, valid: int):
    """A decoder layer's cross-attention: ``q_x`` freshly projected, over a
    *static* ``k``/``v`` (the encoder's output, projected once per clip by
    ``WhisperEncoder`` itself, the full tile-padded width -- this function
    only projects q and the output). Bidirectional (``causal=False``):
    every decoder row, decode step or prompt chunk, attends over the whole
    of the encoder's positions. ``valid`` is documentation only for now
    (the same KNOWN GAP as ``self_attention``'s: the encoder's
    hidden_rows - max_source_positions padding rows are keys here too).
    """
    H, D = n_heads, head_dim
    q = project(q_x, w.q.weight, bias=w.q.bias, k_tile=256)
    o = MHA(
        q.reshape(q.shape[0], H, D),
        k.reshape(k.shape[0], H, D),
        v.reshape(v.shape[0], H, D),
        causal=False,
        heads_interleaved=True,
        kv_interleaved=True,
    )
    return project(
        o.reshape(o.shape[0], H * D), w.out.weight, bias=w.out.bias, k_tile=256
    )


class WhisperEncoder(iron.Graph):
    """The audio encoder, one compile for every 30-second clip: log-mel
    features in (already clamped and affine-transformed by the caller, see
    ``WhisperLogMel``), 1500 soft positions out, plus -- so the decoder's
    cross-attention needs no device step of its own at decode time -- each
    of the decoder's own ``encoder_attn`` k/v projections of those same
    1500 positions, once per clip.

    Args:
        config: ``EncoderConfig``.
        weights: ``load_weights`` over ``encoder_layout(config)``.
        cross_weights: the decoder's own per-layer ``cross_attn.k``/``v``
            (``SimpleNamespace`` of ``weight``/``bias``), projected here so
            the decoder graph never reads the encoder's own weights.
    """

    def __init__(self, config: EncoderConfig, weights, cross_weights):
        self.config = config
        self.weights = weights
        self.cross_weights = cross_weights
        c = config
        self.conv1 = Conv1d(
            weights.conv1.weight, weights.conv1.bias, channels=c.mels, stride=1
        )
        self.conv2 = Conv1d(
            weights.conv2.weight, weights.conv2.bias, channels=c.d_model, stride=2
        )
        pos = np.zeros((c.hidden_rows, c.d_model), bfloat16)
        pos[: c.max_source_positions] = np.asarray(weights.pos_embedding, bfloat16)
        self.pos_embedding = iron.weight(pos)
        # conv1's valid 3000 rows at [1 : frames + 1], its one real padding
        # row at 0; rows past frames + 1 are tiling padding only, zeroed.
        self.conv1_out = iron.state((c.conv2_rows, c.d_model))
        self.conv1_tail_zero = iron.weight(
            np.zeros((c.conv2_rows - c.frames - 1, c.d_model), bfloat16)
        )

    def body(self, x):
        c = self.config
        Copy(self.conv1_tail_zero, self.conv1_out[c.frames + 1 :])
        h = GELU(self.conv1(x, rows=c.frames))
        Copy(h, self.conv1_out[1 : c.frames + 1])
        h = GELU(self.conv2(self.conv1_out, rows=c.hidden_rows))
        x = ElementwiseAdd(h, self.pos_embedding)
        for w in self.weights.layers:
            h = affine_norm(x, w.norm1.weight, w.norm1.bias)
            a = self_attention(
                w.attn, h, c.n_heads, c.head_dim, c.max_source_positions, causal=False
            )
            x = ElementwiseAdd(x, a)
            x = feed_forward(x, w, "norm2")
        x = affine_norm(x, self.weights.norm.weight, self.weights.norm.bias)
        # Projected from the full, already 256-row-aligned width (flm.GEMM's
        # own M tiling); only the decoder's cross-attention MHA call, later,
        # bounds these to the first max_source_positions valid rows.
        cross = []
        for w in self.cross_weights:
            k = project(x, w.k.weight, k_tile=256)
            v = project(x, w.v.weight, bias=w.v.bias, k_tile=256)
            cross.append((k, v))
        # A graph returns whole handles only: the caller reads back just the
        # first max_source_positions rows of this one itself.
        return (x, *[t for pair in cross for t in pair])


class WhisperDecoder(CausalLM):
    """Whisper-large-v3-turbo's 4-layer causal decoder, over
    ``iron.lm.CausalLM``: the same decode-step/prompt-chunk, device-loop,
    cache and ``Sample`` machinery every decoder-only model uses, extended
    with one static per-layer cross-attention cache, written once per clip
    (``encode()``) rather than once per call.

    This decoder carries no RoPE (``config.rope_base`` is unused filler: a
    tiny, harmless table `CausalLM.__init__` still builds) -- its position
    embedding is a learned table added once, like the encoder's, not
    rotated per layer -- so ``body()`` is overridden to add it and to skip
    building ``step.angles``, which ``layer()`` never reads.
    """

    profile = Path(__file__).with_name("profiles")

    def __init__(self, config: DecoderConfig, weights):
        super().__init__(config, weights)
        self.pos_embedding = iron.weight(np.asarray(weights.pos_embedding, bfloat16))
        H, D = config.n_heads, config.head_dim
        self.cross_keys = [
            iron.state((ENCODER.hidden_rows, H * D)) for _ in self.layers
        ]
        self.cross_values = [
            iron.state((ENCODER.hidden_rows, H * D)) for _ in self.layers
        ]

    def body(
        self,
        x=None,
        ids=None,
        *,
        token: Carried[np.int32],
        position: Carried[np.int32],
        chunk: Scratchpad[np.int32],
        rows: Scratchpad[np.int32],
    ):
        c = self.config
        prompt = x is not None or ids is not None
        if prompt:
            if ids is not None:
                x = Copy(self.embedding[ids])
            x = x[:rows]
            pos = Copy(self.pos_embedding[:rows])
        else:
            x = Copy(self.embedding[token]).reshape(1, c.emb_dim)
            pos = Copy(self.pos_embedding[position]).reshape(1, c.emb_dim)
        x = ElementwiseAdd(x, pos)
        step = Step(prompt, None, chunk, rows, position)
        for i, weights in enumerate(self.layers):
            x = self.layer(step, i, weights, x)
        if prompt:
            x = Copy(x[rows - 1]).reshape(1, c.emb_dim)
        logits = self.head(x)
        _, drawn = Sample(
            logits.reshape(c.vocab_size),
            self.draws,
            self.drawn,
            row=position * ROW_WORDS,
            at=position,
        )
        return logits, iron.carry(token=drawn, position=position + 1)

    def layer(self, step: Step, i: int, w, x):
        c, n = self.config, x.shape[0]
        H, D = c.n_heads, c.head_dim
        h = affine_norm(x, w.norm1.weight, w.norm1.bias)
        q = project(h, w.self_attn.q.weight, bias=w.self_attn.q.bias, k_tile=256)
        k = project(h, w.self_attn.k.weight, k_tile=256)
        v = project(h, w.self_attn.v.weight, bias=w.self_attn.v.bias, k_tile=256)
        q, k, v = (t.reshape(n * H, D) for t in (q, k, v))
        a = project(
            self.attend(step, i, q, k, v),
            w.self_attn.out.weight,
            bias=w.self_attn.out.bias,
            k_tile=256,
        )
        x = ElementwiseAdd(x, a)
        h = affine_norm(x, w.norm2.weight, w.norm2.bias)
        a = cross_attention(
            w.cross_attn,
            h,
            self.cross_keys[i],
            self.cross_values[i],
            H,
            D,
            valid=ENCODER.max_source_positions,
        )
        x = ElementwiseAdd(x, a)
        return feed_forward(x, w, "norm3")

    def head(self, x):
        h = affine_norm(x, self.norm.weight, self.norm.bias)
        return GEMV(self.embedding, h.reshape(self.config.emb_dim))

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens``, overriding
        ``CausalLM.logits``: with no prompt version
        (``load()``), its own ``_chunks()`` path (anything but exactly
        one new token) asserts ``self._prompt is not None``. A fresh
        multi-token call here instead runs a decode step a token at a
        time, which needs no prompt version at all (``self(token=...,
        chunk=0, rows=1)`` takes ``__call__``'s ``x is None and ids is
        None`` branch, straight to ``self._decode``).
        """
        tokens = self._tokens(tokens)
        n, L = tokens.size, self.config.max_seq_len
        if not 0 < n <= L:
            raise ValueError(f"{n} tokens do not fit {L} rows")
        held = self._held(tokens)
        if held == n - 1 == self._seen.size:
            out, _ = self(token=int(tokens[-1]), position=n - 1, chunk=0, rows=1)
        else:
            self._seen = tokens[:held]
            for position in range(held, n):
                out, _ = self(
                    token=int(tokens[position]), position=position, chunk=0, rows=1
                )
        self._seen = tokens
        # A copy: the next call rewrites the output buffer.
        logits = out.numpy()
        return np.array(logits).reshape(-1)

    def load(
        self, release=None, tuner=None, boundaries=None, dev=None
    ) -> "WhisperDecoder":
        """Only the decode step: Whisper's own prompt (the four special
        tokens that open a transcription, ``<|startoftranscript|>`` and its
        language/task/timestamp tokens) is far too short for a dedicated
        prompt-chunk version to be worth its own compile, and
        ``prefill_chunk`` would have to be a multiple of 256 (flm.GEMM's
        own M tiling) while also dividing ``max_seq_len`` -- 448, Whisper's
        own ``max_target_positions``, has no such divisor at all. With no
        prompt version, ``logits()``'s own fallback already runs the
        prompt a token at a time through the decode step (``GEVM``, which
        has no 256-row constraint); see ``iron.lm.CausalLM.logits``.
        """
        if dev is None:
            dev = aie_utils.ensure_current_device()
        decode = self.compile(
            dev=dev, coresident=tuner, boundaries=boundaries, **self.shapes(1)
        )
        decode.load(release=release)
        self._image = decode.plan.image
        self._prompt, self._decode = None, decode
        return self

    def encode(self, cross_arrays: tuple[np.ndarray, ...]) -> None:
        """Write one clip's cross-attention K/V, from ``WhisperEncoder``'s
        own output (``k0, v0, k1, v1, ...``, one pair a layer, already
        projected on the device): once per clip, not once per decode step,
        the only crossing between the encoder's compiled graph and the
        decoder's own.
        """
        assert self._decode is not None, f"{type(self).__name__}: load() first"
        for i in range(len(self.layers)):
            self._decode.write(self.cross_keys[i], cross_arrays[2 * i])
            self._decode.write(self.cross_values[i], cross_arrays[2 * i + 1])


# -- the oracle: float32 on the host, not composed from the operators' own
# -- references, so it catches a wiring mistake the graph's reference repeats
# -- (iron.lm's own convention for every CausalLM's Oracle).


def _widen(tree):
    if isinstance(tree, list):
        return [_widen(t) for t in tree]
    if isinstance(tree, SimpleNamespace):
        return SimpleNamespace(**{k: _widen(v) for k, v in vars(tree).items()})
    return np.asarray(tree, np.float32)


def _oracle_erf(x):
    # Abramowitz & Stegun 7.1.26, max abs error 1.5e-7: well under bf16 noise,
    # and this host has no torch/scipy to call exactly.
    a1, a2, a3, a4, a5, p = (
        0.254829592,
        -0.284496736,
        1.421413741,
        -1.453152027,
        1.061405429,
        0.3275911,
    )
    sign, ax = np.sign(x), np.abs(x)
    t = 1.0 / (1.0 + p * ax)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * np.exp(-ax * ax)
    return sign * y


def _oracle_gelu(x):
    return 0.5 * x * (1.0 + _oracle_erf(x / np.sqrt(2.0)))


def _oracle_norm(x, w, eps: float = 1e-5):
    mean = x.mean(axis=-1, keepdims=True)
    var = ((x - mean) ** 2).mean(axis=-1, keepdims=True)
    return (x - mean) / np.sqrt(var + eps) * w.weight + w.bias


def _oracle_linear(x, w, bias=None):
    y = x @ w.T
    return y if bias is None else y + bias


def _oracle_mha(q, k, v, n_heads: int, causal: bool):
    T, E = q.shape
    S = k.shape[0]
    D = E // n_heads
    q = q.reshape(T, n_heads, D).transpose(1, 0, 2)
    k = k.reshape(S, n_heads, D).transpose(1, 0, 2)
    v = v.reshape(S, n_heads, D).transpose(1, 0, 2)
    scores = (q @ k.transpose(0, 2, 1)) / np.sqrt(D)
    if causal:
        scores = scores + np.triu(np.full((T, S), -np.inf, np.float32), k=1 + (S - T))
    scores = scores - scores.max(axis=-1, keepdims=True)
    p = np.exp(scores)
    p /= p.sum(axis=-1, keepdims=True)
    return (p @ v).transpose(1, 0, 2).reshape(T, E)


def _oracle_conv1d(x, weight, bias, stride: int):
    k = weight.shape[-1]
    pad = (k - 1) // 2
    xp = np.pad(x, ((pad, pad), (0, 0)))
    out_rows = (xp.shape[0] - k) // stride + 1
    cols = [
        np.tensordot(weight, xp[t * stride : t * stride + k], axes=([2, 1], [0, 1]))
        for t in range(out_rows)
    ]
    return np.stack(cols, axis=0) + bias


class WhisperEncoderOracle:
    """The audio encoder's float32 forward pass on the host, from a raw
    waveform, the reference ``WhisperEncoder`` is judged by. Not composed
    from the operators' own ``reference()``s: a numpy reimplementation
    from the architecture directly, so it catches a wiring mistake the
    graph's own reference would repeat.

    Args:
        config: ``EncoderConfig``.
        weights: ``load_weights`` over ``encoder_layout(config)``, any dtype.
    """

    def __init__(self, config: EncoderConfig, weights):
        self.config = config
        self.weights = _widen(weights)
        self._logmel = WhisperLogMel(config)

    def __call__(self, waveform: np.ndarray) -> np.ndarray:
        """``(max_source_positions, d_model)`` float32 encoder output."""
        c, w = self.config, self.weights
        feats = self._logmel.exact(waveform)
        h = _oracle_gelu(_oracle_conv1d(feats, w.conv1.weight, w.conv1.bias, 1))
        h = _oracle_gelu(_oracle_conv1d(h, w.conv2.weight, w.conv2.bias, 2))
        x = h + w.pos_embedding
        for layer in w.layers:
            h = _oracle_norm(x, layer.norm1)
            q = _oracle_linear(h, layer.attn.q.weight, layer.attn.q.bias)
            k = _oracle_linear(h, layer.attn.k.weight)
            v = _oracle_linear(h, layer.attn.v.weight, layer.attn.v.bias)
            a = _oracle_mha(q, k, v, c.n_heads, causal=False)
            a = _oracle_linear(a, layer.attn.out.weight, layer.attn.out.bias)
            x = x + a
            h = _oracle_norm(x, layer.norm2)
            h = _oracle_gelu(_oracle_linear(h, layer.fc1.weight, layer.fc1.bias))
            h = _oracle_linear(h, layer.fc2.weight, layer.fc2.bias)
            x = x + h
        return _oracle_norm(x, w.norm)


class WhisperDecoderOracle:
    """The decoder's float32 forward pass on the host, cross-attending over
    one fixed encoder output (as the real decoder's cross-attention k/v are
    fixed once a clip): ``logits(tokens)`` matches
    ``iron.lm.CausalLM.logits``'s own contract (the logits after the last
    of ``tokens``) so ``iron.lm.generation``'s ``accuracy``/``determinism``/
    ``generate`` take it exactly as they take the NPU model.

    Args:
        config: ``DecoderConfig`` (this application's ``DECODER``).
        weights: ``load_weights`` over ``decoder_layout(config)``, any
            dtype; ``embedding`` at the checkpoint's own ``vocab_size``
            (unpadded -- padding is a ``Sample``-only concern).
        encoder_hidden: ``(max_source_positions, d_model)`` float32, one
            clip's ``WhisperEncoderOracle`` output.
    """

    def __init__(self, config: DecoderConfig, weights, encoder_hidden: np.ndarray):
        self.config = config
        self.weights = _widen(weights)
        self.encoder_hidden = np.asarray(encoder_hidden, np.float32)

    def logits(self, tokens) -> np.ndarray:
        c, w = self.config, self.weights
        ids = np.asarray(tokens, np.int64).reshape(-1)
        x = w.embedding[ids] + w.pos_embedding[: len(ids)]
        for layer in w.layers:
            h = _oracle_norm(x, layer.norm1)
            q = _oracle_linear(h, layer.self_attn.q.weight, layer.self_attn.q.bias)
            k = _oracle_linear(h, layer.self_attn.k.weight)
            v = _oracle_linear(h, layer.self_attn.v.weight, layer.self_attn.v.bias)
            a = _oracle_mha(q, k, v, c.n_heads, causal=True)
            a = _oracle_linear(a, layer.self_attn.out.weight, layer.self_attn.out.bias)
            x = x + a
            h = _oracle_norm(x, layer.norm2)
            q = _oracle_linear(h, layer.cross_attn.q.weight, layer.cross_attn.q.bias)
            k = _oracle_linear(self.encoder_hidden, layer.cross_attn.k.weight)
            v = _oracle_linear(
                self.encoder_hidden, layer.cross_attn.v.weight, layer.cross_attn.v.bias
            )
            a = _oracle_mha(q, k, v, c.n_heads, causal=False)
            a = _oracle_linear(
                a, layer.cross_attn.out.weight, layer.cross_attn.out.bias
            )
            x = x + a
            h = _oracle_norm(x, layer.norm3)
            h = _oracle_gelu(_oracle_linear(h, layer.fc1.weight, layer.fc1.bias))
            h = _oracle_linear(h, layer.fc2.weight, layer.fc2.bias)
            x = x + h
        x = _oracle_norm(x, w.norm)
        return (x[-1] @ w.embedding.T).reshape(-1)


# -- the runner: the checkpoint (or random weights), the two towers, and the
# -- pipeline that connects them.


def _to_bf16(tree):
    if isinstance(tree, list):
        return [_to_bf16(t) for t in tree]
    if isinstance(tree, SimpleNamespace):
        return SimpleNamespace(**{k: _to_bf16(v) for k, v in vars(tree).items()})
    return np.asarray(tree, np.float32).astype(bfloat16)


class Runner:
    """Whisper-large-v3-turbo: the encoder and the decoder, from one
    checkpoint (or, with no ``weights_path``, weights drawn at ``seed``),
    and the pipeline that connects them -- an audio clip's log-mel features
    through the encoder once a clip, its cross-attention k/v written into
    the decoder once (``encode``), then any number of decode steps or
    ``generate`` calls against that fixed audio context.

    Not a subclass of ``iron.lm.Runner``: that assumes one decoder-only
    model, one tokenizer and a free-text prompt, none of which fits an
    encoder-decoder speech model (Whisper's decoder prompt is four fixed
    special tokens, not free text, and there are two towers' weights, not
    one). ``iron.lm.generation``'s ``accuracy``/``determinism``/
    ``generate`` are plain functions over anything with ``.logits()``/
    ``.generate()``, so they still apply directly to ``WhisperDecoder`` and
    ``WhisperDecoderOracle`` here without that base class at all.
    """

    #: <|startoftranscript|>, <|en|>, <|transcribe|>, <|notimestamps|>
    #: (generation_config.json's decoder_start_token_id/lang_to_id['<|en|>']/
    #: task_to_id['transcribe']/no_timestamps_token_id): not read from the
    #: checkpoint directory here (no tokenizer wrapper yet, see README.md),
    #: so hardcoded at the real checkpoint's own values.
    PROMPT = (50258, 50259, 50360, 50364)

    def __init__(self, weights_path=None, seed: int = 0):
        self.seed = seed
        real_decoder_config = dataclasses.replace(DECODER, vocab_size=51866)
        if weights_path is None:
            self.checkpoint = None
            self.encoder_weights = random_weights(
                encoder_layout(ENCODER), ENCODER.n_layers, seed
            )
            self.decoder_weights = random_weights(
                decoder_layout(real_decoder_config), real_decoder_config.n_layers, seed
            )
        else:
            self.checkpoint = Checkpoint(weights_path)
            self.encoder_weights = load_weights(
                encoder_tensors(self.checkpoint.tensors),
                encoder_layout(ENCODER),
                ENCODER.n_layers,
            )
            self.decoder_weights = load_weights(
                decoder_tensors(self.checkpoint.tensors),
                decoder_layout(real_decoder_config),
                real_decoder_config.n_layers,
            )
        padded = np.zeros((VOCAB_SIZE, DECODER.emb_dim), np.float32)
        padded[:51866] = np.asarray(self.decoder_weights.embedding, np.float32)
        self._padded_embedding = padded
        self.encoder: WhisperEncoder | None = None
        self.decoder: WhisperDecoder | None = None
        self._logmel: WhisperLogMel | None = None

    def npu(self) -> "WhisperDecoder":
        """Both towers compiled and loaded; returns the decoder (the model
        ``iron.lm.generation``'s helpers call ``.logits()``/``.generate()``
        on). Call ``encode(waveform)`` before either: cross-attention has no
        audio context until then.
        """
        cross_weights = _to_bf16([w.cross_attn for w in self.decoder_weights.layers])
        self.encoder = WhisperEncoder(
            ENCODER, _to_bf16(self.encoder_weights), cross_weights
        )
        self.encoder.compile(x=((ENCODER.conv1_rows, ENCODER.mels), bfloat16))
        decoder_weights = SimpleNamespace(**vars(self.decoder_weights))
        decoder_weights.embedding = self._padded_embedding.astype(bfloat16)
        self.decoder = WhisperDecoder(DECODER, _to_bf16(decoder_weights))
        self.decoder.load()
        self._logmel = WhisperLogMel(ENCODER)
        wave_len = (ENCODER.frames - 1) * ENCODER.hop + self._logmel.k_pad
        self._logmel.compile(wave=((wave_len,), np.float32))
        return self.decoder

    def encode(self, waveform: np.ndarray) -> None:
        """Run the encoder on ``waveform`` and write its cross-attention
        k/v into the loaded decoder: once a clip, not once a decode step.
        """
        assert self.encoder is not None and self.decoder is not None, "npu() first"
        x = self._logmel.conv1_input(waveform)
        out = self.encoder(x)
        c = ENCODER
        cross = tuple(
            np.asarray(o.numpy(), np.float32)
            .reshape(c.hidden_rows, c.d_model)
            .astype(bfloat16)
            for o in out[1:]
        )
        self.decoder.encode(cross)

    def cpu(self, waveform: np.ndarray) -> WhisperDecoderOracle:
        """The float32 oracle of both towers, for the same ``waveform``
        ``encode`` was given: a fresh ``WhisperEncoderOracle`` run once,
        its output fixed into a ``WhisperDecoderOracle``.
        """
        encoder_oracle = WhisperEncoderOracle(ENCODER, self.encoder_weights)
        real_decoder_config = dataclasses.replace(DECODER, vocab_size=51866)
        return WhisperDecoderOracle(
            real_decoder_config, self.decoder_weights, encoder_oracle(waveform)
        )

    def prompt(self, num_tokens: int = 0) -> list[int]:
        """The fixed special-token prompt, optionally extended by
        ``num_tokens`` random continuation tokens (no tokenizer wrapper
        yet: a real-text continuation needs a vocabulary and a decoder,
        see README.md -- random tokens still exercise every real run path,
        the same convention ``iron.lm.Runner.prompt`` uses with no
        tokenizer).
        """
        rng = np.random.default_rng(self.seed)
        extra = rng.integers(0, 51866, num_tokens).tolist()
        return [*self.PROMPT, *extra]
