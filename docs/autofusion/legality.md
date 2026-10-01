<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Automatic operator fusion in IRON: legality and metadata model

> Design notes from 2026-09-25, committed as written. `file:line` citations
> refer to the IRON tree of that date and may have drifted. The scratch scripts
> and run outputs the notes name were not kept.

Scope: the metadata a fusion pass needs in order to decide, from a traced graph
alone, whether two adjacent operators can be fused. The model is written to be
graph-agnostic. Llama is one test case of six.

Code base: the IRON tree of 2026-09-25 (branch `ehunhoff/llama-graph-arena`).
All paths below are relative to its `iron/` directory unless stated otherwise.

Tool: `edge_stats.py`. It runs compile-free and
device-free. For each graph it:

- traces the graph on handles;
- tunes every operator against an `npu2` (8-column) or `npu1` (4-column)
  device model;
- runs each overlay's `design()` only to count workers, fifos and shim streams
  (no MLIR is resolved and no aiecc runs);
- classifies every producer→consumer edge.

Raw outputs are `run_npu2.txt` and `run_npu1.txt`.

Legend for claims:

- **[verified]**: read in the code or measured by the tool.
- **[estimate]**: arithmetic on verified numbers.
- **[speculative]**: not checked against the toolchain or hardware.

---

## 0. Why, and the headline

### Measured motivation (from earlier hardware work)

- A dispatch costs about 146 µs in turbo mode.
- Switching designs inside one ELF costs about 80-110 µs per switch.
- Running the same design back to back costs about 11 µs.
- Llama decode spends about 24 ms of its 122 ms per token on 321 design
  switches, which is about 75 µs per switch on average.
- Every intermediate round-trips through DDR.

### Tool validation

- The tool counts **322 configure points = 321 switches** for Llama-1B decode
  (16 layers). This is the measured count, so the switch model below is
  anchored to hardware. **[verified]**

### Headline findings

1. **The shim budget, not structure, is the first blocker today.** Every
   elementwise operator tunes `num_aie_columns` to the whole shim budget by
   default (`common/elementwise.py:96-118` → `Overlay.shim_columns`,
   `common/declare/overlay.py:71`). GEMV uses 16 of the 16 input channels on
   NPU2. [verified]
   - Co-residence is structurally legal on 401 of the 432 decode data edges,
     but only 32 fit the shim budget as tuned.
   - Stream fusion is legal on 210 edges ignoring the shim budget, and on 81
     as tuned.
   - Any fusion pass therefore has to **re-tune jointly** under a shared
     budget. Fusion cannot be a post-pass over independently tuned operators.
2. **Per-slot order is undeclared for every operator that overrides
   `design(rt)`**: GEMM, MHA, Transpose, Repeat, StridedCopy, MemCopy,
   flm.GEMM and flm.DequantBFP. In prefill, 290 of 369 edges are blocked on
   this alone. [verified]
   - The one override the tool could model (GEMV) **contradicts its own
     declaration**. `GEMVOverlay.b = StreamIn(K, per=num_aie_columns)`
     (`operators/gemv/op.py:60`) is not declared `replicate`, but `design(rt)`
     sends the whole vector to every column (`gemv/op.py:321`).
   - Declarations have to become authoritative before a pass can trust them.
3. **Multi-consumer values are the next blocker** (142 decode edges): q/k/v
   read the same normed `x`, and gate/up read the same `x`. These are
   *horizontal* (sibling) fusions, a fourth kind the three-kind taxonomy
   misses. With multi-consumer and shim lifted, decode stream legality is
   **352/432**.
4. **Kernel fusion (epilogues) is narrow but real.** It is legal on
   GEMV/GEMM→unary activation and on activation→elementwise. It is limited by
   **core DMA channels**: a GEMV or GEMM core already uses both S2MM channels,
   so any binary consumer is out. GEMV's `epilogue="gelu"`
   (`gemv/op.py:55,216-217`) is exactly this pattern, hand-written.
5. **Extent-free design keys alone** (the overlay key instead of the operator
   key) save 32 decode switches (q→k GEMV, q→k RoPE). About 2.4 ms per token.
   [estimate]

Same results on npu1: every graph except prefill gives identical counts on
the 4-column model. Prefill does not trace on npu1, because MHA raises
`Untunable` (`operators/mha/op.py:108`). [verified]

---

## 1. Operator inventory

### Semantics classes

| Class | Meaning |
|---|---|
| **E** elementwise | `Local(block=1)` |
| **R** row-local | `Local(block=row)`: norm, softmax, RoPE, group dequant |
| **C** contraction | reduction over an axis the output does not have |
| **M** movement | pure re-indexing |
| **X** composite | a multi-stage pipeline with internal dataflow |

### Measured resources

