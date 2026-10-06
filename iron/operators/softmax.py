# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import dataclasses

import ml_dtypes
import numpy as np
from aie.extras.dialects import arith
from aie.iron import Buffer, ObjectFifo, Worker, WorkerRuntimeBarrier
from aie.iron.controlflow import range_
from aie.iron.kernels import activation, zero
from aie.utils.verify import Tolerance

from iron.common import Extent, In, Incompatible, Operator, Out, Value, auto, param
from iron.common.testing import Case, Testing

# softmax_bf16's vector step on both targets (activation.softmax holds a row
# to a multiple of it). Its loops cover only whole steps.
_VECTOR_STEP = 32


class Softmax(Operator):
    """AIE-accelerated Softmax operation: one core per (column, channel), one
    row per tile.

    Each row is masked to ``vector_size`` valid elements before the softmax:
    the whole row, unless a graph binds a per-call value to it (``Softmax(x,
    vector_size=n)``, attention over a context that grows each call), which
    the core then reads per call. ``vector_size`` must be at least 1.

    The kernels only run over the span: ``vector_size`` rounded up to the
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
            # Benched: 2 Mi elements, well past the dispatch cost.
            Case(
                dict(rows=4096, cols=512, num_aie_columns=2, num_channels=2),
                bench=True,
            ),
        ]
    )

    rows: int = param()
    cols: int = param()
    # None: every column the device's shim budget allows.
    num_aie_columns: int = auto()
    num_channels: int = auto(1)

    valid = Extent(rows)  # rows, or fewer per call

    x = In(rows, cols, tile=(cols,), per=(num_aie_columns, num_channels))
    y = Out(rows, cols, tile=(cols,), per=(num_aie_columns, num_channels))
    count = Value(np.int32, derive=lambda op: op.valid // op.cores)  # rows per core
    vector_size = Value(np.int32, derive=lambda op: op.cols)  # valid elements per row

    def validate(self) -> None:
        if self.rows % 16 != 0:
            raise ValueError(f"rows ({self.rows}) must be a multiple of 16")
        if self.cols % 16 != 0:
            raise ValueError(f"cols ({self.cols}) must be a multiple of 16")

    def resolve(self, dev):
        """Columns default to the most the device's shim budget allows that
        leave every core a whole number of rows.
        """
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: self.rows % (c * self.num_channels) == 0,
        )
        return dataclasses.replace(self, num_aie_columns=cols)

    @property
    def cores(self) -> int:
        return self.num_aie_columns * self.num_channels

    def compatible(self) -> None:
        if self.rows % self.cores:
            raise Incompatible(
                f"rows ({self.rows}) must be a multiple of the {self.cores} cores"
            )

    def array(self, target) -> list:
        tile_ty = self.x.tile
        cols, chans = self.num_aie_columns, self.num_channels
        n_cores = cols * chans
        softmax_k = activation.softmax(self.cols)
        # mask_bf16 is exported by the same softmax.cc translation unit.
        mask_k = softmax_k.object_file.bind("mask_bf16", [tile_ty, np.int32, np.int32])
        zero_k = zero(self.cols, ml_dtypes.bfloat16)
        of_ins = [
            ObjectFifo(tile_ty, name=f"in1_{i}_{j}")
            for i in range(cols)
            for j in range(chans)
        ]
        of_outs = [
            ObjectFifo(tile_ty, name=f"out_{i}_{j}")
            for i in range(cols)
            for j in range(chans)
        ]
        # [count, vector_size] per core in an RTP, less whichever is a
        # per-call value the core reads from the scratchpad instead (the
        # count when a graph bounds the rows, the mask length when it binds
        # it). On an image without a scratchpad the sequence writes the
        # per-call values into the RTP.
        elf = target.image == "elf"
        dyn_count = self.uses_value("count") and elf
        dyn_vs = self.uses_value("vector_size") and elf
        static = [
            n for n, d in (("count", dyn_count), ("vector_size", dyn_vs)) if not d
        ]
        rtp_ty = np.ndarray[(max(1, len(static)),), np.dtype[np.int32]]
        rtps = [
            Buffer(rtp_ty, name=f"rtp_{k}", use_write_rtp=True) for k in range(n_cores)
        ]
        barriers = [WorkerRuntimeBarrier() for _ in range(n_cores)]
        per_tile = self.cols
        params = [
            p
            for p, d in (
                (self.count.param, dyn_count),
                (self.vector_size.param, dyn_vs),
            )
            if d
        ]

        def core_body(
            of_in,
            of_out,
            softmax_kernel,
            mask_kernel,
            zero_kernel,
            rtp,
            barrier,
            *words,
        ):
            barrier.wait_for_value(1)
            # dyn_count/dyn_vs are compile-time constants, so each value is
            # emitted once: a scratchpad parameter read or an RTP load.
            words = list(words)
            n = words.pop(0).read() if dyn_count else rtp[static.index("count")]
            vector_size = (
                words.pop(0).read() if dyn_vs else rtp[static.index("vector_size")]
            )
            i32 = vector_size.type
            span = arith.minsi(
                arith.andi(
                    arith.addi(vector_size, arith.constant(_VECTOR_STEP - 1, i32)),
                    arith.constant(-_VECTOR_STEP, i32),
                ),
                arith.constant(per_tile, i32),
            )
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                zero_kernel(elem_out)
                mask_kernel(elem_in, vector_size, span)
                softmax_kernel(elem_in, elem_out, span)
                of_in.release(1)
                of_out.release(1)

        workers = [
            Worker(
                core_body,
                [
                    of_ins[k].cons(),
                    of_outs[k].prod(),
                    softmax_k,
                    mask_k,
                    zero_k,
                    rtps[k],
                    barriers[k],
                ]
                + params,
            )
            for k in range(n_cores)
        ]
        for k in range(n_cores):
            self.x.lane(k).bind(of_ins[k].prod())
            self.y.lane(k).bind(of_outs[k].cons())
        if not dyn_count:
            self.count.bind(rtps, static.index("count"))
        if not dyn_vs:
            self.vector_size.bind(rtps, static.index("vector_size"))
        return workers + barriers

    def tolerance(self) -> Tolerance | None:
        return activation.softmax(self.cols).contract.tolerance

    def reference(self, x, vector_size=None):
        """The softmax kernel's contract reference, a row per call, after the
        mask: ``mask_bf16`` fills ``[vector_size, cols)`` with the lowest bf16,
        so the masked tail comes out as exact zeros. Without a per-call value
        the whole row is valid.
        """
        x = x.reshape(self.rows, self.cols, copy=False)
        if vector_size is not None and int(vector_size) < self.cols:
            x = x.copy()
            x[:, int(vector_size) :] = ml_dtypes.finfo(x.dtype).min
        return activation.softmax(self.cols).contract.reference(x)
