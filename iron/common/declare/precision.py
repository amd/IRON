# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How far an operator may round past its reference for speed."""

from enum import StrEnum


class Precision(StrEnum):
    """The roundings a matmul may make beyond its reference's, named as
    ``torch.set_float32_matmul_precision`` names its levels. Each level
    allows what the one above it does, and more:

    - ``HIGHEST``: f32 partial sums, rounded once to the output's type.
    - ``HIGH``: partial sums rounded to the output's type per K tile.
    - ``MEDIUM``: A and B rounded to block floating point (bfp16) for the
      multiplies, where the device has bfp16 macs.

    A matmul takes the fastest kernel its level allows.
    """

    HIGHEST = "highest"
    HIGH = "high"
    MEDIUM = "medium"

    def at_least(self, floor: str) -> "Precision":
        """This level, or ``floor`` where that rounds less."""
        order = list(Precision)
        return min(self, Precision(floor), key=order.index)
