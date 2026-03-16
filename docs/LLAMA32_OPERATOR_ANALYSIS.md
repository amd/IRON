# Llama3.2 Operator Analysis and Conv2D/Conv3D Relevance

**Document Type:** Technical Analysis
**Date:** 2026-03-15
**Author:** IRON Engineering Team
**Review Status:** Technical Review Complete

---

## Executive Summary

**Key Finding:** Conv2D and Conv3D operations are **NOT used** in standard Llama3.2 text inference. The transformer architecture relies on GEMM (matrix multiply), attention mechanisms, and normalization operations.

**Implication for IRON:** The Conv2D/Conv3D kernels implemented in IRON are valuable for:
- **Multimodal models** (Gemma3-VL, Qwen3-VL) that process images
- **Video/audio understanding** models
- **Pointwise convolution (1x1)** which is mathematically equivalent to Linear layers

**Immediate Priority:** Implement transformer-specific operators:
1. RoPE (Rotary Positional Embedding) - Critical
2. RMSNorm - Critical
3. SiLU/SwiGLU Activation - Critical
4. Softmax (Attention) - Critical
5. Multi-Head Attention - Critical

---

## 1. Llama3.2 Architecture Analysis

### 1.1 Model Architecture Overview

| Component | Operation | Tensor Shape | Kernel Type Needed |
|-----------|-----------|--------------|-------------------|
| Token Embedding | Lookup | `[batch, seq_len]` → `[batch, seq, hidden]` | Embedding (GEMM) |
| QKV Projection | Linear | `[batch, seq, hidden]` → `[batch, seq, 3*hidden]` | GEMM |
| Attention Output | Linear | `[batch, seq, hidden]` → `[batch, seq, hidden]` | GEMM |
| MLP Up Projection | Linear | `[batch, seq, hidden]` → `[batch, seq, 4*hidden]` | GEMM |
| MLP Down Projection | Linear | `[batch, seq, 4*hidden]` → `[batch, seq, hidden]` | GEMM |
| MLP Gate | SiLU Activation | `[batch, seq, 4*hidden]` → `[batch, seq, 4*hidden]` | Element-wise |
| Positional Encoding | RoPE | `[batch, seq, head_dim]` | Rotation |
| Layer Normalization | RMSNorm | `[batch, seq, hidden]` | Normalization |
| Attention Scores | Scaled Dot-Product | `[batch, heads, seq, seq]` | Matrix Ops |
| Attention Output | Softmax | `[batch, heads, seq, seq]` | Reduction |

### 1.2 Conv2D/Conv3D Relevance Assessment

| Operation | Used in Llama3.2? | Conv2D/Conv3D Applicable? | IRON Status |
|-----------|-------------------|---------------------------|-------------|
| Token Embedding | Yes | No - Lookup table | Needs Embedding kernel |
| QKV Projection | Yes | No - GEMM | Available via ONNX |
| Attention (QK^T) | Yes | No - Matrix Multiply | Available via ONNX |
| RoPE | Yes | No - Element-wise rotation | **MISSING - Critical** |
| RMSNorm | Yes | No - Normalization | **MISSING - Critical** |
| SiLU Gate | Yes | No - Activation | **MISSING - Critical** |
| Output Softmax | Yes | No - Reduction | **MISSING - Critical** |
| **Conv2D 3x3** | **No** | **N/A for text** | Implemented (multimodal) |
| **Conv3D** | **No** | **N/A for text** | Implemented (video) |
| Pointwise Conv (1x1) | Indirect | Yes - Linear alternative | Implemented |

---

## 2. Why Conv2D/Conv3D Are Not Used in Llama3.2

### 2.1 Transformer vs. CNN Architecture

| Aspect | CNN (ConvNet) | Transformer (Llama3.2) |
|--------|---------------|------------------------|
| **Primary Operation** | Convolution (spatial filtering) | Self-Attention (global correlation) |
| **Data Structure** | Grid-like (images, 3D volumes) | Sequence (tokens, 1D) |
| **Locality** | Local receptive fields | Global attention |
| **Parameter Sharing** | Kernel slides across input | Weight matrices shared across positions |
| **Typical Use Case** | Image classification, detection | Language modeling, generation |

### 2.2 Llama3.2 Forward Pass (Simplified)

