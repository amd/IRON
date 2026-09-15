<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.DequantBFP` — q4nx weights to `flm.GEMM`'s packed B

```python
from iron.operators.flm import DequantBFP

op = DequantBFP(K=2048, N=2048, context=ctx)
op.compile()
op.get_callable()(q4nx_blob, packed_b)
```

Dequantizes 4-bit weights straight into the bfp16ebs8 layout
[`flm.GEMM`](../gemm) reads, so the runtime neither dequantizes to bf16 first
nor packs B on the host.

The output is **byte-identical to `GEMM.pack_B`** under `Rounding.FLOOR`, which
is the mode the cores run in. `test.py` asserts that against `pack_B` itself,
not against a private reference.

## What it replaces

FastFlowLM's shipped pipeline runs `dequant.xclbin` to produce bf16 in the order
its `mm` overlay wants, then multiplies. Swapping in `flm.GEMM` needs B in a
different format *and* a different blocking:

| | shipped `dequant` + `mm` | this operator + `flm.GEMM` |
|---|---|---|
| B element | bf16, 2 bytes | bfp16ebs8, 9 bytes per 8 values |
| `n` tile | 128 | 64 |
| k slice per compute tile | 512 | 128 |
| within an 8x8 tile | `n` contiguous | **`k` contiguous** |

The last row is the one that costs work. The 8 values sharing a bfp16 exponent
must be 8 consecutive `k` for one `n`, and the file stores the opposite — one
byte holds two `n` at the same `k`.

## One xclbin for every shape

Nothing in the device configuration depends on K or N. Every buffer descriptor
comes from the q4nx block geometry and the GEMM tiling constants, and the cores
loop forever over identical per-block work:

```python
for _ in range_(sys.maxsize):
    qw = qw_in.acquire(1)
    out = out_of.acquire(1)
    k(qw, out)
```

The shim sequence bounds the real work. A core parks on an empty input fifo
once that sequence has delivered its last block, so a column with no work in a
dispatch simply idles.

This is what makes the operator usable in a model. A shape-keyed xclbin would
take one hardware context per weight shape — ten for Gemma4 E2B, against a
budget of 16 — and pay a reconfiguration per projection. Instead `config_name`
keys the xclbin on `tile_n` and the device while `name` keys the instruction
stream on the shape. A clean build of the test suite produces **one xclbin and
seven instruction streams**.

A compile-time trip count would have put K and N in the core program. Making it
a runtime parameter would have fixed that, but needs a barrier and a re-read per
dispatch; a core that does the same thing every iteration needs neither.
`test_one_xclbin_serves_every_shape` pins this, and includes a shape that leaves
three of eight columns idle — the case a compile-time trip count cannot express
at all, since a core that never acquires fails lowering.

## Where each reorder happens, and why it has to

A DMA addresses memory in 4-byte units. A bfp16 block is 9 bytes, and 9 is
coprime with 4, so a single block is not addressable at all; the smallest unit a
descriptor can move is a whole 8x8 tile, at 72 bytes. That splits the work:

* **The core** does everything inside a tile: the nibble unpack, `min + scale *
  quant`, the 8x8 transpose, and the conversion. The transpose has to precede
  the conversion, because the conversion fuses 8 values under one exponent and
  no permutation of them survives it.
* **The drain** does everything coarser. Every stride above a tile is a multiple
  of 72 bytes, so one buffer descriptor covers it.

Two hardware limits shape that descriptor, and each rules out the other's
workaround:

* A shim BD carries three access dimensions plus a hardware repeat. Unpicking a
  whole 64x512 output tile needs four before anything else.
* The BD's size field counts **4-byte granules, not elements**, and stops at
  1023. The core's natural run is 512 blocks = 4608 bytes = 1152 granules, so it
  has to be split, which costs a dimension.

So a column joins its four cores into **two** memtile objects, one per k-half of
the tile. The half rides in the offset, which pays for the split. See
`DRAIN_DIMS`.

## Input layout

`qw_layout` selects how the q4nx blocks are ordered in the buffer:

| | order | descriptor |
|---|---|---|
| `QwLayout.FILE` | the weights file: blocks row-major | 4-D gather |
| `QwLayout.ENGINE` | what FastFlowLM writes to DRAM, pairs of block-rows interleaved | linear read |

Both deliver the same blocks to the same cores in the same sequence, verified as
index arithmetic by `test_engine_order_matches_file_order`. So this changes the
shim descriptor and nothing else — not the cores, not the join, not
`DRAIN_DIMS`, and not the xclbin.

## Interleaved projections

FastFlowLM packs gate and up into one blob, 512 out-features of each in a 1024
period, so a projection's column blocks come in runs with a gap:

```python
DequantBFP(K=1536, N=6144, qw_layout="engine",
           run_out_features=512, run_period_out_features=1024, ...)
