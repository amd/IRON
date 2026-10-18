# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""RoPE, rotary position embedding, over mlir-aie's ``datamovement.rope``.

``method_type`` rotates the two halves of each row (0, Hugging Face's) or
interleaved pairs (1, Meta's); Llama weights converted to Hugging Face are
re-permuted for the halves (huggingface/transformers#25199).
"""

import dataclasses

import numpy as np
from aie.iron import ObjectFifo, Worker, ceildiv, kernels
from aie.iron.controlflow import range_
from aie.iron.device import Device
from aie.iron.kernels import datamovement
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Extent,
    In,
    Operator,
    Out,
    Value,
    Auto,
    Param,
    Built,
    Operand,
    Rtp,
)
from iron.common.testing import Case, Testing


def _cases(cls, dev: Device):
    # One column, four (npu1's widest) and eight.
    out = [
        Case(
            dict(
                rows=32,
                cols=512,
                num_aie_columns=cols,
                angle_rows=angle_rows,
                method_type=0,
            )
        )
        for cols in (1, 4, 8)
        if cols <= dev.cols
        for angle_rows in (8, 32)
    ]
    # The second method, and the third angle-table size at the widest grid.
    out += [
        Case(dict(rows=32, cols=128, num_aie_columns=1, angle_rows=8, method_type=1)),
        Case(
            dict(
                rows=64,
                cols=128,
                num_aie_columns=dev.cols,
                angle_rows=16,
                method_type=0,
            ),
            extensive=True,
        ),
    ]
    out.append(Case(dict(rows=4096, cols=512, angle_rows=8, method_type=0), bench=True))
    return out


def _angles(op):
    """A random angle table, cos and sin interleaved, a row per position."""
    rng = np.random.default_rng(0)
    theta = rng.uniform(-np.pi, np.pi, (op.angle_rows, op.cols // 2))
    table = np.empty((op.angle_rows, op.cols), dtype=np.float32)
    table[:, ::2], table[:, 1::2] = np.cos(theta), np.sin(theta)
    return dict(given={op.angles: table.astype(bfloat16)})


class RoPE(Operator):
    """AIE-accelerated RoPE: one core per column, each rotating rows of
    ``cols``; each angle row serves ``rows / angle_rows`` consecutive rows.
    """

    test = Testing(_cases, draw=_angles)

    rows: int = Param()
    cols: int = Param()
    angle_rows: int = Param(derive=lambda op: op.rows)  # one row per position
    num_aie_columns: int = Auto()
    method_type: int = Param(default=0)

    x = In(rows, cols, obj_type=(1, cols), per=(num_aie_columns,))
    angles = In(angle_rows, cols, obj_type=(1, cols), per=(num_aie_columns,))
    y = Out(rows, cols, obj_type=(1, cols), per=(num_aie_columns,))
    # Either row count may be bounded per call: x[:n] and angles[:m].
    valid = Extent(rows)
    valid_angles = Extent(angle_rows)
    lut_rows = Value(derive=lambda op: ceildiv(op.valid_angles, op.num_aie_columns))
    rows_per_lut = Value(derive=lambda op: op.valid // op.valid_angles)

    def validate(self) -> None:
        if not (self.cols % 32 == 0 and self.cols >= 32):
            raise ValueError("cols must be multiple of 32 and >= 32")
        if self.method_type not in {0, 1}:
            raise ValueError(f"method_type must be 0 or 1, got {self.method_type}")
        if not (self.angle_rows <= self.rows and self.rows % self.angle_rows == 0):
            raise ValueError("angle_rows must divide rows")

    def resolve(self, dev):
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            fits=lambda c: self.rows % c == 0 and self.angle_rows % c == 0,
        )
        return dataclasses.replace(self, num_aie_columns=cols)

    def compatible(self) -> None:
        n = self.num_aie_columns
        if self.rows % n:
            raise ValueError("rows must be divisible by num_aie_columns")
        if not (self.angle_rows >= n and self.angle_rows % n == 0):
            raise ValueError("angle_rows must be divisible by num_aie_columns")

    def extent_unit(self, buffer: str) -> int | None:
        """A position's rows at a time, so each core gets its angle row."""
        return self.rows // self.angle_rows if buffer in ("x", "y") else None

    class Array(Operator.Array):
        cols: int
        method_type: int
        num_aie_columns: int
        angles: Operand
        lut_rows: Value
        rows_per_lut: Value
        x: Operand
        y: Operand

        def build(self) -> Built:

            tile = self.x.obj_type
            n = self.num_aie_columns
            kernel = kernels.datamovement.rope(
                self.cols, two_halves=self.method_type == 0
            )
            of_in = [ObjectFifo(tile) for i in range(n)]
            of_lut = [ObjectFifo(self.angles.obj_type) for i in range(n)]
            of_out = [ObjectFifo(tile) for i in range(n)]
            rtps = [Rtp([self.lut_rows, self.rows_per_lut]) for _ in range(n)]

            def core_body(of_in, of_lut, of_out, rope_kernel, rtp):
                words = rtp.read()
                lut_rows, rows_per_lut = words[self.lut_rows], words[self.rows_per_lut]
                for _ in range_(lut_rows):
                    elem_lut = of_lut.acquire(1)
                    for _ in range_(rows_per_lut):
                        elem_in = of_in.acquire(1)
                        elem_out = of_out.acquire(1)
                        rope_kernel(elem_in, elem_lut, elem_out, self.cols)
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
                        rtps[i],
                    ],
                )
                for i in range(n)
            ]
            self.x.bind([f.prod() for f in of_in])
            self.angles.bind([f.prod() for f in of_lut])
            self.y.bind([f.cons() for f in of_out])
            return Built(workers, rtps)

    def _kernel(self):
        return kernels.datamovement.rope(self.cols, two_halves=self.method_type == 0)

    def ops(self) -> int:
        return self._kernel().contract.ops_per_call * self.rows

    def reference(self, x, angles):
        """``datamovement.rope_ref`` on the packed ``angles`` buffer, each angle row
        serving ``rows / angles.shape[0]`` consecutive rows of ``x``.
        """
        rows, cols, lut_rows = x.shape[0], x.shape[-1], angles.shape[0]
        if rows % lut_rows != 0:
            raise ValueError(f"{rows} rows cannot share {lut_rows} angle rows evenly")
        # The table broadcast over the rows each angle row serves: no copy.
        y = datamovement.rope_ref(
            x.reshape(lut_rows, -1, cols, copy=False),
            angles.reshape(lut_rows, 1, cols, copy=False),
            two_halves=self.method_type == 0,
        )
        return y.reshape(x.shape, copy=False)

    def tolerance(self) -> Tolerance:
        return self._kernel().contract.tolerance
