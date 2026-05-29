# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
MLIR Generation for MaxPool Operator

Generates MLIR for max pooling operations on AIE2 (NPU) and AIE2P (NPU2) architectures.
"""

# =============================================================================
# MODELING STATUS (post Modeling Pass - maxpool)
# =============================================================================
# - No bias, no kernel variants (symmetric to avgpool).
# - Chunk/tile consistency + honest docs added (identical improvements).
# - range_(1) + skeleton rationale documented.
# =============================================================================

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


def my_max_pool2d(
    dev,
    N,  # batch size
    channels,
    in_height,
    in_width,
    out_height,
    out_width,
    kernel_h,
    kernel_w,
    stride_h,
    stride_w,
    pad_h,
    pad_w,
    num_columns,
    tile_size,
    trace_size,
):
    """
    Generate MLIR for 2D max pooling operation.

    Args:
        dev: AIE device (NPU1 or NPU2)
        N: Batch size
        channels: Number of channels
        in_height: Input height
        in_width: Input width
        out_height: Output height
        out_width: Output width
        kernel_h: Kernel height
        kernel_w: Kernel width
        stride_h: Stride height
        stride_w: Stride width
        pad_h: Padding height
        pad_w: Padding width
        num_columns: Number of AIE columns to use
        tile_size: Size of each tile
        trace_size: Size of trace buffer

    Returns:
        MLIR module
    """
    dtype = bfloat16

    # Calculate tensor sizes
    input_size = N * channels * in_height * in_width
    output_size = N * channels * out_height * out_width

    # Define tensor types
    input_ty = np.ndarray[(input_size,), np.dtype[dtype]]
    output_ty = np.ndarray[(output_size,), np.dtype[dtype]]

    # Per-column chunks for FIFO types (TAP consistency)
    input_chunk = input_size // num_columns if num_columns > 0 else input_size
    output_chunk = output_size // num_columns if num_columns > 0 else output_size

    input_tile_ty = np.ndarray[
        (input_chunk if input_chunk > 0 else 1,), np.dtype[dtype]
    ]
    output_tile_ty = np.ndarray[
        (output_chunk if output_chunk > 0 else 1,), np.dtype[dtype]
    ]

    # P2-11 FIX: Explicit ObjectFifo depth calculation for MaxPool stability
    # (parity with Conv3D gold: Depth=4 for 8+ cols, 3 for 4+ cols, 2 for 2+ cols;
    # depth=1 fallback only for very large tiles on tiny col counts)
    fifodepth = (
        4
        if num_columns >= 8
        else (
            3
            if num_columns >= 4
            else (2 if num_columns >= 2 else (1 if tile_size > 4096 else 2))
        )
    )

    # AIE-array data movement with object fifos (explicit depth for column stability)
    of_ins = [
        ObjectFifo(input_tile_ty, name=f"in_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]
    of_outs = [
        ObjectFifo(output_tile_ty, name=f"out_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]

    # Kernel name
    kernel_name = "max_pool2d_bf16_vector"

    # AIE Core Function declaration (matches max_pool2d_bf16_vector exactly)
    maxpool_kernel = Kernel(
        kernel_name,
        "maxpool.o",
        [
            input_tile_ty,
            output_tile_ty,
            np.int32,  # N
            np.int32,  # channels
            np.int32,  # in_height
            np.int32,  # in_width
            np.int32,  # out_height
            np.int32,  # out_width
            np.int32,  # kernel_h
            np.int32,  # kernel_w
            np.int32,  # stride_h
            np.int32,  # stride_w
            np.int32,  # pad_h
            np.int32,  # pad_w
        ],
    )

    # Define a task that will run on a compute tile
    def core_body(of_in, of_out, pool_kernel):
        # Single chunk transfer (see MODELING STATUS for rationale)
        for _ in range_(1):
            elem_in = of_in.acquire(1)
            elem_out = of_out.acquire(1)

            pool_kernel(
                elem_in,
                elem_out,
                N,
                channels,
                in_height,
                in_width,
                out_height,
                out_width,
                kernel_h,
                kernel_w,
                stride_h,
                stride_w,
                pad_h,
                pad_w,
            )

            of_in.release(1)
            of_out.release(1)

    # Create workers (one per column)
    my_workers = [
        Worker(
            core_body,
            [
                of_ins[i].cons(),
                of_outs[i].prod(),
                maxpool_kernel,
            ],
            while_true=False,
        )
        for i in range(num_columns)
    ]

    # Create TensorAccessPatterns for data movement (chunks match FIFO types)
    input_taps = [
        TensorAccessPattern(
            (1, input_size),
            input_chunk * i,
            [1, 1, 1, input_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    output_taps = [
        TensorAccessPattern(
            (1, output_size),
            output_chunk * i,
            [1, 1, 1, output_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(input_ty, output_ty) as (A, C):
        rt.start(*my_workers)

        # Initialize a group for parallel tasks
        tg = rt.task_group()

        # Fill input objectFIFOs
        for i in range(num_columns):
            rt.fill(
                of_ins[i].prod(),
                A,
                input_taps[i],
                task_group=tg,
            )

        # Drain output objectFIFOs
        for i in range(num_columns):
            rt.drain(
                of_outs[i].cons(),
                C,
                output_taps[i],
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

    # Device
    p.add_argument(
        "-d",
        "--dev",
        required=True,
        dest="device",
        help="AIE Device (npu or npu2)",
        type=str_to_device,
    )

    # Batch size
    p.add_argument("-N", "--batch", type=int, default=1, help="Batch size")

    # Input dimensions
    p.add_argument("-c", "--channels", type=int, required=True, help="Channels")
    p.add_argument("-ih", "--in-height", type=int, required=True, help="Input height")
    p.add_argument("-iw", "--in-width", type=int, required=True, help="Input width")

    # Kernel parameters
    p.add_argument("-kh", "--kernel-h", type=int, default=2, help="Kernel height")
    p.add_argument("-kw", "--kernel-w", type=int, default=2, help="Kernel width")

    # Stride
    p.add_argument("-sh", "--stride-h", type=int, default=2, help="Stride height")
    p.add_argument("-sw", "--stride-w", type=int, default=2, help="Stride width")

    # Padding
    p.add_argument("-ph", "--pad-h", type=int, default=0, help="Padding height")
    p.add_argument("-pw", "--pad-w", type=int, default=0, help="Padding width")

    # Number of columns
    p.add_argument(
        "-co", "--columns", type=int, default=4, help="Number of AIE columns"
    )

    # Tile size
    p.add_argument("-ts", "--tile-size", type=int, default=1024, help="Tile size")

    # Trace size
    p.add_argument("-t", "--trace-size", type=int, default=0, help="Trace size")

    p.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )

    opts = p.parse_args(sys.argv[1:])

    dev = opts.device
    N = opts.batch
    channels = opts.channels
    in_height = opts.in_height
    in_width = opts.in_width
    kernel_h = opts.kernel_h
    kernel_w = opts.kernel_w
    stride_h = opts.stride_h
    stride_w = opts.stride_w
    pad_h = opts.pad_h
    pad_w = opts.pad_w
    columns = opts.columns
    tile_size = opts.tile_size
    trace_size = opts.trace_size

    # Validate columns based on device type
    if isinstance(dev, NPU1) and columns > 4:
        raise ValueError("[ERROR] NPU device cannot allocate more than 4 columns")
    elif isinstance(dev, NPU2) and columns > 8:
        raise ValueError("[ERROR] NPU2 device cannot allocate more than 8 columns")

    # Calculate output dimensions
    out_height = (in_height + 2 * pad_h - kernel_h) // stride_h + 1
    out_width = (in_width + 2 * pad_w - kernel_w) // stride_w + 1

    module = my_max_pool2d(
        dev,
        N,
        channels,
        in_height,
        in_width,
        out_height,
        out_width,
        kernel_h,
        kernel_w,
        stride_h,
        stride_w,
        pad_h,
        pad_w,
        columns,
        tile_size,
        trace_size,
    )

    output_file_path = Path(opts.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
