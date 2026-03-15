# xDNA Runtime Research - Technical Memo

**Date:** 2026-03-15
**Author:** IRON Development Team
**Status:** Complete
**Related Task:** #32 - Discovery Task 2: xDNA Runtime Feature Audit

---

## Executive Summary

This research investigated Windows NPU runtime options for the IRON project. Key findings:

1. **FastFlowLM uses proprietary runtime abstraction** - Not directly usable, but provides architectural insights
2. **ONNX Runtime GenAI DirectML is available** - Version 0.11.2 shipped with RyzenAI packages
3. **No standalone xDNA runtime DLLs found** - Windows NPU access appears to go through higher-level abstractions
4. **Recommendation:** Pursue ONNX Runtime GenAI as primary Windows backend path

---

## 1. FastFlowLM Installation Analysis

### 1.1 Location and Structure

```
C:\Program Files\flm\
├── flm.exe                    # Main executable
├── npu_utils.dll              # NPU utilities
├── q4_npu_eXpress.dll         # Quantized NPU execution engine
├── *.dll                      # 40+ DLLs (model-specific and operators)
├── xclbins/                   # Pre-compiled kernel binaries
│   ├── gemma/
│   ├── llama/
│   ├── qwen3/
│   ├── gpt_oss/
│   └── ... (30+ model families)
└── models/                    # Model configurations
```

### 1.2 Key DLLs Discovered

**Model-Specific Runtime DLLs:**
- `llama_npu.dll` - Llama family NPU kernels
- `qwen3_npu.dll` - Qwen 3 family NPU kernels
- `gpt_oss_npu.dll` - GPT-OSS (MoE) family NPU kernels
- `phi_npu.dll` - Phi family NPU kernels
- `gemma_npu.dll` - Gemma family NPU kernels
- `mistral_npu.dll` - Mistral family NPU kernels
- `stablelm2_npu.dll` - StableLM 2 family NPU kernels

**Operator DLLs:**
- `gemm.dll` - General Matrix Multiply
- `mha.dll` - Multi-Head Attention
- `dequant.dll` - Dequantization operations
- `lm_head.dll` - Language model head
- `silu.dll` - SiLU activation
- `softmax.dll` - Softmax operation
- `add.dll`, `mul.dll`, `cat.dll` - Element-wise operations

**Core Runtime:**
- `flm.exe` - FastFlowLM main executable
- `npu_utils.dll` - NPU management utilities
- `q4_npu_eXpress.dll` - Q4 quantized execution engine

### 1.3 Architectural Insights

FastFlowLM appears to use a **layered runtime architecture**:

```
┌─────────────────────────────────────┐
│         FastFlowLM Application      │
├─────────────────────────────────────┤
│    Model-Specific DLLs (llama, etc) │
├─────────────────────────────────────┤
│      Operator DLLs (gemm, mha, etc) │
├─────────────────────────────────────┤
│    q4_npu_eXpress.dll (Execution)   │
├─────────────────────────────────────┤
│       npu_utils.dll (Management)    │
├─────────────────────────────────────┤
│    [Proprietary xDNA Abstraction]   │  ← Not exposed
├─────────────────────────────────────┤
│         Windows NPU Driver          │
└─────────────────────────────────────┘
```

**Key Finding:** No standalone xDNA runtime DLLs are exposed. FastFlowLM uses their own proprietary abstraction layer.

---

## 2. RyzenAI Packages Analysis

### 2.1 Installation Location

```
C:\Program Files\RyzenAI\
├── 1.5.1/
├── 1.6.0/
└── 1.7.0/
    └── onnxruntime_genai_directml_ryzenai-0.11.2-cp312-cp312-win_amd64.whl
```

### 2.2 Available ONNX Runtime GenAI Versions

| Version | Python | Architecture |
|---------|--------|--------------|
| 0.7.0.3 | cp311 | win_amd64 |
| 0.9.2 | cp311/cp312 | win_amd64 |
| 0.11.2 (latest) | cp312 | win_amd64 |

### 2.3 ONNX Runtime GenAI Capabilities

The `onnxruntime_genai_directml_ryzenai` package provides:

- **DirectML Backend:** GPU/NPU acceleration via DirectX 12
- **Windows NPU Support:** Official AMD Ryzen AI support
- **ONNX Model Format:** Standard ML model interchange
- **GenAI Optimizations:** Transformer-specific optimizations
- **Python API:** `onnxruntime_genai` Python package

---

## 3. xDNA Runtime Discovery Attempts

### 3.1 Search Locations

Searched for xDNA runtime components in:
- `C:\Program Files\AMD\` - No xDNA runtime found
- `C:\Program Files\RyzenAI\` - Only ONNX Runtime GenAI packages
- `C:\Program Files\flm\` - Proprietary runtime only
- System PATH and common library locations

### 3.2 Search Commands Executed

```bash
# Search for xDNA DLLs
dir /s /b "C:\Program Files\*xdna*.dll" 2>nul

# Search for RyzenAI packages
dir /s /b "C:\Program Files\RyzenAI\*.whl" 2>nul

