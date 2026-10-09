#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's text encoder: its shape, where its checkpoint keeps
each weight, and the encoder on the NPU as one graph.
"""

import dataclasses
import math
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16, finfo

import iron
from iron.common import Scratchpad
from iron.common.graph.narrowing import JointNarrowing
from iron.lm import Layout, rope_angles
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gelu import GELU
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.softmax import Softmax

# An f32 accumulator and native bf16 inputs: the defaults' bfp16 inputs and
# per-K-tile bf16 rounding cost the encoder accuracy.
ACCURATE = dict(prio_accuracy=True, emulate_bf16_mmul_with_bfp16=False)

# The fewest rows a version has, 16 to each row of cores: a version's rows
# are a multiple of it.
ROWS = 64

# Where the text tune writes its tables, one per device; the vision tower's
# are its own (``vision.model.COSTS``), merged where a graph holds both.
COSTS = Path(__file__).parent


@dataclasses.dataclass(frozen=True)
class Config:
    vocab_size: int = 262144
    emb_dim: int = 512
    n_layers: int = 24
    n_heads: int = 4
    hidden_dim: int = 2048
    # A sliding layer's KV heads and head size, then a global layer's.
    sliding_kv_groups: int = 2
    sliding_head_dim: int = 256
    global_kv_groups: int = 1
    global_head_dim: int = 512
    global_layers: tuple[int, ...] = (5, 11, 17, 23)
    sliding_window: int = 512
    sliding_rope_base: float = 10000.0
    global_rope_base: float = 1000000.0
    ple_dim: int = 512
    out_dim: int = 768
    # The Matryoshka truncations, each renormalized.
    mrl_dims: tuple[int, ...] = (768, 512, 256, 128)
    eps: float = 1e-6
    bos: int = 2
    eos: int = 1
    # The placeholders an image's or a clip's soft tokens take the place of,
    # and the markers either side of a run of them.
    image_token: int = 258880
    audio_token: int = 258881
    video_token: int = 258884
    pad: int = 0
    boi: int = 255999
    eoi: int = 258882
    boa: int = 256000
    eoa: int = 258883

    def heads(self, i: int) -> tuple[int, int]:
        """Layer ``i``'s KV groups and head size."""
        if i in self.global_layers:
            return self.global_kv_groups, self.global_head_dim
        return self.sliding_kv_groups, self.sliding_head_dim


EMBEDDINGGEMMA_2 = Config()


