# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""
IRON Generation Package - Autoregressive Text Generation.

This package provides components for autoregressive token generation
with KV cache persistence for Llama3.2 models.

FEATURES:
- Autoregressive generation loop (prefill + decode phases)
- Token sampling with temperature, top_p, top_k filtering
- KV cache persistence for context retention
- Stop condition handling (EOS, max_tokens, stop_strings)
- Streaming generation output

COMPONENTS:
- GenerationLoop: Main generation loop with prefill() and decode()
- TokenSampler: Token sampling with various strategies
- KVCacheManager: KV cache management for token-by-token generation
- StopConditionChecker: Stop condition detection and handling

EXAMPLE USAGE:
    >>> from iron.generation import GenerationLoop, TokenSampler, KVCacheManager
    >>> from iron.generation import StopConditionChecker
    >>> from iron.models.llama32 import Llama32Config, LlamaWeights
    >>> from iron.api.generation_config import GenerationConfig
    >>>
    >>> # Initialize components
    >>> config = Llama32Config.from_pretrained("meta-llama/Llama-3.2-1B")
    >>> weights = LlamaWeights.from_safetensors(model_path, config)
    >>> gen_config = GenerationConfig(temperature=0.7, max_new_tokens=512)
    >>>
    >>> # Create generation loop
    >>> loop = GenerationLoop(config, weights, gen_config)
    >>>
    >>> # Generate tokens
    >>> prompt_tokens = tokenizer.encode("Hello, how are you?")
    >>> for result in loop.generate(prompt_tokens):
    ...     print(tokenizer.decode([result.token_id]), end="")

CLASSES:
    GenerationLoop: Main autoregressive generation loop
    GenerationResult: Result from a generation step
    TokenSampler: Token sampling with temperature, top_p, top_k
    KVCacheManager: KV cache management for generation
    StopConditionChecker: Stop condition detection
    StopResult: Result of stop condition check

Author: Jordan Lee
Version: 1.0.0
"""

from __future__ import annotations

from .loop import GenerationLoop, GenerationResult
from .sampling import TokenSampler
from .kv_manager import KVCacheManager
from .stop_conditions import StopConditionChecker, StopResult

__all__ = [
    # Generation loop
    "GenerationLoop",
    "GenerationResult",
    # Sampling
    "TokenSampler",
    # KV cache management
    "KVCacheManager",
    # Stop conditions
    "StopConditionChecker",
    "StopResult",
]

__version__ = "1.0.0"
__author__ = "Jordan Lee"
