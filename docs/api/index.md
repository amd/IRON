<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Python API

IRON's Python API, generated from its docstrings. It sits on mlir-aie's
`aie.iron`, whose own reference is on the
[MLIR-AIE site](https://xilinx.github.io/mlir-aie/dev/api/).

| Page | Module | What it holds |
|---|---|---|
| [Graphs](graph.md) | `iron` | `Graph`, its compiled form, and what a `body()` declares with |
| [Functional](functional.md) | `iron.functional` | functions for a graph's body, under `torch.nn.functional`'s names |
| [Operators](operators.md) | `iron.operators` | the operator library, and the FastFlowLM ports |
| [Writing an operator](operator.md) | `iron.common` | `Operator`, its operands and values, the elementwise templates |
| [Testing and tracing](testing.md) | `iron.common.testing` | how an operator declares its tests, and the device test harness |
| [Language models](lm.md) | `iron.lm` | what every language model shares |
| [Tuning](tune.md) | `iron.tune` | timing operator settings and writing profiles |
