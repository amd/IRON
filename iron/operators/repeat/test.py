#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.common.test_utils import operator_test
from iron.operators.repeat.op import Repeat

# rows, cols, repeat, transfer_size.
#
# design.py splits cols into chunks <= 1023 by picking the smallest divisor that
# gets under the hardware limit, so cols on either side of 1023 take different
# paths and both need covering. The llama arm is the shape the only caller in the
# tree actually dispatches: n_kv_groups=8 groups expanded to n_heads=32 over a
# max_seq_len=2048 context of head_dim=64, i.e. repeat=4 with cols=2048*64.
CASES = [
    dict(rows=8, cols=64, repeat=4, transfer_size=None),
    dict(rows=8, cols=512, repeat=4, transfer_size=64),
    dict(rows=4, cols=1024, repeat=2, transfer_size=None),
    pytest.param(
        dict(rows=4, cols=2048, repeat=2, transfer_size=None),
        marks=[pytest.mark.extensive],
    ),
    pytest.param(
        dict(rows=8, cols=2048 * 64, repeat=4, transfer_size=64),
        marks=[pytest.mark.extensive],
    ),
]

# Repeat moves data and computes nothing, so the gate is exact equality. A
# tolerance gate would accept a permutation that reads the wrong group, which
# is the whole failure mode here: the only caller uses this to expand KV groups
# to attention heads, and a misrouted group is numerically plausible.
test_repeat = operator_test(Repeat, CASES, rel_tol=0.0, abs_tol=0.0)


@pytest.mark.parametrize(
    "cols,why",
    [
        (513, "odd: every divisor is odd, so no chunk is a whole 32-bit word"),
        (1031, "prime > 1023: the only divisors are 1 and cols, neither legal"),
        (2062, "2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count"),
    ],
)
def test_cols_without_a_legal_split_is_rejected(cols, why, aie_context):
    """A split has to satisfy the innermost dim AND the dim holding the chunk count.

    Both land on a 10-bit wrap field, and the innermost is denominated in 32-bit words,
    so bounding the chunk length alone lets through taps the BD verifier then rejects
    with a much less legible error.
    """
    operator = Repeat(rows=8, cols=cols, repeat=4, context=aie_context)
    with pytest.raises(ValueError, match="Cannot split cols"):
        operator.compile()
