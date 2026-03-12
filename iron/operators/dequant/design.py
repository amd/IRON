# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_


def my_dequant_kernel(
    dev,
    num_elements,
    num_columns,
    num_channels,
    trace_size,
    tile_size,
    group_size,
    kernel_archive=None,
):
    per_tile_elements = (
        16384 if tile_size > 16384 else tile_size
    )  # Largest tile size for 64KB in L1 and possible
    # group size of 1 with objfifo depth of 1
    n = per_tile_elements * num_columns
    if num_elements % n != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {n}."
        )
    N_div_n = num_elements // n
    chunk = num_elements // num_columns // num_channels  # For offset calculation
    in_dtype = np.uint8
    out_dtype = bfloat16

    # Input data: int4 packed data + scale factors
    # For N int4 values, we need N/2 bytes + N/group_size scale factors (bfloat16, 2 bytes each)
    input_tensor_size = (num_elements // 2) + (num_elements // group_size) * 2
    input_tile_size = (per_tile_elements // 2) + (per_tile_elements // group_size) * 2

    # Define tensor types
    in_tensor_ty = np.ndarray[(input_tensor_size,), np.dtype[in_dtype]]
    out_tensor_ty = np.ndarray[(num_elements,), np.dtype[out_dtype]]
    in_tile_ty = np.ndarray[(input_tile_size,), np.dtype[in_dtype]]
    out_tile_ty = np.ndarray[(per_tile_elements,), np.dtype[out_dtype]]

    fifodepth = 1 if tile_size > 8192 else 2
    enable_trace = trace_size > 0

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(in_tile_ty, name=f"in1_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(out_tile_ty, name=f"out_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # AIE Core Function declaration
    dequant_kernel = Kernel(
        "expand_int4_to_bfloat16",
        f"expand_aie2_{tile_size}.o",
        [in_tile_ty, out_tile_ty],
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_out, dequant_kernel):
        # Number of sub-vector "tile" iterations
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out.acquire(1)
            dequant_kernel(elem_in1, elem_out)
            of_in1.release(1)
            of_out.release(1)

    # Create a worker to run the task on a compute tile
    my_workers = [
        Worker(
            core_body,
            [
                of_in1s[i * num_channels + j].cons(),
                of_outs[i * num_channels + j].prod(),
                dequant_kernel,
            ],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # Create a TensorAccessPattern for each channel
    # to describe the data movement
    # The pattern chops the data in equal chunks
    # and moves them in parallel across the columns
    # and channels.
    in_chunk = (chunk // 2) + (chunk // group_size) * 2
    taps_in = [
        TensorAccessPattern(
            (1, input_tensor_size),
            in_chunk * i * num_channels + in_chunk * j,
            [1, 1, 1, in_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    taps_out = [
        TensorAccessPattern(
            (1, num_elements),
            chunk * i * num_channels + chunk * j,
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(in_tensor_ty, out_tensor_ty) as (A, C):
        if enable_trace:
            rt.enable_trace(trace_size)
        rt.start(*my_workers)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(num_columns):
            for j in range(num_channels):
                rt.fill(
                    of_in1s[i * num_channels + j].prod(),
                    A,
                    taps_in[i * num_channels + j],
                    task_group=tg,
                )
        # Drain the output objectFIFOs with data
        for i in range(num_columns):
            for j in range(num_channels):
                rt.drain(
                    of_outs[i * num_channels + j].cons(),
                    C,
                    taps_out[i * num_channels + j],
                    wait=True,  # wait for the transfer to complete and data to be available
                    task_group=tg,
                )
        rt.finish_task_group(tg)

    # Place program components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt).resolve_program(SequentialPlacer())
