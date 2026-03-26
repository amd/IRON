# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Rotary Positional Encoding (RoPE) design

Applies RoPE to each row of the input tensor.
Expects input tensor of shape (rows, cols) and a tensor of precomputed angles (look-up table) of shape (angle_rows, cols).
Another interpretation of the input tensor is (rows / num_heads, num_heads, cols), where num_heads = rows / angle_rows.

- rows: number of rows in the input tensor (e.g., number of tokens)
- cols: number of columns in the input tensor (e.g., head dimension)
- angle_rows: number of input rows in the angle look-up table.
  If this is less than `rows`, each row of angles will be reused for `rows / angle_rows` consecutive rows of the input tensor.
  This is useful for models where multiple heads share the same positional encodings and the heads are 'interspersed' in the input tensor (i.e. input tensor shape is (rows, n_heads, cols)).
"""

import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.helpers.dialects.scf import _for as range_
from ml_dtypes import bfloat16


def rope(
    dev,
    rows,
    cols,
    angle_rows=None,
    num_aie_columns=1,
    trace_size=0,
    method_type=None,
    func_prefix="",
):
    dtype = bfloat16

    if angle_rows is None:
        angle_rows = rows
    kernel_object = (
        f"{func_prefix}rope"
        + (f"_{method_type}" if method_type is not None else "")
        + ".o"
    )

    assert cols % (16 * 2) == 0 and cols >= (
        16 * 2
    ), "cols must be multiple of 32 and >= 32 (rope.cc kernel processes two 16-element vectors at a time)"
    assert rows % num_aie_columns == 0, "rows must be divisible by num_aie_columns"
    assert angle_rows <= rows and rows % angle_rows == 0, "angle_rows must divide rows"
    assert (
        angle_rows >= num_aie_columns and angle_rows % num_aie_columns == 0
    ), "angle_rows must be divisible by num_aie_columns"

    tensor_rows_per_aie_column = rows // num_aie_columns
    angle_rows_per_aie_column = angle_rows // num_aie_columns
    tensor_rows_per_angle_row = rows // angle_rows

    # Define tensor types
    tensor_ty = np.ndarray[(rows, cols), np.dtype[dtype]]
    angle_ty = np.ndarray[(angle_rows, cols), np.dtype[dtype]]
    tensor_tile_ty = np.ndarray[(1, cols), np.dtype[dtype]]
    angle_tile_ty = np.ndarray[(1, cols), np.dtype[dtype]]

    # AIE-array data movement with object fifos (one per column, not per channel)
    of_in = [ObjectFifo(tensor_tile_ty, name=f"in_{i}") for i in range(num_aie_columns)]
    of_lut = [
        ObjectFifo(angle_tile_ty, name=f"lut_{i}") for i in range(num_aie_columns)
    ]
    of_out = [
        ObjectFifo(tensor_tile_ty, name=f"out_{i}") for i in range(num_aie_columns)
    ]

    # AIE Core Function declaration
    rope_kernel = Kernel(
        f"{func_prefix}rope",
        kernel_object,
        [tensor_tile_ty, angle_tile_ty, tensor_tile_ty, np.int32],
    )

    # Define a task that will run on a compute tile
    def core_body(of_in, of_lut, of_out, rope_kernel):
        # Number of sub-vector "tile" iterations
        for _ in range_(angle_rows_per_aie_column):
            elem_lut = of_lut.acquire(1)
            for _ in range_(tensor_rows_per_angle_row):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                rope_kernel(elem_in, elem_lut, elem_out, cols)
                of_in.release(1)
                of_out.release(1)
            of_lut.release(1)

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
    tensor_taps = [
        TensorAccessPattern(
            (rows, cols),
            i * tensor_rows_per_aie_column * cols,  # Start offset for column i
            [1, 1, 1, tensor_rows_per_aie_column * cols],
            [0, 0, 0, 1],
        )
        for i in range(num_aie_columns)
    ]
    angle_taps = [
        TensorAccessPattern(
            (angle_rows, cols),
            i * angle_rows_per_aie_column * cols,  # Start offset for column i
            [1, 1, 1, angle_rows_per_aie_column * cols],
            [0, 0, 0, 1],
        )
        for i in range(num_aie_columns)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(tensor_ty, angle_ty, tensor_ty) as (A, B, C):
        rt.start(*my_workers)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(num_aie_columns):
            rt.fill(
                of_in[i].prod(),
                A,
                tensor_taps[i],
                task_group=tg,
            )
            rt.fill(
                of_lut[i].prod(),
                B,
                angle_taps[i],
                task_group=tg,
            )
        # Drain the output objectFIFOs with data
        for i in range(num_aie_columns):
            rt.drain(
                of_out[i].cons(),
                C,
                tensor_taps[i],
                wait=True,  # wait for the transfer to complete and data to be available
                task_group=tg,
            )
        rt.finish_task_group(tg)

    # Place program components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt).resolve_program(SequentialPlacer())
