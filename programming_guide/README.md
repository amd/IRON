<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# IRON Programming Guide

This guide teaches `iron`, the operator and graph layer on top of
mlir-aie's `aie.iron`. You will declare an operator, record a graph of
operators, compile it, and run it on an NPU.

> **New to the NPU itself?** This guide assumes you know what a Worker, an
> ObjectFifo and `@iron.jit` are. If not, start with mlir-aie's
> [programming guide](https://github.com/Xilinx/mlir-aie/tree/main/programming_guide).
> IRON's operators are built from exactly those pieces.

## The mental model

* An **operator** (`iron.operators.GEMM`, `ReLU`, `MHA`, ...) is a declared
  class. Its shape and tunables are `param()` and `tunable()` fields, and
  its compute is a `build()` over `aie.iron`. Called on its own,
  `op(*tensors)` compiles once and runs on the device.
* A **graph** is a subclass of `iron.Graph` whose `body()` method records a
  model's operators, once per input shape. The positional parameters of
  `body()` are the graph's inputs and its return value is the output.
  Inside `body()`, `Op.step(...)` records a step and returns a `Handle` in
  place of a tensor.
* `graph.compile(**shapes)` lowers one recorded shape to an image for the
  device: one full ELF on NPU2, an xclbin per step on NPU1.
  `graph(*tensors)` calls the compiled version that matches the inputs'
  shapes. Compile every shape you need before the first call: once a
  version is loaded, a call with a new shape raises instead of compiling.
* `graph.reference(*tensors)` runs the same `body()` on the host through
  each operator's numpy `reference()`, so you can check a design without
  an NPU.

```python
import numpy as np

import iron
from iron import Scratchpad
from iron.operators import GEMM, SiLU


class FeedForward(iron.Graph):
    """(SiLU(x @ w_gate.T) * (x @ w_up.T)) @ w_down.T, the first n rows of x."""

    def __init__(self, w_gate, w_up, w_down):
        self.w_gate, self.w_up, self.w_down = map(iron.param, (w_gate, w_up, w_down))

    def body(self, x, *, n: Scratchpad[np.int32]):
        gate = GEMM.step(x[:n], self.w_gate, b_col_maj=True)
        up = GEMM.step(x[:n], self.w_up, b_col_maj=True)
        return GEMM.step(SiLU.step(gate) * up, self.w_down, b_col_maj=True)


ffn = FeedForward(w_gate, w_up, w_down)
ffn.compile(x=(256, hidden))     # one compile serves any n up to 256 rows
y = ffn(x, n=37)                  # the device runs the first 37 rows
```

## Where to go next

| You want... | Read |
|---|---|
| The full guide, top to bottom | [Section 0](./section-0/) onward |
| An operator by itself, no graph | [Section 1](./section-1/) |
| Your first graph: `body`, handles, `.step`, `compile`, calling it | [Section 2](./section-2/) |
| One compile that serves any input extent | [Section 3](./section-3/) |
| Weights a graph holds, and state it keeps on the device | [Section 4](./section-4/) |
| A device loop that never comes back to the host | [Section 5](./section-5/) |
| Checking a design without an NPU | [Section 6](./section-6/) |
| Tunables, and a profile that sets them for a whole model | [Section 7](./section-7/) |
| From graphs to a language model (`iron.lm`) | [Section 8](./section-8/) |
| Several steps fused into one device configuration | [Section 9](./section-9/) |
| The rules a contributor or agent follows | [AGENTS.md](../AGENTS.md) |

## Sections

* [Section 0 — Getting started](./section-0/)
* [Section 1 — An operator on its own](./section-1/)
* [Section 2 — Your first graph](./section-2/)
* [Section 3 — Per-call values and bounds](./section-3/)
* [Section 4 — Weights and state](./section-4/)
* [Section 5 — Carried values and device loops](./section-5/)
* [Section 6 — The host reference and check mode](./section-6/)
* [Section 7 — Profiles and tunables](./section-7/)
* [Section 8 — From graphs to a language model](./section-8/)
* [Section 9 — Fusing steps on-chip](./section-9/)

-----
[Section 0 — Getting started →](./section-0/)
