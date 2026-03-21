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


def my_weighted_rms_norm(
    dev, num_elements, num_columns, num_channels, weight_length, trace_size
):
    per_tile_elements = weight_length
    total_cores = num_columns  # For each core that does rms norm, another core will take its output to do eltwise mul
    n = per_tile_elements * total_cores
    if num_elements % n != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {n}."
        )
    N_div_n = num_elements // n
    chunk = num_elements // total_cores
    dtype = bfloat16
    # Define tensor types
    tensor_ty = np.ndarray[(num_elements,), np.dtype[dtype]]
    weights_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    # P1-HIGH FIX: Enhanced adaptive ObjectFifo depth for bandwidth/stability regressions
    # Issues:
    #   - 1-col/2-ch: -22.59% to -31.19% bandwidth, +45.30% latency (weighted_rms_norm_1_cols_2_channels_2048_weights_2048)
    #   - 8-col/2-ch: +67.90% latency stddev explosion (weighted_rms_norm_8_cols_2_channels_2048_weights_256)
    # Source: weightrmsnorm.txt benchmark file (897d04e vs 84d3478)
    # Depth=5 for 8+ columns (stddev fix)
    # Depth=4 for 1-col/2-ch (bandwidth fix)
    # Depth=3 for 4-col/2-ch
    # Depth=2 for 2-col/2-ch or large tiles (>=1024)
    # Depth=1 baseline
    fifodepth = (
        5 if num_columns >= 8 else
        (4 if num_channels == 2 and num_columns == 1 else
         (3 if num_columns >= 4 and num_channels == 2 else
          (2 if num_channels == 2 or weight_length >= 1024 else 1))))

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(tile_ty, name=f"in1_{i}", depth=fifodepth)
        for i in range(total_cores)
    ]
    of_in2s = ObjectFifo(weights_ty, name=f"in2_weights", depth=fifodepth)
    of_out1s = [
        ObjectFifo(tile_ty, name=f"out1_{i}", depth=fifodepth)
        for i in range(total_cores)
    ]
    of_out2s = [
        ObjectFifo(tile_ty, name=f"out2_{i}", depth=fifodepth)
        for i in range(total_cores)
    ]

    # AIE Core Function declaration
    rms_norm_kernel = Kernel(
        "rms_norm_bf16_vector", "rms_norm_archive.a", [tile_ty, tile_ty, np.int32]
    )
    eltwise_mul_kernel = Kernel(
        "eltwise_mul_bf16_vector",
        "rms_norm_archive.a",
        [tile_ty, weights_ty, tile_ty, np.int32],
    )

    # Define a task that will run on a compute tile
    def core_body_norm(of_in1, of_out1, rms_norm):
        # Number of sub-vector "tile" iterations
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out1.acquire(1)
            rms_norm(elem_in1, elem_out, per_tile_elements)
            of_in1.release(1)
            of_out1.release(1)

    def core_body_mul(of_in1, of_in2, of_out2, eltwise_mul):
        # Number of sub-vector "tile" iterations
        elem_in2 = of_in2.acquire(1)
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out2.acquire(1)
            eltwise_mul(elem_in1, elem_in2, elem_out, per_tile_elements)
            of_in1.release(1)
            of_out2.release(1)
        of_in2.release(1)

    # Create workers to run the task on compute tiles,
    # one core for rms norm and another pipelined to do eltwise mul
    my_workers = []
    for i in range(total_cores):
        my_workers.append(
            Worker(
                core_body_norm,
                [
                    of_in1s[i].cons(),
                    of_out1s[i].prod(),
                    rms_norm_kernel,
                ],
            )
        )
    for i in range(total_cores):
        my_workers.append(
            Worker(
                core_body_mul,
                [
                    of_out1s[i].cons(),
                    of_in2s.cons(),
                    of_out2s[i].prod(),
                    eltwise_mul_kernel,
                ],
            )
        )

    # Create a TensorAccessPattern for each core
    # to describe the data movement
    # The pattern chops the data in equal chunks
    # and moves them in parallel across the cores.
    taps = [
        TensorAccessPattern(
            (1, num_elements),
            chunk * i,
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(total_cores)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(tensor_ty, weights_ty, tensor_ty) as (A, B, C):
        rt.start(*my_workers)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(total_cores):
            rt.fill(
                of_in1s[i].prod(),
                A,
                taps[i],
                task_group=tg,
            )
        rt.fill(
            of_in2s.prod(),
            B,
            task_group=tg,
        )
        # Drain the output objectFIFOs with data
        for i in range(total_cores):
            rt.drain(
                of_out2s[i].cons(),
                C,
                taps[i],
                wait=True,
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
    # Weight length
    p.add_argument(
        "-wl",
        "--weight-length",
        required=True,
        dest="weight_length",
        help="Weight vector length",
    )
    # Trace Size
    p.add_argument(
        "-ts", "--trace-size", required=True, dest="trace_size", help="Trace size"
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
    weight_length = int(opts.weight_length)
    # For weighted RMS norm: cores = columns (weights are broadcasted)
    total_cores = columns
    if (length % (weight_length * total_cores)) != 0:
        print(
            "transfer size ("
            + str(length)
            + ") must be a multiple of weight_length * total_cores ("
            + str(weight_length * total_cores)
            + ")"
        )
        raise ValueError
    trace_size = int(opts.trace_size) if opts.trace_size is not None else 0

    module = my_weighted_rms_norm(
        dev, length, columns, channels, weight_length, trace_size
    )

    output_file_path = Path(opts.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
