# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Grouped-query decode attention's two products, read in place from the caches.

One query's heads against ``(seq_len, groups, head_dim)`` key and value
caches: ``GQAScores`` is each head's dot product with its group's keys,
``GQAContext`` each head's softmax weights over its group's values. Between
them a graph runs ``Softmax``:

```python
scores = GQAScores(keys[:n], q)              # (heads, seq_len), q pre-scaled
ctx = GQAContext(values[:n], Softmax(scores))  # (heads, head_dim)
```

A call bounded to ``n`` positions streams the ``chunk``-position blocks
``n`` covers, so a step costs its context, not the cache, and one array
serves every cache length.
"""

import dataclasses

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
from aie.iron.kernels import MV_COL_MAJ_FIRST, MV_COL_MAJ_LAST, linalg
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Divisors, Extent, In, Operator, Out, Value, auto, param
from iron.common.testing import Case, Testing

# The context kernel's partial sums per output: the vector width GEMV's
# kernel takes over any context of 128 positions or more.
_LANES = 64


def reference(values, weights) -> np.ndarray:
    """``ctx[h, d] = sum_l weights[h, l] * values[l, h // (heads // groups), d]``.

    ``values`` is ``(L, groups, D)`` and ``weights`` ``(heads, L)``, both bf16;
    the result is ``(heads, D)`` bf16. Summed as the kernel sums: lane ``j``
    of each output takes positions ``_LANES * i + j`` in order of ``i``,
    starting from the first product; the lanes are halved, lane ``j +
    lanes / 2`` onto lane ``j``, down to 1; the float left is rounded to
    bf16, to nearest even. Positions past ``L`` are zero products, which
    change no sum. A product of two bf16 is exact in float32, so each step
    is one float32 addition, as on the core. The core's adder is not IEEE
    on every cancelling add of mixed signs, so on signed operands this can
    miss an output bit now and then; on non-negative ones it is exact.
    """
    values = np.asarray(values, dtype=bfloat16)
    weights = np.asarray(weights, dtype=bfloat16)
    length, groups, dim = values.shape
    heads = weights.shape[0]
    if weights.shape != (heads, length) or heads % groups:
        raise ValueError(
            f"weights {weights.shape} are not (a multiple of {groups} heads, {length})"
        )
    rounds = ceildiv(length, _LANES)
    v = np.zeros((heads, rounds * _LANES, dim), dtype=np.float32)
    v[:, :length] = np.repeat(
        values.astype(np.float32).transpose(1, 0, 2), heads // groups, axis=0
    )
    p = np.zeros((heads, rounds * _LANES), dtype=np.float32)
    p[:, :length] = weights
    # (heads, rounds, lanes, D): position lanes * i + j is round i, lane j.
    products = (v * p[:, :, None]).reshape(heads, rounds, _LANES, dim)
    partial = products[:, 0].copy()
    for i in range(1, rounds):
        partial += products[:, i]
    half = _LANES // 2
    while half >= 1:
        partial[:, :half] += partial[:, half : 2 * half]
        half //= 2
    return partial[:, 0].astype(bfloat16)


class _KVGroups(Operator):
    """One query's heads against a ``(seq_len, groups, head_dim)`` cache.

    A column takes ``groups / num_aie_columns`` groups in turn, one core per
    head of a group. The group's cache rows stream once through the column,
    ``chunk`` positions at a time, broadcast to its cores; each head's own
    stream goes through a memtile split or join.
    """

    heads: int = param()
    groups: int = param(array=True)
    seq_len: int = param()
    head_dim: int = param(default=64)
    heads_per_group: int = param(default=lambda op: op.heads // op.groups)
    # None: the most columns the shim budget allows that divide the groups.
    num_aie_columns: int = auto()
    # A core holds one (chunk, head_dim) block of the cache, and the context
    # kernel takes chunk in whole rounds of its lanes.
    chunk: int = auto(
        128,
        domain=Divisors(
            of=lambda op: op.seq_len,
            step=_LANES,
            cap=lambda op, dev: dev.core_memory_bytes
            // (op.head_dim * np.dtype(bfloat16).itemsize),
        ),
    )

    valid = Extent(seq_len)  # seq_len, or fewer positions per call
    calls = Value(np.int32, derive=lambda op: ceildiv(op.valid, op.chunk))

    def validate(self) -> None:
        if self.heads % self.groups:
            raise ValueError(
                f"heads ({self.heads}) must be a multiple of groups ({self.groups})"
            )
        self.check_derived("heads_per_group")

    def resolve(self, dev):
        if self.heads_per_group > len(dev.core_rows):
            raise ValueError(
                f"heads_per_group ({self.heads_per_group}) must be at most "
                f"{len(dev.core_rows)}: one core per head, in one column"
            )
        cols = self.resolve_columns(
            dev, self.num_aie_columns, fits=lambda c: self.groups % c == 0
        )
        return dataclasses.replace(self, num_aie_columns=cols)

    def compatible(self) -> None:
        if self.groups % self.num_aie_columns:
            raise ValueError(
                f"groups ({self.groups}) must be a multiple of the "
                f"{self.num_aie_columns} columns"
            )
        if self.seq_len % self.chunk:
            raise ValueError(
                f"seq_len ({self.seq_len}) must be a multiple of chunk ({self.chunk})"
            )

    def extent_unit(self, buffer: str) -> int:
        return 0  # no tiles-per-lane word: the sequence bounds the blocks itself

    @property
    def rounds(self) -> int:
        """The groups each column takes in turn."""
        return self.groups // self.num_aie_columns

    def _calls(self, target) -> tuple[list, list, bool]:
        """Each core's source of ``calls``, its barrier, and whether the source
        is the scratchpad word a full ELF's call sets rather than a runtime
        parameter the sequence writes. A core re-arms its barrier once it
        has read the count: an xclbin's cores outlive the call, and would
        else start the next on this one's.
        """
        cores = self.num_aie_columns * self.heads_per_group
        barriers = [WorkerRuntimeBarrier() for _ in range(cores)]
        if target.image == "elf" and self.uses_value("calls"):
            return [self.calls.param] * cores, barriers, True
        rtps = [
            Buffer(
                np.ndarray[(1,), np.dtype[np.int32]],
                name=f"calls_{i}",
                use_write_rtp=True,
            )
            for i in range(cores)
        ]
        self.calls.bind(rtps)
        return rtps, barriers, False

    def _cache_rows(self, col: int) -> TensorAccessPattern:
        """Column ``col``'s groups of a cache, as ``(group, block, position, d)``."""
        shape = (self.seq_len, self.groups, self.head_dim)
        rows = TensorAccessPattern.full(shape).permute((1, 0, 2))
        groups = slice(col * self.rounds, (col + 1) * self.rounds)
        return rows[groups, : ceildiv(self.valid, self.chunk) * self.chunk].split(
            1, self.chunk
        )

    def _head_blocks(self, col: int) -> TensorAccessPattern:
        """Column ``col``'s heads of a ``(heads, seq_len)`` buffer, as ``(group,
        block, head, position)``.
        """
        hpg = self.heads_per_group
        heads = slice(col * self.rounds * hpg, (col + 1) * self.rounds * hpg)
        span = ceildiv(self.valid, self.chunk) * self.chunk
        tap = TensorAccessPattern.full((self.heads, self.seq_len))[heads, :span]
        return tap.split(0, hpg).split(2, self.chunk).permute((0, 2, 1, 3))


class GQAScores(_KVGroups):
    """Each head's dot product with its group's cached keys.

    ``scores[h, l] = q[h] . keys[l, h // heads_per_group]``: each core holds
    its head's query and runs GEMV's kernel over a block of its group's keys
    at a time. A call bounded to ``n`` positions writes the blocks ``n``
    covers; the positions past ``n`` in the last are what the cache holds
    there, which a ``Softmax`` over ``scores[:, :n]`` masks.
    """

    test = Testing(
        [
            Case(dict(heads=8, groups=2, seq_len=256), id="small"),
            Case(
                dict(heads=6, groups=3, seq_len=128, chunk=64, num_aie_columns=1),
                id="three_groups_a_column",
                lower=True,
            ),
            Case(dict(heads=4, groups=4, seq_len=128), id="one_head_a_group"),
            Case(
                dict(heads=32, groups=8, seq_len=2048, num_aie_columns=4),
                id="llama_npu1_columns",
            ),
            Case(dict(heads=32, groups=8, seq_len=2048), id="llama", bench=True),
        ],
        draw=dict(normal=("keys", "q")),
    )

    keys = In(
        _KVGroups.seq_len,
        _KVGroups.groups,
        _KVGroups.head_dim,
        tile=(_KVGroups.chunk, _KVGroups.head_dim),
        per=(_KVGroups.num_aie_columns,),
        depth=2,
    )
    q = In(
        _KVGroups.heads,
        _KVGroups.head_dim,
        tile=(_KVGroups.heads_per_group, _KVGroups.head_dim),
        per=(_KVGroups.num_aie_columns,),
        depth=2,
    )
    scores = Out(
        _KVGroups.heads,
        _KVGroups.seq_len,
        tile=(_KVGroups.heads_per_group, _KVGroups.chunk),
        per=(_KVGroups.num_aie_columns,),
        depth=2,
    )

    def array(self, target) -> list:
        D, chunk, hpg, rounds = (
            self.head_dim,
            self.chunk,
            self.heads_per_group,
            self.rounds,
        )
        # The width GEMV's kernel takes at K = head_dim, so the sums are its.
        width = next(w for w in (64, 32, 16) if D % w == 0 and D >= 2 * w)
        matvec = linalg.mv(chunk, D, bfloat16, bfloat16, vec_size=width)
        q_ty = np.ndarray[(D,), np.dtype[bfloat16]]
        s_ty = np.ndarray[(chunk,), np.dtype[bfloat16]]
        sources, barriers, per_call = self._calls(target)

        def core_body(of_k, of_q, of_s, matvec, calls, barrier):
            barrier.wait_for_value(1)
            n = calls.read() if per_call else calls[0]
            barrier.release_with_value(1)
            for _ in range_(rounds):
                q = of_q.acquire(1)
                for _ in range_(n):
                    k = of_k.acquire(1)
                    s = of_s.acquire(1)
                    matvec(chunk, 0, k, q, s)
                    of_k.release(1)
                    of_s.release(1)
                of_q.release(1)

        workers = []
        for c in range(self.num_aie_columns):
            of_k = ObjectFifo(self.keys.tile, name=f"k_{c}", depth=2)
            self.keys.lane(c).bind(of_k.prod())
            of_q = ObjectFifo(self.q.tile, name=f"q_{c}", depth=2)
            self.q.lane(c).bind(of_q.prod())
            q_heads = of_q.cons().split(
                [D * k for k in range(hpg)],
                obj_types=[q_ty] * hpg,
                names=[f"q_{c}_{k}" for k in range(hpg)],
                depths=[2] * hpg,
            )
            of_s = ObjectFifo(self.scores.tile, name=f"s_{c}", depth=2)
            self.scores.lane(c).bind(of_s.cons())
            s_heads = of_s.prod().join(
                [chunk * k for k in range(hpg)],
                obj_types=[s_ty] * hpg,
                names=[f"s_{c}_{k}" for k in range(hpg)],
                depths=[2] * hpg,
            )
            for k in range(hpg):
                i = c * hpg + k
                workers.append(
                    Worker(
                        core_body,
                        [
                            of_k.cons(),
                            q_heads[k].cons(),
                            s_heads[k].prod(),
                            matvec,
                            sources[i],
                            barriers[i],
                        ],
                    )
                )
        return workers + barriers

    def sequence(self, rt):
        """Column ``c`` takes its groups' queries, then each group's keys a
        block at a time, and gives back each block of the group's scores,
        every head's together.
        """
        size_by = {1: self.calls} if self.uses_value("calls") else None
        hpg = self.heads_per_group
        q = TensorAccessPattern.full(self.q.shape)
        tg = TaskGroup()
        for c in range(self.num_aie_columns):
            heads = slice(c * self.rounds * hpg, (c + 1) * self.rounds * hpg)
            rt.fill(self.q.lane(c), q[heads].coalesce(), group=tg)
            rt.fill(
                self.keys.lane(c),
                self._cache_rows(c),
                group=tg,
                size_by=size_by,
            )
        for c in range(self.num_aie_columns):
            rt.drain(
                self.scores.lane(c),
                self._head_blocks(c),
                group=tg,
                wait=True,
                size_by=size_by,
            )
        tg.finish()

    def ops(self) -> int:
        return 2 * self.heads * self.seq_len * self.head_dim

    def tolerance(self) -> Tolerance:
        return Tolerance.relative(0.04, 1e-3, note="f32 accumulation, rounded once")

    def reference(self, keys, q):
        k = np.repeat(np.asarray(keys).astype(np.float32), self.heads_per_group, axis=1)
        scores = np.einsum("lhd,hd->hl", k, np.asarray(q).astype(np.float32))
        return scores.astype(bfloat16)


class GQAContext(_KVGroups):
    """Each head's softmax weights over its group's cached values.

    ``ctx[h] = sum_l weights[h, l] * values[l, h // heads_per_group]``: each
    core carries its head's partial sums across the blocks in its own
    memory, ``linalg.mv(..., a_col_maj=True)``, GEMV's kernel reading its
    matrix transposed, so the sums are a GEMV's over the transpose. A call
    bounded to ``n`` positions reads the blocks ``n`` covers, so the weights
    past ``n`` in the last must be zeros, as a bounded ``Softmax`` writes
    them, and the values there finite.
    """

    # The reference is the kernel's order in IEEE float32, which the core
    # matches on the non-negative operands drawn here (see reference), so
    # any difference is a bug. Equality with a GEMV over the transpose, on
    # signed data, is iron/tests/operators/gqa_context_vs_gemv.py.
    test = Testing(
        [
            Case(dict(heads=8, groups=2, seq_len=256), id="small"),
            Case(
                dict(heads=6, groups=3, seq_len=128, chunk=64, num_aie_columns=1),
                id="three_groups_a_column",
                lower=True,
            ),
            Case(dict(heads=1, groups=1, seq_len=128), id="single_call"),
            Case(dict(heads=16, groups=4, seq_len=64, chunk=64), id="shortest"),
            Case(
                dict(heads=32, groups=8, seq_len=2048, num_aie_columns=4),
                id="llama_npu1_columns",
            ),
            Case(dict(heads=32, groups=8, seq_len=2048), id="llama", bench=True),
        ],
        tolerance=Tolerance.exact(),
    )

    cache = In(
        _KVGroups.seq_len,
        _KVGroups.groups,
        _KVGroups.head_dim,
        tile=(_KVGroups.chunk, _KVGroups.head_dim),
        per=(_KVGroups.num_aie_columns,),
        depth=2,
    )
    weights = In(
        _KVGroups.heads,
        _KVGroups.seq_len,
        tile=(_KVGroups.heads_per_group, _KVGroups.chunk),
        per=(_KVGroups.num_aie_columns,),
        depth=2,
    )
    ctx = Out(
        _KVGroups.heads,
        _KVGroups.head_dim,
        tile=(_KVGroups.heads_per_group, _KVGroups.head_dim),
        per=(_KVGroups.num_aie_columns,),
        depth=1,
    )

    def compatible(self) -> None:
        super().compatible()
        # The kernel checks the rest: head_dim a whole number of vectors,
        # chunk whole rounds of the lanes.
        self._kernel()

    def _kernel(self):
        return linalg.mv(
            self.head_dim,
            self.chunk,
            bfloat16,
            bfloat16,
            vec_size=_LANES,
            a_col_maj=True,
        )

    def array(self, target) -> list:
        kernel = self._kernel()
        D, chunk, hpg, rounds = (
            self.head_dim,
            self.chunk,
            self.heads_per_group,
            self.rounds,
        )
        acc_ty = np.ndarray[(_LANES * D,), np.dtype[np.float32]]
        p_ty = np.ndarray[(chunk,), np.dtype[bfloat16]]
        out_ty = np.ndarray[(D,), np.dtype[bfloat16]]
        sources, barriers, per_call = self._calls(target)

        def core_body(of_v, of_p, of_out, acc, kernel, calls, barrier):
            barrier.wait_for_value(1)
            n = calls.read() if per_call else calls[0]
            barrier.release_with_value(1)
            last = n - 1
            for _ in range_(rounds):
                out = of_out.acquire(1)
                for b in range_(n):
                    b32 = arith.index_cast(b, to=n.type)
                    # Where the block sits in the context: the first starts
                    # the sums, the last writes them.
                    flags = arith.extui(n.type, b32 == 0) * MV_COL_MAJ_FIRST
                    flags = flags + arith.extui(n.type, b32 == last) * MV_COL_MAJ_LAST
                    v = of_v.acquire(1)
                    p = of_p.acquire(1)
                    kernel(flags, v, p, acc, out)
                    of_v.release(1)
                    of_p.release(1)
                of_out.release(1)

        workers = []
        for c in range(self.num_aie_columns):
            of_v = ObjectFifo(self.cache.tile, name=f"v_{c}", depth=2)
            self.cache.lane(c).bind(of_v.prod())
            of_p = ObjectFifo(self.weights.tile, name=f"p_{c}", depth=2)
            self.weights.lane(c).bind(of_p.prod())
            p_heads = of_p.cons().split(
                [chunk * k for k in range(hpg)],
                obj_types=[p_ty] * hpg,
                names=[f"p_{c}_{k}" for k in range(hpg)],
                depths=[2] * hpg,
            )
            of_ctx = ObjectFifo(self.ctx.tile, name=f"ctx_{c}", depth=1)
            self.ctx.lane(c).bind(of_ctx.cons())
            ctx_heads = of_ctx.prod().join(
                [D * k for k in range(hpg)],
                obj_types=[out_ty] * hpg,
                names=[f"ctx_{c}_{k}" for k in range(hpg)],
                depths=[1] * hpg,
            )
            for k in range(hpg):
                i = c * hpg + k
                workers.append(
                    Worker(
                        core_body,
                        [
                            of_v.cons(),
                            p_heads[k].cons(),
                            ctx_heads[k].prod(),
                            Buffer(acc_ty, name=f"acc_{c}_{k}"),
                            kernel,
                            sources[i],
                            barriers[i],
                        ],
                    )
                )
        return workers + barriers

    def sequence(self, rt):
        """Column ``c`` takes each of its groups' values a block at a time and
        its heads' weights for the same block, every head's together; its
        heads' contexts come back contiguous.
        """
        size_by = {1: self.calls} if self.uses_value("calls") else None
        hpg = self.heads_per_group
        ctx = TensorAccessPattern.full(self.ctx.shape)
        tg = TaskGroup()
        for c in range(self.num_aie_columns):
            rt.fill(
                self.cache.lane(c),
                self._cache_rows(c),
                group=tg,
                size_by=size_by,
            )
            rt.fill(
                self.weights.lane(c),
                self._head_blocks(c),
                group=tg,
                size_by=size_by,
            )
        for c in range(self.num_aie_columns):
            heads = slice(c * self.rounds * hpg, (c + 1) * self.rounds * hpg)
            rt.drain(self.ctx.lane(c), ctx[heads].coalesce(), group=tg, wait=True)
        tg.finish()

    def ops(self) -> int:
        return 2 * self.heads * self.seq_len * self.head_dim

    def reference(self, values, weights):
        return reference(values, weights)
