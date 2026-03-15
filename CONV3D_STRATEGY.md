<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Conv3D Strategy: Convolution as Compute Primitive for Text and Video Models

## Executive Summary

This document captures key insights about repurposing convolution operators (Conv2D, Conv3D) as **compute primitives** for both video AND text models through strategic shape manipulation. The Conv3D operator is identified as the next critical implementation to enable efficient LLM operations on AMD Ryzen AI NPUs.

---

## 1. Current Operator Status

| Operator | Status | AIE2 | AIE2P | Location |
|----------|--------|------|-------|----------|
| Conv2D | ✅ Complete | ✓ | ✓ | `iron/operators/conv2d/` |
| MaxPool2D | ✅ Complete | ✓ | ✓ | `iron/operators/maxpool/` |
| AveragePool2D | ✅ Complete | ✓ | ✓ | `iron/operators/avgpool/` |
| Reduction | ✅ Complete | ✓ | ✓ | `iron/operators/reduction/` |
| **Conv3D** | ✅ **Complete** | ✓ | ✓ | `iron/operators/conv3d/` |

### Original Request Completion Status

User's original list: **"CONVOLUTION, MAX POOL, AVERAGE POOL AND Reduction"**

- ✅ Convolution (Conv2D + Conv3D)
- ✅ Max Pool (2D)
- ✅ Average Pool (2D)
- ✅ Reduction (sum, mean, max, min)

---

## 2. Key Insight: Convolution as Compute Primitive

### 2.1 The Fundamental Realization

> **Convolution operators are not just for semantic convolution - they are COMPUTE PRIMITIVES that can be repurposed through shape manipulation.**

This insight transforms how we view Conv3D:
- **Before**: Conv3D = video model operator only
- **After**: Conv3D = 5D compute primitive for video + text models

### 2.2 Apple's Conv2D Trick (Proven Pattern)

Apple's Neural Engine uses this proven technique for Linear layers:

```
Original:  (B, S, D)           # Batch, Sequence, Hidden
Reshape:   (B, D, 1, S)        # Treat as image: (B, C, H, W)
Conv2D:    kernel=(1,1)        # Pointwise convolution = Matrix multiply
Output:    (B, D_out, 1, S)    # Result
Reshape:   (B, S, D_out)       # Back to sequence format
```

**Our Conv2D already supports this** via `pointwise_conv2d_bf16_vector` kernel when `kernel_size=(1,1)`.

### 2.3 Extending to Conv3D for Text Models

The 5D structure of Conv3D naturally maps to blocked LLM tensor layouts:

#### MHA 5D Blocked Format
```
(B, G, H, S, D_h) where:
  B  = Batch
  G  = Groups (for Grouped Query Attention)
  H  = Heads per group
  S  = Sequence length (tiled)
  D_h = Head dimension (e.g., 128)
```

#### Conv3D 5D Structure
```
(N, C, T, H, W) where:
  N = Batch
  C = Channels
  T = Temporal/Depth
  H = Height
  W = Width
```

#### Proposed Mapping
| Conv3D | MHA | Use Case |
|--------|-----|----------|
| N | B | Batch processing |
| C | G | GQA groups |
| T | H | Head dimension |
| H | S_tiles | Sequence tiles |
| W | D_h_tiles | Head dimension tiles |

---

## 3. Conv3D Implementation Strategy

### 3.1 Dual-Purpose Design

Conv3D must support two usage patterns:

#### Pattern A: Semantic Video Convolution
```python
# Standard video input: (N, C, T, H, W)
conv3d = AIEConv3d(
    in_channels=64,
    out_channels=128,
    kernel_size=(3, 3, 3),
    stride=(1, 2, 2),
    padding=(1, 1, 1)
)
# Video classification, action recognition, etc.
```

#### Pattern B: Text Model Compute Primitive
```python
# MHA blocked format: (B, G, H, S_tiles, D_h_tiles)
conv3d = AIEConv3d(
    in_channels=G,        # Groups
    out_channels=G,       # Same groups
    kernel_size=(1, 3, 3),  # Process local S x D_h windows
    stride=(1, 1, 1),
    padding=(0, 1, 1)
)
# Reshape MHA tensors to 5D, apply Conv3D as attention primitive
```

