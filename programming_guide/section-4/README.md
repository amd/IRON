<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 4 - Weights and State

So far every tensor a graph's `body` used was passed in on the call (`x`,
`y`). A graph can also hold tensors of its own, which live on the device
and are not passed again:

* **Weights** are read-only and fixed for the graph's life.
* **State** is read and written by the graph's own steps, and keeps its
  contents from one call to the next.

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

`iron.param(array)` makes `array` a weight of this graph. It is copied to
the device once, on the first call (or earlier, if you call the compiled
graph's `load()`), and never again. A model whose weights are loaded later
(Section 8) declares it by shape instead, as in
`iron.param(out_features, in_features)`, and binds it with
`Graph.load_state_dict`.

`x * self.weight` records an `ElementwiseMul` step. Arithmetic on a handle
is shorthand for an operator's `.step(...)`: `+` and `*` reach the
elementwise add and multiply, `-` reaches `AXPY`, `/` divides by a number,
and `@` multiplies a single row by a matrix with `GEMV`. See
[`Handle`](../../iron/common/graph/handle.py) for the details.

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

`iron.state(shape, dtype, name=)` declares a tensor that stays on the
device across calls and starts at zero. A KV cache is the real-world
example (Section 8). This one is a running total: `rows` independent slots
of `width` elements each.

`self.total[pos]` indexes the state by the per-call value `pos`, which
selects one row. `Copy.step(view)` reads that row into a new handle, and
`Copy.step(value, view)` writes a handle back into it.

Calling `accumulate(x, pos=0)` twice adds into the same row both times,
because state is never reset between calls. Calling `accumulate(x, pos=2)`
works on a different row of the same state, with no new compile.

## <u>Exercises</u>

1. Run `python3 weights_and_state.py`. It checks `Scale` against numpy,
   then calls `Accumulate` four times at three different `pos` values and
   checks each running total against a numpy accumulator.
2. Call `accumulate.reference(x, pos=0)` a few times and print
   `accumulate.total.host` after each. That array is the state as the host
   reference sees it. On a device, read it with
   `accumulate.compile(x=(width,)).read(accumulate.total)`.
3. Change `Accumulate.body` to subtract instead of add
   (`new = old - x`) and rerun. The reference still matches, because
   `reference()` runs the same `body` on the host.

-----
[Prev](../section-3/) &middot; [Top](..) &middot; [Next](../section-5/)
