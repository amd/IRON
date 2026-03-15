# IronServer C++ Backend Implementation - Integration Guide

**Date:** 2026-03-15
**Status:** IMPLEMENTATION COMPLETE - PENDING LEMONADE REPO INTEGRATION

---

## Executive Summary

The IronServer C++ backend wrapper has been fully implemented. The files are ready to be integrated into the Lemonade repository at `C:\antmi\lemonade\` when it becomes available.

---

## File Locations

### Current Location (Staging Area)
All IronServer files are currently staged at:
```
C:/Users/antmi/IRON/lemonade/
├── src/
│   └── cpp/
│       ├── include/
│       │   └── lemon/
│       │       └── backends/
│       │           └── iron_server.h           [NEW]
│       ├── server/
│       │   ├── backends/
│       │   │   ├── iron_server.cpp             [NEW]
│       │   │   └── backend_utils.cpp           [MODIFIED]
│       │   └── router.cpp                       [MODIFIED]
│       ├── resources/
│       │   └── backend_versions.json            [MODIFIED]
│       └── CMakeLists.txt                       [MODIFIED]
```

### Target Location (Lemonade Repo)
When the Lemonade repo is available at `C:\antmi\lemonade\`, copy files as follows:

| Source | Target |
|--------|--------|
| `C:/Users/antmi/IRON/lemonade/src/cpp/include/lemon/backends/iron_server.h` | `C:/antmi/lemonade/src/cpp/include/lemon/backends/iron_server.h` |
| `C:/Users/antmi/IRON/lemonade/src/cpp/server/backends/iron_server.cpp` | `C:/antmi/lemonade/src/cpp/server/backends/iron_server.cpp` |
| `C:/Users/antmi/IRON/lemonade/src/cpp/server/backends/backend_utils.cpp` | `C:/antmi/lemonade/src/cpp/server/backends/backend_utils.cpp` |
| `C:/Users/antmi/IRON/lemonade/src/cpp/server/router.cpp` | `C:/antmi/lemonade/src/cpp/server/router.cpp` |
| `C:/Users/antmi/IRON/lemonade/src/cpp/resources/backend_versions.json` | `C:/antmi/lemonade/src/cpp/resources/backend_versions.json` |
| `C:/Users/antmi/IRON/lemonade/src/cpp/CMakeLists.txt` | `C:/antmi/lemonade/src/cpp/CMakeLists.txt` |

---

## Integration Steps

### Step 1: Copy Files to Lemonade Repo

```powershell
# Assuming Lemonade repo is at C:\antmi\lemonade\
$source = "C:/Users/antmi/IRON/lemonade"
$target = "C:/antmi/lemonade"

# Copy header
Copy-Item "$source/src/cpp/include/lemon/backends/iron_server.h" `
          "$target/src/cpp/include/lemon/backends/iron_server.h"

# Copy implementation
Copy-Item "$source/src/cpp/server/backends/iron_server.cpp" `
          "$target/src/cpp/server/backends/iron_server.cpp"

# Copy modified files (will overwrite)
Copy-Item "$source/src/cpp/server/backends/backend_utils.cpp" `
          "$target/src/cpp/server/backends/backend_utils.cpp"

Copy-Item "$source/src/cpp/server/router.cpp" `
          "$target/src/cpp/server/router.cpp"

Copy-Item "$source/src/cpp/resources/backend_versions.json" `
          "$target/src/cpp/resources/backend_versions.json"

Copy-Item "$source/src/cpp/CMakeLists.txt" `
          "$target/src/cpp/CMakeLists.txt"
```

### Step 2: Verify Build

```bash
cd C:\antmi\lemonade\build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release
```

### Step 3: Test Integration

```bash
# Test 1: Verify iron backend is recognized
python -c "import lemonade; print(lemonade.list_backends())"

# Test 2: Load a model with iron backend
lemonade-server run meta-llama/Llama-3.2-1B --backend iron

# Test 3: Send a chat completion request
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "meta-llama/Llama-3.2-1B", "messages": [{"role": "user", "content": "Hello"}]}'
```

---

## Implementation Summary

### Files Created

1. **iron_server.h** (36 KB)
   - IronServer class definition
   - Inherits from WrappedServer
   - Backend specification static member
   - Method declarations for load/unload, chat_completion/completion/responses

2. **iron_server.cpp** (7.2 KB)
   - Constructor/destructor implementation
   - `is_available()` - checks Python + iron package
   - `load()` - starts Python subprocess
   - `unload()` - stops subprocess
   - Request forwarding methods

### Files Modified

1. **backend_utils.cpp**
   - Added `#include "lemon/backends/iron_server.h"`
   - Added `{"iron", &IronServer::SPEC}` to spec_map

2. **router.cpp**
   - Added `#include "lemon/backends/iron_server.h"`
   - Added iron case to `create_backend_server()`

