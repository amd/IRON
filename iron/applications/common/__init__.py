# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What every language model application shares.

* :mod:`.model` -- :class:`CausalLM`, a decoder as one graph: prefill and
  decode, the caches, attention over them and ``logits(tokens)``; a model
  gives its ``layer`` and ``head``, and its :class:`Oracle`, the float32
  forward pass on the host it is judged by, its ``layer`` and ``head`` in
  numpy. :func:`project` is a weight's projection at either row count.
* :mod:`.checkpoint` -- the mapped ``.safetensors`` file and the weight
  tree a model's layout places its tensors in.
* :mod:`.generation` -- sampling, and the generation, accuracy and
  determinism loops over any model with ``logits(tokens)``.
* :mod:`.runner` -- :class:`Runner`, which builds a model and its oracle
  from a checkpoint, and the command line.
* :mod:`.testing` -- what an application's device test checks.
"""

from .checkpoint import Checkpoint, Layout, checkpoint_shapes, load_weights
from .generation import SEED, Sampler, accuracy, determinism, generate, greedy
from .model import CausalLM, Config, Oracle, Step, project, prompt_rows
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
