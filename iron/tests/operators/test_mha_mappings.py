# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""MHA's mappings, one core a query block and today's three, are one result at equal B_kv, on a device.

Each runs the same inputs, and their outputs are compared bit for bit:
mha.cc's attend_block is matmul_bf16_bf16_wrapper, partial_softmax and
matmul_PV in one, and a row's keys go by in the same order whatever its
query block.
"""

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.common.testing import vectors
from iron.operators.mha import MHA


@pytest.mark.supported_devices("npu1")
@pytest.mark.parametrize(
    "heads,kv_heads,d,seq_len,kv_len,window",
    [
        # Llama 3.2 1B's and 3B's prompt chunk over a deeper cache.
        (32, 8, 64, 2048, 8192, None),
        (24, 8, 128, 2048, 4096, None),
        # Gemma 4 E2B's sliding layer.
        (8, 1, 256, 512, 2048, 511),
    ],
)
def test_one_core_a_block_is_three(heads, kv_heads, d, seq_len, kv_len, window):
    inputs, outs = None, []
    for cores in (1, 3):
        op = MHA(
            num_heads=heads,
            num_KV_heads=kv_heads,
            d=d,
            seq_len=seq_len,
            kv_len=kv_len,
            window=window,
            heads_interleaved=True,
            kv_paired=True,
            num_pipelines=4,
            cores_per_block=cores,
        ).resolved()
        if inputs is None:
            inputs = vectors(op).inputs
        op.compile()
        tensor = aie_utils.DEFAULT_TENSOR_CLASS
        args = [
            (
                tensor(b.device_form(inputs[b.name]))
                if b.fills
                else tensor(b.host_shape, dtype=b.host_dtype)
            )
            for b in op.buffers
        ]
        op(*args)
        (o,) = (a.numpy() for a, b in zip(args, op.buffers) if b.drains)
        outs.append((op.B_q, op.B_kv, o.view(np.uint16)))
    (q1, kv1, fused), (q3, kv3, pipeline) = outs
    assert kv1 == kv3 and q1 != q3, (q1, kv1, q3, kv3)
    differ = np.argwhere(fused != pipeline)
    assert not len(differ), f"{len(differ)} of O differ, first {differ[:4]}"
