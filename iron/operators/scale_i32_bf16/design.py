# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_


def my_scale_i32_bf16_kernel(
    dev,
    num_elements,
    num_columns,
    num_channels,
    trace_size,
    tile_size,
):
    # Cap tile size for L1 memory: i32 input (tile*4B) + bf16 output (tile*2B) + scale (32B)
    per_tile_elements = 8192 if tile_size > 8192 else tile_size
    total_cores = num_columns * num_channels
    per_core_elements = num_elements // total_cores
    if num_elements % total_cores != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {total_cores}."
        )
    N_div_n = per_core_elements // per_tile_elements

    # Types
    data_tile_ty = np.ndarray[(per_tile_elements,), np.dtype[np.int32]]
    data_tensor_ty = np.ndarray[(num_elements,), np.dtype[np.int32]]
    scale_tile_ty = np.ndarray[(16,), np.dtype[bfloat16]]  # 16 for DMA alignment
    scale_tensor_ty = np.ndarray[(total_cores * 16,), np.dtype[bfloat16]]
    out_tile_ty = np.ndarray[(per_tile_elements,), np.dtype[bfloat16]]
    out_tensor_ty = np.ndarray[(num_elements,), np.dtype[bfloat16]]

    fifodepth = 1 if tile_size > 4096 else 2
    enable_trace = trace_size > 0

    # ObjectFIFOs
    of_ins = [
        ObjectFifo(data_tile_ty, name=f"in_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    of_scales = [
        ObjectFifo(scale_tile_ty, name=f"scale_{i}_{j}", depth=1)
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(out_tile_ty, name=f"out_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # Kernel
    scale_kernel = Kernel(
        "scale_i32_to_bf16",
        f"scale_i32_bf16_{tile_size}.o",
        [data_tile_ty, scale_tile_ty, out_tile_ty, np.int32],
    )

    # Core task: acquire scale once, process all tiles
    def core_body(of_in, of_scale, of_out, kernel):
        elem_scale = of_scale.acquire(1)
        for _ in range_(N_div_n):
            elem_in = of_in.acquire(1)
            elem_out = of_out.acquire(1)
            kernel(elem_in, elem_scale, elem_out, per_tile_elements)
            of_in.release(1)
            of_out.release(1)
        of_scale.release(1)

    # Workers
    my_workers = [
        Worker(
            core_body,
            [
                of_ins[i * num_channels + j].cons(),
                of_scales[i * num_channels + j].cons(),
                of_outs[i * num_channels + j].prod(),
                scale_kernel,
            ],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # TensorAccessPatterns
    chunk = num_elements // total_cores  # elements per core
    data_taps = [
        TensorAccessPattern(
            (1, num_elements),
            chunk * (i * num_channels + j),
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    scale_taps = [
        TensorAccessPattern(
            (1, total_cores * 16),
            16 * (i * num_channels + j),
            [1, 1, 1, 16],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # Runtime
    rt = Runtime()
    with rt.sequence(data_tensor_ty, scale_tensor_ty, out_tensor_ty) as (A, S, C):
        if enable_trace:
            rt.enable_trace(trace_size)
        rt.start(*my_workers)

        tg = rt.task_group()
        for i in range(num_columns):
            for j in range(num_channels):
                idx = i * num_channels + j
                rt.fill(of_ins[idx].prod(), A, data_taps[idx], task_group=tg)
                rt.fill(of_scales[idx].prod(), S, scale_taps[idx], task_group=tg)
        for i in range(num_columns):
            for j in range(num_channels):
                idx = i * num_channels + j
                rt.drain(
                    of_outs[idx].cons(),
                    C,
                    data_taps[idx],
                    wait=True,
                    task_group=tg,
                )
        rt.finish_task_group(tg)

    return Program(dev, rt).resolve_program(SequentialPlacer())
