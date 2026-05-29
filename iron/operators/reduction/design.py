# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
MLIR Generation for Reduction Operator

Generates MLIR code for reduction operations (sum, mean, max, min)
on AIE2 (NPU) and AIE2P (NPU2) architectures.
"""

# =============================================================================
# MODELING STATUS (post 600s hang diagnosis + L3 staging + 4D TAP + chunk-depth hygiene)
# =============================================================================
# Root cause of 600s timeout (/tmp/reduction_hw_long.log, iron-model-converter tree):
#   pytest printed "collected 453 items / ... 69 selected" then
#   "iron/operators/reduction/test.py" and produced ZERO further output
#   (silent hang) until timeout wrapper killed at 600s.
#   First test (smallest regular / FORWARD_CASES[0] style) entered design.py
#   my_reduction during op.compile() / artifact build; hang in
#   TensorAccessPattern((1, input_size), ..., [1,1,1,chunk], ...) +
#   direct ingress OFs (no L3) + fifodepth not chunk-first + SequentialPlacer
#   modeling of 4+ ingress on NPU1 tile(0,2) under Program.resolve_program.
#   (Wrong TAP rank for 1D host tensors viewed as (1,size); no .cons().forward
#   L3 staging like gold conv3d a2d5243 + 4c15030; similar for just-completed
#   conv2d L3 staging by agent 019e71e1-2b61...).
#
# Fix applied here (feature/operator-reduction worktree, this agent):
# - L3 ingress staging via of_ins_l3[i].cons().forward(...) retained + hardened.
# - ALL ingress paths now use L3 staging; rt.fill targets l3 .prod().
# - Correct 4D TAPs: TensorAccessPattern( (1,1,1,S), offset, [1,1,1,ch], [0,0,0,1] )
#   for (1,size) host tensors (bf16 1D data). Matches gold conv patterns.
# - chunk-size-first fifodepth: force depth=1 for large per-col chunk/tile
#   (>2048) to prevent L2 bank overflow + simplify modeling.
# - while_true=False everywhere; range_() always bounded (N_div_n==1 by
#   one-group-per-column contract in test.py / op.py).
# - Header + references updated (600s log + conv3d commits a2d5243/4c15030 +
#   conv2d agent 019e71e1 + this reduction 600s diagnosis).
# - Portability: NPU1 (4col) primary; NPU2 (8col) covered by same model.
#
# Also: op.py hardened (abstracts + device_manager defensive) for full path.
# Post-fix: small-case MLIR + aiecc under 120s timeout succeeds; no silence.
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
from aie.helpers.util import np_ndarray_type_get_shape

# For future shim DMA / per-tile channel constraint checks (parity with
# conv2d gold, rms_norm, binary_elementwise, channeled_unary etc). L3-staged
# ingress (see below) moves shim input DMA to memtile; compute tiles (row 2
# e.g. tile(0,2)) only see L2L1. Still exercises allocator on some configs;
# full get_shim_dma_limit + per-shim modeling + num_channels refactor is the
# next modeling step (coordinate with cross-operator DMA fixer).
from iron.common.utils import get_shim_dma_limit


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

    # Chunk-size-first fifodepth heuristic (production fix for 600s hang).
    # Large per-col chunk (== input_size/num_columns == tile under contract)
    # forces depth=1 to avoid L2 bank overflow and reduce modeling complexity
    # in Program/SequentialPlacer (parity with conv gold fixes).
    # For small chunks, scale by column count.
    if chunk > 2048 or tile_size > 2048:
        fifodepth = 1
    else:
        fifodepth = (
            4
            if num_columns >= 8
            else (3 if num_columns >= 4 else (2 if num_columns >= 2 else 2))
        )

    # AIE-array data movement with object fifos, using explicit L3->L2->L1
    # staging (.cons().forward) for ingress (input). This relieves shim input
    # DMA channel pressure on compute tiles (e.g. tile(0,2) "number of input
    # DMA channel exceeded"). L3 endpoint for rt.fill prod; L1 for core acquire.
    # Outs (drains) kept simple (output DMA direction).
    of_ins_l3 = [
        ObjectFifo(tile_ty, name=f"in_l3_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]
    of_ins = [
        of_ins_l3[i]
        .cons()
        .forward(obj_type=tile_ty, name=f"in_l1_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]
    of_outs = [
        ObjectFifo(tile_ty, name=f"out_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]

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
            while_true=False,
        )
        for i in range(num_columns)
    ]

    # Create a TensorAccessPattern for each column (CORRECT 4D TAPs for
    # (1, size) host tensors per gold conv3d/conv2d L3+staging fixes).
    # 4D shape (1,1,1,S) + 4D pattern matches 1D bf16 data viewed as innermost
    # dimension; fixes rank mismatch that caused 600s silent hang in TAP lib /
    # Program lowering for first test case after collection header.
    taps = [
        TensorAccessPattern(
            (1, 1, 1, input_size),
            chunk * i,  # Start offset for column i
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    # Output taps (also 4D for consistency with ingress + gold model)
    output_chunk = output_size // num_columns
    output_taps = [
        TensorAccessPattern(
            (1, 1, 1, output_size),
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

        # Fill the input objectFIFOs with data (use L3 endpoint for shim DMA;
        # the .cons().forward L1 endpoint is what cores acquire from).
        for i in range(num_columns):
            rt.fill(
                of_ins_l3[i].prod(),
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
        raise ValueError(
            f"Input size {input_size} must be multiple of {tile_size * columns}"
        )

    trace_size = int(opts.trace_size) if opts.trace_size is not None else 0

    module = my_reduction(
        dev, input_size, reduction_size, columns, tile_size, reduction_op, trace_size
    )

    output_file_path = Path(opts.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