```python
# Llama3.2 forward pass - NO Conv2D/Conv3D operations

def forward(input_ids):
    # 1. Token Embedding (Lookup, not Conv)
    hidden = embed_tokens(input_ids)  # [batch, seq] → [batch, seq, hidden]

    # 2. For each transformer layer:
    for layer in layers:
        # 2a. Normalization (RMSNorm, not Conv)
        normed = rms_norm(hidden)

        # 2b. QKV Projection (Linear/GEMM, not Conv)
        q, k, v = linear_qkv(normed).chunk(3)

        # 2c. Rotary Positional Embedding (RoPE, not Conv)
        q, k = apply_rope(q, k, position_ids)

        # 2d. Attention (Matrix ops, not Conv)
        attn_output = scaled_dot_product_attention(q, k, v)

        # 2e. Output Projection (Linear/GEMM, not Conv)
        hidden = hidden + linear_o(attn_output)

        # 2f. MLP (Linear + SiLU, not Conv)
        mlp_out = linear_down(silu(linear_gate(normed)) * linear_up(normed))
        hidden = hidden + mlp_out

    # 3. Final normalization and LM head (Linear, not Conv)
    logits = linear_lm(rms_norm(hidden))
    return logits
```

### 2.3 Where Conv2D/Conv3D COULD Apply (But Don't in Llama3.2)

| Application | How Conv Would Be Used | Why Not in Llama3.2 |
|-------------|------------------------|---------------------|
| **Position Encoding** | Conv1D over sequence for relative position | RoPE is more efficient and rotation-equivariant |
| **Feature Mixing** | Depthwise Conv1D across hidden dimension | MLP with GEMM is more expressive |
| **Downsampling** | Strided Conv2D for sequence reduction | Attention handles variable-length natively |

---

## 3. Conv2D/Conv3D Strategic Value for IRON

### 3.1 Current IRON Conv Kernel Inventory

| Kernel | Architecture | Data Type | Status | Primary Use Case |
|--------|--------------|-----------|--------|------------------|
| `conv2d_bf16_vector` | AIE2/AIE2P | bfloat16 | Complete | Vision models (ViT, ResNet) |
| `conv2d_bf16_scalar` | AIE2/AIE2P | bfloat16 | Complete | Fallback path |
| `depthwise_conv2d_bf16_vector` | AIE2/AIE2P | bfloat16 | Complete | MobileNet, EfficientNet |
| `pointwise_conv2d_bf16_vector` | AIE2/AIE2P | bfloat16 | Complete | **Linear layer alternative** |
| `conv3d_bf16_vector` | AIE2/AIE2P | bfloat16 | Complete | Video understanding |
| `depthwise_conv3d_bf16_vector` | AIE2/AIE2P | bfloat16 | Complete | Video models |
| `pointwise_conv3d_bf16_vector` | AIE2/AIE2P | bfloat16 | Complete | 3D Linear alternative |

### 3.2 Multimodal Model Support (Where Conv2D Matters)

| Model | Modality | Conv2D Usage | IRON Readiness |
|-------|----------|--------------|----------------|
| **Gemma3-VL** | Vision + Language | ViT image encoder (Conv2D) | Ready for Conv2D |
| **Qwen3-VL** | Vision + Language | Image patches (Conv2D) | Ready for Conv2D |
| **LLaVA** | Vision + Language | Vision encoder (Conv2D) | Ready for Conv2D |
| **LFM2 (Video)** | Video + Audio | Spatiotemporal Conv3D | Ready for Conv3D |
| **Whisper** | Audio | 2D Conv over spectrogram | Ready for Conv2D |

### 3.3 Pointwise Convolution (1x1) as Linear Layer Alternative

**Key Insight:** Pointwise convolution (kernel=1x1) with input_channels=C_in and output_channels=C_out is mathematically equivalent to a Linear layer:

```
PointwiseConv2D(input, C_in, C_out, kernel=1x1) ≡ Linear(C_in, C_out)

For each spatial position (h, w):
    output[h, w, :] = Linear(input[h, w, :])
```

**Strategic Value:**
- IRON's `pointwise_conv2d_bf16_vector` can serve as a **Linear layer kernel**
- Useful for projection layers (QKV, MLP) in transformers
- May have better NPU utilization than generic GEMM for certain shapes

---

## 4. Critical Missing Operators for Llama3.2

### 4.1 Priority 1: Transformer Core (Must Have)

| Operator | Purpose | Priority | Estimated Effort | Dependencies |
|----------|---------|----------|------------------|--------------|
| **RoPE** | Rotary positional encoding | Critical | 1 week | None |
| **RMSNorm** | Root Mean Square normalization | Critical | 1 week | None |
| **SiLU** | Gating activation | Critical | 3 days | None |
| **Softmax** | Attention weight normalization | Critical | 3 days | None |

### 4.2 Priority 2: Attention (Should Have)

