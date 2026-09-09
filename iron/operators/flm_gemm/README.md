<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# FLMGEMM — bf16 GEMM on a fixed 4x8 grid

A second GEMM design, ported from FastFlowLM's `mm` overlay. It is a different
dataflow from [`GEMM`](../gemm), not a retuning of it:

| | `GEMM` | `FLMGEMM` |
|---|---|---|
| geometry | parameterized tiles, 1–8 columns | fixed m=64 k=512, r/s/t 8/8/8, 4x8 grid; n selectable |
| A delivery | per column | broadcast along each compute row from 4 shim columns |
| C staging | full m x n tile in L1 | streamed out in 512-element chunks |
| C collection | per column | ObjectFifo `join` of 4 rows through the memtile |
| epilogue | separate `convert_copy` | fused f32→bf16 + activation + clamp |
| B layout | plain `(K, N)` | **pre-packed**, see below |

On NPU2 (aie2p) only: the r=8 mmul shape exists solely on the bfp16-emulated
path, and the grid needs all 8 columns.

## Shape constraints

`M % 256 == 0`, `K % 512 == 0`, `N % tile_n == 0` (so 64 by default).

N only has to tile to `tile_n`, not to the grid's `tile_n * 8` stride: a
trailing group of fewer than 8 column-blocks is handled by giving the columns
different trip counts. That matters in practice — a transformer's `o` and
`down` projections have N = model dim, which is essentially never a multiple
of the full stride.

## B must be pre-packed

```python
op = FLMGEMM(M=M, K=K, N=N, context=ctx)
op.compile().get_callable()(A, op.pack_B(B), C_out)
```

`pack_B` reorders a row-major `(K, N)` matrix into the order the memtile
expects — each `K_TILE x tile_n` tile as the odometer `(n//T, k%S, k//S, n%T)`,
outermost first — so each fill is one contiguous read.

This is deliberately the caller's job rather than something the fill
descriptor does. The same reorder *is* expressible as a strided descriptor
over an unpacked B, and that was the original implementation, but its
innermost run is then `T=8` bf16 = 16 bytes: each 128 KB transfer becomes 8192
scattered bursts. B is ~70% of the bytes a dispatch moves, so the whole
operator ran at ~10 GB/s instead of ~47, a 5.4x end-to-end penalty. Weights
are packed once and reused across dispatches, so the cost belongs at the
caller.

## Matching the shipped FastFlowLM overlay

`rounding="floor"` reproduces the shipped `mm.xclbin` **bit for bit**. The AIE
core powers up in `rounding_mode::floor` and the original kernel never calls
`set_rounding`, so that is the arithmetic it ships with.

```python
FLMGEMM(M=M, K=K, N=N, rounding="floor", context=ctx)   # matches shipped
FLMGEMM(M=M, K=K, N=N, context=ctx)                     # conv_even, default
```

Verified against FastFlowLM v1.0.4's
`xclbins/Gemma4-E2B-IT-NPU2/mm.xclbin`, driving it directly with the
instruction stream from that project's own TXN generator, on identical inputs:

| | err/mass | vs shipped |
|---|---|---|
| `rounding="floor"` | 0.009867 | **bit-identical, 6291456/6291456 elements** |
| `rounding="conv_even"` (default) | 0.000241 | differs everywhere |

All four epilogues are bit-identical to the shipped kernel too, with `floor`
(the shipped kernel selects its activation from RTP word 4; this operator
bakes it in at compile time, with the same 0/1/2/3 mapping):

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

The r=8 mmul exists only on the bfp16-emulated path, so the error budget is
that of an emulated GEMM. Do not compare against `GEMM`'s test tolerances,
which assert on the exact r=4 path (`emulate_bf16_mmul_with_bfp16=False`).

A pure elementwise *relative* tolerance is not meaningful here: with signed A
the K-term sum cancels by ~sqrt(K), so |C| is ~20x smaller than the
accumulated magnitude while the error tracks that magnitude, leaving
near-zero outputs relatively uncheckable. Bound the error against the
accumulated mass instead, as `test.py` does. Reference points on random
signed A / non-negative B:

