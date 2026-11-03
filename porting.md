<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Porting the decode layer to ObjectFifos

## State (2026-11-03)

The port spans these branches, in dependency order:

| Repository | Branch / PR | Base | Purpose |
| --- | --- | --- | --- |
| MLIR-AIE | `main` at `b40bf79e249` | — | Includes [#3964](https://github.com/Xilinx/mlir-aie/pull/3964), the Python `ObjectFifoPool` API and manual pool endpoints (merged October 23, Mountain time). |
| MLIR-AIE | `objectfifo-out-of-order` at `9392ae95c15`, [#3949](https://github.com/Xilinx/mlir-aie/pull/3949) | `main` | Packet FIFOs sharing receive channels, shared shim sending channels, and core-issued DMA queue operations. |
| MLIR-AIE | `objectfifo-mm2s-sharing` at `3bc0c413ca6`, no PR | `objectfifo-out-of-order` | Core producers sharing a sending channel with `release_strategy="push_queue"`. |
| MLIR-AIE | `flm-decode-lock-move` at `e179e5d1932`, [#3912](https://github.com/Xilinx/mlir-aie/pull/3912) | `objectfifo-mm2s-sharing` | Eleven decode kernel/factory commits; the combined stack used to build this design. |
| IRON | `fastflowlm-explicit-compile`, [#261](https://github.com/amd/IRON/pull/261) | `devel` at `d59559f9c` | Current operator/model integration, including the rewritten decode design. |
| IRON | `flm-decode-lock-move`, [#242](https://github.com/amd/IRON/pull/242) | `fastflowlm-explicit-compile` | Worker control flow, ObjectFifo streams, and partial pools for the decode layer. |

The channel-sharing branches already contained current `main`. End-to-end
validation exposed one missing case: explicit unplaced shim tiles were cloned
by runtime endpoints, and the placer counted their shared DMA channels more
than once. #3949 now preserves explicit typed shim tiles and counts a shared
channel once on the same logical tile, before its coordinates are known.
Python and placer regression tests cover this. The kernel
branch was rebased onto them, dropping its obsolete copies of the pool and
out-of-order implementations. The compiler branches contain no kernel changes;
the kernel branch adds only kernels, factories, and their test metadata.

The IRON port now keeps the integration branch's `_Array`, automatic tile and
channel placement, `LayerDims`/`LayerType`, and `DispatchTime` parameters. RTPs
are written through their `Buffer` objects, rather than pinned addresses. The
port uses `ObjectFifoPool` and `Transport.dma(packet=Packet(id=...))`, replacing
the old `BufferPool`, `packet=True`, and `packet_id=` spellings. FIFO endpoints
use `port=Port.dma(...)` instead of `channel=`. Runtime FIFO
handles are explicit `Runtime` arguments, so endpoint discovery sees them.

T1 covers `decode_glu.cc` and `decode_rope.cc`. The remaining tiers below still
describe work to do; this rebase does not move more paths onto ObjectFifos.
The decode currently needs #3949's shim channel sharing. It does not yet use
the core MM2S sharing of `objectfifo-mm2s-sharing`; that branch is included in
the compiler build for the planned T6 work.

Local worktrees are `/scratch/roesti/mlir-aie-out-of-order`,
`/scratch/roesti/mlir-aie-shared-mm2s`, `/scratch/roesti/mlir-aie-decode-port`,
and `/scratch/roesti/IRON`. Pre-rebase refs are saved under
`backup/2026-11-03/` in both repositories. The merged `objectfifo-manual-dma`
branch is historical and no longer needs to be stacked or rebased.

## Paths already on an ObjectFifo

- The PLI weight streams: down, gate and up
- The layer output
- The up projection input, joined on the merge tile
- The KV cache: four packet ObjectFifos through the attention memtile
- q, from the RoPE core to the qk cores
- The scores, from the qk core to the kv core

## Open complications

Each tier states one complication. A kernel or a path appears in every tier that affects it.

### T1 — A kernel owns a counted loop and its ping-pong pair

**Affects** 
- decode_proj_main.cc

**Done** 
- decode_glu.cc 
- decode_rope.cc

**Complication** The C++ kernel holds the loop and a static ping-pong flag. The kernel acquires and releases the buffers. The design therefore states no lock traffic for them.

**Change** Move the loop into the Worker. One ObjectFifo handle replaces the ping buffer and the pong buffer. `_bf16_proj` already takes this form.

rope and GLU expose one entry point per iteration: `rope_q`, `rope_k`, `rope_v`, `glu_chunk` and `glu_emit`. The Worker runs the loops. The Worker acquires and releases every lock. A depth-2 `ObjectFifoPool` replaces each ping-pong pair. The core reaches that pool through a handle. `ROPE_LOCKS` and `GLU_LOCKS` are therefore empty.

The median latency measures 947.9 us before this tier and 944.8 us after it, over 25 dispatches each, with a standard deviation near 17 us.

proj_main holds three flags. The x flag and the w flag belong to this tier. The y flag belongs to T6, because the ping-pong parity selects the lock. This tier also moves `y_acc` and `b_col_reduce_add` into design buffers. The kernel declares both on its stack.

**Compiler** None.

### T2 — An RTP selects between compile-time counts

**Affects** 
- decode_rms_residual.cc (the lock count)
- decode_proj_main.cc (the set of projections)

**Done** 
- decode_glu.cc 
- decode_rope.cc

**Complication** `SKIP_KV` and `IS_SWA` select between constants. decode_layout.h declares every count `constexpr`. The design computes none of them at run time.

**Change** Emit an `scf.if` in the Worker. The Worker takes this branch together with the loop of T1. The glu Worker and the rope Worker therefore already hold theirs. Each Worker reads the RTP word through `buffer[0]`. Each Worker branches with `if_` and `else_`.

**Compiler** None.

### T3 — One object leaves N times

**Affects** 
- decode_rms_residual.cc (`y`)
- the attention kv `o` output BD

**Complication** The core releases the consumer lock N times. One BD therefore sends the same buffer N times. An ObjectFifo states this count as `repeat_count` and fixes it at compile time.

**Change** `o` uses a fixed N. Set `repeat_count` for it. rms selects N per dispatch. Drive that edge from a raw `Lock`, or add a runtime `repeat_count` to `ObjectFifoCreateOp`. AIEX already takes a runtime repeat count.

**Compiler** Optional.

### T4 — Several streams share one S2MM channel

**Affects** 
- the embedding's three inputs: `x0_per_layer`, `norm_w`, `x0`

**Complication** One channel carries three streams through a three-BD cyclic chain. Arrival order alone routes each stream to its buffer. An ObjectFifo holds one object type and one rotation. Three ObjectFifos therefore cannot share the channel.

**Change** Use out-of-order ObjectFifos. `Transport.dma(packet=Packet(), out_of_order=True)` enables descriptor selection by the packet header. The lowering allocates the descriptors and out-of-order IDs; the shim sequence tags each transfer. Out-of-order ObjectFifos remove the `manual_fill` ObjectFifoPool.

**Compiler** The `objectfifo-out-of-order` branch implements this. mlir-aie `main` does not hold it.

### T5 — Several channels fill one object behind chained locks

**Affects** 
- proj weight memtile
- proj gather memtile (two tiles)
- proj x memtile

**Complication** Two to four S2MM channels write disjoint slices of one buffer pair. Up to four MM2S channels read disjoint slices. The locks form a chain: `yp0 → yp1 → yp2 → yp3 → yc`. Each consumer releases the lock of the next consumer. The last consumer returns the object.

**Change** `join` and `split` state this dataflow. The chain of locks needs a lowering that reproduces it. One lock pair per slice is the alternative.

**Compiler** Needed for the chain.

**Channel budget** The gather memtile uses 6 of 6 S2MM channels. The x memtile uses 6 of 6 MM2S channels. T4 frees channels here. T4 does not unblock this tier.

### T6 — Ping-pong parity selects the lock

**Affects** 
- decode_proj_main.cc

**Complication** Two cores fill one output object. The lower core writes the packet header and its row block at offset 16. The upper core writes its row block at offset 16+m, into the memory of the lower tile. No data crosses a stream between the two cores. A `join` moves data through DMAs. This path is therefore not a `join`.

The `y` lock identity follows the ping-pong parity across four locks. `send_x_output` selects between the lock space of the core's own tile and the lock space of the tile below. An ObjectFifo states one producer and one consumer.

**Change** Open.

A pool of two segments, one slice per core, fails. A BD block acquires at most one lock: `'aie.mem' op BD block must have at most one acquire UseLockOp`. One BD drains the object. That BD therefore cannot wait on one lock pair per slice. The design uses four locks for this reason. Both cores release one lock. The BD acquires that lock with value 2. One pair per buffer lets the two cores use different buffers. Per-slice locks need one BD per slice, which costs a channel. Two segments may instead share one lock pair and a count.

That attempt settled two points. Place the endpoint on the tile of the acting core: `verifyAccessPlacement` requires the two tiles to match. `ObjectFifoCoreEndpointOp::getAccessType` builds the subview type `memref<48xbf16, strided<[1]>>` for one segment. `ObjectFifoPoolHandle._memref_type` builds a plain memref.

A second route gives each core its own ObjectFifo over its own slice. Each ObjectFifo then needs its own BD, its own packet header, and a share of the MM2S channel. The `objectfifo-mm2s-sharing` branch supplies the last part. `release_strategy="push_queue"` has the core push the descriptor of each buffer it releases, so two ObjectFifos share one core MM2S channel. A hardware test covers two ObjectFifos on channel 0 of one tile. Two items remain for this route. Each slice carries its own packet header. The gather memtile receives two arrivals per object instead of one.

**Compiler** Likely.

### T7 — Several tiles fill one buffer in turn

**Affects** 
- proj x memtile (`x`, from rms, attn_kv, swa_attn_kv and glu)
- rms (`x`, from the shim and from the proj x memtile)

**Complication** Four tiles send `x` into one buffer pair on the proj x memtile. The memtile forwards `x` to the 16 projection cores. Each producer writes the whole object. One producer sends at a time.

T4 covers one producer and several object types on one channel. T5 covers several channels and one slice each. This tier covers neither.

An ObjectFifo states one producer tile and a list of consumer tiles. The consumer side therefore takes several tiles. The producer side takes one.

The switchbox merges the four streams. Four packet flows meet on one channel. Three of them carry packet id 0. The receiving BD writes each arrival into the rotation.

**Change** Let an ObjectFifo state several producer tiles. No check enforces the order of the producers. Each producer waits for the result of the previous phase. That order is a property of the schedule. The IR states no such property. Such an ObjectFifo is correct only while the producers do not overlap. An arbiter is the alternative.

**Compiler** Needed.

## Design sites that wait on the kernels

`_Array.rms` and `_Array.proj_core` call `self.locks(...)` with a pinned table, because each kernel states its lock ids as compile-time constants. T1, T2, T3 and T6 remove the locks from the matching kernel. Each site becomes free at that point. `_Array.rope` and `_Array.glu` pin no lock.

## Runtime lock values

A core-side lock value is dynamic along the whole path. `aie.use_lock` takes an i32 SSA operand. The core lowering passes that operand through. Peano holds the count in a register, `acq #48, r0`, even for a constant. `Lock.acquire` and `Lock.release` take `int | ir.Value`. Only the BD descriptor path requires a constant: two sites in AIETargetXAIEV2.cpp, two sites in AIERT.cpp.

`objectfifo.acquire` is the exception. Its count is the result arity. It therefore takes no runtime value. This design requires none.



## Build and validation

Build the entire MLIR-AIE stack from the kernel worktree, so the tools,
Python API, compiler library, factories, and kernel sources agree. Do not
combine a new `aie-opt` with an older Python compiler library.

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

The regression suite compares the layer output and new KV rows with the CPU
reference, checks that other KV rows and the remainder of the output buffer
are untouched, and alternates global and sliding-window layer dispatches.
It covers E2B/E4B, all four layer types, and context lengths before, at, and
after the sliding-window wrap. Captured engine dispatches additionally need
`FLM_LAYER_CASES`; none were configured for this run.

Validation on NPU2 (Strix), with MLIR-AIE `e179e5d1932` and Peano
`22.0.0.2026101201+83ba9ea9`:

- Complete decode suite: **40 passed, 1 skipped**, 179.66 seconds.
- Focused pool, transport, logical-shim, shared-send, and out-of-order compiler
  regressions: **18 passed**.
- Standalone hardware regressions: shared MM2S sending and out-of-order
  receiving both pass; receiving also passes with queue-space checks disabled.
- The modified decode design passes Black, Ruff, Pyright, and REUSE checks.
  The rebased kernel Python/C++ files also pass formatting and lint checks.
- The broader tracked-source Pyright run reports three unrelated diagnostics:
  missing optional `tokenizers`, `lm_server.py`'s optional model access, and
  `mha.py`'s `stream_dims` attribute. None is in the decode port.

Local logs are in `build/decode-validation/`.

The installed release wheel in `requirements.txt` does not contain these
unmerged changes. This port still requires the source build above until the
dependencies merge and a matching wheel is published.
