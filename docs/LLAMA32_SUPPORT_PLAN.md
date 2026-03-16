# Llama3.2 Support Implementation Plan

**Document Type:** Implementation Roadmap
**Date:** 2026-03-15
**Author:** IRON Engineering Team
**Version:** 1.0.0

---

## Executive Summary

This document outlines the implementation plan for full Llama3.2 support on the IRON NPU runtime framework. The plan addresses critical operator gaps, establishes performance targets, and defines a 90-day roadmap to production-ready Llama3.2 inference.

**Current Status:** 39% operator coverage (9/23 operators)
**Target Status:** 100% operator coverage for Llama3.2 core inference
**Timeline:** 90 days to production-ready implementation

---

## 1. Gap Analysis

### 1.1 Current Operator Coverage

| Category | Implemented | Required for Llama3.2 | Gap |
|----------|-------------|----------------------|-----|
| Convolution (Conv2D/Conv3D) | 8 | 0 (not used in Llama3.2) | ✅ N/A |
| GEMM (via ONNX) | 1 | Yes (QKV, MLP projections) | ✅ Complete |
| Normalization (RMSNorm) | 0 | Yes (layer norm) | 🔴 -1 |
| Activation (SiLU) | 0 | Yes (MLP gate) | 🔴 -1 |
| Attention (RoPE, Softmax) | 0 | Yes (positional, attention) | 🔴 -2 |
| Embedding | 0 | Yes (token lookup) | 🟡 -1 (can use ONNX) |

**Critical Gap:** 4 operators missing for minimal Llama3.2 support

### 1.2 Implementation Status by Component

| Component | Status | Ready for Llama3.2? |
|-----------|--------|---------------------|
| C++ Runtime Abstraction | ✅ Complete | Yes |
| ONNX Runtime GenAI Backend | ✅ Complete | Yes |
| XRT Backend (Linux) | ✅ Complete | Yes |
| Python Bindings (pybind11) | ✅ Complete | Yes |
| Conv2D/Conv3D Operators | ✅ Complete | Yes (for multimodal) |
| **RoPE Operator** | ❌ Not Started | **No** |
| **RMSNorm Operator** | ❌ Not Started | **No** |
| **SiLU Operator** | ❌ Not Started | **No** |
| **Softmax Operator** | ❌ Not Started | **No** |
| **Benchmark Suite** | ❌ Not Started | **No** |

---

## 2. Implementation Phases

### Phase 1: Critical Operators (Weeks 1-2)

**Goal:** Enable minimal Llama3.2 inference

| Task | Owner | Deliverable | Acceptance Criteria |
|------|-------|-------------|---------------------|
| **RoPE Implementation** | Kernel Team | `iron/operators/rope/rope_bf16.cpp` | Passes unit tests, <0.5ms latency |
| **RMSNorm Implementation** | Kernel Team | `iron/operators/normalization/rmsnorm_bf16.cpp` | Passes unit tests, <1ms latency |
| **SiLU Implementation** | Kernel Team | `iron/operators/activations/silu_bf16.cpp` | Passes unit tests, <0.3ms latency |
| **Softmax Implementation** | Kernel Team | `iron/operators/softmax/softmax_bf16.cpp` | Passes unit tests, <2ms latency |
| **Operator Integration** | Runtime Team | All operators registered in INpuRuntime | Python API accessible |

**Phase 1 Exit Criteria:**
- All 4 critical operators implemented and tested
- Python API functional: `from iron.operators import rope, rmsnorm, silu, softmax`
- Unit test coverage >90% for new operators

---

### Phase 2: Benchmark Suite (Weeks 3-4)

**Goal:** Establish performance baselines

| Task | Owner | Deliverable | Acceptance Criteria |
|------|-------|-------------|---------------------|
| **Benchmark Framework** | Performance Team | `iron/benchmarks/run.py` | Executable benchmark script |
| **TTFT Measurement** | Performance Team | TTFT metrics for Llama3.2-1B | Baseline established |
| **Token Speed Measurement** | Performance Team | tokens/sec metrics | Baseline established |
| **Memory Profiling** | Performance Team | Memory usage breakdown | Baseline established |
| **Operator Latency Profiling** | Performance Team | Per-operator latency | All 4 critical operators profiled |

