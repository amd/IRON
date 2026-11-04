# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""MHA's mappings, one core a query block and today's three, are one result at equal B_kv, on a device.

Each runs the same inputs, and their outputs are compared bit for bit:
mha.cc's attend_block is matmul_bf16_bf16_wrapper, partial_softmax and
matmul_PV in one, and a row's keys go by in the same order whatever its
query block.
"""

from math import prod

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron import Buffer
from aie.iron.dataflow.objectfifo import ObjectFifoHandle
from aie.utils.compile.utils import resolve_target_arch

from iron.common import Rtp
from iron.common.design import OperatorDesign
from iron.common.image.compose import BuiltArray
from iron.common.testing import vectors
from iron.operators.mha import MHA
from iron.tests.support.tools import DEVICES


@pytest.mark.supported_devices("npu1", "npu2")
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
            # The mappings agree bit for bit over one score type: bf16, mapping 3's.
            f32_scores=False,
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


@pytest.mark.parametrize("window", [None, 100], ids=["unmasked", "two_sided"])
def test_one_core_a_block_streams_every_key_a_non_causal_query_attends(window, npu1):
    op = MHA(
        num_heads=8,
        num_KV_heads=8,
        d=64,
        seq_len=2048,
        causal=False,
        window=window,
        kv_paired=True,
        heads_interleaved=True,
        num_pipelines=4,
        cores_per_block=1,
    ).resolved(npu1)
    assert op.fused
    for g, rounds in enumerate(op.round_groups):
        end = min(rounds.stop * op.positions * op.streams, op.q_tokens)
        attended = op.first_query + end + (op.kv_tokens if window is None else window)
        assert op.group_blocks(g) * op.B_kv >= min(attended, op.kv_tokens)


@pytest.mark.parametrize("device", ["npu1", "npu2"])
@pytest.mark.parametrize(
    "seq_len,f32_scores",
    [(2048, None), (2048, False), (1, None)],
    ids=["prompt", "prompt_bf16", "split_decode"],
)
def test_a_fused_cores_estimate_holds_what_it_declares(device, seq_len, f32_scores):
    """``fused_core_bytes`` and ``split_core_bytes`` cover every buffer, fifo end and word a built core holds, beside the stack and the kernel's frame."""
    dev = DEVICES[device]()
    with aie_utils.set_current_device(dev):
        op = MHA(
            num_heads=32,
            num_KV_heads=8,
            seq_len=seq_len,
            kv_len=4096,
            heads_interleaved=True,
            kv_paired=True,
            num_pipelines=4,
            cores_per_block=1,
            f32_scores=f32_scores,
        ).resolved(dev)
        if op.split:
            estimate = op.split_core_bytes(dev, op.B_kv, op.kv_lanes, op.lane_heads)
            kernel = op.fused_kernel(dev, op.B_q, op.B_kv, 1, op.lane_heads)
        else:
            estimate = op.fused_core_bytes(dev, op.B_q, op.B_kv, op.f32_scores)
            kernel = op.fused_kernel(dev, op.B_q, op.B_kv, op.group, f32=op.f32_scores)
        room = (
            estimate
            - dev.default_core_stack_bytes
            - kernel.frame_bytes(resolve_target_arch(dev))
        )
        for worker in BuiltArray(OperatorDesign(op)).workers:
            held = 0
            for arg in worker.fn_args:
                if isinstance(arg, Rtp):
                    arg = arg.buffer
                if isinstance(arg, Buffer):
                    held += prod(arg.shape) * np.dtype(arg.dtype).itemsize
                elif isinstance(arg, ObjectFifoHandle):
                    held += arg.depth * prod(arg.shape) * np.dtype(arg.dtype).itemsize
            assert held <= room, (worker.name, held, room)