```

The offset is computed per column block in Python and baked into the
instruction stream, so the gap costs no descriptor dimension. `quantized_size()`
spans the gaps, because the operator strides over them.

These parameters describe the stride pattern only, never a base offset. Point
the operator at the projection's own start — with a `Tensor.subview` on a
`proj_weights` buffer, for instance.

## Shape constraints

`K % 512 == 0` and `N % 64 == 0`. AIE2P only — `bfp16ebs8` does not exist on
AIE2.

**`K == 512` is rejected.** `flm.GEMM` picks `tile_n = 128` when K has a single
k iteration, and at that tile an output tile spans 128 out-features, so it takes
eight q4nx blocks where a column has four cores. Emitting the `tile_n = 64`
order anyway would produce a buffer of the right size that the GEMM reads
wrongly, with nothing raising, so `__post_init__` refuses instead.

`N` does not have to fill the grid. A column block count below `N_TILE * COLS`
narrows the grid rather than idling part of it, because an objectfifo whose
consumer never acquires fails lowering.

## Input format

The q4nx blob, as the weights file stores it. Blocks of 32 out-features by 256
in-features, row-major, 5120 bytes each:

| Run | Bytes | Contents |
|---|---|---|
| scales | 512 | 8 groups x 32 out-features, bf16 |
| mins | 512 | same shape |
| codes | 4096 | 8192 4-bit codes |

A scale group spans 32 consecutive in-features for **one** out-feature. The min
is **added**, not subtracted — it is an offset, despite the zero-point name the
shipped kernel gives its buffer.

The grouping nests cleanly: 8 divides 32, so every bfp16 block lies inside one
scale group and the kernel reads exactly one scale and one min per block.

## Rounding

Two conversions, both in the AIE's power-up `floor` mode, because nothing in the
kernel calls `set_rounding`:

1. f32 accumulator to bf16, rounding toward negative infinity.
2. bf16 to bfp16ebs8, truncating onto the block's shared exponent.

`reference.py` reproduces both exactly, which is what lets the tests compare
bytes. Rounding toward zero instead of negative infinity differs on every
inexact negative — about 11% of a real weight tensor — so a tolerance-based test
would pass while the bytes diverged.

## Validation

| Check | Where |
|---|---|
| descriptors reproduce `pack_b`'s ordering, in index arithmetic | [`iron/tests/operators/flm_dequant_layout.py`](../../../tests/operators/flm_dequant_layout.py) |
| device output equals the CPU reference, byte for byte | `test.py::test_matches_reference` |
| device output equals `GEMM.pack_B`, byte for byte | `test.py::test_output_feeds_gemm_unchanged` |

The layout tests exist because a wrong stride is otherwise silent: it produces a
buffer of the right size, full of real weight values, in the wrong order.

`reference.py` was also checked against FastFlowLM_IRON's sidecar generator
(`tools/replace-gemm/sidecar.py`), which had itself been validated byte for byte
against the shipped `dequant.xclbin`. They agree exactly at K/N of
1024x128, 2048x256, 1536x640 and 2048x2048. That check cannot live here, since
it needs the other repository.
