# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import dataclasses
from typing import Any

import ml_dtypes
import numpy as np
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.helpers.util import np_dtype_to_mlir_type
from aie.iron import (
    Buffer,
    ObjectFifo,
    TaskGroup,
    Worker,
    ceildiv,
)
from aie.iron.controlflow import range_
from aie.iron.kernels import activation, zero
from aie.utils.verify import Tolerance

from iron.common import (
    Auto,
    Built,
    Divisors,
    Extent,
    In,
    Operand,
    Operator,
    Out,
    Param,
    Rtp,
    Value,
)
from iron.common.testing import Case, Testing

# softmax_bf16's vector step: its loops cover only whole steps.
_VECTOR_STEP = 32
# The longest row a core holds whole: its input and output, double-buffered.
_ROW_CAP = 4096
# A streamed row's block, read three times a call.
_BLOCK = 1024
# The floats a streamed row carries between blocks: the lanes' sums and the maximum.
_STATE = 64
# A streamed core unrolls its rows: 48 fit AIE2P's program memory, 64 do not.
_STREAMED_ROWS = 48


def _kernel(op, n: int):
    """The softmax factory over rows of ``n``, with ``op``'s (a Softmax's or
    its Array's) float32 options: banded, or with a pre-cap addend.
    """
    options = dict(input_dtype=op.input_dtype, soft_cap=op.soft_cap)
    if op.window is not None:
        return activation.softmax(n, window=op.window, period=op.period, **options)
    return activation.softmax(n, addend=op.has_addend, **options)


def _draw(op) -> dict:
    """``vectors()``'s keywords: the float32 path's logits and addend
    centred. The bf16 path draws its default, ``[0, 1)``.
    """
    if np.dtype(op.input_dtype) != np.dtype(np.float32):
        return {}
    return dict(centered=(op.x,) + ((op.addend,) if op.has_addend else ()))


def _banded_case(cls, dev) -> list:
    """EG2 audio's own combination: a soft cap, its own window and period,
    and a pre-cap addend.
    """
    return [
        Case(
            dict(
                rows=64,
                cols=32,
                num_aie_columns=2,
                num_channels=2,
                input_dtype=np.float32,
                soft_cap=50.0,
                has_addend=True,
                window=12,
                period=16,
            ),
            id="f32_soft_cap_banded_addend",
        )
    ]


