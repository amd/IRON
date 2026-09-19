# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from dataclasses import dataclass, field

import aie.utils as aie_utils

from iron.common.device_utils import get_kernel_dir
from iron.common import (
    MLIROperator,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
    same_shape_unary,
)
import numpy as np
from aie.iron import (
    Kernel,
    ObjectFifo,
    ScratchpadParameter,
    Program,
    Runtime,
    TaskGroup,
    Worker,
    Buffer,
    WorkerRuntimeBarrier,
    sync_parameters,
)
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.helpers.dialects.scf import _for as range_
from ml_dtypes import bfloat16
from iron.operators._kernels import declare_kernel, lut_sources
from iron.operators._trace import maybe_enable_trace
import torch
from iron.common.test_utils import torch_dtype_map


@dataclass
class Softmax(MLIROperator):
    """AIE-accelerated Softmax operation"""

    rows: int
    cols: int
    num_aie_columns: int = 1
    num_channels: int = 1
    rtp_vector_size: int | None = None
    vector_size_parameter: str | None = None
    context: object = field(default=None, repr=False)

    @property
    def size(self):
        return self.rows * self.cols

    def __post_init__(self):
        if self.rows % 16 != 0:
            raise ValueError(f"rows ({self.rows}) must be a multiple of 16")
        if self.cols % 16 != 0:
            raise ValueError(f"cols ({self.cols}) must be a multiple of 16")
        if self.rows % self.num_aie_columns != 0:
            raise ValueError(
                f"rows ({self.rows}) must be a multiple of num_aie_columns ({self.num_aie_columns})"
            )
        MLIROperator.__init__(self, context=self.context)

    @property
    def bundled_sources(self) -> tuple:
        """Translation units softmax.cc links but never calls through MLIR."""
        return lut_sources()

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            # The design is declared below in this file, so hand the function
            # over rather than importing this module a second time by path.
            DesignGenerator(fn=softmax, bind_from=self),
        )

    def get_kernel_artifacts(self):
        # None: the design declares its kernels as ExternalFunctions, with the
        # lut tables compiled into the same translation unit.
        return []

    @staticmethod
    def arg_spec(rows, cols):
        return same_shape_unary(rows * cols)

    def reference(self, x):
        """CPU reference: row-wise softmax over ``cols``.

        Note: ignores the runtime ``vector_size_parameter`` (if any); the
        reference always softmaxes over the full ``cols``. For decode-style
        usage with a masked tail, the trailing positions will not match the
        NPU output."""
        return reference(x.reshape(self.rows, self.cols))


# --------------------------------------------------------------------------
# The MLIR this operator generates.
# --------------------------------------------------------------------------


def softmax(
    dev,
    size,
    num_aie_columns,
    num_channels,
    trace_size,
    cols,
    rtp_vector_size=None,
    vector_size_parameter=None,
    func_prefix="",
    bundled_sources=(),
    kernels_dir=None,
):
    per_tile_elements = cols
    if rtp_vector_size is None:
        rtp_vector_size = per_tile_elements
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

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(tile_ty, name=f"in1_{i}_{j}")
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]
    of_outs = [
        ObjectFifo(tile_ty, name=f"out_{i}_{j}")
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # AIE Core Function declaration
    # Both live in softmax.cc, so they name one object: declared separately
    # they would compile that translation unit twice and each copy would
    # define both symbols.
    softmax_source = Path(kernels_dir) / get_kernel_dir(dev) / "softmax.cc"
    softmax_kernel = declare_kernel(
        "softmax_bf16",
        [tile_ty, tile_ty, np.int32],
        source=softmax_source,
        bundled_sources=bundled_sources,
        object_file_name="softmax.o",
        func_prefix=func_prefix,
    )
    mask_kernel = declare_kernel(
        "mask_bf16",
        [tile_ty, np.int32, np.int32],
        source=softmax_source,
        bundled_sources=bundled_sources,
        object_file_name="softmax.o",
        func_prefix=func_prefix,
    )

    # Vector size source: either a scratchpad Parameter (synced from host each
    # dispatch) or a write-RTP buffer set via rt.inline_ops at compile time.
    use_scratchpad = vector_size_parameter is not None
    vector_size_param = (
        ScratchpadParameter(vector_size_parameter, np.int32) if use_scratchpad else None
    )

    def core_body(
        of_in1, of_out, softmax_kernel, mask_kernel, vector_size_src, barrier
    ):
        barrier.wait_for_value(1)
        # `use_scratchpad` is a compile-time constant, so only one of these
        # branches is emitted into the core: a scratchpad Parameter read or a
        # write-RTP buffer load.
        if use_scratchpad:
            vector_size = vector_size_src.read()
        else:
            vector_size = vector_size_src[0]
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out.acquire(1)
            mask_kernel(elem_in1, vector_size, per_tile_elements)
            softmax_kernel(elem_in1, elem_out, per_tile_elements)
            of_in1.release(1)
            of_out.release(1)

    rtps = (
        []
        if use_scratchpad
        else [
            Buffer(
                np.ndarray[(1,), np.dtype[np.int32]],
                name=f"rtp_{i}_{j}",
                use_write_rtp=True,
            )
            for i in range(num_aie_columns)
            for j in range(num_channels)
        ]
    )

    barriers = [
        WorkerRuntimeBarrier()
        for i in range(num_aie_columns)
        for j in range(num_channels)
    ]

    # Create a worker to run the task on a compute tile
    def worker_args(i, j):
        idx = i * num_channels + j
        per_core_runtime = vector_size_param if use_scratchpad else rtps[idx]
        return [
            of_in1s[idx].cons(),
            of_outs[idx].prod(),
            softmax_kernel,
            mask_kernel,
            per_core_runtime,
            barriers[idx],
        ]

    my_workers = [
        Worker(core_body, worker_args(i, j))
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
    def sequence(A, C, in1_prods, out_conses):
        if use_scratchpad:
            # The host writes vector_size into the scratchpad via
            # ParameterScratchpad before each dispatch; sync delivers it to the
            # per-core parameter buffer.
            sync_parameters()
        else:
            # Set the static (compile-time) run-time parameter controlling how
            # many elements each core processes.
            for rtp in rtps:
                rtp[0] = rtp_vector_size

        for i in range(num_aie_columns * num_channels):
            barriers[i].set(1)

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = TaskGroup()

        # Fill the input objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                in1_prods[i * num_channels + j].fill(
                    A,
                    taps[i * num_channels + j],
                    group=tg,
                )
        # Drain the output objectFIFOs with data
        for i in range(num_aie_columns):
            for j in range(num_channels):
                out_conses[i * num_channels + j].drain(
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
    prog = Program(dev, rt, workers=my_workers)
    maybe_enable_trace(prog, trace_size, my_workers)
    return prog.resolve_program()


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------

"""Golden reference generator for softmax operator."""


def reference(x):
    """CPU reference: row-wise softmax over the last dim (ground truth)."""
    return torch.softmax(x, dim=-1)


def generate_golden_reference(rows: int, cols: int, dtype="bf16", seed=42):
    """
    Generate golden reference data for softmax.

    Returns:
        dict: Dictionary with tensors for inputs and outputs
    """
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    output_tensor = reference(input_tensor)
    return {"input": input_tensor, "output": output_tensor}
