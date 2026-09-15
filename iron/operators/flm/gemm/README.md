<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.GEMM` — bf16 GEMM with a fused epilogue

```python
from iron.operators.flm import GEMM
from iron.operators.flm.gemm.design import Epilogue

op = GEMM(M=1024, K=1536, N=6144, epilogue=Epilogue.SILU, context=ctx)
op.compile()
op.get_callable()(A, op.pack_B(B), C_out)
```

`epilogue` and `rounding` are `StrEnum`s, so the bare strings `"silu"` /
`"conv_even"` are accepted too.

A second GEMM implementation alongside [`iron.operators.GEMM`](../../gemm),
specialised for transformer projection shapes and ported from FastFlowLM's `mm`
overlay.

**M, K, N and the activation are runtime parameters**, so one xclbin serves
every shape and only the instruction stream is rebuilt per shape. The
FastFlowLM harness needs that: it registers one `mm.xclbin` per model and swaps
instruction streams, against a budget of 16 xclbins for a whole model. See
[Runtime parameters](#runtime-parameters).

The overall dataflow is the same whole-array shape as `iron.operators.GEMM`'s —
A broadcast along each compute row, B down each column, C joined through the
memtile — so those are *not* what distinguishes it. What does:

| | `iron.operators.GEMM` | `flm.GEMM` |
|---|---|---|
| tiling | parameterized tiles, 1–8 columns | fixed m=64 k=512, r/s/t 8/8/8; `n` selectable |
| epilogue | none (separate `convert_copy`) | fused f32→bf16 + activation + clamp |
| B layout | plain `(K, N)` | **pre-packed by the caller**, see below |
| A tile height | tied to the accumulator | decoupled (asymmetric tile buffering) |

Pick this one for a projection-shaped GEMM that wants an activation folded in
and can pack its weights once. Pick `iron.operators.GEMM` when you need tiling
control or cannot pre-pack B.

The shipped overlay itself is available as
[`iron.operators.flm.MMPrebuilt`](../mm_prebuilt) for comparison; `benchmark.py`
measures the two against each other and against `iron.operators.GEMM`.

## Architectures

Runs on both NPU2 (aie2p — Strix/Krackan) and NPU1 (aie2 — Phoenix/Hawk Point).
The tiling and the whole blocked L1 layout are shared; only the grid width and
two lowering details differ.

| | NPU2 | NPU1 |
|---|---|---|
| grid | 4 x 8 | 4 x 4 |
| A broadcast sources | shim columns 0/2/4/6 | shim columns 0/1/2/3 |
| 8x8x8 mmul lowers to | 2 bfp16-emulated macs | 4 native 4x8x4 bf16 macs |
| `tile_n` default | 128 at K=512, else 64 | always 64 |
| epilogue `tanh` | native `aie::tanh` | `getTanhBf16` LUT |

The mmul shape is **not** specific to the bfp16 path, despite needing
`AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16` to get the fast lowering on NPU2:
`aie::mmul<8,8,8>` decomposes onto AIE2's native 4x8x4 bf16 mac as exactly four
macs with no wasted lanes, so `pack_B`, the stream-dimension lists and
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
| `clamp_min` / `clamp_max` | the bounds, as raw `int32` bit patterns |

A word is not free: each costs ~66 ns per core and the sequence writes
`ROWS * COLS` = 32 of them, so **every word is ~2 us of dispatch latency**
(measured by padding the buffer at a fixed core count). Against a ~107 us
floor that is most of a short-prefill dispatch, so `rtp_layout()` in design.py
sizes the buffer per configuration rather than sending words a build cannot
use. Two groups are therefore conditional or gone:

* `n_chunks` / `n_units` are sent **only when `m_chunk > 1`**. They are
  `m_row_blocks // M_CHUNK` and each other, so at the shipped `M_CHUNK = 1`
  the core just reads `m_row_blocks`.