| | mean err / mass |
|---|---|
| `FLMGEMM` (default) | 0.000241 |
| `GEMM`, same mode (`emulate=True, prio_accuracy=True`) | 0.000241 |
| `GEMM`, bf16 accumulator (`prio_accuracy=False`) | 0.000445 |
| `GEMM`, exact r=4 path (`emulate=False`) | 0.00007 |

This operator and `GEMM` in the same mode are numerically **indistinguishable**
-- identical mean error, signed bias and maximum, at both `tile_n` values.
Same mmul shape, same bfp16 emulation, same f32 accumulation, same rounding,
so there is no reason for them to differ and they do not. The only accuracy
difference worth knowing about is `conv_even` versus the shipped overlay's
`floor` (above).

## Choosing `tile_n`

`tile_n` defaults to `None`, which picks per shape: **128 when `K == 512`,
otherwise 64**. Override only if you have measured a reason to.

`n=64` gives the mmul `colA=8` rather than 4, halving accumulator traffic per
mac. `n=128` instead halves A fetches, because the grid then covers 1024
columns of N per pass rather than 512. Which wins depends on whether compute
or data movement is the critical path, and that turns on how much K there is
to reduce over -- with a single k iteration there is not enough compute to
hide the extra A traffic. Measured, minimum of 3 runs:

> **Stale:** the sweep below predates the re-rolled mmul and the widened
> residency gate, which together took 1024/1536/6144 from 1741 to 1434 us. The
> `tile_n` choice it justifies is unlikely to have changed sign (residency does
> not fit at `tile_n=128`, whose `mt_b` is 128 KB), but the absolute numbers
> are no longer right and it wants re-measuring.

| M / K / N | k_iters | `tile_n=64` | `tile_n=128` |
|---|---|---|---|
| 1024 / 512 / 4096 | 1 | 642 us | **589 us** |
| 1024 / 1024 / 4096 | 2 | **850 us** | 1034 us |
| 1024 / 1536 / 6144 | 3 | **1741 us** | 2178 us |
| 1024 / 2560 / 4096 | 5 | **1891 us** | 2371 us |
| 2048 / 2048 / 2048 | 4 | **1535 us** | 1924 us |
| 256 / 4096 / 1024 | 8 | **254 us** | 316 us |

`pack_B` is bound to the operator because the packing layout depends on
`tile_n`; call `op.pack_B(B)`, not `FLMGEMM.pack_B(B)`.

## Performance

M=1024 K=1536 N=6144, min of per-run medians across separate processes:

| | bytes moved | latency | DMA-only (compute nulled) |
|---|---|---|---|
| `FLMGEMM` (`tile_n=64`) | 47 MB | **1143 us** | -- |
| shipped `mm.xclbin` | 107 MB | 2175 us | -- |
| `GEMM` (`emulate=True, prio_accuracy=True`) | 126 MB | 3353 us | 3374 us |

**1.90x the shipped overlay.** Accuracy is err/mass 2.69e-04 against the
shipped overlay's 9.87e-03 -- 37x better -- but see the note below: it is
2.69e-04 rather than the 2.41e-04 this operator reached before B was stored
in bfp16, and that gap is a known open bug, not a fundamental cost. The 69 MB is with B resident in the memtile; the 126 MB figure
this table used to quote was the non-resident fallback. At 1252 us against a
1231 us data-movement floor, this operator is now essentially DMA-bound: the
mmul is finally cheap enough to hide, so further gains have to come from
moving fewer bytes.

Three changes compound to get there, and none of them works alone:

* **The mmul's inner loop is rolled**, not hand-unrolled. 2446 -> 1875 cycles
  per call.
* **`pack_B` emits the final consumption order**, so both B hops are linear
  descriptors instead of blocked ones. Worth nothing by itself -- it is what
  frees the descriptor dimensions the other two need.
