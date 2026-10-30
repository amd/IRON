<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.ProjectionGEMM` — bf16 GEMM with a fused epilogue

Ported from the `mm` overlay of [FastFlowLM](https://github.com/ROCm/FastFlowLM)'s Gemma 4 engine.

```python
from iron.operators.flm import ProjectionGEMM

op = ProjectionGEMM(M=1024, K=1536, N=6144, epilogue="silu")
op(A, op.pack_b(B), C_out)  # compiles once, then runs
```

The epilogue applies the activation that follows the product, a SiLU, a
Sigmoid or the port's own gelu, FastFlowLM's `x * sigmoid(1.702x)`, from its
runtime parameters. `epilogue`, `rounding` and `gelu` are `StrEnum`s, so the
bare strings `"gelu"` / `"conv_even"` / `"bf16_steps"` are accepted too.

This is the GEMM `F.linear` runs for any input of more than one row. It reads
the checkpoint's weight as stored, `(N, K)`, with `b_col_maj=True`; a
dequantized weight comes as bfp16 B packed once by `pack_b`. It was ported from
FastFlowLM's `mm` overlay. [`iron.operators.GEMM`](../../gemm.py) is the GEMM of
`F.linear(..., precision=Precision.HIGHEST)` and of integer types.

**M, K, N and the activation are runtime parameters**, so one xclbin serves
every shape and only the instruction stream is rebuilt per shape. The
FastFlowLM harness needs that: it registers one `mm.xclbin` per model and swaps
instruction streams, against a budget of 16 xclbins for a whole model. See
[Runtime parameters](#runtime-parameters).

The overall dataflow is the same whole-array shape as `iron.operators.GEMM`'s —
A broadcast along each compute row, B down each column, C joined through the
memtile — so those are *not* what distinguishes it. What does:

| | `iron.operators.GEMM` | `flm.ProjectionGEMM` |
|---|---|---|
| tiling | parameterized tiles, 1–8 columns | m=64, r/s/t 8/8/8; `k_tile` and `tile_n` tunable |
| after the product | nothing | fused f32→bf16 + activation |
| B layout | `(K, N)`, or `(N, K)` with `b_col_maj` | `(N, K)` with `b_col_maj`, or packed by `pack_b` |
| A tile height | tied to the accumulator | decoupled (asymmetric tile buffering) |

The shipped overlay itself is a test fixture, `iron/tests/support/shipped.py`
([Matching the shipped FastFlowLM overlay](#matching-the-shipped-fastflowlm-overlay)),
that `test.py` compares the port against.

## Architectures

Runs on both NPU2 (aie2p — Strix/Krackan) and NPU1 (aie2 — Phoenix/Hawk Point).
The tiling and the whole blocked L1 layout are shared; only the grid width and
two lowering details differ.

| | NPU2 | NPU1 |
|---|---|---|
| grid | 4 x 8 | 4 x 4 |
| A forwarded through | every other memtile | every memtile |
| 8x8x8 mmul lowers to | 2 bfp16-emulated macs | 4 native 4x8x4 bf16 macs |

The mmul shape is **not** specific to the bfp16 path, despite needing
`AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16` to get the fast lowering on NPU2:
`aie::mmul<8,8,8>` decomposes onto AIE2's native 4x8x4 bf16 mac as exactly four
macs with no wasted lanes, so `pack_b`, the stream-dimension lists and
`gather_dims` are shared verbatim. On AIE2 that flag is silently ignored, so it
is only passed where it changes codegen.

Two consequences of the native-vs-emulated split are worth knowing:

* **NPU1 is materially more accurate**, because bfp16 emulation drops mantissa
  bits and native bf16 macs accumulating in f32 do not. See
  [Accuracy](#accuracy).
* **`Rounding.FLOOR` reproduces the shipped FastFlowLM overlay bit-for-bit on
  NPU2 only.** NPU1 sums the K reduction in a different order, so it matches the
  rounding *mode* but not the exact results.

## Runtime parameters

**Six words** in an L1 buffer per core, written by the runtime sequence and
read by the core once its barrier opens:

| word | value |
|---|---|
| `N` | the raw N; the core derives its own `n_work` / `n_drain` from it |
| `m_row_blocks` | `M / 256` |
| `k_iters` | `K / 512` |
| epilogue | the `Epilogue` mode |
| `clamp_min` / `clamp_max` | the kernel's clamp bounds, `(-inf, +inf)` as raw `int32` bit patterns |

A word is not free: each costs ~66 ns per core and the sequence writes
`ROWS * COLS` = 32 of them, so **every word is ~2 us of dispatch latency**
(measured by padding the buffer at a fixed core count). Against a ~107 us
floor that is most of a short-prefill dispatch, so `build()` lists only the
words a configuration's cores read (`Rtp(...)`), and the buffer is sized
to them. Two groups are therefore conditional or gone:

* `n_units` is sent **only when `m_chunk > 1`**. It is
  `m_row_blocks // m_chunk`, so at the default `m_chunk = 1` the core just
  reads `m_row_blocks`.
