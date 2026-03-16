# IRON Operator Catalog

**Document Type:** Technical Reference
**Date:** 2026-03-15
**Author:** IRON Engineering Team
**Version:** 1.0.0

---

## Executive Summary

This document provides a comprehensive catalog of all operators implemented in the IRON NPU runtime framework, including their implementation status, supported data types, and target use cases.

---

## 1. Operator Inventory Summary

| Category | Implemented | Planned | Total | Coverage |
|----------|-------------|---------|-------|----------|
| **Convolution** | 8 | 0 | 8 | 100% |
| **Normalization** | 0 | 2 | 2 | 0% |
| **Activation** | 0 | 3 | 3 | 0% |
| **Attention** | 0 | 4 | 4 | 0% |
| **Matrix (GEMM)** | 1 (via ONNX) | 0 | 1 | 100% |
| **Element-wise** | 0 | 4 | 4 | 0% |
| **Embedding** | 0 | 1 | 1 | 0% |
| **TOTAL** | 9 | 14 | 23 | 39% |

---

## 2. Implemented Operators

### 2.1 Convolution Operators (8/8 - 100%)

All convolution operators are implemented in the `iron/operators/` directory with bfloat16 precision support for AIE2/AIE2P architectures.

| Operator | File | Data Type | Vectorization | Status | Primary Use Case |
|----------|------|-----------|---------------|--------|------------------|
| **Conv2D 3x3 (Vector)** | `conv2d/conv2d_bf16_vector.cpp` | bfloat16 | 8/16-way | ✅ Complete | Vision models (ViT, ResNet) |
| **Conv2D 3x3 (Scalar)** | `conv2d/conv2d_bf16_scalar.cpp` | bfloat16 | Scalar | ✅ Complete | Fallback path |
| **Depthwise Conv2D** | `conv2d/depthwise_conv2d_bf16_vector.cpp` | bfloat16 | 8/16-way | ✅ Complete | MobileNet, EfficientNet |
| **Pointwise Conv2D (1x1)** | `conv2d/pointwise_conv2d_bf16_vector.cpp` | bfloat16 | 8/16-way | ✅ Complete | Channel mixing, Linear alternative |
| **Conv3D 3x3x3 (Vector)** | `conv3d/conv3d_bf16_vector.cpp` | bfloat16 | 8/16-way | ✅ Complete | Video understanding |
| **Conv3D Large Kernel** | `conv3d/conv3d_bf16_large_kernel.cpp` | bfloat16 | 8/16-way | ✅ Complete | Large spatiotemporal receptive fields |
| **Depthwise Conv3D** | `conv3d/depthwise_conv3d_bf16_vector.cpp` | bfloat16 | 8/16-way | ✅ Complete | Video models |
| **Pointwise Conv3D (1x1)** | `conv3d/pointwise_conv3d_bf16_vector.cpp` | bfloat16 | 8/16-way | ✅ Complete | 3D Linear alternative |

#### Conv2D Operator API

```cpp
// Header: iron/operators/conv2d/conv2d_bf16.hpp
template<typename T>
void conv2d_fwd(
    const T* input,           // [N, IC, IH, IW]
    const T* weight,          // [OC, IC, KH, KW]
    const T* bias,            // [OC] (optional)
    T* output,                // [N, OC, OH, OW]
    int N, int IC, int IH, int IW,
    int OC, int KH, int KW,
    int stride_h, int stride_w,
    int pad_h, int pad_w,
    int dilation_h, int dilation_w
);
```

#### Conv3D Operator API

```cpp
// Header: iron/operators/conv3d/conv3d_bf16.hpp
template<typename T>
void conv3d_fwd(
    const T* input,           // [N, IC, ID, IH, IW]
    const T* weight,          // [OC, IC, KD, KH, KW]
    const T* bias,            // [OC] (optional)
    T* output,                // [N, OC, OD, OH, OW]
    int N, int IC, int ID, int IH, int IW,
    int OC, int KD, int KH, int KW,
    int stride_d, int stride_h, int stride_w,
    int pad_d, int pad_h, int pad_w,
    int dilation_d, int dilation_h, int dilation_w
);
```

---

## 3. Planned Operators (Critical for Llama3.2)

### 3.1 Normalization Operators (0/2 - 0%)

