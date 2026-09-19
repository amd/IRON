# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar, Dict

import aie.utils as aie_utils
from iron.common import (
    ChanneledUnaryOperator,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from ml_dtypes import bfloat16
import numpy as np
from aie.iron import Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_
from iron.operators._trace import maybe_enable_trace
import torch
from iron.common.test_utils import torch_dtype_map


@dataclass
class LeakyReLU(ChanneledUnaryOperator):
    """AIE-accelerated Leaky ReLU operator"""

    alpha: float = 0.01

    kernel_name: ClassVar[str] = "leaky_relu"
    kernel_fn_name: ClassVar[str] = "leaky_relu_bf16"
    callback_fn: ClassVar[str] = "my_leaky_relu"
    _name_aliases: ClassVar[Dict[str, str]] = {
        **ChanneledUnaryOperator._name_aliases,
        "alpha": "a",
    }

    # Minimum per-core line length (in bfloat16 elements) required by the
    # vectorized kernels. They tell the pipeliner a minimum loop-trip count via
    # AIE_LOOP_MIN_ITERATION_COUNT -- a hard contract under xchesscc -- so that
    # promise must be backed by a lower bound on the line length, or the
    # compiler may drop the low-trip guard and corrupt results. The kernels
    # vectorize by 16 (aie2) or 32 (aie2p) elements and promise 4 / 2 iterations
    # respectively, i.e. at least 64 elements per line.
    min_line_size: ClassVar[int] = 64

    def __post_init__(self) -> None:
        line_size = min(self.tile_size, self.tile_cap)
        if line_size < self.min_line_size:
            raise ValueError(
                f"tile_size ({self.tile_size}) yields a per-core line of "
                f"{line_size} bfloat16 elements; leaky_relu requires at least "
                f"{self.min_line_size} to satisfy the kernel's minimum "
                f"loop-iteration promise"
            )
        super().__post_init__()

    def _mlir_callback_args(self):
        return super()._mlir_callback_args() + [self.alpha]

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                fn=my_leaky_relu,
                bind_from=self,
            ),
        )


# --------------------------------------------------------------------------
# The MLIR this operator generates.
# --------------------------------------------------------------------------


def my_leaky_relu(
    dev,
    size,
    num_aie_columns,
    num_channels,
    tile_size,
    trace_size,
    alpha,
):
    xfr_dtype = bfloat16
    # Cap to 4096 bfloat16 elements (8 KB) to fit AIE core local memory
    line_size = 4096 if tile_size > 4096 else tile_size
    line_type = np.ndarray[(line_size,), np.dtype[xfr_dtype]]
    transfer_type = np.ndarray[(size,), np.dtype[xfr_dtype]]

    # Calculate number of iterations per core
    total_cores = num_aie_columns * num_channels
    per_core_elements = size // total_cores
    N_div_n = per_core_elements // line_size

    # Chunk size sent per DMA channel
    chunk = size // num_aie_columns // num_channels

    # Dataflow with ObjectFifos
    of_ins = [
        ObjectFifo(line_type, name=f"in{i}_{j}")
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(line_type, name=f"out{i}_{j}")
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # External, binary kernel definition
    # Leaky RELU kernel takes: input, output, input_size, alpha
    leaky_relu_fcn = Kernel(
        "leaky_relu_bf16",
        "leaky_relu.o",
        [line_type, line_type, np.int32, xfr_dtype],
    )

    # Task for the core to perform
    def core_fn(of_in, of_out, leaky_relu_line):
        for _ in range_(N_div_n):
            elemIn = of_in.acquire(1)
            elemOut = of_out.acquire(1)
            leaky_relu_line(elemIn, elemOut, line_size, alpha)
            of_in.release(1)
            of_out.release(1)

    # Create a worker to perform the task
    my_workers = [
        Worker(
            core_fn,
            [
                of_ins[i * num_channels + j].cons(),
                of_outs[i * num_channels + j].prod(),
                leaky_relu_fcn,
            ],
        )
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # Create a TensorAccessPattern for each channel
    # to describe the data movement
    # The pattern chops the data in equal chunks
    # and moves them in parallel across the columns
    # and channels.
    taps = [
        TensorAccessPattern(
            (1, size),
            chunk * i * num_channels + chunk * j,
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # Runtime operations to move data to/from the AIE-array
    def sequence(a_in, b_out, of_ins_prods, of_outs_conss):

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = TaskGroup()

        # Fill the input objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                of_ins_prods[i * num_channels + j].fill(
                    a_in,
                    taps[i * num_channels + j],
                    group=tg,
                )
        # Drain the output objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                of_outs_conss[i * num_channels + j].drain(
                    b_out,
                    taps[i * num_channels + j],
                    wait=True,  # wait for the transfer to complete and data to be available
                    group=tg,
                )
        tg.finish()

    rt = Runtime(
        sequence,
        [
            transfer_type,
            transfer_type,
            [of.prod() for of in of_ins],
            [of.cons() for of in of_outs],
        ],
    )
    # Place components (assign them resources on the device) and generate an MLIR module
    prog = Program(dev, rt, workers=my_workers)
    maybe_enable_trace(prog, trace_size, my_workers)
    return prog.resolve_program()


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def generate_golden_reference(input_length: int, alpha=0.01, dtype="bf16", seed=42):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = (
        torch.rand(input_length, dtype=torch_dtype_map[dtype]) * val_range
        - val_range / 2
    )
    output_tensor = torch.nn.functional.leaky_relu(input_tensor, negative_slope=alpha)
    return {"input": input_tensor, "output": output_tensor}