Numbers come from `edge_stats.py --verbose` at Llama-1B decode and prefill
shapes on npu2. L1 is the busiest core: fifo objects × depth + buffers +
stack. [verified by the tool; the L1 figure is an estimate of the allocator's
result]

- "Seq" is derived when the sequence comes from `common/design/runtime.py:264`
  `transfers()`, and **override** when it comes from a hand-written
  `design(rt)`.
- "Shim in/out" counts channels: one per slot, or one per replicated stream.

| Operator (file:line) | Sem. | Declared streams: object shape, slots | Cores | L1 bytes | Shim in/out | Core body | Residents / values | Seq |
|---|---|---|---|---|---|---|---|---|
| ElementwiseAdd/Mul, AXPY (`common/elementwise.py:267-282`, `operators/elementwise_*.py`) | E | a, b, y: `line_size` per (cols, chans) | 8 | 4 100 - 50 180 | 16/8 | 1 kernel call per line (`elementwise.py:183-192`) | `count` (`:104`); `barrier` | derived |
| SiLU, GELU, ReLU, Sigmoid, Tanh, LeakyReLU (`elementwise.py:245-256`) | E | x, y: `line_size` per (cols, chans) | 8 | 3 076 - 33 796 | 8/8 | 1 call | `count` | derived |
| LayerNorm (`operators/layer_norm.py:18-28`) | **R(line_size)** | as the unary template | 8 | 9 220 | 8/8 | 1 call, normalises each *line* | `count` | derived |
| Dequant (`operators/dequant.py:28-145`) | R(group) | x, y per cols | cols | n/m | n/m | 1 call | residents (`:145`) | derived |
| RMSNorm / WeightedRMSNorm (`operators/rms_norm.py:70-200`) | R(row) | x, y per (cols, chans); w `replicate=True` (`:104-106`) | 2 decode / 16 prefill (2 per slot, pipelined `core_norm`→`core_mul`, `:94-195`) | 25 604 - 50 180 | 2/1, 9/8 | 1 call per core, 2 cores per slot | `count` per core | derived; `resolve_class` picks Weighted (`:221`) |
| Softmax / DynamicSoftmax (`operators/softmax.py:30-181`) | R(cols) | x, y: `cols` per (cols, chans) (`:43-44`) | 1 | 17 412 - 33 800 | 1/1 | 1 call (mask+softmax already fused in the kernel) | `count`, `vector_size` (`:45-46`); Dynamic: `Scratchpad vector_size` (`:136`) | derived; `resolve_class` (`:176`) |
| RoPE (`operators/rope/op.py:28-171`) | R(cols) | x, lut, y: (1, cols) per cols (`:44-46`) | 1 decode / 8 prefill | 1 800 | 2/1, 16/8 | 1 call in a 2-deep loop (`:76-78`) | `lut_rows`, `rows_per_lut` (`:47-48`) | derived |
| GEMV (`operators/gemv/op.py:34-345`) | C | a: (tile_in, K) per cols; b: K per cols (**not** replicate, `:60`); c: tile_out per cols (`:59-61`) | 8 | 3 200 - 51 200 | 16/8 | matvec loop over tile_out/tile_in, **optional gelu epilogue on the released C tile** (`:200-217`) | none; infinite loop over batches | **override** (`:295-334`): Access taps that equal the derived split for A and C, and B whole to every column |
| GEMM (`operators/gemm/op.py:43-513`) | C | a per `n_shim_mem_a`, b and c per cols (`:72-74`), all L2-sized objects | 32 (4×8) | 52 488 (stack 0xD00, `:416`) | 12/8 | **not** a single call: `zero`, K-loop `matmul`, optional `convert_copy` (`:373-395`) | `k_div_k`, `n_tiles` (`:75-76`) | **override** (`:513`); shims pinned `Tile(c,0)` (`:427-431`) |
| flm.GEMM (`operators/flm/gemm/op.py:106-769`) | C (+ epilogue) | a per rows, b per cols, c per cols (`:147-149`) | 32 | sized from L1 | n/m | chunked mmul plus `mm_fused_epilogue_chunk` | 8 residents incl. `epilogue`, `clamp_*` (`:152-159`) | **override** (`:769`) |
| MHA (`operators/mha/op.py:57-708`) | X | q, o per `q_shims` via `Shim(4)`/`Shim(7)`; k, v via `Shim(5)`/`Shim(6)` (`:75-78`) | 24, **pinned** | 53 528 | 4/2 | 3-stage pipeline per head/Q-block (`:284-410`) | 4 residents (`:79-82`); NPU2 only (`:108`) | **override** (`:708`); memtiles pinned at cols 3, 4, 6, 7 (`:230-249`) |
| Transpose (`operators/transpose.py:33-266`) | M (cores) | x, y: (m, n) per (cols, chans) (`:48-49`) | 2 | 33 804 | 2/2 | s×s kernel tiles over a memtile reshuffle | 3 residents (`:50-52`) | **override** (`:266`) |
| Repeat (`operators/repeat.py:29-142`) | M (DMA only) | s, d: `transfer_size` (`:41-42`) | 0 | 0 | 1/1 | none | none | **override** (`:142`): stride-0 re-read |
| StridedCopy (`operators/strided_copy.py:28-262`) | M (DMA only) | s, d per channels (`:43-44`) | 0 | 0 | 1/1 | none | `Scratchpad in_offset/out_offset` (`:147-148`) | **override** (`:262`) |
| MemCopy (`operators/mem_copy.py:57-269`) | M (cores) | s, d per cores (`:68-69`) | cores | n/m | n/m | 1 call | none | **override** (`:269`) |
| flm.DequantBFP (`operators/flm/dequant/op.py:57-265`) | R(block) | qw per cols; out per (cols, halves) (`:77-78`) | cols | stack 2048 | n/m | 1 call | none; AIE2P only (`:96`) | **override** (`:265`) |

