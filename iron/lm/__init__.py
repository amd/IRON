# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Language models on IRON's operators: what every model shares. The models
themselves are applications over it, each a package of
``iron/applications/``; nothing in the library imports a model, and
``generation`` and ``testing`` need nothing of one but ``logits(tokens)``.
"""

from .checkpoint import Checkpoint, subtree
from .config import Config, DecoderConfig, not_json, rope_angles
from .model import Model, OnHost, Tokenizer
from .cli import main
from .blocks import (
    MLP,
    Attention,
    BatchNorm2d,
    Conv1d,
    CrossAttention,
    CrossCache,
    CrossDecoderLayer,
    DecoderLayer,
    Embedding,
    EncoderLayer,
    GatedMLP,
    ImagePatches,
    KVCache,
    LayerNorm,
    Linear,
    LogMel,
    NoCache,
    PleLayer,
    RMSNorm,
    Rope,
    SandwichLayer,
    Weights,
    activation,
    residual_add,
)
from iron.common.feature_map import ConcatChannels, Conv2d, MaxPool2d
from .causal import Call, CausalConv1d, CausalLM, Checkpoints, Decoder
from .encoder import Encoder, Tower
from .encoder_decoder import EncoderDecoder
from .golden import Golden, HuggingFace
from .generation import Sampler, accuracy, determinism, generate_on_host
from .multimodal import Multimodal
from .session import Session

__all__ = [
    "Attention",
    "BatchNorm2d",
    "Call",
    "CausalConv1d",
    "CausalLM",
    "Checkpoint",
    "Checkpoints",
    "ConcatChannels",
    "Config",
    "Conv1d",
    "Conv2d",
    "CrossAttention",
    "CrossCache",
    "CrossDecoderLayer",
    "Decoder",
    "DecoderConfig",
    "DecoderLayer",
    "Embedding",
    "Encoder",
    "EncoderDecoder",
    "EncoderLayer",
    "GatedMLP",
    "Golden",
    "HuggingFace",
    "ImagePatches",
    "KVCache",
    "LayerNorm",
    "Linear",
    "LogMel",
    "MLP",
    "MaxPool2d",
    "Model",
    "Multimodal",
    "NoCache",
    "OnHost",
    "PleLayer",
    "RMSNorm",
    "Rope",
    "Sampler",
    "SandwichLayer",
    "Session",
    "Tokenizer",
    "Tower",
    "Weights",
    "accuracy",
    "activation",
    "determinism",
    "generate_on_host",
    "main",
    "not_json",
    "residual_add",
    "rope_angles",
    "subtree",
]
