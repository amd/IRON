# Task #34: Lemonade Backend API Review - Deliverables

**Date:** 2026-03-15
**Author:** Jordan Lee, Senior Software Developer
**Status:** Complete

---

## Executive Summary

This document provides a comprehensive analysis of Lemonade's `WrappedServer` interface, existing backend implementation patterns, and a detailed implementation checklist for Task #30 (IronServer C++ Backend Wrapper).

### Key Findings

1. **WrappedServer** is the abstract base class for all Lemonade backends
2. Backends run as **subprocesses** - Lemonade forwards HTTP requests to them
3. The pattern is well-established with 6 existing backends (llamacpp, ryzenai, flm, whisper, sd, kokoro)
4. IRON integration will follow the **RyzenAIServer pattern** (Python subprocess wrapper)

---

## 1. WrappedServer Interface Documentation

### 1.1 Class Hierarchy

```
ICapability (base interface)
    └── ICompletionServer (core completion capabilities)
            └── WrappedServer (abstract base for backends)
                    ├── LlamaCppServer
                    ├── RyzenAIServer
                    ├── FastFlowLMServer
                    ├── WhisperServer
                    ├── KokoroServer
                    ├── SdServer
                    └── IronServer (TO BE CREATED)
```

### 1.2 ICompletionServer Interface

**File:** `src/cpp/include/lemon/server_capabilities.h`

```cpp
class ICompletionServer : public virtual ICapability {
public:
    virtual ~ICompletionServer() = default;
    virtual json chat_completion(const json& request) = 0;
    virtual json completion(const json& request) = 0;
};
```

### 1.3 WrappedServer Abstract Class

**File:** `src/cpp/include/lemon/wrapped_server.h`

#### Constructor Signature
```cpp
WrappedServer(
    const std::string& server_name,     // e.g., "IRON-Server"
    const std::string& log_level,       // "info" or "debug"
    ModelManager* model_manager = nullptr,
    BackendManager* backend_manager = nullptr
)
```

#### Pure Virtual Methods (MUST IMPLEMENT)

| Method | Signature | Purpose |
|--------|-----------|---------|
| `load` | `void load(const std::string& model_name, const ModelInfo& model_info, const RecipeOptions& options, bool do_not_upgrade = false)` | Load model and start server process |
| `unload` | `void unload()` | Unload model and stop server process |
| `chat_completion` | `json chat_completion(const json& request)` | Handle OpenAI chat completion requests |
| `completion` | `json completion(const json& request)` | Handle OpenAI legacy completion requests |
| `responses` | `json responses(const json& request)` | Handle OpenAI responses endpoint |

#### Protected Helper Methods (AVAILABLE FOR USE)

