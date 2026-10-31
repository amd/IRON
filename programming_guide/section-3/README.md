<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 3 - Per-Call Values and Bounds

Section 2's graph ran one fixed shape on every call. A language model needs
more than that: a prompt chunk may be 1 row or 2048, and a KV cache sized
for `max_seq_len` should only be read up to the current position.

An operator's `param()` and `tunable()` values (Section 1) are fixed once
the image is compiled. To let an extent change from call to call, a graph
declares a **per-call value**: a number the device reads at run time
instead of one baked into the image.

## Walkthrough of [bounded_graph.py](./bounded_graph.py)

```python
import numpy as np

import iron
from iron import Scratchpad
from iron.operators import ReLU


class BoundedRelu(iron.Graph):
    """``relu(x[:n])``: one compile serves any ``n`` up to ``len(x)``."""

    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU.step(x[:n])
```

A keyword-only parameter of `body` annotated `Scratchpad[T]` is a per-call
value. It is not a tensor. It is a scalar that the host writes into the
image's scratchpad before each call, and that the device reads when it
needs it. Here `x[:n]` means "the first `n` elements of `x`, with `n` given
on each call".

Only a slice by a per-call value is bounded per call. A plain slice like
`x[:16]` is a fixed shape, set at compile time like any other.

Per-call values must be integers. The scratchpad holds at most 30 bits per
value, so declaring one as `Scratchpad[np.float32]` raises a `TypeError`.

## Compiling once, calling at several extents

```python
graph = BoundedRelu()
graph.compile(x=(256,))

graph(x, n=16)
graph(x, n=128)
graph(x, n=256)
```

One `compile()` builds one image for `x`'s full shape. `n` can change on
every call without a second compile. The same idea runs through the whole
library: an operator's `build()` never sees the extent, so a decoder's
prompt-chunk version serves a 1-row call and a 2048-row call alike.

A bound is checked on the host before anything runs. Calling with `n`
larger than the compiled shape raises an `IndexError` that names the view
and its limits.

A device call always returns an array of the *compiled* shape:
`graph(x, n=16)` returns shape `(256,)`, and only the first 16 elements were
written by this call. `graph.reference(...)` trims its result to `n`
elements. That is why [bounded_graph.py](./bounded_graph.py) compares
`result[:n]` against the reference. Read only as many rows of a device
call's output as you bounded it to.

The example takes its tolerance from the compiled graph's one recorded
step, `relu.resolved().tolerance()`, and checks with
`aie.utils.verify.compare`. For `ReLU` that tolerance is exact.

## <u>Exercises</u>

1. Run `python3 bounded_graph.py` on an attached NPU. It calls the same
   compiled graph at three values of `n` and checks each against numpy.
2. Call `graph(x, n=300)`, past the compiled size of 256, and read the
   error it raises.
3. Change `body` to bound two operators on the same `n`
   (`ReLU.step(x[:n])` then `AXPY.step(..., y[:n], scalar_factor=2.0)`, with
   a second input `y`) and confirm both still run from one compiled image.

-----
[Prev](../section-2/) &middot; [Top](..) &middot; [Next](../section-4/)
