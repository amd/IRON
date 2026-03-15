<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# IRON Integration with Lemonade - Comprehensive Plan

## Executive Summary

This document outlines the plan to integrate IRON as a backend for Lemonade, enabling LLM inference on AMD Ryzen AI NPUs through Lemonade's OpenAI-compatible API.

## Part 1: Understanding Conv3D's Role

### 1.1 Conv3D Status - COMPLETE

Conv3D is **fully implemented** for both AIE2 (NPU) and AIE2P (NPU2) architectures with the following capabilities:

#### Dual-Purpose Design

**1. Semantic Video Convolution** (Traditional Use)
```python
# Standard video input: (N, C, T, H, W)
conv3d = AIEConv3d(
    in_channels=64,
    out_channels=128,
    kernel_size=(3, 3, 3),
    stride=(1, 2, 2),
    padding=(1, 1, 1)
)
# Use: Video classification, action recognition, etc.
```

**2. Compute Primitive for Text Models** (Key Insight)
```python
# MHA blocked format: (B, G, H, S_tiles, D_h_tiles)
conv3d = AIEConv3d(
    in_channels=G,
    out_channels=G,
    kernel_size=(1, 3, 3),  # Process local S x D_h windows
    stride=(1, 1, 1),
    padding=(0, 1, 1)
)
# Use: Windowed attention, cross-head mixing, linear projection
```

### 1.2 5D Shape Mapping for MHA

| Conv3D Dim | MHA Dim | Description |
|------------|---------|-------------|
| N | B | Batch |
| C | G | GQA Groups |
| T | H | Heads per group |
| H | S_tiles | Sequence tiles |
| W | D_h_tiles | Head dimension tiles |

### 1.3 Kernel Configurations

| Kernel Size | Use Case | Description |
|-------------|----------|-------------|
| (1, 1, 1) | Channel projection | Linear layer equivalent for 5D |
| (1, 3, 3) | Local attention | Windowed attention over S × D_h |
| (3, 3, 3) | Full 3D convolution | Video models, spatiotemporal |
| (1, 1, k) | Cross-head mixing | Mix information across heads |

### 1.4 Key Files (Already Complete)

| File | Status | Description |
|------|--------|-------------|
| `iron/operators/conv3d/op.py` | ✅ Complete | Operator interface |
| `iron/operators/conv3d/design.py` | ✅ Complete | MLIR generation |
| `iron/operators/conv3d/reference.py` | ✅ Complete | CPU reference |
| `iron/operators/conv3d/test.py` | ✅ Complete | Test suite |
| `aie_kernels/aie2/conv3d.cc` | ✅ Complete | AIE2 kernel (vec=8) |
| `aie_kernels/aie2p/conv3d.cc` | ✅ Complete | AIE2P kernel (vec=16) |

### 1.5 Conv3D in the Lemonade Context

For **LLM inference via Lemonade**, Conv3D serves as:

1. **Optional Compute Primitive** - For specialized attention patterns
2. **Video Model Support** - For video understanding models
3. **Future Optimization Path** - Custom attention via shape manipulation

**Primary LLM operators** (more commonly used):
- `AIEGEMM` - Matrix multiplication (FFN, QKV projection)
- `AIEGEMV` - Matrix-vector multiplication (decode phase)
- `AIERMSNorm` - RMS normalization
- `AIERoPE` - Rotary position embeddings
- `AIEMHA` - Multi-head attention (fused)

---

## Part 2: Lemonade Backend Architecture

### 2.1 How Lemonade Backends Work

Lemonade uses a **wrapped server** architecture:

```
┌─────────────────────────────────────────────────────────┐
│                    Lemonade Server                       │
│  ┌─────────────────────────────────────────────────┐    │
│  │              OpenAI-Compatible API               │    │
│  │  /v1/chat/completions  /v1/completions  /v1/models│   │
│  └─────────────────────────────────────────────────┘    │
│                          │                               │
│  ┌───────────────────────▼─────────────────────────┐    │
│  │              Backend Router                      │    │
│  │  Routes requests to appropriate backend server   │    │
│  └───────────────────────┬─────────────────────────┘    │
└──────────────────────────┼──────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
┌───────▼────────┐  ┌─────▼────────┐  ┌─────▼────────┐
│ llamacpp       │  │ ryzenai      │  │ IRON (new)   │
│ Server         │  │ Server       │  │ Server       │
│ (C++ binary)   │  │ (C++ binary) │  │ (Python)     │
│ localhost:8001 │  │ localhost:8002│ │ localhost:800X│
└────────────────┘  └──────────────┘  └──────────────┘
```

