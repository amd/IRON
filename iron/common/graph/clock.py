# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A kernel's cycles a call on one core, traced on the NPU, as the dataflow analysis prices its actors."""

from __future__ import annotations

import tempfile
from pathlib import Path

from aie.iron.algorithms.kernel_design import KernelDesign
from aie.iron.kernel import ExternalFunction

# Calls a kernel is traced at: the fewest cycles of them is its figure.
KERNEL_CALLS = 4

# A traced run's buffer: mlir-aie's kernel checks size it so.
TRACE_SIZE = 16384
TRACE_BYTES_PER_INTERVAL = 512
TRACE_MAX_BYTES = 4 << 20

_traced: dict[str, int] = {}


def kernel_cycles(fn: ExternalFunction) -> int:
    """Return ``fn``'s fewest cycles a call on one core, ``KERNEL_CALLS`` calls traced in one run (mlir-aie's ``KernelDesign.cycles_per_call``).

    Kept per recipe for the process. The trace buffer doubles, up to
    ``TRACE_MAX_BYTES``, while the run fills it.

    Raises:
        ValueError: The trace holds no whole call, or fills its largest buffer.
        RuntimeError: The run fails.
    """
    if fn.recipe_key in _traced:
        return _traced[fn.recipe_key]
    harness = KernelDesign(fn, calls=KERNEL_CALLS)
    inputs = harness.sample_inputs()
    size = max(TRACE_SIZE, TRACE_BYTES_PER_INTERVAL * harness.traced_intervals())
    with tempfile.TemporaryDirectory() as scratch:
        while True:
            traced = harness.cycles_per_call(
                inputs, trace_size=size, workdir=Path(scratch) / fn.recipe_key
            )
            if not traced.truncated or size >= TRACE_MAX_BYTES:
                break
            size = min(2 * size, TRACE_MAX_BYTES)
    if traced.untimed or traced.truncated or not traced.kernel:
        raise ValueError(f"{fn.name} ({fn.recipe_key}) not traced: {traced}")
    _traced[fn.recipe_key] = min(traced.kernel)
    return _traced[fn.recipe_key]
