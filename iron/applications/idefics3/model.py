#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM over the shared decoder and layer (``iron.lm``): its text
backbone's head on the NPU (``SmolVLMText``) and on the CPU in float32
(``SmolVLMTextOracle``, the reference it is judged by), and SmolVLM-256M-
Instruct's shape, read from its checkpoint's own (nested) ``config.json``.
Run it with ``python -m iron.applications.idefics3.model``.

SmolVLM (Idefics3) is a vision tower (``iron/applications/idefics3/vision/``)
whose projected patch features are spliced into this text backbone's input
embedding before its layers run; the text backbone is Llama's layer
(``iron.lm.Layer``: 9 heads over 3 KV groups) with an **untied** output head
(``lm_head``, distinct from the input embedding).

Its tunables at 576 wide, which flm.GEMM's default tiles do not divide,
are its profile's: ``tile_n`` 32 and ``k_tile`` 192.
"""

import dataclasses
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16
from tokenizers import Tokenizer as HFTokenizer

from aie.iron.kernels.sample import ROW_WORDS

import iron
from iron import Carried, Scratchpad, lm
from iron.lm import CausalLM, DecodeStep, DecoderConfig, Oracle, widen
from iron.applications.idefics3.vision.model import (
    VisionConfig,
    VisionOracle,
    VisionTower,
)
from iron.operators.copy import Copy
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.sample import Sample
from iron.tune.narrowing import CostTable, JointNarrowing, NarrowingKinds


@dataclasses.dataclass(frozen=True)
class SmolVLMTextConfig(DecoderConfig):
    """SmolVLM's text backbone's shape, from the checkpoint's nested
    ``text_config``.
    """

    vocab_size: int = dataclasses.field(metadata={"json": "text_config.vocab_size"})
    emb_dim: int = dataclasses.field(metadata={"json": "text_config.hidden_size"})
    n_layers: int = dataclasses.field(
        metadata={"json": "text_config.num_hidden_layers"}
    )
    n_heads: int = dataclasses.field(
        metadata={"json": "text_config.num_attention_heads"}
    )
    n_kv_groups: int = dataclasses.field(
        metadata={"json": "text_config.num_key_value_heads"}
    )
    head_dim: int | None = dataclasses.field(
        default=None, kw_only=True, metadata={"json": "text_config.head_dim"}
    )
    hidden_dim: int = dataclasses.field(
        metadata={"json": "text_config.intermediate_size"}
    )
    rope_base: float = dataclasses.field(metadata={"json": "text_config.rope_theta"})
    eps: float = dataclasses.field(
        default=1e-5, kw_only=True, metadata={"json": "text_config.rms_norm_eps"}
    )
    max_seq_len: int = dataclasses.field(
        metadata={"json": "text_config.max_position_embeddings"}
    )


class SmolVLMTextOracle(Oracle):
    """SmolVLM's text backbone's forward pass in float32, on the host."""

    def __init__(self, config, weights):
        super().__init__(config, weights, decoder=weights.model.text_model)
        self.lm_head = widen(weights.lm_head.weight)

    def head(self, x):
        norm = widen(self.decoder.norm.weight)
        return self.rms_norm(x, norm) @ self.lm_head.T


class SmolVLMText(CausalLM):
    """SmolVLM's text backbone on ``config``'s shape and a checkpoint's
    ``weights``, by its names: the decoder under ``model.text_model``, the
    untied ``lm_head`` at the root. Every matrix is read ``(out, in)``, as
    the checkpoint ships it.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = SmolVLMTextOracle

    def __init__(self, config, weights):
        super().__init__(config, weights, decoder=weights.model.text_model)
        self.lm_head = weights.lm_head.weight

    def head(self, x):
        return GEMV.step(
            self.lm_head,
            RMSNorm.step(x, weight=self.decoder.norm.weight, epsilon=self.config.eps),
        )


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
    return Tokenizer(HFTokenizer.from_file(str(path)))


#: ``<|im_start|>``, the turn marker every prompt starts with.
BOS = 1