* **Asymmetric tile buffering.** The A tile is 16 rows while the accumulator
  is 64 (`rho = 4`), which pays for a 128-deep k slice. That halves the
  accumulator traffic per mac and doubles the inner loop's trip count:
  3.67 -> 2.64 cycles per 8x8x8 mac.

**Measure this carefully.** Dispatch latency on this part is *bimodal*, with
modes about 6% apart, and both show up for every configuration. A batch that
lands wholly in one mode turns min-of-medians into a mode selector rather than
a measurement -- that is how a change later shown to do nothing at all first
produced a convincing 5% "win". Compare configurations **interleaved**
round-robin rather than one after the other, use at least 8 rounds each, and
believe a difference only when the min and the median agree on it.

Nulling the mmul out is what makes this legible. `GEMM` does not change at all
without it (3374 vs 3353 us), so it is entirely data-movement bound.

This operator is **not**. An earlier revision of this section read the small
gap between the nulled floor and the full time (1692 of 1741 us) as proof that
`tile_n=64` was data-movement bound, and concluded that "further gains come
from moving fewer bytes, not from a faster kernel". That was backwards. The
floor sat just *above* the mmul, hiding it; the operator was compute bound the
whole time, and every attempt to move fewer bytes duly measured as worth
nothing. Re-rolling the mmul's inner loop cut it 23% (2446 -> 1875 cycles per
call, HW trace) and only then did keeping B resident pay -- together 1741 ->
1434 us.

Two lessons worth keeping. When total latency is `max(compute, DMA)`, testing
levers **one at a time scores both as zero**: residency alone gained nothing
while the mmul was the wall, and the re-rolled mmul alone gained little while
the non-resident floor was. And a nulled-mmul floor close to the full time does
not by itself mean DMA-bound -- it equally means compute is hiding just
underneath. Compare against the *nulled floor*, not the full time, when judging
a data-movement change.

Its transfers are cheaper mostly because B arrives pre-packed: the contiguous
run per transfer is 128 KB for B and 1 KB for A, against 128 bytes on every
leg for `GEMM`, which reorders in the descriptor instead.

Two things dominate, and both are in the runtime sequence rather than the
kernel: B must be pre-packed (above), and each of A, B and C must go out as
**one transfer per column-block** rather than one per fifo object. A single
fill or drain may span many objects; issuing per object instead means a host
await per row-block, and a C await waits on the cores. Collapsing those is
also what makes overlapping column-blocks affordable — a block then costs 3
buffer descriptors on a shim tile instead of `1 + 2*k_iters`, so two can be in
flight without exhausting the 16 available.

### Resident B

Where a whole column-block's B fits in the memtile double-buffered
(`k_iters <= 2`, i.e. K <= 1024 at `tile_n=64`) it is held there and replayed
per row-block, so DDR reads it once instead of `m_row_blocks` times -- about
43% less traffic. Larger K falls back to re-reading it, unchanged.

This operator is DDR-bandwidth bound, so that is a latency win as well as a
power one, and it grows with the height of the problem because B's re-reads
scale with `m_row_blocks`. At K=1024 N=4096:

| M | row-blocks | non-resident | resident | |
|---|---|---|---|---|
| 512 | 2 | 470.8 us | 468.5 us | 0.5% |
| 1024 | 4 | 860.4 us | 846.5 us | 1.6% |
| 2048 | 8 | 1760.1 us | **1622.8 us** | 7.8% |

Do not evaluate this at small M: at M=512 the effect is inside the noise, which
is how it was first mistaken for a power-only optimisation.

Most of the available win is still on the table. With the mmul nulled, the
non-resident floor at M=2048 is 1739 us -- 118 MB at 68 GB/s, against a
memcpy-measured 63-70 GB/s roof for mixed read/write traffic -- and residency
drops that floor to 1135 us. Only 137 us of those 604 us reaches the full
build; the rest goes to `repeat_count` restarting the memtile BD chain at every
replay boundary. Closing that is the largest known remaining lever here.
