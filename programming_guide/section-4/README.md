<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 4 - Weights and State

So far every tensor a graph's `body` saw came in through its call: `x`,
`y`. Two more kinds of tensor live in the graph itself, uploaded once and
reused every call, rather than passed in each time: **weights**, read-only
and fixed for the graph's life, and **state**, device-resident and read and
written by the graph's own steps, outliving any one call.

## Walkthrough of [weights_and_state.py](./weights_and_state.py)

### A weight

```python
class Scale(iron.Graph):
    """``x * weight``, elementwise, against a weight this graph holds."""

    def __init__(self, weight):
        self.weight = iron.param(weight)

    def body(self, x):
        return x * self.weight
```

`iron.param(array)` holds `array` as a weight of this graph: uploaded to the
device once, on the first compile, never again. Passed an already-known
array, as here, it is bound immediately; a model layer that loads weights
later (Section 8) instead declares `iron.param(shape)` and binds it with
`Graph.load_state_dict`. `x * self.weight` records an `ElementwiseMul` step
the same way `AXPY.step(...)` did in Section 2 — `*`, `+`, `-`, `/` and `@`
on a handle are shorthand for an operator's `.step(...)`, for the common
cases (see [`Handle`](../../iron/common/graph/handle.py)'s arithmetic
methods for which operator each reaches).

### State

```python
class Accumulate(iron.Graph):
    """A running total at row ``pos`` of a device-resident state: each call
    adds ``x`` into ``total[pos]`` and returns the new value."""

    def __init__(self, rows, width):
        self.total = iron.state((rows, width), name="total")

    def body(self, x, *, pos: Scratchpad[np.int32]):
        old = Copy.step(self.total[pos])
        new = x + old
        Copy.step(new, self.total[pos])
        return new
```

`iron.state(shape, dtype, name=)` declares a tensor that lives on the
device across calls, zero the first time it is uploaded — a KV cache is the
model-layer example (Section 8); this one is a plain running total, `rows`
independent slots of `width` elements. `self.total[pos]` indexes it by the
per-call value `pos`, dropping that axis to give one row; `Copy.step(...)`
reads a state row into a fresh handle, and `Copy.step(value, view)` writes
one back into it, the same two-argument shape as any other write into a
view (Section 3's bounds, Section 5's carried values).

`accumulate(x, pos=0)` called twice adds into the same row both times:
state is not reset between calls the way a weight is never touched again,
and not supplied fresh by the host the way `x` is. `pos` can also move
between calls — `accumulate(x, pos=2)` touches a different row of the same
state, with no new compile.

## <u>Exercises</u>

1. Run `python3 weights_and_state.py`; it checks `Scale` against numpy, then
   calls `Accumulate` four times at three different `pos` values, checking
   each running total against a plain numpy accumulator.
2. Call `accumulate.reference(x, pos=0)` a few times and read
   `accumulate.total.host` after each: it mirrors state the way the host
   reference path sees it. On a real device, the equivalent read is
   `accumulate.compile(x=(width,)).read(accumulate.total)`.
3. Change `Accumulate.body` to subtract instead of add
   (`new = old - x`) and rerun; confirm the reference still matches, since
   `reference()` runs the exact same `body` on the host.

-----
[Prev](../section-3/) &middot; [Top](..) &middot; [Next](../section-5/)
