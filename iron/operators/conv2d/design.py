# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
MLIR Generation for 2D Convolution Operator

Generates MLIR code for conv2d operations on AIE2 (NPU) and AIE2P (NPU2).

==============================================================================
MODELING STATUS (Phase A–C MVP + Phase D.1 construction hardening)
==============================================================================
DMA legality (hard):
  Each AIE compute tile has only **2 input DMA channels**. Designs must attach
  at most two consumers per core (input + weight). Bias ObjectFifo is illegal;
  bias is applied on the host (op.py) after the NPU run (+ ``_sync_to_device``).

Phase A — L1 tiling per column (no kernel ABI break):

  1) Standard / pointwise (groups==1): **out-channel (OC) tiling**
     Full input in L1; weight/output OC-sliced per worker iteration.
     Input TAP rebroadcasts full input per tile when num_tiles>1.

  2) Depthwise: **channel tiling** of in+w+out (channel-contiguous packets).

  3) Other groups>1 (non-depthwise): full-tensor 1-col (must fit L1).

Phase B — multi-column split, still ≤2 input DMAs/core:
  Prior multi-col failures were illegal 3-ingress (bias OF) + invalid flattened
  chunking — not OC-split itself.

  - groups==1: split out_channels across columns (requires OC % cols == 0,
    else columns clamped down). Each column: full input broadcast + weight/out
    TAP offset to its OC block; Phase A oc_tile applied to oc_per_col.
  - depthwise: split channels across columns (C % cols == 0 or clamp).
  - Host bias unchanged (no third OF).

Phase C — mature-op CI / package surface (not a dataflow redesign):
  - ``AIEConv2d`` exported from ``iron.operators`` (public package surface).
  - not-extensive matrix: 16x16/32x32 CORE @ 1c (Phase A) **and** 16x16 CORE
    @ 2c multi-col smoke (Phase B path). Larger multi-col (4c/8c, 32x32+) and
    broader configs remain ``@pytest.mark.extensive``.

Phase D — full-parity remaining work (in progress):

  D.1 DONE — Construct-time constraints (op.py mirrors this file):
    - Column policy via ``_resolve_num_columns`` (divisibility + device max;
      NPU1≤4, NPU2≤8). ``effective_num_columns`` / ``requested_num_columns``.
    - L1 triple budget ``_L1_TRIPLE_BUDGET_BYTES`` (56 KiB): fail fast with
      ``AIEOperatorConstraintError`` when min OC/channel tile (or full grouped
      triple) cannot fit. groups==1 notes that multi-col does **not** shrink
      input L1 (broadcast). Bare asserts → ConstraintError (dilation/groups/
      positive dims/output spatial).
    - Re-validated in ``set_up_artifacts`` after device column clamp.

  D.2 OPEN — On-device packed bias (weights||bias, apply_bias=1) under ≤2
    input DMAs; host path remains default until implemented or measured
    evidence documents host-only as permanent.

  D.3 OPEN — Spatial L1 tiling when full input still exceeds budget after
    OC/channel tiles.

  D.4 OPEN — Expand extensive multi-col matrix (4c where safe) / tol audit.

  D.5 OPEN — Kernel vector perf (only after D.1–D.2 stable).

Certainty (honest):
  Phase A 1c + Phase B/C 2c not-extensive paths are the supported CI surface
  (host bias, ≤2 DMA). Construct-time L1/col errors are in place (D.1).
  Extensive multi-col and exotic shapes are best-effort until promoted.
  Packed bias and spatial tiling remain open (D.2–D.3).
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


def _largest_divisor_fit(n: int, fits) -> int:
    """Largest positive divisor of ``n`` for which ``fits(d)`` is true, else 1."""
    if n <= 0:
        return 1
    if fits(n):
        return n
    for d in range(n - 1, 0, -1):
        if n % d == 0 and fits(d):
            return d
    return 1


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

    return _largest_divisor_fit(out_channels, fits)


def _choose_channel_tile(
    channels: int,
    in_spatial: int,
    out_spatial: int,
    weight_per_c: int,
    l1_budget_bytes: int = _L1_TRIPLE_BUDGET_BYTES,
) -> int:
    """Largest channel tile for depthwise: tiles in+w+out together.

    Per-channel elems = in_spatial + weight_per_c + out_spatial (bf16).
    """

    def fits(c_t: int) -> bool:
        elems = c_t * (in_spatial + weight_per_c + out_spatial)
        return elems * _BYTES_PER_BF16 <= l1_budget_bytes

    return _largest_divisor_fit(channels, fits)


