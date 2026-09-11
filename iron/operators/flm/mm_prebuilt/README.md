<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.MMPrebuilt` — FastFlowLM's shipped `mm` overlay

```python
from iron.operators.flm import MMPrebuilt

op = MMPrebuilt(M=1024, K=1536, N=6144, epilogue="silu", context=ctx)
op.compile()
op.get_callable()(A, op.pack_B(B), C_out)
```

Runs FastFlowLM's `mm.xclbin` **unmodified**. It exists so that
[`flm.GEMM`](../gemm), the IRON port of that overlay, can be measured against
what it was ported from, on identical inputs and through the same host path.
[`../gemm/benchmark.py`](../gemm/benchmark.py) does exactly that.

**NPU2 only** — the overlay is an 8-column NPU2 binary. Constructing it
elsewhere raises `NotImplementedError`.

## How it is obtained

The xclbin is not checked in. It is a `RemoteFileArtifact`: downloaded on demand
into the (gitignored) build directory and pinned by SHA-256 against an immutable
FastFlowLM commit, so the fetch is reproducible and a substituted file is
rejected.

Because this is the only thing in the tree that touches the network, the
benchmark that uses it is marked `extensive` and is not reached by the default
`-m "not extensive"` run.

## What this operator supplies

The overlay ships as a binary, so every core program, memtile buffer and
stream-switch route comes from the xclbin. This operator emits only the
host-side half of a dispatch:

* **The runtime parameters.** One overlay serves every projection in a model, so
  the shape, the activation and the clamp arrive as words in each core's data
  memory. A core blocks on a lock until the sequence releases it, so a dispatch
  that writes no parameters hangs.
* **The shim DMA transfers**, reproducing the overlay's fixed channel map.

## Differences from `flm.GEMM`

| | `flm.MMPrebuilt` | `flm.GEMM` |
|---|---|---|
| provenance | shipped binary, downloaded | built from source in this repo |
| devices | NPU2 only | NPU2 and NPU1 |
| `tile_n` | fixed at 128 | 64 or 128, chosen per shape and device |
| epilogue selected | at runtime, by parameter | at compile time |
| rounding | core power-up `floor` | `conv_even` by default |
| B | pre-packed bf16 | pre-packed, bfp16 on NPU2 |

The epilogue difference is the interesting one. Selecting at runtime means one
build serves every activation; baking it in, as `flm.GEMM` does, costs a build
per activation but leaves the inner loop branch-free. The rounding difference is
why `flm.GEMM` is ~41x more accurate by default — see
[the port's README](../gemm/README.md#matching-the-shipped-fastflowlm-overlay),
which also records that `flm.GEMM(rounding="floor")` reproduces this overlay bit
for bit.
