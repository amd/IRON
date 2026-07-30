# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


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
from iron.operators._trace import maybe_enable_trace


def softmax(
    dev,
    num_elements,
    num_aie_columns,
    num_channels,
    trace_size,
    tile_size,
    rtp_vector_size=None,
    vector_size_parameter=None,
    func_prefix="",
    kernel_obj_file="softmax.o",
):
    per_tile_elements = tile_size
    if rtp_vector_size is None:
        rtp_vector_size = per_tile_elements
    total_cores = num_aie_columns * num_channels
    per_core_elements = num_elements // total_cores
    if num_elements % total_cores != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {total_cores}."
        )
    N_div_n = per_core_elements // per_tile_elements
    chunk = num_elements // num_aie_columns // num_channels  # For offset calculation
    dtype = bfloat16

    # Define tensor types
    tensor_ty = np.ndarray[(num_elements,), np.dtype[dtype]]
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
    softmax_kernel = Kernel(
        f"{func_prefix}softmax_bf16",
        f"{func_prefix}{kernel_obj_file}",
        [tile_ty, tile_ty, np.int32],
    )
    mask_kernel = Kernel(
        f"{func_prefix}mask_bf16",
        f"{func_prefix}{kernel_obj_file}",
        [tile_ty, np.int32, np.int32],
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
            (1, num_elements),
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
