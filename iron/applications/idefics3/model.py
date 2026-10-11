#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM over the shared decoder (``iron.lm``): its text backbone's layer
and head on the NPU (``SmolVLMText``) and on the CPU in float32
(``SmolVLMTextOracle``, the reference it is judged by), SmolVLM-256M-
Instruct's shape. Run it with ``python -m iron.applications.idefics3.model``.

SmolVLM (Idefics3) is a vision tower (``iron/applications/idefics3/vision/``) whose
projected patch features are spliced into this text backbone's input
embedding before its layers run (``iron.lm.CausalLM``'s
``embed(x, pixel_values)`` hook); traced from the real checkpoint
(``Idefics3ForConditionalGeneration``/``VLlama3ForCausalLM``), the text
backbone itself is the plain Llama architecture: RMSNorm, RoPE with no
frequency scaling, SwiGLU, no projection bias, grouped-query attention
(9 heads over 3 KV groups) and an **untied** output head (``lm_head``,
distinct from the input embedding, unlike Llama/SmolLM2/Qwen 2.5).
"""

from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron import lm
from iron.lm import (
    Checkpoint,
    CausalLM,
    Config,
    Layout,
    Oracle,
    load_weights,
    project,
    random_weights,
    swiglu,
)
from iron.applications.idefics3.vision.model import (
    VISION,
    VisionTower,
    VisionTowerOracle,
    layout as vision_layout,
    vision_tensors,
)
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE

SMOLVLM_256M_INSTRUCT = Config(
    vocab_size=49280,
    emb_dim=576,
    n_layers=30,
    n_heads=9,
    n_kv_groups=3,
    head_dim=64,
    hidden_dim=1536,
    max_seq_len=8192,
    rope_base=100000.0,
)

# SmolVLM's text backbone's RMSNorm epsilon.
EPS = np.float32(1e-5)


class SmolVLMTextOracle(Oracle):
    """SmolVLM's text backbone's forward pass in float32, on the host."""

    norm: np.ndarray
    lm_head: np.ndarray

    def layer(self, angles, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        h = rms_norm(x, w.norm1)
        q = self.rotate((h @ w.q.T).reshape(n, H, D), angles)
        k = self.rotate((h @ w.k.T).reshape(n, G, D), angles)
        v = (h @ w.v.T).reshape(n, G, D)
        x = x + self.attend(q, k, v) @ w.o.T
        h = rms_norm(x, w.norm2)
        F = w.gate.shape[0]
        half = np.matmul(h, w.gate.T, out=self.buffer("gate", (n, F)))
        half *= np.float32(0.5)
        # SiLU, with the sigmoid as a tanh, which does not overflow.
        silu = np.tanh(half, out=self.buffer("silu", (n, F)))
        silu += 1
        silu *= half
        silu *= np.matmul(h, w.up.T, out=self.buffer("up", (n, F)))
        return x + silu @ w.down.T

    def head(self, x):
        return rms_norm(x, self.norm) @ self.lm_head.T


def rms_norm(x, w):
    return x / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + EPS) * w


class SmolVLMText(CausalLM):
    """SmolVLM's text backbone on ``config``'s shape and ``weights``
    (``embedding``, ``lm_head`` -- untied, ``norm`` and ``layers``). Every
    matrix is read ``(out, in)``, as the checkpoint ships it.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = SmolVLMTextOracle
    norm: np.ndarray
    lm_head: np.ndarray

    def layer(self, step, i, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        h = RMSNorm(x, weight=w.norm1)
        # emb_dim (576 = 2**6 * 3**2) is not a multiple of flm.GEMM's
        # default k_tile (512); its own default tile_n's ct_max_k (128,
        # 2**7) divides no multiple of 576, so tile_n=32 (ct_max_k=32)
        # too, at k_tile=192 -- hidden_dim (1536) is a multiple of both.
        tiled = dict(k_tile=192, tile_n=32)
        q, k, v = (
            project(h, p, tile_size_output=D // 2, **tiled) for p in (w.q, w.k, w.v)
        )
        q = RoPE(q.reshape(n * H, D), step.angles)
        k = RoPE(k.reshape(n * G, D), step.angles)
        x = ElementwiseAdd(x, project(self.attend(step, i, q, k, v), w.o, **tiled))
        h = RMSNorm(x, weight=w.norm2)
        return ElementwiseAdd(x, swiglu(h, w.gate, w.up, w.down, **tiled))

    def head(self, x):
        return GEMV(self.lm_head, RMSNorm(x, weight=self.norm))


def layout(config: Config) -> Layout:
    """Each weight's place in ``SmolVLMText``, its name in a Hugging Face
    checkpoint and its shape. The output head is ``lm_head``, untied from
    the input embedding.
    """
    c = config
    E, F, V = c.emb_dim, c.hidden_dim, c.vocab_size
    Q, KV = c.n_heads * c.head_dim, c.n_kv_groups * c.head_dim
    layer = "model.text_model.layers.{i}"
    return {
        "embedding": ("model.text_model.embed_tokens.weight", (V, E)),
        "lm_head": ("lm_head.weight", (V, E)),
        "norm": ("model.text_model.norm.weight", (E,)),
        "layers.{i}.norm1": (f"{layer}.input_layernorm.weight", (E,)),
        "layers.{i}.q": (f"{layer}.self_attn.q_proj.weight", (Q, E)),
        "layers.{i}.k": (f"{layer}.self_attn.k_proj.weight", (KV, E)),
        "layers.{i}.v": (f"{layer}.self_attn.v_proj.weight", (KV, E)),
        "layers.{i}.o": (f"{layer}.self_attn.o_proj.weight", (E, Q)),
        "layers.{i}.norm2": (f"{layer}.post_attention_layernorm.weight", (E,)),
        "layers.{i}.gate": (f"{layer}.mlp.gate_proj.weight", (F, E)),
        "layers.{i}.up": (f"{layer}.mlp.up_proj.weight", (F, E)),
        "layers.{i}.down": (f"{layer}.mlp.down_proj.weight", (E, F)),
    }


def text_tensors(tensors: dict) -> dict:
    """The text backbone's tensors of the full checkpoint, plus the untied
    output head.
    """
    return {
        k: v
        for k, v in tensors.items()
        if k.startswith("model.text_model.") or k == "lm_head.weight"
    }


class Tokenizer:
    """SmolVLM's BPE tokenizer (its ``tokenizer.json``)."""

    def __init__(self, hf):
        self.hf = hf

    def encode(self, text: str) -> list[int]:
        return self.hf.encode(text).ids

    def decode(self, tokens: list[int]) -> str:
        return self.hf.decode(tokens)


def tokenizer(path) -> Tokenizer:
    """SmolVLM's tokenizer, from its ``tokenizer.json``."""
    from tokenizers import Tokenizer as HFTokenizer

    return Tokenizer(HFTokenizer.from_file(str(path)))


#: ``<|im_start|>``, the turn marker every prompt starts with.
BOS = 1


class Runner(lm.Runner):
    """SmolVLM-256M-Instruct's text backbone, from its checkpoint and
    ``tokenizer.json`` (text-only: no image input yet).

    The checkpoint also holds the vision tower and connector; ``__init__``
    filters to the text backbone's own tensors (``text_tensors``) before
    ``load_weights``, which is strict about what the layout does not cover.
    """

    config = SMOLVLM_256M_INSTRUCT
    layout = staticmethod(layout)
    model = SmolVLMText
    open_tokenizer = staticmethod(tokenizer)
    bos = BOS

    def __init__(self, weights_path=None, tokenizer_path=None, config=None, seed=0):
        if weights_path is None:
            super().__init__(
                weights_path=None,
                tokenizer_path=tokenizer_path,
                config=config,
                seed=seed,
            )
            return
        self.config = config or type(self).config
        self.seed = seed
        self.checkpoint = Checkpoint(weights_path)
        self.weights = load_weights(
            text_tensors(self.checkpoint.tensors),
            self.layout(self.config),
            self.config.n_layers,
        )
        self.tokenizer = (
            None if tokenizer_path is None else self.open_tokenizer(tokenizer_path)
        )


# The real processor's token layout for one unsplit 512x512 image, first in
# the turn, behind the fixed "<|im_start|>User:" role preamble: a
# compile-time constant for this first pass, empirically confirmed against
# the real Idefics3Processor (do_image_splitting=False) -- two different
# questions after the image both put its first token at position 5, and
# the image block is always exactly 64 tokens (image_seq_len) long.
IMAGE_PREAMBLE = 5
IMAGE_TOKENS = 64

# The real processor's own ids either side of the question, for exactly
# the preamble/image layout above ("<|im_start|>User:<image>{question}
# <end_of_utterance>\nAssistant:", one image, no splitting): read off
# Idefics3Processor's real output, not guessed. A prompt built this way
# differs from the real processor's only in skipping its image-splitting
# tiles (out of scope: module docstring).
_PREAMBLE_IDS = [1, 11126, 42, 49189, 49152]
_SUFFIX_IDS = [49189]
_TAIL_IDS = [49279, 198, 9519, 9531, 42]


def build_prompt(tokenizer, question: str) -> list[int]:
    """The token ids for one unsplit 512x512 image, first in the turn,
    then ``question``, the real processor's own layout (``IMAGE_PREAMBLE``/
    ``IMAGE_TOKENS``) at any question text.
    """
    image = [49190] * IMAGE_TOKENS
    return _PREAMBLE_IDS + image + _SUFFIX_IDS + tokenizer.encode(question) + _TAIL_IDS


class SmolVLM(SmolVLMText):
    """SmolVLM's text backbone with its vision tower spliced in
    (``embed()``'s ``pixel_values``): one 512x512 image, first in the
    turn, behind the fixed role preamble (module docstring, ``IMAGE_PREAMBLE``).
    """

    def __init__(self, config, weights):
        super().__init__(config, weights)
        self.vision = VisionTower(VISION, self.vision)
        self.combined = iron.state((config.prefill_chunk, config.emb_dim))

    def embed(self, x, pixel_values=None, rows=None):
        if pixel_values is None:
            return x
        # x is bounded to rows (ids[:rows]'s Extent); copying it into a
        # scratch state bound the same way keeps that bound (an unbounded
        # destination does not: it copies the whole chunk, a real compute
        # and buffer-descriptor cost, found the slow way -- see
        # skill-gaps.md). The image's own fixed rows (always within the
        # real prompt's valid length: the image is always first) overwrite
        # after, a plain slice of the now-unbounded-again scratch buffer.
        features = self.vision(pixel_values)
        Copy(x, self.combined[:rows])
        Copy(features, self.combined[IMAGE_PREAMBLE : IMAGE_PREAMBLE + IMAGE_TOKENS])
        return self.combined[:rows]

    def shapes(self, rows: int) -> dict:
        shapes = super().shapes(rows)
        if rows > 1:
            shapes["pixel_values"] = ((512, 512 * 3), bfloat16)
        return shapes


class SmolVLMOracle(SmolVLMTextOracle):
    """SmolVLM's forward pass in float32, on the host, the vision tower
    spliced in the same way ``SmolVLM`` is.
    """

    def __init__(self, config, weights):
        super().__init__(config, weights)
        self.vision = VisionTowerOracle(VISION, self.vision)

    def embed(self, x, pixel_values=None):
        if pixel_values is None:
            return x
        features = self.vision(pixel_values)
        x = x.copy()
        x[IMAGE_PREAMBLE : IMAGE_PREAMBLE + IMAGE_TOKENS] = features
        return x


class VLMRunner(Runner):
    """SmolVLM-256M-Instruct, the text backbone and the vision tower
    together, from its checkpoint and ``tokenizer.json``.
    """

    model = SmolVLM

    def __init__(self, weights_path=None, tokenizer_path=None, config=None, seed=0):
        super().__init__(weights_path, tokenizer_path, config, seed)
        if weights_path is None:
            vision_weights = random_weights(
                vision_layout(VISION), VISION.n_layers, seed
            )
        else:
            vision_weights = load_weights(
                vision_tensors(self.checkpoint.tensors),
                vision_layout(VISION),
                VISION.n_layers,
            )
        self.weights.vision = vision_weights

    def npu(self, cost_table=None, boundaries=None, kinds=None):
        model = self.model(self.config, self.weights)
        tuner = (
            None
            if cost_table is None
            else JointNarrowing(CostTable(cost_table), kinds=kinds or NarrowingKinds())
        )
        release = None if self.checkpoint is None else self.checkpoint.release
        return model.load(release, tuner, boundaries)

    def cpu(self):
        return SmolVLMOracle(self.config, self.weights)


if __name__ == "__main__":
    lm.main(Runner, "SmolVLM-256M-Instruct's text backbone on the NPU")
