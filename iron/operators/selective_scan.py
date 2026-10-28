# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SelectiveScan: Mamba2's state space recurrence over a run of rows."""

from typing import ClassVar

import numpy as np
from aie.dialects import vector
from aie.extras import types
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, In, ObjectFifo, Out, TaskGroup, Worker, kernels
from aie.iron.controlflow import range_
from aie.utils.verify import Tolerance
from aie.utils.compile.jit.context import compile_context
from aie.utils.compile.utils import resolve_target_arch
from aie.utils.compile.jit.params import param, per_call, tunable, widths
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp
from iron.common.testing import Case, Testing
from iron.operators.state_slices import SLICE, depths, resolve_heads, resolve_rows


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
    state at a time, and gathers a block of rows' ``x``, ``B``, ``C`` and
    ``dt`` for the slice from whole rows of ``xbc``, which one memtile
    joins to each row's ``dt`` and every core reads; another joins each
    slice's state to its head's ``head``, so a core reads two streams.
    The kernel keeps the state from block to block. Scalar.
    """

    test = Testing(
        [
            Case(dict(rows=5, heads=2, head_dim=16, state_size=16, columns=1)),
            Case(dict(rows=8, heads=4, head_dim=32, state_size=32, groups=2)),
            # Granite 4.0-H's decode: a one-row block over a 128-wide state,
            # its B and C off the 64-byte line an even block keeps them on.
            Case(
                dict(rows=1, heads=2, head_dim=16, state_size=128, columns=1),
                id="decode",
            ),
            Case(
                dict(rows=3, heads=2, head_dim=16, state_size=64, columns=1),
                id="odd_rows",
                extensive=True,
            ),
            Case(
                dict(rows=64, heads=16, head_dim=64, state_size=64, groups=2),
                bench=True,
            ),
            # Too many shim BDs at once without reclaiming them.
            Case(
                dict(rows=2048, heads=8, head_dim=64, state_size=16),
                id="reclaim",
                extensive=True,
            ),
        ],
        draw=_trained,
    )

    # A long prefill holds more shim BDs than a tile has.
    aiecc_flags: ClassVar[tuple[str, ...]] = ("--reclaim-runtime-bds",)

    rows: int = param(array=True)
    heads: int = param(array=True)
    head_dim: int = param(array=True)
    state_size: int = param(array=True)
    groups: int = param(default=1, array=True)
    columns: int = tunable(domain=widths)
    inner: int = param(derive=lambda op: op.heads * op.head_dim, repr=False, array=True)
    width: int = param(
        derive=lambda op: op.inner + 2 * op.groups * op.state_size, repr=False
    )
    # The rows of y one kernel call writes: whole SLICE-row runs that fit L1.
    block: int = tunable(repr=False)
    slice_state: int = param(derive=lambda op: SLICE * op.state_size, repr=False)

    xbc = In(rows, width, obj_shape=(width,))
    dt = In(rows, heads, obj_shape=(heads,))
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
    y = Out(rows, inner, obj_shape=(block,), per=(columns,))
    final = Out(
        heads,
        head_dim,
        state_size,
        dtype=np.float32,
        obj_shape=(slice_state,),
        per=(columns,),
        depth=1,
    )
    valid = per_call(bounds=rows)
    count = per_call(derive=lambda op: op.valid)

    def validate(self) -> None:
        if self.head_dim % SLICE or self.heads % self.groups or self.heads % 2:
            raise ValueError(
                f"SelectiveScan: head_dim ({self.head_dim}) must be whole "
                f"{SLICE}-row slices, and heads ({self.heads}) whole groups "
                f"({self.groups}) and even, so a row's dt after its xbc is "
                "whole 4-byte words"
            )

    def resolve(self, dev):
        return resolve_rows(resolve_heads(self, dev, self.heads), dev)

    def slice_bytes(self) -> tuple[int, int]:
        """Bytes of a slice's (dt_bias, A, D) then state in, and its final out."""
        return 4 * (3 + self.slice_state), 4 * self.slice_state

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
        return 2 * (self.width + self.heads) + block + 4 * rows * SLICE + frame

    def kernel(self, rows: int):
        return kernels.ssm.selective_scan(
            rows=rows,
            head_dim=SLICE,
            state=self.state_size,
            blocks=self.rows // rows,
        )

    def build(self) -> Built:
        H, P, N, I = self.heads, self.head_dim, self.state_size, self.inner
        T, per_group, heads = self.block // SLICE, H // self.groups, H // self.columns
        kernel = self.kernel(T)
        f32 = lambda n: np.ndarray[(n,), np.dtype[np.float32]]
        bf16 = lambda n: np.ndarray[(n,), np.dtype[bfloat16]]
        deep_in, deep_out = depths(self)
        # A core takes two streams, a memtile joining each: a row's xbc
        # then its dt, one stream every core reads, and a slice's (dt_bias,
        # A, D) then its state.
        row = ObjectFifo(bf16(self.width + H), depth=1)
        parts = row.prod().join(
            [0, self.width], obj_types=[self.xbc.obj_type, self.dt.obj_type]
        )
        for o, f in zip((self.xbc, self.dt), parts):
            o.bind([f.prod()])
        starts, ends = [], ([], [])
        for _ in range(self.columns):
            start = ObjectFifo(f32(3 + SLICE * N), depth=deep_in)
            part = start.prod().join(
                [0, 3], obj_types=[self.head.obj_type, self.state.obj_type]
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

        def core_fn(of_row, of_slice, of_y, of_final, scan, block, rtp, first):
            valid = rtp.read()[self.count]
            i32 = valid.type
            zero, size = arith.constant(0, i32), arith.constant(T, i32)
            bc, dt = T * SLICE, T * (SLICE + 2 * N)
            for q in range_(_slices(self) // heads):
                for r in range_(heads):
                    # Slice q of head r of the core's heads in turn, q and r
                    # each their own loop counter rather than a flattened
                    # index's div/mod (AIE2's backend cannot legalize the
                    # bitreverse Peano's mid-end folds that div/mod into).
                    h = r + first
                    p = q * SLICE + h * P
                    g = (h // per_group) * N + I
                    start, final = of_slice.acquire(1), of_final.acquire(1)
                    for j in range_(self.rows // T):
                        # Gather the block: x, then B and C, then dt, a
                        # vector of SLICE at a time; xbc first keeps each
                        # 32-byte aligned.
                        for t in range_(T):
                            row = of_row.acquire(1)
                            block[dt + t] = row[self.width + h]
                            lane = types.vector(SLICE, types.bf16())
                            runs = [(t * SLICE, p)] + [
                                (
                                    bc + t * 2 * N + c * N + n,
                                    g + c * self.groups * N + n,
                                )
                                for c in range(2)
                                for n in range(0, N, SLICE)
                            ]
                            for to, at in runs:
                                vector.store(
                                    vector.load(lane, row, [at], alignment=32),
                                    block.op,
                                    [to],
                                    alignment=32,
                                )
                            of_row.release(1)
                        b = arith.index_cast(j, to=i32)
                        left = valid - b * size
                        live = arith.minsi(arith.maxsi(left, zero), size)
                        y = of_y.acquire(1)
                        scan(block, start, final, y, live, b)
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
        """Every row of ``xbc`` and ``dt`` once a slice, for every core; per
        core, its heads' parameters and states, and its slices of ``y`` and
        ``final``.
        """
        R, H, W, I = self.rows, self.heads, self.width, self.inner
        P, SN = self.head_dim, SLICE * self.state_size
        S, heads = _slices(self), H // self.columns
        per, states, run = S // heads, H * P * self.state_size, S * SN
        # A core's heads' states, a slice of each head in turn.
        slices = lambda k: TensorAccessPattern(
            (states,), k * run, [per, heads, SN], [SN, P * self.state_size, 1]
        )
        tg = TaskGroup()
        self.xbc.fill(TensorAccessPattern((R, W), 0, [S, R, W], [0, W, 1]), group=tg)
        self.dt.fill(TensorAccessPattern((R, H), 0, [S, R, H], [0, H, 1]), group=tg)
        for k in range(self.columns):
            self.head.fill(
                TensorAccessPattern((H, 3), 3 * k * heads, [per, heads, 3], [0, 3, 1]),
                lane=k,
                group=tg,
            )
            self.state.fill(slices(k), lane=k, group=tg)
        for k in range(self.columns):
            self.y.drain(
                TensorAccessPattern(
                    (R, I), k * heads * P, [per, heads, R, SLICE], [SLICE, P, I, 1]
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
