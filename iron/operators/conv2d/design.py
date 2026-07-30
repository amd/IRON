# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
MLIR Generation for 2D Convolution Operator

Generates MLIR code for conv2d operations on AIE2 (NPU) and AIE2P (NPU2).

==============================================================================
MODELING STATUS (Phase A: OC tiling for L1 fit, 1-col, host bias)
==============================================================================
DMA legality (hard):
  Each AIE compute tile has only **2 input DMA channels**. Designs must attach
  at most two consumers per core (input + weight). Bias ObjectFifo is illegal;
  bias is applied on the host (op.py).

Phase A (this revision) — out-channel (OC) tiling on a single column:
  Full NCHW input + full weights + full output often exceed ~64KB L1
  (e.g. 16→16 @ 32x32 ≈ 70KB triple). OC tiling keeps the full input in L1
  but only an ``oc_tile`` slice of weights and output per worker iteration:

    - Worker loops ``range_(num_oc_tiles)`` with OF elements sized to the tile.
    - Input TAP rebroadcasts the full input once per OC tile
      (sizes=[num_oc_tiles,1,1,input_size], strides=[0,0,0,1]).
    - Weight/output TAPs stream contiguous OC-major slices (axpy multi-packet
      style: one large TAP, OF packet = tile size).
    - Existing C++ kernels are invoked as mini-convs with out_channels=oc_tile
      (groups==1 only). No kernel ABI change.

  Depthwise / groups>1: OC tiling would require matching channel splits of
  input+weights; still full-tensor (must fit L1 or future spatial/channel
  tiling). Multi-column OC-split is Phase B.

Certainty: DMA 2-in legality 95%; OC tiling numerical for groups=1 ~85%
(pending NPU green); multi-col deferred.
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

# Leave headroom under ~64KB L1 for stack/locks when depth=1 holds in+w+out.
_L1_TRIPLE_BUDGET_BYTES = 56 * 1024
_BYTES_PER_BF16 = 2


