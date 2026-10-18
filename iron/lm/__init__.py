# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Language models on IRON's operators: what every model shares. The models
themselves are applications over it, each a package of
``iron/applications/``; nothing in the library imports a model, and
``generation`` and ``testing`` need nothing of one but ``logits(tokens)``.
"""

from .checkpoint import Checkpoint
from .config import Config, DecoderConfig, not_json, rope_angles
from .model import Model, OnHost, Tokenizer, prompt_text
from .cli import main
from .blocks import (
    MLP,
    Attention,
    ConcatChannels,
    Conv1d,
    Conv2d,
    CrossDecoderLayer,
    DecoderLayer,
    ImagePatches,
    LogMel,
    MaxPool2d,
    Norm,
    filterbank,
)
from .causal import CausalLM, Checkpoints, DecodeStep
from .encoder import EncodeStep, Encoder, Tower
from .encoder_decoder import EncoderDecoder
from .golden import Golden, HuggingFace
from .generation import Sampler, accuracy, determinism, generate_on_host
from .multimodal import Multimodal

__all__ = [
    "Attention",
    "CrossDecoderLayer",
    "DecoderLayer",
    "MLP",
    "Norm",
    "CausalLM",
    "Checkpoint",
    "Checkpoints",
    "ConcatChannels",
    "Config",
    "Conv1d",
    "Conv2d",
    "DecodeStep",
    "DecoderConfig",
    "EncodeStep",
    "Encoder",
    "EncoderDecoder",
    "Golden",
    "HuggingFace",
    "ImagePatches",
    "LogMel",
    "MaxPool2d",
    "Model",
    "Multimodal",
    "OnHost",
    "Sampler",
    "Tokenizer",
    "Tower",
    "accuracy",
    "determinism",
    "filterbank",
    "generate_on_host",
    "main",
    "not_json",
    "prompt_text",
    "rope_angles",
]
