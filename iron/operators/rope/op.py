# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import numpy as np
import torch

from iron.common.declare import (
    Incompatible,
    In,
    Operator,
    Out,
    Overlay,
    Resident,
    StreamIn,
    StreamOut,
    dim,
    operator,
    tunable,
)


@operator
class RoPEOverlay(Overlay):
    """The array for RoPE: one core per column, each rotating rows of ``cols``.

    Applies RoPE to each row of the input against a row of precomputed
    angles. The angle table may have fewer rows than the input; each angle
    row is then reused for ``rows / angle_rows`` consecutive input rows,
    which is the layout of a tensor holding several heads per token.

    - cols: the head dimension; rope.cc processes two 16-element vectors at a time
    - method_type: 0 = two-halves (HF), 1 = interleaved/Llama
    """

    cols: int = dim()
    num_aie_columns: int = tunable(1)
    method_type: int = 0

    x = StreamIn(1, cols, per=num_aie_columns)
    lut = StreamIn(1, cols, per=num_aie_columns)
    y = StreamOut(1, cols, per=num_aie_columns)
    lut_rows = Resident(np.int32)  # angle rows each core consumes
    rows_per_lut = Resident(np.int32)  # input rows per angle row

    def validate(self) -> None:
        if not (self.cols % 32 == 0 and self.cols >= 32):
            raise ValueError("cols must be multiple of 32 and >= 32")
        if self.method_type not in {0, 1}:
            raise ValueError(f"method_type must be 0 or 1, got {self.method_type}")

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker
        from aie.iron.controlflow import range_

        tile = self.x.tile
        n = self.num_aie_columns
        symbol = "rope_two_halves" if self.method_type == 0 else "rope"
        kernel = target.kernel(
            symbol,
            [tile, self.lut.tile, tile, np.int32],
            source=target.kernels_dir / "generic" / "rope.cc",
        )
        of_in = [ObjectFifo(tile, name=f"in_{i}") for i in range(n)]
        of_lut = [ObjectFifo(self.lut.tile, name=f"lut_{i}") for i in range(n)]
        of_out = [ObjectFifo(tile, name=f"out_{i}") for i in range(n)]
        i32x2 = np.ndarray[(2,), np.dtype[np.int32]]
        counts = [target.rtp(i32x2, name=f"counts_{i}") for i in range(n)]
        barriers = [target.barrier() for _ in range(n)]
        cols = self.cols

        def core_body(of_in, of_lut, of_out, rope_kernel, counts, barrier):
            barrier.wait_for_value(1)
            lut_rows = counts[0]
            rows_per_lut = counts[1]
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
                ],
            )
            for i in range(n)
        ]
        for i in range(n):
            self.x[i].bind(of_in[i].prod())
            self.lut[i].bind(of_lut[i].prod())
            self.y[i].bind(of_out[i].cons())
        self.lut_rows.bind(counts, 0)
        self.rows_per_lut.bind(counts, 1)
        return workers


