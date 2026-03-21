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


def my_dequant_kernel(
    dev, num_elements, num_columns, num_channels, trace_size, tile_size, group_size
):
    per_tile_elements = (
        16384 if tile_size > 16384 else tile_size
    )  # Largest tile size for 64KB in L1 and possible
    # group size of 1 with objfifo depth of 1
    n = per_tile_elements * num_columns
    if num_elements % n != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {n}."
        )
    N_div_n = num_elements // n
    chunk = num_elements // num_columns // num_channels  # For offset calculation
    in_dtype = np.uint8
    out_dtype = bfloat16

    # Input data: int4 packed data + scale factors
    # For N int4 values, we need N/2 bytes + N/group_size scale factors (bfloat16, 2 bytes each)
    input_tensor_size = (num_elements // 2) + (num_elements // group_size) * 2
    input_tile_size = (per_tile_elements // 2) + (per_tile_elements // group_size) * 2

    # Define tensor types
    in_tensor_ty = np.ndarray[(input_tensor_size,), np.dtype[in_dtype]]
    out_tensor_ty = np.ndarray[(num_elements,), np.dtype[out_dtype]]
    in_tile_ty = np.ndarray[(input_tile_size,), np.dtype[in_dtype]]
    out_tile_ty = np.ndarray[(per_tile_elements,), np.dtype[out_dtype]]

    # P0-P1 DEQUANT FIX: Enhanced ObjectFifo depth for stddev and bandwidth regressions
    #
    # P0-CRITICAL - Stddev explosions (latency stability):
    #   - dequant_2_cols_2_channels_2048_tile_512: +280.15% stddev -> depth=4
    #   - dequant_4_cols_1_channels_2048_tile_512: +194.26% stddev -> depth=4
    #   - dequant_1_cols_2_channels_2048_tile_1024_0: +149.23% stddev -> depth=4
    #
    # P0-CRITICAL - Bandwidth regressions:
    #   - dequant_8_cols_1_channels_2048_tile_256_0: -25.19% BW -> depth=4
    #   - dequant_8_cols_2_channels_2048_tile_128_0: -26.69% BW -> depth=4
    #
    # P1-HIGH:
    #   - dequant_1_cols_1_channels_2048_tile_2048: -18.83% BW -> depth=2+tile_factor
    #   - dequant_2_cols_1_channels_2048_tile_1024: +78.52% stddev -> depth=4
    #   - dequant_8_cols_2_channels_2048_tile_128: +87.19% stddev -> depth=4
    #
    # FIFO Depth Formula (UPDATED with tile_size_factor):
    #   Base depth: 4 for 2+ columns OR 2 channels (stability)
    #   For 1-column/1-channel: Use tile_size_factor for DMA pre-fetch optimization
    #   - tile_size <= 256: factor = 3 (very small tiles, max DMA pre-fetch)
    #   - tile_size < 512: factor = 2 (small tiles need +2 depth)
    #   - tile_size < 1024: factor = 1 (moderate tiles need +1 depth)
    #   - tile_size >= 1024: factor = 0 (large tiles have natural buffering)
    #   Clamped to range [2, 8]
    #
    # TILE SIZE FACTOR RATIONALE:
    # Smaller tiles complete compute faster, requiring deeper FIFOs for DMA pre-fetch
    # to stay ahead. Pattern consistent with MEM_COPY and AXPY operators.
    if num_columns >= 2 or num_channels == 2:
        # Multi-column or 2-channel: fixed depth=4 for stability
        fifodepth = 4
    else:
        # 1-column/1-channel: use tile_size_factor for optimal DMA pre-fetch
        base_depth = 2
        tile_size_factor = 0
        if tile_size <= 256:
            tile_size_factor = 3  # Very small tiles - maximum DMA pre-fetch needed
        elif tile_size < 512:
            tile_size_factor = 2  # Small tiles need +2 depth
        elif tile_size < 1024:
            tile_size_factor = 1  # Moderate tiles need +1 depth
        fifodepth = max(2, min(8, base_depth + tile_size_factor))
    enable_trace = 1 if trace_size > 0 else None

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(in_tile_ty, name=f"in1_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(out_tile_ty, name=f"out_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # AIE Core Function declaration
    dequant_kernel = Kernel(
        "expand_int4_to_bfloat16",
        f"expand_aie2_{tile_size}.o",
        [in_tile_ty, out_tile_ty],
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_out, dequant_kernel):
        # Number of sub-vector "tile" iterations
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out.acquire(1)
            dequant_kernel(elem_in1, elem_out)
            of_in1.release(1)
            of_out.release(1)

    # Create a worker to run the task on a compute tile
    my_workers = [
        Worker(
            core_body,
            [
                of_in1s[i * num_channels + j].cons(),
                of_outs[i * num_channels + j].prod(),
                dequant_kernel,
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
    in_chunk = (chunk // 2) + (chunk // group_size) * 2
    taps_in = [
        TensorAccessPattern(
            (1, input_tensor_size),
            in_chunk * i * num_channels + in_chunk * j,
            [1, 1, 1, in_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    taps_out = [
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
    with rt.sequence(in_tensor_ty, out_tensor_ty) as (A, C):
        if enable_trace:
            rt.enable_trace(trace_size)
        rt.start(*my_workers)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = rt.task_group()

        # Fill the input objectFIFOs with data
        for i in range(num_columns):
            for j in range(num_channels):
                rt.fill(
                    of_in1s[i * num_channels + j].prod(),
                    A,
                    taps_in[i * num_channels + j],
                    task_group=tg,
                )
        # Drain the output objectFIFOs with data
        for i in range(num_columns):
            for j in range(num_channels):
                rt.drain(
                    of_outs[i * num_channels + j].cons(),
                    C,
                    taps_out[i * num_channels + j],
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
    # It must be a multiple of tile size and divisible by the number of columns and 2 channels per column
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
    # Group size (elements per scaling factor)
    p.add_argument(
        "-gs",
        "--group_size",
        required=False,
        dest="group_size",
        default="32",
        help="Dequantization group size (super block size)",
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
    dev = opts.device

    # Validate columns based on device type
    if isinstance(dev, NPU1) and columns > 4:
        raise ValueError("[ERROR] NPU device cannot allocate more than 4 columns")
    elif isinstance(dev, NPU2) and columns > 8:
        raise ValueError("[ERROR] NPU2 device cannot allocate more than 8 columns")

    channels = int(opts.chans)
    if channels < 1 or channels > 2:
        raise ValueError("Number of channels must be 1 or 2")
    tile_size = int(opts.tile_size)
    group_size = int(opts.group_size)
    if (((length // 2) % tile_size) % columns % channels) != 0:
        print(
            "input transfer size in Bytes ("
            + str(length // 2)
            + ") must be a multiple of "
            + str(tile_size)
            + f" and divisible by the number of columns ({columns}) and {channels} channels per column"
        )
        raise ValueError
    if (((length * 2) % tile_size) % columns % channels) != 0:
        print(
            "output transfer size in Bytes ("
            + str(length * 2)
            + ") must be a multiple of "
            + str(tile_size)
            + f" and divisible by the number of columns ({columns}) and {channels} channels per column"
        )
        raise ValueError
    if tile_size % group_size != 0:
        print(f"Tile {tile_size} size must be a multiple of group size ({group_size})")
        raise ValueError
    trace_size = int(opts.trace_size) if opts.trace_size is not None else 0

    module = my_dequant_kernel(
        dev, length, columns, channels, trace_size, tile_size, group_size
    )

    output_file_path = Path(opts.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
