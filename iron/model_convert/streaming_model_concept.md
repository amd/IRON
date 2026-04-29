# IRON NPU - Streaming Model Architecture Concept

> Exploring an alternative to the "load everything at once" model pattern.
> Target: Llama-3.2-1B on AMD Ryzen AI NPU

## Current Architecture (Baseline)

```
  SYSTEM RAM (all loaded simultaneously):
  +---------------------------------------------------------+
  |  Embedding Layer      [128256, 2048]     525MB           |
  |  Layer 0  Weights     9 tensors           116MB          |
  |  Layer 1  Weights     9 tensors           116MB          |
  |  Layer 2  Weights     9 tensors           116MB          |
  |  ...                                                      |
  |  Layer 15 Weights     9 tensors           116MB          |
  |  LM Head              [2048, 128256]      525MB          |
  |  KV Cache (16 layers)  growing             128MB-4GB     |
  +---------------------------------------------------------+
  TOTAL: ~2.9GB + KV cache

  DATA FLOW:
  All weights resident in RAM at all times.
  Forward pass streams through layers 0..15 sequentially.
  KV cache grows in place for all 16 layers.
```

## Problem This Solves

The current approach loads **every weight tensor into memory before inference starts**. For a 1.3B model that's ~2.9GB. Fine for a laptop with 16GB RAM. But:

1. **Scaling up**: A 7B model needs ~14GB, a 70B model needs ~140GB. You can't fit them.
2. **Multi-model**: Running multiple models simultaneously requires N * weight_size RAM.
3. **KV cache pressure**: At long context (S=4096+), KV cache adds 128MB+ on top of weights.
4. **NPU bottleneck**: The NPU can only compute one layer at a time anyway, so loading all weights doesn't speed up inference -- it just wastes RAM.

---

## Concept A: Streaming Layers (Layer-at-a-Time)

Process one layer at a time, loading weights on demand.

```
  ITERATION i (for each layer i = 0..15):
  +---------------------------------------------------------+
  |  Layer i Weights     9 tensors           ~116MB          |
  |  KV Cache (ALL 16)   for layer i only     growing        |
  +---------------------------------------------------------+
  PEAK MEMORY: ~116MB + KV cache (not 2.9GB)
```

```
  DATA FLOW:

  [Embedding] -> hidden [1, T, 2048]
       |
       v
  +------------------+
  | LOAD Layer 0     |  <- DMA from disk / npy files
  | Compute L0       |  <- NPU runs 15 ops
  | UNLOAD Layer 0   |  <- free 116MB
  +------------------+
       |
       v  hidden [1, T, 2048]
  +------------------+
  | LOAD Layer 1     |
  | Compute L1       |
  | UNLOAD Layer 1   |
  +------------------+
       |
       v
  ... (repeat for layers 2-15)
       |
       v
  [Final Norm] -> [LM Head] -> logits [1, T, 128256]

  KV CACHE: Async, pre-allocated in system RAM
  Each layer's K/V is DMA'd from/to its own region.
  KV cache persists across layer iterations.
```

### Trade-offs

| Aspect | Current (All Loaded) | Streaming (Layer-at-a-Time) |
|--------|---------------------|----------------------------|
| RAM usage | ~2.9GB + KV cache | ~116MB + KV cache |
| Max model size | Limited by total RAM | Limited by single-layer RAM |
| Prefill latency | Lower (weights always in RAM) | Higher (16 load/unload cycles) |
| Decode latency | Lower | Higher (same 16 load/unload cycles) |
| Multi-model | No (OOM) | Possible (swap between models) |
| Disk I/O | Once at startup | Every forward pass |

### When This Wins

- Running models larger than available RAM
- Multi-model serving (swap between models without reloading)
- Edge devices with tight memory budgets
- Cold start: first token latency for small prompts

---

## Concept B: Async KV Cache (Decoupled from Compute)

Currently, KV cache is tightly coupled to the forward pass -- each layer reads/writes its KV slice synchronously. What if KV cache operations were async?

```
  CURRENT (Sync):
  Layer i:
    1. DMA READ K_cache[i] from RAM     <- blocks
    2. DMA READ V_cache[i] from RAM     <- blocks
    3. AIE COMPUTE attention            <- blocks
    4. DMA WRITE new K[i] to RAM        <- blocks
    5. DMA WRITE new V[i] to RAM        <- blocks

  PROPOSED (Async):
  Layer i:
    1. Issue DMA READ K_cache[i]        <- non-blocking
    2. Issue DMA READ V_cache[i]        <- non-blocking
    3. COMPUTE Q_proj + K_proj          <- overlaps with DMA
    4. DMA completes, COMPUTE attention <- no idle time
    5. Issue DMA WRITE K/V (double buf) <- non-blocking
    6. COMPUTE O_proj + MLP            <- overlaps with DMA

  DOUBLE BUFFERING:
  Buffer A: Layer i reads from K_cache_A[i]
  Buffer B: Layer i+1 pre-fetches K_cache_B[i+1]
  While layer i computes, layer i+1's KV is already loading.
```

```
  TIMELINE (Decode, S=1000):

  Time ---->
  Layer 0: [DMA READ K/V] [COMPUTE] [DMA WRITE]
  Layer 1:       [DMA READ K/V] [COMPUTE] [DMA WRITE]
  Layer 2:             [DMA READ K/V] [COMPUTE] [DMA WRITE]
  Layer 3:                   [DMA READ K/V] [COMPUTE] [DMA WRITE]

  VS PIPELINED (Async):
  Layer 0: [DMA READ][COMPUTE    ][DMA WRITE]
  Layer 1:          [DMA READ][COMPUTE    ][DMA WRITE]
  Layer 2:                   [DMA READ][COMPUTE    ][DMA WRITE]
  Layer 3:                            [DMA READ][COMPUTE    ][DMA WRITE]

  DMA and COMPUTE overlap. No idle cycles.
```

