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
from aie.helpers.util import np_ndarray_type_get_shape


def my_layer_norm(dev, num_elements, num_columns, num_channels, trace_size, tile_size):
    per_tile_elements = 8192 if tile_size > 8192 else tile_size
    n = per_tile_elements * num_columns
    if num_elements % n != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {n}."
        )
    N_div_n = num_elements // n
    chunk = num_elements // num_columns // num_channels  # For offset calculation
    dtype = bfloat16

    # Define tensor types
    tensor_ty = np.ndarray[(num_elements,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    # LAYER_NORM FIX PLAN 2026-03-20: Enhanced ObjectFifo Depth for Multi-Column Stability
    # P0 FIX: +376.41% latency stddev (layer_norm_2_cols_2_channels_2048_tile_512)
    # P1 FIX: +57.24% latency stddev (layer_norm_4_cols_1_channels_2048_tile_512)
    # P1 FIX: +68.93% latency stddev (layer_norm_4_cols_2_channels_2048_tile_256)
    # P2 FIX: +32.41% bandwidth stddev (layer_norm_1_cols_2_channels_2048_tile_1024)
    # Source: layernorm.txt benchmark file
    # Conservative formula - only increase depth for known problematic configurations
    if num_columns == 2 and num_channels == 2 and tile_size <= 512:
        fifodepth = 4  # P0 fix for catastrophic 2-col 2-channel tile=512
    elif num_columns == 4 and num_channels == 2 and tile_size <= 512:
        fifodepth = 5  # P1 fix for 4-col 2-channel
    elif num_columns == 4 and num_channels == 1 and tile_size <= 512:
        fifodepth = 4  # P1 fix for 4-col 1-channel
    elif num_columns >= 8:
        # QM-004: 8-col configs get depth=4 regardless of channels because
        # higher column counts provide natural parallelism that stabilizes
        # data flow. Depth=4 has been proven stable across all 8-col
        # configurations in benchmark testing, so we use it as the baseline
        # for any configuration with 8 or more columns.
        fifodepth = 4  # 8+ columns: proven stable at depth=4 (inherent parallelism)
    elif num_channels == 2 and tile_size >= 1024:
        fifodepth = 3  # Moderate depth for large tiles with 2 channels
    else:
        fifodepth = 2  # Default for other configurations

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(tile_ty, name=f"in1_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(tile_ty, name=f"out_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # AIE Core Function declaration
    layer_norm_kernel = Kernel(
        "layer_norm", "layer_norm.o", [tile_ty, tile_ty, np.int32]
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_out, layer_norm_kernel):
        # Number of sub-vector "tile" iterations
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out.acquire(1)
            layer_norm_kernel(elem_in1, elem_out, per_tile_elements)
            of_in1.release(1)
            of_out.release(1)

    # Create a worker to run the task on a compute tile
    my_workers = [
        Worker(
            core_body,
            [
                of_in1s[i * num_channels + j].cons(),
                of_outs[i * num_channels + j].prod(),
                layer_norm_kernel,
            ],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # Create a TensorAccessPattern for each channel
    # to describe the data movement
    # The pattern chops the data in equal chunks
    # and moves them in parallel across the columns
    # and channels.
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
    with rt.sequence(tensor_ty, tensor_ty) as (A, C):
        rt.start(*my_workers)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(num_columns):
            for j in range(num_channels):
                rt.fill(
                    of_in1s[i * num_channels + j].prod(),
                    A,
                    taps[i * num_channels + j],
                    task_group=tg,
                )
        # Drain the output objectFIFOs with data
        for i in range(num_columns):
            for j in range(num_channels):
                rt.drain(
                    of_outs[i * num_channels + j].cons(),
                    C,
                    taps[i * num_channels + j],
                    wait=True,  # wait for the transfer to complete and data to be available
                    task_group=tg,
                )
        rt.finish_task_group(tg)

    # Place program components (assign them resources on the device) and generate an MLIR module
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
    # Parse command line arguments

    # Device name is required to select the AIE device: npu or npu2
    p.add_argument(
        "-d",
        "--dev",
        required=True,
        dest="device",
        help="AIE Device",
        type=str_to_device,
    )
    # Transfer size is required to define the size of the data to be transferred
    # It must be a multiple of 1024 and divisible by the number of columns and 2 channels per column
    p.add_argument("-l", "--length", required=True, dest="length", help="Transfer size")
    # Number of columns is required to define the number of columns to be used
    # It must be less than or equal to 4 for npu and 8 for npu2
    p.add_argument(
        "-co", "--columns", required=True, dest="cols", help="Number of columns"
    )
    # Number of channels is required to define the number of channels to be used
    # It must be 1 or 2
    p.add_argument(
        "-ch", "--channels", required=True, dest="chans", help="Number of channels"
    )
    # Tile size (columns per tile) - defaults to 1024 for backward compatibility
    p.add_argument(
        "-ts",
        "--tile-size",
        required=False,
        dest="tile_size",
        default="1024",
        help="Tile size (columns per tile)",
    )
    # Trace Size
    p.add_argument(
        "-tr", "--trace-size", required=True, dest="trace_size", help="Trace size"
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
    dev = opts.device  # Now this is already a device object!

    # Validate columns based on device type
    if isinstance(dev, NPU1) and columns > 4:
        raise ValueError("[ERROR] NPU device cannot allocate more than 4 columns")
    elif isinstance(dev, NPU2) and columns > 8:
        raise ValueError("[ERROR] NPU2 device cannot allocate more than 8 columns")

    channels = int(opts.chans)
    if channels < 1 or channels > 2:
        raise ValueError("Number of channels must be 1 or 2")
    tile_size = int(opts.tile_size)
    if ((length % tile_size) % columns % channels) != 0:
        print(
            "transfer size ("
            + str(length)
            + ") must be a multiple of "
            + str(tile_size)
            + " and divisible by the number of columns and 2 channels per column"
        )
        raise ValueError
    trace_size = int(opts.trace_size) if opts.trace_size is not None else 0

    module = my_layer_norm(dev, length, columns, channels, trace_size, tile_size)

    output_file_path = Path(opts.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