**Phase 2 Exit Criteria:**
- `BENCHMARK_RESULTS.md` populated with measurements
- Performance dashboard operational
- Weekly benchmark automation in place

---

### Phase 3: End-to-End Integration (Weeks 5-6)

**Goal:** Full Llama3.2 inference chain

| Task | Owner | Deliverable | Acceptance Criteria |
|------|-------|-------------|---------------------|
| **Model Loader** | Runtime Team | `iron/models/llama32.py` | Can load Llama3.2-1B weights |
| **Tokenizer Integration** | Runtime Team | HuggingFace tokenizer support | Tokenizer functional |
| **KV Cache Management** | Runtime Team | Paged KV cache implementation | 128+ token context supported |
| **Generation Loop** | Runtime Team | Autoregressive generation | Can generate 128+ tokens |
| **OpenAI API Integration** | API Team | `/v1/chat/completions` with Llama3.2 | API returns valid completions |

**Phase 3 Exit Criteria:**
- End-to-end Llama3.2-1B inference working
- Can generate coherent responses to prompts
- TTFT <200ms (initial target, optimize later)

---

### Phase 4: Performance Optimization (Weeks 7-10)

**Goal:** Meet performance targets

| Task | Owner | Deliverable | Acceptance Criteria |
|------|-------|-------------|---------------------|
| **RoPE Optimization** | Kernel Team | Optimized RoPE kernel | <0.5ms latency |
| **RMSNorm Optimization** | Kernel Team | Optimized RMSNorm kernel | <1ms latency |
| **Operator Fusion** | Kernel Team | Fused SiLU+Linear kernel | 20% MLP speedup |
| **KV Cache Optimization** | Runtime Team | Paged attention | 50% memory reduction |
| **Graph Optimization** | Runtime Team | Operator fusion, constant folding | 10% end-to-end speedup |

**Phase 4 Exit Criteria:**
- TTFT <100ms
- Token generation >20 tok/s
- Memory footprint <1.5GB for Llama3.2-1B

---

### Phase 5: Production Hardening (Weeks 11-12)

**Goal:** Production-ready implementation

| Task | Owner | Deliverable | Acceptance Criteria |
|------|-------|-------------|---------------------|
| **Stress Testing** | QA Team | 24-hour stability test | No memory leaks, no crashes |
| **Error Handling** | Runtime Team | Graceful error recovery | Invalid input handled properly |
| **Documentation** | Technical Writing | User guide, API reference | Complete documentation |
| **Example Applications** | API Team | Sample chatbot, completion API | Working examples |
| **CI/CD Integration** | DevOps | Automated testing | All tests pass on PR |

**Phase 5 Exit Criteria:**
- All acceptance tests passing
- Documentation complete
- Ready for external beta testing

---

## 3. Technical Specifications

### 3.1 Llama3.2 Model Variants

| Model | Parameters | Hidden Size | Layers | Heads | Max Context |
|-------|------------|-------------|--------|-------|-------------|
| **Llama3.2-1B** | 1.23B | 2048 | 16 | 32 | 128K |
| **Llama3.2-3B** | 3.21B | 3072 | 28 | 24 | 128K |

**Initial Target:** Llama3.2-1B (smaller memory footprint, faster iteration)

### 3.2 Operator Specifications

#### RoPE (Rotary Positional Embedding)

