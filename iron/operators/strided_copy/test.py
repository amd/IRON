#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.operators.strided_copy.op import StridedCopy
from iron.operators.strided_copy.reference import generate_golden_reference
from iron.common.test_utils import run_test

# Llama's KV-cache write, shrunk: the cache is (n_kv_groups, seq, head_dim) and one
# token's keys land in slot t of every group. SEQ is 128 rather than the real 2048 to
# keep the output buffer at 128 KB; the full-size arm is extensive.
N_KV, HEAD_DIM, SEQ = 8, 64, 128


def _kv_slot(seq, slot, num_aie_channels=1):
    """StridedCopy kwargs writing one (N_KV, HEAD_DIM) token into cache slot `slot`."""
    return dict(
        input_sizes=[N_KV, HEAD_DIM],
        input_strides=[HEAD_DIM, 1],
        input_offset=0,
        input_buffer_size=N_KV * HEAD_DIM,
        output_sizes=[1, N_KV, HEAD_DIM],
        output_strides=[0, seq * HEAD_DIM, 1],
        output_offset=slot * HEAD_DIM,
        output_buffer_size=N_KV * seq * HEAD_DIM,
        num_aie_channels=num_aie_channels,
    )


def _flat(size, num_aie_channels=1, transfer_size=None):
    return dict(
        input_sizes=[size],
        input_strides=[1],
        input_offset=0,
        input_buffer_size=size,
        output_sizes=[size],
        output_strides=[1],
        output_offset=0,
        output_buffer_size=size,
        num_aie_channels=num_aie_channels,
        transfer_size=transfer_size,
    )


def get_params():
    return [
        pytest.param(_flat(1024), id="contiguous"),
        pytest.param(_flat(1024, num_aie_channels=2), id="two_channels"),
        pytest.param(_flat(1024, num_aie_channels=4), id="four_channels"),
        pytest.param(
            _flat(1024, num_aie_channels=2, transfer_size=256),
            id="two_channels_chunked",
        ),
        pytest.param(_flat(1024, transfer_size=256), id="chunked_transfer"),
        pytest.param(_kv_slot(SEQ, 0), id="kv_slot0"),
        pytest.param(_kv_slot(SEQ, 5), id="kv_slot5"),
        pytest.param(_kv_slot(SEQ, SEQ - 1), id="kv_slot_last"),
        # The KV-cache write is what num_aie_channels exists to widen, so it carries the
        # strided arms too -- the flat cases split a stride-1 run, these split head_dim.
        pytest.param(_kv_slot(SEQ, 5, num_aie_channels=2), id="kv_slot5_two_channels"),
        pytest.param(_kv_slot(SEQ, 5, num_aie_channels=4), id="kv_slot5_four_channels"),
        pytest.param(
            _kv_slot(2048, 1000), id="kv_llama_full", marks=[pytest.mark.extensive]
        ),
    ]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize("kwargs", get_params())
def test_strided_copy(kwargs, aie_context):
    """StridedCopy moves data and computes nothing, so the gate is exact equality."""
    # transfer_size only sizes the ObjectFifo; it does not move the data anywhere else,
    # so the golden is computed without it.
    golden_kwargs = {k: v for k, v in kwargs.items() if k != "transfer_size"}
    golden_ref = generate_golden_reference(**golden_kwargs)

    operator = StridedCopy(**kwargs, context=aie_context)

    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        {"input": golden_ref["input"]},
        {"output": golden_ref["output"]},
        rel_tol=0.0,
        abs_tol=0.0,
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


def test_transfer_size_not_dividing_per_channel_share_is_rejected(aie_context):
    """A BD shorter than the ObjectFifo object hangs the device, so it must not compile.

    4 channels over 1024 elements is a 256-element BD; a 512-element object leaves the
    MemTile's S2MM waiting for a second half that no channel sends, and the drain's
    dma_await_task returns ERT_CMD_STATE_TIMEOUT with no diagnostic.
    """
    operator = StridedCopy(
        **_flat(1024, num_aie_channels=4, transfer_size=512), context=aie_context
    )
    with pytest.raises(AssertionError, match="must divide the per-channel transfer"):
        operator.compile()
