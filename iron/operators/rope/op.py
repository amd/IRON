# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import dataclasses

import numpy as np
from aie.iron import ObjectFifo, Worker, kernels
from aie.iron.controlflow import range_
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Extent,
    In,
    Incompatible,
    Operator,
    Out,
    Value,
    auto,
    param,
)
from iron.common.testing import Case, Testing, device_columns


def _cases(cls):
    out = []
    for cols in [c for c in (1, 2, 4, 8) if c <= device_columns()]:
        for rows in (32, 64):
            for angle_rows in (8, 16, 32):
                for width in (128, 512):
                    for method_type in (0, 1):
                        regular = (
                            rows == 32
                            and width == 512
                            and angle_rows in (8, 32)
                            and method_type == 0
                        )
                        if not regular and width != 128:
                            continue
                        out.append(
                            Case(
                                dict(
                                    rows=rows,
                                    cols=width,
                                    num_aie_columns=cols,
                                    angle_rows=angle_rows,
                                    method_type=method_type,
                                ),
                                extensive=not regular,
                            )
                        )
    return out


def _angles(op):
    # One angle row per position, applied to rows // angle_rows consecutive
    # rows of x (the heads of one position, in the design's layout).
    return dict(angles=angle_table(op.angle_rows, op.cols, op.method_type))


