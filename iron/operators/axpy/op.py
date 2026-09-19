# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from dataclasses import dataclass
from typing import ClassVar

from iron.common import (
    BinaryElementwiseOperator,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from ml_dtypes import bfloat16
import numpy as np
from aie.iron import ObjectFifo, Program, Runtime, TaskGroup, Worker
from iron.operators._kernels import declare_kernel
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_
from iron.operators._trace import maybe_enable_trace
import torch
from iron.common.test_utils import torch_dtype_map


@dataclass
class AXPY(BinaryElementwiseOperator):
    """AIE-accelerated aX + Y operator"""

    scalar_factor: float = 3.0

    kernel_name: ClassVar[str] = "axpy"
    kernel_fn_name: ClassVar[str] = "saxpy"
    callback_fn: ClassVar[str] = "my_axpy"

    def _mlir_callback_args(self):
        return super()._mlir_callback_args() + [self.scalar_factor]

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                fn=my_axpy,
                bind_from=self,
            ),
        )


# --------------------------------------------------------------------------
# The MLIR this operator generates.
# --------------------------------------------------------------------------


def my_axpy(
    dev,
    size,
    num_aie_columns,
    tile_size,
    trace_size,
    scalar_factor,
    kernels_dir=None,
):
    factor = scalar_factor
    per_tile_elements = 4096 if tile_size > 4096 else tile_size
    n = per_tile_elements * num_aie_columns
    if size % n != 0:
        raise ValueError(f"Number of elements ({size}) must be a multiple of {n}.")
    N_div_n = size // n
    chunk = size // num_aie_columns
    dtype = bfloat16

    # Define tensor types
    tensor_ty = np.ndarray[(size,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    # AIE-array data movement with object fifos (one per column, not per channel)
    of_in1s = [ObjectFifo(tile_ty, name=f"in1_{i}") for i in range(num_aie_columns)]
    of_in2s = [ObjectFifo(tile_ty, name=f"in2_{i}") for i in range(num_aie_columns)]
    of_outs = [ObjectFifo(tile_ty, name=f"out_{i}") for i in range(num_aie_columns)]

    # AIE Core Function declaration
    axpy_bf16_vector = declare_kernel(
        "saxpy",
        [tile_ty, tile_ty, np.float32, tile_ty, np.int32],
        source=Path(kernels_dir) / "generic" / "axpy.cc",
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_in2, of_out, axpy):
        # Number of sub-vector "tile" iterations
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_in2 = of_in2.acquire(1)
            elem_out = of_out.acquire(1)
            axpy(elem_in1, elem_in2, factor, elem_out, per_tile_elements)
            of_in1.release(1)
            of_in2.release(1)
            of_out.release(1)

    # Create a worker to run the task on a compute tile (one per column)
    my_workers = [
        Worker(
            core_body,
            [
                of_in1s[i].cons(),
                of_in2s[i].cons(),
                of_outs[i].prod(),
                axpy_bf16_vector,
            ],
        )
        for i in range(num_aie_columns)
    ]

    # Create a TensorAccessPattern for each column
    # to describe the data movement
    # The pattern chops the data in equal chunks
    # and moves them in parallel across the columns
    taps = [
        TensorAccessPattern(
            (1, size),
            chunk * i,  # Start offset for column i
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_aie_columns)
    ]

    # Runtime operations to move data to/from the AIE-array
    def sequence(A, B, C, in1_prods, in2_prods, out_conses):
        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = TaskGroup()

        # Fill the input objectFIFOs with data
        for i in range(num_aie_columns):
            in1_prods[i].fill(
                A,
                taps[i],
                group=tg,
            )
            in2_prods[i].fill(
                B,
                taps[i],
                group=tg,
            )
        # Drain the output objectFIFOs with data
        for i in range(num_aie_columns):
            out_conses[i].drain(
                C,
                taps[i],
                wait=True,  # wait for the transfer to complete and data to be available
                group=tg,
            )
        tg.finish()

    rt = Runtime(
        sequence,
        [
            tensor_ty,
            tensor_ty,
            tensor_ty,
            [of_in1s[i].prod() for i in range(num_aie_columns)],
            [of_in2s[i].prod() for i in range(num_aie_columns)],
            [of_outs[i].cons() for i in range(num_aie_columns)],
        ],
    )

    # Place program components (assign them resources on the device) and generate an MLIR module
    prog = Program(dev, rt, workers=my_workers)
    maybe_enable_trace(prog, trace_size, my_workers)
    return prog.resolve_program()


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def generate_golden_reference(input_length: int, scalar=3.0, dtype="bf16", seed=42):
    torch.manual_seed(seed)
    val_range = 4
    dtype_torch = torch_dtype_map[dtype]
    A = torch.rand(input_length, dtype=dtype_torch) * val_range
    B = torch.rand(input_length, dtype=dtype_torch) * val_range
    s = torch.tensor(scalar, dtype=dtype_torch)

    # Generate golden outputs
    C = s * A + B

    return {
        "A": A,
        "B": B,
        "C": C,
    }
