#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""StridedCopy's per-call output offset, on a device.

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

import aie.utils as aie_utils
from aie.iron.device import from_name

import iron
from iron.common.declare import Scratchpad
from iron.operators.strided_copy import StridedCopy

# Llama's KV-cache write, shrunk: (n_kv_groups, seq, head_dim), one token's
# keys landing in slot t of every group.
N_KV, HEAD_DIM, SEQ = 8, 64, 128


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


@pytest.mark.supported_devices("npu2")
def test_the_cache_offset_is_applied_per_call(npu_runtime):
    cache = iron.state((N_KV, SEQ * HEAD_DIM), name="cache")

    @iron.graph
    def write(x, *, pos: Scratchpad[np.int32]):
        StridedCopy(
            x,
            cache,
            out_offset=pos,
            input_sizes=(N_KV, HEAD_DIM),
            input_strides=(HEAD_DIM, 1),
            input_offset=0,
            output_sizes=(1, N_KV, HEAD_DIM),
            output_strides=(0, SEQ * HEAD_DIM, 1),
            output_offset=0,
            num_aie_channels=1,
        )

    net = write.compile(x=(N_KV, HEAD_DIM))
    assert net.plan.image == "elf", "only the full ELF carries a scratchpad"

    expected = np.zeros((N_KV, SEQ, HEAD_DIM), dtype=np.float32)
    net.write(cache, expected.reshape(N_KV, SEQ * HEAD_DIM))
    rng = np.random.default_rng(0)
    for slot in (0, 5, SEQ - 1):
        x = rng.standard_normal((N_KV, HEAD_DIM)).astype(bfloat16)
        expected[:, slot, :] = x.astype(np.float32)
        # The value is an element count; the firmware scales it by the element size.
        write(x, pos=slot * HEAD_DIM)
        got = np.asarray(net.read(cache), dtype=np.float32).reshape(expected.shape)
        wrong = np.argwhere(got != expected)
        assert not len(
            wrong
        ), f"slot {slot}: {len(wrong)} elements differ, first {wrong[:4]}"
