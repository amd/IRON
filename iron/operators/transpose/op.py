# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

import aie.utils as aie_utils
from iron.common import (
    MLIROperator,
    same_shape_unary,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from ml_dtypes import bfloat16
import numpy as np
from aie.iron import Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_
import torch
from iron.common.test_utils import torch_dtype_map


@dataclass
class Transpose(MLIROperator):
    """AIE-accelerated transpose operator.

    ``num_batches`` > 1 performs that many independent (M,N)->(N,M) transposes on
    contiguous matrices laid back-to-back in memory (results concatenated), mirroring
    GEMV's batching — the per-batch tile work rides the same ObjectFifos, so B batched
    transposes cost ONE dispatch instead of B unrolled ones.
    """

    M: int
    N: int
    num_aie_columns: int
    num_channels: int
    m: int
    n: int
    s: int
    num_batches: int = 1
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_batches": "batch",
    }

    def __post_init__(self):
        if self.M % self.m != 0:
            raise ValueError(f"Matrix rows ({self.M}) must be a multiple of {self.m}")
        if self.N % self.n != 0:
            raise ValueError(
                f"Matrix columns ({self.N}) must be a multiple of {self.n}"
            )
        if self.m % self.s != 0:
            raise ValueError(f"AIE tile rows ({self.m}) must be a multiple of {self.s}")
        if self.n % self.s != 0:
            raise ValueError(
                f"AIE tile columns ({self.n}) must be a multiple of {self.s}"
            )
        if (
            self.M
            * self.N
            % (self.m * self.n * self.num_aie_columns * self.num_channels)
            != 0
        ):
            raise ValueError(
                "Transfer size must be divisible by m*n*num_columns*num_channels"
            )
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(fn=shuffle_transpose, bind_from=self),
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                f"transpose_{self.m}x{self.n}.o",
                dependencies=[
                    SourceArtifact(
                        self.context.kernels_dir / "generic" / "transpose.cc"
                    )
                ],
                extra_flags=[
                    f"-DDIM_m={self.m}",
                    f"-DDIM_n={self.n}",
                ],
            ),
        ]

    @staticmethod
    def arg_spec(M, N, num_batches=1):
        # A transpose relayouts a flat buffer; M*N == N*M, so both sides carry
        # the same shape and only the interpretation of it changes.
        batch_dim = (num_batches,) if num_batches > 1 else ()
        return same_shape_unary(batch_dim + (M * N,))

    def reference(self, x):
        """CPU reference: 2D transpose of an (M, N) matrix stored row-major."""
        return reference(x.reshape(self.M, self.N))


# --------------------------------------------------------------------------
# The MLIR this operator generates.
# --------------------------------------------------------------------------


def shuffle_transpose(
    dev, M, N, num_aie_columns, num_channels, m, n, s, num_batches=1, func_prefix=""
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
                + (N // num_aie_columns) * i,
                [M // num_channels // m, N // num_aie_columns // n, m, n],
                [m * N, n, N, 1],
            )
            for batch in range(num_batches)
        ]
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    taps_in_L2L1 = [
        TensorAccessPattern(
            (M, N),
            (M // num_channels) * j * N + (N // num_aie_columns) * i,
            [m // s, s, n // s, s],
            [s, m, s * m, 1],
        )
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    taps_out_L1L3 = [
        [
            TensorAccessPattern(
                out_dims,
                batch * num_elements
                + (N // num_aie_columns) * i * M
                + (M // num_channels) * j,
                [M // num_channels // m, N // num_aie_columns // n, n, m],
                [m, n * M, M, 1],
            )
            for batch in range(num_batches)
        ]
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # AIE-array data movement with object fifos
    of_in1s_L3L2 = [
        ObjectFifo(tile_ty, name=f"of_in1s_L3L2_{i}_{j}", depth=fifodepth)
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    of_in1s_L2L1 = [
        of_in1s_L3L2[i * num_channels + j]
        .cons(dims_from_stream=taps_in_L2L1[i * num_channels + j].transformation_dims)
        .forward(obj_type=tile_ty, name=f"of_in1s_L2L1_{i}_{j}", depth=fifodepth)
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(tile_ty, name=f"out_{i}_{j}", depth=fifodepth)
        for i in range(num_aie_columns)
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
            for _ in range_(N // n // num_aie_columns):
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
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # Runtime operations to move data to/from the AIE-array
    def sequence(A, C, of_in1s_L3L2_prods, of_outs_conss):

        # One task group per batch (each a parallel fill+drain over all columns/channels), so the
        # num_batches contiguous matrices stream through the same FIFOs in sequence.
        for batch in range(num_batches):
            # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
            tg = TaskGroup()

            # Fill the input objectFIFOs with data
            for i in range(num_aie_columns):
                for j in range(num_channels):
                    of_in1s_L3L2_prods[i * num_channels + j].fill(
                        A,
                        taps_in_L3L2[i * num_channels + j][batch],
                        group=tg,
                    )
            # Drain the output objectFIFOs of data
            for i in range(num_aie_columns):
                for j in range(num_channels):
                    of_outs_conss[i * num_channels + j].drain(
                        C,
                        taps_out_L1L3[i * num_channels + j][batch],
                        wait=True,  # wait for the transfer to complete and data to be available
                        group=tg,
                    )
            tg.finish()

    rt = Runtime(
        sequence,
        [
            tensor_ty,
            tensor_ty,
            [of.prod() for of in of_in1s_L3L2],
            [of.cons() for of in of_outs],
        ],
    )
    # Place program components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt, workers=my_workers).resolve_program()


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(x):
    """CPU reference: 2D transpose of an ``(rows, cols)`` matrix (ground truth)."""
    return torch.transpose(x, 0, 1)


def generate_golden_reference(
    rows: int, cols: int, dtype="bf16", seed=42, num_batches=1
):
    torch.manual_seed(seed)
    val_range = 4
    # num_batches>1: B independent (rows,cols) matrices laid back-to-back; each is
    # transposed independently and the results concatenated in the same order.
    input_tensor = (
        torch.rand(num_batches, rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    )
    output_tensor = torch.stack(
        [reference(input_tensor[b]) for b in range(num_batches)]
    )
    # drop batch dimension if num_batches == 1
    input_tensor = torch.squeeze(input_tensor, 0)
    output_tensor = torch.squeeze(output_tensor, 0)
    return {"input": input_tensor, "output": output_tensor}