def _resolve_num_columns(
    requested: int,
    out_channels: int,
    in_channels: int,
    groups: int,
    is_depthwise: bool,
    max_cols: int,
) -> int:
    """Clamp column count for legal OC/channel splits and device limits."""
    n = max(1, int(requested) if requested is not None else 1)
    n = min(n, max_cols)
    if is_depthwise:
        while n > 1 and in_channels % n != 0:
            n -= 1
        return n
    if groups == 1:
        while n > 1 and out_channels % n != 0:
            n -= 1
        return n
    # Non-depthwise grouped: 1-col only (Phase A full-tensor).
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
    Generate MLIR for 2D convolution (Phase A L1 tiles + Phase B multi-col).

    ``use_bias`` is accepted for API compatibility but does **not** create a
    bias ObjectFifo (host applies bias). Columns: groups==1 OC-split and
    depthwise channel-split when divisible; otherwise clamped to 1.
    """
    dtype = bfloat16

    _ = (use_bias, tile_size, trace_size)

    # Device column cap (NPU1≤4, NPU2≤8); SequentialPlacer places one worker/col.
    if isinstance(dev, NPU1):
        max_cols = 4
    elif isinstance(dev, NPU2):
        max_cols = 8
    else:
        max_cols = getattr(dev, "cols", 4) or 4

    input_size = N * in_channels * in_height * in_width
    weight_size = out_channels * in_channels // groups * kernel_h * kernel_w
    output_size = N * out_channels * out_height * out_width
    in_spatial = in_height * in_width
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

    num_columns = _resolve_num_columns(
        num_columns, out_channels, in_channels, groups, is_depthwise, max_cols
    )

    # --- Phase A tile selection (per column) + Phase B split sizes -------------
    # rebroadcast_input: full input OF packet, repeated per tile (groups==1).
    # depthwise_split: per-col channel blocks for in/w/out (no full-input broadcast).
    rebroadcast_input = False
    depthwise_split = False
    # Per-column tensor footprints for TAPs (bytes/elems along OC or channel axis).
    weight_elems_per_col = weight_size
    output_elems_per_col = output_size
    input_elems_per_col = input_size

    if is_depthwise:
        # Phase B: split channels across columns; Phase A tile within col.
        c_per_col = in_channels // num_columns
        c_tile = _choose_channel_tile(c_per_col, in_spatial, out_spatial, weight_per_oc)
        if c_per_col % c_tile != 0:
            c_tile = c_per_col
        num_tiles = c_per_col // c_tile
        input_tile_elems = N * c_tile * in_spatial
        weight_tile_elems = c_tile * weight_per_oc
        output_tile_elems = N * c_tile * out_spatial
        kernel_channels = c_tile
        oc_tile = c_tile
        depthwise_split = True
        input_elems_per_col = N * c_per_col * in_spatial
        weight_elems_per_col = c_per_col * weight_per_oc
        output_elems_per_col = N * c_per_col * out_spatial
    elif groups == 1:
        # Phase B: OC split across columns; Phase A OC tile within col.
        oc_per_col = out_channels // num_columns
        oc_tile = _choose_oc_tile(oc_per_col, input_size, weight_per_oc, out_spatial)
        if oc_per_col % oc_tile != 0:
            oc_tile = oc_per_col
        num_tiles = oc_per_col // oc_tile
        input_tile_elems = input_size
        weight_tile_elems = oc_tile * weight_per_oc
        output_tile_elems = N * oc_tile * out_spatial
        rebroadcast_input = num_tiles > 1
        kernel_channels = in_channels
        weight_elems_per_col = oc_per_col * weight_per_oc
        output_elems_per_col = N * oc_per_col * out_spatial
    else:
        # Non-depthwise grouped: full tensors, 1-col only.
        num_columns = 1
        oc_tile = out_channels
        num_tiles = 1
        input_tile_elems = input_size
        weight_tile_elems = weight_size
        output_tile_elems = output_size
        kernel_channels = in_channels

    # FIFO element types = per-iteration L1 footprints.
    input_tile_ty = np.ndarray[
        (input_tile_elems if input_tile_elems > 0 else 1,), np.dtype[dtype]
    ]
    weight_tile_ty = np.ndarray[
        (weight_tile_elems if weight_tile_elems > 0 else 1,), np.dtype[dtype]
    ]
    output_tile_ty = np.ndarray[
        (output_tile_elems if output_tile_elems > 0 else 1,), np.dtype[dtype]
    ]

    # depth=2 when 2x triple fits; else depth=1 (ping-pong would blow L1).
    triple_bytes = (
        input_tile_elems + weight_tile_elems + output_tile_elems
    ) * _BYTES_PER_BF16
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
        # Mini depthwise over c_tile channels (or full when num_tiles==1).
        kernel_int_types = [np.int32] * 13
        kernel_call_scalars = [
            N,
            kernel_channels,
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
        # Standard mini-conv: out_channels = oc_tile when groups==1 tiled.
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
        # One mini-conv per tile (num_tiles==1 => single full-tensor iter).
        for _ in range_(num_tiles):
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

    # --- TAPs: Phase B per-column offsets; Phase A multi-packet within col -----
    if depthwise_split:
        # Channel blocks: in/w/out all offset by column * elems_per_col.
        input_taps = [
            TensorAccessPattern(
                (1, input_size),
                i * input_elems_per_col,
                [1, 1, 1, input_elems_per_col],
                [0, 0, 0, 1],
            )
            for i in range(num_columns)
        ]
    elif rebroadcast_input:
        # Full input rebroadcast once per OC tile (same on every column).
        input_taps = [
            TensorAccessPattern(
                (1, input_size),
                0,
                [num_tiles, 1, 1, input_size],
                [0, 0, 0, 1],
            )
            for _ in range(num_columns)
        ]
    else:
        # Single full-input transfer per column (num_tiles==1 groups==1 or grouped).
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
            i * weight_elems_per_col,
            [1, 1, 1, weight_elems_per_col],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]
    output_taps = [
        TensorAccessPattern(
            (1, output_size),
            i * output_elems_per_col,
            [1, 1, 1, output_elems_per_col],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
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
        "-co",
        "--columns",
        type=int,
        default=1,
        help="AIE columns (OC/channel split; clamped if not divisible)",
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
