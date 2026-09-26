<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Length-free llama: one image for any prompt, any context

Branch `claude/iron-pr221-length-free`, off `claude/iron-pr221-api-simplify`
(`6f7cbb5`). The plan and its progress log; updated as steps land.

## The assumption this branch is built on

A scratchpad parameter can patch a DMA descriptor's **size** as well as its
address. Today mlir-aie's `aiex.scratchpad_parameter` has two kinds: `addr`
(the parameter offsets a BD's address, `offset_parameter=` on the DMA op)
and `core` (a core reads it). This branch assumes a third:

```
kind = size    the BD's wrap for one dimension is replaced per call from the
               scratchpad word; the host writes the element count.
```

with the upstream Python surface `Runtime.fill/drain(..., size_parameter=(dim,
param))`. Nothing here needs more than that. IRON reaches it through one
function, `Sequence._transfer`, so when the kind lands the change is one
keyword. Until then a length-free operator lowers device-free (the sequence
is planned and checked) and the toolchain tests that would compile one skip,
naming the missing kind.

## Why

`npu.py` compiles the prompt at `max_seq_len` rows and pads every prompt to
it, so a 100-token prompt runs 2048 rows of GEMM and 2048-squared of
attention. Decode moves both caches in full every token. Buckets fix the
first and cost an image per bucket; the user wants none. A per-call length
under full ELF, which is the only packaging that shares the caches between
the prompt and decode, fixes both.

## The vocabulary

Three additions to the operator model. Everything else is operators using
them.

**An extent that may be shorter per call.** An operator declares which of
its shape fields a graph may bound:

```python
class Elementwise(Operator):
    size: int = param()
    valid = Extent(size)                     # size, or fewer per call
    count = Value(np.int32, derive=lambda op: op.valid // (op.cores * op.tile_size))
```

`Extent(field)` is a value member. Unbound it reads as the field, so nothing
derived from it changes and no operator that declares one behaves
differently until a graph bounds it. A value derived from a bound extent is
per call: the host evaluates `derive` with the call's extent and writes the
word. So the trip count above becomes per call the moment `valid` does,
with no second declaration.

**A bound on a handle.** `x[:n]`, with `n` a `Scratchpad` graph parameter,
is the first `n` rows of `x`. The view carries the bound on its axis;
`reshape` and `transpose` carry it through when the axis survives whole
(`(n, H*D)` to `(n*H, D)` scales it by `H`, `(n, G, D).transpose(1, 0, 2)`
moves it to axis 1). An operator taking a bounded operand on the axis its
`Extent` field sizes binds the extent to `n`; on any other axis the call is
an error naming the operator. An operator's outputs sized by the same field
are bounded the same way, so `h = RMSNorm(x[:n], w)` bounds `h`, and a block
of operators is bounded by one slice at its top.

**A per-call size in a transfer.** `rt.fill(stream, access, size_by={dim:
value})` patches dimension `dim` of the descriptor from the value, which must
be a scratchpad-kind value (a `DispatchTime` regenerates the stream and needs
no patch; the error says so). `Access` gains nothing; the patch is a property
of the transfer.

## What each operator does with it

The derived sequence (elementwise, RoPE, Softmax, RMSNorm): with a bound
leading axis the split across lanes is **round-robin by tile** instead of
contiguous chunks. Lane `k` reads tiles `k, k + lanes, k + 2*lanes, ...`: a
fixed offset, a fixed stride, and one patched iteration count shared by every
lane. The contiguous split stays for an unbound extent, so today's
instruction streams and the pinned descriptor tests do not move.

GEMV: `M` bounded. A's tiles and C's rows round-robin over the columns the
same way; `tiles` is derived from the extent and becomes the per-call trip
count.

Copy: a bound on any axis of either view patches that axis of the
descriptors; the channel split is unchanged. The cache write
`Copy(k.reshape(n, G, D).transpose(1, 0, 2), keys[i][:, :n])` needs nothing
else.

Repeat: the cache prefix `keys[i][:, :c]` for decode; the bound lands on the
row axis of the `(G, L, D)` cache, the descriptor's chunk dimension.

GEMM and MHA: their A and Q patterns already use all four descriptor
dimensions, so no dimension is free to patch. They keep streaming `L` rows
and bound the **compute** instead: the row-block and Q-block counts derive
from the extent and are read by the cores per call, and a core past the
bound drains its objects without calling the kernel. DMA traffic stays
linear in `L`; the work, which is what dominates and is quadratic for MHA,
follows the prompt.

## The graph

```python
@iron.graph(names_from=W, profile=self.profile)
def forward(x, angles, *, rows: Scratchpad[np.int32], cache_offset: ..., vector_size: ..., last: ...):
    if prompt:
        x, angles = x[:rows], angles[:rows]   # bounds every operator below
    ...
```

`npu.py` passes `rows=prompt_rows(n)` for a prompt, `n` rounded up to what
MHA's pipelines take at once (512 rows at full length), and `rows=1` for a
decode step; the prompt version is traced at `max_seq_len` rows as today,
and `vector_size` stays the true length, which MHA masks to.

Decode reads the caches in full. The context GEMV's `K` is the cache length
and array-tier (the kernel's reduction), so the value side cannot shorten;
the key side alone could, but a chain shortened on one side and full on the
other has no faithful CPU mirror, since the reference computes on the
sliced arrays. So the per-token cost stays proportional to `max_seq_len`;
a context-proportional decode needs the reduction length made a per-call
word inside the GEMV kernel, which is a kernel change.

## Steps

Each ends at both suites compared with their baselines (identical failure
sets), pyright and ruff clean, and a Progress entry.

1. **Vocabulary.** `Extent`, bounds on handles and views, `size_by` on
   transfers with the one-site upstream contract, per-call evaluation of
   derived values, `explain()` naming what is bounded. Device-free tests for
   each rule.
2. **Derived sequence.** Round-robin split under a bound; the elementwise
   template, RMSNorm, RoPE and Softmax declare their extent. The lowering
   tests for a bounded operator skip with the contract's name.
3. **GEMV, Copy, Repeat.** Hand-written sequences take `size_by`.
4. **GEMM and MHA.** Compute bounds read by the cores; arrays drain past
   the bound.
5. **llama.** `x[:rows]` at the top of `forward`'s prompt branch; `npu.py`
   passes the length. The host-parity test checks a prompt shorter than
   the context against the CPU reference.

## Progress

- `5c6369e` Step 5, the llama graph. `forward` takes `rows`; a
  prompt is `x[:rows]` and `angles[:rows]` at the top of its branch, and
  that one slice bounds every operator of every block (the last row's
  copy, the final norm and the head run one row and are not); the cache
  writes take `keys[i][:, :rows]`, and MHA takes `s_q`/`s_kv` from
  `vector_size`, the true length, so the padding rows a call runs are
  masked as before. `npu.py` passes `rows=prompt_rows(n)`, `n` rounded up
  to MHA's pipeline rows, and `rows=1` for a decode step. A per-call index
  on a bounded axis (`x[last]`) drops the bound; a slice of it is refused.
  A value the graph binds itself is not also derived. The CPU reference
  runs the prompt at its rows, and a prompt of eight tokens in a context
  of 1024 matches the oracle at 512 rows, then decodes from the caches it
  wrote. Decode's cache prefix was tried and dropped: see The graph. The
  toolchain conftest turns the missing size kind into a skip for any
  build that reaches it, so the llama prompt's lowering and full-ELF
  tests skip there rather than fail. Both suites identical to baseline.
- `af9cf27` Step 4, GEMM and MHA bound their compute. Both stream
  every row as before (their A and Q patterns use all four descriptor
  dimensions) and say so with `extent_unit() == 0`, so no word of tiles per
  lane is made for them. GEMM's `valid = Extent(M)` derives
  `n_tiles_valid`, the whole row blocks the bound covers times the column
  tiles; under a bound each core computes that many tiles and passes the
  rest through, the same acquires and releases with no kernel call. MHA's
  `valid = Extent(seq_pad)` derives the Q blocks per pipeline and KV blocks
  per Q block the cores attend over (`q_blocks_valid`, `kv_blocks_valid`)
  and the mask lengths `s_q`/`s_kv` from the call's rows; each of the three
  cores attends over those and passes the rest of what the DMAs stream
  through, the PV core's first, middle and last blocks kept. The values a
  bounded build alone reads are optional residents, so an unbounded build
  is what it was. A bound reaches an operand through a `select()` shape by
  the branch the flag takes. Bounded GEMM and MHA use no size patch, so
  they lower through aiecc today: three more toolchain cases pass. Both
  suites identical to baseline.
- `9869c85` Step 3, the hand-written sequences. A `Walk` carries the
  axis a graph bounds; a copy's view operands put a bound on their walk
  and bind `src_valid`/`dst_valid`, and `Copy._taps` keeps a bounded walk
  as one exact descriptor per channel with that axis in its own slot,
  refusing a bound on the axis the channels split; the reference moves
  the bounded rows alone. Repeat bounds either its rows or a stack's
  middle axis, the context of a KV cache, in a slot of its own. GEMV
  bounds `M`: an operator names the round-robin unit per operand
  (`extent_unit`), so a column takes A in output tiles and its rows line
  up with C's, and the sequence issues both from the derived plan
  (`rt.plan`) after B; its trip count derives from the extent and the
  cores read it per call. Both suites identical to baseline.
- `b2b5b01` Step 2, the derived sequence under a bound. For each
  Extent and each operand its field sizes, the operator makes one word of
  tiles per lane (`valid_x`, `valid_y`), derived from the extent like any
  `Value`, so it is per call the moment the extent is and a build finds it
  among the values. `bounded_transfers` splits the bounded axis round-robin
  by tile: lane `k` takes tiles `k, k + lanes, ...` from a fixed offset with
  a fixed stride, the count in one descriptor slot that every lane patches
  with the same word; leading batch axes stay repeats, and a tile past one
  wrap takes the two inner slots as before. The derived sequence plans a
  bounded operand that way and the declared way otherwise, so unbounded
  instruction streams do not move. The elementwise templates, RMSNorm,
  Softmax and RoPE declare their extents (`valid = Extent(size)`, of
  `rows`, and RoPE's `valid_angles` too), their trip counts derive from
  them, and their arrays read a per-call count from the scratchpad where a
  graph bounds it and from the RTP otherwise. A bounded ReLU, RMSNorm,
  Softmax and RoPE build their arrays against the words and stop at the
  size patch with the contract's name, which the lowering test records as
  a skip. Both suites identical to baseline; eight skips more.
- `e5e84d9` Step 1, the vocabulary. `Extent(field)` is a value
  member that reads as its field until a graph bounds it; `x[:n]` puts a
  bound on a handle, carried through `reshape` (rescaled by the merged or
  split axes) and `transpose`, and refused on a slice of a bounded handle
  or a start past zero; the tracer binds a bound to the operator's Extent
  whose field sizes that axis, refuses one where no Extent does, and bounds
  the outputs the same field sizes, so one slice bounds a whole block. A
  `Value` whose derivation reads a bound extent is per call: the operator
  records the extents a derivation touches, `derived_at()` evaluates it at
  a call's bound, and the compiled graph writes one word per bound value
  and one per such derivation. `fill`/`drain` take `size_by={dim: word}`:
  on the dispatch path the scalar replaces the size; on a full ELF it asks
  the upstream handle for `size_parameters=` and, until mlir-aie has the
  size kind, raises naming the contract. `explain()` says what is bounded.
  Both suites identical to baseline; nine new tests.
