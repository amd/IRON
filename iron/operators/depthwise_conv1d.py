# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses

import numpy as np
from aie.extras.dialects import arith
from aie.iron import Buffer, ObjectFifo, TaskGroup, Worker, WorkerRuntimeBarrier
from aie.iron.controlflow import range_
from aie.iron.kernels import conv
from ml_dtypes import bfloat16

from iron.common import In, Operator, Out, Value, auto, param
from iron.common.testing import Case, Testing

TAPS = 5


class DepthwiseConv1d(Operator):
    """A causal depthwise convolution over time, five taps, channels last.

    ``y[t, c] = sum_j weight[j, c] * x[t + j - 4, c]``, with the rows before
    the first zero. One core per column takes a contiguous run of rows; its
    input fifo is the sliding window (``dwconv1d_channels_last`` takes the
    five taps oldest first), and every run but the first is filled from four
    rows before it, so the cores need nothing from each other. The first
    core reads a zero plane for the taps before row 0.
    """

    test = Testing(
        [
            dict(rows=64, channels=64, num_aie_columns=1),
            dict(rows=64, channels=256, num_aie_columns=2),
            dict(rows=32, channels=96, num_aie_columns=8),
            # Benched: the audio tower's light conv at its longest bucket.
            Case(dict(rows=768, channels=1024, num_aie_columns=8), bench=True),
        ],
        draw=dict(centered=("x", "weight")),
    )

    rows: int = param()
    channels: int = param(array=True)
    num_aie_columns: int = auto()

    x = In(rows, channels, tile=(channels,), per=(num_aie_columns,), depth=TAPS + 1)
    weight = In(TAPS, channels, tile=(channels,), broadcast=True, depth=TAPS)
    y = Out(rows, channels, tile=(channels,), per=(num_aie_columns,))
    steps = Value(np.int32, derive=lambda op: op.rows // op.num_aie_columns)

    def validate(self) -> None:
        if self.channels % 32:
            raise ValueError(
                f"DepthwiseConv1d: channels ({self.channels}) is not a whole "
                f"number of 32-lane vectors"
            )

    def resolve(self, dev):
        """Columns default to the most the shim budget allows that leave
        every core a whole run of at least the window's rows.
        """
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            fits=lambda c: self.rows % c == 0 and self.rows // c >= TAPS - 1,
        )
        return dataclasses.replace(self, num_aie_columns=cols)

    def compatible(self) -> None:
        cols = self.num_aie_columns
        if self.rows % cols or self.rows // cols < TAPS - 1:
            raise ValueError(
                f"DepthwiseConv1d: rows ({self.rows}) must split into "
                f"{cols} runs of at least {TAPS - 1} rows"
            )

    def kernel(self):
        return conv.dwconv1d_channels_last(self.channels, clamp=False)

    def tolerance(self):
        return self.kernel().contract.tolerance

    def ops(self) -> int:
        return 2 * TAPS * self.rows * self.channels

    def reference(self, x, weight):
        padded = np.concatenate(
            [np.zeros((TAPS - 1, self.channels), np.float32), x.astype(np.float32)]
        )
        w = weight.astype(np.float32)
        y = sum(w[j] * padded[j : j + self.rows] for j in range(TAPS))
        return y.astype(bfloat16)

    def array(self, target) -> list:
        cols, C = self.num_aie_columns, self.channels
        plane = self.x.tile
        kernel = self.kernel()
        of_ins = [
            ObjectFifo(plane, name=f"in_{k}", depth=TAPS + 1) for k in range(cols)
        ]
        of_outs = [ObjectFifo(plane, name=f"out_{k}") for k in range(cols)]
        of_w = ObjectFifo(plane, name="weight", depth=TAPS)
        zero = Buffer(plane, initial_value=np.zeros(C, bfloat16), name="zero")
        limit = np.ndarray[(1,), np.dtype[np.float32]]
        rtps = [
            Buffer(
                np.ndarray[(1,), np.dtype[np.int32]],
                name=f"rtp_{k}",
                use_write_rtp=True,
            )
            for k in range(cols)
        ]
        barriers = [WorkerRuntimeBarrier() for _ in range(cols)]

        def core_fn(of_in, of_w, of_out, conv_fn, zero, lo, hi, rtp, barrier):
            barrier.wait_for_value(1)
            n = rtp[0]
            w = of_w.acquire(TAPS)
            taps = [w[j] for j in range(TAPS)]
            if zero is not None:
                # The rows before the first are zeros: a window that grows to five.
                for held in range(1, TAPS):
                    got = of_in.acquire(held)
                    window = [got] if held == 1 else [got[j] for j in range(held)]
                    y = of_out.acquire(1)
                    conv_fn(*taps, *[zero] * (TAPS - held), *window, y, lo, hi)
                    of_out.release(1)
                n = arith.subi(n, arith.constant(TAPS - 1, n.type))
            for _ in range_(n):
                window = of_in.acquire(TAPS)
                y = of_out.acquire(1)
                conv_fn(*taps, *[window[j] for j in range(TAPS)], y, lo, hi)
                of_in.release(1)
                of_out.release(1)
            of_in.release(TAPS - 1)
            of_w.release(TAPS)

        workers = [
            Worker(
                core_fn,
                [
                    of_ins[k].cons(),
                    of_w.cons(),
                    of_outs[k].prod(),
                    kernel,
                    zero if k == 0 else None,
                    Buffer(
                        limit, initial_value=np.zeros(1, np.float32), name=f"lo_{k}"
                    ),
                    Buffer(
                        limit, initial_value=np.zeros(1, np.float32), name=f"hi_{k}"
                    ),
                    rtps[k],
                    barriers[k],
                ],
            )
            for k in range(cols)
        ]
        for k in range(cols):
            self.x.lane(k).bind(of_ins[k].prod())
            self.y.lane(k).bind(of_outs[k].cons())
        self.weight.lane(0).bind(of_w.prod())
        self.steps.bind(rtps, 0)
        return workers + barriers

    def sequence(self, rt):
        """The weights once to every core, then each core's run of rows, the
        four before it with it but for the first.
        """
        run = self.rows // self.num_aie_columns
        weights = TaskGroup()
        rt.fill(self.weight.lane(0), self.weight, group=weights)
        tg = TaskGroup()
        for k in range(self.num_aie_columns):
            start = max(0, k * run - (TAPS - 1))
            rt.fill(self.x.lane(k), self.x[start : (k + 1) * run], group=tg)
        for k in range(self.num_aie_columns):
            rt.drain(
                self.y.lane(k), self.y[k * run : (k + 1) * run], group=tg, wait=True
            )
        tg.finish()
        weights.finish()
