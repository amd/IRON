# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
MLIR Generation for AveragePool Operator

Generates MLIR for average pooling operations on AIE2 (NPU) and AIE2P (NPU2) architectures.
"""

# =============================================================================
# MODELING STATUS (post Modeling Pass - avgpool)
# =============================================================================
# - No bias, no kernel variants: simpler than convs.
# - Chunk/tile consistency: FIXED (gold). input_chunk/output_chunk (full size)
#   used for FIFO types + TAPs (effective 1-col for monolithic kernel).
# - core_body loops: gold bounded-loop fix applied (range(1) workaround for
#   #1547 like gemm/conv2d/conv3d; range_(N) avoided for 1-iter skeleton).
# - L3 staging + chunk-first-fifodepth + correct-TAP (full, not partial chunks):
#   fully applied (gold from conv3d/conv2d fixes; resolves OOB/hang for nc>1
#   and large-tile nc=1 cases that caused 600s timeout).
# - Honest docs. MLIR skeleton + runlist dispatch in op.py (kernel does full
#   tensor work; design provides stable 1-lane L3-staged data path).
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

# For future shim DMA / per-tile channel constraint checks (parity with
# conv2d gold, rms_norm, binary_elementwise, channeled_unary etc). L3-staged
# ingress (see below) moves shim input DMA to memtile; compute tiles (row 2
# e.g. tile(0,2)) only see L2L1. Still exercises allocator on some configs;
# full get_shim_dma_limit + per-shim modeling + num_channels refactor is the
# next modeling step (coordinate with cross-operator DMA fixer).
from iron.common.utils import get_shim_dma_limit


def my_avg_pool2d(
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
    Generate MLIR for 2D average pooling operation.

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

    # Gold fix (conv3d/conv2d L3+bounded+correct-TAP+chunk-first-fifodepth):
    # The avgpool kernel (aie2/avgpool.cc + aie2p) is monolithic full-tensor
    # (loops over full N,C,H,W dims with layout strides; no per-chunk awareness).
    # Using num_columns>1 + partial chunks in TAP/FIFO + full-dim kernel calls
    # => OOB accesses in L1 + deadlock/hang (exact root cause of 600s collection-only
    # timeout in /tmp/avgpool_hw_long.log). Force effective=1 (full chunk) for
    # correct-TAP + single worker + L3 staging. num_columns retained for API/
    # artifact naming parity only (xclbin names still reflect caller's nc).
    effective_num_columns = 1
    input_chunk = input_size // effective_num_columns
    output_chunk = output_size // effective_num_columns

    input_tile_ty = np.ndarray[
        (input_chunk if input_chunk > 0 else 1,), np.dtype[dtype]
    ]
    output_tile_ty = np.ndarray[
        (output_chunk if output_chunk > 0 else 1,), np.dtype[dtype]
    ]

    # chunk-first-fifodepth (gold): based on actual full chunk (now always full
    # size due to effective=1), not caller tile_size. Depth=1 for >4096 to fit
    # L1 (8KB+); small depth otherwise. (L3 staging already provides ingress
    # stability.)
    fifodepth = 1 if input_chunk > 4096 else 2

    # AIE-array data movement with object fifos, using explicit L3->L2->L1
    # staging (.cons().forward) for ingress (input) -- gold pattern.
    # L3 for rt.fill prod (shim DMA); L1 for core acquire. 1-lane only.
    of_ins_l3 = [
        ObjectFifo(input_tile_ty, name=f"in_l3_{i}", depth=fifodepth)
        for i in range(effective_num_columns)
    ]
    of_ins = [
        of_ins_l3[i].cons().forward(
            obj_type=input_tile_ty, name=f"in_l1_{i}", depth=fifodepth
        )
        for i in range(effective_num_columns)
    ]
    of_outs = [
        ObjectFifo(output_tile_ty, name=f"out_{i}", depth=fifodepth)
        for i in range(effective_num_columns)
    ]

    # Kernel name
    kernel_name = "avg_pool2d_bf16_vector"

    # AIE Core Function declaration (matches avg_pool2d_bf16_vector exactly)
    avgpool_kernel = Kernel(
        kernel_name,
        "avgpool.o",
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
        # Gold bounded-loop (workaround for issue #1547, exact as gemm + conv
        # post-fix designs): use python range(1) for the 1-iter skeleton case
        # instead of range_(1). Full-tensor kernel does all work in 1 dispatch.
        loop = range(1)
        for _ in loop:
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

    # Create workers (1 lane for monolithic kernel correctness + no hang)
    my_workers = [
        Worker(
            core_body,
            [
                of_ins[i].cons(),
                of_outs[i].prod(),
                avgpool_kernel,
            ],
            while_true=False,
        )
        for i in range(effective_num_columns)
    ]

    # Create TensorAccessPatterns (gold correct-TAP: full size, 1 lane)
    input_taps = [
        TensorAccessPattern(
            (1, input_size),
            input_chunk * i,
            [1, 1, 1, input_chunk],
            [0, 0, 0, 1],
        )
        for i in range(effective_num_columns)
    ]

    output_taps = [
        TensorAccessPattern(
            (1, output_size),
            output_chunk * i,
            [1, 1, 1, output_chunk],
            [0, 0, 0, 1],
        )
        for i in range(effective_num_columns)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(input_ty, output_ty) as (A, C):
        rt.start(*my_workers)

        # Initialize a group for parallel tasks
        tg = rt.task_group()

        # Fill input objectFIFOs (L3 endpoint for shim DMA staging; L1 for cores)
        for i in range(effective_num_columns):
            rt.fill(
                of_ins_l3[i].prod(),
                A,
                input_taps[i],
                task_group=tg,
            )

        # Drain output objectFIFOs
        for i in range(effective_num_columns):
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

    module = my_avg_pool2d(
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
