<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Graphs

A graph is a subclass of `iron.Graph` whose `body()` is recorded on handles,
once per input shape, and compiled to one image per shape. These are the
names `import iron` gives.

::: iron
    options:
      show_root_heading: false

## Handles

What a graph's `body()` reads and writes: each operator step returns one.

::: iron.common.graph.Handle
