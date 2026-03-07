# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

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


def my_silu_mul(dev, num_elements, num_columns, num_channels, tile_size, trace_size):
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

    # AIE-array data movement with object fifos (one per column)
    of_in1s = [ObjectFifo(tile_ty, name=f"in1_{i}") for i in range(num_columns)]
    of_in2s = [ObjectFifo(tile_ty, name=f"in2_{i}") for i in range(num_columns)]
    of_outs = [ObjectFifo(tile_ty, name=f"out_{i}") for i in range(num_columns)]

    # AIE Core Function declaration
    silu_mul_bf16 = Kernel(
        "silu_mul_bf16", "silu_mul.o", [tile_ty, tile_ty, tile_ty, np.int32]
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_in2, of_out, silu_mul_fn):
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_in2 = of_in2.acquire(1)
            elem_out = of_out.acquire(1)
            silu_mul_fn(elem_in1, elem_in2, elem_out, per_tile_elements)
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
                silu_mul_bf16,
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
    rt = Runtime()
    with rt.sequence(tensor_ty, tensor_ty, tensor_ty) as (A, B, C):
        rt.start(*my_workers)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(num_columns):
            rt.fill(
                of_in1s[i].prod(),
                A,
                taps[i],
                task_group=tg,
            )
            rt.fill(
                of_in2s[i].prod(),
                B,
                taps[i],
                task_group=tg,
            )
        # Drain the output objectFIFOs with data
        for i in range(num_columns):
            rt.drain(
                of_outs[i].cons(),
                C,
                taps[i],
                wait=True,
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
    p.add_argument(
        "-d",
        "--dev",
        required=True,
        dest="device",
        help="AIE Device",
        type=str_to_device,
    )
    p.add_argument("-l", "--length", required=True, dest="length", help="Transfer size")
    p.add_argument(
        "-co", "--columns", required=True, dest="cols", help="Number of columns"
    )
    p.add_argument(
        "-ch", "--channels", required=True, dest="chans", help="Number of channels"
    )
    p.add_argument(
        "-ts",
        "--tile-size",
        required=False,
        dest="tile_size",
        default="1024",
        help="Tile size (elements per tile)",
    )
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

    length = int(opts.length)
    columns = int(opts.cols)
    dev = opts.device

    if isinstance(dev, NPU1) and columns > 4:
        raise ValueError("[ERROR] NPU device cannot allocate more than 4 columns")
    elif isinstance(dev, NPU2) and columns > 8:
        raise ValueError("[ERROR] NPU2 device cannot allocate more than 8 columns")

    channels = int(opts.chans)
    if channels < 1 or channels > 2:
        raise ValueError("Number of channels must be 1 or 2")
    tile_size = int(opts.tile_size)
    if length % (tile_size * columns) != 0:
        print(
            "transfer size ("
            + str(length)
            + ") must be a multiple of "
            + str(tile_size * columns)
            + " (tile_size * columns)"
        )
        raise ValueError
    trace_size = int(opts.trace_size) if opts.trace_size is not None else 0

    module = my_silu_mul(dev, length, columns, channels, tile_size, trace_size)

    output_file_path = Path(opts.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
