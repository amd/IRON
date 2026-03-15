# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON API - OpenAI-compatible API server for AMD Ryzen AI NPU

This package provides:
- Auto-conversion of HuggingFace models to IRON format
- OpenAI-compatible API endpoints (/v1/chat/completions, /v1/models, etc.)
- Streaming support via Server-Sent Events (SSE)
- Model caching for fast subsequent loads

Usage:
    # Start server
    python -m iron.api --host 0.0.0.0 --port 8000

    # Or use the CLI entry point
    iron-server --host 0.0.0.0 --port 8000

    # Pre-load a model
    iron-server --model meta-llama/Llama-3.2-1B --preload
"""

from .auto_converter import AutoConverter
from .model_registry import ModelRegistry, ModelEntry
from .tokenizers import (
    TokenizerWrapper,
    get_tokenizer,
    messages_to_prompt,
    tokenize,
    detokenize,
)

__all__ = [
    # Core classes
    "AutoConverter",
    "ModelRegistry",
    "ModelEntry",
    # Tokenizers
    "TokenizerWrapper",
    "get_tokenizer",
    "messages_to_prompt",
    "tokenize",
    "detokenize",
]