class Runner(lm.Runner):
    """SmolVLM-256M-Instruct's text backbone, from its checkpoint and
    ``tokenizer.json`` (text-only: no image input yet).
    """

    config = SmolVLMTextConfig
    model = SmolVLMText
    open_tokenizer = staticmethod(tokenizer)
    bos = BOS


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
# tiles (module docstring: out of scope).
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

    def __init__(self, config, weights, vision_config: VisionConfig):
        super().__init__(config, weights)
        self.vision = VisionTower(vision_config, weights)
        self.combined = iron.state((config.prefill_chunk, config.emb_dim))

    def embed(self, x, pixel_values, rows):
        if pixel_values is None:
            return x
        # x is bounded to rows (ids[:rows]'s Extent); copying it into a
        # scratch state bound the same way keeps that bound (an unbounded
        # destination does not: it copies the whole chunk, a real compute
        # and buffer-descriptor cost). The image's own fixed rows (always
        # within the real prompt's valid length: the image is always
        # first) overwrite after, a plain slice of the now-unbounded-again
        # scratch buffer.
        features = self.vision(pixel_values)
        Copy.step(x, self.combined[:rows])
        Copy.step(
            features, self.combined[IMAGE_PREAMBLE : IMAGE_PREAMBLE + IMAGE_TOKENS]
        )
        return self.combined[:rows]

    def body(
        self,
        ids=None,
        pixel_values=None,
        *,
        token: Carried[np.int32],
        position: Carried[np.int32],
        chunk: Scratchpad[np.int32],
        rows: Scratchpad[np.int32],
    ):
        """``CausalLM.body``, with ``pixel_values`` threaded to ``embed()``:
        the one thing the base class's ``embed(x)`` (no second argument)
        cannot pass through. Deletes once ``iron.lm.Multimodal`` gives every
        multimodal model this hook generically.
        """
        c = self.config
        L, C, A = c.max_seq_len, c.prefill_chunk, c.rope_width
        prompt = ids is not None
        embedding = iron.weight(self.decoder.embed_tokens.weight)
        if prompt:
            x = Copy.step(embedding[ids[:rows]])
            angles = Copy.step(self.rope.reshape(L // C, C, A)[chunk, :rows])
        else:
            x = Copy.step(embedding[token]).reshape(1, c.emb_dim)
            angles = Copy.step(self.rope[position]).reshape(1, A)
        x = self.embed(x, pixel_values, rows)
        step = DecodeStep(prompt, angles, chunk, rows, position)
        for i, weights in enumerate(self.layers):
            x = self.layer(step, i, weights, x)
        if prompt:
            x = Copy.step(x[rows - 1]).reshape(
                1, c.emb_dim
            )  # the last row's logits alone
        logits = self.head(x)
        _, drawn = Sample.step(
            logits.reshape(c.vocab_size),
            self.draws,
            self.drawn,
            row=position * ROW_WORDS,
            at=position,
        )
        return logits, iron.carry(token=drawn, position=position + 1)

    def shapes(self) -> list[dict]:
        versions = super().shapes()
        # Only the prompt chunk (version 1) ever carries an image: it is
        # always the first thing in the turn.
        versions[1] = dict(versions[1], pixel_values=((512, 512 * 3), bfloat16))
        return versions


class SmolVLMOracle(SmolVLMTextOracle):
    """SmolVLM's forward pass in float32, on the host, the vision tower
    spliced in the same way ``SmolVLM`` is.
    """

    def __init__(self, config, weights, vision_config: VisionConfig):
        super().__init__(config, weights)
        self.vision = VisionOracle(vision_config, weights)

    def embed(self, x, pixel_values=None):
        if pixel_values is None:
            return x
        features = self.vision.soft_tokens(pixel_values)
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
        self.vision_config = VisionConfig.from_checkpoint(weights_path)

    def npu(self, cost_table=None, full_elf=None, kinds=None):
        model = SmolVLM(self.config, self.weights, self.vision_config)
        tuner = (
            None
            if cost_table is None
            else JointNarrowing(CostTable(cost_table), kinds=kinds or NarrowingKinds())
        )
        return model.load(
            release=self.checkpoint.release, tuner=tuner, full_elf=full_elf
        )

    def oracle(self):
        return SmolVLMOracle(self.config, self.weights, self.vision_config)


if __name__ == "__main__":
    lm.main(Runner, "SmolVLM-256M-Instruct's text backbone on the NPU")