n/m means not measured: the operator does not appear in the six graphs.

### Existing hand fusions (precedents a general pass must subsume)

- **Kernel epilogue as a string.** GEMV `epilogue="gelu"`
  (`gemv/op.py:55,76-80,216-217`).
- **Kernel epilogue as an enum plus a resident.** flm.GEMM `Epilogue`
  (`flm/gemm/op.py:155,603,650-683`).
- **Stream fusion with a core-to-core fifo.** WeightedRMSNorm: norm core →
  mul core (`rms_norm.py:94-195`).
- **In-kernel fusion.** Softmax mask+softmax.
- **Spatial fusion.** `operators/swiglu_prefill_stream/`, where tile sizes
  shrink as more layers fuse.
- **Graph-level composition.** `operators/swiglu_decode/`.
- **Pattern selection at trace time.** `resolve_class`: RMSNorm(x, w) →
  WeightedRMSNorm, and Softmax + runtime `vector_size` → DynamicSoftmax.

---

## 2. What a fusion decision needs vs what IRON declares

| Needed | Declared today? | Where / gap |
|---|---|---|
| Object (tile) shape of each stream | **Yes** | `StreamIn/StreamOut(shape, per=, broadcast=, replicate=, via=, depth=)` (`common/declare/member.py:134-178`); bound shape and count via `BoundStream` (`declare/bound.py`) |
| Number of slots per stream | **Yes** | `per=` dims; `BoundStream.count` |
| Which elements each slot carries, in what order (the "split dimension") | **Only implicitly, and only for derived sequences** | `transfers()` (`runtime.py:264-292`): count 1 → whole; `replicate` → whole to every slot; else `tiling.split(shape, count, batch_axes)`, i.e. contiguous row blocks of the first non-batch axis (`tiling.py:305`). The operator does not *declare* it. It is a consequence of the emitter. **For the 8 override operators it exists only as imperative code.** |
| Consistency of the declaration with the sequence | **No** | GEMV.b declared per-column split, sent whole (`gemv/op.py:60` vs `:321`). Nothing checks it. |
| Operator semantics: elementwise / row-local (and the row) / contraction / movement | **No** | Not declared anywhere. The tool supplies a `SEMANTICS` table. |
| Whether the local block depends on a tunable | **No** | LayerNorm normalises each `line_size` = `min(tile_size, tile_cap)` (`elementwise.py:102,125`), so its *math* depends on a tunable. A pass that retiles it changes the result. |
| Whether an output tile is final at release | **No** | True for GEMV and GEMM as written, since K is reduced within one core. Would be false for a K-split GEMM. |
| Kernel purity and in-place safety | **No** | Kernels are `ExternalFunction`s; nothing says a kernel is pure, or that out may alias in. |
| Cores, pinned tiles | **Derivable** | Only by running `design()`. `Overlay.cores` exists for elementwise only (`elementwise.py:129`). |
| L1 per core | **Derivable** | By summing fifos, buffers and stack from `design()` (what the tool does). The allocator's result is not exposed. |
| Shim DMA channels | **Derivable** | Stream counts. `get_shim_dma_limit(dev)` gives the budget (`overlay.py:34`). |
| Core DMA channels (2 S2MM, 2 MM2S per core) | **No** | Not modelled. This is the binding constraint on kernel fusion. |
| Memtile bytes, BDs, locks | **No** | Not modelled at declaration level. MHA pins memtiles. The BD and queue-depth hazards found earlier live below IRON. |
| Per-call values (scratchpad) vs build-time residents | **Yes** | `Scratchpad`, `Resident`, `DispatchTime` members (`member.py:184-240`); `build_design` wires them (`design/build.py:65-84`). |
| Graph facts: readers, graph outputs, state, slices | **Yes** | `TracedGraph` / `TracedStep` (`common/graph/trace.py:32-128`); `Handle.role ∈ {input, output, weight, state, intermediate, slice}` (`graph/handle.py:31`). |
| Design identity for switch counting | **Yes, but too fine** | `Operator.design_key()` (`declare/operator.py:140`) includes extents (M, rows). The overlay key (`overlay.py:225`) is extent-free, which is what O5 would use. |

