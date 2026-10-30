<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 2 - Your First Graph

Section 1 called one operator on its own. A real design chains several: a
normalization, a few projections, an activation. A
[`Graph`](../../iron/common/graph/compiled.py) records that chain once, and
the tensors passed between its operators stay in device memory instead of
returning to the host between calls.

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

A graph is a subclass of `iron.Graph` with a `body` you write. The
positional parameters of `body` (`x` and `y`) are the graph's inputs, and
its return value is the graph's output. `__init__` is plain Python that runs
once, at construction.

Inside `body`, `Op.step(...)` adds an operator to the graph. It **records**
a step instead of running one and returns a `Handle`, a stand-in for the
tensor that step will produce. `ReLU.step(x)` records a `ReLU` reading `x`,
and `AXPY.step(activated, y, ...)` reads the handle it returned. Nothing
runs on the device yet: `body` runs once per input shape, when the graph is
recorded.

`Op.step(...)` infers an operator's shape parameters from the handles it is
given, so `AXPY`'s `size` comes from `activated`, just as `GEMV.step(w, x)`
reads `M` and `K` from its inputs. Other construction keywords, such as
`AXPY`'s `scalar_factor`, go to `.step(...)` as they would to the class.

## Compiling and calling it

```python
graph = ReluThenAxpy(scalar_factor=2.0)
graph.compile(x=(2048,), y=(2048,))

result = graph(x, y)
```

`compile(**shapes)` runs `body` on handles of those shapes (the
*recording*) and lowers the recorded steps to an image for the current
device: one full ELF on NPU2, an xclbin per step on NPU1. The graph keeps
the resulting `CompiledGraph`, keyed by input shapes, and `graph(x, y)`
calls the version that matches.

If no version is loaded yet, calling the graph with a new shape compiles it
on the spot. Once a version is loaded, a new shape raises `ValueError`.
**Compile every shape you need before the first call**: all versions share
one device buffer arena, and a later compile may have to grow it.

## Checking it against numpy

As with a single operator, `graph.reference(*tensors)` runs `body` on the
host, each step through its operator's `reference()`, with no NPU needed.
[The guide's tests](../../iron/tests/docs/test_programming_guide.py) use it
to check this example without a device.

A device call is checked with `aie.utils.verify.compare(result, reference,
tolerance)`, as in Section 1. Here only one step rounds: `ReLU` is exact in
bf16, so `AXPY`'s tolerance covers the whole chain. `first_graph.py` takes
the `AXPY` step from the compiled graph's recording
(`compiled.recording.steps`) and uses its `tolerance()`. Section 6 shows how
to check a graph where several steps round.

## <u>Exercises</u>

1. Run `python3 first_graph.py` on an NPU. You should see `PASS!`.
2. Add a third operator, for example another `AXPY.step` that adds a third
   input `z`, and extend `body`'s signature and `main()`'s tensors to
   match. One compile still covers the whole chain.
3. Print `graph.record(x=(2048,), y=(2048,))`, a `Recording`, and look at
   its `.steps`: each is one operator and the handles it reads and writes.
   `compile` builds this before lowering it to an image.
4. Print `ReLU`'s `op.resolved().tolerance()`, as Section 1 did for `AXPY`,
   and confirm it is `Tolerance.exact()`, with no `rtol`, `atol` or `ulps`.

-----
[Prev](../section-1/) &middot; [Top](..) &middot; [Next](../section-3/)
