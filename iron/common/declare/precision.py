# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How far an operator may round past its reference for speed."""

from enum import StrEnum


class Precision(StrEnum):
    """The roundings a matmul may make beyond its reference's, as
    ``torch.set_float32_matmul_precision`` names them; each level allows the one
    above's and more, and a matmul takes the fastest kernel its level allows.

    - ``HIGHEST``: f32 partial sums, rounded once to the output's type.
    - ``HIGH``: partial sums rounded to the output's type per K tile.
    - ``MEDIUM``: A and B rounded to bfp16 for the multiplies, where the
      device has bfp16 macs.
    """

    HIGHEST = "highest"
    HIGH = "high"
    MEDIUM = "medium"