class RoPE(Operator):
    """AIE-accelerated RoPE (Rotary Position Embedding) operator: one core per
    column, each rotating rows of ``cols``.

    Applies RoPE to each row of the input against a row of precomputed
    angles. The angle table may have fewer rows than the input; each angle
    row is then reused for ``rows / angle_rows`` consecutive input rows,
    which is the layout of a tensor holding several heads per token.

    - cols: the head dimension; rope.cc processes two 16-element vectors at a time
    - method_type: 0 = two-halves (HF), 1 = interleaved/Llama
    """

    test = Testing(_cases, tolerance=Tolerance.relative(0.05), draw=_angles)

    rows: int = param()
    cols: int = param()
    angle_rows: int = param(default=lambda op: op.rows)  # one row per position
    # None: every column the device's shim budget allows.
    num_aie_columns: int = auto()
    method_type: int = param(default=0, array=True)

    x = In(rows, cols, tile=(1, cols), per=(num_aie_columns,))
    angles = In(angle_rows, cols, tile=(1, cols), per=(num_aie_columns,))
    y = Out(rows, cols, tile=(1, cols), per=(num_aie_columns,))
    # Either row count may be bounded per call: x[:n] and angles[:m].
    valid = Extent(rows)
    valid_angles = Extent(angle_rows)
    # Angle rows each core consumes, and input rows per angle row: the
    # core's trip counts, written once per build, or per call under a bound.
    lut_rows = Value(np.int32, derive=lambda op: op.valid_angles // op.num_aie_columns)
    rows_per_lut = Value(np.int32, derive=lambda op: op.valid // op.valid_angles)

    def validate(self) -> None:
        if not (self.cols % 32 == 0 and self.cols >= 32):
            raise ValueError("cols must be multiple of 32 and >= 32")
        if self.method_type not in {0, 1}:
            raise ValueError(f"method_type must be 0 or 1, got {self.method_type}")
        if not (self.angle_rows <= self.rows and self.rows % self.angle_rows == 0):
            raise ValueError("angle_rows must divide rows")

    def resolve(self, dev):
        """Columns default to the most the device's shim budget allows that
        divide both the rows and the angle rows.
        """
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            fits=lambda c: self.rows % c == 0 and self.angle_rows % c == 0,
        )
        return dataclasses.replace(self, num_aie_columns=cols)

    def compatible(self) -> None:
        n = self.num_aie_columns
        if self.rows % n:
            raise Incompatible("rows must be divisible by num_aie_columns")
        if not (self.angle_rows >= n and self.angle_rows % n == 0):
            raise Incompatible("angle_rows must be divisible by num_aie_columns")

    def array(self, target) -> list:

        tile = self.x.tile
        n = self.num_aie_columns
        # method_type 0 = two-halves (HF), 1 = interleaved (Llama paper).
        kernel = kernels.datamovement.rope(self.cols, two_halves=self.method_type == 0)
        of_in = [ObjectFifo(tile, name=f"in_{i}") for i in range(n)]
        of_lut = [ObjectFifo(self.angles.tile, name=f"lut_{i}") for i in range(n)]
        of_out = [ObjectFifo(tile, name=f"out_{i}") for i in range(n)]
        # The two trip counts in an RTP, less any a graph bounds, which each
        # core reads from the scratchpad per call.
        elf = target.image == "elf"
        dyn_lut = self.uses_value("lut_rows") and elf
        dyn_rows = self.uses_value("rows_per_lut") and elf
        static = [
            nm for nm, d in (("lut_rows", dyn_lut), ("rows_per_lut", dyn_rows)) if not d
        ]
        rtp_ty = np.ndarray[(max(1, len(static)),), np.dtype[np.int32]]
        counts = [target.rtp(rtp_ty, name=f"counts_{i}") for i in range(n)]
        params = [
            p
            for p, d in (
                (self.lut_rows.param, dyn_lut),
                (self.rows_per_lut.param, dyn_rows),
            )
            if d
        ]
        barriers = [target.barrier() for _ in range(n)]
        cols = self.cols

        def core_body(of_in, of_lut, of_out, rope_kernel, counts, barrier, *words):
            barrier.wait_for_value(1)
            words = list(words)
            lut_rows = (
                words.pop(0).read() if dyn_lut else counts[static.index("lut_rows")]
            )
            rows_per_lut = (
                words.pop(0).read()
                if dyn_rows
                else counts[static.index("rows_per_lut")]
            )
            for _ in range_(lut_rows):
                elem_lut = of_lut.acquire(1)
                for _ in range_(rows_per_lut):
                    elem_in = of_in.acquire(1)
                    elem_out = of_out.acquire(1)
                    rope_kernel(elem_in, elem_lut, elem_out, cols)
                    of_in.release(1)
                    of_out.release(1)
                of_lut.release(1)

        workers = [
            Worker(
                core_body,
                [
                    of_in[i].cons(),
                    of_lut[i].cons(),
                    of_out[i].prod(),
                    kernel,
                    counts[i],
                    barriers[i],
                ]
                + params,
            )
            for i in range(n)
        ]
        for i in range(n):
            self.x.lane(i).bind(of_in[i].prod())
            self.angles.lane(i).bind(of_lut[i].prod())
            self.y.lane(i).bind(of_out[i].cons())
        if not dyn_lut:
            self.lut_rows.bind(counts, static.index("lut_rows"))
        if not dyn_rows:
            self.rows_per_lut.bind(counts, static.index("rows_per_lut"))
        return workers

    def reference(self, x, angles):
        """CPU reference for RoPE: see :func:`reference`."""
        return reference(x, angles, self.method_type)


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def compute_rope_params(
    head_dim,
    theta_base: float = 10_000,
    context_length=4096,
    method_type=0,
    freq_config=None,
    dtype=None,
):
    """Compute RoPE parameters (cos and sin tables)."""
    dtype = np.float32 if dtype is None else dtype
    assert head_dim % 2 == 0, "Embedding dimension must be even"

    # Compute the inverse frequencies
    inv_freq = 1.0 / (
        theta_base
        ** (
            np.arange(0, head_dim, 2, dtype=dtype)[: (head_dim // 2)].astype(np.float32)
            / head_dim
        )
    )

    # Frequency adjustments
    if freq_config is not None:
        low_freq_wavelen = (
            freq_config["original_context_length"] / freq_config["low_freq_factor"]
        )
        high_freq_wavelen = (
            freq_config["original_context_length"] / freq_config["high_freq_factor"]
        )

        wavelen = 2 * np.pi / inv_freq

        inv_freq_llama = np.where(
            wavelen > low_freq_wavelen, inv_freq / freq_config["factor"], inv_freq
        )

        smooth_factor = (
            freq_config["original_context_length"] / wavelen
            - freq_config["low_freq_factor"]
        ) / (freq_config["high_freq_factor"] - freq_config["low_freq_factor"])

        smoothed_inv_freq = (1 - smooth_factor) * (
            inv_freq / freq_config["factor"]
        ) + smooth_factor * inv_freq

        is_medium_freq = (wavelen <= low_freq_wavelen) & (wavelen >= high_freq_wavelen)
        inv_freq_llama = np.where(is_medium_freq, smoothed_inv_freq, inv_freq_llama)
        inv_freq = inv_freq_llama

    # Generate position indices
    positions = np.arange(context_length, dtype=dtype)

    # Compute the angles
    angles = (
        positions[:, None] * inv_freq[None, :]
    )  # Shape: (context_length, head_dim / 2)

    # Precompute sine and cosine
    cos = np.cos(angles)
    sin = np.sin(angles)

    return cos, sin


LLAMA3_FREQ_CONFIG = {
    "factor": 32.0,
    "low_freq_factor": 1.0,
    "high_freq_factor": 4.0,
    "original_context_length": 8192,
}


def angle_table(
    rows, cols, method_type=0, theta_base=500000.0, freq_config=LLAMA3_FREQ_CONFIG
):
    """The ``angles`` buffer for ``rows`` positions: bf16 ``[cos, sin, ...]``
    pairs along each row, the table the device kernel reads (Llama 3's
    frequency scaling by default).
    """
    cos, sin = compute_rope_params(
        head_dim=cols,
        theta_base=theta_base,
        context_length=rows,
        method_type=method_type,
        freq_config=freq_config,
    )
    table = np.zeros((rows, cols), dtype=bfloat16)
    table[:, ::2] = cos[:, : cols // 2]
    table[:, 1::2] = sin[:, : cols // 2]
    return table


def reference(x, angles, method_type=0):
    """CPU reference for RoPE from the operator's packed ``angles`` buffer.

    ``angles`` holds interleaved [cos, sin, cos, sin, ...] pairs along the last
    dim, the bf16 table the device reads. ``method_type`` 0 rotates the two
    halves of each row (HF transformers); 1 rotates its interleaved even/odd
    pairs (the Llama paper). The rotation is computed in fp32 and rounded once.

    ``angles`` may have fewer rows than ``x``; each angle row then applies to
    ``rows / angles.shape[0]`` *consecutive* rows of ``x``, matching the device
    kernel (``core_body`` acquires one angle row and applies it to that many
    consecutive input rows before moving on).
    """
    rows = x.shape[0]
    if rows % angles.shape[0] != 0:
        raise ValueError(
            f"{rows} rows cannot share {angles.shape[0]} angle rows evenly"
        )
    rep = rows // angles.shape[0]
    cos = np.repeat(angles[..., 0::2].astype(np.float32), rep, axis=0)
    sin = np.repeat(angles[..., 1::2].astype(np.float32), rep, axis=0)
    x32 = x.astype(np.float32)
    if method_type == 0:
        half = x.shape[-1] // 2
        x1, x2 = x32[..., :half], x32[..., half:]
        y = np.concatenate([x1 * cos - x2 * sin, x2 * cos + x1 * sin], axis=-1)
    elif method_type == 1:
        xe, xo = x32[..., 0::2], x32[..., 1::2]
        y = np.empty_like(x32)
        y[..., 0::2] = xe * cos - xo * sin
        y[..., 1::2] = xe * sin + xo * cos
    else:
        raise ValueError(f"method_type must be 0 or 1, got {method_type}")
    return y.astype(bfloat16)
