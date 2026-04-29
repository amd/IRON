# IRON NPU - Streaming Block + Async KV Cache Design

> Mapping the ONNX "True Runnable Split" concept to IRON NPU architecture.
> Inspired by: amd/Qwen2.5-0.5B-Instruct ONNX POC (28 independent subgraphs, Transient Session Pattern)

---

## 1. What I Think You're Looking For

You want to port the ONNX "Transient Session Pattern" to IRON's NPU. The idea:

- **Split** the monolithic model into independent, runnable layer blocks
- **Stream** one layer at a time through the NPU (load weights -> compute -> unload)
- **Async KV Cache** decouples memory transfer from compute, double-buffering KV data so DMA overlaps with NPU execution
- **Buffer Registry** acts as shared memory for tensors that cross layer boundaries (hidden_states, KV cache entries)

The ONNX POC proved this works for CPU inference with ORT sessions. You want the equivalent for AMD NPU, where the compute primitives are AIE columns, DMA engines, and compiled `.xclbin` artifacts instead of ORT sessions.

**The key advantage**: IRON's existing `.npy` file format is already perfectly suited for this. The ONNX POC had to split a 779MB monolith into 28 files. IRON already has 147 individual weight files. No splitting needed -- just load them in the right order.

---

## 2. ONNX-to-IRON Concept Mapping

