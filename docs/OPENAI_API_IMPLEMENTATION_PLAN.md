<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# OpenAI-Compatible API Implementation Plan for IRON

## Executive Summary

This document outlines the implementation of an OpenAI-compatible API server for IRON that:
1. **Automatically downloads and converts** HuggingFace models (no manual conversion needed)
2. **Caches converted models** for subsequent requests
3. **Serves OpenAI-compatible endpoints** (`/v1/chat/completions`, `/v1/models`, etc.)
4. **Supports streaming responses** via Server-Sent Events (SSE)

## Current State Analysis

### What Already Works

1. **Weight Format**: IRON already uses `.safetensors` - the optimal format
   - Safe (no arbitrary code execution)
   - Fast loading (memory-mapped)
   - Standard HuggingFace format

2. **Model Conversion Pipeline** (`iron/model_convert/`):
   - `HuggingFaceConverter` - Main conversion API
   - `WeightMapper` - Maps HF names to IRON names
   - `ModelAssembler` - Assembles complete models
   - `OperatorFactory` - Creates AIE operators

3. **Reference Application** (`iron/applications/llama_3.2_1b/`):
   - Working inference with safetensors loading
   - AIE operator compilation and execution

### What's Missing

1. **No API Server Layer** - IRON has no FastAPI/Flask server
2. **No Automatic Conversion** - Users must manually convert models
3. **No Model Cache/Registry** - No tracking of converted models
4. **No OpenAI Endpoints** - No `/v1/chat/completions`, `/v1/models`, etc.

## Implementation Plan

### Phase 1: Model Registry and Auto-Conversion

**Goal**: Users specify a HuggingFace model name, system handles everything automatically.

#### 1.1 Model Registry (`iron/api/model_registry.py`)

```python
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime
import json

@dataclass
class ModelEntry:
    """Represents a converted model in the registry"""
    model_id: str  # User-facing ID (e.g., "meta-llama/Llama-3.2-1B")
    iron_name: str  # Internal IRON name
    status: str  # "pending", "converting", "ready", "error"
    architecture: str
    hidden_size: int
    num_layers: int
    vocab_size: int
    converted_at: Optional[datetime] = None
    error_message: Optional[str] = None
    last_used: Optional[datetime] = None
    use_count: int = 0

class ModelRegistry:
    """Manages converted models and their lifecycle"""

    def __init__(self, cache_dir: str = "~/.cache/iron/models"):
        self.cache_dir = Path(cache_dir).expanduser()
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.models: Dict[str, ModelEntry] = {}
        self._load_registry()

    def get_model_path(self, model_id: str) -> Path:
        """Get path to converted model cache"""
        safe_name = model_id.replace("/", "__")
        return self.cache_dir / safe_name

    def register_model(self, model_id: str) -> ModelEntry:
        """Register a new model for conversion"""
        entry = ModelEntry(
            model_id=model_id,
            iron_name=model_id,
            status="pending",
            architecture="unknown",
            hidden_size=0,
            num_layers=0,
            vocab_size=0,
        )
        self.models[model_id] = entry
        self._save_registry()
        return entry

    def update_status(self, model_id: str, status: str, error: Optional[str] = None):
        """Update model conversion status"""
        if model_id in self.models:
            entry = self.models[model_id]
            entry.status = status
            if status == "ready":
                entry.converted_at = datetime.now()
            if error:
                entry.error_message = error
            self._save_registry()
```

#### 1.2 Auto-Converter (`iron/api/auto_converter.py`)

```python
from ..model_convert import HuggingFaceConverter, ConversionConfig
from .model_registry import ModelRegistry, ModelEntry
import logging

logger = logging.getLogger(__name__)

class AutoConverter:
    """Automatically downloads and converts HuggingFace models"""

    def __init__(self, registry: ModelRegistry):
        self.registry = registry

    def convert_model(self, model_id: str) -> ModelEntry:
        """
        Convert a HuggingFace model to IRON format.

        Flow:
        1. Check if already converted in cache
        2. If not, download from HF Hub
        3. Convert weights to IRON format
        4. Save to cache
        5. Return ModelEntry
        """
        entry = self.registry.get(model_id)

        # Check cache first
        model_path = self.registry.get_model_path(model_id)
        if model_path.exists() and (model_path / "iron_config.json").exists():
            logger.info(f"Model {model_id} already converted in cache")
            entry.status = "ready"
            return entry

        # Start conversion
        entry.status = "converting"
        self.registry.update(entry)

        try:
            # Create converter (downloads config from HF if needed)
            converter = HuggingFaceConverter(model_id)

            # Convert weights to cache
            converter.convert_weights(output_dir=str(model_path))

            # Export config
            converter.export_config(str(model_path / "iron_config.json"))

            # Update registry
            entry.architecture = converter.norm_config.architecture.value
            entry.hidden_size = converter.norm_config.hidden_size
            entry.num_layers = converter.norm_config.num_hidden_layers
            entry.vocab_size = converter.norm_config.vocab_size
            entry.status = "ready"

        except Exception as e:
            entry.status = "error"
            entry.error_message = str(e)
            raise

        self.registry.update(entry)
        return entry
```

