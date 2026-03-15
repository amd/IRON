# IRON-Lemonade Integration - Living Document

**Document Status:** Active
**Last Updated:** 2026-03-15
**Authors:** IRON Development Team
**Reviewers:** TBD

---

## Executive Summary

This document tracks the integration of IRON (AMD Ryzen AI NPU framework) into Lemonade (LLM inference server) as a cross-platform backend. The integration enables OpenAI-compatible API endpoints for Llama-3 and other models running on AMD Ryzen AI NPUs.

### Key Decision: Dual-Backend Strategy

After strategic analysis, we are pursuing a **Dual-Backend Strategy**:

| Platform | Runtime | Kernel Format | Compilation |
|----------|---------|---------------|-------------|
| **Linux** | XRT (Xilinx Runtime) | .xclbin | Runtime via MLIR-AIE |
| **Windows** | xDNA Runtime | .xclbin | Pre-compiled (FastFlowLM) |

**Rationale:** The `.xclbin` format is cross-platform (works on both Windows and Linux), but the runtime loading it differs. This approach leverages existing compiled kernels while maintaining flexibility.

---

## Table of Contents

1. [Current State Assessment](#1-current-state-assessment)
2. [Strategic Analysis](#2-strategic-analysis)
3. [Architecture Design](#3-architecture-design)
4. [Implementation Plan](#4-implementation-plan)
5. [Task Tracking](#5-task-tracking)
6. [Technical Reference](#6-technical-reference)
7. [Decision Log](#7-decision-log)

---

## 1. Current State Assessment

### 1.1 Completed Work (IRON Python API)

**Location:** `iron/api/`

| File | Status | Description |
|------|--------|-------------|
| `server.py` | Complete | FastAPI server with OpenAI-compatible endpoints |
| `auto_converter.py` | Complete | Auto model conversion with caching |
| `model_registry.py` | Complete | Model lifecycle management |
| `tokenizers.py` | Complete | Tokenizer utilities (Llama-3, Mistral, Phi, Gemma) |
| `__init__.py` | Complete | Package exports |

**Key Features:**
- GET `/v1/models` - List available models
- POST `/v1/chat/completions` - Chat completion (streaming + non-streaming)
- POST `/v1/completions` - Legacy completion
- GET `/health` - Health check
- Auto-model loading on first request
- Model caching at `~/.cache/iron/models/`

### 1.2 IRON Operator Library

**Location:** `iron/operators/`

IRON has a comprehensive operator library with MLIR-based compilation:

| Operator | Status | Architecture |
|----------|--------|--------------|
| Conv3D | Complete | AIE2 + AIE2P |
| GEMM | Complete | AIE2 + AIE2P |
| RoPE | Complete | AIE2 + AIE2P |
| SwiGLU | Complete | AIE2 + AIE2P |
| RMSNorm | Complete | AIE2 + AIE2P |
| MHA | Complete | AIE2 + AIE2P |
| LayerNorm | Complete | AIE2 + AIE2P |
| Softmax | Complete | AIE2 + AIE2P |
| Element-wise ops | Complete | AIE2 + AIE2P |

### 1.3 Compilation System Analysis

**Location:** `iron/common/compilation.py`, `iron/common/aie_base.py`

**Current Compilation Flow:**
```
Python Operator Design (.py)
    ↓
MLIR Generation (Python callbacks)
    ↓
aiecc.py compilation
    ↓
.xclbin + insts.bin generation
    ↓
XRT runtime loading
    ↓
NPU execution
```

**Key Classes:**
- `AIEOperatorBase` - Base class for all AIE operators
- `AIEContext` - Manages compilation and runtime state
- `XclbinArtifact` - Represents compiled .xclbin files
- `InstsBinArtifact` - Represents instruction binaries

**Critical Finding:** IRON currently:
1. Compiles MLIR to .xclbin at **runtime** (via `aiecc.py`)
2. Loads .xclbin via **XRT** (Linux only)
3. Uses `pyxrt` Python bindings for kernel execution

### 1.4 Reference Application

**Location:** `iron/applications/llama_3.2_1b/`

The Llama-3.2-1B application demonstrates end-to-end inference:
- Model loading from safetensors
- AIE operator preparation
- Runtime compilation
- Token generation loop

**Key Insight:** The application uses `AIEOperatorBase.get_default_context()` to:
1. `compile_all()` - Compile all operators
2. `prepare_runtime()` - Set up XRT runtime

---

## 2. Strategic Analysis

### 2.1 Problem Statement

**Goal:** Integrate IRON into Lemonade as a cross-platform backend (Windows + Linux).

**Challenge:** NPU runtimes are platform-specific:
- **Linux:** XRT (Xilinx Runtime) - open source, well documented
- **Windows:** xDNA Runtime - proprietary, limited documentation

**Constraint:** Lemonade's backend architecture uses C++ `WrappedServer` interface.

### 2.2 Options Analysis (Updated 2026-03-15)

**CRITICAL INTELLIGENCE UPDATE:** FastFlowLM production infrastructure discovered at `C:\Program Files\flm`:
- 30+ model families with pre-compiled .xclbin files
- Production Windows NPU runtime (DLLs for gemm, mha, dequant, lm_head)
- Model-family DLLs (llama_npu.dll, qwen3_npu.dll, gpt_oss_npu.dll, etc.)
- GPT-OSS-20B-NPU2 proves 20B parameter deployment works (14GB footprint)
- HuggingFace distribution: `FastFlowLM/<model-name>` with versioned releases

| Option | Description | Pros | Cons | Recommendation |
|--------|-------------|------|------|----------------|
| **Option B+ (FastFlowLM-Enhanced Hybrid)** | Leverage FFLM .xclbins + DLLs with IRON abstraction layer | 4-6 week MVP, production-proven kernels, maintains independence | Medium partnership dependency | ✅ **SELECTED** |
| 1. Dual-Backend (Original) | XRT on Linux, xDNA on Windows (build from scratch) | Maximum control | 10-14 weeks, rebuilds existing infrastructure | ❌ Deferred |
| 2. XRT Only | Linux-only backend | Simpler, single codebase | No Windows support | ❌ Reject |
| 3. Full FastFlowLM Dependency | Use FastFlowLM runtime directly | Fastest (2-3 weeks) | High external dependency | ❌ Reject |
| 4. OGA/ONNX Port | Port to ONNX/OGA format | Microsoft ecosystem | 12-16 weeks, loses .xclbin investment | ❌ Reject |

### 2.3 Risk Register (Updated 2026-03-15)

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| R1: FastFlowLM licensing blocks redistribution | Low | Critical | **IMMEDIATE:** Legal review of FastFlowLM terms |
| R2: FastFlowLM .xclbin kernel interface changes | Medium | Medium | Abstraction layer version detection |
| R3: FFLM DLLs undocumented API | Medium | Medium | Reverse-engineer via usage, contact AMD |
| R4: Cross-platform .xclbin incompatibility | Low | High | Early Linux testing of FFLM .xclbins |
| R5: Partnership dependency (FFLM team) | Medium | Medium | Maintain MLIR fallback path |
| R6: Original xDNA runtime API gaps | Low | Medium | FFLM DLLs already solve this |

---

## 3. Architecture Design

### 3.1 High-Level Architecture (Updated 2026-03-15 - Option B+)

```
┌─────────────────────────────────────────────────────────────────┐
│                      Lemonade Server                             │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              OpenAI-Compatible API Layer                   │  │
│  │     /v1/chat/completions  /v1/completions  /v1/models      │  │
│  └──────────────────────────┬────────────────────────────────┘  │
│                             │                                    │
│  ┌──────────────────────────▼────────────────────────────────┐  │
│  │              IronServer (C++ Backend Wrapper)              │  │
│  │  Inherits from: WrappedServer                              │  │
│  │  Implements: load(), unload(), chat_completion(), etc.     │  │
│  └──────────────────────────┬────────────────────────────────┘  │
└─────────────────────────────┼────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
┌────────▼────────┐  ┌────────▼────────┐  ┌───────▼───────┐
│  PlatformUtils  │  │  XclbinLoader   │  │ BufferManager │
│  (detection)    │  │  (.xclbin)      │  │ (memory)      │
└────────┬────────┘  └────────┬────────┘  └───────┬───────┘
         │                    │                    │
         └────────────────────┼────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
┌────────▼────────┐  ┌────────▼────────┐  ┌───────▼───────┐
│  XrtRuntime     │  │  FflmRuntime    │  │  MlirRuntime  │
│  (Linux)        │  │  (Windows)      │  │  (Fallback)   │
│  - Load .xclbin │  │  - FFLM DLLs    │  │  - aiecc.py   │
│  - XRT BOs      │  │  - .xclbin      │  │  - Custom     │
│  - MLIR option  │  │  - Pre-compiled │  │               │
└─────────────────┘  └─────────────────┘  └───────────────┘
       │                    │
       │                    │
┌──────▼────────┐   ┌───────▼────────┐
│ FFLM .xclbin  │   │ FFLM DLLs      │
│ (cross-plat)  │   │ (Windows)      │
└───────────────┘   └────────────────┘
```

### 3.2 Component Specifications

#### 3.2.1 IXclbinRuntime (Abstract Interface)

**File:** `iron/runtime/ixclbin_runtime.h`

```cpp
class IXclbinRuntime {
public:
    virtual ~IXclbinRuntime() = default;

    // Load .xclbin kernel package
    virtual bool load_xclbin(const std::string& path) = 0;

    // Execute kernel with input tensors
    virtual ExecutionResult execute(
        const std::string& kernel_name,
        const std::vector<TensorBuffer>& inputs) = 0;

    // Unload all kernels
    virtual void unload() = 0;

    // Get available kernels
    virtual std::vector<std::string> get_kernel_names() const = 0;

    // Check if loaded
    virtual bool is_loaded() const = 0;

    // Platform name
    virtual std::string get_platform_name() const = 0;

    // Factory method
    static std::unique_ptr<IXclbinRuntime> create();
};
```

#### 3.2.2 Platform Detection

**File:** `iron/runtime/platform_utils.h`

```cpp
enum class Platform {
    WINDOWS_XDNA,
    LINUX_XRT,
    UNKNOWN
};

class PlatformUtils {
public:
    static constexpr Platform get_current_platform() {
#ifdef _WIN32
        return Platform::WINDOWS_XDNA;
#elif defined(__linux__)
        return Platform::LINUX_XRT;
#else
        return Platform::UNKNOWN;
#endif
    }

    static std::string get_platform_name();
    static std::string get_default_xclbin_path();
    static std::string get_xrt_path();  // Linux only
    static bool validate_environment();
};
```

#### 3.2.3 XclbinLoader

**File:** `iron/runtime/xclbin_loader.h`

Manages .xclbin lifecycle:
- Loading and parsing .xclbin files
- Kernel discovery and validation
- Execution with argument binding
- Resource cleanup

#### 3.2.4 IronServer (Lemonade Backend)

**File:** `src/cpp/server/backends/iron_server.cpp` (in Lemonade repo)

Inherits from `WrappedServer`:
```cpp
class IronServer : public WrappedServer {
    void load(...) override;
    void unload() override;
    json chat_completion(const json& request) override;
    json completion(const json& request) override;
    json responses(const json& request) override;
    static bool is_available();
};
```

### 3.3 Data Flow

**Request Flow:**
```
1. OpenAI API Request (HTTP POST)
        ↓
2. Lemonade Server (FastAPI)
        ↓
3. IronServer::chat_completion()
        ↓
4. Apply chat template → prompt
        ↓
5. Tokenize prompt
        ↓
6. Inference loop:
   - Execute GEMM → RoPE → SwiGLU → RMSNorm
   - Sample next token
   - Repeat until EOS/max_tokens
        ↓
7. Detokenize output
        ↓
8. Format OpenAI response
        ↓
9. Return JSON response
```

---

## 4. Implementation Plan

### 4.1 Phase Breakdown (Updated 2026-03-15 - Option B+)

| Phase | Description | Duration | Dependencies |
|-------|-------------|----------|--------------|
| **Phase 0** | FastFlowLM Legal/Licensing Review | Week 1 | None |
| **Phase 1** | Core Infrastructure + FFLM Integration | Weeks 2-3 | Phase 0 |
| **Phase 2** | Windows FFLM Runtime Backend | Weeks 4-6 | Phase 1 |
| **Phase 3** | Linux XRT Backend (FFLM .xclbins) | Weeks 5-7 | Phase 1 |
| **Phase 4** | Lemonade Integration | Weeks 8-10 | Phase 2, Phase 3 |

### 4.2 Phase 0: FastFlowLM Legal/Licensing Review (Week 1)

**Goal:** Clear legal path for FastFlowLM integration

**Deliverables:**
- [ ] Legal review of FastFlowLM licensing terms
- [ ] Redistribution rights assessment
- [ ] Partnership contact with AMD/FastFlowLM team
- [ ] Go/No-Go decision based on licensing

**Success Criteria:**
- Legal clearance to use FastFlowLM .xclbin files
- Redistribution rights confirmed (or alternative path identified)
- AMD/FastFlowLM team contact established

**BLOCKER:** Phase 1 cannot start without legal clearance

### 4.3 Phase 1: Core Infrastructure + FFLM Integration (Weeks 2-3)

**Goal:** Establish cross-platform foundation with FastFlowLM integration

**Deliverables:**
- [ ] `iron/runtime/platform_utils.h/cpp` - Platform detection
- [ ] `iron/runtime/ixclbin_runtime.h` - Cross-platform interface
- [ ] `iron/runtime/fflm_runtime.h/cpp` - FastFlowLM DLL wrapper (Windows)
- [ ] `iron/runtime/xclbin_loader.h/cpp` - .xclbin loader framework
- [ ] `iron/CMakeLists.txt` - CMake configuration
- [ ] `iron/runtime/CMakeLists.txt` - Runtime CMake configuration
- [ ] FastFlowLM .xclbin file inventory and copying mechanism

**Success Criteria:**
- Platform detection compiles on Windows and Linux
- IXclbinRuntime interface defined
- FastFlowLM DLL loading works on Windows
- Can enumerate available FFLM kernels

### 4.4 Phase 2: Windows FFLM Runtime Backend (Weeks 4-6)

**Goal:** Functional Windows backend using FastFlowLM DLLs

**Deliverables:**
- [ ] `iron/runtime/fflm_runtime.h/cpp` - FastFlowLM DLL wrapper
- [ ] `iron/runtime/fflm_buffer_manager.h/cpp` - Buffer management via FFLM
- [ ] Kernel execution interface to FFLM DLLs
- [ ] Model-family DLL detection (llama_npu.dll, qwen3_npu.dll, etc.)
- [ ] Windows test suite with FFLM kernels

**Success Criteria:**
- Can load FFLM .xclbin files on Windows
- Can execute kernels via FFLM DLLs (gemm.dll, mha.dll, etc.)
- GEMM, RMSNorm, RoPE kernels execute successfully
- Performance within 20% of native FFLM runtime

### 4.5 Phase 3: Linux XRT Backend with FFLM .xclbins (Weeks 5-7)

**Goal:** Functional Linux backend using FastFlowLM .xclbin files with XRT

**Deliverables:**
- [ ] `iron/runtime/xrt_runtime.h/cpp` - XRT runtime implementation
- [ ] `iron/runtime/xrt_buffer_manager.h/cpp` - Buffer management
- [ ] FFLM .xclbin loading mechanism for Linux
- [ ] Cross-platform .xclbin compatibility verification
- [ ] Linux test suite with FFLM kernels

**Success Criteria:**
- Can load FFLM .xclbin files on Linux via XRT
- Can execute GEMM, RMSNorm, RoPE kernels
- Same .xclbin files work on both Linux and Windows
- Performance within 20% of Windows FFLM runtime

### 4.6 Phase 4: Lemonade Integration (Weeks 8-10)

**Goal:** End-to-end integration with Lemonade

**Deliverables:**
- [ ] `src/cpp/include/lemon/backends/iron_server.h` - Backend wrapper
- [ ] `src/cpp/server/backends/iron_server.cpp` - Backend implementation
- [ ] `tests/iron_backend_test.cpp` - Integration tests
- [ ] `docs/IRON_LEMONADE_DEPLOYMENT.md` - Deployment guide
- [ ] Performance benchmarking suite

**Success Criteria:**
- Lemonade can load IRON backend
- OpenAI API endpoints work end-to-end
- Streaming and non-streaming responses functional
- Performance meets MVP targets

---

### 4.7 FastFlowLM Kernel Inventory (Reference)

**Available Kernel Families (from C:\Program Files\flm\xclbins\):**

| Model Family | Kernel Files | Parameters | Context | Footprint |
|-------------|--------------|------------|---------|-----------|
| Llama-3.2-1B-NPU2 | attn, dequant, layer, mm | 1B | 131K | 1.3 GB |
| Llama-3.2-3B-NPU2 | attn, dequant, layer, mm | 3B | 65K | 2.7 GB |
| Llama-3.1-8B-NPU2 | attn, dequant, layer, mm | 8B | 16K | 5.4 GB |
| GPT-OSS-20B-NPU2 | attn, dequant, expert, layer, mm, short_seq_mm | 20B | 8K | 14 GB |
| Qwen3-8B-NPU2 | attn, dequant, layer, mm | 8B | 16K | 5.6 GB |
| Gemma3-4B-NPU2 | attn, dequant, layer, mm | 4B | 65K | 4.5 GB |
| Phi4-mini-NPU2 | attn, dequant, layer, mm | 4B | 32K | 3.4 GB |

**Shared Operator DLLs (C:\Program Files\flm\):**
- `gemm.dll` - General matrix multiplication
- `mha.dll` - Multi-head attention
- `dequant.dll` - Q4 quantization handling
- `lm_head.dll` - Language model head projection

**Model-Family DLLs:**
- `llama_npu.dll`, `qwen3_npu.dll`, `gemma_npu.dll`, `gpt_oss_npu.dll`, `phi4_npu.dll`

### Current Tasks

| ID | Subject | Status | Blocked By |
|----|---------|--------|------------|
| #22 | Create OpenAI-compatible API server | Complete | - |
| #23 | Add automatic model conversion | Complete | - |
| #24 | Create iron/api package structure | Complete | - |
| #25 | Explore FastFlowLM .xclbin structure | Complete | - |
| #26 | Create IRON-Lemonade living document | In Progress | - |
| #27 | Implement Phase 1: Core runtime | Pending | #25, #26 |
| #28 | Implement Phase 2: Linux XRT | Pending | #27 |
| #29 | Implement Phase 3: Windows xDNA | Pending | #27 |
| #30 | Implement Phase 4: Lemonade wrapper | Pending | #27, #28, #29 |

### Task Dependencies

```
#25 (Exploration) ─┬─→ #27 (Phase 1) ─┬─→ #28 (Linux) ─┐
                   │                  │                │
#26 (Documentation)─┘                  │                ├─→ #30 (Lemonade)
                                       └─→ #29 (Windows)─┘
```

---

## 6. Technical Reference

### 6.1 Key File Locations

**IRON Repository:**
```
IRON/
├── iron/
│   ├── api/                    # Python API server (COMPLETE)
│   │   ├── server.py
│   │   ├── auto_converter.py
│   │   ├── model_registry.py
│   │   └── tokenizers.py
│   ├── runtime/                # C++ runtime (TO CREATE)
│   │   ├── platform_utils.h/cpp
│   │   ├── ixclbin_runtime.h
│   │   ├── xclbin_loader.h/cpp
│   │   ├── xrt_runtime.h/cpp
│   │   └── xdna_runtime.h/cpp
│   ├── operators/              # Operator library (COMPLETE)
│   │   ├── conv3d/
│   │   ├── gemm/
│   │   ├── rope/
│   │   └── ...
│   └── common/                 # Shared utilities
│       ├── aie_base.py
│       ├── aie_context.py
│       └── compilation.py
└── docs/
    └── IRON_LEMONADE_INTEGRATION.md  # This document
```

**Lemonade Repository (to create):**
```
lemonade/
└── src/cpp/
    ├── include/lemon/backends/
    │   └── iron_server.h
    └── server/backends/
        └── iron_server.cpp
```

### 6.2 Glossary

| Term | Definition |
|------|------------|
| **AIE** | AI Engine - AMD NPU compute array |
| **AIE2** | First-gen Ryzen AI NPU (4x4 array) |
| **AIE2P** | Second-gen Ryzen AI NPU (4x8 array) |
| **.xclbin** | Compiled FPGA/NPU kernel binary |
| **XRT** | Xilinx Runtime (Linux NPU stack) |
| **xDNA** | Windows NPU runtime stack |
| **MLIR-AIE** | MLIR dialect for AIE compilation |
| **FastFlowLM** | AMD's NPU inference engine |
| **Lemonade** | LLM inference server framework |
| **WrappedServer** | Lemonade backend interface |

### 6.3 External References

- [FastFlowLM GitHub](https://github.com/FastFlowLM/FastFlowLM)
- [Lemonade GitHub](https://github.com/lemonade-sdk/lemonade)
- [MLIR-AIE Documentation](https://github.com/Xilinx/mlir-aie)
- [XRT Documentation](https://xilinx.github.io/xrt/)

---

## 7. Decision Log

### 2026-03-15: Strategic Pivot to Option B+ (FastFlowLM-Enhanced Hybrid)

**Decision:** Abandon original Dual-Backend strategy in favor of FastFlowLM-leveraged approach.

**Rationale:**
1. FastFlowLM production infrastructure discovered at C:\Program Files\flm
2. 30+ model families with pre-compiled, production-proven kernels
3. GPT-OSS-20B-NPU2 proves 20B parameter deployment works
4. Building from scratch (Option C) would waste 6-8 weeks
5. FastFlowLM .xclbin files are cross-platform (Linux + Windows)

**New Architecture:**
- Windows: FastFlowLM DLL wrapper (fflm_runtime)
- Linux: XRT with FastFlowLM .xclbin files
- Fallback: IRON MLIR compilation for custom operators

**Participants:** Dr. Sarah Kim (Planning), Jordan Blake (Senior Developer)

**Action Items:**
- [ ] Phase 0: Legal review of FastFlowLM licensing (Week 1)
- [ ] Contact AMD/FastFlowLM team for partnership discussion
- [ ] Update TECHNICAL_DESIGN_DISCOVERY_PHASE.md with new direction
- [ ] Update DISCOVERY_PHASE_SUMMARY.md with FastFlowLM intelligence

### 2026-03-15: Dual-Backend Strategy Selected (ORIGINAL - SUPERSEDED)

**Decision:** Pursue Dual-Backend Strategy (XRT on Linux, xDNA on Windows)

**Rationale:**
1. .xclbin format is cross-platform
2. Leverages existing FastFlowLM pre-compiled kernels on Windows
3. Maintains IRON's runtime compilation flexibility on Linux
4. More feasible than OGA/ONNX port (12+ weeks)

**Alternatives Considered:**
- XRT-only (rejected: no Windows support)
- FastFlowLM dependency (rejected: external dependency)
- OGA/ONNX port (rejected: massive effort, loses IRON advantages)

**Participants:** Dr. Sarah Kim (Planning), Jordan Blake (Senior Developer)

### 2026-03-15: C++ Runtime Layer

**Decision:** Create C++ runtime layer instead of using Python API server directly

**Rationale:**
1. Lemonade uses C++ `WrappedServer` interface
2. Direct XRT/xDNA access requires native code
3. Python GIL would limit performance
4. C++ provides better control over memory and execution

**Implications:**
- Existing Python API server remains as development tool
- C++ runtime is new code, not a port
- Lemonade integration requires C++ backend wrapper

---

## Appendix A: Exploration Findings (2026-03-15)

### A.1 .xclbin File Analysis

**Finding:** No .xclbin files exist in the IRON codebase.

**Reason:** IRON compiles .xclbin at **runtime** from MLIR using `aiecc.py`.

**Implication:** For Windows support, we need pre-compiled .xclbin files (from FastFlowLM or custom compilation).

### A.2 Current Kernel Loading Flow

```python
# From iron/common/aie_base.py
def compile(self):
    self.set_up_artifacts()
    compilation_rules = [
        GenerateMLIRFromPythonCompilationRule(),
        PeanoCompilationRule(),
        ArchiveCompilationRule(),
        AieccCompilationRule(),  # Generates .xclbin
    ]
    compile(compilation_rules, self.artifacts)

# From iron/common/aie_context.py
def prepare_runtime(self):
    for op in self.operators:
        op.set_up_runtime()
        for kernel_name, (xclbin, xclbin_kernel_name, insts) in op.kernels.items():
            handle = self.device_manager.get_kernel_handle(
                str(xclbin.path), xclbin_kernel_name, str(insts.path)
            )
            op.xrt_kernels[kernel_name] = (
                handle.context,
                handle.kernel,
                handle.insts_bo,
                len(handle.insts),
            )
```

### A.3 FastFlowLM .xclbin Locations

Per user guidance, FastFlowLM .xclbin files are located at:
- **Linux:** `~/.config/flm/models/<model-name>/src/xclbins/`
- **Windows:** `C:\ProgramData\AMD\FastFlowLM\kernels\`

**Typical files:**
- `attn.xclbin` - Attention mechanism kernels
- `layer.xclbin` - Transformer layer kernels
- `lm_head.xclbin` - Language model head kernels
- `dequant.xclbin` - Dequantization kernels

---

**END OF DOCUMENT**