* `n_work` / `n_drain` are **not sent at all**. The core derives them from `N`
  and its own column, which it reads from a per-tile buffer initialised at
  build time. Branch-free, and both divisors are powers of two, so it costs
  shifts rather than a `__divsi3` call:

      n_tiles = N // N_TILE
      n_work  = (n_tiles - my_col + COLS - 1) // COLS
      n_drain = ((n_tiles + COLS - 1) // COLS) - n_work

The clamp bounds are the one group that is unconditional despite most callers
not clamping. The kernel has no unclamped instantiation to compile out: an
unclamped dispatch sends `(-inf, +inf)`, which leaves every finite value
bit-identical. Two always-sent words buy one xclbin for clamped and unclamped
callers alike, which is the whole point of the runtime parameters, and a
clamping caller now sends one word fewer than the old `clamp_enabled` trio did.
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
covers tile_n, ct_max_k, tile_ma, the compiled activation set, rounding and the
device, while `name` adds every runtime parameter -- M, K, N, the activation
and the clamp bounds. It has to: the sequence writes those as immediates and
the build cache keys on filename and mtime, so a stem that omits one serves the
first caller's instruction stream to the second. The xclbin is built from a
module emitted at a reference shape, whose runtime sequence is discarded.

One thing stays build-time, because it costs program memory: which activations
the epilogue can *select between* (`epilogue_modes`). It lands in the xclbin's
name. The clamp does not -- every build compiles it, so `clamp=(-2, 2)`,
`clamp=(-4, 4)` and no clamp at all share one xclbin.

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
op = GEMM(M=M, K=K, N=N, context=ctx)
op.compile()
op.get_callable()(A, op.pack_B(B), C_out)
```

`pack_B` reorders a row-major `(K, N)` matrix into the order the compute tiles
read it, so each fill is one contiguous run. On NPU2 it also quantizes to
bfp16ebs8 and returns a flat `uint8` tensor rather than bf16; on NPU1 it stays
bf16. The layout itself lives in
[`iron/operators/flm/packing.py`](../packing.py).

Call it on the operator — `op.pack_B(B)` — not on the class: the layout depends
on the resolved `tile_n` and on the device.

This is deliberately the caller's job rather than something the fill descriptor
does. The same reorder *is* expressible as a strided descriptor over an unpacked
B, but its innermost run is then `t` bf16 values = 16 bytes, so each 128 KB
transfer becomes thousands of scattered bursts. B is ~70% of the bytes a
dispatch moves, so the operator ran at ~10 GB/s instead of ~47 — a 5.4x
end-to-end penalty. Weights are packed once and reused across dispatches, so the
cost belongs at the caller.

## Matching the shipped FastFlowLM overlay

`Rounding.FLOOR` reproduces the shipped `mm.xclbin` **bit for bit**. The AIE
core powers up in `rounding_mode::floor` and the original kernel never calls
`set_rounding`, so that is the arithmetic it ships with.

```python
GEMM(M=M, K=K, N=N, rounding=Rounding.FLOOR, context=ctx)  # matches shipped
GEMM(M=M, K=K, N=N, context=ctx)                           # conv_even, default
```

Verified against the shipped overlay on identical inputs, driven through
[`flm.MMPrebuilt`](../mm_prebuilt), which runs that xclbin unmodified: with
`floor` and no activation, output is **bit-identical across all 6291456
elements**. With the `conv_even` default it differs everywhere, and is far more
accurate — see [Accuracy](#accuracy).

**The activations deliberately do not match bit for bit**, even under `floor`.
The overlay rounds its accumulator to bf16 and then applies the activation to
that; this operator applies the activation to the f32 accumulator and rounds
once, on the store. Rounding before a nonlinearity rounds twice and lets the
activation's slope amplify the first rounding, so the overlay's order is the
less accurate one and is not worth reproducing. The cost of diverging is
visible — at M=256 K=512 N=1024, 117582/262144 silu elements differ from the
overlay — and so is the benefit: against an exact f64 evaluation, mean |err|
improves and gelu's worst case drops 5.5%. Measured perf-neutral (0.993-1.006x,
inside the run-to-run spread).

The shipped kernel selects its activation -- and its shape -- from runtime
parameters, one overlay serving every projection. This operator does the same
(activation keeps the shipped 0/1/2/3 mapping); see
[Runtime parameters](#runtime-parameters). Which activations the epilogue can
*select between* is still a build-time choice, because each one compiled in
costs program memory.

`clamp` has no counterpart in the shipped overlay to compare against — its
`generate_seq` never writes the clamp RTP words, so clamping is always off
there.

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

On NPU2 this operator and `iron.operators.GEMM` in its comparable mode
(`emulate=True, prio_accuracy=True`) are numerically **indistinguishable** —
identical mean error, signed bias and maximum, at both `tile_n` values. Do not
compare against `iron.operators.GEMM`'s own test tolerances, though: those assert
on its exact `r=4` path, which this operator does not offer.

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
is 1.2-1.7x slower, because its `CT_MAX_K` falls to 32 and the compute cost of
the shorter k slice swamps the A traffic it saves.

NPU1 never reaches that crossover. It has half the columns *and* a quarter of
the per-tile bf16 mac throughput, so it stays compute-bound at every K, and
`n=128` also costs it a much larger f32 accumulator. `n=64` wins at every
`k_iters`, by 1.2-1.8x.

`benchmark.py` measures both settings across the full shape sweep; prefer its
CSV output to any table reproduced here.

## Performance

### NPU2

M=1024 K=1536 N=6144, min of per-run medians:

| | bytes moved | latency | err/mass |
|---|---|---|---|
| `flm.GEMM` (`tile_n=64`) | 47 MB | **1143 us** | 2.39e-04 |
| `flm.MMPrebuilt` (the shipped overlay) | 107 MB | 2175 us | 9.87e-03 |
| `iron.operators.GEMM` (same emulated mode) | 126 MB | 3353 us | 2.41e-04 |

**1.90x the shipped overlay, and 41x more accurate than it** — the accuracy
comes from `conv_even` rounding, which the overlay does not set (see above).
`benchmark.py` reproduces this table, and covers 30 shapes rather than one.

Three choices account for most of the gap, and none of them helps alone:

* **`pack_B` emits the final consumption order**, so both B hops are linear
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
> when the min and the median agree on it. `benchmark.py` does this.

### NPU1

Against `iron.operators.GEMM` at its own defaults (64/64/64 over all 4
columns), min of 5 interleaved rounds of 20 dispatches each:

| M / K / N | `flm.GEMM` | `iron.operators.GEMM` | speedup | GFLOP/s |
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
  Collapsing them is also what makes overlapping column-blocks affordable — a
  block then costs 3 shim buffer descriptors instead of `1 + 2*k_iters`, so two
  can be in flight without exhausting the 16 available.

### B is re-fetched per row-block

DDR reads B `m_row_blocks` times rather than once. Holding a whole column-block
in the memtile and replaying it would size that buffer from `k_iters` and set
the replay from `m_row_blocks`, putting **both K and M into the device
configuration** — and the configuration is what one xclbin has to share across
every shape. That is the standing cost of M, K and N being runtime parameters,
and it is why B is the dominant DDR leg here.

**M is the tractable half.** `aiex.npu.push_queue` takes both `bd_id` and
`repeat_count` as SSA operands, and `aiex.dma_channel_reset_for(@fifo)` expands
into the whole re-arm trio a resident fifo needs — channel reset, `aiex.set_lock`
per bound lock, START_QUEUE re-push — inside the **runtime sequence**, which this
operator regenerates per shape. So a per-shape replay count does not have to
reach the xclbin. All of it is reachable from Python and has an npu2 device test
(1000 dispatches on one hardware context).

**K is the part still in the way.** Correct ordering needs one memtile object
spanning every k-block, so the buffer is sized from `k_iters` and that sizing is
device configuration. Selecting among several pre-programmed BD chains via
`push_queue`'s runtime `bd_id` is the obvious line of attack and has not been
tried.

### Split legs retire rolling, not in windows

Where K or N is 10240, the row-block stride overflows the shim BD's 20-bit
iteration step and that leg is issued as one transfer per row-block. Two shim
resources bound how many may be outstanding, and neither is modelled by the
toolchain: BD ids (16/tile, freed without a completion check) and the channel
task queue (4 deep, pushed unconditionally).

The sequence retires the **oldest** transfer as it issues the next, which
bounds both resources directly while keeping the channel full.

**Do not "simplify" this into windowing** — issue four, await the whole window,
issue the next four. That bounds the same two resources and reads more simply,
but it drains the channel to *empty* at every window boundary and again at every
column-block boundary, and on a DDR-rate-bound design those bubbles are the
entire cost of the split path. Measured at up to **-12.4%** on the shapes that
take this path (E4B/gateup M1024), for no change in what is in flight.

`m_chunk` takes this path too, since its only structural effect is to force the
split on for A. It is off by default regardless — see `M_CHUNK_FOR_N` in
design.py, which would fork the xclbin.
