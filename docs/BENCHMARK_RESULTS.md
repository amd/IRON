# IRON Performance Benchmark Results

**Document Type:** Performance Benchmark Report
**Date:** 2026-03-15
**Author:** IRON Engineering Team
**Status:** BASELINE TARGETS DEFINED - AWAITING MEASUREMENT

---

## Executive Summary

This document establishes performance targets and will contain benchmark results for the IRON NPU runtime framework. As of 2026-03-15, **no empirical benchmarks have been collected**. The targets below are based on:
- FastFlowLM reference implementations
- Industry-standard LLM inference metrics
- AMD Ryzen AI NPU hardware specifications

**Test Hardware:** AMD Ryzen AI NPU (AIE2 architecture)
**Test Software:** Windows 11, ONNX Runtime GenAI v0.11.2 with DirectML

---

## 1. Benchmark Targets

### 1.1 End-to-End Targets by Model

| Model | Parameters | TTFT Target | Token/s Target | Memory Target |
|-------|------------|-------------|----------------|---------------|
| **Llama3.2-1B** | 1.23B | <100ms | >20 tok/s | <1.5 GB |
| **Llama3.2-3B** | 3.21B | <150ms | >12 tok/s | <2.7 GB |
| **Gemma2-2B** | 2.61B | <120ms | >15 tok/s | <2.0 GB |
| **Qwen2.5-1.5B** | 1.54B | <100ms | >18 tok/s | <1.7 GB |
| **Phi3-mini** | 3.82B | <150ms | >12 tok/s | <2.8 GB |

### 1.2 Metric Definitions

| Metric | Description | Measurement Method |
|--------|-------------|-------------------|
| **TTFT (Time to First Token)** | Time from prompt submission to first token generated | `time(first_token) - time(prompt_end)` |
| **Token Generation Speed** | Sustained tokens per second during generation | `total_tokens / generation_time` |
| **Memory Footprint** | Peak process memory during inference | `max(memory_usage) - baseline` |
| **NPU Utilization** | Percentage of NPU compute units active | Hardware performance counters |
| **Power Efficiency** | Tokens per watt | `tokens / (average_watts * seconds)` |

---

## 2. Operator-Level Benchmarks

### 2.1 Transformer Operator Targets (Llama3.2-1B)

| Operator | Latency Target | Memory Bandwidth | Compute Intensity |
|----------|---------------|------------------|-------------------|
| **RoPE** | <0.5ms | Low (element-wise) | Low (FLOPs/byte <1) |
| **RMSNorm** | <1.0ms | Medium (reduction) | Low (FLOPs/byte ~1) |
| **SiLU** | <0.3ms | Low (element-wise) | Low (FLOPs/byte <1) |
| **Softmax** | <2.0ms | High (reduction + exp) | Medium (FLOPs/byte ~2) |
| **GEMM (QKV)** | <5.0ms | Very High | High (FLOPs/byte >100) |
| **GEMM (MLP)** | <8.0ms | Very High | High (FLOPs/byte >100) |
| **Attention (QK^T)** | <3.0ms | High | High (FLOPs/byte >50) |

### 2.2 Conv2D Operator Targets (for Multimodal)

| Kernel | Input Shape | Latency Target | Use Case |
|--------|-------------|----------------|----------|
| `conv2d_bf16_vector` | [1, 3, 224, 224], 3x3, 64 | <5ms | ViT patch embedding |
| `depthwise_conv2d_bf16` | [1, 64, 56, 56], 3x3 | <2ms | MobileNet block |
| `pointwise_conv2d_bf16` | [1, 64, 56, 56], 1x1, 256 | <3ms | Channel mixing |

### 2.3 Conv3D Operator Targets (for Video)

| Kernel | Input Shape | Latency Target | Use Case |
|--------|-------------|----------------|----------|
| `conv3d_bf16_vector` | [1, 3, 16, 112, 112], 3x3x3 | <15ms | Video encoder |
| `depthwise_conv3d_bf16` | [1, 32, 8, 28, 28], 3x3x3 | <5ms | Spatiotemporal filter |

---

## 3. Benchmark Methodology

### 3.1 Test Configuration

```yaml
Hardware:
  NPU: AMD Ryzen AI (AIE2)
  CPU: AMD Ryzen 7 (for reference)
  Memory: 16GB LPDDR5

Software:
  OS: Windows 11 Pro 26200
  Runtime: ONNX Runtime GenAI DirectML v0.11.2
  IRON Version: 1.0.0
  Python: 3.11

Test Parameters:
  Precision: bfloat16 (where supported)
  Batch Size: 1
  Sequence Length: 128 (prompt), 256 (generation)
  Temperature: 0.7
  Top-P: 0.9
```