---

## 3. A typed metadata model

The design rules:

- No `getattr`/`hasattr` probing.
- Every fact is a typed value returned by a method that exists on the base
  class.
- Unions are closed and handled with `match`/`isinstance`.
- "Unknown" is a value (`Undeclared(reason)`), not a missing attribute.

This mirrors the running code in `edge_stats.py`. That code keeps two lookup
tables (`SEMANTICS`, `OVERRIDE_ORDER`) *only because the operators do not
declare these facts yet*. Each table entry is what an operator would declare.

### 3.1 Semantics

```python
@dataclass(frozen=True)
class Local:            # out[block] depends only on in[same block]
    block: int          # 1 = elementwise; a row for norm/softmax/RoPE; a group for dequant

@dataclass(frozen=True)
class Contraction:      # reduces an axis the output lacks (GEMV, GEMM)
    final_at_release: bool   # an output object is complete when the core releases it

@dataclass(frozen=True)
class Movement:         # re-indexing only
    has_cores: bool     # False: DMA-only (StridedCopy, Repeat)

@dataclass(frozen=True)
class Composite: ...    # internal multi-stage dataflow (MHA)

Semantics = Local | Contraction | Movement | Composite

class Overlay:
    def semantics(self) -> Semantics:          # proposed; abstract on the base
        raise NotImplementedError
```

`LayerNormOverlay.semantics()` must return `Local(self.line_size)`. Its block
is a function of a tunable, which must be pinned before a pass retiles it.
Better: make the block a `dim()`, not a tunable.

### 3.2 Layout: the per-slot order, as data

```python
@dataclass(frozen=True)
class SlotOrder:
    blocks: tuple[tiling.Block, ...]   # one per slot: offset, run, leading repeats
    replicated: bool                   # every slot carries the whole buffer
    tile: int                          # elements per fifo object
    def indices(self, slot: int) -> np.ndarray: ...   # from Block.unrolled

@dataclass(frozen=True)
class Undeclared:
    reason: str

Layout = SlotOrder | Undeclared

class Operator:
    def order(self, buffer: BoundBuffer) -> Layout:    # proposed
        # Default: exactly what transfers() emits (runtime.py:264).
        # An operator with design(rt) returns its taps; GEMV already builds them.
        ...
```

The key proposal is that **the sequence emitter and the fusion pass read the
same `order()`**:

- `transfers()` becomes "emit `order(buffer)`".
- An override operator returns `Access`/`Block` taps instead of issuing them
  imperatively.
- The GEMV.b mismatch becomes impossible, because the declaration *is* the
  sequence.

GEMV's override is already 90% there: it builds `Access` lists and then issues
them (`gemv/op.py:295-334`).

For a Local operator on a derived sequence, the order is a **choice**, not a
fact. Such an operator can compute any assignment of whole blocks to slots, so
it can *adopt* its producer's order. That observation is what `ADOPT` below
captures (64 decode edges). Model it as:

```python
@dataclass(frozen=True)
class Negotiable:        # any partition into whole `block`s, provided every operand follows it
    block: int
```

### 3.3 Hand-off between two orders

```python
class Handoff(Enum):
    DIRECT = "direct"   # same slots, same indices per slot, same object size -> core-to-core fifo
    RETILE = "retile"   # same indices per slot, different object size -> repack (memtile link)
    ADOPT  = "adopt"    # consumer is Negotiable: it takes the producer's per-slot runs
    STAGED = "staged"   # different assignment -> buffer in memtiles, then redistribute

def handoff(lo: SlotOrder, li: SlotOrder) -> Handoff:
    same = (not lo.replicated and not li.replicated and lo.slots == li.slots
            and all(np.array_equal(lo.indices(k), li.indices(k)) for k in range(lo.slots)))
    if not same:
        return Handoff.STAGED
    return Handoff.DIRECT if lo.tile == li.tile else Handoff.RETILE
# then STAGED -> ADOPT when the consumer is Local on a derived sequence and every
# producer run is a whole number of consumer blocks.
```

### 3.4 Resources

