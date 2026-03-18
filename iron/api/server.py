# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON API Server - OpenAI-compatible API for AMD Ryzen AI NPU

FastAPI server providing OpenAI-compatible endpoints:
- GET  /v1/models - List available models
- POST /v1/chat/completions - Chat completion (streaming + non-streaming)
- POST /v1/completions - Legacy completion endpoint
- GET  /health - Health check

Usage:
    python -m iron.api --host 0.0.0.0 --port 8000
    python -m iron.api --model meta-llama/Llama-3.2-1B --preload
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union, AsyncGenerator
import asyncio
import time
import json
import argparse
import uvicorn
import logging
from pathlib import Path

from .auto_converter import AutoConverter
from .model_registry import ModelRegistry
from .tokenizers import (
    get_tokenizer,
    messages_to_prompt,
    tokenize,
    detokenize,
    TokenizerWrapper,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# ============================================================================
# FastAPI Application
# ============================================================================

app = FastAPI(
    title="IRON API",
    description="OpenAI-compatible API for AMD Ryzen AI NPU",
    version="1.0.0",
)

# ============================================================================
# Global State
# ============================================================================

model_registry: Optional[ModelRegistry] = None
auto_converter: Optional[AutoConverter] = None
loaded_models: Dict[str, Any] = {}  # model_id -> ModelAssembler
loaded_tokenizers: Dict[str, TokenizerWrapper] = {}  # model_id -> TokenizerWrapper

# ============================================================================
# Request/Response Models (OpenAI-compatible)
# ============================================================================


class ChatMessage(BaseModel):
    """Chat message in OpenAI format"""

    role: str = Field(..., description="Role of the message (user, assistant, system)")
    content: str = Field(..., description="Content of the message")


class ChatCompletionRequest(BaseModel):
    """Chat completion request (OpenAI-compatible)"""

    model: str = Field(..., description="Model ID to use")
    messages: List[ChatMessage] = Field(..., description="List of chat messages")
    temperature: Optional[float] = Field(
        default=1.0, ge=0, le=2, description="Sampling temperature"
    )
    top_p: Optional[float] = Field(
        default=1.0, ge=0, le=1, description="Top-p sampling"
    )
    max_tokens: Optional[int] = Field(
        default=None, description="Maximum tokens to generate"
    )
    max_completion_tokens: Optional[int] = Field(
        default=None, description="Maximum completion tokens"
    )
    stop: Optional[Union[str, List[str]]] = Field(
        default=None, description="Stop sequences"
    )
    stream: Optional[bool] = Field(default=False, description="Enable streaming")
    n: Optional[int] = Field(default=1, description="Number of completions to generate")
    presence_penalty: Optional[float] = Field(
        default=0.0, description="Presence penalty"
    )
    frequency_penalty: Optional[float] = Field(
        default=0.0, description="Frequency penalty"
    )


class UsageInfo(BaseModel):
    """Token usage information"""

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionResponseChoice(BaseModel):
    """Chat completion response choice"""

    index: int
    message: ChatMessage
    finish_reason: Optional[str] = None


class ChatCompletionResponse(BaseModel):
    """Chat completion response (OpenAI-compatible)"""

    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[ChatCompletionResponseChoice]
    usage: UsageInfo


class StreamingChoice(BaseModel):
    """Streaming choice chunk"""

    index: int
    delta: Dict[str, str] = Field(default_factory=dict)
    finish_reason: Optional[str] = None


class ChatCompletionChunk(BaseModel):
    """Chat completion chunk (streaming)"""

    id: str
    object: str = "chat.completion.chunk"
    created: int
    model: str
    choices: List[StreamingChoice]


class ModelInfo(BaseModel):
    """Model information for /v1/models endpoint"""

    id: str
    object: str = "model"
    created: int
    owned_by: str
    architecture: Optional[str] = None


class ModelsResponse(BaseModel):
    """Response for /v1/models endpoint"""

    data: List[ModelInfo]


class HealthResponse(BaseModel):
    """Health check response"""

    status: str
    version: str
    models: List[str]
    ready: bool


# ============================================================================
# API Endpoints
# ============================================================================


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint.

    Returns server status and list of loaded models.
    """
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        models=list(loaded_models.keys()),
        ready=len(loaded_models) > 0,
    )


@app.get("/v1/models", response_model=ModelsResponse)
async def list_models():
    """
    List available models (OpenAI-compatible).

    Returns models that have been converted and cached.
    """
    models = []
    if model_registry:
        for entry in model_registry.list_models(status_filter="ready"):
            models.append(
                ModelInfo(
                    id=entry.model_id,
                    created=(
                        int(entry.converted_at.timestamp())
                        if entry.converted_at
                        else int(time.time())
                    ),
                    owned_by="iron",
                    architecture=entry.architecture,
                )
            )
    return ModelsResponse(data=models)


@app.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    """
    Create chat completion (OpenAI-compatible).

    Supports both streaming and non-streaming responses.

    Streaming: Returns Server-Sent Events (SSE) stream with token-by-token generation.
    Non-streaming: Returns complete response after generation finishes.
    """
    model_id = request.model

    # Auto-load model if needed
    if model_id not in loaded_models:
        try:
            await convert_and_load_model(model_id)
        except Exception as e:
            logger.error(f"Failed to load model {model_id}: {e}")
            raise HTTPException(
                status_code=400,
                detail=f"Failed to load model {model_id}: {str(e)}",
            )

    model = loaded_models[model_id]
    tokenizer = loaded_tokenizers.get(model_id)

    # Convert messages to prompt
    architecture = model.config.normalized_config.architecture.value
    prompt = messages_to_prompt(
        [m.dict() for m in request.messages],
        architecture=architecture,
    )

    # Tokenize
    input_ids = tokenizer.encode(prompt, return_tensors="list")
    if isinstance(input_ids, list):
        input_ids = [input_ids]  # Wrap in batch dimension
    prompt_tokens = len(input_ids[0])

    # Determine max tokens
    max_tokens = request.max_completion_tokens or request.max_tokens or 100

    if request.stream:
        return StreamingResponse(
            stream_completion(
                model=model,
                tokenizer=tokenizer,
                input_ids=input_ids,
                max_tokens=max_tokens,
                temperature=request.temperature,
                top_p=request.top_p,
                stop=request.stop,
                model_id=model_id,
            ),
            media_type="text/event-stream",
        )
    else:
        # Non-streaming: generate all tokens at once
        output_ids = await generate_tokens(
            model=model,
            input_ids=input_ids,
            max_tokens=max_tokens,
            temperature=request.temperature,
            top_p=request.top_p,
            stop=request.stop,
        )

        completion_tokens = len(output_ids[0]) - prompt_tokens
        text = detokenize(output_ids[0][prompt_tokens:], tokenizer)

        return ChatCompletionResponse(
            id=f"chatcmpl-{int(time.time())}",
            created=int(time.time()),
            model=model_id,
            choices=[
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": text},
                    "finish_reason": "stop",
                }
            ],
            usage=UsageInfo(
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=prompt_tokens + completion_tokens,
            ),
        )


@app.post("/v1/completions")
async def completions(request: dict):
    """
    Legacy completions endpoint (OpenAI-compatible).

    Similar to /v1/chat/completions but uses prompt directly instead of messages.
    """
    # Convert to ChatCompletionRequest format
    prompt = request.get("prompt", "")
    messages = [{"role": "user", "content": prompt}]

    chat_request = ChatCompletionRequest(
        model=request.get("model", ""),
        messages=messages,
        temperature=request.get("temperature", 1.0),
        top_p=request.get("top_p", 1.0),
        max_tokens=request.get("max_tokens"),
        max_completion_tokens=request.get("max_completion_tokens"),
        stop=request.get("stop"),
        stream=request.get("stream", False),
    )

    return await chat_completions(chat_request)


# ============================================================================
# Helper Functions
# ============================================================================


async def convert_and_load_model(model_id: str):
    """
    Download, convert, and load a model.

    Args:
        model_id: HuggingFace model ID
    """
    global loaded_models, loaded_tokenizers

    logger.info(f"Loading model: {model_id}")

    # Get or convert model
    entry, assembler = auto_converter.get_or_load(model_id)

    # Load tokenizer
    tokenizer = get_tokenizer(model_id)

    # Store in cache
    loaded_models[model_id] = assembler
    loaded_tokenizers[model_id] = tokenizer

    logger.info(f"Model {model_id} loaded successfully")


async def generate_tokens(
    model,
    input_ids: List[List[int]],
    max_tokens: int,
    temperature: float = 1.0,
    top_p: float = 1.0,
    stop: Optional[Union[str, List[str]]] = None,
) -> List[List[int]]:
    """
    Generate tokens using the model.

    Args:
        model: ModelAssembler instance
        input_ids: Input token IDs (batched)
        max_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        top_p: Top-p sampling
        stop: Stop sequences

    Returns:
        Generated token IDs
    """
    # Use model's generate method
    output = model.generate(
        input_ids,
        max_new_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
    )

    return output


async def stream_completion(
    model,
    tokenizer,
    input_ids: List[List[int]],
    max_tokens: int,
    temperature: float = 1.0,
    top_p: float = 1.0,
    stop: Optional[Union[str, List[str]]] = None,
    model_id: str = "",
) -> AsyncGenerator[str, None]:
    """
    Generate streaming completion using SSE.

    Args:
        model: ModelAssembler instance
        tokenizer: Tokenizer wrapper
        input_ids: Input token IDs
        max_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        stop: Stop sequences
        model_id: Model ID for response
    """
    generated_tokens = []
    stop_sequences = [stop] if isinstance(stop, str) else stop

    # Generate token by token
    current_ids = input_ids
    for _ in range(max_tokens):
        # Run single forward pass
        output = model.generate(
            current_ids,
            max_new_tokens=1,
            temperature=temperature,
            top_p=top_p,
        )

        # Get the new token
        new_token = output[0][-1]
        generated_tokens.append(new_token)

        # Decode to text
        text = tokenizer.decode([new_token])

        # Check for stop sequences
        if stop_sequences:
            should_stop = False
            for stop_seq in stop_sequences:
                if stop_seq in text:
                    should_stop = True
                    break
            if should_stop:
                break

        # Send SSE chunk
        chunk = ChatCompletionChunk(
            id=f"chatcmpl-{int(time.time())}",
            created=int(time.time()),
            model=model_id,
            choices=[
                {
                    "index": 0,
                    "delta": {"content": text},
                    "finish_reason": None,
                }
            ],
        )
        yield f"data: {chunk.model_dump_json()}\n\n"

        # Update current IDs for next iteration
        current_ids = output

    # Final chunk
    final_chunk = ChatCompletionChunk(
        id=f"chatcmpl-{int(time.time())}",
        created=int(time.time()),
        model=model_id,
        choices=[
            {
                "index": 0,
                "delta": {},
                "finish_reason": "stop",
            }
        ],
    )
    yield f"data: {final_chunk.model_dump_json()}\n\n"
    yield "data: [DONE]\n\n"


# ============================================================================
# Startup/Shutdown
# ============================================================================


@app.on_event("startup")
async def startup_event():
    """Initialize global state on startup"""
    global model_registry, auto_converter

    logger.info("Starting IRON API server...")

    # Initialize registry and converter
    model_registry = ModelRegistry()
    auto_converter = AutoConverter(registry=model_registry)

    logger.info("IRON API server ready")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("Shutting down IRON API server...")

    # Clear loaded models
    loaded_models.clear()
    loaded_tokenizers.clear()

    logger.info("IRON API server shutdown complete")


# ============================================================================
# CLI
# ============================================================================


def main():
    """CLI entry point for running the server"""
    parser = argparse.ArgumentParser(description="IRON API Server")
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind to",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind to",
    )
    parser.add_argument(
        "--model",
        help="Pre-load a model on startup",
    )
    parser.add_argument(
        "--preload",
        action="store_true",
        help="Pre-load the specified model",
    )
    parser.add_argument(
        "--cache-dir",
        default="~/.cache/iron/models",
        help="Model cache directory",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Number of worker processes",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Store args for startup use
    app.state.cache_dir = args.cache_dir
    app.state.preload_model = args.model if args.preload else None

    print(f"Starting IRON API server on {args.host}:{args.port}")
    print(f"Model cache: {args.cache_dir}")
    if args.model:
        print(f"Pre-loading model: {args.model}")

    uvicorn.run(
        "iron.api.server:app",
        host=args.host,
        port=args.port,
        workers=args.workers,
    )


if __name__ == "__main__":
    main()