### 2.2 Backend Interface Requirements

To integrate with Lemonade, a backend must:

1. **Wrap an external server process** that:
   - Listens on a local HTTP port
   - Implements OpenAI-compatible endpoints
   - Supports `/v1/chat/completions` (streaming + non-streaming)
   - Supports `/v1/completions` (legacy)
   - Supports health check endpoint (`/health`)

2. **Implement C++ backend wrapper** (`IronServer`) that:
   - Inherits from `WrappedServer`
   - Implements `load()` - Start IRON server with model
   - Implements `unload()` - Stop IRON server
   - Implements `chat_completion()` - Forward to `/v1/chat/completions`
   - Implements `completion()` - Forward to `/v1/completions`

3. **Model format support**:
   - Accept safetensors weights (standard HF format)
   - Auto-convert to IRON format on load
   - Cache converted models for subsequent loads

---

## Part 3: Implementation Plan

### Phase 1: IRON HTTP Server (Python)

Create `iron/api/server.py` - A FastAPI server that:

#### 1.1 Auto-Conversion System

```python
# iron/api/auto_converter.py

from iron.model_convert import HuggingFaceConverter
from pathlib import Path
import json

class AutoConverter:
    """Automatically downloads and converts HF models to IRON format"""

    def __init__(self, cache_dir: str = "~/.cache/iron/models"):
        self.cache_dir = Path(cache_dir).expanduser()
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get_or_convert(self, model_id: str) -> Path:
        """
        Get converted model path, converting if needed.

        Flow:
        1. Check cache for converted model
        2. If not found, download from HF Hub
        3. Convert to IRON format
        4. Save to cache
        5. Return model path
        """
        safe_name = model_id.replace("/", "__")
        model_path = self.cache_dir / safe_name

        # Check if already converted
        config_path = model_path / "iron_config.json"
        if config_path.exists():
            print(f"Using cached model: {model_path}")
            return model_path

        # Convert from HF
        print(f"Converting {model_id}...")
        converter = HuggingFaceConverter(model_id)
        converter.convert_weights(output_dir=str(model_path))
        converter.export_config(str(config_path))

        return model_path
```

#### 1.2 FastAPI Server

```python
# iron/api/server.py

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
import json
import time

from .auto_converter import AutoConverter
from iron.model_convert import create_model
from iron.common import AIEOperatorBase

app = FastAPI(title="IRON API", version="1.0.0")
auto_converter = AutoConverter()
loaded_models = {}

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    max_tokens: Optional[int] = 100
    stream: Optional[bool] = False

@app.get("/health")
async def health():
    return {"status": "healthy", "models": list(loaded_models.keys())}

@app.get("/v1/models")
async def list_models():
    return {
        "data": [
            {"id": model_id, "object": "model", "owned_by": "iron"}
            for model_id in loaded_models.keys()
        ]
    }

@app.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    model_id = request.model

    # Auto-load model if needed
    if model_id not in loaded_models:
        model_path = auto_converter.get_or_convert(model_id)
        assembler = create_model(
            config_path=model_path / "iron_config.json",
            weights_path=model_path,
        )
        assembler.compile_artifacts()
        loaded_models[model_id] = assembler

    model = loaded_models[model_id]

    # Convert messages to prompt
    prompt = messages_to_prompt(request.messages)

    # Tokenize
    input_ids = tokenize(prompt)

    if request.stream:
        return StreamingResponse(
            generate_stream(model, input_ids, request.max_tokens),
            media_type="text/event-stream"
        )
    else:
        output_ids = generate(model, input_ids, request.max_tokens)
        text = detokenize(output_ids)

        return {
            "id": f"chatcmpl-{int(time.time())}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": model_id,
            "choices": [{
                "index": 0,
                "message": {"role": "assistant", "content": text},
                "finish_reason": "stop"
            }],
            "usage": {
                "prompt_tokens": len(input_ids),
                "completion_tokens": len(output_ids) - len(input_ids),
                "total_tokens": len(output_ids)
            }
        }

def messages_to_prompt(messages: List[ChatMessage]) -> str:
    """Convert chat messages to Llama-3 format"""
    prompt = "<|begin_of_text|>"
    for msg in messages:
        prompt += f"<|start_header_id|>{msg.role}<|end_header_id|>\n\n"
        prompt += f"{msg.content}<|eot_id|>"
    prompt += "<|start_header_id|>assistant<|end_header_id|>\n\n"
    return prompt
```

