# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import dataclasses

import ml_dtypes
import numpy as np
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Buffer,
    ObjectFifo,
    TaskGroup,
    Worker,
    WorkerRuntimeBarrier,
    ceildiv,
)
from aie.iron.controlflow import range_
from aie.iron.kernels import activation, zero
from aie.utils.verify import Tolerance

from iron.common import (
    Choices,
    Divisors,
    Extent,
    In,
    Operator,
    Out,
    Value,
    auto,
    param,
)
from iron.common.testing import Case, Testing

# softmax_bf16's vector step on both targets (activation.softmax holds a row
# to a multiple of it). Its loops cover only whole steps.
_VECTOR_STEP = 32
# The longest row a core holds whole: its input and output, double-buffered.
_ROW_CAP = 4096
# A streamed row's block, read three times a call.
_BLOCK = 1024
# The floats a streamed row carries between blocks: the lanes' sums and the maximum.
_STATE = 64
# A streamed core unrolls its rows, each with its own state: 48 fit its
# program memory on AIE2P, 64 overflow it.
_STREAMED_ROWS = 48


class Softmax(Operator):
    """AIE-accelerated Softmax over each row: one core per (column, channel),
    each taking a contiguous run of rows.

    A graph may bound the rows' length per call, ``Softmax(x[:, :n])``
    (attention over a context that grows each call); the elements past
    ``n`` up to the end of its block come out as zeros, and ``n`` must be
    at least 1.

    A core holds a row whole, or, ``streamed``, reads it as ``block``-element
    blocks three times: for its maximum, for its lanes' sums of exponentials
    and for the output, the kernel's three passes split at block boundaries
    with every lane summing in the same order. A call bounded to ``n`` moves
    only the blocks ``n`` covers. Rows are streamed when a call bounds them
    or they are longer than a core holds.

    The kernels only run over the span: the valid elements rounded up to the
    softmax's 32-element vector step. Past it the masked elements' exponents
    are exact zeros, so leaving them out of the lanes' sums changes no bit;
    the output past the span is zero-filled instead of computed.
    """

    # Four cores, two columns of two: the fewest that exercise both splits.
    test = Testing(
        [
            dict(rows=32, cols=1024, num_aie_columns=2, num_channels=2),
            dict(rows=64, cols=512, num_aie_columns=2, num_channels=2),
            dict(rows=16, cols=2048, num_aie_columns=2, num_channels=2),
            dict(rows=16, cols=4096, block=1024, num_aie_columns=2, num_channels=2),
            dict(rows=16, cols=4608, num_aie_columns=2, num_channels=2),
            dict(rows=32, cols=32768, num_aie_columns=2, num_channels=2),
            # Benched: 2 Mi elements, well past the dispatch cost.
            Case(
                dict(rows=4096, cols=512, num_aie_columns=2, num_channels=2),
                bench=True,
            ),
        ]
    )

    rows: int = param(array=True)
    cols: int = param()
    # None: every column the device's shim budget allows.
    num_aie_columns: int = auto()
    num_channels: int = auto(1)
    # None: the whole row, or where the row is streamed the longest
    # multiple of _VECTOR_STEP up to _BLOCK that divides it.
    block: int = auto(
        domain=Divisors(of=lambda op: op.cols, step=_VECTOR_STEP, cap=_ROW_CAP)
    )
    streamed: bool = auto(array=True, domain=Choices((False, True)))

    length = Extent(cols)  # cols, or fewer per call

    x = In(rows, cols, tile=(block,), per=(num_aie_columns, num_channels))
    y = Out(rows, cols, tile=(block,), per=(num_aie_columns, num_channels))
    valid_cols = Value(np.int32, derive=lambda op: op.length)
    # A row held whole is one block, which the bound does not change.
    blocks = Value(
        np.int32,
        derive=lambda op: ceildiv(op.length, op.block) if op.streamed else 1,
        optional=True,
    )

    def validate(self) -> None:
        if self.rows % 16 != 0:
            raise ValueError(f"rows ({self.rows}) must be a multiple of 16")
        if self.cols % 16 != 0:
            raise ValueError(f"cols ({self.cols}) must be a multiple of 16")

    def resolve(self, dev):
        """Columns default to the most the device's shim budget allows that
        leave every core a whole number of rows. A row is streamed when it
        is longer than ``_ROW_CAP``, or when a call bounds it and a core's
        rows fit a streamed core (``_STREAMED_ROWS``).
        """
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: self.rows % (c * self.num_channels) == 0,
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
        if self.rows % self.cores:
            raise ValueError(
                f"rows ({self.rows}) must be a multiple of the {self.cores} cores"
            )
        if self.block % _VECTOR_STEP or self.cols % self.block:
            raise ValueError(
                f"block ({self.block}) must be a multiple of {_VECTOR_STEP} "
                f"dividing cols ({self.cols})"
            )
        if not self.streamed and self.block != self.cols:
            raise ValueError(
                f"a row a core holds whole is one block: block ({self.block}) "
                f"must be cols ({self.cols}) unless streamed"
            )
        if self.streamed and self.rows // self.cores > _STREAMED_ROWS:
            raise ValueError(
                f"a streamed core holds at most {_STREAMED_ROWS} rows, not "
                f"{self.rows // self.cores}"
            )

    def extent_unit(self, buffer: str) -> int:
        return 0  # no tiles-per-lane word: the sequence bounds the blocks itself

    def array(self, target) -> list:
        tile_ty = self.x.tile
        n_cores = self.cores
        rows_per_core = self.rows // n_cores
        block = self.block
        softmax_k = activation.softmax(block)
        # The blocked passes and mask_bf16 are exported by the same softmax.cc.
        obj = softmax_k.object_file
        mask_k = obj.bind("mask_bf16", [tile_ty, np.int32, np.int32])
        zero_k = zero(block, ml_dtypes.bfloat16)
        state_ty = np.ndarray[(_STATE,), np.dtype[np.float32]]
        of_ins = [ObjectFifo(tile_ty, name=f"in1_{k}") for k in range(n_cores)]
        of_outs = [ObjectFifo(tile_ty, name=f"out_{k}") for k in range(n_cores)]
        # A count a call sets is read from its scratchpad word on a full ELF;
        # else it is in the core's runtime-parameter buffer, which the sequence
        # writes. A core re-arms its barrier once it has read them: an xclbin's
        # cores outlive the call, and would else start the next on these counts.
        counts = ("valid_cols", "blocks") if self.streamed else ("valid_cols",)
        per_call = [n for n in counts if target.image == "elf" and self.uses_value(n)]
        static = [n for n in counts if n not in per_call]
        rtp_ty = np.ndarray[(max(1, len(static)),), np.dtype[np.int32]]
        rtps = [
            Buffer(rtp_ty, name=f"rtp_{k}", use_write_rtp=True) for k in range(n_cores)
        ]
        barriers = [WorkerRuntimeBarrier() for _ in range(n_cores)]
        params = [self.value(n).param for n in per_call]

        def read(rtp, words):
            return [
                (
                    words[per_call.index(n)].read()
                    if n in per_call
                    else rtp[static.index(n)]
                )
                for n in counts
            ]

        def whole(of_in, of_out, softmax, mask, zero, rtp, barrier, *words):
            barrier.wait_for_value(1)
            (valid,) = read(rtp, words)
            barrier.release_with_value(1)
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
            of_in, of_out, row_max, row_sum, row_scale, mask, zero, rtp, barrier, *rest
        ):
            # Blocks arrive block by block across the core's rows, so each
            # row carries its own state.
            words, states = rest[: len(per_call)], rest[len(per_call) :]
            barrier.wait_for_value(1)
            valid, blocks = read(rtp, words)
            barrier.release_with_value(1)
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
                            row_max(elem_in, state, arith.extui(i32, b32 == 0), span)
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
                obj.bind("softmax_max_bf16", [tile_ty, state_ty, np.int32, np.int32]),
                obj.bind("softmax_sum_bf16", [tile_ty, state_ty, np.int32]),
                obj.bind("softmax_scale_bf16", [tile_ty, tile_ty, state_ty, np.int32]),
            ]
            workers = [
                Worker(
                    streamed,
                    [of_ins[k].cons(), of_outs[k].prod(), *kernels, mask_k, zero_k]
                    + [rtps[k], barriers[k]]
                    + params
                    + [
                        Buffer(state_ty, name=f"state_{k}_{r}")
                        for r in range(rows_per_core)
                    ],
                )
                for k in range(n_cores)
            ]
        else:
            workers = [
                Worker(
                    whole,
                    [of_ins[k].cons(), of_outs[k].prod(), softmax_k, mask_k, zero_k]
                    + [rtps[k], barriers[k]]
                    + params,
                )
                for k in range(n_cores)
            ]
        for k in range(n_cores):
            self.x.lane(k).bind(of_ins[k].prod())
            self.y.lane(k).bind(of_outs[k].cons())
        for n in static:
            self.value(n).bind(rtps, static.index(n))
        return workers + barriers

    def sequence(self, rt):
        """Each lane's rows as ``(block, row, element)``: every block of the
        call's length, across the lane's rows, read three times if streamed.
        A bounded call patches the block count.
        """
        lanes = self.cores
        rows = self.rows // lanes
        blocks = ceildiv(self.length, self.block)
        bounded = self.streamed and self.uses_value("blocks")
        size_by = {1: self.value("blocks")} if bounded else None
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
            rt.fill(self.x.lane(k), tap.repeat(reads), group=tg, size_by=size_by)
        for k, tap in enumerate(taps):
            rt.drain(
                self.y.lane(k), tap.repeat(1), group=tg, wait=True, size_by=size_by
            )
        tg.finish()

    def tolerance(self) -> Tolerance | None:
        return activation.softmax(self.cols).contract.tolerance

    def reference(self, x):
        """The softmax kernel's contract reference, a row at a time. A
        graph's reference constructs a bounded call at its valid columns.
        """
        return activation.softmax_ref(x, tile_size=self.cols)
