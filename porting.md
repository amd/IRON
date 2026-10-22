<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Porting the decode layer to ObjectFifos

## Already on ObjectFifo

- PLI weight streams: down, gate, up
- Layer output drain
- Up projection input, joined on the merge tile
- KV cache: four packet fifos, forwarded through the attention memtile
- q from RoPE to the qk cores
- Scores between qk and kv

## Open complications

One complication per tier. A kernel or path appears in every tier that affects it.

### T1 — The kernel owns a counted loop and its ping-pong

**Affects** 
- decode_proj_main.cc

Done for decode_glu.cc and decode_rope.cc.

**Complication** The loop and a static ping/pong toggle sit in C++, so the design cannot see the per-iteration acquire.

**Change** Hoist the loop into the Worker. One fifo handle replaces the ping and pong buffers. `_bf16_proj` already works this way.

rope and GLU now expose one entry point per iteration: `rope_q`, `rope_k`, `rope_v`, and `glu_chunk`, `glu_emit`. The design runs the loops and works the locks, and each ping-pong pair is a depth-2 `BufferPool` the core reaches through a handle, so `ROPE_LOCKS` and `GLU_LOCKS` are empty. Latency did not move: median 947.9 us before, 944.8 us after, over 25 dispatches each with a standard deviation near 17 us.

proj_main holds three toggles. x and w are this tier. y is T6, since parity picks the lock, so hoisting it needs that tier's answer. Splitting proj_main also means `y_acc` and `b_col_reduce_add` become design buffers, since the kernel declares them on its stack today.

**Compiler** None.

### T2 — An RTP picks between compile-time counts

**Affects** 
- decode_rms_residual.cc (release count)
- decode_proj_main.cc (which projections run)

Done for decode_glu.cc and decode_rope.cc.

**Complication** `SKIP_KV` and `IS_SWA` select between constants. Every count is `constexpr` in decode_layout.h; none is computed at run time.

**Change** `scf.if` in the Worker. Hoisting a loop forces its tier-2 branch with it, so glu and rope took theirs: the Worker reads the RTP word through `buffer[0]` and branches with `if_`/`else_`.

**Compiler** None.

### T3 — One object goes out N times

**Affects** 
- decode_rms_residual.cc (`y`), attention kv `o` output BD

**Complication** The core releases the consumer lock N times so one BD sends the same buffer N times. A fifo calls this `repeat_count` and fixes it at compile time.

**Change** `o` has a fixed N, so set `repeat_count`. rms picks N per dispatch: drive that edge from a raw `Lock`, or give `ObjectFifoCreateOp` a runtime `repeat_count`. AIEX takes a runtime repeat count already.

**Compiler** Optional.

### T4 — Several streams share one S2MM channel

**Affects** 
- the embedding's three inputs: `x0_per_layer`, `norm_w`, `x0`

**Complication** One channel, a three-BD cyclic chain, and arrival order is the only thing that routes each stream to its buffer. A fifo owns one object type and one rotation, so three fifos cannot share the channel.

**Change** Out-of-order fifos: each packet names its descriptor through `out_of_order_id`, and `bd_id_base` keeps the BD ranges disjoint. The shim sequence tags each transfer. This retires the `manual_fill` BufferPool.

**Compiler** Implemented on the sibling branch.

### T5 — Many channels into one object, with chained locks

**Affects** 
- proj weight memtile
- proj gather memtile (two tiles)
- proj x memtile

**Complication** Two to four S2MM channels write disjoint slices of one buffer pair, and up to four MM2S channels read disjoint slices out. The locks daisy-chain (`yp0 → yp1 → yp2 → yp3 → yc`), so each consumer starts the next and only the last returns the object.

**Change** `join` and `split` state the dataflow. The chained hand-off needs a lowering that reproduces it, or one lock pair per slice.

**Compiler** Needed for the chained form.

**Channel budget** The gather memtile holds 6/6 S2MM, the x memtile 6/6 MM2S. Sharing a channel through T4 frees channels here, but does not unblock the port.

### T6 — Parity picks which lock to use

**Affects** 
- decode_proj_main.cc

**Complication** The `y` lock identity follows ping/pong parity across four locks, and `send_x_output` switches between the local lock space and the tile below. A fifo models one producer/consumer pair.

**Change** Open.

**Compiler** Likely.

## Design sites waiting on the kernels

`_build_rms` and `_build_proj_core` call `ctx.locks(...)` with a pinned table, because each kernel names its lock ids as compile-time constants. Each site unblocks when T1, T2, T3 and T6 take the locks out of the matching kernel. `_build_rope` and `_build_glu` no longer pin anything.

## Runtime lock values

Core-side lock values are already dynamic end to end. `aie.use_lock` takes an i32 SSA operand, the core lowering passes it through, and Peano holds the count in a register (`acq #48, r0`) even for a constant. `Lock.acquire` and `Lock.release` take `int | ir.Value`. Only the BD descriptor path demands constants: two sites in AIETargetXAIEV2.cpp, two in AIERT.cpp.

`objectfifo.acquire` is the exception. Its count is the result arity, so it cannot take a runtime value, and nothing in this design asks for one.


