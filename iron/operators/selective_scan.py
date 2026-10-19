# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SelectiveScan: Mamba2's state space recurrence over a run of rows."""

import dataclasses

import numpy as np
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Buffer,
    CompileTime,
    In,
    ObjectFifo,
    Out,
    TaskGroup,
    Worker,
    kernels,
)
from aie.iron.controlflow import range_
from ml_dtypes import bfloat16

from iron.common import Auto, Built, Extent, Operator, Rtp, Unresolvable, Value, field
from iron.common.testing import Case, Testing

#: The rows of a head's state a kernel call carries.
SLICE = 16


def _trained(op: "SelectiveScan") -> dict:
    """Heads as a trained Mamba2's are: ``A < 0``, so the state decays."""
    rng = np.random.default_rng(3)
    H = op.heads
    head = np.stack(
        [rng.uniform(-4, 0, H), -rng.uniform(0.5, 16, H), rng.uniform(0, 2, H)], 1
    )
    xbc = rng.standard_normal((op.rows, op.width)) * 0.5
    return dict(
        given={op.xbc: xbc.astype(bfloat16), op.head: head.astype(np.float32)},
        normal=(op.dt, op.state),
    )


class SelectiveScan(Operator):
    """Each row ``t`` of ``xbc``, split into ``x`` ``(heads, head_dim)``
    and ``groups`` rows each of ``B`` and ``C`` ``(state_size,)``, updates
    each head's state ``(head_dim, state_size)`` and reads it out:

        dt = softplus(dt[t] + dt_bias)
        state = exp(dt * A) * state + dt * outer(x, B)
        y[t] = state @ C + D * x

    head ``h`` reading group ``h // (heads // groups)``'s ``B`` and ``C``
    and its ``(dt_bias, A, D)`` from ``head``. ``state`` is the state
    before the first row; ``final`` the state after the last valid one.
    Float32 throughout, ``y`` rounded once.

    Each of ``columns`` cores takes whole heads, ``SLICE`` rows of a head's
    state at a time, and gathers each row's ``x``, ``B`` and ``C`` for the
    slice from the whole row of ``xbc``. Scalar.
    """

    test = Testing(
        [
            Case(dict(rows=4, heads=2, head_dim=16, state_size=16, columns=1)),
            Case(dict(rows=8, heads=4, head_dim=32, state_size=32, groups=2)),
            Case(
                dict(rows=64, heads=16, head_dim=64, state_size=64, groups=2),
                bench=True,
            ),
        ],
        draw=_trained,
    )

    rows: CompileTime[int] = field()
    heads: CompileTime[int] = field()
    head_dim: CompileTime[int] = field()
    state_size: CompileTime[int] = field()
    groups: CompileTime[int] = field(default=1)
    columns: CompileTime[int] = Auto()
    inner: CompileTime[int] = field(
        derive=lambda op: op.heads * op.head_dim, repr=False
    )
    width: CompileTime[int] = field(
        derive=lambda op: op.inner + 2 * op.groups * op.state_size, repr=False
    )
    slice_state: CompileTime[int] = field(
        derive=lambda op: SLICE * op.state_size, repr=False
    )

    xbc = In(rows, width, obj_shape=(width,), per=(columns,))
    dt = In(rows, heads, obj_shape=(heads,), per=(columns,))
    head = In(heads, 3, dtype=np.float32, obj_shape=(3,), per=(columns,))
    state = In(
        heads,
        head_dim,
        state_size,
        dtype=np.float32,
        obj_shape=(slice_state,),
        per=(columns,),
        depth=1,
    )
    y = Out(rows, inner, obj_shape=(SLICE,), per=(columns,))
    final = Out(
        heads,
        head_dim,
        state_size,
        dtype=np.float32,
        obj_shape=(slice_state,),
        per=(columns,),
        depth=1,
    )
    valid = Extent(rows)
    count = Value(derive=lambda op: op.valid)

    def validate(self) -> None:
        if self.head_dim % SLICE or self.heads % self.groups:
            raise ValueError(
                f"SelectiveScan: head_dim ({self.head_dim}) must be whole "
                f"{SLICE}-row slices and heads ({self.heads}) whole groups "
                f"({self.groups})"
            )

    def resolve(self, dev):
        columns = self.columns or max(
            c for c in range(1, dev.cols + 1) if self.heads % c == 0
        )
        if self.heads % columns or columns > dev.cols:
            raise Unresolvable(
                f"SelectiveScan: {self.heads} heads over {columns} cores, on a "
                f"device of {dev.cols} columns"
            )
        return dataclasses.replace(self, columns=columns)

    @property
    def slices(self) -> int:
        """A core's slices: its heads' ``SLICE``-row runs of state."""
        return self.heads // self.columns * self.head_dim // SLICE

    class Array(Operator.Array):
        def kernel(self):
            return kernels.ssm.selective_scan(
                rows=1, head_dim=SLICE, state=self.state_size
            )

        def build(self) -> Built:
            P, N, I = self.head_dim, self.state_size, self.inner
            per_group = self.heads // self.groups
            per_head = P // SLICE
            kernel = self.kernel()
            operands = (self.xbc, self.dt, self.head, self.state)
            outputs = (self.y, self.final)
            fifos = [
                [ObjectFifo(o.obj_type, depth=o.depth) for _ in range(self.columns)]
                for o in (*operands, *outputs)
            ]
            rtps = [Rtp([self.count]) for _ in range(self.columns)]
            row_ty = np.ndarray[(SLICE + 2 * N,), np.dtype[bfloat16]]
            dt_ty = np.ndarray[(1,), np.dtype[bfloat16]]

            def core_fn(of_xbc, of_dt, of_head, of_state, of_y, of_final, *rest):
                scan, x, dt, rtp, first = rest
                valid = rtp.read()[self.count]
                i32 = valid.type
                for u in range_(self.slices):
                    h = u // per_head + first
                    p = (u % per_head) * SLICE + h * P
                    b = (h // per_group) * N + I
                    c = b + self.groups * N
                    params = of_head.acquire(1)
                    given, state = of_state.acquire(1), of_final.acquire(1)
                    for i in range_(SLICE * N):
                        state[i] = given[i]
                    of_state.release(1)
                    for t in range_(self.rows):
                        row, step, y = (
                            of_xbc.acquire(1),
                            of_dt.acquire(1),
                            of_y.acquire(1),
                        )
                        for i in range_(SLICE):
                            x[i] = row[p + i]
                        for n in range_(N):
                            x[SLICE + n] = row[b + n]
                            x[SLICE + N + n] = row[c + n]
                        dt[0] = step[h]
                        left = valid - arith.index_cast(t, to=i32)
                        live = arith.minsi(
                            arith.maxsi(left, arith.constant(0, i32)),
                            arith.constant(1, i32),
                        )
                        scan(x, dt, params, state, y, live)
                        of_xbc.release(1)
                        of_dt.release(1)
                        of_y.release(1)
                    of_final.release(1)
                    of_head.release(1)

            heads = self.heads // self.columns
            workers = [
                Worker(
                    core_fn,
                    [
                        *(f[k].cons() for f in fifos[:4]),
                        *(f[k].prod() for f in fifos[4:]),
                        kernel,
                        Buffer(row_ty),
                        Buffer(dt_ty),
                        rtps[k],
                        k * heads,
                    ],
                )
                for k in range(self.columns)
            ]
            for o, f in zip(operands, fifos):
                o.bind([lane.prod() for lane in f])
            for o, f in zip(outputs, fifos[4:]):
                o.bind([lane.cons() for lane in f])
            return Built(workers, rtps)

    def sequence(self, rt):
        """Per core, every row of ``xbc`` and ``dt`` once a slice, its heads'
        parameters and states, and its slices of ``y`` and ``final``.
        """
        R, H, W, I = self.rows, self.heads, self.width, self.inner
        S, heads = self.slices, H // self.columns
        states = self.heads * self.head_dim * self.state_size
        run = S * SLICE * self.state_size
        tg = TaskGroup()
        for k in range(self.columns):
            self.xbc.fill(
                TensorAccessPattern((R, W), 0, [S, R, W], [0, W, 1]), lane=k, group=tg
            )
            self.dt.fill(
                TensorAccessPattern((R, H), 0, [S, R, H], [0, H, 1]), lane=k, group=tg
            )
            self.head.fill(
                TensorAccessPattern(
                    (H, 3), 3 * k * heads, [heads, S // heads, 3], [3, 0, 1]
                ),
                lane=k,
                group=tg,
            )
            self.state.fill(
                TensorAccessPattern((states,), k * run, [run], [1]), lane=k, group=tg
            )
        for k in range(self.columns):
            self.y.drain(
                TensorAccessPattern(
                    (R, I), k * S * SLICE, [S, R, SLICE], [SLICE, I, 1]
                ),
                lane=k,
                group=tg,
                wait=True,
            )
            self.final.drain(
                TensorAccessPattern((states,), k * run, [run], [1]),
                lane=k,
                group=tg,
                wait=True,
            )
        tg.finish()

    def tolerance(self):
        return self.array_config().kernel().contract.tolerance

    def reference(self, xbc, dt, head, state):
        H, P, N, G = self.heads, self.head_dim, self.state_size, self.groups
        xbc, dt = np.asarray(xbc, np.float32), np.asarray(dt, np.float32)
        dt_bias, A, D = np.asarray(head, np.float32).T
        state = np.array(state, np.float32)
        y = np.zeros((self.rows, self.inner), np.float32)
        for t in range(self.valid):
            x = xbc[t, : self.inner].reshape(H, P)
            B, C = (
                np.repeat(m.reshape(G, N), H // G, axis=0)
                for m in np.split(xbc[t, self.inner :], 2)
            )
            step = np.logaddexp(0, dt[t] + dt_bias)[:, None, None]
            state = np.exp(step * A[:, None, None]) * state
            state += step * x[:, :, None] * B[:, None, :]
            y[t] = (np.einsum("hpn,hn->hp", state, C) + D[:, None] * x).reshape(-1)
        return y.astype(bfloat16), state
