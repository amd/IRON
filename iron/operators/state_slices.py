# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What SelectiveScan and GatedDeltaRule share: a head's state taken
``SLICE`` at a time, a block of rows a kernel call, and the cores resolved
over whole heads.
"""

from iron.common import Unresolvable

#: The rows (SelectiveScan) or columns (GatedDeltaRule) of a head's state a
#: kernel call carries.
SLICE = 16


def block_rows(op) -> int:
    """The rows a kernel call takes: the most up to 32 that divide
    ``op.rows``, a bound on the block buffer's share of a core's memory.
    """
    return max(d for d in range(1, 33) if op.rows % d == 0)


def resolve_rows(op, dev):
    """Return ``op`` with its ``block`` set.

    ``block`` is the most rows, up to ``block_rows``, that divide
    ``op.rows`` and leave room in a core for ``op.held`` plus one slice's
    state and final state.

    Raises:
        Unresolvable: Not even one row fits.
    """
    if op.block is not None:
        return op
    state, final = op.slice_bytes()
    mem = dev.core_memory_bytes
    rows = next(
        (
            t
            for t in range(block_rows(op), 0, -1)
            if op.rows % t == 0 and op.held(dev, t) + state + final <= mem
        ),
        None,
    )
    if rows is None:
        raise Unresolvable(
            f"{type(op).__name__}: no block of rows fits a core's {mem} bytes"
        )
    return op.replace(block=rows * SLICE)


def depths(op) -> tuple[int, int]:
    """How many slices' states and finals ``op``'s core holds at once: two
    of each, the next streaming during the kernel, where its memory fits.
    """
    held = op.held(op.dev, op.block // SLICE)
    state, final = op.slice_bytes()
    mem = op.dev.core_memory_bytes
    deep_in = 2 if held + 2 * state + final <= mem else 1
    deep_out = 2 if held + deep_in * state + 2 * final <= mem else 1
    return deep_in, deep_out


def resolve_heads(op, dev, heads: int):
    """``op`` on as many cores as divide its ``heads`` and the shim's input
    channels feed.

    Raises:
        Unresolvable: No count divides the heads.
    """
    columns = op.resolve_columns(dev, op.columns, fits=lambda c: heads % c == 0)
    if heads % columns:
        raise Unresolvable(f"{type(op).__name__}: {heads} heads over {columns} cores")
    return op.replace(columns=columns)