```python
@dataclass(frozen=True)
class Resources:
    cores: int
    pinned: frozenset[tuple[int, int]]   # (col, row) of pinned workers
    l1_bytes: int                        # busiest core: fifos x depth + buffers + stack
    core_dma_in: int                     # consumer fifos on the busiest core (<= 2)
    shim_in: int
    shim_out: int
    # not yet modelled: memtile bytes, BDs and locks per tile, program memory

class Overlay:
    def resources(self, target: Target) -> Resources: ...   # proposed; today read off design()
```

### 3.5 Edges, kinds, verdicts

```python
class Kind(Enum):
    CO_RESIDENCE = "co-residence"
    STREAM = "stream"
    KERNEL = "kernel"

class Blocker(Enum):
    SAME_DESIGN, CORE_BUDGET, PINNED_CORE_CLASH, SHIM_BUDGET,     # resources
    STATE, GRAPH_OUTPUT, MULTI_CONSUMER, COMPOSITE,               # graph / value
    UNDECLARED_ORDER, MEMTILE_BUDGET,                             # stream hand-off
    NO_CORE, NOT_FINAL, CONSUMER_NOT_LOCAL, TILE_SPLITS_BLOCK,    # kernel
    NO_DMA_CHANNEL, L1_BUDGET

@dataclass(frozen=True)
class Edge:
    producer: int   # step index
    consumer: int
    value: str      # root handle name (a slice resolves to its parent)
    role: str       # Handle.role of the root

@dataclass
class Verdict:
    edge: Edge
    blockers: dict[Kind, list[Blocker]]
    handoff: Handoff | None
    def legal(self, kind: Kind) -> bool: return not self.blockers[kind]
```

- `edges(t)` makes an edge from the latest writer of each root value to every
  later step that reads it. Edges through `role == "state"` (KV caches) are
  counted separately.
- `classify(t, edge, resources, dev) -> Verdict` implements §4.

---

## 4. Legality conditions per kind, and what breaks each

Notation:

- A is the producer and B the consumer.
- `v` is the value on the edge.
- `L` is `get_shim_dma_limit(dev)`, which is 16 per direction on the 8-column
  NPU2.

### 4.1 Co-residence

What changes: A and B are placed on disjoint tiles in one configuration. No
reconfiguration happens between them, and `v` still goes through DDR.

Conditions:

- **C1.** `design_key(A) != design_key(B)`. If the keys are equal, the
  back-to-back case is already free (`image/fusion.py:206-213`).
- **C2.** `cores(A) + cores(B) <= 4 × cols`, and `pinned(A) ∩ pinned(B) = ∅`.
  A real placement must exist; the tool checks counts only.
- **C3.** `shim_in(A) + shim_in(B) <= L`, and the same for `shim_out`. The tool
  checks the global total; per-column shim placement is not checked.
- **C4 (not modelled).** Memtile bytes and pins (MHA pins memtiles at cols 3,
  4, 6 and 7), BDs and locks per shim tile, and program memory.
- **C5 [speculative].** Toolchain support. Today `fuse_mlir` assumes one runtime sequence
  per `aie.device`: it reads the first one it finds (`fusion.py:27-40`). The main sequence emits
  `ConfigureOp`+`RunOp` per step and only skips configure when the op *name*
  repeats (`fusion.py:206-213`; its own TODO asks for the same-device
  optimisation).

  Co-residence needs one device holding several designs' cores and several
  named sequences, with `RunOp` selecting the sequence without
  reconfiguring. Whether aiex/aiebu supports several runtime sequences per
  device, and what a run-without-configure costs, is unmeasured. The ~11 µs
  same-design back-to-back cost suggests the target.
- Does **not** require: matching orders, a single consumer, a non-output
  value, or a non-state value. Any two ops qualify, including non-adjacent
  ones, which makes this a *packing* problem over the runlist.

Breakers observed:

- **Greedy shim defaults.** Every elementwise op and GEMV takes the full
  budget, so almost nothing fits beside it.
- **GEMM's 32 cores.**
- **MHA's pins.**
- **Same design.** In decode, 31 residual Add→Add edges are the same design,
  so co-residence has nothing to gain there.

### 4.2 Stream fusion

What changes: A's output stream feeds B's input stream on chip, and `v` never
reaches DDR.

Conditions:

- **S1.** Resources as C2 and C3, with `v`'s channels credited back:
  `shim_in(A) + shim_in(B) - slots(B.in[v]) <= L`, and likewise for `out`.
- **S2.** `v` is not state, is not a graph output, and has exactly one reader.
  Relaxations:
  - (a) A graph output could be *teed* to DDR at the cost of one more MM2S per
    slot.
  - (b) Several readers could all join the fused group, with the producer
    multicasting ("multi-consumer lifted" below).
