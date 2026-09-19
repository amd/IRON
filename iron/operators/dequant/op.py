# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from dataclasses import dataclass, field

import numpy as np
from ml_dtypes import bfloat16

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from iron.common.device_utils import get_kernel_dir
import aie.utils as aie_utils
from aie.iron import ObjectFifo, Program, Runtime, TaskGroup, Worker
from iron.operators._kernels import declare_kernel
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_
import torch


@dataclass
class Dequant(MLIROperator):
    """AIE-accelerated dequantization operator"""

    size: int
    num_aie_columns: int
    num_channels: int
    tile_size: int
    group_size: int = field(default=32, repr=False)
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        # Calculate buffer sizes (in bytes)
        # Input: int4 packed data + scale factors
        self.input_size = (self.size // 2) + (self.size // self.group_size) * 2
        self.output_size = self.size

        total_cores = self.num_aie_columns * self.num_channels
        if self.size % total_cores != 0:
            raise ValueError(
                f"size ({self.size}) must be divisible by total cores ({total_cores})"
            )
        if total_cores > 16:
            raise ValueError(f"total cores ({total_cores}) must be <= 16")
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                fn=my_dequant_kernel,
                bind_from=self,
            ),
        )

    @staticmethod
    def arg_spec(size, group_size=32):
        # Packed input: two 4-bit values per byte, plus a bf16 scale and zero
        # point per group. __post_init__ caches these as input_size/output_size.
        input_size = (size // 2) + (size // group_size) * 2
        return [
            AIERuntimeArgSpec("in", (input_size,), dtype=np.uint8),
            AIERuntimeArgSpec("out", (size,), dtype=bfloat16),
        ]


# --------------------------------------------------------------------------
# The MLIR this operator generates.
# --------------------------------------------------------------------------


def my_dequant_kernel(
    dev,
    size,
    num_aie_columns,
    num_channels,
    trace_size,
    tile_size,
    group_size,
    kernels_dir=None,
):
    per_tile_elements = (
        16384 if tile_size > 16384 else tile_size
    )  # Largest tile size for 64KB in L1 and possible
    # group size of 1 with objfifo depth of 1
    total_cores = num_aie_columns * num_channels
    per_core_elements = size // total_cores
    if size % total_cores != 0:
        raise ValueError(
            f"Number of elements ({size}) must be a multiple of {total_cores}."
        )
    N_div_n = per_core_elements // per_tile_elements
    chunk = size // num_aie_columns // num_channels  # For offset calculation
    in_dtype = np.uint8
    out_dtype = bfloat16

    # Input data: int4 packed data + scale factors
    # For N int4 values, we need N/2 bytes + N/group_size scale factors (bfloat16, 2 bytes each)
    input_tensor_size = (size // 2) + (size // group_size) * 2
    input_tile_size = (per_tile_elements // 2) + (per_tile_elements // group_size) * 2

    # Define tensor types
    in_tensor_ty = np.ndarray[(input_tensor_size,), np.dtype[in_dtype]]
    out_tensor_ty = np.ndarray[(size,), np.dtype[out_dtype]]
    in_tile_ty = np.ndarray[(input_tile_size,), np.dtype[in_dtype]]
    out_tile_ty = np.ndarray[(per_tile_elements,), np.dtype[out_dtype]]

    fifodepth = 1 if tile_size > 8192 else 2
    enable_trace = trace_size > 0

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(in_tile_ty, name=f"in1_{i}_{j}", depth=fifodepth)
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(out_tile_ty, name=f"out_{i}_{j}", depth=fifodepth)
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # AIE Core Function declaration
    dequant_kernel = declare_kernel(
        "expand_uint4_to_bfloat16",
        [in_tile_ty, out_tile_ty],
        source=Path(kernels_dir) / "generic" / "expand.cc",
        compile_flags=[f"-DTILE_SIZE={tile_size}", f"-DGROUP_SIZE={group_size}"],
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
        for i in range(num_aie_columns)
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
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    taps_out = [
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
    def sequence(A, C, of_in1s_prods, of_outs_conss):

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = TaskGroup()

        # Fill the input objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                of_in1s_prods[i * num_channels + j].fill(
                    A,
                    taps_in[i * num_channels + j],
                    group=tg,
                )
        # Drain the output objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                of_outs_conss[i * num_channels + j].drain(
                    C,
                    taps_out[i * num_channels + j],
                    wait=True,  # wait for the transfer to complete and data to be available
                    group=tg,
                )
        tg.finish()

    rt = Runtime(
        sequence,
        [
            in_tensor_ty,
            out_tensor_ty,
            [of.prod() for of in of_in1s],
            [of.cons() for of in of_outs],
        ],
    )
    # Place program components (assign them resources on the device) and generate an MLIR module
    prog = Program(dev, rt, workers=my_workers)
    if enable_trace:
        prog.enable_trace(trace_size)
    return prog.resolve_program()


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def generate_golden_reference(input_length, tile_size, group_size):
    torch.manual_seed(42)

    if input_length % tile_size != 0:
        raise ValueError("Input length must be a multiple of tile size.")
    if tile_size % group_size != 0:
        raise ValueError("Tile size must be a multiple of group size.")

    num_tiles = input_length // tile_size
    num_scale_factors = tile_size // group_size
    scale_size = num_scale_factors * 2  # Total bytes (uint8 elements) for scale factors
    per_tile_size = tile_size // 2
    per_tile_bytes = (
        scale_size + per_tile_size
    )  # Total bytes (uint8 elements) after processing each tile
    val_range = 3.75  # Values in [0, 3.75)

    # Generate golden output with uniform distribution between 0 and val_range
    # This output will be quantized to be used as the input
    A = (
        torch.rand(num_tiles * num_scale_factors, group_size, dtype=torch.bfloat16)
        * val_range
    )

    # Generate scale factors in [0.25, 1) for each tile
    # The quantized values will thus be within [0,15], which is the range of int4
    # Zero points for each tile are fixed to 0 since the kernel only uses the scale factors
    r1, r2 = 1 / val_range, 1
    scales = r1 + (r2 - r1) * torch.rand(
        num_tiles * num_scale_factors, dtype=torch.bfloat16
    )
    zero_points = torch.zeros(num_tiles * num_scale_factors, dtype=torch.bfloat16)

    A = torch.quantize_per_channel(
        A.to(torch.float32),
        scales=scales.to(torch.float32),
        zero_points=zero_points.to(torch.float32),
        axis=0,
        dtype=torch.quint8,
    )
    B = torch.dequantize(A)

    # Convert A from a quantized tensor type to regular tensor type for data packing
    # We do the data packing here instead of the host to show how the data would need to be
    # manipulated from a PyTorch standpoint in order to use the dequant kernel.
    A = A.int_repr()

    # Concatenate the bottom four bits of every two elements across the tiles in A to generate
    # an 8-bit value (little endian order). This is because there's no native 4-bit datatype in C++.
    # At the end of each tile, concatenate the bf16 scale factor, which comes out to two int8 values.
    A_concat = torch.zeros(num_tiles, per_tile_bytes, dtype=torch.uint8)
    for i in range(num_tiles):
        for j in range(num_scale_factors):
            for k in range(group_size // 2):
                A_concat[i, j * (group_size // 2) + k] = torch.bitwise_or(
                    torch.bitwise_and(A[i * num_scale_factors + j, 2 * k], 0x0F),
                    torch.bitwise_and(A[i * num_scale_factors + j, 2 * k + 1], 0x0F)
                    * 2**4,
                )
        for j in range(num_scale_factors):
            A_concat[i, per_tile_size + 2 * j] = torch.bitwise_and(
                scales[i * num_scale_factors + j].view(torch.uint16), 0xFF
            )
            # Extract high byte (bits 15-8) of the bfloat16 bit pattern.
            # View as int16 (same width), promote to int32 for bitwise_right_shift
            # support, shift right 8, then mask to 8 bits. The & 0xFF also
            # handles sign-extension from int32 arithmetic right shift.
            A_concat[i, per_tile_size + 2 * j + 1] = torch.bitwise_and(
                scales[i * num_scale_factors + j].view(torch.int16).to(torch.int32)
                >> 8,
                0xFF,
            )

    return {
        "input": A_concat,
        "output": B,
    }
