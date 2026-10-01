<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Prior art: automatic operator fusion, for an IRON auto-fusion pass

> Design notes from 2026-09-25, committed as written. `file:line` citations
> refer to the IRON tree of that date and may have drifted. The scratch scripts
> and run outputs the notes name were not kept.

Date: 2026-09-25. Scope: this survey feeds the design of a general-purpose
auto-fusion pass for IRON (AIE2/AIE2P NPUs, MLIR-AIE). Everything is read-only:
no code was run and the NPU was not used.

How the claims were checked:

- Source-code claims were read from the files linked at the tag or branch
  named. Files on `main` branches move, so line-level details may drift.
- Paper claims were checked against the abstract, the arXiv HTML/PDF, or
  Crossref metadata.
- Anything I could not confirm from a primary source is marked **[unverified]**.

The IRON numbers used in the cost-model sections come from the Strix Point
measurements of 2026-09-25 (dispatch microbenchmarks):

- Dispatch costs about 159 µs on the device plus 53 µs of host round trip.
- Inside one full-ELF image, a further op of the **same** design costs about
  11 µs.
- A switch between **different** designs costs about 110 µs, falling to about
  105 µs in turbo mode.
- Llama decode runs 386 steps over 19 designs, with 321 switches. The switches
  cost about 24 ms, roughly 20% of each step.
- A dependency-legal reorder still leaves 321 switches, so the order is already
  switch-optimal.
- Peak DDR bandwidth is about 64-70 GB/s.

---

## 0. The three IRON fusion mechanisms, mapped to the literature

