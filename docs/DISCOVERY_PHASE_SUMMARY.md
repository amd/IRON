# IRON-Lemonade Integration: Discovery Phase - Summary

**Date:** 2026-03-15
**Author:** Jordan Blake, Principal Software Engineer & Technical Lead
**Status:** SUPERSEDED - Option B+ Strategic Pivot

---

## Executive Summary

**UPDATE 2026-03-15:** This document has been SUPERSEDED by the Option B+ strategic decision.

**CRITICAL INTELLIGENCE:** FastFlowLM production infrastructure discovered at `C:\Program Files\flm`:

### FastFlowLM Installation Analysis

**Location:** `C:\Program Files\flm\`

**Pre-compiled .xclbin files (30+ model families):**
```
xclbins/
├── Llama-3.2-1B-NPU2/       (attn.xclbin, dequant.xclbin, layer.xclbin, mm.xclbin)
├── Llama-3.2-3B-NPU2/
├── Llama-3.1-8B-NPU2/
├── GPT-OSS-20B-NPU2/        (attn, dequant, expert, layer, mm, short_seq_mm)
├── Qwen3-8B-NPU2/
├── Qwen3-4B-NPU2/
├── Gemma3-4B-NPU2/
├── Phi4-mini-Instruct-NPU2/
├── DeepSeek-R1-Distill-Llama-8B-NPU2/
└── ... (25+ more model families)
```

**NPU DLLs (Windows runtime):**
```
Shared Operator DLLs:
- gemm.dll (163 KB)      - General matrix multiplication
- mha.dll (169 KB)       - Multi-head attention
- dequant.dll (378 KB)   - Q4 quantization handling
- lm_head.dll (1.4 MB)   - Language model head projection

Model-Family DLLs:
- llama_npu.dll (1.5 MB)
- qwen3_npu.dll (1.5 MB)
- gemma_npu.dll (1.7 MB)
- gpt_oss_npu.dll (1.7 MB)
- phi4_npu.dll (1.5 MB)
- qwen2_npu.dll, qwen2vl_npu.dll, whisper_npu.dll, etc.

Core Runtime:
- flm.exe (6.2 MB)       - FastFlowLM executable
- npu_utils.dll (488 KB) - NPU utilities
- q4_npu_eXpress.dll     - Quantized execution engine
```

**Model Format (from model_list.json):**
- Distributed via HuggingFace: `FastFlowLM/<model-name>`
- Quantized weights: `.q4nx` format (Q4_0, Q4_1)
- Configuration: `config.json`, `tokenizer.json`, `tokenizer_config.json`
- Vision models: Additional `vision_weight.q4nx`
- Versioned releases with `flm_min_version` requirements
- Memory footprints: 0.62 GB (Embedding-Gemma) to 14 GB (GPT-OSS-20B)

### Strategic Implications

**What FastFlowLM Has Solved:**
1. **Windows NPU Deployment** - Pre-compiled kernels + DLL runtime
2. **Large-Scale Models** - GPT-OSS-20B (20B parameters, 14GB footprint)
3. **Cross-Platform .xclbins** - Same kernel files work on Linux and Windows
4. **Model Distribution** - HuggingFace pipeline with versioning
5. **Memory Optimization** - Documented footprints per model
6. **Quantization** - Q4_0/Q4_1 format with specialized runtime

**Our Original Strategy (Now Obsolete):**
- 4 Discovery Tasks (kernel audit, runtime audit, format analysis, API review)
- Build C++ runtime abstraction layer from scratch
- XRT backend with runtime MLIR compilation (Linux)
- xDNA backend with custom .xclbin loading (Windows)
- Estimated: 10-14 weeks to MVP

**New Strategy (Option B+):**
- Leverage FastFlowLM .xclbin files directly
- Build thin C++ wrapper around FFLM DLLs (Windows)
- Use XRT with FFLM .xclbins (Linux)
- Maintain MLIR fallback for custom operators
- Estimated: 4-6 weeks to MVP

---

## Original Document Follows (for reference)

---

## Deliverables Created

### 1. Technical Design Document

**File:** `docs/TECHNICAL_DESIGN_DISCOVERY_PHASE.md`

**Contents:**
- Part 1: Discovery Task Technical Specifications (4 tasks)
- Part 2: FastFlowLM .xclbin Kernel Audit (detailed plan)
- Part 3: IXclbinRuntime Interface Design (C++ header)
- Part 4: Revised Phase 1 Implementation Plan
- Part 5: Technical Questions for FastFlowLM Team

### 2. Discovery Tools

**Directory:** `iron/runtime/tools/`

| Tool | Purpose |
|------|---------|
| `xclbin_inspector.py` | Extract kernel interfaces from .xclbin files |
| `kernel_comparator.py` | Compare FastFlowLM kernels with IRON operators |

**Supporting Files:**
- `iron/runtime/tools/README.md` - Usage documentation
- `iron/runtime/include/iron/runtime/ixclbin_runtime.h` - C++ interface design

---

## Discovery Tasks Overview

### Task 1: FastFlowLM Kernel Audit (Priority #1)

**Duration:** Week 1-2
**Owner:** TBD

**Objective:** Inventory all available kernels in FastFlowLM .xclbin files and map to IRON operators.

**Commands:**
```bash
# Find FastFlowLM .xclbin files
find ~/.config/flm -name "*.xclbin" 2>/dev/null