| Operator | Priority | Estimated Effort | Target Use Case |
|----------|----------|------------------|-----------------|
| **RMSNorm** | Critical | 1 week | Llama3.2 layer normalization |
| **LayerNorm** | Medium | 1 week | General transformer support |

#### RMSNorm Specification

```python
# Mathematical formulation
def rms_norm(x, weight, eps=1e-6):
    rms = sqrt(mean(x^2, dim=-1) + eps)
    return (x / rms) * weight
```

```cpp
// Planned API: iron/operators/normalization/rmsnorm_bf16.hpp
template<typename T>
void rms_norm_fwd(
    const T* input,       // [batch, seq, hidden]
    const T* weight,      // [hidden]
    T* output,            // [batch, seq, hidden]
    int batch, int seq, int hidden,
    float eps = 1e-6
);
```

---

### 3.2 Activation Operators (0/3 - 0%)

| Operator | Priority | Estimated Effort | Target Use Case |
|----------|----------|------------------|-----------------|
| **SiLU (Swish)** | Critical | 3 days | Llama3.2 MLP gate |
| **GeLU** | Medium | 3 days | BERT, general transformers |
| **SwiGLU** | Medium | 3 days | Llama3.2 fused MLP |

#### SiLU Specification

```python
# Mathematical formulation
def silu(x):
    return x * sigmoid(x)
```

```cpp
// Planned API: iron/operators/activations/silu_bf16.hpp
template<typename T>
void silu_fwd(
    const T* input,       // [batch, seq, hidden]
    T* output,            // [batch, seq, hidden]
    int batch, int seq, int hidden
);
```

---

### 3.3 Attention Operators (0/4 - 0%)

| Operator | Priority | Estimated Effort | Target Use Case |
|----------|----------|------------------|-----------------|
| **RoPE (Rotary Positional Embedding)** | Critical | 1 week | Llama3.2 positional encoding |
| **Scaled Dot-Product Attention** | High | 1 week | Core attention mechanism |
| **Multi-Head Attention** | High | 1 week | Multi-head grouping |
| **Paged Attention** | Low | 2 weeks | Memory-efficient KV cache |

#### RoPE Specification

```python
# Mathematical formulation
def apply_rope(q, k, cos, sin):
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed

def rotate_half(x):
    x1, x2 = x[..., :dim//2], x[..., dim//2:]
    return torch.cat((-x2, x1), dim=-1)
```

```cpp
// Planned API: iron/operators/rope/rope_bf16.hpp
template<typename T>
void rope_fwd(
    const T* q,           // [batch, heads, seq, head_dim]
    const T* k,           // [batch, heads, seq, head_dim]
    const T* cos,         // [1, 1, seq, head_dim]
    const T* sin,         // [1, 1, seq, head_dim]
    T* q_out,             // [batch, heads, seq, head_dim]
    T* k_out,             // [batch, heads, seq, head_dim]
    int batch, int heads, int seq, int head_dim
);
```

---

### 3.4 Element-wise Operators (0/4 - 0%)

| Operator | Priority | Estimated Effort | Target Use Case |
|----------|----------|------------------|-----------------|
| **Softmax** | Critical | 3 days | Attention weight normalization |
| **Add (Element-wise)** | Medium | 1 day | Residual connections |
| **Multiply (Element-wise)** | Medium | 1 day | Attention masking |
| **Concat** | Medium | 2 days | Tensor assembly |

#### Softmax Specification

```python
# Mathematical formulation
def softmax(x, dim=-1):
    x_max = max(x, dim=dim, keepdim=True)
    exp_x = exp(x - x_max)
    return exp_x / sum(exp_x, dim=dim)
```

```cpp
// Planned API: iron/operators/softmax/softmax_bf16.hpp
template<typename T>
void softmax_fwd(
    const T* input,       // [batch, heads, seq, seq]
    T* output,            // [batch, heads, seq, seq]
    int batch, int heads, int seq,
    int dim
);
```

---

### 3.5 Embedding Operators (0/1 - 0%)

| Operator | Priority | Estimated Effort | Target Use Case |
|----------|----------|------------------|-----------------|
| **Token Embedding** | Medium | 1 week | Token lookup |

---

## 4. Operator Dependency Graph by Model

### 4.1 Llama3.2 Dependency Graph

