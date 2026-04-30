# IRON NPU - Streaming Architecture: Comprehensive Testing Strategy

> **Author**: Morgan Rodriguez, Senior QA Engineer & Test Automation Architect
> **Date**: 2026-04-29
> **Branch**: `feature/model-converter-analysis`
> **Context**: Based on analysis of `streaming_model_concept.md`, `streaming_block_design.md`, `streaming_architecture_routes.md`, and `STREAMING_PROGRESS.md`

---

## Executive Summary

This testing strategy covers **~220+ tests** across 4 categories (unit, integration, performance, regression) for the 5-phase streaming architecture initiative. The core design principle: **no NPU hardware required** for any test to pass. A `FakeNPUComputeEngine` (numpy-based emulation layer) replaces actual NPU operators, enabling deterministic, fast, platform-independent testing.

| Category | Test Count | Runs When | Pass Required For |
|----------|-----------|-----------|-------------------|
| Unit tests | ~150 | Every push/PR | Merge to main |
| Integration tests | ~30 | Every push/PR | Merge to main |
| Performance benchmarks | ~15 | Weekly schedule | Regression alert only |
| Regression tests | ~25 | Every push/PR | Merge to main |

---

## 1. Unit Testing

### 1.1 AsyncKVCache (`test_async_kv_cache.py`)

**Component**: `streaming/async_kv_cache.py` -- pre-allocates K/V buffers, manages get/append/prefetch, async KV merge between chunks.

#### Core Construction Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U1 | `test_async_kv_cache_init_default()` | Buffer shape `[num_layers, num_kv_heads, max_seq_len, head_dim]`, dtype bf16, `double_buffer=False` by default |
| U2 | `test_async_kv_cache_init_double_buffer()` | 2x buffer allocation (A + B), `active_buffer` starts at `"A"` |
| U3 | `test_async_kv_cache_init_custom_params()` | Custom `num_layers`, `num_kv_heads`, `max_seq_len`, `head_dim` correctly applied |
| U4 | `test_async_kv_cache_init_invalid_params()` | Raises `ValueError` for `num_layers <= 0`, `head_dim <= 0`, `max_seq_len <= 0` |
| U5 | `test_async_kv_cache_zero_initialized()` | All buffer values are exactly `0.0` after construction |

#### Get/Append Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U6 | `test_async_kv_cache_get_valid_slice()` | `get(layer_id, seq_start, seq_len)` returns `(K, V)` with shape `[num_kv_heads, seq_len, head_dim]` |
| U7 | `test_async_kv_cache_get_out_of_bounds_layer()` | Raises `ValueError` for `layer_id >= num_layers` |
| U8 | `test_async_kv_cache_get_out_of_bounds_seq()` | Raises `ValueError` for `seq_start + seq_len > max_seq_len` |
| U9 | `test_async_kv_cache_get_negative_params()` | Raises `ValueError` for negative `seq_start` or `seq_len <= 0` |
| U10 | `test_async_kv_cache_get_zero_length()` | Returns empty arrays with correct shape for `seq_len=0` |
| U11 | `test_async_kv_cache_get_single_token()` | Returns correct shape for `seq_len=1` (decode mode) |
| U12 | `test_async_kv_cache_append_valid()` | `append(layer_id, pos, K, V)` writes data retrievable via subsequent `get()` |
| U13 | `test_async_kv_cache_append_overwrite()` | Append at same position overwrites previous data (idempotent write) |
| U14 | `test_async_kv_cache_append_out_of_bounds_pos()` | Raises `ValueError` for `pos + k.shape[1] > max_seq_len` |
| U15 | `test_async_kv_cache_append_wrong_shape()` | Raises `ValueError` when K/V shape doesn't match expected `[num_kv_heads, seq_len, head_dim]` |
| U16 | `test_async_kv_cache_append_wrong_dtype()` | Raises `ValueError` when K/V dtype doesn't match bf16 |
| U17 | `test_async_kv_cache_append_full_sequence()` | Append at positions `0, 1, ..., max_seq_len-1` fills entire buffer correctly |

#### Prefetch/Double-Buffer Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U18 | `test_async_kv_cache_prefetch_single_buffer_noop()` | `prefetch()` is no-op when `double_buffer=False` (logs warning) |
| U19 | `test_async_kv_cache_prefetch_double_buffer()` | Data loaded into buffer B, `active_buffer` still A |
| U20 | `test_async_kv_cache_buffer_swap()` | `swap_buffers()` switches `active_buffer` A->B, data accessible from new active buffer |
| U21 | `test_async_kv_cache_double_buffer_independence()` | Buffer A and Buffer B modifications don't affect each other |
| U22 | `test_async_kv_cache_prefetch_out_of_bounds_layer()` | Raises `ValueError` for prefetch of non-existent layer |

#### Async KV Merge Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U23 | `test_async_kv_cache_kv_merge_async()` | Async merge completes before next chunk needs data (uses `threading.Event` for timing) |
| U24 | `test_async_kv_cache_kv_merge_timing()` | Merge completes within expected time budget (configurable `max_seq_len * dma_latency`) |
| U25 | `test_async_kv_cache_kv_merge_failure_recovery()` | Failed merge (simulated timeout) can be retried without corrupting data |
| U26 | `test_async_kv_cache_kv_merge_sequential_chunks()` | Multiple chunk merges in sequence don't interfere with each other |

#### Edge Cases

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U27 | `test_async_kv_cache_dtype_preservation()` | bf16 preserved through complete get/append/prefetch/swap cycle |
| U28 | `test_async_kv_cache_memory_bounds()` | Buffer allocation doesn't exceed expected memory (`num_layers * num_kv_heads * max_seq_len * head_dim * 2 bytes * 2 for double buffer`) |
| U29 | `test_async_kv_cache_concurrent_access()` | Thread-safe: concurrent `get()` and `append()` from different threads don't corrupt data |
| U30 | `test_async_kv_cache_large_seq_len()` | Handles `max_seq_len=131072` (edge case for 128K context) without OOM |