### Phase 2: Lemonade C++ Backend Wrapper

Create `src/cpp/server/backends/iron_server.cpp`:

```cpp
// src/cpp/server/backends/iron_server.cpp

#include "lemon/backends/iron_server.h"
#include "lemon/backends/backend_utils.h"
#include "lemon/backend_manager.h"
#include "lemon/utils/process_manager.h"
#include "lemon/error_types.h"
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

namespace lemon {

InstallParams IronServer::get_install_params(const std::string& /*backend*/, const std::string& /*version*/) {
    return {"amd/iron", "iron-server.zip"};
}

IronServer::IronServer(const std::string& model_name, bool debug,
                       ModelManager* model_manager, BackendManager* backend_manager)
    : WrappedServer("IRON-Server", debug ? "debug" : "info", model_manager, backend_manager),
      model_name_(model_name),
      is_loaded_(false) {
}

IronServer::~IronServer() {
    if (is_loaded_) {
        try {
            unload();
        } catch (...) {
            // Suppress exceptions in destructor
        }
    }
}

bool IronServer::is_available() {
    // Check if Python and iron package are available
    try {
        auto result = utils::ProcessManager::execute_command("python -c \"import iron\"");
        return result.exit_code == 0;
    } catch (...) {
        return false;
    }
}

void IronServer::load(const std::string& model_name,
                     const ModelInfo& model_info,
                     const RecipeOptions& options,
                     bool do_not_upgrade) {
    LOG(DEBUG, "IRON") << "Loading model: " << model_name << std::endl;

    // Get model path from model manager
    model_path_ = model_manager_->get_model_path(model_info.checkpoint);
    if (model_path_.empty()) {
        throw std::runtime_error("Model path not found for: " + model_info.checkpoint);
    }

    // Find Python
    std::string python_path = "python";  // Could also use full path detection

    // Build command line
    std::vector<std::string> args = {
        "-m", "iron.api.server",
        "--model-path", model_path_,
        "--port", "0"  // Auto-select port
    };

    if (is_debug()) {
        args.push_back("--verbose");
    }

    // Choose port
    port_ = choose_port();

    // Start Python server
    process_handle_ = utils::ProcessManager::start_process(python_path, args, "", is_debug(), true);

    if (!utils::ProcessManager::is_running(process_handle_)) {
        throw std::runtime_error("Failed to start IRON server process");
    }

    // Wait for ready
    if (!wait_for_ready("/health")) {
        utils::ProcessManager::stop_process(process_handle_);
        process_handle_ = {nullptr, 0};
        throw std::runtime_error("IRON server failed to start");
    }

    is_loaded_ = true;
    LOG(INFO, "IRON") << "Model loaded on port " << port_ << std::endl;
}

void IronServer::unload() {
    if (!is_loaded_) return;

    LOG(DEBUG, "IRON") << "Unloading model..." << std::endl;

#ifdef _WIN32
    if (process_handle_.handle) {
#else
    if (process_handle_.pid > 0) {
#endif
        utils::ProcessManager::stop_process(process_handle_);
        process_handle_ = {nullptr, 0};
    }

    is_loaded_ = false;
    port_ = 0;
    model_path_.clear();
}

json IronServer::chat_completion(const json& request) {
    if (!is_loaded_) {
        throw ModelNotLoadedException("IRON-Server");
    }
    return forward_request("/v1/chat/completions", request);
}

json IronServer::completion(const json& request) {
    if (!is_loaded_) {
        throw ModelNotLoadedException("IRON-Server");
    }
    return forward_request("/v1/completions", request);
}

json IronServer::responses(const json& request) {
    if (!is_loaded_) {
        throw ModelNotLoadedException("IRON-Server");
    }
    return forward_request("/v1/responses", request);
}

} // namespace lemon
```

Create `src/cpp/include/lemon/backends/iron_server.h`:

```cpp
// src/cpp/include/lemon/backends/iron_server.h

#pragma once

#include "lemon/wrapped_server.h"
#include "lemon/server_capabilities.h"
#include "lemon/backends/backend_utils.h"
#include "lemon/error_types.h"
#include <string>

namespace lemon {

using backends::BackendSpec;
using backends::InstallParams;

class IronServer : public WrappedServer {
public:
#ifndef LEMONADE_TRAY
    static InstallParams get_install_params(const std::string& backend, const std::string& version);
#endif

    inline static const BackendSpec SPEC = BackendSpec(
        "iron-server",
#ifdef _WIN32
        "iron-server.exe"
#else
        "iron-server"
#endif
#ifndef LEMONADE_TRAY
        , get_install_params
#endif
    );

    IronServer(const std::string& model_name, bool debug, ModelManager* model_manager,
               BackendManager* backend_manager);
    ~IronServer() override;

    static bool is_available();

    void load(const std::string& model_name,
             const ModelInfo& model_info,
             const RecipeOptions& options,
             bool do_not_upgrade = false) override;

    void unload() override;

    json chat_completion(const json& request) override;
    json completion(const json& request) override;
    json responses(const json& request) override;

private:
    std::string model_name_;
    std::string model_path_;
    bool is_loaded_;
};

} // namespace lemon
```

### Phase 3: Registration and Build

#### 3.1 Update backend_versions.json

```json
{
  "ryzenai-llm": {
    "npu": "1.0.0",
    "iron": "1.0.0"
  }
}
```

#### 3.2 Update CMakeLists.txt

Add iron_server.cpp to the build:

```cmake
target_sources(lemonade PRIVATE
    src/cpp/server/backends/iron_server.cpp
)
```

#### 3.3 Register Backend Spec

In `src/cpp/server/backends/backend_utils.cpp`:

```cpp
#include "lemon/backends/iron_server.h"

namespace lemon {
namespace backends {

static const BackendSpec* get_iron_spec() {
    static BackendSpec spec = IronServer::SPEC;
    return &spec;
}

void register_all_specs() {
    // ... existing registrations ...
    register_spec(get_iron_spec());
}

} // namespace backends
} // namespace lemon
```

---

## Part 4: Usage Flow

### 4.1 User Experience

```bash
# 1. Install IRON backend
lemonade recipes --install ryzenai-llm:iron

# 2. Run with HuggingFace model (auto-converts on first load)
lemonade-server run meta-llama/Llama-3.2-1B-Instruct --backend iron

# 3. Use with OpenAI client
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="not-needed")

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-1B-Instruct",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### 4.2 First Load vs Cached Load

**First Load:**
```
1. User requests: meta-llama/Llama-3.2-1B-Instruct
2. Lemonade routes to IRON backend
3. IRON backend starts iron-server.py
4. iron-server.py:
   - Downloads HF safetensors
   - Converts to IRON format
   - Saves to ~/.cache/iron/models/meta-llama__Llama-3.2-1B-Instruct
   - Compiles AIE artifacts
5. Server ready, inference begins
```

**Cached Load (subsequent):**
```
1. User requests: meta-llama/Llama-3.2-1B-Instruct
2. Lemonade routes to IRON backend
3. IRON backend starts iron-server.py
4. iron-server.py:
   - Finds cached converted model
   - Loads IRON format directly
   - Compiles AIE artifacts
5. Server ready (much faster)
```

---

## Part 5: Files to Create

| File | Type | Description |
|------|------|-------------|
| `iron/api/__init__.py` | New | API package |
| `iron/api/server.py` | New | FastAPI OpenAI server |
| `iron/api/auto_converter.py` | New | HF model auto-conversion |
| `iron/api/tokenizers.py` | New | Tokenizer utilities |
| `src/cpp/include/lemon/backends/iron_server.h` | New | C++ backend header |
| `src/cpp/server/backends/iron_server.cpp` | New | C++ backend implementation |

---

## Summary

### Conv3D Status
- ✅ **COMPLETE** - Dual-purpose (video + compute primitive for text)
- ✅ AIE2 and AIE2P kernels with 5 variants each
- ✅ Can be used for specialized attention patterns via 5D shape manipulation

### Lemonade Integration
1. **IRON HTTP Server** - Python FastAPI server with OpenAI endpoints
2. **Auto-Converter** - Downloads HF models, converts to IRON format, caches
3. **C++ Backend Wrapper** - `IronServer` class for Lemonade integration
4. **User Experience** - Just specify HF model name, everything automatic

### Next Steps
1. Create `iron/api/` directory with FastAPI server
2. Implement auto-converter with caching
3. Create C++ backend wrapper for Lemonade
4. Test with Llama-3.2-1B model
5. Submit PR to Lemonade repository

<p align="center">
Copyright&copy; 2025 Advanced Micro Devices, Inc
</p>
