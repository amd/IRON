# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from dataclasses import dataclass, field
from typing import ClassVar, Dict

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
import aie.utils as aie_utils
from iron.common.device_utils import get_kernel_dir
from iron.common.utils import get_shim_dma_limit
from ml_dtypes import bfloat16
import numpy as np
from aie.iron import Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker
from iron.operators._kernels import declare_kernel
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_
import torch
from iron.common.test_utils import torch_dtype_map


@dataclass
class RMSNorm(MLIROperator):
    """AIE-accelerated RMS Normalization layer"""

    size: int
    num_aie_columns: int
    num_channels: int
    tile_size: int
    weighted: bool = False
    epsilon: float = 1e-5  # RMSNorm eps; Llama 1e-5 (default), Gemma 1e-6
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "weighted": "w",
        "epsilon": "eps",
    }

    def __post_init__(self):
        dev = aie_utils.get_current_device()
        shim_dma_limit = get_shim_dma_limit(dev)

        # The weighted design uses one weight ObjectFifo per channel shared across all
        # columns, so its ShimDMA budget is:
        #   (num_aie_columns * num_channels) in-fills
        #   + num_channels weight-fills
        #   + (num_aie_columns * num_channels) out-drains
        # The binding constraint is on the output (host→AIE) shim DMA channels:
        #   num_channels * (num_aie_columns + 1) <= shim_dma_limit
        if self.weighted:
            weighted_shim_usage = self.num_channels * (self.num_aie_columns + 1)
            if weighted_shim_usage > shim_dma_limit:
                raise ValueError(
                    f"weighted RMSNorm with num_aie_columns={self.num_aie_columns}, "
                    f"num_channels={self.num_channels} requires {weighted_shim_usage} ShimDMA "
                    f"output channels but device only has {shim_dma_limit}"
                )
        max_multiple = self.num_aie_columns * self.num_channels * self.tile_size
        if self.size % max_multiple != 0:
            raise ValueError(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * num_channels * tile_size ({max_multiple})"
            )
        total_shimdma_channels = self.num_aie_columns * self.num_channels
        if total_shimdma_channels > shim_dma_limit:
            raise ValueError(
                f"num_aie_columns * num_channels ({total_shimdma_channels}) "
                f"exceeds ShimDMA limit of {shim_dma_limit} for this device"
            )
        MLIROperator.__init__(self, context=self.context)

    @property
    def weight_length(self) -> int:
        """Length of the weight vector, which here is one tile."""
        return self.tile_size

    def get_mlir_artifact(self):
        # Two designs, chosen by a field rather than by a file path now that
        # both live in this module.
        design = my_weighted_rms_norm if self.weighted else my_rms_norm
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(fn=design, bind_from=self),
        )

        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                source_path,
                callback_fn,
                (
                    aie_utils.get_current_device(),
                    self.size,
                    self.num_aie_columns,
                    self.num_channels,
                    self.tile_size,
                    0,  # trace_size
                    self.epsilon,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        # None: the designs declare their kernels as ExternalFunctions, from
        # two separate sources (rms_norm.cc and, when weighted, mul.cc), so
        # each gets its own object and upstream compiles both.
        return []

    @staticmethod
    def arg_spec(size, tile_size, weighted=False):
        # The optional weight sits between input and output, so this is not a
        # same-shape unary even though the two ends match.
        rows = (size // tile_size, tile_size)
        specs = [AIERuntimeArgSpec("in", rows)]
        if weighted:
            specs.append(AIERuntimeArgSpec("in", (tile_size,)))
        specs.append(AIERuntimeArgSpec("out", rows))
        return specs

    def reference(self, x, w=None):
        """CPU reference: row-wise RMS normalization, optionally weighted."""
        return reference(x, w=w, weighted=self.weighted, eps=self.epsilon)


# --------------------------------------------------------------------------
# The MLIR this operator generates (unweighted).
# --------------------------------------------------------------------------


def my_rms_norm(
    dev,
    size,
    num_aie_columns,
    num_channels,
    tile_size,
    trace_size,
    epsilon=1e-5,
    kernels_dir=None,
):
    per_tile_elements = 8192 if tile_size > 8192 else tile_size
    total_cores = num_aie_columns * num_channels
    per_core_elements = size // total_cores
    if size % total_cores != 0:
        raise ValueError(
            f"Number of elements ({size}) must be a multiple of {total_cores}."
        )
    N_div_n = per_core_elements // per_tile_elements
    chunk = size // num_aie_columns // num_channels  # For offset calculation
    dtype = bfloat16

    # Define tensor types
    tensor_ty = np.ndarray[(size,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    fifodepth = 1 if tile_size > 4096 else 2

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(tile_ty, name=f"in1_{i}_{j}", depth=fifodepth)
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(tile_ty, name=f"out_{i}_{j}", depth=fifodepth)
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # AIE Core Function declaration
    rms_norm_kernel = declare_kernel(
        "rms_norm_eps",
        [tile_ty, tile_ty, np.int32, np.float32],
        source=Path(kernels_dir) / get_kernel_dir(dev) / "rms_norm.cc",
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_out, rms_norm_kernel):
        # Number of sub-vector "tile" iterations
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out.acquire(1)
            rms_norm_kernel(elem_in1, elem_out, per_tile_elements, epsilon)
            of_in1.release(1)
            of_out.release(1)

    # Create a worker to run the task on a compute tile
    my_workers = [
        Worker(
            core_body,
            [
                of_in1s[i * num_channels + j].cons(),
                of_outs[i * num_channels + j].prod(),
                rms_norm_kernel,
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
    def sequence(A, C, of_in1s_prods, of_outs_conss):

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = TaskGroup()

        # Fill the input objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                of_in1s_prods[i * num_channels + j].fill(
                    A,
                    taps[i * num_channels + j],
                    group=tg,
                )
        # Drain the output objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                of_outs_conss[i * num_channels + j].drain(
                    C,
                    taps[i * num_channels + j],
                    wait=True,  # wait for the transfer to complete and data to be available
                    group=tg,
                )
        tg.finish()

    rt = Runtime(
        sequence,
        [
            tensor_ty,
            tensor_ty,
            [of.prod() for of in of_in1s],
            [of.cons() for of in of_outs],
        ],
    )
    # Place program components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt, workers=my_workers).resolve_program()


# --------------------------------------------------------------------------
# The MLIR this operator generates (weighted).
# --------------------------------------------------------------------------


def my_weighted_rms_norm(
    dev,
    size,
    num_aie_columns,
    num_channels,
    weight_length,
    trace_size,
    epsilon=1e-5,
    func_prefix="",
    kernels_dir=None,
):
    per_tile_elements = weight_length
    total_cores = num_aie_columns * num_channels
    n = per_tile_elements * total_cores
    if size % n != 0:
        raise ValueError(f"Number of elements ({size}) must be a multiple of {n}.")
    N_div_n = size // n
    chunk = size // total_cores
    dtype = bfloat16
    # Define tensor types
    tensor_ty = np.ndarray[(size,), np.dtype[dtype]]
    weights_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    # Set fifodepth based on weight_length
    fifodepth = 1 if weight_length > 4096 else 2

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(tile_ty, name=f"in1_{i}_{j}", depth=fifodepth)
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    # One weight ObjectFifo per channel, shared across columns in that channel
    of_in2s = [
        ObjectFifo(weights_ty, name=f"in2_weights_{j}", depth=fifodepth)
        for j in range(num_channels)
    ]
    of_out1s = [
        ObjectFifo(tile_ty, name=f"out1_{i}_{j}", depth=fifodepth)
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    of_out2s = [
        ObjectFifo(tile_ty, name=f"out2_{i}_{j}", depth=fifodepth)
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # AIE Core Function declaration
    arch_dir = get_kernel_dir(dev)
    rms_norm_kernel = declare_kernel(
        "rms_norm_eps",
        [tile_ty, tile_ty, np.int32, np.float32],
        source=Path(kernels_dir) / arch_dir / "rms_norm.cc",
        func_prefix=func_prefix,
    )
    eltwise_mul_kernel = declare_kernel(
        "eltwise_mul_bf16_vector_size",
        [tile_ty, weights_ty, tile_ty, np.int32],
        source=Path(kernels_dir) / arch_dir / "mul.cc",
        func_prefix=func_prefix,
    )

    # Define a task that will run on a compute tile
    def core_body_norm(of_in1, of_out1, rms_norm):
        # Number of sub-vector "tile" iterations
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out1.acquire(1)
            rms_norm(elem_in1, elem_out, per_tile_elements, epsilon)
            of_in1.release(1)
            of_out1.release(1)

    def core_body_mul(of_in1, of_in2, of_out2, eltwise_mul):
        # Number of sub-vector "tile" iterations
        elem_in2 = of_in2.acquire(1)
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out2.acquire(1)
            eltwise_mul(elem_in1, elem_in2, elem_out, per_tile_elements)
            of_in1.release(1)
            of_out2.release(1)
        of_in2.release(1)

    # Create workers to run the task on compute tiles,
    # one core for rms norm and another pipelined to do eltwise mul
    my_workers = []
    for i in range(num_aie_columns):
        for j in range(num_channels):
            idx = i * num_channels + j
            my_workers.append(
                Worker(
                    core_body_norm,
                    [
                        of_in1s[idx].cons(),
                        of_out1s[idx].prod(),
                        rms_norm_kernel,
                    ],
                )
            )
    for i in range(num_aie_columns):
        for j in range(num_channels):
            idx = i * num_channels + j
            my_workers.append(
                Worker(
                    core_body_mul,
                    [
                        of_out1s[idx].cons(),
                        of_in2s[j].cons(),
                        of_out2s[idx].prod(),
                        eltwise_mul_kernel,
                    ],
                )
            )

    # Create a TensorAccessPattern for each core
    # to describe the data movement.
    # The pattern chops the data in equal chunks
    # and moves them in parallel across columns and channels.
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
    def sequence(A, B, C, of_in1s_prods, of_in2s_prods, of_out2s_conss):

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = TaskGroup()

        # Fill the input objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                idx = i * num_channels + j
                of_in1s_prods[idx].fill(
                    A,
                    taps[idx],
                    group=tg,
                )
        # Fill weights (one per channel)
        for j in range(num_channels):
            of_in2s_prods[j].fill(
                B,
                group=tg,
            )
        # Drain the output objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                idx = i * num_channels + j
                of_out2s_conss[idx].drain(
                    C,
                    taps[idx],
                    wait=True,
                    group=tg,
                )
        tg.finish()

    rt = Runtime(
        sequence,
        [
            tensor_ty,
            weights_ty,
            tensor_ty,
            [of.prod() for of in of_in1s],
            [of.prod() for of in of_in2s],
            [of.cons() for of in of_out2s],
        ],
    )
    # Place program components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt, workers=my_workers).resolve_program()


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(x, w=None, weighted=False, eps=1e-5):
    """CPU reference: row-wise RMS normalization, optionally weighted (ground truth).

    Matches the AIE kernel: normalize by 1/sqrt(mean(x^2) + eps).
    """
    rms = torch.sqrt(torch.mean(x**2, dim=-1, keepdim=True) + eps)
    out = x / rms
    if weighted:
        out = out * w
    return out


def generate_golden_reference(
    rows: int, cols: int, dtype="bf16", seed=42, weighted=False, eps=1e-5
):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    if weighted:
        weights = torch.rand(cols, dtype=torch_dtype_map[dtype]) * val_range
        output_tensor = reference(input_tensor, weights, weighted=True, eps=eps)
        return {"input": input_tensor, "weight": weights, "output": output_tensor}
    else:
        output_tensor = reference(input_tensor, eps=eps)
        return {"input": input_tensor, "output": output_tensor}
