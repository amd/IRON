# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
MLIR Generation for 2D Convolution Operator

Generates MLIR code for conv2d operations on AIE2 (NPU) and AIE2P (NPU2).

==============================================================================
MODELING STATUS (Phase A–C MVP + Phase D.1 + D.3 partial spatial)
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

  D.3 PARTIAL — Spatial L1 tiling when full input exceeds budget after OC tiles:
    - DONE (pointwise): **H-strip** tiling for groups==1 + k=1 (no halo).
      When full-input L1 does not fit, choose largest ``tile_h | H`` such that
      **full oc_per_col** fits (num_oc_tiles==1; avoids combined OC×spatial).
      Worker iterations = num_spatial; multi-dim NCHW strip TAPs for in/out with
      **leading size=1** so aiex does not treat the strip count as
      repeat_count (transfer_len=prod(sizes[-3:])); weights rebroadcast with
      leading num_spatial + stride 0 (Phase A pattern). Kernel ABI unchanged
      (pointwise height=tile_h). HW-green: fat pointwise 32→64 @32×32 and
      @64×64 (1–8c, bias/nobias).
    - DONE (standard k>1, groups==1): **halo-aware H-strip** via host zero-pad.
      When full-input L1 does not fit: host pads input to (H+2ph)×(W+2pw);
      design L3 input is the padded tensor; kernel runs with pad_h=pad_w=0 and
      fixed receptive-field strip height
      ``in_h_tile = (tile_oh-1)*stride_h + kernel_h`` for output strips of
      height ``tile_oh | out_height`` (prefer full oc_per_col, num_oc_tiles==1).
      Overlapping input TAP stride = ``tile_oh * stride_h * padded_w``. Same
      leading-size=1 multi-dim pattern as pointwise. Kernel ABI unchanged.
      Enables e.g. 16→16 k3@64×64 and strided k3@64 that previously CE'd on
      full input (~128 KiB) alone.
    - DONE (DMA parity pad): when natural OH/OW only admit odd bf16 strip
      sizes (e.g. s2 p0 → 31×31, toh∈{1,31}), ``_plan_halo_h_strip`` adds a
      small **bottom/right** extra zero-pad so design OH/OW are DMA-legal
      (e.g. pad 64→66 → design 32×32), runs pad=0 strips, and host **crops**
      NPU output to true OH×OW. External API shapes stay true; staging out
      buffer when design spatial > true. Shared plan helper in design.py.
    - OPEN: OC×spatial without illegal mid-stride-0 rebroadcast, depthwise
      spatial if needed, W-strip/2D tiles, non-depthwise groups>1.
    - Still CE + extensive skip: groups=2 (non-depthwise) full-tensor L1
      (no channel/OC tiling for non-DW groups>1 yet).

  D.4 OPEN — Expand extensive multi-col matrix (4c where safe) / tol audit.

  D.5 OPEN — Kernel vector perf (only after D.1–D.2 stable).

Certainty (honest):
  Phase A 1c + Phase B/C 2c not-extensive paths are the supported CI surface
  (host bias, ≤2 DMA). D.3 pointwise + groups==1 k>1 host-pad H-strip
  (incl. DMA bottom/right extra-pad + crop) are implemented; packed bias and
  groups>1 non-DW L1 tiling remain open.
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


def _choose_h_tile_pointwise(
    height: int,
    in_channels: int,
    width: int,
    oc_per_col: int,
    weight_per_oc: int,
    l1_budget_bytes: int = _L1_TRIPLE_BUDGET_BYTES,
) -> int:
    """Largest ``tile_h | height`` so the full ``oc_per_col`` triple fits.

    Prefers **num_oc_tiles=1** with H-strip spatial only. AIE DMA BDs require
    positive strides, so we avoid multi-dim rebroadcast (stride 0) of input
    across OC tiles or weights across spatial tiles.

    Pointwise: in = IC*th*W, weight = oc_per_col*weight_per_oc, out = oc*th*W.
    Falls back to largest th where at least OC=1 fits (caller may still CE).
    """

    def fits_full_oc(th: int) -> bool:
        elems = (
            in_channels * th * width
            + oc_per_col * weight_per_oc
            + oc_per_col * th * width
        )
        return elems * _BYTES_PER_BF16 <= l1_budget_bytes

    th = _largest_divisor_fit(height, fits_full_oc)
    if fits_full_oc(th):
        return th

    def fits_min_oc(th: int) -> bool:
        elems = in_channels * th * width + weight_per_oc + th * width
        return elems * _BYTES_PER_BF16 <= l1_budget_bytes

    return _largest_divisor_fit(height, fits_min_oc)


