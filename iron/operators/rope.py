# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""RoPE, rotary position embedding, over the mlir-aie ``datamovement.rope``
kernel, with its angle table (:func:`rope_angles`) and Llama 3's frequency
scaling (:data:`LLAMA_3_2`).

The kernel rotates in one of two conventions, ``method_type``: the two
halves of each row (0, the default) or interleaved pairs (1). Hugging
Face's ``transformers`` uses the halves and Meta's own repository the
pairs; Llama weights converted to Hugging Face have some layers re-permuted
for the halves, so with those weights it must be the halves
(huggingface/transformers#25199).
"""

import dataclasses
from collections.abc import Callable

import numpy as np
from aie.iron import ObjectFifo, Worker, kernels
from aie.iron.controlflow import range_
from aie.iron.kernels import datamovement
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
    return dict(angles=angle_table(op.angle_rows, op.cols))


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

    def extent_unit(self, buffer: str) -> int | None:
        """Under a bound the rows go round-robin over the columns, the input
        and output a position at a time (the rows one angle row serves), so
        each core gets the angle row of every position it rotates.
        """
        return self.rows // self.angle_rows if buffer in ("x", "y") else None

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
                    rope_kernel(elem_in, elem_lut, elem_out)
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

    def ops(self, target) -> int:
        kernel = kernels.datamovement.rope(self.cols, two_halves=self.method_type == 0)
        return kernel.contract.ops_per_call * self.rows

    def reference(self, x, angles):
        """CPU reference for RoPE: see :func:`reference`."""
        return reference(x, angles, self.method_type)


# --------------------------------------------------------------------------
# The angle table the kernel reads, and the CPU reference.
# --------------------------------------------------------------------------


#: A RoPE frequency scaling: the frequencies (radians per position, float64)
#: in, scaled out. :class:`Llama3RopeScaling` is Llama 3's.
RopeScaling = Callable[[np.ndarray], np.ndarray]


@dataclasses.dataclass(frozen=True)
class Llama3RopeScaling:
    """Llama 3's RoPE frequency scaling (``"rope_type": "llama3"``).

    How Llama 3.1 and later stretch a model trained at
    ``original_max_position_embeddings`` to a longer context, by frequency:
    one whose wavelength is under ``original / high_freq_factor`` positions
    is kept, one over ``original / low_freq_factor`` is divided by
    ``factor``, and one between is interpolated between the two by where its
    wavelength falls. The fields are the checkpoint's ``rope_scaling``.
    """

    factor: float
    low_freq_factor: float
    high_freq_factor: float
    original_max_position_embeddings: int

    def __call__(self, inv_freq: np.ndarray) -> np.ndarray:
        """``inv_freq`` (radians per position, per frequency), scaled."""
        original = self.original_max_position_embeddings
        wavelen = 2 * np.pi / inv_freq
        smooth = (original / wavelen - self.low_freq_factor) / (
            self.high_freq_factor - self.low_freq_factor
        )
        between = (1 - smooth) * inv_freq / self.factor + smooth * inv_freq
        return np.where(
            wavelen < original / self.high_freq_factor,
            inv_freq,
            np.where(
                wavelen > original / self.low_freq_factor,
                inv_freq / self.factor,
                between,
            ),
        )


#: Llama 3.2's scaling, as its checkpoints' ``rope_scaling`` gives it.
LLAMA_3_2 = Llama3RopeScaling(
    factor=32.0,
    low_freq_factor=1.0,
    high_freq_factor=4.0,
    original_max_position_embeddings=8192,
)


def rope_angles(
    head_dim: int,
    context_length: int,
    rope_base: float = 500000.0,
    scaling: RopeScaling | None = None,
) -> np.ndarray:
    """The RoPE table, ``(context_length, head_dim)`` float32: cos and sin
    interleaved per frequency, as the kernel reads it.

    ``inv_freq`` and each ``position * inv_freq`` are rounded to float32;
    ``scaling``, if given, is applied to the frequencies in float64 before
    that rounding, and each transcendental is evaluated in float64 and
    rounded once, so every entry is the correctly rounded float32 of the
    formula.
    """
    exponents = np.arange(0, head_dim, 2, dtype=np.float32) / np.float32(head_dim)
    inv_freq = 1.0 / np.power(rope_base, exponents.astype(np.float64))
    if scaling is not None:
        inv_freq = scaling(inv_freq)
    inv_freq = inv_freq.astype(np.float32)
    freqs = np.outer(np.arange(context_length, dtype=np.float32), inv_freq)
    angles = np.empty((context_length, head_dim), dtype=np.float32)
    angles[:, ::2] = np.cos(freqs.astype(np.float64))
    angles[:, 1::2] = np.sin(freqs.astype(np.float64))
    return angles


def angle_table(rows, cols):
    """The ``angles`` buffer for ``rows`` positions, bf16: Llama 3.2's table."""
    return rope_angles(cols, rows, scaling=LLAMA_3_2).astype(bfloat16)


def reference(x, angles, method_type=0):
    """CPU reference for RoPE from the operator's packed ``angles`` buffer.

    ``angles`` holds interleaved [cos, sin, cos, sin, ...] pairs along the last
    dim, the bf16 table the device reads. ``method_type`` 0 rotates the two
    halves of each row (HF transformers); 1 rotates its interleaved even/odd
    pairs (the Llama paper). It is the rope kernel's contract reference,
    ``datamovement.rope_ref``: computed in fp32 and rounded once.

    ``angles`` may have fewer rows than ``x``; each angle row then applies to
    ``rows / angles.shape[0]`` *consecutive* rows of ``x``, matching the device
    kernel (``core_body`` acquires one angle row and applies it to that many
    consecutive input rows before moving on).
    """
    if method_type not in (0, 1):
        raise ValueError(f"method_type must be 0 or 1, got {method_type}")
    rows, cols, lut_rows = x.shape[0], x.shape[-1], angles.shape[0]
    if rows % lut_rows != 0:
        raise ValueError(f"{rows} rows cannot share {lut_rows} angle rows evenly")
    # x viewed as (angle row, the rows it serves, cols) and the table
    # broadcast over the middle axis: no copy of either.
    y = datamovement.rope_ref(
        x.reshape(lut_rows, -1, cols, copy=False),
        angles.reshape(lut_rows, 1, cols, copy=False),
        two_halves=method_type == 0,
    )
    return y.reshape(x.shape, copy=False)
