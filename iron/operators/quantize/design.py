# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_


def my_quantize_kernel(
    dev,
    num_elements,
    num_columns,
    num_channels,
    trace_size,
    tile_size,
    group_size,
):
    # Cap tile size to fit in L1 memory
    # bf16 input: tile_size*2 bytes
    # int8 output + scales: tile_size + (tile_size/group_size)*2 bytes
    # Total ~ tile_size*3 bytes; 16384 elements ~ 49KB fits in 64KB L1
    per_tile_elements = 16384 if tile_size > 16384 else tile_size
    total_cores = num_columns * num_channels
    per_core_elements = num_elements // total_cores
    if num_elements % total_cores != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {total_cores}."
        )
    N_div_n = per_core_elements // per_tile_elements
    chunk = num_elements // num_columns // num_channels

    in_dtype = bfloat16
    out_dtype = np.uint8

    # Input: bf16 values
    input_tensor_size = num_elements
    input_tile_size = per_tile_elements

    # Output: int8 data + bf16 scale factors (packed as uint8)
    output_tensor_size = num_elements + (num_elements // group_size) * 2
    output_tile_size = per_tile_elements + (per_tile_elements // group_size) * 2

    # Define tensor types
    in_tensor_ty = np.ndarray[(input_tensor_size,), np.dtype[in_dtype]]
    out_tensor_ty = np.ndarray[(output_tensor_size,), np.dtype[out_dtype]]
    in_tile_ty = np.ndarray[(input_tile_size,), np.dtype[in_dtype]]
    out_tile_ty = np.ndarray[(output_tile_size,), np.dtype[out_dtype]]

    fifodepth = 1 if tile_size > 8192 else 2
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
    quantize_kernel = Kernel(
        "quantize_bfloat16_to_i8",
        f"quantize_bf16_i8_{tile_size}.o",
        [in_tile_ty, out_tile_ty],
    )

    # Core task
    def core_body(of_in, of_out, quantize_kernel):
        for _ in range_(N_div_n):
            elem_in = of_in.acquire(1)
            elem_out = of_out.acquire(1)
            quantize_kernel(elem_in, elem_out)
            of_in.release(1)
            of_out.release(1)

    # Workers
    my_workers = [
        Worker(
            core_body,
            [
                of_ins[i * num_channels + j].cons(),
                of_outs[i * num_channels + j].prod(),
                quantize_kernel,
            ],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # TensorAccessPatterns
    out_chunk = chunk + (chunk // group_size) * 2  # bytes per core in output
    taps_in = [
        TensorAccessPattern(
            (1, input_tensor_size),
            chunk * (i * num_channels + j),
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    taps_out = [
        TensorAccessPattern(
            (1, output_tensor_size),
            out_chunk * (i * num_channels + j),
            [1, 1, 1, out_chunk],
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
