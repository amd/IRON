# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A weight's projection at either row count, for a graph's body."""

from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV


def project(x, weight, **gemv):
    """``x @ weight.T`` for a checkpoint's ``(out, in)`` weight: a GEMV for
    one row (a GEMV's output is a vector), else a GEMM reading it
    column-major. ``gemv`` are the GEMV's tunables, where the profile cannot
    tell it from another of its shape.
    """
    if len(x.shape) == 2 and x.shape[0] > 1:
        return GEMM(x, weight, b_col_maj=True)
    return GEMV(weight, x, **gemv)
