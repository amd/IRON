# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Split decode's walks on the host, with the operator's own patterns (device-free, npu1 and npu2).

Q and a pad fill a lane's first object, its keys are every n-th block of
each pass's heads, and O's walk takes each packed row back to its head.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.device import from_name

from iron.operators.mha import MHA

# Each device with its pipelines per npu1 pipeline: npu1 takes two lanes a
# column, npu2 one, so both run the same lanes.
DEVICES = {
    "npu1": (from_name("npu1", n_cols=4), 1),
    "npu2": (from_name("npu2", n_cols=8), 2),
}

CASES = [
    # Llama 3.2 1B's and 3B's, Granite's group of 5, Qwen3's of 2 at d=64,
    # MHA's of 1; Gemma 3's and Gemma 4's MQA at d=256, two lanes.
    (32, 8, 64, 4),
    (24, 8, 128, 4),
    (40, 8, 64, 4),
    (16, 8, 64, 4),
    (8, 8, 64, 4),
    (4, 1, 256, 1),
    (8, 1, 256, 1),
]


def _split(device, heads, kv_heads, d, pipelines, kv_len=4096):
    dev, per = DEVICES[device]
    with aie_utils.set_current_device(dev):
        return MHA(
            num_heads=heads,
            num_KV_heads=kv_heads,
            d=d,
            seq_len=1,
            kv_len=kv_len,
            heads_interleaved=True,
            kv_paired=True,
            num_pipelines=pipelines * per,
            cores_per_block=1,
        ).resolved(dev)


@pytest.mark.parametrize("device", DEVICES)
@pytest.mark.parametrize("heads,kv_heads,d,pipelines", CASES)
def test_q_and_its_pad_are_one_key_block(device, heads, kv_heads, d, pipelines):
    """A lane's first object is every query head flat, in order, then any keys up to one key block's object."""
    op = _split(device, heads, kv_heads, d, pipelines)
    q = np.arange(heads * d).reshape(op.Q.shape)
    assert np.array_equal(op.split_q().gather(q), np.arange(heads * d))
    obj = op.B_kv * op.lane_heads * 2 * d
    assert heads * d + op.split_pad().sizes[0] == obj


@pytest.mark.parametrize("device", DEVICES)
@pytest.mark.parametrize("heads,kv_heads,d,pipelines", CASES)
def test_a_lane_streams_every_nth_block_of_each_pass(
    device, heads, kv_heads, d, pipelines
):
    """Lane ``l``'s descriptor gives each pass's KV heads, key blocks ``l``, ``l + n``, ... at their positions, K row then V row a head."""
    op = _split(device, heads, kv_heads, d, pipelines)
    shape = op.KV.shape
    kv = np.arange(np.prod(shape)).reshape(shape)
    G, B, lanes, lh = kv_heads, op.B_kv, op.kv_lanes, op.lane_heads
    blocks = op.split_keys(0).sizes[1]
    for lane in range(lanes):
        got = op.split_keys(lane).gather(kv).reshape(G // lh, blocks, B, lh, 2, d)
        for p in range(G // lh):
            for b in range(blocks):
                keys = (lane + b * lanes) * B + np.arange(B)
                pass_heads = p * lh + np.arange(lh)
                want = kv[keys][:, pass_heads]
                assert np.array_equal(got[p, b], want), (lane, p, b)


@pytest.mark.parametrize("device", DEVICES)
@pytest.mark.parametrize("heads,kv_heads,d,pipelines", CASES)
def test_o_returns_each_packed_row_to_its_head(device, heads, kv_heads, d, pipelines):
    """mha.cc's take_q packs rows ``i`` and ``i + 4`` from neighbouring heads of the group; O's walk takes each row back to its head.

    Every head of the group is packed at least once.
    """
    op = _split(device, heads, kv_heads, d, pipelines)
    g = heads // kv_heads
    pairs = 1 if g == 1 else g - 1 if g % 2 else g // 2
    step = 0 if g == 1 else 1 if g % 2 else 2
    rows = [step * (i % pairs) + (j and g > 1) for j in (0, 1) for i in range(4)]
    assert sorted(set(rows)) == list(range(g))
    o = np.arange(heads * d).reshape(op.O.shape)
    for kv_head in range(kv_heads):
        drained = op.split_out(kv_head).gather(o).reshape(8, d)
        want = (kv_head * g + np.array(rows))[:, None] * d + np.arange(d)
        assert np.array_equal(drained, want), kv_head
