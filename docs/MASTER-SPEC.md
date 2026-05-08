# MASTER SPEC: Model Converter Analysis

**Source:** `feature/model-converter-analysis` (239 files, +85,036 lines)
**Target:** `devel` via 45 PRs + 2 tracked issues
**Date:** 2026-05-07

## Overview
Decomposed 239-file mega-branch into 47 focused branches with 33 spec sheets and 4 planning docs. Every new file is assigned to exactly one branch.

## Document Index
- `docs/BRANCH-STRATEGY-PIPELINE-ANALYSIS.md` - Merge order, dependency graph
- `docs/GAP-ANALYSIS-MASTER.md` - Gap status and tracker
- `docs/RISK-REGISTER.md` - 5 risks with mitigation
- `docs/PR-TRACKER.md` - Detailed PR tracker by phase

## Complete PR Inventory

### Phase 1: Infrastructure Foundation (11 PRs)

| PR | Branch | Spec | Description |
|----|--------|------|-------------|
| [#1](https://github.com/antmikinka/IRON/pull/1) | feature/project-files | SPEC-031 | Update root project files (.gitignore, pyproject.toml, README.md, requirements.txt) |
| [#2](https://github.com/antmikinka/IRON/pull/2) | feature/common-module | SPEC-025 | Add AIE common module (aie_mock, base device manager, compilation utilities) |
| [#3](https://github.com/antmikinka/IRON/pull/3) | feature/operator-infrastructure | SPEC-029 | Add operator infrastructure (CMakeLists.txt, shared op.py updates for dequant/gemv/rope/softmax) |
| [#4](https://github.com/antmikinka/IRON/pull/4) | feature/cpp-tests | SPEC-030 | Add C++ tests (8 files: rmsnorm, rope, silu, softmax operators + kv_cache, memory_budget, model_loader, rope_cache runtime) |
| [#5](https://github.com/antmikinka/IRON/pull/5) | feature/runtime-cpp-core | SPEC-027 | Add C++ runtime core (21 files: NPU runtime, KV cache, memory budget, model loader, rope cache, XDNA/XRT implementations) |
| [#6](https://github.com/antmikinka/IRON/pull/6) | feature/runtime-python-bindings | SPEC-028 | Add Python pybind11 bindings for C++ runtime (4 files) |
| [#7](https://github.com/antmikinka/IRON/pull/7) | feature/runtime-tools | SPEC-032 | Add runtime tools (kernel comparator, xclbin inspector utilities) |
| [#8](https://github.com/antmikinka/IRON/pull/8) | feature/misc-scripts | SPEC-033 | Add misc scripts (baseline results, forward test scripts, week 2 quality tests) |
| [#9](https://github.com/antmikinka/IRON/pull/9) | feature/api-server-layer | SPEC-023 | Add API server layer (auto-converter, generation config, model registry, HTTP server, tokenizers) |
| [#10](https://github.com/antmikinka/IRON/pull/10) | feature/converter-core | SPEC-024 | Add model converter core (CLI, converter, layer builder, model assembler, operator factory, shape manager, weight mapper) |
| [#11](https://github.com/antmikinka/IRON/pull/11) | feature/model-registry | SPEC-026 | Add model registry (registry, configuration, test utilities) |

### Phase 2: Operator Fixes (16 PRs)

| PR | Branch | Spec | Description |
|----|--------|------|-------------|
| [#12](https://github.com/antmikinka/IRON/pull/12) | fix/axpy-operator | SPEC-005-A | Fix AXPY operator implementation |
| [#13](https://github.com/antmikinka/IRON/pull/13) | fix/dequant-operator | SPEC-005-B | Fix dequantization operator correctness |
| [#14](https://github.com/antmikinka/IRON/pull/14) | fix/weighted-rms-norm-operator | SPEC-005-C | Fix weighted RMS norm operator (design_weighted.py) |
| [#15](https://github.com/antmikinka/IRON/pull/15) | fix/tanh-operator | SPEC-005-D | Fix tanh activation operator |
| [#16](https://github.com/antmikinka/IRON/pull/16) | fix/transpose-operator | SPEC-005-E | Fix transpose operator (commit 84b2333) |
| [#17](https://github.com/antmikinka/IRON/pull/17) | fix/swiglu-decode-operator | SPEC-005-F | Fix SwiGLU decode operator (commit 588c3b9) |
| [#18](https://github.com/antmikinka/IRON/pull/18) | fix/gemm-gemv-operator | SPEC-005-G | Fix GEMM and GEMV operators |
| [#19](https://github.com/antmikinka/IRON/pull/19) | fix/gelu-operator | SPEC-005-H | Fix GELU activation operator |
| [#20](https://github.com/antmikinka/IRON/pull/20) | fix/relu-operator | SPEC-005-I | Fix ReLU activation operator |
| [#21](https://github.com/antmikinka/IRON/pull/21) | fix/sigmoid-operator | SPEC-005-J | Fix sigmoid activation operator |
| [#22](https://github.com/antmikinka/IRON/pull/22) | fix/silu-operator | SPEC-005-K | Fix SiLU activation operator |
| [#23](https://github.com/antmikinka/IRON/pull/23) | fix/layer_norm-operator | SPEC-005-L | Fix layer normalization operator |
| [#24](https://github.com/antmikinka/IRON/pull/24) | fix/rms_norm-operator | SPEC-005-M | Fix RMS normalization operator |
| [#25](https://github.com/antmikinka/IRON/pull/25) | fix/rope-fix-operator | SPEC-005-N | Fix RoPE positional embedding operator |
| [#26](https://github.com/antmikinka/IRON/pull/26) | fix/mem-copy-operator | SPEC-005-O | Fix memory copy operator |
| [#27](https://github.com/antmikinka/IRON/pull/27) | fix/eltwise-operator | SPEC-005-P | Fix elementwise add/mul operators |

### Phase 3: Feature Branches (7 PRs)

| PR | Branch | Spec | Description |
|----|--------|------|-------------|
| [#28](https://github.com/antmikinka/IRON/pull/28) | feature/model-analysis-framework | SPEC-001 | Add model analysis framework (12 files, 7,064 lines: architecture scanner, capability registry, gap analyzer, transformers integration) |
| [#29](https://github.com/antmikinka/IRON/pull/29) | feature/benchmark-framework | SPEC-004 | Add benchmark framework (6 files, 7,072 lines: benchmark engine, CLI, reporter, profiler) |
| [#30](https://github.com/antmikinka/IRON/pull/30) | feature/generation-infra | SPEC-006 | Add generation infrastructure (15 files, 8,023 lines: generator, KV cache, tokenizer, streaming, sampler, Llama3.2 model) |
| [#31](https://github.com/antmikinka/IRON/pull/31) | feature/interactive-converter | SPEC-007 | Add interactive model converter CLI (1,897 lines) |
| [#32](https://github.com/antmikinka/IRON/pull/32) | feature/streaming-design | SPEC-008 | Add streaming architecture design docs (6 files, design only - Route B chunked inference) |
| [#33](https://github.com/antmikinka/IRON/pull/33) | feature/infrastructure-devel | SPEC-009 | Add development infrastructure (scripts, .clang-format, conftest.py) |
| [#34](https://github.com/antmikinka/IRON/pull/34) | feature/ironserver-backend | SPEC-003 | Add IronServer C++ backend via Lemonade (6 files, 813 lines) |

### Phase 4: NEW Operator Enablement (11 PRs)

| PR | Branch | Spec | Description |
|----|--------|------|-------------|
| [#35](https://github.com/antmikinka/IRON/pull/35) | feature/operator-types-runtime | SPEC-010 | Add operator type definitions and runtime interface (types.hpp, ixclbin_runtime.h) |
| [#36](https://github.com/antmikinka/IRON/pull/36) | feature/operator-reduction | SPEC-011 | Add reduction operator - sum, mean, max, min (7 files, AIE2 + AIE2P kernels) |
| [#37](https://github.com/antmikinka/IRON/pull/37) | feature/operator-conv2d | SPEC-012 | Add 2D convolution operator (7 files, 2,048 lines, AIE2 + AIE2P kernels) |
| [#38](https://github.com/antmikinka/IRON/pull/38) | feature/operator-maxpool | SPEC-013 | Add max pooling 2D operator (7 files, 1,299 lines, AIE2 + AIE2P kernels) |
| [#39](https://github.com/antmikinka/IRON/pull/39) | feature/operator-avgpool | SPEC-014 | Add average pooling 2D operator (7 files, 1,307 lines, AIE2 + AIE2P kernels) |
| [#40](https://github.com/antmikinka/IRON/pull/40) | feature/operator-conv3d | SPEC-015 | Add 3D convolution operator (8 files, 2,937 lines, AIE2 + AIE2P kernels) |
| [#41](https://github.com/antmikinka/IRON/pull/41) | feature/rope-bf16-operator | SPEC-016 | Add BF16 RoPE operator (2 files, 465 lines) |
| [#42](https://github.com/antmikinka/IRON/pull/42) | feature/rmsnorm-bf16-operator | SPEC-017 | Add BF16 RMSNorm operator (2 files, 311 lines) |
| [#43](https://github.com/antmikinka/IRON/pull/43) | feature/silu-bf16-operator | SPEC-018 | Add BF16 SiLU activation operator (2 files, 238 lines) |
| [#44](https://github.com/antmikinka/IRON/pull/44) | feature/softmax-bf16-operator | SPEC-019 | Add BF16 softmax operator (2 files, 301 lines) |
| [#45](https://github.com/antmikinka/IRON/pull/45) | feature/onnx-runtime-genai-backend | SPEC-022 | Add ONNX Runtime GenAI backend (2 files, 1,259 lines) |

### Tracked (No PR Needed)

| Issue | Branch | Spec | Description |
|-------|--------|------|-------------|
| [#47](https://github.com/antmikinka/IRON/issues/47) | feature/gqa-optimization | SPEC-020 | GQA optimization - already merged to devel via PR #73 |
| [#48](https://github.com/antmikinka/IRON/issues/48) | feature/llama32-operator-analysis | SPEC-021 | Llama3.2 operator analysis - documentation already on devel |

## Spec Sheet Index

| Spec | Category | PR |
|------|----------|-----|
| SPEC-001 | Model Analysis Framework | #28 |
| SPEC-002 | AIE2 Operator Kernels (Aggregate) | Superseded |
| SPEC-003 | IronServer Backend | #34 |
| SPEC-004 | Benchmark Framework | #29 |
| SPEC-005-A-P | 16 Operator Fixes | #12-#27 |
| SPEC-006 | Generation Infrastructure | #30 |
| SPEC-007 | Interactive Converter | #31 |
| SPEC-008 | Streaming Architecture | #32 |
| SPEC-009 | Infrastructure Housekeeping | #33 |
| SPEC-010 | Operator Types Runtime | #35 |
| SPEC-011 | Reduction Operator | #36 |
| SPEC-012 | Conv2D Operator | #37 |
| SPEC-013 | MaxPool Operator | #38 |
| SPEC-014 | AvgPool Operator | #39 |
| SPEC-015 | Conv3D Operator | #40 |
| SPEC-016 | RoPE BF16 Operator | #41 |
| SPEC-017 | RMSNorm BF16 Operator | #42 |
| SPEC-018 | SiLU BF16 Operator | #43 |
| SPEC-019 | Softmax BF16 Operator | #44 |
| SPEC-020 | GQA Optimization | Issue #47 |
| SPEC-021 | Llama3.2 Analysis | Issue #48 |
| SPEC-022 | ONNX Runtime GenAI | #45 |
| SPEC-023 | API Server Layer | #9 |
| SPEC-024 | Converter Core | #10 |
| SPEC-025 | Common Module | #2 |
| SPEC-026 | Model Registry | #11 |
| SPEC-027 | Runtime C++ Core | #5 |
| SPEC-028 | Runtime Python Bindings | #6 |
| SPEC-029 | Operator Infrastructure | #3 |
| SPEC-030 | C++ Tests | #4 |
| SPEC-031 | Project Files | #1 |
| SPEC-032 | Runtime Tools | #7 |
| SPEC-033 | Misc Scripts | #8 |

## Metrics

| Metric | Value |
|--------|-------|
| Total new files from mega-branch | 203 |
| Files assigned to branches | 203 |
| Coverage | 100% |
| Total branches | 48 |
| PRs open | 45 |
| Issues (tracked, no PR) | 2 |
| Spec sheets | 33 |
| Planning documents | 4 |

## Merge Priority Order

1. **Phase 1** - Foundation (PRs #1-#11): Infrastructure branches
2. **Phase 2** - Operator Fixes (PRs #12-#27): 16 operator fix branches
3. **Phase 3** - Features (PRs #28-#34): 7 feature branches
4. **Phase 4** - NEW Operators (PRs #35-#45): 11 new operator branches

## Status: COMPLETE

All branches decomposed, spec sheets written, PRs created and open.
