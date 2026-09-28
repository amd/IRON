#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""MHA's declared buffers: Q and O over every head, K and V over the KV
heads alone, each the padded sequence long.
"""

import math

import pytest

from iron.operators.mha import MHA

pytestmark = pytest.mark.usefixtures("npu2")


@pytest.mark.parametrize(
    "num_heads,num_kv_heads",
    [(8, 2), (1, 1)],  # grouped-query, and plain MHA: as many KV heads
)
def test_buffers_are_the_padded_sequence_by_head(num_heads, num_kv_heads):
    seq_len, d = 16384, 64
    op = MHA(
        num_heads=num_heads,
        seq_len=seq_len,
        d=d,
        num_KV_heads=num_kv_heads,
        num_pipelines=8,
    )
    q, k, v, o = (math.prod(b.shape) for b in op.buffers)

    pad = op.seq_padding(seq_len)
    assert q == o == num_heads * pad * d
    assert k == v == num_kv_heads * pad * d