def _rf_in_h(tile_oh: int, stride_h: int, kernel_h: int) -> int:
    """Input rows needed for ``tile_oh`` output rows (pad=0, fixed RF)."""
    return (max(1, tile_oh) - 1) * stride_h + kernel_h


def _extend_in_for_dma_even_out(
    in_h: int,
    in_w: int,
    kernel_h: int,
    kernel_w: int,
    stride_h: int,
    stride_w: int,
    pad_h: int,
    pad_w: int,
) -> tuple:
    """Minimal bottom/right input growth so OH and OW are both even and >=1.

    Odd OH/OW blocks H-strip TAP dims (bf16 BD sizes must be even). Extra
    input pixels are zeros on the host; valid crop is the un-extended out
    spatial (op crops after NPU). Returns (in_h', in_w', out_h', out_w').
    """

    def _out(h, w):
        oh = (h + 2 * pad_h - kernel_h) // stride_h + 1
        ow = (w + 2 * pad_w - kernel_w) // stride_w + 1
        return oh, ow

    h, w = int(in_h), int(in_w)
    for _ in range(h + w + 8):
        oh, ow = _out(h, w)
        if oh >= 1 and ow >= 1 and (oh % 2 == 0) and (ow % 2 == 0):
            return h, w, oh, ow
        if oh < 1 or (oh % 2 != 0):
            h += 1
        elif ow < 1 or (ow % 2 != 0):
            w += 1
        else:
            h += 1
    oh, ow = _out(h, w)
    return h, w, oh, ow


def _choose_h_tile_standard(
    out_height: int,
    in_channels: int,
    padded_w: int,
    oc_per_col: int,
    weight_per_oc: int,
    out_width: int,
    kernel_h: int,
    stride_h: int,
    l1_budget_bytes: int = _L1_TRIPLE_BUDGET_BYTES,
) -> int:
    """Largest ``tile_oh | out_height`` so full ``oc_per_col`` RF triple fits.

    Host-padded k>1 path: input strip height =
    ``(tile_oh-1)*stride_h + kernel_h``, width = padded_w, pad=0 in kernel.
    Prefers num_oc_tiles=1 (same DMA constraint as pointwise H-strip).
    """

    def fits_full_oc(toh: int) -> bool:
        ih = _rf_in_h(toh, stride_h, kernel_h)
        elems = (
            in_channels * ih * padded_w
            + oc_per_col * weight_per_oc
            + oc_per_col * toh * out_width
        )
        return elems * _BYTES_PER_BF16 <= l1_budget_bytes

    th = _largest_divisor_fit(out_height, fits_full_oc)
    if fits_full_oc(th):
        return th

    def fits_min_oc(toh: int) -> bool:
        ih = _rf_in_h(toh, stride_h, kernel_h)
        elems = in_channels * ih * padded_w + weight_per_oc + toh * out_width
        return elems * _BYTES_PER_BF16 <= l1_budget_bytes

    return _largest_divisor_fit(out_height, fits_min_oc)


