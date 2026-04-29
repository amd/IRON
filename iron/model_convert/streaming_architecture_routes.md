# IRON NPU - Block Architecture: Routes Inspired by Proven Implementations

> What Apple CoreML's Llama-2-7b-ANE implementation proves about chunked block inference.
> Target: Llama-3.2-1B as baseline, scalable to 7B+ models.
> Key constraint: IRON has unified memory access.
>
> **Status:** Reviewed by Quality, Strategy, and Program Management agents. Corrected and updated 2026-04-29.

---

## Decision Context

The current architecture loads **all weights into RAM at startup** (~3.0GB for Llama-3.2-1B). This works for small models but doesn't scale to 7B+ or multi-model scenarios.

Apple already proved this works on ANE with Llama-2-7b in CoreML. Their approach: **chunk the model into blocks**, run one chunk at a time, update KV cache asynchronously. The model is split into:

- 1 chunk: embedding + attention mask + RoPE cos/sin
- N chunks: transformer blocks (3 blocks per chunk)
- 1 chunk: LM head

This enables faster loading + async KV cache manipulation. Proven on M1 Max and M3 Max chips (see Apple's [CoreML LLM CLI](https://github.com/apple/coremltools) and WWDC sessions on ANE deployment).

IRON has **unified memory** — the NPU can access system RAM directly. Combined with Apple's chunked block pattern, this gives us a solid foundation.

---

## Terminology: Block vs Layer vs Chunk

This is the key distinction that the previous design doc got confused about.

### Block = One Transformer Layer (Self-Contained Unit)

```python
class Block(nn.Module):
    def forward(self, x, cos, sin, mask, input_pos):
        x_normed = self.norm_1(x)
        attention_output = self.attn(x_normed, cos, sin, mask, input_pos)
        x = attention_output + x
        x = self.mlp(self.norm_2(x)) + x
        return x
```

A Block = Norm_1 + Attention + Norm_2 + MLP + Residuals. **This is exactly one transformer layer.** The terms "layer" and "block" are used interchangeably in most codebases.

Each block has **~9 weight files (.npy format), ~121MB total** for Llama-3.2-1B (FP16):

```
Q_proj:  2048 * 2048 * 2B = 8.39MB
K_proj:  2048 * 512  * 2B = 2.10MB
V_proj:  2048 * 512  * 2B = 2.10MB
O_proj:  2048 * 2048 * 2B = 8.39MB
Gate:    2048 * 8192 * 2B = 33.55MB
Up:      2048 * 8192 * 2B = 33.55MB
Down:    8192 * 2048 * 2B = 33.55MB
RMSNorm: 2048 * 2B * 2  = 0.01MB
Total per block: ~121.6MB (FP16)
```

### Chunk = Multiple Blocks Grouped Together (Execution Unit)

```
Chunk 0: Blocks 0, 1, 2     (3 blocks)
Chunk 1: Blocks 3, 4, 5     (3 blocks)
...
```

Each chunk is a **separate CoreML model file** that can be loaded and run independently. For Llama-2-7B (32 blocks), that's ~11 chunk files.

### Three Levels of Granularity

| Level | What It Contains | Llama-3.2-1B Count | Llama-2-7B Count |
|-------|-----------------|-------------------|------------------|
| Operator | Single GEMM, Norm, etc. | ~240 ops total | ~480 ops total |
| Block | 15 operators = 1 transformer layer (~121MB) | 16 blocks | 32 blocks |
| Chunk | Multiple blocks grouped | configurable | 11 chunks (3 blocks each) |

### Current IRON Terminology vs What We Should Use

| IRON Currently Says | What It Actually Means | CoreML Equivalent |
|--------------------|----------------------|-------------------|
| "Layer 0 weights" | 9 .npy files for one transformer block | Block 0 weights |
| "All layers loaded" | All 16 blocks' weights resident | Not used (CoreML chunks) |
| N/A | Group of blocks loaded together | Chunk model (.mlpackage) |

---

## Apple's Proven Approach (CoreML Llama-2-7b)

### Chunking Architecture

```
  ┌──────────────┐      ┌───────────────┐
  │  Embedding    │      │  Precomputed   │
  │  Chunk       │─────>│  RoPE cos/sin  │
  └──────────────┘      └───────────────┘
                              │
                              v
  ┌─────────────────────────────────────────────────────┐
  │  BLOCK CHUNKS (3 blocks per chunk)                  │
  │                                                      │
  │  Chunk 0:  Block_0 → Block_1 → Block_2  → hidden   │
  │  Chunk 1:  Block_3 → Block_4 → Block_5  → hidden   │
  │  ...                                                 │
  │  Chunk 10: Block_30 → Block_31          → hidden   │
  └─────────────────────────────────────────────────────┘
                              │
                              v
  ┌──────────────┐      ┌────────────────┐
  │  LM Head     │<─────│  Final Norm     │
  │  Chunk       │      │                 │
  └──────────────┘      └────────────────┘
```

### Async KV Cache (Proven by Apple)

```
  BEFORE CHUNK PREDICTION:
  ┌──────────────┐      ┌───────────────┐
  │ Old KV Cache │      │ Hidden States │
  │ (Length 448) │      │  (Length 64)  │
  └──────────────┘      └───────────────┘
              ↘        ↙
             ┌───────────┐
             │Chunk Model│  (3 blocks)
             └───────────┘
              ↙        ↘
  ┌──────────────┐      ┌─────────────────┐
  │ New KV Cache │      │New Hidden States│
  │ (Length 64)  │      │   (Length 64)   │
  └──────────────┘      └─────────────────┘

  ASYNC (after chunk completes, before next chunk):
  ┌──────────────┐     ┌──────────────┐
  │ Old KV Cache │     │ New KV Cache │
  │ (Length 448) │     │ (Length 64)  │
  └──────────────┘     └──────────────┘
               ↘         ↙
           ┌──────────────────┐
           │Cache Update Model│  (separate model)
           └──────────────────┘
                    ↓
            ┌────────────────┐
            │Updated KV Cache│
            │  (Length 512)  │
            └────────────────┘

  Time saved: ~1-2ms per chunk, ~20ms overall for Llama-2-7B
```

The key insight: **KV cache update doesn't need to happen inside each chunk**. It can happen asynchronously after the chunk returns its new KV entries and before the next chunk needs the updated cache. This is ~1 full forward pass of future time to do the update.

### Tensor Layout Optimization (20% Speedup)

Apple proved that reshaping MLP tensors from `(B, C, 1, S)` to `(B, C, 8, 8)` makes convolutions 50% faster on ANE. They reshape before QKV projections and back after attention output.

**Note:** ANE is convolution-based; IRON's AIE uses GEMM (systolic arrays). The principle (match tensor shape to compute unit) transfers, but the specific dimensions differ. For IRON, the relevant shape is aligned with tile sizes (M=64, K=64, N=64), not 8x8.

---

## Routes: What IRON Should Do

Given Apple's proven approach + IRON's unified memory, here are the possible routes:

---

## Route A: Pure Unified Memory (Async KV Only)

**Philosophy**: All weights always resident. Only optimization is async KV cache.

```
  STARTUP:
  - mmap all weights once (stay mapped forever)
  - Allocate KV cache in system RAM
  - Allocate activation buffers

  INFERENCE:
  - NPU accesses weights through unified memory
  - No explicit load/unload — OS handles paging automatically
  - KV cache DMA overlaps with NPU compute (async)

  MEMORY:
  | Weights (all 16 blocks) | 1.94GB resident      |
  | Embedding + LM Head     | 1.05GB mmap'd        |
  | KV Cache (S=4096)       | 128MB                |
  | Activations             | ~50MB                |
  | TOTAL                   | ~3.0GB               |
```

### Pros
- Simplest change from current architecture
- Lowest per-block latency (no reload overhead)
- No disk I/O after startup
- KV async still gives measurable speedup (Apple proved ~20ms for 7B)

### Cons
- Doesn't solve the "model too big for RAM" problem
- No multi-model support
- Same memory ceiling as current approach

### Complexity: **Low** (add AsyncKVCache + BufferRegistry only)

### When to Choose This
- You have enough RAM for your target models
- You want the simplest path to better performance
- Multi-model and large models are not priorities

---

## Route B: Unified Memory + Block Chunking (Apple's Pattern)

**Philosophy**: All weights stay mapped (unified memory), but we organize them into chunks of blocks — exactly like Apple's CoreML approach. One chunk is "active" at a time. KV cache updates happen asynchronously between chunks.

```
  STARTUP:
  - mmap all weights once (stay mapped, unified memory)
  - Organize into chunks: [Blocks 0-2], [Blocks 3-5], [Blocks 6-8], ...

  INFERENCE:
  for chunk in chunks:
      activate_chunk(chunk)                    # NPU reconfigures for this chunk
      for block in chunk.blocks:
          hidden = block.forward(hidden)       # NPU compute
      async_kv.enqueue_update(chunk.blocks)    # non-blocking KV merge

  CHUNK SIZE TRADE-OFFS (Llama-3.2-1B, 16 blocks):
  | Blocks/Chunk | Num Chunks | Chunk Size | KV Update Windows |
  |--------------|------------|------------|-------------------|
  | 8            | 2          | 973MB      | 1 per pass        |
  | 4            | 4          | 486MB      | 4 per pass        |
  | 3 (Apple)    | ~5-6       | 365MB      | 5-6 per pass      |
  | 2            | 8          | 243MB      | 8 per pass        |
  | 1            | 16         | 121MB      | 16 per pass       |
```

### Apple's 3-Blocks-Per-Chunk Pattern Applied to IRON

For Llama-3.2-1B (16 blocks), Apple's pattern gives us 6 chunks:

```
  Chunk 0: Blocks 0, 1, 2      (3 blocks, 365MB)
  Chunk 1: Blocks 3, 4, 5      (3 blocks, 365MB)
  Chunk 2: Blocks 6, 7, 8      (3 blocks, 365MB)
  Chunk 3: Blocks 9, 10, 11    (3 blocks, 365MB)
  Chunk 4: Blocks 12, 13, 14   (3 blocks, 365MB)
  Chunk 5: Block 15            (1 block, 121MB)

  Each chunk has its own KV cache update window:
  - Chunk 0 returns new K/V for blocks 0-2
  - While Chunk 1 is computing, async KV merge happens for blocks 0-2
  - By the time Chunk 2 needs blocks 0-2's KV, it's already updated
```

### Async KV Cache per Chunk (Apple's Pattern)

```
  TIMELINE (Llama-3.2-1B, 6 chunks of ~3 blocks):

  Chunk 0: [Compute Blocks 0-2] ──→ returns K/V[0-2] + hidden
  Chunk 1:          [Compute Blocks 3-5] ──→ returns K/V[3-5] + hidden
  Chunk 2:                   [Compute Blocks 6-8] ──→ returns K/V[6-8] + hidden

  Async KV Update (runs between chunks):
  Chunk 0:          [Async KV Merge K/V[0-2]]
  Chunk 1:                   [Async KV Merge K/V[3-5]]
  Chunk 2:                            [Async KV Merge K/V[6-8]]

  KV merge happens with ~1 chunk's worth of time buffer (future).
  No blocking on KV write. Apple saves ~1-2ms per chunk this way.
```

### Pros
- Proven pattern (Apple runs 7B model on ANE with this)
- Tunable chunk size (pick based on available RAM)
- Multi-model: switch active chunks between models **only if combined weights fit in RAM**
- KV async gives measurable speedup (~20ms for 7B on Apple)
- Unified memory: no explicit mmap/unmap cycles

### Cons
- Still maps all weights at startup (virtual memory, not RSS)
- More complex than Route A
- Chunk boundaries add minor overhead
- **Multi-model limited**: if all models' weights are mapped, total RAM ceiling remains

### Complexity: **Medium** (add chunking logic + AsyncKVCache + BufferRegistry)

### When to Choose This
- You want a proven, battle-tested pattern
- You want flexibility across devices (8GB to 64GB RAM)
- You might run multiple models eventually

---

## Route C: True Block Streaming + Unified Memory

**Philosophy**: Weights are NOT pre-mapped. Load one block (or chunk of blocks) at a time on demand. Unified memory means the NPU pages data in automatically.

```
  STARTUP:
  - mmap nothing (zero weights resident)
  - Allocate KV cache
  - Allocate activation buffers
  - Build operator graphs for all blocks (metadata only)

  PREFILL:
  for chunk in chunks:
      page_in(chunk)               # OS maps chunk's weights
      async_kv.enqueue_update(chunk.blocks)
      hidden = chunk.forward(hidden)
      page_out(chunk)              # OS reclaims pages

  PEAK RAM (3-block chunks, Llama-3.2-1B):
  | One chunk weights | 365MB resident           |
  | Embedding (mmap)  | 525MB mapped, ~0 resident|
  | LM Head (mmap)    | 525MB mapped, ~0 resident|
  | KV Cache (S=4096) | 128MB                    |
  | Activations       | ~10MB                    |
  | TOTAL             | ~486MB (single chunk)    |

  PEAK RAM (1-block at a time):
  | One block weights | 121MB resident           |
  | Embedding (mmap)  | 525MB mapped, ~0 resident|
  | LM Head (mmap)    | 525MB mapped, ~0 resident|
  | KV Cache (S=4096) | 128MB                    |
  | Activations       | ~10MB                    |
  | TOTAL             | ~254MB (single block)    |
```

### The Unified Memory Difference

Old approach (without unified memory):
```
mmap("layer_0/*.npy")  -> explicit file mapping
compute()
munmap()               -> explicit file unmapping
```

New approach (with unified memory):
```
page_in(chunk)         -> OS/driver pages into unified address space
compute()              -> NPU accesses through unified memory
page_out(chunk)        -> OS reclaims pages (doesn't unmap, just evicts)
```

The key difference: `page_out` doesn't unmap — it just marks pages as reclaimable. The mapping stays. Next access re-faults from disk. Faster than full mmap/unmap.

### Disk I/O Cost (per forward pass)

| Chunk Size | Total Data | NVMe (~3GB/s) | SATA SSD (~500MB/s) |
|------------|-----------|---------------|---------------------|
| 1 block (121MB * 16) | 1.94GB | ~0.6s | ~3.9s |
| 3 blocks (365MB * 6) | 1.94GB | ~0.6s | ~3.9s |
| 4 blocks (486MB * 4) | 1.94GB | ~0.6s | ~3.9s |

**Note:** All chunk sizes read the same total data (all blocks). The difference is in file seek overhead (9 files per block vs. bundled chunk files).

### Weight Cache (Mitigation for Decode)

Keep recently-used chunks in RAM:
```
cache_size = 2 chunks  # keep last 2 chunks resident (~730MB)
for chunk in chunks:
    if chunk not in cache:
        page_in(chunk)
    compute()
    if cache.full():
        evict_lru()
    cache.add(chunk)
```

With 2-chunk cache: first pass loads all 6 chunks, second pass (next token) only loads 4 (2 are cached). Decode becomes faster after the first token.

**Note:** The weight cache partially converges Route C toward Route B — if you cache all chunks, you end up with Route B's resident model. This is a feature, not a bug: Route C and Route B form a continuum, and the cache size is the dial.

### Prefill vs. Decode

| Phase | Route C Behavior | Disk I/O Impact |
|-------|-----------------|-----------------|
| **Prefill** (prompt tokens, T=100) | Each block loaded once, computed, unloaded | 1.94GB total, one-time cost |
| **Decode** (single token, T=1, repeated) | Each block loaded every token generation | 1.94GB per token — dominant cost |

During decode, disk I/O dominates. On NVMe, ~0.6s per token is acceptable. On SATA SSD, ~3.9s per token is unusable for interactive use. This is why Route C requires fast storage or aggressive weight caching.

### Pros
- Smallest memory footprint (~254MB single block vs ~3.0GB)
- Can run models larger than RAM
- Multi-model trivial (switch active weights)
- Unified memory makes page_in/page_out cheaper than mmap/unmap

### Cons
- Disk I/O per forward pass (6-16 load cycles depending on chunk size)
- Most complex architecture
- Decode latency dominated by storage speed
- Requires weight cache for acceptable performance on slow storage
- **Critical dependency**: AMD NPU driver must expose page_in/page_out APIs

### Complexity: **High** (full streaming + AsyncKVCache + BufferRegistry + weight cache)

### When to Choose This
- You need to run models larger than available RAM
- You want multi-model serving
- You're targeting edge devices with tight memory budgets
- You have fast storage (NVMe)

---

## Route D: Hybrid — Streaming at Init, Unified at Runtime

**Philosophy**: Stream blocks in one at a time during startup (low peak memory during load), then keep them resident for fast inference.

```
  STARTUP (Streaming Load):
  for block_id in 0..15:
      page_in(block_id)       # load one block (~121MB peak)
      keep_resident(block_id)  # don't page out
      # Peak during load: ~121MB (not 3.0GB)

  RESULT: All weights resident, but startup only needed
  ~121MB available RAM instead of 3.0GB

  INFERENCE (All Resident):
  - NPU accesses weights through unified memory
  - No reload, no page faults
  - KV cache async for performance (Apple's pattern)

  PEAK RAM DURING LOAD: ~121MB
  PEAK RAM DURING RUNTIME: ~3.0GB (same as Route A)
```

### The Key Insight

Some systems have 16GB total RAM but only 2GB free at any moment (browser, IDE, etc. using 14GB). The current architecture fails because it needs 3.0GB contiguous free memory at startup. Route D works because it only needs 121MB free at a time.

### Prefill vs. Decode

Route D has **identical** prefill and decode performance to Route A (all weights resident). The only difference is at startup:
- Route A: needs 3.0GB free at startup (may fail)
- Route D: needs 121MB free at startup (always succeeds)

### Pros
- Fast startup on memory-constrained systems
- Full-speed inference after loading (no reload overhead)
- Simpler than Route C (no per-forward-pass streaming)
- Unified memory handles page reclamation under pressure
- Can organize into chunks at runtime (Apple's pattern) for async KV

### Cons
- Still needs 3.0GB eventually (just not all at once)
- If OS evicts pages under pressure, you get page faults during inference
- More complex startup than Route A

### Complexity: **Low-Medium** (streaming load + keep_resident, no runtime streaming)

### When to Choose This
- Users have enough total RAM but fragmented availability
- You want fast inference after a brief startup
- You don't need multi-model support

---

## Route E: Adaptive — Pick Strategy Based on Model + Hardware

**Philosophy**: Detect model size and available RAM at runtime, choose the best strategy automatically.

```
  DETECTION:
  model_size = weight_size (from manifest)
  available_ram = get_available_memory()

  DECISION TREE (thresholds to be tuned empirically):
  if model_size < available_ram * 0.4:
      -> Route A (Pure Unified)     # plenty of room
  elif model_size < available_ram * 0.8:
      -> Route D (Hybrid)           # tight but fits
  elif model_size < available_ram * 1.5:
      -> Route B (Chunked)          # over RAM, use chunks
  else:
      -> Route C (True Streaming)   # can't fit, must stream
```

### Decision Matrix

| Model | Available RAM | Chosen Route | Chunk Config |
|-------|--------------|--------------|--------------|
| 1B (3GB) | 16GB | A (Unified) | All blocks resident |
| 1B (3GB) | 4GB | D (Hybrid) | Stream load, keep resident |
| 7B (14GB) | 16GB | B (Chunked) | 3 blocks/chunk (Apple's pattern) |
| 7B (14GB) | 8GB | C (Streaming) | 3 blocks/chunk, stream at runtime |
| 70B (140GB) | 64GB | C (Streaming) | 4 blocks/chunk, stream at runtime |

### Pros
- Works across all hardware and model sizes
- Users don't need to understand the trade-offs
- Graceful degradation (best available strategy)
- Future-proof (new strategies can be added)

### Cons
- Most complex to implement (need all strategies + selector)
- Harder to debug ("which mode am I in?")
- Testing matrix is large (N models x M hardware configs)

### Complexity: **High** (implement multiple strategies + detection + selector)

### When to Choose This
- You want to support a wide range of models and hardware
- You want a "just works" experience for users
- You're building a production product, not a prototype

---

## Quantization Impact

All memory calculations above assume FP16 (2 bytes per parameter). Quantization dramatically changes the picture:

| Quantization | Per Block (Llama-3.2-1B) | Full Model (1B) | Full Model (7B) |
|-------------|-------------------------|-----------------|-----------------|
| FP16 (baseline) | 121MB | 3.0GB | 14GB |
| INT8 | 61MB | 1.5GB | 7GB |
| INT4 | 30MB | 0.75GB | 3.5GB |

At INT4, Route C's single-block peak drops from 254MB to ~163MB, and a 7B model fits in 8GB RAM with Route B. Quantization shifts which routes are needed for which model sizes.

---

## Comparison Summary

| Route | Init RAM | Runtime RAM | Disk I/O | Multi-Model | Complexity | Proven By |
|-------|----------|-------------|----------|-------------|------------|-----------|
| A: Pure Unified | 3.0GB | 3.0GB | None | No | Low | Standard |
| B: Chunked | 3.0GB | 3.0GB mapped | None | Partial (RAM-limited) | Medium | **Apple CoreML** |
| C: True Streaming | ~10MB | 254-486MB | 6-16x/pass | Yes | High | ONNX POC |
| D: Hybrid Init | 121MB | 3.0GB | Once | No | Low-Medium | Logical extension |
| E: Adaptive | Varies | Varies | Depends | Depends | High | N/A |

---

## Recommended Phasing (Agent-Consensus)

Three agents independently analyzed this document and converged on this phasing order:

```
Phase 0: Technical Spike (Week 1)
         Validate AMD NPU driver capabilities for unified memory page management.
         This is the #1 program risk — if page_in/page_out APIs don't exist,
         Routes C and D collapse. 1-week spike de-risks the entire plan.

Phase 1: Foundation (Weeks 2-4)
         Build AsyncKVCache + ChunkManager + BufferRegistry.
         This is the shared prerequisite for ALL routes.
         Chunk size is configurable (1, 2, 3, 4, 8 blocks/chunk) for benchmarking.

Phase 2: Route D + Route B — Parallel (Weeks 4-8)
         Route D: Streaming block load at startup, keep resident. (1-2 weeks)
         Route B: Chunked inference with async KV between chunks. (3-4 weeks)
         These share the ChunkManager from Phase 1. Route D adds streaming load;
         Route B adds chunked execution. They can be developed in parallel.

Phase 3: Route C — True Runtime Streaming (Weeks 8-16)
         Add page_in/page_out per forward pass, weight cache with LRU eviction.
         Depends on Phase 1 (ChunkManager + AsyncKVCache) and Phase 2's
         page management primitives from Route D.
         Only begin after Route B is stable and 7B+ model support is needed.

Phase 4: Route E — Adaptive Selector (Weeks 15-20)
         Hardware detection + strategy selection layer.
         Requires Phases 1-3 to exist. Can overlap with late Phase 3.
```

**Why this order over the original D->B->C->E:** The chunking infrastructure (Phase 1) is foundational — it's reused by Routes B, C, and E. Route D (streaming load) and Route B (chunked execution) share this foundation and can be built in parallel. The original plan (Route D first) would have you write an inference loop without chunking, then rewrite it in Phase 2 — wasted effort.

### Success Metrics

| Metric | Target | Phase |
|--------|--------|-------|
| Async KV cache overlap efficiency | >80% compute/KV overlap | Phase 1 |
| Route D startup peak memory | <200MB for 1B model | Phase 2 |
| Route B throughput vs baseline | >=1.1x tokens/sec | Phase 2 |
| Route C peak runtime memory | <500MB for 7B model | Phase 3 |
| Route C decode latency on NVMe | <50ms/token for 7B | Phase 3 |
| Route E strategy selection accuracy | Correct route in >95% of configs | Phase 4 |
| NPU compilation overhead (per chunk) | <500ms | Phase 2 |
| Weight cache hit rate (decode) | >70% after first token | Phase 3 |

### Module Hierarchy

```
iron/model_convert/streaming/
  __init__.py                 # Exports: StreamingBlock, AsyncKVCache, ChunkManager
  async_kv_cache.py           # Phase 1
  chunk_manager.py            # Phase 1
  buffer_registry.py          # Phase 1
  streaming_load.py           # Phase 2 (Route D)
  chunked_inference.py        # Phase 2 (Route B)
  runtime_streaming.py        # Phase 3 (Route C)
  weight_cache.py             # Phase 3 (Route C)
  adaptive_selector.py        # Phase 4 (Route E)
  streaming_infer.py          # New runtime entry point (separate from interactive_convert.py)
```

**Note:** `interactive_convert.py` remains an offline conversion tool. `streaming_infer.py` is a new runtime inference entry point.

---

## Top 3 Program Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| AMD NPU driver lacks page_in/page_out APIs | Medium | Critical | Phase 0 spike. Fallback: mmap/munmap. Secondary: Route B with all weights resident. |
| Route C disk I/O dominates decode (slow storage) | High | High | Weight cache with LRU eviction. Bundle chunk files. Quantization support. I/O prefetching. |
| Integration breaks existing functionality | High | Medium | Feature flags (`streaming_mode=False` default). Separate module hierarchy. `StreamingModelAssembler` alongside existing `ModelAssembler`. |

---

## Prefill vs. Decode Analysis

Every route behaves differently for prefill vs. decode:

| Route | Prefill (T=prompt_len) | Decode (T=1, repeated) |
|-------|-----------------------|------------------------|
| A: Unified | All weights resident. Fast. KV async helps. | All weights resident. Fast. KV async helps. |
| B: Chunked | Chunks loaded once, sequential. KV async between chunks. | Same as prefill (all weights resident, chunked execution). |
| C: Streaming | Each block loaded once. Disk I/O = one-time cost (~0.6s NVMe). | Each block loaded every token. Disk I/O = per-token cost (~0.6s NVMe). |
| D: Hybrid | Identical to Route A (all resident after streaming load). | Identical to Route A. |
| E: Adaptive | Picks best route for prompt length. | Picks best route for decode pattern. |

**Key insight:** Route C's disk I/O is amortized during prefill but incurred every token during decode. This is why Route C requires a weight cache for decode — without it, every token generation reads the entire model from disk.

---

## NPU Compilation Considerations

Each chunk may require NPU-specific compilation at load time. Three strategies:

| Strategy | When | Cost | Memory |
|----------|------|------|--------|
| AOT (Ahead of Time) | At model conversion | One-time, done before deployment | Artifacts stored on disk |
| JIT (Just in Time) | First time chunk is used | Seconds per chunk, one-time | Artifacts cached in memory |
| Pre-compiled | Included with model | Zero at runtime | Artifacts stored on disk |

For Route B and C, AOT or pre-compiled is required. JIT compilation per chunk per forward pass (Route C decode) would be catastrophic. The recommendation is **AOT compilation during model conversion**, storing artifacts alongside weight files.

---

## Windows-Specific Considerations

The target platform is Windows 11 (AMD Ryzen AI). Key differences from Apple's macOS:

| Factor | macOS (Apple) | Windows (AMD) | Impact |
|--------|--------------|---------------|--------|
| Memory-mapped file behavior | Mature, aggressive caching | More conservative, may page out under pressure | Route D's keep_resident may need explicit locking |
| File caching (SuperFetch) | Not applicable | Windows pre-fetches frequently accessed files | May help Route C's weight cache hit rate |
| DMA driver maturity | Mature (Apple controls full stack) | Newer (AMD driver, Windows DDI) | Async KV timing may be less precise |
| Virtual address space | 64-bit, generous | 64-bit, but user-mode limited | Route B's "all weights mapped" may hit limits on 32-bit processes |

---

## Key Differences from Previous Design Doc

| Previous Doc Said | This Doc Says | Why |
|-------------------|--------------|-----|
| "Stream one layer at a time" | "Chunk multiple blocks together" | Apple proved 3-blocks-per-chunk is optimal |
| "mmap load/unload cycles" | "Unified memory page management" | IRON has unified memory — no explicit mmap needed |
| "Async KV per layer" | "Async KV per chunk" | Apple proved chunk-level async KV saves ~20ms |
| "Layer = independent unit" | "Block = self-contained, chunk = execution unit" | Clarified terminology: Block = Layer, Chunk = group of blocks |
| "KV double buffering" | "KV async merge between chunks" | Apple's pattern: return new KV, merge asynchronously |
| "Per block = ~116MB" | "Per block = ~121MB (FP16)" | Corrected weight calculation |
| "Route D first, then B" | "Phase 1: Foundation, then D+B parallel" | Chunking infrastructure is foundational for both |

---

## What Apple's Implementation Proves

| Claim | Apple's Evidence | Applicable to IRON |
|-------|-----------------|-------------------|
| Chunking works | Llama-2-7B runs on ANE | Yes — IRON can chunk blocks too |
| Async KV saves time | ~1-2ms per chunk on 7B | Yes — IRON DMA can overlap with NPU compute |
| 3 blocks/chunk is sweet spot | Used across M1/M3 | **Needs validation** — IRON's AIE columns may prefer different size |
| Tensor reshaping helps | 20% speedup on MLP (ANE-specific) | Principle transfers, not dimensions — IRON needs AIE-optimal shapes |
| Models can be > RAM | CoreML maps, doesn't load | Yes — IRON unified memory does the same |

---

## Clarifying Questions

1. **Chunk size**: Apple uses 3 blocks/chunk. Should IRON use the same, or should we calculate optimal chunk size based on AIE column count (8 columns) and tile sizes (64x64)? **Recommendation: implement as tunable parameter, start with 3, benchmark 2/3/4/8.**

2. **KV cache async**: Should we implement Apple's exact pattern (chunk returns new KV, separate merge happens asynchronously), or a simpler double-buffer approach where KV reads/writes overlap with NPU compute? **Recommendation: Apple's exact pattern — it provides the future-time buffer that makes async work.**

3. **Block file organization**: Currently IRON has 9 separate .npy files per block. Should we bundle each chunk into a single file (like CoreML's .mlpackage per chunk) or keep individual .npy files? **Recommendation: keep individual .npy but add chunk manifest (JSON). Bundle into chunk files only for Route C to reduce seek overhead.**

4. **Tensor reshaping**: Apple proved 20% speedup from reshaping MLP tensors to `(B,C,8,8)`. Should IRON explore similar tensor layout optimizations for its AIE tile sizes? **Recommendation: yes, but target AIE tile sizes (64x64) not Apple's 8x8.**

5. **Block parity**: Should IRON implement both parallel and non-parallel residual patterns (like the `Block` class shows), or commit to one? Llama uses non-parallel residual. **Recommendation: commit to non-parallel residual. Add parallel as special case if a model requires it.**

6. **Max sequence length**: Apple's example caps at a certain context length. Should IRON support dynamic max_seq_len or fix it at compile time? **Recommendation: dynamic with configurable cap. Fix cap at build-time, not hardcoded.**