```
Llama3.2 Inference
│
├── Token Embedding ────────────────┐ (MISSING: Embedding)
│                                   │
├── Transformer Layer               │
│   │                               │
│   ├── Attention Path              │
│   │   ├── RMSNorm ────────────────┤ (MISSING: RMSNorm)
│   │   ├── QKV Projection ─────────┤ (AVAILABLE: GEMM via ONNX)
│   │   ├── RoPE ───────────────────┤ (MISSING: RoPE)
│   │   ├── Scaled Dot-Product      │
│   │   │   ├── Matrix Multiply ────┤ (AVAILABLE: GEMM via ONNX)
│   │   │   └── Softmax ────────────┤ (MISSING: Softmax)
│   │   └── Output Projection ──────┤ (AVAILABLE: GEMM via ONNX)
│   │                               │
│   └── MLP Path                    │
│       ├── RMSNorm (reused) ───────┤
│       ├── Gate Projection ────────┤ (AVAILABLE: GEMM via ONNX)
│       ├── SiLU ───────────────────┤ (MISSING: SiLU)
│       ├── Up Projection ──────────┤ (AVAILABLE: GEMM via ONNX)
│       └── Down Projection ────────┘ (AVAILABLE: GEMM via ONNX)
│
└── Final Output
    ├── RMSNorm (reused) ───────────┘
    └── LM Head ──────────────────── (AVAILABLE: GEMM via ONNX)
```

**Summary for Llama3.2:**
- **Available via ONNX:** 5 operators (GEMM for all linear layers)
- **Missing (Critical):** 4 operators (RoPE, RMSNorm, SiLU, Softmax)
- **Missing (Medium):** 1 operator (Embedding)

---

### 4.2 Gemma3-VL Dependency Graph

```
Gemma3-VL Inference
│
├── Vision Path
│   ├── Patch Embedding (Conv2D 16x16) ── (MISSING: Large-kernel Conv2D)
│   ├── Transformer Layers              │
│   │   ├── RMSNorm ────────────────────┤ (MISSING: RMSNorm)
│   │   ├── Attention (with RoPE) ──────┤ (MISSING: RoPE)
│   │   └── MLP (with GeLU) ────────────┤ (MISSING: GeLU)
│   └── Vision Output                   │
│                                       │
└── Language Path (same as Llama3.2) ───┘
```

**Summary for Gemma3-VL:**
- **Available:** Conv2D operators (existing in IRON)
- **Missing (Critical):** RoPE, RMSNorm, GeLU, Softmax
- **Missing (Medium):** Large-kernel Conv2D for patch embedding

---

### 4.3 Whisper (Audio) Dependency Graph

```
Whisper Audio Encoder
│
├── Audio Spectrogram Input
│
├── Conv2D Encoder (3x3, 128 filters) ── (AVAILABLE: conv2d_bf16_vector)
├── Conv2D Encoder (3x3, 256 filters) ── (AVAILABLE: conv2d_bf16_vector)
│
└── Transformer Decoder                 │
    ├── RMSNorm ────────────────────────┤ (MISSING: RMSNorm)
    ├── Multi-Head Attention ───────────┤ (MISSING: Attention)
    └── MLP (with GeLU) ────────────────┘ (MISSING: GeLU)
```

**Summary for Whisper:**
- **Available:** Conv2D operators (existing in IRON)
- **Missing:** Transformer operators (RoPE, RMSNorm, GeLU, Attention)

---

## 5. Data Type Support Matrix

| Operator | FP32 | FP16 | BF16 | INT8 | INT4 |
|----------|------|------|------|------|------|
| Conv2D 3x3 | ⏳ Planned | ⏳ Planned | ✅ Complete | ❌ Not planned | ❌ Not planned |
| Conv3D 3x3x3 | ⏳ Planned | ⏳ Planned | ✅ Complete | ❌ Not planned | ❌ Not planned |
| RoPE | ❌ Not started | ❌ Not started | 🔜 Planned | ❌ Not planned | ❌ Not planned |
| RMSNorm | ❌ Not started | ❌ Not started | 🔜 Planned | ❌ Not planned | ❌ Not planned |
| SiLU | ❌ Not started | ❌ Not started | 🔜 Planned | ❌ Not planned | ❌ Not planned |
| Softmax | ❌ Not started | ❌ Not started | 🔜 Planned | ❌ Not planned | ❌ Not planned |
| GEMM (ONNX) | ✅ Available | ✅ Available | ✅ Available | ⏳ Planned | ⏳ Planned |