| IRON mechanism (from the brief) | Closest names in prior art |
|---|---|
| **(a) Co-residence:** several designs on disjoint tiles of one array configuration | Horizontal fusion (XLA horizontal loop fusion, IREE horizontal contraction fusion); heterogeneous co-resident accelerators (CHARM, SSR "spatial/hybrid"); Tenstorrent SubDevices; the AIR *segment*; configuration caching / multi-context in the reconfigurable-computing literature (Li, Compton, Hauck 2000) |
| **(b) Stream fusion:** producer to consumer on chip, with no DDR round trip | Layer fusion / layer pipelining (Alwani et al. MICRO'16, Tangram *segments*, SET, Stream, DFModel partitions); SambaNova's spatial kernel fusion; Plasticine/Spatial `Pipelined`/`Streaming` controllers |
| **(c) Kernel/epilogue fusion:** one kernel does several operations | TVM `kOutEWiseFusable` + elementwise; XLA loop/input fusion; Inductor vertical fusion; IREE dispatch regions; MLIR tile-and-fuse; ttnn `fused_activation`; AIE4ML fused bias+ReLU |

One fact shapes everything below. On GPUs, horizontal fusion only pays for
**independent** ops, and it saves a ~1 µs launch. In IRON, co-residence also
pays for **dependent** ops that still round-trip through DDR, because what it
saves is a ~110 µs reconfiguration.

That makes (a) closer to *configuration caching* (FPGA literature) than to GPU
horizontal fusion. Almost no ML-compiler cost model has a term shaped like it;
the reconfigurable-computing literature does.

---

## 1. General ML compilers

### 1.1 TVM (Relay FuseOps; Relax FuseOps / FuseOpsByPattern)

Paper: T. Chen et al., "TVM: An Automated End-to-End Optimizing Compiler for
Deep Learning", OSDI 2018, [arXiv:1802.04799](https://arxiv.org/abs/1802.04799).

**Metadata each op must supply.** One `OpPatternKind` per op
([`include/tvm/relay/op_attr_types.h` @ v0.14.0](https://github.com/apache/tvm/blob/v0.14.0/include/tvm/relay/op_attr_types.h)).
The kinds are totally ordered:

- `kElemWise`=0
- `kBroadcast`=1: "can always map output axis to the input in order"; the
  header notes that a transpose is not a broadcast.
- `kInjective`=2: "can always injectively map output axis to a single input
  axis. All injective operator can still be safely fused to injective and
  reduction."
- `kCommReduce`=3
- `kOutEWiseFusable`=4: "Complex operation, can still fuse elemwise
  operations into its output. but cannot chain another complex op."
- `kTuple`=7
- `kOpaque`=8

In Relax the kind is **inferred, not hand-labelled**.
[`src/relax/analysis/tir_op_pattern_kind.cc`](https://github.com/apache/tvm/blob/main/src/relax/analysis/tir_op_pattern_kind.cc)
(`AnalyzeOpPatternKind`) derives it from the TIR load/store index expressions:

- It takes the maximum of elemwise/broadcast/injective over all loads.
- A block with more than one store is opaque.

[`src/relax/transform/fuse_ops.cc`](https://github.com/apache/tvm/blob/main/src/relax/transform/fuse_ops.cc)
reads the resulting `op_pattern` attribute of each PrimFunc.

**Algorithm.** Implemented in
[`src/relay/transforms/fuse_ops.cc`](https://github.com/apache/tvm/blob/v0.14.0/src/relay/transforms/fuse_ops.cc)
and
[`src/relay/analysis/graph_partitioner.cc`](https://github.com/apache/tvm/blob/v0.14.0/src/relay/analysis/graph_partitioner.cc):

- The pass builds a **post-dominator tree**, using the LCA of consumers on the
  DAG.
- For node *n* with immediate post-dominator *p*, `CheckPath` verifies that
  every node on every path *n→p* satisfies a pattern-kind predicate.
  `CommitFuse` then unions all of them (union-find).
- It runs in three phases:
  - **Phase 0:** a `kOutEWiseFusable` node fuses into an elementwise
    post-dominator if all paths are ≤`kBroadcast`. A ≤`kBroadcast` node fuses
    into an injective/reduce post-dominator.
  - **Phase 1:** injective and tuple nodes fuse if all paths are ≤`kInjective`.
  - **Phase 2:** injective ops fuse into intermediate tuples.
- `CombinePattern` refuses to merge two groups that are both >`kBroadcast`
  ("Cannot merge two complex group together").

**Legality/budget knobs:**

- `kMaxFusedOps = 256`
- `relay.FuseOps.max_depth`
- The target attribute `max_function_args`, a limit on argument count.
- The `annotation.stop_fusion` op, a user-placed barrier.

There is **no cost model**: fusion is purely by legality, on the premise that
fusion is always profitable.

**Takeaway for IRON:**

- The ordered kind lattice and the post-dominator "everything between me and
  my post-dominator must be simple" rule are cheap, and they are proven.
- The rule "at most one complex (root) op per group" matches (c) exactly.
- "Always fuse if legal" is wrong for IRON (see §3).
- Relax's *derive the kind from access expressions* is the right model,
  because IRON operators already declare TAPs.

### 1.2 DNNFusion (a finer taxonomy than TVM)

W. Niu, J. Guan, Y. Wang, G. Agrawal, B. Ren, "DNNFusion: Accelerating Deep
Neural Networks Execution with Advanced Operator Fusion", PLDI 2021,
[doi:10.1145/3453483.3454083](https://doi.org/10.1145/3453483.3454083),
[arXiv:2108.13342](https://arxiv.org/abs/2108.13342).

**Metadata.** Each op has a *mapping type*:

- **One-to-One:** Add, Relu.
- **One-to-Many:** broadcast elementwise, Expand, Gather, Resize, Upsample.
- **Many-to-Many:** Conv, GEMM.
- **Reorganize:** Flatten, Reshape, Squeeze, Unsqueeze.
- **Shuffle:** DepthToSpace, SpaceToDepth, Transpose.

**Legality and profit.** Table 3 classifies every (producer type, consumer
type) pair:

- green: legal and profitable;
- yellow: legal, but profit must be profiled;
- red: illegal or unprofitable.

Many-to-Many × Many-to-Many and One-to-Many × Many-to-Many are not fusable.
The paper defines "transformation impedance" and resolves yellow cases from an
offline profiling database.

**Takeaway:**

- Reorganize and Shuffle get their own classes. TVM lumps them into
  "injective".
- For IRON this distinction matters: a reshape or transpose can often be
  absorbed into a neighbour's DMA access pattern for free, which is a
  "layout folding" case.
- The three-colour table (legal+profitable / legal+needs-cost-model / illegal)
  is a good shape for IRON's legality table.

### 1.3 XLA (instruction fusion, priority fusion, multi-output, horizontal)

Overview: D. Snider and R. Liang, "Operator Fusion in XLA: Analysis and
Evaluation", [arXiv:2301.13062](https://arxiv.org/abs/2301.13062). This is a
University of Toronto course-project paper, not a peer-reviewed venue.

**Producer/consumer legality**
([`xla/service/instruction_fusion.cc`](https://github.com/openxla/xla/blob/main/xla/service/instruction_fusion.cc)):

- `ShouldFuse` never fuses across the computation root.
- It refuses to **duplicate** an expensive producer that has several consumers
  (`is_expensive_`, `may_duplicate_`), unless the producer `IsAlwaysDuplicable`
  (e.g. a broadcast or a widening convert).
- `ReusesOperandElements` blocks fusion when the consumer reads producer
  elements many times, since that would recompute them.
- `ShouldFuseInPlaceOp` checks aliasing for in-place ops such as
  dynamic-update-slice.

**GPU priority fusion**
([`xla/backends/gpu/transforms/priority_fusion.cc`](https://github.com/openxla/xla/blob/main/xla/backends/gpu/transforms/priority_fusion.cc)):

- Producers sit in a priority queue keyed by `time_unfused − time_fused`.
- The pass greedily fuses the max-benefit producer into all its consumers,
  then updates only the neighbours' priorities.
- `CanFuse` checks the following:
  - not the root;
  - both sides `IsFusible`;
  - reduce-into-reduce is forbidden;
  - fusing into the output of a reduce fusion is forbidden;
  - `FusionFitsInBudget`;
  - `ProducerConsumerMergedTooLarge`;
  - a **cycle check**: the fusion must not create a path that leaves the group
    and comes back.

**Cost model**
([`xla/service/gpu/model/gpu_performance_model.cc`](https://github.com/openxla/xla/blob/main/xla/service/gpu/model/gpu_performance_model.cc),
[`gpu_performance_model_base.h`](https://github.com/openxla/xla/blob/main/xla/service/gpu/model/gpu_performance_model_base.h)):

- `time_unfused = kKernelLaunchOverhead·(n+1) + t(producer) + Σ t(consumer_i)`
- `time_fused = kKernelLaunchOverhead·n + Σ t(fused_i)`
- `kKernelLaunchOverhead = 1 µs`
- `kNcclKernelLaunchOverhead = 5 µs`
- Per kernel, `t = compute + memory − 0.95·min(compute, memory)`, with
  `kMemoryComputeParallelism = 0.95`.
- The multi-output variant compares 2× against 1× launch overhead.

**Resource budget**
([`xla/service/gpu/gpu_fusible.cc`](https://github.com/openxla/xla/blob/main/xla/service/gpu/gpu_fusible.cc)).
`FusionFitsInBudget` checks:

- shared memory per block;
- `kMaxUnnestedReductionOutputsPerFusion`;
- the parameter/operand count.

`ShapesCompatibleForMultiOutputFusion` ("Multi-output fusion kernels share a
common parallel loop") and `FusionHeroesAreCompatible` require the "hero" ops
(reductions/transposes) of the two sides to agree on iteration space.

**Multi-output fusion**
([`xla/backends/gpu/transforms/multi_output_fusion.cc`](https://github.com/openxla/xla/blob/main/xla/backends/gpu/transforms/multi_output_fusion.cc),
[`xla/service/multi_output_fusion.cc`](https://github.com/openxla/xla/blob/main/xla/service/multi_output_fusion.cc)):

- **Sibling MOF** fuses consumers of the same operand, sharing its read.
- **Producer-consumer MOF** keeps the producer's output live as an extra
  output of the fused kernel.
- Both have cycle checks and a small-parameter exemption (1024 bytes).

**Horizontal loop fusion**
([`horizontal_loop_fusion.h` @ TF v2.12](https://github.com/tensorflow/tensorflow/blob/v2.12.0/tensorflow/compiler/xla/service/gpu/horizontal_loop_fusion.h)).
It "horizontally fuses computations for reducing kernel launch overhead while
increasing kernel launch dims… does not change the amount of memory
read+written". Candidates are instructions whose outputs are all consumed by
the same instruction. I could not find this pass on current openxla `main`.

**Takeaway:**

- XLA gives the cleanest template for a **cost-driven greedy pass**: a
  benefit-ordered priority queue, local re-scoring, a hard legality predicate,
  a resource-budget predicate and a cycle check.
- Its model hard-codes one launch overhead. IRON must replace that with a
  **sequence-dependent** switch cost (§3).
- Multi-output fusion is the exact analogue of a stream-fused producer that
  must *also* drain its result to DDR for an outside consumer.

### 1.4 PyTorch Inductor (scheduler `can_fuse` / scoring)

Paper: J. Ansel et al., "PyTorch 2: Faster Machine Learning Through Dynamic
Python Bytecode Transformation and Graph Compilation", ASPLOS 2024
([PDF](https://docs.pytorch.org/assets/pytorch2-2.pdf)).

**Metadata.** Each scheduler node carries read and write sets of `MemoryDep`
objects: buffer name, index expression and loop ranges (sympy).

**Legality**
([`torch/_inductor/scheduler.py`](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/scheduler.py)):

- `can_fuse_vertical` requires that "all the reads of node2 either match
  corresponding writes in node1, or are written by nodes that can be scheduled
  before".
- Index expressions must be identical: `MemoryDep(x)` vs `MemoryDep(x+1)` is
  rejected ("memory deps did not match").
- `will_fusion_create_cycle` is checked.
- `fusion_prevent_too_many_reads_and_writes` is checked.
- `are_long_distant_nodes` is checked.
- `speedup_by_fusion` optionally benchmarks the fused kernel.

**Heuristics and scoring**
([`torch/_inductor/choices.py`](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/choices.py)):

- `can_fuse` rejects:
  - pairs with `shared_data_score == 0`;
  - fusions larger than `config.max_fusion_size`;
  - fusions that raise peak memory (`can_fusion_increase_peak_memory`);
  - fusions over `max_fusion_unique_io_buffers`.
- `can_fuse_horizontal` uses `score_fusion_memory_threshold` and the
  long-distance check.
- `score_fusion` returns a lexicographic `FusionScore` of template score, node
  type, memory score (bytes shared), buffer overlap and proximity.

**Takeaway:**

- The legality test is **exact equality of access functions** on the shared
  buffer. That is precisely the stream-fusion (b) condition in IRON: the
  producer's write order and tiling must match the consumer's read order and
  tiling.
- Proximity and peak-memory guards are cheap and worth copying.

### 1.5 IREE (dispatch-region formation)

**Metadata.** IREE uses linalg structure: iterator types
(parallel/reduction), indexing maps, and `TilingInterface`.

The core file is
[`compiler/src/iree/compiler/DispatchCreation/FormDispatchRegions.cpp`](https://github.com/iree-org/iree/blob/main/compiler/src/iree/compiler/DispatchCreation/FormDispatchRegions.cpp):

- **Root ops** (`isRootLikeOp`):
  - linalg named ops except fill;
  - `linalg.generic` with reduction loops;
  - TilingInterface ops except gather/pad/concat/pack.
- Each dispatch region is formed around one root. A `FusionGroup` records, for
  every member, the `AffineMap` from the root's outer parallel loops to that
  op's loops.
- A consumer fuses only if **all** of these hold:
  - it is all-parallel;
  - it shares the root's iteration space;
  - it has no more non-unit loops than the root;
  - it can bufferize in place (`canUseInOperandAsInitOperand`);
  - it does not exceed `kIreeMaxOperandCount` (`wouldExceedOperandLimit`).
- Producer fusion is mostly restricted, and the CPU backend requires identity
  indexing maps.

[`FuseHorizontalContractions.cpp`](https://github.com/iree-org/iree/blob/main/compiler/src/iree/compiler/DispatchCreation/FuseHorizontalContractions.cpp)
merges matmuls that share an LHS into one multi-result op. This is the QKV
pattern.

**Takeaway:**

- The "one root per group, plus elementwise consumers expressed as affine maps
  of the root's parallel loops" model is TVM's rule with a precise, general
  legality test.
- Horizontal contraction fusion is a concrete, cheap (a)/(c) hybrid for IRON:
  GEMVs that share an input become one op with concatenated weights.

### 1.6 MLIR tile-and-fuse (TilingInterface, linalg fusion)

**Interface.**
[`mlir/include/mlir/Interfaces/TilingInterface.td`](https://github.com/llvm/llvm-project/blob/main/mlir/include/mlir/Interfaces/TilingInterface.td)
requires the following of each op:

- `getLoopIteratorTypes`
- `getIterationDomain`
- `getTiledImplementation`
- `getResultTilePosition`
- `generateResultTileValue`
- `getTiledImplementationFromOperandTiles`
- `getIterationDomainTileFromOperandTiles`
- `getIterationDomainTileFromResultTile`
- `isOpFusableWithConsumerSlice`
- `isOpFusableWithProducerSlices`
- the partial-reduction hooks

**Drivers.**
[`mlir/lib/Dialect/SCF/Transforms/TileUsingInterface.cpp`](https://github.com/llvm/llvm-project/blob/main/mlir/lib/Dialect/SCF/Transforms/TileUsingInterface.cpp)
provides:

- `scf::tileConsumerAndFuseProducersUsingSCF`, which tiles the consumer and
  pulls producer tiles in by *recomputing the producer tile for each consumer
  tile*;
- `scf::tileAndFuseConsumerOfSlices`.

**Elementwise fusion.**
[`mlir/lib/Dialect/Linalg/Transforms/ElementwiseOpFusion.cpp`](https://github.com/llvm/llvm-project/blob/main/mlir/lib/Dialect/Linalg/Transforms/ElementwiseOpFusion.cpp)
defines `areElementwiseOpsFusable`, which requires:

- the producer is a `linalg.generic` with tensor semantics and all-parallel
  loops;
- the producer feeds a consumer input, not an init operand;
- the consumer's indexing map for that operand has as many results as the
  producer has loops;
- the producer's result map is a permutation;
- reductions keep all loop bounds computable.

**Takeaway.** The metadata IRON would need is exactly a
TilingInterface-shaped contract:

- "given an output tile, which input tiles do I need" (`getIterationDomainTileFromResultTile`);
- "is fusion with this slice legal" (`isOpFusable*`).

IRON's TAP already *is* the tile-position function at the L3 boundary.

### 1.7 Related research systems (brief)

- **Welder** (Y. Shi et al., OSDI 2023,
  [USENIX page](https://www.usenix.org/conference/osdi23/presentation/shi)).
  Operators are described as tile-graphs, and fusion is chosen per memory
  level by a cost model of traffic at each level. Hierarchical memory makes
  this the closest to IRON's L1/L2/L3.
- **AStitch** (Zheng et al., ASPLOS 2022,
  [doi:10.1145/3503222.3507723](https://doi.org/10.1145/3503222.3507723)).
  Memory-intensive op stitching with hierarchical data reuse.
- **Korch** (Hu et al., "Optimal Kernel Orchestration for Tensor Programs with
  Korch", ASPLOS 2024,
  [doi:10.1145/3620666.3651383](https://doi.org/10.1145/3620666.3651383)).
  Fissions ops into primitives, then chooses kernels by binary linear
  programming. An example of MILP-optimal kernel selection.
- **Chimera** (Zheng et al., HPCA 2023,
  [doi:10.1109/hpca56546.2023.10071018](https://doi.org/10.1109/hpca56546.2023.10071018))
  fuses compute-intensive chains such as GEMM→GEMM.
- **TileFlow** (Zheng et al., MICRO 2023,
  [doi:10.1145/3613424.3623792](https://doi.org/10.1145/3613424.3623792))
  models the fusion dataflow space on accelerators.

These are relevant if IRON ever wants GEMM→GEMM fusion, which DNNFusion marks
red.

---

## 2. Spatial and dataflow accelerators

### 2.1 Layer fusion and segment scheduling on tiled accelerators

- **Fused-layer CNN accelerators** (M. Alwani, H. Chen, M. Ferdman, P. Milder,
  MICRO 2016,
  [doi:10.1109/micro.2016.7783725](https://doi.org/10.1109/micro.2016.7783725)).
  This is the original "keep intermediate feature maps on chip across layers"
  paper.

- **TETRIS** (Gao et al., ASPLOS 2017,
  [doi:10.1145/3093336.3037702](https://doi.org/10.1145/3093336.3037702)).
  Its NN-dataflow scheduler is the predecessor of Tangram.

- **Tangram** (M. Gao, X. Yang, J. Pu, M. Horowitz, C. Kozyrakis, ASPLOS 2019,
  [doi:10.1145/3297858.3304014](https://doi.org/10.1145/3297858.3304014); tool
  [stanford-mast/nn_dataflow](https://github.com/stanford-mast/nn_dataflow)).
  **This is the closest match to IRON's (b)+(a) problem.**
  - "At each time, only a single segment of layers is scheduled… Only the
    first layer input and the last layer output in the segment require
    off-chip accesses."
  - The engine array is spatially partitioned among the segment's layers, and
    successive segments are time-multiplexed. The paper discusses the
    pipeline fill/drain cost of each segment.
  - **Segment legality:**
    - Segments are selected in topological order.
    - A layer joins the current segment only if it shares a dependency with
      it, either a producer in the segment or a shared off-chip input.
    - A layer's output must be consumed entirely inside the segment or else
      written off-chip. Partial splits are avoided, with an LSTM-motivated
      relaxation that allows one outside consumer.
  - ACT/POOL/element-wise layers are merged into the preceding CONV/FC
    *region*. That is epilogue fusion (c) folded into the spatial mapping.
  - There is an explicit trade-off between deeper segments (more DDR saved,
    fewer engines per layer, more fill/drain) and shallower ones.
  - Search: dynamic programming over segment boundaries plus beam search over
    region allocations.

- **SET** (J. Cai et al., "Inter-layer Scheduling Space Definition and
  Exploration for Tiled Accelerators", ISCA 2023,
  [doi:10.1145/3579371.3589048](https://doi.org/10.1145/3579371.3589048)).
  - A *Resource Allocation Tree* notation expresses nested
    spatial/temporal partitioning of layers onto tiles.
  - It explores a strictly larger space than Tangram's segments, and reports
    1.78× over Tangram. Check the metric in the paper before quoting this
    number.

- **Stream** (A. Symons, L. Mei, S. Colleman, P. Houshmand, S. Karl,
  M. Verhelst, IEEE Trans. Computers 2025,
  [doi:10.1109/tc.2024.3477938](https://doi.org/10.1109/tc.2024.3477938);
  [kuleuven-micas/stream](https://github.com/kuleuven-micas/stream)).
  - Layer-fused scheduling for heterogeneous multi-core accelerators, with
    fine-grained computation nodes.
  - Reports up to 2.2× lower EDP.
  - **Already integrated into IRON**:
    - `iron/common/stream/mapping.py` holds hand-declared `Placement(columns,
      splits, kernel_kwargs, rows)` and `FusedGroup(name, layers,
      intra_core_tiling)`. `group_boundaries()` computes each group's external
      I/O.
    - `iron/operators/swiglu_prefill_stream/` is the one stream-fused
      operator.
    - `requirements_stream.txt` requires `stream-dse>=1.13.14`, whose
      MILP-based "TETRA" allocation emits MLIR-AIE.
  - Today the **grouping and placement are manual**. An auto-fusion pass could
    *produce* `FusedGroup`/`Placement` and reuse stream-dse as the backend for
    (b).

- **DFModel** (S. Ko, N. Zhang, O. Hsu, A. Pedram, K. Olukotun,
  [arXiv:2412.16432](https://arxiv.org/abs/2412.16432)).
  - A MILP (Gurobi) assigns kernels to *sequential partitions* on each chip,
    subject to tile-count, SRAM and DRAM capacity.
  - A tensor crossing partitions pays a DRAM store+load.
  - The objective sums each partition's critical-path latency.
  - I found **no explicit reconfiguration-cost term** in the parts I read.

- **LoopTree** (Gilbert et al., ISPASS 2023) models the fused-layer dataflow
  design space. I checked only the title and venue.

### 2.2 Versal AIE and AMD NPU work

- **CHARM** (J. Zhuang et al., 13 authors including J. Lo, K. Denolf,
  S. Neuendorffer, J. Cong, P. Zhou, FPGA 2023,
  [doi:10.1145/3543622.3573210](https://doi.org/10.1145/3543622.3573210),
  [arXiv:2301.02359](https://arxiv.org/abs/2301.02359)). **Canonical prior art
  for co-residence (a).**
  - It composes several heterogeneous matmul accelerators on one Versal array,
    running concurrently, instead of one monolithic accelerator.
  - The CDAC allocator sorts MM kernels by op count, splits them into *n*
    groups, and assigns AIEs/PLIOs in proportion to work.
  - Reported gains over a single monolithic accelerator: BERT 5.40× (the arXiv
    abstract; the HTML body says 5.29×, a version difference), ViT 32.51×,
    NCF/MLP 1.00×.
  - Everything is static: **no reconfiguration is modelled**.
  - Follow-up: CHARM 2.0, ACM TRETS 2024,
    [doi:10.1145/3686163](https://doi.org/10.1145/3686163).

- **SSR** (J. Zhuang et al., FPGA 2024,
  [doi:10.1145/3626202.3637569](https://doi.org/10.1145/3626202.3637569),
  [arXiv:2401.10417](https://arxiv.org/abs/2401.10417)).
  - Explicit taxonomy:
    - *sequential*: one accelerator reused over time;
    - *spatial*: one accelerator per layer;
    - *hybrid*: any layers onto any accelerators.
  - Search is evolutionary over the Layer→Accelerator map, with greedy
    pipeline scheduling and on-chip forwarding between accelerators.
  - Force-partitioning avoids memory-bank conflicts.
  - It is static, so there is no reconfiguration cost.
  - Reports DeiT-T at 0.54 ms on a VCK190 using 394/400 AIEs.

- **ARIES** (J. Zhuang, S. Xiang, H. Chen, N. Zhang, Z. Yang, T. Mao,
  Z. Zhang, P. Zhou, FPGA 2025,
  [doi:10.1145/3706628.3708870](https://doi.org/10.1145/3706628.3708870);
  [arc-research-lab/Aries](https://github.com/arc-research-lab/Aries)).
  - An MLIR-based flow with task-level and tile-level parallelism: different
    kernels map to separate AIE cores.
  - Reports GEMM at 1.17-1.59× over CHARM.
  - On a **Ryzen AI NPU**, it reports a ResNet residual layer at up to 22.58×
    over Riallto.

- **MaxEVA** (E. Taka, A. Arora, K.-C. Wu, D. Marculescu, ICFPT 2023,
  [doi:10.1109/icfpt59805.2023.00016](https://doi.org/10.1109/icfpt59805.2023.00016),
  [arXiv:2311.04980](https://arxiv.org/abs/2311.04980)).
  - Matmul kernel placement and patterns on the Versal AIE, reporting up to
    2.19× over prior work.
  - It is single-op, so it matters only for per-design tuning.

- **AutoMM** ([arXiv:2305.18698](https://arxiv.org/abs/2305.18698), Zhuang,
  Yang, Zhou et al.): multi-datatype MM on Versal. **[venue unverified]**

- **AIE4ML** (Danopoulos et al.,
  [arXiv:2512.15946](https://arxiv.org/abs/2512.15946)).
  - End-to-end NN compilation onto AIE-ML with fused bias+ReLU epilogues and
    the whole model kept on chip via memtiles.
  - Graph placement search, using 296/304 tiles.
  - A pure-spatial (never reconfigure) point in the space.

- Marginal: GAMA ([arXiv:2504.09688](https://arxiv.org/abs/2504.09688)) and
  EA4RCA ([arXiv:2407.05621](https://arxiv.org/abs/2407.05621)) are single-op
  or regular-algorithm AIE design frameworks.

- **MLIR-AIR** (Wang et al., including Hunhoff and Rösti, "From Loop Nests to
  Silicon: Mapping AI Workloads onto AMD NPUs with MLIR-AIR",
  [arXiv:2510.14871](https://arxiv.org/abs/2510.14871); compute model in
  [`docs/AIRComputeModel.md`](https://github.com/Xilinx/mlir-air/blob/main/docs/AIRComputeModel.md)).
  - A **launch** "groups co-resident work" and guarantees that its segments
    are co-resident.
  - A **segment** is a "physically contiguous grouping of processing elements
    together with their associated L2". Its resources are known statically,
    and all its instances are active simultaneously.
  - A **herd** is an always-parallel array of PEs.
  - The paper shows fused MHA in about 150 lines, but fusion is
    **user-directed**, not automatic.
  - The AIR hierarchy is a ready vocabulary for IRON's co-resident region (see
    §4.4).

- **IRON** (E. Hunhoff, J. Melber, K. Denolf, A. Bisca, S. Bayliss,
  S. Neuendorffer, "Efficiency, Expressivity, and Extensibility in a
  Close-to-Metal NPU Programming Interface", FCCM 2025,
  [doi:10.1109/fccm62733.2025.00043](https://doi.org/10.1109/fccm62733.2025.00043)).

- **Rösti & Franz**, "Unlocking the AMD Neural Processing Unit for ML Training
  on the Client Using Bare-Metal-Programming Tools", FCCM 2025
  ([doi:10.1109/fccm62733.2025.00031](https://doi.org/10.1109/fccm62733.2025.00031),
  [arXiv:2504.03083](https://arxiv.org/abs/2504.03083)).

- **Riallto**
  ([software framework notebook](https://riallto.ai/notebooks/4_1_software_framework.html)).
  - `AppBuilder.callgraph()` composes kernels and data movement (memtile,
    tile-to-tile) into **one** xclbin, with one or several kernels per compute
    tile.
  - Composition is manual. The docs I read say nothing about reconfiguration
    cost.

- **Vitis AI** (UG1414 compiler page). It lists "computation node fusion, e.g.
  batch norm fused into a preceding convolution". **[unverified]** How the DPU
  compiler partitions graphs between DPU and CPU, and any cost model behind
  it.

### 2.3 Dataflow machines

- **SambaNova SN40L** (R. Prabhakar et al., MICRO 2024,
  [arXiv:2405.07518](https://arxiv.org/abs/2405.07518)).
  - "without fused operations, smaller models have lower operational
    intensity."
  - Fusion is a "combination of automatic compiler optimizations and
    programmer hints" (§VI-A1). "SN40L fuses entire decoders into a single
    kernel call."
  - Llama-7B prefill needs 11× fewer kernel launches.
  - Decode gains 1×-13× from fusion and a further 1.4×-8× from
    *hardware-orchestrated kernel launch*.
  - This is the strongest published evidence that on spatial dataflow parts
    **per-kernel launch/reconfiguration overhead is first-order for decode**,
    as IRON's 20% figure also shows.

- **Plasticine** (R. Prabhakar et al., ISCA 2017,
  [doi:10.1145/3079856.3080256](https://doi.org/10.1145/3079856.3080256)) and
  **Spatial** (D. Koeplinger et al., PLDI 2018,
  [doi:10.1145/3192366.3192379](https://doi.org/10.1145/3192366.3192379)).
  - Spatial's controllers carry a schedule per
    [spatial-lang.org/control-flow](https://spatial-lang.org/control-flow):
    - `Pipelined` is the default: children run as a coarse-grained pipeline.
    - `Sequenced`: one child at a time.
    - `ForkJoin`: children run in parallel.
    - `Streaming`: children are driven by stream/FIFO availability.
  - This is a per-region choice between time-multiplexing and on-chip
    pipelining/streaming, the same (b)-vs-sequential decision, expressed
    hierarchically.

- **SARA** (Y. Zhang et al., ISCA 2021,
  [doi:10.1109/isca52012.2021.00085](https://doi.org/10.1109/isca52012.2021.00085))
  compiles Spatial programs by decomposing the program graph across
  distributed heterogeneous resources.

- **Cerebras** (S. Lie, "Cerebras Architecture Deep Dive", IEEE Micro 2023,
  [doi:10.1109/mm.2023.3256384](https://doi.org/10.1109/mm.2023.3256384); Hot
  Chips 34,
  [doi:10.1109/hcs55958.2022.9895479](https://doi.org/10.1109/hcs55958.2022.9895479)).
  **[unverified]** The two execution modes: layer-pipelined, with the whole
  model spatially laid out, and weight streaming, with one layer at a time and
  weights streamed. I could not fetch a primary text describing them, so treat
  this as secondary knowledge.

- **Graphcore**
  ([PopART performance guide](https://docs.graphcore.ai/projects/popart-user-guide/en/latest/performance.html)).
  - Pipelining and IPU placement are **user-annotated** (`pipelineStage`,
    `virtualGraph`), not automatic.
  - Microbenchmarks: Jia et al., "Dissecting the Graphcore IPU Architecture via
    Microbenchmarking", [arXiv:1912.03413](https://arxiv.org/abs/1912.03413).
  - **[unverified]** Any automatic fusion inside Poplar.

- **Tenstorrent tt-metal / ttnn:**
  - `ttnn.matmul(..., program_config, activation, core_grid)` supports a fused
    activation, carried as `fused_activation` in the sharded program configs
    (ttnn.matmul API docs). This is manual epilogue fusion (c).
  - Tech report *AdvancedPerformanceOptimizationsForModels*: **Metal Trace**
    records dispatch commands to DRAM and replays them, shrinking op-to-op
    gaps. IRON's full-ELF runlist is the analogous mechanism.
  - Tech report *SubDevices*: disjoint core groups run programs concurrently,
    each with its own allocator. This is a runtime-level analogue of
    co-residence (a).
  - As far as I read, fusion and co-residence are user-chosen in ttnn models.

### 2.4 Classic reconfigurable-computing scheduling

This is where reconfiguration cost *is* a first-class term:

- **Temporal partitioning.**
  - K. M. G. Purna and D. Bhatia, "Temporal partitioning and scheduling data
    flow graphs for reconfigurable computers", IEEE TC 1999,
    [doi:10.1109/12.773795](https://doi.org/10.1109/12.773795).
  - M. Kaul and R. Vemuri, "Optimal temporal partitioning and synthesis for
    reconfigurable architectures", DATE 1998,
    [doi:10.1109/date.1998.655887](https://doi.org/10.1109/date.1998.655887),
    an ILP.
  - Both cut a DAG into a sequence of device-sized partitions, each one
    configuration, and minimise the number of partitions and the inter-partition
    traffic. **This is the IRON problem with (a)+(b) collapsed.**
- **Configuration prefetch.** S. Hauck, "Configuration prefetch for single
  context reconfigurable coprocessors", FPGA 1998,
  [doi:10.1145/275107.275121](https://doi.org/10.1145/275107.275121).
  Prefetching overlaps the next configuration load with current execution.
- **Configuration caching.** Z. Li, K. Compton, S. Hauck, "Configuration
  caching management techniques for reconfigurable computing", FCCM 2000,
  [doi:10.1109/fpga.2000.903390](https://doi.org/10.1109/fpga.2000.903390).
  It keeps several configurations resident (multi-context/partial) to avoid
  reloads. **This is co-residence (a) viewed as a cache.**
- **Sequence-dependent setup times.** A. Allahverdi, "The third comprehensive
  survey on scheduling problems with setup times/costs", EJOR 2015,
  [doi:10.1016/j.ejor.2015.04.004](https://doi.org/10.1016/j.ejor.2015.04.004).
  The formal home of "a switch A→B costs s(A,B), and 0 if A=B".

---

## 3. Cost models

### 3.1 What the literature models, and what it omits

| System | Launch / reconfig term | DDR traffic | Compute | On-chip memory limit | Search |
|---|---|---|---|---|---|
| TVM | none (always fuse) | implicit | none | arg/depth caps | post-dominator rules |
| XLA GPU | constant 1 µs per kernel | bytes / BW | FLOPs / peak, 0.95 overlap | shared memory, operands | greedy priority queue |
| Inductor | implicit (score) | shared-bytes score | optional benchmark | peak memory, I/O cap | greedy by score |
| IREE | none | implicit | none | operand cap | root-anchored greedy |
| Tangram | segment fill/drain | only segment boundary I/O | per-region model | buffer fit | DP + beam |
| DFModel | none found | cross-partition store+load | per-partition critical path | SRAM/DRAM/tiles | MILP |
| Stream | per-node timing | modelled | modelled | modelled | GA / MILP |
| CHARM / SSR | none (static) | modelled | modelled | AIE/PLIO/BRAM | proportional / evolutionary |
| Temporal partitioning | #partitions × reconfig | inter-partition | yes | device capacity | ILP / heuristics |

None of the ML-compiler models has a **sequence-dependent** reconfiguration
term. XLA's constant per-kernel overhead is the nearest. The FPGA temporal
partitioning and setup-time literature has one.

### 3.2 The cost model this implies for IRON

A schedule is an ordered list of **steps**. Each step runs one operator, or one
stream-fused group, inside a **configuration** *C*: a set of co-resident
designs placed on disjoint resources. The model:

```
T = Σ_steps  t_step(op | resources given to it in C)
  + Σ_adjacent pairs  s(C_i, C_{i+1}, d_i, d_{i+1})
  (+ per-dispatch fixed ~150-159 µs, amortised by the full-ELF runlist)

t_step ≈ max(compute(op, tiles), DDR_bytes(op) / BW_DDR) + fill_drain(group)
s(C, C', d, d') ≈ 11 µs    if C' = C and d' = d (same design)
                ≈ ?        if C' = C, d' ≠ d (co-resident, different region: MEASURE)
                ≈ 80-110 µs if C' ≠ C
```

For t_step, use XLA's combination `compute + mem − 0.95·min` if overlap is
imperfect.

Key properties:

1. **Break-even.** One switch (~110 µs) costs as much as moving about
   **7 MB** at 64 GB/s.
   - Llama decode activations are KBs, so in decode the DDR saved by stream
     fusion (b) is negligible next to the switch it removes.
   - Decode wins therefore come from *removing switches*, through (a) or (b).
     It does not matter which, except that (b) also removes a step.
   - In prefill the activations are MBs, and DDR savings start to count.
2. **Co-residence costs throughput.** A design squeezed from 8 columns to 2
   runs slower. That is CHARM's central trade-off, and Tangram's
   deeper-vs-shallower segment trade-off. For bandwidth-bound ops like decode
   GEMV, the DDR roof saturates at about 4 channels (`project_npu_fabric_rates`),
   so shrinking may cost little. Compute-bound ops pay roughly linearly.
3. **The in-config switch cost is the unknown the whole (a) strategy rests
   on.** The ~11 µs figure is for the same design. The cost of a step that
   runs a *different* sub-design within the same configuration has to be
   measured before the model can be trusted.
4. **Reorder alone is exhausted.** The Llama decode order is already
   switch-optimal (321 switches either way). Reordering only becomes useful
   again *jointly* with co-residence, because grouping steps whose designs
   share a configuration then pays off. This is a sequence-dependent-setup
   scheduling problem (Allahverdi) over a DAG.
5. **Prefetch is an open question.** If reconfiguring toward C_{i+1} could
   overlap step i (Hauck 1998), s(·) would shrink for every mechanism. Whether
   the NPU firmware or ELF flow allows this is unknown.

### 3.3 Fusion under limited on-chip memory

The rules that recur across the literature:

- **Stream fusion needs a FIFO, not the tensor.** This holds only when the
  consumer reads the producer's output in the order it was written, once (see
  Inductor's MemoryDep equality and XLA's `ReusesOperandElements`).
  Otherwise the intermediate must be materialised whole in L2/L1, or the
  producer recomputed (MLIR tile-and-fuse; forbidden by XLA when the producer
  is expensive).
- **Reductions break streaming.** A split-K or row reduction yields no output
  until it has consumed all its input. Downstream stream fusion then degrades
  to "stage the whole tensor on chip", which is legal only if it fits
  (Tangram's buffering, DFModel's SRAM constraint).
- **Resource budgets are hard constraints, not costs** (XLA
  `FusionFitsInBudget`, IREE operand limit, DFModel tile/SRAM constraints). For
  IRON the budget vector is:
  - compute tiles;
  - memtile L2 bytes;
  - DMA channels: memtile 6/direction, shim 2/direction per shim tile;
  - BD ids and locks per tile;
  - shim columns.

  See also `project_objectfifo_join_interleave_limit` and
  `project_mlir_aie_bd_id_free_hazard`.

### 3.4 Partitioning a DAG into array-sized segments

Three solution tiers, in increasing cost:

1. **Greedy with a priority queue** (XLA PriorityFusion). Merge the max-Δ pair,
   re-score its neighbours, and repeat until no positive Δ remains. It is fast
   and incremental, but myopic.
2. **Dynamic programming over a topological order** (Tangram; also classic
   temporal partitioning). Choose segment boundaries along a linearised DAG,
   where a segment's cost is the best configuration for that window: its
   co-resident set, column split and stream-fused edges. It is exact for
   chain-like graphs, and decoder-only LLMs are close to a chain with
   repeating layers.
3. **MILP** (DFModel, Kaul & Vemuri, Korch, stream-dse's allocator). Optimal
   within the model, but slow, and only as good as the model. Best used as an
   offline oracle to check the heuristics on small graphs.

The graph's repetition, identical decoder layers, lets a segment plan for one
layer be reused, which keeps DP/MILP tractable.

---

## 4. Recommendation for IRON

### 4.1 Taxonomy: two orthogonal axes

**Axis 1: operator kind, derived rather than declared.** Adopt the TVM lattice,
refined with DNNFusion's data-movement classes:

| Kind | Examples | Derived from |
|---|---|---|
| `ELEMWISE` (1:1) | add, mul, silu, gelu | every stream's TAP is the same identity-ordered map |
| `BROADCAST` (1:many) | scalar/row broadcast | an input TAP with a stride-0 dimension |
| `LAYOUT` (reorganize/shuffle) | reshape, transpose, strided_copy | no compute kernel; the output TAP is a permutation or reshape of the input |
| `REDUCE` | rmsnorm, softmax row stats | an output TAP smaller than the input along a declared axis |
| `ROOT` (many:many) | GEMM, GEMV, attention | declared contraction; IREE-style anchor |
| `OPAQUE` | anything with runtime-offset streams, or undeclared | fallback |

Derive the kind the way Relax derives `op_pattern` from TIR accesses: from the
TAPs and tile shapes operators already declare. Hand labels drift.

**Axis 2: fusion mechanism, a property of a group, not of an op.**

- **(a) co-reside**: same configuration, disjoint resources, and data still
  goes through DDR.
- **(b) stream**: on-chip edges inside a co-resident group.
- **(c) kernel/epilogue**: one core kernel computes several ops.
- **(d) layout folding** (new; recommended): a `LAYOUT` op disappears into the
  DMA access pattern of its producer or consumer. This is DNNFusion's
  Reorganize/Shuffle and TVM's injective-into-consumer, and it is often free on
  the NPU because the DMAs do up to 4-D addressing. It removes a step
  entirely, so it removes a switch.

The mechanisms nest: (b) implies (a), (c) happens inside one design, and (d)
can apply at any level. This matches AIR's launch ⊇ segment ⊇ herd hierarchy.

### 4.2 Operator metadata the pass needs

Most of this already exists in IRON's stream/buffer/scalar declarations.

1. **Resource footprint.** Columns × rows of compute tiles, memtiles, L1 bytes
   per tile, L2 bytes, DMA channels per direction, BDs/locks, and shim
   columns. Also: can the design be **relocated** to a column offset, and at
   which column counts can it be built? The column count is a knob, as in
   CHARM's allocator.
2. **Per stream:** buffer name, direction, dtype, the L3 TAP, tile shape,
   per-column split, and whether each element is read once (streamable) or
   re-read. The last is XLA's `ReusesOperandElements`.
3. **Per scalar:** whether it changes the *addresses* of a stream (e.g. RoPE
   position or KV-cache offset). If it does, that stream is `OPAQUE` for
   legality of (b) and (d); (a) stays legal.
4. **An epilogue hook for (c).** Does the root kernel accept a fused
   elementwise tail, as ttnn `fused_activation` and AIE4ML's bias+ReLU do? This
   is a kernel-library capability, not something the pass can synthesise from
   C++.
5. **Cost hooks:** estimated t_step at a given column count, or a measured
   table, plus DDR bytes.

### 4.3 Legality, layered by mechanism

- **(a) Co-residence.** Legal if the members' resource vectors fit the array
  simultaneously on disjoint tiles and channels, every member is relocatable to
  its assigned offset, and the combined image builds. **No dependency condition
  is needed**, since members still execute as ordered steps through DDR. If
  independent members are to run *concurrently*, they additionally need no
  path between them, as in XLA sibling MOF and horizontal fusion.
- **(b) Stream edge P→C.** Legal if:
  1. (a) holds for {P, C}.
  2. P's output order and tiling on the edge equal C's input order and tiling
     (Inductor's MemoryDep equality, IREE's affine-map composition). A
     mismatch is allowed only if it can be expressed as a memtile DMA
     transform within the hardware dims limits. Note that ObjectFifo join
     cannot interleave sources (`project_objectfifo_join_interleave_limit`).
  3. C reads each element once, **or** the whole edge tensor fits in the
     buffering the group allots it.
  4. P is not a `REDUCE` or split-K `ROOT` whose output only completes at the
     end, unless condition 3's fit holds.
  5. All consumers of the edge are in the group, **or** P also drains to DDR
     (a multi-output group, which costs a DMA channel; Tangram's "one outside
     consumer" relaxation).
  6. Merging creates no cycle through a node outside the group (XLA and
     Inductor cycle checks).
  7. FIFO depth is enough to avoid deadlock on reconvergent paths, e.g. the
     diamond in SwiGLU's gate/up → mul.
- **(c) Epilogue.** Legal if the consumer is `ELEMWISE` or `BROADCAST`, is the
  single consumer of a `ROOT` output, uses the root's output tiling, the root
  exposes an epilogue hook for it, and L1 fits. At most one `ROOT` per kernel
  (TVM's "cannot chain another complex op"; DNNFusion Many-to-Many × Many-to-Many
  is red). Horizontal root fusion, such as QKV sharing an input (IREE
  `FuseHorizontalContractions`), is a separate, explicitly enabled rewrite.
- **(d) Layout folding.** Legal if the `LAYOUT` op's composed TAP stays within
  DMA addressing limits on the side it folds into, and its scalar parameters do
  not change per call.

Give each rule the DNNFusion three colours: *illegal*, *legal and always
profitable* ((d), and (c) when available), and *legal but needs the cost
model* ((a) and (b)).

### 4.4 Search and staging

1. **Start with (d) and (c).** Both are local rewrites, like TVM phases 0-2,
   and are nearly always profitable because each removes a step.
2. **Then run (a)+(b) as segment formation.** Use a Tangram/temporal-
   partitioning DP over a topological order of the traced graph:
   - A segment's value is the cheapest configuration covering its distinct
     designs: a column split chosen CHARM-style (proportional to cost, then
     locally improved), plus the (b) edges that are legal and profitable.
   - Allow reordering inside the DAG's freedom, since co-residence is what
     makes reordering pay again.
   - Fall back to an XLA-style greedy pass if the DP window gets large.
3. **Treat MILP as an oracle, not the default.** stream-dse is already a
   dependency. Emit `FusedGroup`/`Placement` from the pass, so stream-dse can
   serve as the (b) backend and as a cross-check on small graphs.
4. **Name things to avoid a collision.** Tangram's *segment* is a time slice;
   AIR's *segment* is a spatial region. I suggest *configuration* for the time
   slice and *region* for the spatial part.

### 4.5 Pros and cons of the choices

| Choice | Pros | Cons |
|---|---|---|
| TVM-style kind lattice (hand-labelled) | trivial to implement; proven | coarse; transpose/reshape land in "injective"; labels drift from the design |
| Kinds **derived from TAPs** (recommended) | general; stays in sync with the design; Relax precedent | needs every op to declare accurate TAPs; runtime-offset streams must fall back to opaque |
| Access-map equality for (b) (Inductor/IREE) | precise; catches order and tiling mismatch | rejects fusions a DMA reorder could fix, unless DMA-transform matching is added |
| Always-fuse (TVM) | no model needed | wrong for IRON: shrinking columns can lose more than a switch saves |
| Greedy priority queue (XLA) | incremental, explainable, fast | myopic; misses segment-level optima |
| DP segments (Tangram) | exact on chain-like graphs; fits LLM structure | needs a linear order; windows blow up with many small ops |
| MILP (DFModel, stream-dse) | optimal within the model | slow; an opaque failure mode; the model's quality bounds everything |
| Adding (d) layout folding | removes steps and switches at no compute cost | limited by DMA dims and BD limits, which are easy to get subtly wrong |

### 4.6 What to measure before trusting the model

1. The switch cost between two **different sub-designs of the same
   configuration**, i.e. co-resident regions. This decides whether (a) is worth
   anything.
2. Per-op t_step against column count for the ~19 Llama decode designs. This
   is CHARM's allocation input.
3. Whether reconfiguration can be prefetched or overlapped (Hauck 1998).

---

## 5. Items I could not verify

- Cerebras layer-pipelined vs weight-streaming modes: no primary text fetched.
- Vitis AI DPU/CPU graph partitioning and any fusion cost model.
- Graphcore Poplar's internal automatic fusion, if any. PopART pipelining is
  verified to be user-annotated.
- The AutoMM venue.
- Whether DFModel has a reconfiguration term anywhere I did not read.
- The exact metrics behind SET's 1.78× and MaxEVA's 2.19×.
- Web search was unavailable. Verification used Crossref, arXiv pages,
  Semantic Scholar and the sources themselves; dblp and the ACM DL were
  unreachable.
