<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Writing an operator

What an operator is declared with. The declaration itself (`param`,
`tunable`, `per_call`) is mlir-aie's, in `aie.utils.compile.jit`; the
[contributing guide](../contributing.md) walks through adding one.

## Declaration

::: iron.common.declare
    options:
      show_root_heading: false

## Elementwise templates

::: iron.common.elementwise
    options:
      show_root_heading: false

## Design and runtime sequence

::: iron.common.design
    options:
      show_root_heading: false
