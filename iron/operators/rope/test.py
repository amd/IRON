#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils
from aie.utils.verify import Tolerance
from iron.operators.rope.op import RoPE
from iron.operators.rope.reference import generate_inputs
from iron.common.test_utils import assert_matches_reference


def get_params():
    max_cols = aie_utils.get_current_device().cols
    num_aie_columns_options = [c for c in [1, 2, 4, 8] if c <= max_cols]

    # Combine all options
    input_rows = [32, 64]
    input_cols = [128, 512]
    input_angle_rows = [8, 16, 32]
    method_types = [0, 1]  # 0: Two-halves method, 1: interleaved method

    params = []
    for num_aie_columns in num_aie_columns_options:
        for n_rows in input_rows:
            for n_angle_rows in input_angle_rows:
                for n_cols in input_cols:
                    for method_type in method_types:
                        is_regular = (
                            n_rows == 32
                            and n_cols == 512
                            and n_angle_rows in [8, 32]
                            and method_type == 0
                        )

                        is_extensive_valid = n_cols == 128

                        if not is_regular and not is_extensive_valid:
                            continue

                        marks = [] if is_regular else [pytest.mark.extensive]

                        params.append(
                            pytest.param(
                                n_rows,
                                n_cols,
                                n_angle_rows,
                                num_aie_columns,
                                method_type,
                                marks=marks,
                            )
                        )
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "rows,cols,angle_rows,aie_columns,method_type",
    get_params(),
)
def test_rope(rows, cols, angle_rows, aie_columns, method_type, aie_context):
    x, angles = generate_inputs(rows=rows, cols=cols, context_len=angle_rows)

    operator = RoPE(
        rows=rows,
        cols=cols,
        num_aie_columns=aie_columns,
        angle_rows=angle_rows,
        method_type=method_type,
        context=aie_context,
    )

    assert_matches_reference(
        operator,
        x,
        angles,
        # The tighter of this test's former rel_tol and the kernel contract's
        # atol (none): an output that cancels to near zero is judged
        # relatively like any other.
        tolerance=Tolerance.relative(0.05),
    )
