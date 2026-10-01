<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Automatic fusion of adjacent operators: mechanism

> Design notes from 2026-09-25, committed as written. `file:line` citations
> refer to the IRON tree of that date and may have drifted. The scratch scripts
> and run outputs the notes name were not kept.

Scope: how a generic pass gets from two adjacent operators to a fused design,
with no knowledge of which operators they are. Three mechanisms, from the
loosest coupling to the tightest. Paths are relative to IRON at
commit `16f01ff` (branch `autofusion/mechanism`, since merged into
`ehunhoff/onnpu-next`).

Legend: **[measured]** means verified here, on hardware or through the compiler.
**[read]** means read in the code. **[speculation]** means not verified.

## Summary

| Mechanism | Generic? | Built | Main blocker | Effort |
|---|---|---|---|---|
| 1. Co-residence (pack designs into one device config; dataflow stays in DDR) | Yes: works on device ops, reads no operator | Yes: MLIR, ELF, HW-correct, also through a traced graph | Ops default to the full array, so they must be narrowed before they fit | Built and hardened: pin conflicts tested, traced graph bit-exact on HW (-45% at 5 steps) |
| 2. Stream fusion (A's output fifo feeds B's cores on chip) | Yes, when the per-slot access patterns match (checkable from MLIR) | No | Needs (1) plus a merged runtime sequence | ~1 week [speculation] |
| 3. Epilogue fusion (B's kernel on A's core, on A's out buffer) | Only with a declared trait and hook | No | In-place aliasing and the core's code shape are per design | Narrow rule ~3 days; general: no [speculation] |

Recommendation: ship (1) behind the policy as built. Build (2) on top of it:
it reuses the merge and adds one rewrite plus a sequence merge. Keep (3) as a
per-overlay hook, not a graph pass.

---

## 1. Co-residence

### What it is
Temporal fusion (`iron/common/image/fusion.py:76 fuse_mlir`) gives each design
its own `aie.device`. The main sequence then does `aiex.configure @dev { aiex.run @sequence }`
per step, so every change of design is a PDI reload. Co-residence merges
several designs into one `aie.device`. Each member's runtime sequence keeps its
own symbol, and the main sequence configures the pack once and `aiex.run`s any
member's sequence. [read] mlir-aie allows several named
`aie.runtime_sequence`s per device: `RunOp` resolves `runtime_sequence_symbol`
inside the configured device (AIEXDialect.cpp ~1640-1680).

### Why it is generic
Every IRON design already has cores that loop forever, and each round is gated
by a lock that the design's own sequence sets. `ElementwiseOverlay.design`
shows this at `iron/common/elementwise.py:155-192`: `barrier.wait_for_value(1)`
followed by `range_(count[0])`. So a member's cores sit idle while another
member's sequence runs. [read] The existing rule that "consecutive steps of
one design share a configure point" (`needs_additional_reset`, fusion.py:56)
already assumes this re-entrancy. The merge itself never looks at an operator.

### Hook points (built)
- `iron/common/image/coresidence.py` (new):
  - `Packing` (:82) partitions the designs into device configurations. The
    device symbol is a digest of the member names (:123), so a pack has the
    same text wherever it is used.
  - `merge_devices` (:176) merges the device ops:
    - It namespaces every device-scope symbol per member (`_namespace`, :159).
      Fifos become `<design>__in0_0`, RTPs become `<design>__count_0`, and the
      runtime sequence becomes `@<design>`.
    - It dedupes kernel declarations, which are already digest-prefixed by
      `declare_kernel`, and raises if two declarations differ.
    - It shares pinned `aie.tile`s, but refuses a core or DMA program that two
      members pin to the same tile.
    - It leaves logical tiles to `aie-place-tiles`.
  - `fits` (:246) asks, in process, whether a union places, allocates and
    routes. It returns `None` or the diagnostic. `_FIT_PIPELINE` (:61) holds
    the resource stages of aiecc's own pipeline, in aiecc's order
    (`tools/aiecc/IRTransforms.h`):
    - `aie-place-tiles`, `aie-lower-scratchpad-parameters`;
    - the whole `aie-objectFifo-stateful-transform`;
    - lock, runtime-BD, BD-id and buffer-address assignment;
    - `aie-create-pathfinder-flows`.

    The first version ran `aie-objectfifo-allocate` alone. That pass on
    unsplit fifos checks nothing, so two members pinning one shim DMA channel
    passed as fitting. [measured]
  - `AdjacentPacking` (:288) is the automatic policy. It walks the runlist and
    grows the current pack while `fits` accepts the union. The placer is its
    only judge.
- `fusion.py:151` resolves an `AdjacentPacking` against the design texts.
  `:165-185` merges each pack. `:188-191` applies the parity rule on
  *devices*, not designs. `:228` configures only when the device changes.
  `:300` runs `packing.sequence_of(design)`.
- `fused.py:23 fused_plan` maps `seq.coresident` (operators) to design names,
  and `fused_identity` hashes the packing.
- `sequence.py:92` adds `OperatorSequence(coresident=[[op, ...]] | AdjacentPacking())`.
  It is refused unless `dispatch` is fused/auto.
- `iron/common/graph/trace.py:104 TracedGraph.sequence(**kwargs)` forwards
  kwargs, so `traced.sequence(coresident=AdjacentPacking())` needs no change.
  [measured, see Evidence] `GraphFunction.compile(...)` (`graph/compiled.py`)
  does **not** forward `coresident`: a `CompiledGraph` builds its sequence
  from `plan.dispatch` and the placement only. Wiring it through is a
  one-kwarg change, not made. [read]

### Evidence
- Prototype `prototype_coresidence.py` builds
  y = silu(a+b), 8192 bf16, 4 cores per op, three ways. MLIR for each was in
  `proto/`. Each builds to a full ELF through
  aiecc. [measured]
  - temporal: 2 devices, 2 configures.
  - packed (by hand): 1 device `pack2_eec80174` plus the parity reset. There
    is one `aiex.configure` holding `aiex.run @ElementwiseAdd_dec87329` and
    `@SiLU_e093313a`.
  - auto (`AdjacentPacking`): **byte-identical** to the hand-packed MLIR.
  - `full_elf_config.json` shows kernel `pack2_eec80174` with two instances.
  - The placer put the 8 cores in columns 0-1, rows 2-5.
- Negative case: at 8 cores per op, the policy declines. The diagnostic is
  `no ShimNOCTile ... all 8 ShimNOCTile(s) are at 8/16 input, 16/16 output
  channels used`. [measured]
- Temporal fused MLIR is **byte-identical** to the base branch when no packing
  is given (add, silu, add). [measured]
- Tests: `iron/tests/infrastructure/coresidence.py` has 12 tests, all real and
  compile-only, with no mocks. All 12 pass, as do the 4 `fused_identity`
  tests. [measured] They cover:
  - manual pack; auto equals manual; the shim-budget decline;
  - the pinned-core conflict; `Packing` validation; the stray-operator check;
  - an aiecc compile of a pack;
  - two members pinning one shim tile + MM2S channel (refused, "already in
    use"), and the same pin against another channel or column (fits);
  - `fusion.py` and `coresidence.py` lie under the fused identity's digest;
  - a traced `@iron.graph` packed through `TracedGraph.sequence`, compiled
    from an empty cache.
- Traced graph (`graph_coresidence.py`):
  - The graph is `silu(add(mul(silu(add(a, b)), b), b))`. Each op is narrowed
    to 2 columns, tile 256, on 8192 bf16.
  - The runlist has 5 steps over 3 designs, since add and silu recur and
    `share_designs` dedupes them.
  - Temporal has 6 configures (5 steps + the reset). `AdjacentPacking` puts
    all 3 designs in `pack3_85ae4d37`, for 2 configures (pack + reset).
  - Hardware run under `flock`, pmode turbo, 8 interleaved rounds × 50 calls:

    | variant | configures | µs (median of per-round medians) |
    |---|---|---|
    | temporal | 6 | 328.8 |
    | packed | 2 | 180.2 (**-45%**) |

    Per-round medians were 328-330 µs temporal and 179-183 µs packed.
  - Packed output is **bit-identical** to temporal. Both match the graph's own
    CPU reference (`GraphFunction.reference`) at rtol 4% / atol 1e-2 on 100%
    of elements.
  - That is ~37 µs per avoided configure point here, vs ~58 µs in the
    2-design case. [measured]
- Hardware (`hw_coresidence.py`, run under
  `flock`, pmode turbo, 8 interleaved rounds × 50 calls, median of per-round
  medians):

  | runlist | temporal configures | packed configures | temporal µs | packed µs |
  |---|---|---|---|---|
  | add → silu | 2 | 2 (pack + parity reset) | 188.9 | 191.6 (+1.4%) |
  | (add → silu) ×2 | 4 | 2 | 309.7 | 193.3 (**-38%**) |

  Packed output is **bit-identical** to temporal in both runlists. Both
  variants show the same deviation from the float numpy reference, so packing
  does not add any. The saving is ~58 µs per avoided configure point. In the
  packed ×2 case, the second add+silu costs ~2 µs. [measured, this size only]

### Blockers and limits
1. **Array budget: the real limiter.** An op fits a pack only if the union's
   cores and shim channels fit. `ElementwiseOverlay` and GEMM/GEMV default to
   every column the shim budget allows, so default-tuned ops will never pack.
   The policy honestly declines them. Packing pays when:
   - ops are small or latency-bound (decode-sized elementwise ops, norms), and
   - a graph-level tuner narrows them first.
   Narrowing trades compute width for fewer switches. **Built since** as
   `iron/common/graph/narrowing.py` (`JointNarrowing`) + `probe.py`, commits
   `0ded157`, `bebeaf4`; see "Joint narrowing tuner" below.
2. **The parity reset.** `--expand-load-pdis` alternates two empty PDIs, so an
   odd number of configure points costs one empty reset configure. A lone pack
   is therefore no cheaper than two designs (row 1 of the table).
   - The objective is the number of device transitions in the runlist, rounded
     up to even.
   - `AdjacentPacking` is greedy. A design recurring far apart (per layer)
     stays in the pack where it first appeared. It is not optimal: an interval
     or graph-coloring formulation would be. [read]
3. **NPU2 / full-ELF only.** An xclbin has one device per kernel. `packaging.py`
   forces xclbin on NPU1 and for `DispatchTime` values, so co-residence does
   nothing there. [read]
4. **Cache identity: no gap.** An earlier draft said `fused_identity` misses
   `fusion.py` and `coresidence.py`. That was wrong. `source_digest` hashes
   every `.py` under `jit_compile._GENERATOR_TREES`, and `iron/common` is one
   of them. An edit probe changed the identity, and reverting restored it.
   A test now pins that both files lie under the trees. [measured]
5. **Pinned resources.**
   - `via=Shim(col, ch)` on a declared stream is only read by External
     (downloaded-xclbin) overlays (`iron/common/external.py:277`). A built design
     never lowers it, so two built members cannot conflict through `via=`,
     and an External overlay has no device to co-reside. [read]
   - A built design pins a shim channel with `ObjectFifo.prod(tile=Tile(c, 0),
     channel=ch)`, which emits a logical shim tile with `prod_dma_channel`.
     Two members doing that on one channel are refused by the fifo lowering
     inside `fits` ("already in use"); another channel or column fits.
     `merge_devices` needs no change for it. [measured]
   - Two members pinning a core to one tile are refused: by `merge_devices` for
     `aie.tile`, and by the placer for `aie.logical_tile`. [measured]
6. **Untested member shapes** [speculation]:
   - designs whose cores terminate instead of looping; they break on any
     second run in one configure, same as today's same-design rule;
   - members with resident buffers.

### Effort to harden
Done: the identity check, the pinned-shim test (it found and fixed the fit
pipeline), the traced-graph path on hardware, `coresident` through
`GraphFunction.compile` (`7ac5546`), and the joint narrowing tuner below.

### Joint narrowing tuner (built)
- Model (measured, not assumed): `T = D0 + sum t_step + sum over device
  entries (base + sum member loads) + R if entries odd`. A configure's cost
  scales with what it loads (Add<->SiLU: 38 us at 1 column, 87 us at 8), so
  a flat switch cost is wrong. Calibrated on 3 pairs: D0 50-57, R 29-31,
  base 31-32 us (turbo).
- Probe: t_step = (T9 - T1)/8 per design and width, fresh buffers per step
  (repeating on one buffer flattered 4-col GEMVs ~15%, a cache effect).
  Narrower widths are candidates only if bit-identical to the default.
- Packer: exact partition search over connected sets of the runlist
  adjacency, with parity; placer asked lazily. Not a range DP over
  first-use order: Llama's RMSNorm-Add pair (4x/layer) is first used 13
  designs apart.
- Results (turbo, interleaved, all bit-identical): synthetic 596 -> 156 us;
  GELU MLP joint = greedy (-26..-34% paired; per-process bimodal DDR);
  Llama decode graph 121.4 -> 108.2 ms (greedy 109.2, 4/4 runs); Llama app
  decode 8.10 -> 9.08 tok/s (median of 4 alternating runs), KL identical.

---

## 2. Stream fusion (A → B on chip)

### Legality (generic, decidable from the packed MLIR)
For intermediate `t` written by A and read only by B:
- **Graph condition:** `t` is not a graph output and has exactly one reader
  (B, right after A). This comes from the runlist / `allocator.live_ranges`.
- **Per slot k:** A's drain `dma_configure_task_for @A__out_k` and B's fill
  `@B__in0_k` must touch `t` with identical `(offset, sizes, strides, len)`
  and the same issue order. The fifo element types must be equal.
  - In the packed prototype, slot 0 is `offset = 0 len = 2048 sizes = [1, 1, 1, 2048] strides = [0, 0, 0, 1]`
    on both sides (packed.mlir:194 and :365), and elem is `memref<256xbf16>`
    on both. [measured]
  - At the declaration level this is `transfers(t, A.y) == transfers(t, B.x)`
    per slot (`iron/common/design/runtime.py:264`, derived in `_derived`
    :56-77). That only covers derived sequences; an overlay with its own
    `sequence()` or a `design(rt)` override must be checked in MLIR.
- **Slot counts must match.** Otherwise the stream needs memtile re-tiling
  (split/join through a memtile). That is possible but no longer a plain
  rewire: ObjectFifo join cannot interleave sources (project memory). Out of
  scope for a first version.

### Rewrite (on the merged device, after `merge_devices`)
1. Retarget `aie.objectfifo @A__out_k`'s consumer from its shim to B's core
   tile, the consumer tile of `@B__in0_k`.
2. `replace_all_symbol_uses(B__in0_k → A__out_k)` inside B's core, then erase
   `@B__in0_k`.
3. Delete A's drain tasks and B's fill tasks for `t` (configure, start, await,
   free).
4. **Merge A's and B's runtime sequences into one.** This is the real work.
   Today they are two `aiex.run`s in sequence, and A's sequence ends by
   awaiting its drains. Once the drains are gone, A would leave in-flight fill
   tasks and cores blocked on a consumer that is not started yet. The merged
   sequence must:
   - issue both preambles (RTP writes, barrier `set_lock`s);
   - issue all fills;
   - await only B's drains.
   With no `t` transfer left in the main runlist, `t` also drops out of the
   arena.

### Hook points
- `coresidence.py` gets a pass after `merge_devices` that takes the runlist
  pairs.
- `fusion.py:224-300`: one `aiex.run` of the merged sequence replaces two.
- `fused.py:23 fused_plan` feeds the pairs, and the arena planner must learn
  that `t` is gone.

### Blockers and effort
- Merging sequence bodies in MLIR: concatenate the two `aie.runtime_sequence`
  regions over a union of arguments, then hoist awaits to the end. It is
  mechanical, but it must respect the 4-deep shim task queue and BD-id
  recycling (project memories on the push-queue and BD-free hazards).
- L1: B's core now also holds the producer side of a core-to-core fifo, unless
  the placer puts the cores in shared-memory neighbours. `fits` already checks
  this.
- The win is one DDR round trip of `t` plus a dispatch step. For bandwidth-bound
  elementwise chains that is potentially large. **Not measured.**
- Effort ~1 week including hardware tests. [speculation]

---

## 3. Kernel / epilogue fusion

### Mechanism
Run B's kernel on A's core, on A's acquired output element, before
`release(Produce)`. B's cores, fifos and sequence disappear, and A's drain
writes B's output. In `ElementwiseOverlay.design` this is exactly
`kernel_call` (`iron/common/elementwise.py:148`):

```python
kernel(*elements, self.line_size); epilogue(elements[-1], elements[-1], self.line_size)
```

### Why it is not a generic graph pass
- **Legality needs facts not in the IR or the declarations:**
  - B is pointwise;
  - B's kernel is safe in place (`in == out`; a `restrict`-qualified or
    look-ahead kernel is UB);
  - B's line size divides A's element;
  - both kernels fit one core's program memory.
  None of these are declared today. [read]
- **The splice point differs per design.** In elementwise it is after the one
  `func.call`. In a GEMM it is after the k-reduction, on the C tile, inside a
  loop nest the design owns. Finding "the call that last writes the out
  buffer" in MLIR works for single-call cores and is brittle beyond that.
  [speculation]

### Narrow version that is generic enough
- A declared `pointwise=True` (+ `in_place_safe`) trait on unary overlays.
- A producer-side hook `Overlay.epilogue_slot(kernel)` that templates such as
  Elementwise and GEMM implement at their `kernel_call`/C-release site.
- Adjacency and the trait decide; the producer's hook splices.

Effort ~3 days for elementwise→unary, and more per producer template.
[speculation] It is the right tool for GEMM+activation. Stream fusion (2)
covers the non-pointwise and the unhooked cases.

---

## Files
- `iron/common/image/coresidence.py` (new): merge, fit oracle, `Packing`, `AdjacentPacking`
- `iron/common/image/fusion.py`, `fused.py`, `sequence.py`: packing threaded through
- `iron/tests/infrastructure/coresidence.py`: 7 compile-only tests
- Not kept: `prototype_coresidence.py` (compile prototype),
  `hw_coresidence.py` (HW correctness + interleaved latency),
  `graph_coresidence.py` and `proto/{temporal,packed,auto}.mlir`