def _plan_halo_h_strip(
    in_height: int,
    in_width: int,
    true_out_height: int,
    true_out_width: int,
    in_channels: int,
    oc_per_col: int,
    weight_per_oc: int,
    kernel_h: int,
    kernel_w: int,
    stride_h: int,
    stride_w: int,
    pad_h: int,
    pad_w: int,
    l1_budget_bytes: int = _L1_TRIPLE_BUDGET_BYTES,
    max_extra: int = 16,
):
    """Plan k>1 host-pad RF H-strip; may add bottom/right DMA pad.

    When natural padded spatial dims yield only odd DMA transfer sizes
    (e.g. s2 p0 → OW=31, toh∈{1,31}), search a small bottom/right extra
    zero-pad so design OH/OW admit even bf16 strip lengths. Host crops the
    NPU output back to ``true_out_*``.

    Returns a dict on success::
        padded_h, padded_w, design_oh, design_ow, tile_oh, in_h_tile,
        num_spatial, extra_h, extra_w
    or ``None`` if no legal pure-H-strip plan (num_oc_tiles==1) fits L1 with
    DMA-aligned strip sizes.
    """
    if oc_per_col <= 0 or true_out_height <= 0 or true_out_width <= 0:
        return None

    # Prefer zero extra, then minimal total extra (symmetric first).
    candidates = [(0, 0)]
    for total in range(1, max_extra + 1):
        for eh in range(0, total + 1):
            ew = total - eh
            candidates.append((eh, ew))
        # Also try equal-ish extras for square-ish outs (already covered).
    best = None
    best_key = None

    for extra_h, extra_w in candidates:
        padded_h = in_height + 2 * pad_h + extra_h
        padded_w = in_width + 2 * pad_w + extra_w
        if padded_h < kernel_h or padded_w < kernel_w:
            continue
        design_oh = (padded_h - kernel_h) // stride_h + 1
        design_ow = (padded_w - kernel_w) // stride_w + 1
        if design_oh < true_out_height or design_ow < true_out_width:
            continue
        if design_oh <= 0 or design_ow <= 0:
            continue

        # Try all toh | design_oh (large→small), not only max L1 toh — larger
        # toh can violate BD size dim max 1023 (strip = in_h_tile * padded_w).
        for tile_oh in range(design_oh, 0, -1):
            if design_oh % tile_oh != 0:
                continue
            num_spatial = design_oh // tile_oh
            if num_spatial <= 1:
                continue
            # TAP size dims must be even for bf16 (4-byte BD granularity).
            if num_spatial % 2 != 0:
                continue
            in_h_tile = _rf_in_h(tile_oh, stride_h, kernel_h)
            last_end = (num_spatial - 1) * tile_oh * stride_h + in_h_tile
            if last_end > padded_h:
                continue
            out_strip = tile_oh * design_ow
            in_strip = in_h_tile * padded_w
            if (out_strip % 2 != 0) or (in_strip % 2 != 0):
                continue
            # Each BD size dim is u10 [0:1023].
            if (
                in_strip > 1023
                or out_strip > 1023
                or in_channels > 1023
                or oc_per_col > 1023
                or num_spatial > 1023
            ):
                continue
            in_tile = in_channels * in_h_tile * padded_w
            out_tile = oc_per_col * tile_oh * design_ow
            w_tile = oc_per_col * weight_per_oc
            if not _l1_triple_fits(in_tile, w_tile, out_tile, l1_budget_bytes):
                continue

            # Prefer: zero extra, then smaller total extra, larger tile_oh.
            key = (
                extra_h + extra_w,
                abs(extra_h - extra_w),
                -tile_oh,
                padded_h + padded_w,
            )
            if best is None or key < best_key:
                best_key = key
                best = {
                    "padded_h": padded_h,
                    "padded_w": padded_w,
                    "design_oh": design_oh,
                    "design_ow": design_ow,
                    "tile_oh": tile_oh,
                    "in_h_tile": in_h_tile,
                    "num_spatial": num_spatial,
                    "extra_h": extra_h,
                    "extra_w": extra_w,
                }
            # First valid toh for this (extra_h,extra_w) is largest (range down);
            # still continue outer extras search via best_key ranking.
            break
            # Natural (0,0) with any valid toh is best-class; keep searching for
            # larger tile_oh only within same extra (key orders -tile_oh).

    return best