@operator
class RoPE(Operator[RoPEOverlay]):
    """AIE-accelerated RoPE (Rotary Position Embedding) operator"""

    rows: int = dim()
    angle_rows: int | None = dim(None)

    x = In(rows, RoPEOverlay.cols, to=RoPEOverlay.x)
    angles = In(angle_rows, RoPEOverlay.cols, to=RoPEOverlay.lut)
    y = Out(rows, RoPEOverlay.cols, from_=RoPEOverlay.y)

    def validate(self) -> None:
        if self.angle_rows is None:
            self.angle_rows = self.rows
        if not (self.angle_rows <= self.rows and self.rows % self.angle_rows == 0):
            raise ValueError("angle_rows must divide rows")

    def compatible(self) -> None:
        n = self.ov.num_aie_columns
        if self.rows % n:
            raise Incompatible("rows must be divisible by num_aie_columns")
        if not (self.angle_rows >= n and self.angle_rows % n == 0):
            raise Incompatible("angle_rows must be divisible by num_aie_columns")

    def residents(self) -> dict[str, int]:
        return {
            "lut_rows": self.angle_rows // self.ov.num_aie_columns,
            "rows_per_lut": self.rows // self.angle_rows,
        }

    @property
    def cols(self) -> int:
        return self.ov.cols

    @property
    def method_type(self) -> int:
        return self.ov.method_type

    def reference(self, x, angles):
        """CPU reference for RoPE.

        Assumes ``angles`` holds interleaved [cos, sin, cos, sin, ...] pairs
        along the last dim (length ``cols``).  Only ``method_type == 0``
        (TWO_HALVES) is currently supported.

        ``angles`` may have fewer rows than ``x``; in that case the angles
        are tiled along the row dimension to match ``x``."""
        return reference(x, angles, self.method_type, self.rows, self.cols)


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def compute_rope_params(
    head_dim,
    theta_base=10_000,
    context_length=4096,
    method_type=0,
    freq_config=None,
    dtype=torch.float32,
):
    """Compute RoPE parameters (cos and sin tables)."""
    assert head_dim % 2 == 0, "Embedding dimension must be even"

    # Compute the inverse frequencies
    inv_freq = 1.0 / (
        theta_base
        ** (
            torch.arange(0, head_dim, 2, dtype=dtype)[: (head_dim // 2)].float()
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

        wavelen = 2 * torch.pi / inv_freq

        inv_freq_llama = torch.where(
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
        inv_freq_llama = torch.where(is_medium_freq, smoothed_inv_freq, inv_freq_llama)
        inv_freq = inv_freq_llama

    # Generate position indices
    positions = torch.arange(context_length, dtype=dtype)

    # Compute the angles
    angles = positions.unsqueeze(1) * inv_freq.unsqueeze(
        0
    )  # Shape: (context_length, head_dim / 2)

    # Precompute sine and cosine
    cos = torch.cos(angles)
    sin = torch.sin(angles)

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
    frequency scaling by default)."""
    cos, sin = compute_rope_params(
        head_dim=cols,
        theta_base=theta_base,
        context_length=rows,
        method_type=method_type,
        freq_config=freq_config,
    )
    table = torch.zeros((rows, cols), dtype=torch.bfloat16)
    table[:, ::2] = cos[:, : cols // 2]
    table[:, 1::2] = sin[:, : cols // 2]
    return table


def reference(x, angles, method_type=0, rows=None, cols=None):
    """CPU reference for RoPE from the operator's packed ``angles`` buffer.

    ``angles`` holds interleaved [cos, sin, cos, sin, ...] pairs along the last
    dim (length ``cols``), the bf16 table the device reads. ``method_type`` 0
    rotates the two halves of a row, 1 rotates even/odd pairs (the Llama
    paper's interleaving). ``angles`` may have fewer rows than ``x``; in that
    case each angle row is repeated for ``rows / angles.shape[0]``
    *consecutive* rows of ``x``, matching the device kernel (design.py's
    ``core_body`` acquires one angle row and applies it to that many
    consecutive input rows before moving on).
    """
    if method_type not in (0, 1):
        raise ValueError(f"method_type must be 0 or 1, got {method_type}")
    if cols is None:
        cols = x.shape[-1]
    if rows is None:
        rows = x.shape[0]
    half = cols // 2
    cos = angles[..., 0::2].to(torch.float32)
    sin = angles[..., 1::2].to(torch.float32)
    if cos.shape[0] != rows:
        if rows % cos.shape[0] == 0:
            rep = rows // cos.shape[0]
            cos = cos.repeat_interleave(rep, dim=0)
            sin = sin.repeat_interleave(rep, dim=0)
        else:
            cos = cos[:rows]
            sin = sin[:rows]
    x32 = x.to(torch.float32)
    if method_type == 1:
        x1, x2 = x32[..., 0::2], x32[..., 1::2]
    else:
        x1, x2 = x32[..., :half], x32[..., half:]
    y1 = x1 * cos - x2 * sin
    y2 = x2 * cos + x1 * sin
    if method_type == 1:
        y = torch.stack([y1, y2], dim=-1).reshape(x.shape)
    else:
        y = torch.cat([y1, y2], dim=-1)
    return y.to(torch.bfloat16)