```cpp
// File: iron/operators/rope/rope_bf16.hpp
#pragma once

#include <cstdint>

namespace iron {
namespace operators {
namespace rope {

/**
 * @brief Apply Rotary Positional Embedding to query and key tensors
 *
 * Mathematical formulation:
 *   q_embed = (q * cos) + (rotate_half(q) * sin)
 *   k_embed = (k * cos) + (rotate_half(k) * sin)
 *
 * @param q Query tensor [batch, heads, seq, head_dim]
 * @param k Key tensor [batch, heads, seq, head_dim]
 * @param cos Cosine cache [1, 1, seq, head_dim]
 * @param sin Sine cache [1, 1, seq, head_dim]
 * @param q_out Output query tensor [batch, heads, seq, head_dim]
 * @param k_out Output key tensor [batch, heads, seq, head_dim]
 * @param batch Batch size
 * @param heads Number of attention heads
 * @param seq Sequence length
 * @param head_dim Head dimension (typically 64)
 */
template<typename T>
void rope_fwd(
    const T* q,
    const T* k,
    const T* cos,
    const T* sin,
    T* q_out,
    T* k_out,
    int batch,
    int heads,
    int seq,
    int head_dim
);

/**
 * @brief Rotate half of the last dimension (180 degree rotation)
 *
 * @param x Input tensor [..., head_dim]
 * @param out Output tensor [..., head_dim]
 * @param num_elements Total elements to process
 */
template<typename T>
void rotate_half(
    const T* x,
    T* out,
    int num_elements,
    int head_dim
);

} // namespace rope
} // namespace operators
} // namespace iron
```

#### RMSNorm

```cpp
// File: iron/operators/normalization/rmsnorm_bf16.hpp
#pragma once

#include <cstdint>

namespace iron {
namespace operators {
namespace normalization {

/**
 * @brief Root Mean Square Layer Normalization
 *
 * Mathematical formulation:
 *   rms = sqrt(mean(x^2, dim=-1) + eps)
 *   output = (x / rms) * weight
 *
 * @param input Input tensor [batch, seq, hidden]
 * @param weight Scale parameter [hidden]
 * @param bias Bias parameter [hidden] (optional, can be nullptr)
 * @param output Output tensor [batch, seq, hidden]
 * @param batch Batch size
 * @param seq Sequence length
 * @param hidden Hidden dimension
 * @param eps Epsilon for numerical stability (default: 1e-6)
 */
template<typename T>
void rms_norm_fwd(
    const T* input,
    const T* weight,
    const T* bias,  // optional
    T* output,
    int batch,
    int seq,
    int hidden,
    float eps = 1e-6f
);

} // namespace normalization
} // namespace operators
} // namespace iron
```

#### SiLU (Swish Linear Unit)

```cpp
// File: iron/operators/activations/silu_bf16.hpp
#pragma once

#include <cstdint>

namespace iron {
namespace operators {
namespace activations {

/**
 * @brief SiLU (Sigmoid Linear Unit) activation function
 *
 * Mathematical formulation:
 *   silu(x) = x * sigmoid(x)
 *           = x / (1 + exp(-x))
 *
 * @param input Input tensor [batch, seq, hidden]
 * @param output Output tensor [batch, seq, hidden]
 * @param num_elements Total number of elements to process
 */
template<typename T>
void silu_fwd(
    const T* input,
    T* output,
    int num_elements
);

} // namespace activations
} // namespace operators
} // namespace iron
```

#### Softmax

```cpp
// File: iron/operators/softmax/softmax_bf16.hpp
#pragma once

#include <cstdint>

namespace iron {
namespace operators {
namespace softmax {

/**
 * @brief Softmax activation function with numerical stability
 *
 * Mathematical formulation:
 *   x_max = max(x, dim)
 *   exp_x = exp(x - x_max)
 *   output = exp_x / sum(exp_x, dim)
 *
 * @param input Input tensor [N, M] (flattened [batch*heads, seq])
 * @param output Output tensor [N, M]
 * @param N Number of rows (batch * heads)
 * @param M Number of columns (seq length)
 */
template<typename T>
void softmax_fwd(
    const T* input,
    T* output,
    int N,
    int M
);

} // namespace softmax
} // namespace operators
} // namespace iron
```

---

## 4. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **RoPE implementation complexity** | Medium | High | Reference implementation from RoPE papers |
| **AIE2 scheduling issues** | Medium | High | Early profiling, iterative optimization |
| **Memory bandwidth bottleneck** | High | Medium | Operator fusion, KV cache optimization |
| **Numerical accuracy issues** | Medium | Medium | Extensive unit testing with PyTorch reference |
| **ONNX Runtime integration issues** | Low | Medium | Maintain fallback path |

