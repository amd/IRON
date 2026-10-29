# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GatedDeltaRule: Gated DeltaNet's recurrence over a run of rows."""

from typing import ClassVar

import numpy as np
from aie.dialects import vector
from aie.extras import types
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, In, ObjectFifo, Out, TaskGroup, Worker, kernels
from aie.iron.controlflow import range_
from aie.utils.compile.jit.context import compile_context
from aie.utils.compile.utils import resolve_target_arch
from aie.utils.verify import Tolerance
from aie.utils.compile.jit.params import param, per_call, tunable, widths
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp
from iron.common.testing import Case, Testing
from iron.operators.state_slices import SLICE, depths, resolve_heads, resolve_rows


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
    one memtile joins to each row's ``a`` and ``b`` and every core reads;
    another joins each slice's state to its head's ``head``, so a core
    reads two streams. The kernel keeps the state from block to block.
    Scalar.
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
            # Too many shim BDs at once without reclaiming them.
            Case(
                dict(rows=1536, k_heads=2, v_heads=4, key_dim=16, value_dim=128),
                id="reclaim",
                extensive=True,
            ),
            # Qwen3.5's prefill: one command outlasts the driver's watchdog.
            Case(
                dict(rows=2048, k_heads=16, v_heads=32, key_dim=128, value_dim=128),
                id="qwen35_prefill",
                lower=True,
                run=False,
            ),
        ],
        draw=_trained,
    )

    # A long prefill holds more shim BDs than a tile has.
    aiecc_flags: ClassVar[tuple[str, ...]] = ("--reclaim-runtime-bds",)

    rows: int = param(array=True)
    k_heads: int = param(array=True)
    v_heads: int = param(array=True)
    key_dim: int = param(array=True)
    value_dim: int = param(array=True)
    columns: int = tunable(domain=widths)
    width: int = param(
        derive=lambda op: 2 * op.k_heads * op.key_dim + op.v_heads * op.value_dim,
        repr=False,
    )
    inner: int = param(
        derive=lambda op: op.v_heads * op.value_dim, repr=False, array=True
    )
    # The rows of y one kernel call writes, a whole number of SLICE-row runs.
    block: int = tunable(repr=False)
    slice_state: int = param(derive=lambda op: op.key_dim * SLICE, repr=False)

    qkv = In(rows, width, obj_shape=(width,))
    a = In(rows, v_heads, obj_shape=(v_heads,))
    b = In(rows, v_heads, obj_shape=(v_heads,))
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
    valid = per_call(bounds=rows)
    count = per_call(derive=lambda op: op.valid)

    def validate(self) -> None:
        if self.value_dim % SLICE or self.v_heads % self.k_heads or self.v_heads % 2:
            raise ValueError(
                f"GatedDeltaRule: value_dim ({self.value_dim}) must be whole "
                f"{SLICE}-column slices, and v_heads ({self.v_heads}) whole "
                f"groups of k_heads ({self.k_heads}) and even, so a row's b "
                "after its a is 4-byte aligned"
            )

    def resolve(self, dev):
        return resolve_rows(resolve_heads(self, dev, self.v_heads), dev)

    def slice_bytes(self) -> tuple[int, int]:
        """Bytes of a slice's (dt_bias, A) then state in, and its final out."""
        return 4 * (2 + self.slice_state), 4 * self.slice_state

    def held(self, dev, rows: int) -> int:
        """Return the bytes a core of ``dev`` uses at ``rows`` rows per call.

        That is the input row, the block buffer, y, the kernel's data and
        stack (its own copy of the state included), and the device's default
        stack, which covers the core's own frame. One slice's state and final
        state are not counted.
        """
        # Only measured, never built, so it stays out of the build's registry.
        with compile_context(_iron_kernel_registry=set()):
            kernel = self.kernel(rows)
            block = 2 * int(np.prod(kernel.arg_shape(0)))
            frame = kernel.frame_bytes(resolve_target_arch(dev))
        frame += dev.default_core_stack_bytes
        return 2 * (self.width + 2 * self.v_heads) + block + 4 * rows * SLICE + frame

    def kernel(self, rows: int):
        return kernels.ssm.gated_delta_rule(
            rows=rows,
            key_dim=self.key_dim,
            value_dim=SLICE,
            blocks=self.rows // rows,
        )

    def build(self) -> Built:
        V, Dk, Dv, W = self.v_heads, self.key_dim, self.value_dim, self.width
        T, per_group, heads = self.block // SLICE, V // self.k_heads, V // self.columns
        kernel = self.kernel(T)
        f32 = lambda n: np.ndarray[(n,), np.dtype[np.float32]]
        bf16 = lambda n: np.ndarray[(n,), np.dtype[bfloat16]]
        deep_in, deep_out = depths(self)
        # A core takes two streams, a memtile joining each: a row's qkv
        # then its a and b, one stream every core reads, and a slice's
        # (dt_bias, A) then its state.
        row = ObjectFifo(bf16(W + 2 * V), depth=1)
        parts = row.prod().join(
            [0, W, W + V],
            obj_types=[self.qkv.obj_type, self.a.obj_type, self.b.obj_type],
        )
        for o, f in zip((self.qkv, self.a, self.b), parts):
            o.bind([f.prod()])
        starts, ends = [], ([], [])
        for _ in range(self.columns):
            start = ObjectFifo(f32(2 + self.slice_state), depth=deep_in)
            part = start.prod().join(
                [0, 2], obj_types=[self.head.obj_type, self.state.obj_type]
            )
            starts.append(start)
            for lane, f in zip(ends, part):
                lane.append(f.prod())
        for o, lane in zip((self.head, self.state), ends):
            o.bind(lane)
        of_ys = [ObjectFifo(self.y.obj_type) for _ in range(self.columns)]
        of_finals = [
            ObjectFifo(self.final.obj_type, depth=deep_out) for _ in range(self.columns)
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
            for q in range_(_slices(self) // heads):
                for r in range_(heads):
                    # Slice q of head r of the core's heads in turn, q and r
                    # each their own loop counter rather than a flattened
                    # index's div/mod (AIE2's backend cannot legalize the
                    # bitreverse Peano's mid-end folds that div/mod into).
                    h = r + first
                    p = 2 * self.k_heads * Dk + h * Dv + q * SLICE
                    g = (h // per_group) * Dk
                    start, final = of_slice.acquire(1), of_final.acquire(1)
                    for j in range_(self.rows // T):
                        # Gather the block: q, k, v, then a and b; q, k and v a
                        # vector of SLICE at a time where q's and k's rows are
                        # whole vectors, which qkv first keeps 32-byte aligned.
                        for t in range_(T):
                            row = of_row.acquire(1)
                            runs = []
                            if Dk % SLICE:
                                for i in range_(Dk):
                                    block[t * Dk + i] = row[g + i]
                                    block[k + t * Dk + i] = row[
                                        g + self.k_heads * Dk + i
                                    ]
                                for i in range_(SLICE):
                                    block[v + t * SLICE + i] = row[p + i]
                            else:
                                runs = [
                                    (c * k + t * Dk + i, g + c * self.k_heads * Dk + i)
                                    for c in range(2)
                                    for i in range(0, Dk, SLICE)
                                ] + [(v + t * SLICE, p)]
                            lane = types.vector(SLICE, types.bf16())
                            for to, at in runs:
                                vector.store(
                                    vector.load(lane, row, [at], alignment=32),
                                    block.op,
                                    [to],
                                    alignment=32,
                                )
                            block[ab + t] = row[W + h]
                            block[ab + T + t] = row[W + V + h]
                            of_row.release(1)
                        b = arith.index_cast(j, to=i32)
                        left = valid - b * size
                        live = arith.minsi(arith.maxsi(left, zero), size)
                        y = of_y.acquire(1)
                        rule(block, start, final, y, live, b)
                        of_y.release(1)
                    of_slice.release(1)
                    of_final.release(1)

        workers = [
            Worker(
                core_fn,
                [
                    row.cons(),
                    starts[k].cons(),
                    of_ys[k].prod(),
                    of_finals[k].prod(),
                    kernel,
                    Buffer(kernel.arg_types()[0]),
                    rtps[k],
                    k * heads,
                ],
            )
            for k in range(self.columns)
        ]
        return Built(workers, rtps)

    def sequence(self, rt):
        """Every row of ``qkv``, ``a`` and ``b`` once a slice, for every core;
        per core, its heads' parameters and states, and its slices of ``y``
        and ``final``.
        """
        R, V, W, I = self.rows, self.v_heads, self.width, self.inner
        Dk, Dv = self.key_dim, self.value_dim
        S, heads = _slices(self), V // self.columns
        per = S // heads
        # A core's heads' states, a slice (each key row's SLICE columns) of
        # each head in turn.
        slices = lambda k: TensorAccessPattern(
            (V, Dk, Dv),
            k * heads * Dk * Dv,
            [per, heads, Dk, SLICE],
            [SLICE, Dk * Dv, Dv, 1],
        )
        tg = TaskGroup()
        self.qkv.fill(TensorAccessPattern((R, W), 0, [S, R, W], [0, W, 1]), group=tg)
        for o in (self.a, self.b):
            o.fill(TensorAccessPattern((R, V), 0, [S, R, V], [0, V, 1]), group=tg)
        for k in range(self.columns):
            self.head.fill(
                TensorAccessPattern((V, 2), 2 * k * heads, [per, heads, 2], [0, 2, 1]),
                lane=k,
                group=tg,
            )
            self.state.fill(slices(k), lane=k, group=tg)
        for k in range(self.columns):
            self.y.drain(
                TensorAccessPattern(
                    (R, I), k * heads * Dv, [per, heads, R, SLICE], [SLICE, Dv, I, 1]
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
