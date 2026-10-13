# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Language models on IRON's operators: what every model shares. The models
themselves are applications over it, each a package of
``iron/applications/`` (``llama``, ``embedding_gemma2``).

* ``base``: a model's ``Config``, its checkpoint ``Layout`` (each weight's
  place in the model, its name in the ``.safetensors`` file and its shape)
  and the ``Checkpoint`` it is read from; ``Oracle``, the float32 forward
  pass on the host a model is judged by; ``Model``, a graph whose versions
  ``load()`` compiles up front; and ``Runner``, which opens a decoder's
  checkpoint and tokenizer and builds it and its oracle (``main`` is its
  command line).
* ``causal``: ``CausalLM``, a decoder on the NPU as one graph (prefill and
  decode, the caches, attention over them and ``logits(tokens)``), to
  which a model gives its ``layer`` and ``head``.
* ``encoder``: ``Encoder``, a bidirectional encoder compiled once for every
  length, and the sandwich layer EmbeddingGemma 2's towers share.
* ``blocks``: what layers are built from: ``project``, a weight's
  projection at either row count, the SwiGLU and GELU-gated feed-forwards,
  sandwich norms and an encoder's attention; and ``Block``/``BlockOracle``,
  the attention + SwiGLU layer a Llama-style model mixes in.

Sampling and the generation, accuracy and determinism loops
(``generation``), and what a model's device test checks
(``testing``), need nothing of a model but ``logits(tokens)``.

Nothing in the library imports a model, so one can be replaced or deleted
on its own.
"""

from .base import (
    Checkpoint,
    Config,
    Layout,
    Model,
    Oracle,
    RopeScaling,
    Runner,
    checkpoint_shapes,
    load_weights,
    main,
    random_weights,
    rope_angles,
    unread_weights,
    widen,
)
from .blocks import (
    Block,
    BlockOracle,
    ConcatChannels,
    Conv1d,
    Conv2d,
    ImagePatches,
    LogMel,
    MaxPool2d,
    SwiGLU,
    attention,
    filterbank,
    geglu,
    project,
    rms_norm,
    sandwich,
    swiglu,
)
from .causal import CausalLM, Step
from .encoder import Encoder, sandwich_layer
from .generation import SEED, Sampler, accuracy, determinism, generate, greedy

__all__ = [
    "SEED",
    "Block",
    "BlockOracle",
    "CausalLM",
    "Checkpoint",
    "ConcatChannels",
    "Config",
    "Conv1d",
    "Conv2d",
    "Encoder",
    "ImagePatches",
    "Layout",
    "LogMel",
    "MaxPool2d",
    "Model",
    "Oracle",
    "RopeScaling",
    "Runner",
    "Sampler",
    "Step",
    "SwiGLU",
    "accuracy",
    "attention",
    "checkpoint_shapes",
    "determinism",
    "filterbank",
    "geglu",
    "generate",
    "greedy",
    "load_weights",
    "main",
    "project",
    "random_weights",
    "rms_norm",
    "rope_angles",
    "sandwich",
    "sandwich_layer",
    "swiglu",
    "unread_weights",
    "widen",
]
