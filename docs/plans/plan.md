<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# iron-next: integrated plan (committee review + duplication review)

Sources (not in the repo; untracked in `scratch_review/` on xcoradaie220):
- `committee_report.md`: the R-items, D1–D14 there.
- `dedupe_report.md`: its D-items. Its table IDs are written here as **X** plus the number (X1–X50), so they don't clash with the committee's disagreements D1–D14.

- The tuning-architect's review, `tuning_review.md` (T1–T14, placer Q1–Q8 with the Q8 run, spatial fusion), folded into Wave 2 steps 6–7, the S-track and Wave 3.

**Priority (user, 10-09): spatial fusion.** It is the S-track below, and the waves are re-sequenced around it.

## Status and decisions, 10-10

The plan below is as decided on 10-09. What changed since:

- **Wave 1 has largely landed** (the commits from d3ec5c22 to 0a0774d9 on iron-next, among them the X37 calibration triangle d91e8146 and the refusal of a table whose rows it would drop, 97704ce3). Its items have not been checked off one by one.
- **The stale npu2 tables are gone,** and the Llama npu2 tables are being re-measured on dev22 (see `HANDOFF.md`).
- **Dataflow fusion: yes** (user). It is the S-track: steps streaming into each other on the array, through an L2 memtile or directly core to core, both in the design.
- **Configure work: no** (user). No pack-budget shim sharing, no MHA reload work and no pack growth, although configures are ~9.4 ms of a decode step.
- **Order now:**
  1. Finish the dev22 tables (fused, then `--dispatch separate`), re-tune, interleaved A/B (8 or more rounds) with accuracy, commit them.
  2. Count a fold's streams per core in `Operator._finish_at`, not across the array (EG2's weighted RMSNorm → residual Add). mlir-aie's sequential placer already forces surplus core-to-core peers onto shared-L1 neighbours (`AIEPlacer.cpp`, Phase 2c), so no hand pinning is needed.
  3. A held ride (EG2's layer scale): one fifo whose object is the weight and the scale row, two fills in order per call, the core taking subviews. No mlir-aie primitive is needed (verified in mlir-aie's `scratch_chsh/ride/test_ride.py`).
  4. The dataflow fusion design. Its first step is a null-kernel experiment: two GEMVs' weight streams running concurrently in one design, against DDR peak, to learn whether ~50–57 GB/s is a per-array cap.
  5. An iron-next venv on mlir-aie iron-next, for `Runtime.add_buffer` (the uncommitted edits in the main tree).
- **flm.GEMM finishes stay SiLU only** (user). Its residual and `up` folds stay out.
- **EG2 fold gaps are recorded as a limit** (c9dc5cbd, AGENTS.md); step 2 lifts the first.
- **Estimates given (not measured):** decode 16.5 tok/s tuned today → ~18 with dataflow fusion (the GEMV ramp and tail hidden) → ~21 with the fewer configures that follow; the ceiling is ~25 (2.47 GB of weights at 65 GB/s). For EG2, at most ~12% of a document from the activation round trips. Short queries might gain more, if a fused layer's row-block count can follow the per-call length. That is a hypothesis.
- **Placement:** IRON runs mlir-aie's sequential placer. On 10-07, `--placer=sa_placer` matched MHA's hand placement at 8 pipelines with no pins (about 18 s to place); the sequential placer failed to route it. A GEMM check (unpinned under SA against the shipped "tiles" placement) was offered, not decided.

## Decisions already taken (from the Q&A)

- **Order** (revised for the S-track; see "Sequencing" below):
  1. Wave 1.
  2. S0, the spatial spike, then the S-prerequisites pulled forward from Wave 3.
  3. The kernel and accuracy work of Wave 2 (D9: bfp16 matmul off, accurate exp2, vtanh LUT, f32 scale), measured, alongside S1–S2.
  4. Tuner integrity and speed, then S3 (the tuner prices groups).
  5. One re-tune on the final kernels, measuring packs and groups together.
  6. S4, then the rest of Waves 3 and 4.
- **D14:** GEMM `prio_accuracy` gets a commit of its own.
- **D5:** Awake while measuring. A table is accepted only if R97's extended `check_model`, run without Awake, shows tuned beating untuned.
- **R5/D7:** keyword-only outputs, every caller migrated.
- **R17:** explore first (copy cost, a read-only view, copy-on-next-call), then bring the numbers back.
- **R18/R103/R104:** `graph.on_miss = Miss.COMPILE | Miss.RAISE`.
  - The default is COMPILE; `CausalLM.load()` sets RAISE.
  - A miss logs its reason and compiles with the first compile's options.
- **R43/R106:** coupled fields become derived `auto()`s, domains are re-evaluated at the current point, and an illegal move steps to the nearest legal value.
- **D6:** the no-one-line-helpers rule stays; a shared key policy is a public method on the class that owns the identity.
- **D2:** `DispatchTime` stays separate. Whether `Scratchpad` folds into `Value` is decided after R59.

## Priority track S: spatial fusion

### Why it's the priority

IRON fuses in time today:
- A full ELF and co-residence packs save dispatches and configures, but data between steps still goes through DDR (`coresidence.py:9-10`), and members don't run at the same time.
- Folds merge a step into one kernel.
- The tuner picks settings inside each operator's own `array()`. It never links two operators on chip, and `model_us` adds step times, so it can't price a pipeline.

Spatial pipelines run in IRON only when someone writes them by hand (`flm/layer`) or exports them from Stream (`swiglu_prefill_stream`, via `exported_design`). The repo already shows they pay off:

| SwiGLU prefill (seq 256, emb 512, hidden 2048, npu2) | Median (us) |
|---|---|
| Hand-written graph (IRON's shape today) | 1348 |
| Stream k=5 (one design per layer) | 1399 |
| **Stream k=1 (whole block pipelined on disjoint columns)** | **1165 (0.86x)** |

Expected gains by workload:
- **Prefill and CNN-like work:** large. Activations are big, so the DDR round trips and per-layer configures are the main cost.
- **Llama decode, bf16 weights:** up to about 1.3–1.5x (inferred), capped by the 35–39 ms DDR floor. In decode an activation is 4 KB, so the gain is the step boundaries (configures at 9.4 of 59.8 ms, plus per-step sync), not the traffic. S0 measures that split before we promise a number.
- **FLM's decode lead** is mostly q4 weights, which trade accuracy, so that part stays off the table.

### Link kinds (user, 10-09)

Both are required:
- **L2:** through a memtile, which can reshape, join or split, and buffer.
- **Direct core-to-core (L1 → L1):** one ObjectFifo from the producer's core to the consumer's core. On neighbouring tiles it lowers to shared memory, with no DMA.

Today every operator creates its own fifos in `array()` and binds their shim ends to its lanes (60 bind sites). A memtile link can join two such ends. A direct link cannot: it needs one fifo with the producer core on one end and the consumer core on the other.

**User decision (10-09):** operators can be made fusable through library-owned streams, and operators not built that way (flm, hand-written arrays) stay supported. That gives three tiers, per operand:

| Operand's stream | Links it can take |
|---|---|
| Library-owned fifo | direct L1 → L1, and L2 |
| Bound by hand in `array()` (today's form) | L2 only: an `ObjectFifoLink` at a memtile between the two shim ends |
| Shipped binary (`via=`), `exported_design` | none; it fuses in time only (packs, full ELF), as today |

The tier follows from how an operand's stream is built, not from which family the operator is in. An flm operator whose `array()` can take a library-owned fifo, or bind its shim ends by hand, links like any other. Only its shipped-binary forms (`via=`) can't.

**S-Q1, decided (10-09): ownership is inferred from `array()`.**
- An operand is owned if `array()` takes its fifo from the library (`self.x.fifo(k)`), and hand-bound if `array()` calls `.bind()`. No flag.
- `op.x.owned` reports it after a build, and `verbose=True` lists it.
- The tuner builds members' arrays (in-process Python, no compile) to list candidate links. Candidate links are per setting, since a tunable can change `array()`.
- In a group, the library creates one fifo per direct link and hands the same object to the producer's `Out` lane and the consumer's `In` lane.
- First migration: the shared elementwise array (`elementwise.py:798`), which covers every elementwise operator at once.

**S-Q8, decided (10-09): every operator migrates to library-owned fifos, flm included, unless it would break flm compatibility.**
- Scope: the 17 operator files that bind lanes by hand (GEMM, GEMV, MHA, GQA, RMSNorm, RoPE, Softmax, Copy, Transpose, Sample, Clamp, Merge, Resample, depthwise conv1d, flm's GEMM and dequant), after the elementwise array.
- **Each migration's acceptance:**
  - The unlinked design is unchanged: the generated module is identical before and after, and the core ELFs are byte-identical (`array_identity.py`'s style).
  - The operator's device tests pass on a full ELF and an xclbin.
- **flm compatibility** means its device tests still match FLM's binary and its own accumulator, its weight packing is unchanged, and the design is unchanged.
  - A lane that can't become a fifo without changing the design (flm GEMM's B, bound to a raw `Flow` at `flm/gemm/op.py:841`) stays a `Flow`.
  - `op.streams()` reports it with its typed reason.
  - Shipped binaries (`via=`) are untouched.
- An owned operand whose tiles don't match its neighbour's still links through L2 (S-Q4's rule). The point is uniform ownership, not more L1 edges.
- **When:** the elementwise array in S1, the rest in S2, before S2b. The S-Q3 guard test covers every migrated operator.

**Introspection (user, 10-09):** fusability is inferred, not written down, so the writer of an operator or a graph must be able to ask for it.
- The operator class and the graph class both expose public methods for it.
- The answers name the reason for each refusal (a hand-bound lane, a raw flow, a tile mismatch, a shipped binary), as typed reasons (T4), not strings.
- **S-Q3, decided (10-09): typed records on both classes.**
  - `op.streams() -> tuple[StreamInfo, ...]`: per operand, its lanes, its ownership (`Owned`, `HandBound`, `Flow`, `Shipped`), the link kinds it can take (`L1`, `L2`), and a typed reason when there are none.
  - `graph.links(**shapes) -> tuple[Link, ...]`: per producer→consumer edge (from `trace()`), the kinds both ends allow, or the typed reason why not.
  - `version.groups`: what the tuner or compile chose.
  - `verbose=True` prints the same records.
  - Answers build `array()` at the resolved settings on the bound device (no compile).
  - It lands in S1, with a guard test: the migrated operators stay `Owned`.

**S-Q4, decided (10-09): the rule is the default, and the tuner may flip an edge.**
- The link kind is a tunable of the group. Its default is a rule: L1 when both ends are owned, the tiles match and both L1 budgets (R71's account) fit the depth; otherwise L2.
- The tuner tries the other kind only on edges in groups that carry a meaningful share of the graph's time (T11).
- A profile can pin a link kind.

**S-Q2, decided (10-09): native groups.**
- Stream's SwiGLU stays one operator. Its k=1 (1165 us) is S2's acceptance bar and a reference partition for checking the tuner's choices.
- `STREAM_OPS` is not extended, and Stream's `k` doesn't become a tunable.

**S-Q5, decided (10-09): the tuner forms groups; a pin forces one.**
- The joint search proposes groups from the graph's edges and keeps those that measure faster. An untuned compile forms none, as with packs today, so the default is never slower than now (Stream's k=2, 1452 us against the hand graph's 1348, is why there's no greedy default).
- A profile entry pins a group (and its link kinds); `compile(groups=...)` does the same for tests and experiments. `body()` gets no grouping syntax.
- `graph.links()` says why an edge didn't link, and `version.groups` what was chosen.

**S-Q6, decided (10-09): stages share the array the way pack members do.**
- A group candidate picks one measured variant per member (`_cheapest`, `narrowing.py:965`) within the array's budget. The budget extends from shim channels to cores and memtiles, read from the built `array()`, and a linked lane frees its shim channels.
- Group picks are ranked by the pipeline estimate (slowest stage plus fill and drain) instead of the sum, and T3's floor orders them so balanced splits are measured first. The group itself is then measured (S3).
- The placer decides where the tiles go (Q1). No sub-device view: a stage that must sit on given columns gets a `Placement` pin.

### What already exists to build on

No new MLIR representation is needed. Every piece below is an existing mlir-aie primitive or an IRON mechanism:

- **The on-chip link** is mlir-aie's `ObjectFifoLink(srcs, dsts, tile=AnyMemTile)` (`aie/iron/dataflow/objectfifo.py:1153`). It is one-to-one, or many-to-one/one-to-many with offsets: the same op `forward`, `join` and `split` use.
- **IRON's lanes are already the right ends.** An `In` lane holds its fifo's producer end, the one the shim feeds, and an `Out` lane holds its consumer end (`declare/bound.py:23-57`). Linking producer `Out` lane `i` to consumer `In` lane `j` is `ObjectFifoLink(out.lane(i).handle, in_.lane(j).handle)` at a memtile, with neither operator's `array()` changing.
- **Declared tiles** (`tile=`, `per=`) give the shape check:
  - equal tiles link one-to-one;
  - a lane-count mismatch is `join`/`split` with offsets;
  - anything else is a refusal (`Unresolvable`) until a memtile reshape is built.
- **Co-residence** already merges several arrays into one `aie.device` and asks the placer whether the union fits (`coresidence.fits`). A group is a pack whose members are linked instead of shim-routed, and which run concurrently under one sequence instead of being lock-gated.
- **The graph's edges** (`trace.Binding`, the producer/consumer walk `fold.py` uses) say which lanes can link.
- **The joint search** (the DP over partitions, `narrowing.py:1453-1485`) already partitions a step chain into packs. A group is one more kind of partition cell.
- **`exported_design`** stays as it is. Stream's k=1 SwiGLU becomes the bar the native path has to reach.

### Steps

**S0. Spike and measurement (first device work after Wave 1).**
- Build one group by hand in a scratch test:
  - two single-lane elementwise operators with equal tiles (e.g. SiLU then Tanh);
  - each operator's `array()` into one `Program`;
  - one `ObjectFifoLink` between them;
  - one sequence that fills the head and drains the tail.
- Verify it against the composed numpy reference.
- Answer, with real runs:
  1. Does a link land on a memtile when the consumer's own fifo already forwards through one (GEMM's L3→L2→L1)?
  2. Do trip counts read from `Value`s stay consistent when both stages run at once?
  3. What does a Llama decode layer spend between steps (configure, sync, data)? Trace one layer of the tuned graph.
- The outcome is a go/no-go note with numbers, and the first upstream asks if any primitive is missing.
- **Pre-read, device-free on dev22 (10-09; scratch design `/tmp/s0/design.py`, `fit.sh`):**
  - Pinning works: a `logical_tile` pinned from Python stays put under the sequential placer, and re-emitting SA's placement as pins reproduces it exactly, shims included (answers Q1's "does sequential keep the pins"). Pin `sa-seed`; 0 is non-deterministic.
  - Memtile links work, including a join of a core output and a shim input. A fifo can sit in one `ObjectFifoLink` only: core→mt→mt→core, or one broadcast fifo forwarded per consumer, fails the verifier. Fan out after the link instead.
  - Direct L1 fifos work: neighbouring cores share one pool (2 locks, no DMA) on one tile, so a neighbour link moves L1 budget between the members; distant cores or `via_DMA` get two pools and a flow.
  - RTPs and barriers of two cores don't interact (each a lock/buffer on its own tile). IRON-side hazards: both trip counts from one `Value`, or the dispatch deadlocks until TDR; one sequence writes every member's RTPs and barriers before the first fill; check per-tile lock budgets (inferred).
  - Possible upstream asks: a written guarantee that pins aren't moved; a fifo in two links; a trip-count mismatch check.
- **Lane inventory (10-09):** 24 bind sites, 22 can take a library-built fifo (Copy, Repeat and PatchPositions only via an explicit `ObjectFifoLink`, which prints identical MLIR to `.forward`, checked). A constructor `x.fifo(k, *, name, depth=None, obj_type=None, to_stream=None, shim=None)` returning the `ObjectFifo` itself covers them; names must pass through (`Program` sorts fifos by name). Transpose's x needs `obj_type` (flat tile). flm GEMM's B is a raw `Flow` into a memtile slot pool that `sequence()` reprograms per shape: it stays a `Flow`-kind lane.
- **Gate (decided 10-09):** S0 is a functional go: it builds, verifies, and nothing blocks the three questions. It also reports a mechanism check: the linked pair against the same pair temporally (full ELF, through DDR), at a size well past the dispatch floor. A working link moves two buffers instead of four, so it should take about one operator's time. A large miss is investigated before S1, but it isn't a stop. The "does it pay" gate is S2b's.

**S-prerequisites (pulled forward from Wave 3 or 2).** These are the items the group build would otherwise grow around:
- **R87** (only the part that moves the fold/finish walk out of `Operator`), so the group's lane accounting gets a home of its own instead of growing the 1,449-line class.
- **R66 + R59:** typed `BufferRef`s and the `Packaging` enum, so "this lane is linked" is a typed fact, not a parsed name.
- **R23:** `coresident=` already has three meanings, and a group would add a fourth. Type it first: `Pack` and `Group`.
- **R71** (Wave 2): the L1 account with measured stacks. A stage on fewer columns must know what fits.
- **R57 + placer Q1:** the fit authority. Groups are whole-array packing, exactly where the sequential placer is weakest.

**S1. `Group`, the native build.** A sibling of `build_design` in `design/build.py`:
- `build_group(ops, links, image)`: each member's `build_array(target)` into one `Program`, then the links;
- one `Sequence` over the members that skips linked lanes, then fills inputs and weights and drains outputs;
- refusals as `Unresolvable` (tile mismatch, link count, L1 or placer refusal);
- `OperatorDesign` for a group, keyed on the members' `design_key()`s plus the links;
- device tests on both a full ELF and an xclbin image, verified against the graph's reference.

**S2. Linked shapes.**
- Lane-count mismatch through `join`/`split`.
- A memtile reshape where the tiles differ.
- The remaining operators migrate to owned fifos (S-Q8), each with the unchanged-design check.
- Sharing the array between stages (S-Q6, below): each member's measured variants are its share, picked within the array's budget.
- **Acceptance:** SwiGLU prefill, as a native group, at or below Stream k=1's 1165 us, against the same reference.

**S2b. Pinned groups on a model (decided 10-09).** After S2 and after Wave 2 step 4's accuracy flips, so the numbers stay valid:
- Hand-picked groups, pinned with `compile(groups=...)` (S-Q5), on one prefill layer (the Llama prompt chunk or EG2 text).
- Interleaved against Wave 2's A/B baseline (8 or more rounds) and checked against the oracle.
- Report the measured time against S3's pipeline estimate (slowest stage plus fill and drain), so the estimate is checked before the search is built on it.
- **The gate:** the paired gain's lower bound (T7's rule) must be above zero and past the practical floor. A failure comes back to you with the numbers before S3 is built.

**S3. The tuner prices groups.**
- Groups become candidate partition cells in the joint search, beside packs and folds, proposed from the graph's edges.
- A group is measured as one design, like any other, so the model needs only a pruning estimate (the slowest stage, plus fill and drain), not an exact price.
- Candidates come from `_connected` over linkable edges and the picks within each from `_cheapest` under the array budget (S-Q5, S-Q6). T3's floor orders them, T2's racing drops the losers, and T11's share picks which groups get the link-kind flip (S-Q4).
- The placer rule (Q1, Q4) applies to groups, and the build replays the recorded placement.
- Q2's evidence gate: one A/B of annealed against sequential placement on the groups carrying the most time, reported with the S3 numbers.
- Group residuals (measured against the pipeline estimate) go in T12's gate report.
- This lands before the one re-tune, so that re-tune measures packs and groups together. That keeps "one re-tune".

**S4. Models.**
- **Order (decided 10-09):** the Llama prompt chunk, then EG2's text encoder, then the Llama decode layer. Decode moves to the front if S0's trace shows that time between steps (that packs don't already remove) is a large share of a decode step. Decode's activations are 4 KB and GEMV is at the DMA floor, so its spatial gain is per-step overhead only.
- Each is accepted on R97's unpinned `check_model` from the one re-tune, which includes the temporal-only partition as a candidate, so a group is kept only where it wins.
- Report tok/s, TTFT and the remaining gap to the DDR floor.

### Decisions (S-track and placer), all taken 10-09

- **Placer** (which placer the fit check and build use, and how it's searched). Spatial raises the stakes: groups are where annealing helps most.
  - Measured by the reviewer (CPU only, a ~1,000-run sweep over the Llama decode step and prompt chunk still running):
    - `sa_placer` takes about 1.1–1.3 s per fit check, against about 0.01 s for sequential (2–4-design decode packs), roughly 100x slower.
    - The placer is chosen per image, not per pack. A fused image is one aiecc call, and the members' `aiecc_flags` are merged into it (`fused.py:67-75`), so `--placer=sa_placer` applies to every device in the ELF. A per-pack choice means IRON places those devices itself before aiecc runs (the placement pinned into the IR, so aiecc's sequential pass keeps it; unverified, so it's checked in S0).
  - So Q1 (c) costs about 1 s per refused candidate in the search, and the build must replay the placement, not the flag.
  - **Q1, decided (10-09): (c).** Sequential first. `sa_placer` runs only when sequential refuses, and the verdict records which placer won (a typed field, T4). The annealed placement is pinned into the IR and the build replays it, so the check and the build always agree. S0 adds the question: does aiecc's sequential pass keep those pins? Cached verdicts for packs that fit today stay valid.
  - **Q2/Q3, decided (10-09): Q1's rule, behind an evidence gate.** The placer isn't searched, and `"anneal"` doesn't become an operator `Placement` value (a per-image option would clash inside a pack). S3's A/B measures annealed against sequential once on the groups carrying the most time; if one wins past the noise margin, the placer becomes a group tunable flipped like the link kind (S-Q4).
  - **Q4, decided (10-09): a fixed seed list.** Seed 1 at effort 1.0; on refusal, a fixed list of a few more seeds (3) before the refusal is recorded. The verdict records the winning seed, the build replays the placement (not the seed), and the stage-2 verdict key (T5, T10) holds the seed list.
  - **Q5, decided (10-09): the search stays exact.** `_connected` (`narrowing.py:1414`) enumerates a second family of candidates over linkable edges (`graph.links()`), capped at `max_members` and budgeted by the whole array rather than the shims. Each group candidate is measured, and `_partition` chooses among singles, packs and groups. This covers fan-out (SwiGLU's gate and up meeting at the Mul). Revisit only if S4's whole-layer groups need more than 8 members, with T13's search-time log as the number.
  - **Q6, decided (10-09): refusal kinds from the stage that refused; bindings only on need.** `coresidence.fits` runs `_FIT_PIPELINE` stage by stage and returns a typed refusal. The kind comes from the failing stage: `PLACEMENT`, `MEMORY` (stateful transform, buffer addresses), `DESCRIPTOR` (lock and BD ids), `ROUTING` (pathfinder) or `MERGE`, with its diagnostics attached. This lands with T4 and T5. The annealing placer's per-term cost through the Python bindings is drafted as an upstream ask only if a measured refusal's kind doesn't say what to change. As a pre-filter it would cost ~1.2 s against the ~0.01 s check it filters.
  - **Q7, decided (10-09): the annealing weights stay fixed.** `SAConfig`'s weights (`AIEPlacer.h:501`) stay compile-time defaults. The upstream ask to expose them as pass options is drafted only if annealed groups keep failing on one penalty kind (Q6).
  - Also from the reviewer's run: the 8-design decode window is refused at `merge_devices`, before placement, because GEMV binds `passThroughLine` with its A tile (`gemv.py:421-423`), which follows `tile_size_input` while the digest prefix doesn't cover the bound types. Two GEMVs at different `tile_size_input` declare one symbol at two types. The fix is IRON-only (GEMV binds a type that doesn't follow `tile_size_input`); it goes in Wave 2's legality step with a guard test, and the refusal gets a `MERGE` kind under T4.
- **S-Q7, decided (10-09): the re-tune is held for S3.** One campaign measures packs and groups together. Until then, the temporal baseline S0–S4 compare against is Wave 2's A/Bs, which are measured untuned and tuned on the same graph in the same run. HEAD's shipped npu2 tables load no rows; they are removed in Wave 1 ("Tuner") and re-measured after X37.

## Vetting the upstream asks: feature or incidental?

The test applied to each ask:
- Would an mlir-aie user who has never heard of IRON hit it?
- Does dev22 already offer a way around it?
- Could IRON change shape and stop needing it?

The checks behind each verdict are in the "Evidence" column.

### Keep: real gaps, an mlir-aie user hits them

| Ask | Who else hits it | Evidence (dev22) | Form |
|---|---|---|---|
| **R56.** `aie-expand-load-pdis` alternates two empty PDIs from a fixed start, so a full ELF with an odd number of configure points, dispatched twice, starts its second dispatch on a no-op load. | Anyone dispatching a multi-configure full ELF more than once. | `fusion.py:157-172` documents it and adds a reset device to compensate. IRON also models it in `narrowing.py` and `probe.py` (`reset_us`). | **Bug report**, after an mlir-aie-only repro: three configures, two dispatches. If confirmed, IRON deletes `RESET_DEVICE`, `needs_reset`, the DP parity and `reset_us`. |
| **R4.** The MHA scale is a bf16 argument multiplied in bf16 in the log2 domain. | Every user of `mha_softmax`/`mha` (+0.18% at D=64, +0.32% at D=128). | `linalg.py:1324` rounds `scale` to bf16; `mha.cc:290-405` multiplies bf16 vectors by it. IRON cannot fix this from outside. | **Issue.** The fix can be a two-limb bf16 scale rather than a float32 ABI change; the kernel already works in limbs. |
| **R108.** `silu_sized` has no `use_lut=`. Its siblings `gelu_sized`, `silu`, `gelu` and `swiglu` do. | Any SiLU user on AIE2P who wants the accurate path. | `activation.py:522` against `:543`. IRON's SiLU calls `silu_sized` (`silu.py:46`). | **Small PR** (sibling parity). It blocks the D9 vtanh flip for SiLU. |
| **R35 + R37.** The XRT backend has no `run_chain`, and DispatchTime allocates a new instruction BO and re-checks the device on every call. | Every NPU1 user (XRT only), and every xclbin dispatch with a generated stream. | HRX and HSA have `run_chain`; XRT doesn't. `xrtruntime/hostruntime.py:351-367` allocates an `XrtTransport` per call; `:322` runs `check_device_consistency` per call. **Correction to the plan: R37 is mlir-aie code, not IRON's.** | **Issue**, with a measurement on xcoradaie203 attached (Llama per-step overhead before and after a local patch). |
| **R88a.** `ParameterScratchpad` is not DMA-writable: its BO is on the device heap, where a shim transfer "silently goes nowhere". | Anyone chaining per-call values on device, such as an autoregressive loop feeding a sampled token to the next step. | IRON's `xrt.py:30-74` works around it with a `pyxrt.ext.bo` over the mapping, through `_bo`, `_mv`, `runtime._device` and a ctypes capsule. | **Issue:** a public `alias()` (or a DMA-reachable scratchpad), plus a refusal when a transfer targets the heap BO. It removes three private-name uses. |
| **R62.** No Python access to `verifyStridesWraps`. | Users of `fill/drain(length_parameter=)`. A bounded transfer must fit one descriptor, and today that fails only at aiecc time. | dev22 exposes only per-field bit widths (`device.py:131-144`). IRON restates the rules in `bd.py:16-151`, which can drift per device. | **Issue**, medium. Framed as validation at `fill/drain` construction, with the binding as the mechanism. It deletes ~135 IRON lines. |
| **R64, narrowed.** aiecc failures are a bare `RuntimeError` with the exit code in the text. | Anyone caching or retrying builds, e.g. a DSE loop. | `compile/utils.py:646-657`. `aiecc_diagnostics()` already exists, so a typed error is a few lines. | **Small PR:** `AieccError(RuntimeError)` with `returncode` and `diagnostics`. That unblocks R107: a signal or OSError is never a refusal. The XRT heap `err=-28` string is pyxrt's, not mlir-aie's, so IRON keeps that check. |
| **R76/R110.** No builder for writing BDs with control packets, and no BD-id/channel reservation for them. | Anyone doing data-dependent DMA on device (gather by an index computed on device). | `copy.py:53-300` hard-codes the shim BD register map and writes 16 BDs outside the compiler's accounting. | **Issue**, lowest priority. Until then, the interim refusal in `packaging.plan`. |

### Drop the ask: IRON-shaped, or dev22 already covers it

| Ask | Why it's not an upstream feature | What IRON does instead |
|---|---|---|
| **R7.** Per-sequence reclaim | Reclaim acts only when a tile runs out of BD ids, so the union is a no-op for any sequence that builds without it. No failure has been demonstrated. | Keep the toolchain guard (each operator in a fused image builds standalone without reclaim). If it ever fires, the ask comes back with that repro. |
| **R57.** aiecc's resource stages as a callable | They already exist: `aiecc --get-input-with-addresses` runs only the stages that edge needs (checked with `--emit-dot`). In dev22 that edge depends on the core compiles, because #3903 measures stack from probe ELFs. | IRON's in-process `_FIT_PIPELINE` uses literal and default stacks, not measured ones, so it can disagree with aiecc. Decide, within R57/R71: an approximate in-process check pruning first, then aiecc's edge as the authority before a verdict is persisted. |
| **R58.** Per-design compile plus a cheap link | `CompilableDesign` already passes `--device-cache` (`compilabledesign.py:652`), so a design re-chained after a different predecessor reuses its placement and core ELFs. | Measure one cold and one re-chained build of an NPU1 graph. Ask only if the re-link dominates. |
| **R71.** Stack upper bound in the kernel contract | `Worker(stack_size=None)` (the dev22 default) reserves the measured stack, and `readobj.linked(obj, sym).stack` reads it from a kernel object. Runtime routines are not counted (a known caveat). | Delete the ~25 literal stacks and use the measured ones. The L1 account reads the measured stack, plus a stated allowance for runtime routines. |
| **R61.** `load_pdi=` keyword | It is IRON's own hook (`_iron_full_elf`) inside mlir-aie's `program.py:293`; only a composer of Programs needs it. | Bundle a one-line rename into the hygiene PR with R64, or leave it alone. Not an issue. |
| **R68.** Blocked-layout MHA kernels | A perf idea, unmeasured. | Trace the QK/P memtile round trip's share first. Ask only with a number. |
| **R38.** `run_iters` docstring | A doc fix. | One line in the R64 PR. |
| **X3.** `Tolerance.admitted()` | Only IRON's elementwise chain composition inverts a tolerance. | Keep the 38 lines, and add a drift guard: values at `lo`/`hi` pass `compare`, `nextafter` beyond fails, for every tolerance kind. |
| **X8.** `CompilableDesign.kernel()` | `NPUKernel` is public and takes `num_host_bos`. | IRON passes `num_host_bos=len(op.buffers)` at both sites (`standalone.py:89`, `callable.py:488`). That gains XRT's segfault guard with no upstream change. |
| **X10.** `KernelContract.call_plan()`, **X13.** static params.txt reader, **X16.** public `bf16_floor`, **X28.** upstream `q4nx_decode` | Each serves only IRON's current form, at 4–8 lines each. | Keep IRON's lines. X28 becomes a block-local decode in `flm/q4nx.py`. |
| **X4 (optional).** Upstream test for `full_elf` in the cache key | A test-coverage gap, not a feature. | Offer it only if we're already sending a PR. |

**Net:** the upstream batch goes from 7 issue drafts plus 5 dedupe asks to:
- 6 issues: R56, R4, R35+R37, R88a, R62, R76/R110;
- 2 small PRs: R108, R64 with R38/R61.

That changes your earlier Wave 4 choice:
- R7 is dropped (the guard test stays);
- R64 is narrowed;
- R56 and R108 are added.

## Wave 1: device-free correctness and cuts

Committee items as planned:
- **Verification:** R12, R2 and R47's re-key.
- **Call contract:** R5's interim guard, R96/R27, R10, R9/R109, R103, R33 with R18's device scoping, and R19's keyword-only `dev`.
- **Llama:** R1.
- **Build identity:** R6, R65, R26, R8 and R99.
- **Tuner:** a minimal R53, R43 and R98.
  - **The shipped Llama table is empty in effect (found 10-09).**
    - HEAD's `costs_npu2.json` has 441 step rows, last written in 8e7862f2. Its descendant 3a38c8f0 made `StepCost.noise_us` required, and the rows lack it, so `CostTable.__init__` drops all 441 without a word: it loads with 0 steps.
    - T10's loud row drop (a logged count, or a refusal for a shipped table) moves here from Wave 2, with a test that loads every shipped table and asserts no row is dropped.
    - Traced (10-09, device-free): a tuned Llama compile on it is identical to an untuned one (0 folds, 0/17 designs moved, no packs); only the `[Tuning]` report shows it. Restoring `noise_us` is not enough: the rows lack `beside`/`pair_us`, the search raises on an unresolvable load, and only 10/17 decode designs have a row under the current keys. `costs_npu2_separate.json` is the same. Any tuned npu2 run after the 10-08 merge was untuned.
    - **Decided (10-09): remove, re-measure later.** Delete both stale tables, fix the Llama README's description of them, make `CostTable` refuse a table whose rows it would drop, and add a test that every shipped table loads every row. Re-measure `costs_npu2.json` after X37 lands and the Wave 1 device tests are through.
    - The working-tree rewrite (saved as `scratch_review/costs_npu2.wip.json`, 341 rows with `noise_us`) loads, but 338 of its steps have no resolvable load: Copy and the others were measured neither beside another design nor in a calibration pair.
- **Runtime:** R36, plus R39/R95/R102.
- **Small fixes:** R13, R14, R15.
- **Hygiene:** R34, R77, R84, R85, R89, R90 and R100's comment.

From the duplication review, landing beside the committee item each overlaps:
- **X37, the calibration triangle (bug).** First, before any EG2 tune. Includes a device-free test showing two pairs leave entries undetermined.
- **X19 + X49:** drop `tests/common/cases.py`, add `Case(lower=True)`, and add the f32-out GEMM to `Testing`.
- **X48, X50:** dead code. X50 removes the latent CSV clobber.
- **With R2:** X9 (Verdict's figures; keep `FALLBACK_TOLERANCE`) and X17 (only the None check goes).
- **With R12:** X11 (`ExternalFunction.expected`) and X32 (`harness.judge`).
- **The X3 drift-guard test** (see above).
- **X8 as an IRON fix:** `num_host_bos` at both `NPUKernel` sites.
- **Device-free swaps:**
  - X15 (`bfp.BLOCK`);
  - X14 (`NPUKernel.__call__`);
  - X12 (`limbs_f32_split`);
  - X4 (drop the re-tests; keep contract tests 2 and 5);
  - X7 (`compile_mlir_module`; keep the `_instances` clear).
- **Device-free internal items:** X29, X33, X43, X45, X46, X47 and X41.
- **Fixtures:**
  - X24 (one device-bind factory);
  - X26 (`supported_devices` marker; it stops opening the runtime at collection);
  - X38;
  - X20 (one npu2 run).
- **AGENTS.md:** drop `ExternalFunction(..., digest_prefix=True)`; the factories prefix inside `_make_extern`.

Deferred into the structural item they belong to: X34 and X44 into R66, X36 into R60, X25 into R87.

## Wave 2: device, accuracy and kernels, then one re-tune

Everything that changes a kernel or an array lands **before** the re-tune, so the tables are measured on the final code.

1. **IRON kernels → dev22 factories** (each with device tests):
   - **X2** (Log, Limbs, Magnitude): run the catalog `-k 'Log or Limbs or Magnitude'` and the EG2 audio test. The tolerances tighten.
   - **X1** (Merge, Resample, Resize, PatchPositions). Watch for:
     - resize's `counts` going from (8,) to (5,);
     - the ResampleTaps L1 fit (+4 KB);
     - Merge's `vision_at=2560`;
     - the resize pragma build;
     - keeping `resample/reference.py`.
   - With these, IRON hosts no kernels again.
2. **X18, the shared core-read helper, then X22** (delete `Clamp.array`). Test each touched operator on both a full ELF and an xclbin image, because the barrier re-arm that Merge and Resample lack changes behaviour. It also lands before the D2 decision (Scratchpad into Value), since it is the code that decision would reshape.
3. **R71, revised:**
   - measured stacks (`stack_size=None`), with literal stacks deleted;
   - one L1 account reading the measured stack;
   - GEMM's missing check;
   - R110's interim refusal.
4. **The accuracy flips (D9), each measured, in separate commits:**
   - R100: bfp16 off, with the TTFT/tok/s cost and the watchdog margin reported; `prefill_chunk` shrinks only if needed.
   - R3: accurate exp2.
   - R108: vtanh LUT. GELU now; SiLU when `silu_sized(use_lut=)` lands upstream (a small PR).
   - D14's GEMM `prio_accuracy` (its own commit).
   - R4 waits on upstream.
   - Then retighten `MAX_KL`/`DEEP_KL`.
5. **Oracles:** R93, R80, R81.
6. **Legality typing** (R48, R16, R106, R22, R57, R107, with T4 and T5 and the placer decisions):
   - **T4:**
     - `Unresolvable` gets a `kind`: `MEMORY`, `DESCRIPTOR`, `SHIMS`, `DIVISIBILITY`, `PLACEMENT`, plus Q6's `ROUTING` and `MERGE`.
     - `variants()` enumerates in dependency order, evaluating each domain at the partial point (R106's per-point domains), and returns the refusals counted by kind.
     - Nearest legal follows each domain's own order: index on `Divisors`, log2 on `Width`, declared order for `Choices` and `Placement`, ties toward the resolved value.
     - No CP or SAT solver: the spaces are about 10^3 points.
   - **T5:**
     - Closed-form checks move to stage 1: per-core L1 from R71's account, and `BdLimits.fits`. MHA's "must fit one buffer descriptor" refusals are the first.
     - `fits` runs stage by stage (Q6).
     - Stage-2 verdicts are cached under T10's key; stage-3 verdicts only for a classified failure (R107).
     - A stage-2 refusal of something stage 1 admitted is logged as a missing declared constraint.
   - **R57 with placer Q1 and Q4:** sequential first, then annealing on refusal over a fixed seed list. The placement is pinned into the IR, and the build replays it.
   - **The GEMV `passThroughLine` merge fix** (see placer Q1, below), with a guard test packing two GEMVs at different `tile_size_input`.
7. **Tuner integrity and speed** (R45, R44, R49, R50, R51, R97, R11, X40, X42 and T1–T14). Each item carries its T14 tests. This all lands before S3, since the re-tune waits for it (S-Q7):
   - **R86 + T6 first, pulled forward from Wave 3.**
     - The tuner moves out of `graph/` into one module per concern: `space`, `legality`, `measure`, `stats`, `records`, `model`, `search`, `joint`, `campaign`.
     - Separate commits in the same PR.
     - Every item below then touches one module.
   - **T10 with R45, R46, R47:**
     - A `KeyContext` (device and columns, power mode, firmware and driver, mlir-aie and Peano versions, the kernel-source digest) and a hand-bumped `SCHEMA` integer in place of `SEARCH_DIGEST`'s file hash.
     - The context goes into the `CostCache`, fit, tuning and judged keys.
     - A table header (schema, context, commit, `Timing`, Awake) and a per-row artifact digest.
     - Loud row drops, and an atomic save through `_write`. X29 and X43 are already in.
   - **T1:**
     - Each round's calls are sized by time (`Timing.round_s`, the rule `measure_points` already uses), fixed across rounds so the pairing holds.
     - Repeats are set per design from the default's warm figures.
     - Rounds stay at 8.
   - **T7 with R44, R50, R51:**
     - Paired per-round differences under a Student-t quantile at n−1, or Wilcoxon or bootstrap for bimodal rounds.
     - A practical-significance floor: `max(1 us, 0.5% of t_step)`.
     - Randomized order within a round.
     - A confirmation run that re-times the chosen setting against the default and becomes the row's price.
   - **T12 = R97 (D5):** `check_model` becomes the gate.
     - Paired rounds (at least 8), in randomized order, unpinned.
     - Tuned output bit-equal to untuned, or passing the same judge gates.
     - The verdict goes in the table header.
     - `iron.lm.tune.main` calls it and refuses to write the table on a fail.
   - **R49 and T11:**
     - Measurement goes where the graph's time is: designs ordered by `share − count × floor`.
     - A design below the version's dispatch noise keeps its default, logged as "not worth tuning".
     - Pack residuals (measured against modelled) go in the gate's report.
   - **T3, then T2:**
     - `Operator.floor_us(dev)` (DDR, per-channel shim and compute peaks, calibrated per device) orders and prunes, and never prices.
     - Then racing: a setting drops once its paired lower bound against the incumbent is above zero, with 1.5x kept as a first cut.
     - No Bayesian optimisation or learned cost model.
   - **T13:**
     - Batch k+1 builds in a bounded process pool (memory-capped with `ulimit -v`) while batch k is timed.
     - One NPU job at a time.
     - `build_s` and `time_s` are logged per batch.
   - **T8 and T9:**
     - First trace why HEAD's table has no `points` rows.
     - Bounded designs are measured at the smallest and largest context and fitted to `a + b · ceil(c / block)`, with a middle-point residual check that falls back to the ladder.
     - `max_seq_len` becomes `param(probe=)`, so one cost key serves every context, proved by a cost-identity test.
     - A design's search is seeded with the nearest measured design's top settings.
   - **R11, X40 and X42**, as planned.
   - **T14, the tests that come with the above:**
     - the T2 and T7 rules as pure functions on recorded `round_us`;
     - a trace replay showing racing plus floor ordering picks the exhaustive winner while measuring less;
     - `_partition` against brute force on small graphs;
     - one real failing shape per `Unresolvable.kind`;
     - a per-catalog drift test (stage 1 admits nothing stage 2 refuses);
     - nearest-legal reachability;
     - a device gate test;
     - a `KeyContext` bump that misses every store.
8. **Measurement fidelity:**
   - R38/R105, with X5 (`run_iters` in the EG2 tests) and X6 (`power_mode()`/`device_name()`; the CostCache slug may move once).
9. **X21, the A/B:** weighted RMSNorm on one core against two, interleaved, at least 8 rounds, at Llama decode and prefill. Adopt it only at parity.
10. **The re-tune, after S3:** Llama and EG2 text, vision and audio, Awake on, with packs and groups measured together. Accepted on R97's unpinned check.
11. **EG2 model cleanups,** confirmed by the EG2 device tests: X23, X35, X31, X39, X30 and X27/X28.

## Wave 3: typed vocabulary and structure

The committee items as planned, with the X-items inside. **R59, R66 (with X34 and X44), R23 and R87's fold-walk move are pulled forward as S-prerequisites, and R86 into Wave 2 step 7 with T6.** What stays here:
- R19 `packaging=` and R91, on R59; the rest of R87 (underscoring internals, listing the author hooks by tier).
- **R17** (after the exploration numbers), R18/R104 with `on_miss`, R20, R21, R25, R29, and R5's keyword-only outputs.
- X25 (with the rest of R87), R88b (public `PlaceWord`, `ExtentWord` and the value type), R63, R60 (with X36), R61 locally, R55, R54, R24 and R94.
- **D2:** decide on folding `Scratchpad` into `Value` after R59 and X18.

## Wave 4: features and upstream

- **IRON only:**
  - R67 (MHA live-band streaming);
  - R69 (bounded GEMM movement, on R59);
  - R78 (stop tokens, chat template);
  - R82 (Config beyond Llama, with R4's D=128 pre-scale);
  - R40, R41, R42, R72, R73, R74, R75, R79, R83, R31, R32, R52 and R30.
- **Upstream (vetted above):**
  - Issue drafts to `$ESHARE/issues-to-file/`: R56 (after its repro), R4, R35+R37 (after the xcoradaie203 measurement), R88a, R62, R76/R110.
  - Small PRs: R108; R64 with R38 and R61.
  - Each lands in IRON with the pin bump that carries it: R56's deletions, R35's `StepCallable` submit, R88a's capsule removal, R62's `bd.py` deletion.
- **Measure, then decide whether to ask:** R58 (the re-chain cost) and R68 (the round-trip share).

## Sequencing, with the S-track first

There is one NPU, so device work runs one job at a time. Where an S-step and a Wave 2 step both need the device, the S-step goes first.

| # | Work | Device? | Why here |
|---|---|---|---|
| 1 | Wave 1 | no | Bugs and cuts that every later step reads; the X37 calibration fix in particular. |
| 2 | **S0** spike + decode-layer trace | yes | Go/no-go with numbers before anything is reshaped for it. |
| 3 | S-prerequisites: R87 fold-walk move, R59 + R66, R23 | no | The group build lands on typed ground instead of growing the god class. |
| 4 | Wave 2 steps 1–3: kernels → factories, X18/X22, R71's L1 account | yes | Shared prerequisites: final kernels, and the L1 account stages need. |
| 5 | **S1** `Group` build, then **S2** linked shapes; SwiGLU vs Stream k=1 | yes | The feature itself. |
| 6 | Wave 2 step 4: the D9 accuracy flips, measured | yes | Kernels final before any tuning. Interleaved with 5 on the device. |
| 6b | **S2b** pinned groups on one prefill layer | yes | The first model-level spatial number, and a check on S3's estimate. |
| 7 | Wave 2 steps 5–8: oracles, legality (T4, T5, R57 + placer Q1/Q4/Q6, the GEMV merge fix), tuner integrity and speed (R86 + T6 first, then T10, T1, T7, T12, T11, T3/T2, T13, T8/T9, with T14's tests), measurement fidelity | mixed | A faster tuner matters more now: groups add candidates. |
| 8 | **S3** the tuner prices groups | yes | Before the one re-tune. |
| 9 | Wave 2 steps 9–11: X21 A/B, **the one re-tune** (packs + groups), EG2 cleanups | yes | |
| 10 | **S4** Llama decode/prefill, EG2 text | yes | The payoff, against the step-9 tables. |
| 11 | The rest of Wave 3, then Wave 4 | mixed | |

## Size

- **Firm cuts:**
  - duplication: ~1,550 lines usable today;
  - committee consolidations: ~1–1.5k;
  - upstream-gated: R62's ~135 and R56's parity code.
- **In all,** roughly 2.7–3.2k lines (~5–6% of `iron/`), with every feature kept.
- **X21 is conditional:** +55 if the A/B allows it.
- **The S-track adds code.** S0 sizes it; I won't guess before then. The cuts above are net of everything else.