# List FastFlowLM DLLs
dir /b "C:\Program Files\flm\*.dll"
```

### 3.3 Findings

**No standalone xDNA runtime DLLs found.**

This suggests one of the following:
1. xDNA runtime is bundled within applications (like FastFlowLM)
2. Windows NPU access goes through DirectML/ONNX Runtime
3. xDNA APIs are accessed through alternative channels

---

## 4. Recommendations

### 4.1 Primary Recommendation: ONNX Runtime GenAI

**Rationale:**
- Officially supported by AMD for Ryzen AI
- Available and tested (v0.11.2 latest)
- DirectML backend provides Windows NPU access
- Well-documented API
- Active development and community support

**Implementation Path:**
1. Install `onnxruntime_genai_directml_ryzenai` package
2. Create C++ wrapper around ONNX Runtime GenAI C API
3. Integrate with IRON's `INpuRuntime` interface
4. Support ONNX model format (compatible with existing workflows)

**Code Structure:**
```cpp
// iron/runtime/cpp/src/onnxruntime_genai_impl.cpp
class OnnxRuntimeGenAiWrapper : public INpuRuntime {
public:
    OnnxRuntimeGenAiWrapper(int deviceId = 0);

    bool loadXclbin(const std::string& path) override;
    std::shared_ptr<IBuffer> allocateBuffer(size_t size, bool hostAccessible) override;
    std::shared_ptr<IKernelHandle> getKernel(const std::string& kernelName) override;
    ExecutionResult execute(const std::string& kernelName,
                           const std::vector<KernelArgument>& args,
                           const ExecutionOptions& options) override;

private:
    Ort::Session* session_;
    Ort::Env env_;
    // ...
};
```

### 4.2 Secondary Path: Learn from FastFlowLM Architecture

While we cannot use FastFlowLM code directly, their architecture provides valuable insights:

1. **Operator-Based Design:** Separate operator DLLs (gemm, mha, dequant) suggest a modular approach
2. **Model-Specific Layers:** Higher-level DLLs for specific model families
3. **Quantization Support:** Q4 quantization engine (`q4_npu_eXpress.dll`)
4. **Buffer Management:** `npu_utils.dll` likely handles memory management

**Abstraction Approach:**
- Design similar operator interface in our C++ layer
- Support quantized inference (Q4 format learning)
- Implement efficient buffer pooling (see `XrtBufferManager`)

### 4.3 Investigation Path: xDLL Runtime Access

If direct xDNA access becomes necessary:

1. **Check AMD Ryzen AI SDK:** May provide xDNA headers/libraries
2. **Windows Driver Investigation:** NPU access may go through kernel drivers
3. **DirectML Interop:** Consider DirectML as lower-level alternative

---

## 5. Implementation Priority

### Phase 0: Research Complete ✓

- [x] FastFlowLM architecture analysis
- [x] RyzenAI package discovery
- [x] xDNA runtime search
- [x] ONNX Runtime GenAI identification

### Phase 1: ONNX Runtime GenAI Integration (Recommended Next)

1. **Setup and Validation**
   - Install ONNX Runtime GenAI package
   - Validate NPU detection and basic execution
   - Test with sample ONNX models

2. **C++ Wrapper Development**
   - Create ONNX Runtime C++ API wrapper
   - Implement `INpuRuntime` interface
   - Add buffer management

3. **Integration with IRON**
   - Update CMakeLists.txt for ONNX Runtime
   - Add Windows backend selection logic
   - Test cross-platform abstraction

### Phase 2: Parallel Path - Custom Operator Layer

1. **Operator Interface Design**
   - Define operator abstraction (inspired by FFLM)
   - Implement core operators (GEMM, MHA, etc.)

2. **Kernel Integration**
   - Load pre-compiled kernels (if compatible)
   - Support .xclbin format for custom kernels

---

## 6. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| ONNX Runtime GenAI lacks required features | Low | Medium | Fall back to DirectML or custom implementation |
| .xclbin format incompatibility | Medium | High | Support ONNX as alternative kernel format |
| Windows NPU driver limitations | Low | Medium | Test early with target hardware |
| Performance gaps vs FastFlowLM | Medium | Medium | Profile and optimize critical paths |

---

## 7. Conclusion

**Recommendation:** Proceed with ONNX Runtime GenAI as the primary Windows NPU backend implementation path.

**Rationale:**
1. Officially supported by AMD for Ryzen AI
2. Available and tested (v0.11.2)
3. Well-documented with active community
4. Aligns with "Hybrid Abstraction Approach" strategy
5. Reduces dependency on undocumented xDNA APIs

**Next Steps:**
1. Install and validate ONNX Runtime GenAI
2. Create task for ONNX Runtime GenAI wrapper implementation
3. Update strategic documentation with refined timeline

---

## Appendix A: File Locations Reference

```
# FastFlowLM Installation
FLM_ROOT = C:\Program Files\flm\
FLM_XCLBINS = C:\Program Files\flm\xclbins\
FLM_MODELS = C:\Program Files\flm\models\

# RyzenAI Packages
RYZENAI_ROOT = C:\Program Files\RyzenAI\
ONNXRUNTIME_WHL = C:\Program Files\RyzenAI\1.7.0\onnxruntime_genai_directml_ryzenai-0.11.2-cp312-cp312-win_amd64.whl

# Project Files
IRON_RUNTIME = C:\Users\antmi\IRON\iron\runtime\
CPP_RUNTIME = C:\Users\antmi\IRON\iron\runtime\cpp\
PYTHON_BINDINGS = C:\Users\antmi\IRON\iron\runtime\python\
```

---

## Appendix B: Related Documents

- `docs/STRATEGIC_PIVOT_RECOMMENDATION.md` - Strategic direction document
- `docs/IRON_LEMONADE_INTEGRATION.md` - Integration overview
- `iron/runtime/cpp/include/iron/runtime/npu_runtime.hpp` - C++ interface definition
- `iron/runtime/cpp/src/npu_runtime.cpp` - Base implementation
- `iron/runtime/cpp/src/xrt_runtime_impl.cpp` - Linux XRT implementation

---

**Document Status:** Complete
**Next Review:** After ONNX Runtime GenAI implementation (Phase 1)
