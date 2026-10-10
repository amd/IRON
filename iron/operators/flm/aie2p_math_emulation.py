# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""AIE2P arithmetic in numpy, for references that match the device bit for bit.

The functions take and return float arrays unless they say otherwise. A
"bf16" result is a float array whose values bf16 represents.

- Every float to bf16, bfp16 or integer conversion on the device rounds toward
  minus infinity unless a kernel sets the rounding mode register. Host-side
  constants round to nearest even.
- AIE2P has no fp32 multiplier. fmul emulates its bf16-limb product.
- inv_kernel and gelu_kernel are aie_runtime_lib's table lookups for AIE2P.
  aie.iron.kernels.bf16_exp_lut_ref models the exponential table.
"""

import re
from functools import cache
from pathlib import Path

import numpy as np
from aie.iron.kernels.datamovement import limbs_f32_split
from aie.utils import bfp, config
from ml_dtypes import bfloat16

from iron.operators.flm.q4nx import bf16_to_f32


def f32_to_bf16_floor(x):
    """Round f32 to bf16 toward negative infinity, as the cores do."""
    u = np.ascontiguousarray(x, dtype=np.float32).view(np.uint32)
    inexact = (u & 0xFFFF) != 0
    negative = (u >> 31) != 0
    return ((u >> 16) + (inexact & negative)).astype(np.uint16)


def f32(x):
    """Round `x` to fp32."""
    return np.asarray(x, np.float64).astype(np.float32)


def to_bf16(x, rounding="floor"):
    """Convert floats to bf16 bit patterns, `rounding` "floor" (the device) or "rne"."""
    if rounding == "rne":
        return f32(x).astype(bfloat16).view(np.uint16)
    return f32_to_bf16_floor(f32(x))


def rb(x, rounding="floor"):
    """Round `x` to a bf16 value."""
    return bf16_to_f32(to_bf16(x, rounding))


def fmul(a, b):
    """An fp32 product as AIE2P computes it.

    AIE2P splits each operand into three bf16 limbs and adds the nine limb
    products in fp32. The result differs from the IEEE product in the last bit
    for a few inputs.
    """
    a, b = np.broadcast_arrays(np.asarray(a, np.float64), np.asarray(b, np.float64))
    A, B = ([l.astype(np.float32) for l in limbs_f32_split(v)] for v in (a, b))
    acc = None
    for i, j in (
        (0, 0),
        (0, 1),
        (1, 0),
        (0, 2),
        (1, 1),
        (2, 0),
        (1, 2),
        (2, 1),
        (2, 2),
    ):
        p = A[i].astype(np.float64) * B[j]
        acc = f32(p) if acc is None else f32(acc + p)
    return acc


def tree_sum(x, lanes):
    """fp32 sum over the last axis as an accumulator of `lanes` lanes computes
    it: running sums per lane, then a pairwise halving of the lanes.
    """
    x = np.asarray(x, np.float64)
    xs = x.reshape(x.shape[:-1] + (-1, lanes))
    acc = f32(xs[..., 0, :])
    for i in range(1, xs.shape[-2]):
        acc = f32(acc + xs[..., i, :])
    while acc.shape[-1] > 1:
        h = acc.shape[-1] // 2
        acc = f32(acc[..., :h] + acc[..., h:])
    return acc[..., 0]


def bfp16(x, axis):
    """Convert `x` to bfp16ebs8 in blocks of 8 along `axis`, with floor rounding.

    AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16 converts the operands of a bf16
    matmul to this format.
    """
    x = np.moveaxis(np.asarray(x, np.float32), axis, -1)
    return np.moveaxis(bfp.quantize(x, rounding="floor").astype(np.float64), -1, axis)


def fast_rsqrt(s):
    """1 / sqrt(s) in fp32: a 0x5f3759df seed, then two Newton steps."""
    s = f32(s)
    half = fmul(s, np.float32(0.5))
    y = (
        (np.uint32(0x5F3759DF) - (s.view(np.uint32) >> 1))
        .astype(np.uint32)
        .view(np.float32)
    )
    for _ in range(2):
        y = fmul(y, f32(np.float32(1.5) - fmul(fmul(half, y), y)))
    return y


# The mantissa of 1 / (1 + m / 128), in 7 bits.
INV_MANTISSA = np.round(256 / (1 + np.arange(128) / 128)).astype(np.uint32) & 0x7F


def inv_kernel(denom):
    """getInvBf16: 1 / `denom` as bf16, from the exponent and INV_MANTISSA. The
    relative error is up to 0.4%.
    """
    bits = f32(denom).view(np.uint32).astype(np.uint64) + 0x8000
    exponent = (bits & 0x7F800000) >> 23
    mantissa = (bits & 0x007FFFFF) >> 16
    inv_exp = (mantissa == 0).astype(np.uint64) + (253 - exponent)
    return bf16_to_f32(
        (((inv_exp << 7) + INV_MANTISSA[mantissa]) & 0xFFFF).astype(np.uint16)
    )


@cache
def gelu_segments():
    """getGeluBf16's table: 64 (slope, offset) segments of width 1/8 on [-4, 4).

    The function reads gelu_lut_ab from the aie_runtime_lib sources that the
    kernels compile against. No simple fit of GELU reproduces the table. The
    source holds each run of four segments twice, for the gather read.
    """
    path = Path(config.aie_runtime_lib_dir()) / "AIE2P" / "lut_based_ops.cpp"
    table = re.search(r"gelu_lut_ab\[\d+\]\s*=\s*\{([^}]*)\}", path.read_text())
    if table is None:
        raise ValueError(f"{path} has no gelu_lut_ab table")
    body = table[1]
    values = [float(v.strip().rstrip("f")) for v in body.split(",") if v.strip()]
    return np.array(values, np.float32).reshape(-1, 2, 8)[:, 0].reshape(-1, 2)


def gelu_kernel(x):
    """getGeluBf16: GELU from gelu_segments. The device reads the slope as bf16
    and the offset as fp32. Inputs outside [-4, 4) take the end segments.
    """
    x = np.asarray(x, np.float64)
    k = np.clip(np.floor(x * 128).astype(np.int64), -512, 511) >> 4
    pair = gelu_segments()[k + 32]
    slope = (pair[..., 0].view(np.uint32) & 0xFFFF0000).view(np.float32)
    return rb(f32(slope.astype(np.float64) * x + pair[..., 1]))
