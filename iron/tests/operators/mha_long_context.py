#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""MHA of one query over a long cache holds its accuracy at every depth.

The online softmax adds each key block's weights and outputs to a running
sum and output. Kept in bf16, each addition would round to the total's 8
bits and lose a block's share the more the larger the total had grown: on
npu2 it held 4% of the output's range at position 1023 and was 45% off at
32703. A cache of a few rows tiled
over its length keeps every block's share alike and the outputs far from 0,
as a prompt the decoder has repeated does; random keys average the outputs
to near 0, where the loss hides under any absolute floor.
"""

import numpy as np
import pytest
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.harness import verify_buffer
from iron.operators.mha import MHA

# Llama 3.2 1B's decode: its heads packed, over its default context.
HEADS, KV_HEADS, D, CACHE, DISTINCT = 32, 8, 64, 32768, 55

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


class Decode(iron.Graph):
    def body(self, q, k, v, *, position: Scratchpad[np.int32]):
        return MHA(
            q.reshape(1, HEADS, D),
            k[: position + 1],
            v[: position + 1],
            heads_interleaved=True,
            kv_interleaved=True,
            num_pipelines=4,
        )


@pytest.mark.supported_devices("npu2")
def test_one_query_is_as_accurate_deep_in_the_cache_as_near_its_start(npu_runtime):
    rng = np.random.default_rng(0)
    rows = (DISTINCT, KV_HEADS, D)
    k = np.resize(rng.standard_normal(rows) * 2, (CACHE, KV_HEADS, D)).astype(bfloat16)
    v = np.resize(rng.standard_normal(rows), (CACHE, KV_HEADS, D)).astype(bfloat16)
    q = rng.standard_normal((1, HEADS * D)).astype(bfloat16)
    net = Decode().compile(q=q.shape, k=k.shape, v=v.shape)
    for position in (1023, CACHE - 65):
        n = position + 1
        o = np.asarray(net(q, k, v, position=position), np.float32)
        expected = MHA(
            num_heads=HEADS,
            num_KV_heads=KV_HEADS,
            seq_len=1,
            kv_len=n,
            heads_interleaved=True,
            kv_interleaved=True,
        ).reference(q.reshape(1, HEADS, D), k[:n], v[:n])
        expected = np.asarray(expected, np.float32).reshape(o.shape)
        # 2.0% of the range measured at both positions, aie::exp2's error.
        peak = float(np.abs(expected).max())
        verdict = verify_buffer(
            o, "O", expected, tolerance=Tolerance(rtol=0, atol=0.04 * peak)
        )
        assert verdict, f"{position=}: {verdict.detail}"
