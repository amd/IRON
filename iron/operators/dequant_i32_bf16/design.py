# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_


def my_dequant_i32_kernel(
    dev,
    num_elements,
    num_columns,
    num_channels,
    trace_size,
    tile_size,
    group_size,
):
    # Cap tile size to fit in L1 memory
    # int32 input: tile_size*4 bytes + scale factors: (tile_size/group_size)*2 bytes
    # bf16 output: tile_size*2 bytes
    # Total per tile ~ tile_size*6 bytes; 8192 elements ~ 49KB fits in 64KB L1
    per_tile_elements = 8192 if tile_size > 8192 else tile_size
    total_cores = num_columns * num_channels
    per_core_elements = num_elements // total_cores
    if num_elements % total_cores != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {total_cores}."
        )
    N_div_n = per_core_elements // per_tile_elements
    chunk = num_elements // num_columns // num_channels

    in_dtype = np.uint8
    out_dtype = bfloat16

    # Input: int32 data (4 bytes each) + bf16 scale factors (2 bytes each, one per group)
    input_tensor_size = num_elements * 4 + (num_elements // group_size) * 2
    input_tile_size = per_tile_elements * 4 + (per_tile_elements // group_size) * 2

    # Define tensor types
    in_tensor_ty = np.ndarray[(input_tensor_size,), np.dtype[in_dtype]]
    out_tensor_ty = np.ndarray[(num_elements,), np.dtype[out_dtype]]
    in_tile_ty = np.ndarray[(input_tile_size,), np.dtype[in_dtype]]
    out_tile_ty = np.ndarray[(per_tile_elements,), np.dtype[out_dtype]]

    fifodepth = 1 if tile_size > 4096 else 2
    enable_trace = trace_size > 0

    # ObjectFIFOs for data movement
    of_ins = [
        ObjectFifo(in_tile_ty, name=f"in_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(out_tile_ty, name=f"out_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # Kernel declaration
    dequant_kernel = Kernel(
        "dequant_i32_to_bfloat16",
        f"dequant_i32_bf16_{tile_size}.o",
        [in_tile_ty, out_tile_ty],
    )

    # Core task
    def core_body(of_in, of_out, dequant_kernel):
        for _ in range_(N_div_n):
            elem_in = of_in.acquire(1)
            elem_out = of_out.acquire(1)
            dequant_kernel(elem_in, elem_out)
            of_in.release(1)
            of_out.release(1)

    # Workers
    my_workers = [
        Worker(
            core_body,
            [
                of_ins[i * num_channels + j].cons(),
                of_outs[i * num_channels + j].prod(),
                dequant_kernel,
            ],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # TensorAccessPatterns
    in_chunk = chunk * 4 + (chunk // group_size) * 2  # bytes per core in input
    taps_in = [
        TensorAccessPattern(
            (1, input_tensor_size),
            in_chunk * (i * num_channels + j),
            [1, 1, 1, in_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    taps_out = [
        TensorAccessPattern(
            (1, num_elements),
            chunk * (i * num_channels + j),
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # Runtime
    rt = Runtime()
    with rt.sequence(in_tensor_ty, out_tensor_ty) as (A, C):
        if enable_trace:
            rt.enable_trace(trace_size)
        rt.start(*my_workers)

        tg = rt.task_group()
        for i in range(num_columns):
            for j in range(num_channels):
                rt.fill(
                    of_ins[i * num_channels + j].prod(),
                    A,
                    taps_in[i * num_channels + j],
                    task_group=tg,
                )
        for i in range(num_columns):
            for j in range(num_channels):
                rt.drain(
                    of_outs[i * num_channels + j].cons(),
                    C,
                    taps_out[i * num_channels + j],
                    wait=True,
                    task_group=tg,
                )
        rt.finish_task_group(tg)

    return Program(dev, rt).resolve_program(SequentialPlacer())
