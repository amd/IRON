# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_
from iron.operators._trace import maybe_enable_trace


def binary_elementwise_design(
    dev,
    num_elements,
    num_columns,
    tile_size,
    trace_size,
    kernel_fn_name,
    kernel_obj_file,
    func_prefix="",
):
    per_tile_elements = 4096 if tile_size > 4096 else tile_size
    n = per_tile_elements * num_columns
    if num_elements % n != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {n}."
        )
    N_div_n = num_elements // n
    chunk = num_elements // num_columns
    dtype = bfloat16

    # Define tensor types
    tensor_ty = np.ndarray[(num_elements,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    # AIE-array data movement with object fifos (one per column, not per channel)
    of_in1s = [ObjectFifo(tile_ty, name=f"in1_{i}") for i in range(num_columns)]
    of_in2s = [ObjectFifo(tile_ty, name=f"in2_{i}") for i in range(num_columns)]
    of_outs = [ObjectFifo(tile_ty, name=f"out_{i}") for i in range(num_columns)]

    # AIE Core Function declaration
    eltwise_kernel = Kernel(
        f"{func_prefix}{kernel_fn_name}",
        f"{func_prefix}{kernel_obj_file}",
        [tile_ty, tile_ty, tile_ty, np.int32],
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_in2, of_out, eltwise_fn):
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_in2 = of_in2.acquire(1)
            elem_out = of_out.acquire(1)
            eltwise_fn(elem_in1, elem_in2, elem_out, per_tile_elements)
            of_in1.release(1)
            of_in2.release(1)
            of_out.release(1)

    # Create a worker to run the task on a compute tile (one per column)
    my_workers = [
        Worker(
            core_body,
            [
                of_in1s[i].cons(),
                of_in2s[i].cons(),
                of_outs[i].prod(),
                eltwise_kernel,
            ],
        )
        for i in range(num_columns)
    ]

    # Create a TensorAccessPattern for each column
    taps = [
        TensorAccessPattern(
            (1, num_elements),
            chunk * i,
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    # Runtime operations to move data to/from the AIE-array
    def sequence(A, B, C, in1_prods, in2_prods, out_conses):
        tg = TaskGroup()

        # Fill the input objectFIFOs with data
        for i in range(num_columns):
            in1_prods[i].fill(
                A,
                taps[i],
                group=tg,
            )
            in2_prods[i].fill(
                B,
                taps[i],
                group=tg,
            )
        # Drain the output objectFIFOs with data
        for i in range(num_columns):
            out_conses[i].drain(
                C,
                taps[i],
                wait=True,
                group=tg,
            )
        tg.finish()

    rt = Runtime(
        sequence,
        [
            tensor_ty,
            tensor_ty,
            tensor_ty,
            [of_in1s[i].prod() for i in range(num_columns)],
            [of_in2s[i].prod() for i in range(num_columns)],
            [of_outs[i].cons() for i in range(num_columns)],
        ],
    )

    # Place program components and generate an MLIR module
    prog = Program(dev, rt, workers=my_workers)
    maybe_enable_trace(prog, trace_size, my_workers)
    return prog.resolve_program()
