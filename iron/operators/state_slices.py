# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What SelectiveScan and GatedDeltaRule share: a head's state taken
``SLICE`` at a time, a block of rows a kernel call, and the cores resolved
over whole heads within what a shim BD holds.
"""

import dataclasses

from iron.common import Unresolvable

#: The rows (SelectiveScan) or columns (GatedDeltaRule) of a head's state a
#: kernel call carries.
SLICE = 16
#: The times a shim BD repeats a run, and the most a BD dimension counts.
REPEATS, BD_SIZE = 64, 1023


def block_rows(op) -> int:
    """The rows a kernel call takes: the most up to 32 that divide
    ``op.rows``, a bound on the block buffer's share of a core's memory.
    """
    return max(d for d in range(1, 33) if op.rows % d == 0)


def resolve_heads(op, dev, heads: int, width: int):
    """``op`` on as many cores as divide its ``heads`` (each ``width``
    wide) and the shim's input channels feed.

    Raises:
        Unresolvable: No count divides the heads; a core's slices are more
            than a BD repeats its rows; or the rows are more than a BD
            dimension counts.
    """
    name = type(op).__name__
    columns = op.resolve_columns(dev, op.columns, fits=lambda c: heads % c == 0)
    if heads % columns:
        raise Unresolvable(f"{name}: {heads} heads over {columns} cores")
    slices = heads // columns * width // SLICE
    if slices > REPEATS:
        raise Unresolvable(
            f"{name}: {slices} slices a core, more than the {REPEATS} times a "
            "shim BD repeats the rows"
        )
    if op.rows > BD_SIZE:
        raise Unresolvable(
            f"{name}: {op.rows} rows, more than a BD dimension's {BD_SIZE}"
        )
    return dataclasses.replace(op, columns=columns)