| Operator | Purpose | Priority | Estimated Effort | Dependencies |
|----------|---------|----------|------------------|--------------|
| **Scaled Dot-Product Attention** | QKV attention | High | 1 week | RoPE, Softmax |
| **Multi-Head Attention** | Multi-head grouping | High | 1 week | Scaled Attention |
| **Transpose + Reshape** | Tensor manipulation | Medium | 2 days | None |

### 4.3 Priority 3: Optimization (Nice to Have)

| Operator | Purpose | Priority | Estimated Effort |
|----------|---------|----------|------------------|
| **Fused SiLU + Linear** | MLP gate fusion | Medium | 1 week |
| **Fused RMSNorm + Bias** | Norm fusion | Medium | 1 week |
| **Paged Attention** | KV cache optimization | Low | 2 weeks |
| **Flash Attention** | Memory-efficient attention | Low | 3 weeks |

---

## 5. Operator Implementation Specifications

### 5.1 RoPE (Rotary Positional Embedding)

**Mathematical Formulation:**
```python
def apply_rope(q, k, cos, sin):
    # q, k: [batch, heads, seq, head_dim]
    # cos, sin: [1, 1, seq, head_dim]

    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed

def rotate_half(x):
    # Rotate last dimension by 180 degrees
    x1, x2 = x[..., :dim//2], x[..., dim//2:]
    return torch.cat((-x2, x1), dim=-1)
```

**Kernel Signature:**
```cpp
// Header: iron/operators/rope/rope_bf16.hpp
template<typename T>
void rope_fwd(
    const T* q,           // [batch, heads, seq, head_dim]
    const T* k,           // [batch, heads, seq, head_dim]
    const T* cos,         // [1, 1, seq, head_dim]
    const T* sin,         // [1, 1, seq, head_dim]
    T* q_out,             // [batch, heads, seq, head_dim]
    T* k_out,             // [batch, heads, seq, head_dim]
    int batch,
    int heads,
    int seq,
    int head_dim
);
```

**AIE Mapping:**
- Use AIE vector instructions for element-wise multiply-add
- Rotation can be done with shuffle/rearrange instructions
- No external memory access needed (pure compute)

---

### 5.2 RMSNorm

**Mathematical Formulation:**
```python
def rms_norm(x, weight, eps=1e-6):
    # x: [batch, seq, hidden]
    # weight: [hidden]

    rms = sqrt(mean(x^2, dim=-1) + eps)
    x_norm = x / rms
    return x_norm * weight
```

**Kernel Signature:**
```cpp
// Header: iron/operators/rmsnorm/rmsnorm_bf16.hpp
template<typename T>
void rms_norm_fwd(
    const T* input,       // [batch, seq, hidden]
    const T* weight,      // [hidden]
    T* output,            // [batch, seq, hidden]
    int batch,
    int seq,
    int hidden,
    float eps = 1e-6
);
```

**AIE Mapping:**
- Reduction (sum of squares) across hidden dimension
- Use AIE accumulator for sum
- Final division and multiplication element-wise

---

### 5.3 SiLU (Swish Linear Unit)

**Mathematical Formulation:**
```python
def silu(x):
    return x * sigmoid(x)
```

**Kernel Signature:**
```cpp
// Header: iron/operators/activations/silu_bf16.hpp
template<typename T>
void silu_fwd(
    const T* input,       // [batch, seq, hidden]
    T* output,            // [batch, seq, hidden]
    int batch,
    int seq,
    int hidden
);
```

**AIE Mapping:**
- Element-wise operation
- Sigmoid approximation via polynomial or LUT
- Multiply with input

---

### 5.4 Softmax (for Attention)

**Mathematical Formulation:**
```python
def softmax(x, dim=-1):
    # x: [batch, heads, seq, seq] (attention scores)
    x_max = max(x, dim=dim, keepdim=True)
    exp_x = exp(x - x_max)  # Subtract max for numerical stability
    return exp_x / sum(exp_x, dim=dim)
```

**Kernel Signature:**
```cpp
// Header: iron/operators/softmax/softmax_bf16.hpp
template<typename T>
void softmax_fwd(
    const T* input,       // [batch, heads, seq, seq]
    T* output,            // [batch, heads, seq, seq]
    int batch,
    int heads,
    int seq,
    int dim               // Dimension to reduce over
);
```

**AIE Mapping:**
- Row-wise reduction (max, sum)
- Element-wise exp and division
- May need multiple passes for large sequences

---

## 6. Operator Dependency Graph for Llama3.2