---

### 1.2 BufferRegistry (`test_buffer_registry.py`)

**Component**: `streaming/buffer_registry.py` -- manages hidden_states, attention_mask, rope_angles, position_ids with typed contracts (shape, dtype, alignment, contiguity).

#### Allocation Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U31 | `test_buffer_registry_allocate_basic()` | `allocate(name, shape, dtype)` creates buffer with correct shape and dtype |
| U32 | `test_buffer_registry_allocate_hidden_states()` | `[1, max_T, dim]` bf16 allocated, zero-initialized |
| U33 | `test_buffer_registry_allocate_attention_mask()` | `[1, 1, T, S]` bf16 allocated |
| U34 | `test_buffer_registry_allocate_rope_angles()` | `[max_seq_len, head_dim]` bf16 allocated |
| U35 | `test_buffer_registry_allocate_position_ids()` | `[1, T]` int32 allocated |
| U36 | `test_buffer_registry_allocate_duplicate_name()` | Raises `ValueError` for duplicate allocation name |
| U37 | `test_buffer_registry_allocate_invalid_shape()` | Raises `ValueError` for empty shape, negative dimensions |

#### Get/Set Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U38 | `test_buffer_registry_get_existing()` | `get(name)` returns previously allocated buffer |
| U39 | `test_buffer_registry_get_nonexistent()` | Raises `KeyError` for unregistered name |
| U40 | `test_buffer_registry_set_overwrite()` | `set(name, data)` overwrites buffer content, preserves shape/dtype |
| U41 | `test_buffer_registry_set_shape_mismatch()` | Raises `ValueError` when data shape doesn't match contract |
| U42 | `test_buffer_registry_set_dtype_mismatch()` | Raises `ValueError` when data dtype doesn't match contract |
| U43 | `test_buffer_registry_set_automatic_broadcast()` | Broadcasting smaller arrays to match contract shape (where applicable) |

#### Contract Enforcement Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U44 | `test_buffer_registry_alignment_check()` | Buffer is page-aligned (4096 bytes) or raises warning if not |
| U45 | `test_buffer_registry_contiguity_check()` | Buffer is C-contiguous; raises `ValueError` if non-contiguous data provided |
| U46 | `test_buffer_registry_contiguous_set()` | Setting a non-contiguous array raises error (required for DMA compatibility) |

