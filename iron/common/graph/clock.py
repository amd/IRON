# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A kernel's cycles a call on one core, traced on the NPU, as the dataflow analysis prices its actors."""

from __future__ import annotations

import math
import tempfile
from pathlib import Path

from aie.helpers.npdtypes import np_ndarray_type_get_shape
from aie.iron.algorithms.kernel_design import KernelDesign
from aie.iron.kernel import ExternalFunction

# Calls a kernel is traced at: the fewest cycles of them is its figure.
KERNEL_CALLS = 4

# A traced run's buffer: mlir-aie's kernel checks size it so.
TRACE_SIZE = 16384
TRACE_BYTES_PER_INTERVAL = 512
TRACE_MAX_BYTES = 4 << 20

_traced: dict[tuple[str, tuple], int] = {}


def kernel_cycles(fn: ExternalFunction, scalars: tuple = ()) -> int:
    """Return ``fn``'s fewest cycles a call on one core, its calls traced in one run (mlir-aie's ``KernelDesign.cycles_per_call``).

    ``KERNEL_CALLS`` calls, or as many as its contract says make its output:
    a kernel writing a slice of its output tile a call fills the tile, and
    one writing it on its last call runs its required calls. Kept per
    recipe and scalars for the process. The trace buffer doubles, up to
    ``TRACE_MAX_BYTES``, while the run fills it.

    Args:
        fn: The kernel.
        scalars: The scalar arguments its contract leaves unbound, in
            order, as its operator passes them (``Elementwise.scalars``).

    Raises:
        ValueError: The trace holds no whole call, or fills its largest buffer.
        RuntimeError: The run fails.
    """
    key = (fn.recipe_key, scalars)
    if key in _traced:
        return _traced[key]
    contract = fn.contract
    if contract.out_last:
        calls = contract.required_calls
    elif contract.out_offset is not None:
        tile = fn.arg_types()[contract.out_index]
        calls = math.prod(np_ndarray_type_get_shape(tile)) // contract.out_offset[1]
    else:
        calls = KERNEL_CALLS
    harness = KernelDesign(fn, calls=calls, scalars=scalars)
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
    _traced[key] = min(traced.kernel)
    return _traced[key]
