<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 3 - Per-Call Values and Bounds

Section 2's graph compiled for one fixed shape and ran it, over and over,
unchanged. A language model's decoder is not that regular: a prompt chunk
might run 1 row or 2048, and a `max_seq_len`-sized cache is read up to
wherever the conversation currently is, not its full length, every call.
As in Section 1, an operator's `param()` describes a fixed property of the
problem, such as the input size, while a `tunable()` describes a choice of
how to map the work onto the device, such as how many columns to use.
Both are fixed for a compiled image. A graph handles an extent that changes
between calls by declaring a **per-call value**, read on the device rather
than baked into the compiled image.

## Walkthrough of [bounded_graph.py](./bounded_graph.py)

```python
import iron
from iron import Scratchpad
from iron.operators import ReLU


class BoundedRelu(iron.Graph):
    """``relu(x[:n])``: one compile serves any ``n`` up to ``len(x)``."""

    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU.step(x[:n])
```

A keyword-only parameter of `body` annotated `Scratchpad[T]` is a per-call
value: not a tensor, a scalar the host writes into the image's scratchpad
before each call, and the device reads where the design needs it. `n` here
bounds how many leading elements of `x` the step actually touches —
`x[:n]` is IRON's spelling of "the first `n` rows of `x`, `n` given per
call" (the same slice the PR that introduced graphs used as its own
example: `GEMM.step(x[:n], w, b_col_maj=True)` in a GEMM-based graph).

Only this one slice form records a per-call bound: a plain Python slice like
`x[:16]` is a compile-time constant, baked into the image like any other
shape; `x[:n]` with `n` the body's own per-call parameter is what makes the
bound a per-call value. `Scratchpad[np.int32]` (not `np.float32`): a
per-call value is encoded into scratchpad bits a core reads as an integer,
so it cannot be floating point.

## Compiling once, calling at several extents

```python
graph = BoundedRelu()
graph.compile(x=(256,))

graph(x, n=16)
graph(x, n=128)
graph(x, n=256)
```

One `compile()` builds one image sized for `x`'s full shape; `n` is free to
change every call, with no second compile and no second image. This is the
"one array, every extent" rule the whole operator and graph layer is built
around:
`build()` only ever sees an operator's declared shape, so a decoder's
prompt-chunk version serves a 1-row call and a 2048-row one alike, bounded
by a per-call value rather than rebuilt per length.

A bound is checked before it reaches the device: a call with `n` larger than
the compiled shape, or an index that would read outside it, raises before
anything runs, the same way `Write: start + rows is 101, outside` is raised
in `iron/tests/common/test_graph.py` for a bound that overruns its buffer.

A device call's own output, though, is always the *compiled* shape, not
`n`'s: `graph(x, n=16)` returns an array of shape `(256,)`, only the first
16 elements of which this call wrote (the rest is whatever was in that
output buffer before — a previous call's values, or uninitialized, never
garbage past the device's allocation). `graph.reference(...)` is the one
that trims its result to `n` elements, which is what lets
[bounded_graph.py](./bounded_graph.py) compare `result[:n]` against it.
Read only as many rows of a device call's output as you bounded it to.
`bounded_graph.py` checks `result[:n]` against `reference` with
`aie.utils.verify.compare(..., relu.resolved().tolerance())`, `relu` read off
the compiled graph's one recorded step — `ReLU`'s own `Tolerance.exact()`,
the same one Section 2's exercises asked you to confirm, not an invented
number.

## <u>Exercises</u>

1. Run `python3 bounded_graph.py` on an attached NPU; it calls the same
   compiled graph at three values of `n` and checks each against numpy.
2. Call `graph(x, n=300)` (past the compiled size of 256) and read the
   error it raises.
3. Change `body` to bound two operators on the same `n`
   (`ReLU.step(x[:n])` then `AXPY.step(..., y[:n], scalar_factor=2.0)`, with
   a second input `y`) and confirm both still ride one compiled image.

-----
[Prev](../section-2/) &middot; [Top](..) &middot; [Next](../section-4/)