def layout(config: Config) -> Layout:
    """Each weight's place in the encoder, its name in the checkpoint and
    its shape. A global layer's attention is wider than a sliding one's, so
    the attention weights are listed layer by layer.
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
        G, D = c.heads(i)
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


class EmbeddingGemma(iron.Graph):
    """The encoder over ``max_tokens`` rows at most, a version per row count.

    A call takes the token ids, padded with ``vocab_size``, the id of a zero
    row past the scaled embedding table, and ``n``, the real rows, which
    masks the padded keys and the pooling; padded rows are computed and
    never read. The table's rows are gathered on the device. It returns one
    unit-length embedding per ``mrl_dims`` truncation, a row each, zero past
    its length. Attention is bidirectional and unscaled. A version longer
    than the sliding window adds a band mask to a sliding layer's scores,
    its ``(heads, rows, rows)`` held per version.
    """

    def __init__(self, config: Config, weights, max_tokens: int):
        if max_tokens % ROWS:
            raise ValueError(f"{max_tokens} rows are not whole {ROWS}-row versions")
        c = config
        self.config = config
        self.max_tokens = max_tokens
        # Each version's rows: doubling from ROWS, then max_tokens.
        self.rows = [
            ROWS * 2**j
            for j in range(max_tokens.bit_length())
            if ROWS * 2**j < max_tokens
        ]
        self.rows.append(max_tokens)
        r = c.n_heads // c.sliding_kv_groups
        self.bands = {}
        for T in self.rows:
            if T > c.sliding_window + 1:
                i = np.arange(T)
                band = abs(i[:, None] - i) <= c.sliding_window
                self.bands[T] = np.tile(
                    np.where(band, 0, finfo(bfloat16).min).astype(bfloat16), (r, 1)
                )
        table = np.zeros((c.vocab_size + 1, c.emb_dim), bfloat16)
        table[:-1] = weights.embedding.astype(np.float32) * np.sqrt(
            np.float32(c.emb_dim)
        )
        self.embedding = iron.weight(table)
        self.norm = weights.norm
        self.ple = weights.ple
        self.ple_norm = weights.ple_norm
        self.layers = weights.layers
        self.scales = [
            np.full((max_tokens, c.emb_dim), w.scalar[0], bfloat16)
            for w in weights.layers
        ]
        self.angles = {
            D: iron.weight(rope_angles(D, max_tokens, base).astype(bfloat16))
            for D, base in (
                (config.sliding_head_dim, config.sliding_rope_base),
                (config.global_head_dim, config.global_rope_base),
            )
        }
        # Softmax of zeros bounded to n is the pooling weights, 1/n each; 32
        # rows of them, the fewest a GEMM takes.
        self.pool = {T: iron.weight(np.zeros((32, T), bfloat16)) for T in self.rows}
        # A power of four: a row's RMS over it is its norm over a power of two.
        width = 4 ** math.ceil(math.log(c.out_dim, 4))
        self.projection = np.zeros((len(c.mrl_dims), width, c.emb_dim), bfloat16)
        for j, d in enumerate(c.mrl_dims):
            self.projection[j, :d] = weights.projection[:d]
        self.projection = self.projection.reshape(-1, c.emb_dim)
        self.unit = np.full(width, 1 / np.sqrt(width), bfloat16)

    def body(self, ids, *, n: Scratchpad[np.int32]):
        return self.encoder(Copy(self.embedding[ids]), n)

    def encoder(self, x, n):
        """The encoder over the token embeddings ``x`` ``(T, emb_dim)``, of
        which the first ``n`` are real.
        """
        c = self.config
        T, E, P, L = x.shape[0], c.emb_dim, c.ple_dim, c.n_layers
        # The projection's E ** -0.5 scale folded into the norm's epsilon:
        # RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        ple = GEMM(x, self.ple, b_col_maj=True, **ACCURATE).reshape(T * L, P)
        ple = RMSNorm(ple, weight=self.ple_norm, epsilon=c.eps * E)
        ple = Copy(ple.reshape(T, L, P).transpose(1, 0, 2)).reshape(L, T, P)
        for i, w in enumerate(self.layers):
            x = self.layer(i, w, x, ple[i], n)
        h = RMSNorm(x, weight=self.norm, epsilon=c.eps)
        mean = Softmax(self.pool[T][:, :n])
        y = GEMV(self.projection, GEMM(mean, h[:n], **ACCURATE)[0])
        return RMSNorm(
            y.reshape(len(c.mrl_dims), self.unit.size), weight=self.unit, epsilon=0.0
        )

    def layer(self, i, w, x, ple, n):
        c = self.config
        h = RMSNorm(x, weight=w.norm1, epsilon=c.eps)
        a = RMSNorm(self.attention(i, w, h, n), weight=w.norm2, epsilon=c.eps)
        x = ElementwiseAdd(x, a)
        h = RMSNorm(x, weight=w.norm3, epsilon=c.eps)
        gate = GELU(GEMM(h, w.gate, b_col_maj=True, **ACCURATE))
        f = ElementwiseMul(gate, GEMM(h, w.up, b_col_maj=True, **ACCURATE))
        f = GEMM(f, w.down, b_col_maj=True, **ACCURATE)
        x = ElementwiseAdd(x, RMSNorm(f, weight=w.norm4, epsilon=c.eps))
        g = GELU(GEMM(x, w.ple_gate, b_col_maj=True, **ACCURATE))
        g = GEMM(ElementwiseMul(g, ple), w.ple_proj, b_col_maj=True, **ACCURATE)
        x = ElementwiseAdd(x, RMSNorm(g, weight=w.ple_norm, epsilon=c.eps))
        return ElementwiseMul(x, self.scales[i][: x.shape[0]])

    def attention(self, i, w, h, n):
        c = self.config
        T, H = h.shape[0], c.n_heads
        G, D = c.heads(i)
        r = H // G
        angles = self.angles[D][:T]
        q = GEMM(h, w.q, b_col_maj=True, **ACCURATE).reshape(T * H, D)
        k = GEMM(h, w.k, b_col_maj=True, **ACCURATE).reshape(T * G, D)
        v = GEMM(h, w.v, b_col_maj=True, **ACCURATE).reshape(T * G, D)
        q = RoPE(RMSNorm(q, weight=w.q_norm, epsilon=c.eps), angles)
        k = RoPE(RMSNorm(k, weight=w.k_norm, epsilon=c.eps), angles)
        v = RMSNorm(v, epsilon=c.eps)
        q = Copy(q.reshape(T, H, D).transpose(1, 0, 2)).reshape(H, T, D)
        if G > 1:
            k = Copy(k.reshape(T, G, D).transpose(1, 0, 2)).reshape(G, T, D)
            v = Copy(v.reshape(T, G, D).transpose(1, 0, 2)).reshape(G, T, D)
        else:
            k, v = k.reshape(1, T, D), v.reshape(1, T, D)
        for g in range(G):
            heads = q[g * r : (g + 1) * r].reshape(r * T, D)
            scores = GEMM(heads, k[g], b_col_maj=True, **ACCURATE)
            if i not in c.global_layers and T in self.bands:
                scores = ElementwiseAdd(scores, self.bands[T])
            weights = Softmax(scores[:, :n])
            # Over the group's queries, which the scores were their last use of.
            GEMM(weights, v[g, :n], heads, **ACCURATE)
        o = Copy(q.transpose(1, 0, 2)).reshape(T, H * D)
        return GEMM(o, w.o, b_col_maj=True, **ACCURATE)

    # -- on the host -----------------------------------------------------------

    def shapes(self) -> list[dict]:
        """Each version's input shapes, fewest rows first."""
        return [dict(ids=((T,), np.int32)) for T in self.rows]

    def load(self, tuner: JointNarrowing | None = None) -> "EmbeddingGemma":
        """Compile every version before the first call, so the arena is made once.

        Args:
            tuner: Narrows and packs each version's designs by cost.
        """
        for shapes in self.shapes():
            self.compile(coresident=tuner, **shapes)
        return self

    def inputs(self, tokens) -> tuple[np.ndarray, int]:
        """A call's ``ids`` and ``n`` for ``tokens``, padded to the fewest rows
        a version has.

        Raises:
            ValueError: ``tokens`` is empty or longer than ``max_tokens``.
            IndexError: A token is outside ``[-vocab_size, vocab_size)``.
        """
        tokens = np.asarray(tokens)
        n, V = len(tokens), self.config.vocab_size
        if not 0 < n <= self.max_tokens:
            raise ValueError(f"{n} tokens do not fit {self.max_tokens} rows")
        outside = tokens[(tokens < -V) | (tokens >= V)]
        if outside.size:
            raise IndexError(f"tokens {outside} are outside [-{V}, {V})")
        ids = np.full(min(T for T in self.rows if T >= n), V, np.int32)
        ids[:n] = tokens % V
        return ids, n

    def encode(self, tokens, dims: int = 768) -> np.ndarray:
        """The unit-length embedding of ``tokens`` truncated to ``dims``, one
        of ``mrl_dims``.
        """
        ids, n = self.inputs(tokens)
        rows = self(ids, n=n).numpy().reshape(len(self.config.mrl_dims), -1)
        return np.asarray(rows[self.config.mrl_dims.index(dims), :dims], np.float32)


def text_tensors(tensors: dict) -> dict:
    """The text encoder's tensors of the full checkpoint, which also holds
    the vision and audio towers.
    """
    return {k: v for k, v in tensors.items() if k.startswith("language_model.")}