* `units_valid`, the 256-row units a per-call row bound reaches, is a word
  **only for a bounded design on an xclbin**; elsewhere the cores run
  `m_row_blocks`. See "A row bound per call" below.
* `n_work` / `n_drain` are **not sent at all**. The core derives them from `N`
  and its own column, which it reads from a per-tile buffer initialised at
  build time. Branch-free, and both divisors are powers of two, so it costs
  shifts rather than a `__divsi3` call:

      n_tiles = N // N_TILE
      n_work  = (n_tiles - my_col + COLS - 1) // COLS
      n_drain = ((n_tiles + COLS - 1) // COLS) - n_work

The clamp bounds are the one group that is unconditional though no caller
clamps. The kernel has no unclamped instantiation to compile out, so every
dispatch sends `(-inf, +inf)`, which leaves every finite value bit-identical.
The bounds stay raw `int32` because `npu_write_rtp` writes i32 only; the kernel
casts back with `__builtin_bit_cast`, since `memcpy` leaves an unresolved
external call rather than folding to a register move.

  The column index is per-tile **static data**, deliberately not a constant
  folded into the program: the 32 core programs today differ only in symbol
  names, and baking it into code would make them differ in instructions,
  foreclosing a future one-program xclbin.

Measured on the 30-shape suite at **four** words: **-3.5% median at M=256**
(best -11.3%, E2B/kv), and within noise at M >= 1024 -- the saving is a
constant ~12 us, so it is a short-prefill and decode lever, not a prefill one.
Making the clamp bounds unconditional put two words back, which the ~2 us per
word above prices at **~4 us of that ~12**; the shape of the result is
unchanged but the median has not been re-measured since.

All columns are always built. One with no work for a shape gets `n_work = 0`
and still drains its share of the A broadcast, because the memtile will not
release an A object until every consumer has taken it.

The two artifacts therefore carry different stems: the xclbin's `config_name`
covers tile_n, ct_k, tile_ma, the compiled activation set, rounding and the
device, while `name` adds every runtime parameter -- M, K, N and the
activation -- so two instruction streams never share a name. The
xclbin is built from a module emitted at a reference shape, whose runtime
sequence is discarded.

One thing stays build-time, because it costs program memory: which activations
the epilogue can *select between* (`epilogue_modes`). It lands in the xclbin's
name.

The core releases its barrier straight after reading the parameters.
`wait_for_value` emits `LockAction.Acquire`, which does not leave the lock
consumed, so without the release a core that runs twice does not wait the
second time and reads the previous dispatch's parameters. Releasing before the
work is safe, because the sequence cannot set the barrier again until it has
drained this dispatch's C.

The repo's other barrier users never hit this, because neither waits twice:
`mha` puts its infinite loop *inside* the wait, and `softmax` writes the same
parameters every dispatch. `test_one_xclbin_serves_every_shape` is the
regression test -- without the release it hangs the device on the second
shape, and the parametrised tests cannot catch it, because the `aie_context`
fixture reconfigures the array between cases.

## Shape constraints

`M % 256 == 0`, `K % 512 == 0`, `N % tile_n == 0` (so 64 by default).

N only has to tile to `tile_n`, not to the grid's `tile_n * cols` stride: a
trailing group of fewer column-blocks than the grid is wide is handled by giving
the columns different trip counts. That matters in practice — a transformer's
`o` and `down` projections have N = model dim, which is essentially never a
multiple of the full stride.

## B must be pre-packed

```python
op = ProjectionGEMM(M=M, K=K, N=N)
op(A, op.pack_b(B), C_out)
```

`pack_b` reorders a row-major `(K, N)` matrix into the order the compute tiles
read it, so each fill is one contiguous run. On NPU2 it also quantizes to
bfp16ebs8 and returns a flat `uint8` tensor rather than bf16; on NPU1 it stays
bf16. The layout itself lives in
[`iron/operators/flm/packing.py`](../packing.py).

Call it on the operator — `op.pack_b(B)` — not on the class: the layout depends
on the resolved `tile_n` and on the device.

This is deliberately the caller's job rather than something the fill descriptor
does. The same reorder *is* expressible as a strided descriptor over an unpacked
B, but its innermost run is then `t` bf16 values = 16 bytes, so each 128 KB
transfer becomes thousands of scattered bursts. B is ~70% of the bytes a
dispatch moves, so the operator ran at ~10 GB/s instead of ~47 — a 5.4x
end-to-end penalty. Weights are packed once and reused across dispatches, so the
cost belongs at the caller.

### Or read as stored

```python
op = ProjectionGEMM(M=M, K=K, N=N, b_col_maj=True)
op(A, W, C_out)  # W is (N, K), a checkpoint's layout
```

`b_col_maj=True` takes B as a checkpoint stores a projection, `(N, K)`, in
bf16, so no packed copy sits beside the one a decode GEMV reads. The shim
reads each `(tile_n, k_tile)` block as `tile_n` runs of `k_tile` elements
(1 KB each), the memtile hands the core one 8-deep k panel at a time, and the
kernel transposes it (`fused_mm(..., b_col_maj=True)`). The short runs are
between the memtile and the core, not in DDR. On NPU2 the core converts the
bf16 B to bfp16 for the bfp16 macs (`precision="medium"`), so its
arithmetic is the packed path's; `"high"` multiplies in bf16. `precision`
has no default: every caller names it.

At Llama 3.2 1B's prompt projections (M = 2048, `epilogue_modes=("none",)`)
on Strix, the times below are the fastest of 8 interleaved rounds, each the
median of 10 runs, and the error is the mean |C − C_f32| over the mean |C_f32|:

| K × N | packed | `b_col_maj` | `b_col_maj`, bf16 macs | `iron.operators.GEMM` |
|---|---|---|---|---|
| 2048 × 8192 | 4.10 ms | 4.40 ms | 103.4 ms | 12.8 ms |
| 2048 × 2048 | 1.10 ms | 1.16 ms | 26.4 ms | 3.11 ms |
| 2048 × 512 | 0.35 ms | 0.40 ms | 6.81 ms | 0.86 ms |
| 8192 × 2048 | 5.55 ms | 7.35 ms | 103.5 ms | 28.0 ms |
| error | 2.6e-4 | 2.6e-4 | 3.9e-5 | 3.2e-4 |

`b_col_maj` moves 1.78x the B bytes of the packed path. Where B is resident
(K ≤ 2048 here) that costs 5-14%; at K = 8192 both stream B, and it costs 32%.

On Phoenix, where B is bf16 either way, the times below are the range over 8
interleaved rounds, each the median of 10 runs:

| K × N | packed | `b_col_maj` | `iron.operators.GEMM` |
|---|---|---|---|
| 2048 × 8192 | 28.5–28.7 ms | 25.4–25.7 ms | 28.0–28.3 ms |
| 2048 × 2048 | 7.5–8.0 ms | 7.0–7.3 ms | 7.3–7.9 ms |
| 2048 × 512 | 2.5–3.8 ms | 1.9–3.6 ms | 2.9–3.7 ms |
| 8192 × 2048 | 27.9–28.2 ms | 25.0–25.4 ms | 43.4–45.0 ms |

## Matching the shipped FastFlowLM overlay

`Rounding.FLOOR` reproduces the shipped `mm.xclbin` **bit for bit**. The AIE
core powers up in `rounding_mode::floor` and the original kernel never calls
`set_rounding`, so that is the arithmetic it ships with.

```python
ProjectionGEMM(M=M, K=K, N=N, rounding=Rounding.FLOOR)  # matches shipped
ProjectionGEMM(M=M, K=K, N=N)                           # conv_even, default
```

Verified against the shipped overlay on identical inputs, driven through
the test fixture `iron/tests/support/shipped.py`, which runs that xclbin unmodified: with
`floor` and no activation, output is **bit-identical across all 6291456
elements**. With the `conv_even` default it differs everywhere, and is far more
accurate — see [Accuracy](#accuracy).

**By default the activations deliberately do not match bit for bit**, even under
`floor`. The overlay rounds its accumulator to bf16 and then applies the
activation to that; this operator applies the activation to the f32 accumulator
and rounds once, on the store. Rounding before a nonlinearity rounds twice and
lets the activation's slope amplify the first rounding, so the overlay's order
is the less accurate one and is not worth reproducing. The cost of diverging is
visible — at M=256 K=512 N=1024, 117582/262144 silu elements differ from the
overlay — and so is the benefit: against an exact f64 evaluation, mean |err|
improves and gelu's worst case drops 5.5%. Measured perf-neutral (0.993-1.006x,
inside the run-to-run spread).

**gelu can match the overlay on request.** A port of a whole model must
reproduce the shipped engine's tokens, and Gemma 4's gate projections use gelu.
`gelu=Gelu.BF16_STEPS` selects the overlay's arithmetic: the kernel rounds the
accumulator to bf16 and then rounds after each step of `x * sigmoid(1.702x)`,
as the overlay's `getGeluBf16_nonLUT` does. fp32 is the default, for the
accuracy reasons above. silu and sigmoid have no such option.

```python
ProjectionGEMM(M=M, K=K, N=N, epilogue="gelu", rounding="floor", gelu="bf16_steps")
# gelu matches Shipped
```

With `floor`, gelu output is **bit-identical** to the overlay's on NPU2 at
M=256 K=512 N=1024, M=512 K=1536 N=6144 (Gemma 4 E2B `gate_proj`) and M=512
K=1536 N=256 (E2B per-layer-input gate), at input scales 0.5 and 4.0. With the
fp32 default, 121917/262144 elements differ at the first shape and scale 0.5.
`test_gemm_gelu_bf16_steps_matches_overlay` checks this against `Shipped`.
`gelu` changes only the gelu arm of the kernel.

The shipped kernel selects its activation -- and its shape -- from runtime
parameters, one overlay serving every projection. This operator does the same
(activation keeps the shipped 0/1/2/3 mapping); see
[Runtime parameters](#runtime-parameters). Which activations the epilogue can
*select between* is still a build-time choice, because each one compiled in
costs program memory.

## Accuracy

Everything about accuracy is in this section; other sections link here.

**How to measure it.** A pure elementwise *relative* tolerance is not meaningful:
with signed A the K-term sum cancels by ~sqrt(K), so |C| is ~20x smaller than the
accumulated magnitude while the error tracks that magnitude, leaving near-zero
outputs relatively uncheckable. Bound the error against the accumulated mass
`K * mean|a| * mean|b|` instead, as `test.py` does.

**It is architecture-dependent**, because the same 8x8x8 mmul lowers differently:
NPU2 emulates it with two bfp16 macs, which drop mantissa bits, while NPU1 uses
four native 4x8x4 bf16 macs, which do not. `test.py` sets the budget per
architecture — inheriting NPU2's on NPU1 would leave ~70x of slack.

Mean |err| against the accumulated mass, random signed A / non-negative B:

| | NPU2 | NPU1 |
|---|---|---|
| `Rounding.CONV_EVEN` (default) | 0.000241 | < 1e-6 |
| `Rounding.FLOOR` | 0.009867 | 0.00015 |

**Prefer the `conv_even` default.** Truncation biases every conversion the same
direction, so the error accumulates over the K reduction instead of cancelling:
~41x more error for no measured speed difference. Use `floor` only to reproduce
the shipped overlay (see [below](#matching-the-shipped-fastflowlm-overlay)).

Do not hold this operator to `iron.operators.GEMM`'s test tolerances: those
assert on its `r=4` path at `precision="highest"`, which this operator does
not offer.

## Choosing `tile_n`

`tile_n` defaults to `None`, which picks per shape and per device: on NPU2,
**128 when `K == 512`, otherwise 64**; on NPU1, **always 64**. Override only if
you have measured a reason to.

`n=64` gives the mmul `colA=8` rather than 4, halving accumulator traffic per
mac. `n=128` instead halves A fetches, because the grid then covers twice as
many columns of N per pass. Which wins depends on whether compute or data
movement is the critical path, and on NPU2 that turns on how much K there is
to reduce over -- with a single k iteration there is not enough compute to
hide the extra A traffic.

On NPU2, `tile_n=128` wins only at `k_iters=1`, and by ~3%; at `k_iters>=2` it
was 1.2-1.7x slower, measured while its k slice (`ct_k`) was fixed at 32: the
compute cost of the shorter k slice swamps the A traffic it saves.

NPU1 never reaches that crossover. It has half the columns *and* a quarter of
the per-tile bf16 mac throughput, so it stays compute-bound at every K, and
`n=128` also costs it a much larger f32 accumulator. `n=64` wins at every
`k_iters`, by 1.2-1.8x.

## Performance

### NPU2

M=1024 K=1536 N=6144, min of per-run medians:

| | bytes moved | latency | err/mass |
|---|---|---|---|
| `flm.ProjectionGEMM` (`tile_n=64`) | 47 MB | **1143 us** | 2.39e-04 |
| `Shipped(...)` (the shipped overlay) | 107 MB | 2175 us | 9.87e-03 |
| `iron.operators.GEMM` (same emulated mode) | 126 MB | 3353 us | 2.41e-04 |

**1.90x the shipped overlay, and 41x more accurate than it** — the accuracy
comes from `conv_even` rounding, which the overlay does not set (see above).

Three choices account for most of the gap, and none of them helps alone:

* **`pack_b` emits the final consumption order**, so both B hops are linear
  descriptors. Worth nothing by itself — it is what frees the descriptor
  dimensions the other two need.
* **Asymmetric tile buffering**, which pays for a k slice deep enough to halve
  the accumulator traffic per mac.
* **A rolled mmul inner loop**, which is faster than hand-unrolling it here
  (see `mm_fused_mmul.h`).

Storing B in bfp16 is numerically free: the NPU2 mmul only multiplies bfp16, so
quantizing on the host hoists a rounding that already happened on every mac
call. It does have to reproduce the core's rounding *mode* to be free — see
`iron/operators/flm/packing.py`.

> **Measuring this.** Dispatch latency on this part is *bimodal*, with modes
> about 6% apart, and both show up for every configuration. A batch that lands
> wholly in one mode turns min-of-medians into a mode selector rather than a
> measurement. Compare configurations **interleaved** round-robin rather than
> one after the other, use at least 8 rounds each, and believe a difference only
> when the min and the median agree on it.

### NPU1

L1 tile selection reserves the linked `lut_based_ops.cpp` tables (5,248 bytes
per core) and the stack before it sizes the data buffers. It then takes
double-buffered L1 B, the deepest k slice (`ct_k`) that still fits, and the
tallest A tile: the default `tile_n=64` configuration takes `ct_k=64` and
`tile_ma=64`, `tile_n=32` takes `ct_k=128`, and `tile_n=128` takes `ct_k=32`.
Each k slice reloads and stores the f32 accumulator, and a B chunk the core
waits on stalls it, so both matter; the A height measured no effect. On
xcoradaie205 (Phoenix), median of 20 dispatches, every output checked:

| M / K / N | tiles | before (ct_k fixed) | L1-derived ct_k |
|---|---|---|---|
| 512 / 2048 / 2048 | `tile_n=64` | 2878 us (ct_k 128, single B) | **2355 us** (ct_k 64) |
| 1024 / 2048 / 1024 | `tile_n=64` | 2870 us (ct_k 128, single B) | **2337 us** (ct_k 64) |
| 512 / 2048 / 2048 | `tile_n=32` | 3232 us (ct_k 32) | **2344 us** (ct_k 128) |

The table below predates the LUT reservation and the L1-derived k slice.

Against `iron.operators.GEMM` at its own defaults (64/64/64 over all 4
columns), min of 5 interleaved rounds of 20 dispatches each:

| M / K / N | `flm.ProjectionGEMM` | `iron.operators.GEMM` | speedup | GFLOP/s |
|---|---|---|---|---|
| 256 / 512 / 512 | **218 us** | 227 us | 1.04x | 615 |
| 512 / 512 / 1024 | **390 us** | 466 us | 1.19x | 1377 |
| 512 / 1024 / 1024 | **639 us** | 798 us | 1.25x | 1680 |
| 1024 / 1024 / 1024 | **1071 us** | 1418 us | 1.32x | 2005 |
| 1024 / 2048 / 1024 | **2134 us** | 2738 us | 1.28x | 2013 |
| 512 / 1536 / 1536 | **1498 us** | 1699 us | 1.13x | 1613 |
| 1024 / 2560 / 2560 | **6364 us** | 8232 us | 1.29x | 2109 |

`K=1536` is the weak shape, at 1.13x against 1.25-1.32x for its neighbours.
It is the one place the L1 configuration below does not suit NPU1: `k_iters=3`
leaves the k slice partly unused. Worth a look if NPU1 throughput matters.

The margin is smaller than NPU2's ~1.9x, and that is expected rather than a
port problem: much of the NPU2 win comes from the bfp16 fast path (two macs per
8x8x8 shape against four) and from spreading A across eight columns. On NPU1
both operators lower to the same native 4x8x4 mac, so what remains is the
cheaper transfers below — pre-packed B and one transfer per column-block —
which is why the gap grows with the problem size rather than being flat.

Unlike NPU2, compute here is **not** hidden behind the transfers, so on NPU1
both a faster mmul and less traffic pay off, where on NPU2 only the latter does.

### Why the transfers are cheap

Two things, both in the runtime sequence rather than the kernel:

* **B arrives pre-packed**, so the contiguous run per transfer is 128 KB for B
  and 1 KB for A, against 128 bytes on every leg for `iron.operators.GEMM`,
  which reorders in the descriptor instead.
* **Each of A, B and C goes out as one transfer per column-block**, not one per
  fifo object. A single fill or drain may span many objects; issuing per object
  means a host await per row-block, and a C await waits on the cores.
  Collapsing them also keeps the sequence short: a block is 3 shim transfers
  instead of `1 + 2*k_iters`.

### B is resident where it fits, programmed per shape

Where a column-block of B fits in the memtile, DDR reads it **once** and the
memtile replays it to every row-block, instead of DDR re-reading it
`m_row_blocks` times. A fifo cannot do this under one xclbin per config: its
memtile BDs are device configuration, so a resident fifo would put K (buffer
size) and M (replay count) into the xclbin every shape shares.

So B does not use an ObjectFifo. The **device** side is shape-independent,
built in `build()` and returned from it with the Workers (the pool on `rt.built`):

* per column, a memtile pool of `B_SLOTS` k-block slots with one producer and
  one consumer lock per slot, and an L1 ring on each core fed by a static
  looping `TileDma`;
* explicit `Flow`s: shim → memtile, and a memtile broadcast → every core in
  the column. They name no channel: the compiler assigns them around A and
  C, and the DMA programs run on `flow.endpoint(tile)`. No tile is pinned;
  the placer places them all.

B's lanes are bound to the shim flows, so `sequence()` fills them like any
other stream. The **runtime sequence**, which is generated per shape, programs
both memtile channels with tasks of one BD per slot
(`flow.endpoint(memtile).task(...)`), walked `runs` times:

| | resident (`k_iters <= B_SLOTS`, `n_units <= 63`) | streamed (otherwise) |
|---|---|---|
| slots used | `k_iters` | largest divisor of `n_units * k_iters` up to `B_SLOTS` |
| fill: acquire prod ≥ `b_uses`, release cons by `b_uses` | once per column-block | once per unit |
| drain: acquire cons ≥ 1, release prod by 1 | once per unit | once per unit |
| `b_uses` | `n_units` | 1 |

A resident slot is therefore not refilled until every unit has read it, and a
streamed one turns over like a fifo object. Both end the dispatch with each
producer lock back at their own `b_uses`, which is why the sequence
sets it (`Lock.set`) at the start: the previous dispatch on the context may have
been a different shape.

On NPU2, `B_SLOTS` is 8 at `tile_n` ≤ 64 (K ≤ 4096) and 3 at `tile_n` = 128,
which op.py only picks for K ≤ 512. The 63 is the 6-bit lock value, so
residency also needs M ≤ 16128. **Down projections stay streamed**, K being
6144 or 10240; for them B moves exactly as it did through the fifo.

Constraints, all enforced in op.py:

* **A column-block's memtile pushes must fit one task queue**, 4 pushes of 256
  passes (`repeat_count` is 8 bits). A chain is pushed at the first block it
  covers, so every queue wait the compiler inserts is for an earlier block,
  whose fills and C are already out; one past the queue would wait on its own
  block's C, which goes out after it. M is cut into slabs where needed. Memtile
  tasks are never awaited — C completing implies them. None of the benchmark
  shapes comes near.
* **Arm B after the first block's fills, not before** (the class sets
  `own_preamble`, so `sequence()` places `rt.preamble()` itself). `set_lock` is cheap
  (~0.2 µs each), but putting it and the RTP writes ahead of the first A and B
  fills cost up to +9% at M=256. Issued between the first block's fills and its
  C, the setup hides under the fill latency. That reordering is independent of
  residency and is part of the M=256 gain below.
* **NPU1 fits exactly**: bf16 B at `tile_n=64` leaves room for 5 slots, which
  fill the memtile to the byte. It builds and places, but every shape
  currently times out on NPU1 hardware, so its tests and benchmark skip there.

This needs mlir-aie #3791 (first in the 1.4.4.dev69 wheel): runtime tasks on a
memtile's channels, `Task.start(repeat_count=...)`, `Lock.set`, and repeat
counts past one push. The instruction stream is built with
`aiecc --reclaim-runtime-bds` (`ProjectionGEMM.aiecc_flags`), since a split leg's pieces outnumber the shim's
BD ids. Every hardware limit the design uses but `B_MAX_SLOTS` comes from the
target model.

Measured on NPU2 (Strix, power mode `default`) against the fifo version over
the 30 benchmark shapes, 4 interleaved rounds on mlir_aie 1.4.4.dev73, errors
bit-identical on all: median **-23.9%**, best -37.7% (E4B gateup M2048).

| shapes | change |
|---|---|
| resident, M ≥ 1024 | -20.9% to -37.7% |
| M = 256 (one row-block, nothing to replay) | +0.9% to -13.5%, from the setup ordering and queue depth |
| down projections (streamed), M ≥ 1024 | -2.0% to +1.8%, i.e. noise |

### Each half of the core rows takes its own range of M

A shim tile has two S2MM channels, so C goes out in two joins per column, one
per half of the core rows (rows 0-1 and 2-3), each on its own channel. Each
half takes its own range of M, its two rows' 64-row blocks interleaved in it:
half `h`'s unit `u` is the 128 rows from `(h * n_units + u) * 128`. A leg so
steps 128 rows a unit, not 256, and K or N up to 16384 fits a descriptor's
20-bit step (4 MiB); with one join of all four rows, Qwen2.5 1.5B's 8960-wide
up and down projections did not. The cores are unchanged: each computes the
rows its A brings and drops its C in order.

### The compiler bounds what is outstanding

The sequence issues one transfer per leg per column-block, whatever the shape.
Where K or N is past 16384, a half's row-block stride overflows the shim BD's
20-bit step, and under `m_chunk` A's pattern has 5 dimensions. The compiler
cuts such a leg into pieces a BD can take, one task each, and interleaves them
with the other legs' transfers so that a wait on one leg is for transfers the
other has already been given.

Two shim resources bound how many transfers may be outstanding: BD ids
(16/tile) and the channel task queue (4 deep). The compiler owns both. Every
transfer is unmanaged: before a push that would overrun a queue it polls for a
slot, and when a tile runs out of BD ids it takes one back from a transfer a
status poll proves finished. Both waits are per transfer, so the channel stays
full. Awaiting in windows instead — issue four, await all four — drains the
channel at every boundary and measured up to 12.4% slower on the shapes that
cut a leg (E4B/gateup M1024).

The sequence's only share is order and one token. Only each column's last C of
a slab carries a token: C drains in order, so it finishing means the slab is
done.

`m_chunk` is 1 by default: a shape it does not divide would fork the xclbin.

### A row bound per call

A prompt chunk projects `x[:rows]` (`valid`, `per_call(bounds=M)`), and one
compile serves every row count. A and C move, and the cores compute, only the
units the bound reaches. A unit is the 256 rows (`rows * M_TILE`) the four
core rows compute at once, 128 in each half's range, so a bound rounds up to
it: that is the array's granularity, not a DMA rule. The second half's range
starts past the first's 128 rows a unit, a per-call offset.

| | xclbin | full ELF (NPU2) |
|---|---|---|
| cores | read `units_valid` from a parameter word bounded designs add | read it from the scratchpad |
| A | one transfer per lane, `units_repeat` (units less one) its runtime repeat count | the same, a scratchpad repeat parameter (mlir-aie's repeat-parameter) |
| C | `units_valid` row blocks, a runtime size | the same, a patched length |
| second half | A and C start at `a_half` and `c_half`, the units' 128 rows of K and of N, a runtime offset | the same, scratchpad offset parameters |
| B, streamed | one fill per lane, `units_repeat` its runtime repeat count; the memtile ring's passes `b_passes_repeat`, a runtime repeat count | the same, scratchpad repeat parameters (on the memtile's queues too) |
| B, resident | as unbounded | as unbounded |

Every GEMM bounded by the same rows shares `units_valid` and `units_repeat`,
and every one as wide shares a half's offset (a K's `a_half` is the same word
as an N's `c_half`); `b_passes_repeat` is `units_repeat` where B is resident,
and its own word where B streams (one per ring), so Llama 3.2 1B's prompt
chunk takes 6 of a full ELF's 32.

Streamed B follows the bound: DDR reads it once per unit reached, and the
memtile ring, whose slots then divide one unit's k tiles, passes it on as
many times, so a short call strands nothing in the memtile. Resident B does
not: its replay count is the memtile's lock values, which no per-call word
reaches, so the memtile replays it for every unit and the cores drain a unit
past the bound's replay without computing it (`b_resident`). They drain those
first, since every replay is the same B, so each column's last C still ends
the call; a call with no rows has no C to end it, and is refused. A resident
unit past the bound therefore still costs its B broadcast from L2, never DDR.
A bound needs `m_chunk = 1`, M in one slab, and a streamed column-block's
ring passes in one queue push.

## The shipped overlay

```python
from iron.tests.support.shipped import Shipped

op = Shipped(M=1024, K=1536, N=6144, epilogue="silu")
op(A, op.pack_b(B), C_out)
```

`Shipped` (`iron/tests/support/shipped.py`) is FastFlowLM's `mm.xclbin` **unmodified**, as a
second overlay for the same operator: the binary the port was ported from,
driven by the same `ProjectionGEMM`, its reference and its packing, so the two can be
measured against each other on identical inputs through one host path.
`test.py` does exactly that, and checks the shipped overlay's epilogues
against its own accumulator.

**NPU2 only** — the overlay is an 8-column NPU2 binary. Tuning it for
anything else raises.

### How it is obtained

The xclbin is not checked in. It is an `Xclbin`: downloaded on first use into
`NPU_CACHE_HOME` and pinned by SHA-256 against an immutable FastFlowLM commit,
so the fetch is reproducible and a substituted file is rejected.

Because this is the only thing in the tree that touches the network, the
device tests that use it are marked `extensive` and are not reached by the
default `-m "not extensive"` run.

### What the overlay supplies

The overlay ships as a binary, so every core program, memtile buffer and
stream-switch route comes from the xclbin. The overlay supplies only the
host-side half of a dispatch, and `ProjectionGEMM`'s own `pack_b`, `reference` and
packaging serve it:

* **The runtime parameters.** One overlay serves every projection in a model, so
  the shape and the activation arrive as words in each core's data
  memory. A core blocks on a lock until the sequence releases it, so a dispatch
  that writes no parameters hangs.
* **The shim DMA transfers**, reproducing the overlay's fixed channel map.

### Differences from the port

| | `Shipped(...)` | `ProjectionGEMM(...)` |
|---|---|---|
| provenance | shipped binary, downloaded | built from source in this repo |
| devices | NPU2 only | NPU2 and NPU1 |
| `tile_n` | fixed at 128 | 64 or 128, chosen per shape and device |
| epilogue selected | at runtime, by parameter | at compile time |
| rounding | core power-up `floor` | `conv_even` by default |
| B | pre-packed bf16 | pre-packed, bfp16 on NPU2 |

The epilogue difference is the interesting one. Selecting at runtime means one
build serves every activation; baking it in, as `flm.ProjectionGEMM` does, costs a build
per activation but leaves the inner loop branch-free. The rounding difference is
why `flm.ProjectionGEMM` is ~41x more accurate by default — see
[Matching the shipped FastFlowLM overlay](#matching-the-shipped-fastflowlm-overlay),
which also records that `ProjectionGEMM(rounding="floor")` reproduces this overlay bit
for bit.