### 3.2 Kernel Configurations

| Kernel Size | Use Case | Description |
|-------------|----------|-------------|
| (1, 1, 1) | Channel projection | Linear layer equivalent for 5D |
| (1, 3, 3) | Local attention | Windowed attention over S × D_h |
| (3, 3, 3) | Full 3D convolution | Video models, spatiotemporal |
| (1, 1, k) | Cross-head mixing | Mix information across heads |

### 3.3 Vectorization Strategy

Based on our existing patterns:

| Architecture | vec_factor | Kernel File |
|--------------|------------|-------------|
| AIE2 (NPU) | 8 | `aie_kernels/aie2/conv3d.cc` |
| AIE2P (NPU2) | 16 | `aie_kernels/aie2p/conv3d.cc` |

---

## 4. Shape Manipulation Patterns for Text Models

### 4.1 Tiling for NPU Efficiency

Standard PyTorch: `(B, S, D)`

NPU-optimized 5D: `(B, S_outer, S_inner, D_outer, D_inner)`

Where:
- `S_inner` = tile size (e.g., 32 for NPU vector width)
- `D_inner` = tile size (e.g., 32 or 64)

Example for Llama 3 (S=128, D=4096, tile=32):
```
Original:  (1, 128, 4096)
5D Tiled:  (1, 4, 32, 128, 32)  # (B, S_outer, S_inner, D_outer, D_inner)
Permuted:  (1, 4, 128, 32, 32)  # For NPU memory layout
```

### 4.2 The Conv3D Trick Workflow

```
Step 1: Start with MHA tensors
  Q, K, V: (B, num_heads, S, D_h)

Step 2: Reshape for GQA format
  (B, G, H, S, D_h) where G = groups, H = heads_per_group

Step 3: Tile for NPU
  (B, G, H, S_tiles, D_h_tiles) where tile_size matches NPU vector width

Step 4: Apply Conv3D with kernel (1, 3, 3)
  Processes local 3x3 windows over (S × D_h) space
  Efficient attention computation

Step 5: Collapse back to standard format
  (B, num_heads * S, D_h) → project to output
```

---

## 5. Implementation Plan

### 5.1 Files to Create

```
iron/operators/conv3d/
├── __init__.py      # Module exports
├── op.py            # Main operator class (AIEConv3d)
├── design.py        # MLIR generation (my_conv3d)
├── reference.py     # CPU reference (torch.nn.Conv3d)
└── test.py          # Pytest test suite

aie_kernels/aie2/conv3d.cc    # AIE2 kernel (vec_factor=8)
aie_kernels/aie2p/conv3d.cc   # AIE2P kernel (vec_factor=16)
```

### 5.2 Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Support 5D input (N, C, T, H, W) | Matches both video and blocked text formats |
| Separate kernels for depthwise/pointwise | Optimization paths like Conv2D |
| Configurable num_aie_columns (1-8) | Scale from NPU to NPU2 |
| Tile size parameter | Enable NPU memory optimization |
| Groups support | Enable GQA-style operations |

### 5.3 Kernel API Design

```cpp
// AIE2: vec_factor = 8
void conv3d_bf16_vector(
    bfloat16* input, bfloat16* weight, bfloat16* output,
    int N, int C, int T, int H, int W,  // Input dimensions
    int out_T, int out_H, int out_W,     // Output dimensions
    int kT, int kH, int kW,              // Kernel sizes
    int sT, int sH, int sW,              // Strides
    int pT, int pH, int pW,              // Padding
    int groups
);

// AIE2P: vec_factor = 16 (enhanced throughput)
void conv3d_bf16_vector_enhanced(...);  // Same signature, optimized implementation
```

---

## 6. After Conv3D: Related Operators

Once Conv3D is complete, consider these extensions:

| Operator | Purpose | Priority |
|----------|---------|----------|
| Conv3DTranspose | Video generation, decoding | Medium |
| MaxPool3D / AveragePool3D | Video downsampling | Low |
| Attention-specific kernels | Dedicated MHA optimization | High |
| Shape manipulation utilities | Reshape/permute helpers | High |

---

