# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_


def shuffle_transpose(
    dev, M, N, num_columns, num_channels, m, n, s, num_batches=1, func_prefix=""
):
    num_elements = M * N
    per_tile_elements = m * n
    dtype = bfloat16

    if M % m != 0:
        raise ValueError(f"Matrix rows ({M}) must be a multiple of {m}.")
    if N % n != 0:
        raise ValueError(f"Matrix columns ({N}) must be a multiple of {n}.")
    if m % s != 0:
        raise ValueError(f"AIE tile rows ({m}) must be a multiple of {s}.")
    if n % s != 0:
        raise ValueError(f"AIE tile columns ({n}) must be a multiple of {s}.")
    if per_tile_elements > 8192:
        raise ValueError(
            f"Kernel tile size {per_tile_elements} needs to be below 8192 to fit within data memory."
        )

    # Minimum tile sizes required by the two kernels
    if s == 4 and (m <= 4 or n <= 4):
        raise ValueError(f"Kernel tile {s} needs AIE tile rows > 4 and columns > 4.")
    if s == 8 and (m <= 16 or n <= 16):
        raise ValueError(f"Kernel tile {s} needs AIE tile rows > 16 and columns > 16.")

    # Define tensor types. The runtime tensor spans all batches (contiguous matrices);
    # per-tile work on the cores is identical regardless of batch count.
    tensor_ty = np.ndarray[(num_batches * num_elements,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    fifodepth = 1 if per_tile_elements > 4096 else 2

    # Create a TensorAccessPattern for each channel
    # to describe the data movement
    # The pattern chops the data in equal chunks
    # and moves them in parallel across the columns
    # and channels. Partially transposes the input
    # data so that the kernel only needs to
    # transpose s*s-sized sub-tiles.
    # The L3 tensors hold num_batches contiguous (M,N) matrices stacked along the row
    # dimension: in-dims (num_batches*M, N), out-dims (num_batches*N, M); at num_batches==1
    # these are simply (M,N)/(N,M). Each (i,j) column/channel emits one TAP per batch, offset
    # by batch*num_elements; the per-batch internal sizes/strides are the same for every batch
    # because each matrix is contiguous and row-major.
    in_dims = (num_batches * M, N)
    out_dims = (num_batches * N, M)
    taps_in_L3L2 = [
        [
            TensorAccessPattern(
                in_dims,
                batch * num_elements
                + (M // num_channels) * j * N
                + (N // num_columns) * i,
                [M // num_channels // m, N // num_columns // n, m, n],
                [m * N, n, N, 1],
            )
            for batch in range(num_batches)
        ]
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    taps_in_L2L1 = [
        TensorAccessPattern(
            (M, N),
            (M // num_channels) * j * N + (N // num_columns) * i,
            [m // s, s, n // s, s],
            [s, m, s * m, 1],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    taps_out_L1L3 = [
        [
            TensorAccessPattern(
                out_dims,
                batch * num_elements
                + (N // num_columns) * i * M
                + (M // num_channels) * j,
                [M // num_channels // m, N // num_columns // n, n, m],
                [m, n * M, M, 1],
            )
            for batch in range(num_batches)
        ]
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # AIE-array data movement with object fifos
    of_in1s_L3L2 = [
        ObjectFifo(tile_ty, name=f"of_in1s_L3L2_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    of_in1s_L2L1 = [
        of_in1s_L3L2[i * num_channels + j]
        .cons(dims_from_stream=taps_in_L2L1[i * num_channels + j].transformation_dims)
        .forward(obj_type=tile_ty, name=f"of_in1s_L2L1_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(tile_ty, name=f"out_{i}_{j}", depth=fifodepth)
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # AIE Core Function declaration
    transpose_kernel = Kernel(
        f"{func_prefix}transpose_{s}x{s}",
        f"{func_prefix}transpose_{m}x{n}.o",
        [tile_ty, tile_ty],
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_out, transpose_kernel):
        # Process num_batches contiguous matrices through the same FIFOs: num_batches x the per-matrix
        # tile iterations. The kernel only ever sees s*s sub-tiles, so it is batch-agnostic.
        for _ in range_(num_batches):
            # Number of sub-matrix "tile" iterations
            for _ in range_(N // n // num_columns):
                for _ in range_(M // m // num_channels):
                    elem_in1 = of_in1.acquire(1)
                    elem_out = of_out.acquire(1)
                    transpose_kernel(elem_in1, elem_out)
                    of_out.release(1)
                    of_in1.release(1)

    # Create a worker to run the task on a compute tile
    my_workers = [
        Worker(
            core_body,
            [
                of_in1s_L2L1[i * num_channels + j].cons(),
                of_outs[i * num_channels + j].prod(),
                transpose_kernel,
            ],
        )
        for i in range(num_columns)
        for j in range(num_channels)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(tensor_ty, tensor_ty) as (A, C):
        rt.start(*my_workers)

        # One task group per batch (each a parallel fill+drain over all columns/channels), so the
        # num_batches contiguous matrices stream through the same FIFOs in sequence.
        for batch in range(num_batches):
            # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
            tg = rt.task_group()

            # Fill the input objectFIFOs with data
            for i in range(num_columns):
                for j in range(num_channels):
                    rt.fill(
                        of_in1s_L3L2[i * num_channels + j].prod(),
                        A,
                        taps_in_L3L2[i * num_channels + j][batch],
                        task_group=tg,
                    )
            # Drain the output objectFIFOs of data
            for i in range(num_columns):
                for j in range(num_channels):
                    rt.drain(
                        of_outs[i * num_channels + j].cons(),
                        C,
                        taps_out_L1L3[i * num_channels + j][batch],
                        wait=True,  # wait for the transfer to complete and data to be available
                        task_group=tg,
                    )
            rt.finish_task_group(tg)

    # Place program components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt).resolve_program(SequentialPlacer())
