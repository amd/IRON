# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import numpy as np
from aie.extras.dialects import arith
from aie.iron import Buffer, In, Out, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import conv
from aie.utils.compile.jit.params import param, per_call, tunable, widths
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp
from iron.common.testing import Case, Testing

TAPS = 5


class DepthwiseConv1d(Operator):
    """A causal depthwise convolution over time, five taps, channels last: one
    core per column takes a run of rows, its input fifo the sliding window;
    every run but the first is filled from four rows before it.
    """

    test = Testing(
        [
            Case(dict(rows=64, channels=64, num_aie_columns=1)),
            Case(dict(rows=64, channels=256, num_aie_columns=2)),
            Case(dict(rows=32, channels=96, num_aie_columns=8)),
            # Benched: the audio tower's light conv at its longest bucket.
            Case(dict(rows=768, channels=1024, num_aie_columns=8), bench=True),
        ],
        draw=lambda op: dict(centered=(op.x, op.weight)),
    )

    rows: int = param()
    channels: int = param()
    num_aie_columns: int = tunable(domain=widths)

    x = In(
        rows, channels, obj_shape=(channels,), per=(num_aie_columns,), depth=TAPS + 1
    )
    weight = In(TAPS, channels, obj_shape=(channels,), depth=TAPS)
    y = Out(rows, channels, obj_shape=(channels,), per=(num_aie_columns,))
    # Every row is still computed under a bound: a row reads only those before it.
    valid = per_call(bounds=rows)
    steps = per_call(derive=lambda op: op.rows // op.num_aie_columns)

    def validate(self) -> None:
        if self.channels % 32:
            raise ValueError(
                f"DepthwiseConv1d: channels ({self.channels}) is not a whole "
                f"number of 32-lane vectors"
            )

    def resolve(self, dev):
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            fits=lambda c: self.rows % c == 0 and self.rows // c >= TAPS - 1,
        )
        return self.replace(num_aie_columns=cols)

    def compatible(self) -> None:
        cols = self.num_aie_columns
        if self.rows % cols or self.rows // cols < TAPS - 1:
            raise ValueError(
                f"DepthwiseConv1d: rows ({self.rows}) must split into "
                f"{cols} runs of at least {TAPS - 1} rows"
            )

    def kernel(self):
        return conv.dwconv1d_channels_last(self.channels, clamp=False)

    def build(self) -> Built:
        cols, C = self.num_aie_columns, self.channels
        plane = self.x.obj_type
        kernel = self.kernel()
        x_ends = self.x.fifos(self.x.depth)
        y_ends = self.y.fifos(self.y.depth)
        # One fifo, each column taking its own cons(): every core reads the
        # same weights.
        (w_ends,) = self.weight.fifos(self.weight.depth, readers=cols)
        zero = Buffer(plane, initial_value=np.zeros(C, bfloat16))
        limit = np.ndarray[(1,), np.dtype[np.float32]]
        rtps = [Rtp([self.steps]) for _ in range(cols)]

        def core_fn(of_in, of_w, of_out, conv_fn, zero, lo, hi, rtp):
            n = rtp.read()[self.steps]
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
                    x_ends[k],
                    w_ends[k],
                    y_ends[k],
                    kernel,
                    zero if k == 0 else None,
                    Buffer(limit, initial_value=np.zeros(1, np.float32)),
                    Buffer(limit, initial_value=np.zeros(1, np.float32)),
                    rtps[k],
                ],
            )
            for k in range(cols)
        ]
        return Built(workers, rtps)

    def tolerance(self):
        return self.layout().kernel().contract.tolerance

    def ops(self) -> int:
        return 2 * TAPS * self.rows * self.channels

    def reference(self, x, weight):
        padded = np.concatenate(
            [np.zeros((TAPS - 1, self.channels), np.float32), x.astype(np.float32)]
        )
        w = weight.astype(np.float32)
        y = sum(w[j] * padded[j : j + self.rows] for j in range(TAPS))
        return y.astype(bfloat16)

    def sequence(self, rt):
        """The weights to every core, then each run with the four rows before it."""
        run = self.rows // self.num_aie_columns
        weights = rt.task_group()
        self.weight.fill(group=weights)
        tg = rt.task_group()
        for k in range(self.num_aie_columns):
            start = max(0, k * run - (TAPS - 1))
            self.x.fill(self.x[start : (k + 1) * run], lane=k, group=tg)
        for k in range(self.num_aie_columns):
            self.y.drain(self.y[k * run : (k + 1) * run], lane=k, group=tg, wait=True)
        rt.finish(tg)
        rt.finish(weights)
