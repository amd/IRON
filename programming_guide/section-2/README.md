<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 2 - Your First Graph

Section 1 called one operator on its own. A real design usually chains
several: a normalization, a couple of projections, an activation. A
[`Graph`](../../iron/common/graph/compiled.py) records that chain once, so
the intermediate tensors between operators stay on the device instead of
round-tripping to the host between calls.

## Walkthrough of [first_graph.py](./first_graph.py)

```python
import iron
from iron.operators import AXPY, ReLU


class ReluThenAxpy(iron.Graph):
    """``scalar_factor * relu(x) + y``, two operators as one compiled image."""

    def __init__(self, scalar_factor=2.0):
        self.scalar_factor = scalar_factor

    def body(self, x, y):
        activated = ReLU.step(x)
        return AXPY.step(activated, y, scalar_factor=self.scalar_factor)
```

A graph is a subclass of `iron.Graph` whose `body` you write. Its positional
parameters (`x`, `y` here) are the graph's inputs; its return value is the
graph's output. `__init__` is plain Python — anything it does runs once, at
construction, not per call.

Inside `body`, `Op.step(...)` is how an operator joins the graph: it
**records** a step rather than running one, and gives back a `Handle` — a
stand-in for a tensor, remembering where it lives and what produced it.
`ReLU.step(x)` records a `ReLU` step reading `x`; the `activated` handle it
returns is what `AXPY.step(activated, y, ...)` reads next. Nothing has run
yet — `body` only runs once per input shape, when the graph is recorded
(Section 3 covers the one-compile-many-calls part of that).

`Op.step(...)` infers an operator's shape parameters (`AXPY`'s `size`, here)
from the handles it is given, the same way `GEMV.step(w, x)` reads `M` and
`K` off `w` and `x`'s shapes — you don't repeat a dimension the handles
already carry. A construction keyword an operator still needs (`AXPY`'s
`scalar_factor`) is passed to `.step(...)` same as to the class itself.

## Compiling and calling it

```python
graph = ReluThenAxpy(scalar_factor=2.0)
graph.compile(x=(2048,), y=(2048,))

result = graph(x, y)
```

`compile(**shapes)` runs `body` once on handles of the given shapes (this is
the *recording*), then lowers the recorded steps to an image for the current
device: one full ELF on NPU2, one xclbin per step on NPU1. The returned
`CompiledGraph` is also stored on `graph` itself, keyed by shape, so you
don't have to hold onto it: `graph(x, y)` finds the version whose shapes
match `x` and `y`'s and calls it. If no version is loaded yet, calling the
graph with an uncompiled shape compiles it on the spot and logs that it did.
Once any version is loaded, an uncompiled shape raises `ValueError` rather
than compiling automatically. **Compile every shape you'll need before the
first device call**: the versions share a scratch arena that a later compile
can grow — see [Section 4](../section-4/).

## Checking it against numpy

As with a single operator, `graph.reference(*tensors)` runs `body` on the
host, each step through its operator's own `reference()`; no NPU needed.
[The test](../../iron/tests/docs/test_programming_guide.py) uses it to check
the example device-free.

A device call is checked the same way Section 1 checked `AXPY` alone —
`aie.utils.verify.compare(result, reference, tolerance)` — but a graph's
`tolerance` is not one number invented for the whole chain: it is the
tolerance of whichever step actually rounds. `ReLU` is exact in bf16 (it only
selects `max(x, 0)`); `AXPY` is the one step with a kernel contract, so its
`tolerance()` is the whole chain's. `first_graph.py` reads it straight off
the compiled graph's own recording (`compiled.recording.steps`), rather than
reconstructing an `AXPY` by hand. A graph where more than one step rounds
needs a different approach — Section 6.

## <u>Exercises</u>

1. Run `python3 first_graph.py` on an attached NPU; you should see `PASS!`.
2. Add a third operator to the chain (for example another `AXPY.step` adding
   a third input `z`) and extend `body`'s signature and `main()`'s tensors
   to match. One compile still serves one call to the whole chain.
3. `print(graph.record(x=(2048,), y=(2048,)))` — a `Recording` — and inspect
   its `.steps`: each is one recorded operator instance and the handles it
   reads and writes. This is what `compile` calls internally before lowering
   to an image.
4. Read `op.resolved().tolerance()` for `ReLU` on its own (as Section 1 did
   for `AXPY`) and confirm it really is `Tolerance.exact()` — no `rtol`,
   `atol` or `ulps` set.

-----
[Prev](../section-1/) &middot; [Top](..) &middot; [Next](../section-3/)
