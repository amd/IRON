# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""IRON model architectures package.

This package provides model configurations, weight loaders, and registry
for supported model architectures including Llama3.2.

Modules:
    registry: Model registry for supported architectures
    llama32: Llama3.2 model implementation

Example:
    >>> from iron.models import Llama32Config, ModelRegistry
    >>> config = Llama32Config.from_pretrained("meta-llama/Llama-3.2-1B")
    >>> print(config.hidden_size)
    2048
"""

from iron.models.registry import ModelRegistry, ModelSpec
from iron.models.llama32.config import Llama32Config
from iron.models.llama32.weights import LlamaWeights, TransformerWeights

__all__ = [
    # Registry
    "ModelRegistry",
    "ModelSpec",
    # Llama3.2
    "Llama32Config",
    "LlamaWeights",
    "TransformerWeights",
]

__version__ = "1.0.0"