### Phase 2: OpenAI-Compatible Server

#### 2.1 Server Main (`iron/api/server.py`)

```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union
import asyncio
import time
import json

app = FastAPI(
    title="IRON API",
    description="OpenAI-compatible API for AMD Ryzen AI NPU",
    version="1.0.0",
)

# Global state
model_registry = None
auto_converter = None
loaded_models: Dict[str, Any] = {}  # model_id -> ModelAssembler

# ============================================================================
# Request/Response Models (OpenAI-compatible)
# ============================================================================

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    temperature: Optional[float] = 1.0
    top_p: Optional[float] = 1.0
    max_tokens: Optional[int] = None
    max_completion_tokens: Optional[int] = None
    stop: Optional[Union[str, List[str]]] = None
    stream: Optional[bool] = False
    n: Optional[int] = 1

class UsageInfo(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

class ChatCompletionResponseChoice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: Optional[str] = None

class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[ChatCompletionResponseChoice]
    usage: UsageInfo

class StreamingChoice(BaseModel):
    index: int
    delta: Dict[str, str]
    finish_reason: Optional[str] = None

# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/v1/models")
async def list_models():
    """List available models (OpenAI-compatible)"""
    models = []
    for model_id, entry in model_registry.models.items():
        if entry.status == "ready":
            models.append({
                "id": model_id,
                "object": "model",
                "created": int(entry.converted_at.timestamp()),
                "owned_by": "iron",
                "architecture": entry.architecture,
            })
    return {"data": models}

@app.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    """
    Create chat completion (OpenAI-compatible)

    Supports both streaming and non-streaming responses.
    """
    model_id = request.model

    # Auto-convert model if needed
    if model_id not in loaded_models:
        try:
            await convert_and_load_model(model_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to load model: {str(e)}")

    model = loaded_models[model_id]

    # Convert messages to prompt
    prompt = messages_to_prompt(request.messages)

    # Tokenize
    input_ids = tokenize(prompt)
    prompt_tokens = len(input_ids[0])

    if request.stream:
        return StreamingResponse(
            stream_completion(model, input_ids, request),
            media_type="text/event-stream",
        )
    else:
        # Non-streaming
        output_ids = await generate_tokens(
            model,
            input_ids,
            max_tokens=request.max_completion_tokens or request.max_tokens or 100,
            temperature=request.temperature,
            top_p=request.top_p,
            stop=request.stop,
        )

        completion_tokens = len(output_ids[0]) - prompt_tokens
        text = detokenize(output_ids[0][prompt_tokens:])

        return ChatCompletionResponse(
            id=f"chatcmpl-{int(time.time())}",
            created=int(time.time()),
            model=model_id,
            choices=[{
                "index": 0,
                "message": {"role": "assistant", "content": text},
                "finish_reason": "stop",
            }],
            usage=UsageInfo(
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=prompt_tokens + completion_tokens,
            ),
        )

@app.post("/v1/completions")
async def completions(request: dict):
    """Legacy completions endpoint (OpenAI-compatible)"""
    # Similar to chat_completions but for /completions endpoint
    ...

# ============================================================================
# Helper Functions
# ============================================================================

async def convert_and_load_model(model_id: str):
    """Download, convert, and load a model"""
    global loaded_models

    # Get model path from registry
    model_path = model_registry.get_model_path(model_id)

    # Check if already converted
    if not model_path.exists():
        # Trigger conversion
        auto_converter.convert_model(model_id)

    # Load model into memory
    from iron.model_convert import create_model

    assembler = create_model(
        config_path=model_path / "iron_config.json",
        weights_path=model_path,
    )

    # Compile AIE artifacts
    assembler.compile_artifacts()

    loaded_models[model_id] = assembler

def messages_to_prompt(messages: List[ChatMessage]) -> str:
    """Convert chat messages to model-specific prompt format"""
    # Implementation depends on model (Llama, Mistral, etc.)
    # For Llama-3:
    prompt = "<|begin_of_text|>"
    for msg in messages:
        prompt += f"<|start_header_id|>{msg.role}<|end_header_id|>\n\n{msg.content}<|eot_id|>"
    prompt += "<|start_header_id|>assistant<|end_header_id|>\n\n"
    return prompt

async def stream_completion(model, input_ids, request: ChatCompletionRequest):
    """Generate streaming response using SSE"""
    max_tokens = request.max_completion_tokens or request.max_tokens or 100

    # Stream tokens one by one
    generated_tokens = []
    for token in generate_tokens_streamed(model, input_ids, max_tokens):
        text = detokenize([token])
        generated_tokens.append(text)

        # Send SSE chunk
        chunk = {
            "id": f"chatcmpl-{int(time.time())}",
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": request.model,
            "choices": [{
                "index": 0,
                "delta": {"content": text},
                "finish_reason": None,
            }],
        }
        yield f"data: {json.dumps(chunk)}\n\n"

    # Final chunk
    final_chunk = {
        "id": f"chatcmpl-{int(time.time())}",
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": request.model,
        "choices": [{
            "index": 0,
            "delta": {},
            "finish_reason": "stop",
        }],
    }
    yield f"data: {json.dumps(final_chunk)}\n\n"
    yield "data: [DONE]\n\n"
```

