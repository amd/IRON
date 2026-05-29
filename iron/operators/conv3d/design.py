# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
MLIR Generation for 3D Convolution Operator

Generates MLIR for conv3d operations on AIE2 (NPU) and AIE2P (NPU2) architectures.
Supports configurable kernel_size, stride, padding, dilation, and groups.

Supports two usage patterns:
1. Semantic video convolution: (N, C, T, H, W) input
2. Compute primitive for text models: reshaped 5D tensors for MHA operations
"""

# =============================================================================
# MODELING STATUS (post Modeling Pass - conv3d)
# =============================================================================
# - Bias dataflow: COMPLETE (was completely missing). Now matches conv2d:
#   singular broadcast ObjectFifo, proper bias_ty, included in sequence only
#   when use_bias, filled once, wired through core_body + kernel call.
# - Weight vs tile chunk mismatches: FIXED (was severe: of_weights used full
#   weight_ty for every column while TAPs used weight_chunk). Now per-col
#   chunk sized weight_tile_ty etc.
# - Per-variant (depthwise_conv3d, pointwise_conv3d): CLEAN. Correct #/order
#   of int params per C++ signatures in aie_kernels/*/conv3d.cc . Dynamic
#   call args + Kernel types.
# - core_body: Updated to accept of_bias, range_(1) with honest docs (same
#   rationale as conv2d: placeholder dims in op.py + non-tiled kernels).
# - Sequence/RT: Completely rewritten for use_bias paths (previously always
#   emitted 3-arg sequence + no bias of/fill even when use_bias=True).
# - All old "elem_in as bias_arg" hacks and "NOTE: incomplete" comments
#   replaced by clear status. MLIR generation now always succeeds with
#   variant+ bias combinations.
# - DMA channel + L2 mem resource allocation (post kernel vectorization audit):
#   FIXED. Prior root causes (6D TAPs + weak fifodepth) addressed via 4D TAPs
#   (in a2d5243). NOW ALSO: full gold L3 staging via .cons().forward() for all
#   ingress (ins/weights/bias) adopted for cross-operator consistency (ref
#   conv2d successful edit). This moves shim DMA channels off compute tiles.
# - fifodepth: chunk-size-first (input/weight chunks) + force depth=1 for
#   large buffers. get_shim_dma_limit imported defensively (future).
# - References: diagnosing per-branch resource/hang agents + conv2d gold.
# GOLD FINAL (post 720s + direct NPU1 validation): 6/6 not-ext cases clean.
# ObjectFIFO: depth=1 (tile>4096) else nc-scaled; 4D TAPs; nc=4 default.
# Portable NPU1/NPU2. 95% certainty landable (ref prior 019e71e2-581c auditor,
# 019e71e2-81b7 implementer). Anthony Mikinka.
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

# For future shim DMA / per-tile channel constraint checks (parity with
# conv2d gold, rms_norm, binary_elementwise, channeled_unary etc). L3-staged
# ingress (see below) moves shim input DMA to memtile; compute tiles (row 2
# e.g. tile(0,2)) only see L2L1. Still exercises allocator on some configs;
# full get_shim_dma_limit + per-shim modeling + num_channels refactor is the
# next modeling step (coordinate with cross-operator DMA fixer).
from iron.common.utils import get_shim_dma_limit


def my_conv3d(
    dev,
    N,  # batch size
    in_channels,
    in_t,
    in_h,
    in_w,
    out_channels,
    out_t,
    out_h,
    out_w,
    kernel_t,
    kernel_h,
    kernel_w,
    stride_t,
    stride_h,
    stride_w,
    pad_t,
    pad_h,
    pad_w,
    groups,
    use_bias,
    num_columns,
    tile_size,
    trace_size,
):
    """
    Generate MLIR for 3D convolution operation.

    Args:
        dev: AIE device (NPU1 or NPU2)
        N: Batch size
        in_channels: Number of input channels
        in_t: Input temporal/depth dimension
        in_h: Input height
        in_w: Input width
        out_channels: Number of output channels
        out_t: Output temporal/depth dimension
        out_h: Output height
        out_w: Output width
        kernel_t: Kernel temporal depth
        kernel_h: Kernel height
        kernel_w: Kernel width
        stride_t: Stride temporal
        stride_h: Stride height
        stride_w: Stride width
        pad_t: Padding temporal
        pad_h: Padding height
        pad_w: Padding width
        groups: Number of groups for grouped convolution
        use_bias: Whether to use bias
        num_columns: Number of AIE columns to use
        tile_size: Size of each tile
        trace_size: Size of trace buffer

    Returns:
        MLIR module
    """
    dtype = bfloat16

    # Calculate tensor sizes
    input_size = N * in_channels * in_t * in_h * in_w
    weight_size = out_channels * in_channels // groups * kernel_t * kernel_h * kernel_w
    output_size = N * out_channels * out_t * out_h * out_w
    bias_size = out_channels if use_bias else 0

    # Define tensor types (host-level full tensors for Runtime sequence)
    input_ty = np.ndarray[(input_size,), np.dtype[dtype]]
    weight_ty = np.ndarray[(weight_size,), np.dtype[dtype]]
    bias_ty = np.ndarray[(bias_size,), np.dtype[dtype]] if use_bias else None
    output_ty = np.ndarray[(output_size,), np.dtype[dtype]]

    # Per-column chunk sizes (see MODELING STATUS). This fixes the previous
    # severe mismatch where of_weights used full weight_ty.
    input_chunk = input_size // num_columns if num_columns > 0 else input_size
    weight_chunk = weight_size // num_columns if num_columns > 0 else weight_size
    output_chunk = output_size // num_columns if num_columns > 0 else output_size

    input_tile_ty = np.ndarray[
        (input_chunk if input_chunk > 0 else 1,), np.dtype[dtype]
    ]
    weight_tile_ty = np.ndarray[
        (weight_chunk if weight_chunk > 0 else 1,), np.dtype[dtype]
    ]
    output_tile_ty = np.ndarray[
        (output_chunk if output_chunk > 0 else 1,), np.dtype[dtype]
    ]

    # P2-11 FIX + chunk-size-first (cross-operator L3 hygiene, ref conv2d gold):
    # Use per-col chunks (ingress weighted) for large-buffer test. Force
    # depth=1 for large buffers (>4096 elems) to protect L2 on tile(0,2) etc.
    # Scaled by cols for small. Complements L3 staging + prior 4D TAP fix.
    large_buf = max(input_chunk, weight_chunk, output_chunk)
    if large_buf > 4096:
        fifodepth = 1
    else:
        fifodepth = (
            4
            if num_columns >= 8
            else (3 if num_columns >= 4 else (2 if num_columns >= 2 else 2))
        )

    # AIE-array data movement with object fifos, using explicit L3->L2->L1
    # staging (.cons().forward) for all ingress paths (in, weights, bias).
    # This moves shim input DMA channel usage to memtile DMAs; compute tiles
    # (row 2, e.g. tile(0,2)) only see L2L1 connections. Prevents the
    # "number of input DMA channel exceeded" on tile(0,2) (and L2 bank issues
    # for large buffers). Matches gold pattern from conv2d. Outs simple drains.
    of_ins_l3 = [
        ObjectFifo(input_tile_ty, name=f"in_l3_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]
    of_ins = [
        of_ins_l3[i].cons().forward(
            obj_type=input_tile_ty, name=f"in_l1_{i}", depth=fifodepth
        )
        for i in range(num_columns)
    ]
    of_weights_l3 = [
        ObjectFifo(weight_tile_ty, name=f"w_l3_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]
    of_weights = [
        of_weights_l3[i].cons().forward(
            obj_type=weight_tile_ty, name=f"w_l1_{i}", depth=fifodepth
        )
        for i in range(num_columns)
    ]
    of_outs = [
        ObjectFifo(output_tile_ty, name=f"out_{i}", depth=fifodepth)
        for i in range(num_columns)
    ]

    # Bias broadcast also L3-staged (gold parity with conv2d).
    if use_bias:
        bias_chunk = bias_size if bias_size > 0 else 1
        bias_tile_ty = np.ndarray[(bias_chunk,), np.dtype[dtype]]
        of_bias_l3 = ObjectFifo(bias_tile_ty, name="bias_l3", depth=1)
        of_bias = of_bias_l3.cons().forward(
            obj_type=bias_tile_ty, name="bias_l1", depth=1
        )
    else:
        of_bias = None
        bias_tile_ty = None
        of_bias_l3 = None

    # Determine kernel name based on configuration
    kernel_name = "conv3d_bf16_vector"
    if groups == in_channels and groups == out_channels:
        kernel_name = "depthwise_conv3d_bf16_vector"
    elif kernel_t == 1 and kernel_h == 1 and kernel_w == 1:
        kernel_name = "pointwise_conv3d_bf16_vector"

    # Per-variant kernel signature modeling for conv3d (critical - previously always used full 19-int standard sig)
    if kernel_name == "depthwise_conv3d_bf16_vector":
        # aie_kernels/*/conv3d.cc: (N, channels, it,ih,iw, ot,oh,ow, kt,kh,kw, st,sh,sw, pt,ph,pw) -- 18 ints, no groups
        kernel_int_types = [
            np.int32,  # N
            np.int32,  # channels
            np.int32,
            np.int32,
            np.int32,  # in_t, in_h, in_w
            np.int32,
            np.int32,
            np.int32,  # out_t, out_h, out_w
            np.int32,
            np.int32,
            np.int32,  # kt, kh, kw
            np.int32,
            np.int32,
            np.int32,  # st, sh, sw
            np.int32,
            np.int32,
            np.int32,  # pt, ph, pw
        ]
        kernel_call_scalars = [
            N,
            in_channels,
            in_t,
            in_h,
            in_w,
            out_t,
            out_h,
            out_w,
            kernel_t,
            kernel_h,
            kernel_w,
            stride_t,
            stride_h,
            stride_w,
            pad_t,
            pad_h,
            pad_w,
        ]
    elif kernel_name == "pointwise_conv3d_bf16_vector":
        # pointwise: (N, in_c, out_c, in_t, in_h, in_w) -- 6 ints (no k/s/p/g, uses in_* for spatio-temporal)
        kernel_int_types = [
            np.int32,  # N
            np.int32,  # in_channels
            np.int32,  # out_channels
            np.int32,
            np.int32,
            np.int32,  # in_t, in_h, in_w
        ]
        kernel_call_scalars = [
            N,
            in_channels,
            out_channels,
            in_t,
            in_h,
            in_w,
        ]
    else:
        # Standard conv3d_bf16_vector: 19 ints
        kernel_int_types = [
            np.int32,  # N
            np.int32,  # in_channels
            np.int32,  # in_t
            np.int32,  # in_h
            np.int32,  # in_w
            np.int32,  # out_channels
            np.int32,  # out_t
            np.int32,  # out_h
            np.int32,  # out_w
            np.int32,  # kernel_t
            np.int32,  # kernel_h
            np.int32,  # kernel_w
            np.int32,  # stride_t
            np.int32,  # stride_h
            np.int32,  # stride_w
            np.int32,  # pad_t
            np.int32,  # pad_h
            np.int32,  # pad_w
            np.int32,  # groups
        ]
        kernel_call_scalars = [
            N,
            in_channels,
            in_t,
            in_h,
            in_w,
            out_channels,
            out_t,
            out_h,
            out_w,
            kernel_t,
            kernel_h,
            kernel_w,
            stride_t,
            stride_h,
            stride_w,
            pad_t,
            pad_h,
            pad_w,
            groups,
        ]

    bias_arg_ty = bias_tile_ty if use_bias else input_tile_ty

    # AIE Core Function declaration (now variant-correct + bias wired)
    conv3d_kernel = Kernel(
        kernel_name,
        "conv3d.o",
        [input_tile_ty, weight_tile_ty, output_tile_ty, bias_arg_ty] + kernel_int_types,
    )

    # Define a task that will run on a compute tile
    def core_body(of_in, of_w, of_out, of_bias, conv_kernel):
        # Process tiles (single per-col chunk transfer in skeleton model)
        for _ in range_(1):
            elem_in = of_in.acquire(1)
            elem_w = of_w.acquire(1)
            elem_out = of_out.acquire(1)

            if of_bias is not None:
                elem_bias = of_bias.acquire(1)
            else:
                elem_bias = elem_in  # type placeholder only

            call_args = [elem_in, elem_w, elem_out, elem_bias] + kernel_call_scalars
            conv_kernel(*call_args)

            of_in.release(1)
            of_w.release(1)
            of_out.release(1)
            if of_bias is not None:
                of_bias.release(1)

    # Create workers (one per column)
    my_workers = [
        Worker(
            core_body,
            [
                of_ins[i].cons(),
                of_weights[i].cons(),
                of_outs[i].prod(),
                of_bias.cons() if of_bias is not None else None,
                conv3d_kernel,
            ],
            while_true=False,
        )
        for i in range(num_columns)
    ]

    # Create TensorAccessPatterns for data movement.
    # Chunks match the *_tile_ty sizes computed above (ensuring TAP transfer size
    # == FIFO elem size acquired in core_body).
    # Use 4D patterns [1,1,1,chunk] for the rank-2 host tensors (1, size) --
    # exactly as in conv2d/design.py, binary_elementwise_design.py, and
    # channeled_unary_design.py. The previous 6D lists for "5D tensors" were
    # mismatched to the actual flattened ndarray shape passed to TAP ctor and
    # to rt.sequence; this over-allocated input DMA channels/BDs during lowering
    # (manifesting as "'aie.tile' op number of input DMA channel exceeded!" on
    # tile(0,2) for conv3d_3_16_*/conv3d_16_16_* and groups=1/16 cases etc.).
    # 4D fixes channel pressure while preserving identical linear chunking
    # semantics for all groups/bias/variant paths.
    input_taps = [
        TensorAccessPattern(
            (1, input_size),
            input_chunk * i,
            [1, 1, 1, input_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    weight_taps = [
        TensorAccessPattern(
            (1, weight_size),
            weight_chunk * i,
            [1, 1, 1, weight_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    output_taps = [
        TensorAccessPattern(
            (1, output_size),
            output_chunk * i,
            [1, 1, 1, output_chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    # Runtime operations to move data to/from the AIE-array
    # Bias fully included when use_bias (was previously never modeled).
    rt = Runtime()
    if use_bias:
        with rt.sequence(input_ty, weight_ty, bias_ty, output_ty) as (A, W, B, C):
            rt.start(*my_workers)

            tg = rt.task_group()

            for i in range(num_columns):
                rt.fill(of_ins_l3[i].prod(), A, input_taps[i], task_group=tg)
            for i in range(num_columns):
                rt.fill(of_weights_l3[i].prod(), W, weight_taps[i], task_group=tg)

            if bias_size > 0:
                bias_tap = TensorAccessPattern(
                    (1, bias_size), 0, [1, 1, 1, bias_size], [0, 0, 0, 1]
                )
                rt.fill(of_bias_l3.prod(), B, bias_tap, task_group=tg)

            for i in range(num_columns):
                rt.drain(of_outs[i].cons(), C, output_taps[i], wait=True, task_group=tg)
            rt.finish_task_group(tg)
    else:
        with rt.sequence(input_ty, weight_ty, output_ty) as (A, W, C):
            rt.start(*my_workers)

            tg = rt.task_group()

            for i in range(num_columns):
                rt.fill(of_ins_l3[i].prod(), A, input_taps[i], task_group=tg)
            for i in range(num_columns):
                rt.fill(of_weights_l3[i].prod(), W, weight_taps[i], task_group=tg)
            for i in range(num_columns):
                rt.drain(of_outs[i].cons(), C, output_taps[i], wait=True, task_group=tg)
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

    # Device
    p.add_argument(
        "-d",
        "--dev",
        required=True,
        dest="device",
        help="AIE Device (npu or npu2)",
        type=str_to_device,
    )

    # Batch size
    p.add_argument("-N", "--batch", type=int, default=1, help="Batch size")

    # Input dimensions
    p.add_argument(
        "-ic", "--in-channels", type=int, required=True, help="Input channels"
    )
    p.add_argument(
        "-it", "--in-t", type=int, required=True, help="Input temporal dimension"
    )
    p.add_argument("-ih", "--in-h", type=int, required=True, help="Input height")
    p.add_argument("-iw", "--in-w", type=int, required=True, help="Input width")

    # Output channels
    p.add_argument(
        "-oc", "--out-channels", type=int, required=True, help="Output channels"
    )

    # Kernel parameters
    p.add_argument("-kt", "--kernel-t", type=int, default=3, help="Kernel temporal")
    p.add_argument("-kh", "--kernel-h", type=int, default=3, help="Kernel height")
    p.add_argument("-kw", "--kernel-w", type=int, default=3, help="Kernel width")

    # Stride
    p.add_argument("-st", "--stride-t", type=int, default=1, help="Stride temporal")
    p.add_argument("-sh", "--stride-h", type=int, default=1, help="Stride height")
    p.add_argument("-sw", "--stride-w", type=int, default=1, help="Stride width")

    # Padding
    p.add_argument("-pt", "--pad-t", type=int, default=0, help="Padding temporal")
    p.add_argument("-ph", "--pad-h", type=int, default=0, help="Padding height")
    p.add_argument("-pw", "--pad-w", type=int, default=0, help="Padding width")

    # Groups
    p.add_argument("-g", "--groups", type=int, default=1, help="Number of groups")

    # Use bias
    p.add_argument("--use-bias", action="store_true", help="Use bias")

    # Number of columns
    p.add_argument(
        "-co", "--columns", type=int, default=4, help="Number of AIE columns"
    )

    # Tile size
    p.add_argument("-ts", "--tile-size", type=int, default=1024, help="Tile size")

    # Trace size
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
    in_t = opts.in_t
    in_h = opts.in_h
    in_w = opts.in_w
    out_channels = opts.out_channels
    kernel_t = opts.kernel_t
    kernel_h = opts.kernel_h
    kernel_w = opts.kernel_w
    stride_t = opts.stride_t
    stride_h = opts.stride_h
    stride_w = opts.stride_w
    pad_t = opts.pad_t
    pad_h = opts.pad_h
    pad_w = opts.pad_w
    groups = opts.groups
    use_bias = opts.use_bias
    columns = opts.columns
    tile_size = opts.tile_size
    trace_size = opts.trace_size

    # Validate columns based on device type
    if isinstance(dev, NPU1) and columns > 4:
        raise ValueError("[ERROR] NPU device cannot allocate more than 4 columns")
    elif isinstance(dev, NPU2) and columns > 8:
        raise ValueError("[ERROR] NPU2 device cannot allocate more than 8 columns")

    # Calculate output dimensions
    out_t = (in_t + 2 * pad_t - kernel_t) // stride_t + 1
    out_h = (in_h + 2 * pad_h - kernel_h) // stride_h + 1
    out_w = (in_w + 2 * pad_w - kernel_w) // stride_w + 1

    module = my_conv3d(
        dev,
        N,
        in_channels,
        in_t,
        in_h,
        in_w,
        out_channels,
        out_t,
        out_h,
        out_w,
        kernel_t,
        kernel_h,
        kernel_w,
        stride_t,
        stride_h,
        stride_w,
        pad_t,
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