| Method | Purpose |
|--------|---------|
| `choose_port()` | Find and assign an available port |
| `wait_for_ready(endpoint, timeout, poll_interval)` | Wait for server health endpoint to respond |
| `forward_request(endpoint, request, timeout)` | Forward JSON request to wrapped server |
| `forward_multipart_request(endpoint, fields, timeout)` | Forward multipart form data |
| `forward_streaming_request(endpoint, body, sink, sse, timeout)` | Forward streaming SSE requests |
| `get_base_url()` | Get server base URL (http://127.0.0.1:PORT) |
| `get_address()` | Get full API address (base_url + "/v1") |
| `is_process_running()` | Check if subprocess is still running |
| `is_debug()` | Check if debug logging is enabled |

#### Member Variables (INHERITED)

| Variable | Type | Purpose |
|----------|------|---------|
| `server_name_` | `std::string` | Display name for logging |
| `port_` | `int` | Server listening port |
| `process_handle_` | `ProcessHandle` | Subprocess handle |
| `telemetry_` | `Telemetry` | Performance metrics |
| `log_level_` | `std::string` | Logging level |
| `model_manager_` | `ModelManager*` | Non-owning pointer |
| `backend_manager_` | `BackendManager*` | Non-owning pointer |
| `model_name_` | `std::string` | Current model name |
| `checkpoint_` | `std::string` | Model checkpoint identifier |
| `model_type_` | `ModelType` | LLM, embedding, reranking, audio, image, tts |
| `device_type_` | `DeviceType` | DEVICE_NONE, DEVICE_NPU, DEVICE_GPU, DEVICE_CPU |
| `recipe_options_` | `RecipeOptions` | Backend-specific options |
| `last_access_time_` | `time_point` | For LRU cache eviction |
| `is_busy_` | `bool` | Inference in progress flag |

---

## 2. Backend Implementation Patterns

### 2.1 Backend Pattern Comparison

| Backend | Type | Subprocess | Key Characteristics |
|---------|------|------------|---------------------|
| **LlamaCppServer** | Native binary | `llama-server.exe` | Complex arg building, GPU layer config |
| **RyzenAIServer** | Native binary | `ryzenai-server.exe` | Simple arg pattern, model path required |
| **FastFlowLMServer** | Native binary | `flm-server.exe` | Multi-model, advanced features |
| **WhisperServer** | Native binary | `whisper-server.exe` | Audio transcription |
| **KokoroServer** | Native binary | `kokoro-server.exe` | TTS audio generation |
| **SdServer** | Native binary | `sd-server.exe` | Image generation |
| **IronServer** | **Python server** | **`python -m iron.api.server`** | **TO BE CREATED** |

### 2.2 Minimal Backend Pattern (RyzenAIServer - Recommended Template)

**Header File:** `src/cpp/include/lemon/backends/iron_server.h`

```cpp
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
        "python"  // Uses system Python
#else
        "python3"
#endif
#ifndef LEMONADE_TRAY
        , get_install_params
#endif
    );

    IronServer(const std::string& model_name, bool debug,
               ModelManager* model_manager, BackendManager* backend_manager);
    ~IronServer() override;

    // Check if IRON Python package is available
    static bool is_available();

    void load(const std::string& model_name,
             const ModelInfo& model_info,
             const RecipeOptions& options,
             bool do_not_upgrade = false) override;

    void unload() override;

    // Inference operations (from ICompletionServer via WrappedServer)
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

**Implementation File:** `src/cpp/server/backends/iron_server.cpp`

```cpp
#include "lemon/backends/iron_server.h"
#include "lemon/backends/backend_utils.h"
#include "lemon/backend_manager.h"
#include "lemon/utils/process_manager.h"
#include "lemon/error_types.h"
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;
using namespace lemon::utils;

namespace lemon {

// Installation parameters (if packaging Python environment)
InstallParams IronServer::get_install_params(const std::string& /*backend*/, const std::string& /*version*/) {
    // For Python-based backend, we rely on system Python + pip package
    // Return empty params or package Python environment if needed
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
    std::string gguf_path = model_info.resolved_path();
    if (gguf_path.empty()) {
        throw std::runtime_error("Model file not found for checkpoint: " + model_info.checkpoint());
    }

    // Find Python executable
    std::string python_path = "python";  // Could use full path detection

    // Choose port
    port_ = choose_port();

    // Build command line arguments
    std::vector<std::string> args = {
        "-m", "iron.api.server",
        "--model-path", gguf_path,
        "--port", std::to_string(port_)
    };

    // Add debug flag if enabled
    if (is_debug()) {
        args.push_back("--verbose");
    }

    // Set Python environment variables if needed
    std::vector<std::pair<std::string, std::string>> env_vars;
    // Example: env_vars.push_back({"PYTHONPATH", "/path/to/iron"});

    LOG(DEBUG, "IRON") << "Starting: \"" << python_path << "\"";
    for (const auto& arg : args) {
        LOG(DEBUG, "IRON") << " \"" << arg << "\"";
    }
    LOG(DEBUG, "IRON") << std::endl;

    // Start the process (filter health check spam)
    process_handle_ = utils::ProcessManager::start_process(
        python_path,
        args,
        "",  // Working directory
        is_debug(),  // Inherit output if debug
        true,        // Filter health check spam
        env_vars
    );

    if (!utils::ProcessManager::is_running(process_handle_)) {
        throw std::runtime_error("Failed to start IRON server process");
    }

    LOG(DEBUG, "ProcessManager") << "Process started successfully, PID: "
                << process_handle_.pid << std::endl;

    // Wait for server to be ready
    if (!wait_for_ready("/health")) {
        utils::ProcessManager::stop_process(process_handle_);
        process_handle_ = {nullptr, 0};  // Reset to prevent double-stop
        throw std::runtime_error("IRON server failed to start (check logs for details)");
    }

    is_loaded_ = true;
    LOG(INFO, "IRON") << "Model loaded on port " << port_ << std::endl;
}

void IronServer::unload() {
    if (!is_loaded_) {
        return;
    }

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

    // Forward to /v1/chat/completions endpoint
    return forward_request("/v1/chat/completions", request);
}

json IronServer::completion(const json& request) {
    if (!is_loaded_) {
        throw ModelNotLoadedException("IRON-Server");
    }

    // Forward to /v1/completions endpoint
    return forward_request("/v1/completions", request);
}

json IronServer::responses(const json& request) {
    if (!is_loaded_) {
        throw ModelNotLoadedException("IRON-Server");
    }

    // Forward to /v1/responses endpoint
    return forward_request("/v1/responses", request);
}

} // namespace lemon
```

### 2.3 Registration Requirements

**File:** `src/cpp/server/backends/backend_utils.cpp`

Add include:
```cpp
#include "lemon/backends/iron_server.h"
```

Add to `try_get_spec_for_recipe`:
```cpp
const BackendSpec* try_get_spec_for_recipe(const std::string& recipe) {
    if (recipe == "llamacpp") return &LlamaCppServer::SPEC;
    if (recipe == "whispercpp") return &WhisperServer::SPEC;
    if (recipe == "sd-cpp") return &SDServer::SPEC;
    if (recipe == "kokoro") return &KokoroServer::SPEC;
    if (recipe == "ryzenai-llm") return &::lemon::RyzenAIServer::SPEC;
    if (recipe == "iron") return &IronServer::SPEC;  // ADD THIS
    return nullptr;
}
```

**File:** `src/cpp/server/router.cpp`

Add to `create_backend_server`:
```cpp
std::unique_ptr<WrappedServer> Router::create_backend_server(const ModelInfo& model_info) {
    std::unique_ptr<WrappedServer> new_server;

    if (model_info.recipe == "whispercpp") {
        new_server = std::make_unique<backends::WhisperServer>(log_level_, model_manager_, backend_manager_);
    } else if (model_info.recipe == "kokoro") {
        new_server = std::make_unique<backends::KokoroServer>(log_level_, model_manager_, backend_manager_);
    } else if (model_info.recipe == "sd-cpp") {
        new_server = std::make_unique<backends::SDServer>(log_level_, model_manager_, backend_manager_);
    } else if (model_info.recipe == "flm") {
        new_server = std::make_unique<backends::FastFlowLMServer>(log_level_, model_manager_, backend_manager_);
    } else if (model_info.recipe == "ryzenai-llm") {
        // ... existing code ...
    } else if (model_info.recipe == "iron") {  // ADD THIS
        LOG(DEBUG, "Router") << "Creating IronServer backend" << std::endl;
        new_server = std::make_unique<IronServer>(model_info.model_name,
                                                   log_level_ == "debug",
                                                   model_manager_, backend_manager_);
    } else {
        new_server = std::make_unique<backends::LlamaCppServer>(log_level_, model_manager_, backend_manager_);
    }

    return new_server;
}
```

**File:** `src/cpp/resources/backend_versions.json`

```json
{
  "iron": {
    "python": "1.0.0"
  }
}
```

**File:** `CMakeLists.txt`

```cmake
target_sources(lemonade-router PRIVATE
    # ... existing sources ...
    src/cpp/server/backends/iron_server.cpp
)
```

---

## 3. Data Flow Architecture

### 3.1 Request Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER REQUEST                             │
│  POST http://localhost:8000/v1/chat/completions                  │
│  { "model": "meta-llama/Llama-3.2-1B", "messages": [...] }       │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                      LEMONADE ROUTER                             │
│  1. Parse request                                                │
│  2. Extract model name                                           │
│  3. Find loaded IronServer instance                              │
│  4. Mark server as busy                                          │
│  5. Call IronServer::chat_completion()                           │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                       IRONSERVER (C++)                           │
│  1. Check is_loaded_                                             │
│  2. Build URL: http://127.0.0.1:{port}/v1/chat/completions       │
│  3. Call forward_request()                                       │
│  4. HTTP POST with JSON body                                     │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    IRON PYTHON SERVER                            │
│  1. FastAPI receives request                                     │
│  2. Check model loaded (auto-load if needed)                     │
│  3. Convert messages to prompt                                   │
│  4. Tokenize prompt                                              │
│  5. Run inference loop (GEMM -> RoPE -> SwiGLU -> RMSNorm)       │
│  6. Detokenize output                                            │
│  7. Format OpenAI response                                       │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                        RESPONSE                                  │
│  { "choices": [{"message": {"content": "..."}}], "usage": ... } │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Model Loading Flow

```
┌─────────────────────────────────────────────────────────────────┐
│  Lemonade::load_model(model_name, model_info, options)          │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│  1. Check if model already loaded                               │
│  2. Check NPU exclusivity rules                                 │
│  3. LRU eviction if at capacity                                 │
│  4. Create IronServer instance                                  │
│  5. Call IronServer::load()                                     │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│  IronServer::load()                                             │
│  1. Get model path from model_info                              │
│  2. Choose available port                                       │
│  3. Build Python command line                                   │
│  4. Start subprocess: python -m iron.api.server                 │
│  5. Wait for /health endpoint                                   │
│  6. Mark is_loaded_ = true                                      │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│  Iron Python Server Startup                                     │
│  1. Parse command line args                                     │
│  2. Initialize ModelRegistry                                    │
│  3. Initialize AutoConverter                                    │
│  4. Load model (auto-convert if needed)                         │
│  5. Compile AIE artifacts                                       │
│  6. Start Uvicorn server on specified port                      │
│  7. Health endpoint becomes available                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Implementation Checklist for Task #30

### Phase 1: IronServer C++ Implementation

#### 1.1 Header File
- [ ] Create `src/cpp/include/lemon/backends/iron_server.h`
- [ ] Define `IronServer` class inheriting from `WrappedServer`
- [ ] Declare `BackendSpec SPEC` static member
- [ ] Declare constructor with proper signature
- [ ] Declare destructor with `override`
- [ ] Declare `is_available()` static method
- [ ] Declare `load()`, `unload()` override methods
- [ ] Declare `chat_completion()`, `completion()`, `responses()` override methods
- [ ] Add private members: `model_name_`, `model_path_`, `is_loaded_`

#### 1.2 Implementation File
- [ ] Create `src/cpp/server/backends/iron_server.cpp`
- [ ] Include required headers
- [ ] Implement `get_install_params()` (return empty or package info)
- [ ] Implement constructor (initialize base class and members)
- [ ] Implement destructor (call `unload()` if loaded)
- [ ] Implement `is_available()` (check Python + iron package)
- [ ] Implement `load()`:
  - [ ] Extract model path from `model_info`
  - [ ] Call `choose_port()`
  - [ ] Build Python command line args
  - [ ] Start subprocess with `ProcessManager::start_process()`
  - [ ] Wait for health with `wait_for_ready("/health")`
  - [ ] Set `is_loaded_ = true`
- [ ] Implement `unload()`:
  - [ ] Check `is_loaded_`
  - [ ] Stop process with `ProcessManager::stop_process()`
  - [ ] Reset `process_handle_`, `port_`, `model_path_`
  - [ ] Set `is_loaded_ = false`
- [ ] Implement `chat_completion()` - forward to `/v1/chat/completions`
- [ ] Implement `completion()` - forward to `/v1/completions`
- [ ] Implement `responses()` - forward to `/v1/responses`

#### 1.3 Build System Integration
- [ ] Add `src/cpp/server/backends/iron_server.cpp` to `CMakeLists.txt`
- [ ] Add include directory to CMake if needed

#### 1.4 Backend Registration
- [ ] Add `#include "lemon/backends/iron_server.h"` to `backend_utils.cpp`
- [ ] Add iron spec to `try_get_spec_for_recipe()`
- [ ] Add iron case to `Router::create_backend_server()`
- [ ] Add entry to `backend_versions.json`

### Phase 2: IRON Python Server Validation

#### 2.1 Verify iron.api.server Module
- [ ] Confirm `iron/api/server.py` exists and is functional
- [ ] Verify command-line argument parsing (`--model-path`, `--port`, `--verbose`)
- [ ] Test standalone execution: `python -m iron.api.server --port 8000`
- [ ] Verify `/health` endpoint responds correctly
- [ ] Verify `/v1/models` endpoint works
- [ ] Verify `/v1/chat/completions` endpoint works (streaming + non-streaming)
- [ ] Verify `/v1/completions` endpoint works

#### 2.2 Model Auto-Conversion
- [ ] Verify `AutoConverter` class exists in `iron/api/auto_converter.py`
- [ ] Test model conversion flow with a sample HuggingFace model
- [ ] Verify model caching at `~/.cache/iron/models/`
- [ ] Confirm tokenizer utilities in `iron/api/tokenizers.py`

### Phase 3: Testing

#### 3.1 Unit Tests
- [ ] Test `IronServer::is_available()` detection
- [ ] Test `load()` with valid model path
- [ ] Test `load()` error handling (missing model, port conflict)
- [ ] Test `unload()` properly stops process
- [ ] Test `chat_completion()` request forwarding
- [ ] Test `completion()` request forwarding

#### 3.2 Integration Tests
- [ ] Load model via Lemonade: `lemonade-server run <model> --backend iron`
- [ ] Send chat completion request via OpenAI client
- [ ] Test streaming responses
- [ ] Test non-streaming responses
- [ ] Verify telemetry collection
- [ ] Test model unloading
- [ ] Test multiple sequential requests

#### 3.3 Performance Tests
- [ ] Measure time-to-first-token (TTFT)
- [ ] Measure tokens-per-second generation speed
- [ ] Compare with native Python server (no Lemonade overhead)
- [ ] Profile memory usage

### Phase 4: Documentation

#### 4.1 Code Documentation
- [ ] Add Doxygen comments to `iron_server.h`
- [ ] Add inline comments for complex logic in `iron_server.cpp`
- [ ] Document command-line argument expectations

#### 4.2 User Documentation
- [ ] Create `docs/IRON_BACKEND_GUIDE.md` in Lemonade repo
- [ ] Document installation requirements (Python version, iron package)
- [ ] Provide usage examples with OpenAI client
- [ ] Document troubleshooting steps

#### 4.3 Developer Documentation
- [ ] Update `CLAUDE.md` in Lemonade repo with IronServer reference
- [ ] Document the Python subprocess architecture
- [ ] Note any platform-specific considerations (Windows vs Linux)

---

## 5. Special Considerations

### 5.1 Platform Compatibility

| Platform | Python Command | Notes |
|----------|---------------|-------|
| Windows | `python` | Ensure Python is in PATH |
| Linux | `python3` | May need `python3` explicitly |
| macOS | `python3` | Not primary target for NPU |

### 5.2 Environment Variables

Consider setting:
```cpp
env_vars.push_back({"PYTHONPATH", "/path/to/iron"});  // If not installed
env_vars.push_back({"IRON_CACHE_DIR", "~/.cache/iron"});  // Custom cache
```

### 5.3 Error Handling

Key error scenarios to handle:
1. **Python not found** - `is_available()` should return false
2. **iron package not installed** - Provide helpful error message
3. **Port conflict** - `choose_port()` handles this
4. **Model conversion failure** - Propagate error to Lemonade
5. **NPU not available** - Python server should detect and report

### 5.4 Logging Strategy

```cpp
// Debug logging example
LOG(DEBUG, "IRON") << "Detailed debug info" << std::endl;

// Info logging for user-facing messages
LOG(INFO, "IRON") << "Model loaded on port " << port_ << std::endl;

// Error logging
LOG(ERROR, "IRON") << "Load failed: " << error_message << std::endl;
```

### 5.5 Health Check Endpoint

The IRON Python server MUST implement:
```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "models": list(loaded_models.keys()),
        "ready": len(loaded_models) > 0,
    }
```

### 5.6 Streaming Support

For streaming chat completions:
```cpp
void IronServer::chat_completion_stream(const std::string& request_body,
                                        httplib::DataSink& sink) {
    forward_streaming_request("/v1/chat/completions", request_body, sink, true);
}
```

---

## 6. References

### 6.1 Source Files Analyzed

| File | Purpose |
|------|---------|
| `src/cpp/include/lemon/wrapped_server.h` | Base class definition |
| `src/cpp/server/wrapped_server.cpp` | Base class implementation |
| `src/cpp/include/lemon/server_capabilities.h` | Capability interfaces |
| `src/cpp/include/lemon/backends/llamacpp_server.h` | Complex backend example |
| `src/cpp/server/backends/llamacpp_server.cpp` | Complex backend implementation |
| `src/cpp/include/lemon/backends/ryzenaiserver.h` | Simple backend example |
| `src/cpp/server/backends/ryzenaiserver.cpp` | Simple backend implementation |
| `src/cpp/server/router.cpp` | Backend routing logic |
| `src/cpp/include/lemon/backend_manager.h` | Backend management |
| `src/cpp/resources/backend_versions.json` | Version configuration |

### 6.2 IRON Files Referenced

| File | Purpose |
|------|---------|
| `iron/api/server.py` | Python FastAPI server |
| `iron/api/auto_converter.py` | Model conversion |
| `iron/api/model_registry.py` | Model registry |
| `iron/api/tokenizers.py` | Tokenizer utilities |
| `docs/LEMONADE_INTEGRATION_PLAN.md` | Integration strategy |
| `docs/IRON_LEMONADE_INTEGRATION.md` | Detailed integration plan |

---

## 7. Recommendations for Task #30

### 7.1 Immediate Next Steps

1. **Verify iron.api.server functionality** - Ensure the Python server works standalone
2. **Create IronServer header and implementation** - Follow RyzenAIServer pattern
3. **Register backend** - Update router, backend_utils, CMakeLists.txt
4. **Test end-to-end** - Run via Lemonade with a test model

### 7.2 Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Python path issues | Use full path detection or document requirements |
| Model conversion delays | Implement progress callback during load() |
| NPU driver conflicts | Check NPU availability in is_available() |
| Port conflicts | choose_port() already handles this |

### 7.3 Success Criteria

Task #30 is complete when:
- [ ] IronServer compiles without errors
- [ ] Lemonade can load IRON backend
- [ ] Chat completion requests succeed
- [ ] Streaming responses work
- [ ] Model unloading works cleanly
- [ ] No memory leaks on repeated load/unload cycles

---

**Document End**

*Copyright 2026 Advanced Micro Devices, Inc. All rights reserved.*
