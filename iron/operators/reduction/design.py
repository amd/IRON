# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
MLIR Generation for Reduction Operator

Generates MLIR code for reduction operations (sum, mean, max, min)
on AIE2 (NPU) and AIE2P (NPU2) architectures.
"""

from ml_dtypes import bfloat16
from pathlib import Path
import numpy as np
import argparse
import sys

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_
from aie.helpers.util import np_ndarray_type_get_shape


def my_reduction(
    dev,
    input_size,
    reduction_size,
    num_columns,
    tile_size,
    reduction_op,
    trace_size,
):
    """
    Generate MLIR for reduction operation.

    Args:
        dev: AIE device (NPU1 or NPU2)
        input_size: Total size of input tensor
        reduction_size: Size of dimension being reduced
        num_columns: Number of AIE columns to use
        tile_size: Size of each tile
        reduction_op: Type of reduction ("sum", "mean", "max", "min")
        trace_size: Size of trace buffer

    Returns:
        MLIR module
    """
    # Calculate output size (input_size / reduction_size)
    output_size = input_size // reduction_size

    # Elements per tile across all columns
    per_tile_elements = tile_size
    n = per_tile_elements * num_columns

    if input_size % n != 0:
        raise ValueError(
            f"Input size ({input_size}) must be divisible by {n} (per_tile_elements * num_columns)."
        )

    # Number of tile iterations
    N_div_n = input_size // n

    # Chunk per column
    chunk = input_size // num_columns

    dtype = bfloat16

    # Define tensor types
    tensor_ty = np.ndarray[(input_size,), np.dtype[dtype]]
    output_ty = np.ndarray[(output_size,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    # AIE-array data movement with object fifos
    of_ins = [ObjectFifo(tile_ty, name=f"in_{i}") for i in range(num_columns)]
    of_outs = [ObjectFifo(tile_ty, name=f"out_{i}") for i in range(num_columns)]

    # Select kernel based on reduction op
    kernel_suffix = reduction_op
    eltwise_reduction = Kernel(
        f"reduction_{reduction_op}_bf16_vector",
        "reduction.o",
        [tile_ty, tile_ty, np.int32],
    )

    # Define a task that will run on a compute tile
    def core_body(of_in, of_out, reduction_kernel):
        # Number of sub-vector "tile" iterations
        for _ in range_(N_div_n):
            elem_in = of_in.acquire(1)
            elem_out = of_out.acquire(1)
            reduction_kernel(elem_in, elem_out, reduction_size)
            of_in.release(1)
            of_out.release(1)

    # Create a worker to run the task on a compute tile (one per column)
    my_workers = [
        Worker(
            core_body,
            [
                of_ins[i].cons(),
                of_outs[i].prod(),
                eltwise_reduction,
            ],
        )
        for i in range(num_columns)
    ]

    # Create a TensorAccessPattern for each column
    # The pattern chops the data in equal chunks and moves them in parallel
    taps = [
        TensorAccessPattern(
            (1, input_size),
            chunk * i,  # Start offset for column i
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    # Output taps
    output_chunk = output_size // num_columns
    output_taps = [
        TensorAccessPattern(
            (1, output_size),
            output_chunk * i,  # Start offset for column i
            [1, 1, 1, output_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(tensor_ty, output_ty) as (A, C):
        rt.start(*my_workers)

        # Initialize a group for parallel drain tasks
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(num_columns):
            rt.fill(
                of_ins[i].prod(),
                A,
                taps[i],
                task_group=tg,
            )

        # Drain the output objectFIFOs with data
        for i in range(num_columns):
            rt.drain(
                of_outs[i].cons(),
                C,
                output_taps[i],
                wait=True,  # wait for the transfer to complete
                task_group=tg,
            )

        rt.finish_task_group(tg)

    # Place program components and generate an MLIR module
    return Program(dev, rt).resolve_program(SequentialPlacer())


if __name__ == "__main__":

    def str_to_device(device: str):
        if device == "npu":
            return NPU1()
        elif device == "npu2":
            return NPU2()
        else:
            raise ValueError(f"Device name {device} is unknown.")

    p = argparse.ArgumentParser()

    # Device name is required
    p.add_argument(
        "-d",
        "--dev",
        required=True,
        dest="device",
        help="AIE Device (npu or npu2)",
        type=str_to_device,
    )

    # Input size
    p.add_argument(
        "-i", "--input-size", required=True, dest="input_size", help="Input size"
    )

    # Reduction size (size of dimension being reduced)
    p.add_argument(
        "-r",
        "--reduction-size",
        required=True,
        dest="reduction_size",
        help="Reduction size",
    )

    # Number of columns
    p.add_argument(
        "-co", "--columns", required=True, dest="cols", help="Number of columns"
    )

    # Tile size
    p.add_argument(
        "-ts",
        "--tile-size",
        required=False,
        dest="tile_size",
        default="1024",
        help="Tile size (elements per tile)",
    )

    # Reduction operation
    p.add_argument(
        "-op",
        "--reduction-op",
        required=False,
        dest="reduction_op",
        default="sum",
        help="Reduction operation (sum, mean, max, min)",
        choices=["sum", "mean", "max", "min"],
    )

    # Trace Size
    p.add_argument(
        "-t", "--trace-size", required=True, dest="trace_size", help="Trace size"
    )

    p.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )

    opts = p.parse_args(sys.argv[1:])

    input_size = int(opts.input_size)
    reduction_size = int(opts.reduction_size)
    columns = int(opts.cols)
    dev = opts.device

    # Validate columns based on device type
    if isinstance(dev, NPU1) and columns > 4:
        raise ValueError("[ERROR] NPU device cannot allocate more than 4 columns")
    elif isinstance(dev, NPU2) and columns > 8:
        raise ValueError("[ERROR] NPU2 device cannot allocate more than 8 columns")

    tile_size = int(opts.tile_size)
    reduction_op = opts.reduction_op

    # Mean is only supported on AIE2P
    if reduction_op == "mean" and isinstance(dev, NPU1):
        print(
            "[WARNING] Mean reduction is only supported on AIE2P (npu2). Falling back to sum."
        )
        reduction_op = "sum"

    if input_size % (tile_size * columns) != 0:
        print(
            "Input size ("
            + str(input_size)
            + ") must be a multiple of "
            + str(tile_size * columns)
            + " (tile_size * columns)"
        )
        raise ValueError

    trace_size = int(opts.trace_size) if opts.trace_size is not None else 0

    module = my_reduction(
        dev, input_size, reduction_size, columns, tile_size, reduction_op, trace_size
    )

    output_file_path = Path(opts.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
