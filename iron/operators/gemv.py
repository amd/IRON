# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import math
from contextlib import nullcontext
from enum import StrEnum
from typing import Any, ClassVar

import aie.dialects.arith as arith
import aie.dialects.index as index
import numpy as np
from aie.dialects.aie import AIEArch, T
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Buffer,
    ObjectFifo,
    TaskGroup,
    Worker,
    WorkerRuntimeBarrier,
    ceildiv,
)
from aie.iron.controlflow import if_, range_
from aie.iron.device import Device
from aie.iron.kernels import activation, linalg
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Extent,
    In,
    Operator,
    Out,
    UnaryElementwise,
    Unresolvable,
    Value,
    auto,
    OptionalDim,
    param,
)
from iron.common.design import BdLimits, Target
from iron.common.testing import Case, Testing


def _cases(cls, dev: Device):
    # M, K, columns, tile_size_input, tile_size_output
    plain = [
        (128, 128, 1, 32, 128),
        (2048, 8192, 1, 1, 2048),
        (8192, 2048, 1, 4, 1024),
        (2048, 8192, 2, 1, 1024),
        (8192, 2048, 2, 4, 1024),
        (2048, 8192, 4, 1, 512),
        (8192, 2048, 4, 4, 1024),
        (2048, 8192, 8, 1, 256),
        (8192, 2048, 8, 4, 1024),
    ]
    # ... and num_batches: the coalesced batch path and its fallback.
    batched = [
        (256, 128, 1, 1, 256, 4),  # tiny, coalesced
        (256, 128, 8, 1, 32, 100),  # large num_batches: the size-uncapped dim
        (448, 64, 8, 1, 56, 192),  # a multi-dim run split, and many batches
        (64, 1536, 1, 1, 64, 8),  # large K
        (1026, 64, 1, 1, 2, 2),  # a run that needs an even (granule) split
        (1024, 1024, 1, 1, 64, 2),  # batch stride > 2**20: per-batch fallback
        (512, 64, 8, 4, 64, 32),  # attention's: several rows, a batch per head
    ]
    # ... and repeat: several batches per matrix of A.
    repeated = [
        (256, 128, 2, 1, 64, 8, 4),  # coalesced: A re-read in the iteration slot
        (256, 128, 2, 1, 64, 4, 4),  # one matrix for every batch
        (1024, 1024, 1, 1, 64, 4, 2),  # A's run does not factor: one per batch
        (2048, 64, 8, 4, 256, 32, 4),  # Llama decode's scores: 32 heads, 8 groups
    ]

    def case(M, K, cols, tsi, tso, *, bench=False, **extra):
        kwargs = dict(M=M, K=K, num_aie_columns=cols, tile_size_input=tsi)
        return Case(dict(kwargs, tile_size_output=tso, **extra), bench=bench)

    # Benched: the large matrices across the whole device, which run well
    # past the dispatch cost.
    widest = dev.cols

    def bench(M, K, cols, *_):
        return cols == widest and M * K >= 2048 * 8192

    return (
        [case(*p, bench=bench(*p)) for p in plain]
        + [case(*p, num_batches=batches) for *p, batches in batched]
        + [case(*p, num_batches=batches, repeat=r) for *p, batches, r in repeated]
        # The fused GELU epilogue, aie2p's alone.
        + [case(*p, epilogue="gelu") for p in plain[:3]]
        + [case(*p, epilogue="silu") for p in plain[:3]]
        # One array serving both, each design selecting its own.
        + [
            case(*p, epilogue=e, epilogues=("none", "silu"))
            for e in ("none", "silu")
            for p in plain[2:3]
        ]
    )


class Epilogue(StrEnum):
    """The activation each core applies to an output tile it produced."""

    NONE = "none"
    GELU = "gelu"  # tanh approximation, aie2p's in-place gelu_tile_bf16
    SILU = "silu"

    @property
    def mode(self) -> int:
        """The word a core reads to select this epilogue among its array's."""
        return list(Epilogue).index(self)


