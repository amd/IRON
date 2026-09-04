# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Strided copy design

This can be useful for data layout manipulation and data copying such as:
input[0, :, 0] -> output[:, 0, 0]
"""

import numpy as np

from aie.dialects.aiex import TensorAccessPattern
from aie.iron import (
    ObjectFifo,
    Program,
    Runtime,
    ScratchpadParameter,
    TaskGroup,
    sync_parameters,
)


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
    input_offset_parameter=None,
    output_offset_parameter=None,
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

    # Each channel's BD carries 1/num_aie_channels of the tensor, so the ObjectFifo object
    # is sized against the per-channel share. A BD shorter than the object starves the
    # MemTile's S2MM -- it never completes an object, never releases the lock, and the
    # drain's dma_await_task never returns (ERT_CMD_STATE_TIMEOUT). An integer multiple is
    # fine; it just cycles the buffer.
    assert int(np.prod(input_sizes)) == int(np.prod(output_sizes)), (
        f"a copy moves the same element count both ways: input_sizes {input_sizes} "
        f"has {int(np.prod(input_sizes))} elements, output_sizes {output_sizes} has "
        f"{int(np.prod(output_sizes))}"
    )
    per_channel_size = int(np.prod(input_sizes)) // num_aie_channels
    if transfer_size is None:
        transfer_size = per_channel_size
    assert per_channel_size % transfer_size == 0, (
        f"transfer_size {transfer_size} must divide the per-channel transfer "
        f"{per_channel_size} (= {int(np.prod(input_sizes))} / {num_aie_channels} channels)"
    )
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

    # input_offset_parameter (and output_offset_parameter) is the name of an
    # aiex.scratchpad_parameter used to patch the DMA BD base address at runtime. The
    # statically-computed offset is used as the base; the parameter's value is
    # additively combined onto it inside the BD address registers via UPDATE_REG.
    # The host writes an ELEMENT count into the ctrl scratchpad before each
    # dispatch via ParameterScratchpad; the firmware multiplies by elemBytes
    # before adding it into the address register.
    in_offset_param = (
        ScratchpadParameter(input_offset_parameter, np.int32)
        if input_offset_parameter is not None
        else None
    )
    out_offset_param = (
        ScratchpadParameter(output_offset_parameter, np.int32)
        if output_offset_parameter is not None
        else None
    )

    input_taps = [
        TensorAccessPattern(
            tensor_dims=(int(input_buffer_size),),
            offset=(
                input_offset
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
            tensor_dims=(int(output_buffer_size),),
            offset=(
                output_offset
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

    def sequence(inp, out, fifos_in_prods, fifos_out_conss):
        if in_offset_param is not None or out_offset_param is not None:
            sync_parameters()
        tg = TaskGroup()
        for c in range(num_aie_channels):
            fifos_in_prods[c].fill(
                inp,
                input_taps[c],
                group=tg,
                offset_parameter=in_offset_param,
            )
            fifos_out_conss[c].drain(
                out,
                output_taps[c],
                group=tg,
                wait=True,
                offset_parameter=out_offset_param,
            )
        tg.finish()

    rt = Runtime(
        sequence,
        [
            inp_ty,
            out_ty,
            [of.prod() for of in fifos_in],
            [of.cons() for of in fifos_out],
        ],
    )
    return Program(dev, rt).resolve_program()
