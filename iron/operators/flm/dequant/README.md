<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.DequantBFP`

Dequantizes q4nx weights into the bfp16ebs8 layout [`flm.GEMM`](../gemm) reads
as B, on the device.

```python
from iron.operators.flm import DequantBFP

op = DequantBFP(K=2048, N=2048, context=ctx)
op.compile()
op.get_callable()(q4nx_blob, packed_b)
```

`K` is the in-feature count and `N` the out-feature count, so the result is B
for a `(M, K) x (K, N)` GEMM. The output equals `GEMM.pack_B` byte for byte
under `Rounding.FLOOR`, the mode the cores run in.

## Input layout

Each layer holds a whole number of the layer below it.

| Layer | Unit | Holds | Values | Bytes |
|---|---|---|---|---|
| 1 | byte | 2 codes: one `k`, two adjacent `n` | 2 | 1 |
| 2 | slice | 8 bytes, stepping `n` by 2 | 16 | 8 |
| 3 | half | 256 slices, stepping `k` by 1 | 4096 | 2048 |
| 4 | codes | 2 halves, stepping `n` by 16 | 8192 | 4096 |
| 5 | block | 512 B scales, 512 B mins, then layer 4 | 8192 | 5120 |
| 6 | pair | 2 blocks, stepping `n` by 32 | 16384 | 10240 |
| 7 | object | 2 pairs, stepping `k` by 256 | 32768 | 20480 |
| 8 | column block | K/512 objects, stepping `k` by 512 | 64·K | 40·K |
| 9 | matrix | N/64 column blocks, stepping `n` by 64 | N·K | 5·N·K/8 |

A scale and a min cover 32 consecutive `k` for one `n`, so a block has 8 groups
over its 32 `n`. The reader computes `min + scale * code`: the min is an
offset, not a subtracted zero point.

Layers 6 to 9 are the operator's input contract. It reads them as one linear
sweep, so a layer 7 object is the four blocks one column's four cores take, in
the order they take them. Whoever fills the buffer owes this order; the
operator assumes it and validates nothing above layer 5.

## Output layout

| Layer | Unit | Holds | Values | Bytes |
|---|---|---|---|---|
| 1 | bfp16 block | 1 exponent byte, 8 mantissa bytes: 8 `k`, one `n` | 8 | 9 |
| 2 | tile | 8 blocks, stepping `n` by 1 | 64 | 72 |
| 3 | | 16 tiles, stepping `k` by 8 | 1024 | 1152 |
| 4 | | 4 of layer 3, stepping `n` by 8 | 4096 | 4608 |
| 5 | slab | 8 of layer 4: outer `k` step 128 (x4), inner `n` step 32 (x2) | 32768 | 36864 |
| 6 | column block | K/512 slabs, stepping `k` by 512 | 64·K | 72·K |
| 7 | matrix | N/64 column blocks, stepping `n` by 64 | N·K | 9·N·K/8 |

The two formats order the innermost pair in opposite directions: the input puts
`n` next to `n`, the output puts `k` next to `k`.

8 divides 32, so every bfp16 block lies inside one scale group and the kernel
reads one scale and one min per block.

## Where the work happens

A DMA addresses memory in 4-byte units and a bfp16 block is 9 bytes, so no
descriptor reaches inside layer 2. The core produces layers 1 and 2: it unpacks
the nibbles, applies `min + scale * code`, transposes the 8x8 tile, and converts.
The transpose precedes the conversion because the conversion fuses 8 values
under one exponent.

Layers 3 and up are multiples of 72 bytes, so one buffer descriptor covers
them. A shim BD has three access dimensions plus a repeat, and its size
field counts 4-byte granules with a ceiling of 1023. Layer 4 is 1152 granules,
so it splits in two and spends a dimension. A column therefore drains two
memtile objects per slab, one per k-half, and the half rides in the offset.

## One xclbin per configuration

No K or N reaches the device configuration: every descriptor comes from the
layout above, and the cores loop over identical per-block work. `config_name`
keys the xclbin on `tile_n` and the device; `name` keys the instruction stream
on the shape. A clean build of the test suite emits one xclbin and ten
instruction streams.

## Parameters

`run_out_features` and `run_period_out_features` describe a matrix interleaved
with another in one buffer. FastFlowLM packs gate and up at 512 out-features
each in a 1024 period:

```python
DequantBFP(K=1536, N=6144,
           run_out_features=512, run_period_out_features=1024, ...)
```

They describe the stride pattern, never a base offset. Point the operator at
the matrix's own start, with `Tensor.subview` on the containing buffer.
`quantized_size()` spans the gaps.

## Constraints

`K % 512 == 0`, `N % 64 == 0`, AIE2P only.

`K == 512` raises. `flm.GEMM` picks `tile_n = 128` at a single k iteration,
which packs B in a different order, and a mismatch there yields a buffer of the
right size that the GEMM reads wrongly.

## Rounding

The cores never call `set_rounding`, so both conversions run in the power-up
`floor` mode: f32 to bf16 rounds toward negative infinity, and bf16 to
bfp16ebs8 truncates onto the shared exponent. `reference.py` reproduces both,
so the tests compare bytes.

## Validation

| Check | Where |
|---|---|
| descriptors reproduce `pack_b`'s order | `iron/tests/operators/flm_dequant_layout.py` |
| device output equals the CPU reference | `test.py::test_matches_reference` |
| device output equals `GEMM.pack_B` | `test.py::test_output_feeds_gemm_unchanged` |

A wrong stride yields a buffer of the right size holding real weight values in
the wrong order. The layout tests therefore compare index arithmetic.
