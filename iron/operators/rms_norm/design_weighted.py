# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_


def my_weighted_rms_norm(
    dev,
    num_elements,
    num_columns,
    num_channels,
    weight_length,
    trace_size,
    func_prefix="",
):
    per_tile_elements = weight_length
    total_cores = num_columns * num_channels
    n = per_tile_elements * total_cores
    if num_elements % n != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {n}."
        )
    N_div_n = num_elements // n
    chunk = num_elements // total_cores
    dtype = bfloat16
    # Define tensor types
    tensor_ty = np.ndarray[(num_elements,), np.dtype[dtype]]
    weights_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    # Set fifodepth based on weight_length
    fifodepth = 1 if weight_length > 4096 else 2

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(tile_ty, name=f"in1_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    # One weight ObjectFifo per channel, shared across columns in that channel
    of_in2s = [
        ObjectFifo(weights_ty, name=f"in2_weights_{j}", depth=fifodepth)
        for j in range(num_channels)
    ]
    of_out1s = [
        ObjectFifo(tile_ty, name=f"out1_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    of_out2s = [
        ObjectFifo(tile_ty, name=f"out2_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # AIE Core Function declaration
    rms_norm_kernel = Kernel(
        f"{func_prefix}rms_norm_bf16_vector",
        f"{func_prefix}rms_norm.o",
        [tile_ty, tile_ty, np.int32],
    )
    eltwise_mul_kernel = Kernel(
        f"{func_prefix}eltwise_mul_bf16_vector",
        f"{func_prefix}mul.o",
        [tile_ty, weights_ty, tile_ty, np.int32],
    )

    # Define a task that will run on a compute tile
    def core_body_norm(of_in1, of_out1, rms_norm):
        # Number of sub-vector "tile" iterations
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out1.acquire(1)
            rms_norm(elem_in1, elem_out, per_tile_elements)
            of_in1.release(1)
            of_out1.release(1)

    def core_body_mul(of_in1, of_in2, of_out2, eltwise_mul):
        # Number of sub-vector "tile" iterations
        elem_in2 = of_in2.acquire(1)
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out2.acquire(1)
            eltwise_mul(elem_in1, elem_in2, elem_out, per_tile_elements)
            of_in1.release(1)
            of_out2.release(1)
        of_in2.release(1)

    # Create workers to run the task on compute tiles,
    # one core for rms norm and another pipelined to do eltwise mul
    my_workers = []
    for i in range(num_columns):
        for j in range(num_channels):
            idx = i * num_channels + j
            my_workers.append(
                Worker(
                    core_body_norm,
                    [
                        of_in1s[idx].cons(),
                        of_out1s[idx].prod(),
                        rms_norm_kernel,
                    ],
                )
            )
    for i in range(num_columns):
        for j in range(num_channels):
            idx = i * num_channels + j
            my_workers.append(
                Worker(
                    core_body_mul,
                    [
                        of_out1s[idx].cons(),
                        of_in2s[j].cons(),
                        of_out2s[idx].prod(),
                        eltwise_mul_kernel,
                    ],
                )
            )

    # Create a TensorAccessPattern for each core
    # to describe the data movement.
    # The pattern chops the data in equal chunks
    # and moves them in parallel across columns and channels.
    taps = [
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
    with rt.sequence(tensor_ty, weights_ty, tensor_ty) as (A, B, C):
        rt.start(*my_workers)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(num_columns):
            for j in range(num_channels):
                idx = i * num_channels + j
                rt.fill(
                    of_in1s[idx].prod(),
                    A,
                    taps[idx],
                    task_group=tg,
                )
        # Fill weights (one per channel)
        for j in range(num_channels):
            rt.fill(
                of_in2s[j].prod(),
                B,
                task_group=tg,
            )
        # Drain the output objectFIFOs with data
        for i in range(num_columns):
            for j in range(num_channels):
                idx = i * num_channels + j
                rt.drain(
                    of_out2s[idx].cons(),
                    C,
                    taps[idx],
                    wait=True,
                    task_group=tg,
                )
        rt.finish_task_group(tg)

    # Place program components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt).resolve_program(SequentialPlacer())