| ONNX Concept | IRON NPU Equivalent | Notes |
|---|---|---|
| `embeddings.onnx` (519MB) | `embedding.npy` (525MB, mmap'd) | Already separate file |
| `layer_0..23.onnx` (15.6MB each) | `layer_N/*.npy` (9 files, ~116MB) | Already separate files |
| `lm_head.onnx` (69.5MB) | `lm_head.npy` (525MB, mmap'd) | Already separate file |
| `other.onnx` (dispatcher) | `BufferRegistry` + `StreamingRunner` | New component |
| ORT Session (per layer) | `StreamingBlock` (per layer) | NPU compute unit |
| Session load/unload | mmap load/release + AIE reconfigure | No compilation needed if artifacts pre-built |
| tensor_registry dict | `BufferRegistry` class | Manages hidden_states + KV cache |
| Typed handshakes (INT32) | Buffer interface contracts (shape, dtype, alignment) | NPU requires strict alignment |
| disable_node_shape_check | Streaming mode skips shape validation | Same idea: trust the contract |
| MatMulNBits (INT4 quant) | Dequant operator (future) | ONNX uses INT4, IRON uses bf16 |
| GroupQueryAttention op | Separate Q/K/V + MHA + RoPE ops | IRON decomposes GQA into individual ops |
| External data linking | `weight_manifest.json` -> .npy paths | Same concept, different format |
| Metadata inheritance | `TilingConfig` + `PaddedShape` per block | Each block carries its own shape info |
| Mutual exclusivity | Only one layer's weights resident | mmap handles this natively |

---

## 3. Architecture: Streaming Block

Each `StreamingBlock` is a self-contained, independently runnable unit that represents one transformer layer.

### 3.1 Block Structure

```
  STREAMING BLOCK (Layer N):
  +----------------------------------------------------------------+
  |  BLOCK METADATA (from manifest)                                |
  |  - layer_id: int                                               |
  |  - weight_files: List[Path]  (9 .npy paths)                   |
  |  - tiling_config: TilingConfig  (M=64, K=64, N=64)           |
  |  - shapes: Dict[str, PaddedShape]  (input/output contracts)   |
  |  - dtype: np.dtype  (bfloat16)                                 |
  +----------------------------------------------------------------+
  |  WEIGHT LOADER (Transient)                                     |
  |  - mmap_load(weights)  -> Dict[str, np.ndarray]               |
  |  - mmap_release()      -> None                                |
  |  Peak: ~116MB (Llama-3.2-1B) per load                         |
  +----------------------------------------------------------------+
  |  NPU OPERATORS (Built or Pre-compiled)                         |
  |  [1]  RMSNorm_1    (size=2048)                                 |
  |  [2]  Q_proj GEMM   (M=T, K=2048, N=2048)                     |
  |  [3]  K_proj GEMM   (M=T, K=2048, N=512)                      |
  |  [4]  V_proj GEMM   (M=T, K=2048, N=512)                      |
  |  [5]  RoPE          (seq_len=T, head_dim=64)                   |
  |  [6]  Attention GQA (num_heads=32, num_kv=8, S=cache_len)     |
  |  [7]  O_proj GEMM   (M=T, K=2048, N=2048)                     |
  |  [8]  RMSNorm_2    (size=2048)                                 |
  |  [9]  Gate_proj GEMM(M=T, K=2048, N=8192)                     |
  |  [10] Up_proj GEMM (M=T, K=2048, N=8192)                      |
  |  [11] SiLU          (size=T*8192)                              |
  |  [12] ElementwiseMul(size=T*8192)                              |
  |  [13] Down_proj GEMM(M=T, K=8192, N=2048)                     |
  |  [14] Residual Add  (size=T*2048) x2                          |
  +----------------------------------------------------------------+
  |  BUFFER INTERFACE (Handshakes)                                 |
  |  Input:  hidden_states [1, T, 2048] from BufferRegistry        |
  |  Output: hidden_states [1, T, 2048] to   BufferRegistry        |
  |  KV:     K/V [8, T, 64] per layer to   AsyncKVCache           |
  +----------------------------------------------------------------+
```

### 3.2 Block Lifecycle

```
  INIT (once at startup):
  - Read manifest.json to discover all layer blocks
  - Pre-build AIE operator pipelines (or pre-compile artifacts)
  - Allocate BufferRegistry (hidden_states buffer)
  - Allocate AsyncKVCache (K/V buffers for all layers)

  PREFILL (prompt tokens, T = prompt_len):
  for layer_id in 0..15:
      block = StreamingBlock(layer_id)           # get block metadata
      block.load_weights()                        # mmap 9 .npy files (~116MB)
      block.async_kv.prefetch(layer_id + 1)       # non-blocking KV load
      hidden = block.forward(hidden, layer_id)    # NPU compute
      block.async_kv.append(layer_id, K, V)       # async KV write
      block.release_weights()                     # unmap 9 .npy files

  DECODE (single token, T = 1):
  for layer_id in 0..15:
      block = StreamingBlock(layer_id)
      block.load_weights()                        # mmap 9 .npy files
      block.async_kv.prefetch(layer_id + 1)       # non-blocking KV load
      hidden = block.forward(hidden, layer_id)    # NPU compute (T=1)
      block.async_kv.append(layer_id, K, V)       # async KV write
      block.release_weights()                     # unmap
```

### 3.3 Memory Comparison

| Component | Current (All Loaded) | Streaming Block |
|-----------|---------------------|-----------------|
| Embedding | 525MB resident | 525MB mmap'd (pages on access) |
| Layer weights (all 16) | 1.86GB resident | 116MB resident (one layer) |
| LM Head | 525MB resident | 525MB mmap'd (pages on access) |
| KV Cache (S=4096) | 128MB | 128MB (same) + optional 128MB double buffer |
| AIE buffers | ~50MB | ~50MB (same) |
| **Peak RAM** | **~3.0GB** | **~819MB** (single buffer) or **~947MB** (double buffer) |

---

## 4. Architecture: Async KV Cache

The KV Cache runs as an independent subsystem, decoupled from compute.

### 4.1 Design

```
  ASYNC KV CACHE MANAGER:
  +----------------------------------------------------------------+
  |  PRE-ALLOCATED BUFFERS (System RAM)                            |
  |  K_cache[16, num_kv_heads, max_seq_len, head_dim]              |
  |  V_cache[16, num_kv_heads, max_seq_len, head_dim]              |
  |  Llama-3.2-1B: 16 * 8 * 4096 * 64 * 2 * 2 = 128MB            |
  +----------------------------------------------------------------+
  |  DOUBLE BUFFERING (Optional)                                   |
  |  Buffer A: Active read/write for current layer                 |
  |  Buffer B: Prefetch for next layer                             |
  |  Swap pointers between layers (zero-copy)                      |
  +----------------------------------------------------------------+
  |  DMA ENGINE (Async)                                            |
  |  - prefetch(layer_id)  -> issues non-blocking read             |
  |  - append(layer_id, K, V) -> issues non-blocking write         |
  |  - wait(layer_id) -> blocks until DMA completes                |
  +----------------------------------------------------------------+
  |  KV CACHE LAYOUT (per layer):                                  |
  |  K[layer_id]: [num_kv_heads, seq_len, head_dim]               |
  |  V[layer_id]: [num_kv_heads, seq_len, head_dim]               |
  |  Llama-3.2-1B: K/V each [8, 4096, 64] = 4MB per layer        |
  +----------------------------------------------------------------+
```

### 4.2 Async Timeline (Decode, S=1000)

```
  CURRENT (Sync):
  Layer 0: [DMA K/V READ 32MB] [NPU 976M MACs] [DMA K/V WRITE 32KB]
  Layer 1:                          [DMA K/V READ 32MB] [NPU 976M MACs] [DMA K/V WRITE 32KB]
  Layer 2:                                                   [DMA K/V READ 32MB] [NPU 976M MACs] [DMA K/V WRITE 32KB]
  ...

  PROPOSED (Async + Double Buffer):
  Layer 0: [DMA K/V READ 32MB][NPU 976M MACs        ][DMA K/V WRITE 32KB]
  Layer 1:           [DMA K/V READ 32MB][NPU 976M MACs        ][DMA K/V WRITE 32KB]
  Layer 2:                    [DMA K/V READ 32MB][NPU 976M MACs        ][DMA K/V WRITE 32KB]
  Layer 3:                             [DMA K/V READ 32MB][NPU 976M MACs        ][DMA K/V WRITE 32KB]

  DMA overlaps with NPU compute. No idle cycles.
  At S=1000: 32MB DMA per layer, ~50ms NPU per layer.
  If DMA < NPU time, DMA is free (hidden behind compute).
```

### 4.3 KV Cache Interface Contract

```python
class AsyncKVCache:
    """Manages KV cache with async DMA for streaming layers."""

    def __init__(
        self,
        num_layers: int,        # 16
        num_kv_heads: int,      # 8
        max_seq_len: int,       # 4096
        head_dim: int,          # 64
        double_buffer: bool = False,  # 2x memory, better overlap
    ):
        # Pre-allocate: [num_layers, num_kv_heads, max_seq_len, head_dim]
        self.k_cache = np.zeros(...)   # bf16
        self.v_cache = np.zeros(...)   # bf16
        if double_buffer:
            self.k_cache_b = np.zeros(...)
            self.v_cache_b = np.zeros(...)
        self.active_buffer = "A"

    def get(self, layer_id: int, seq_start: int, seq_len: int) -> tuple:
        """Get K/V slice for layer_id[seq_start:seq_start+seq_len]."""
        k = self.k_cache[layer_id, :, seq_start:seq_start+seq_len, :]
        v = self.v_cache[layer_id, :, seq_start:seq_start+seq_len, :]
        return k, v

    def append(self, layer_id: int, pos: int, k: np.ndarray, v: np.ndarray):
        """Append new K/V at position pos. Async if double-buffered."""
        self.k_cache[layer_id, :, pos:pos+k.shape[1], :] = k
        self.v_cache[layer_id, :, pos:pos+v.shape[1], :] = v

    def prefetch(self, next_layer_id: int):
        """Pre-fetch next layer's KV into double buffer. Non-blocking."""
        # Only meaningful with double buffering.
        # Triggers DMA to load next layer's KV from RAM to NPU-local memory.
        pass
```

---

## 5. Architecture: Buffer Registry

The `BufferRegistry` is the shared memory that replaces ONNX's `tensor_registry`.

```
  BUFFER REGISTRY:
  +----------------------------------------------------------------+
  |  REGISTERED BUFFERS                                            |
  |  - hidden_states: np.ndarray [1, max_T, 2048] bf16            |
  |    (Passed between all layers: output of N -> input of N+1)    |
  |                                                                |
  |  - attention_mask: np.ndarray [1, 1, T, S] bf16               |
  |    (Causal mask, computed once, reused by all layers)          |
  |                                                                |
  |  - rope_angles: np.ndarray [max_seq_len, head_dim] bf16       |
  |    (Precomputed RoPE frequencies, reused by all layers)        |
  |                                                                |
  |  - position_ids: np.ndarray [1, T] int32                      |
  |    (Position indices for current forward pass)                 |
  +----------------------------------------------------------------+
  |  BUFFER LIFECYCLE                                              |
  |  allocate(name, shape, dtype) -> np.ndarray                    |
  |  get(name) -> np.ndarray                                       |
  |  set(name, data) -> None                                       |
  |  release(name) -> None                                         |
  |  clear() -> None (releases all, keeps allocation pool)         |
  +----------------------------------------------------------------+
  |  TYPED HANDHAKES                                               |
  |  Each buffer has a contract:                                   |
  |  - Shape: exact dimensions (with padding for AIE alignment)    |
  |  - dtype: bfloat16 for activations, int32 for masks/ids        |
  |  - Alignment: buffer must be page-aligned (4096 bytes)         |
  |  - Contiguity: C-contiguous for DMA                            |
  +----------------------------------------------------------------+
```

### 5.1 Data Flow Through Registry

```
  PREFILL:
  [Tokenizer] -> token_ids [1, 8]
      |
      v
  [Embedding] -> hidden_states [1, 8, 2048]
      |
      v
  BufferRegistry.set("hidden_states", hidden)

  for layer_id in 0..15:
      hidden = BufferRegistry.get("hidden_states")  # input
      mask   = BufferRegistry.get("attention_mask")  # read-only
      angles = BufferRegistry.get("rope_angles")     # read-only

      block = StreamingBlock(layer_id)
      block.load_weights()
      output = block.forward(hidden, mask, angles, kv_cache)

      BufferRegistry.set("hidden_states", output)     # output (overwrites)
      block.release_weights()

  FINAL:
  hidden = BufferRegistry.get("hidden_states")
  [Final Norm] -> [LM Head] -> logits [1, 8, 128256]
  [Sample] -> next_token
```

---

## 6. Complete Pipeline: Streaming + Async KV

```
  +==========================================================================+
  |  STREAMING NPU INFERENCE PIPELINE                                        |
  +==========================================================================+

  INIT (once):
  +--------------------------------------------------------------------------+
  |  1. Load manifest.json -> discover all layers, weights, shapes          |
  |  2. Build StreamingBlocks for all 16 layers (operator graphs)            |
  |  3. Pre-compile AIE artifacts (optional: compile at layer load time)    |
  |  4. Allocate BufferRegistry (hidden_states, mask, angles, pos_ids)       |
  |  5. Allocate AsyncKVCache (K/V for all 16 layers)                        |
  |  6. mmap embedding.npy (lazy, on-access)                                 |
  |  7. mmap lm_head.npy (lazy, on-access)                                   |
  |  PEAK INIT MEMORY: ~128MB (KV cache) + buffers (~10MB)                  |
  +--------------------------------------------------------------------------+

  PREFILL (T = prompt_len):
  +--------------------------------------------------------------------------+
  |  1. Tokenize prompt -> token_ids [1, T]                                  |
  |  2. Embed: mmap embedding -> lookup -> hidden [1, T, 2048]               |
  |  3. Precompute: attention_mask [1,1,T,T], rope_angles [T,64]             |
  |  4. Register in BufferRegistry                                           |
  |  5. for layer_id in 0..15:                                               |
  |     a. StreamingBlock.load_weights()        <- mmap 9 .npy (116MB)       |
  |     b. AsyncKVCache.prefetch(layer_id + 1)  <- non-blocking KV read      |
  |     c. hidden = block.forward(hidden, ...)  <- NPU compute               |
  |     d. AsyncKVCache.append(layer_id, K, V)  <- async KV write            |
  |     e. StreamingBlock.release_weights()     <- unmap 9 .npy              |
  |  6. Final Norm -> LM Head (mmap) -> logits [1, T, 128256]               |
  |  7. Sample -> next_token_id                                              |
  |  PEAK MEMORY: ~116MB (one layer) + 128MB (KV) + 10MB (buffers) = 254MB  |
  +--------------------------------------------------------------------------+

  DECODE (T = 1, repeat until EOS):
  +--------------------------------------------------------------------------+
  |  1. Embed single token -> hidden [1, 1, 2048]                            |
  |  2. for layer_id in 0..15:                                               |
  |     a. StreamingBlock.load_weights()        <- mmap 9 .npy (116MB)       |
  |     b. AsyncKVCache.prefetch(layer_id + 1)  <- non-blocking KV read      |
  |     c. hidden = block.forward(hidden, ...)  <- NPU compute (T=1)         |
  |     d. AsyncKVCache.append(layer_id, K, V)  <- async KV write            |
  |     e. StreamingBlock.release_weights()     <- unmap 9 .npy              |
  |  3. LM Head (mmap) -> logits [1, 1, 128256]                              |
  |  4. Sample -> next_token_id                                              |
  |  5. position += 1; if EOS: break                                        |
  |  PEAK MEMORY: ~116MB (one layer) + KV (growing) + 10MB = ~254MB + KV    |
  +--------------------------------------------------------------------------+
```

---

## 7. Implementation Plan

### 7.1 New Module Structure

```
iron/model_convert/
  streaming/
    __init__.py           # Exports: StreamingBlock, AsyncKVCache, BufferRegistry, StreamingRunner
    block.py              # StreamingBlock class (per-layer runnable unit)
    kv_cache.py           # AsyncKVCache class (double-buffered KV management)
    registry.py           # BufferRegistry class (shared tensor memory)
    runner.py             # StreamingRunner class (orchestrates prefill + decode)
    manifest.py           # StreamingManifest class (reads/writes layer metadata)
    test_streaming.py     # Unit tests for each component
```

### 7.2 Phase 1: Core Components (No NPU)

| Component | What It Does | Dependencies |
|-----------|-------------|-------------|
| `StreamingManifest` | Reads `manifest.json`, validates layer metadata | json, pathlib |
| `BufferRegistry` | Allocates/manages hidden_states, mask, angles buffers | numpy |
| `AsyncKVCache` | Pre-allocates KV cache, provides get/append/prefetch | numpy |

### 7.3 Phase 2: Streaming Block

| Component | What It Does | Dependencies |
|-----------|-------------|-------------|
| `StreamingBlock` | Load/unload layer weights, build AIE operator pipeline | OperatorFactory, LayerBuilder, WeightMapper |
| `WeightLoader` (streaming) | mmap-based weight loading for 9 .npy files per layer | numpy, pathlib |

### 7.4 Phase 3: Streaming Runner

| Component | What It Does | Dependencies |
|-----------|-------------|-------------|
| `StreamingRunner` | Orchestrates prefill + decode using all components | All above |
| Integration with `GenerationLoop` | Replace monolithic forward pass with streaming | generation/loop.py |

---

## 8. Memory Scaling Comparison

### Llama-3.2-1B (16 layers)

| Scenario | Current (All Loaded) | Streaming Block |
|----------|---------------------|-----------------|
| Init | 3.0GB | ~10MB (buffers only) |
| Prefill (T=100) | 3.0GB + ~140MB activations | ~254MB |
| Decode (S=100) | 3.0GB + 32KB KV | ~148MB |
| Decode (S=4096) | 3.0GB + 128MB KV | ~382MB |
| Decode (S=131072) | 3.0GB + 4GB KV | ~4.1GB |

### Qwen2.5-7B (28 layers, hypothetical)

| Scenario | Current (All Loaded) | Streaming Block |
|----------|---------------------|-----------------|
| Init | ~14GB | ~20MB (buffers only) |
| Prefill (T=100) | 14GB + ~500MB activations | ~700MB |
| Decode (S=4096) | 14GB + 512MB KV | ~640MB |

**Key insight**: Streaming makes RAM scale with **layer size**, not **model size**. This enables running 70B models on hardware that can only hold 7B in RAM.

---

## 9. Clarifying Questions

1. **AIE compilation strategy**: Should we pre-compile AIE artifacts for all layers at startup (one-time cost, artifacts stay in memory ~50MB), or compile each layer on-demand when it's loaded (no artifact memory, but adds compile latency per layer per forward pass)? For decode, this is per-token, so on-demand compilation would be very expensive.

2. **Weight file format**: Keep individual `.npy` files (current format, 9 per layer) or bundle each layer into a single `layer_N.npy` (one mmap per layer instead of 9)? The ONNX POC uses one file per layer. Bundling reduces mmap overhead but increases individual file size.

3. **Embedding/LM Head streaming**: Should embedding and LM Head also stream (mmap on access, unmap after) or stay mmap'd resident? They're the largest single components (525MB each). If mmap'd, they contribute ~0MB to peak RAM but add page fault latency. If resident, they're always in RAM.

4. **Layer grouping**: Instead of strictly one layer at a time, should we support configurable group sizes? E.g., load layers 0-3 together (464MB), compute them, then load 4-7, etc. This reduces load/unload cycles from 16 to 4 (for groups of 4) while still being much better than loading all 16.

5. **KV cache double buffering**: Enable by default? It doubles KV cache memory (128MB -> 256MB at S=4096) but can fully hide KV DMA behind NPU compute. If the NPU compute is slower than DMA (likely for decode T=1), double buffering doesn't help and wastes memory.

6. **Multi-model support**: Is running multiple models simultaneously a requirement? The streaming architecture makes this natural (switch between models by swapping active weights), but adds complexity to the BufferRegistry and KV Cache manager.

7. **Disk I/O bottleneck**: For decode, you do 16 load/unload cycles per token. At 116MB per load, that's 1.86GB of reads per token. On NVMe (~3GB/s), that's ~0.6 seconds just for disk I/O. On a slower SSD (~500MB/s), it's ~3.7 seconds. Is this acceptable, or should we add a weight cache (keep recently-used layers in RAM)?

8. **Integration point**: Should this be a new entry point (`python -m iron.model_convert.streaming`) or a mode within the existing `interactive_convert.py`? Or should it replace the current `model_assembler.py` entirely?