def _l1_triple_fits(
    input_elems: int,
    weight_elems: int,
    output_elems: int,
    l1_budget_bytes: int = _L1_TRIPLE_BUDGET_BYTES,
) -> bool:
    """True if in+weight+out (bf16) fit the L1 triple budget."""
    return (
        input_elems + weight_elems + output_elems
    ) * _BYTES_PER_BF16 <= l1_budget_bytes


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
    # spatial_h_tiling: D.3 H-strip when full input exceeds L1 (pointwise or k>1).
    # spatial_halo_pad: k>1 host-padded RF strips (kernel pad=0; L3 input padded).
    rebroadcast_input = False
    depthwise_split = False
    spatial_h_tiling = False
    spatial_halo_pad = False
    tile_h = in_height  # output strip height when spatial; else full in/out H
    in_h_tile = in_height  # input strip height (RF size when spatial_halo_pad)
    padded_h = in_height
    padded_w = in_width
    num_spatial = 1
    num_oc_tiles = 1
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
        num_oc_tiles = num_tiles
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
        # D.3: if full input still OOMs L1 → pointwise H-strip or k>1 host-pad RF.
        oc_per_col = out_channels // num_columns
        oc_tile = _choose_oc_tile(oc_per_col, input_size, weight_per_oc, out_spatial)
        if oc_per_col % oc_tile != 0:
            oc_tile = oc_per_col
        full_fits = _l1_triple_fits(
            input_size, oc_tile * weight_per_oc, N * oc_tile * out_spatial
        )
        if (not full_fits) and is_pointwise:
            # Pointwise H-strip (D.3): prefer full oc_per_col in L1 (num_oc=1)
            # so TAPs need no stride-0 rebroadcast (illegal on aie.dma_bd).
            tile_h = _choose_h_tile_pointwise(
                in_height, in_channels, in_width, oc_per_col, weight_per_oc
            )
            if in_height % tile_h != 0:
                tile_h = in_height
            num_spatial = max(1, in_height // tile_h)
            in_h_tile = tile_h
            in_tile_elems_base = N * in_channels * tile_h * in_width
            out_tile_sp = tile_h * out_width
            # Prefer full OC block when it fits with this tile_h.
            if _l1_triple_fits(
                in_tile_elems_base,
                oc_per_col * weight_per_oc,
                N * oc_per_col * out_tile_sp,
            ):
                oc_tile = oc_per_col
            else:
                oc_tile = _choose_oc_tile(
                    oc_per_col, in_tile_elems_base, weight_per_oc, out_tile_sp
                )
                if oc_per_col % oc_tile != 0:
                    oc_tile = oc_per_col
            num_oc_tiles = oc_per_col // oc_tile if oc_tile else 1
            # Only enable multi-dim spatial TAPs when pure H-strip (no OC
            # rebroadcast). Combined OC×spatial needs nested acquire (future).
            if num_oc_tiles != 1:
                # Cannot legally TAP-rebroadcast; keep full-input path (will
                # OOM at aiecc) — op._validate_l1_fit CEs when min tile fails.
                tile_h = in_height
                in_h_tile = in_height
                num_spatial = 1
                oc_tile = _choose_oc_tile(
                    oc_per_col, input_size, weight_per_oc, out_spatial
                )
                if oc_per_col % oc_tile != 0:
                    oc_tile = oc_per_col
                input_tile_elems = input_size
                weight_tile_elems = oc_tile * weight_per_oc
                output_tile_elems = N * oc_tile * out_spatial
                spatial_h_tiling = False
            else:
                spatial_h_tiling = num_spatial > 1
                input_tile_elems = in_tile_elems_base
                weight_tile_elems = oc_tile * weight_per_oc
                output_tile_elems = N * oc_tile * out_tile_sp
        elif not full_fits:
            # Standard k>1 H-strip (D.3): host zero-pads (conv pad + optional
            # bottom/right DMA pad); kernel pad=0 with fixed RF strip height;
            # overlapping input TAPs. May use design_oh/ow > true out (crop).
            plan = _plan_halo_h_strip(
                in_height,
                in_width,
                out_height,
                out_width,
                in_channels,
                oc_per_col,
                weight_per_oc,
                kernel_h,
                kernel_w,
                stride_h,
                stride_w,
                pad_h,
                pad_w,
            )
            if plan is not None:
                spatial_h_tiling = True
                spatial_halo_pad = True
                padded_h = plan["padded_h"]
                padded_w = plan["padded_w"]
                design_oh = plan["design_oh"]
                design_ow = plan["design_ow"]
                tile_oh = plan["tile_oh"]
                in_h_tile = plan["in_h_tile"]
                num_spatial = plan["num_spatial"]
                tile_h = tile_oh
                oc_tile = oc_per_col
                num_oc_tiles = 1
                in_tile_elems_base = N * in_channels * in_h_tile * padded_w
                out_tile_sp = tile_oh * design_ow
                input_tile_elems = in_tile_elems_base
                weight_tile_elems = oc_tile * weight_per_oc
                output_tile_elems = N * oc_tile * out_tile_sp
                # L3: padded input; output may be design spatial (host crops).
                input_size = N * in_channels * padded_h * padded_w
                input_ty = np.ndarray[(input_size,), np.dtype[dtype]]
                if design_oh != out_height or design_ow != out_width:
                    out_height = design_oh
                    out_width = design_ow
                    out_spatial = out_height * out_width
                    output_size = N * out_channels * out_spatial
                    output_ty = np.ndarray[(output_size,), np.dtype[dtype]]
            else:
                tile_h = out_height
                in_h_tile = in_height
                num_spatial = 1
                padded_h = in_height
                padded_w = in_width
                oc_tile = _choose_oc_tile(
                    oc_per_col, input_size, weight_per_oc, out_spatial
                )
                if oc_per_col % oc_tile != 0:
                    oc_tile = oc_per_col
                input_tile_elems = input_size
                weight_tile_elems = oc_tile * weight_per_oc
                output_tile_elems = N * oc_tile * out_spatial
                spatial_h_tiling = False
                spatial_halo_pad = False
        else:
            input_tile_elems = input_size
            weight_tile_elems = oc_tile * weight_per_oc
            output_tile_elems = N * oc_tile * out_spatial

        num_oc_tiles = oc_per_col // oc_tile if oc_tile else 1
        num_tiles = num_spatial * num_oc_tiles
        if not spatial_h_tiling:
            rebroadcast_input = num_oc_tiles > 1
        kernel_channels = in_channels
        weight_elems_per_col = oc_per_col * weight_per_oc
        output_elems_per_col = N * oc_per_col * out_spatial
    else:
        # Non-depthwise grouped: 1-col; full tensor or k>1 host-pad H-strip.
        num_columns = 1
        oc_per_col = out_channels
        oc_tile = out_channels
        kernel_channels = in_channels
        weight_elems_per_col = weight_size
        output_elems_per_col = output_size
        if _l1_triple_fits(input_size, weight_size, output_size):
            num_tiles = 1
            input_tile_elems = input_size
            weight_tile_elems = weight_size
            output_tile_elems = output_size
        else:
            plan = _plan_halo_h_strip(
                in_height,
                in_width,
                out_height,
                out_width,
                in_channels,
                oc_per_col,
                weight_per_oc,
                kernel_h,
                kernel_w,
                stride_h,
                stride_w,
                pad_h,
                pad_w,
            )
            if plan is not None:
                spatial_h_tiling = True
                spatial_halo_pad = True
                padded_h = plan["padded_h"]
                padded_w = plan["padded_w"]
                design_oh = plan["design_oh"]
                design_ow = plan["design_ow"]
                tile_oh = plan["tile_oh"]
                in_h_tile = plan["in_h_tile"]
                num_spatial = plan["num_spatial"]
                tile_h = tile_oh
                oc_tile = oc_per_col
                num_oc_tiles = 1
                num_tiles = num_spatial
                in_tile_elems_base = N * in_channels * in_h_tile * padded_w
                out_tile_sp = tile_oh * design_ow
                input_tile_elems = in_tile_elems_base
                weight_tile_elems = oc_tile * weight_per_oc
                output_tile_elems = N * oc_tile * out_tile_sp
                input_size = N * in_channels * padded_h * padded_w
                input_ty = np.ndarray[(input_size,), np.dtype[dtype]]
                if design_oh != out_height or design_ow != out_width:
                    out_height = design_oh
                    out_width = design_ow
                    out_spatial = out_height * out_width
                    output_size = N * out_channels * out_spatial
                    output_ty = np.ndarray[(output_size,), np.dtype[dtype]]
                weight_elems_per_col = weight_tile_elems
                output_elems_per_col = output_size
            else:
                num_tiles = 1
                input_tile_elems = input_size
                weight_tile_elems = weight_size
                output_tile_elems = output_size

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
        # Mini pointwise over oc_tile out-channels; height may be H-strip (D.3).
        kernel_int_types = [np.int32] * 6
        kernel_call_scalars = [
            N,
            in_channels,
            oc_tile,
            tile_h,
            in_width,
            apply_bias,
        ]
    else:
        # Standard mini-conv: out_channels = oc_tile when groups==1 tiled.
        # Halo H-strip: strip-local spatial dims + pad=0 (host supplies pad).
        k_in_h = in_h_tile if spatial_halo_pad else in_height
        k_in_w = padded_w if spatial_halo_pad else in_width
        k_out_h = tile_h if spatial_halo_pad else out_height
        k_pad_h = 0 if spatial_halo_pad else pad_h
        k_pad_w = 0 if spatial_halo_pad else pad_w
        kernel_int_types = [np.int32] * 15
        kernel_call_scalars = [
            N,
            in_channels,
            k_in_h,
            k_in_w,
            oc_tile,
            k_out_h,
            out_width,
            kernel_h,
            kernel_w,
            stride_h,
            stride_w,
            k_pad_h,
            k_pad_w,
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
        # Spatial H-strip: num_tiles == num_spatial (num_oc_tiles==1); weights
        # rebroadcast via outermost TAP dim stride 0 (legal Phase A pattern).
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
    if spatial_h_tiling:
        # D.3 H-strip (pointwise or k>1 host-pad RF), num_oc_tiles==1.
        # CRITICAL (aiex.shim_dma_single_bd_task): sizes[0] becomes
        # repeat_count=sizes[0]-1 and transfer_len=prod(sizes[-3:]).
        # For strided multi-packet, put a leading 1 so repeat_count=0 and
        # transfer_len covers all strips (one BD, no BD-ID blowup).
        # Weight rebroadcast uses leading num_spatial + stride 0 (same as
        # Phase A full-input rebroadcast).
        if spatial_halo_pad:
            # Overlapping RF strips on host-padded NCHW: step tile_oh * sh rows.
            strip_elems = in_h_tile * padded_w
            strip_step = tile_h * stride_h * padded_w
            ch_plane = padded_h * padded_w
        else:
            # Pointwise: non-overlapping equal in/out H strips.
            strip_elems = tile_h * in_width
            strip_step = strip_elems
            ch_plane = in_height * in_width
        out_strip = tile_h * out_width
        input_taps = [
            TensorAccessPattern(
                (1, input_size),
                0,
                [1, num_spatial, in_channels, strip_elems],
                [0, strip_step, ch_plane, 1],
            )
            for _ in range(num_columns)
        ]
        weight_taps = [
            TensorAccessPattern(
                (1, weight_size),
                i * weight_elems_per_col,
                [num_spatial, 1, 1, weight_tile_elems],
                [0, 0, 0, 1],
            )
            for i in range(num_columns)
        ]
        output_taps = [
            TensorAccessPattern(
                (1, output_size),
                i * output_elems_per_col,
                [1, num_spatial, oc_tile, out_strip],
                [0, out_strip, out_height * out_width, 1],
            )
            for i in range(num_columns)
        ]
    elif depthwise_split:
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