def _choose_oc_tile(
    out_channels: int,
    input_elems: int,
    weight_per_oc: int,
    out_spatial: int,
    l1_budget_bytes: int = _L1_TRIPLE_BUDGET_BYTES,
) -> int:
    """Largest ``oc_tile`` dividing ``out_channels`` whose L1 triple fits.

    Triple = full input + weight tile + output tile (bf16).
    Returns 1 if even a single OC does not fit (caller may still OOM; spatial
    tiling is future work).
    """

    def fits(oc_t: int) -> bool:
        elems = input_elems + oc_t * weight_per_oc + oc_t * out_spatial
        return elems * _BYTES_PER_BF16 <= l1_budget_bytes

    if out_channels <= 0:
        return 1
    if fits(out_channels):
        return out_channels
    # Prefer larger tiles (fewer DMA iterations).
    for oc_t in range(out_channels - 1, 0, -1):
        if out_channels % oc_t == 0 and fits(oc_t):
            return oc_t
    return 1


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
    Generate MLIR for 2D convolution (single-column, Phase A OC tiling).

    ``use_bias`` is accepted for API compatibility with op.py / DesignGenerator
    but does **not** create a bias ObjectFifo (host applies bias). ``num_columns``
    is forced to 1. For ``groups==1``, out-channels may be tiled so L1 holds
    only (full input + weight/out OC tile) per iteration.
    """
    dtype = bfloat16

    # Single-core path (see MODELING STATUS). Multi-col is Phase B.
    _ = (use_bias, num_columns, tile_size, trace_size)
    num_columns = 1

    input_size = N * in_channels * in_height * in_width
    weight_size = out_channels * in_channels // groups * kernel_h * kernel_w
    output_size = N * out_channels * out_height * out_width
    out_spatial = out_height * out_width
    weight_per_oc = (in_channels // groups) * kernel_h * kernel_w

    input_ty = np.ndarray[(input_size,), np.dtype[dtype]]
    weight_ty = np.ndarray[(weight_size,), np.dtype[dtype]]
    output_ty = np.ndarray[(output_size,), np.dtype[dtype]]

    # Variant selection (must match C++ symbols in aie_kernels/*/conv2d.cc).
    is_depthwise = groups == in_channels and groups == out_channels
    is_pointwise = (not is_depthwise) and kernel_h == 1 and kernel_w == 1
    if is_depthwise:
        kernel_name = "depthwise_conv2d_bf16_vector"
    elif is_pointwise:
        kernel_name = "pointwise_conv2d_bf16_vector"
    else:
        kernel_name = "conv2d_bf16_vector"

    # OC tiling only for groups==1 (standard + pointwise). Depthwise / grouped
    # need coordinated input-channel splits (future).
    enable_oc_tiling = groups == 1 and not is_depthwise
    if enable_oc_tiling:
        oc_tile = _choose_oc_tile(
            out_channels, input_size, weight_per_oc, out_spatial
        )
    else:
        oc_tile = out_channels

    if out_channels % oc_tile != 0:
        # Defensive: _choose_oc_tile only returns divisors; full-OC path is fine.
        oc_tile = out_channels
    num_oc_tiles = out_channels // oc_tile

    weight_tile_elems = oc_tile * weight_per_oc
    output_tile_elems = N * oc_tile * out_spatial

    # FIFO element types = per-iteration L1 footprints.
    input_tile_ty = np.ndarray[(input_size if input_size > 0 else 1,), np.dtype[dtype]]
    weight_tile_ty = np.ndarray[
        (weight_tile_elems if weight_tile_elems > 0 else 1,), np.dtype[dtype]
    ]
    output_tile_ty = np.ndarray[
        (output_tile_elems if output_tile_elems > 0 else 1,), np.dtype[dtype]
    ]

    # depth=2 when 2x triple fits; else depth=1 (ping-pong would blow L1).
    triple_bytes = (input_size + weight_tile_elems + output_tile_elems) * _BYTES_PER_BF16
    fifodepth = 1 if triple_bytes * 2 > _L1_TRIPLE_BUDGET_BYTES else 2

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

    # apply_bias is always 0 here: host applies bias after NPU (DMA-safe).
    apply_bias = 0

    if kernel_name == "depthwise_conv2d_bf16_vector":
        # Full-channel depthwise (no OC tile split).
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
        # Mini pointwise over oc_tile out-channels.
        kernel_int_types = [np.int32] * 6
        kernel_call_scalars = [
            N,
            in_channels,
            oc_tile,
            in_height,
            in_width,
            apply_bias,
        ]
    else:
        # Standard mini-conv: out_channels = oc_tile, groups must be 1 for tiling.
        kernel_int_types = [np.int32] * 15
        kernel_call_scalars = [
            N,
            in_channels,
            in_height,
            in_width,
            oc_tile,
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
        # One mini-conv per OC tile (num_oc_tiles==1 => single full-tensor iter).
        for _ in range_(num_oc_tiles):
            elem_in = of_in.acquire(1)
            elem_w = of_w.acquire(1)
            elem_out = of_out.acquire(1)
            # Dummy bias pointer (apply_bias==0 => kernel does not read it).
            elem_bias = elem_in
            conv_kernel(elem_in, elem_w, elem_out, elem_bias, *kernel_call_scalars)
            of_in.release(1)
            of_w.release(1)
            of_out.release(1)

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

    # Input: rebroadcast full tensor once per OC tile (stride-0 outer dim).
    # When num_oc_tiles==1 this is equivalent to a plain linear full-tensor TAP.
    input_taps = [
        TensorAccessPattern(
            (1, input_size),
            0,
            [num_oc_tiles, 1, 1, input_size],
            [0, 0, 0, 1],
        )
        for _ in range(num_columns)
    ]
    # Weight/output: contiguous OC-major stream; OF packetization = tile elems
    # (same multi-packet pattern as axpy: one TAP covering all tiles).
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
