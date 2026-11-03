<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Porting the decode layer to ObjectFifos

## Stack

| Repository | Branch / PR | Base | Purpose |
| --- | --- | --- | --- |
| MLIR-AIE | `main` at `b40bf79e249` | — | Includes [#3964](https://github.com/Xilinx/mlir-aie/pull/3964), the Python `ObjectFifoPool` API and manual pool endpoints (merged October 23, Mountain time). |
| MLIR-AIE | `objectfifo-out-of-order` at `9392ae95c15`, [#3949](https://github.com/Xilinx/mlir-aie/pull/3949) | `main` | Packet FIFOs sharing receive channels, shared shim sending channels, and core-issued DMA queue operations. |
| MLIR-AIE | `objectfifo-mm2s-sharing` at `3bc0c413ca6`, no PR | `objectfifo-out-of-order` | Core producers sharing a sending channel with `release_strategy="push_queue"`. |
| MLIR-AIE | `flm-decode-lock-move` at `846919d3b44`, [#3912](https://github.com/Xilinx/mlir-aie/pull/3912) | `objectfifo-mm2s-sharing` | Decode kernels and factories; the combined stack used to build this design. |
| IRON | `fastflowlm-explicit-compile`, [#261](https://github.com/amd/IRON/pull/261) | `devel` at `d59559f9c` | Current operator/model integration, including the rewritten decode design. |
| IRON | `flm-decode-lock-move`, [#242](https://github.com/amd/IRON/pull/242) | `fastflowlm-explicit-compile` | Worker control flow, ObjectFifo streams, and partial pools for the decode layer. |

The compiler remains at the rebased stack above. This follow-up changes IRON,
compute kernels and their factories/tests; it makes no compiler changes.
The source install is `/scratch/roesti/mlir-aie-decode-port/install`.

## Current design

Workers own every decode kernel's loops, dispatch branches and synchronization.
The kernels no longer take numeric lock IDs or keep static ping/pong flags.

- Projection weights use two ObjectFifos per group, each split into two
  core streams on its memtile. This replaces all four weight memtiles'
  hand-written DMA and lock chains.
- Projection inputs use a temporal `merge()` of RMS, global attention,
  sliding-window attention and GLU. Each producer sends 512-element objects;
  the merged FIFO broadcasts 256-element consumer objects to all 16 cores.
  RMS and attention emit their repeats in Worker loops. Attention's emitter
  also converts its interleaved head layout to the projection order.
- Each projection pair uses a shared-memory FIFO for the neighboring core's
  row block. The sending core assembles the two rows, then releases its
  output pool. There is one producer per output object and no parity-selected
  locks. This costs one 32-bf16 copy per output block.
- RMS has three compute entry points and retains its weights and residual
  scratch across them. Its final output reaches the PLI gate through a
  shared-memory FIFO.
- RMS and both RoPE weight inputs are ordinary packet FIFOs sharing one shim
  sending channel. RoPE sends K then V through one depth-two FIFO per layer
  kind, including the existing skip-KV branch.
- PLI embedding consumes one packed input object: per-layer embedding,
  normalization data, then the input row. The two host transfers complete
  that object. This replaces three manual pools and their three-BD receive
  chain without needing out-of-order receive descriptors.
- The PLI weight/output paths, KV-cache inputs, queries and attention scores
  remain ObjectFifos as before.

Attention finalization narrows and normalizes the accumulator in place. The
separate attention output buffer is gone, saving `2 * num_attn_heads * dh`
bytes on each KV core. The scores and handshake share the KV core's memory.
The attention pairs have row hints (QK row 2, KV row 3) to keep the current
greedy placer from stranding their neighbors; columns and the remaining
cores are placed automatically.

`decode_layout.h`, the unused kernel lock/address helpers, `PingPong`, empty
linkage stubs and the monolithic projection/RMS entry points were removed.
The obsolete kernel-lock test harness is replaced by a projection FIFO
handoff test with south, north and west memory neighbors. Kernel wrappers
that still supply independently tested numerical contracts remain.

## Remaining manual path

The projection-output gather still carries a destination packet header that
changes between QKV, output, up/gate and down projections. Two gather memtiles
assemble slices before the final gather forwards them to RMS, RoPE or GLU.
This path retains its DMA chains and packet routes. The producer and receiving
cores access it through `ObjectFifoPool` handles. RMS's first input also shares
that receiving chain with the host input.

A fixed cyclic `dispatch()` does not express this destination schedule: the
number of objects per destination depends on the layer's RTPs. Separating the
destinations into FIFOs would also require scheduling multiple outgoing FIFOs
on the gather memtiles. The stack's shared-MM2S queue support is for core
producers, so it does not supply that memtile scheduler. The new design avoids
this limitation for projection *inputs* with `merge()`, which accepts objects
in arrival order. It does not claim to solve it for projection *outputs*.

The former porting tiers are consequently resolved as follows:

| Tier | Result |
| --- | --- |
| T1/T2: kernel loops and RTP branches | In Workers; kernels have no locks. |
| T3: output repetition | Explicit Worker loops over FIFO objects. |
| T4: embedding receive-channel sharing | One packed FIFO replaces the three-stream chain. |
| T5: chained slice locks | Weight paths use `split()`; destination-bearing output gather remains manual. |
| T6: two-core shared output/parity | Shared-memory row FIFO, one packet producer. |
| T7: multiple projection-input producers | Temporal `merge()`; RMS's mixed host/gather input remains a manual pool. |

## Build and validation

Use one kernel compiler job and at most two general build jobs:

```bash
cd /scratch/roesti/mlir-aie-decode-port
source /home/androsti/setup_min_buildenv.sh
CMAKE_BUILD_PARALLEL_LEVEL=2 COMPILE_JOBS=2 LINK_JOBS=1 AIECC_JOBS=1 \
  ./utils/build-mlir-aie-from-wheels.sh ./my_install/mlir build install \
  /scratch/roesti/buildenv/lib/python3.12/site-packages/llvm-aie

cd /scratch/roesti/IRON
source /opt/xilinx/xrt/setup.sh
source /scratch/roesti/buildenv/bin/activate
source /scratch/roesti/mlir-aie-decode-port/utils/env_setup.sh \
  /scratch/roesti/mlir-aie-decode-port/install \
  /scratch/roesti/buildenv/lib/python3.12/site-packages/llvm-aie
unset MLIR_AIE_KERNEL_SOURCES
export AIECC_JOBS=1 CMAKE_BUILD_PARALLEL_LEVEL=2
export NPU_CACHE_HOME="$PWD/build/decode-stack-cache"
python -m pytest iron/operators/flm/layer/test.py -q
```


The full decode suite checks both geometries, all layer types, window boundaries,
deep contexts and alternating dispatches against the CPU reference. It also
checks that other cache rows and the unused output region remain untouched.
Captured-engine tests require `FLM_LAYER_CASES`.

Validation on NPU2 (Strix), using the stack above and Peano
`22.0.0.2026101201+83ba9ea9`:

- Full decode suite: **40 passed, 1 skipped** (captured engine data absent).
- Final source-install smoke checks: **2 passed**, one per geometry.
- Projection FIFO hardware regression: **3 passed** (south/north/west neighbors).
- Kernel contract and factory metadata suite: **5,646 passed, 276 skipped**.
- Changed Python files pass Black and Ruff; the IRON design passes Pyright.
  Changed C++ files pass clang-format, and changed IRON files pass REUSE.
  Whole-workspace REUSE still reports pre-existing untracked local agent files.

An isolated copy of the pre-change design and kernel sources was benchmarked
against this version with the same compiler and NPU. Each case uses E2B,
context length 700, two warmups and 25 timed dispatches. Both versions also
passed the CPU comparison and untouched-buffer checks on those inputs.

| Case | Before median | After median | Change |
| --- | ---: | ---: | ---: |
| Global | 767.5 us | 765.2 us | -0.3% |
| Sliding window | 633.2 us | 635.4 us | +0.3% |

These measurements show no material latency change for these two cases;
they do not establish a performance bound for every layer configuration.
Logs are in `build/decode-validation/port-*.log`.