class GEMV(Operator):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer.

    ``C = A @ B`` as row-blocks of A per column, each column's core calling
    the mv.cc kernel over ``tile_size_input`` rows at a time. ``K`` is
    compiled into the kernel (``-DDIM_K``) and the tiles name it, so it is
    array-tier; the number of rows ``M`` is not, and reaches the core as
    the ``tiles`` value.

    - num_aie_columns: columns to split the rows of A across
    - tile_size_input: rows of A stored on each core per acquire (chunk size of A)
    - tile_size_output: rows of C stored on each core per acquire (chunk size of C)
    """

    test = Testing(_cases, draw=dict(normal=("A", "B")))

    M: int = param()
    K: int = param()
    num_batches: int = param(default=1)
    # Batches per matrix of A: batch ``b`` is multiplied by matrix
    # ``b // repeat``. Grouped-query attention's scores, where each group's
    # keys serve ``n_heads // n_kv_groups`` query heads: the matrix is read
    # once per batch it serves, so no repeated copy is ever materialized.
    repeat: int = param(default=1)
    num_matrices: int = param(default=lambda op: op.num_batches // op.repeat)
    # None: every column the device's shim budget allows that leaves each
    # column a whole number of tiles of M.
    num_aie_columns: int = auto()
    # None: two rows, or one where two would span more than two banks: A is
    # double-buffered beside the whole of B, and at K = 8192 two rows each
    # way would be all of a core's memory.
    tile_size_input: int = auto()
    # None: tile_size_input, and at least two rows: the shim moves C in
    # 4-byte granules. Not a column's rows, which M would set: one array
    # serves every M.
    tile_size_output: int = auto()
    # None picks the widest legal size for K (see validate).
    kernel_vector_size: int = auto(repr=False, array=True)
    epilogue: Epilogue | str = param(default=Epilogue.NONE)
    # The epilogues the array can apply. More than one, and each core reads
    # its design's ``mode``, so designs differing in epilogue share an array.
    epilogues: tuple = param(default=lambda op: (op.epilogue,), array=True)

    # A single batch carries no batch dimension at all, rather than one of
    # extent 1, so an unbatched operator has 2-D shapes. One fifo per column
    # for each of A and C; B, the whole vector, is one fifo every column's
    # core reads, so it takes one shim channel however wide the array.
    A = In(
        OptionalDim(num_matrices),
        M,
        K,
        tile=(tile_size_input, K),
        per=(num_aie_columns,),
        depth=2,
    )
    B = In(OptionalDim(num_batches), K, tile=(K,), depth=1)
    C = Out(
        OptionalDim(num_batches),
        M,
        tile=(tile_size_output,),
        per=(num_aie_columns,),
        depth=2,
    )
    valid = Extent(M)  # M, or fewer rows per call (``A[:n]`` in a graph)
    # Output tiles each column produces per batch: the core's trip count,
    # written once per build, so the array does not depend on M; per call
    # under a bound, read by each core.
    tiles = Value(
        np.int32,
        derive=lambda op: ceildiv(op.valid, op.num_aie_columns * op.tile_size_output),
    )
    batches = Value(np.int32, derive=lambda op: op.num_batches)
    mode = Value(np.int32, derive=lambda op: Epilogue(op.epilogue).mode, optional=True)

    def extent_unit(self, buffer: str) -> int | None:
        # A column takes A in output tiles (several input tiles each) so
        # its rows and C's line up under the round-robin split.
        return self.tile_size_output if buffer == "A" else None

    # Vector widths mv.cc's matvec_vectorized is instantiated at, widest first.
    # Each is a legal aie::vector<bfloat16, r> width; anything narrower than 16
    # is not worth a kernel launch, so a K below 32 is rejected rather than
    # silently run at a width nothing has been tested at.
    _KERNEL_VECTOR_SIZES: ClassVar[tuple[int, ...]] = (64, 32, 16)

    def validate(self):
        if self.repeat < 1 or self.num_batches % self.repeat:
            raise ValueError(
                f"repeat={self.repeat} does not divide num_batches={self.num_batches}"
            )
        self.check_derived("num_matrices")
        tso, tsi = self.tile_size_output, self.tile_size_input
        if tso is not None and tsi is not None and not (tso % tsi == 0 and tso >= tsi):
            raise ValueError("tile_size_output must be a multiple of tile_size_input")
        self._legal_kernel_vector_size()
        self.epilogue = Epilogue(self.epilogue)
        given = {Epilogue(e) for e in self.epilogues}
        self.epilogues = tuple(e for e in Epilogue if e in given)
        if self.epilogue not in self.epilogues:
            raise ValueError(
                f"epilogue {self.epilogue} is not in epilogues "
                f"{tuple(str(e) for e in self.epilogues)}"
            )
        if Epilogue.GELU in self.epilogues and tso is not None and tso % 16 != 0:
            raise ValueError(
                f"gelu epilogue needs tile_size_output % 16 == 0 (got {tso})"
            )

    def _legal_kernel_vector_size(self) -> int:
        """The vector width the matvec kernel is compiled at.

        mv.cc requires ``DIM_K % VEC_SIZE == 0`` and ``DIM_K >= 2 * VEC_SIZE``:
        its inner loop carries a pipelining pragma that assumes at least two
        iterations. Both are static_asserts, so getting this wrong is a C++
        error from inside a kernel build rather than a message a caller can
        read. The second condition is easy to miss: K == VEC_SIZE divides
        evenly and still does not build.

        Left unset, the widest legal width for this K is chosen, so callers do
        not have to know the rule. Set explicitly, the value is checked and the
        reason reported here instead of in Peano's output.
        """
        legal = [
            size
            for size in self._KERNEL_VECTOR_SIZES
            if self.K % size == 0 and self.K >= 2 * size
        ]
        if self.kernel_vector_size is None:
            if not legal:
                raise ValueError(
                    f"K={self.K} has no legal kernel_vector_size: need a width w "
                    f"in {self._KERNEL_VECTOR_SIZES} with K % w == 0 and K >= 2*w. "
                    "K must be an even multiple of at least 16."
                )
            return legal[0]
        if self.kernel_vector_size not in legal:
            raise ValueError(
                f"kernel_vector_size={self.kernel_vector_size} is not legal for "
                f"K={self.K}: the matvec kernel needs K % kernel_vector_size == 0 "
                f"and K >= 2*kernel_vector_size. "
                + (
                    f"Legal here: {legal}."
                    if legal
                    else "No width works for this K; it must be an even multiple "
                    "of at least 16."
                )
            )
        return self.kernel_vector_size

    def resolve(self, dev):
        """Columns default to the most the device's shim budget allows that
        leave each column a whole number of tiles of M; the tiles follow
        from K, not from the device.
        """
        if Epilogue.GELU in self.epilogues and dev.arch is not AIEArch.AIE2p:
            # gelu_tile_bf16 is exported by gelu_aie2p.h alone.
            raise Unresolvable(f"GEMV's gelu epilogue is aie2p-only; got {dev.arch}")
        # Two rows of A per acquire where two fit a bank's worth of L1.
        row_bytes = self.K * np.dtype(bfloat16).itemsize
        rows = self.tile_size_input or (2 if row_bytes <= Target.L1_BANK_BYTES else 1)
        # silu.cc runs whole vector registers over the tile.
        lanes = 32 if dev.arch is AIEArch.AIE2p else 16
        silu = Epilogue.SILU in self.epilogues
        tile = self.tile_size_output or (
            math.lcm(rows, lanes) if silu else max(rows, 2)
        )
        if silu and tile % lanes:
            raise ValueError(
                f"silu epilogue needs tile_size_output % {lanes} == 0 on "
                f"{dev.arch} (got {tile})"
            )
        unit = math.lcm(tile, rows)
        cols = self.resolve_columns(
            dev, self.num_aie_columns, fits=lambda c: self.M % (c * unit) == 0
        )
        return dataclasses.replace(
            self,
            num_aie_columns=cols,
            tile_size_input=rows,
            tile_size_output=tile,
            kernel_vector_size=self._legal_kernel_vector_size(),
        )

    def compatible(self):
        cols = self.num_aie_columns
        rows = self.M // cols
        if self.M % cols:
            raise ValueError(f"M={self.M} does not divide across {cols} columns")
        # We first acquire output rows from the C FIFO, then fill those rows
        # from the A input, so both tiles must divide each column's share.
        for name, tile in (
            ("tile_size_output", self.tile_size_output),
            ("tile_size_input", self.tile_size_input),
        ):
            if tile > rows:
                raise ValueError(f"{name}={tile} exceeds M/num_aie_columns={rows}")
            if rows % tile:
                raise ValueError(
                    f"{name}={tile} does not evenly divide M/num_aie_columns={rows}"
                )

    def array(self, target):
        K, cols = self.K, self.num_aie_columns
        tile_size_input, tile_size_output = self.tile_size_input, self.tile_size_output

        # The kernels are declared and built by one object each. They must be
        # constructed here rather than at import: an ExternalFunction
        # registers itself into a process-global set that CompilableDesign
        # clears when it starts generating, so anything built before that is
        # discarded.
        matvec = linalg.mv(
            tile_size_input,
            K,
            bfloat16,
            bfloat16,
            vectorized=True,
            vec_size=self.kernel_vector_size,
            output_rows=tile_size_output,
        )
        # The epilogue runs over the whole C tile, once the matvec calls have
        # filled it: one call's tile_size_input rows can be narrower than an
        # activation's vector.
        epilogues = self.epilogues
        select = len(epilogues) > 1
        kernels = []
        if Epilogue.GELU in epilogues:
            # gelu.cc's in-place gelu_tile_bf16, which only gelu_aie2p.h
            # exports; it rides in the object the gelu factory builds. A second
            # object, not an archive bundled with the first: each func.func
            # carries its own link_with and aie-assign-core-link-files
            # aggregates them onto the core.
            kernels.append(
                activation.gelu().object_file.bind(
                    "gelu_tile_bf16", [np.int32, self.C.tile]
                )
            )
        if Epilogue.SILU in epilogues:
            kernels.append(activation.silu_sized(tile_size_output))

        A_fifos = [
            ObjectFifo(self.A.tile, name=f"A_L3L1_{i}", depth=self.A.depth)
            for i in range(cols)
        ]
        B_fifo = ObjectFifo(self.B.tile, name="B_L3L1", depth=self.B.depth)
        C_fifos = [
            ObjectFifo(self.C.tile, name=f"C_L1L3_{i}", depth=self.C.depth)
            for i in range(cols)
        ]
        # Per column: the trip count (unless a graph bounds M, when each core
        # reads it from the scratchpad), the batches of a call and, when the
        # array has a choice, the epilogue.
        dynamic = self.uses_value("tiles") and target.image == "elf"
        rtps = [
            Buffer(
                np.ndarray[(3,), np.dtype[np.int32]],
                name=f"rtp_{i}",
                use_write_rtp=True,
            )
            for i in range(cols)
        ]
        barriers = [WorkerRuntimeBarrier() for _ in range(cols)]

        def core_body(A_fifo, B_fifo, C_fifo, matvec, rtp, barrier, *rest):
            rest = iter(rest)
            barrier.wait_for_value(1)
            n = next(rest).read() if dynamic else rtp[0]
            batches = rtp[1]
            mode = rtp[2] if select else epilogues[0].mode
            # The wait leaves the barrier set: release it, or a design sharing
            # this array runs on these values.
            barrier.release_with_value(1)
            gelu = next(rest) if Epilogue.GELU in epilogues else None
            silu = next(rest) if Epilogue.SILU in epilogues else None
            # silu.cc reads and writes through restrict pointers, so its
            # input is a tile of its own.
            acc = next(rest) if silu is not None else None
            for _ in range_(batches):
                b = B_fifo.acquire(1)
                # Each column produces tiles output tiles of tile_size_output
                # rows per batch, tile_size_input rows per kernel call.
                for _ in range_(n):
                    c = C_fifo.acquire(1)
                    out = c
                    if silu is not None:
                        out = (
                            arith.select(mode == Epilogue.SILU.mode, acc.op, c)
                            if select
                            else acc
                        )
                    for j_idx in range_(tile_size_output // tile_size_input):
                        j_i32: Any = index.casts(T.i32(), j_idx)
                        output_row_offset = j_i32 * tile_size_input
                        a = A_fifo.acquire(1)
                        matvec(tile_size_input, output_row_offset, a, b, out)
                        A_fifo.release(1)
                    if gelu is not None:
                        with (
                            if_(mode == Epilogue.GELU.mode) if select else nullcontext()
                        ):
                            gelu(tile_size_output, c)
                    if silu is not None:
                        with (
                            if_(mode == Epilogue.SILU.mode) if select else nullcontext()
                        ):
                            silu(acc, c, tile_size_output)
                    C_fifo.release(1)
                B_fifo.release(1)

        workers = [
            Worker(
                core_body,
                [
                    A_fifos[i].cons(),
                    B_fifo.cons(),
                    C_fifos[i].prod(),
                    matvec,
                    rtps[i],
                    barriers[i],
                    *([self.tiles.param] if dynamic else []),
                    *kernels,
                    *(
                        [Buffer(self.C.tile, name=f"acc_{i}")]
                        if Epilogue.SILU in epilogues
                        else []
                    ),
                ],
            )
            for i in range(cols)
        ]
        self.B.lane(0).bind(B_fifo.prod())
        for i in range(cols):
            self.A.lane(i).bind(A_fifos[i].prod())
            self.C.lane(i).bind(C_fifos[i].cons())
        if not dynamic:
            self.tiles.bind(rtps, 0)
        self.batches.bind(rtps, 1)
        if select:
            self.mode.bind(rtps, 2)
        return workers + barriers

    def sequence(self, rt):
        """The runtime sequence: B, the whole vector, once for every column,
        then A and C as derived: each column's rows of every batch, or,
        under a bound, output tiles round-robin over the columns. A repeated
        GEMV walks the batches in ``_batch_order`` instead.
        """
        if self.repeat > 1:
            self._repeated_sequence(rt)
            return
        vector = TaskGroup()
        rt.fill(self.B.lane(0), self.B, group=vector)
        tg = TaskGroup()
        for slot, tap, size_by in rt.plan(self.A):
            rt.fill(slot, (self.A, tap), group=tg, size_by=size_by)
        for slot, tap, size_by in rt.plan(self.C):
            rt.drain(slot, (self.C, tap), group=tg, wait=True, size_by=size_by)
        tg.finish()
        vector.finish()

    def _batch_order(self) -> list[int]:
        """The batches in the order a repeated GEMV computes them.

        A matrix is re-read, and the shim can re-read only in its outermost
        (iteration) dimension, whose stride alone may be 0: it cannot re-read
        one matrix for consecutive batches inside a walk over the matrices.
        So the walk over every matrix repeats, and pass ``r`` computes batch
        ``m * repeat + r`` of each matrix ``m``. B and C visit the batches in
        the same order; each batch's product is its own, so the order
        changes no output.
        """
        rep, nm = self.repeat, self.num_matrices
        return [m * rep + r for r in range(rep) for m in range(nm)]

    def _walks(self, lane: int) -> dict[str, list[TensorAccessPattern]]:
        """Each of A, B and C's transfers to or from ``lane`` in
        ``_batch_order``: one descriptor that walks every matrix once per
        pass, or, where a run does not factor into one, one per batch.
        """
        M, K, rep, nm = self.M, self.K, self.repeat, self.num_matrices
        rows = M // self.num_aie_columns
        shim = BdLimits.of(self.dev, 0, 0)
        lane_rows = slice(lane * rows, (lane + 1) * rows)
        # Each walk is (pass, matrix, run): A's rows come from the batch's
        # matrix, re-read each pass (stride 0); B's and C's go to the batch
        # itself, batch m * repeat + r of matrix m in pass r.
        A = TensorAccessPattern.full((nm, M, K))
        B = TensorAccessPattern.full((nm, rep, K))
        C = TensorAccessPattern.full((nm, rep, M))
        walks = {
            "A": (self.A, A[:, lane_rows].merge(1).repeat(rep)),
            "B": (self.B, B.permute((1, 0, 2))),
            "C": (self.C, C[:, :, lane_rows].permute((1, 0, 2))),
        }
        out = {}
        for name, (buf, walk) in walks.items():
            halves = shim.factor(walk.sizes[-1], shim.granule(buf.dtype))
            if halves is not None:
                tap = walk.split(2, halves[1])
                if shim.fits(tap, buf.dtype):
                    out[name] = [tap]
                    continue
            out[name] = [walk[b % rep, b // rep] for b in self._batch_order()]
        return out

    def _repeated_sequence(self, rt):
        for buf in (self.A, self.C):
            if buf.bounded is not None:
                raise ValueError(
                    f"GEMV.{buf.name}: a repeated GEMV takes no per-call bound"
                )
        walks = [self._walks(col) for col in range(self.num_aie_columns)]
        vectors = TaskGroup()
        for tap in walks[0]["B"]:
            rt.fill(self.B.lane(0), (self.B, tap), group=vectors)
        tg = TaskGroup()
        for col, w in enumerate(walks):
            for tap in w["A"]:
                rt.fill(self.A.lane(col), (self.A, tap), group=tg)
        for col, w in enumerate(walks):
            for tap in w["C"]:
                rt.drain(self.C.lane(col), (self.C, tap), group=tg, wait=True)
        tg.finish()
        vectors.finish()

    def fold(self, consumer):
        if (
            not isinstance(consumer, UnaryElementwise)
            or consumer.as_epilogue not in Epilogue
            or self.epilogue is not Epilogue.NONE
        ):
            return None
        epilogue = Epilogue(consumer.as_epilogue)
        return dataclasses.replace(
            self, epilogue=epilogue, epilogues=(*self.epilogues, epilogue)
        )

    def on_array(self, other):
        if not isinstance(other, GEMV) or self.epilogue not in other.epilogues:
            return None
        return dataclasses.replace(self, epilogues=other.epilogues)

    def ops(self) -> int:
        return 2 * self.M * self.K * self.num_batches

    def reference(self, A, B):
        """``C = A @ B``, then the epilogue: one product per batch when ``A``
        is ``(batches, M, K)`` and ``B`` ``(batches, K)``, each matrix of
        ``A`` serving ``repeat`` consecutive batches.
        """
        if self.repeat > 1:
            A = np.repeat(A.reshape(-1, *A.shape[-2:]), self.repeat, axis=0)
        # Not linalg.mv's contract: that is one tile's product, and mv_ref's
        # float64 would double the host copy of the LM head's weight. In
        # float32 and rounded once: numpy's matmul would otherwise accumulate
        # in bfloat16, where the AIE kernel's accumulator is f32. einsum has
        # no bfloat16 loop at all, so the batched case reshapes into a matmul.
        a, b = A.astype(np.float32), B.astype(np.float32)
        if A.ndim == 3:
            b = b.reshape(A.shape[0], A.shape[2], 1)
            C = np.matmul(a, b).reshape(A.shape[0], A.shape[1]).astype(A.dtype)
        else:
            C = (a @ b.reshape(A.shape[-1])).astype(A.dtype)
        match self.epilogue:
            case Epilogue.GELU:
                return activation.gelu_ref(C)
            case Epilogue.SILU:
                return activation.silu_ref(C)
        return C

    def tolerance(self) -> Tolerance:
        """The gate GEMV's sweeps hold: C accumulates in f32 and rounds
        once, and an epilogue's tanh approximation adds its own.
        Tighter than linalg.mv's contract, the C++ matmul harness's 0.05
        and 0.5.
        """
        if self.epilogue is Epilogue.GELU:
            return Tolerance.relative(0.06, 2e-2, note="f32 accumulation, then GELU")
        if self.epilogue is Epilogue.SILU:
            return Tolerance.relative(0.08, 0.035, note="f32 accumulation, then SiLU")
        return Tolerance.relative(0.04, 1e-3, note="f32 accumulation, rounded once")