3. **backend_versions.json**
   - Added iron backend version: `{"python": "1.0.0"}`

4. **CMakeLists.txt**
   - Added `iron_server.h` to LEMONADE_HEADERS
   - Added `iron_server.cpp` to LEMONADE_SOURCES

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Lemonade (C++)                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Router                                               │   │
│  │    └── create_backend_server()                        │   │
│  │         └── IronServer                                │   │
│  └─────────────────────────┬─────────────────────────────┘   │
│                            │                                  │
│                            │ load()/chat_completion()         │
│                            ▼                                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  IronServer (C++ wrapper)                             │   │
│  │    - choose_port()                                    │   │
│  │    - start_process()                                  │   │
│  │    - wait_for_ready("/health")                        │   │
│  │    - forward_request()                                │   │
│  └─────────────────────────┬─────────────────────────────┘   │
└────────────────────────────┼─────────────────────────────────┘
                             │ subprocess (HTTP)
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              IRON Python Server                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  python -m iron.api.server                           │   │
│  │    - FastAPI server                                  │   │
│  │    - OpenAI-compatible endpoints                     │   │
│  │    - NPU inference via C++ runtime                   │   │
│  │    - Model auto-conversion                           │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Implementation Details

### Subprocess Command
```
python -m iron.api.server --model-path <path> --port <port> [--verbose]
```

### Health Check
```
GET http://127.0.0.1:<port>/health
```

### Endpoints Forwarded
| Lemonade Method | Endpoint | IRON Python Handler |
|-----------------|----------|---------------------|
| `chat_completion()` | `/v1/chat/completions` | `handle_chat_completion()` |
| `completion()` | `/v1/completions` | `handle_completion()` |
| `responses()` | `/v1/responses` | `handle_responses()` |

---

## Prerequisites

Before integrating, ensure:

1. **IRON Python package is installed:**
   ```bash
   pip install -e "C:/Users/antmi/IRON"
   ```

2. **Lemonade repo is available at `C:\antmi\lemonade\`**

3. **Build tools are installed:**
   - Visual Studio 2022 with C++ workload
   - CMake 3.16+
   - Python 3.10+ (for subprocess backends)

---

## Troubleshooting

### Issue: "iron-server.h not found"
**Solution:** Ensure the header is copied to the correct location:
```
C:/antmi/lemonade/src/cpp/include/lemon/backends/iron_server.h
```

### Issue: Build fails with "IronServer undefined"
**Solution:** Check that both the header AND implementation are copied, and that:
- `backend_utils.cpp` includes `iron_server.h`
- `router.cpp` includes `iron_server.h`
- `CMakeLists.txt` lists `iron_server.cpp` in LEMONADE_SOURCES

### Issue: "Python not found" at runtime
**Solution:** Ensure Python is in PATH or configure the Python path in `iron_server.cpp`:
```cpp
std::string python_path = "C:/path/to/python.exe";  // Instead of "python"
```

### Issue: "IRON server failed to start"
**Solution:** Check:
1. `python -m iron.api.server --help` works manually
2. `--model-path` points to a valid model file
3. Port is not already in use
4. Check logs for detailed error messages

---

## Next Steps After Integration

1. **Build Verification:**
   ```bash
   cd C:\antmi\lemonade\build
   cmake .. -DCMAKE_BUILD_TYPE=Release
   cmake --build . --config Release
   ```

2. **Unit Testing:**
   - Test `IronServer::is_available()`
   - Test load/unload lifecycle
   - Test request forwarding

3. **Integration Testing:**
   - Run via lemonade-server
   - Test with OpenAI client
   - Measure performance metrics

4. **Documentation:**
   - Update Lemonade README with iron backend
   - Add iron backend to documentation

---

## Files Checklist

| File | Status | Location |
|------|--------|----------|
| iron_server.h | COMPLETE | `C:/Users/antmi/IRON/lemonade/src/cpp/include/lemon/backends/` |
| iron_server.cpp | COMPLETE | `C:/Users/antmi/IRON/lemonade/src/cpp/server/backends/` |
| backend_utils.cpp | COMPLETE (modified) | `C:/Users/antmi/IRON/lemonade/src/cpp/server/backends/` |
| router.cpp | COMPLETE (modified) | `C:/Users/antmi/IRON/lemonade/src/cpp/server/` |
| backend_versions.json | COMPLETE (modified) | `C:/Users/antmi/IRON/lemonade/src/cpp/resources/` |
| CMakeLists.txt | COMPLETE (modified) | `C:/Users/antmi/IRON/lemonade/src/cpp/` |

---

**Integration Status:** PENDING LEMONADE REPO AVAILABILITY

All implementation files are ready. Once the Lemonade repository is available at `C:\antmi\lemonade\`, follow the integration steps above.

---

*Copyright &copy; 2026 Advanced Micro Devices, Inc. All rights reserved.*