---

## 5. Success Metrics

### 5.1 Technical Metrics

| Metric | Target | Measurement Method |
|--------|-------|-------------------|
| TTFT (Llama3.2-1B, 128 prompt) | <100ms | Benchmark suite |
| Token Generation Speed | >20 tok/s | Benchmark suite |
| Memory Footprint | <1.5 GB | Process memory tracking |
| NPU Utilization | >70% | Hardware counters |
| Operator Test Coverage | >90% | Unit test framework |

### 5.2 Quality Metrics

| Metric | Target | Measurement Method |
|--------|-------|-------------------|
| Unit Test Pass Rate | 100% | CI/CD pipeline |
| Integration Test Pass Rate | >95% | CI/CD pipeline |
| Memory Leak Detection | 0 leaks | Valgrind, sanitizers |
| Code Review Coverage | 100% | All PRs reviewed |

---

## 6. Dependencies

### 6.1 Internal Dependencies

| Dependency | Status | Owner |
|------------|--------|-------|
| C++ Runtime Abstraction | ✅ Complete | Runtime Team |
| ONNX Runtime Backend | ✅ Complete | Runtime Team |
| Python Bindings | ✅ Complete | Runtime Team |
| Build System (CMake) | ✅ Complete | DevOps Team |

### 6.2 External Dependencies

| Dependency | Version | Status | Owner |
|------------|---------|--------|-------|
| ONNX Runtime GenAI | v0.11.2 | ✅ Available | Runtime Team |
| DirectML | Latest | ✅ Available | Runtime Team |
| HuggingFace Transformers | latest | ✅ Available | API Team |
| AMD Ryzen AI Driver | 1.7.0 | ✅ Available | Runtime Team |

---

## 7. Timeline Summary

```
Week 1-2:  Phase 1 - Critical Operators (RoPE, RMSNorm, SiLU, Softmax)
Week 3-4:  Phase 2 - Benchmark Suite
Week 5-6:  Phase 3 - End-to-End Integration (Llama3.2 inference chain)
Week 7-10: Phase 4 - Performance Optimization
Week 11-12: Phase 5 - Production Hardening
```

**Key Milestones:**
- **Week 2:** All 4 critical operators implemented
- **Week 4:** First benchmark results published
- **Week 6:** First successful Llama3.2-1B generation
- **Week 10:** Performance targets met
- **Week 12:** Production-ready release

---

## 8. Resource Requirements

| Role | FTE | Duration | Focus Area |
|------|-----|----------|------------|
| Kernel Developer | 2.0 | 12 weeks | Operator implementation |
| Runtime Developer | 1.0 | 12 weeks | Integration, KV cache |
| Performance Engineer | 0.5 | 8 weeks | Benchmarking, optimization |
| QA Engineer | 0.5 | 6 weeks | Testing, validation |
| Technical Writer | 0.25 | 4 weeks | Documentation |

**Total Effort:** ~30 FTE-weeks

---

## 9. Next Steps

### Immediate (Week 1)

1. **Start RoPE Implementation**
   - Owner: Kernel Team
   - Deliverable: `iron/operators/rope/rope_bf16.cpp`
   - Due: End of Week 1

2. **Start RMSNorm Implementation**
   - Owner: Kernel Team
   - Deliverable: `iron/operators/normalization/rmsnorm_bf16.cpp`
   - Due: End of Week 1

3. **Create Benchmark Framework**
   - Owner: Performance Team
   - Deliverable: `iron/benchmarks/run.py`
   - Due: End of Week 2

4. **Set Up CI/CD Integration**
   - Owner: DevOps Team
   - Deliverable: Automated operator tests
   - Due: End of Week 1

---

**Document Approval:**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Technical Lead | | 2026-03-15 | |
| Kernel Team Lead | | 2026-03-15 | |
| Performance Lead | | 2026-03-15 | |
| Project Manager | | 2026-03-15 | |

---

**Revision History:**

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-03-15 | Initial creation | IRON Engineering Team |

---

*Copyright © 2026 IRON Project. All rights reserved.*
