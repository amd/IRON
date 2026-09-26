#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Copy's per-call index into the cache, on a device.

Decode drives the KV-cache write through ``out_offset`` bound to a per-call
value; every declared case bakes the offset in at compile time instead, so
the path the application runs had no coverage. This drives it across three
token positions on one compiled graph, checking the whole cache each time so
a mis-scaled addend (elements vs bytes) cannot land in the wrong slot
undetected.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.operators.copy import Copy

# Llama's KV-cache write, shrunk: (n_kv_groups, seq, head_dim), one token's
# keys landing in slot t of every group.
N_KV, HEAD_DIM, SEQ = 8, 64, 128


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


@pytest.mark.supported_devices("npu2")
def test_the_cache_offset_is_applied_per_call(npu_runtime):
    cache = iron.state((N_KV, SEQ, HEAD_DIM), name="cache")

    @iron.graph
    def write(x, *, pos: Scratchpad[np.int32]):
        Copy(x, cache[:, pos])

    net = write.compile(x=(N_KV, HEAD_DIM))
    assert net.plan.image == "elf", "only the full ELF carries a scratchpad"

    expected = np.zeros((N_KV, SEQ, HEAD_DIM), dtype=np.float32)
    net.write(cache, expected)
    rng = np.random.default_rng(0)
    for slot in (0, 5, SEQ - 1):
        x = rng.standard_normal((N_KV, HEAD_DIM)).astype(bfloat16)
        expected[:, slot, :] = x.astype(np.float32)
        # The value is the row; the library scales it to an element offset.
        write(x, pos=slot)
        got = np.asarray(net.read(cache), dtype=np.float32).reshape(expected.shape)
        wrong = np.argwhere(got != expected)
        assert not len(
            wrong
        ), f"slot {slot}: {len(wrong)} elements differ, first {wrong[:4]}"
