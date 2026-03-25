# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_


def my_silu(
    dev, size, num_columns, tile_size, trace_size, kernel_archive, func_prefix=""
):
    xfr_dtype = bfloat16
    # Cap to 4096 bfloat16 elements (8 KB) to fit AIE core local memory
    line_size = 4096 if tile_size > 4096 else tile_size
    line_type = np.ndarray[(line_size,), np.dtype[xfr_dtype]]
    transfer_type = np.ndarray[(size,), np.dtype[xfr_dtype]]

    # Calculate number of iterations per core
    per_core_elements = size // num_columns
    N_div_n = per_core_elements // line_size

    # Chunk size sent per DMA channel
    chunk = size // num_columns

    # Dataflow with ObjectFifos
    of_ins = [ObjectFifo(line_type, name=f"in{i}") for i in range(num_columns)]
    of_outs = [ObjectFifo(line_type, name=f"out{i}") for i in range(num_columns)]

    # External, binary kernel definition
    silu_fcn = Kernel(
        f"{func_prefix}silu_bf16",
        kernel_archive,
        [line_type, line_type, np.int32],
    )

    # Task for the core to perform
    def core_fn(of_in, of_out, silu_line):
        for _ in range_(N_div_n):
            elem_in = of_in.acquire(1)
            elem_out = of_out.acquire(1)
            silu_line(elem_in, elem_out, line_size)
            of_in.release(1)
            of_out.release(1)

    # Create a worker to perform the task
    my_workers = [
        Worker(
            core_fn,
            [
                of_ins[i].cons(),
                of_outs[i].prod(),
                silu_fcn,
            ],
        )
        for i in range(num_columns)
    ]

    # Create a TensorAccessPattern for each channel
    # to describe the data movement
    # The pattern chops the data in equal chunks
    # and moves them in parallel across the columns.
    taps = [
        TensorAccessPattern(
            (1, size),
            chunk * i,
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(transfer_type, transfer_type) as (
        a_in,
        b_out,
    ):
        rt.start(*my_workers)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(num_columns):
            rt.fill(
                of_ins[i].prod(),
                a_in,
                taps[i],
                task_group=tg,
            )
        # Drain the output objectFIFOs with data
        for i in range(num_columns):
            rt.drain(
                of_outs[i].cons(),
                b_out,
                taps[i],
                wait=True,  # wait for the transfer to complete and data to be available
                task_group=tg,
            )
        rt.finish_task_group(tg)

    # Place components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt).resolve_program(SequentialPlacer())