## 7. Immediate Next Steps

1. **Implement Conv3D operator** (`iron/operators/conv3d/`)
   - Follow established pattern from Conv2D
   - Support both semantic and compute-primitive use cases

2. **Create AIE2/AIE2P kernels** (`aie_kernels/*/conv3d.cc`)
   - vec_factor=8 for AIE2
   - vec_factor=16 for AIE2P

3. **Update exports and documentation**
   - Add to `iron/operators/__init__.py`
   - Update README.md operator dashboard

4. **Test with both use cases**
   - Video convolution (semantic)
   - Shape-manipulated text operations (compute primitive)

---

## 8. Verification Checklist

- [x] Conv3D op.py follows Conv2D pattern
- [x] design.py generates correct MLIR for 5D tensors
- [x] Kernels use correct vec_factor per architecture (8 for AIE2, 16 for AIE2P)
- [x] Test suite covers both video and text use cases
- [x] README.md updated with Conv3D entry
- [x] __init__.py exports AIEConv3d
- [x] Kernel files created for both AIE2 and AIE2P
- [x] Syntax errors fixed and verified

### Verification Summary (Completed)

All Conv3D implementation files have been verified:

| File | Status | Notes |
|------|--------|-------|
| `iron/operators/conv3d/op.py` | ✅ | Correct buffer calculations, kernel selection logic |
| `iron/operators/conv3d/design.py` | ✅ | 21 parameters match C++ signatures |
| `iron/operators/conv3d/reference.py` | ✅ | Uses torch.nn.functional.conv3d |
| `iron/operators/conv3d/test.py` | ✅ | Parametrized tests for all configurations |
| `iron/operators/conv3d/__init__.py` | ✅ | Exports AIEConv3d |
| `aie_kernels/aie2/conv3d.cc` | ✅ | vec_factor=8, 4 kernel variants |
| `aie_kernels/aie2p/conv3d.cc` | ✅ | vec_factor=16, 5 kernel variants (incl. large_kernel) |

---

## 9. References

### Internal Documentation
- [`iron/operators/conv2d/`](./iron/operators/conv2d/) - Conv2D implementation reference
- [`iron/operators/conv3d/`](./iron/operators/conv3d/) - Conv3D implementation (complete)
- [`iron/operators/reduction/`](./iron/operators/reduction/) - Reduction implementation
- [README.md](./README.md) - Operator dashboard

### External References
- Apple CoreML Conv2D trick for Linear layers
- Qualcomm Hexagon 5D/6D tiled layouts
- Huawei Ascend 5D fractal format
- Grouped Query Attention (GQA) in Llama 3, Mistral

---

## 10. Implementation Complete - Summary

The Conv3D operator has been fully implemented and verified for both AIE2 (NPU) and AIE2P (NPU2) architectures.

### Key Achievements

1. **Dual-Purpose Design**: Conv3D supports both:
   - Semantic video convolution (standard 5D tensors)
   - Compute primitive for text models (via shape manipulation)

2. **Kernel Variants**:
   - `conv3d_bf16_vector` - Standard vectorized convolution
   - `depthwise_conv3d_bf16_vector` - Channel-wise convolution
   - `pointwise_conv3d_bf16_vector` - 1x1x1 convolution (Linear layer equivalent)
   - `conv3d_bf16_large_kernel` - Optimized for large kernels (AIE2P only)

3. **Architecture Support**:
   - AIE2 (NPU): 4x4 array, vec_factor=8
   - AIE2P (NPU2): 4x8 array, vec_factor=16

4. **Configuration Flexibility**:
   - Configurable kernel_size, stride, padding (temporal, height, width)
   - Grouped convolution support (including depthwise)
   - Optional bias
   - Scalable column allocation (1-8 columns)

### Next Steps

With Conv3D complete, the IRON project now has a comprehensive set of operators for both video and text model inference on AMD Ryzen AI NPUs. The Conv3D operator enables:

- Video understanding models (video classification, action recognition)
- Compute primitives for LLM operations via shape manipulation
- Foundation for custom attention mechanisms
- Building block for 3D vision transformers

---

<p align="center">
Copyright&copy; 2025 Advanced Micro Devices, Inc
</p>