#### Lifecycle Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U47 | `test_buffer_registry_release_single()` | `release(name)` frees buffer, subsequent `get()` raises `KeyError` |
| U48 | `test_buffer_registry_release_nonexistent()` | Raises `KeyError` for releasing unregistered buffer |
| U49 | `test_buffer_registry_clear()` | `clear()` releases all buffers but keeps allocation pool metadata |
| U50 | `test_buffer_registry_allocation_pool_reuse()` | Re-allocate after release reuses pool slot (doesn't grow pool indefinitely) |
| U51 | `test_buffer_registry_full_lifecycle()` | Full cycle: allocate -> set -> get -> release -> clear -> re-allocate |
| U52 | `test_buffer_registry_multiple_buffers_concurrent()` | Multiple named buffers coexist independently |

#### Edge Cases

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U53 | `test_buffer_registry_zero_dimension()` | Handles zero-dimension tensor gracefully (empty array, not crash) |
| U54 | `test_buffer_registry_max_size()` | Handles `max_T=4096`, `dim=2048` (full-size hidden_states = 16MB) without issues |
| U55 | `test_buffer_registry_repeated_alloc_release()` | 1000x allocate/release cycle doesn't leak memory or corrupt state |

---

### 1.3 ChunkManager (`test_chunk_manager.py`)

**Component**: `streaming/chunk_manager.py` -- organizes blocks into chunks, manages chunk activation/deactivation, reads chunk manifest JSON.

#### Chunking Logic Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U56 | `test_chunk_manager_init_auto_chunk()` | 16 blocks, `chunk_size=3` -> 6 chunks: `[3,3,3,3,3,1]` |
| U57 | `test_chunk_manager_init_chunk_size_4()` | 16 blocks, `chunk_size=4` -> 4 chunks: `[4,4,4,4]` |
| U58 | `test_chunk_manager_init_chunk_size_8()` | 16 blocks, `chunk_size=8` -> 2 chunks: `[8,8]` |
| U59 | `test_chunk_manager_init_chunk_size_1()` | 16 blocks, `chunk_size=1` -> 16 chunks: `[1]*16` |
| U60 | `test_chunk_manager_init_invalid_chunk_size()` | Raises `ValueError` for `chunk_size <= 0` or `chunk_size > num_blocks` |
| U61 | `test_chunk_manager_init_non_divisible()` | 17 blocks, `chunk_size=3` -> 6 chunks: `[3,3,3,3,3,2]` |
| U62 | `test_chunk_manager_init_single_block()` | 1 block, `chunk_size=3` -> 1 chunk: `[1]` |
| U63 | `test_chunk_manager_init_zero_blocks()` | Raises `ValueError` for `num_blocks <= 0` |

#### Chunk Access Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U64 | `test_chunk_manager_get_chunk_by_id()` | `get_chunk(0)` returns blocks `[0,1,2]` for `chunk_size=3` |
| U65 | `test_chunk_manager_get_chunk_out_of_range()` | Raises `ValueError` for `chunk_id >= num_chunks` |
| U66 | `test_chunk_manager_get_chunk_negative()` | Raises `ValueError` for negative `chunk_id` |
| U67 | `test_chunk_manager_block_to_chunk_mapping()` | `get_chunk_id_for_block(block_id)` returns correct chunk for all blocks |
| U68 | `test_chunk_manager_chunk_sizes_list()` | `chunk_sizes` property returns `[3,3,3,3,3,1]` for default config |
| U69 | `test_chunk_manager_total_chunks()` | `num_chunks` property returns correct count |

#### Manifest Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U70 | `test_chunk_manager_read_manifest_valid()` | Loads valid manifest.json, discovers blocks, weights, shapes |
| U71 | `test_chunk_manager_read_manifest_missing_file()` | Raises `FileNotFoundError` for non-existent manifest |
| U72 | `test_chunk_manager_read_manifest_invalid_json()` | Raises `ValueError` for malformed JSON |
| U73 | `test_chunk_manager_read_manifest_missing_fields()` | Raises `ValueError` for missing required fields (layer_id, weight_files) |
| U74 | `test_chunk_manager_read_manifest_extra_fields()` | Extra fields ignored gracefully (forward-compatible) |
| U75 | `test_chunk_manifest_write_and_read()` | `write_manifest()` followed by `read_manifest()` produces identical data |

#### Activation/Deactivation Tests

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U76 | `test_chunk_manager_activate_chunk()` | Activation sets `active_chunk_id`, calls weight load (mocked) |
| U77 | `test_chunk_manager_deactivate_chunk()` | Deactivation clears `active_chunk_id`, calls weight release (mocked) |
| U78 | `test_chunk_manager_only_one_active()` | Activating chunk B automatically deactivates chunk A |
| U79 | `test_chunk_manager_activate_nonexistent()` | Raises `ValueError` for non-existent chunk_id |
| U80 | `test_chunk_manager_transition_all_chunks()` | Full cycle: activate 0 -> deactivate -> activate 1 -> ... -> activate N |
| U81 | `test_chunk_manager_double_activate()` | Activating same chunk twice is idempotent (no error, no double-load) |

---

### 1.4 Phase 2-4 Component Unit Tests

#### StreamingLoad (Route D) -- `test_streaming_load.py`

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U82 | `test_streaming_load_init()` | Initialization with manifest, weight paths |
| U83 | `test_streaming_load_load_single_block()` | Single block loads, memory tracked (< 121MB for Llama-3.2-1B) |
| U84 | `test_streaming_load_load_all_blocks_sequential()` | 16 blocks loaded one at a time, peak RSS < 200MB |
| U85 | `test_streaming_load_keep_resident()` | After `load_all()`, all blocks remain resident |
| U86 | `test_streaming_load_peak_memory_tracking()` | Peak RSS tracked and reported via `get_peak_memory()` |
| U87 | `test_streaming_load_failure_recovery()` | Block N fails to load -> previous blocks intact, error reported |
| U88 | `test_streaming_load_interrupted()` | Interrupted load cleans up partially loaded blocks |
| U89 | `test_streaming_load_duplicate_load()` | Loading same block twice is idempotent |
| U90 | `test_streaming_load_storage_speed_gate()` | Load time measured per block, warns if exceeds NVMe threshold |

#### ChunkedInference (Route B) -- `test_chunked_inference.py`

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U91 | `test_chunked_inference_init()` | Initialization with chunk_manager, kv_cache, buffer_registry |
| U92 | `test_chunked_inference_single_chunk_forward()` | Single chunk forward produces correct output shape |
| U93 | `test_chunked_inference_multi_chunk_forward()` | Multi-chunk forward chains: output of chunk N = input to chunk N+1 |
| U94 | `test_chunked_inference_async_kv_between_chunks()` | KV merge scheduled after chunk, completes before next chunk needs it |
| U95 | `test_chunked_inference_hidden_state_passthrough()` | hidden_states passed between chunks without mutation |
| U96 | `test_chunked_inference_decode_mode()` | Decode (T=1) produces `[1, 1, vocab_size]` output |
| U97 | `test_chunked_inference_prefill_mode()` | Prefill (T=prompt_len) produces `[1, T, vocab_size]` output |
| U98 | `test_chunked_inference_eos_termination()` | Generation stops at EOS token (mocked sampling) |
| U99 | `test_chunked_inference_max_tokens_termination()` | Generation stops at `max_tokens` limit |

#### RuntimeStreaming (Route C) -- `test_runtime_streaming.py`

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U100 | `test_runtime_streaming_init()` | Initialization with all components |
| U101 | `test_runtime_streaming_prefill_single_pass()` | Each block loaded once, computed, unloaded |
| U102 | `test_runtime_streaming_decode_multi_pass()` | Each block loaded every decode step |
| U103 | `test_runtime_streaming_page_in_page_out_cycle()` | page_in -> compute -> page_out for single block |
| U104 | `test_runtime_streaming_unified_memory_fallback()` | Falls back to mmap if page_in/page_out unavailable |

#### WeightCache (Route C) -- `test_weight_cache.py`

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U105 | `test_weight_cache_init_fixed_size()` | Cache initialized with capacity N |
| U106 | `test_weight_cache_get_hit()` | Added chunk retrievable (cache hit) |
| U107 | `test_weight_cache_get_miss()` | Non-existent chunk returns None (cache miss) |
| U108 | `test_weight_cache_lru_eviction()` | When full, LRU chunk evicted on new add |
| U109 | `test_weight_cache_access_updates_lru()` | Accessing chunk moves it to MRU position |
| U110 | `test_weight_cache_hit_rate_tracking()` | `hit_rate = hits / (hits + misses)` tracked correctly |
| U111 | `test_weight_cache_resize()` | Capacity changeable at runtime |
| U112 | `test_weight_cache_clear()` | Clear empties cache, hit rate resets |
| U113 | `test_weight_cache_eviction_order()` | With 5 inserts into 3-slot cache, evicts in correct LRU order |

#### AdaptiveSelector (Route E) -- `test_adaptive_selector.py`

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| U114 | `test_adaptive_selector_init()` | All route strategies available |
| U115 | `test_selector_plenty_of_ram()` | `model_size < ram * 0.4` -> Route A |
| U116 | `test_selector_tight_but_fits()` | `model_size < ram * 0.8` -> Route D |
| U117 | `test_selector_over_ram()` | `model_size < ram * 1.5` -> Route B |
| U118 | `test_selector_cannot_fit()` | `model_size > ram * 1.5` -> Route C |
| U119 | `test_selector_boundary_0_4x()` | Exactly `0.4 * ram` -> Route A (left-inclusive boundary) |
| U120 | `test_selector_boundary_0_8x()` | Exactly `0.8 * ram` -> Route D (left-inclusive boundary) |
| U121 | `test_selector_boundary_1_5x()` | Exactly `1.5 * ram` -> Route B (left-inclusive boundary) |
| U122 | `test_selector_storage_speed_check()` | Slow storage (SATA) makes Route C non-viable |
| U123 | `test_selector_npu_api_check()` | Missing page_in/page_out API makes Route C/D non-viable |
| U124 | `test_selector_report()` | Returns human-readable decision rationale |
| U125 | `test_selector_edge_cases()` | Handles zero RAM, negative model size, unknown model gracefully |

---

### 1.5 Mocking/Stubbing Strategy (No NPU Hardware)

| Layer | What Is Mocked | How | Why |
|-------|---------------|-----|-----|
| **NPU Compute** | GEMM, Norm, RoPE, Attention operators | `FakeNPUComputeEngine`: numpy matmul + elementwise ops | Deterministic results, configurable delays, no hardware dependency |
| **NPU Driver** | `page_in`, `page_out`, DMA engines | `FakeNpuDriver`: in-memory buffer management with configurable latency | Test fallback paths, validate API contracts |
| **Memory** | RSS tracking, available RAM | `tracemalloc` for real tracking + `unittest.mock.patch` for simulated values | Cross-platform consistency, test extreme memory scenarios |
| **File I/O** | .npy weight file reads | Small dummy .npy files (scaled-down: 64x64 matrices) created via `tmp_path` fixture | Fast tests, no large file dependencies |
| **Disk Speed** | NVMe/SATA read throughput | `time.sleep()` proportional to data size / simulated bandwidth | Test Route C viability across storage configurations |
| **Async Operations** | DMA prefetch, KV merge | `threading.Event` + `concurrent.futures.ThreadPoolExecutor` | Test non-blocking behavior, race conditions |
| **Token Sampling** | Next token selection | Deterministic argmax or fixed token sequence | Reproducible test results |
| **System Info** | `psutil.virtual_memory()`, disk info | `unittest.mock.patch` with controlled return values | Test adaptive selector across hardware configs |

#### FakeNPUComputeEngine Design

```python
class FakeNPUComputeEngine:
    """Numpy-based NPU emulation for testing without hardware."""

    def __init__(self, config, compute_delay_ms=0, dma_delay_ms=0):
        self.config = config
        self.compute_delay_ms = compute_delay_ms  # Simulate NPU compute time
        self.dma_delay_ms = dma_delay_ms          # Simulate DMA transfer time
        self.timeline = []                        # Record operation timestamps

    def gemm(self, a, b):
        """Emulate GEMM: C = A @ B with optional delay."""
        time.sleep(self.compute_delay_ms / 1000)
        self.timeline.append(("gemm", time.monotonic(), a.shape, b.shape))
        return a @ b

    def rmsnorm(self, x, weight):
        """Emulate RMSNorm with optional delay."""
        time.sleep(self.compute_delay_ms / 1000)
        self.timeline.append(("rmsnorm", time.monotonic(), x.shape))
        return x / np.sqrt(np.mean(x**2) + 1e-5) * weight

    def rope(self, x, cos, sin, position_ids):
        """Emulate RoPE with optional delay."""
        time.sleep(self.compute_delay_ms / 1000)
        self.timeline.append(("rope", time.monotonic(), x.shape))
        # Simplified RoPE using numpy
        return x  # Shape-preserving for test purposes

    def attention(self, q, k, v, mask):
        """Emulate attention with optional delay."""
        time.sleep(self.compute_delay_ms / 1000)
        self.timeline.append(("attention", time.monotonic(), q.shape))
        scores = (q @ k.transpose(-2, -1)) / np.sqrt(q.shape[-1])
        if mask is not None:
            scores = scores + mask
        weights = softmax(scores, axis=-1)
        return weights @ v

    def dma_transfer(self, data, direction="read"):
        """Emulate DMA with configurable delay proportional to data size."""
        size_bytes = data.nbytes
        delay = (size_bytes / (3 * 1024**3)) + (self.dma_delay_ms / 1000)  # NVMe baseline
        time.sleep(delay)
        self.timeline.append(("dma", time.monotonic(), direction, size_bytes))
        return data.copy()

    def get_overlap_stats(self):
        """Compute compute/DMA overlap percentage from recorded timeline."""
        # Analyze timeline to determine what fraction of DMA overlaps with compute
        ...
```

---

## 2. Integration Testing

### 2.1 Chunked Inference Without NPU

**Strategy**: `FakeNPUComputeEngine` replaces all NPU operators. Tests run the full inference loop (prefill + decode) using numpy-based compute, verifying end-to-end correctness.

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| I1 | `test_chunked_inference_full_prefill()` | Tokenize -> embed -> chunk0..N -> LM head -> logits `[1, T, vocab_size]` |
| I2 | `test_chunked_inference_full_decode()` | Single token -> chunk0..N -> LM head -> sample -> `[1, 1, vocab_size]` |
| I3 | `test_chunked_inference_multi_token_generation()` | Generate 10 tokens from mock prompt; each step shape-correct, KV cache grows |
| I4 | `test_chunked_inference_kv_merge_timing()` | Async KV merge completes before next chunk starts (instrumented mock) |
| I5 | `test_chunked_inference_attention_mask_applied()` | Causal mask correctly applied across all chunks (lower triangular) |
| I6 | `test_chunked_inference_position_ids_increment()` | Position IDs increment correctly across decode steps |
| I7 | `test_chunked_inference_chunk_boundary_correctness()` | Hidden state at chunk boundary matches monolithic execution (numpy tolerance) |

### 2.2 Async KV Overlap Measurement

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| I8 | `test_kv_overlap_compute_dominant()` | compute=50ms, DMA=5ms -> overlap > 80% (DMA fully hidden) |
| I9 | `test_kv_overlap_dma_dominant()` | compute=10ms, DMA=20ms -> partial overlap measured correctly |
| I10 | `test_kv_overlap_double_buffer_advantage()` | Double-buffer overlap > single-buffer overlap (same config) |
| I11 | `test_kv_overlap_varying_seq_lengths()` | Overlap at S=1, S=100, S=1000, S=4096 (DMA scales with seq length) |
| I12 | `test_kv_overlap_chunk_boundaries()` | Overlap maintained across chunk boundaries (not just block boundaries) |
| I13 | `test_kv_overlap_apple_pattern()` | Apple's async KV merge pattern: KV update happens with 1 chunk's worth of future time |

### 2.3 Cross-Component Integration

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| I14 | `test_registry_chunk_manager_lifecycle()` | Full lifecycle: allocate -> activate chunk -> forward -> deactivate -> next |
| I15 | `test_registry_buffer_reuse_across_chunks()` | hidden_states buffer reused across all chunks (not reallocated) |
| I16 | `test_streaming_load_then_inference()` | Stream load all blocks -> keep resident -> run chunked inference -> correct output |
| I17 | `test_kv_cache_with_varying_chunks()` | KV cache correctly handles different chunk sizes (1, 2, 3, 4, 8 blocks) |

### 2.4 Test Data Generation Strategy

All test data is generated via **pytest fixtures** with **deterministic seeds**:

```python
# conftest.py

DATA_GENERATION_SEED = 42  # Fixed seed for reproducibility

@pytest.fixture
def config_llama_1b_small():
    """Scaled-down config for fast testing.
    dim=128, heads=4, kv_heads=2, layers=4, seq_len=64, head_dim=32, vocab_size=1000
    """
    return ModelConfig(
        hidden_size=128, num_attention_heads=4, num_key_value_heads=2,
        num_hidden_layers=4, max_position_embeddings=64, head_dim=32,
        vocab_size=1000, intermediate_size=512
    )

@pytest.fixture
def config_llama_1b_full():
    """Full Llama-3.2-1B config for realistic tests.
    dim=2048, heads=32, kv_heads=8, layers=16, seq_len=4096, head_dim=64, vocab_size=128256
    """
    return ModelConfig(
        hidden_size=2048, num_attention_heads=32, num_key_value_heads=8,
        num_hidden_layers=16, max_position_embeddings=4096, head_dim=64,
        vocab_size=128256, intermediate_size=8192
    )

@pytest.fixture
def dummy_manifest(tmp_path):
    """Creates manifest.json for 16 blocks with weight paths and shapes."""
    manifest = {
        "num_blocks": 16,
        "blocks": [
            {
                "layer_id": i,
                "weight_files": [f"layer_{i}/weight_{j}.npy" for j in range(9)],
                "shapes": {"hidden": [1, 64, 128], "kv": [2, 64, 32]},
                "tiling": {"M": 64, "K": 64, "N": 64},
                "dtype": "bfloat16"
            }
            for i in range(16)
        ]
    }
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps(manifest))
    return manifest_path

@pytest.fixture
def dummy_weights(tmp_path, config_llama_1b_small):
    """Creates scaled-down .npy weight files for each block."""
    rng = np.random.default_rng(DATA_GENERATION_SEED)
    for block_id in range(config_llama_1b_small.num_hidden_layers):
        block_dir = tmp_path / f"layer_{block_id}"
        block_dir.mkdir()
        for weight_idx in range(9):
            # Scaled-down weights: small matrices for fast testing
            weight = rng.standard_normal((32, 32)).astype(np.float32)
            np.save(block_dir / f"weight_{weight_idx}.npy", weight)
    return tmp_path

@pytest.fixture
def sample_prompt_tokens():
    """Fixed token IDs representing 'Hello, world' for reproducibility."""
    return np.array([[128000, 15339, 28399, 28399]], dtype=np.int32)

@pytest.fixture
def fake_compute_engine(config_llama_1b_small):
    """Zero-delay numpy compute engine for fast unit tests."""
    return FakeNPUComputeEngine(config_llama_1b_small, compute_delay_ms=0, dma_delay_ms=0)

@pytest.fixture
def fake_compute_engine_slow(config_llama_1b_small):
    """Simulated NPU timing: compute=50ms, DMA=5ms per operation."""
    return FakeNPUComputeEngine(config_llama_1b_small, compute_delay_ms=50, dma_delay_ms=5)
```

**Two-tier data strategy**:
- **Fast tier** (`config_llama_1b_small`): 4 layers, dim=128, seq_len=64. Used for 90% of unit tests. Runs in < 1 second.
- **Realistic tier** (`config_llama_1b_full`): Full config, uses mocked weights. Used for integration and performance tests. Marked `@pytest.mark.slow`.

---

## 3. Performance Testing

### 3.1 Framework: pytest-benchmark

All performance tests use `pytest-benchmark` for standardized measurement:

```python
def test_benchmark_chunk_size_comparison(benchmark):
    """Compare chunk sizes 1, 2, 3, 4, 8 for throughput and memory."""
    results = {}
    for chunk_size in [1, 2, 3, 4, 8]:
        result = benchmark(
            _run_inference_with_chunk_size,
            chunk_size=chunk_size,
            config=config_llama_1b_small,
            num_tokens=10
        )
        results[chunk_size] = {
            "tokens_per_sec": result.tokens_per_sec,
            "peak_rss_mb": result.peak_rss_mb,
            "kv_overlap_pct": result.kv_overlap_pct,
            "total_time_ms": result.total_time_ms,
        }
    # Assert: chunk_size=3 should be competitive (within 10% of best)
    assert results[3]["tokens_per_sec"] >= max(r["tokens_per_sec"] for r in results.values()) * 0.90
```

### 3.2 Chunk Size Tuning Benchmarks

| # | Benchmark Function | What It Measures | Success Criterion |
|---|-------------------|-----------------|-------------------|
| P1 | `benchmark_chunk_size_comparison()` | tokens/sec, RSS, overlap% for sizes [1,2,3,4,8] | Optimal size identified (within 10% of best) |
| P2 | `benchmark_chunk_activation_overhead()` | Time to activate chunk (NPU reconfig) per size | Overhead < 5% of total inference time |
| P3 | `benchmark_chunk_memory_footprint()` | Peak RSS during prefill/decode per size | RSS scales linearly with chunk size |
| P4 | `benchmark_chunk_kv_merge_frequency()` | KV merge count per forward pass per size | Matches expected: `num_chunks = ceil(num_blocks / chunk_size)` |

### 3.3 Compute/KV Overlap Efficiency

| # | Benchmark Function | What It Measures | Success Criterion |
|---|-------------------|-----------------|-------------------|
| P5 | `benchmark_overlap_timeline()` | Precise timestamps of compute vs DMA operations | > 80% DMA time overlaps with compute |
| P6 | `benchmark_overlap_varying_dma_speeds()` | Overlap at NVMe (3GB/s), SATA (500MB/s), HDD (100MB/s) | NVMe: >80%, SATA: >50%, HDD: <20% |
| P7 | `benchmark_overlap_with_weight_cache()` | Overlap with/without weight cache during decode | Cache improves overlap by > 20% |

### 3.4 Baseline Comparison Methodology

| # | Benchmark Function | What It Compares | Success Criterion |
|---|-------------------|-----------------|-------------------|
| P8 | `benchmark_streaming_vs_monolithic()` | Route B vs current monolithic architecture | Route B >= 1.1x tokens/sec |
| P9 | `benchmark_before_after_kv_async()` | With async KV vs sync KV | Async KV >= 1.05x throughput |
| P10 | `benchmark_memory_scaling_1b_7b()` | Memory usage for 1B vs 7B model configs | Streaming: memory scales with layer size, not model size |
| P11 | `benchmark_ttft_comparison()` | Time-to-first-token: streaming vs monolithic | Streaming TTFT within 20% of monolithic |
| P12 | `benchmark_decode_latency_per_token()` | Per-token decode latency across 100 tokens | p95 latency < 2x mean latency |

### 3.5 Benchmark Execution Protocol

- **Warmup**: 3 iterations before measurement
- **Measurement**: 10 iterations per benchmark
- **Statistics**: mean, median, std_dev, min, max, p50, p95, p99
- **Baseline storage**: JSON files in `streaming/tests/performance/baselines/`
- **Regression alert**: CI fails if any metric degrades > 10% from baseline
- **Schedule**: Weekly (not per-commit, too slow)

---

## 4. Regression Testing

### 4.1 Feature Flag Testing

The architecture specifies `streaming_mode=False` as the default. These tests ensure no breakage:

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| R1 | `test_feature_flag_default_off()` | `streaming_mode` defaults to `False`; existing behavior unchanged |
| R2 | `test_feature_flag_explicit_on()` | `streaming_mode=True` activates streaming pipeline |
| R3 | `test_feature_flag_config_file()` | `streaming_mode` settable via config file (`config.yaml`) |
| R4 | `test_feature_flag_cli_override()` | CLI `--streaming` flag overrides config file setting |
| R5 | `test_feature_flag_partial_enable()` | Can enable `kv_async=True` but `chunked=False` (partial streaming) |
| R6 | `test_feature_flag_no_cross_contamination()` | Streaming mode on request A doesn't affect request B (isolation) |
| R7 | `test_feature_flag_toggle_at_runtime()` | Toggling mode mid-inference raises clear error (not silent corruption) |
| R8 | `test_feature_flag_env_var_override()` | `STREAMING_MODE=true` environment variable respected |

### 4.2 Output Parity Tests

Same inputs, both modes, compare outputs:

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| R9 | `test_output_parity_prefill()` | Same tokens, both modes produce logits within `np.allclose(atol=1e-3)` |
| R10 | `test_output_parity_decode()` | Same tokens + KV state, both modes produce same next token id |
| R11 | `test_output_parity_attention_mask()` | Same mask applied, both modes mask same positions |
| R12 | `test_output_parity_rope()` | Same RoPE angles, both modes produce same rotated embeddings |
| R13 | `test_output_parity_residual()` | Residual addition produces same result in both modes |
| R14 | `test_output_parity_full_generation()` | Generate 20 tokens: both modes produce identical token sequence |

### 4.3 Cross-Platform Testing (Windows 11 Focus)

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| R15 | `test_windows_mmap_behavior()` | mmap works correctly on Windows NTFS (different from Linux semantics) |
| R16 | `test_path_handling_windows()` | `pathlib.Path` handles Windows backslash paths correctly |
| R17 | `test_memory_available_windows()` | `psutil.virtual_memory()` works on Windows, correct RSS measurement |
| R18 | `test_file_locking_windows()` | Windows file locking doesn't prevent .npy access during streaming load |
| R19 | `test_conftest_platform_auto_detect()` | conftest.py auto-detects platform, adjusts test parameters |
| R20 | `test_conftest_npu_skip_auto()` | Tests marked `@pytest.mark.requires_npu` auto-skipped on non-NPU platforms |

### 4.4 Dependency Compatibility

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| R21 | `test_numpy_version_compatibility()` | Current numpy version supports mmap, bf16 operations |
| R22 | `test_python_3_10_support()` | Tests pass on Python 3.10 (minimum supported version) |
| R23 | `test_python_3_12_support()` | Tests pass on Python 3.12 (latest supported version) |

### 4.5 Migration/Upgrade Compatibility

| # | Test Function | What It Verifies |
|---|--------------|------------------|
| R24 | `test_model_weights_backward_compat()` | New streaming code reads existing .npy files without modification |
| R25 | `test_manifest_backward_compat()` | New manifest.json format compatible with existing weight files |
| R26 | `test_config_migration()` | Existing config files work with new streaming section added |

---

## 5. Acceptance Criteria by Phase

### Phase 1: Foundation (AsyncKVCache + ChunkManager + BufferRegistry)

| # | Criterion | Measurement | Target |
|---|-----------|------------|--------|
| AC1 | All 3 components implemented | Code review + API contract check | Full public APIs matching design docs |
| AC2 | Unit test coverage | `pytest-cov --cov=streaming` | >= 90% line coverage per component |
| AC3 | All unit tests pass | CI (GitHub Actions, Linux + Windows) | 0 failures, 0 errors |
| AC4 | Async KV overlap efficiency | Integration test `test_kv_overlap_compute_dominant()` | > 80% DMA hidden behind compute |
| AC5 | ChunkManager partitioning correctness | Parametrized tests across (blocks, chunk_size) | All combinations correct |
| AC6 | BufferRegistry contract enforcement | Tests for shape/dtype/alignment/contiguity | All violations caught |
| AC7 | No NPU hardware required | Verify all tests pass without NPU | 100% software-only |
| AC8 | Component interfaces stable | Interface review, no breaking changes expected | Signatures match design docs |
| AC9 | Documentation | Docstrings + usage examples | All public methods documented |
| AC10 | Benchmark framework operational | pytest-benchmark configured, runs successfully | Baseline data generated |

### Phase 2: Route D + Route B (Streaming Load + Chunked Inference)

| # | Criterion | Measurement | Target |
|---|-----------|------------|--------|
| AC11 | Route D startup peak memory | tracemalloc during streaming load | < 200MB for 1B model |
| AC12 | Route B throughput | Tokens/sec vs monolithic baseline | >= 1.1x baseline |
| AC13 | NPU compilation overhead | Timing mocked chunk compilation | < 500ms per chunk |
| AC14 | Feature flag preservation | Regression tests R1-R8 | All pass |
| AC15 | Output parity | Regression tests R9-R14 | All pass (tolerance: atol=1e-3) |
| AC16 | Chunked inference e2e | Integration tests I1-I7 | All pass |
| AC17 | Async KV merge e2e | Integration tests I8-I13 | All pass |
| AC18 | CLI entry point functional | `streaming_infer.py --help`, `--config`, `--model` | Correct output |
| AC19 | Cross-platform (Windows 11) | Regression tests R15-R20 | All pass |
| AC20 | Performance baselines stored | Benchmark output JSON files | Created and committed |

### Phase 3: Route C (True Runtime Streaming + Weight Cache)

| # | Criterion | Measurement | Target |
|---|-----------|------------|--------|
| AC21 | Route C peak runtime memory | RSS measurement during decode | < 500MB for 7B model |
| AC22 | Route C decode latency | Per-token timing on simulated NVMe | < 50ms/token for 7B |
| AC23 | Weight cache hit rate | Cache stats over 100 decode steps | > 70% after first token |
| AC24 | page_in/page_out cycle | Tests U100-U104 | All pass |
| AC25 | LRU eviction correctness | Tests U105-U113 | All pass |
| AC26 | Fallback paths tested | Route C with simulated API absence | Falls back to mmap/munmap |

### Phase 4: Route E (Adaptive Selector)

| # | Criterion | Measurement | Target |
|---|-----------|------------|--------|
| AC27 | Strategy selection accuracy | Test matrix: 5 model sizes x 5 RAM configs | > 95% correct |
| AC28 | Boundary conditions | Tests U119-U121 | All pass |
| AC29 | Human-readable reports | Test U124 | Report includes rationale |
| AC30 | Edge case handling | Test U125 | No crashes, graceful degradation |
| AC31 | End-to-end selector + route | Integration: selector picks -> route executes | Full pipeline works |

---

## 6. Test Infrastructure

### 6.1 Test Directory Structure

```
C:\Users\antmi\IRON\iron\model_convert\streaming\tests\
  conftest.py                          # Shared fixtures (see Section 2.4)
  __init__.py
  unit/
    test_async_kv_cache.py             # Tests U1-U30
    test_buffer_registry.py            # Tests U31-U55
    test_chunk_manager.py              # Tests U56-U81
    test_streaming_manifest.py         # Manifest reading/writing tests
    test_streaming_load.py             # Tests U82-U90 (Phase 2)
    test_chunked_inference.py          # Tests U91-U99 (Phase 2)
    test_runtime_streaming.py          # Tests U100-U104 (Phase 3)
    test_weight_cache.py               # Tests U105-U113 (Phase 3)
    test_adaptive_selector.py          # Tests U114-U125 (Phase 4)
  integration/
    test_chunked_inference_e2e.py      # Tests I1-I7
    test_kv_overlap_efficiency.py      # Tests I8-I13
    test_cross_component.py            # Tests I14-I17
  performance/
    test_chunk_size_benchmarks.py      # Benchmarks P1-P4
    test_overlap_benchmarks.py         # Benchmarks P5-P7
    test_baseline_comparison.py        # Benchmarks P8-P12
    baselines/                         # Stored baseline JSON files
  regression/
    test_feature_flags.py              # Tests R1-R8
    test_output_parity.py             # Tests R9-R14
    test_cross_platform.py             # Tests R15-R20
    test_dependency_compat.py          # Tests R21-R23
    test_backward_compat.py            # Tests R24-R26
  mocks/
    fake_compute_engine.py             # FakeNPUComputeEngine class
    fake_npu_driver.py                 # FakeNpuDriver class
    test_data_factory.py               # Deterministic test data generators
```

### 6.2 pytest Configuration

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["iron/model_convert/streaming/tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*", "benchmark_*"]
markers = [
    "slow: tests taking >10 seconds (skip in CI by default)",
    "requires_npu: tests requiring actual NPU hardware",
    "benchmark: performance benchmark tests",
    "windows: Windows-specific tests",
    "integration: integration tests",
    "regression: regression tests",
]
addopts = "-v --tb=short --strict-markers"

[tool.coverage.run]
source = ["iron/model_convert/streaming"]
omit = ["**/tests/**", "**/mocks/**"]

[tool.coverage.report]
fail_under = 90
show_missing = true
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
]
```

### 6.3 CI/CD Pipeline Integration

```yaml
# .github/workflows/streaming-tests.yml
name: Streaming Architecture Tests

