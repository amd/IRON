# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Language models on IRON's operators: what every model shares. The models
themselves are applications over it, each a package of
``iron/applications/``; nothing in the library imports a model, and
``generation`` and ``testing`` need nothing of one but ``logits(tokens)``.
"""

from .base import (
    Checkpoint,
    Config,
    DecoderConfig,
    Derived,
    Model,
    Oracle,
    Runner,
    main,
    prompt_text,
    rope_angles,
    widen,
)
from .blocks import (
    ConcatChannels,
    Conv1d,
    Conv2d,
    ImagePatches,
    Layer,
    LogMel,
    MaxPool2d,
    filterbank,
    project,
)
from .causal import CausalLM, DecodeStep
from .encoder import Encoder
from .generation import Sampler, accuracy, determinism, generate_on_host

__all__ = [
    "CausalLM",
    "Checkpoint",
    "ConcatChannels",
    "Config",
    "Conv1d",
    "Conv2d",
    "DecodeStep",
    "DecoderConfig",
    "Derived",
    "Encoder",
    "ImagePatches",
    "Layer",
    "LogMel",
    "MaxPool2d",
    "Model",
    "Oracle",
    "Runner",
    "Sampler",
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
