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
    Tokenizer,
    main,
    prompt_text,
    rope_angles,
    widen,
)
from .blocks import (
    ConcatChannels,
    Conv1d,
    Conv2d,
    Experts,
    ImagePatches,
    Layer,
    LogMel,
    Mamba2,
    MaxPool2d,
    filterbank,
)
from .causal import CausalLM, Checkpoints, DecodeStep
from .encoder import EncodeStep, Encoder, Tower
from .encoder_decoder import EncoderDecoder, EncoderDecoderOracle
from .generation import Sampler, accuracy, determinism, generate_on_host
from .multimodal import Multimodal

__all__ = [
    "CausalLM",
    "Checkpoint",
    "Checkpoints",
    "ConcatChannels",
    "Config",
    "Conv1d",
    "Conv2d",
    "DecodeStep",
    "DecoderConfig",
    "Derived",
    "EncodeStep",
    "Encoder",
    "EncoderDecoder",
    "EncoderDecoderOracle",
    "Experts",
    "ImagePatches",
    "Layer",
    "LogMel",
    "Mamba2",
    "MaxPool2d",
    "Model",
    "Multimodal",
    "Oracle",
    "Runner",
    "Sampler",
    "Tokenizer",
    "Tower",
    "accuracy",
    "determinism",
    "filterbank",
    "generate_on_host",
    "main",
    "prompt_text",
    "rope_angles",
    "widen",
]