on:
  push:
    branches: [feature/model-converter-analysis, main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 9 * * 1'  # Weekly benchmarks (Monday 9am)

jobs:
  unit-tests:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ['3.10', '3.11', '3.12']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -e ".[dev]"
      - run: >
          pytest streaming/tests/unit/
          --cov=streaming
          --cov-report=xml
          --cov-report=term-missing
          --cov-fail-under=90
      - uses: codecov/codecov-action@v4

  integration-tests:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    steps:
      - uses: actions/checkout@v4
      - run: pip install -e ".[dev]"
      - run: >
          pytest streaming/tests/integration/
          -m "not slow"
          -v

  regression-tests:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    steps:
      - uses: actions/checkout@v4
      - run: pip install -e ".[dev]"
      - run: >
          pytest streaming/tests/regression/
          -v

  benchmarks:
    if: github.event_name == 'schedule'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -e ".[dev]"
      - run: >
          pytest streaming/tests/performance/
          --benchmark-json=benchmarks/output.json
          --benchmark-min-rounds=10
      - name: Check baseline regression
        run: python scripts/check_baseline_regression.py
      - uses: actions/upload-artifact@v4
        with:
          name: benchmark-results
          path: benchmarks/output.json
```

### 6.4 Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: streaming-unit-tests
        name: Run streaming unit tests
        entry: pytest streaming/tests/unit/ -q --last-failed
        language: system
        pass_filenames: false
        always_run: true

      - id: streaming-coverage
        name: Check streaming test coverage
        entry: pytest streaming/tests/unit/ --cov=streaming --cov-fail-under=90 --no-cov-on-fail
        language: system
        pass_filenames: false

      - id: streaming-lint
        name: Lint streaming test files
        entry: ruff check streaming/tests/
        language: system
        types: [python]
```

### 6.5 Required Dependencies

```toml
# pyproject.toml
[project.optional-dependencies]
dev = [
    "pytest>=7.4",
    "pytest-cov>=4.1",
    "pytest-benchmark>=4.0",
    "pytest-mock>=3.12",
    "pytest-xdist>=3.5",      # Parallel test execution
    "ruff>=0.1",
    "coverage[toml]>=7.3",
    "ml_dtypes>=0.3",          # bfloat16 support
    "psutil>=5.9",             # Memory monitoring
    "trio>=0.23",              # Async testing utilities
]
```

---

## 7. Risk Mitigation Through Testing

| Architecture Risk | How Testing Mitigates It |
|------------------|-------------------------|
| R1: AMD NPU driver lacks page_in/page_out APIs | Tests U104, U123 verify fallback to mmap/munmap works correctly. Selector test U123 prevents Route C/D selection when APIs unavailable. |
| R2: Route C disk I/O dominates decode | Test U90 measures storage speed per block. Benchmark P6 quantifies overlap at different storage speeds. Test R25 validates weight cache hit rate. |
| R3: Integration breaks existing functionality | Tests R1-R14 (feature flags + output parity) run on every PR. CI blocks merge if any regression test fails. |
| R4: Chunk size suboptimal for AIE | Benchmarks P1-P4 systematically test sizes 1/2/3/4/8. Baseline comparison identifies optimal size empirically. |
| R5: Windows memory management differences | Tests R15-R19 specifically validate Windows mmap, file locking, RSS measurement. CI runs on windows-latest. |
| R6: DMA driver timing variance | Tests I8-I13 measure overlap across simulated DMA speeds. Tests designed with tolerance for timing variance. |
| Document issue C2: Conflicting KV cache patterns | Tests I8-I13, U18-U26, and I13 specifically validate the chosen Apple merge pattern. Both patterns can be tested and compared. |

---

## 8. Test Execution Summary

| Phase | Tests to Add | Est. Time to Write | Est. Time to Run (CI) |
|-------|-------------|-------------------|----------------------|
| Phase 1 | ~81 unit tests (U1-U81) | 2-3 weeks | ~30 seconds (parallel) |
| Phase 2 | ~35 unit + ~17 integration tests (U82-U113, I1-I17) | 2 weeks | ~60 seconds |
| Phase 3 | ~14 unit tests (U100-U113) | 1 week | ~15 seconds |
| Phase 4 | ~12 unit tests (U114-U125) | 1 week | ~10 seconds |
| Regression | ~26 regression tests (R1-R26) | 1 week (parallel with Phase 1-2) | ~45 seconds |
| Performance | ~12 benchmarks (P1-P12) | 1 week | ~5 minutes (weekly) |
| **Total** | **~220 tests** | **~8 weeks** | **~2.5 minutes (per push)** |

---

*This testing strategy is designed to be executable without NPU hardware, ensuring rapid feedback loops throughout development. All acceptance criteria map directly to the success metrics defined in `STREAMING_PROGRESS.md` Section 11.*