- **S3.** Neither side is `Composite`.
- **S4.** Both orders are declared (`SlotOrder`, not `Undeclared`).
- **S5.** The hand-off is one of the following:
  - `DIRECT`: a core-to-core object fifo.
  - `RETILE`: the same per-slot indices with a different object size. This is
    repacked through a memtile link.
  - `ADOPT`: B is `Local(block)` on a derived sequence and every run of A is a
    multiple of `block`. B takes A's slot assignment, and B's other operands
    follow the same taps.
  - `STAGED`: a different assignment, so `v` is buffered in memtiles. This
    needs `bytes(v) <= memtile_bytes × cols` (512 KB per AIE2P memtile
    assumed).

  When B needs the whole value on every slot (GEMV's B vector), STAGED also
  serialises: B cannot start until A finishes. The DDR round trip is saved but
  there is no overlap.
- **S6 [not modelled].** Rate and deadlock:
  - A's object count per slot must equal B's;
  - fifo depths must cover any reordering;
  - B's other DDR operands must be issued concurrently in the one fused
    sequence.
- **S7.** Per-call values: a scratchpad-driven access (StridedCopy's
  `out_offset`) makes the order value-dependent, hence `Undeclared`. It does
  not block co-residence.

Breakers observed:

- shim as tuned;
- multi-consumer (the q/k/v and gate/up siblings);
- undeclared order (every override operator except GEMV);
- the 32-core GEMM;
- MHA (composite).

Order mismatches exist but are not blockers: a row op after a column-split
GEMV (scores→scale→softmax) is an ADOPT or a STAGE, not a failure.

### 4.3 Kernel fusion

What changes: B's kernel runs on A's core, on A's output object before
release. This is the GEMV `epilogue` pattern (`gemv/op.py:216-217`).

Conditions:

- **K1.** S2 and S3 hold.
- **K2.** A has a core (it is not DMA-only Movement), and B is
  `Local(block)`. `Contraction`, `Movement` and `Composite` consumers are out.
- **K3.** A's object is final at release (`Contraction.final_at_release`,
  which is true for GEMV and GEMM as written).
- **K4.** A's object holds whole B blocks, and A's slot runs start on block
  boundaries: `tile(A.out) % block == 0` and `run % block == 0`. This breaks
  in two cases:
  - GEMV→RoPE: a 32-element `tile_size_output` against a 64-element row;
  - Add→RMSNorm: a 256-element line against a 2048-element row.
- **K5.** Each of B's *other* operands needs its own S2MM channel on A's core:
  `core_dma_in(A) + |other inputs of B| <= 2`. **This is the binding
  constraint.** GEMV and GEMM cores already use both channels (A and B), so
  no binary consumer (a residual Add, the SwiGLU Mul) can join them.

  Reading the operand from a neighbour's shared memory is a possible
  workaround. [speculative]
- **K6.** L1: `l1(A) +` B's extra objects, LUTs and stack must fit in 64 KB.
  This fails for GEMM→Mul in prefill.
- **K7.** Numerics: B must run on the *rounded* output dtype, as it does
  unfused. Running it on an f32 accumulator before rounding changes the
  result, and accuracy is a hard constraint.
- **K8.** Pairwise legality is **not transitive**. Resources accumulate along
  a chain: GEMV→SiLU is legal and SiLU→Mul is legal, but GEMV→SiLU→Mul puts
  Mul's gate operand on the GEMV core as a third input. A chain pass must
  re-check K5 and K6 cumulatively.

### 4.4 Kinds the three-way taxonomy misses

- **Horizontal (sibling) fusion.** Several consumers of one value, of the same
  class and the same contraction axis, become one operator:
  - Q/K/V GEMVs: M = 2048 + 512 + 512, K = 2048;
  - gate/up GEMVs.

  It is legal when the siblings are independent and share the input's order.
  It removes MULTI_CONSUMER on 80 decode edges and saves two switches per
  group. This is how the lifted counts become achievable.
- **Movement folding [speculative].** StridedCopy, Repeat and Transpose are
  pure re-indexing. Instead of running them, fold their access pattern into
  the neighbour's DMA descriptor: the producer's drain or the consumer's
  fill. This is legal when the composed pattern fits the DMA's dimension and
  stride limits and, for scratchpad-offset copies, when the offset can drive
  the neighbour's descriptor. Earlier work shows a scratchpad value can
  drive a DMA address on hardware.

  In decode, 64 edges touch a DMA-only movement op. Folding the KV-cache
  StridedCopy into RoPE's/GEMV's drain would remove 32 steps (and their switches) per token.

---

## 5. Edge statistics

### Method

- Each graph is traced compile-free and tuned as `build_design` would tune it.
- Resources are read off `design()`.
- Every data edge is classified by §4.
- "Data edges" excludes the 32 decode edges that go through KV-cache state.
- Legal kinds are not exclusive: an edge can be legal under several kinds.

### Graphs

