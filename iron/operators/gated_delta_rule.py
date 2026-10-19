# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GatedDeltaRule: Gated DeltaNet's recurrence over a run of rows."""

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
from iron.operators.selective_scan import SLICE, _block


def _slices(op) -> int:
    """A core's slices: its value heads' ``SLICE``-column runs of state."""
    return op.v_heads // op.columns * op.value_dim // SLICE


def _trained(op: "GatedDeltaRule") -> dict:
    """Heads as a trained Gated DeltaNet's are: ``A < 0``, so the state
    decays; and one row's ``q`` near zero, where ``eps`` decides its norm.
    """
    rng = np.random.default_rng(3)
    V = op.v_heads
    head = np.stack([rng.uniform(-4, 0, V), -rng.uniform(0.5, 16, V)], 1)
    qkv = rng.standard_normal((op.rows, op.width))
    qkv[0, : op.key_dim] *= 1e-4
    return dict(
        given={op.qkv: qkv.astype(bfloat16), op.head: head.astype(np.float32)},
        normal=(op.a, op.b, op.state),
    )


class GatedDeltaRule(Operator):
    """Each row ``t`` of ``qkv``, split into ``q`` and ``k`` ``(k_heads,
    key_dim)`` and ``v`` ``(v_heads, value_dim)``, updates each value head's
    state ``(key_dim, value_dim)`` and reads it out:

        q, k = q / |q| / sqrt(key_dim), k / |k|
        g = A * softplus(a[t] + dt_bias), beta = sigmoid(b[t])
        state = exp(g) * state
        state += outer(k, beta * (v - k @ state))
        y[t] = q @ state

    value head ``h`` reading key head ``h // (v_heads // k_heads)``'s ``q``
    and ``k``, and its ``(dt_bias, A)`` from ``head``; ``|x|`` is
    ``sqrt(x @ x + 1e-6)``. ``state`` is the state before the first row;
    ``final`` the state after the last valid one. Float32 throughout, ``y``
    rounded once.

    Each of ``columns`` cores takes whole value heads, ``SLICE`` columns of
    a head's state at a time, and gathers a block of rows' ``q``, ``k``,
    ``v``, ``a`` and ``b`` for the slice from whole rows of ``qkv``, which
    a memtile joins to each row's ``a`` and ``b``; another joins each
    slice's state to its head's ``head``, so a core reads two streams. The
    kernel keeps the state from block to block. Scalar.
    """

    test = Testing(
        [
            Case(
                dict(rows=5, k_heads=1, v_heads=2, key_dim=16, value_dim=16, columns=1)
            ),
            Case(dict(rows=8, k_heads=2, v_heads=4, key_dim=32, value_dim=32)),
            Case(
                dict(rows=64, k_heads=8, v_heads=16, key_dim=64, value_dim=64),
                bench=True,
            ),
        ],
        draw=_trained,
    )

    rows: CompileTime[int] = field(array=True)
    k_heads: CompileTime[int] = field(array=True)
    v_heads: CompileTime[int] = field(array=True)
    key_dim: CompileTime[int] = field(array=True)
    value_dim: CompileTime[int] = field(array=True)
    columns: CompileTime[int] = Auto()
    width: CompileTime[int] = field(
        derive=lambda op: 2 * op.k_heads * op.key_dim + op.v_heads * op.value_dim,
        repr=False,
    )
    inner: CompileTime[int] = field(
        derive=lambda op: op.v_heads * op.value_dim, repr=False, array=True
    )
    block: CompileTime[int] = field(derive=lambda op: _block(op) * SLICE, repr=False)
    slice_state: CompileTime[int] = field(
        derive=lambda op: op.key_dim * SLICE, repr=False
    )

    qkv = In(rows, width, obj_shape=(width,), per=(columns,))
    a = In(rows, v_heads, obj_shape=(v_heads,), per=(columns,))
    b = In(rows, v_heads, obj_shape=(v_heads,), per=(columns,))
    head = In(v_heads, 2, dtype=np.float32, obj_shape=(2,), per=(columns,))
    state = In(
        v_heads,
        key_dim,
        value_dim,
        dtype=np.float32,
        obj_shape=(slice_state,),
        per=(columns,),
        depth=1,
    )
    y = Out(rows, inner, obj_shape=(block,), per=(columns,))
    final = Out(
        v_heads,
        key_dim,
        value_dim,
        dtype=np.float32,
        obj_shape=(slice_state,),
        per=(columns,),
        depth=1,
    )
    valid = Extent(rows)
    count = Value(derive=lambda op: op.valid)

    def validate(self) -> None:
        if self.value_dim % SLICE or self.v_heads % self.k_heads or self.v_heads % 2:
            raise ValueError(
                f"GatedDeltaRule: value_dim ({self.value_dim}) must be whole "
                f"{SLICE}-column slices, and v_heads ({self.v_heads}) whole "
                f"groups of k_heads ({self.k_heads}) and even, so a row's b "
                "after its a is 4-byte aligned"
            )

    def resolve(self, dev):
        columns = self.columns or max(
            c for c in range(1, dev.cols + 1) if self.v_heads % c == 0
        )
        if self.v_heads % columns or columns > dev.cols:
            raise Unresolvable(
                f"GatedDeltaRule: {self.v_heads} value heads over {columns} "
                f"cores, on a device of {dev.cols} columns"
            )
        return dataclasses.replace(self, columns=columns)

    class Array(Operator.Array):
        def kernel(self):
            return kernels.ssm.gated_delta_rule(
                rows=_block(self),
                key_dim=self.key_dim,
                value_dim=SLICE,
                blocks=self.rows // _block(self),
            )

        def build(self) -> Built:
            V, Dk, Dv, W = self.v_heads, self.key_dim, self.value_dim, self.width
            T, per_group, per_head = _block(self), V // self.k_heads, Dv // SLICE
            kernel = self.kernel()
            f32 = lambda n: np.ndarray[(n,), np.dtype[np.float32]]
            bf16 = lambda n: np.ndarray[(n,), np.dtype[bfloat16]]
            # A core takes two streams, a memtile joining each: a row's a
            # and b then its qkv, and a slice's (dt_bias, A) then its state.
            rows, starts, ends = [], [], ([], [], [], [], [])
            for _ in range(self.columns):
                row = ObjectFifo(bf16(2 * V + W), depth=1)
                part = row.prod().join(
                    [0, V, 2 * V],
                    obj_types=[self.a.obj_type, self.b.obj_type, self.qkv.obj_type],
                )
                start = ObjectFifo(f32(2 + self.slice_state), depth=1)
                part += start.prod().join(
                    [0, 2], obj_types=[self.head.obj_type, self.state.obj_type]
                )
                rows.append(row)
                starts.append(start)
                for lane, f in zip(ends, part):
                    lane.append(f.prod())
            for o, lane in zip((self.a, self.b, self.qkv, self.head, self.state), ends):
                o.bind(lane)
            of_ys = [ObjectFifo(self.y.obj_type) for _ in range(self.columns)]
            of_finals = [
                ObjectFifo(self.final.obj_type, depth=1) for _ in range(self.columns)
            ]
            self.y.bind([f.cons() for f in of_ys])
            self.final.bind([f.cons() for f in of_finals])
            rtps = [Rtp([self.count]) for _ in range(self.columns)]

            def core_fn(of_row, of_slice, of_y, of_final, rule, block, rtp, first):
                valid = rtp.read()[self.count]
                i32 = valid.type
                zero, size = arith.constant(0, i32), arith.constant(T, i32)
                k, v = T * Dk, 2 * T * Dk
                ab = v + T * SLICE
                for u in range_(_slices(self)):
                    h = u // per_head + first
                    p = 2 * V + 2 * self.k_heads * Dk + h * Dv + (u % per_head) * SLICE
                    g = 2 * V + (h // per_group) * Dk
                    start, final = of_slice.acquire(1), of_final.acquire(1)
                    for j in range_(self.rows // T):
                        # Gather the block: q, k, v, then a and b.
                        for t in range_(T):
                            row = of_row.acquire(1)
                            for i in range_(Dk):
                                block[t * Dk + i] = row[g + i]
                                block[k + t * Dk + i] = row[g + self.k_heads * Dk + i]
                            for i in range_(SLICE):
                                block[v + t * SLICE + i] = row[p + i]
                            block[ab + t] = row[h]
                            block[ab + T + t] = row[V + h]
                            of_row.release(1)
                        b = arith.index_cast(j, to=i32)
                        left = valid - b * size
                        live = arith.minsi(arith.maxsi(left, zero), size)
                        y = of_y.acquire(1)
                        rule(block, start, final, y, live, b)
                        of_y.release(1)
                    of_slice.release(1)
                    of_final.release(1)

            heads = V // self.columns
            workers = [
                Worker(
                    core_fn,
                    [
                        rows[k].cons(),
                        starts[k].cons(),
                        of_ys[k].prod(),
                        of_finals[k].prod(),
                        kernel,
                        Buffer(bf16(T * (2 * Dk + SLICE + 2))),
                        rtps[k],
                        k * heads,
                    ],
                )
                for k in range(self.columns)
            ]
            return Built(workers, rtps)

    def sequence(self, rt):
        """Per core, every row of ``a``, ``b`` and ``qkv`` once a slice, its
        heads' parameters and states, and its slices of ``y`` and ``final``.
        """
        R, V, W, I = self.rows, self.v_heads, self.width, self.inner
        Dk, Dv = self.key_dim, self.value_dim
        S, heads = _slices(self), V // self.columns
        # A core's heads' states, slice by slice: each key row's SLICE columns.
        slices = lambda k: TensorAccessPattern(
            (V, Dk, Dv),
            k * heads * Dk * Dv,
            [heads, Dv // SLICE, Dk, SLICE],
            [Dk * Dv, SLICE, Dv, 1],
        )
        tg = TaskGroup()
        for k in range(self.columns):
            for o in (self.a, self.b):
                o.fill(
                    TensorAccessPattern((R, V), 0, [S, R, V], [0, V, 1]),
                    lane=k,
                    group=tg,
                )
            self.qkv.fill(
                TensorAccessPattern((R, W), 0, [S, R, W], [0, W, 1]), lane=k, group=tg
            )
            self.head.fill(
                TensorAccessPattern(
                    (V, 2), 2 * k * heads, [heads, S // heads, 2], [2, 0, 1]
                ),
                lane=k,
                group=tg,
            )
            self.state.fill(slices(k), lane=k, group=tg)
        for k in range(self.columns):
            self.y.drain(
                TensorAccessPattern(
                    (R, I), k * heads * Dv, [S, R, SLICE], [SLICE, I, 1]
                ),
                lane=k,
                group=tg,
                wait=True,
            )
            self.final.drain(slices(k), lane=k, group=tg, wait=True)
        tg.finish()

    def tolerance(self):
        return Tolerance.relative(
            8e-3, range_frac=1e-3, note="f32 throughout, y rounded once: a bf16 ulp"
        )

    def reference(self, qkv, a, b, head, state):
        K, V, Dk = self.k_heads, self.v_heads, self.key_dim
        qkv, a, b = (np.asarray(m, np.float32) for m in (qkv, a, b))
        dt_bias, A = np.asarray(head, np.float32).T
        state = np.array(state, np.float32)
        y = np.zeros((self.rows, self.inner), np.float32)
        for t in range(self.valid):
            q, k = (
                np.repeat(m.reshape(K, Dk), V // K, axis=0)
                for m in np.split(qkv[t, : 2 * K * Dk], 2)
            )
            v = qkv[t, 2 * K * Dk :].reshape(V, self.value_dim)
            q = q / np.sqrt((q * q).sum(-1, keepdims=True) + 1e-6) / np.sqrt(Dk)
            k = k / np.sqrt((k * k).sum(-1, keepdims=True) + 1e-6)
            g = A * np.logaddexp(0, a[t] + dt_bias)
            beta = 1 / (1 + np.exp(-b[t]))
            state *= np.exp(g)[:, None, None]
            delta = beta[:, None] * (v - np.einsum("hk,hkv->hv", k, state))
            state += k[:, :, None] * delta[:, None, :]
            y[t] = np.einsum("hk,hkv->hv", q, state).reshape(-1)
        return y.astype(bfloat16), state
