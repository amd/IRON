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
