# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Language models on IRON's operators: what every model shares. The models
themselves are applications over it, each a package of
``iron/applications/`` (``llama``, ``embedding_gemma2``).

* ``base``: a model's ``Config`` (``eps`` and ``from_checkpoint``, built from
  a checkpoint's own ``config.json``) and the ``Checkpoint`` it is read from,
  whose ``tree()`` is its weights by their own names; ``DecoderConfig``, a
  decoder's own shape; ``Oracle``, the float32 forward pass on the host a
  model is judged by (``rms_norm``, ``gelu_tanh``, ``attend(causal=,
  window=)`` and ``rotate``, shared with every model's own oracle);
  ``Model``, a graph whose versions ``load()`` compiles up front; and
  ``Runner``, which opens a decoder's checkpoint and tokenizer and builds
  it and its oracle (``main`` is its command line).
* ``causal``: ``CausalLM``, a decoder on the NPU as one graph (prefill and
  decode, the caches, attention over them and ``logits(tokens)``), to
  which a model gives its ``layer`` and ``head``; ``DecodeStep``, a call's
  per-call values.
* ``encoder``: ``Encoder``, a bidirectional encoder compiled once for every
  length.
* ``blocks``: what layers are built from: ``project``, a weight's
  projection at either row count, and ``SwiGLU``, the feed-forward as a
  graph of its own; and ``Block``, the attention + SwiGLU layer a
  Llama-style model mixes in on the NPU. EmbeddingGemma 2's own Gemma-shaped
  blocks (the GELU-gated feed-forward, sandwich norms and an encoder's
  attention) are its application's, not the library's.

Sampling and the generation, accuracy and determinism loops
(``generation``), and what a model's device test checks
(``testing``), need nothing of a model but ``logits(tokens)``.

Nothing in the library imports a model, so one can be replaced or deleted
on its own.
"""

from .base import (
    Checkpoint,
    Config,
    DecoderConfig,
    Model,
    Oracle,
    Runner,
    main,
    prompt_text,
    rope_angles,
    widen,
)
from .blocks import (
    Block,
    ConcatChannels,
    Conv1d,
    Conv2d,
    ImagePatches,
    LogMel,
    MaxPool2d,
    SwiGLU,
    filterbank,
    project,
)
from .causal import CausalLM, DecodeStep
from .encoder import Encoder
from .generation import Sampler, accuracy, determinism, generate_on_host

__all__ = [
    "Block",
    "CausalLM",
    "Checkpoint",
    "ConcatChannels",
    "Config",
    "Conv1d",
    "Conv2d",
    "DecodeStep",
    "DecoderConfig",
    "Encoder",
    "ImagePatches",
    "LogMel",
    "MaxPool2d",
    "Model",
    "Oracle",
    "Runner",
    "Sampler",
    "SwiGLU",
    "accuracy",
    "determinism",
    "filterbank",
    "generate_on_host",
    "main",
    "project",
    "prompt_text",
    "rope_angles",
    "widen",
]
