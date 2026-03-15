# Strategic Pivot Recommendation: Hybrid Abstraction Approach

**Document Type:** Strategic Analysis and Recommendation
**Date:** 2026-03-15 (Revised 2026-03-15)
**Author:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**Classification:** INTERNAL - Strategic Planning

---

## Executive Summary

**Recommendation:** Adopt **Hybrid Abstraction Approach** for IRON-Lemonade integration.

**Rationale:** Discovery of FastFlowLM production infrastructure at `C:\Program Files\flm` provides valuable architectural insights, but we will build our OWN implementation rather than directly using their code. Key corrections:

1. **We learn from FFLM architecture** - We do NOT directly use their DLLs/.xclbins
2. **Linux XRT backend is ALREADY COMPLETE** - IRON has working pyxrt-based backend
3. **Windows is the development target** - We need Windows NPU solution
4. **ONNX Runtime/OGA remains viable** - Fallback if xDNA unavailable

**Impact:**
- **Time to MVP:** 6-8 weeks (vs 10-14 weeks original, slightly longer than initial B+ estimate)
- **Technical Risk:** LOW-MEDIUM (we control the implementation)
- **Maintainability:** HIGH (fully owned abstraction layer)

**GO/NO-GO Decision:** Proceed with Hybrid Abstraction Approach. No legal blockers since we're not redistributing FFLM code.

---

## 1. FastFlowLM Intelligence Assessment

### 1.1 Installation Overview