### 3.2 Measurement Procedure

1. **Warm-up:** Run 10 inference iterations to stabilize
2. **TTFT Measurement:**
   - Record timestamp before prompt processing
   - Record timestamp when first token is generated
   - TTFT = difference
3. **Token Speed Measurement:**
   - Generate 128 tokens
   - Record total generation time
   - Tokens/s = 128 / time
4. **Memory Measurement:**
   - Sample process memory every 100ms
   - Peak = max - baseline

### 3.3 Statistical Treatment

| Metric | Samples | Aggregation |
|--------|---------|-------------|
| TTFT | 100 runs | Median, P95, P99 |
| Token Speed | 100 runs | Mean, Std Dev |
| Memory | Continuous | Peak, Average |
| Operator Latency | 1000 runs | Median, P99 |

---

## 4. Benchmark Results (To Be Populated)

### 4.1 Llama3.2-1B Results

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| TTFT (128 token prompt) | _PENDING_ | <100ms | ⏳ Awaiting measurement |
| Token Generation Speed | _PENDING_ | >20 tok/s | ⏳ Awaiting measurement |
| Memory Footprint | _PENDING_ | <1.5 GB | ⏳ Awaiting measurement |
| NPU Utilization | _PENDING_ | >70% | ⏳ Awaiting measurement |

### 4.2 Operator Latency Results

| Operator | Median Latency | P99 Latency | Target | Status |
|----------|---------------|-------------|--------|--------|
| RoPE | _PENDING_ | _PENDING_ | <0.5ms | ⏳ Not implemented |
| RMSNorm | _PENDING_ | _PENDING_ | <1.0ms | ⏳ Not implemented |
| SiLU | _PENDING_ | _PENDING_ | <0.3ms | ⏳ Not implemented |
| Softmax | _PENDING_ | _PENDING_ | <2.0ms | ⏳ Not implemented |

### 4.3 Conv2D Operator Results

| Kernel | Median Latency | Target | Status |
|--------|---------------|--------|--------|
| `conv2d_bf16_vector` | _PENDING_ | <5ms | ✅ Implemented, ⏳ Not benchmarked |
| `depthwise_conv2d_bf16` | _PENDING_ | <2ms | ✅ Implemented, ⏳ Not benchmarked |
| `pointwise_conv2d_bf16` | _PENDING_ | <3ms | ✅ Implemented, ⏳ Not benchmarked |

---

## 5. Comparison with Reference Implementations

### 5.1 FastFlowLM Reference (Expected)

| Model | Platform | TTFT | Token/s | Source |
|-------|----------|------|---------|--------|
| Llama3.2-1B | Ryzen AI NPU | ~80ms | ~25 tok/s | FastFlowLM estimates |
| Llama3.2-3B | Ryzen AI NPU | ~120ms | ~15 tok/s | FastFlowLM estimates |

### 5.2 CPU/GPU Reference (For Context)

| Model | Platform | TTFT | Token/s | Source |
|-------|----------|------|---------|--------|
| Llama3.2-1B | CPU (Ryzen 7) | ~500ms | ~5 tok/s | Industry average |
| Llama3.2-1B | GPU (RTX 4070) | ~50ms | ~50 tok/s | Industry average |
| Llama3.2-1B | NPU (Ryzen AI) | _TARGET: 100ms_ | _TARGET: 20 tok/s_ | IRON target |

---

## 6. Performance Optimization Roadmap

### 6.1 Phase 1: Baseline (Current)

- ✅ C++ runtime abstraction complete
- ✅ ONNX Runtime GenAI backend complete
- ✅ Conv2D/Conv3D kernels implemented
- ⏳ Transformer operators pending
- ⏳ First benchmarks pending

### 6.2 Phase 2: Optimization (Weeks 1-4)

| Optimization | Expected Gain | Effort |
|--------------|---------------|--------|
| RoPE kernel optimization | +15% token/s | 1 week |
| RMSNorm optimization | +10% token/s | 1 week |
| Operator fusion (SiLU+Linear) | +20% token/s | 1 week |
| KV cache optimization | -30% memory | 2 weeks |

### 6.3 Phase 3: Advanced (Weeks 5-8)