| Graph | What it is |
|---|---|
| llama_decode / llama_prefill | Llama-3.2-1B, 16 layers, rows 1 / 512, L = 2048, np.empty weights (no real weights read) |
| mlp_decode | MNIST-style MLP at batch 1: GEMV→ReLU→GEMV→GELU→GEMV→Sigmoid |
| mlp_batched | batch 256 on GEMM: GEMM→ReLU→GEMM→GELU→Add(residual)→LayerNorm→GEMM→Tanh |
| conv_as_gemm | im2col conv stack: GEMM→+bias→ReLU→GEMM→+bias→ReLU. IRON has no conv operator. |
| reduction_elementwise | RMSNorm(x, w)→SiLU→Mul(gate)→Softmax→Add(x), 64 × 4096 |

### Legal-edge counts (npu2; npu1 is identical where it runs)

In the co-residence and stream columns, "a / b" means legal as tuned / legal
ignoring the shim budget.

| Graph | Steps | Data edges | Co-residence | Stream | Stream hand-offs (as tuned) | Kernel | Stream, multi-consumer lifted (as tuned / + shim) | Runlist-adjacent |
|---|---|---|---|---|---|---|---|---|
| llama_decode | 386 | 432 | 32 / 401 | 81 / 210 | adopt 16, direct 32, staged 33 | 32 | 161 / 352 | 209 |
| llama_prefill | 291 | 369 | 17 / 114 | 17 / 17 | direct 16, staged 1 | 32 | 17 / 79 | 162 |
| mlp_decode | 6 | 5 | 0 / 5 | 5 / 5 | direct 3, staged 2 | 3 | 5 / 5 | 5 |
| mlp_batched | 8 | 7 | 0 / 2 | 2 / 2 | direct 1, retile 1 | 4 | 2 / 2 | 7 |
| conv_as_gemm | 6 | 5 | 0 / 2 | 2 / 2 | direct 2 | 2 | 2 / 2 | 5 |
| reduction_elementwise | 5 | 4 | 0 / 4 | 4 / 4 | adopt 2, direct 1, retile 1 | 3 | 4 / 4 | 4 |

### Blocker histograms, as tuned

An edge can have several blockers.

| Graph | Kind | Blockers |
|---|---|---|
| decode | co-residence | SHIM 400, SAME_DESIGN 31 |
| decode | stream | SHIM 191, MULTI_CONSUMER 142, UNDECLARED 80 |
| decode | kernel | NO_DMA_CHANNEL 288, CONSUMER_NOT_LOCAL 193, MULTI 142, TILE_SPLITS_BLOCK 80, NO_CORE 64 |
| prefill | co-residence | SHIM 320, CORE 224, SAME 31 |
| prefill | stream | UNDECLARED 290, SHIM 270, CORE 224, MULTI 206, COMPOSITE 64 |
| prefill | kernel | NO_DMA 303, MULTI 206, NOT_LOCAL 161, COMPOSITE 64, NO_CORE 34, UNDECLARED 33, L1 16 |
| mlp_batched | stream | CORE 5, UNDECLARED 5 (all GEMM) |
| conv_as_gemm | kernel | NO_DMA 2 (GEMM→+bias) |

### Llama decode edge patterns

C/S/K marks the kinds legal as tuned. Hand-offs are in brackets.

| Count | Edge | Legal | Why not more |
|---|---|---|---|
| 80 | WeightedRMSNorm → GEMV (q/k/v, gate/up) | - | multi-consumer → horizontal fusion |
| 32 | GEMV → RoPE | - | shim as tuned (S would be adopt); kernel: 32-element tile splits the 64-element row |
| 32 | GEMV → Mul (scores·scale, up·silu) | - | shim; kernel: no DMA channel for the second operand |
| 32 | GEMV → Add (residual) | - | shim; kernel: no DMA channel |
| 32 | Add → WeightedRMSNorm | - | multi-consumer (the residual is read twice); kernel: 256-element line splits the 2048-element row |
| 31 | Add → Add | - | same design; multi-consumer |
| 16 | RoPE → StridedCopy (K cache) | C | DMA-only consumer; order is scratchpad-driven → movement folding |
| 16 | GEMV → StridedCopy (V cache) | - | as above |
| 16 | Repeat → GEMV, Repeat → Transpose | Transpose: C | undeclared order (stride-0 read) |
| 16 | Transpose → GEMV | - | undeclared order |
| 16 | RoPE → GEMV (q → scores) | S (staged) | GEMV needs the whole vector on every column |
| 16 | Mul → DynamicSoftmax | S (adopt) | kernel: 256-element line vs 2048-element row |
| 16 | DynamicSoftmax → GEMV (→ ctx) | S (staged) | |
| 16 | GEMV → GEMV (ctx → o) | - | shim (would be staged) |
| 16 | GEMV → SiLU | S K (direct) | |
| 16 | SiLU → Mul | S K (direct) | but GEMV→SiLU→Mul as a chain fails K5 |
| 16 | Mul → GEMV (down) | - | shim (would be staged) |