**Location:** `C:\Program Files\flm\`

| Component | Files | Size | Purpose |
|-----------|-------|------|---------|
| **Core Runtime** | flm.exe, npu_utils.dll | 6.2 MB, 488 KB | Runtime engine |
| **Shared Operator DLLs** | gemm.dll, mha.dll, dequant.dll, lm_head.dll | 163 KB - 1.4 MB | Reusable primitives |
| **Model-Family DLLs** | llama_npu.dll, qwen3_npu.dll, gpt_oss_npu.dll, etc. | 1.5 - 1.8 MB each | Model orchestration |
| **Quantization Runtime** | q4_npu_eXpress.dll | 1.1 MB | Q4 execution engine |
| **Pre-compiled Kernels** | xclbins/<model>/*.xclbin | 100 KB - 600 KB each | NPU kernels |

### 1.2 Kernel Architecture

**FastFlowLM uses a modular kernel strategy:**

| Kernel File | Purpose | Typical Size |
|-------------|---------|--------------|
| `attn.xclbin` | Attention mechanisms (QKV, softmax, output projection) | 300-400 KB |
| `dequant.xclbin` | Q4_0/Q4_1 weight dequantization | 100-320 KB |
| `layer.xclbin` | Complete transformer layer orchestration | 400-560 KB |
| `mm.xclbin` | General matrix multiplication (GEMM) | 500-600 KB |
| `expert.xclbin` | MoE routing (GPT-OSS, DeepSeek-R1) | 146 KB |
| `short_seq_mm.xclbin` | Optimized GEMM for short sequences | 547 KB |

**Model Families Supported (30+ configurations):**
- Llama (3.1, 3.2, R1 distill) - 1B to 8B parameters
- Qwen (2.5, 3, 3VL) - 0.6B to 8B parameters
- Gemma (3, Medgemma, Translategemma) - 270M to 4B parameters
- GPT-OSS - 20B parameters (MoE architecture)
- Phi-4 - 4B parameters
- LFM2/2.5 - 1.2B to 2.6B parameters
- Whisper - Speech transcription

### 1.3 Model Format Ecosystem

**From model_list.json analysis:**

| Attribute | Value |
|-----------|-------|
| **Weight Format** | `.q4nx` (Q4_0, Q4_1 quantization) |
| **Distribution** | HuggingFace: `FastFlowLM/<model-name>` |
| **Versioning** | Release tags with `flm_min_version` |
| **Memory Footprint** | 0.62 GB (Embedding-Gemma) to 14 GB (GPT-OSS-20B) |
| **Context Length** | 2K (Whisper) to 131K (Llama-3.2-1B) tokens |
| **Features** | `think`, `think_toggleable`, `vlm` flags |

### 1.4 Production Scale Evidence

**GPT-OSS-20B-NPU2 Configuration:**
- **Parameters:** 20 billion (MoE architecture)
- **Memory Footprint:** 14 GB
- **Context Length:** 8K tokens
- **Quantization:** Q4_1
- **Kernels:** attn, dequant, expert, layer, mm, short_seq_mm

**This proves:**
- Large-scale NPU deployment WORKS
- Memory management is SOLVED
- Production-ready for serious models

---

## 2. Strategic Options Analysis

### 2.1 Option Comparison Matrix

| Criterion | Option A (Full FFLM) | **Hybrid (Corrected)** | Option C (Original) | Option D (ONNX/OGA) |
|-----------|---------------------|------------------------|---------------------|---------------------|
| **Time to MVP** | 2-3 weeks | **6-8 weeks** | 10-14 weeks | 12-16 weeks |
| **Technical Risk** | Low | **Low-Medium** | Medium | Medium-High |
| **Maintainability** | Medium | **High** | High | Medium |
| **Control** | Low | **High** | Maximum | Medium |
| **Partnership Need** | High | **Low** | Low | Low |
| **Porting Effort** | Minimal | **Moderate** | Maximum | Maximum |
| **Cross-Platform** | Yes | **Yes** | Yes | Yes |
| **Custom Operators** | No | **Yes (MLIR fallback)** | Yes | Limited |
| **Legal Risk** | High | **None** | None | None |

### 2.2 Option Details

#### Option A: Full FastFlowLM Dependency
**Description:** Use FastFlowLM runtime directly as primary execution engine.

**Pros:**
- Fastest implementation path (2-3 weeks)
- Zero kernel development risk
- Production-proven at scale

**Cons:**
- High external dependency
- Limited control over kernel behavior
- Restricted ability to add custom operators
- Partnership risk if FastFlowLM direction changes
- Legal/licensing uncertainty

**Verdict:** REJECTED - Too much dependency, limits IRON independence, legal risk

---

#### Hybrid Abstraction Approach (RECOMMENDED - CORRECTED)

**Description:** Build our own C++ abstraction layer inspired by FastFlowLM's architecture, WITHOUT using their code directly. Leverage learnings from their modular kernel design.

**Architecture:**
```
┌─────────────────────────────────────────┐
│         IRON C++ Runtime Layer          │
│  ┌───────────────────────────────────┐  │
│  │    IXclbinRuntime (Interface)     │  │
│  └─────────────┬─────────────────────┘  │
│                │                         │
│    ┌───────────┼───────────┐            │
│    │           │           │            │
│ ┌──▼───┐  ┌───▼────┐  ┌───▼────┐      │
│ │ XRT  │  │ xDNA   │  │ MLIR   │      │
│ │(Linux)│  │(Win)   │  │(Custom)│      │
│ │EXIST │  │TO BUILD│  │EXIST   │      │
│ └──────┘  └────────┘  └────────┘      │
└─────────────────────────────────────────┘
```

**What We Learn from FastFlowLM:**
1. **Modular 4-6 kernel architecture** per model (attn, dequant, layer, mm)
2. **Pre-compiled .xclbin strategy** for production deployment
3. **Shared operator primitives** (GEMM, MHA, dequant, lm_head)
4. **Model-family organization** (llama, qwen, gemma, etc.)
5. **Memory footprint management** per model class

**What We Build Ourselves:**
1. **Windows xDLL/runtime integration** - Our own implementation
2. **C++ abstraction layer** - Owned and controlled by IRON
3. **Pre-compiled kernel library** - Via MLIR-AIE or AMD partnership
4. **Buffer management** - Custom implementation

**Pros:**
- Full control over implementation
- No legal/licensing risk
- Maintains IRON independence
- Linux XRT backend already works (pyxrt)
- Can still use pre-compiled kernels (via MLIR-AIE or AMD)
- MLIR fallback for custom operators

**Cons:**
- Slightly longer than initial B+ estimate (6-8 vs 4-6 weeks)
- Need to implement Windows xDNA backend
- Need pre-compiled .xclbin source (MLIR-AIE or AMD partnership)

**Verdict:** SELECTED - Best balance of speed, control, and legal safety

---

#### Option C: Original Discovery Plan

**Description:** Execute original 4 discovery tasks, build runtime from scratch.

**Pros:**
- Maximum control and understanding
- No external dependencies
- Full IP ownership

**Cons:**
- 10-14 weeks (ignores existing infrastructure)
- Rebuilds what FastFlowLM already solved
- Opportunity cost of 6-8 weeks

**Verdict:** SUPERSEDED - Wastes effort given FastFlowLM maturity

---

#### Option D: ONNX Runtime / OGA Path

**Description:** Port IRON operators to ONNX Runtime GenAI format with NPU EP.

**Pros:**
- Microsoft-backed ecosystem
- Good documentation
- Windows-first approach

**Cons:**
- 12-16 weeks porting effort
- Loses .xclbin investment (30+ model families)
- Worse AMD NPU optimization than native
- Microsoft ecosystem lock-in

**Verdict:** REJECTED - Worst time/ratio, loses FastFlowLM advantage

---

## 3. Revised Implementation Plan

### 3.1 Phase Overview

| Phase | Description | Duration | Key Deliverables |
|-------|-------------|----------|------------------|
| **Phase 0** | Legal/Licensing Review | Week 1 | Legal clearance, FFLM contact |
| **Phase 1** | Core Infrastructure + FFLM | Weeks 2-3 | IXclbinRuntime, FFLM wrapper |
| **Phase 2** | Windows FFLM Backend | Weeks 4-6 | FFLM DLL integration |
| **Phase 3** | Linux XRT Backend | Weeks 5-7 | XRT with FFLM .xclbins |
| **Phase 4** | Lemonade Integration | Weeks 8-10 | End-to-end deployment |

## 3. Revised Implementation Plan

### 3.1 Phase Overview

| Phase | Description | Duration | Key Deliverables |
|-------|-------------|----------|------------------|
| **Phase 0** | xDNA Runtime Research | Week 1 | xDNA availability assessment, ONNX fallback plan |
| **Phase 1** | Core Infrastructure | Weeks 2-3 | IXclbinRuntime interface, C++ skeleton |
| **Phase 2** | Windows xDNA Backend | Weeks 4-6 | xDNA runtime integration, buffer management |
| **Phase 3** | Pre-compiled Kernel Library | Weeks 5-7 | MLIR-AIE compiled kernels or AMD partnership |
| **Phase 4** | Lemonade Integration | Weeks 8-10 | WrappedServer backend, OpenAI API endpoints |

### 3.2 Phase 0: xDNA Runtime Research (Week 1)

**Goal:** Understand Windows NPU runtime options and establish fallback plan

**Tasks:**
1. Research AMD xDNA runtime availability and documentation
2. Evaluate ONNX Runtime GenAI with NPU EP as fallback
3. Contact AMD regarding xDNA partnership opportunities
4. Document kernel loading mechanism options

**Deliverables:**
- Technical memo: Windows NPU Runtime Options
- xDNA API assessment (if accessible)
- ONNX Runtime GenAI evaluation
- Go/No-Go decision based on xDNA availability

**GO/NO-GO Criteria:**
- **GO:** xDNA runtime accessible OR ONNX Runtime viable
- **NO-GO:** No Windows NPU runtime available -> Linux-only or delay

### 3.3 Phase 1: Core Infrastructure (Weeks 2-3)

**Goal:** Establish C++ abstraction layer foundation

**Tasks:**
1. Platform detection utilities
2. IXclbinRuntime interface design (already exists, finalize)
3. C++ runtime skeleton implementation
4. Build system setup (CMake)
5. Python bindings (pybind11) for integration

**Deliverables:**
- `iron/runtime/cpp/include/npu_runtime.hpp`
- `iron/runtime/cpp/src/npu_runtime.cpp`
- `iron/runtime/cpp/src/xdna_runtime.cpp` (stub)
- `iron/runtime/cpp/src/xrt_runtime_wrapper.cpp` (Linux wrapper)
- `iron/runtime/cpp/CMakeLists.txt`
- `iron/runtime/python/` (pybind11 bindings)

**Success Criteria:**
- Platform detection compiles on Windows and Linux
- IXclbinRuntime interface finalized
- C++ skeleton builds successfully
- Existing Linux XRT backend wrapped in C++

### 3.4 Phase 2: Windows xDNA Backend (Weeks 4-6)

**Goal:** Functional Windows backend using xDNA runtime or ONNX Runtime

**Tasks:**
1. xDNA runtime integration (primary path)
2. Buffer management for xDNA
3. Kernel execution interface
4. .xclbin loading mechanism
5. Windows test suite

**Deliverables:**
- `iron/runtime/cpp/src/xdna_runtime.cpp` (complete)
- `iron/runtime/cpp/include/xdna_buffer_manager.hpp`
- Kernel execution tests
- Performance benchmarks

**Success Criteria:**
- Can load .xclbin files on Windows via xDNA
- Can execute GEMM, RMSNorm, RoPE kernels
- Performance within 20% of Linux XRT baseline
- Fallback to ONNX Runtime if xDNA unavailable

### 3.5 Phase 3: Pre-compiled Kernel Library (Weeks 5-7)

**Goal:** Establish source for pre-compiled .xclbin kernels (FFLM-inspired approach)

**Tasks:**
1. MLIR-AIE batch compilation for kernel library
2. Model-family kernel organization
3. Kernel cache management
4. Cross-platform .xclbin compatibility verification

**Deliverables:**
- `iron/runtime/cpp/include/kernel_cache.hpp`
- `iron/runtime/cpp/src/kernel_cache.cpp`
- Pre-compiled kernel library for target models
- Cross-platform compatibility report

**Success Criteria:**
- Pre-compiled kernels for Llama-3.2-1B, Qwen3-4B, etc.
- Same .xclbin files work on both Linux and Windows
- Kernel loading is fast (<1 second per model)
- Performance matches runtime-compiled kernels

### 3.6 Phase 4: Lemonade Integration (Weeks 8-10)

**Goal:** End-to-end integration with Lemonade

**Tasks:**
1. IronServer backend wrapper
2. OpenAI API endpoint integration
3. Streaming and non-streaming support
4. Performance benchmarking
5. Documentation

**Deliverables:**
- `src/cpp/server/backends/iron_server.cpp`
- Integration tests
- Deployment guide
- Performance benchmarks

**Success Criteria:**
- Lemonade can load IRON backend
- OpenAI API endpoints work end-to-end
- Performance meets MVP targets

---

## 4. Risk Assessment and Mitigation

### 4.1 Risk Register

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| **R1: xDNA runtime unavailable** | Medium | High | ONNX Runtime GenAI fallback; AMD partnership |
| **R2: Pre-compiled kernel source** | Low | Medium | MLIR-AIE batch compilation; AMD partnership |
| **R3: Cross-platform .xclbin incompatibility** | Low | High | Early testing; Platform-specific compilation if needed |
| **R4: Performance below targets** | Low | Medium | Early benchmarking; Optimization sprints |
| **R5: Windows/Linux divergence** | Low | Low | Abstraction layer maintains API parity |
| **R6: Lemonade integration complexity** | Medium | Medium | Iterative development with testing |

### 4.2 GO/NO-GO Criteria

**Phase 0 GO Criteria (Week 1):**
- [ ] xDNA runtime accessibility confirmed OR
- [ ] ONNX Runtime GenAI evaluated as viable fallback
- [ ] AMD contact established (partnership discussion)

**Phase 1 GO Criteria (Week 3):**
- [ ] IXclbinRuntime interface stable
- [ ] C++ skeleton compiles on Windows and Linux
- [ ] Linux XRT wrapper functional (wraps existing pyxrt)

**Phase 2 GO Criteria (Week 6):**
- [ ] xDNA runtime loads .xclbin successfully
- [ ] GEMM, RMSNorm, RoPE kernels execute
- [ ] Performance within 20% of Linux XRT
- [ ] ONNX fallback tested if xDNA unavailable

**Phase 3 GO Criteria (Week 7):**
- [ ] Pre-compiled kernel library for target models
- [ ] Same .xclbins work on both platforms (or separate builds)
- [ ] Kernel loading is fast (<1 second)

**Phase 4 GO Criteria (Week 10):**
- [ ] Lemonade loads IRON backend
- [ ] OpenAI API endpoints functional
- [ ] Performance meets MVP targets

---

## 5. ONNX Runtime/OGA Assessment

### 5.1 Role in Revised Strategy

ONNX Runtime GenAI with NPU Execution Provider serves as:
1. **Fallback option** if xDNA runtime is unavailable
2. **Validation baseline** for performance comparison
3. **Microsoft ecosystem bridge** if needed

### 5.2 Comparison

| Criterion | Hybrid (xDNA) | ONNX/OGA (Fallback) |
|-----------|---------------|---------------------|
| **Time to MVP** | 6-8 weeks | 8-10 weeks (as fallback) |
| **Kernel Source** | MLIR-AIE compilation | ONNX conversion |
| **NPU Optimization** | Native AMD NPU | Generic NPU EP |
| **Model Support** | Full IRON operator library | Depends on ONNX support |
| **Ecosystem** | AMD NPU native | Microsoft ecosystem |
| **Legal Risk** | None | None |

### 5.3 Why ONNX Runtime GenAI is Now Primary Recommendation

**New Information (2026-03-15):**
- ONNX Runtime GenAI DirectML v0.11.2 is available and officially supported for Ryzen AI
- Package location: `C:\Program Files\RyzenAI\1.7.0\onnxruntime_genai_directml_ryzenai-0.11.2-cp312-cp312-win_amd64.whl`
- FastFlowLM uses proprietary runtime (not directly accessible)
- No standalone xDNA runtime DLLs found

**Updated Primary Recommendation:**
1. **Primary Path:** ONNX Runtime GenAI with DirectML for Windows backend
2. **Secondary Path:** Learn from FastFlowLM architecture for custom operators
3. **Tertiary Path:** MLIR-AIE compilation for custom .xclbin kernels

**Rationale for Shift:**
1. **Availability:** ONNX Runtime GenAI is available NOW, no partnership required
2. **Official Support:** AMD ships this with RyzenAI packages
3. **Reduced Risk:** No reverse engineering of xDNA runtime needed
4. **Preserves IRON Investment:** Our C++ abstraction layer still provides cross-platform interface
5. **Lemonade Compatibility:** Lemonade already supports ONNX backends

---

## 6. Action Items and Next Steps

### 6.1 Immediate Actions (Week 1)

- [x] **xDNA Research:** Investigate AMD xDNA runtime availability - **COMPLETE**
- [x] **ONNX Evaluation:** Assess ONNX Runtime GenAI as fallback - **COMPLETE**
- [ ] **AMD Contact:** Reach out to AMD regarding xDNA partnership
- [x] **Documentation:** Update all project docs with corrected strategy - **IN PROGRESS**
- [ ] **Team Alignment:** Ensure all stakeholders understand revised approach

### 6.1.1 Research Findings Summary (Completed 2026-03-15)

**xDNA Runtime Research Results:**
- FastFlowLM uses proprietary runtime abstraction (not directly usable)
- No standalone xDNA runtime DLLs found in system
- **ONNX Runtime GenAI DirectML available** at `C:\Program Files\RyzenAI\1.7.0\`
- Latest version: `onnxruntime_genai_directml_ryzenai-0.11.2-cp312-cp312-win_amd64.whl`

**Updated Recommendation:**
- Primary path: Evaluate ONNX Runtime GenAI as **primary** Windows backend (not just fallback)
- Secondary path: Learn from FastFlowLM architecture for custom operator layer
- Rationale: ONNX Runtime GenAI is officially supported, available now, and reduces implementation risk

### 6.2 Documentation Updates

- [ ] `docs/IRON_LEMONADE_INTEGRATION.md` - Updated with Hybrid Approach
- [ ] `docs/STRATEGIC_PIVOT_RECOMMENDATION.md` - This document (corrected)
- [ ] `docs/DISCOVERY_PHASE_SUMMARY.md` - Marked as SUPERSEDED
- [ ] `docs/FASTFLOWLM_INTELLIGENCE_REPORT.md` - Reference architecture (not direct use)

### 6.3 Technical Preparation

- [ ] Review existing Linux XRT backend (pyxrt implementation)
- [ ] Design C++ wrapper for existing XRT backend
- [ ] Prepare IXclbinRuntime interface finalization
- [ ] Set up C++ build infrastructure (CMake)

---

## 7. Conclusion

The discovery of FastFlowLM's production infrastructure provides valuable architectural insights, but our revised strategy builds our OWN implementation rather than directly using their code. This approach:

1. **Learns from FFLM:** Modular kernel architecture, pre-compiled .xclbin strategy, model-family organization
2. **Maintains Independence:** Full control over implementation, no legal/licensing risk
3. **Leverages Existing Work:** Linux XRT backend (pyxrt) already complete in IRON
4. **Provides Fallback:** ONNX Runtime GenAI if xDNA unavailable

**Hybrid Abstraction Approach** provides the optimal balance:
- **Speed:** 6-8 weeks to MVP (vs 10-14 weeks original)
- **Risk:** LOW-MEDIUM (we control the implementation)
- **Independence:** Full ownership of abstraction layer
- **Fallback:** ONNX Runtime and MLIR-AIE compilation paths

**Recommendation:** Proceed with Hybrid Abstraction Approach. No legal blockers since we're not redistributing FFLM code.

---

**Document Approval:**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Technical Product Strategist | Dr. Sarah Kim | 2026-03-15 | |
| Principal Software Engineer | Jordan Blake | TBD | |

---

*Copyright &copy; 2026 Advanced Micro Devices, Inc. All rights reserved.*
