<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.GEMM` — bf16 GEMM with a fused epilogue

```python
from iron.operators.flm import GEMM

op = GEMM(M=1024, K=1536, N=6144, epilogue="silu", context=ctx)
op.compile()
op.get_callable()(A, op.pack_B(B), C_out)
```

A second GEMM implementation alongside [`iron.operators.GEMM`](../../gemm),
specialised for transformer projection shapes and ported from FastFlowLM's `mm`
overlay.

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

* **NPU1 is materially more accurate.** bfp16 emulation drops mantissa bits;
  native bf16 macs accumulating in f32 do not. Measured mean |err| against the
  accumulated mass is under 1e-6 on NPU1 with `conv_even` versus 0.00042 on
  NPU2, and 0.00015 versus 0.0099 with `floor`. `test.py` sets the budget per
  architecture — inheriting NPU2's would leave ~70x of slack.
* **`rounding="floor"` reproduces the shipped FastFlowLM overlay bit-for-bit on
  NPU2 only.** NPU1 sums the K reduction in a different order, so it matches the
  rounding *mode* but not the exact results.

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

`rounding="floor"` reproduces the shipped `mm.xclbin` **bit for bit**. The AIE
core powers up in `rounding_mode::floor` and the original kernel never calls
`set_rounding`, so that is the arithmetic it ships with.

```python
GEMM(M=M, K=K, N=N, rounding="floor", context=ctx)   # matches shipped
GEMM(M=M, K=K, N=N, context=ctx)                     # conv_even, default
```

Verified against the shipped overlay on identical inputs, driven through
[`flm.MMPrebuilt`](../mm_prebuilt), which runs that xclbin unmodified:

| | err/mass | vs shipped |
|---|---|---|
| `rounding="floor"` | 0.009867 | **bit-identical, 6291456/6291456 elements** |
| `rounding="conv_even"` (default) | 0.000241 | differs everywhere |

All four epilogues are bit-identical to the shipped kernel too, with `floor`.
The shipped kernel selects its activation from a runtime parameter, one overlay
serving every projection; this operator bakes it in at compile time instead,
with the same 0/1/2/3 mapping, which is what lets its inner loop be branch-free:

| epilogue | vs shipped `output_mode` |
|---|---|
| `none` / `gelu` / `silu` / `sigmoid` | bit-identical, 1048576/1048576 each |

**The default is `conv_even`, not `floor`.** Truncation biases every conversion
the same direction, so the error accumulates over the K reduction instead of
cancelling: ~41x more error for no measured speed difference. Use `floor` only
to reproduce the original.

`clamp` has no counterpart in the shipped overlay to compare against — its
`generate_seq` never writes the clamp RTP words, so clamping is always off
there.

## Accuracy expectations

**Accuracy is architecture-dependent**, because the same 8x8x8 mmul lowers
differently: NPU2 uses two bfp16-emulated macs, which drop mantissa bits, while
NPU1 uses four native 4x8x4 bf16 macs, which do not. See
[Architectures](#architectures). `test.py` sets the budget per architecture.

A pure elementwise *relative* tolerance is not meaningful here: with signed A
the K-term sum cancels by ~sqrt(K), so |C| is ~20x smaller than the accumulated
magnitude while the error tracks that magnitude, leaving near-zero outputs
relatively uncheckable. Bound the error against the accumulated mass instead,
as `test.py` does.

Reference points on NPU2, random signed A / non-negative B:

| | mean err / mass |
|---|---|
| `flm.GEMM` (default) | 0.000241 |
| `iron.operators.GEMM`, same mode (`emulate=True, prio_accuracy=True`) | 0.000241 |
| `iron.operators.GEMM`, bf16 accumulator (`prio_accuracy=False`) | 0.000445 |
| `iron.operators.GEMM`, exact r=4 path (`emulate=False`) | 0.00007 |

So on NPU2 this operator and `iron.operators.GEMM` in the same mode are
numerically **indistinguishable** — identical mean error, signed bias and
maximum, at both `tile_n` values. Same mmul shape, same emulation, same f32
accumulation, same rounding. Do not compare against `iron.operators.GEMM`'s own
test tolerances, though: those assert on its exact r=4 path, which this operator
does not offer.

## Choosing `tile_n`

`tile_n` defaults to `None`, which picks per shape and per device: on NPU2,
**128 when `K == 512`, otherwise 64**; on NPU1, **always 64**. Override only if
you have measured a reason to.

`n=64` gives the mmul `colA=8` rather than 4, halving accumulator traffic per
mac. `n=128` instead halves A fetches, because the grid then covers twice as
many columns of N per pass. Which wins depends on whether compute or data
movement is the critical path, and on NPU2 that turns on how much K there is
to reduce over -- with a single k iteration there is not enough compute to
hide the extra A traffic. Measured on NPU2 against the current design (rolled
mmul, resident B, ATB, bfp16 B), min of per-run medians over 6 rounds with the
two `tile_n` builds interleaved round-robin -- that box is bimodal ~6%, so
running all of one and then all of the other measures drift rather than design:

| M / K / N | k_iters | `tile_n=64` | `tile_n=128` |
|---|---|---|---|
| 1024 / 512 / 4096 | 1 | 514 us | **498 us** |
| 1024 / 1024 / 4096 | 2 | **591 us** | 931 us |
| 1024 / 1536 / 6144 | 3 | **1141 us** | 1960 us |
| 1024 / 2560 / 4096 | 5 | **1239 us** | 1940 us |
| 2048 / 2048 / 2048 | 4 | **915 us** | 1581 us |
| 256 / 4096 / 1024 | 8 | **227 us** | 265 us |

So `tile_n=128` wins only at `k_iters=1`, and by ~3%; at `k_iters>=2` it is
1.2-1.7x slower. Both follow from `tile_n=128` giving up resident B — its
`mt_b` is 128 KB, so `k_iters` copies do not fit the memtile — and the more k
there is to reduce over, the more that costs.

NPU1 never reaches that crossover. It has half the columns *and* a quarter of
the per-tile bf16 mac throughput, so it stays compute-bound at every K, and
`n=128` also costs it a much larger f32 accumulator. `n=64` wins at every
`k_iters`, by a wide margin. Measured on Phoenix, min of 8 interleaved rounds
of 20 dispatches:

| M / K / N | k_iters | `tile_n=64` | `tile_n=128` |
|---|---|---|---|
| 512 / 512 / 1024 | 1 | **414 us** | 603 us |
| 512 / 1024 / 1024 | 2 | **618 us** | 1119 us |
| 512 / 1536 / 1536 | 3 | **1503 us** | 2066 us |

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

Unlike NPU2, compute here is **not** hidden behind the transfers — an earlier
split of wall time put it at roughly 40%, with a ceiling near 1.65x if compute
were free. So on NPU1 both a faster mmul and less traffic pay off, where on
NPU2 only the latter does.

That split was measured on the previous L1 configuration and has not been
re-measured since; treat the 40% as indicative. It also cannot be reproduced as
written, because it relied on an ablation that nulled the mmul, and that knob
has been removed from the operator.

### Measured dead ends on NPU1

Recorded so they are not retried. Both were plausible and both lost:

* **Resident B does nothing here.** Measured off-versus-on at M=2048, the shape
  where NPU2 gains 7.8%: 1259/1269 us against 1262/1268 (min/median) at K=512,
  and 2238/2248 against 2221/2229 at K=1024 -- i.e. at best a no-op, marginally
  negative at K=1024, against a 1.4-4.4% round spread. The `repeat_count`
  BD-chain restart noted under [Resident B](#resident-b) eats ~77% of the win on
  NPU2; on NPU1 it appears to eat all of it. Making B resident
  *single*-buffered to reach K=2560 is worse
  still, 5-12%, because it gives up the next column-block's prefetch.
* **The native 4x8x4 mmul shape is 22-30% slower.** See `register_tiling` in
  `design.py`. Composing 8x8x8 out of native macs costs 2.5 `vshuffle` per
  `vmac` and 4x8x4 costs zero, but removing every shuffle made it slower: the
  kernel is load-port bound, not shuffle bound, and the narrower shape needs 53%
  more loads per unit work because the 2x2 register block amortizes each load
  over a quarter as much arithmetic.

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

### Resident B

Where a whole column-block's B fits in the memtile double-buffered
(`k_iters <= 2`, i.e. K <= 1024 at `tile_n=64`) it is held there and replayed
per row-block, so DDR reads it once instead of `m_row_blocks` times -- about
43% less traffic. Larger K falls back to re-reading it, unchanged.

On NPU2 this is a latency win as well as a power one, because there the
operator is close to DDR-bandwidth bound; it grows with the height of the
problem, since B's re-reads scale with `m_row_blocks`. On NPU1 it is neither —
see [the dead ends above](#measured-dead-ends-on-npu1). At K=1024 N=4096 on
NPU2:

| M | row-blocks | non-resident | resident | |
|---|---|---|---|---|
| 512 | 2 | 470.8 us | 468.5 us | 0.5% |
| 1024 | 4 | 860.4 us | 846.5 us | 1.6% |
| 2048 | 8 | 1760.1 us | **1622.8 us** | 7.8% |

Do not evaluate this at small M: at M=512 the effect is inside the noise.

Most of the available win is still on the table. With the mmul nulled, the
non-resident floor at M=2048 is 1739 us -- 118 MB at 68 GB/s, against a
memcpy-measured 63-70 GB/s roof for mixed read/write traffic -- and residency
drops that floor to 1135 us. Only 137 us of those 604 us reaches the full
build; the rest goes to `repeat_count` restarting the memtile BD chain at every
replay boundary. Closing that is the largest known remaining lever here.