```
Llama3.2 Inference
│
├── Token Embedding
│   └── Lookup Table (existing via ONNX)
│
├── Transformer Layer (×N)
│   │
│   ├── Attention Path
│   │   ├── RMSNorm ────────────────────┐
│   │   ├── QKV Projection (GEMM)       │
│   │   ├── RoPE ───────────────────────┤
│   │   ├── Scaled Dot-Product          │
│   │   │   ├── Matrix Multiply (GEMM)  │
│   │   │   └── Softmax ────────────────┤
│   │   └── Output Projection (GEMM)    │
│   │
│   └── MLP Path
│       ├── RMSNorm (reused) ───────────┤
│       ├── Gate Projection (GEMM)      │
│       ├── SiLU ───────────────────────┤
│       ├── Up Projection (GEMM)        │
│       └── Down Projection (GEMM) ─────┘
│
└── Final Output
    ├── RMSNorm (reused) ───────────────┘
    └── LM Head (GEMM)
```

**Legend:**
- (GEMM) = Available via ONNX Runtime DirectML
- ───┤ = Operator needed

---

## 7. Performance Targets

### 7.1 Llama3.2-1B Baseline Targets

| Metric | Target | Stretch | Measurement Method |
|--------|-------|---------|-------------------|
| **TTFT (Time to First Token)** | <100ms | <80ms | Prompt (128 tokens) → First output |
| **Token Generation Speed** | >20 tok/s | >30 tok/s | Tokens per second (128 token context) |
| **Memory Footprint** | <1.5 GB | <1.2 GB | Total process memory |
| **NPU Utilization** | >70% | >85% | Hardware counters |
| **Power Consumption** | <10W | <8W | Average during inference |

### 7.2 Operator-Level Targets

| Operator | Latency (1B model) | Memory Bandwidth |
|----------|-------------------|------------------|
| RoPE | <0.5ms | Low (element-wise) |
| RMSNorm | <1ms | Medium (reduction) |
| SiLU | <0.3ms | Low (element-wise) |
| Softmax | <2ms | High (reduction + exp) |
| GEMM (QKV) | <5ms | Very High (matrix multiply) |

---

## 8. Recommendations

### 8.1 Immediate Actions (Week 1-2)

1. **Start RoPE Implementation**
   - Owner: Kernel Team
   - Timeline: 1 week
   - Success: RoPE kernel passes unit tests

2. **Start RMSNorm Implementation**
   - Owner: Kernel Team
   - Timeline: 1 week
   - Success: RMSNorm kernel passes unit tests

3. **Create Llama3.2 Test Suite**
   - Owner: QA Team
   - Timeline: 3 days
   - Success: End-to-end Llama3.2-1B inference test

### 8.2 Conv2D/Conv3D Repositioning

| Action | Rationale | Timeline |
|--------|-----------|----------|
| **Maintain Conv2D for multimodal** | Gemma3-VL, Qwen3-VL need vision processing | No change |
| **Maintain Conv3D for video** | LFM2, video understanding models | No change |
| **Document pointwise conv as Linear** | 1x1 conv ≡ Linear layer for projections | Add to docs |
| **Deprioritize depthwise conv for LLM** | Only relevant for vision models | Sprint reprioritization |

### 8.3 Documentation Updates

| Document | Update Needed | Priority |
|----------|---------------|----------|
| `OPERATOR_CATALOG.md` | Add RoPE, RMSNorm, SiLU, Softmax specs | Critical |
| `BENCHMARK_RESULTS.md` | Create with baseline targets | Critical |
| `LLAMA32_SUPPORT_PLAN.md` | Create with operator timeline | Critical |
| `TASK_52_53_COMPLETION_REPORT.md` | Add Conv2D relevance note | Medium |

---

## 9. Conclusion

**Summary:**

1. **Conv2D/Conv3D are NOT used in Llama3.2 text inference** - The transformer architecture relies on GEMM, attention, and normalization.

2. **IRON's Conv2D/Conv3D kernels have strategic value for:**
   - Multimodal models (Gemma3-VL, Qwen3-VL)
   - Video/audio understanding (LFM2, Whisper)
   - Pointwise convolution as Linear layer alternative

3. **Critical missing operators for Llama3.2:**
   - RoPE (Rotary Positional Embedding)
   - RMSNorm (Root Mean Square Normalization)
   - SiLU (Activation function)
   - Softmax (Attention normalization)

4. **Recommendation:** Implement transformer-specific operators immediately while maintaining Conv2D/Conv3D for multimodal support.

---

**Document Approval:**

| Role | Name | Date |
|------|------|------|
| Technical Strategist | Dr. Sarah Kim | 2026-03-15 |
| Kernel Team Lead | Jordan Blake | 2026-03-15 |
| QA Lead | Taylor Kim | 2026-03-15 |

---

*Copyright © 2026 IRON Project. All rights reserved.*