**Legend:**
- ✅ Complete and tested
- 🔜 In development
- ⏳ Planned (not started)
- ❌ Not planned

---

## 6. Performance Targets by Operator

| Operator | Input Shape | Latency Target | Memory Bandwidth |
|----------|-------------|----------------|------------------|
| Conv2D 3x3 | [1, 3, 224, 224] → 64 filters | <5ms | High |
| Conv3D 3x3x3 | [1, 3, 16, 112, 112] → 32 filters | <15ms | Very High |
| RoPE | [1, 12, 128, 64] | <0.5ms | Low |
| RMSNorm | [1, 128, 2048] | <1ms | Medium |
| SiLU | [1, 128, 8192] | <0.3ms | Low |
| Softmax | [1, 12, 128, 128] | <2ms | High |

---

## 7. Implementation Priority Matrix

### 7.1 Critical Priority (Implement First - Weeks 1-2)

| Operator | Use Case | Impact | Effort |
|----------|----------|--------|--------|
| RoPE | Llama3.2 positional encoding | Enables LLM inference | 1 week |
| RMSNorm | Llama3.2 layer normalization | Enables LLM inference | 1 week |
| SiLU | Llama3.2 MLP gate | Enables LLM inference | 3 days |
| Softmax | Attention weights | Enables LLM inference | 3 days |

### 7.2 High Priority (Implement Second - Weeks 3-4)

| Operator | Use Case | Impact | Effort |
|----------|----------|--------|--------|
| Scaled Dot-Product Attention | Core attention | Enables transformer | 1 week |
| Multi-Head Attention | Multi-head support | Performance improvement | 1 week |
| GeLU | BERT, Gemma support | Broader model support | 3 days |

### 7.3 Medium Priority (Implement Third - Weeks 5-6)

| Operator | Use Case | Impact | Effort |
|----------|----------|--------|--------|
| Token Embedding | Lookup table | Complete inference chain | 1 week |
| LayerNorm | BERT compatibility | Alternative normalization | 1 week |
| Fused SiLU+Linear | MLP optimization | 20% speedup | 1 week |

### 7.4 Low Priority (Future - Weeks 7+)

| Operator | Use Case | Impact | Effort |
|----------|----------|--------|--------|
| Paged Attention | Long sequence | Memory efficiency | 2 weeks |
| Flash Attention | Large batch | Memory efficiency | 3 weeks |
| INT8 Quantization | Model compression | 2x speedup, 50% memory | 4 weeks |

---

## 8. API Usage Examples

### 8.1 Python API (Planned)

```python
import iron.operators as ops

# RoPE
q, k = ops.apply_rope(q, k, cos, sin)

# RMSNorm
hidden = ops.rms_norm(hidden, weight, eps=1e-6)

# SiLU
gate = ops.silu(gate)

# Softmax
attn_weights = ops.softmax(scores, dim=-1)
```

### 8.2 C++ API (Planned)

```cpp
#include <iron/operators/rope.hpp>
#include <iron/operators/rmsnorm.hpp>
#include <iron/operators/silu.hpp>
#include <iron/operators/softmax.hpp>

// RoPE
rope_fwd<bf16>(q, k, cos, sin, q_out, k_out, batch, heads, seq, head_dim);

// RMSNorm
rms_norm_fwd<bf16>(input, weight, output, batch, seq, hidden);

// SiLU
silu_fwd<bf16>(input, output, batch, seq, hidden);

// Softmax
softmax_fwd<bf16>(input, output, batch, heads, seq, dim);
```

---

## 9. Testing Status

| Operator | Unit Tests | Integration Tests | E2E Tests |
|----------|-----------|-------------------|-----------|
| Conv2D | ✅ Complete | ⏳ Pending | ⏳ Pending |
| Conv3D | ✅ Complete | ⏳ Pending | ⏳ Pending |
| RoPE | ❌ Not started | ❌ Not started | ❌ Not started |
| RMSNorm | ❌ Not started | ❌ Not started | ❌ Not started |
| SiLU | ❌ Not started | ❌ Not started | ❌ Not started |
| Softmax | ❌ Not started | ❌ Not started | ❌ Not started |

---

**Document History:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-15 | Initial creation |

---

*Copyright © 2026 IRON Project. All rights reserved.*