### KV Cache as Independent Subsystem

```
  +-------------------+     +-------------------+
  |  KV Cache Manager |     |  Compute Engine   |
  |                   |     |                   |
  |  - Pre-allocates  |     |  - Loads weights  |
  |    all K/V slots  |-----|    only for layer i|
  |  - DMA prefetches |     |  - Reads KV from  |
  |    next layer's   |     |    manager's buffer|
  |    KV into SRAM   |     |  - Writes new K/V |
  |  - Manages eviction|    |    back to manager|
  |  - Paging/swap    |     |                   |
  +-------------------+     +-------------------+
         ^                          ^
         |                          |
    System RAM                 AIE NPU Cores
    (KV data)                  (compute)
```

---

## Concept C: Unified Streaming Block

Combine A + B: A single "complete block" abstraction that owns one layer's weights + its async KV interface.

```
  STREAMING BLOCK (one instance, reused 16 times):
  +-----------------------------------------------------------+
  |                                                           |
  |  +-------------------+    +---------------------------+   |
  |  |  Weight Loader    |    |  KV Cache Interface       |   |
  |  |                   |    |                           |   |
  |  |  - Loads layer i  |--->|  - Async DMA K/V[i]       |   |
  |  |  - 116MB max      |    |  - Double-buffered        |   |
  |  |  - npy mmap       |    |  - Prefetch next layer    |   |
  |  |  - Free on swap   |    |  - Page/evict if needed   |   |
  |  +-------------------+    +---------------------------+   |
  |         |                          |                      |
  |         v                          v                      |
  |  +---------------------------------------------------+   |
  |  |              AIE Compute Pipeline                  |   |
  |  |                                                   |   |
  |  |  RMSNorm -> Q_proj -> K_proj -> V_proj -> RoPE   |   |
  |  |  -> Attention -> O_proj -> RMSNorm -> Gate       |   |
  |  |  -> Up -> SiLU -> Mul -> Down -> Residual        |   |
  |  +---------------------------------------------------+   |
  |         |                                                  |
  |         v  hidden [1, T, 2048] (passed to next iter)      |
  +-----------------------------------------------------------+

  EXECUTION:
  for layer_id in range(16):
      block.load_weights(layer_id)       # 116MB from .npy
      block.prefetch_kv(layer_id + 1)    # async, next layer
      block.forward(hidden, layer_id)    # NPU compute
      block.release_weights(layer_id)    # free 116MB
      hidden = block.output              # pass to next
```

### Memory Comparison (Llama-3.2-1B, S=4096)

| Component | Current | Streaming + Async KV |
|-----------|---------|---------------------|
| Embedding | 525MB | 525MB (mmap, not resident) |
| Layer weights (all 16) | 1.86GB | 116MB (one layer) |
| LM Head | 525MB | 525MB (mmap, not resident) |
| KV Cache | 128MB | 128MB (same, but double-buffered) |
| **Peak RAM** | **~3.0GB** | **~1.3GB** |
| Disk I/O | Once | 16x per forward pass |

---

## Clarifying Questions

1. **Mmap weights**: Should embedding and LM head stay mmap'd (loaded on access, not resident) or should they also stream? Embedding is 525MB -- if we mmap it, the lookup is slower but peak RAM drops.

2. **Decode vs Prefill**: Streaming helps prefill more (sequential compute anyway) but hurts decode more (you do 16 load/unload cycles per single token). Is the trade-off acceptable, or should decode use a different strategy?

3. **Weight caching**: Should we keep the last-used layer's weights in RAM as a "hot cache"? If attention is iterative, layers 0-3 might get hit more often in autoregressive generation.

4. **KV cache paging**: At very long context (S > 16K), should the KV Cache Manager evict old tokens to disk/swap? This would let you run 128K context on 8GB RAM, but with latency spikes on cache misses.

5. **Multi-model**: Is running multiple models simultaneously a goal? Streaming architecture makes this trivial (swap weights between models), but if it's not a use case, the added complexity might not be worth it.

6. **Disk speed matters**: Streaming loads weights every forward pass. On a slow HDD, 116MB * 16 layers = 1.86GB of reads per token (decode) could be 3-10 seconds. On NVMe, it's ~0.6 seconds. Does this need to be gated on storage speed?

7. **Layer grouping**: Instead of one layer at a time, should we load N layers at once (e.g., groups of 4)? This gives a middle ground: 4 * 116MB = 464MB peak instead of 2.9GB, but only 4 load/unload cycles instead of 16.

---

## Summary

| Concept | What Changes | Main Benefit | Main Cost |
|---------|-------------|-------------|-----------|
| A: Streaming Layers | Load one layer at a time | 25x less RAM | Disk I/O per layer |
| B: Async KV Cache | Decouple KV from compute | Overlap DMA + compute | Double-buffer memory |
| C: Unified Block | A + B combined | Best of both | Most complex |

The key insight: **the NPU computes one layer at a time anyway**. Loading all 16 layers' weights simultaneously doesn't speed anything up -- it just holds 2.9GB of RAM hostage. Streaming reclaims that RAM by loading only what's needed, when it's needed.
