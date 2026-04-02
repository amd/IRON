# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Strided copy design

This can be useful for data layout manipulation and data copying such as:
input[0, :, 0] -> output[:, 0, 0]
"""

import numpy as np

from aie.dialects.aiex import TensorAccessPattern
from aie.iron import ObjectFifo, Program, Runtime
from aie.iron.placers import SequentialPlacer


def strided_copy(
    dev,
    dtype,
    input_buffer_size,
    input_sizes,
    input_strides,
    input_offset,
    output_buffer_size,
    output_sizes,
    output_strides,
    output_offset,
    transfer_size=None,
    num_aie_channels=1,
    input_offset_patch_marker=0,
    output_offset_patch_marker=0,
):
    assert len(input_sizes) == len(input_strides)
    assert len(output_sizes) == len(output_strides)

    # Pad out dimensions to 4D; dropping leading dimensions leads to compiler not initializing these registers, causing hard-to-debug errors
    input_sizes = [1] * (4 - len(input_sizes)) + list(input_sizes)
    input_strides = [0] * (4 - len(input_strides)) + list(input_strides)
    output_sizes = [1] * (4 - len(output_sizes)) + list(output_sizes)
    output_strides = [0] * (4 - len(output_strides)) + list(output_strides)

    input_highest_sz_idx = max(idx for idx, sz in enumerate(input_sizes) if sz >= 1)
    output_highest_sz_idx = max(idx for idx, sz in enumerate(output_sizes) if sz >= 1)
    assert (
        input_sizes[input_highest_sz_idx] % num_aie_channels == 0
    ), "Highest dimension of input_sizes must be divisible by num_aie_channels"
    assert (
        output_sizes[output_highest_sz_idx] % num_aie_channels == 0
    ), "Highest dimension of output_sizes must be divisible by num_aie_channels"

    if transfer_size is None:
        transfer_size = int(np.prod(input_sizes))
    assert np.prod(input_sizes) % transfer_size == 0
    transfer_ty = np.ndarray[
        (transfer_size,),
        np.dtype[dtype],
    ]

    inp_ty = np.ndarray[
        (int(input_buffer_size),),
        np.dtype[dtype],
    ]
    out_ty = np.ndarray[
        (int(output_buffer_size),),
        np.dtype[dtype],
    ]

    # input_offset_patch_marker (and output_offset_patch_marker) is a deferred-offset mechanism:
    # When non-zero, it is used as a placeholder offset value in the TensorAccessPattern instead
    # of the statically-computed input_offset. The actual offset is then patched at runtime by the
    # caller (e.g., StridedCopy.forward()) by writing the real byte offset into the instruction
    # stream. This allows the same compiled xclbin/insts to be reused with different runtime offsets
    # into a shared buffer, without recompilation. The tensor_dims is also expanded by the marker
    # value to prevent the compiler from flagging out-of-bounds accesses during code generation.
    input_taps = [
        TensorAccessPattern(
            tensor_dims=(int(input_buffer_size + input_offset_patch_marker),),
            offset=(
                input_offset_patch_marker
                if input_offset_patch_marker != 0
                else input_offset
                + c
                * (input_sizes[input_highest_sz_idx] // num_aie_channels)
                * input_strides[input_highest_sz_idx]
            ),
            sizes=(
                input_sizes[:input_highest_sz_idx]
                + [input_sizes[input_highest_sz_idx] // num_aie_channels]
                + input_sizes[input_highest_sz_idx + 1 :]
            ),
            strides=list(input_strides),
        )
        for c in range(num_aie_channels)
    ]

    output_taps = [
        TensorAccessPattern(
            tensor_dims=(int(output_buffer_size + output_offset_patch_marker),),
            offset=(
                output_offset_patch_marker
                if output_offset_patch_marker != 0
                else output_offset
                + c
                * (output_sizes[output_highest_sz_idx] // num_aie_channels)
                * output_strides[output_highest_sz_idx]
            ),
            sizes=(
                output_sizes[:output_highest_sz_idx]
                + [output_sizes[output_highest_sz_idx] // num_aie_channels]
                + output_sizes[output_highest_sz_idx + 1 :]
            ),
            strides=list(output_strides),
        )
        for c in range(num_aie_channels)
    ]

    # Use smaller FIFOs for the transfer amount
    fifos_in = [
        ObjectFifo(transfer_ty, name=f"fifo_in_{c}", depth=1)
        for c in range(num_aie_channels)
    ]
    fifos_out = [
        fifos_in[c].cons().forward(name=f"fifo_out_{c}", depth=1)
        for c in range(num_aie_channels)
    ]

    rt = Runtime()
    with rt.sequence(inp_ty, out_ty) as (inp, out):
        tg = rt.task_group()
        for c in range(num_aie_channels):
            rt.fill(fifos_in[c].prod(), inp, input_taps[c], task_group=tg)
            rt.drain(fifos_out[c].cons(), out, output_taps[c], task_group=tg, wait=True)
        rt.finish_task_group(tg)

    return Program(dev, rt).resolve_program(SequentialPlacer())
