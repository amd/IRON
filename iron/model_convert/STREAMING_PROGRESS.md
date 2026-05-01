# IRON NPU - Streaming Architecture Initiative: Progress Document

> **Project**: Streaming Inference Architecture for AMD Ryzen AI NPU
> **Target Model**: Llama-3.2-1B (baseline), scalable to 7B+ models
> **Branch**: `feature/model-converter-analysis`
> **Last Updated**: 2026-04-30
> **Status**: Phase 0 Pending (Architecture Design Complete, Route B confirmed as primary, all quality review issues CV1-CV11 resolved, awaiting unified memory validation spike)
> **Owner**: Dr. Sarah Kim, Technical Product Strategist & Engineering Lead

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [What Has Been Done](#2-what-has-been-done)
3. [What Was Analyzed](#3-what-was-analyzed)
   - [3.5 User Answers Impact Analysis](#35-user-answers-impact-analysis)
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
14. [Senior Developer Assessment (Initial)](#14-senior-developer-assessment-enhanced-senior-developer-agent)
15. [Testing Strategy Summary](#15-testing-strategy-summary-testing-quality-specialist-agent)
16. [Program Management Update](#16-program-management-update---user-decisions-impact)
17. [Quality Review - Post-User Decisions](#17-quality-review---post-user-decisions)
18. [Senior Developer Assessment - Route B Implementation](#18-senior-developer-assessment---route-b-implementation)
19. [Coherence Verification](#19-coherence-verification)
20. [Testing Strategy Update - Route B](#20-testing-strategy-update---route-b)
21. [Planning Analysis - Pipeline Round 2](#21-planning-analysis---pipeline-round-2)
22. [Program Management Review - Pipeline Round 2](#22-program-management-review---pipeline-round-2)
23. [Quality Review - Pipeline Round 2 Coherence Check](#23-quality-review---pipeline-round-2-coherence-check)

---

## 1. Executive Summary

This initiative designs a streaming inference architecture for the IRON NPU model converter, replacing the current "load everything at once" pattern (~3.0GB resident for Llama-3.2-1B) with a chunked, streaming approach that can reduce peak memory to as low as ~254MB (single block) while maintaining or improving throughput.

The architecture is inspired by Apple's CoreML Llama-2-7B implementation on ANE, which uses chunked blocks with asynchronous KV cache updates. Three independent agents (Quality, Strategy, Program Management) reviewed the proposed routes and converged on a 5-phase implementation plan.

**Key outcome**: User has answered all 6 clarifying questions, definitively selecting **Route B (Chunked Inference with Unified Memory)** as the primary architecture. Route C (disk streaming) is deprioritized. Route D is merged into Route B. Route E is simplified to configuration selection. Multi-model support is a Phase 2 requirement. Total estimated timeline: ~17 weeks.

**5 architectural routes evaluated**, with updated phasing: Phase 0 (unified memory validation) -> Phase 1 (Foundation + KV Paging) -> Phase 2 (Route B + Multi-Model) -> Phase 3 (Multi-Model Weight Manager) -> Phase 4 (Auto-Configuration).

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
- [x] **User questions answered**: All 6 clarifying questions answered, Route B confirmed as primary
- [x] **Route re-evaluation completed**: Route B primary, Route C deprioritized, Route D merged, Route E simplified
- [x] **Impact analysis documented**: Section 3.5 with full route re-evaluation, memory analysis, and risk assessment

### 2.3 Decisions Made

See [Decision Log](#8-decision-log) for complete details. Summary: 17 architectural decisions made, including 6 user-driven decisions (D12-D17) that confirm Route B as primary, deprioritize Route C, require multi-model support, confirm resident embedding/LM head, enable KV paging, and make quantization optional.

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
| C1 | KV cache DMA size "32MB per layer" is incorrect in timeline diagrams. Correct: 2.05MB per layer at S=1000, 8.39MB per layer at S=4096 | `streaming_block_design.md` Section 4.2 | **DOCUMENT NOTE**: Legacy doc (pre-decision). Add deprecation banner. Not critical for Route B implementation. |
| C2 | Conflicting KV cache patterns: Concept/Block Design docs describe double-buffer per-layer; Routes doc describes Apple's chunk-level async merge | All three documents | **RESOLVED by D3**: Apple's merge pattern adopted. Legacy docs retain old pattern but are deprecated. |
| C3 | Per-block weight size discrepancy: Concept/Block Design docs say ~116MB; Routes doc says ~121.6MB (verified correct) | Concept doc, Block Design doc | **DOCUMENT NOTE**: Legacy docs (pre-decision). Routes doc and STREAMING_PROGRESS.md use correct value. Add deprecation banners. |

**Medium Issues:**

| # | Issue | Status |
|---|-------|--------|
| M1 | "Layer" vs "Block" terminology not unified in Concept/Block Design docs | **RESOLVED by D1**: Routes doc clarifies. Legacy docs deprecated. |
| M2 | Concept/Block Design docs don't mention chunking as design parameter | Acceptable -- Routes doc introduces it. Legacy docs deprecated. |
| M3 | Total model weight inconsistent (1.86GB vs 1.94GB across docs) | **RESOLVED by D2**: 1.94GB verified correct. Legacy docs deprecated. |
| M4 | Module hierarchy mismatch: Concept doc has `block.py`; Routes doc has `chunk_manager.py` | **RESOLVED by Routes doc hierarchy**: Legacy doc deprecated. |
| M5 | Peak memory calculations ambiguous about mmap RSS contribution | **RESOLVED**: Section 3.5.4 clarifies with resident weights (Q5). |

**Overall Quality Rating: 7/10** -- Excellent analysis, but older documents (concept, block design) need deprecation banners to prevent confusion with the current Route B architecture.

---

## 3.5 User Answers Impact Analysis

> **Date**: 2026-04-30
> **Analyst**: Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
> **Trigger**: User provided definitive answers to all 6 clarifying questions (Q1-Q6)

### 3.5.1 User Decisions Summary

| Question | Decision | Implication |
|----------|----------|-------------|
| Q1: Multi-model support | **REQUIRED** | Architecture must support running multiple models. Eliminates Route A and Route D as standalone strategies. |
| Q2: Memory model preference | **Unified memory** -- NPU accesses system RAM directly, no per-token disk reads | Eliminates Route C's core premise (disk streaming per forward pass). Confirms unified memory as foundation. |
| Q3: Weight residency | **Resident in RAM** -- OS page cache handles hot pages | No explicit weight streaming at runtime. Weights are mmap'd and resident. Route B philosophy confirmed. |
| Q4: KV cache paging | **Yes, reasonable** for S > 16K | AsyncKVCache must support paging/eviction for long context sequences. |
| Q5: Embedding + LM Head | **RESIDENT** -- keep in RAM (1.05GB combined) | Baseline RSS increases. No streaming for these components. |
| Q6: Quantization | **OPTIONAL** -- support but don't require | Design with quantization in mind, but don't block any phase on it. |

### 3.5.2 Route Re-Evaluation Matrix

| Route | Before User Answers | After User Answers | Rationale |
|-------|-------------------|-------------------|-----------|
| **A: Pure Unified** | Viable baseline | **INSUFFICIENT** alone | Cannot support multi-model requirement (Q1). Its primitives (unified memory + async KV) remain foundational. |
| **B: Chunked** | Strong candidate (parallel with D) | **PRIMARY ROUTE** | Perfectly aligns with all user decisions: unified memory (Q2), resident weights (Q3), multi-model via chunk switching (Q1), KV paging (Q4). |
| **C: True Streaming** | Contingent on Phase 0 spike | **DEPRIORITIZED / ELIMINATED** | User explicitly rejected per-token disk streaming (Q2). page_in/page_out APIs no longer required. |
| **D: Hybrid Init** | Parallel with B in Phase 2 | **MERGED into Route B** | Streaming load at startup becomes an implementation detail of Route B initialization, not a separate strategy. |
| **E: Adaptive** | Long-term goal (Phase 4) | **SIMPLIFIED but RETAINED** | Instead of choosing between streaming/resident strategies, it now selects chunk sizes, KV configs, and paging thresholds based on hardware. |

### 3.5.3 Primary Route: Route B (Chunked Inference with Unified Memory)

**Why Route B wins:**

1. **Unified memory alignment**: User explicitly wants NPU to access system RAM directly (Q2). Route B's "all weights mapped, unified memory" model matches exactly.
2. **Multi-model support**: Route B supports multi-model by activating/deactivating chunks between models. While it requires combined weights to fit in RAM, this is acceptable given the user's resident-weight preference (Q3).
3. **No disk I/O at runtime**: Route B has zero disk reads during inference (weights already mapped). This eliminates the Route C decode latency problem entirely.
4. **Async KV optimization**: Route B's chunk-level async KV merge (Apple's proven pattern) provides measurable performance gains without architectural complexity.
5. **Proven pattern**: Apple's CoreML Llama-2-7B implementation uses this exact approach on ANE.

### 3.5.4 Memory Impact Analysis (Llama-3.2-1B, Route B, User's Decisions)

| Component | Size | Resident? | Notes |
|-----------|------|-----------|-------|
| Embedding | 525MB | Yes (Q5) | Resident as requested |
| Layer weights (16 blocks) | 1.94GB | Yes (mapped) | Unified memory, all resident |
| LM Head | 525MB | Yes (Q5) | Resident as requested |
| KV Cache (S=4096) | 128MB | Yes | Grows with sequence length |
| KV Cache (S=16384) | 512MB | Yes | Threshold before paging kicks in (Q4) |
| KV Cache (S=131072) | 4.0GB | Paged | Paging active above 16K |
| Activations | ~50MB | Yes | Temporary, per-forward-pass |
| **Total (S=4096)** | **~3.14GB** | | Baseline for single model |
| **Total (2 models, S=4096)** | **~6.28GB** | | Multi-model on 16GB system |
| **Total (3 models, S=4096)** | **~9.42GB** | | Multi-model on 16GB system (tight) |

**Key insight**: Route B does not reduce peak RSS compared to the current architecture (~3.0GB). Its value is in: (a) enabling async KV optimization, (b) supporting multi-model via chunk activation, and (c) providing tunable chunk sizes for different hardware configurations.

### 3.5.5 Multi-Model Architecture Implications

With multi-model REQUIRED (Q1), the ChunkManager must support:

1. **Multiple model manifests**: Load and track metadata for N models simultaneously.
2. **Chunk activation switching**: Deactivate Model A's chunks, activate Model B's chunks (weight pointers remain mapped, but NPU reconfigures for active model).
3. **Shared KV cache pools**: Partition KV cache memory across active models.
4. **Shared BufferRegistry**: Reuse activation buffers between models (sequential execution, not parallel).

Since all weights stay resident (Q3), multi-model switching is primarily about NPU reconfiguration and KV cache management, not weight loading/unloading. This simplifies the design significantly.

### 3.5.6 What Changes

| Area | Before | After |
|------|--------|-------|
| Primary route | D+B parallel in Phase 2 | Route B is PRIMARY, D is an optimization within B |
| Route C status | Planned for Phase 3 | Deprioritized -- disk streaming eliminated |
| Phase 0 scope | Validate page_in/page_out APIs | Validate unified memory bandwidth + concurrent mmap limits |
| KV cache design | Fixed allocation | Must support paging for S > 16K |
| Route E scope | Strategy selection (A/B/C/D) | Configuration selection (chunk size, KV size, paging thresholds) |
| Multi-model | Nice-to-have | Phase 2 requirement |
| #1 program risk | R1: missing page_in/page_out APIs | Eliminated -- unified memory is standard |

### 3.5.7 What Is Deprioritized

| Item | Reason |
|------|--------|
| Route C (True Runtime Streaming) | User rejected per-token disk I/O (Q2). The entire premise is invalidated. |
| Route D as separate strategy | Merged into Route B as a startup optimization. Not a distinct inference strategy. |
| Quantization as blocker | Explicitly optional (Q6). Can be added later without architectural changes. |
| Weight cache LRU (Route C artifact) | No longer needed -- weights are resident. |
| Complex adaptive strategy selection (Route E original) | Simplified to configuration selection since there's only one strategy (Route B). |

### 3.5.8 Updated Risk Assessment

| Risk ID | Before | After | Change |
|---------|--------|-------|--------|
| R1: Missing page_in/page_out | Critical impact | **ELIMINATED** | Not needed for Route B |
| R2: Route C disk I/O dominates | High impact | **ELIMINATED** | Route C deprioritized |
| R7: User acceptance of Route C latency | High impact | **RESOLVED** | User chose unified memory |
| R5: Windows memory management | Medium | **ELEVATED** | Now the key risk for Route B's mmap behavior |
| NEW: Multi-model RAM pressure | N/A | **NEW** | 2-3 models on 16GB system may cause OS paging pressure |
| NEW: KV cache paging latency | N/A | **NEW** | Paging old tokens during attention may cause latency spikes |

---

## 4. Current State

### 4.1 Phase Status

| Phase | Name | Status | Estimated Duration | Blockers |
|-------|------|--------|--------------------|----------|
| **Phase 0** | Unified Memory Validation | **PENDING** | 1 week | Scope updated (see Section 3.5) |
| **Phase 1** | Foundation (AsyncKVCache + ChunkManager + BufferRegistry + KV Paging) | Not Started | 4 weeks | Phase 0 completion |
| **Phase 2** | Route B (Chunked Inference) + Multi-Model Support | Not Started | 5 weeks | Phase 1 completion |
| **Phase 3** | Multi-Model Weight Manager (rescoped from Route C) | Not Started | 4 weeks | Phase 2 completion |
| **Phase 4** | Auto-Configuration (rescoped from Route E) | Not Started | 3 weeks | Phases 1-3 completion |

### 4.2 What Is Blocking Progress

1. **All 6 clarifying questions have been answered** (Section 5) -- Phase 0 scope has been updated and is ready to begin
2. **Phase 0 scope changed**: No longer requires validating page_in/page_out APIs. Instead validates unified memory bandwidth, concurrent mmap limits, and OS page cache behavior on Windows 11 with AMD NPU driver
3. **Route B is confirmed as primary strategy** -- implementation can proceed without waiting for Route C feasibility
4. **No implementation has begun** -- all work so far is design and analysis

### 4.3 Architecture Decision Summary

Following user answers to all 6 clarifying questions, we have converged on a **Route B-first, unified memory** approach:
- Route B (Chunked Inference) is the primary architecture -- all weights resident, organized into chunks, async KV between chunks
- Multi-model support is a Phase 2 requirement via chunk activation/deactivation
- Route C (disk streaming) is deprioritized -- user explicitly rejected per-token disk I/O
- Route D (streaming load) is merged into Route B as an initialization optimization
- Route E (adaptive) is simplified to configuration selection (chunk size, KV size, paging thresholds)
- Quantization is optional and does not block any phase
- KV cache must support paging for sequences exceeding 16K tokens

---

## 5. Open Questions

### Status: **All answered by user (2026-04-30)**

| Question | Answer | Impact on Architecture |
|----------|--------|----------------------|
| Q1: Multi-model support | **Yes, required** | Route B primary; multi-model via chunk switching |
| Q2: Decode latency (Route C) | **Prefer unified memory model** -- NPU accesses system RAM directly | Route C eliminated; no per-token disk I/O |
| Q3: Weight caching | **Unified RAM** -- weights stay resident, OS page cache handles hot pages | No explicit weight streaming at runtime |
| Q4: KV cache paging | **Yes, reasonable** for S > 16K | AsyncKVCache must support paging/eviction |
| Q5: Embedding / LM head | **Resident** -- keep in RAM (1.05GB combined) | Baseline RSS = ~3.14GB for 1B model |
| Q6: Quantization | **Support but not required** -- optional feature | Design compatible, don't block phases |

**Direction**: User answers definitively select **Route B (Chunked Inference with Unified Memory)** as the primary architecture. Route C is deprioritized. Route D merged into B. Route E simplified to configuration selection. Multi-model is a Phase 2 requirement. Quantization is optional.

---

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

### 6.1 Unanimous Agreement (All 3 Agents + Planning Analysis)

| Item | Consensus |
|------|-----------|
| **Primary route** | Route B (Chunked Inference with Unified Memory) -- confirmed by user answers |
| **Phasing order** | Phase 0 (unified memory validation) -> Phase 1 (Foundation + KV paging) -> Phase 2 (Route B + multi-model) -> Phase 3 (Multi-model Weight Manager) -> Phase 4 (Auto-Configuration) |
| **Phase 1 priority** | ChunkManager + AsyncKVCache + BufferRegistry + KV Paging are shared prerequisites |
| **Phase 0 spike** | Unified memory bandwidth and concurrent mmap validation (replaced page_in/page_out API check) |
| **Route C status** | Deprioritized -- user rejected per-token disk streaming |
| **Route D status** | Merged into Route B as startup optimization |
| **Route E status** | Simplified to configuration selection (chunk size, KV size, paging thresholds) |
| **Apple pattern validity** | Apple's CoreML chunked approach with async KV is proven and transferable to IRON |
| **Terminology** | Block = 1 transformer layer; Chunk = group of blocks; Operator = single GEMM/norm |
| **Compilation strategy** | AOT during model conversion, never JIT per forward pass |
| **Separate entry point** | New `streaming_infer.py`, not integrated into existing `interactive_convert.py` |
| **Feature flags** | Streaming mode defaults to `False` to prevent breaking existing functionality |
| **Multi-model** | Required -- Phase 2 deliverable via chunk activation/deactivation |
| **Quantization** | Optional -- design compatible, don't block phases |
| **KV paging** | Required for S > 16K -- AsyncKVCache must support eviction |

### 6.2 Disagreements and Resolutions

| Disagreement | Resolution |
|--------------|------------|
| **Original phasing** (D -> B -> C -> E) vs **Agent-recommended** (Foundation first) vs **User-driven** (Route B primary) | All resolved. Route B is primary. Foundation (Phase 1) first. Multi-model in Phase 2. Route C deprioritized. |
| **Chunk size** (fixed vs tunable) | Consensus: implement as tunable parameter, start with 3 (Apple's), benchmark 2/3/4/8 |
| **KV async pattern** (double-buffer vs Apple's merge pattern) | Consensus: Apple's exact pattern (chunk returns new KV, separate async merge) provides future-time buffer |
| **Block file organization** (individual .npy vs bundled) | Consensus: keep individual .npy + chunk manifest JSON. Bundle only for Route C to reduce seek overhead |
| **Route C viability** | User resolved: rejected per-token disk streaming. Route C deprioritized. |

### 6.3 Outstanding Tensions

| Tension | Status |
|---------|--------|
| Multi-model RAM pressure on 16GB systems (2-3 models = 6-9GB RSS) | Requires empirical validation during Phase 2 |
| KV cache paging latency spikes at S > 16K | Requires empirical validation during Phase 1 |
| Windows memory management differences from macOS | Requires empirical validation during Phase 1-2 |
| Unified memory bandwidth sufficient for multi-model chunk switching | Phase 0 spike will validate |

---

## 7. Next Steps

### Immediate Actions (Week 1 - Phase 0)

1. **Assign Phase 0 spike owner** -- Senior engineer with NPU driver and Windows memory management experience
2. **Execute Phase 0 unified memory validation spike**:
   - Measure unified memory bandwidth between system RAM and AMD NPU
   - Determine concurrent mmap region limits for NPU driver
   - Profile OS page cache behavior on Windows 11 for large mmap'd files (1GB+)
   - Identify alignment/page size requirements for NPU-accessible memory
   - Measure NPU reconfiguration latency between chunks
   - **CRITICAL ADDITION**: Validate Python GIL behavior during NPU compute -- confirm async KV merge thread can run numpy ops simultaneously
3. **Begin Phase 1 design refinement** -- incorporate KV paging requirement (Q4) and GIL mitigation strategy into AsyncKVCache design
4. **Set up development environment** -- FakeNPUComputeEngine, test fixtures, CI pipeline for streaming module

### After Phase 0 Completion (Go/No-Go Gate)

5. **Review spike results** -- confirm unified memory bandwidth supports Route B's chunk switching pattern; confirm GIL does not block async KV
6. **Begin Phase 1** -- implement in priority order: BufferRegistry -> ChunkManager -> AsyncKVCache (with paging)
7. **Start test implementation** -- begin with BufferRegistry unit tests (U31-U55), then ChunkManager (U56-U81)
8. **Set up benchmarking framework** -- pytest-benchmark configured for chunk size tuning in Phase 2

### Milestone Checklist

- [x] User answers to Q1-Q6
- [ ] Phase 0 spike plan defined and assigned (unified memory validation)
- [ ] Phase 0 spike completed
- [ ] Spike results reviewed, Route B confirmed as primary
- [ ] Phase 1 foundation modules implemented (AsyncKVCache + ChunkManager + BufferRegistry + KV Paging)
- [ ] Phase 1 success metrics validated (>80% compute/KV overlap)
- [ ] Phase 2 Route B implemented (chunked inference)
- [ ] Phase 2 multi-model support implemented (chunk activation/deactivation)
- [ ] Phase 2 success metrics validated (<1.2GB peak during streaming load initialization; steady-state RSS: ~3.14GB; >=1.1x throughput; multi-model switching)
- [ ] Phase 3 Multi-Model Weight Manager implemented
- [ ] Phase 4 Auto-Configuration implemented

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
| D12 | 2026-04-30 | **Primary route**: Route B (Chunked Inference with Unified Memory) | User confirmed unified memory preference (Q2), resident weights (Q3), multi-model required (Q1). Route C rejected. | User answers Q1-Q6 |
| D13 | 2026-04-30 | **Route C deprioritized**: No per-token disk streaming | User explicitly rejected per-token disk reads (Q2). Eliminates page_in/page_out dependency. | User answer Q2 |
| D14 | 2026-04-30 | **Multi-model required**: Phase 2 deliverable | User confirmed multi-model is a requirement (Q1). ChunkManager must support multiple model manifests and activation switching. | User answer Q1 |
| D15 | 2026-04-30 | **Embedding + LM Head resident**: Keep in RAM (1.05GB) | User confirmed these stay resident (Q5). Increases baseline RSS but eliminates page fault latency. | User answer Q5 |
| D16 | 2026-04-30 | **KV paging for S > 16K**: AsyncKVCache supports eviction | User confirmed KV cache paging is reasonable (Q4). Phase 1 must include paging capability. | User answer Q4 |
| D17 | 2026-04-30 | **Quantization optional**: Design compatible, don't block phases | User confirmed quantization is optional (Q6). All phases proceed without quantization dependency. | User answer Q6 |

---

## 9. Risk Register

> **Consolidated**: 2026-04-30 (Pipeline Round 2) -- Merged with Section 16.6 and Section 14 findings. Single source of truth.
> **Numbering**: Sequential R1-R12. Eliminated risks marked and preserved for traceability.

| ID | Risk | Probability | Impact | Status | Mitigation | Owner |
|----|------|-------------|--------|--------|------------|-------|
| ~~R1~~ | ~~AMD NPU driver lacks `page_in`/`page_out` APIs~~ | N/A | N/A | ~~OPEN~~ **ELIMINATED** | Route B does not require these APIs. Unified memory is standard. | N/A |
| ~~R2~~ | ~~Route C disk I/O dominates decode on slow storage~~ | N/A | N/A | ~~OPEN~~ **ELIMINATED** | Route C deprioritized. No per-token disk streaming. | N/A |
| ~~R3~~ | ~~User acceptance of Route C decode latency~~ | N/A | N/A | ~~OPEN~~ **RESOLVED** | User chose unified memory model (Q2). Route C deprioritized. | N/A |
| R1 | Multi-model RAM pressure exceeds available memory (16GB system, 2-3 models) | High | **High** | **OPEN** | Chunk activation/deactivation with OS page cache. Monitor RSS. Consider model unload on switch. Tests MR1-MR4, I25. | Phase 2 |
| R2 | Integration breaks existing functionality | High | Medium | **MITIGATED** | Feature flags (`streaming_mode=False` default). Separate module hierarchy (`streaming/`). `StreamingModelAssembler` alongside existing `ModelAssembler`. Regression tests R1-R14. | All phases |
| R3 | Chunk size (3 blocks) suboptimal for AIE architecture | Medium | Medium | **OPEN** | Implement as tunable parameter. Benchmark 2/3/4/8 during Phase 2. Tests P1-P4. | Phase 2 |
| R4 | Windows memory management differs from macOS (mmap behavior under pressure) | Medium | **High** | **OPEN** | Empirical validation during Phase 1-2. Use Windows memory locking APIs if needed. Monitor page cache hit rates. Tests R15-R20. | Phase 1-2 |
| R5 | DMA driver maturity on Windows/AMD (async KV timing less precise) | Medium | Medium | **OPEN** | Design async KV with tolerance for timing variance. Add fallback to sync mode. Tests I8-I13. | Phase 1 |
| R6 | KV cache at long context (S > 16K) exceeds available RAM | Medium | Medium | **OPEN** | User confirmed paging is acceptable. Implement KV paging with eviction policy in Phase 1. Monitor paging latency. Tests K1-K6. | Phase 1 |
| R7 | KV cache paging latency spikes during attention computation | Medium | **High** | **NEW** | Implement intelligent eviction (evict oldest/least-used tokens first). Benchmark paging overhead. Add sync fallback. Tests K4-K5. | Phase 1 |
| R8 | Python GIL invalidates async KV (NPU compute holds GIL, KV async thread blocked) | Medium | **Critical** | **CRITICAL** | Phase 0 must validate GIL behavior. Design kv_async_ops.py with `use_multiprocessing` flag. Fallback: subprocess/multiprocessing for KV merge. Tests G1-G8. | Phase 0 |
| R9 | NumPy memory alignment for DMA (8-16 byte vs 4096-byte page alignment) | High | Medium | **NEW** | Use `np.memmap` with page-aligned offsets. Fall back to `ctypes.VirtualAlloc` on Windows if needed. Test B6. | Phase 1 |
| R10 | AIE compilation artifact format undefined | Medium | High | **NEW** | Define artifact format during Phase 1 design. Store alongside weight files. Validate format stability. | Phase 1 |
| R11 | Thread safety of double-buffer KV (numpy arrays not thread-safe for concurrent reads/writes) | Medium | **High** | **NEW** | Use pointer-swap with locks. Test concurrent access patterns. Validate in kv_async_ops.py. | Phase 1 |
| R12 | Phase 2 resource contention (multi-model requirement increases scope; 2-3 engineers needed) | Medium | Medium | **NEW** | Prioritize chunked inference first, multi-model second within Phase 2. Defer multi-model if constrained. | Phase 2 |

### Risk Summary

- **Critical risks**: 1 (R8 GIL -- must validate in Phase 0)
- **High risks**: 4 (R1 multi-model RAM, R4 Windows memory, R7 KV paging latency, R11 thread safety) -- all require empirical validation
- **Medium risks**: 6 (R2 mitigated, R3/R5/R6/R9 need validation, R10/R12 design/resource)
- **Eliminated**: ~~R1~~ (original, page_in/page_out), ~~R2~~ (original, Route C disk I/O), ~~R3~~ (original, Route C latency)

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

**Phase 1 -- Foundation** (4 weeks) -- Updated per Section 18.4 detailed design:

| File | Purpose | Dependencies |
|------|---------|-------------|
| `streaming/__init__.py` | Package init; exports StreamingConfig, ChunkManager, AsyncKVCache, BufferRegistry, ChunkedInferenceEngine | -- |
| `streaming/config.py` | StreamingConfig dataclass + validation (chunk_size, streaming_mode, kv_paging_threshold, max_concurrent_models) | -- |
| `streaming/buffer_registry.py` | BufferRegistry: manages hidden_states, attention_mask, rope_angles, position_ids with typed contracts | numpy |
| `streaming/kv_cache.py` | KVCache pure data structure: pre-allocates K/V, get/append/prefetch, paging/eviction for S > 16K | numpy |
| `streaming/kv_async_ops.py` | AsyncKVCache threading/DMA overlap engine: scheduling, multiprocessing fallback, GIL mitigation | kv_cache.py, concurrent.futures |
| `streaming/chunk_manifest.py` | ChunkManifest dataclass: reads/writes chunk manifest JSON (weight paths, shapes, tiling config) | json, pathlib |
| `streaming/chunk_manager.py` | ChunkManager: organizes blocks into chunks, activation/deactivation, multi-model manifest management | chunk_manifest.py, config.py |

**Phase 2 -- Route B + Multi-Model** (5 weeks):

| File | Purpose | Dependencies |
|------|---------|-------------|
| `streaming/inference_loop.py` | Shared forward-pass orchestration (prefill + decode) with chunk boundaries and async KV scheduling | All Phase 1 modules |
| `streaming/streaming_assembler.py` | StreamingModelAssembler: parallels ModelAssembler API, wraps ChunkedInferenceEngine | inference_loop.py, model_assembler.py |
| `streaming/streaming_infer.py` | Runtime entry point for streaming inference (CLI) | All Phase 1-2 modules |
| `streaming/fakes/fake_npu.py` | FakeNPUComputeEngine: numpy matmul with configurable delays, GIL behavior testing | numpy |
| `streaming/fakes/fake_dma.py` | Simulated DMA: time.sleep proportional to data size | time |

**Phase 3 -- Multi-Model Weight Manager** (4 weeks) -- Rescoped from Route C:

| File | Purpose | Dependencies |
|------|---------|-------------|
| `streaming/weight_manager.py` | Weight residency optimization, OS page cache tuning, hot-page identification for multi-model | chunk_manager.py, psutil |
| `streaming/memory_monitor.py` | Memory pressure monitoring, RSS tracking, graceful degradation thresholds, auto-unload triggers | psutil, chunk_manager.py |
| `streaming/model_lifecycle.py` | Model load/unload lifecycle, KV cache cleanup between models, state preservation | All Phase 1-3 modules |

**Phase 4 -- Auto-Configuration** (3 weeks) -- Rescoped from Route E:

| File | Purpose | Dependencies |
|------|---------|-------------|
| `streaming/auto_config.py` | Hardware detection + automatic configuration: optimal chunk size, KV cache size, paging thresholds, multi-model concurrency limits | psutil, all route modules |

**Supporting files** (as needed, per Section 18.4):

| File | Purpose |
|------|---------|
| `streaming/fakes/fake_npu.py` | FakeNPUComputeEngine: numpy matmul with configurable delays, GIL behavior testing |
| `streaming/fakes/fake_dma.py` | Simulated DMA: time.sleep proportional to data size |
| `streaming/tests/` | Test suite organized by component (not single test file) -- see Section 20.10 |
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

> **Updated**: 2026-04-30 (Pipeline Round 2) -- Replaced Route C relic metrics with Multi-Model Weight Manager targets. Added program-level metrics.

**Important note on Route B memory**: Route B with resident weights does NOT reduce steady-state RSS compared to the current architecture (~3.14GB for 1B model at S=4096). Its value is in async KV throughput optimization, multi-model support via chunk switching, and tunable chunk sizes. The "<1.2GB" metric refers only to peak memory during streaming load initialization (Route D optimization merged into Route B), NOT steady-state RSS.

| Metric | Target | Phase | Measurement Method |
|--------|--------|-------|-------------------|
| Async KV cache overlap efficiency | >80% compute/KV overlap | Phase 1 | Profiling memory transfer vs compute timeline |
| KV paging overhead at S=16K | <5% latency increase vs non-paged | Phase 1 | Benchmark paged vs non-paged KV |
| GIL behavior validation | GIL released OR multiprocessing fallback works | Phase 0 | Tests G1-G8, concurrent numpy during NPU compute |
| Route B throughput vs baseline | >=1.1x tokens/sec | Phase 2 | Benchmark: tokens/sec comparison |
| NPU compilation overhead (per chunk) | <500ms | Phase 2 | Timing chunk compilation |
| Multi-model switching latency | <100ms between models | Phase 2 | Timing chunk deactivation/activation |
| Multi-model concurrent RSS (2 models) | <7GB for two 1B models | Phase 2 | RSS measurement during dual-model inference |
| Startup initialization peak memory | <1.2GB peak during load (steady-state RSS: ~3.14GB) | Phase 2 | tracemalloc during resident load initialization |
| Memory pressure detection accuracy | Detects pressure within 100ms | Phase 3 | RSS monitoring during multi-model inference |
| Model load/unload lifecycle latency | <200ms full model unload + reload | Phase 3 | Timing model switch with KV cleanup |
| Graceful degradation compliance | Auto-unload least-used model under pressure, no data loss | Phase 3 | Memory pressure simulation tests |
| Multi-model RSS management (2x 1B on 16GB) | RSS within expected range, no OS paging thrashing | Phase 3 | RSS tracking under sustained multi-model load |
| Page cache hit rate for resident weights | >99% hit rate during inference | Phase 3 | OS-level page fault monitoring |
| Auto-configuration accuracy | Optimal config in >95% of setups | Phase 4 | Test matrix coverage |
| **Zero regression in existing functionality** | **All regression tests pass** | **All phases** | **CI pipeline on every PR (R1-R35)** |
| **Test coverage** | **>=90% line coverage** | **Per-phase** | **pytest-cov** |
| **Steady-state RSS honesty** | **RSS = ~3.14GB for 1B model at S=4096 (within 5%)** | **Phase 2** | **Tests MR1-MR4, no false memory reduction claims** |

---

## 12. Phasing Plan

```
Phase 0: Unified Memory Validation (Week 1)
         Validate AMD NPU unified memory capabilities:
         - Unified memory bandwidth (RAM -> NPU)
         - Concurrent mmap region limits
         - OS page cache behavior on Windows 11 for large files (1GB+)
         - NPU reconfiguration latency between chunks
         This is lower risk than the original page_in/page_out spike
         since unified memory is a standard feature.

Phase 1: Foundation + KV Paging (Weeks 2-5)
         Build AsyncKVCache (with paging for S > 16K) + ChunkManager
         (with multi-model support) + BufferRegistry.
         This is the shared prerequisite for ALL routes.
         Chunk size is configurable (1, 2, 3, 4, 8 blocks/chunk) for benchmarking.
         NEW: AsyncKVCache must support paging/eviction for long context.

Phase 2: Route B + Multi-Model (Weeks 5-10)
         Route B: Chunked inference with async KV between chunks. (4 weeks)
         Multi-Model: Chunk activation/deactivation between models. (1-2 weeks)
         Route D (streaming load) is merged here as a startup optimization.
         Multi-model support is now a Phase 2 requirement (not optional).

Phase 3: Multi-Model Weight Manager (Weeks 10-14)
         Rescoped from Route C. No longer about disk streaming.
         Focus on efficient weight management when running multiple models:
         - Weight residency optimization (OS page cache tuning)
         - Model load/unload lifecycle
         - Memory pressure monitoring and graceful degradation
         Depends on Phase 2 stability.

Phase 4: Auto-Configuration (Weeks 14-17)
         Rescoped from Route E. No longer about strategy selection.
         Hardware detection + automatic configuration:
         - Optimal chunk size based on RAM and AIE columns
         - KV cache size based on expected context lengths
         - KV paging thresholds based on available memory
         - Multi-model concurrency limits
         Requires Phases 1-3 to exist.
```

### Why This Order

The user's answers fundamentally simplified the architecture:
1. **Route B is primary** -- no need to choose between strategies. All weights resident, organized into chunks.
2. **Route C eliminated** -- user rejected per-token disk streaming. This removes 8 weeks of complexity.
3. **Route D merged** -- streaming load is an implementation detail of Route B startup, not a separate strategy.
4. **Route E simplified** -- instead of choosing between A/B/C/D, it now selects configurations within Route B.
5. **Multi-model required** -- moved from optional to Phase 2 requirement.
6. **Total timeline: ~17 weeks** (down from 20, saved 3 weeks by eliminating Route C complexity).

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
| ~~Q1~~ | Multi-model support | `streaming_model_concept.md` (Q5) | **ANSWERED** (Required -> D14) |
| ~~Q2~~ | Decode latency / memory model | `streaming_model_concept.md` (Q6) | **ANSWERED** (Unified memory -> D13) |
| ~~Q3~~ | Weight caching strategy | `streaming_model_concept.md` (Q3) | **ANSWERED** (Resident, OS page cache -> D12) |
| ~~Q4~~ | KV cache paging at long context | `streaming_model_concept.md` (Q4) | **ANSWERED** (Yes, S > 16K -> D16) |
| ~~Q5~~ | Embedding/LM Head streaming | `streaming_block_design.md` (Q3) | **ANSWERED** (Resident -> D15) |
| ~~Q6~~ | Quantization priority | `streaming_architecture_routes.md` (Quantification Impact) | **ANSWERED** (Optional -> D17) |
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
| Phase 2 | <1.2GB peak during streaming load init (steady-state: ~3.14GB), >=1.1x throughput, <500ms chunk compile |
| Phase 3 | Memory pressure detection <100ms, model unload/reload <200ms, graceful degradation under pressure, >99% page cache hit rate |
| Phase 4 | >95% strategy selection accuracy across test matrix |

---

## 16. Program Management Update - User Decisions Impact

> **Date**: 2026-04-30
> **Analyst**: Program Management Agent
> **Trigger**: Planning-analysis-strategist completed full re-evaluation after user answered all 6 clarifying questions. Route B confirmed as primary architecture. Timeline reduced from 20 to ~17 weeks.

### 16.1 Executive Impact Summary

The user's definitive answers to all 6 clarifying questions have fundamentally reshaped the program from a multi-route exploration to a focused, single-route implementation. This is a significant program simplification that reduces complexity, eliminates 3 weeks of schedule risk, and concentrates effort on the highest-value deliverable.

**Key program-level impacts:**

| Dimension | Before | After | Delta |
|-----------|--------|-------|-------|
| Primary architecture | 5 routes, parallel exploration | Route B only | Scope reduced 80% |
| Total timeline | 20 weeks | ~17 weeks | -3 weeks (15%) |
| Route C investment | 8 weeks | 0 (deprioritized) | -8 weeks eliminated |
| Route D treatment | Separate parallel track | Merged into Route B | Complexity reduced |
| Route E scope | Multi-strategy selector | Configuration tuner | Scope reduced 60% |
| Multi-model support | Nice-to-have | Phase 2 requirement | Scope increased |
| Critical risks | 2 (R1, R2) | 0 | All eliminated |
| High risks | 0 | 3 (R2, R5, R8) | New empirical risks |

### 16.2 Updated Phasing Plan - Program View

| Phase | Name | Weeks | Duration | Key Deliverables | Entry Criteria | Exit Criteria |
|-------|------|-------|----------|------------------|----------------|---------------|
| **Phase 0** | Unified Memory Validation | W1 | 1 week | Spike report: bandwidth, mmap limits, page cache behavior, NPU reconfig latency | Architecture design complete | Go/No-Go decision for Route B |
| **Phase 1** | Foundation + KV Paging | W2-W5 | 4 weeks | AsyncKVCache (with paging), ChunkManager (multi-model ready), BufferRegistry, >80% KV overlap verified | Phase 0 Go decision | 55+ unit tests passing, >90% coverage, >80% KV overlap |
| **Phase 2** | Route B + Multi-Model | W5-W10 | 5 weeks | Chunked inference engine, multi-model chunk switching, streaming load startup optimization, benchmark framework | Phase 1 exit criteria met | >=1.1x throughput, <1.2GB peak during load init (steady-state: ~3.14GB), <100ms model switch |
| **Phase 3** | Multi-Model Weight Manager | W10-W14 | 4 weeks | Weight residency optimizer, model load/unload lifecycle, memory pressure monitoring, graceful degradation | Phase 2 exit criteria met | Memory pressure detection <100ms, model unload/reload <200ms, graceful degradation, >99% page cache hit rate |
| **Phase 4** | Auto-Configuration | W14-W17 | 3 weeks | Hardware detector, auto chunk size selector, KV cache auto-tuner, multi-model concurrency limiter | Phases 1-3 complete | >95% correct config across test matrix |

**Critical Path**: Phase 0 -> Phase 1 -> Phase 2 -> Phase 3 -> Phase 4 (fully sequential; no parallelization possible given dependencies).

**Schedule Compression**: The 3-week reduction comes from eliminating Route C's disk streaming implementation (8 weeks saved) partially offset by expanding multi-model in Phase 2 (+1 week) and Phase 3 scope (+4 weeks for weight manager).

### 16.3 Resource Allocation

#### 16.3.1 Phase-by-Phase Resource Requirements

| Phase | FTE Engineers | Key Skills | Estimated Effort (person-weeks) |
|-------|--------------|------------|--------------------------------|
| Phase 0 | 1 (Senior) | NPU driver APIs, Windows memory management, performance profiling | 1 |
| Phase 1 | 2 (1 Senior + 1 Mid) | Async Python, numpy, memory management, threading, DMA patterns | 8 |
| Phase 2 | 2-3 (1 Senior + 1-2 Mid) | Inference engine design, chunked computation, benchmarking, multi-model architecture | 12 |
| Phase 3 | 2 (1 Senior + 1 Mid) | OS memory management, LRU cache algorithms, memory pressure monitoring | 8 |
| Phase 4 | 1-2 (1 Senior + 0-1 Mid) | Hardware detection, configuration management, optimization algorithms | 4 |
| **Total** | **Peak 3 FTE** | | **~33 person-weeks** |

#### 16.3.2 Phase 2 Resource Focus - Route B + Multi-Model

Phase 2 is now the program's most resource-intensive phase due to the multi-model requirement:

- **Chunked Inference Engine** (3 weeks): Core inference loop, async KV merge between chunks, NPU operator orchestration per chunk
- **Multi-Model Chunk Switching** (1 week): Activation/deactivation between models, KV cache partitioning, shared BufferRegistry
- **Streaming Load Optimization** (0.5 week, merged from Route D): Low-peak-memory startup initialization
- **Benchmark Framework** (0.5 week): Chunk size tuning infrastructure, baseline comparison tooling

**Resource risk**: Phase 2 requires 2-3 engineers simultaneously. If only 2 are available, the multi-model deliverable may slip by 1 week. Mitigation: prioritize chunked inference first, multi-model second within the phase.

#### 16.3.3 Phase 3 Resource Focus - Multi-Model Weight Manager

Phase 3 was rescoped from Route C (disk streaming) to Multi-Model Weight Manager:

- **Weight Residency Optimization** (1.5 weeks): OS page cache tuning, memory residency controls (Windows memory locking APIs), hot-page identification
- **Model Load/Unload Lifecycle** (1 week): Clean model switching, state preservation, KV cache cleanup between models
- **Memory Pressure Monitoring** (1 week): RSS monitoring, graceful degradation thresholds, automatic model unload under pressure
- **Integration Testing** (0.5 week): End-to-end multi-model scenarios under memory pressure

### 16.4 Milestone Definitions

| Milestone | Phase | Week | Deliverable | Acceptance |
|-----------|-------|------|-------------|------------|
| **M0** | Phase 0 | W1 | Unified memory spike report | Bandwidth validated, mmap limits documented, NPU reconfig latency measured, Go/No-Go issued |
| **M1** | Phase 1 | W5 | Foundation modules complete | AsyncKVCache, ChunkManager, BufferRegistry implemented; 55+ tests passing; >80% KV overlap |
| **M2** | Phase 2 | W7 | Chunked inference MVP | Single-model chunked inference works; >=1.0x throughput vs baseline |
| **M3** | Phase 2 | W10 | Multi-model + benchmarks | Multi-model switching <100ms; >=1.1x throughput; <1.2GB peak during load init (steady-state: ~3.14GB); benchmark framework operational |
| **M4** | Phase 3 | W14 | Weight manager complete | Memory pressure monitoring active; graceful degradation tested; model unload/reload <200ms |
| **M5** | Phase 4 | W17 | Auto-configuration complete | >95% correct config across test matrix; hardware detection working |
| **M6** | Program | W17 | Production-ready release | All phases complete; all acceptance criteria met; regression tests passing on Windows 11 |

### 16.5 Success Criteria - Program Level

| Criteria | Target | Measurement | Phase Gate |
|----------|--------|-------------|------------|
| Route B throughput improvement | >=1.1x tokens/sec vs monolithic | Benchmark comparison | M3 (W10) |
| Multi-model switching latency | <100ms between models | Timing deactivation/activation | M3 (W10) |
| Memory efficiency (load initialization) | <1.2GB peak during streaming load init (steady-state RSS: ~3.14GB) | tracemalloc during load | M3 (W10) |
| KV cache paging overhead | <5% latency increase at S=16K | Paged vs non-paged benchmark | M1 (W5) |
| Async KV overlap efficiency | >80% compute/KV overlap | DMA vs compute timeline profiling | M1 (W5) |
| Multi-model RAM management | <7GB RSS for two 1B models | RSS during dual-model inference | M3 (W10) |
| Multi-model graceful degradation (Phase 3) | Auto-unload least-used model under pressure, zero data loss | Memory pressure simulation | M4 (W14) |
| Auto-configuration accuracy | >95% correct across hardware configs | Test matrix coverage | M5 (W17) |
| Zero regression in existing functionality | All R1-R26 regression tests pass | CI pipeline on every PR | Continuous |
| Test coverage | >=90% line coverage | pytest-cov | Per-phase |

### 16.6 Updated Risk Register - Program Perspective

#### 16.6.1 Risk Changes from User Decisions

| Risk ID | Risk | Previous Status | New Status | Change Driver |
|---------|------|----------------|------------|---------------|
| R1 (original) | Missing page_in/page_out APIs | Critical | **ELIMINATED** | User chose unified memory (Q2) |
| R2 (original) | Route C disk I/O dominates | High | **ELIMINATED** | Route C deprioritized |
| R7 (original) | User acceptance of Route C latency | High | **RESOLVED** | User chose unified memory (Q2) |
| R5 | Windows memory management | Medium | **ELEVATED to High** | Now the primary OS risk for Route B's mmap behavior |
| **NEW-R2** | Multi-model RAM pressure | N/A | **NEW - High** | 2-3 models on 16GB system (6-9GB RSS) may cause OS paging pressure |
| **NEW-R8** | KV cache paging latency spikes | N/A | **NEW - High** | Paging old tokens during attention may cause latency spikes at S > 16K |
| **NEW-R9** | Python GIL invalidates async KV | N/A | **NEW - Critical** | Identified by Senior Developer assessment; if NPU compute holds GIL, KV async thread cannot run numpy ops simultaneously |
| **NEW-R10** | Phase 2 resource contention | N/A | **NEW - Medium** | Multi-model requirement increases Phase 2 scope; 2-3 engineers needed simultaneously |

#### 16.6.2 Current Risk Profile

| Severity | Count | Risks | Program Action |
|----------|-------|-------|----------------|
| **Critical** | 1 | NEW-R9 (GIL) | Phase 1 must validate GIL behavior early; implement C-level GIL release or multiprocessing fallback |
| **High** | 3 | R2 (multi-model RAM), R5 (Windows memory), R8 (KV paging latency) | All require empirical validation; mitigation paths defined |
| **Medium** | 5 | R3 (mitigated), R4, R6, R7, NEW-R10 | Monitor; mitigation in place for R3 |
| **Low** | 1 | R1 (bandwidth) | Phase 0 spike will validate |

**Risk trend**: Net positive. Eliminated 3 original risks through user decisions. Added 2 new risks (RAM pressure, KV paging) that are manageable with empirical validation. GIL risk is the only critical remaining risk and must be addressed in Phase 1.

### 16.7 Stakeholder Communication Plan

| Stakeholder Group | Communication | Frequency | Key Messages |
|-------------------|--------------|-----------|--------------|
| **Executive sponsors** | Program status brief | Bi-weekly | Route B confirmed; 17-week timeline; 3 original risks eliminated; multi-model requirement in Phase 2 |
| **Engineering team** | Technical standup | Weekly | Phase 0 spike results; foundation module progress; GIL validation; test coverage metrics |
| **QA team** | Test strategy alignment | Weekly | ~210 tests across 4 categories; no NPU hardware required; Phase 1 target: 55+ tests passing |
| **Product management** | Feature prioritization review | Bi-weekly | Multi-model as Phase 2 requirement; quantization deferred; auto-configuration as Phase 4 |
| **AMD NPU driver team** | Technical coordination | As needed | Unified memory bandwidth requirements; NPU reconfiguration latency expectations; DMA timing precision |

**Key stakeholder talking points:**
1. Architecture simplified from 5 routes to 1 (Route B) based on definitive user decisions
2. Timeline compressed by 15% (20 -> 17 weeks) while adding multi-model requirement
3. All original critical risks eliminated; new risks are empirical (validation-based), not architectural
4. No NPU hardware required for development or testing -- FakeNPUComputeEngine enables full software development
5. Feature flags ensure zero impact on existing model converter functionality

### 16.8 Dependency Map - Updated

```
Phase 0 (W1)
    |
    v
Phase 1 (W2-W5): Foundation modules
    |-- AsyncKVCache (with paging) --------+
    |-- ChunkManager (multi-model ready) --+--> Phase 2 (W5-W10): Route B + Multi-Model
    |-- BufferRegistry --------------------+       |-- Chunked inference engine
    |                                              |-- Multi-model chunk switching
    |                                              |-- Streaming load optimization
    |                                              |-- Benchmark framework
    |                                              |
    |                                              v
    +------------------------------------> Phase 3 (W10-W14): Multi-Model Weight Manager
                                                  |-- Weight residency optimization
                                                  |-- Model load/unload lifecycle
                                                  |-- Memory pressure monitoring
                                                  |
                                                  v
                                            Phase 4 (W14-W17): Auto-Configuration
                                                  |-- Hardware detection
                                                  |-- Auto chunk size selection
                                                  |-- KV cache auto-tuning
```

**No parallel tracks**: The simplified architecture means all phases are sequential. This is both a risk (no schedule compression possible) and a benefit (clear focus, no context switching between parallel workstreams).

### 16.9 Program Health Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Scope clarity** | 9/10 | Route B confirmed; all other routes deprioritized or merged. Zero ambiguity on primary architecture. |
| **Schedule realism** | 7/10 | 17 weeks is aggressive for 5 sequential phases. Phase 2 (5 weeks) is the most aggressive given multi-model requirement. |
| **Resource adequacy** | 7/10 | 2-3 FTE required for Phase 2-3. If team is understaffed, schedule will slip. |
| **Risk exposure** | 6/10 | GIL risk (NEW-R9) is critical and could invalidate async KV premise. Multi-model RAM pressure (NEW-R2) is high impact but manageable. |
| **Test coverage plan** | 9/10 | Comprehensive 220+ test strategy with no hardware dependency. Clear acceptance criteria per phase. |
| **Stakeholder alignment** | 10/10 | User provided definitive answers to all 6 questions. Zero outstanding clarifications. |
| **Overall program health** | **7.5/10** | Strong direction, clear scope, but execution risk concentrated in Phase 1-2. GIL validation is the make-or-break item. |

### 16.10 Recommendations

1. **Immediate (Week 1)**: Assign Phase 0 spike owner. Begin GIL validation alongside unified memory spike -- this is the highest-leverage risk mitigation activity.
2. **Phase 1 priority order**: Implement BufferRegistry first (easiest, zero deps), then ChunkManager, then AsyncKVCache (highest complexity, GIL dependency).
3. **Phase 2 resourcing**: Ensure 2-3 engineers available from W5. If constrained, defer multi-model to late Phase 2 and prioritize chunked inference.
4. **Phase 3 scope guard**: Keep Phase 3 focused on weight management only. Do not re-introduce Route C disk streaming concepts.
5. **Continuous**: Maintain feature flag discipline. Every commit must pass regression tests R1-R26. No exceptions.

---

## 17. Quality Review - Post-User Decisions

> **Date**: 2026-04-30
> **Reviewer**: Taylor Kim, Senior Quality Management Specialist
> **Scope**: Comprehensive cross-document quality review after user confirmed Route B as primary architecture. Reviewed all four streaming documents for internal contradictions, numerical inconsistencies, outdated content, logical gaps, and terminology consistency.
> **Overall Quality Rating: 5/10** -- Down from 7/10 (previous review). The user's Route B decision has made significant portions of the two older documents (concept, block design) actively misleading. Critical contradictions exist between the updated progress document and the legacy docs.

---

### 17.1 Critical Issues (Must Fix Before Phase 0 Begins)

| ID | Issue | Location | Detail |
|----|-------|----------|--------|
| **C1** | Phase 2 success metric "<1.2GB startup peak" contradicts user decision Q5 | STREAMING_PROGRESS.md: Sections 11, 12, 16.2, 16.5 | User confirmed embedding (525MB) + LM head (525MB) must stay resident (Q5 / D15). This means peak RSS during startup is **at minimum ~1.05GB**, not <200MB. The "<1.2GB startup peak" metric was written when Route D (streaming load) was a separate strategy. Now that Route D is merged into Route B **and** embedding/LM head are resident, this metric is impossible to achieve. **Must be updated to "<1.2GB startup peak"** (1.05GB + buffers). |
| **C2** | streaming_model_concept.md states "Disk I/O: Every forward pass" -- directly contradicts Route B | streaming_model_concept.md: Trade-offs table (line 91), Summary table (line 245) | The trade-off table for "Streaming (Layer-at-a-Time)" shows "Disk I/O: Every forward pass". The summary says Concept C has "Disk I/O per layer". The user's Q2 answer explicitly chose unified memory with **no per-token disk reads**. These tables present the old paradigm as if it were still viable. Anyone reading the concept doc first would get the wrong impression of the chosen architecture. |
| **C3** | streaming_block_design.md entire architecture model contradicts Route B | streaming_block_design.md: Sections 3.2, 6, 7 | The block lifecycle (Section 3.2) shows `load_weights()` / `release_weights()` called every forward pass for both prefill and decode. The complete pipeline (Section 6) shows "mmap 9 .npy" and "unmap 9 .npy" for every layer in every forward pass. The implementation plan (Section 7) describes a `WeightLoader` for "mmap-based weight loading." **All of this is invalidated by user decision Q3**: weights stay resident, OS page cache handles hot pages. There should be no per-forward-pass load/unload cycle in the Route B architecture. |
| **C4** | Phase 3 success metrics reference deprioritized Route C criteria | STREAMING_PROGRESS.md: Section 11 (metrics table), Section 16.5 | Phase 3 metrics include "Route C peak runtime memory <500MB for 7B model", "Route C decode latency on NVMe <50ms/token", and "Weight cache hit rate >70% after first token". Route C was deprioritized (D13). Phase 3 was rescoped to "Multi-Model Weight Manager" (Section 12, 16.3.3), but the success metrics were not updated to match the new scope. These metrics are meaningless for the rescoped phase. |

### 17.2 High-Severity Issues

| ID | Issue | Location | Detail |
|----|-------|----------|--------|
| **H1** | Per-block weight size ~116MB in older docs (should be ~121MB) | streaming_model_concept.md (lines 49, 86, 113, 201, 213); streaming_block_design.md (lines 63, 121, 316, 324, 338) | Decision D2 corrected the per-block weight calculation to ~121.6MB (FP16), not ~116MB. The routes doc uses the correct value. The concept doc and block design doc still use ~116MB. This propagates into all memory calculations in those documents. For 16 blocks, the error is 16 * 5.6MB = ~90MB discrepancy in total model weight (1.86GB vs 1.94GB). |
| **H2** | KV cache DMA sizes in timeline diagrams are off by ~16x | streaming_block_design.md: Section 4.2 (lines 164-177) | Timeline diagrams show "DMA K/V READ 32MB" and "DMA K/V WRITE 32KB" per layer at S=1000. Correct calculation: at S=1000, K/V per layer = 8 heads * 1000 seq * 64 head_dim * 2 bytes (bf16) * 2 (K+V) = **2.05MB per layer** (not 32MB). For K/V write (single new token at decode): 8 * 1 * 64 * 2 * 2 = **2KB** (not 32KB). The 32MB figure may have been calculated for S=4096 and mislabeled as S=1000. This undermines the async overlap analysis. |
| **H3** | streaming_block_design.md peak memory calculations omit resident embedding + LM head | streaming_block_design.md: Sections 3.3, 6 | Peak memory tables show ~819MB (single buffer) and ~947MB (double buffer) -- calculated with embedding/LM head as mmap'd (not resident). With user's Q5 decision, these must add 1.05GB: **~1.87GB** (single buffer) or **~2.00GB** (double buffer). The pipeline memory estimates in Section 6 ("PEAK MEMORY: ~254MB") are even further off -- they should be **~1.3GB+**. |
| **H4** | Clarifying questions in older documents still appear unanswered | streaming_model_concept.md: Section "Clarifying Questions" (lines 221-236); streaming_block_design.md: Section 9 (lines 408-425) | Both documents end with open clarifying questions. All have been answered by the user (2026-04-30). The questions should either be marked as answered with references to the decisions (D12-D17), or the documents should include a prominent notice that they predate user decisions and should be read in conjunction with streaming_architecture_routes.md. |
| **H5** | Success metrics table references eliminated Route C metrics | STREAMING_PROGRESS.md: Section 11 | Metrics for Phase 3 include "<500MB for 7B model" and "<50ms/token on NVMe" -- both were Route C targets. Phase 3 was rescoped to Multi-Model Weight Manager, which has different success criteria (memory pressure monitoring, model switching, graceful degradation). The metric table needs a complete rewrite for the new Phase 3 scope. |
| **H6** | streaming_model_concept.md memory comparison table contradicts Q5 decision | streaming_model_concept.md: Section "Memory Comparison" table (lines 208-217) | Table shows Embedding as "525MB (mmap, not resident)" and LM Head as "525MB (mmap, not resident)". User's Q5 decision (D15) makes both resident. The "Streaming + Async KV" column showing ~1.3GB peak RAM should be **~2.35GB+** with resident embedding and LM head. |

### 17.3 Medium-Severity Issues

| ID | Issue | Location | Detail |
|----|-------|----------|--------|
| **M1** | Risk numbering in Section 9 is confusing due to ID reuse | STREAMING_PROGRESS.md: Section 9 (lines 473-485) | Eliminated risks (original R1, R2, R7) are struck through but their IDs are reused for new risks (new R1 = bandwidth, new R2 = multi-model RAM, new R7 = KV cache long context). This creates ambiguity when referencing "R1" or "R2" in discussions. Recommendation: Use distinct IDs for new risks (e.g., R1-new, or continue numbering from R8). Note that Section 16.6 adds NEW-R2, NEW-R8, NEW-R9, NEW-R10 -- creating a parallel numbering system that conflicts with Section 9. |
| **M2** | Section 10.2 Phase 3/4 file descriptions reference outdated concepts | STREAMING_PROGRESS.md: Section 10.2 (lines 545-556) | Phase 3 files described as "runtime_streaming.py: Per-forward-pass page_in/page_out" and "weight_cache.py: LRU weight cache" -- these are Route C artifacts. Phase 4 file described as "adaptive_selector.py: Hardware detection + strategy selection; automatically picks best route" -- but Route E was simplified to configuration selection within Route B, not route selection. These descriptions need updating to match the rescoped phases. |
| **M3** | GIL risk (NEW-R9) not in Section 9 risk register | STREAMING_PROGRESS.md: Section 9 vs Section 14 | Section 14 (Senior Developer Assessment) identifies Python GIL as a CRITICAL risk that could invalidate the async KV premise. Section 16.6.1 also lists NEW-R9 (GIL) as Critical. However, Section 9's risk register does not include this risk. Section 9 states "Critical risks: 0" which is incorrect given the GIL finding. |
| **M4** | "Streaming" terminology is now misleading for Route B | All documents | The term "streaming" in Route B context is confusing. Route B does not stream weights at runtime -- weights are resident, organized into chunks. The term "streaming" historically implies load/unload cycles (as in the concept and block design docs). Consider renaming to "Chunked Inference Architecture" or adding a terminology note clarifying that "streaming" in this initiative refers to chunked execution, not weight streaming. |
| **M5** | Section 3.4 critical issues C1-C3 marked "NEEDS FIX" but not acted upon | STREAMING_PROGRESS.md: Section 3.4 (lines 119-138) | The previous quality review identified the same numerical inconsistencies (C1: KV DMA sizes, C2: conflicting KV patterns, C3: per-block weight size). These were flagged as needing fixes but remain unfixed in the source documents. This review confirms C1 and C3 remain outstanding; C2 was resolved by D3 but the older documents were not updated. |
| **M6** | Total weight inconsistency across documents | streaming_model_concept.md says ~2.9GB total; streaming_block_design.md says ~3.0GB; streaming_architecture_routes.md says ~3.0GB; STREAMING_PROGRESS.md Section 3.5.4 says ~3.14GB (with resident embedding) | While the variation is partially explained by different assumptions (mmap vs resident), the documents do not clearly state which assumptions apply to each number. |

### 17.4 Section 3.5 vs Section 16 Consistency Check

| Check | Result | Detail |
|-------|--------|--------|
| Route B as primary | CONSISTENT | Both sections confirm Route B as primary architecture |
| Route C deprioritized | CONSISTENT | Both sections confirm Route C is deprioritized |
| Route D merged into B | CONSISTENT | Both sections confirm merger |
| Route E simplified | CONSISTENT | Both sections confirm simplification to configuration selection |
| Multi-model required | CONSISTENT | Both sections confirm Phase 2 requirement |
| KV paging for S > 16K | CONSISTENT | Both sections confirm paging requirement |
| Quantization optional | CONSISTENT | Both sections confirm optional status |
| Timeline: 17 weeks | CONSISTENT | Section 3.5.8 implies 17 weeks; Section 16.2 explicitly states 17 weeks |
| **Phase 2 startup peak metric** | **INCONSISTENT** | Section 3.5.4 memory table implies ~3.14GB baseline; Section 16.2/16.5 still references "<1.2GB startup peak" -- this is the C1 critical issue |
| Risk register | **INCONSISTENT** | Section 9 lists different risks than Section 16.6. Section 16.6 includes GIL risk (NEW-R9, Critical); Section 9 does not |
| Phase 3 scope description | **INCONSISTENT** | Section 12 describes Phase 3 as "Multi-Model Weight Manager"; Section 11 success metrics still reference Route C targets |

### 17.5 Document Health Summary

| Document | Currency | Accuracy | Completeness | Action Needed |
|----------|----------|----------|--------------|---------------|
| streaming_model_concept.md | **OUTDATED** | Partially incorrect | Incomplete (pre-decision) | Add deprecation notice OR update to reflect Route B. Key tables and trade-offs are misleading. |
| streaming_block_design.md | **OUTDATED** | Partially incorrect | Incomplete (pre-decision) | Add deprecation notice OR major update. Architecture diagrams, memory calculations, and lifecycle all contradict Route B. |
| streaming_architecture_routes.md | CURRENT | Correct | Complete | Minor: update Route C description to note it is deprioritized (not just an option). Add user decision references. |
| STREAMING_PROGRESS.md | MOSTLY CURRENT | Mostly correct | Complete | Fix C1 (success metrics), C4 (Phase 3 metrics), M1 (risk numbering), M3 (add GIL risk). Sections 3.5 and 16 are internally consistent with each other but inconsistent with Sections 9, 11, and 12 in specific areas. |

### 17.6 Recommended Actions (Priority Order)

1. **Fix C1 immediately**: Update all instances of "<1.2GB startup peak" across STREAMING_PROGRESS.md Sections 11, 12, and 16 to "<1.2GB startup peak" (reflecting resident embedding + LM head). This metric appears in success criteria, phasing plan, milestone definitions, and program success criteria.
2. **Add deprecation notices**: Add prominent banners to streaming_model_concept.md and streaming_block_design.md stating they predate user decisions (2026-04-30), that Route B is confirmed as primary, and that readers should consult streaming_architecture_routes.md for the current architecture.
3. **Consolidate risk registers**: Merge Section 9 and Section 16.6 risk registers into a single source of truth. Add GIL risk (Critical) to Section 9. Fix risk numbering to avoid ID collisions.
4. **Update Phase 3 success metrics**: Replace Route C targets with Multi-Model Weight Manager targets (e.g., "memory pressure detection accuracy", "model unload/reload latency", "graceful degradation threshold compliance").
5. **Update Section 10.2 file descriptions**: Rewrite Phase 3 and Phase 4 file descriptions to match rescoped phases (remove page_in/page_out, LRU cache, and route selection language).
6. **Clarify terminology**: Add a note in STREAMING_PROGRESS.md clarifying that "streaming" in this initiative refers to chunked inference execution, not per-forward-pass weight streaming.

### 17.7 Positive Findings

- The user decision analysis in Section 3.5 is thorough, well-structured, and correctly re-evaluates all five routes against the six user answers.
- The memory impact analysis (Section 3.5.4) is numerically correct for the Route B configuration with resident embedding and LM head.
- The multi-model architecture implications (Section 3.5.5) correctly identify that with resident weights, multi-model switching is primarily about NPU reconfiguration and KV cache management.
- The program management update (Section 16) provides excellent resource allocation, milestone definitions, and dependency mapping.
- The decision log (Section 8) is complete and correctly traces all 17 decisions to their sources.
- The agent consensus section (Section 6) accurately captures agreements and resolved disagreements.

---

*Review complete. 4 critical, 6 high, and 6 medium issues identified. Recommend addressing all critical items before Phase 0 begins to prevent building on contradictory requirements.*

---

## 18. Senior Developer Assessment - Route B Implementation

> **Date**: 2026-04-30
> **Author**: Jordan Blake, Principal Software Engineer & Technical Lead
> **Scope**: Route B (Chunked Inference with Unified Memory) implementation feasibility, module refactoring vs. new files analysis, risk assessment, and recommended implementation order.

---

### 18.1 Overall Ratings

| Dimension | Rating | Key Finding |
|-----------|--------|-------------|
| Implementation Feasibility | 8/10 | Route B is the simplest of all proposed routes. All weights resident eliminates the hardest engineering problems. Async KV is the primary complexity. |
| Code Structure | 7/10 | Existing codebase has clean separation. `streaming/` package should be additive, not invasive. Missing inference loop abstraction. |
| Technical Risk Coverage | 6/10 | GIL risk remains critical. Alignment and driver API risks are real but manageable with proper mitigation patterns. |
| Refactoring Scope | 6/10 | Low surface area -- 2 files need moderate changes, rest are additive. `model_assembler.py` needs `StreamingModelAssembler` sibling. |
| Developer Readiness | 7/10 | `FakeNPUComputeEngine` enables full software development. Test strategy is solid. Need to validate GIL behavior in Phase 0. |
| Test Strategy | 9/10 | CPU-only testing via FakeNPU is excellent. No hardware dependency for Phases 0-2. |

### 18.2 Route B Fundamental Characterization

Route B is the **least risky** of all five routes evaluated. Here is why:

1. **No per-forward-pass weight I/O**. Unlike Route C, there are zero disk reads during inference. Weights are mmap'd once at startup and stay mapped. This eliminates the single largest source of latency variance.

2. **No load/unload lifecycle complexity**. The `StreamingBlock.load_weights()` / `release_weights()` pattern from `streaming_block_design.md` (Sections 3.2, 6) is **invalidated** by user decision Q3. Weights stay resident. What we actually need is `ChunkManager.activate_chunk()` which is NPU reconfiguration, not weight loading.

3. **Async KV is the only novel engineering challenge**. Apple proved this pattern works. The question is whether Python threading model (GIL) allows true overlap.

4. **Multi-model is chunk activation, not weight management**. With resident weights, switching models means: (a) deactivate current model's chunks, (b) activate target model's chunks, (c) partition KV cache. This is pointer/flag manipulation, not I/O.

**Bottom line**: Route B's difficulty is not in weight management. It is in **orchestration correctness** -- getting chunk activation, KV cache lifecycle, and the inference loop right without data corruption.

### 18.3 Existing Codebase Analysis: What Needs Refactoring

| File | Change Required | Effort | Detail |
|------|----------------|--------|--------|
| `model_assembler.py` | **Add `StreamingModelAssembler`** | Moderate (30%) | Current `ModelAssembler` creates all layers eagerly and runs monolithic forward pass. Need a sibling class that: (a) accepts chunk configuration, (b) creates `ChunkedInferenceEngine`, (c) exposes same `forward()`/`generate()` API. Do NOT modify existing `ModelAssembler` -- preserve backward compatibility. |
| `layer_builder.py` | **Extract KV cache management** | Minor (15%) | `AttentionLayerBuilder` currently owns `k_cache`/`v_cache` buffers (lines 124-126) with `use_kv_cache` flag. For Route B, KV cache must be external to the layer (managed by `AsyncKVCache`). Refactor: remove cache buffers from `AttentionLayerBuilder`, accept external KV reference in `forward()`. Keep existing behavior as default. |
| `weight_mapper.py` | **No changes** | 0% | `WeightMapper` is conversion-time only. Its `.get_weights_for_layer()` method (line 358) is already perfect for chunked weight organization. |
| `config_adapter.py` | **Add `StreamingConfig` dataclass** | Minor (5%) | Add new dataclass with `chunk_size`, `streaming_mode`, `kv_paging_threshold`, `max_concurrent_models`. Add `streaming_config` field to `NormalizedConfig.npu_config`. No breaking changes. |
| `operator_factory.py` | **No changes** | 0% | Operator creation is identical whether monolithic or chunked. |
| `shape_manager.py` | **Add per-chunk memory mode** | Minor (5%) | Current `get_memory_requirements()` returns full-model numbers. Add `chunk_memory_requirements(chunk_id, chunk_size)` method. |
| `interactive_convert.py` | **No changes** | 0% | Offline conversion tool. Unchanged. |

### 18.4 New Module Hierarchy for Route B

```
iron/model_convert/
  streaming/                          # New package (additive, no existing file modifications)
    __init__.py                       # Package init; exports: StreamingConfig, ChunkManager, AsyncKVCache, BufferRegistry, ChunkedInferenceEngine
    config.py                         # StreamingConfig dataclass + validation
    buffer_registry.py                # Pre-allocated activation buffers with typed contracts
    kv_cache.py                       # KVCache pure data structure (no async)
    kv_async_ops.py                   # AsyncKVCache with threading/DMA overlap engine
    chunk_manager.py                  # Chunk organization, activation/deactivation, manifest I/O
    chunk_manifest.py                 # ChunkManifest dataclass (private: read/write JSON)
    inference_loop.py                 # Shared forward-pass orchestration (prefill + decode)
    streaming_assembler.py            # StreamingModelAssembler (parallel to ModelAssembler)
    streaming_infer.py                # Runtime entry point (replaces planned streaming_infer.py at root)
    fakes/                            # Test infrastructure
      __init__.py
      fake_npu.py                     # FakeNPUComputeEngine: numpy matmul with configurable delays
      fake_dma.py                     # Simulated DMA: time.sleep proportional to data size
    tests/                            # Test suite (not single test file)
      __init__.py
      test_buffer_registry.py         # Buffer allocation, typed contracts, alignment
      test_kv_cache.py                # KV data structure, paging, eviction
      test_kv_async_ops.py            # Threading, overlap measurement, GIL behavior
      test_chunk_manager.py           # Chunk organization, activation switching, manifest I/O
      test_inference_loop.py          # Full prefill/decode loops with FakeNPU
      test_streaming_assembler.py     # Assembly parity with ModelAssembler
      test_multi_model.py             # Model switching, KV partitioning
      integration/
        __init__.py
        test_full_pipeline.py         # End-to-end with FakeNPU
        test_output_parity.py         # Output matches monolithic ModelAssembler
```

### 18.5 Critical Technical Risk Deep-Dive

#### R9: Python GIL and Async KV (CRITICAL -- Probability: Medium, Impact: Catastrophic)

This is the single highest-leverage risk in the entire initiative. If the NPU compute call holds the Python GIL, the KV async merge thread cannot execute any Python bytecode during compute -- which means no numpy operations, no buffer manipulation, no nothing. The "async" KV becomes effectively synchronous.

**Verification approach (Phase 0 spike):**

```python
import threading
import time
import numpy as np

gil_released = False

def npu_compute_simulation():
    """Simulate NPU compute. Does this release the GIL?"""
    global gil_released
    # If the actual AMD NPU driver uses ctypes/cffi with
    # Py_BEGIN_ALLOW_THREADS, this will release the GIL.
    # If it uses pure Python bindings, it likely holds it.
    # ... actual NPU call here ...
    gil_released = True  # Verify via timing

def concurrent_numpy():
    """Try to run numpy ops while NPU computes."""
    start = time.monotonic()
    arr = np.zeros((1000, 1000))
    np.matmul(arr, arr)
    elapsed = time.monotonic() - start
    return elapsed  # If < baseline, GIL was released

# If concurrent_numpy() takes full time while NPU runs,
# GIL was NOT released. Async KV is invalid.
```

**Mitigation patterns (ordered by preference):**

1. **C-level GIL release in AMD driver**: If the driver's `submit()`/`execute()` calls use `Py_BEGIN_ALLOW_THREADS`, we are fine. This is the most likely scenario for any mature hardware driver. **Must verify in Phase 0.**

2. **`multiprocessing` with shared memory**: Run NPU compute in a separate process. Python multiprocessing does not share the GIL. Use `multiprocessing.shared_memory` for buffer passing. Adds serialization overhead but guarantees parallelism.

3. **`concurrent.futures.ProcessPoolExecutor`**: Higher-level abstraction over multiprocessing. Same GIL benefit, easier to test.

4. **Drop to C extension for compute submit**: Wrap the NPU submit call in a minimal C extension that explicitly releases the GIL. This is the nuclear option but guarantees the behavior.

**Recommendation**: Assume GIL is NOT released until proven otherwise. Design `kv_async_ops.py` with a `use_multiprocessing` flag. Default to `ThreadPoolExecutor` for development/test (FakeNPU), switch to `ProcessPoolExecutor` for production if GIL validation fails.

#### R10: NumPy Memory Alignment for DMA (HIGH -- Probability: High, Impact: Medium)

Standard `np.zeros()` and `np.empty()` allocate memory with 8-16 byte alignment (cache-line aligned). DMA engines typically require 4096-byte (page) alignment for optimal or correct operation.

**Verification approach (Phase 0 spike):**

```python
import numpy as np
import ctypes

arr = np.zeros((1024, 1024), dtype=np.float16)
addr = arr.ctypes.data
print(f"Alignment: {addr % 4096} bytes")  # Likely 8-16, not 0
```

**Mitigation patterns:**

1. **`ctypes.VirtualAlloc` (Windows)**: Allocate page-aligned memory via Win32 API, then create numpy array on top via `np.ctypeslib.as_array()`.

2. **`np.memmap` with page-aligned offsets**: Create a memory-mapped file with offset at a page boundary. The mmap data will be page-aligned.

3. **`posix_memalign` equivalent on Windows**: Use `ctypes.windll.kernel32.VirtualAlloc` with `MEM_COMMIT | MEM_RESERVE`.

4. **Accept 8-16 byte alignment**: Some DMA drivers handle unaligned memory with internal buffering (at a performance cost). If the AMD driver handles this, no action needed.

**Recommendation**: Use `np.memmap` on a temporary file with page-aligned offsets for KV cache buffers. This is cross-platform and does not require Win32-specific code paths. Reserve `VirtualAlloc` for if memmap proves insufficient.

#### R11: AMD NPU Driver Unified Memory API (MEDIUM -- Probability: Low, Impact: High)

Route B depends on the NPU reading system RAM directly via unified memory. The question is whether the AMD NPU driver on Windows exposes the necessary APIs to: (a) submit buffers from system RAM for NPU access, (b) signal completion, (c) handle page faults if OS reclaims pages.

**Assessment**: Unified memory is a standard feature on modern AMD NPUs (Ryzen AI / NPU2). The driver almost certainly supports submitting system RAM buffers. The unknown is:
- Does it require pinned/locked memory, or does it handle page faults transparently?
- Is there a bandwidth limit compared to dedicated VRAM?
- Are there concurrent buffer submission limits?

**Phase 0 spike scope**: Measure unified memory bandwidth, concurrent buffer limits, and page fault behavior. This is lower risk than the original `page_in/page_out` API check because unified memory is a mature technology.

### 18.6 Recommended Implementation Order

Following the principle of "build the easy, testable things first to de-risk the hard things," here is the recommended build order within Phase 1:

1. **`streaming/config.py`** (Day 1-2): Define `StreamingConfig` dataclass. Zero dependencies. Establishes the configuration contract for everything else.

2. **`streaming/buffer_registry.py`** (Day 3-5): Easiest component. Pure numpy buffer management with typed contracts. Immediately testable. No threading, no hardware dependency.

3. **`streaming/kv_cache.py`** (Day 6-10): Pure data structure. Pre-allocate KV cache, implement get/append/prefetch, add paging/eviction for S > 16K. Testable with FakeNPU.

4. **`streaming/chunk_manifest.py` + `streaming/chunk_manager.py`** (Day 11-17): Chunk organization, manifest I/O, activation/deactivation. Depends on Config. Testable with manifests generated from existing weight files.

5. **`streaming/kv_async_ops.py`** (Day 18-25): **Highest complexity component**. Threading/multiprocessing engine for async KV overlap. This is where GIL mitigation lives. Requires `FakeNPUComputeEngine` to test overlap behavior without hardware.

6. **`streaming/inference_loop.py`** (Day 26-30): Orchestrates all components into prefill/decode loops. Integration test with FakeNPU.

7. **`streaming/streaming_assembler.py`** (Day 31-35): `StreamingModelAssembler` that wraps the inference loop. API parity with `ModelAssembler`.

8. **`streaming/streaming_infer.py`** (Day 36-38): CLI entry point. Wiring exercise.

**Total Phase 1 estimate: 5-6 weeks** (consistent with Program Management estimate of 4 weeks, with 1-2 week buffer for GIL investigation).

### 18.7 GIL Validation in Phase 0 Spike

The Phase 0 unified memory validation spike must include GIL behavior testing. Recommended spike additions:

1. **Measure GIL release**: Start NPU compute, immediately try numpy operations in another thread. Measure if they execute concurrently.

2. **Measure threading overhead**: Even if GIL is released, context switching between compute and KV threads may negate async benefit.

3. **Identify blocking calls**: Map which NPU driver calls hold the GIL and which release it. The `submit()` call is critical; `wait()` or `sync()` calls may also hold it.

4. **Test multiprocessing alternative**: If GIL is held, verify that `ProcessPoolExecutor` with shared memory achieves the desired overlap. Measure serialization overhead.

### 18.8 What the Current Codebase Gets Right

1. **`weight_mapper.py`**: The `.get_weights_for_layer()` method is exactly what chunked organization needs. Each chunk can call this to get its subset of weights.

2. **`config_adapter.py`**: The `NormalizedConfig` dataclass is clean and extensible. Adding `npu_config` streaming fields is natural.

3. **`model_assembler.py`**: The `ModelAssembler` class structure (assemble -> load_weights -> forward -> generate) provides the API contract that `StreamingModelAssembler` must match.

4. **`layer_builder.py`**: The builder pattern is sound. The only change needed is externalizing KV cache.

### 18.9 What the Current Codebase Gets Wrong (for Route B)

1. **`ModelAssembler.forward()` (line 426)**: Iterates all layers sequentially in a single forward pass. For Route B chunked inference, this needs to iterate chunks, trigger async KV between chunks, and respect chunk boundaries.

2. **`ModelAssembler.generate()` (line 503)**: Monolithic autoregressive loop. Needs chunk-aware version that handles KV cache updates between chunks.

3. **`AttentionLayerBuilder.k_cache` / `v_cache` (lines 124-126)**: KV cache is per-layer-embedded. For Route B, it must be a centralized, externally-managed pool that all chunks share.

4. **`TransformerBlockBuilder.forward()` (line 717)**: Takes `mask` and `angles` as parameters per call. For Route B, these should be in `BufferRegistry` (computed once, reused across all chunks).

### 18.10 Route B Memory Reality Check

The documents claim Route B reduces memory. Let me be precise about what it actually does:

| Metric | Current Architecture | Route B (User Decisions) | Delta |
|--------|---------------------|--------------------------|-------|
| Embedding | 525MB resident | 525MB resident (Q5) | No change |
| LM Head | 525MB resident | 525MB resident (Q5) | No change |
| Layer weights | 1.94GB resident | 1.94GB mmap'd (Q3) | Virtual memory same, RSS may vary |
| KV Cache (S=4096) | 128MB | 128MB | No change |
| Activations | ~50MB | ~50MB | No change |
| **Total RSS** | **~3.0GB** | **~3.14GB** | **+5% (resident embedding)** |
| **Total Virtual** | **~3.0GB** | **~3.14GB** | **+5%** |

Route B does NOT reduce peak memory for the 1B model with the user's resident-weight decision. Its value propositions are:
- **Async KV optimization**: Apple proved ~20ms speedup for 7B via chunk-level async KV merge.
- **Multi-model via chunk switching**: Switch between models without weight reload.
- **Tunable chunk sizes**: Optimize for different hardware configurations.
- **Foundation for future optimization**: If memory pressure becomes an issue, the chunking infrastructure enables progressive eviction.

If the primary goal is memory reduction, Route B with resident weights does not achieve it. The documents should be honest about this to set correct stakeholder expectations.

### 18.11 Module Dependency Graph

```
config.py                    (no deps)
     |
     v
buffer_registry.py          (numpy)
     |
     v
kv_cache.py                 (numpy)
     |
     v
chunk_manifest.py           (json, pathlib)
     |
     v
chunk_manager.py            (chunk_manifest.py, config.py)
     |
     +----+
     |    |
     v    v
kv_async_ops.py            (kv_cache.py, threading/concurrent.futures)
     |
     v
inference_loop.py           (all above + buffer_registry.py + chunk_manager.py)
     |
     v
streaming_assembler.py      (inference_loop.py + model_assembler.py reference)
     |
     v
streaming_infer.py          (all above + CLI framework)
```

### 18.12 Test Infrastructure Recommendation

The `FakeNPUComputeEngine` concept from the testing strategy is critical. Here is the recommended implementation approach:

```python
class FakeNPUComputeEngine:
    """Simulates AMD NPU compute using numpy matmul with configurable delays."""

    def __init__(
        self,
        compute_delay_ms: float = 50.0,   # Simulated NPU latency per op
        dma_bandwidth_mb_s: float = 2000,  # Simulated DMA bandwidth
        release_gil: bool = True,          # Does the "driver" release GIL?
    ):
        self.compute_delay = compute_delay_ms / 1000
        self.dma_bandwidth = dma_bandwidth_mb_s * 1024 * 1024
        self.release_gil = release_gil

    def compute(self, op_name: str, inputs: dict) -> np.ndarray:
        """Execute a fake NPU operation."""
        if op_name == "gemm":
            time.sleep(self.compute_delay)  # Simulates NPU latency
            return np.matmul(inputs["a"], inputs["b"])
        # ... other ops ...

    def submit_dma(self, data: np.ndarray, direction: str) -> float:
        """Simulate DMA transfer with timing proportional to data size."""
        size_bytes = data.nbytes
        transfer_time = size_bytes / self.dma_bandwidth
        time.sleep(transfer_time)
        return transfer_time
```

With `release_gil=True`, the fake engine should use a threading mechanism that simulates GIL release. With `release_gil=False`, it should hold the GIL, allowing the async KV code to be tested under the worst-case condition.

### 18.13 Final Assessment

Route B is the **right choice** given the user's decisions. It trades memory reduction (which the user is willing to accept) for architectural cleanliness and async optimization opportunities. The critical path to success is:

1. **Phase 0 GIL validation**: This is the make-or-break item. If GIL is not released by the AMD driver, async KV must use multiprocessing, which adds serialization complexity.

2. **Phase 1 foundation**: Build BufferRegistry -> KVCache -> ChunkManager -> AsyncKVOps in that order. Each layer de-risks the next.

3. **Phase 2 integration**: Chunked inference loop + multi-model switching. The hardest part is getting the async KV merge timing right -- it must complete before the next chunk needs the updated cache.

4. **Honest stakeholder communication**: Route B does not reduce RSS for the 1B model with resident weights. Its benefits are in throughput optimization and multi-model support. Set expectations accordingly.

**Overall feasibility: 8/10**. Route B is achievable with disciplined phased execution. The GIL risk (R9) is the only item that could invalidate the async KV premise, and it can be de-risked in a 1-week Phase 0 spike before committing to full implementation.

---

*Assessment complete by Jordan Blake, Principal Software Engineer & Technical Lead.*

---

## 19. Coherence Verification

> **Date**: 2026-04-30
> **Reviewer**: Taylor Kim, Senior Quality Management Specialist
> **Scope**: Cross-section coherence check after all four agent passes and user decisions. Verified that Sections 3.5, 12, 16, 17, and 18 are internally consistent, user decisions are reflected throughout, risk numbers do not collide, and success metrics are coherent.

### 19.1 Verification Summary

| Check | Status | Detail |
|-------|--------|--------|
| Route B confirmed as primary | PASS | Consistent across Sections 3.5, 6, 12, 16, 17, 18 |
| Route C deprioritized | PASS | Consistent everywhere |
| Route D merged into B | PASS | Consistent everywhere |
| Route E simplified to config selection | PASS | Consistent everywhere |
| Multi-model as Phase 2 requirement | PASS | Consistent across all sections |
| KV paging for S > 16K | PASS | Consistent across Sections 3.5, 12, 16, 17 |
| Quantization optional | PASS | Consistent everywhere |
| User decisions Q1-Q6 reflected | PASS | All 6 decisions consistently reflected in Sections 3.5.1, 5, 6.1, 8 (D12-D17), 12, 16, 17, 18 |
| 17-week timeline | PASS | Sections 12, 16.1, 16.2 all state ~17 weeks |
| Phase boundaries and durations | PASS | Phase 0 (1wk), Phase 1 (4wk), Phase 2 (5wk), Phase 3 (4wk), Phase 4 (3wk) consistent in Sections 4.1, 12, 16.2, 16.8 |
| Memory numbers (3.14GB single model) | PASS | Sections 3.5.4 and 18.10 both cite ~3.14GB RSS for 1B model at S=4096 |
| Decision log (D1-D17) | PASS | Complete, correctly sourced, no gaps |
| Implementation order | PASS | Sections 16.10 and 18.6 agree on BufferRegistry first, then ChunkManager, then AsyncKV |
| Senior dev memory honesty | PASS | Section 18.10 explicitly states Route B does NOT reduce RSS; Section 3.5.4 "Key insight" confirms |

**Overall coherence: 7/10** -- Major architectural decisions are consistent throughout. Remaining issues are concentrated in success metrics, risk register fragmentation, and documentation hygiene.

### 19.2 Remaining Inconsistencies Requiring Fixes

#### CRITICAL (Must fix before Phase 0)

| ID | Issue | Location | Detail |
|----|-------|----------|--------|
| **CV1** | GIL risk missing from Section 9 risk register | Section 9 vs Sections 14, 16.6 | Section 9 states "Critical risks: 0" but Section 16.6.2 lists "Critical: 1 (NEW-R9 GIL)". Section 14 identifies GIL as the single highest-leverage risk. Section 9 must be updated to include GIL risk with Critical severity. |
| **CV2** | Phase 3 success metrics are Route C relics | Sections 11, 15, 16.5 | Section 11 Phase 3 metric "<1% page fault rate" does not match Multi-Model Weight Manager scope. Section 15 Phase 3 acceptance criteria ("<500MB for 7B model", "<50ms/token on NVMe", ">70% cache hit rate") are all Route C targets. Section 16.5 also includes "<500MB for 7B model". All must be replaced with Multi-Model Weight Manager metrics (e.g., memory pressure detection accuracy, model unload/reload latency, graceful degradation threshold compliance). |
| **CV3** | Table of Contents missing Sections 14-18 | Section 1 (TOC) | TOC ends at Section 13. Sections 14 (Senior Developer Assessment), 15 (Testing Strategy), 16 (Program Management), 17 (Quality Review), and 18 (Route B Implementation Assessment) are not listed. This is a significant documentation gap for any reader using the TOC. |

#### HIGH (Should fix before Phase 1)

| ID | Issue | Location | Detail |
|----|-------|----------|--------|
| **CV4** | "<1.2GB startup peak" metric is ambiguous | Sections 7, 15, 16.2, 16.5 | This metric refers to the streaming load initialization peak (merged Route D optimization), NOT steady-state RSS. Steady-state RSS is ~3.14GB (Sections 3.5.4, 18.10). Without clarification, stakeholders may incorrectly believe Route B reduces overall memory. Should be renamed to "<1.2GB peak during streaming load initialization" with a note that steady-state RSS is ~3.14GB. |
| **CV5** | Risk ID collisions between Section 9 and Section 16.6 | Sections 9, 16.6 | Section 9 reuses R1, R2, R7 IDs (strikethrough old, assign new). Section 16.6 uses NEW-R prefix (NEW-R2, NEW-R8, NEW-R9, NEW-R10). These parallel numbering systems conflict. Recommendation: Use a single sequential numbering scheme (R1 through R11, with eliminated risks marked). |
| **CV6** | Section 10.2 Phase 3/4 file descriptions are outdated | Section 10.2 | Phase 3 files described as "runtime_streaming.py: Per-forward-pass page_in/page_out" and "weight_cache.py: LRU weight cache" -- these are Route C artifacts. Phase 4 file described as "adaptive_selector.py: automatically picks best route" -- but Route E was simplified to configuration selection within Route B. Must be rewritten for rescoped phases. |
| **CV7** | Section 10.2 Phase 1 file list doesn't match Section 18.4 | Section 10.2 vs 18.4 | Section 10.2 lists 3 Phase 1 files (async_kv_cache.py, chunk_manager.py, buffer_registry.py). Section 18.4 proposes 8 files including config.py, kv_cache.py/kv_async_ops.py split, inference_loop.py, chunk_manifest.py. Section 18.4 is the more detailed and current design. Section 10.2 should be updated. |

#### MEDIUM (Recommended)

| ID | Issue | Location | Detail |
|----|-------|----------|--------|
| **CV8** | Section 4.1 Phase 1 duration inconsistency | Section 4.1 vs Sections 12, 16.2 | Section 4.1 says "3-4 weeks"; Sections 12 and 16.2 say "4 weeks". Update Section 4.1 to "4 weeks". |
| **CV9** | Section 3.4 critical issues still marked "NEEDS FIX" | Section 3.4 | Previous quality review flagged C1 (KV DMA sizes), C2 (KV patterns), C3 (per-block weight size) as needing fixes. C1 was fixed in the progress document; C2 resolved by D3; C3 remains in source docs. Section 3.4 should be updated to reflect current status. |
| **CV10** | Section 11 missing key program-level metrics | Section 11 vs 16.5 | Section 16.5 includes "Zero regression in existing functionality" and ">=90% test coverage" which are not in Section 11. Section 11 should be the canonical metrics table and include all program-level criteria. |
| **CV11** | Section 11 should note Route B does not reduce steady-state RSS | Section 11 | Section 18.10 and Section 3.5.4 are explicit about this. Section 11 should include a clarifying note to prevent stakeholder misinterpretation of the metrics. |

### 19.3 Section-by-Section Health Assessment

| Section | Currency | Internal Consistency | Cross-Section Consistency | Notes |
|---------|----------|---------------------|--------------------------|-------|
| 1-2 (Executive Summary, What's Done) | CURRENT | GOOD | GOOD | Accurate summary of current state |
| 3-3.4 (Analysis, Previous Quality Review) | MOSTLY CURRENT | GOOD | GOOD | Section 3.4 needs status update on C1-C3 |
| 3.5 (User Answers Impact) | CURRENT | EXCELLENT | EXCELLENT | Thorough, accurate, well-structured |
| 4 (Current State) | CURRENT | GOOD | MINOR GAP | Phase 1 duration should say "4 weeks" not "3-4 weeks" |
| 5 (Open Questions) | CURRENT | EXCELLENT | EXCELLENT | All answered, properly documented |
| 6 (Agent Consensus) | CURRENT | EXCELLENT | EXCELLENT | Accurately captures all agreements |
| 7 (Next Steps) | CURRENT | GOOD | MINOR GAP | "<1.2GB startup peak" needs clarification (CV4) |
| 8 (Decision Log) | CURRENT | EXCELLENT | EXCELLENT | Complete D1-D17, all correctly sourced |
| 9 (Risk Register) | OUTDATED | POOR | POOR | Missing GIL risk (CV1), ID collisions (CV5), says "Critical: 0" incorrectly |
| 10 (Codebase Impact) | MOSTLY CURRENT | MINOR GAP | MINOR GAP | Phase 1 file list (CV7) and Phase 3/4 descriptions (CV6) outdated |
| 11 (Success Metrics) | OUTDATED | POOR | POOR | Phase 3 metrics are Route C relics (CV2), missing program metrics (CV10), needs Route B memory note (CV11) |
| 12 (Phasing Plan) | CURRENT | GOOD | GOOD | Consistent with Sections 16 and 3.5 |
| 13 (Appendix) | CURRENT | GOOD | GOOD | Accurate cross-references |
| 14 (Senior Dev Assessment) | CURRENT | EXCELLENT | EXCELLENT | Excellent, honest assessment of Route B realities |
| 15 (Testing Strategy) | MOSTLY CURRENT | MINOR GAP | MINOR GAP | Phase 3 acceptance criteria are Route C relics (CV2) |
| 16 (Program Management) | CURRENT | GOOD | MINOR GAP | Solid, but "<500MB for 7B model" in 16.5 is Route C relic (CV2) |
| 17 (Quality Review) | CURRENT | EXCELLENT | EXCELLENT | Accurate identification of issues; its recommendations remain valid |
| 18 (Route B Implementation) | CURRENT | EXCELLENT | EXCELLENT | Best section for understanding Route B realities and honest memory assessment |

### 19.4 Critical Finding: Risk Register Fragmentation

The most significant coherence gap is the **fragmented risk register**. Three different sections contain risk information that does not converge into a single source of truth:

- **Section 9**: Original risk register, missing GIL risk, has ID collisions, incorrectly states "Critical risks: 0"
- **Section 14**: Identifies 4 critical unaddressed risks (GIL, NumPy alignment, AIE artifact format, thread safety)
- **Section 16.6**: Program perspective risk register with NEW-R prefixed risks, correctly identifies GIL as Critical

**Recommendation**: Consolidate all risks into Section 9 as the single source of truth. Use sequential numbering R1-R12+. Mark eliminated risks clearly. Ensure Section 14's findings and Section 16.6's risks are all represented.

### 19.5 Recommendation Priority

1. **Fix CV1 immediately**: ~~Add GIL risk to Section 9.~~ **DONE** -- Section 9 consolidated with all 12 risks (R1-R12), GIL risk listed as R8 Critical.
2. **Fix CV2**: ~~Replace all Phase 3 Route C relic metrics~~ **DONE** -- Sections 11, 15, 16.2, 16.5, and M4 updated with Multi-Model Weight Manager metrics.
3. **Fix CV3**: ~~Update TOC to include Sections 14-18.~~ **DONE** -- TOC now includes Sections 14-21.
4. **Fix CV4**: ~~Clarify "<1.2GB startup peak"~~ **DONE** -- All instances clarified to "<1.2GB peak during streaming load initialization (steady-state RSS: ~3.14GB)" across Sections 7, 15, 16.2, 16.5, M3.
5. **Fix CV5**: ~~Consolidate risk numbering.~~ **DONE** -- Section 9 uses sequential R1-R12 with eliminated risks struck through.
6. **Fix CV6, CV7**: ~~Update Section 10.2 file descriptions.~~ **DONE** -- Phase 1 updated to match Section 18.4 (8 files), Phase 3/4 rescoped to Multi-Model Weight Manager and Auto-Configuration.
7. **Fix CV8-CV11**: ~~Address medium-severity inconsistencies.~~ **DONE** -- CV8 (Section 4.1 duration), CV9 (Section 3.4 status markers), CV10 (Section 11 program metrics), CV11 (Section 11 Route B memory note) all resolved.

---

*Coherence verification complete by Taylor Kim, Senior Quality Management Specialist. Document coherence rated 7/10 -- architecturally sound with targeted fixes needed in risk register, success metrics, and documentation hygiene.*

---

## 20. Testing Strategy Update - Route B

> **Date**: 2026-04-30
> **Author**: Morgan Rodriguez, Senior QA Engineer & Test Automation Architect
> **Trigger**: Route B confirmed as primary architecture (D12). Route C deprioritized (D13). Multi-model required (D14). Resident embedding + LM head (D15). KV paging for S > 16K (D16). Quantization optional (D17).
> **Source**: Updated from `C:\Users\antmi\IRON\iron\model_convert\streaming_test_strategy.md`

---

### 20.1 Executive Summary of Changes

The original testing strategy (`streaming_test_strategy.md`) was written before user decisions confirmed Route B. It assumed a multi-route architecture where Route C (disk streaming per forward pass) was a viable path. The Route B confirmation fundamentally changes what needs to be tested.

**Key changes**:
- **REMOVED**: 58 tests related to disk streaming, page_in/page_out, weight load/unload per forward pass, Route C weight cache, Route E adaptive selector
- **ADDED**: 43 tests for multi-model chunk switching, GIL behavior validation, unified memory bandwidth, resident weight stability, KV paging
- **UPDATED**: Acceptance criteria to reflect Route B metrics (not Route C)
- **UPDATED**: Mocking strategy to reflect resident weights (no per-forward-pass weight I/O)
- **NET**: ~205 tests (down from ~220, but higher value density -- every test targets Route B reality)

---

### 20.2 Test Count Changes

#### Tests Removed (58 total)

| Category | Tests Removed | Reason |
|----------|--------------|--------|
| **RuntimeStreaming (Route C)** | U100-U104 (5 tests) | Route C deprioritized. No per-forward-pass page_in/page_out. |
| **WeightCache (Route C)** | U105-U113 (9 tests) | Route C LRU weight cache irrelevant. Weights stay resident. |
| **AdaptiveSelector (Route E)** | U114-U125 (12 tests) | Route E simplified to config selection, not route selection. Multi-strategy selector eliminated. |
| **StreamingLoad per-pass I/O** | U82-U90 (9 tests) | Weight load/unload per forward pass invalidated by Q3. Resident weights only. |
| **Disk I/O integration tests** | I8-I13 partial (6 tests) | DMA overlap tests based on disk streaming eliminated. Async KV overlap tests retained but re-scoped. |
| **Route C performance benchmarks** | P5-P7, P10 (4 tests) | Benchmarks comparing Route C vs baseline eliminated. |
| **Route C acceptance criteria** | AC21-AC26 (6 criteria) | Phase 3 Route C metrics replaced with Multi-Model Weight Manager criteria. |
| **Storage speed tests** | U90 storage speed gate (1 test) | No disk I/O at runtime means no storage speed gate needed. |
| **Selector boundary tests** | U119-U121 boundary tests (3 tests) | No route selection means no boundary testing between routes. |
| **Route C regression** | R25 weight cache test (1 test) | Route C cache hit rate regression eliminated. |
| **Route C fallback tests** | U104 unified memory fallback (2 tests) | Route C fallback to mmap eliminated. |

#### Tests Added (43 total)

| Category | Tests Added | Purpose |
|----------|------------|---------|
| **GIL Behavior Validation** | G1-G8 (8 tests) | Validate that NPU compute releases GIL, async KV can run concurrently, multiprocessing fallback works |
| **Multi-Model Chunk Switching** | M1-M12 (12 tests) | Test model activation/deactivation, KV partitioning, shared BufferRegistry, switching latency |
| **Unified Memory Bandwidth** | B1-B6 (6 tests) | Measure and validate RAM-to-NPU bandwidth, concurrent mmap limits, bandwidth scaling with chunk size |
| **Resident Weight Stability** | R27-R31 (5 tests) | Validate weights stay resident during inference, no unexpected pageouts, OS page cache behavior |
| **KV Paging (S > 16K)** | K1-K6 (6 tests) | Test KV cache eviction, paging latency, intelligent eviction policy, sync fallback |
| **Memory Reality Validation** | MR1-MR4 (4 tests) | Validate ~3.14GB RSS for 1B model, multi-model RSS scaling, no false memory reduction claims |
| **Quantization Compatibility** | Q1-Q2 (2 tests) | Ensure architecture is quantization-compatible without requiring it (optional path) |

---

### 20.3 Updated Test Inventory

| Category | Test Count | Runs When | Pass Required For |
|----------|-----------|-----------|-------------------|
| Unit tests | ~125 | Every push/PR | Merge to main |
| Integration tests | ~25 | Every push/PR | Merge to main |
| Performance benchmarks | ~12 | Weekly schedule | Regression alert only |
| Regression tests | ~28 | Every push/PR | Merge to main |
| GIL validation tests | ~8 | Phase 0 spike + weekly | Async KV viability |
| Multi-model tests | ~12 | Phase 2 + weekly | Multi-model support |
| **Total** | **~210 tests** | | |

---

### 20.4 Updated Unit Tests (Route B Focus)

#### 20.4.1 AsyncKVCache -- Extended with Paging (U1-U30 + K1-K6)

Existing tests U1-U30 remain valid. **ADDITIONS for KV paging (D16)**:

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| K1 | `test_kv_cache_paging_init_threshold()` | Paging activates when `current_seq_len > kv_paging_threshold` (default 16384) |
| K2 | `test_kv_cache_paging_eviction_oldest()` | Evicts oldest tokens first (FIFO) when memory pressure exceeds threshold |
| K3 | `test_kv_cache_paging_eviction_lru()` | LRU eviction policy: least-recently-accessed tokens evicted first |
| K4 | `test_kv_cache_paging_latency_budget()` | Paging operation completes within <5% of compute latency budget (per AC) |
| K5 | `test_kv_cache_paging_sync_fallback()` | When paging fails, falls back to synchronous KV update without data corruption |
| K6 | `test_kv_cache_paging_128k_context()` | Handles S=131072 with paging enabled; RSS stays within configured budget |

#### 20.4.2 BufferRegistry (U31-U55) -- No Changes

All existing tests remain valid. BufferRegistry is independent of routing decisions.

#### 20.4.3 ChunkManager -- Extended with Multi-Model (U56-U81 + M1-M12)

Existing tests U56-U81 remain valid. **ADDITIONS for multi-model (D14)**:

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| M1 | `test_chunk_manager_multi_model_init()` | Initialize with multiple model manifests simultaneously |
| M2 | `test_chunk_manager_model_activation()` | `activate_model(model_id)` sets active model, deactivates previous |
| M3 | `test_chunk_manager_model_deactivation()` | `deactivate_model(model_id)` clears active chunks for that model |
| M4 | `test_chunk_manager_model_switching_latency()` | Model switch (deactivate A + activate B) completes within <100ms |
| M5 | `test_chunk_manager_model_isolation()` | Activating Model B does not corrupt Model A's chunk state |
| M6 | `test_chunk_manager_shared_kv_partitioning()` | KV cache correctly partitioned between active models |
| M7 | `test_chunk_manager_shared_buffer_registry()` | BufferRegistry correctly reused between models (no reallocation) |
| M8 | `test_chunk_manager_model_manifest_switch()` | Switching model loads correct manifest, correct block mapping |
| M9 | `test_chunk_manager_concurrent_model_requests()` | Sequential model inference requests don't interfere (no parallel execution) |
| M10 | `test_chunk_manager_model_state_preservation()` | KV cache state preserved when switching back to previously active model |
| M11 | `test_chunk_manager_model_resource_cleanup()` | Deactivating model cleans up KV partitions, frees activation buffers |
| M12 | `test_chunk_manager_three_model_rotation()` | Rotate through 3 models: A->B->C->A; each switch <100ms, state preserved |

#### 20.4.4 GIL Behavior Validation (NEW -- G1-G8)

**CRITICAL**: These tests validate R9 (Python GIL risk). If these fail, the async KV premise is invalidated.

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| G1 | `test_gil_npu_compute_releases()` | NPU compute call releases GIL (verified by concurrent numpy ops completing during compute) |
| G2 | `test_gil_kv_async_thread_unblocked()` | KV async merge thread can execute numpy ops while NPU compute is running |
| G3 | `test_gil_concurrent_compute_kv()` | Compute thread and KV merge thread achieve >80% temporal overlap |
| G4 | `test_gil_threading_overhead()` | Threading overhead <5% of total inference time (context switching doesn't negate async benefit) |
| G5 | `test_gil_multiprocessing_fallback()` | If threading fails (GIL held), multiprocessing fallback achieves async KV with shared memory |
| G6 | `test_gil_multiprocessing_serialization()` | Multiprocessing serialization overhead measured; acceptable if <10ms per chunk switch |
| G7 | `test_gil_blocking_calls_mapped()` | All NPU driver calls cataloged: which hold GIL, which release it. `submit()` MUST release. |
| G8 | `test_gil_process_pool_executor()` | `ProcessPoolExecutor` achieves desired overlap; shared memory buffer passing works correctly |

#### 20.4.5 ChunkedInference -- Updated (U91-U99, modified)

| # | Test Function | What It Verifies | Route B Change |
|---|--------------|------------------|----------------|
| U91 | `test_chunked_inference_init()` | Init with ChunkManager, KVCache, BufferRegistry, resident weights | Updated: no streaming_load dependency |
| U92 | `test_chunked_inference_single_chunk_forward()` | Single chunk forward produces correct output shape | Unchanged |
| U93 | `test_chunked_inference_multi_chunk_forward()` | Multi-chunk chains: output of chunk N = input to chunk N+1 | Unchanged |
| U94 | `test_chunked_inference_async_kv_between_chunks()` | Async KV merge scheduled after chunk, completes before next chunk needs it | Unchanged |
| U95 | `test_chunked_inference_hidden_state_passthrough()` | hidden_states passed between chunks without mutation | Unchanged |
| U96 | `test_chunked_inference_decode_mode()` | Decode (T=1) produces `[1, 1, vocab_size]` output | Unchanged |
| U97 | `test_chunked_inference_prefill_mode()` | Prefill (T=prompt_len) produces `[1, T, vocab_size]` output | Unchanged |
| U98 | `test_chunked_inference_eos_termination()` | Generation stops at EOS token (mocked sampling) | Unchanged |
| U99 | `test_chunked_inference_max_tokens_termination()` | Generation stops at `max_tokens` limit | Unchanged |
| **U91b** | `test_chunked_inference_resident_weights()` | Weights are resident at inference time; no weight load during forward pass | NEW: Route B specific |
| **U91c** | `test_chunked_inference_no_disk_io()` | Zero disk reads during inference (weights mmap'd, not streamed) | NEW: Route B specific |

#### 20.4.6 Unified Memory Bandwidth Tests (NEW -- B1-B6)

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| B1 | `test_unified_memory_bandwidth_baseline()` | RAM-to-NPU bandwidth >= expected baseline (measured in Phase 0) |
| B2 | `test_unified_memory_concurrent_mmap_limits()` | Concurrent mmap regions supported up to N limit (measured in Phase 0) |
| B3 | `test_unified_memory_bandwidth_chunk_size()` | Bandwidth consistent across chunk sizes (1, 2, 3, 4, 8 blocks) |
| B4 | `test_unified_memory_multi_model_bandwidth()` | Bandwidth maintained during multi-model chunk switching |
| B5 | `test_unified_memory_page_cache_behavior()` | OS page cache hits >99% for resident weights during inference |
| B6 | `test_unified_memory_alignment_requirements()` | NPU-accessible buffers meet alignment requirements (4096-byte or driver-specific) |

#### 20.4.7 Resident Weight Stability Tests (NEW -- R27-R31)

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| R27 | `test_resident_weights_no_pageouts()` | Weights remain resident during inference; <1% page fault rate |
| R28 | `test_resident_weights_memory_pressure()` | Under system memory pressure, OS reclaims pages gracefully (no crash) |
| R29 | `test_resident_weights_os_page_cache()` | OS page cache correctly serves repeated weight accesses (hit rate >99%) |
| R30 | `test_resident_weights_windows_behavior()` | Windows 11 mmap behavior under pressure: pages reclaimable, re-accessible |
| R31 | `test_resident_weights_mmap_lazy_loading()` | Initial mmap lazy loading: first access triggers page-in, subsequent accesses hit cache |

#### 20.4.8 Memory Reality Validation (NEW -- MR1-MR4)

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| MR1 | `test_memory_rss_single_model_1b()` | Steady-state RSS for 1B model at S=4096 = ~3.14GB (within 5% tolerance) |
| MR2 | `test_memory_rss_multi_model_2x_1b()` | RSS for two 1B models at S=4096 = ~6.28GB (within 5% tolerance) |
| MR3 | `test_memory_virtual_vs_rss()` | Virtual memory ~3.14GB, RSS varies by OS page cache; both tracked and reported |
| MR4 | `test_memory_no_false_reduction_claims()` | Test explicitly validates that Route B does NOT claim RSS reduction vs current architecture |

#### 20.4.9 Quantization Compatibility Tests (NEW -- Q1-Q2)

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| Q1 | `test_quantization_fp16_compatibility()` | Architecture works correctly with FP16 weights (baseline, no quantization) |
| Q2 | `test_quantization_int8_optional_path()` | INT8 weights can be loaded without architectural changes (compatibility, not requirement) |

---

### 20.5 Updated Integration Tests

#### 20.5.1 Chunked Inference Without NPU (I1-I7, modified)

| # | Test Function | What It Verifies | Route B Change |
|---|--------------|------------------|----------------|
| I1 | `test_chunked_inference_full_prefill()` | Tokenize -> embed -> chunk0..N -> LM head -> logits | Unchanged |
| I2 | `test_chunked_inference_full_decode()` | Single token -> chunk0..N -> LM head -> sample | Unchanged |
| I3 | `test_chunked_inference_multi_token_generation()` | Generate 10 tokens; each step shape-correct, KV cache grows | Unchanged |
| I4 | `test_chunked_inference_kv_merge_timing()` | Async KV merge completes before next chunk starts | Unchanged |
| I5 | `test_chunked_inference_attention_mask_applied()` | Causal mask correctly applied across all chunks | Unchanged |
| I6 | `test_chunked_inference_position_ids_increment()` | Position IDs increment correctly across decode steps | Unchanged |
| I7 | `test_chunked_inference_chunk_boundary_correctness()` | Hidden state at chunk boundary matches monolithic execution | Unchanged |

#### 20.5.2 Async KV Overlap Measurement (I8-I13, re-scoped)

Tests I8-I13 remain but are **re-scoped from disk DMA to memory bandwidth**:

| # | Test Function | What It Verifies | Route B Change |
|---|--------------|------------------|----------------|
| I8 | `test_kv_overlap_compute_dominant()` | compute=50ms, memory_transfer=5ms -> overlap >80% | Changed from "DMA" to "memory transfer" |
| I9 | `test_kv_overlap_memory_dominant()` | compute=10ms, memory_transfer=20ms -> partial overlap | Changed from DMA-dominant to memory-dominant |
| I10 | `test_kv_overlap_async_advantage()` | Async overlap > sync execution (same config) | Unchanged logic |
| I11 | `test_kv_overlap_varying_seq_lengths()` | Overlap at S=1, S=100, S=1000, S=4096 | Unchanged |
| I12 | `test_kv_overlap_chunk_boundaries()` | Overlap maintained across chunk boundaries | Unchanged |
| I13 | `test_kv_overlap_apple_pattern()` | Apple's async KV merge pattern: 1 chunk's worth of future time | Unchanged |

#### 20.5.3 Cross-Component Integration (I14-I17, updated)

| # | Test Function | What It Verifies | Route B Change |
|---|--------------|------------------|----------------|
| I14 | `test_registry_chunk_manager_lifecycle()` | Full lifecycle: allocate -> activate chunk -> forward -> deactivate -> next | Unchanged |
| I15 | `test_registry_buffer_reuse_across_chunks()` | hidden_states buffer reused across all chunks | Unchanged |
| **I16** | `test_resident_weights_inference()` | Weights resident at startup, no load during inference, correct output | **REPLACES** old I16 (streaming load + inference) |
| **I17** | `test_multi_model_chunk_switching()` | Switch between Model A and Model B during inference; both produce correct output | **REPLACES** old I17 (KV cache with varying chunks) |

#### 20.5.4 Multi-Model Integration Tests (NEW -- I18-I25)

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| I18 | `test_multi_model_full_pipeline()` | Full inference: Model A (5 tokens) -> switch -> Model B (5 tokens) -> correct output |
| I19 | `test_multi_model_kv_partition_isolation()` | KV cache partitions don't bleed between models |
| I20 | `test_multi_model_shared_registry_no_corruption()` | Shared BufferRegistry correctly isolates model activation buffers |
| I21 | `test_multi_model_rss_during_switch()` | RSS tracked during model switch; no unexpected memory spike |
| I22 | `test_multi_model_three_way_rotation()` | Rotate A->B->C->A; each inference correct, KV state preserved |
| I23 | `test_multi_model_concurrent_requests_sequential()` | Two model inference requests processed sequentially (not parallel); isolation verified |
| I24 | `test_multi_model_model_a_b_b_a()` | Switch A->B->B->A; returning to A produces same result as if B never ran |
| I25 | `test_multi_model_memory_pressure_handling()` | Under memory pressure, system gracefully degrades (model unload, not crash) |

---

### 20.6 Updated Performance Tests

#### 20.6.1 Chunk Size Tuning Benchmarks (P1-P4, updated)

| # | Benchmark Function | What It Measures | Success Criterion |
|---|-------------------|-----------------|-------------------|
| P1 | `benchmark_chunk_size_comparison()` | tokens/sec, RSS, overlap% for sizes [1,2,3,4,8] | Optimal size identified (within 10% of best) |
| P2 | `benchmark_chunk_activation_overhead()` | Time to activate chunk (NPU reconfig) per size | Overhead <5% of total inference time |
| P3 | `benchmark_chunk_memory_footprint()` | Peak RSS during prefill/decode per size | RSS consistent across chunk sizes (weights resident) |
| P4 | `benchmark_chunk_kv_merge_frequency()` | KV merge count per forward pass per size | Matches expected: `num_chunks = ceil(num_blocks / chunk_size)` |

#### 20.6.2 Async KV Overlap Efficiency (P5-P7, re-scoped)

| # | Benchmark Function | What It Measures | Success Criterion |
|---|-------------------|-----------------|-------------------|
| P5 | `benchmark_overlap_timeline()` | Precise timestamps of compute vs memory transfer operations | >80% memory transfer time overlaps with compute |
| P6 | `benchmark_overlap_varying_bandwidths()` | Overlap at different unified memory bandwidths (measured Phase 0) | High bandwidth: >80%, Medium: >50% |
| P7 | `benchmark_overlap_with_resident_weights()` | Overlap with resident weights vs lazy-loaded weights | Resident: consistent overlap; Lazy: first-access penalty measured |

#### 20.6.3 Baseline Comparison (P8-P12, updated for Route B)

| # | Benchmark Function | What It Compares | Success Criterion |
|---|-------------------|-----------------|-------------------|
| P8 | `benchmark_chunked_vs_monolithic()` | Route B vs current monolithic architecture | Route B >= 1.1x tokens/sec (async KV advantage) |
| P9 | `benchmark_before_after_kv_async()` | With async KV vs sync KV | Async KV >= 1.05x throughput |
| **P10** | `benchmark_multi_model_switching_overhead()` | Single model vs multi-model switching overhead | Switching overhead <10% of total inference time |
| P11 | `benchmark_ttft_comparison()` | Time-to-first-token: chunked vs monolithic | Chunked TTFT within 20% of monolithic |
| P12 | `benchmark_decode_latency_per_token()` | Per-token decode latency across 100 tokens | p95 latency < 2x mean latency |

#### 20.6.4 Multi-Model Benchmarks (NEW -- P13-P15)

| # | Benchmark Function | What It Measures | Success Criterion |
|---|-------------------|-----------------|-------------------|
| P13 | `benchmark_model_switch_latency()` | Time to deactivate Model A + activate Model B | <100ms for 1B model, <200ms for 7B model |
| P14 | `benchmark_multi_model_rss_scaling()` | RSS with 1, 2, 3 models loaded simultaneously | Linear scaling (2x model = ~2x RSS) |
| P15 | `benchmark_kv_paging_overhead()` | Latency with KV paging enabled (S > 16K) vs disabled | Paging overhead <5% latency increase |

---

### 20.7 Updated Regression Tests

#### 20.7.1 Feature Flag Testing (R1-R8) -- No Changes

All existing feature flag tests remain valid.

#### 20.7.2 Output Parity Tests (R9-R14) -- No Changes

All existing output parity tests remain valid.

#### 20.7.3 Cross-Platform Testing (R15-R20, updated)

| # | Test Function | What It Verifies | Route B Change |
|---|--------------|------------------|----------------|
| R15 | `test_windows_mmap_behavior()` | mmap works correctly on Windows NTFS for large resident weight files | Updated: focus on large-file behavior (1GB+) |
| R16 | `test_path_handling_windows()` | pathlib.Path handles Windows backslash paths correctly | Unchanged |
| R17 | `test_memory_available_windows()` | psutil.virtual_memory() works on Windows, correct RSS measurement | Unchanged |
| **R18** | `test_windows_page_cache_pressure()` | Windows page cache behavior under memory pressure for mmap'd weights | **REPLACES** old R18 (file locking) |
| R19 | `test_conftest_platform_auto_detect()` | conftest.py auto-detects platform, adjusts test parameters | Unchanged |
| R20 | `test_conftest_npu_skip_auto()` | Tests marked requires_npu auto-skipped on non-NPU platforms | Unchanged |

#### 20.7.4 Dependency Compatibility (R21-R23) -- No Changes

#### 20.7.5 Migration/Upgrade Compatibility (R24-R26, updated)

| # | Test Function | What It Verifies | Route B Change |
|---|--------------|------------------|----------------|
| R24 | `test_model_weights_backward_compat()` | New streaming code reads existing .npy files without modification | Unchanged |
| R25 | `test_manifest_backward_compat()` | New manifest.json format compatible with existing weight files | Unchanged |
| **R26** | `test_config_migration_streaming_section()` | Existing configs work with new streaming section added (chunk_size, kv_paging_threshold, streaming_mode) | Updated: removed streaming_load references |

#### 20.7.6 GIL Regression Tests (NEW -- R32-R35)

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| R32 | `test_gil_behavior_no_regression()` | GIL behavior consistent across Python versions (3.10, 3.11, 3.12) |
| R33 | `test_gil_threading_stability()` | Async KV threading stable over 1000+ inference iterations |
| R34 | `test_gil_multiprocessing_consistency()` | Multiprocessing fallback produces identical results to threading mode |
| R35 | `test_gil_python_version_compatibility()` | GIL behavior consistent across Python 3.10-3.12 (no version-specific breaks) |

---

### 20.8 Updated Mocking Strategy

The Route B confirmation changes the mocking approach significantly. Weights are resident, not streamed.

| Layer | What Is Mocked | How | Why | Route B Change |
|-------|---------------|-----|-----|----------------|
| **NPU Compute** | GEMM, Norm, RoPE, Attention operators | `FakeNPUComputeEngine`: numpy matmul + elementwise ops | Deterministic results, configurable delays | **UNCHANGED** -- compute mocking is route-agnostic |
| **NPU Driver** | Unified memory access, buffer submission | `FakeUnifiedMemoryDriver`: in-memory buffer management with configurable latency | Test memory transfer paths, bandwidth simulation | **CHANGED** from `FakeNpuDriver` (page_in/page_out) to unified memory model |
| **Memory** | RSS tracking, available RAM | `tracemalloc` + `unittest.mock.patch` with controlled values | Cross-platform consistency, test extreme scenarios | **ENHANCED** to track resident weight RSS (~3.14GB baseline) |
| **File I/O** | .npy weight file reads (startup only) | Small dummy .npy files via `tmp_path` fixture | Fast tests, no large file dependencies | **CHANGED** -- weights loaded once at startup, not per forward pass |
| **Disk Speed** | No longer relevant | N/A | No disk I/O at runtime | **REMOVED** -- Route B has zero runtime disk reads |
| **Async Operations** | Memory transfer + KV merge | `threading.Event` + `concurrent.futures` + optional `multiprocessing` | Test non-blocking behavior, GIL interactions | **ENHANCED** with GIL-aware mocking (`release_gil=True/False`) |
| **Token Sampling** | Next token selection | Deterministic argmax or fixed token sequence | Reproducible test results | **UNCHANGED** |
| **System Info** | `psutil.virtual_memory()`, disk info | `unittest.mock.patch` with controlled return values | Test memory pressure scenarios | **ENHANCED** to simulate multi-model RSS scenarios |
| **GIL Behavior** | GIL release/hold during NPU compute | `FakeNPUComputeEngine(release_gil=True/False)` | Test async KV under both GIL scenarios | **NEW** -- critical for R9 validation |
| **Multi-Model** | Model switching, KV partitioning | Multiple `FakeNPUComputeEngine` instances with model-specific configs | Test chunk activation switching | **NEW** -- multi-model requirement |

#### Updated FakeNPUComputeEngine Design

```python
class FakeNPUComputeEngine:
    """Numpy-based NPU emulation for Route B testing without hardware.
    
    Route B specific: weights are resident (loaded once at startup),
    no per-forward-pass weight I/O. Supports GIL behavior testing.
    """

    def __init__(
        self,
        config,
        compute_delay_ms: float = 0,
        memory_transfer_delay_ms: float = 0,
        release_gil: bool = True,  # NEW: test GIL behavior
        model_id: str = "default",  # NEW: multi-model support
    ):
        self.config = config
        self.compute_delay_ms = compute_delay_ms
        self.memory_transfer_delay_ms = memory_transfer_delay_ms
        self.release_gil = release_gil
        self.model_id = model_id
        self.timeline = []
        self._resident_weights = {}  # Route B: weights loaded once

    def load_weights(self, weight_files: list[str]):
        """Route B: Load weights once at startup. Stays resident."""
        for f in weight_files:
            self._resident_weights[f] = np.load(f)

    def compute(self, op_name: str, inputs: dict) -> np.ndarray:
        """Execute fake NPU operation with optional GIL release simulation."""
        if self.release_gil:
            # Simulate GIL release: other threads can run concurrently
            self._simulate_gil_release()
        time.sleep(self.compute_delay_ms / 1000)
        self.timeline.append((op_name, time.monotonic(), self.model_id))
        return self._execute_op(op_name, inputs)

    def _simulate_gil_release(self):
        """If release_gil=True, use mechanism that allows concurrent execution."""
        pass  # In real driver, this would be Py_BEGIN_ALLOW_THREADS

    def memory_transfer(self, data: np.ndarray, direction: str = "read"):
        """Simulate unified memory transfer (not disk I/O)."""
        size_bytes = data.nbytes
        delay = (size_bytes / (20 * 1024**3)) + (self.memory_transfer_delay_ms / 1000)
        time.sleep(delay)
        self.timeline.append(("mem_transfer", time.monotonic(), direction, size_bytes))
        return data.copy()
```

---

### 20.9 Updated Acceptance Criteria

#### Phase 1: Foundation (AsyncKVCache + ChunkManager + BufferRegistry + KV Paging)

| # | Criterion | Measurement | Target | Route B Change |
|---|-----------|------------|--------|----------------|
| AC1 | All 3 components implemented | Code review + API contract check | Full public APIs matching design docs | Unchanged |
| AC2 | Unit test coverage | `pytest-cov --cov=streaming` | >= 90% line coverage per component | Unchanged |
| AC3 | All unit tests pass | CI (Linux + Windows) | 0 failures, 0 errors | Unchanged |
| AC4 | Async KV overlap efficiency | Integration test `test_kv_overlap_compute_dominant()` | > 80% memory transfer hidden behind compute | Changed from "DMA" to "memory transfer" |
| AC5 | ChunkManager partitioning correctness | Parametrized tests across (blocks, chunk_size) | All combinations correct | Unchanged |
| AC6 | BufferRegistry contract enforcement | Tests for shape/dtype/alignment/contiguity | All violations caught | Unchanged |
| AC7 | No NPU hardware required | Verify all tests pass without NPU | 100% software-only | Unchanged |
| AC8 | Component interfaces stable | Interface review, no breaking changes | Signatures match design docs | Unchanged |
| AC9 | Documentation | Docstrings + usage examples | All public methods documented | Unchanged |
| AC10 | Benchmark framework operational | pytest-benchmark configured, runs | Baseline data generated | Unchanged |
| **AC11** | **KV paging functional** | Tests K1-K6 all pass | Paging at S > 16K, <5% latency overhead | **NEW** (D16) |
| **AC12** | **GIL behavior validated** | Tests G1-G4 all pass | GIL released OR multiprocessing fallback works | **NEW** (R9) |

#### Phase 2: Route B (Chunked Inference) + Multi-Model

| # | Criterion | Measurement | Target | Route B Change |
|---|-----------|------------|--------|----------------|
| AC13 | Route B throughput | Tokens/sec vs monolithic baseline | >= 1.1x baseline | Unchanged |
| AC14 | NPU compilation overhead | Timing mocked chunk compilation | < 500ms per chunk | Unchanged |
| AC15 | Feature flag preservation | Regression tests R1-R8 | All pass | Unchanged |
| AC16 | Output parity | Regression tests R9-R14 | All pass (tolerance: atol=1e-3) | Unchanged |
| AC17 | Chunked inference e2e | Integration tests I1-I7 | All pass | Unchanged |
| AC18 | Async KV merge e2e | Integration tests I8-I13 | All pass | Unchanged |
| AC19 | CLI entry point functional | `streaming_infer.py --help`, `--config`, `--model` | Correct output | Unchanged |
| AC20 | Cross-platform (Windows 11) | Regression tests R15-R20 | All pass | Unchanged |
| AC21 | Performance baselines stored | Benchmark output JSON files | Created and committed | Unchanged |
| **AC22** | **Multi-model chunk switching** | Tests M1-M12, I18-I25 | All pass; switch latency < 100ms | **NEW** (D14) |
| **AC23** | **Resident weight stability** | Tests R27-R31 | < 1% page fault rate during inference | **NEW** (D3) |
| **AC24** | **RSS reality validation** | Tests MR1-MR4 | RSS = ~3.14GB for 1B model (within 5%) | **NEW** (memory honesty) |
| **AC25** | **Startup initialization peak** | tracemalloc during resident load | < 1.2GB peak during load init (steady-state: ~3.14GB) | **UPDATED** (clarified: init peak vs steady-state) |
| **AC26** | **Unified memory bandwidth** | Tests B1-B6 | Bandwidth meets Phase 0 baseline | **NEW** (Phase 0 validation) |

#### Phase 3: Multi-Model Weight Manager (Rescoped from Route C)

| # | Criterion | Measurement | Target | Route B Change |
|---|-----------|------------|--------|----------------|
| **AC27** | **Memory pressure monitoring** | RSS monitoring during multi-model inference | Detects pressure within 100ms | **NEW** (replaces Route C criteria) |
| **AC28** | **Model load/unload lifecycle** | Clean model switching, KV cleanup | < 200ms full model unload + reload | **NEW** (replaces Route C criteria) |
| **AC29** | **Graceful degradation** | Under memory pressure, system degrades without crash | Auto-unload least-used model, no data loss | **NEW** (replaces Route C criteria) |
| **AC30** | **Multi-model RSS management** | 2x 1B models RSS < 7GB on 16GB system | RSS within expected range, no OS paging thrashing | **NEW** (replaces Route C criteria) |
| **AC31** | **Page cache hit rate** | OS page cache monitoring during inference | > 99% hit rate for resident weights | **NEW** (replaces Route C criteria) |

#### Phase 4: Auto-Configuration (Rescoped from Route E)

| # | Criterion | Measurement | Target | Route B Change |
|---|-----------|------------|--------|----------------|
| **AC32** | **Chunk size auto-selection** | Hardware detection -> optimal chunk size | > 95% correct across test matrix | **UPDATED** (was route selection) |
| **AC33** | **KV cache auto-sizing** | Based on available RAM and expected context | Optimal size within 10% of manual tuning | **UPDATED** (was strategy selection) |
| **AC34** | **KV paging threshold auto-config** | Based on available memory | Correct threshold within 2K tokens | **NEW** |
| **AC35** | **Multi-model concurrency auto-limit** | Based on RAM capacity | Correct max models within 1 of optimal | **NEW** |

---

### 20.10 Updated Test Directory Structure

```
C:\Users\antmi\IRON\iron\model_convert\streaming\tests\
  conftest.py                          # Shared fixtures (updated for Route B)
  __init__.py
  unit/
    test_async_kv_cache.py             # Tests U1-U30 + K1-K6 (paging)
    test_buffer_registry.py            # Tests U31-U55 (unchanged)
    test_chunk_manager.py              # Tests U56-U81 + M1-M12 (multi-model)
    test_chunked_inference.py          # Tests U91-U99 + U91b, U91c (resident weights)
    test_gil_behavior.py               # Tests G1-G8 (NEW - critical)
    test_unified_memory.py             # Tests B1-B6 (NEW)
    test_resident_weights.py           # Tests R27-R31 (NEW)
    test_memory_reality.py             # Tests MR1-MR4 (NEW)
    test_quantization_compat.py        # Tests Q1-Q2 (NEW - optional)
  integration/
    test_chunked_inference_e2e.py      # Tests I1-I7
    test_kv_overlap_efficiency.py      # Tests I8-I13 (re-scoped)
    test_cross_component.py            # Tests I14-I17 (updated)
    test_multi_model.py                # Tests I18-I25 (NEW)
  performance/
    test_chunk_size_benchmarks.py      # Benchmarks P1-P4
    test_overlap_benchmarks.py         # Benchmarks P5-P7 (re-scoped)
    test_baseline_comparison.py        # Benchmarks P8-P12 (updated)
    test_multi_model_benchmarks.py     # Benchmarks P13-P15 (NEW)
  regression/
    test_feature_flags.py              # Tests R1-R8
    test_output_parity.py              # Tests R9-R14
    test_cross_platform.py             # Tests R15-R20 (updated)
    test_dependency_compat.py          # Tests R21-R23
    test_backward_compat.py            # Tests R24-R26 (updated)
    test_gil_regression.py             # Tests R32-R35 (NEW)
  mocks/
    fake_compute_engine.py             # FakeNPUComputeEngine (updated for Route B + GIL)
    fake_unified_memory_driver.py      # FakeUnifiedMemoryDriver (NEW, replaces fake_npu_driver)
    test_data_factory.py               # Deterministic test data generators
```

---

### 20.11 Test Execution Summary (Route B)

| Phase | Tests to Add | Est. Time to Write | Est. Time to Run (CI) | Route B Change |
|-------|-------------|-------------------|----------------------|----------------|
| Phase 0 | ~8 GIL + bandwidth tests | 1 week | ~15 seconds | NEW (critical spike) |
| Phase 1 | ~75 unit tests (U1-U81, K1-K6, B1-B6, R27-R31) | 2-3 weeks | ~25 seconds (parallel) | Added paging + resident weight tests |
| Phase 2 | ~40 unit + ~17 integration tests (U91-U99, M1-M12, I1-I25) | 3 weeks | ~45 seconds | Added multi-model tests |
| Phase 3 | ~15 integration + memory pressure tests | 2 weeks | ~20 seconds | Rescoped from Route C |
| Phase 4 | ~10 auto-config tests | 1 week | ~10 seconds | Rescoped from Route E |
| Regression | ~33 regression tests (R1-R35) | 1 week (parallel) | ~40 seconds | Updated, added GIL regression |
| Performance | ~15 benchmarks (P1-P15) | 1 week | ~5 minutes (weekly) | Updated, removed Route C, added multi-model |
| **Total** | **~210 tests** | **~11 weeks** | **~2.5 minutes (per push)** | Down from 220, higher value density |

---

### 20.12 Risk Mitigation Through Testing (Updated)

| Architecture Risk | How Testing Mitigates It | Route B Change |
|------------------|-------------------------|----------------|
| R3: Integration breaks existing functionality | Tests R1-R14 (feature flags + output parity) run on every PR | Unchanged |
| R4: Chunk size suboptimal for AIE | Benchmarks P1-P4 systematically test sizes 1/2/3/4/8 | Unchanged |
| R5: Windows memory management differences | Tests R15-R20 specifically validate Windows mmap, page cache under pressure | **ENHANCED** -- focus on large-file mmap behavior |
| R6: Memory transfer timing variance | Tests I8-I13 measure overlap across simulated bandwidths | Changed from "DMA" to "memory transfer" |
| R8: KV cache paging latency spikes | Tests K1-K6 validate paging latency budget, sync fallback | Unchanged |
| **R9: Python GIL invalidates async KV** | **Tests G1-G8 validate GIL behavior; multiprocessing fallback tested** | **NEW -- critical, addressed explicitly** |
| **R10: Multi-model RAM pressure** | **Tests MR1-MR4, I21, I25 validate RSS scaling and graceful degradation** | **NEW -- multi-model requirement** |
| **NEW: Resident weight stability** | **Tests R27-R31 validate <1% page fault rate, OS page cache behavior** | **NEW -- Route B resident weights** |
| **NEW: Memory honesty** | **Tests MR1-MR4 explicitly validate ~3.14GB RSS (no false reduction claims)** | **NEW -- stakeholder expectation management** |

---

### 20.13 Key Changes Summary

**Removed from test strategy**:
- Route C disk streaming tests (page_in/page_out, weight load/unload per forward pass): 23 tests
- Route E adaptive selector tests (strategy selection, boundary conditions): 12 tests
- Route C weight cache tests (LRU eviction, hit rate tracking): 9 tests
- Storage speed gate tests (NVMe/SATA/HDD throughput): 4 tests
- Route C performance benchmarks (storage-dependent overlap): 4 tests
- Route C regression tests (cache hit rate, weight cache): 2 tests
- Route C acceptance criteria (AC21-AC26): 6 criteria

**Added to test strategy**:
- GIL behavior validation tests (G1-G8): 8 tests
- Multi-model chunk switching tests (M1-M12): 12 tests
- Unified memory bandwidth tests (B1-B6): 6 tests
- Resident weight stability tests (R27-R31): 5 tests
- KV paging tests (K1-K6): 6 tests
- Memory reality validation tests (MR1-MR4): 4 tests
- Multi-model integration tests (I18-I25): 8 tests
- Multi-model benchmarks (P13-P15): 3 tests
- Quantization compatibility tests (Q1-Q2): 2 tests
- GIL regression tests (R32-R35): 4 tests
- Updated acceptance criteria (AC11-AC35): 15 criteria (replacing Route C criteria)

**Net result**: ~210 tests (down from ~220), but every test targets Route B reality. Test coverage quality increased because removed tests tested features that no longer exist, and added tests test critical Route B capabilities (GIL behavior, multi-model, memory reality).

---

*Testing strategy updated by Morgan Rodriguez, Senior QA Engineer & Test Automation Architect. All changes reflect Route B (Chunked Inference with Unified Memory) as confirmed by user decisions D12-D17. The strategy is executable without NPU hardware via FakeNPUComputeEngine with GIL-aware mocking.*

---

## 21. Planning Analysis - Pipeline Round 2

> **Date**: 2026-04-30
> **Analyst**: Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
> **Trigger**: Second pass of recursive iterative agent pipeline. Review and resolve all outstanding quality review issues (CV1-CV11) from Section 19. Produce actionable Phase 0 plan.

### 21.1 Issues Resolved in This Pass

All 11 outstanding issues from the Coherence Verification review (Section 19.2) have been addressed:

| ID | Issue | Sections Affected | Resolution |
|----|-------|-------------------|------------|
| **CV1** | GIL risk missing from Section 9 | Section 9 | Consolidated risk register with 12 sequential risks (R1-R12). GIL listed as R8 (Critical). Eliminated risks struck through. |
| **CV2** | Phase 3 metrics are Route C relics | Sections 11, 15, 16.2, 16.5 | All Phase 3 metrics replaced with Multi-Model Weight Manager targets: memory pressure detection <100ms, model unload/reload <200ms, graceful degradation, >99% page cache hit rate. |
| **CV3** | TOC missing Sections 14-20 | Section 1 (TOC) | TOC expanded to include all sections through Section 21. |
| **CV4** | "<1.2GB startup peak" ambiguous | Sections 7, 15, 16.2, 16.5, M3 | Clarified to "<1.2GB peak during streaming load initialization (steady-state RSS: ~3.14GB)" in all instances. |
| **CV5** | Risk ID collisions | Section 9 vs 16.6 | Single sequential numbering R1-R12 in Section 9. Section 16.6 references preserved for traceability. |
| **CV6** | Section 10.2 Phase 3/4 Route C relics | Section 10.2 | Phase 3 files: weight_manager.py, memory_monitor.py, model_lifecycle.py. Phase 4 files: auto_config.py. All descriptions updated. |
| **CV7** | Section 10.2 Phase 1 file list outdated | Section 10.2 | Updated to match Section 18.4: 8 files including config.py, kv_cache.py/kv_async_ops.py split, chunk_manifest.py. |
| **CV8** | Phase 1 duration inconsistency | Section 4.1 | Changed from "3-4 weeks" to "4 weeks" for consistency. |
| **CV9** | Section 3.4 legacy status markers | Section 3.4 | All C1-C3 and M1-M5 status markers updated to reflect resolution or deprecation of legacy documents. |
| **CV10** | Section 11 missing program metrics | Section 11 | Added program-level metrics: zero regression, >=90% test coverage, steady-state RSS honesty validation. |
| **CV11** | Section 11 needs Route B memory honesty | Section 11 | Added prominent note: Route B does NOT reduce steady-state RSS. "<1.2GB" refers to load initialization peak only. |

### 21.2 Document Coherence Assessment (Post-Fix)

| Section | Status | Notes |
|---------|--------|-------|
| Section 1 (TOC) | FIXED | Complete, all 21 sections listed |
| Section 3.4 (Legacy Review) | FIXED | Status markers updated, resolved/deprecated |
| Section 4.1 (Phase Status) | FIXED | Phase 1 duration consistent ("4 weeks") |
| Section 7 (Next Steps) | FIXED | Startup peak metric clarified |
| Section 9 (Risk Register) | FIXED | Consolidated, 12 sequential risks, GIL included as Critical |
| Section 10.2 (File Impact) | FIXED | All phase file descriptions match current scope |
| Section 11 (Success Metrics) | FIXED | Route C relics replaced, program metrics added, memory honesty note |
| Section 15 (Testing Summary) | FIXED | Phase 3 acceptance criteria updated |
| Section 16.2 (Phasing Table) | FIXED | Phase 3 exit criteria corrected |
| Section 16.5 (Program Criteria) | FIXED | Route C relics replaced with Weight Manager targets |
| Section 17 (Quality Review) | UNCHANGED | Historical record preserved; recommendations acted upon |
| Section 19 (Coherence Verify) | UNCHANGED | Historical record preserved; Section 19.5 priorities marked DONE |

**Coherence Rating: 9/10** (up from 7/10). All internal contradictions resolved. Document is now internally consistent and ready for Phase 0 execution.

### 21.3 What Remains Outstanding

| Item | Priority | Location | Action Required |
|------|----------|----------|-----------------|
| **Legacy doc deprecation banners** | Medium | streaming_model_concept.md, streaming_block_design.md | Add prominent banners noting these predate user decisions and Route B confirmation |
| **C1 (KV DMA sizes in block design)** | Low (legacy doc) | streaming_block_design.md Section 4.2 | Numbers corrected in STREAMING_PROGRESS.md; legacy doc can be updated separately with deprecation banner |
| **C3 (116MB vs 121MB in legacy docs)** | Low (legacy doc) | streaming_model_concept.md, streaming_block_design.md | STREAMING_PROGRESS.md uses correct 121MB; legacy docs deprecated |
| **Phase 0 execution** | **CRITICAL** | N/A | Execute the unified memory validation spike (see 21.4) |

### 21.4 Phase 0 Plan - Actionable Execution Guide

**Phase 0: Unified Memory Validation Spike** (Week 1)

**Owner**: Senior engineer with NPU driver and Windows memory management experience

**Objective**: Validate that the AMD NPU unified memory model supports Route B's chunked inference architecture on Windows 11.

**Spike Deliverables**: A written report with empirical measurements answering these 5 questions:

#### Spike Task 1: Unified Memory Bandwidth Measurement
- **What**: Measure RAM-to-NPU bandwidth for chunked weight access patterns
- **How**: Load individual block weights via mmap, submit to NPU, measure throughput
- **Success Criterion**: Bandwidth sufficient for chunk switching within <5% of compute time
- **Tools**: `perf` counters, `time.perf_counter()`, numpy matmul baseline

#### Spike Task 2: Concurrent mmap Region Limits
- **What**: Determine how many simultaneous mmap regions the NPU driver supports
- **How**: Open N concurrent mmap handles for weight files, submit NPU operations
- **Success Criterion**: Support at least 16 concurrent regions (16 blocks for 1B model)
- **Failure Fallback**: If limited, bundle blocks into fewer mmap regions

#### Spike Task 3: OS Page Cache Behavior (Windows 11)
- **What**: Profile how Windows manages page cache for large mmap'd files (1GB+)
- **How**: Load model weights, monitor RSS vs virtual memory, induce memory pressure
- **Success Criterion**: Page cache hit rate >99% during steady-state inference
- **Monitoring**: `psutil.Process().memory_info()`, Windows Performance Monitor

#### Spike Task 4: NPU Reconfiguration Latency
- **What**: Measure time to switch NPU from one chunk to another
- **How**: Time the sequence: deactivate chunk A -> activate chunk B -> first forward pass
- **Success Criterion**: <50ms reconfiguration latency (target: <100ms per AC)

#### Spike Task 5: GIL Behavior Validation (CRITICAL)
- **What**: Determine if NPU compute releases the Python GIL
- **How**: Start NPU compute in main thread, attempt numpy operations in concurrent thread, measure overlap
- **Success Criterion**: Concurrent numpy ops execute during NPU compute (>80% overlap)
- **If GIL NOT released**: Design kv_async_ops.py with `multiprocessing` + shared memory from Day 1
- **This is the make-or-break finding** for the async KV premise

**Go/No-Go Decision Criteria**:
- **Go to Phase 1**: All 5 tasks completed, bandwidth acceptable, GIL released OR multiprocessing viable
- **No-Go / Redesign**: NPU cannot access system RAM, or GIL blocks with no viable alternative
- **Conditional Go**: Bandwidth marginal but usable, GIL not released but multiprocessing confirmed viable (adds ~1 week to Phase 1)

### 21.5 Phase 0 Resource and Timeline

| Day | Activity | Output |
|-----|----------|--------|
| Day 1 | Set up test environment, write spike test scripts | Test scripts ready |
| Day 2-3 | Tasks 1-2: Bandwidth + mmap limits | Bandwidth numbers, mmap limit |
| Day 3-4 | Tasks 3-4: Page cache + reconfig latency | Page cache behavior, reconfig time |
| Day 4-5 | Task 5: GIL validation (parallel with report writing) | GIL release determination |
| Day 5 | Write spike report, present findings | Go/No-Go recommendation |

**Estimated effort**: 1 person-week

### 21.6 Post-Phase 0 Immediate Actions

Upon Go decision:
1. Begin Phase 1 implementation in order: `config.py` -> `buffer_registry.py` -> `kv_cache.py` -> `chunk_manifest.py` -> `chunk_manager.py` -> `kv_async_ops.py` -> `inference_loop.py` -> `streaming_assembler.py`
2. Set up `streaming/tests/` directory structure per Section 20.10
3. Implement FakeNPUComputeEngine with GIL-aware mocking
4. Begin writing Phase 1 unit tests alongside implementation (test-driven approach)

### 21.7 Strategic Summary

The document is now internally consistent and actionable. The architecture has been simplified from a 5-route exploration to a focused Route B implementation. All quality review issues have been resolved. The critical path is clear:

1. **Phase 0** (this week): Validate unified memory + GIL behavior
2. **Phase 1** (weeks 2-5): Build foundation modules
3. **Phase 2** (weeks 5-10): Implement chunked inference + multi-model
4. **Phase 3** (weeks 10-14): Multi-model weight management
5. **Phase 4** (weeks 14-17): Auto-configuration

The single highest-leverage activity is the **GIL validation in Phase 0**. If the AMD NPU driver releases the GIL during compute, async KV is straightforward with threading. If not, we need multiprocessing from Day 1, which adds serialization complexity but is proven viable. This risk cannot be mitigated without empirical data -- it must be measured.

---

*Planning analysis complete by Dr. Sarah Kim, Technical Product Strategist & Engineering Lead. Document coherence improved from 7/10 to 9/10. All 11 quality review issues resolved. Phase 0 plan is ready for immediate execution.*

---

## 22. Program Management Review - Pipeline Round 2

> **Date**: 2026-04-30
> **Reviewer**: Program Management Agent
> **Trigger**: Second pass of recursive iterative agent pipeline. Planning-analysis-strategist completed Round 2 fixes (11 issues resolved, coherence 7/10 -> 9/10). Section 21 added with Phase 0 execution plan.
> **Scope**: Milestone coherence, resource allocation actionability, success criteria measurability, Phase 0 stakeholder communication, remaining program-level gaps.

### 22.1 Milestone Status Review (M0-M6)

| Milestone | Phase | Week | Status | Coherence Assessment |
|-----------|-------|------|--------|---------------------|
| **M0** | Phase 0 | W1 | **PENDING** | **Coherent**. Scope is well-defined with 5 concrete spike tasks (Section 21.4). Go/No-Go criteria are explicit. The addition of GIL validation as Task 5 is the correct prioritization. Minor gap: no explicit success criterion for Task 2 (concurrent mmap limits) beyond "support 16 concurrent regions" -- this should specify a minimum acceptable number (e.g., >=16) and a fallback path if the limit is lower. |
| **M1** | Phase 1 | W5 | **DEFINED** | **Coherent**. Exit criteria are specific and measurable: 55+ tests passing, >90% coverage, >80% KV overlap. The split of kv_cache.py and kv_async_ops.py (per Section 18.4) makes the >80% KV overlap criterion properly scoped to kv_async_ops.py. The GIL validation dependency from M0 is correctly sequenced. |
| **M2** | Phase 2 | W7 | **DEFINED** | **Mostly coherent**. "Single-model chunked inference works; >=1.0x throughput vs baseline" is measurable. However, the M2 criterion of >=1.0x is a weaker target than M3's >=1.1x, which is appropriate for an MVP gate. One gap: M2 does not include a GIL regression check -- if GIL behavior changes between Phase 1 and Phase 2, the async KV advantage could regress. Recommend adding GIL stability verification (R32-R35 from Section 20.7.6) to M2 exit criteria. |
| **M3** | Phase 2 | W10 | **DEFINED** | **Coherent**. All acceptance criteria are numeric and testable: <100ms model switch, >=1.1x throughput, <1.2GB peak during load init, <7GB RSS for 2 models. The clarification of "peak during streaming load initialization (steady-state: ~3.14GB)" prevents stakeholder misinterpretation. |
| **M4** | Phase 3 | W14 | **DEFINED** | **Coherent (post-fix)**. After Round 2 fixes replaced Route C relic metrics, M4 now has measurable targets: <100ms memory pressure detection, <200ms model unload/reload, graceful degradation. One concern: M4 depends on multi-model scenarios under sustained load, which requires real-world memory pressure testing that may be difficult to reproduce deterministically in CI. |
| **M5** | Phase 4 | W17 | **DEFINED** | **Coherent**. ">95% correct config across test matrix" is measurable if the test matrix is defined. Current gap: the test matrix hardware configurations are not enumerated. Recommend defining a minimum set of 5-8 hardware profiles (e.g., 8GB/16GB/32GB RAM, 1B/7B models, different AIE column counts) to make the 95% target auditable. |
| **M6** | Program | W17 | **DEFINED** | **Mostly coherent**. "Production-ready release" is a program-level milestone, but "all phases complete; all acceptance criteria met; regression tests passing" is a binary gate, not a production-readiness assessment. Missing: security review, performance regression baseline, documentation completeness check, and stakeholder sign-off criteria. |

**Milestone Coherence Rating: 8.5/10**. M0-M5 are well-defined with measurable acceptance criteria. M6 needs expansion to include production readiness criteria beyond test pass rates.

### 22.2 Resource Readiness Assessment

#### Current State Analysis

The resource allocation plan (Section 16.3) proposes peak 3 FTE across phases with ~33 person-weeks total effort. Assessment:

| Phase | Planned FTE | Readiness | Assessment |
|-------|------------|-----------|------------|
| **Phase 0** | 1 Senior | **READY** | Spike scope is well-bounded (5 tasks, 1 week). The Phase 0 plan (Section 21.4) is actionable. The owner assignment is the single blocking item -- no named owner exists. |
| **Phase 1** | 1 Senior + 1 Mid | **PARTIALLY READY** | Module dependency graph is clear (Section 18.11). Implementation order is defined (Section 18.6). Gap: the GIL risk (R8/Critical) may require a senior engineer with C/Python extension experience if multiprocessing fallback is needed -- this is a more specialized skill than the current plan assumes. |
| **Phase 2** | 1 Senior + 1-2 Mid | **NOT READY** | Multi-model requirement (D14) significantly expands scope. The plan assumes 2-3 engineers, but the skill matrix is unclear. Chunked inference needs someone who understands NPU operator orchestration; multi-model needs someone who understands memory partitioning and lifecycle management. These are distinct skill sets. |
| **Phase 3** | 1 Senior + 1 Mid | **NOT READY** | Windows memory management at scale (OS page cache tuning, memory locking APIs) is a specialized domain. The plan does not identify whether the team has this expertise. |
| **Phase 4** | 1 Senior + 0-1 Mid | **NOT READY** | Auto-configuration requires hardware profiling across multiple configurations. The plan does not specify what hardware will be available for this work. |

#### Resource Risk Summary

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| **No named Phase 0 owner** | High | Critical | Assign owner immediately. If no NPU-experienced engineer is available, pair a senior Python engineer with an AMD driver liaison. |
| **Phase 2 skill gap (NPU orchestration + multi-model)** | Medium | High | Begin knowledge transfer during Phase 1. Document NPU reconfiguration patterns. Consider hiring or contracting if internal skills are insufficient. |
| **Windows memory management expertise gap (Phase 3)** | Medium | Medium | Engage Windows platform team or external consultant for OS page cache tuning. Alternatively, scope Phase 3 to "monitoring only" without active tuning. |
| **Hardware availability for Phase 4 auto-config** | Medium | Medium | Define hardware test matrix early (by Phase 1 end). Procure or identify target machines before Phase 4 begins. |
| **Single point of failure (1 Senior across all phases)** | High | High | If the same senior engineer is planned for all 5 phases, bus factor is 1. Cross-train mid-level engineer during Phase 1. |

### 22.3 Success Criteria Measurability Audit

Every success criterion in the program has been evaluated for measurability:

| Criterion | Target | Measurable? | Measurement Method | Audit Notes |
|-----------|--------|-------------|-------------------|-------------|
| Async KV overlap | >80% | YES | Profiling timeline of compute vs memory transfer | Well-defined. Test I8-I13 cover this. |
| KV paging overhead | <5% latency | YES | Benchmark paged vs non-paged | Well-defined. Tests K4-K5 cover this. |
| GIL behavior | Released or fallback works | YES | Tests G1-G8 with FakeNPU | Phase 0 spike will produce definitive answer. |
| Route B throughput | >=1.1x tokens/sec | YES | Benchmark vs monolithic baseline | Well-defined. Test P8 covers this. |
| NPU compile overhead | <500ms/chunk | YES | Timing measurement | Well-defined. AC14 covers this. |
| Multi-model switch latency | <100ms | YES | Timing deactivation/activation | Well-defined. Test M4 covers this. |
| Startup peak memory | <1.2GB (init), ~3.14GB (steady) | YES | tracemalloc + RSS monitoring | Clarified in Round 2. Tests MR1-MR4 cover this. |
| Multi-model RSS (2x) | <7GB | YES | RSS during dual-model inference | Well-defined. Test MR2 covers this. |
| Memory pressure detection | <100ms | YES | RSS monitoring during pressure injection | Measurable but requires test harness for pressure injection. |
| Model unload/reload | <200ms | YES | Timing full lifecycle | Well-defined. AC28 covers this. |
| Page cache hit rate | >99% | YES | OS-level page fault monitoring | Well-defined. Test R29 covers this. |
| Auto-config accuracy | >95% | **PARTIALLY** | Test matrix coverage | Test matrix not yet defined. Needs enumeration by Phase 1 end. |
| Zero regression | All tests pass | YES | CI pipeline | Well-defined. R1-R35 regression suite covers this. |
| Test coverage | >=90% line | YES | pytest-cov | Well-defined. AC2 covers this. |

**Measurability Rating: 9.5/10**. All criteria are numeric and testable except auto-config accuracy, which depends on an as-yet-undefined test matrix. This is a manageable gap with a clear resolution path.

### 22.4 Phase 0 Stakeholder Communication Plan

Phase 0 is the highest-visibility gate because its results determine whether the entire 17-week program proceeds. Stakeholder communication needs are significant.

#### Stakeholder Map for Phase 0

| Stakeholder | Interest | Communication Need | Timing |
|-------------|----------|-------------------|--------|
| **Executive sponsors** | Go/No-Go decision, timeline impact, risk exposure | 1-page brief: spike scope, 5 tasks, Go/No-Go criteria, risk summary | Before spike starts (kickoff) and after spike completes (decision) |
| **Engineering team** | Technical findings, implementation implications, GIL determination | Technical briefing: all 5 task results, raw data, recommended Phase 1 design adjustments | Within 2 days of spike completion |
| **AMD NPU driver team** | Driver capability validation results, API behavior feedback | Technical report: unified memory bandwidth, mmap limits, GIL release behavior, any driver issues encountered | After spike completion (offer to share findings) |
| **QA team** | Test strategy validation, GIL test design confirmation | GIL test approach review, bandwidth baseline for future regression tests | During spike (Day 3-4, parallel with Tasks 3-4) |
| **Product management** | Scope confirmation (Route B still viable after spike), multi-model timeline | Summary: spike results impact on Route B viability, multi-model readiness | After Go/No-Go decision |

#### Phase 0 Communication Artifacts

| Artifact | Audience | Format | Timing |
|----------|----------|--------|--------|
| Phase 0 Kickoff Brief | Executives + Engineering | 1-page email/memo | Day 1 of Phase 0 |
| Mid-Spike Check-in | Engineering | Slack/Teams update | Day 3 (Tasks 1-2 complete) |
| Spike Report | Engineering + QA | 5-10 page technical report with data | Day 5 |
| Go/No-Go Decision Memo | Executives + Product | 1-page decision document | Day 5 (with Spike Report) |
| Phase 1 Transition Brief | Engineering + QA | Technical briefing with design adjustments | Day 5-7 (post-decision) |

#### Key Messages for Phase 0 Communications

1. **This is a validation spike, not an implementation phase.** No production code will be written. The output is a report with empirical data.
2. **The GIL question is the single highest-leverage finding.** It determines whether async KV uses threading (simpler) or multiprocessing (more complex but viable). Either outcome is acceptable -- the question is which design path to take.
3. **Route B viability is NOT at risk from this spike.** Route B's core premise (unified memory, resident weights) is based on standard AMD NPU capabilities. The spike validates performance characteristics, not fundamental feasibility.
4. **Go/No-Go criteria are conservative.** The only true No-Go scenario is if the NPU cannot access system RAM at all (extremely unlikely) AND GIL blocks with no multiprocessing alternative (also unlikely). Conditional Go is the most probable outcome.

### 22.5 Remaining Program-Level Gaps

After thorough review of the post-fix document, the following program-level gaps remain:

#### Gap 1: No Named Resource Assignments

**Severity**: High
**Detail**: The resource plan specifies FTE counts and skill requirements but does not name specific engineers. Phase 0 cannot begin without an assigned owner.
**Recommendation**: Identify and assign the Phase 0 spike owner within 48 hours. Begin Phase 1 resource planning in parallel.

#### Gap 2: M6 (Production-Ready Release) Lacks Definition

**Severity**: Medium
**Detail**: M6 states "all phases complete; all acceptance criteria met; regression tests passing" but does not include production readiness criteria such as: security review, performance regression baseline establishment, documentation completeness, operational runbooks, or stakeholder sign-off.
**Recommendation**: Define M6 acceptance criteria to include: (a) all Phase 1-5 acceptance criteria met, (b) zero open critical/high bugs, (c) security review completed, (d) performance baseline documented, (e) user documentation complete, (f) stakeholder sign-off obtained.

#### Gap 3: No Change Management Process Defined

**Severity**: Medium
**Detail**: The program assumes a fixed scope (Route B), but does not define a change control process for handling scope changes during execution. Given that Phase 0 may reveal unexpected constraints, a formal change request process should be established.
**Recommendation**: Define a lightweight change control process: any scope change requires (a) impact assessment (timeline, resources, risk), (b) stakeholder review, (c) documented decision. This should be established before Phase 0 begins.

#### Gap 4: No Dependency on External Teams Formalized

**Severity**: Medium
**Detail**: The program depends on: (a) AMD NPU driver team for Phase 0 validation access and API behavior information, (b) Windows platform team for memory management expertise (Phase 3), (c) hardware procurement for Phase 4 auto-config testing. None of these dependencies are formalized with agreed timelines.
**Recommendation**: Create external dependency tracker with named contacts, expected deliverables, and target dates for each external team. Review weekly.

#### Gap 5: Phase 2-3 Resource Overlap Not Planned

**Severity**: Low
**Detail**: The sequential phasing (Section 16.8) shows no overlap between phases. However, the same senior engineer is planned for all phases, which creates a continuity risk if that person becomes unavailable mid-program. Additionally, Phase 3's Windows memory management work may benefit from starting knowledge acquisition during Phase 2.
**Recommendation**: Plan for 1-week overlap between Phase 2 and Phase 3 where the Phase 3 engineer shadows Phase 2 work. Cross-train mid-level engineer on async KV patterns during Phase 1 to reduce bus factor.

#### Gap 6: Budget Tracking Not Addressed

**Severity**: Low
**Detail**: The program estimates ~33 person-weeks of effort but does not translate this into budget terms (cost per FTE, total program budget, contingency reserve).
**Recommendation**: Convert person-week estimates to budget figures using current FTE rates. Add 15-20% contingency reserve (5-7 person-weeks) given the empirical validation risks in Phase 1-2.

#### Gap 7: Legacy Document Debt Not Scheduled

**Severity**: Low
**Detail**: Section 21.3 identifies legacy document deprecation banners as outstanding. While low priority, unresolved legacy documentation creates ongoing confusion risk for new team members.
**Recommendation**: Schedule deprecation banner creation as a Day 1 activity in Phase 0 (takes <1 hour). This is a quick win that prevents ongoing confusion.

### 22.6 Program Health Assessment - Post Round 2

| Dimension | Rating | Delta from Round 1 | Rationale |
|-----------|--------|-------------------|-----------|
| **Scope clarity** | 10/10 | +1 | All 11 coherence issues resolved. Zero ambiguity on Route B scope. |
| **Schedule realism** | 7/10 | No change | 17 weeks remains aggressive for 5 sequential phases. Phase 0 spike plan (Section 21.4) is realistic. Phase 2 (5 weeks for chunked inference + multi-model) remains the schedule risk. |
| **Resource adequacy** | 6/10 | -1 | Resource plan is defined but no named assignments. Phase 0 owner is the critical missing piece. Skill gaps for Phase 2-3 not addressed. |
| **Risk exposure** | 7/10 | +1 | GIL risk (R8) correctly identified as Critical with clear mitigation path. Remaining risks are empirical (validation-based) with defined test strategies. |
| **Test coverage plan** | 9/10 | No change | 210-test strategy with no hardware dependency. Comprehensive GIL, multi-model, and memory reality coverage. |
| **Stakeholder alignment** | 9/10 | -1 | User decisions are definitive, but stakeholder communication plan for Phase 0 Go/No-Go needs formalization (provided in 22.4). |
| **Documentation quality** | 9/10 | +2 | Coherence improved from 7/10 to 9/10. All internal contradictions resolved. Phase 0 plan is actionable. |
| **Overall program health** | **8/10** | **+0.5** | Strong foundation. Program is ready for Phase 0 execution pending resource assignment. The GIL validation spike is the single highest-leverage activity. |

### 22.7 Executive Recommendations (Priority Order)

1. **Assign Phase 0 spike owner (IMMEDIATE)**. This is the single blocking action. Identify a senior engineer with NPU driver and Windows memory management experience. If unavailable, pair a senior Python engineer with an AMD driver liaison.
2. **Execute Phase 0 spike per Section 21.4 plan**. The 5-task spike is well-scoped and can be completed in 1 week. GIL validation (Task 5) is the highest-leverage finding.
3. **Establish lightweight change control process** before Phase 0 begins. Define scope change impact assessment and stakeholder review procedure.
4. **Create external dependency tracker** for AMD NPU driver team, Windows platform team, and hardware procurement. Assign named contacts and target dates.
5. **Define M6 production readiness criteria** to include security review, performance baseline, documentation, and stakeholder sign-off.
6. **Convert person-week estimates to budget figures** with 15-20% contingency reserve.
7. **Schedule legacy document deprecation banners** as a Day 1 Phase 0 activity (quick win, <1 hour effort).

### 22.8 Program Readiness Verdict

**VERDICT: CONDITIONALLY READY FOR PHASE 0**

The program architecture, scope, phasing, test strategy, and success criteria are all well-defined and internally consistent. The document coherence improvement from 7/10 to 9/10 reflects genuine progress in eliminating contradictions and ambiguities.

The only condition preventing unconditional readiness is the **absence of a named Phase 0 spike owner**. Once this is assigned, Phase 0 can begin immediately using the actionable execution plan in Section 21.4.

The program's critical path remains: Phase 0 (GIL validation) -> Phase 1 (foundation modules) -> Phase 2 (chunked inference + multi-model). All other activities support this critical path.

---

*Program management review complete by Program Management Agent. Overall program health: 8/10. Conditionally ready for Phase 0 execution pending resource assignment.*

---

## 23. Quality Review - Pipeline Round 2 Coherence Check

> **Date**: 2026-04-30
> **Reviewer**: Quality Reviewer Agent
> **Scope**: Verify all previous critical issues (CV1-CV11) are resolved, check for new inconsistencies

### 23.1 Previous Critical Issue Verification

| ID | Issue | Status | Verification |
|----|-------|--------|-------------|
| CV1 | GIL risk missing from Section 9 | **PASS** | Section 9 includes R8 (GIL) as Critical with R1-R12 sequential numbering |
| CV2 | Phase 3 metrics are Route C relics | **PASS** | All sections (11, 15, 16.2, 16.5) now have Multi-Model Weight Manager targets |
| CV3 | TOC missing Sections 14-20 | **PASS** (partial) | TOC expanded through Section 21; now needs Section 22 added |
| CV4 | "<1.2GB startup peak" ambiguous | **PASS** | All instances clarified with "(steady-state RSS: ~3.14GB)" |
| CV5 | Risk ID collisions | **PASS** | Sequential R1-R12 numbering eliminates parallel conflict |
| CV6 | Section 10.2 Phase 3/4 Route C relics | **PASS** | Updated to weight_manager.py, memory_monitor.py, auto_config.py |
| CV7 | Section 10.2 Phase 1 file list outdated | **PASS** | 8 files match Section 18.4 |
| CV8 | Phase 1 duration inconsistency | **PASS** | Section 4.1 says "4 weeks" consistently |
| CV9 | Section 3.4 legacy status markers | **PASS** | All marked RESOLVED or DOCUMENT NOTE |
| CV10 | Section 11 missing program metrics | **PASS** | Added regression, coverage, RSS honesty validation |
| CV11 | Section 11 needs Route B memory honesty | **PASS** | Prominent note that Route B does NOT reduce RSS |

**Resolution rate: 11/11 PASS**

### 23.2 New Issues Found (Low Priority)

| ID | Issue | Severity | Detail |
|----|-------|----------|--------|
| N1 | Test count inconsistency | Low | Section 16.7 referenced "~220 tests", Section 20 says "~210" -- fixed |
| N2 | Section 22 missing from TOC | Low | TOC lists through Section 21 only |
| N3 | Phase 1 duration in Section 18.6 | Low | States "5-6 weeks" vs "4 weeks" elsewhere -- design-level estimate vs committed timeline |

### 23.3 Numerical Consistency Check

| Metric | Value | Consistent? |
|--------|-------|-------------|
| Llama-3.2-1B specs | hidden=2048, intermediate=8192, vocab=128256, 16 blocks | Yes |
| Per-block weight (FP16) | ~121.6MB | Yes |
| Total model weight (1B) | ~1.94GB | Yes |
| Steady-state RSS (Route B, 1B) | ~3.14GB (with resident embedding + LM head) | Yes |
| Startup peak | <1.2GB (initialization, not steady-state) | Yes, clarified |
| Timeline | 17 weeks, 5 phases | Yes |
| Test count | ~210 tests | Yes, fixed |
| Risk IDs | R1-R12 sequential | Yes |
| Phases | 0 (1w) + 1 (4w) + 2 (5w) + 3 (4w) + 4 (3w) = 17w | Yes |

### 23.4 Overall Quality Rating: 9/10

The document is now internally consistent across all 22 sections. All 11 previous critical/high/medium issues are resolved. Three low-priority items remain (N1-N3), none of which block Phase 0 execution.

**The document is ready for Phase 0 execution pending resource assignment.**

---

*Quality review complete by Quality Reviewer Agent. Document coherence: 9/10. Phase 0 readiness: Conditional (requires named owner).*

---

## 24. Senior Developer Final Assessment - Pipeline Round 2

> **Date**: 2026-04-30
> **Author**: Jordan Blake, Principal Software Engineer & Technical Lead
> **Trigger**: Second-pass coherence review completed. Planning fixed 11 issues (7/10 -> 9/10), Program Management confirmed conditional Phase 0 readiness (8/10), Quality verified all critical issues resolved.
> **Scope**: Phase 0 spike plan technical soundness, 9-file module hierarchy validation, implementation order assessment, gap analysis, biggest technical risk identification, go/no-go recommendation.

---

### 24.1 Phase 0 Spike Plan Technical Assessment (Section 21.4)

**Verdict: Technically Sound with 3 Recommended Additions**

The 5-task spike plan is well-scoped and covers the right validation targets. Each task has a clear success criterion and fallback path. Assessment of individual tasks:

| Task | Soundness | Comment |
|------|-----------|---------|
| Task 1: Unified Memory Bandwidth | **Sound** | Correct approach. Must test both streaming access pattern (sequential block loads) and random access (chunk switching). Add a test for sustained bandwidth over 1000+ iterations to catch thermal throttling on the NPU. |
| Task 2: Concurrent mmap Limits | **Sound** | Correct approach. Also test what happens when the limit is exceeded -- does the driver fail gracefully or crash? This determines our error-handling strategy. |
| Task 3: OS Page Cache Behavior | **Sound** | Critical for Route B's resident-weight model. Add a test that simulates memory pressure by allocating competing processes and verify weights remain accessible (even if page-faulted). |
| Task 4: NPU Reconfiguration Latency | **Sound** | <50ms target is reasonable. Also measure reconfiguration latency variance (p50/p95/p99) -- a single slow reconfiguration could blow the async KV timing budget. |
| Task 5: GIL Validation | **Sound -- but needs sharpening** | The current test approach (start compute, try numpy in thread) is correct but insufficient. Must also test: (a) whether numpy operations that allocate memory during compute hold the GIL, (b) whether the driver's `wait()`/`sync()` calls release the GIL, and (c) whether multiprocessing shared_memory works with numpy bf16 arrays (the `multiprocessing.shared_memory` module has known issues with non-standard dtypes). |

**Recommended Spike Additions:**

- **Task 6: NPU Driver Python API Maturity Assessment**. Document the actual Python API surface: what methods exist, what dtypes are supported, what error handling exists. This is not optional -- we cannot design `kv_async_ops.py` without knowing the exact API contract. The planning agent assumed the driver API exists and is usable; this must be verified empirically.

- **Task 7: bf16/Numpy Compatibility Validation**. Route B uses bfloat16 throughout. Numpy's bf16 support is limited (no native dtype). Verify: (a) can the NPU driver accept bf16 arrays, (b) does numpy matmul work with bf16 (via view casting or structured dtypes), and (c) does multiprocessing shared_memory preserve bf16 data correctly. If bf16 is not well-supported, we may need to use float16 for the KV cache or add explicit conversion layers.

- **Task 8: FakeNPU Fidelity Baseline**. Before building production components, we need to know how accurately FakeNPUComputeEngine models real NPU behavior. Run a small subset of operations on the real NPU and compare timing, output precision, and memory behavior against the fake. If FakeNPU is >2x off in timing or produces different numerical results, our test suite will give false confidence.

### 24.2 Module Hierarchy Assessment (Section 18.4)

**Verdict: 8 of 9 Files Are Correct. 1 Missing. 1 Should Be Restructured.**

The proposed module hierarchy is well-reasoned. Here is my file-by-file assessment:

| File | Assessment | Action |
|------|-----------|--------|
| `streaming/__init__.py` | **Correct** | Good exports list. Add `StreamingModelAssembler` to exports. |
| `streaming/config.py` | **Correct** | Right to build this first. Should include `StreamingConfig`, `ChunkConfig`, and `KVCacheConfig` as nested dataclasses with validation. |
| `streaming/buffer_registry.py` | **Correct** | Pure numpy, zero deps. Good first implementation target. Add alignment validation (4096-byte) per R9. |
| `streaming/kv_cache.py` | **Correct** | Pure data structure split is the right call. Must include paging interface even if implementation is deferred. |
| `streaming/kv_async_ops.py` | **Correct but high-risk** | This is the most complex file. Design with `use_multiprocessing` flag from Day 1. Do NOT write threading-only code and refactor later. |
| `streaming/chunk_manager.py` | **Correct** | Should own manifest I/O directly. The separate `chunk_manifest.py` adds an unnecessary abstraction layer. |
| `streaming/chunk_manifest.py` | **Merge into chunk_manager.py** | This is a dataclass with JSON read/write. It has no independent consumers. Fold it into `chunk_manager.py` as a private `_ChunkManifest` dataclass. Reduces module count and import complexity. |
| `streaming/inference_loop.py` | **Correct** | Critical missing piece from the original planning doc. Must define the prefill/decode orchestration contract. |
| `streaming/streaming_assembler.py` | **Correct** | API parity with `ModelAssembler` is the right design. Must match `assemble()`, `load_weights()`, `forward()`, `generate()` signatures exactly. |
| `streaming/streaming_infer.py` | **Correct** | Separate CLI entry point per D10. Keep thin -- delegate to `StreamingModelAssembler`. |
| **MISSING: `streaming/error_recovery.py`** | **Must Add** | What happens when a chunk forward fails? The current plan assumes all chunks succeed. Need error recovery: partial state cleanup, KV cache rollback, model state restoration. This is not a Phase 1 deliverable but must be designed in Phase 1 to avoid breaking the inference_loop.py contract later. |

**Restructured File Count: 9 files (merge chunk_manifest.py, add error_recovery.py as Phase 1 design-only)**

The fakes/ and tests/ subdirectory structure from Section 20.10 is correct and well-organized. No changes needed there.

### 24.3 Implementation Order Assessment

**Verdict: Correct, with 2 Adjustments**

The Section 18.6 implementation order follows the right principle (build simple deps first, de-risk hard things early). My assessment:

| Order | Module | Assessment | Adjustment |
|-------|--------|-----------|------------|
| 1 | `config.py` | **Correct** | Day 1-2 is right. Add validation tests immediately. |
| 2 | `buffer_registry.py` | **Correct** | Day 3-5. Zero deps, immediately testable. |
| 3 | `kv_cache.py` | **Correct** | Day 6-10. Pure data structure. |
| 4 | `chunk_manifest.py` + `chunk_manager.py` | **Merge these** | Day 11-17. Build as a single module with private `_ChunkManifest` dataclass. |
| 5 | `kv_async_ops.py` | **Correct -- highest priority** | Day 18-25. This is where GIL mitigation lives. Start with multiprocessing-first design, add threading as optimization. |
| 6 | `inference_loop.py` | **Correct** | Day 26-30. Integration test with FakeNPU. |
| 7 | `streaming_assembler.py` | **Correct** | Day 31-35. API parity with ModelAssembler. |
| 8 | `streaming_infer.py` | **Correct** | Day 36-38. Thin CLI wrapper. |

**Adjustment 1:** `kv_async_ops.py` should be designed with multiprocessing-first architecture, not threading-first with multiprocessing as fallback. The planning doc says "assume GIL is NOT released until proven otherwise" (Section 18.5) but the implementation order still puts threading first. This is a contradiction. If we design multiprocessing-first, the GIL-validation outcome from Phase 0 only determines whether we can simplify to threading -- not whether we need to rewrite.

**Adjustment 2:** `FakeNPUComputeEngine` should be built in parallel with `buffer_registry.py` (Day 3-5), not after Phase 0. The fake engine is needed for testing `kv_async_ops.py` and `inference_loop.py`. If it is not ready by Day 18, the async development stalls.

### 24.4 Technical Gap Analysis

The planning analysis (Section 21) is thorough but missed 5 technical gaps that will impact implementation:

#### Gap 1: Error Recovery and Partial State Rollback

**Severity: High**

The plan assumes chunks always complete successfully. In practice:
- NPU operator errors (shape mismatch, dtype error, driver timeout)
- Memory pressure causing OS page reclamation during forward pass
- KV cache paging failure at chunk boundary

What happens: hidden_states buffer is partially updated, KV cache is in an inconsistent state (some layers appended, some not), and the model cannot continue.

**Required:** Design error recovery contract in Phase 1. `inference_loop.py` must: (a) snapshot hidden_states before each chunk, (b) track KV cache append positions, (c) on failure, restore snapshot and clean partial KV entries. This is a design-only deliverable for Phase 1; implementation in Phase 2.

#### Gap 2: AIE Compilation Artifact Lifecycle

**Severity: High**

Decision D9 mandates AOT compilation during model conversion. But the plan does not define:
- Where artifacts are stored (alongside .npy files? separate directory?)
- How artifacts are versioned (if the NPU driver updates, do artifacts need recompilation?)
- How artifacts are validated at inference startup (detect stale artifacts vs. driver mismatch)
- What happens if artifacts are missing (fall back to JIT compilation?)

**Required:** Define artifact format, storage location, versioning scheme, and validation logic during Phase 1 design. This is not optional -- without it, `chunk_manager.py` cannot implement `activate_chunk()` because it does not know whether compilation artifacts exist.

#### Gap 3: Dtype Conversion Layer

**Severity: Medium**

Route B uses bfloat16 throughout. However:
- PyTorch's bf16 support is hardware-dependent (requires Ampere+ GPU or CPU with AVX512-BF16)
- numpy has no native bf16 dtype
- Windows 11 on consumer hardware may not support bf16 in PyTorch
- The NPU driver may expect float16 or float32

**Required:** Add a dtype conversion/normalization layer between PyTorch tensors and numpy/NPU buffers. This layer must handle: (a) bf16 <-> fp16 conversion, (b) numpy bf16 emulation (via uint16 view), (c) validation that the target hardware supports the chosen dtype. Phase 1 design, Phase 2 implementation.

#### Gap 4: Existing Code Refactoring Scope Underestimated

**Severity: Medium**

Section 18.3 estimates `layer_builder.py` refactoring at 15% effort ("extract KV cache management"). After reading the actual code, I assess this higher:

- `AttentionLayerBuilder` has `k_cache`/`v_cache` buffers embedded (lines 124-126)
- These buffers are used in `forward()` (lines 263-333) but the actual attention mechanism is a TODO (line 327: "TODO: Implement attention mechanism")
- The `forward()` method has two paths (fused MHA vs separate QKV), both with reshaping logic that assumes specific tensor layouts
- `TransformerBlockBuilder.forward()` (lines 717-753) has hardcoded mask/angles parameter passing that conflicts with BufferRegistry design

The refactoring is not just "extract KV cache to external manager." It is:
1. Externalize KV cache reference
2. Define buffer contract (shape, dtype, alignment)
3. Update all forward() methods to accept external buffers
4. Ensure backward compatibility (default behavior unchanged)

**Revised effort estimate: 30-35%** for `layer_builder.py`. This is not a blocker but must be accounted for in Phase 1-2 resource planning.

#### Gap 5: Testing the "Chunk Boundary Correctness" Invariant

**Severity: Medium**

Test I7 (`test_chunked_inference_chunk_boundary_correctness`) verifies that "hidden state at chunk boundary matches monolithic execution." But this test requires running both the chunked and monolithic inference paths and comparing outputs. The monolithic `ModelAssembler` (existing code) has:
- Incomplete attention implementation (TODO at line 327)
- No NPU operator integration (uses PyTorch nn.Linear/nn.Embedding)
- Different numerical precision (PyTorch bf16 vs numpy bf16 emulation)

**Required:** Either (a) complete the existing `ModelAssembler`'s attention implementation before Phase 2, or (b) use a reference PyTorch implementation (e.g., HuggingFace transformers) as the ground truth for output parity testing. This is a Phase 1 dependency that was not identified.

### 24.5 Single Biggest Technical Risk for Phase 0

**The AMD NPU Driver Python API Maturity and Documentation Quality**

This is the single biggest technical risk, and it subsumes the GIL risk (R8).

Here is why: the entire Phase 0 spike plan assumes the AMD NPU driver has a usable Python API that we can call to measure bandwidth, test mmap limits, validate GIL behavior, and measure reconfiguration latency. But if the driver:

- Has no public Python API (only C/C++ SDK)
- Has an undocumented or poorly documented Python API
- Has a Python API that does not support the operations we need (unified memory submission, buffer management, async execution)
- Has a Python API that crashes on large buffer submissions

Then Phase 0 cannot complete its 5 tasks, and we cannot make a Go/No-Go decision based on empirical data. Instead, we are blocked on obtaining driver access, documentation, or engineering support from AMD.

The GIL validation (Task 5) is the most dependent on driver API maturity. We cannot test GIL release behavior without being able to submit NPU compute operations from Python. If the driver does not exist or is inaccessible, the entire async KV premise cannot be validated, and we must design `kv_async_ops.py` blind -- assuming the worst case (multiprocessing required) without empirical confirmation.

**Probability: Medium. Impact: Critical. Mitigation:**
- Contact AMD NPU driver team before Phase 0 begins to confirm Python API availability
- Request driver documentation and sample code
- Identify a technical liaison at AMD who can answer API questions during the spike
- Prepare a fallback: if no Python API exists, write a minimal C wrapper using ctypes/cffi to call the driver's C API, then use that wrapper for Phase 0 measurements

### 24.6 Phase 0 Technical Readiness Verdict

| Criterion | Status | Detail |
|-----------|--------|--------|
| Spike scope well-defined | PASS | 5 tasks (need 3 additions: driver API, bf16 compat, fake NPU baseline) |
| Success criteria measurable | PASS | All tasks have numeric or boolean success criteria |
| Go/No-Go criteria clear | PASS | Conservative and reasonable |
| Resource plan adequate | CONDITIONAL | Requires named owner with NPU driver experience |
| Dependencies identified | CONDITIONAL | Missing AMD driver team contact, bf16 hardware support verification |
| Fallback paths defined | PASS | Each task has a fallback, but driver API fallback needs fleshing out |
| Integration with existing codebase assessed | PASS | Refactoring scope identified (Gap 4) |
| Test infrastructure ready | CONDITIONAL | FakeNPUComputeEngine must be built in parallel with Phase 0 |

### 24.7 Technical Corrections Required Before Phase 0

| # | Correction | Priority | Detail |
|---|-----------|----------|--------|
| TC1 | Add Task 6-8 to Phase 0 spike | High | Driver API assessment, bf16 compatibility, FakeNPU fidelity baseline |
| TC2 | Design kv_async_ops.py multiprocessing-first | High | Contradiction in planning doc: says "assume GIL not released" but designs threading-first |
| TC3 | Merge chunk_manifest.py into chunk_manager.py | Medium | Unnecessary module boundary; reduces Phase 1 file count from 8 to 7 |
| TC4 | Add error_recovery.py design to Phase 1 | Medium | Not implementation, but design the contract and data flow |
| TC5 | Revise layer_builder.py refactoring estimate to 30-35% | Medium | Actual code analysis shows more extensive changes needed |
| TC6 | Define AIE artifact lifecycle in Phase 1 | High | Storage, versioning, validation, fallback -- required for chunk activation |
| TC7 | Contact AMD driver team before Phase 0 | Critical | Confirm Python API availability, request docs, identify liaison |
| TC8 | Build FakeNPUComputeEngine parallel to Phase 0 | Medium | Needed for Phase 1 testing; cannot stall on hardware availability |

### 24.8 Go/No-Go Recommendation

**RECOMMENDATION: CONDITIONAL GO**

The architecture plan for Route B (Chunked Inference with Unified Memory) is technically sound. The document coherence improvement from 7/10 to 9/10 reflects genuine engineering rigor. The 9-file module hierarchy is correct (with the chunk_manifest.py merge), the implementation order is sound (with the multiprocessing-first adjustment), and the Phase 0 spike plan covers the right validation targets (with 3 additions).

The condition for Go is: **TC7 must be completed before Phase 0 begins.** Contact the AMD NPU driver team to confirm Python API availability and request documentation. If the API exists and is usable, Phase 0 proceeds as planned (with Tasks 6-8 added). If the API does not exist or is inaccessible, escalate to AMD engineering leadership before committing Phase 0 resources.

Everything else can be addressed during Phase 0 execution. The architecture is not at risk -- the question is implementation details (GIL behavior, dtype support, artifact lifecycle) that can be resolved empirically during the spike.

**Confidence: 8/10**

Route B is the right architectural choice for the stated requirements. The plan is executable. The risks are identified and have mitigation paths. The single blocking item is AMD driver API access, which is an organizational problem, not a technical one.

---

*Final assessment complete by Jordan Blake, Principal Software Engineer & Technical Lead. Phase 0 technical readiness: CONDITIONAL GO pending AMD driver API confirmation (TC7). Document coherence: 9/10. Architecture soundness: 8/10.*

---

## 25. Final Quality Coherence Assessment

> **Date**: 2026-04-30
> **Reviewer**: Taylor Kim, Senior Quality Management Specialist
> **Trigger**: Recursive iterative pipeline completed its second pass. All agents have run: Planning (Round 2, 11 issues fixed, coherence 9/10), Program Management (Round 2, 8/10 health, conditionally ready), Quality (Round 2, 11 CV issues PASS), Senior Developer (Round 2, Phase 0 technically sound, 5 technical gaps, conditional GO).
> **Scope**: Final quality gate before Phase 0. Verify all 24 sections are internally consistent. Confirm Section 24 findings do not contradict earlier sections. Validate Phase 0 plan completeness. Provide explicit pass/fail, quality rating, and Phase 0 readiness verdict.

### 25.1 Previous Critical Issue Verification (CV1-CV11)

| ID | Issue | Round 2 Status | My Verification | Verdict |
|----|-------|----------------|-----------------|---------|
| CV1 | GIL risk missing from Section 9 | PASS | Section 9 line 498: R8 listed as Critical with full mitigation. Line 506: "Critical risks: 1 (R8 GIL)." | **PASS** |
| CV2 | Phase 3 metrics are Route C relics | PASS | Sections 11, 15, 16.2, 16.5 all contain Multi-Model Weight Manager targets (AC27-AC31). No Route C relic metrics remain. | **PASS** |
| CV3 | TOC missing Sections 14-20 | PASS (partial) | TOC now extends through Section 23. However, Section 24 is NOT listed in the TOC (line 37 is the last entry). This is a residual gap. | **PASS (residual)** |
| CV4 | "<1.2GB startup peak" ambiguous | PASS | All instances now read "<1.2GB peak during streaming load initialization (steady-state RSS: ~3.14GB)." Verified in Sections 7, 11, 15, 16.2, 16.5. | **PASS** |
| CV5 | Risk ID collisions | PASS | Section 9 uses sequential R1-R12 with 3 struck-through eliminated risks. No parallel numbering conflict. | **PASS** |
| CV6 | Section 10.2 Phase 3/4 Route C relics | PASS | Phase 3 files: weight_manager.py, memory_monitor.py, model_lifecycle.py. Phase 4: auto_config.py. All descriptions match rescoped phases. | **PASS** |
| CV7 | Section 10.2 Phase 1 file list outdated | PASS | 8 files listed in Section 10.2 match Section 18.4 hierarchy (config.py, buffer_registry.py, kv_cache.py, kv_async_ops.py, chunk_manifest.py, chunk_manager.py, inference_loop.py, streaming_assembler.py). | **PASS** |
| CV8 | Phase 1 duration inconsistency | PASS | Section 4.1: "4 weeks." Sections 12, 16.2: "4 weeks." Consistent. (Note: Section 18.6 says "5-6 weeks" but self-reconciles as "design-level estimate with 1-2 week GIL buffer.") | **PASS** |
| CV9 | Section 3.4 legacy status markers | PASS | All C1-C3 and M1-M5 marked as RESOLVED or DOCUMENT NOTE. | **PASS** |
| CV10 | Section 11 missing program metrics | PASS | Added: zero regression, >=90% test coverage, steady-state RSS honesty. All present in Section 11. | **PASS** |
| CV11 | Section 11 needs Route B memory honesty | PASS | Prominent note on line 605: "Route B with resident weights does NOT reduce steady-state RSS." | **PASS** |

**Resolution rate: 11/11 PASS** (CV3 has a residual TOC gap for Section 24, noted below).

### 25.2 Section 24 Cross-Check Against Earlier Sections

Section 24 (Senior Developer Final Assessment) introduces 8 technical corrections (TC1-TC8). I verified each against earlier sections:

| TC | Finding | Contradiction or Gap? | Assessment |
|----|---------|----------------------|------------|
| TC1 | Add Tasks 6-8 to Phase 0 | GAP (enhancement) | Section 21.4 defines 5 tasks. TC1 adds driver API assessment, bf16 compatibility, and FakeNPU fidelity. These strengthen the spike but are not corrections to errors. The existing 5 tasks are sound. |
| TC2 | Multiprocessing-first vs threading-first | CORRECTION (design direction) | Section 18.5 says "assume GIL not released" but recommends ThreadPoolExecutor default. Section 24 correctly identifies this as a contradiction. Design direction should be multiprocessing-first. This should be noted before Phase 1 begins. |
| TC3 | Merge chunk_manifest.py | PREFERENCE | Architecture refinement. Section 18.4 lists it separately; TC3 says fold it in. Not a factual contradiction. |
| TC4 | Add error_recovery.py design | GAP | Valid gap. Not present in Section 18.4. Should be designed in Phase 1 to avoid breaking inference_loop.py contract later. |
| TC5 | layer_builder.py 30-35% not 15% | CORRECTION (estimate) | Section 18.3 says 15%. Section 24 references specific code lines (TODO at 327, hardcoded mask/angles) showing more work is needed. The revised estimate is more credible. |
| TC6 | AIE artifact lifecycle undefined | GAP | Decision D9 mandates AOT but no lifecycle defined. Valid gap for Phase 1 design. |
| TC7 | Contact AMD driver team before Phase 0 | ORGANIZATIONAL | Not a document issue. This is the single blocking action before Phase 0 can begin. |
| TC8 | Build FakeNPU parallel to Phase 0 | SCHEDULING | Valid adjustment. Does not contradict earlier sections. |

**Summary**: Section 24 findings are gap identifications and design refinements. They do NOT contradict the architectural decisions, numerical values, or phasing established in earlier sections. Two items (TC2, TC5) are genuine corrections to earlier statements. Six items are enhancements or gap identifications that strengthen the plan.

### 25.3 Numerical Consistency Audit

| Metric | Value | Verified Across Sections | Status |
|--------|-------|-------------------------|--------|
| Per-block weight (FP16) | ~121.6MB | D2, 3.5.4, 18.10, 23.3 | **CONSISTENT** |
| Total model weight (1B) | ~1.94GB | 3.5.4, 18.10, 23.3 | **CONSISTENT** |
| Embedding + LM Head | 1.05GB (resident) | 3.5.4, D15, 18.10 | **CONSISTENT** |
| Steady-state RSS (Route B, 1B, S=4096) | ~3.14GB | 3.5.4, 11, 16.5, 18.10, 23.3 | **CONSISTENT** |
| Startup initialization peak | <1.2GB (init only) | 7, 11, 15, 16.2, 16.5 | **CONSISTENT** (clarified) |
| Timeline | 17 weeks (1+4+5+4+3) | 12, 16.2, 21.6, 23.3 | **CONSISTENT** |
| Test count | ~210 | 20.3, 20.11, 23.2 | **CONSISTENT** |
| Risk IDs | R1-R12 (sequential) | 9, 21.1, 23.1 | **CONSISTENT** |
| Decision count | D1-D17 | 8, 21.1 | **CONSISTENT** |
| KV paging threshold | S > 16K | 3.5.1, D16, 12, 16.2 | **CONSISTENT** |
| Multi-model switching latency | <100ms | 11, 16.2, 16.5, M4 | **CONSISTENT** |
| Async KV overlap target | >80% | 11, 16.2, 16.5, AC4 | **CONSISTENT** |

**Result: Zero numerical inconsistencies found.**

### 25.4 Remaining Low-Priority Items

| ID | Issue | Severity | Detail |
|----|-------|----------|--------|
| N2 | TOC missing Section 24 | Low | TOC lists through Section 23. Section 24 was added after the last TOC update. Takes <5 minutes to fix. |
| N3 | Phase 1 duration 5-6w in Section 18.6 vs 4w elsewhere | Trivial | Section 18.6 self-reconciles: "5-6 weeks (consistent with Program Management estimate of 4 weeks, with 1-2 week buffer for GIL investigation)." This is a design-level estimate vs committed timeline distinction, not a contradiction. |
| R-ADD | Driver API maturity not in risk register | Low-Medium | Section 24.5 identifies AMD NPU driver Python API maturity as the "single biggest technical risk" that "subsumes the GIL risk." This could be added to Section 9 as R13, but the risk is addressed by TC7 (contact AMD team before Phase 0). |

### 25.5 Section-by-Section Health Assessment

| Section | Currency | Internal Consistency | Cross-Section Consistency | Notes |
|---------|----------|---------------------|--------------------------|-------|
| 1 (Executive Summary) | CURRENT | EXCELLENT | EXCELLENT | Accurate, current |
| 2 (What Has Been Done) | CURRENT | EXCELLENT | EXCELLENT | Complete |
| 3-3.5 (Analysis) | CURRENT | EXCELLENT | EXCELLENT | Section 3.5 user impact analysis is thorough |
| 4 (Current State) | CURRENT | GOOD | GOOD | Phase 1 duration consistent |
| 5 (Open Questions) | CURRENT | EXCELLENT | EXCELLENT | All answered |
| 6 (Agent Consensus) | CURRENT | EXCELLENT | EXCELLENT | Complete |
| 7 (Next Steps) | CURRENT | GOOD | GOOD | Startup peak clarified |
| 8 (Decision Log) | CURRENT | EXCELLENT | EXCELLENT | D1-D17 complete |
| 9 (Risk Register) | CURRENT | GOOD | GOOD | R1-R12 sequential, GIL as R8 Critical |
| 10 (Codebase Impact) | CURRENT | GOOD | GOOD | All file descriptions updated |
| 11 (Success Metrics) | CURRENT | EXCELLENT | EXCELLENT | Route B memory note present |
| 12 (Phasing Plan) | CURRENT | EXCELLENT | EXCELLENT | Consistent with all sections |
| 13 (Appendix) | CURRENT | GOOD | GOOD | Accurate |
| 14 (Senior Dev Initial) | CURRENT | EXCELLENT | EXCELLENT | Historical, superseded by 18, 24 |
| 15 (Testing Strategy) | CURRENT | EXCELLENT | EXCELLENT | Phase 3 metrics updated |
| 16 (Program Management) | CURRENT | EXCELLENT | EXCELLENT | Solid program view |
| 17 (Quality Review) | CURRENT | EXCELLENT | EXCELLENT | Historical record, recommendations acted on |
| 18 (Route B Assessment) | CURRENT | EXCELLENT | EXCELLENT | Thorough, honest memory assessment |
| 19 (Coherence Verify) | CURRENT | EXCELLENT | EXCELLENT | All CV items marked DONE |
| 20 (Testing Update) | CURRENT | EXCELLENT | EXCELLENT | Route B focused, comprehensive |
| 21 (Planning Analysis) | CURRENT | EXCELLENT | EXCELLENT | Phase 0 plan actionable |
| 22 (Program Review) | CURRENT | EXCELLENT | EXCELLENT | Milestones coherent, 7 gaps identified |
| 23 (Quality Round 2) | CURRENT | EXCELLENT | EXCELLENT | 11/11 CV issues PASS |
| 24 (Senior Dev Final) | CURRENT | EXCELLENT | EXCELLENT | 8 TC items, conditional GO |

### 25.6 Phase 0 Plan Completeness Assessment

The Phase 0 spike plan (Section 21.4) defines 5 tasks. Section 24 recommends 3 additions (TC1). Assessment:

| Task | Defined In | Scope Clear? | Success Criterion? | Fallback Path? |
|------|-----------|-------------|-------------------|----------------|
| Task 1: Unified Memory Bandwidth | 21.4 | YES | YES (<5% of compute time) | YES |
| Task 2: Concurrent mmap Limits | 21.4 | YES | YES (>=16 regions) | YES (bundle blocks) |
| Task 3: OS Page Cache Behavior | 21.4 | YES | YES (>99% hit rate) | YES |
| Task 4: NPU Reconfiguration Latency | 21.4 | YES | YES (<50ms) | YES |
| Task 5: GIL Validation | 21.4 | YES | YES (>80% overlap) | YES (multiprocessing) |
| Task 6: Driver API Assessment (TC1) | 24.1 | YES | N/A (documentation) | YES (C wrapper via ctypes) |
| Task 7: bf16 Compatibility (TC1) | 24.1 | YES | N/A (validation) | YES (use fp16) |
| Task 8: FakeNPU Fidelity Baseline (TC1) | 24.1 | YES | N/A (measurement) | N/A |

**Verdict**: The Phase 0 plan is complete. The original 5 tasks cover all critical validation targets. The 3 additional tasks from Section 24 are valuable enhancements that reduce implementation risk but are not blockers for the spike itself.

### 25.7 Final Quality Rating

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Architectural coherence** | 10/10 | Route B consistently defined across all 24 sections. Zero contradictions in core architecture. |
| **Numerical consistency** | 10/10 | All metrics, calculations, and figures verified consistent. |
| **Decision traceability** | 10/10 | D1-D17 complete, sourced, and reflected throughout. |
| **Risk management** | 9/10 | R1-R12 comprehensive. GIL correctly flagged Critical. One gap: driver API maturity (addressed by TC7). |
| **Phasing clarity** | 10/10 | 5 phases, 17 weeks, sequential, clear entry/exit criteria. |
| **Test strategy** | 9/10 | ~210 tests, no hardware dependency, comprehensive GIL/multi-model coverage. |
| **Documentation quality** | 9/10 | All contradictions resolved. Minor TOC gap (Section 24 missing). |
| **Phase 0 actionability** | 9/10 | 5 well-defined tasks with clear success criteria. 3 recommended enhancements from Section 24. |
| **Overall document quality** | **9.5/10** | The highest coherence this document has achieved. All 11 CV issues resolved. Section 24's findings complement (not contradict) earlier work. The document is a reliable source of truth for Phase 0 execution. |

### 25.8 Phase 0 Readiness Verdict

**VERDICT: CONDITIONAL GO FOR PHASE 0**

The document is internally consistent, architecturally sound, and technically ready for Phase 0 execution. The following conditions must be met before Phase 0 begins:

**Blocking Conditions (must resolve before Day 1):**

1. **Assign named Phase 0 spike owner** -- Per Program Management (Section 22.7, Gap 1). This is an organizational action, not a document fix.
2. **Contact AMD NPU driver team** -- Per Senior Developer TC7 (Section 24.5, line 2629). Confirm Python API availability, request documentation, identify technical liaison. This is the single highest-leverage organizational action.

**Recommended Pre-Phase 0 Actions (can be done in parallel with blocking conditions):**

3. **Add Section 24 to TOC** -- Takes <5 minutes. Residual from CV3 fix chain.
4. **Update Section 18.3 layer_builder.py estimate to 30-35%** -- Per TC5. Takes <1 hour.
5. **Note multiprocessing-first design direction** -- Per TC2. Document that kv_async_ops.py should be designed multiprocessing-first, with threading as a simplification path if GIL validation succeeds. Takes <5 minutes as a note in Section 21.6 or 18.6.
6. **Log error_recovery.py and AIE artifact lifecycle as Phase 1 design items** -- Per TC4, TC6. These are Phase 1 deliverables but should be acknowledged in the Phase 0 kickoff to set expectations.

**Not Required Before Phase 0:**
- Tasks 6-8 (TC1): Can be added to the spike during execution. They are enhancements, not prerequisites.
- chunk_manifest.py merge (TC3): Can be decided during Phase 1 implementation.
- FakeNPU parallel build (TC8): Can be scheduled during Phase 0 execution.
- Budget conversion, change management, M6 definition (Section 22.5 Gaps 2-6): Program-level items, not Phase 0 blockers.

### 25.9 Executive Summary

This document has undergone four rounds of agent review (Planning, Program Management, Quality, Senior Developer) across two pipeline passes. All 11 critical/high/medium coherence issues from Round 1 have been resolved. Section 24 (Senior Developer Final Assessment) identified 8 technical corrections, of which 2 are genuine corrections (TC2, TC5) and 6 are gap identifications or enhancements. None contradict the core architectural decisions.

**The document is ready.** Phase 0 can begin once the two organizational conditions (named owner, AMD driver contact) are satisfied. The architecture is sound, the phasing is logical, the test strategy is comprehensive, and the risk register is current. The single highest-leverage activity remains the GIL validation in Phase 0 Task 5.

---

*Final quality coherence assessment complete by Taylor Kim, Senior Quality Management Specialist. Document quality: 9.5/10. Phase 0 readiness: CONDITIONAL GO (2 organizational conditions). All 11 CV issues: PASS.*

---

## 26. Final Test Readiness Assessment

> **Date**: 2026-04-30
> **Author**: Morgan Rodriguez, Senior QA Engineer & Test Automation Architect
> **Trigger**: Final pass of recursive iterative agent pipeline. Route B confirmed, document coherence 9.5/10, Phase 0 readiness CONDITIONAL GO.
> **Scope**: Verify test strategy alignment with final Route B scope, assess GIL test adequacy, validate multi-model coverage, evaluate Phase 0 spike test validation criteria, audit FakeNPU compute engine design, and confirm all acceptance criteria are testable.

### 26.1 Route B Scope Alignment Audit

The test strategy exists in two versions: the original `streaming_test_strategy.md` (~220 tests, multi-route) and the Route B-updated Section 20 in this document (~210 tests, Route B-only). This audit verifies Section 20's alignment with the final Route B scope as defined by decisions D12-D17 and validated through Sections 23-25.

| Route B Decision | Test Coverage Present? | Test IDs | Alignment Status |
|-----------------|----------------------|----------|-----------------|
| D12: Route B as primary architecture | YES | Full Section 20 | **ALIGNED** -- 58 Route C/E tests removed, 43 Route B tests added |
| D13: Route C deprioritized | YES | U100-U104, U105-U113 removed | **ALIGNED** -- RuntimeStreaming and WeightCache tests eliminated |
| D14: Multi-model required | YES | M1-M12, I18-I25, P13-P15 | **ALIGNED** -- 12 unit + 8 integration + 3 benchmark tests |
| D15: Resident embedding + LM head | YES | U91b, U91c, R27-R31 | **ALIGNED** -- Resident weight stability explicitly tested |
| D16: KV paging for S > 16K | YES | K1-K6, AC11 | **ALIGNED** -- Paging functional tests with <5% latency overhead |
| D17: Quantization optional | YES | Q1-Q2 | **ALIGNED** -- Compatibility tested, not required |

**Scope Alignment Verdict: ALIGNED**. Section 20 accurately reflects the final Route B scope. All user decisions D12-D17 have corresponding test coverage. The net test count of ~210 (down from ~220) reflects genuine scope reduction, not coverage loss.

**Critical Document State Note**: The standalone `streaming_test_strategy.md` file has NOT been updated to reflect Route B. It still contains Route C, Route E, and AdaptiveSelector tests. Section 20 of this document IS the authoritative Route B test strategy. Before Phase 1 begins, `streaming_test_strategy.md` must either be updated to match Section 20 or deprecated with a pointer to Section 20. This is a pre-Phase 1 action item.

### 26.2 GIL Test Adequacy Assessment (G1-G8)

The GIL risk (R8/R9) is rated Critical. The async KV premise depends on NPU compute releasing the GIL. Eight tests (G1-G8) target this risk. Here is the adequacy breakdown:

#### 26.2.1 Coverage Matrix

| GIL Risk Aspect | Test ID | Covered? | Adequacy |
|----------------|---------|----------|----------|
| NPU compute releases GIL | G1 | YES | **ADEQUATE** -- Direct verification via concurrent numpy ops |
| KV async thread unblocked during compute | G2 | YES | **ADEQUATE** -- Thread-level unblocking verified |
| Compute + KV temporal overlap >80% | G3 | YES | **ADEQUATE** -- Measurable overlap percentage |
| Threading overhead <5% of inference time | G4 | YES | **ADEQUATE** -- Numeric threshold |
| Multiprocessing fallback works | G5 | YES | **ADEQUATE** -- Fallback path validated |
| Multiprocessing serialization overhead <10ms | G6 | YES | **ADEQUATE** -- Numeric threshold |
| All driver GIL behavior cataloged | G7 | YES | **PARTIAL** -- Tests catalog but requires real driver |
| ProcessPoolExecutor overlap + shared memory | G8 | YES | **ADEQUATE** -- End-to-end multiprocessing path |

#### 26.2.2 Gaps Identified by Section 24 (Senior Developer)

Section 24, Task 5 identified three additional GIL test requirements not covered by G1-G8:

| Gap | Description | Severity | Recommendation |
|-----|-------------|----------|----------------|
| **GIL-GAP-1** | numpy memory allocation during compute holding GIL | High | Add test G9: allocate large numpy arrays during NPU compute; verify allocation completes without blocking |
| **GIL-GAP-2** | Driver wait()/sync() calls releasing GIL | High | Add test G10: submit NPU operation, call wait()/sync() from different thread; verify no deadlock |
| **GIL-GAP-3** | multiprocessing shared_memory with bf16 arrays | Medium | Add test G11: create shared_memory with bf16 (uint16 view), verify data integrity across process boundary |

#### 26.2.3 GIL Test Adequacy Verdict

**G1-G8: ADEQUATE AS BASELINE, INCOMPLETE WITHOUT G9-G11**. The 8 existing tests cover the core GIL behavior verification. However, the 3 gaps identified by the senior developer are real and testable. These should be added as G9-G11 before Phase 1 begins.

| Metric | Value |
|--------|-------|
| Existing GIL tests | 8 |
| Recommended additions | 3 |
| Total recommended | 11 |
| Minimum for Phase 0 spike | 5 (G1, G3, G5, G7, G8) |
| Minimum for Phase 1 entry | 8 (G1-G8) |
| Full coverage | 11 (G1-G11) |

### 26.3 Multi-Model Test Coverage Assessment

Multi-model support (D14) adds significant complexity. 20 tests (M1-M12 unit, I18-I25 integration) cover this requirement.

#### 26.3.1 Scenario Coverage Matrix

| Multi-Model Scenario | Test ID | Covered? | Notes |
|---------------------|---------|----------|-------|
| Initialize with multiple manifests | M1 | YES | Basic initialization |
| Model activation/deactivation lifecycle | M2, M3 | YES | Core lifecycle |
| Switching latency <100ms | M4 | YES | Numeric threshold |
| Model isolation (no state corruption) | M5 | YES | Critical invariant |
| KV cache partitioning | M6 | YES | Resource isolation |
| Shared BufferRegistry between models | M7 | YES | Resource sharing |
| Manifest switching | M8 | YES | Configuration |
| Sequential request handling | M9 | YES | No parallel execution |
| State preservation on return | M10 | YES | KV state survives switch |
| Resource cleanup on deactivation | M11 | YES | Memory hygiene |
| 3-model rotation | M12 | YES | Extended scenario |
| Full pipeline A->B switch | I18 | YES | End-to-end |
| KV partition isolation | I19 | YES | No cross-model bleeding |
| Shared registry corruption check | I20 | YES | Data integrity |
| RSS tracking during switch | I21 | YES | Memory monitoring |
| 3-way rotation end-to-end | I22 | YES | Extended pipeline |
| Sequential request isolation | I23 | YES | Concurrency safety |
| A->B->B->A state preservation | I24 | YES | Idempotent switching |
| Memory pressure graceful degradation | I25 | YES | Failure mode |

#### 26.3.2 Multi-Model Stress/Chaos Gap

| Gap | Description | Severity | Recommendation |
|-----|-------------|----------|----------------|
| **MM-GAP-1** | Rapid switching (100+ switches/sec) under sustained load | Medium | Add integration test I26: rapid model switching stress test |
| **MM-GAP-2** | KV cache state corruption during interrupted switch | Medium | Add test I27: switch interrupted mid-way, verify both models' KV state intact |
| **MM-GAP-3** | Memory pressure during multi-model inference with paging enabled | High | Add test I28: combine memory pressure (R28) with KV paging (K1-K6) and multi-model switching |

#### 26.3.3 Multi-Model Test Verdict

**M1-M12 + I18-I25: ADEQUATE for normal operations, need 3 stress tests for production readiness.** The 20 existing tests cover all nominal and error scenarios for multi-model support. The 3 identified gaps (rapid switching, interrupted switches, pressure + paging combination) are edge cases that should be tested before Phase 3 (Multi-Model Weight Manager) begins.

### 26.4 Phase 0 Spike Test Validation Plan

Phase 0 has 5 core tasks + 3 recommended additions (Section 24, TC1). Each task requires explicit test validation criteria.

#### 26.4.1 Phase 0 Task Validation Criteria

| Task | Validation Test(s) | Pass Criterion | Fail Criterion | Conditional Pass |
|------|-------------------|----------------|----------------|-----------------|
| **T1: Unified Memory Bandwidth** | Phase 0 bandwidth measurement script | Streaming + random access >= Phase 0 baseline; sustained 1000+ iterations within 5% variance | Bandwidth < 50% of expected (thermal throttling detected) | Bandwidth within 80-100% of expected; proceed with adjusted expectations |
| **T2: Concurrent mmap Limits** | Open N concurrent mmap regions | N >= 16 concurrent regions supported | N < 8; driver crashes or hangs | 8 <= N < 16; proceed with block bundling fallback |
| **T3: OS Page Cache Behavior** | Memory pressure + weight access test | >99% page cache hit rate; weights re-accessible after pressure | Page cache hit rate < 90%; weights inaccessible after pressure | 90-99% hit rate; proceed with page cache tuning |
| **T4: NPU Reconfiguration Latency** | Measure reconfig latency 100+ times | p50 < 50ms, p95 < 75ms, p99 < 100ms | p50 > 100ms (reconfig too slow for chunk switching) | p50 < 50ms but p99 > 100ms; proceed with latency budget adjustment |
| **T5: GIL Validation** | G1-G5 with real NPU driver | NPU compute releases GIL; overlap >80% achievable | GIL held during ALL compute; overlap <20% even with multiprocessing | Threading achieves 50-80% overlap; proceed with hybrid approach |
| **T6: Driver API Assessment** (recommended) | Driver API surface inventory | Python API documented; all needed methods available | No Python API exists | API exists but undocumented; proceed with reverse engineering |
| **T7: bf16 Compatibility** (recommended) | bf16 round-trip through driver | bf16 arrays accepted, data integrity preserved | bf16 not supported; must use fp16 | bf16 works but with precision loss; proceed with validation |
| **T8: FakeNPU Fidelity Baseline** (recommended) | Compare FakeNPU vs real NPU on 10 ops | Timing within 2x, output within np.allclose(atol=1e-3) | FakeNPU >5x slower or different precision | FakeNPU within 2-3x; proceed with calibrated timing |

#### 26.4.2 Phase 0 Go/No-Go Decision Tree

```
Phase 0 Results -> Decision:
  T1 FAIL (no unified memory)        -> NO-GO (Route B impossible)
  T2 FAIL (<8 mmaps) + no fallback   -> CONDITIONAL GO (requires block bundling)
  T3 FAIL (<90% page cache)          -> CONDITIONAL GO (requires page cache tuning)
  T4 FAIL (p50 >100ms reconfig)      -> NO-GO for chunk_size=1; proceed with chunk_size>=3
  T5 PASS (GIL released)             -> GO (threading-first viable)
  T5 CONDITIONAL (50-80% overlap)    -> CONDITIONAL GO (hybrid threading+multiprocessing)
  T5 FAIL (GIL held, multiprocessing works) -> CONDITIONAL GO (multiprocessing-first)
  T5 FAIL (GIL held, multiprocessing fails) -> NO-GO (async KV impossible; redesign needed)
  T6 FAIL (no Python API)            -> CONDITIONAL GO (requires C wrapper via ctypes)
  T7 FAIL (no bf16 support)          -> CONDITIONAL GO (use fp16 with conversion layer)
  T8 FAIL (FakeNPU inaccurate)       -> GO (proceed, but calibrate test timing expectations)
```

**Phase 0 Test Validation Verdict: COMPLETE**. All 5 core tasks have explicit pass/fail/conditional criteria. The 3 recommended additions (T6-T8) should be added to the formal spike plan but are not blocking for Phase 0 execution.

### 26.5 FakeNPU Compute Engine Design Assessment

The FakeNPUComputeEngine design (Section 20.8, streaming_test_strategy.md Section 1.5) provides numpy-based NPU emulation. Assessment of its soundness:

#### 26.5.1 Strengths

| Aspect | Assessment |
|--------|-----------|
| Numpy-based compute | **Sound** -- GEMM, RMSNorm, RoPE, Attention all implementable in numpy with correct numerical behavior |
| Configurable delays | **Sound** -- compute_delay_ms and memory_transfer_delay_ms allow timing scenario testing |
| Timeline recording | **Sound** -- Operation timestamps enable overlap analysis |
| GIL behavior flag | **Sound concept** -- release_gil=True/False allows testing both GIL scenarios |
| Resident weight loading | **Sound** -- load_weights() at startup matches Route B architecture |
| Multi-model model_id | **Sound** -- Separate FakeNPU instances per model for isolation testing |
| Two-tier data strategy | **Sound** -- Small config (4 layers) for fast unit tests, full config for integration |

#### 26.5.2 Design Deficiencies

| Deficiency | Severity | Detail | Fix |
|-----------|----------|--------|-----|
| `_simulate_gil_release()` is a no-op | High | The method does nothing (line 1911: `pass`). It does not actually simulate GIL release or holding. This means G1-G8 cannot validate real GIL behavior. | Implement using `threading.Lock` to block/unblock concurrent threads, simulating GIL hold/release patterns |
| bf16 not handled | High | numpy has no native bf16. All operations use float32. Route B uses bf16 throughout. This creates a fidelity gap for dtype-related tests (U27, Q1, T7). | Use `np.uint16` view casting with `ml_dtypes.bfloat16`, or add explicit conversion layer |
| `get_overlap_stats()` not implemented | Medium | The method body is `...` (Section 1.5, line 332). Overlap analysis is critical for AC4 (>80% overlap). | Implement timeline analysis: compute DMA intervals, find overlapping compute intervals, calculate percentage |
| No error injection | Medium | No way to simulate NPU operator failures, timeout, or memory errors for error recovery testing. | Add `failure_rate` config; randomly raise simulated errors for chaos testing |
| DMA delay formula hardcoded | Low | Line 1916: `delay = (size_bytes / (20 * 1024**3))` assumes 20GB/s unified memory bandwidth. This should be configurable from Phase 0 baseline. | Make `bandwidth_gbs` a constructor parameter; default to Phase 0 measurement |
| No softmax implementation | Low | `softmax` is called in `attention()` but not defined in the class. Will cause NameError. | Add `def softmax(x, axis=-1): e = np.exp(x - np.max(x)); return e / e.sum(axis=axis, keepdims=True)` |

#### 26.5.3 FakeNPU Fidelity Requirements

For the test suite to provide meaningful confidence, FakeNPU must match real NPU behavior within these bounds:

| Property | Required Fidelity | How to Validate |
|----------|------------------|-----------------|
| Numerical output (GEMM, Norm) | Within np.allclose(atol=1e-3) of real NPU | Task 8: run same inputs through both, compare |
| Compute timing (per operation) | Within 2x of real NPU | Task 8: benchmark both, measure ratio |
| Memory transfer behavior | Within 2x of real unified memory | Task 1 + Task 8: compare bandwidth curves |
| GIL release behavior | Binary match (release/hold) | Task 5: verify real driver behavior, match FakeNPU flag |
| bf16 precision | Within 1 ULP of real NPU bf16 | Task 7: bf16 round-trip comparison |

#### 26.5.4 FakeNPU Design Verdict

**SOUND CONCEPT, 6 FIXES REQUIRED before Phase 1 test implementation**. The design is architecturally correct and covers all Route B testing needs. The 6 identified deficiencies (no-op GIL simulation, missing bf16, incomplete overlap stats, no error injection, hardcoded bandwidth, missing softmax) must be fixed before the FakeNPU can serve as a reliable test foundation. Estimated fix effort: 1-2 days.

### 26.6 Acceptance Criteria Testability Audit

All 35 acceptance criteria (AC1-AC35) evaluated for testability:

#### 26.6.1 Phase 1 Criteria (AC1-AC12)

| AC | Criterion | Testable? | Test Method | Risk |
|----|-----------|-----------|-------------|------|
| AC1 | APIs match design docs | YES | Code review + interface contract check | Low |
| AC2 | >=90% line coverage | YES | pytest-cov --fail-under=90 | Low |
| AC3 | 0 failures on CI | YES | CI pipeline | Low |
| AC4 | >80% memory transfer overlap | YES | Integration test I8 | Medium (timing variance) |
| AC5 | Partitioning correctness | YES | Parametrized unit tests U56-U69 | Low |
| AC6 | Contract enforcement | YES | Unit tests U44-U46 | Low |
| AC7 | No NPU required | YES | Run tests without NPU | Low |
| AC8 | Interfaces stable | YES | Interface review | Low |
| AC9 | Documentation complete | YES | Docstring audit | Low |
| AC10 | Benchmark framework operational | YES | Run P1-P12 successfully | Low |
| AC11 | KV paging functional | YES | Tests K1-K6 | Medium (requires S>16K test data) |
| AC12 | GIL behavior validated | YES | Tests G1-G4 (need G9-G11) | **High** (depends on real NPU) |

#### 26.6.2 Phase 2 Criteria (AC13-AC26)

| AC | Criterion | Testable? | Test Method | Risk |
|----|-----------|-----------|-------------|------|
| AC13 | >=1.1x throughput | YES | Benchmark P8 | Medium (baseline stability) |
| AC14 | <500ms compile/chunk | YES | Timing measurement | Low |
| AC15 | Feature flags R1-R8 pass | YES | Regression tests | Low |
| AC16 | Output parity R9-R14 | YES | Regression tests | **Medium** (needs reference model, Section 24 Gap 5) |
| AC17 | Chunked inference I1-I7 | YES | Integration tests | Medium (FakeNPU fidelity) |
| AC18 | Async KV I8-I13 | YES | Integration tests | Medium (timing) |
| AC19 | CLI functional | YES | Smoke test | Low |
| AC20 | Cross-platform R15-R20 | YES | CI on Windows + Linux | Low |
| AC21 | Baselines stored | YES | File existence check | Low |
| AC22 | Multi-model M1-M12, I18-I25 | YES | Unit + integration tests | Medium (complexity) |
| AC23 | Resident weight R27-R31 | YES | OS-level monitoring | Medium (OS-dependent) |
| AC24 | RSS ~3.14GB +/-5% | YES | tracemalloc + RSS | Low |
| AC25 | Startup peak <1.2GB | YES | tracemalloc during init | Low |
| AC26 | Bandwidth meets baseline | YES | Tests B1-B6 vs Phase 0 data | Medium (depends on Phase 0) |

#### 26.6.3 Phase 3 Criteria (AC27-AC31)

| AC | Criterion | Testable? | Test Method | Risk |
|----|-----------|-----------|-------------|------|
| AC27 | Pressure detection <100ms | YES | RSS monitoring + injection | Medium (pressure injection harness needed) |
| AC28 | Unload/reload <200ms | YES | Timing full lifecycle | Low |
| AC29 | Graceful degradation | YES | Test I25 + pressure injection | Medium (defining "graceful") |
| AC30 | 2x 1B models <7GB RSS | YES | RSS measurement | Low |
| AC31 | Page cache >99% hit rate | YES | OS page fault monitoring | Medium (OS-dependent) |

#### 26.6.4 Phase 4 Criteria (AC32-AC35)

| AC | Criterion | Testable? | Test Method | Risk |
|----|-----------|-----------|-------------|------|
| AC32 | >95% chunk size selection | **PARTIALLY** | Needs test matrix (Section 22, Gap) | **High** (test matrix undefined) |
| AC33 | KV cache sizing within 10% | YES | Compare auto vs manual tuning | Medium (defining "optimal") |
| AC34 | Paging threshold within 2K | YES | Compare auto vs manual threshold | Low |
| AC35 | Max models within 1 of optimal | YES | Compare auto vs manual max | Low |

#### 26.6.5 Acceptance Criteria Testability Verdict

| Metric | Value |
|--------|-------|
| Fully testable | 32/35 (91.4%) |
| Partially testable | 2/35 (AC16 needs reference model, AC32 needs test matrix) |
| Not testable | 1/35 (AC12 requires real NPU driver, cannot be fully tested with FakeNPU alone) |
| Test method defined | 35/35 (100%) |
| Numeric threshold | 35/35 (100%) |

**Overall: 91.4% fully testable with software-only approach. 8.6% requires real NPU hardware or external inputs (Phase 0 baseline data, reference model).**

### 26.7 Test Coverage Gap Analysis

The following gaps were identified between the current test strategy and complete Route B coverage:

| Gap ID | Category | Description | Severity | Test Count Impact | Recommendation |
|--------|----------|-------------|----------|-------------------|----------------|
| TC-GAP-1 | GIL | G9-G11: numpy alloc during compute, driver wait/sync, shared_memory bf16 | High | +3 | Add to Phase 0 spike test plan |
| TC-GAP-2 | Multi-Model | I26-I28: rapid switching stress, interrupted switch, pressure+paging | Medium | +3 | Add before Phase 3 |
| TC-GAP-3 | Error Recovery | No tests for chunk forward failure, partial state rollback, KV cache cleanup | High | +5 | Design in Phase 1 (Section 24, Gap 1), implement in Phase 2 |
| TC-GAP-4 | AIE Artifacts | No tests for AIE compilation artifact lifecycle, versioning, validation | Medium | +4 | Design in Phase 1 (Section 24, Gap 2), implement in Phase 2 |
| TC-GAP-5 | Dtype Conversion | No tests for bf16/fp16 conversion layer (Section 24, Gap 3) | Medium | +3 | Add in Phase 1 |
| TC-GAP-6 | Output Parity | Test I7 needs reference model; existing ModelAssembler is incomplete (Section 24, Gap 5) | Medium | +1 (setup) | Add reference PyTorch model or complete existing attention |
| TC-GAP-7 | M2 Gate | No GIL regression check between Phase 1 and Phase 2 (Section 22.1) | Low | +1 | Add R36: GIL stability verification to M2 exit criteria |
| TC-GAP-8 | Document Sync | streaming_test_strategy.md not updated to Route B scope | High | N/A | Update or deprecation-banner standalone file |

**Total gap impact: +20 new tests needed (3 immediate, 17 phased).** Updated total: ~230 tests.

### 26.8 Updated Test Inventory

| Category | Original | Section 20 | After Gap Analysis | Change |
|----------|----------|-----------|-------------------|--------|
| Unit tests | ~150 | ~125 | ~140 | +15 (G9-G11, error recovery, dtype, artifacts) |
| Integration tests | ~30 | ~25 | ~29 | +4 (I26-I28, reference model setup) |
| Performance benchmarks | ~15 | ~15 | ~15 | No change |
| Regression tests | ~25 | ~28 | ~32 | +4 (R36 + 3 gap regression tests) |
| GIL validation tests | 0 | ~8 | ~11 | +3 (G9-G11) |
| Multi-model tests | 0 | ~12 | ~12 | No change |
| **Total** | **~220** | **~210** | **~230** | **+20 from gap analysis** |

### 26.9 Pre-Phase 1 Test Action Items

The following test-related actions must be completed before Phase 1 implementation begins:

| Priority | Action | Effort | Owner | Dependency |
|----------|--------|--------|-------|------------|
| **P0** | Fix FakeNPU _simulate_gil_release() no-op | 0.5 days | QA + Dev | None |
| **P0** | Add softmax() to FakeNPU | 0.25 days | QA | None |
| **P0** | Implement get_overlap_stats() | 0.5 days | QA | None |
| **P0** | Add bf16 support via ml_dtypes | 1 day | QA | None |
| **P1** | Update streaming_test_strategy.md to Route B scope | 1 day | QA | None |
| **P1** | Add G9-G11 to GIL test plan | 0.5 days | QA | Phase 0 driver access |
| **P1** | Add error recovery test design (TC-GAP-3) | 1 day | QA + Dev | Section 24 Gap 1 design |
| **P1** | Add AIE artifact test design (TC-GAP-4) | 1 day | QA + Dev | Section 24 Gap 2 design |
| **P2** | Define AC32 test matrix (hardware profiles) | 0.5 days | PM + QA | Section 22 Gap |
| **P2** | Add I26-I28 multi-model stress tests | 1 day | QA | None |
| **P2** | Set up reference model for output parity (TC-GAP-6) | 1 day | Dev | HuggingFace transformers |

### 26.10 Final Test Readiness Verdict

**VERDICT: CONDITIONAL GO FOR PHASE 0, CONDITIONAL GO FOR PHASE 1 PLANNING**

The test strategy is fundamentally sound and aligned with Route B scope. All acceptance criteria are testable (91.4% with software-only, 8.6% requires Phase 0 baseline data or real NPU). The FakeNPU design needs 4 immediate fixes (P0 items) before it can serve as a reliable test foundation. The GIL test suite (G1-G8) is adequate as a baseline but needs 3 additions (G9-G11) for complete critical risk coverage.

**Conditions for Phase 0 execution:**
1. Same organizational conditions from Section 25.8 (named owner, AMD driver contact)
2. FakeNPU P0 fixes completed (4 items, ~2.25 days effort)

**Conditions for Phase 1 start:**
1. Phase 0 spike completed with empirical data
2. All 10 P1 action items completed
3. GIL test suite extended to G1-G11
4. Error recovery and AIE artifact test designs completed
5. streaming_test_strategy.md synchronized with Section 20

### 26.11 Test Strategy Health Dashboard

| Dimension | Rating | Trend | Notes |
|-----------|--------|-------|-------|
| **Route B alignment** | 10/10 | Stable | Section 20 fully aligned with D12-D17 |
| **GIL coverage** | 7/10 | Improving | G1-G8 solid; G9-G11 needed for 10/10 |
| **Multi-model coverage** | 8/10 | Stable | M1-M12 + I18-I25 comprehensive; stress tests needed |
| **FakeNPU quality** | 5/10 | Needs work | 4 P0 fixes required before Phase 1 |
| **Acceptance criteria testability** | 9/10 | Stable | 91.4% fully testable; 3 require external inputs |
| **Phase 0 readiness** | 8/10 | Stable | Dependent on organizational conditions |
| **CI/CD pipeline design** | 9/10 | Stable | Well-structured, cross-platform, coverage-gated |
| **Overall test strategy health** | **8/10** | **Improving** | Strong foundation; 2.25 days of FakeNPU fixes + 20 additional tests needed for 10/10 |

---

*Final test readiness assessment complete by Morgan Rodriguez, Senior QA Engineer & Test Automation Architect. Test strategy health: 8/10. Phase 0 readiness: CONDITIONAL GO (same organizational conditions as Section 25.8 + 4 FakeNPU P0 fixes). Gap analysis: 8 gaps identified, +20 tests needed, updated total ~230 tests.*
