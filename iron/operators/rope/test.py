#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.common.test_utils import operator_test
from iron.operators.rope.op import RoPE, angle_table


def cases():
    max_cols = aie_utils.get_current_device().cols
    out = []
    for cols in [c for c in (1, 2, 4, 8) if c <= max_cols]:
        for rows in (32, 64):
            for angle_rows in (8, 16, 32):
                for width in (128, 512):
                    for method_type in (0, 1):
                        regular = (
                            rows == 32
                            and width == 512
                            and angle_rows in (8, 32)
                            and method_type == 0
                        )
                        if not regular and width != 128:
                            continue
                        out.append(
                            pytest.param(
                                dict(
                                    rows=rows,
                                    cols=width,
                                    num_aie_columns=cols,
                                    angle_rows=angle_rows,
                                    method_type=method_type,
                                ),
                                marks=[] if regular else [pytest.mark.extensive],
                            )
                        )
    return out


def angles(op):
    # One angle row per position, applied to rows // angle_rows consecutive
    # rows of x (the heads of one position, in the design's layout).
    return dict(angles=angle_table(op.angle_rows, op.cols, op.method_type))


test_rope = operator_test(RoPE, cases(), rel_tol=0.05, abs_tol=0.5, draw=angles)
