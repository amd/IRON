# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
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
    kernel_archive="softmax.a",
    func_prefix="",
):
    per_tile_elements = tile_size
    if rtp_vector_size is None:
        rtp_vector_size = per_tile_elements
    n = per_tile_elements * num_aie_columns
    if num_elements % n != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {n}."
        )
    N_div_n = num_elements // n
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
        f"{func_prefix}softmax_bf16", kernel_archive, [tile_ty, tile_ty, np.int32]
    )
    mask_kernel = Kernel(
        f"{func_prefix}mask_bf16", kernel_archive, [tile_ty, np.int32, np.int32]
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_out, softmax_kernel, mask_kernel, rtp, barrier):
        # Number of sub-vector "tile" iterations
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
    my_workers = [
        Worker(
            core_body,
            [
                of_in1s[i * num_channels + j].cons(),
                of_outs[i * num_channels + j].prod(),
                softmax_kernel,
                mask_kernel,
                rtps[i * num_channels + j],
                barriers[i * num_channels + j],
            ],
        )
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

        # Set run-time parameter for actual vector size (remainder is considered padding and ignored by the computation)
        def set_rtps(*args):
            for rtp in args:
                rtp[0] = rtp_vector_size if not mask_patch_value else mask_patch_value

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
