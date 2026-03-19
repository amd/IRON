# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
MLIR Generation for 2D Convolution Operator

Generates MLIR code for conv2d operations on AIE2 (NPU) and AIE2P (NPU2) architectures.
Supports configurable kernel_size, stride, padding, dilation, and groups.
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


def my_conv2d(
    dev,
    N,  # batch size
    in_channels,
    in_height,
    in_width,
    out_channels,
    out_height,
    out_width,
    kernel_h,
    kernel_w,
    stride_h,
    stride_w,
    pad_h,
    pad_w,
    groups,
    use_bias,
    num_columns,
    tile_size,
    trace_size,
):
    """
    Generate MLIR for 2D convolution operation.

    Args:
        dev: AIE device (NPU1 or NPU2)
        N: Batch size
        in_channels: Number of input channels
        in_height: Input height
        in_width: Input width
        out_channels: Number of output channels
        out_height: Output height
        out_width: Output width
        kernel_h: Kernel height
        kernel_w: Kernel width
        stride_h: Stride height
        stride_w: Stride width
        pad_h: Padding height
        pad_w: Padding width
        groups: Number of groups for grouped convolution
        use_bias: Whether to use bias
        num_columns: Number of AIE columns to use
        tile_size: Size of each tile
        trace_size: Size of trace buffer

    Returns:
        MLIR module
    """
    dtype = bfloat16

    # Calculate tensor sizes
    input_size = N * in_channels * in_height * in_width
    weight_size = out_channels * in_channels // groups * kernel_h * kernel_w
    output_size = N * out_channels * out_height * out_width
    bias_size = out_channels if use_bias else 0

    # Define tensor types
    input_ty = np.ndarray[(input_size,), np.dtype[dtype]]
    weight_ty = np.ndarray[(weight_size,), np.dtype[dtype]]
    bias_ty = np.ndarray[(bias_size,), np.dtype[dtype]] if use_bias else None
    output_ty = np.ndarray[(output_size,), np.dtype[dtype]]

    # Tile types
    input_tile_ty = np.ndarray[(tile_size,), np.dtype[dtype]]
    output_tile_ty = np.ndarray[(tile_size,), np.dtype[dtype]]

    # P2-10 FIX: Explicit ObjectFifo depth calculation for 8-column stability
    # Depth=4 for 8+ columns, depth=3 for 4+ columns, depth=2 for 2 columns, depth=1 for large tiles
    fifodepth = (
        4
        if num_columns >= 8
        else (
            3
            if num_columns >= 4
            else (2 if num_columns >= 2 else (1 if tile_size > 4096 else 2))
        )
    )

    # AIE-array data movement with object fifos
    of_ins = [
        ObjectFifo(input_tile_ty, name=f"in_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]
    of_weights = [
        ObjectFifo(input_tile_ty, name=f"w_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]
    of_outs = [
        ObjectFifo(output_tile_ty, name=f"out_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]

    # Determine kernel name based on configuration
    kernel_name = "conv2d_bf16_vector"
    if groups == in_channels and groups == out_channels:
        kernel_name = "depthwise_conv2d_bf16_vector"
    elif kernel_h == 1 and kernel_w == 1:
        kernel_name = "pointwise_conv2d_bf16_vector"

    # AIE Core Function declaration
    conv2d_kernel = Kernel(
        kernel_name,
        "conv2d.o",
        [
            input_tile_ty,
            weight_ty,
            output_tile_ty,
            bias_ty if use_bias else input_tile_ty,  # Placeholder if no bias
            np.int32,  # N
            np.int32,  # in_channels
            np.int32,  # in_height
            np.int32,  # in_width
            np.int32,  # out_channels
            np.int32,  # out_height
            np.int32,  # out_width
            np.int32,  # kernel_h
            np.int32,  # kernel_w
            np.int32,  # stride_h
            np.int32,  # stride_w
            np.int32,  # pad_h
            np.int32,  # pad_w
            np.int32,  # groups
        ],
    )

    # Define a task that will run on a compute tile
    def core_body(of_in, of_w, of_out, conv_kernel):
        # Process tiles
        for _ in range_(1):  # Single iteration for now
            elem_in = of_in.acquire(1)
            elem_w = of_w.acquire(1)
            elem_out = of_out.acquire(1)

            # Call kernel with all parameters
            conv_kernel(
                elem_in,
                elem_w,
                elem_out,
                bias if use_bias else elem_in,  # NULL placeholder
                N,
                in_channels,
                in_height,
                in_width,
                out_channels,
                out_height,
                out_width,
                kernel_h,
                kernel_w,
                stride_h,
                stride_w,
                pad_h,
                pad_w,
                groups,
            )

            of_in.release(1)
            of_w.release(1)
            of_out.release(1)

    # Create workers (one per column)
    my_workers = [
        Worker(
            core_body,
            [
                of_ins[i].cons(),
                of_weights[i].cons(),
                of_outs[i].prod(),
                conv2d_kernel,
            ],
        )
        for i in range(num_columns)
    ]

    # Create TensorAccessPatterns for data movement
    input_chunk = input_size // num_columns
    input_taps = [
        TensorAccessPattern(
            (1, input_size),
            input_chunk * i,
            [1, 1, 1, input_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    weight_chunk = weight_size // num_columns
    weight_taps = [
        TensorAccessPattern(
            (1, weight_size),
            weight_chunk * i,
            [1, 1, 1, weight_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    output_chunk = output_size // num_columns
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
    with rt.sequence(input_ty, weight_ty, output_ty) as (A, W, C):
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

        # Fill weight objectFIFOs
        for i in range(num_columns):
            rt.fill(
                of_weights[i].prod(),
                W,
                weight_taps[i],
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
    p.add_argument(
        "-ic", "--in-channels", type=int, required=True, help="Input channels"
    )
    p.add_argument("-ih", "--in-height", type=int, required=True, help="Input height")
    p.add_argument("-iw", "--in-width", type=int, required=True, help="Input width")

    # Output channels
    p.add_argument(
        "-oc", "--out-channels", type=int, required=True, help="Output channels"
    )

    # Kernel parameters
    p.add_argument("-kh", "--kernel-h", type=int, default=3, help="Kernel height")
    p.add_argument("-kw", "--kernel-w", type=int, default=3, help="Kernel width")

    # Stride
    p.add_argument("-sh", "--stride-h", type=int, default=1, help="Stride height")
    p.add_argument("-sw", "--stride-w", type=int, default=1, help="Stride width")

    # Padding
    p.add_argument("-ph", "--pad-h", type=int, default=0, help="Padding height")
    p.add_argument("-pw", "--pad-w", type=int, default=0, help="Padding width")

    # Groups
    p.add_argument("-g", "--groups", type=int, default=1, help="Number of groups")

    # Use bias
    p.add_argument("--use-bias", action="store_true", help="Use bias")

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
    in_channels = opts.in_channels
    in_height = opts.in_height
    in_width = opts.in_width
    out_channels = opts.out_channels
    kernel_h = opts.kernel_h
    kernel_w = opts.kernel_w
    stride_h = opts.stride_h
    stride_w = opts.stride_w
    pad_h = opts.pad_h
    pad_w = opts.pad_w
    groups = opts.groups
    use_bias = opts.use_bias
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

    module = my_conv2d(
        dev,
        N,
        in_channels,
        in_height,
        in_width,
        out_channels,
        out_height,
        out_width,
        kernel_h,
        kernel_w,
        stride_h,
        stride_w,
        pad_h,
        pad_w,
        groups,
        use_bias,
        columns,
        tile_size,
        trace_size,
    )

    output_file_path = Path(opts.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
