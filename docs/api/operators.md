<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Operators

The operator library. Each operator is constructed by keyword
(`GEMV(M=..., K=...)`); outside a graph, `op(*tensors)` compiles once and
runs on the NPU, and inside a graph's `body()` calling it records a step.
`iron.operators.CATALOG` holds every operator by the name a profile gives it.

::: iron.operators
    options:
      show_root_heading: false

## FastFlowLM ports

Catalogued as `"flm.<name>"`. `flm.ProjectionGEMM` is not
`iron.operators.GEMM`.

::: iron.operators.flm
    options:
      show_root_heading: false
