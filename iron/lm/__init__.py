# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Language models on IRON's operators: what every model shares. The models
themselves are applications over it, each a package of
``iron/applications/``; nothing in the library imports a model, and
``generation`` and ``testing`` need nothing of one but ``logits(tokens)``.
"""

from .checkpoint import Checkpoint
from .config import Config, DecoderConfig, not_json, rope_angles
from .model import Model, OnHost, Tokenizer, TokenizerJson, prompt_text
from .cli import main
from .blocks import (
    MLP,
    AttentionSpec,
    Conv1d,
    CrossDecoderLayer,
    DecoderLayerSpec,
    Embedding,
    ImagePatches,
    LayerNorm,
    Linear,
    LogMel,
    Norm,
    RMSNorm,
    filterbank,
)
from iron.common.feature_map import ConcatChannels, Conv2d, MaxPool2d
from .causal import CausalLM, Checkpoints, DecodeStep
from .encoder import EncodeStep, Encoder, Tower
from .encoder_decoder import EncoderDecoder
from .golden import Golden, HuggingFace
from .generation import Sampler, accuracy, determinism, generate_on_host
from .multimodal import Multimodal

__all__ = [
    "AttentionSpec",
    "CrossDecoderLayer",
    "DecoderLayerSpec",
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
    "Embedding",
    "Golden",
    "HuggingFace",
    "ImagePatches",
    "LayerNorm",
    "Linear",
    "LogMel",
    "MaxPool2d",
    "Model",
    "Multimodal",
    "OnHost",
    "RMSNorm",
    "Sampler",
    "Tokenizer",
    "TokenizerJson",
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