# Run inspector
python iron/runtime/tools/xclbin_inspector.py path/to/kernel.xclbin output.json

# Run compatibility analysis
python iron/runtime/tools/kernel_comparator.py output.json report.md
```

**Success Criteria:**
- Complete kernel inventory
- Interface signatures documented
- IRON compatibility mapping (EXACT/COMPATIBLE/INCOMPATIBLE)
- Licensing clarity

### Task 2: xDNA Runtime Feature Audit

**Duration:** Week 1
**Owner:** TBD

**Objective:** Understand xDNA runtime API on Windows and compare with XRT.

**Deliverables:**
- `discovery/xdna/xrt_api.json`
- `discovery/xdna/xdna_api.json`
- `discovery/xdna/api_comparison.md`

**Success Criteria:**
- XRT API documented
- xDNA API documented (if accessible)
- Common patterns identified
- Abstraction design draft

### Task 3: .xclbin Format Analysis

**Duration:** Week 1
**Owner:** TBD

**Objective:** Understand .xclbin binary format and platform compatibility.

**Commands:**
```bash
# Use xclbinutil (if available)
xclbinutil --info --input kernel.xclbin

# Run format analyzer
python iron/runtime/tools/xclbin_format_analyzer.py kernel.xclbin analysis.json
```

**Success Criteria:**
- Header structure documented
- Section inventory complete
- Platform differences identified
- Cross-platform strategy defined

### Task 4: Lemonade Backend API Review

**Duration:** Week 1 (2-3 days)
**Owner:** TBD

**Objective:** Understand WrappedServer interface requirements.

**Deliverables:**
- `discovery/lemonade/wrapped_server_api.md`
- `discovery/lemonade/backend_lifecycle.md`

**Success Criteria:**
- WrappedServer interface documented
- Lifecycle understood
- Integration points identified
- Model format clarified

---

## Week 2 GO/NO-GO Decision

### Decision Criteria

**GO (Proceed with Implementation):**
- 80%+ critical operator compatibility (GEMM, RMSNorm, RoPE, SwiGLU, Softmax)
- No legal blockers for kernel redistribution
- .xclbin files loadable programmatically
- xDNA runtime provides equivalent functionality to XRT

**NO-GO (Alternative Approach):**
- Critical operators incompatible (no matching kernels)
- .xclbin format is platform-specific
- Licensing restrictions prevent redistribution
- xDNA runtime missing critical APIs

### Contingency Options (if NO-GO)

1. **Option A:** Linux-only backend (XRT), Windows deferred
2. **Option B:** Continue with IRON's MLIR runtime compilation for both platforms
3. **Option C:** Partner with AMD/FastFlowLM team for kernel interface documentation

---

## Implementation Timeline (if GO)

### Week 3-5: C++ Runtime Abstraction

**Deliverables:**
- `iron/runtime/ixclbin_runtime.h` - Core interface (draft complete)
- `iron/runtime/xrt_runtime.h/.cpp` - Linux XRT implementation
- `iron/runtime/xdna_runtime.h/.cpp` - Windows xDNA implementation
- `iron/runtime/platform_utils.h/.cpp` - Platform detection
- `iron/runtime/CMakeLists.txt` - Build configuration

**Milestones:**
- Week 3: Interface finalization, platform detection
- Week 4: XRT implementation (Linux)
- Week 5: xDNA implementation (Windows)

### Week 6-10: Linux XRT Backend

**Week 6-7:** MLIR integration, runtime compilation
**Week 8-9:** Buffer management, optimization
**Week 10:** Integration testing, documentation

---

## File Structure

```
IRON/
├── docs/
│   ├── TECHNICAL_DESIGN_DISCOVERY_PHASE.md    # Complete technical design
│   └── DISCOVERY_PHASE_SUMMARY.md             # This document
├── iron/
│   └── runtime/
│       ├── tools/
│       │   ├── xclbin_inspector.py            # .xclbin analysis tool
│       │   ├── kernel_comparator.py           # Compatibility analysis
│       │   └── README.md                      # Tool documentation
│       ├── include/iron/runtime/
│       │   └── ixclbin_runtime.h              # C++ interface design
│       └── CMakeLists.txt                     # To create (Week 3)
└── discovery/                                 # To be populated
    ├── fastflowlm/
    │   ├── xclbins/                           # .xclbin files for analysis
    │   ├── kernels/                           # JSON kernel descriptions
    │   └── kernel_audit.md                    # Final report
    ├── xdna/
    │   ├── xrt_api.json
    │   ├── xdna_api.json
    │   └── runtime_audit.md
    ├── xclbin_format/
    │   ├── analysis.json
    │   └── analysis.md
    └── lemonade/
        └── wrapped_server_api.md
