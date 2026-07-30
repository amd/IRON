# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
MLIR Generation for 2D Convolution Operator

Generates MLIR code for conv2d operations on AIE2 (NPU) and AIE2P (NPU2).

==============================================================================
MODELING STATUS (post quintuple-check DMA + correctness pass)
==============================================================================
Root cause of residual "'aie.tile' op number of input DMA channel exceeded"
(even after L3 staging + get_shim_dma_limit column clamps):

  Each AIE compute tile has only **2 input DMA channels**. The prior design
  attached three consumers per core (input + weight + bias broadcast), which
  is illegal for any num_columns whenever use_bias=True. Global shim-channel
  budgeting cannot fix per-tile consumer oversubscription. Evidence:
  build/*/resource_alloc_crash.mlir + aiecc_repeater diagnostics (Jun 2026)
  and tests_latest.csv 0/1 on tip f5b586c bias 4c cases.

Correctness constraint with current C++ kernels:
  Kernels expect full NCHW tensors and full weight tensors. Flattened
  per-column chunking of input/weight/output is numerically invalid.
  Multi-column out-channel split + input broadcast is future work.

Production dataflow (this revision):
  - Force num_columns = 1 (full tensors on a single core).
  - Exactly 2 input ObjectFIFOs (in, weight) + 1 output ObjectFIFO.
  - No bias ObjectFifo. Bias is applied on the host after the NPU run
    (see op.py get_callable / _process_single). Kernels receive apply_bias=0
    and a dummy bias pointer so the dead `bias != NULL` path is not taken.
  - Simple (non-L3) ObjectFIFOs sufficient for 1-col / 2-ingress.
  - Variant kernels (standard / depthwise / pointwise) keep matching C++ decls.

Certainty: DMA legality 95% (2 in + 1 out per tile); numerical path 90% for
N=1 full-tensor 1-col with host bias; multi-col deferred.
==============================================================================
"""

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


def my_conv2d(
    dev,
    N,  # batch size
    in_channels,
    in_height,
    in_width,
    out_channels,
    out_height,
    out_width,
    kernel_h,
    kernel_w,
    stride_h,
    stride_w,
    pad_h,
    pad_w,
    groups,
    use_bias,
    num_columns,
    tile_size,
    trace_size,
):
    """
    Generate MLIR for 2D convolution (single-column full-tensor path).

    ``use_bias`` is accepted for API compatibility with op.py / DesignGenerator
    but does **not** create a bias ObjectFifo (host applies bias). ``num_columns``
    is forced to 1 so FIFO element sizes match full tensors expected by kernels.
    """
    dtype = bfloat16

    # Full-tensor single-core path (see MODELING STATUS).
    # Keep the parameter for call-site compatibility; ignore multi-col requests.
    _ = (use_bias, num_columns, tile_size, trace_size)
    num_columns = 1

    input_size = N * in_channels * in_height * in_width
    weight_size = out_channels * in_channels // groups * kernel_h * kernel_w
    output_size = N * out_channels * out_height * out_width

    input_ty = np.ndarray[(input_size,), np.dtype[dtype]]
    weight_ty = np.ndarray[(weight_size,), np.dtype[dtype]]
    output_ty = np.ndarray[(output_size,), np.dtype[dtype]]

    # Full tensors as FIFO elements (1-col).
    input_tile_ty = np.ndarray[(input_size if input_size > 0 else 1,), np.dtype[dtype]]
    weight_tile_ty = np.ndarray[
        (weight_size if weight_size > 0 else 1,), np.dtype[dtype]
    ]
    output_tile_ty = np.ndarray[
        (output_size if output_size > 0 else 1,), np.dtype[dtype]
    ]

    # 2 input OFs + 1 output OF => legal on AIE compute tiles (2 in DMA max).
    # depth=2 (axpy default) for reliable ping-pong; force depth=1 when the
    # three full-tensor buffers would exceed ~56KB of the ~64KB L1 budget
    # (bf16 = 2 bytes/elem; leave room for stack + locks).
    bytes_per = 2
    triple_bytes = (input_size + weight_size + output_size) * bytes_per
    fifodepth = 1 if triple_bytes * 2 > 56 * 1024 else 2
    of_ins = [
        ObjectFifo(input_tile_ty, name=f"in_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]
    of_weights = [
        ObjectFifo(weight_tile_ty, name=f"w_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]
    of_outs = [
        ObjectFifo(output_tile_ty, name=f"out_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]

    # Variant selection (must match C++ symbols in aie_kernels/*/conv2d.cc).
    kernel_name = "conv2d_bf16_vector"
    if groups == in_channels and groups == out_channels:
        kernel_name = "depthwise_conv2d_bf16_vector"
    elif kernel_h == 1 and kernel_w == 1:
        kernel_name = "pointwise_conv2d_bf16_vector"

    # apply_bias is always 0 here: host applies bias after NPU (DMA-safe).
    # Dummy bias buffer is the input tile (never read when apply_bias==0).
    apply_bias = 0

    if kernel_name == "depthwise_conv2d_bf16_vector":
        # (N, channels, ih, iw, oh, ow, kh, kw, sh, sw, ph, pw, apply_bias)
        kernel_int_types = [np.int32] * 13
        kernel_call_scalars = [
            N,
            in_channels,
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
            apply_bias,
        ]
    elif kernel_name == "pointwise_conv2d_bf16_vector":
        # (N, in_c, out_c, height, width, apply_bias)
        kernel_int_types = [np.int32] * 6
        kernel_call_scalars = [
            N,
            in_channels,
            out_channels,
            in_height,
            in_width,
            apply_bias,
        ]
    else:
        # Standard: 14 geometric ints + apply_bias
        kernel_int_types = [np.int32] * 15
        kernel_call_scalars = [
            N,
            in_channels,
            in_height,
            in_width,
            out_channels,
            out_height,
            out_width,
            kernel_h,
            kernel_w,
            stride_h,
            stride_w,
            pad_h,
            pad_w,
            groups,
            apply_bias,
        ]

    # 4th buffer arg kept for ABI; dummy type = input tile (unused when apply_bias=0).
    bias_arg_ty = input_tile_ty

    conv2d_kernel = Kernel(
        kernel_name,
        "conv2d.o",
        [input_tile_ty, weight_tile_ty, output_tile_ty, bias_arg_ty] + kernel_int_types,
    )

    def core_body(of_in, of_w, of_out, conv_kernel):
        for _ in range_(1):
            elem_in = of_in.acquire(1)
            elem_w = of_w.acquire(1)
            elem_out = of_out.acquire(1)
            # Dummy bias pointer (apply_bias==0 => kernel does not read it).
            elem_bias = elem_in
            conv_kernel(elem_in, elem_w, elem_out, elem_bias, *kernel_call_scalars)
            of_in.release(1)
            of_w.release(1)
            of_out.release(1)

    # Match axpy/binary: default while_true so the runtime keeps the core
    # alive for the DMA sequence; range_(1) performs a single full-tensor
    # transfer matching the host fill/drain.
    my_workers = [
        Worker(
            core_body,
            [
                of_ins[i].cons(),
                of_weights[i].cons(),
                of_outs[i].prod(),
                conv2d_kernel,
            ],
        )
        for i in range(num_columns)
    ]

    input_taps = [
        TensorAccessPattern(
            (1, input_size),
            0,
            [1, 1, 1, input_size],
            [0, 0, 0, 1],
        )
        for _ in range(num_columns)
    ]
    weight_taps = [
        TensorAccessPattern(
            (1, weight_size),
            0,
            [1, 1, 1, weight_size],
            [0, 0, 0, 1],
        )
        for _ in range(num_columns)
    ]
    output_taps = [
        TensorAccessPattern(
            (1, output_size),
            0,
            [1, 1, 1, output_size],
            [0, 0, 0, 1],
        )
        for _ in range(num_columns)
    ]

    rt = Runtime()
    # Always 3 host buffers: in, weight, out. Bias is host-side (op.py).
    with rt.sequence(input_ty, weight_ty, output_ty) as (A, W, C):
        rt.start(*my_workers)
        tg = rt.task_group()
        for i in range(num_columns):
            rt.fill(of_ins[i].prod(), A, input_taps[i], task_group=tg)
        for i in range(num_columns):
            rt.fill(of_weights[i].prod(), W, weight_taps[i], task_group=tg)
        for i in range(num_columns):
            rt.drain(
                of_outs[i].cons(),
                C,
                output_taps[i],
                wait=True,
                task_group=tg,
            )
        rt.finish_task_group(tg)

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
    p.add_argument(
        "-d",
        "--dev",
        required=True,
        dest="device",
        help="AIE Device (npu or npu2)",
        type=str_to_device,
    )
    p.add_argument("-N", "--batch", type=int, default=1, help="Batch size")
    p.add_argument(
        "-ic", "--in-channels", type=int, required=True, help="Input channels"
    )
    p.add_argument("-ih", "--in-height", type=int, required=True, help="Input height")
    p.add_argument("-iw", "--in-width", type=int, required=True, help="Input width")
    p.add_argument(
        "-oc", "--out-channels", type=int, required=True, help="Output channels"
    )
    p.add_argument("-kh", "--kernel-h", type=int, default=3, help="Kernel height")
    p.add_argument("-kw", "--kernel-w", type=int, default=3, help="Kernel width")
    p.add_argument("-sh", "--stride-h", type=int, default=1, help="Stride height")
    p.add_argument("-sw", "--stride-w", type=int, default=1, help="Stride width")
    p.add_argument("-ph", "--pad-h", type=int, default=0, help="Padding height")
    p.add_argument("-pw", "--pad-w", type=int, default=0, help="Padding width")
    p.add_argument("-g", "--groups", type=int, default=1, help="Number of groups")
    p.add_argument("--use-bias", action="store_true", help="Use bias (host-side)")
    p.add_argument(
        "-co", "--columns", type=int, default=1, help="AIE columns (forced to 1)"
    )
    p.add_argument("-ts", "--tile-size", type=int, default=1024, help="Tile size")
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
    in_channels = opts.in_channels
    in_height = opts.in_height
    in_width = opts.in_width
    out_channels = opts.out_channels
    kernel_h = opts.kernel_h
    kernel_w = opts.kernel_w
    stride_h = opts.stride_h
    stride_w = opts.stride_w
    pad_h = opts.pad_h
    pad_w = opts.pad_w
    groups = opts.groups
    use_bias = opts.use_bias
    columns = opts.columns
    tile_size = opts.tile_size
    trace_size = opts.trace_size

    if isinstance(dev, NPU1) and columns > 4:
        raise ValueError("[ERROR] NPU device cannot allocate more than 4 columns")
    elif isinstance(dev, NPU2) and columns > 8:
        raise ValueError("[ERROR] NPU2 device cannot allocate more than 8 columns")

    out_height = (in_height + 2 * pad_h - kernel_h) // stride_h + 1
    out_width = (in_width + 2 * pad_w - kernel_w) // stride_w + 1

    module = my_conv2d(
        dev,
        N,
        in_channels,
        in_height,
        in_width,
        out_channels,
        out_height,
        out_width,
        kernel_h,
        kernel_w,
        stride_h,
        stride_w,
        pad_h,
        pad_w,
        groups,
        use_bias,
        columns,
        tile_size,
        trace_size,
    )

    output_file_path = Path(opts.output_file_path)
    with open(output_file_path, "w") as f:
        f.write(str(module))
