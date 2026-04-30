# IRON NPU - Streaming Architecture Initiative: Progress Document

> **Project**: Streaming Inference Architecture for AMD Ryzen AI NPU
> **Target Model**: Llama-3.2-1B (baseline), scalable to 7B+ models
> **Branch**: `feature/model-converter-analysis`
> **Last Updated**: 2026-04-29
> **Status**: Phase 0 Pending (Architecture Design Complete, awaiting NPU driver spike)
> **Owner**: Dr. Sarah Kim, Technical Product Strategist & Engineering Lead

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [What Has Been Done](#2-what-has-been-done)
3. [What Was Analyzed](#3-what-was-analyzed)
4. [Current State](#4-current-state)
5. [Open Questions](#5-open-questions)
6. [Agent Consensus](#6-agent-consensus)
7. [Next Steps](#7-next-steps)
8. [Decision Log](#8-decision-log)
9. [Risk Register](#9-risk-register)
10. [Codebase Impact](#10-codebase-impact)
11. [Success Metrics](#11-success-metrics)
12. [Phasing Plan](#12-phasing-plan)
13. [Appendix: Document Cross-Reference](#13-appendix-document-cross-reference)

---

## 1. Executive Summary

This initiative designs a streaming inference architecture for the IRON NPU model converter, replacing the current "load everything at once" pattern (~3.0GB resident for Llama-3.2-1B) with a chunked, streaming approach that can reduce peak memory to as low as ~254MB (single block) while maintaining or improving throughput.

The architecture is inspired by Apple's CoreML Llama-2-7B implementation on ANE, which uses chunked blocks with asynchronous KV cache updates. Three independent agents (Quality, Strategy, Program Management) reviewed the proposed routes and converged on a 5-phase implementation plan.

**Key outcome**: 5 architectural routes evaluated (A-E), with recommended phasing: Phase 0 (NPU driver spike) -> Phase 1 (Foundation) -> Phase 2 (Routes D+B parallel) -> Phase 3 (Route C) -> Phase 4 (Route E).

---

## 2. What Has Been Done

### 2.1 Documents Created

| # | Document | Path | Date | Purpose |
|---|----------|------|------|---------|
| 1 | Initial Exploration | `C:\Users\antmi\IRON\iron\model_convert\streaming_model_concept.md` | 2026-04-29 | Explored 3 concepts (Streaming Layers, Async KV Cache, Unified Streaming Block) with trade-off analysis |
| 2 | Design Mapping | `C:\Users\antmi\IRON\iron\model_convert\streaming_block_design.md` | 2026-04-29 | Mapped ONNX "Transient Session Pattern" to IRON NPU architecture, detailed block/KV/registry design |
| 3 | Architecture Routes | `C:\Users\antmi\IRON\iron\model_convert\streaming_architecture_routes.md` | 2026-04-29 | 5 routes with agent-reviewed consensus, phasing plan, risk register |
| 4 | **This Document** | `C:\Users\antmi\IRON\iron\model_convert\STREAMING_PROGRESS.md` | 2026-04-29 | Progress tracking, decision log, risk register, next steps |

### 2.2 Key Accomplishments

- [x] **Problem defined**: Current architecture loads all weights simultaneously (~3.0GB for 1B model), which does not scale to 7B+ models or multi-model scenarios
- [x] **3 concepts explored**: Streaming Layers (A), Async KV Cache (B), Unified Streaming Block (C)
- [x] **ONNX-to-IRON mapping completed**: Full concept mapping table from Apple's CoreML approach to IRON NPU equivalents
- [x] **Architecture detailed**: StreamingBlock, AsyncKVCache, BufferRegistry components designed with interfaces and lifecycles
- [x] **5 routes evaluated**: A (Pure Unified), B (Chunked), C (True Streaming), D (Hybrid Init), E (Adaptive)
- [x] **3-agent review completed**: Quality, Strategy, and Program Management agents independently reviewed and converged
- [x] **Phasing plan finalized**: 5-phase plan with success metrics and module hierarchy
- [x] **Risk register created**: Top risks identified with probability, impact, and mitigation strategies
- [x] **Terminology resolved**: Block = 1 transformer layer, Chunk = group of blocks (resolved design doc confusion)

### 2.3 Decisions Made

See [Decision Log](#8-decision-log) for complete details. Summary: 11 architectural decisions made, including corrected weight calculations, async KV pattern, file organization, compilation strategy, and entry point design.

---

## 3. What Was Analyzed

### 3.1 Three-Agent Review Process

Three independent agents reviewed `streaming_architecture_routes.md`:

| Agent | Role | Focus Area |
|-------|------|------------|
| Quality Agent | Code/Architecture Quality | Implementation correctness, code structure, technical soundness |
| Strategy Agent | Product/Technical Strategy | Route selection, competitive positioning, long-term viability |
| Program Management Agent | Project/Program Management | Phasing order, resource planning, risk mitigation, timeline |

### 3.2 Review Findings

**Quality Agent**:
- Confirmed technical soundness of all 5 routes
- Identified terminology confusion (Block vs Layer vs Chunk) -- resolved in routes doc
- Validated memory calculations (corrected per-block from ~116MB to ~121MB FP16)
- Confirmed ONNX-to-IRON concept mapping is complete and accurate

**Strategy Agent**:
- Validated Apple CoreML pattern as proven reference architecture
- Recommended Route E (Adaptive) as long-term goal, but agreed phased approach is correct
- Noted that Routes C and E require significant additional complexity -- justified by phasing
- Emphasized quantization impact (INT4 reduces 7B model from 14GB to 3.5GB)

**Program Management Agent**:
- Identified critical flaw in original phasing (D->B->C->E): ChunkManager infrastructure is prerequisite for ALL routes
- Recommended reordering to: Phase 0 spike -> Phase 1 foundation -> Phase 2 (D+B parallel) -> Phase 3 C -> Phase 4 E
- Flagged Phase 0 (NPU driver capability validation) as #1 program risk -- must de-risk before any implementation
- Estimated timeline: 20 weeks total across all phases

### 3.3 Convergence

All 3 agents independently agreed on:
- The 5-route framework is comprehensive
- Phase 1 (ChunkManager + AsyncKVCache + BufferRegistry) is foundational and must come first
- Phase 0 technical spike is the highest priority
- Route D and Route B should be developed in parallel (not sequentially)

The only disagreement was on the original phasing order (D->B->C->E), which all 3 agents rejected in favor of the corrected order.

### 3.4 Second-Round Quality Review Findings

A follow-up quality review identified **3 critical** and **5 medium** issues across the three documents:

**Critical Issues:**

| # | Issue | Location | Status |
|---|-------|----------|--------|
| C1 | KV cache DMA size "32MB per layer" is incorrect in timeline diagrams. Correct: 2.05MB per layer at S=1000, 8.39MB per layer at S=4096 | `streaming_block_design.md` Section 4.2 | **NEEDS FIX** |
| C2 | Conflicting KV cache patterns: Concept/Block Design docs describe double-buffer per-layer; Routes doc describes Apple's chunk-level async merge | All three documents | **NEEDS RESOLUTION** (see D3) |
| C3 | Per-block weight size discrepancy: Concept/Block Design docs say ~116MB; Routes doc says ~121.6MB (verified correct) | Concept doc, Block Design doc | **NEEDS FIX** in older docs |

**Medium Issues:**

| # | Issue | Status |
|---|-------|--------|
| M1 | "Layer" vs "Block" terminology not unified in Concept/Block Design docs | Acceptable -- Routes doc clarifies |
| M2 | Concept/Block Design docs don't mention chunking as design parameter | Acceptable -- Routes doc introduces it |
| M3 | Total model weight inconsistent (1.86GB vs 1.94GB across docs) | Resolved by D2 |
| M4 | Module hierarchy mismatch: Concept doc has `block.py`; Routes doc has `chunk_manager.py` | Resolved by Routes doc hierarchy |
| M5 | Peak memory calculations ambiguous about mmap RSS contribution | Routes doc clarifies per-route |

**Overall Quality Rating: 7/10** -- Excellent analysis, but older documents (concept, block design) need minor numerical updates to align with the corrected Routes doc values.

---

## 4. Current State

### 4.1 Phase Status

| Phase | Name | Status | Estimated Duration | Blockers |
|-------|------|--------|--------------------|----------|
| **Phase 0** | NPU Driver Spike | **PENDING** | 1 week | User answers to open questions |
| **Phase 1** | Foundation (AsyncKVCache + ChunkManager + BufferRegistry) | Not Started | 3 weeks | Phase 0 completion |
| **Phase 2** | Route D (Streaming Load) + Route B (Chunked Inference) -- Parallel | Not Started | 4 weeks | Phase 1 completion |
| **Phase 3** | Route C (True Runtime Streaming + Weight Cache) | Not Started | 8 weeks | Phase 2 completion, 7B+ model need confirmed |
| **Phase 4** | Route E (Adaptive Selector) | Not Started | 5 weeks | Phases 1-3 completion |

### 4.2 What Is Blocking Progress

1. **Phase 0 cannot start** until user answers the 6 open clarifying questions (see Section 5)
2. **AMD NPU driver capabilities unknown** -- the Phase 0 spike must validate whether `page_in`/`page_out` APIs exist. If they do not, Routes C and D collapse and the plan reverts to Route B as the primary strategy
3. **No implementation has begun** -- all work so far is design and analysis

### 4.3 Architecture Decision Summary

We have converged on a **foundational-first, parallel execution** approach:
- Build shared infrastructure first (Phase 1)
- Develop Routes D and B in parallel (Phase 2)
- Add Route C only if large model support is needed (Phase 3)
- Add adaptive selector as production polish (Phase 4)

---

## 5. Open Questions

The following 6 questions require user input before Phase 0 can begin. They are consolidated from all 3 source documents (deduplicated).

### Q1: Multi-Model Support Requirement

**Question**: Is running multiple models simultaneously a requirement for this initiative?

**Context**: The streaming architecture makes multi-model support natural (switch between models by swapping active weights). However, if this is not a use case, the added complexity of Routes C and E may not be justified. Route B supports multi-model only if all models' weights fit in RAM simultaneously.

**Impact**: Determines whether to prioritize Route C (true streaming) or stop at Route B (chunked).

**Where asked**: `streaming_model_concept.md` (Q5), `streaming_block_design.md` (Q8)

---

### Q2: Decode Latency Acceptability

**Question**: Is ~0.6 seconds per token (on NVMe) acceptable for Route C decode mode? On slower storage (~500MB/s SATA SSD), this increases to ~3.9 seconds per token.

**Context**: Route C reads the entire model from disk every token during decode. Weight caching mitigates this but requires additional RAM. If this latency is unacceptable, Route C may not be viable without aggressive caching or quantization.

**Impact**: Determines whether Route C is viable as a production strategy or remains a research prototype.

**Where asked**: `streaming_model_concept.md` (Q6), `streaming_block_design.md` (Q7)

---

### Q3: Weight Caching Strategy

**Question**: Should recently-used blocks/chunks be kept in RAM as a "hot cache" during decode? If so, what is the RAM budget for the cache?

**Context**: A 2-chunk weight cache (~730MB for Llama-3.2-1B) would reduce Route C decode disk I/O from 1.94GB to ~1.21GB per token (4 of 6 chunks cached). Larger caches further reduce I/O but increase RAM usage. This creates a continuum between Route C (streaming) and Route B (resident).

**Impact**: Determines weight cache design and RAM allocation strategy.

**Where asked**: `streaming_model_concept.md` (Q3)

---

### Q4: KV Cache Paging at Long Context

**Question**: At very long context lengths (S > 16K), should the KV Cache Manager evict old tokens to disk/swap? This would enable 128K context on 8GB RAM but introduces latency spikes on cache misses.

**Context**: KV cache at S=131K is ~4GB for a 1B model. Without paging, this requires 4GB+ RAM. With paging, old tokens can be swapped to disk, but cache misses during attention computation cause latency spikes.

**Impact**: Determines KV cache architecture complexity and maximum context length support.

**Where asked**: `streaming_model_concept.md` (Q4)

---

### Q5: Embedding / LM Head Streaming Strategy

**Question**: Should the embedding table (525MB) and LM head (525MB) stream on access (mmap, not resident) or stay mmap'd resident?

**Context**: These are the largest single components (525MB each). If mmap'd with lazy loading, they contribute ~0MB to peak RSS but add page fault latency on first access. If kept resident, they add 1.05GB to RSS but eliminate page faults.

**Impact**: Affects peak memory calculations and first-token latency.

**Where asked**: `streaming_block_design.md` (Q3), `streaming_model_concept.md` (Q1)

---

### Q6: Quantization Priority

**Question**: Should INT4/INT8 quantization support be included in the initial implementation phases, or deferred to a later effort?

**Context**: Quantization dramatically changes the memory picture (7B model: 14GB FP16 -> 7GB INT8 -> 3.5GB INT4). At INT4, Route B supports 7B models on 8GB RAM, and Route C's per-token disk I/O drops from 1.94GB to 0.48GB. However, quantization adds dequantization operator complexity.

**Impact**: Determines whether quantization is a Phase 1-2 consideration or a separate track.

**Where asked**: Indirectly in `streaming_architecture_routes.md` (Quantification Impact section)

---

## 6. Agent Consensus

### 6.1 Unanimous Agreement (All 3 Agents)

| Item | Consensus |
|------|-----------|
| **Phasing order** | Phase 0 -> Phase 1 -> Phase 2 (D+B parallel) -> Phase 3 -> Phase 4 |
| **Phase 1 priority** | ChunkManager + AsyncKVCache + BufferRegistry are shared prerequisites for ALL routes |
| **Phase 0 spike** | AMD NPU driver capability validation is the #1 program risk and must be done first |
| **Apple pattern validity** | Apple's CoreML chunked approach with async KV is proven and transferable to IRON |
| **Terminology** | Block = 1 transformer layer; Chunk = group of blocks; Operator = single GEMM/norm |
| **Compilation strategy** | AOT during model conversion, never JIT per forward pass |
| **Separate entry point** | New `streaming_infer.py`, not integrated into existing `interactive_convert.py` |
| **Feature flags** | Streaming mode defaults to `False` to prevent breaking existing functionality |

### 6.2 Disagreements and Resolutions

| Disagreement | Resolution |
|--------------|------------|
| **Original phasing** (D -> B -> C -> E) vs **Agent-recommended** (Foundation first) | All 3 agents rejected original. Chunking infrastructure is foundational. Adopted agent-recommended phasing. |
| **Chunk size** (fixed vs tunable) | Consensus: implement as tunable parameter, start with 3 (Apple's), benchmark 2/3/4/8 |
| **KV async pattern** (double-buffer vs Apple's merge pattern) | Consensus: Apple's exact pattern (chunk returns new KV, separate async merge) provides future-time buffer |
| **Block file organization** (individual .npy vs bundled) | Consensus: keep individual .npy + chunk manifest JSON. Bundle only for Route C to reduce seek overhead |

### 6.3 Outstanding Tensions

| Tension | Status |
|---------|--------|
| Route C viability depends on Phase 0 spike results | Pending |
| Route E complexity vs. "just works" user experience | Deferred to Phase 4 |
| Windows memory management differences from macOS | Requires empirical validation during Phase 1-2 |

---

## 7. Next Steps

### Immediate Actions (This Week)

1. **Answer 6 open questions** (Section 5) -- required to unblock Phase 0
2. **Scope Phase 0 spike** -- define specific AMD NPU driver capabilities to validate:
   - Does the driver expose `page_in`/`page_out` or equivalent unified memory management APIs?
   - What are the performance characteristics of unified memory access (bandwidth, latency)?
   - Are there limitations on concurrent unified memory mappings?
   - What is the minimum page size and alignment requirement?
3. **Assign Phase 0 ownership** -- who will conduct the spike?

### After Phase 0 Completion

4. **Review spike results** -- if page_in/page_out APIs exist, proceed with full plan. If not, collapse to Route B as primary strategy
5. **Begin Phase 1** -- implement AsyncKVCache, ChunkManager, BufferRegistry
6. **Set up benchmarking framework** -- needed for chunk size tuning in Phase 2

### Milestone Checklist

- [ ] User answers to Q1-Q6
- [ ] Phase 0 spike plan defined and assigned
- [ ] Phase 0 spike completed
- [ ] Spike results reviewed, route strategy confirmed
- [ ] Phase 1 foundation modules implemented
- [ ] Phase 1 success metrics validated (>80% compute/KV overlap)
- [ ] Phase 2 Route D implemented (streaming load)
- [ ] Phase 2 Route B implemented (chunked inference)
- [ ] Phase 2 success metrics validated (<200MB startup, >=1.1x throughput)
- [ ] Phase 3 Route C implemented (if needed)
- [ ] Phase 4 Route E implemented (adaptive selector)

---

## 8. Decision Log

All architectural decisions made during this initiative, with rationale and source.

| # | Date | Decision | Rationale | Source |
|---|------|----------|-----------|--------|
| D1 | 2026-04-29 | **Terminology**: Block = 1 transformer layer, Chunk = group of blocks | Resolved confusion between "layer" and "block" in design doc. Aligned with CoreML terminology. | `streaming_architecture_routes.md` |
| D2 | 2026-04-29 | **Block weight size**: 121MB per block (FP16), not 116MB | Corrected calculation: Q(8.39) + K(2.10) + V(2.10) + O(8.39) + Gate(33.55) + Up(33.55) + Down(33.55) + RMSNorm(0.01*2) = ~121.6MB | `streaming_architecture_routes.md` |
| D3 | 2026-04-29 | **Async KV pattern**: Apple's merge pattern (not double-buffer) | Apple's pattern provides future-time buffer (1 chunk worth of time) for async KV merge. Double-buffer only helps if DMA < compute time. | `streaming_architecture_routes.md` Q2 |
| D4 | 2026-04-29 | **File organization**: Individual .npy + chunk manifest JSON | IRON already has 9 .npy files per block. No splitting needed. Bundle only for Route C to reduce seek overhead. | `streaming_architecture_routes.md` Q3 |
| D5 | 2026-04-29 | **Tensor reshaping**: Target AIE tile sizes (64x64), not Apple's 8x8 | Apple's 20% speedup from (B,C,8,8) is ANE-specific. IRON's AIE uses systolic arrays with 64x64 tiles. | `streaming_architecture_routes.md` Q4 |
| D6 | 2026-04-29 | **Residual pattern**: Non-parallel (Llama style) | Llama-3.2 uses non-parallel residual. Add parallel as special case only if a model requires it. | `streaming_architecture_routes.md` Q5 |
| D7 | 2026-04-29 | **Max sequence length**: Dynamic with configurable cap, fixed at build-time | Provides flexibility without runtime overhead. Cap is configurable, not hardcoded. | `streaming_architecture_routes.md` Q6 |
| D8 | 2026-04-29 | **Chunk size**: Tunable parameter, start with 3, benchmark 2/3/4/8 | Apple uses 3 for ANE. IRON's AIE may prefer different size based on column count (8) and tile size (64). | `streaming_architecture_routes.md` Q1 |
| D9 | 2026-04-29 | **Compilation**: AOT during model conversion, never JIT per forward pass | JIT per chunk per forward pass (Route C decode) would be catastrophic. AOT artifacts stored alongside weight files. | `streaming_architecture_routes.md` |
| D10 | 2026-04-29 | **Entry point**: New `streaming_infer.py`, separate from `interactive_convert.py` | `interactive_convert.py` remains offline conversion tool. Streaming inference needs separate runtime entry point. | `streaming_block_design.md` Q8 |
| D11 | 2026-04-29 | **Phasing order**: Phase 0 -> Phase 1 -> Phase 2 (D+B parallel) -> Phase 3 -> Phase 4 | All 3 agents agreed original D->B->C->E was flawed. ChunkManager is foundational for all routes. | `streaming_architecture_routes.md` |

---

## 9. Risk Register

| ID | Risk | Probability | Impact | Status | Mitigation | Owner |
|----|------|-------------|--------|--------|------------|-------|
| R1 | AMD NPU driver lacks `page_in`/`page_out` APIs | Medium | **Critical** | **OPEN** | Phase 0 spike. Fallback: mmap/munmap. Secondary fallback: Route B with all weights resident. | Phase 0 |
| R2 | Route C disk I/O dominates decode on slow storage | High | **High** | **OPEN** | Weight cache with LRU eviction. Bundle chunk files. Quantization support. I/O prefetching. Gate on storage speed. | Phase 3 |
| R3 | Integration breaks existing functionality | High | Medium | **MITIGATED** | Feature flags (`streaming_mode=False` default). Separate module hierarchy (`streaming/`). `StreamingModelAssembler` alongside existing `ModelAssembler`. | All phases |
| R4 | Chunk size (3 blocks) suboptimal for AIE architecture | Medium | Medium | **OPEN** | Implement as tunable parameter. Benchmark 2/3/4/8 during Phase 2. | Phase 2 |
| R5 | Windows memory management differs from macOS (Route D `keep_resident` may need explicit locking) | Medium | **High** | **OPEN** | Empirical validation during Phase 1-2. Use `madvise`/Windows equivalent for page locking if needed. | Phase 1-2 |
| R6 | DMA driver maturity on Windows/AMD (async KV timing less precise) | Medium | Medium | **OPEN** | Design async KV with tolerance for timing variance. Add fallback to sync mode. | Phase 1 |
| R7 | User acceptance of Route C decode latency (0.6s/token on NVMe) | High | **High** | **OPEN** | **Requires user input (Q2)**. If unacceptable, defer Route C or require weight cache. | Phase 0 |
| R8 | KV cache at long context (S > 16K) exceeds available RAM | Medium | Medium | **OPEN** | **Requires user input (Q4)**. If long context needed, implement KV paging with eviction policy. | Phase 3 |

### Risk Trend Summary

- **Critical risks**: 1 (R1 - driver APIs) -- can be resolved in 1-week Phase 0 spike
- **High risks**: 3 (R2, R5, R7) -- 2 require user input, 1 mitigated by design
- **Medium risks**: 4 (R3 mitigated, R4/R6/R8 need empirical validation)

---

## 10. Codebase Impact

### 10.1 Existing Files (Today)

**Core converter module** (`C:\Users\antmi\IRON\iron\model_convert\`):

| File | Purpose | Streaming Impact |
|------|---------|-----------------|
| `__init__.py` | Package init | Will add streaming submodule exports |
| `__main__.py` | CLI entry point | Unchanged |
| `cli.py` | CLI commands | May add streaming subcommand |
| `converter.py` | Main converter | Unchanged |
| `model_assembler.py` | Model assembly | Reference for `StreamingModelAssembler` |
| `layer_builder.py` | Layer building | Reference for block construction |
| `weight_mapper.py` | Weight mapping | May need streaming-aware weight loading |
| `shape_manager.py` | Shape management | Reference for buffer contracts |
| `config_adapter.py` | Configuration | May need streaming config section |
| `interactive_convert.py` | Interactive conversion | Unchanged (remains offline tool) |
| `operator_factory.py` | Operator factory | Reference for block operator graphs |
| `setup.py` | Package setup | Unchanged |

**Archive** (`C:\Users\antmi\IRON\iron\model_convert\archive\`):
- Historical/reference files. No direct streaming impact.

**Streaming documents** (created during this initiative):
- `streaming_model_concept.md`
- `streaming_block_design.md`
- `streaming_architecture_routes.md`
- `STREAMING_PROGRESS.md` (this file)

### 10.2 Files to Create

**Phase 1 -- Foundation** (3 weeks):

| File | Purpose | Dependencies |
|------|---------|-------------|
| `streaming/__init__.py` | Package init; exports AsyncKVCache, ChunkManager, BufferRegistry | -- |
| `streaming/async_kv_cache.py` | AsyncKVCache class: pre-allocates K/V, provides get/append/prefetch, async KV merge between chunks | numpy |
| `streaming/chunk_manager.py` | ChunkManager class: organizes blocks into chunks, manages chunk activation/deactivation, reads chunk manifest | json, pathlib |
| `streaming/buffer_registry.py` | BufferRegistry class: manages hidden_states, attention_mask, rope_angles, position_ids with typed contracts | numpy |

**Phase 2 -- Routes D + B** (4 weeks, parallel):

| File | Purpose | Route | Dependencies |
|------|---------|-------|-------------|
| `streaming/streaming_load.py` | Streaming block load at startup with keep_resident; low-peak-memory initialization | D | ChunkManager, weight_mapper.py |
| `streaming/chunked_inference.py` | Chunked inference loop: activate chunk, run blocks, async KV merge between chunks | B | ChunkManager, AsyncKVCache, BufferRegistry |
| `streaming/streaming_infer.py` | New runtime entry point for streaming inference | D+B | All Phase 1-2 modules |

**Phase 3 -- Route C** (8 weeks):

| File | Purpose | Dependencies |
|------|---------|-------------|
| `streaming/runtime_streaming.py` | Per-forward-pass page_in/page_out, runtime streaming inference loop | ChunkManager, AsyncKVCache |
| `streaming/weight_cache.py` | LRU weight cache: keeps recently-used chunks in RAM, manages eviction | pathlib, collections |

**Phase 4 -- Route E** (5 weeks):

| File | Purpose | Dependencies |
|------|---------|-------------|
| `streaming/adaptive_selector.py` | Hardware detection + strategy selection; automatically picks best route based on model size and available RAM | psutil, all route modules |

**Supporting files** (as needed):

| File | Purpose |
|------|---------|
| `streaming/manifest.py` | StreamingManifest class: reads/writes chunk manifest JSON (weight paths, shapes, tiling config) |
| `streaming/test_streaming.py` | Unit tests for all streaming components |
| `streaming/benchmarks/` | Benchmark scripts for chunk size tuning, async KV overlap measurement |

### 10.3 Files That May Need Modification

| File | Modification | Reason |
|------|-------------|--------|
| `model_assembler.py` | Add `StreamingModelAssembler` class alongside existing `ModelAssembler` | Alternative assembly path for streaming mode |
| `config_adapter.py` | Add streaming configuration section (chunk_size, streaming_mode, weight_cache_size) | Configuration for streaming features |
| `cli.py` | Add streaming subcommand (`iron model-convert --streaming`) | CLI access to streaming inference |
| `__init__.py` | Add streaming submodule exports | Public API for streaming components |

---

## 11. Success Metrics

| Metric | Target | Phase | Measurement Method |
|--------|--------|-------|-------------------|
| Async KV cache overlap efficiency | >80% compute/KV overlap | Phase 1 | Profiling DMA vs compute timeline |
| Route D startup peak memory | <200MB for 1B model | Phase 2 | RSS measurement during load |
| Route B throughput vs baseline | >=1.1x tokens/sec | Phase 2 | Benchmark: tokens/sec comparison |
| NPU compilation overhead (per chunk) | <500ms | Phase 2 | Timing chunk compilation |
| Route C peak runtime memory | <500MB for 7B model | Phase 3 | RSS measurement during decode |
| Route C decode latency on NVMe | <50ms/token for 7B | Phase 3 | Per-token timing |
| Weight cache hit rate (decode) | >70% after first token | Phase 3 | Cache statistics tracking |
| Route E strategy selection accuracy | Correct route in >95% of configs | Phase 4 | Test matrix coverage |

---

## 12. Phasing Plan

```
Phase 0: Technical Spike (Week 1)
         Validate AMD NPU driver capabilities for unified memory page management.
         This is the #1 program risk -- if page_in/page_out APIs don't exist,
         Routes C and D collapse. 1-week spike de-risks the entire plan.

Phase 1: Foundation (Weeks 2-4)
         Build AsyncKVCache + ChunkManager + BufferRegistry.
         This is the shared prerequisite for ALL routes.
         Chunk size is configurable (1, 2, 3, 4, 8 blocks/chunk) for benchmarking.

Phase 2: Route D + Route B -- Parallel (Weeks 4-8)
         Route D: Streaming block load at startup, keep resident. (1-2 weeks)
         Route B: Chunked inference with async KV between chunks. (3-4 weeks)
         These share the ChunkManager from Phase 1. Route D adds streaming load;
         Route B adds chunked execution. They can be developed in parallel.

Phase 3: Route C -- True Runtime Streaming (Weeks 8-16)
         Add page_in/page_out per forward pass, weight cache with LRU eviction.
         Depends on Phase 1 (ChunkManager + AsyncKVCache) and Phase 2's
         page management primitives from Route D.
         Only begin after Route B is stable and 7B+ model support is needed.

Phase 4: Route E -- Adaptive Selector (Weeks 15-20)
         Hardware detection + strategy selection layer.
         Requires Phases 1-3 to exist. Can overlap with late Phase 3.
```

### Why This Order

The original plan (D -> B -> C -> E) had a critical flaw: the ChunkManager infrastructure is foundational and reused by Routes B, C, and E. Building Route D first would require writing an inference loop without chunking, then rewriting it in Phase 2 -- wasted effort. All 3 agents independently identified this and converged on the corrected order.

---

## 13. Appendix: Document Cross-Reference

### Source Documents

| Document | Path | Role |
|----------|------|------|
| Initial Concept Exploration | `C:\Users\antmi\IRON\iron\model_convert\streaming_model_concept.md` | Problem definition, 3 concepts (A/B/C), 7 initial questions |
| Detailed Design Mapping | `C:\Users\antmi\IRON\iron\model_convert\streaming_block_design.md` | ONNX-to-IRON mapping, component design, 3-phase implementation plan, 8 design questions |
| Architecture Routes + Consensus | `C:\Users\antmi\IRON\iron\model_convert\streaming_architecture_routes.md` | 5 routes, agent review, phasing plan, risk register, 6 route questions |
| **Progress Document** (this) | `C:\Users\antmi\IRON\iron\model_convert\STREAMING_PROGRESS.md` | Living progress tracker, decision log, risk register, next steps |

### Key Concepts by Document

| Concept | Primary Source | Secondary Source |
|---------|---------------|-----------------|
| Streaming Layers (Concept A) | `streaming_model_concept.md` | `streaming_architecture_routes.md` (Route C) |
| Async KV Cache (Concept B) | `streaming_model_concept.md` | `streaming_block_design.md` (Section 4) |
| Unified Streaming Block (Concept C) | `streaming_model_concept.md` | `streaming_block_design.md` (Section 3) |
| ONNX-to-IRON Mapping | `streaming_block_design.md` (Section 2) | `streaming_architecture_routes.md` (terminology) |
| 5 Routes (A-E) | `streaming_architecture_routes.md` (Section "Routes") | `streaming_model_concept.md` (trade-off table) |
| Apple CoreML Pattern | `streaming_architecture_routes.md` (Section "Apple's Proven Approach") | `streaming_block_design.md` (ONNX POC reference) |
| Phasing Plan | `streaming_architecture_routes.md` (Section "Recommended Phasing") | -- |
| Risk Register | `streaming_architecture_routes.md` (Section "Top 3 Program Risks") | Expanded in this document |

### Question Tracking

| Q# | Topic | First Asked In | Status |
|----|-------|---------------|--------|
| Q1 | Multi-model support | `streaming_model_concept.md` (Q5) | **OPEN** |
| Q2 | Decode latency acceptability | `streaming_model_concept.md` (Q6) | **OPEN** |
| Q3 | Weight caching strategy | `streaming_model_concept.md` (Q3) | **OPEN** |
| Q4 | KV cache paging at long context | `streaming_model_concept.md` (Q4) | **OPEN** |
| Q5 | Embedding/LM Head streaming | `streaming_block_design.md` (Q3) | **OPEN** |
| Q6 | Quantization priority | `streaming_architecture_routes.md` (Quantification Impact) | **OPEN** |
| ~~Q7~~ | Chunk size | `streaming_architecture_routes.md` (Q1) | **RESOLVED** (D8: tunable, start with 3) |
| ~~Q8~~ | KV async pattern | `streaming_architecture_routes.md` (Q2) | **RESOLVED** (D3: Apple's merge pattern) |
| ~~Q9~~ | Block file organization | `streaming_architecture_routes.md` (Q3) | **RESOLVED** (D4: individual .npy + manifest) |
| ~~Q10~~ | Tensor reshaping | `streaming_architecture_routes.md` (Q4) | **RESOLVED** (D5: target AIE 64x64) |
| ~~Q11~~ | Residual pattern | `streaming_architecture_routes.md` (Q5) | **RESOLVED** (D6: non-parallel) |
| ~~Q12~~ | Max sequence length | `streaming_architecture_routes.md` (Q6) | **RESOLVED** (D7: dynamic with cap) |
| ~~Q13~~ | AIE compilation | `streaming_block_design.md` (Q1) | **RESOLVED** (D9: AOT) |
| ~~Q14~~ | Weight file format | `streaming_block_design.md` (Q2) | **RESOLVED** (D4: keep individual .npy) |
| ~~Q15~~ | Layer grouping | `streaming_block_design.md` (Q4) | **RESOLVED** (D8: tunable chunk size) |
| ~~Q16~~ | KV double buffering | `streaming_block_design.md` (Q5) | **RESOLVED** (D3: Apple's merge pattern) |
| ~~Q17~~ | Integration point | `streaming_block_design.md` (Q8) | **RESOLVED** (D10: separate entry point) |
| ~~Q18~~ | Mmap weights | `streaming_model_concept.md` (Q1) | **RESOLVED** (D5: mmap with lazy loading) |
| ~~Q19~~ | Decode vs Prefill strategy | `streaming_model_concept.md` (Q2) | **RESOLVED** (context-dependent per Route) |

---

## 14. Senior Developer Assessment (Enhanced-Senior-Developer Agent)

### Overall Ratings

| Dimension | Rating | Key Finding |
|-----------|--------|-------------|
| Implementation Feasibility | 7/10 | Phase 1 buildable but async KV depends on unresolved GIL question |
| Code Structure | 6/10 | Missing config, protocols, and shared inference loop abstractions |
| Technical Risk Coverage | 4/10 | 7 unaddressed risks including one that invalidates core async premise |
| Refactoring Scope | 7/10 | Manageable -- 2 files need significant changes, rest are minor additions |
| Developer Readiness | 6/10 | Good prioritization order, but needs simulated async approach for hardware-free testing |
| Test Strategy | 8/10 | Clear path for CPU-only testing with mocking |

### Critical Unaddressed Risks

| Risk | Severity | Detail |
|------|----------|--------|
| Python GIL invalidates async KV | **CRITICAL** | If NPU compute holds the GIL, KV "async" thread cannot run numpy ops simultaneously. Requires C-level GIL release (`Py_BEGIN_ALLOW_THREADS`), multiprocessing with shared memory, or ctypes/cffi. |
| NumPy memory alignment for DMA | **HIGH** | `np.zeros()` aligns to 8-16 bytes, not 4096. Needs `ctypes.VirtualAlloc` (Windows) or `np.memmap` with page-aligned offsets. |
| AIE compilation artifact format undefined | **HIGH** | Design mentions "pre-compiled artifacts" (~50MB) but never defines format. Route C's page_in/page_out impossible if artifacts encode specific weight addresses. |
| Thread safety of double-buffer KV | **HIGH** | NumPy arrays not thread-safe for concurrent reads/writes. Pointer swap race conditions cause silent data corruption. |

### Recommended Module Hierarchy Changes

**Consolidate:**
- `manifest.py` into `chunk_manager.py` (or make private `_manifest.py`)

**Split:**
- `async_kv_cache.py` into `kv_cache.py` (pure data structure) + `kv_async_ops.py` (async DMA engine)

**Add (missing from plan):**
- `streaming/config.py` -- Single `StreamingConfig` dataclass
- `streaming/protocols.py` -- Abstract `InferenceStrategy` base class with `prefill()`/`decode()` contracts
- `streaming/inference_loop.py` -- Shared forward-pass orchestration
- `tests/` subdirectory instead of single `test_streaming.py`

### Files Needing Refactoring

| File | Effort | Change |
|------|--------|--------|
| `model_assembler.py` | **Critical (40%)** | Add `StreamingModelAssembler` with lazy operator instantiation |
| `layer_builder.py` | **Moderate (25%)** | Add "lazy build" mode; extract KV management to AsyncKVCache |
| `shape_manager.py` | Minor (10%) | Add per-block/chunk memory calculation mode |
| `config_adapter.py` | Minor (5%) | Add `StreamingConfig` dataclass section |
| `operator_factory.py` | Minor (5%) | Add chunk-scoped operator caching |
| `interactive_convert.py` | Minor (10%) | Produce chunk manifest JSON during export |
| `weight_mapper.py` | **No changes** | Existing .npy format is ideal for streaming |

### Recommended Implementation Order

1. `streaming/config.py` -- Define configuration contract first
2. `streaming/buffer_registry.py` -- Easiest, zero external deps, immediately testable
3. `streaming/kv_cache.py` -- Pure data structure (no async)
4. Simulated async via `ThreadPoolExecutor` with mock NPU compute (sleep-based)

---

## 15. Testing Strategy Summary (Testing-Quality-Specialist Agent)

Full testing strategy document: `C:\Users\antmi\IRON\iron\model_convert\streaming_test_strategy.md`

### Test Coverage Overview

| Category | Test Count | Scope |
|----------|-----------|-------|
| Unit Tests | 125 | AsyncKVCache (30), BufferRegistry (25), ChunkManager (26), Phase 2-4 (44) |
| Integration Tests | 17 | Full inference loop, KV overlap measurement, cross-component |
| Performance Tests | 12 | Chunk size tuning, baseline comparison, overlap benchmarks |
| Regression Tests | 26 | Feature flags, output parity, cross-platform, migration |
| Acceptance Criteria | 31 | Per-phase numeric targets |

### Mocking Strategy

- `FakeNPUComputeEngine` -- numpy matmul with configurable delays, no NPU hardware needed
- DMA simulated with `time.sleep()` proportional to data size
- `MockOperatorFactory` -- identity functions or simple CPU matrix multiplications

### Key Test Fixtures (16 total)

`streaming_config`, `chunk_manifest_3block`, `chunk_manifest_4block`, `block_weights`, `fake_npu_engine`, `buffer_registry_config`, `kv_cache_config`, `attention_mask`, `rope_angles`, `hidden_states_buffer`, etc.

### CI/CD Pipeline

4 GitHub Actions jobs: unit tests (3 Python versions x 2 OS), integration tests, regression tests, weekly benchmarks.

Markers: `@pytest.mark.slow`, `@pytest.mark.requires_npu`, `@pytest.mark.benchmark`, `@pytest.mark.windows`, `@pytest.mark.integration`, `@pytest.mark.regression`

### Acceptance Criteria Highlights

| Phase | Key Criteria |
|-------|-------------|
| Phase 1 | >80% KV overlap, >90% test coverage, 55+ unit tests passing |
| Phase 2 | <200MB startup peak, >=1.1x throughput, <500ms chunk compile |
| Phase 3 | <500MB for 7B model, <50ms/token on NVMe, >70% cache hit rate |
| Phase 4 | >95% strategy selection accuracy across test matrix |

---

*This is a living document. Update it as work progresses, decisions are made, and questions are answered. Each update should include the date and a summary of changes.*
