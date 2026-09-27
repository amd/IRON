# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Language models on IRON's operators: what every decoder shares, and one
package per model (:mod:`.llama3`).

A model is five things over this package:

* its :class:`Config`, the shape;
* a :class:`CausalLM`, the decoder on the NPU as one graph (prefill and
  decode, the caches, attention over them and ``logits(tokens)``), to
  which it gives its ``layer`` and ``head``; :func:`project` is a weight's
  projection at either row count;
* an :class:`Oracle`, the same decoder's float32 forward pass on the host
  that it is judged by, to which it gives the same ``layer`` and ``head``
  in numpy;
* its checkpoint :data:`Layout`, each weight's place in the model, its name
  in the ``.safetensors`` file and its shape (:mod:`.checkpoint`);
* a :class:`Runner`, which opens the checkpoint and the tokenizer and
  builds the model and its oracle; :func:`main` is its command line.

Sampling and the generation, accuracy and determinism loops
(:mod:`.generation`), and what a model's device test checks
(:mod:`.testing`), need nothing of a model but ``logits(tokens)``.

A model's package holds what is its alone: those five, its tokenizer and
its profiles. Nothing in the library imports a model, so one can be
replaced or deleted on its own.
"""

from .checkpoint import Checkpoint, Layout, checkpoint_shapes, load_weights
from .decoder import CausalLM, Config, Oracle, Step, project, prompt_rows
from .generation import SEED, Sampler, accuracy, determinism, generate, greedy
from .runner import Runner, main

__all__ = [
    "SEED",
    "CausalLM",
    "Checkpoint",
    "Config",
    "Layout",
    "Oracle",
    "Runner",
    "Sampler",
    "Step",
    "accuracy",
    "checkpoint_shapes",
    "determinism",
    "generate",
    "greedy",
    "load_weights",
    "main",
    "project",
    "prompt_rows",
]