class Softmax(Operator):
    """AIE-accelerated Softmax over each row: one core per (column, channel),
    each taking a contiguous run of rows.

    A core holds a row whole or, ``streamed``, reads it in ``block``-element
    blocks three times (maximum, sums, output). Under a per-call bound the
    elements past it come out as zeros, and only the blocks it covers move.
    """

    # Four cores, two columns of two: the fewest that exercise both splits.
    test = Testing(
        [
            Case(dict(rows=32, cols=1024, num_aie_columns=2, num_channels=2)),
            Case(dict(rows=16, cols=2048, num_aie_columns=2, num_channels=2)),
            Case(
                dict(rows=16, cols=4096, block=1024, num_aie_columns=2, num_channels=2),
                lower=True,
            ),
            Case(dict(rows=16, cols=4608, num_aie_columns=2, num_channels=2)),
            Case(dict(rows=32, cols=32768, num_aie_columns=2, num_channels=2)),
            Case(
                dict(rows=4096, cols=512, num_aie_columns=2, num_channels=2),
                bench=True,
            ),
            # The float32 input path: a plain row, then EG2 audio's own
            # combination (a soft cap, a band and a pre-cap addend).
            Case(
                dict(
                    rows=32,
                    cols=1024,
                    num_aie_columns=2,
                    num_channels=2,
                    input_dtype=np.float32,
                ),
                lower=True,
            ),
            _banded_case,
        ],
        draw=_draw,
    )

    rows: int = Param()
    cols: int = Param()
    num_aie_columns: int = Auto()
    num_channels: int = Auto(default=1)
    block: int = Auto(
        domain=Divisors(of=lambda op, dev: op.cols, step=_VECTOR_STEP, cap=_ROW_CAP)
    )
    streamed: bool = Auto(domain=(False, True))
    input_dtype: Any = Param(default=ml_dtypes.bfloat16, repr=False)
    # Float input only, mlir-aie's softmax_f32_bf16: a pre-cap addend and
    # cap * tanh(x / cap).
    soft_cap: float | None = Param(default=None)
    has_addend: bool = Param(default=False)
    # Float input only, softmax_rows_banded_f32_bf16: a band computed from
    # these two in the core (window, and the row's own query position,
    # wrapped every period rows), not a mask operand -- a core has two
    # input DMA channels, and x and addend already take both.
    window: int | None = Param(default=None)
    period: int | None = Param(default=None)

    length = Extent(cols)  # cols, or fewer per call

    x = In(
        rows,
        cols,
        dtype=input_dtype,
        obj_type=(block,),
        per=(num_aie_columns, num_channels),
    )
    # A float32 row added to x before the cap, such as relative-position logits.
    addend = In(
        rows,
        cols,
        dtype=np.float32,
        obj_type=(block,),
        per=(num_aie_columns, num_channels),
        when=has_addend,
    )
    y = Out(rows, cols, obj_type=(block,), per=(num_aie_columns, num_channels))
    valid_cols = Value(derive=lambda op: op.length)
    # A row held whole is one block, which the bound does not change.
    blocks = Value(derive=lambda op: ceildiv(op.length, op.block) if op.streamed else 1)

    def validate(self) -> None:
        if self.rows % 16 != 0:
            raise ValueError(f"Softmax: rows ({self.rows}) must be a multiple of 16")
        if self.cols % 16 != 0:
            raise ValueError(f"Softmax: cols ({self.cols}) must be a multiple of 16")
        if np.dtype(self.input_dtype) != np.dtype(np.float32) and (
            self.soft_cap is not None
            or self.has_addend
            or self.window is not None
            or self.period is not None
        ):
            raise ValueError(
                "Softmax: soft_cap, addend, window and period are options "
                "of the float32 input path; pass input_dtype=np.float32"
            )
        if (self.window is None) != (self.period is None):
            raise ValueError("Softmax: window and period are given together")
        if self.window is not None and not self.has_addend:
            raise ValueError(
                "Softmax: the banded path (window, period) always takes a "
                "pre-cap addend; pass has_addend=True"
            )

    def resolve(self, dev):
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: self.rows % (c * self.num_channels) == 0,
        )
        if np.dtype(self.input_dtype) == np.dtype(np.float32):
            if self.streamed:
                raise ValueError("Softmax: the float32 input path does not stream")
            return dataclasses.replace(
                self, num_aie_columns=cols, block=self.cols, streamed=False
            )
        block = self.block
        if block is None:
            bounded = "length" in self.bound_extents
            per_core = self.rows // (cols * self.num_channels)
            long = self.cols > _ROW_CAP or (bounded and per_core <= _STREAMED_ROWS)
            block = (
                max(
                    (
                        b
                        for b in range(_VECTOR_STEP, _BLOCK + 1, _VECTOR_STEP)
                        if self.cols % b == 0
                    ),
                    default=min(self.cols, _BLOCK),
                )
                if long
                else self.cols
            )
        streamed = block < self.cols if self.streamed is None else self.streamed
        return dataclasses.replace(
            self, num_aie_columns=cols, block=block, streamed=streamed
        )

    @property
    def cores(self) -> int:
        return self.num_aie_columns * self.num_channels

    def compatible(self) -> None:
        if np.dtype(self.input_dtype) == np.dtype(np.float32) and (
            "length" in self.bound_extents
        ):
            raise ValueError(
                f"Softmax: the float32 input path reads each row's {self.cols} "
                "cols whole; it takes no per-call bound on them"
            )
        if self.rows % self.cores:
            raise ValueError(
                f"Softmax: rows ({self.rows}) must be a multiple of the {self.cores} cores"
            )
        if self.block % _VECTOR_STEP or self.cols % self.block:
            raise ValueError(
                f"Softmax: block ({self.block}) must be a multiple of {_VECTOR_STEP} "
                f"dividing cols ({self.cols})"
            )
        if not self.streamed and self.block != self.cols:
            raise ValueError(
                f"Softmax: a row a core holds whole is one block: block ({self.block}) "
                f"must be cols ({self.cols}) unless streamed"
            )
        if self.streamed and self.rows // self.cores > _STREAMED_ROWS:
            raise ValueError(
                f"Softmax: a streamed core holds at most {_STREAMED_ROWS} rows, not "
                f"{self.rows // self.cores}"
            )

    def extent_unit(self, buffer: str) -> int:
        return 0  # no tiles-per-lane word: the sequence bounds the blocks itself

    class Array(Operator.Array):
        block: int
        num_aie_columns: int
        num_channels: int
        rows: int
        streamed: bool
        input_dtype: Any
        soft_cap: float | None
        has_addend: bool
        window: int | None
        period: int | None
        blocks: Value
        valid_cols: Value
        x: Operand
        addend: Operand | None
        y: Operand

        def build(self) -> Built:
            n_cores = self.num_aie_columns * self.num_channels
            rows_per_core = self.rows // n_cores
            block = self.block
            if np.dtype(self.input_dtype) == np.dtype(np.float32):
                if self.window is not None:
                    return self._build_f32_banded(n_cores, rows_per_core, block)
                return self._build_f32(n_cores, rows_per_core, block)
            tile_ty = self.x.obj_type
            softmax_k = _kernel(self, block)
            # The blocked passes and mask_bf16 are exported by the same softmax.cc.
            obj = softmax_k.object_file
            mask_k = obj.bind("mask_bf16", [tile_ty, np.int32, np.int32])
            zero_k = zero(block, ml_dtypes.bfloat16)
            state_ty = np.ndarray[(_STATE,), np.dtype[np.float32]]
            of_ins = [ObjectFifo(tile_ty) for k in range(n_cores)]
            of_outs = [ObjectFifo(tile_ty) for k in range(n_cores)]
            counts = (
                [self.valid_cols, self.blocks] if self.streamed else [self.valid_cols]
            )
            rtps = [Rtp(counts) for _ in range(n_cores)]

            def whole(of_in, of_out, softmax, mask, zero, rtp):
                valid = rtp.read()[self.valid_cols]
                span = arith.minsi(
                    (valid + (_VECTOR_STEP - 1)) & -_VECTOR_STEP,
                    arith.constant(block, valid.type),
                )
                for _ in range_(rows_per_core):
                    elem_in = of_in.acquire(1)
                    elem_out = of_out.acquire(1)
                    zero(elem_out)
                    mask(elem_in, valid, span)
                    softmax(elem_in, elem_out, span)
                    of_in.release(1)
                    of_out.release(1)

            def streamed(
                of_in, of_out, row_max, row_sum, row_scale, mask, zero, rtp, *states
            ):
                # Blocks arrive across the core's rows: each row carries its own state.
                words = rtp.read()
                valid, blocks = words[self.valid_cols], words[self.blocks]
                i32 = valid.type
                for step in range(3):
                    for b in range_(blocks):
                        b32 = arith.index_cast(b, to=i32)
                        in_block = arith.minsi(
                            valid - b32 * block, arith.constant(block, i32)
                        )
                        span = arith.minsi(
                            (in_block + (_VECTOR_STEP - 1)) & -_VECTOR_STEP,
                            arith.constant(block, i32),
                        )
                        for state in states:
                            elem_in = of_in.acquire(1)
                            mask(elem_in, in_block, span)
                            if step == 0:
                                row_max(
                                    elem_in, state, arith.extui(i32, b32 == 0), span
                                )
                            elif step == 1:
                                row_sum(elem_in, state, span)
                            else:
                                elem_out = of_out.acquire(1)
                                zero(elem_out)
                                row_scale(elem_in, elem_out, state, span)
                                of_out.release(1)
                            of_in.release(1)

            if self.streamed:
                kernels = [
                    obj.bind(
                        "softmax_max_bf16", [tile_ty, state_ty, np.int32, np.int32]
                    ),
                    obj.bind("softmax_sum_bf16", [tile_ty, state_ty, np.int32]),
                    obj.bind(
                        "softmax_scale_bf16", [tile_ty, tile_ty, state_ty, np.int32]
                    ),
                ]
                workers = [
                    Worker(
                        streamed,
                        [of_ins[k].cons(), of_outs[k].prod(), *kernels, mask_k, zero_k]
                        + [rtps[k]]
                        + [Buffer(state_ty) for r in range(rows_per_core)],
                    )
                    for k in range(n_cores)
                ]
            else:
                workers = [
                    Worker(
                        whole,
                        [
                            of_ins[k].cons(),
                            of_outs[k].prod(),
                            softmax_k,
                            mask_k,
                            zero_k,
                            rtps[k],
                        ],
                    )
                    for k in range(n_cores)
                ]
            self.x.bind([f.prod() for f in of_ins])
            self.y.bind([f.cons() for f in of_outs])
            return Built(workers, rtps)

        def _build_f32(self, n_cores: int, rows_per_core: int, block: int) -> Built:
            """The float32 input path: a row held whole, one call to
            ``softmax_f32_bf16`` a row, its ``n`` bound to ``block`` at build time.
            """
            softmax_k = _kernel(self, block)
            of_ins = [ObjectFifo(self.x.obj_type) for _ in range(n_cores)]
            of_outs = [ObjectFifo(self.y.obj_type) for _ in range(n_cores)]
            of_addends = (
                [ObjectFifo(self.addend.obj_type) for _ in range(n_cores)]
                if self.has_addend
                else None
            )

            def whole(of_in, of_out, softmax, *rest):
                of_addend = rest[0] if self.has_addend else None
                for _ in range_(rows_per_core):
                    elem_in = of_in.acquire(1)
                    args = [elem_in]
                    if of_addend is not None:
                        args.append(of_addend.acquire(1))
                    elem_out = of_out.acquire(1)
                    softmax(*args, elem_out, block)
                    of_in.release(1)
                    if of_addend is not None:
                        of_addend.release(1)
                    of_out.release(1)

            workers = [
                Worker(
                    whole,
                    [of_ins[k].cons(), of_outs[k].prod(), softmax_k]
                    + ([of_addends[k].cons()] if of_addends else []),
                )
                for k in range(n_cores)
            ]
            self.x.bind([f.prod() for f in of_ins])
            self.y.bind([f.cons() for f in of_outs])
            if of_addends is not None:
                self.addend.bind([f.prod() for f in of_addends])
            return Built(workers)

        def _build_f32_banded(
            self, n_cores: int, rows_per_core: int, block: int
        ) -> Built:
            """The float32 banded path: one row a call, a real device loop (its
            row count does not grow the core's code, unlike a resident mask's
            row-by-row ``Buffer``s would), to ``softmax_rows_banded_f32_bf16``.
            The band comes from ``window``, ``period`` and the row's own
            position (the core's ``row_offset`` plus the loop index) computed
            in the kernel, so there is no mask operand.
            """
            banded_k = _kernel(self, block)
            of_ins = [ObjectFifo(self.x.obj_type) for _ in range(n_cores)]
            of_addends = [ObjectFifo(self.addend.obj_type) for _ in range(n_cores)]
            of_outs = [ObjectFifo(self.y.obj_type) for _ in range(n_cores)]

            def _whole(core_offset):
                def whole(of_in, of_addend, of_out, fn):
                    for r in range_(rows_per_core):
                        elem_in = of_in.acquire(1)
                        elem_addend = of_addend.acquire(1)
                        elem_out = of_out.acquire(1)
                        i32 = np_dtype_to_mlir_type(np.int32)
                        r32 = arith.index_cast(r, to=i32)
                        row_offset = arith.addi(r32, arith.constant(core_offset, i32))
                        fn(
                            elem_in,
                            elem_addend,
                            elem_out,
                            1,
                            block,
                            self.window,
                            self.period,
                            row_offset,
                        )
                        of_in.release(1)
                        of_addend.release(1)
                        of_out.release(1)

                return whole

            workers = [
                Worker(
                    _whole(k * rows_per_core),
                    [
                        of_ins[k].cons(),
                        of_addends[k].cons(),
                        of_outs[k].prod(),
                        banded_k,
                    ],
                )
                for k in range(n_cores)
            ]
            self.x.bind([f.prod() for f in of_ins])
            self.addend.bind([f.prod() for f in of_addends])
            self.y.bind([f.cons() for f in of_outs])
            return Built(workers)

    def sequence(self, rt):
        """Each lane's rows as ``(block, row, element)``, thrice if streamed."""
        lanes = self.cores
        rows = self.rows // lanes
        blocks = ceildiv(self.length, self.block)
        bounded = self.streamed and self.blocks.per_call
        blocks_valid = self.blocks if bounded else None
        full = TensorAccessPattern.full((self.rows, self.cols))
        taps = [
            full[k * rows : (k + 1) * rows, : blocks * self.block]
            .split(1, self.block)
            .permute((1, 0, 2))
            for k in range(lanes)
        ]
        reads = 3 if self.streamed else 1
        tg = TaskGroup()
        for k, tap in enumerate(taps):
            self.x.fill(
                tap.repeat(reads),
                lane=k,
                group=tg,
                length_parameter=blocks_valid,
                length_unit=rows * self.block,
            )
        if self.has_addend:
            for k, tap in enumerate(taps):
                self.addend.fill(
                    tap.repeat(1),
                    lane=k,
                    group=tg,
                    length_parameter=blocks_valid,
                    length_unit=rows * self.block,
                )
        for k, tap in enumerate(taps):
            self.y.drain(
                tap.repeat(1),
                lane=k,
                group=tg,
                wait=True,
                length_parameter=blocks_valid,
                length_unit=rows * self.block,
            )
        tg.finish()

    def tolerance(self) -> Tolerance | None:
        base = _kernel(self, self.cols).contract.tolerance
        if self.window is not None:
            # judge() calls bound() with this operator's own operands (x,
            # addend): row_offset is not one, so every row's own query
            # position (its index) is closed over instead of taken
            # positionally.
            row_offset = np.arange(self.rows)
            return Tolerance.bounded(
                lambda x, addend: base.bound(x, addend, row_offset),
                max_mismatch_frac=base.max_mismatch_frac,
                note=base.note,
            )
        return base

    def reference(self, x, *rest):
        """The softmax kernel's contract reference, a row at a time.

        ``rest`` is ``addend`` where ``has_addend``: ``_call_reference``
        gives only the operands present, positional. The band, where given,
        comes from the factory's own banded contract, ``row_offset`` each
        row's own index.
        """
        addend = rest[0] if self.has_addend else None
        # A bounded call's first ``length`` columns, the rest left zero.
        n = self.length
        x = x[..., :n]
        addend = None if addend is None else addend[..., :n]
        if self.window is not None:
            y = _kernel(self, n).contract.reference(x, addend, np.arange(self.rows))
        else:
            y = activation.softmax_ref(
                x, addend, None, tile_size=n, soft_cap=self.soft_cap
            )
        if n == self.cols:
            return y
        out = np.zeros((*np.shape(y)[:-1], self.cols), np.asarray(y).dtype)
        out[..., :n] = y
        return out