#### 2.2 Server CLI (`iron/api/cli.py`)

```python
#!/usr/bin/env python3
"""
IRON API Server CLI

Usage:
    python -m iron.api --host 0.0.0.0 --port 8000
    python -m iron.api --model meta-llama/Llama-3.2-1B
"""

import argparse
import uvicorn
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="IRON API Server")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    parser.add_argument("--model", help="Pre-load a model on startup")
    parser.add_argument("--cache-dir", default="~/.cache/iron/models", help="Model cache directory")
    parser.add_argument("--workers", type=int, default=1, help="Number of worker processes")
    args = parser.parse_args()

    print(f"Starting IRON API server on {args.host}:{args.port}")
    print(f"Model cache: {args.cache_dir}")

    uvicorn.run(
        "iron.api.server:app",
        host=args.host,
        port=args.port,
        workers=args.workers,
    )

if __name__ == "__main__":
    main()
```

### Phase 3: Integration and Testing

#### 3.1 Testing with OpenAI Python Client

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed",  # IRON doesn't require API key
)

# Chat completion
response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-1B",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ],
    max_tokens=100,
)

print(response.choices[0].message.content)

# Streaming
stream = client.chat.completions.create(
    model="meta-llama/Llama-3.2-1B",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

## File Structure

```
iron/api/
├── __init__.py           # Package exports
├── server.py             # FastAPI server with OpenAI endpoints
├── cli.py                # CLI for starting server
├── model_registry.py     # Model cache and registry
├── auto_converter.py     # Automatic HF model conversion
├── tokenizers.py         # Tokenizer utilities
└── test/
    └── test_server.py    # Server tests
```

## Dependencies

Add to `requirements.txt`:
```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.0.0
sse-starlette>=1.6.0  # For SSE streaming
```

## Conv3D Integration Notes

**Conv3D is NOT required for basic LLM serving.** It serves two purposes:

1. **Video Models**: Conv3D for spatiotemporal convolution
2. **Compute Primitive**: Advanced attention patterns via shape manipulation

For OpenAI API server implementation:
- Conv3D can be added later as an optional operator
- Focus on GEMM, GEMV, RMSNorm, RoPE, MHA first
- Conv3D integration would require specific model architecture support

## Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Safetensors Support | ✅ Already Complete | Default format in IRON |
| Weight Mapper | ✅ Already Complete | Maps HF names to IRON |
| Model Assembler | ✅ Already Complete | Assembles NPU models |
| Model Registry | 📋 To Implement | Track converted models |
| Auto-Converter | 📋 To Implement | Download + convert from HF |
| OpenAI API Server | 📋 To Implement | FastAPI with endpoints |
| Streaming Support | 📋 To Implement | SSE for token streaming |
| Model Caching | 📋 To Implement | Store converted models |

## Next Steps

1. Create `iron/api/` directory structure
2. Implement `model_registry.py`
3. Implement `auto_converter.py`
4. Implement `server.py` with OpenAI endpoints
5. Add CLI (`cli.py`)
6. Write tests
7. Update documentation

<p align="center">
Copyright&copy; 2025 Advanced Micro Devices, Inc
</p>
