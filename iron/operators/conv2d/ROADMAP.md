<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# AIEConv2d — Future Work Roadmap & Measurement Plan

**Operator:** `iron/operators/conv2d` (`AIEConv2d`)  
**PR context:** [amd/IRON#147](https://github.com/amd/IRON/pull/147)  
**Audience:** authors, reviewers, and anyone planning follow-on work  
**Rule:** this document is the home for open work and measurement plans. Do **not** re-inject phase/DONE/OPEN diaries into source comments (see code-commenting skill).

---

## Critical framing

| Claim | Status |
|-------|--------|
| Merge-response complete for explicit review asks (examples comparison, placers, `dev.cols`, comment cleanup) | Largely **done** on branch / PR |
| Product-complete general bf16 conv | **Not done** |
| Performance-complete vs hand-tuned kernels | **Not done** |
| Benchmark-complete (ranking vs peers or examples) | **Not done** |

This PR is a **general bf16 IRON operator**. It is **complementary** to the mlir-aie programming examples:

- [mlir-aie `conv2d`](https://github.com/Xilinx/mlir-aie/tree/main/programming_examples/ml/conv2d) — int8 **1×1**, blocked layout, optional fused ReLU  
- [mlir-aie `conv2d_14x14`](https://github.com/Xilinx/mlir-aie/tree/main/programming_examples/ml/conv2d_14x14) — fixed **14×14 / stride 14** tokenizer-style block (uint8/int8)

Do **not** claim higher performance than those examples without a fair harness and numbers.

---

## 0. What we have today (honest)

| Area | Status |
|------|--------|
| General bf16 `AIEConv2d` (k / stride / pad / groups / depthwise / pointwise) | Implemented |
| Multi-col OC or channel split; L1 OC / H-strip tiling; host bias | Implemented |
| Construct-time L1 / column checks (`AIEOperatorConstraintError`) | Implemented |
| Local correctness matrix (pytest; extensive reported green) | Correctness only |
| Review response on PR (differentiation, placers, cols, comments) | Done |
| **Real benchmarks / ranking vs peers or examples** | **Missing** |
| Kernel class vs mlir-aie int8 / `aie::mmul` density | **MVP / weak** |

### Metrics wired today

Same IRON smoke pattern as axpy / gemm / relu, plus a conv2d Ring 1 harness:

- Pytest `@metrics` (smoke `test_conv2d`) → **Latency (µs)** + **Effective Bandwidth (GB/s)**  
  from `run_test` **mean** of `result.npu_time`
- Frozen suite + multi-iter **median / p99 / GFLOPS / arithmetic intensity**:  
  `iron/operators/conv2d/benchmark.py`  
  exercised by extensive `test_conv2d_benchmark_shapes`  
  - Warmup default 5, timed default 20  
  - Optional real CSV: env `IRON_CONV2D_BENCH_CSV=/path/to.csv` (append; no fabricated rows)  
  - Optional Ring 4 torch CPU wall-clock: `IRON_CONV2D_BENCH_CPU=1`  
  - Peer / mlir-aie protocol constants: `PEER_BW_REFERENCES`, `MLIR_AIE_COMPARISON_PROTOCOL`

| Metric | Good for | Bad for |
|--------|----------|---------|
| Latency (µs) | Same-op regression | Cross-op ranking |
| Effective BW (GB/s) | Rough data-movement intensity | Compute efficiency / vs GEMM |
| GFLOPS (bench path) | Conv compute rate on frozen shapes | Fair race vs int8 examples / GEMM |
| Correctness pass rate | Functional readiness | Performance |

**Still missing:** captured baseline CSV on NPU1/NPU2, peer comparison tables, mlir-aie head-to-head with disclaimers.

---

## 1. Full future-work roadmap

### Track A — Merge / review hygiene

- [x] Differentiation vs mlir-aie `conv2d` + `conv2d_14x14` posted on PR  
- [x] Drop `aie.iron.placers` / use `Program(...).resolve_program()`  
- [x] Column cap from device model (`dev.cols`)  
- [x] Comment cleanup (current constraints only; no phase/DONE–OPEN diary)  
- [x] Inline review threads replied and marked resolved  
- [ ] Remote CI fully green on maintainer runners (re-run / fork approval as needed)  
- [x] Full design review + nits after high-level read  
  (high-level pass done; review threads answered; placers/cols/comments fixed;
  depthwise float-accum parity aie2/aie2p; verbose diary comments kept out of source.
  Remaining product gaps live in Tracks B–F, not merge-hygiene nits.)  
- [x] Keep PR body scope honest (complementary; no unearned perf claims)

---

### Track B — Design / product completeness

- [ ] **On-device packed bias** (`weights‖bias`, `apply_bias=1`) under ≤2 input DMAs (today: **host-only** bias)  
- [ ] **Dilation > 1** (currently hard-rejected; only `dilation=(1,1)`)  
- [ ] **OC × spatial** joint tiling without illegal mid-BD stride-0 rebroadcast  
- [ ] **Depthwise spatial** H-strip when maps do not fit channel tiling alone  
- [ ] **W-strip / 2D tiles** (not only H-strip)  
- [ ] **Multi-col for grouped non-depthwise** (today forced to 1 column)  
- [ ] **Batch N>1 inside MLIR** (today often Python loop over N=1 design)  
- [ ] Expand **extensive multi-col** matrix (4c / 8c where legal)  
- [ ] **Tolerance audit** (HW tols are relatively loose for bf16; tighten if kernels improve)  
- [ ] Clearer construct-time / user docs for supported vs CE-rejected shapes  
- [ ] Optional: fused activation after conv (examples have fuse_relu on int8 1×1)

---

### Track C — Kernel quality

Largest technical gap vs “already well-tested and performant” examples.

- [ ] True **vector / `aie::mmul`-class** bf16 paths (today: largely nested loops + light vector naming; float accum for accuracy)  
- [ ] **Layout strategy** for contiguous vector loads (memtile reshape / blocked channels if needed)  
- [ ] Specialize microkernels: pointwise, depthwise, k3, general k  
- [x] **AIE trace markers** `event0` / `event1` present on aie2/aie2p entry points (cycle extraction tooling still open)  
- [x] aie2 vs aie2p **accuracy policy parity** for depthwise float accum (vector density still diverges; true quality parity open)  
- [ ] aie2 vs aie2p **performance / vector-density parity** (not just both compile)  
- [ ] Permanent product decision: host bias OK for MVP vs packed on-device for latency

---

### Track D — Measurement and benchmarks

First-class track; Ring 1 harness landed (`benchmark.py`); ranking vs peers still open.

- [x] Document current Latency / Effective-BW semantics (this file; keep out of code diaries)  
- [x] Define **frozen `BENCHMARK_SHAPES`** (see §2.3; `iron/operators/conv2d/benchmark.py`)  
- [x] Multi-iter **warmup + median / p50 / p99** (bench path; smoke `@metrics` still mean)  
- [x] Report **GFLOPS** (and optional arithmetic intensity) — GFLOPS + AI (FLOP/byte) on bench path  
- [x] Capture **baseline CSV** on **NPU2** (B1–B6 suite; see `baselines/npu2_20260808_abc7224.csv`)  
- [ ] Capture **baseline CSV** on **NPU1** when Phoenix-class hardware is available  
- [ ] **Regression tracking** in CI (same channel as other ops’ metric trends)  
- [x] **Peer comparison fairness scaffold** (`PEER_BW_REFERENCES` in `benchmark.py`; §2.4 Ring 2 rules)  
- [ ] Live **peer comparison runners/tables** (maxpool/elementwise/GEMM BW on aligned shapes)  
- [x] **mlir-aie comparison protocol** with hard disclaimers (different problem) — `MLIR_AIE_COMPARISON_PROTOCOL` in `benchmark.py` + §2.4  
- [ ] Captured mlir-aie side-table rows on a real machine (protocol ready; no fabricated rows)  
- [x] Optional: **torch CPU bf16** wall-clock on the same shapes (sanity only) — `run_shape_on_torch_cpu`; NPU bench opt-in via `IRON_CONV2D_BENCH_CPU=1`  
- [x] Document what Effective BW does **and does not** mean

---

### Track E — Complementary specialized ops (separate PRs)

- [ ] Port / wrap mlir-aie **int8 1×1** (+ optional fused ReLU) as a separate IRON op  
- [ ] Port / wrap **14×14 stride-14** tokenizer path (aie2p, fixed shape) as a separate op  
- [ ] Do **not** force those product lines into the general bf16 `AIEConv2d` API

---

### Track F — Integration / productization

- [ ] `OperatorSequence` smoke (e.g. conv → activation → later GEMM-style chain)  
- [ ] Real **application** path if IRON apps need vision / tokenizer-style layers  
- [ ] User-facing docs: constraints, host bias, shape / column rules  
- [ ] Optional quant / int8 product path later if required

---

### Track G — Explicit non-goals

- [ ] Do **not** claim faster than mlir-aie examples without a fair harness and numbers  
- [ ] Do **not** re-insert roadmaps into `design.py` / `op.py` / test module comments  
- [ ] Do **not** treat local extensive green as a performance endorsement  
- [ ] Do **not** compare Effective BW of conv vs elementwise as “who is better at compute”

---

## 2. Measurement plan

### 2.1 Current harness (code facts)

```text
run_test(operator, ...)
  → compile + get_callable
  → warmup_iters × op_func
  → timed_iters × op_func; accumulate result.npu_time
  → latency_us = mean(npu_time_ns) / 1e3
  → bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9

test_conv2d prints:
  Latency (us): ...
  Effective Bandwidth: ... GB/s
  → captured by @metrics regexes for CI CSV / trends
```

### 2.2 Metrics to add before ranking anything

| Metric | Formula / method | Why |
|--------|------------------|-----|
| **NPU latency** | Existing `npu_time`; multi-iter **median** | Primary timer for this design |
| **Effective BW** | Existing; document BO set included | Memory proxy only |
| **GFLOPS** | \(2 \cdot N \cdot C_{out} \cdot O_H \cdot O_W \cdot (C_{in}/G) \cdot K_H \cdot K_W / t\) | Conv compute rate |
| **Arithmetic intensity** | FLOPs / host-visible BO bytes (`estimate_arg_bytes`) | Roofline position (same-op only) |
| **End-to-end host wall** | Optional wall clock around full call | Includes BO sync / host bias |
| **Torch CPU median** | `run_shape_on_torch_cpu` perf_counter on F.conv2d bf16 | Ring 4 sanity only |
| **Core cycles** | AIE trace `event0` / `event1` | Kernel vs DMA-bound truth |

### 2.3 Frozen shape suite (proposed)

Keep a **small fixed set** so trends mean something. Fill actual numbers when first baseline is run.

| ID | Kind | Suggested shape (illustrative) | Columns | Why |
|----|------|----------------------------------|---------|-----|
| B1 | Pointwise | 32→64, 32×32, k1, bias on/off | 1, 2, 4 | Common 1×1 bf16 |
| B2 | Standard k3 | 16→16, 32×32, k3 s1 p1 | 1, 2 | General conv |
| B3 | Strided | 16→16, 64×64, k3 s2 | 1 | H-strip / pad path |
| B4 | Depthwise | C=32, 32×32, k3 | 1, 2 | Channel split |
| B5 | Fat pointwise | 32→64, 64×64 | 1–device max | L1 / multi-col stress |
| B6 | Grouped | g=2, 4→8, 32×32 k3 | 1 | Groups path |

**Run protocol:**

- Devices: NPU1 (Phoenix-class) and NPU2 (Strix/Krackan-class) when available  
- Warmup ≥ 5; timed ≥ 20  
- Report: median latency (µs), GFLOPS, Effective BW (GB/s), pass/fail correctness  
- Output: versioned CSV (commit, device, shape id, cols, metrics)

### 2.4 Comparison rings (fairness rules)

#### Ring 1 — Self / regression (do first)

- Same shapes, same device, track over commits  
- Answers: “did this change help or hurt **this** op?”

#### Ring 2 — IRON peer ops (only partially fair)

| Peer | Compare how? | Do not claim |
|------|----------------|--------------|
| maxpool / avgpool / conv3d (if present) | Same spatial-size family; latency & BW | Same FLOPs (different work) |
| elementwise / relu / mem_copy | **BW ceiling** reference | That conv “should match” them |
| GEMM | Roofline / “are we compute-bound?” only | Direct latency race |
| transpose | Memory-bound reference | Same algorithm |

#### Ring 3 — mlir-aie examples (different product)

| Example | Can measure | Cannot claim |
|---------|-------------|--------------|
| int8 1×1 | Their harness wall-clock on **their** layout/dtype | Fair “faster/slower” vs bf16 NCHW `AIEConv2d` |
| 14×14 | Their README-class numbers (~20 ms → ~5 ms) + re-run | Same as general NCHW bf16 conv |

**Fair rule:** only rank after same dtype, layout, problem shape, and measurement surface — or label as **qualitative / different problem**.

**Protocol (code + process):** `MLIR_AIE_COMPARISON_PROTOCOL` in `benchmark.py` freezes:

1. Example identity columns: name, dtype, layout, problem shape, measurement surface  
2. Procedure: build/run each example with **its** harness on the same machine; record times with the required columns  
3. Hard disclaimers: different product; no single ranked leaderboard vs B1–B6  
4. Output: qualitative side table only — never invent cross-op rankings

#### Ring 4 — Torch CPU bf16 (sanity)

- Same logical shapes via `run_shape_on_torch_cpu` / `IRON_CONV2D_BENCH_CPU=1`  
- Shows NPU win/loss vs host wall-clock; **not** an NPU peer-quality ranking  
- CSV field `cpu_latency_median_us` when CPU path is enabled

### 2.5 Measurement work order

1. ~~Keep this document as the semantics source for Latency / BW.~~  
2. ~~Freeze B1–B6 + runner (`benchmark.py` + extensive pytest).~~  
3. ~~Add **GFLOPS** next to Latency / BW for those IDs only.~~  
4. ~~Capture baseline CSV on one NPU2~~ (`baselines/npu2_20260808_abc7224.csv`; NPU1 still open)  
   (`IRON_CONV2D_BENCH_CSV=... IRON_CONV2D_BENCH_CPU=1 pytest iron/operators/conv2d/test.py -k benchmark_shapes`).  
5. ~~Peer ring scaffold + AI + Ring 4 CPU wall-clock helpers.~~ Live peer runners optional.  
6. Optional: run mlir-aie examples on the same machine using §2.4 protocol; **no ranking claim**.  
7. Wire CI trends for B1/B2 regular cases (like other operators).  
8. Only **after** kernel work (Track C): re-baseline and publish before/after GFLOPS.

---

## 3. Priority order

| Priority | Track | Why |
|----------|--------|-----|
| **P0** | A leftovers (CI green, reviewer nits) | Unblocks merge conversation |
| **P1** | **D measurement** (freeze shapes + GFLOPS + baseline CSV) | Cannot improve or defend perf without it |
| **P2** | C kernel quality (guided by D numbers) | Biggest real gap vs “performant” |
| **P3** | B remaining tiling / bias / dilation | Capability surface |
| **P4** | E specialized int8 / 14×14 ports | Complementary product |
| **P5** | F sequences / apps | Consumption |

---

## 4. Differentiation summary (for measurement readers)

| Dimension | mlir-aie examples | This PR (`AIEConv2d`) |
|-----------|-------------------|------------------------|
| Role | Specialized int8 demos / tokenizer block | General bf16 IRON operator |
| Dtype / layout | int8 or uint8/int8; blocked / DMA-packed | bfloat16 NCHW |
| Shapes | 1×1 only, or fixed 14×14 stride-14 | Configurable k / stride / pad / groups |
| Parallelism | 1-core or full 32-core (14×14) | Multi-col OC / channel split (≤2 input DMAs/core) |
| Bias / fuse | Optional fused ReLU (1×1); quant scales | Host-side bias; no fused ReLU |
| Integration | Makefile / lit programming examples | `MLIROperator`, torch `forward`, pytest |

**Merge justification for this PR is use-case + IRON packaging, not measured superiority.**

---

## 5. One-line truth

- **Roadmap:** large — design gaps, **kernel quality**, baseline capture, optional specialized int8 wraps, integration.  
- **Benchmarks today:** Ring 1 harness (B1–B6, median/p99, GFLOPS, AI) + NPU2 baseline CSV + Ring 4 CPU helper + peer/mlir-aie **protocol**; **no** ranking vs examples yet; NPU1 baseline still open.  
- **How to measure vs others:** **tiered rings** + GFLOPS + frozen shapes; never a single “is conv better than gemm / examples?” number without fairness rules.

---

## 6. Document maintenance

| Item | Policy |
|------|--------|
| Where open work lives | This file, PR description, GitHub issues |
| Where open work must **not** live | Source comments, phase/DONE/OPEN banners |
| When to update | After merge decisions, after first baseline CSV, after major kernel work |
| License | Apache-2.0 (same as IRON) |