### Non-Llama patterns

These show the model is not Llama-shaped.

- **Contraction → unary activation is kernel-legal** in every graph:
  GEMV→ReLU/GELU/Sigmoid and GEMM→ReLU/GELU/Tanh/SiLU. This holds *even
  though GEMM's order is undeclared*, because an elementwise consumer is
  order-agnostic.
- **Contraction → binary op is never kernel-legal** (conv bias, residual,
  SwiGLU), because of K5 (core DMA channels).
- **Elementwise chains are stream DIRECT.** An elementwise op followed by a
  row reduction is RETILE (Add→LayerNorm, RMSNorm→SiLU). A row op after an
  elementwise op, or the reverse, is ADOPT (Mul→Softmax, Softmax→Add).
- **Anything → contraction on a vector operand is STAGED**, because GEMV
  broadcasts x whole to every column.
- Anything touching GEMM's order is UNDECLARED.

### Configure points

The count sets the number of design switches and is anchored to the measured
321.

| Graph | Today (`op.design_key`) | Extent-free (overlay key, "O5") | Greedy co-resident packing | Extent-free + packing | Extent-free + packing, ignoring shim |
|---|---|---|---|---|---|
| llama_decode | **322** | 290 | 258 | 242 | 57 |
| llama_prefill | 243 | 211 | 226 | 194 | 129 |
| mlp_decode | 6 | 6 | 6 | 6 | 2 |
| mlp_batched | 8 | 8 | 8 | 8 | 6 |
| conv_as_gemm | 6 | 6 | 6 | 6 | 4 |
| reduction_elementwise | 5 | 5 | 5 | 5 | 2 |

What each column removes:

- **O5 (extent-free keys)** removes exactly two switches per decode layer: the
  q→k GEMV (same overlay, M 2048 vs 512) and the q→k RoPE (rows 32 vs 8).
  [verified]
- **Packing** is greedy along the runlist. A new configuration starts when
  the distinct designs no longer fit together in cores, pins and shim.

Decode time per token at ~75 µs per switch [estimate; assumes a co-resident
run costs about what a same-design run costs, which is speculative per C5]:

| Change | Switches removed | Time saved |
|---|---|---|
| O5 | 32 | ~2.4 ms |
| O5 + packing within today's shim tuning | 80 | ~6.0 ms |
| O5 + packing with the shim budget re-tuned away | 265 | up to ~19.8 ms of the 24 ms |

Stream and kernel fusion would add DDR savings on top. Those are not
estimated here.

---

## 6. Caveats

- **L1** is summed from fifos × depth + buffers + stack, not taken from the
  allocator. Bank conflicts and alignment are ignored.
- **Memtile** capacity is assumed to be 512 KB per AIE2P memtile. Memtile BDs
  and locks are not modelled.
- **Shim** is checked as a global per-direction total against
  `get_shim_dma_limit`. Per-column placement and per-shim BD budgets are not
  checked.
- **Core DMA** is modelled as 2 S2MM channels per core. Only consumer-fifo
  counts are used; MM2S is not checked.
- **Co-residence** assumes multiple runtime sequences per device work and are
  cheap. [speculative]
- **The ms figures** are estimates from the measured average.
- **GEMV's order** is modelled from reading `design(rt)`. The other override
  operators are `Undeclared` by construction, so their edges are not
  classified "illegal": they are *unknown*.
- **npu1 prefill** does not trace (MHA is NPU2-only). Every other graph gives
  identical counts on npu1 and npu2.

## 7. What to build first (recommendation)

1. **Make order authoritative.** Add `Operator.order(buffer) -> SlotOrder`.
   `transfers()` and every `design(rt)` emit from it. Fix `GEMVOverlay.b` to
   `replicate=True`. This unlocks every stream verdict, and it is useful
   without any fusion.
2. **Add `Overlay.semantics() -> Semantics`.** Make LayerNorm's line a
   `dim()`, not a tunable.
3. **O5: extent-free design keys**, with extents as residents or values:
   about 32 switches per decode token for bookkeeping only.
4. **Joint tuning under a shared budget.** Replace greedy `shim_columns`
   defaults in fused groups. This is a prerequisite for co-residence and for
   most stream fusions.
5. **Generalise GEMV's `epilogue` string** into kernel fusion of any
   `Local(1)` unary consumer onto a `Contraction(final_at_release=True)`
   core, gated by K4-K8.
6. **Horizontal GEMV fusion** for siblings sharing an input. This lifts the
   80 RMSNorm→GEMV multi-consumer edges.
