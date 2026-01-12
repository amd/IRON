# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from pathlib import Path
import numpy as np
import argparse
import sys

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.helpers.dialects.ext.scf import _for as range_
from ml_dtypes import bfloat16


def rope(
    dev,
    rows,
    cols,
    num_aie_columns=1,
    trace_size=0,
    method_type=None,
):
    dtype = bfloat16
    assert cols % (16 * 2) == 0 and cols >= (16 * 2), "cols must be multiple of 32 and >= 32 (rope.cc kernel processes two 16-element vectors at a time)"

    assert rows % num_aie_columns == 0, "rows must be divisible by num_aie_columns"
    column_chunk_rows = rows // num_aie_columns

    # Define tensor types
    tensor_ty = np.ndarray[(rows, cols), np.dtype[dtype]]
    tile_ty = np.ndarray[(1, cols), np.dtype[dtype]]

    # AIE-array data movement with object fifos (one per column, not per channel)
    of_in = [ObjectFifo(tile_ty, name=f"in_{i}") for i in range(num_aie_columns)]
    of_lut = [ObjectFifo(tile_ty, name=f"lut_{i}") for i in range(num_aie_columns)]
    of_out = [ObjectFifo(tile_ty, name=f"out_{i}") for i in range(num_aie_columns)]

    # AIE Core Function declaration
    rope_kernel = Kernel(
        "rope",
        "rope" + (f"_{method_type}" if method_type is not None else "") + ".o",
        [tile_ty, tile_ty, tile_ty, np.int32],
    )

    # Define a task that will run on a compute tile
    def core_body(of_in, of_lut, of_out, rope_kernel):
        # Number of sub-vector "tile" iterations
        for _ in range_(column_chunk_rows):
            elem_in = of_in.acquire(1)
            elem_lut = of_lut.acquire(1)
            elem_out = of_out.acquire(1)
            rope_kernel(elem_in, elem_lut, elem_out, cols)
            of_in.release(1)
            of_lut.release(1)
            of_out.release(1)

    # Create a worker to run the task on a compute tile (one per column)
    my_workers = [
        Worker(
            core_body,
            [
                of_in[i].cons(),
                of_lut[i].cons(),
                of_out[i].prod(),
                rope_kernel,
            ],
        )
        for i in range(num_aie_columns)
    ]

    # This pattern chops the data into equal chunks and moves them in parallel across the columns
    taps = [
        TensorAccessPattern(
            (1, rows * cols),
            i * column_chunk_rows * cols,  # Start offset for column i
            [1, 1, 1, column_chunk_rows * cols],
            [0, 0, 0, 1],
        )
        for i in range(num_aie_columns)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(tensor_ty, tensor_ty, tensor_ty) as (A, B, C):
        rt.start(*my_workers)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(num_aie_columns):
            rt.fill(
                of_in[i].prod(),
                A,
                taps[i],
                task_group=tg,
            )
            rt.fill(
                of_lut[i].prod(),
                B,
                taps[i],
                task_group=tg,
            )
        # Drain the output objectFIFOs with data
        for i in range(num_aie_columns):
            rt.drain(
                of_out[i].cons(),
                C,
                taps[i],
                wait=True,  # wait for the transfer to complete and data to be available
                task_group=tg,
            )
        rt.finish_task_group(tg)

    # Place program components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt).resolve_program(SequentialPlacer())