```

---

## Quick Start

### Step 1: Set Up Discovery Environment

```bash
# Create discovery directory
mkdir -p discovery/fastflowlm/xclbins/
mkdir -p discovery/fastflowlm/kernels/

# Copy .xclbin files for analysis
cp ~/.config/flm/models/*/src/xclbins/*.xclbin discovery/fastflowlm/xclbins/
```

### Step 2: Run Kernel Inspection

```bash
cd discovery/fastflowlm/

# Inspect each .xclbin file
for xclbin in xclbins/*.xclbin; do
    python ../../iron/runtime/tools/xclbin_inspector.py \
        "$xclbin" \
        "kernels/$(basename ${xclbin%.xclbin}).json"
done
```

### Step 3: Run Compatibility Analysis

```bash
# Generate combined compatibility report
python ../../iron/runtime/tools/kernel_comparator.py \
    kernels/*.json \
    > compatibility_report.md

# View GO/NO-GO recommendation
grep -A 10 "GO/NO-GO" compatibility_report.md
```

---

## Technical Questions for FastFlowLM Team

Key questions to resolve during discovery:

1. **Kernel ABI:** What is the exact kernel argument ordering and types?
2. **Interface Stability:** Are kernel interfaces stable across versions?
3. **Cross-Platform:** Are .xclbin files cross-platform (Linux/Windows)?
4. **Licensing:** Can FastFlowLM kernels be redistributed with IRON?
5. **Runtime API:** What is the proper xDNA runtime initialization sequence?

See `docs/TECHNICAL_DESIGN_DISCOVERY_PHASE.md` Part 5 for complete list (22 questions).

---

## Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| FastFlowLM kernels incompatible | Medium | High | Early audit (Week 1), fallback to MLIR |
| xDNA runtime API insufficient | Medium | High | Runtime audit (Week 1), CPU fallback |
| .xclbin format platform-specific | Low | High | Format analysis (Week 1), separate paths |
| Licensing blocks redistribution | Low | Critical | Legal review early |
| No Windows test environment | Medium | Medium | Linux dev, remote Windows testing |

---

## Next Actions

1. **Approve technical design** - Review `docs/TECHNICAL_DESIGN_DISCOVERY_PHASE.md`
2. **Assign discovery task owners** - Identify team members for each task
3. **Set up FastFlowLM access** - Ensure team has access to FastFlowLM kernels
4. **Clone Lemonade repository** - `git clone https://github.com/lemonade-sdk/lemonade`
5. **Begin Week 1 discovery** - Start with kernel audit and format analysis

---

## References

- `docs/TECHNICAL_DESIGN_DISCOVERY_PHASE.md` - Complete technical design
- `docs/IRON_LEMONADE_INTEGRATION.md` - Overall integration plan
- `docs/LEMONADE_INTEGRATION_PLAN.md` - Original integration plan
- `iron/runtime/tools/README.md` - Discovery tools documentation
- `iron/runtime/include/iron/runtime/ixclbin_runtime.h` - C++ interface design

---

**Document End**

*Copyright &copy; 2026 Advanced Micro Devices, Inc. All rights reserved.*
