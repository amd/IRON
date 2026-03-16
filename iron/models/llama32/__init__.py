# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Llama3.2 model implementation package.

This package provides configuration, weight loading, and model
implementation for Meta's Llama3.2 family of models.

Modules:
    config: Llama32Config dataclass for model configuration
    weights: LlamaWeights and TransformerWeights dataclasses
    loader: WeightLoader for downloading and loading weights

Example:
    >>> from iron.models.llama32 import Llama32Config, WeightLoader
    >>> config = Llama32Config.from_pretrained("meta-llama/Llama-3.2-1B")
    >>> loader = WeightLoader()
    >>> model_path = loader.download_model("meta-llama/Llama-3.2-1B")
"""

from iron.models.llama32.config import Llama32Config
from iron.models.llama32.weights import LlamaWeights, TransformerWeights
from iron.models.llama32.loader import WeightLoader, WeightInfo

__all__ = [
    "Llama32Config",
    "LlamaWeights",
    "TransformerWeights",
    "WeightLoader",
    "WeightInfo",
]

__version__ = "1.0.0"
