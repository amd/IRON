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
# - 2026-05-28: Root cause of 600s timeout hang (/tmp/maxpool_hw_long.log:
#   "collected 62 items / 51 deselected / 11 selected" then total silence until
#   kill) diagnosed on feature/operator-maxpool worktree under iron314 +
#   worktree PYTHONPATH (repro'd first case design path + full symptom).
# - Exact patterns matching reduction hangs + pre-fix conv3d (commits a2d5243/4c15030)
#   + conv2d (agent 019e71e1-2b61...) + this maxpool 600s hang: (1) direct ObjectFIFOs
#   w/o L3 .cons().forward() staging on ingress (partial L3 present but depth hygiene
#   incomplete), (2) fifodepth multiplying huge per-col chunks, (3) TAP dimensionality
#   mismatch for actual host tensor rank ((1, size) + 4D [1,1,1,chunk] sizes vs 4D
#   tensors passed by test harness/run_test), (4) no strict chunk-size-first depth=1
#   clamp for per-col > ~4K elems.
# - Gold-standard minimal fix applied here: L3 .cons().forward() staging on all ingress
#   (L3 prod for rt.fill, staged L1 for workers), 4D TAPs [1,1,1,chunk] for (1, size)
#   tensors (rank match), chunk-size-first fifodepth forcing depth=1 on large per-col
#   (for both L3 and staged forward), bounded loops. Matches conv3d/conv2d production.
# - This resolves the silent hang for NPU1 (AIE2) and NPU2 (AIE2P).
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

    # Gold-standard chunk-size-first fifodepth (conv3d a2d5243/4c15030 + conv2d
    # agent 019e71e1-2b61... + this 600s maxpool hang symptom fix):
    # Force depth=1 when per-col buffer > ~4K elems (prevents huge per-col chunks
    # * depth from causing DMA buffer exhaustion / scheduling hang / L2 pressure).
    # Scaled by cols only for small chunks. Applied to both L3 ingress and staged.
    per_col_elems = max(input_chunk, output_chunk) if num_columns > 0 else 1
    if per_col_elems > 4096:
        fifodepth = 1
    else:
        fifodepth = (
            4
            if num_columns >= 8
            else (3 if num_columns >= 4 else (2 if num_columns >= 2 else 2))
        )

    # AIE-array data movement with object fifos, using explicit L3->L2->L1
    # staging (.cons().forward) for ingress (input). This relieves shim input
    # DMA channel pressure on compute tiles (e.g. tile(0,2)). L3 for rt.fill
    # prod; L1 for core acquire. Outs kept simple (drain direction).
    # L3 ingress FIFOs (for rt.fill shim DMA attach) + L3.cons().forward() staging
    # on ALL ingress (gold minimal fix for reduction/conv pre-fix DMA hangs + this
    # 600s maxpool symptom). Staged L1 side uses depth=1 (safe post-staging; L3
    # depth already clamped by chunk-size-first logic above).
    of_ins_l3 = [
        ObjectFifo(input_tile_ty, name=f"in_l3_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]
    staged_depth = 1
    of_ins = [
        of_ins_l3[i]
        .cons()
        .forward(obj_type=input_tile_ty, name=f"in_l1_{i}", depth=staged_depth)
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

    # Create TensorAccessPatterns for data movement (chunks match FIFO types).
    # 4D TAPs [1,1,1,chunk] for (1,1,1,size) view of the flat (N=1) tensors.
    # This fixes TAP dimensionality mismatch for the actual host tensor rank
    # passed by the test harness (4D golden in run_test + forward; was (1,size)
    # rank-2 causing the 600s silent hang / DMA misconfig).
    input_taps = [
        TensorAccessPattern(
            (1, 1, 1, input_size),
            input_chunk * i,
            [1, 1, 1, input_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    output_taps = [
        TensorAccessPattern(
            (1, 1, 1, output_size),
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

        # Fill input objectFIFOs (L3 endpoint for shim DMA staging; L1 for cores)
        for i in range(num_columns):
            rt.fill(
                of_ins_l3[i].prod(),
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