| Optimization | Expected Gain | Effort |
|--------------|---------------|--------|
| Paged attention | -50% memory | 2 weeks |
| Flash attention variant | +30% token/s | 3 weeks |
| Quantization (INT8/INT4) | -50% memory, +2x speed | 4 weeks |

---

## 7. Benchmark Suite Implementation

### 7.1 Python Benchmark Script Template

```python
#!/usr/bin/env python3
"""
IRON Performance Benchmark Suite
Run with: python -m iron.benchmarks.run --model llama3.2-1b
"""

import time
import statistics
from iron.runtime import NpuRuntime
from transformers import AutoTokenizer, AutoModelForCausalLM

class IRONBenchmark:
    def __init__(self, model_path, prompt_length=128, generate_length=128):
        self.runtime = NpuRuntime.create()
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model_path = model_path
        self.prompt_length = prompt_length
        self.generate_length = generate_length

    def warmup(self, iterations=10):
        """Run warmup iterations"""
        for _ in range(iterations):
            # Warmup inference
            pass

    def measure_ttft(self, prompt):
        """Measure time to first token"""
        start = time.perf_counter()
        # Process prompt and get first token
        first_token = self.generate_one(prompt)
        end = time.perf_counter()
        return end - start

    def measure_token_speed(self, prompt, num_tokens=128):
        """Measure sustained token generation speed"""
        start = time.perf_counter()
        tokens = self.generate(prompt, num_tokens)
        end = time.perf_counter()
        return num_tokens / (end - start)

    def run_benchmark(self):
        """Run full benchmark suite"""
        self.warmup()

        ttft_results = []
        speed_results = []

        for _ in range(100):
            prompt = self.generate_prompt(self.prompt_length)
            ttft = self.measure_ttft(prompt)
            ttft_results.append(ttft)

            speed = self.measure_token_speed(prompt, self.generate_length)
            speed_results.append(speed)

        return {
            'ttft_median': statistics.median(ttft_results),
            'ttft_p95': sorted(ttft_results)[95],
            'token_speed_mean': statistics.mean(speed_results),
        }
```

### 7.2 C++ Operator Benchmark

```cpp
// benchmarks/operator_benchmark.cpp
#include <iron/runtime/npu_runtime.hpp>
#include <chrono>
#include <statistics>

template<typename OpFunc>
auto benchmark_operator(OpFunc op, size_t iterations = 1000) {
    // Warmup
    for (size_t i = 0; i < 10; ++i) {
        op();
    }

    // Measurement
    std::vector<double> latencies;
    auto start = std::chrono::high_resolution_clock::now();

    for (size_t i = 0; i < iterations; ++i) {
        auto op_start = std::chrono::high_resolution_clock::now();
        op();
        auto op_end = std::chrono::high_resolution_clock::now();

        double latency_ms = std::chrono::duration<double, std::milli>(
            op_end - op_start).count();
        latencies.push_back(latency_ms);
    }

    auto end = std::chrono::high_resolution_clock::now();
    auto total_time = std::chrono::duration<double, std::milli>(end - start).count();

    std::sort(latencies.begin(), latencies.end());

    return OperatorBenchmarkResult {
        .median = latencies[iterations / 2],
        .p99 = latencies[iterations * 99 / 100],
        .throughput_ops_per_sec = iterations / (total_time / 1000.0),
        .total_time_ms = total_time
    };
}
```

---

## 8. Tracking and Reporting

### 8.1 Update Schedule

| Report Type | Frequency | Owner |
|-------------|-----------|-------|
| Operator benchmarks | Weekly during development | Kernel Team |
| End-to-end benchmarks | Bi-weekly | Performance Team |
| Competitive analysis | Monthly | Strategy Team |

### 8.2 Dashboard Metrics

Key metrics to track on performance dashboard:

1. **TTFT Trend:** Week-over-week improvement
2. **Token/s Trend:** Throughput over time
3. **Memory Efficiency:** bytes/parameter ratio
4. **Operator Coverage:** % of required operators implemented

---

## 9. Action Items

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Implement RoPE kernel | Kernel Team | Week 1 | ⏳ Pending |
| Implement RMSNorm kernel | Kernel Team | Week 1 | ⏳ Pending |
| Create benchmark suite | Performance Team | Week 1 | ⏳ Pending |
| Collect baseline measurements | Performance Team | Week 2 | ⏳ Pending |
| Compare with FastFlowLM | Strategy Team | Week 2 | ⏳ Pending |

---

**Document History:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-15 | Initial creation with targets |

---

*Copyright © 2026 IRON Project. All rights reserved.*
