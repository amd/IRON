# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Language models on IRON's operators: what every decoder shares, and one
package per model (``llama3``).

A model is five things over this package:

* its ``Config``, the shape;
* a ``CausalLM``, the decoder on the NPU as one graph (prefill and
  decode, the caches, attention over them and ``logits(tokens)``), to
  which it gives its ``layer`` and ``head``, built from ``layers``
  (``project``, a weight's projection at either row count, and
  ``swiglu``, the SwiGLU feed-forward);
* an ``Oracle``, the same decoder's float32 forward pass on the host
  that it is judged by, to which it gives the same ``layer`` and ``head``
  in numpy;
* its checkpoint ``Layout``, each weight's place in the model, its name
  in the ``.safetensors`` file and its shape (``checkpoint``);
* a ``Runner``, which opens the checkpoint and the tokenizer and
  builds the model and its oracle; ``main`` is its command line.

Sampling and the generation, accuracy and determinism loops
(``generation``), and what a model's device test checks
(``testing``), need nothing of a model but ``logits(tokens)``.

A model's package holds what is its alone: those five, its tokenizer and
its profiles. Nothing in the library imports a model, so one can be
replaced or deleted on its own.
"""

from .checkpoint import (
    Checkpoint,
    Layout,
    checkpoint_shapes,
    load_weights,
    random_weights,
    unread_weights,
)
from .decoder import (
    CausalLM,
    Config,
    DecodeAttention,
    Oracle,
    RopeScaling,
    Step,
    rope_angles,
)
from .generation import SEED, Sampler, accuracy, determinism, generate, greedy
from .layers import SwiGLU, project, swiglu
from .runner import Runner, main

__all__ = [
    "SEED",
    "CausalLM",
    "Checkpoint",
    "Config",
    "DecodeAttention",
    "Layout",
    "Oracle",
    "RopeScaling",
    "Runner",
    "Sampler",
    "Step",
    "SwiGLU",
    "accuracy",
    "checkpoint_shapes",
    "determinism",
    "generate",
    "greedy",
    "load_weights",
    "main",
    "project",
    "random_weights",
    "rope_angles",
    "swiglu",
    "unread_weights",
]
