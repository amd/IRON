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
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Auto, Built, Extent, Operator, Rtp, Unresolvable, Value, field
from iron.common.testing import Case, Testing

#: The rows of a head's state a kernel call carries.
SLICE = 16


def _slices(op) -> int:
    """A core's slices: its heads' ``SLICE``-row runs of state."""
    return op.heads // op.columns * op.head_dim // SLICE


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
    slice from the whole row of ``xbc``, which a memtile joins to the row's
    ``dt``; another joins each slice's state to its head's ``head``, so a
    core reads two streams. Scalar.
    """

    test = Testing(
        [
            Case(dict(rows=5, heads=2, head_dim=16, state_size=16, columns=1)),
            Case(dict(rows=8, heads=4, head_dim=32, state_size=32, groups=2)),
            Case(
                dict(rows=64, heads=16, head_dim=64, state_size=64, groups=2),
                bench=True,
            ),
        ],
        draw=_trained,
    )

    rows: CompileTime[int] = field(array=True)
    heads: CompileTime[int] = field(array=True)
    head_dim: CompileTime[int] = field(array=True)
    state_size: CompileTime[int] = field(array=True)
    groups: CompileTime[int] = field(default=1, array=True)
    columns: CompileTime[int] = Auto()
    inner: CompileTime[int] = field(
        derive=lambda op: op.heads * op.head_dim, repr=False, array=True
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
        if self.head_dim % SLICE or self.heads % self.groups or self.heads % 2:
            raise ValueError(
                f"SelectiveScan: head_dim ({self.head_dim}) must be whole "
                f"{SLICE}-row slices, and heads ({self.heads}) whole groups "
                f"({self.groups}) and even, so a row's xbc after its dt is "
                "4-byte aligned"
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

    class Array(Operator.Array):
        def kernel(self):
            return kernels.ssm.selective_scan(
                rows=1, head_dim=SLICE, state=self.state_size
            )

        def build(self) -> Built:
            H, P, N, I = self.heads, self.head_dim, self.state_size, self.inner
            SN, per_group, per_head = SLICE * N, H // self.groups, P // SLICE
            kernel = self.kernel()
            f32 = lambda n: np.ndarray[(n,), np.dtype[np.float32]]
            bf16 = lambda n: np.ndarray[(n,), np.dtype[bfloat16]]
            # A core takes two streams, a memtile joining each: a row's dt
            # then its xbc, and a slice's (dt_bias, A, D) then its state.
            rows, starts, ends = [], [], ([], [], [], [])
            for _ in range(self.columns):
                row = ObjectFifo(bf16(H + self.width), depth=1)
                part = row.prod().join(
                    [0, H], obj_types=[self.dt.obj_type, self.xbc.obj_type]
                )
                start = ObjectFifo(f32(3 + SN), depth=1)
                part += start.prod().join(
                    [0, 3], obj_types=[self.head.obj_type, self.state.obj_type]
                )
                rows.append(row)
                starts.append(start)
                for lane, f in zip(ends, part):
                    lane.append(f.prod())
            for o, lane in zip((self.dt, self.xbc, self.head, self.state), ends):
                o.bind(lane)
            of_ys = [ObjectFifo(self.y.obj_type) for _ in range(self.columns)]
            of_finals = [
                ObjectFifo(self.final.obj_type, depth=1) for _ in range(self.columns)
            ]
            self.y.bind([f.cons() for f in of_ys])
            self.final.bind([f.cons() for f in of_finals])
            rtps = [Rtp([self.count]) for _ in range(self.columns)]

            def core_fn(of_row, of_slice, of_y, of_final, scan, *rest):
                x, bc, dt, head, a, b, rtp, first = rest
                valid = rtp.read()[self.count]
                i32 = valid.type
                zero, one = arith.constant(0, i32), arith.constant(1, i32)

                def call(t, state, final):
                    """Row ``t`` of the slice from ``state`` into ``final``."""
                    row, y = of_row.acquire(1), of_y.acquire(1)
                    dt[0] = row[h]
                    for i in range_(SLICE):
                        x[i] = row[H + p + i]
                    for n in range_(N):
                        bc[n] = row[H + g + n]
                        bc[N + n] = row[H + g + self.groups * N + n]
                    left = valid - arith.index_cast(t, to=i32)
                    live = arith.minsi(arith.maxsi(left, zero), one)
                    scan(x, bc, dt, head, state, final, y, live)
                    of_row.release(1)
                    of_y.release(1)

                for u in range_(_slices(self)):
                    h = u // per_head + first
                    p = (u % per_head) * SLICE + h * P
                    g = (h // per_group) * N + I
                    start = of_slice.acquire(1)
                    for i in range(3):
                        head[i] = start[i]
                    for i in range_(SN):
                        a[i] = start[3 + i]
                    of_slice.release(1)
                    # Each call's final the next one's state, two buffers in turn.
                    if self.rows > 1:
                        for t in range_(self.rows // 2):
                            call(2 * t, a, b)
                            call(2 * t + 1, b, a)
                    last = a
                    if self.rows % 2:
                        call(self.rows - 1, a, b)
                        last = b
                    final = of_final.acquire(1)
                    for i in range_(SN):
                        final[i] = last[i]
                    of_final.release(1)

            heads = H // self.columns
            workers = [
                Worker(
                    core_fn,
                    [
                        rows[k].cons(),
                        starts[k].cons(),
                        of_ys[k].prod(),
                        of_finals[k].prod(),
                        kernel,
                        Buffer(bf16(SLICE)),
                        Buffer(bf16(2 * N)),
                        Buffer(bf16(1)),
                        Buffer(f32(3)),
                        Buffer(f32(SN)),
                        Buffer(f32(SN)),
                        rtps[k],
                        k * heads,
                    ],
                )
                for k in range(self.columns)
            ]
            return Built(workers, rtps)

    def sequence(self, rt):
        """Per core, every row of ``xbc`` and ``dt`` once a slice, its heads'
        parameters and states, and its slices of ``y`` and ``final``.
        """
        R, H, W, I = self.rows, self.heads, self.width, self.inner
        S, heads = _slices(self), H // self.columns
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
        return Tolerance.relative(
            8e-3, range_frac=1e-3, note="f32 throughout, y rounded once: a bf16 ulp"
        )

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
