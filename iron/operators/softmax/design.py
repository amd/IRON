# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import numpy as np

from aie.iron import (
    Kernel,
    ObjectFifo,
    Program,
    Runtime,
    Worker,
    Buffer,
    WorkerRuntimeBarrier,
)
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.helpers.dialects.scf import _for as range_
from ml_dtypes import bfloat16


def softmax(
    dev,
    num_elements,
    num_aie_columns,
    num_channels,
    trace_size,
    tile_size,
    rtp_vector_size=None,
    mask_patch_value=0,
    func_prefix="",
    kernel_obj_file="softmax.o",
):
    per_tile_elements = tile_size
    if rtp_vector_size is None:
        rtp_vector_size = per_tile_elements
    total_cores = num_aie_columns * num_channels
    per_core_elements = num_elements // total_cores
    if num_elements % total_cores != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {total_cores}."
        )
    N_div_n = per_core_elements // per_tile_elements
    chunk = num_elements // num_aie_columns // num_channels  # For offset calculation
    dtype = bfloat16

    # Define tensor types
    tensor_ty = np.ndarray[(num_elements,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(tile_ty, name=f"in1_{i}_{j}")
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(tile_ty, name=f"out_{i}_{j}")
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # AIE Core Function declaration
    softmax_kernel = Kernel(
        f"{func_prefix}softmax_bf16",
        f"{func_prefix}{kernel_obj_file}",
        [tile_ty, tile_ty, np.int32],
    )
    mask_kernel = Kernel(
        f"{func_prefix}mask_bf16",
        f"{func_prefix}{kernel_obj_file}",
        [tile_ty, np.int32, np.int32],
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_out, softmax_kernel, mask_kernel, rtp, barrier):
        barrier.wait_for_value(1)
        vector_size = rtp[0]
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out.acquire(1)
            mask_kernel(elem_in1, vector_size, per_tile_elements)
            softmax_kernel(elem_in1, elem_out, per_tile_elements)
            of_in1.release(1)
            of_out.release(1)

    rtps = [
        Buffer(
            np.ndarray[(1,), np.dtype[np.int32]],
            name=f"rtp_{i}_{j}",
            use_write_rtp=True,
        )
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    barriers = [
        WorkerRuntimeBarrier()
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # Create a worker to run the task on a compute tile
    worker_args = lambda i, j: [
        of_in1s[i * num_channels + j].cons(),
        of_outs[i * num_channels + j].prod(),
        softmax_kernel,
        mask_kernel,
        rtps[i * num_channels + j],
        barriers[i * num_channels + j],
    ]
    my_workers = [
        Worker(core_body, worker_args(i, j))
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # Create a TensorAccessPattern for each channel
    # to describe the data movement
    # The pattern chops the data in equal chunks
    # and moves them in parallel across the columns
    # and channels.
    taps = [
        TensorAccessPattern(
            (1, num_elements),
            chunk * i * num_channels + chunk * j,
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(tensor_ty, tensor_ty) as (A, C):
        rt.start(*my_workers)

        # Set run-time parameter controlling how many elements each core processes:
        # - Normal case (mask_patch_value == 0): set to rtp_vector_size (the actual active row width;
        #   elements beyond this are padding and are ignored by the softmax computation).
        # - Masked case (mask_patch_value != 0): set to mask_patch_value, which the mask kernel uses
        #   as a threshold to zero out elements beyond the unmasked patch boundary before softmax.
        def set_rtps(*args):
            for rtp in args:
                rtp[0] = mask_patch_value if mask_patch_value else rtp_vector_size

        rt.inline_ops(set_rtps, rtps)

        for i in range(num_aie_columns * num_channels):
            rt.set_barrier(barriers[i], 1)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                rt.fill(
                    of_in1s[i * num_channels + j].prod(),
                    A,
                    taps[i * num_channels + j],
                    task_group=tg,
                )
        # Drain the output objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                rt.drain(
                    of_outs[i * num_channels + j].cons(),
                    C,
                    taps[i * num_channels + j],
                    wait=True,  # wait for the transfer to complete and data to be available
                    task_group=tg,
                )
        rt.finish_task_group(tg)

    # Place program components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt).resolve_program(SequentialPlacer())
