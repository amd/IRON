# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import math
from typing import Any, ClassVar

import aie.dialects.index as index
import numpy as np
from aie.dialects.aie import T
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Buffer,
    ObjectFifo,
    Worker,
    WorkerRuntimeBarrier,
    ceildiv,
)
from aie.iron.controlflow import range_
from aie.iron.device import Device
from aie.iron.kernels import eltwise, linalg
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron import operators as catalog
from iron.common import (
    Divisors,
    Extent,
    Finish,
    In,
    Link,
    Operator,
    Out,
    Prepare,
    Value,
    auto,
    OptionalDim,
    param,
)
from iron.common.design import Target
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
    # ... and num_batches: each batch's B, then its rows, on every lane.
    batched = [
        (256, 128, 1, 1, 256, 4),  # tiny
        (256, 128, 8, 1, 32, 100),  # large num_batches: the size-uncapped dim
        (448, 64, 8, 1, 56, 192),  # a multi-dim run split, and many batches
        (64, 1536, 1, 1, 64, 8),  # large K
        (1026, 64, 1, 1, 2, 2),  # a run that needs an even (granule) split
        (1024, 1024, 1, 1, 64, 2),  # batch stride > 2**20
        (512, 64, 8, 4, 64, 32),  # attention's: several rows, a batch per head
    ]
    # ... and repeat: several batches per matrix of A.
    repeated = [
        (256, 128, 2, 1, 64, 8, 4),  # A re-read for each batch it serves
        (256, 128, 2, 1, 64, 4, 4),  # one matrix for every batch
        (1024, 1024, 1, 1, 64, 4, 2),  # matrix stride > 2**20
        (2048, 64, 8, 4, 256, 32, 4),  # Llama decode's scores: 32 heads, 8 groups
    ]
    # ... and two lanes a column, so both of its input channels carry A.
    laned = [
        (2048, 8192, 1, 1, 1024),
        (8192, 2048, 4, 4, 1024),
        (8192, 2048, 8, 4, 512),
    ]

    def case(M, K, cols, tsi, tso, *, bench=False, **extra):
        kwargs = dict(M=M, K=K, num_aie_columns=cols, tile_size_input=tsi)
        return Case(dict(kwargs, tile_size_output=tso, **extra), bench=bench)

    def finished(M, K, cols, tsi, tso, *chains, **extra):
        # The first chain is the case's own; more share one array.
        steps = [tuple(Link(step(size=M)) for step in c) for c in chains]
        plain = case(M, K, cols, tsi, tso, **extra)
        shared = tuple(steps) if len(steps) > 1 else ()
        names = ["".join(step.__name__ for step in c) or "none" for c in chains]
        label = f"{plain.label}-finish_{names[0]}" + "".join(
            f"-shares_{n}" for n in names[1:]
        )
        return Case(dict(plain.kwargs, finish=steps[0], finishes=shared), id=label)

    def prepared(M, K, cols, tsi, tso, *chains, **extra):
        # Each chain names its steps; the first is the case's own, more share one array.
        steps = [tuple(Link(op) for _, op in c) for c in chains]
        plain = case(M, K, cols, tsi, tso, **extra)
        shared = tuple(steps) if len(steps) > 1 else ()
        names = ["".join(name for name, _ in c) or "none" for c in chains]
        label = f"{plain.label}-prepare_{names[0]}" + "".join(
            f"-shares_{n}" for n in names[1:]
        )
        return Case(dict(plain.kwargs, prepare=steps[0], prepares=shared), id=label)

    def norm(K, weighted=False):
        name = "RMSNormWeighted" if weighted else "RMSNorm"
        return name, catalog.RMSNorm(rows=1, tile_size=K, weighted=weighted)

    # Benched: the large matrices across the whole device, which run well
    # past the dispatch cost.
    widest = dev.cols

    def bench(M, K, cols, *_):
        return cols == widest and M * K >= 2048 * 8192

    return (
        [case(*p, bench=bench(*p)) for p in plain]
        + [case(*p, num_batches=batches) for *p, batches in batched]
        + [case(*p, num_batches=batches, repeat=r) for *p, batches, r in repeated]
        + [case(*p, bench=bench(*p), num_channels=2) for p in laned]
        + [
            case(256, 128, 2, 1, 32, num_channels=2, num_batches=8),
            case(2048, 64, 4, 4, 256, num_channels=2, num_batches=32, repeat=4),
        ]
        # Each core finishing its output tiles.
        + [finished(*p, (catalog.GELU,)) for p in plain[:3]]
        + [finished(*p, (catalog.SiLU,)) for p in plain[:3]]
        + [finished(*laned[1], (catalog.SiLU,), num_channels=2)]
        # One array serving both, each design selecting its own.
        + [
            finished(*plain[2], (), (catalog.SiLU,)),
            finished(*plain[2], (catalog.SiLU,), ()),
        ]
        # Each core preparing B, the step producing it folded in: a K of
        # 8192 leaves no room in L1 for the prepared line, 4096 weighted the
        # least.
        + [
            prepared(*p, (norm(p[1], weighted),))
            for p in (plain[0], plain[2], plain[4], (2048, 4096, 8, 2, 256))
            for weighted in (False, True)
        ]
        + [
            prepared(*laned[1], (norm(2048, weighted),), num_channels=2)
            for weighted in (False, True)
        ]
        + [
            prepared(*plain[2], (), (norm(2048),)),
            prepared(*plain[2], (norm(2048),), ()),
        ]
    )


class GEMV(Operator):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer.

    ``C = A @ B`` as row-blocks of A per lane, each lane's core calling
    the mv.cc kernel over ``tile_size_input`` rows at a time. ``K`` is
    compiled into the kernel (``-DDIM_K``) and the tiles name it, so it is
    array-tier; the number of rows ``M`` is not, and reaches the core as
    the ``tiles`` value. B rides each lane's A stream ahead of its rows, so
    every input channel of a column can carry A.

    - num_aie_columns: columns to split the rows of A across
    - num_channels: lanes per column, each its own A stream and core
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
    # None: one.
    num_channels: int = auto()
    # None: two rows, or one where two would span more than two banks: A is
    # double-buffered beside the whole of B, and at K = 8192 two rows each
    # way would be all of a core's memory.
    tile_size_input: int = auto(
        domain=Divisors(
            of=lambda op: op.M,
            cap=lambda op, dev: dev.core_memory_bytes
            // (op.A.depth * op.K * np.dtype(bfloat16).itemsize),
        )
    )
    # None: tile_size_input, and at least two rows: the shim moves C in
    # 4-byte granules. Not a column's rows, which M would set: one array
    # serves every M.
    tile_size_output: int = auto(
        domain=Divisors(of=lambda op: op.M, step=lambda op: op.tile_size_input, span=3)
    )
    # None picks the widest legal size for K (see validate).
    kernel_vector_size: int = auto(repr=False, array=True)

    # A single batch carries no batch dimension at all, rather than one of
    # extent 1, so an unbatched operator has 2-D shapes. One fifo per lane
    # for each of A and C; B has no stream of its own (see sequence). Each
    # core prepares B, so the step producing it folds into them. The
    # prologue's and a finish's inputs ride A: a tile of each after B's, or
    # after an output tile's rows.
    A = In(
        OptionalDim(num_matrices),
        M,
        K,
        tile=(tile_size_input, K),
        per=(num_aie_columns, num_channels),
        depth=2,
        feed=True,
    )
    B = In(OptionalDim(num_batches), K, prepare=True)
    C = Out(
        OptionalDim(num_batches),
        M,
        tile=(tile_size_output,),
        per=(num_aie_columns, num_channels),
        depth=2,
        finish=True,
    )
    valid = Extent(M)  # M, or fewer rows per call (``A[:n]`` in a graph)
    # Output tiles each lane produces per batch: the core's trip count,
    # written once per build, so the array does not depend on M; per call
    # under a bound, read by each core.
    tiles = Value(
        np.int32,
        derive=lambda op: ceildiv(
            op.valid, op.num_aie_columns * op.num_channels * op.tile_size_output
        ),
    )
    batches = Value(np.int32, derive=lambda op: op.num_batches)

    def extent_unit(self, buffer: str) -> int | None:
        # A lane takes A in output tiles (several input tiles each) so
        # its rows and C's line up under the round-robin split.
        return self.tile_size_output if buffer == "A" else None

    # Vector widths mv.cc's matvec_vectorized is instantiated at, widest first.
    # Each is a legal aie::vector<bfloat16, r> width; anything narrower than 16
    # is not worth a kernel launch, so a K below 32 is rejected rather than
    # silently run at a width nothing has been tested at.
    _KERNEL_VECTOR_SIZES: ClassVar[tuple[int, ...]] = (64, 32, 16)
    # bf16 elements in one of eltwise.passthrough's 64-byte vectors.
    _COPY_ELEMENTS: ClassVar[int] = 32
    # A batched sequence's tasks outnumber a shim's BD ids, so the compiler
    # recycles finished tasks' ids. Safe: C's drains go out before the fills
    # feeding them, so no task waits on a push issued after it.
    aiecc_flags: ClassVar[tuple[str, ...]] = ("--reclaim-runtime-bds",)

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
        if self.K % self._COPY_ELEMENTS:
            raise ValueError(
                f"K={self.K}: each core copies B out of its A stream in "
                f"{self._COPY_ELEMENTS}-element vectors, so K must be a multiple "
                f"of {self._COPY_ELEMENTS}"
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
        leave each lane a whole number of tiles of M, at one lane per column
        unless ``num_channels`` says more; the tiles follow from K, and from
        the line each finish of the array runs at.
        """
        # Two rows of A per acquire where two fit a bank's worth of L1.
        row_bytes = self.K * np.dtype(bfloat16).itemsize
        rows = self.tile_size_input or (2 if row_bytes <= Target.L1_BANK_BYTES else 1)
        channels = self.num_channels or 1
        if self.tile_size_output is None and self.finish_inputs:
            # A finish input's tile, re-read to fill one of A's riding it,
            # costs A's stream the less the more rows it is: a lane's
            # share, or the most that fits a descriptor's re-reads.
            cols = self.resolve_columns(
                dev,
                self.num_aie_columns,
                channels,
                fits=lambda c: self.M % (c * channels * rows) == 0,
            )
            share, carried = self.M // (cols * channels), rows * self.K
            reads = 1 << dev.get_dma_bd_iter_bits(0, 0)
            tile = self.finish_line(
                dev,
                [
                    n
                    for n in range(share, 0, -rows)
                    if share % n == 0 and carried % n == 0 and carried // n <= reads
                ],
            )
        else:
            tile = self.tile_size_output or self.finish_line(
                dev, (max(rows, 2), *(math.lcm(rows, 2**i) for i in range(2, 8)))
            )
            unit = math.lcm(tile, rows)
            cols = self.resolve_columns(
                dev,
                self.num_aie_columns,
                channels,
                fits=lambda c: self.M % (c * channels * unit) == 0,
            )
        new = dataclasses.replace(
            self,
            num_aie_columns=cols,
            num_channels=channels,
            tile_size_input=rows,
            tile_size_output=tile,
            kernel_vector_size=self._legal_kernel_vector_size(),
        )
        # A core holds A's tiles (which carry B and each prologue and finish
        # input), B's line, C's tiles, a scratch line per kind of chain it
        # applies, and the default stack, which no elementwise kernel exceeds.
        item = np.dtype(bfloat16).itemsize
        line, out = self.K * item, new.tile_size_output * item
        held = (
            new.A.depth * new.tile_size_input * line
            + line
            + new.C.depth * out
            + line * any(new.prepares or (new.prepare,))
            + out * any(new.finishes or (new.finish,))
            + dev.default_core_stack_bytes
        )
        if held > dev.core_memory_bytes:
            raise ValueError(
                f"K={self.K}, tile_size_input={new.tile_size_input}: a core "
                f"holds {held} bytes, past its {dev.core_memory_bytes}"
            )
        return new

    def compatible(self):
        lanes = self.num_aie_columns * self.num_channels
        rows = self.M // lanes
        if self.M % lanes:
            raise ValueError(f"M={self.M} does not divide across {lanes} lanes")
        # We first acquire output rows from the C FIFO, then fill those rows
        # from the A input, so both tiles must divide each lane's share.
        for name, tile in (
            ("tile_size_output", self.tile_size_output),
            ("tile_size_input", self.tile_size_input),
        ):
            if tile > rows:
                raise ValueError(f"{name}={tile} exceeds M/lanes={rows}")
            if rows % tile:
                raise ValueError(f"{name}={tile} does not evenly divide M/lanes={rows}")

    def array(self, target):
        K, lanes = self.K, self.num_aie_columns * self.num_channels
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
        vector = np.ndarray[(K,), np.dtype[bfloat16]]
        # A lossless copy of the head tile's first row, B, as 16-bit words.
        copy = eltwise.passthrough(K, np.int16).object_file.bind(
            "passThroughLine", [self.A.tile, vector, np.int32]
        )
        # The finish runs over the whole C tile, once the matvec calls have
        # filled it: one call's tile_size_input rows can be narrower than a
        # step's vector.
        finish = Finish(self, lanes)
        prepare = Prepare(self, lanes)

        A_fifos = [
            ObjectFifo(self.A.tile, name=f"A_L3L1_{i}", depth=self.A.depth)
            for i in range(lanes)
        ]
        C_fifos = [
            ObjectFifo(self.C.tile, name=f"C_L1L3_{i}", depth=self.C.depth)
            for i in range(lanes)
        ]
        vectors = [Buffer(vector, name=f"B_{i}") for i in range(lanes)]
        # Per lane: the trip count (unless a graph bounds M, when each core
        # reads it from the scratchpad) and the batches of a call.
        dynamic = self.uses_value("tiles") and target.image == "elf"
        rtps = [
            Buffer(
                np.ndarray[(2,), np.dtype[np.int32]],
                name=f"rtp_{i}",
                use_write_rtp=True,
            )
            for i in range(lanes)
        ]
        barriers = [WorkerRuntimeBarrier() for _ in range(lanes)]

        def core_body(A_fifo, C_fifo, b, matvec, copy, rtp, barrier, *rest):
            barrier.wait_for_value(1)
            n = rest[0].read() if dynamic else rtp[0]
            rest = rest[1:] if dynamic else rest
            prepared, rest = rest[: prepare.arity], rest[prepare.arity :]
            batches = rtp[1]
            mode_p = prepare.read(prepared)
            mode = finish.read(rest)
            # The wait leaves the barrier set: release it, or a design sharing
            # this array runs on these values.
            barrier.release_with_value(1)
            for _ in range_(batches):
                # The batch's head tile carries B; the prologue's inputs,
                # then the rows of A follow it.
                head = A_fifo.acquire(1)
                copy(head, b, K)
                A_fifo.release(1)
                line = prepare.apply(prepared, mode_p, b, A_fifo)
                # Each lane produces tiles output tiles of tile_size_output
                # rows per batch, tile_size_input rows per kernel call.
                for _ in range_(n):
                    c = C_fifo.acquire(1)
                    out = finish.target(rest, mode, c)
                    for j_idx in range_(tile_size_output // tile_size_input):
                        j_i32: Any = index.casts(T.i32(), j_idx)
                        output_row_offset = j_i32 * tile_size_input
                        a = A_fifo.acquire(1)
                        matvec(tile_size_input, output_row_offset, a, line, out)
                        A_fifo.release(1)
                    finish.apply(rest, mode, c, A_fifo)
                    C_fifo.release(1)

        workers = [
            Worker(
                core_body,
                [
                    A_fifos[i].cons(),
                    C_fifos[i].prod(),
                    vectors[i],
                    matvec,
                    copy,
                    rtps[i],
                    barriers[i],
                    *([self.tiles.param] if dynamic else []),
                    *prepare.args(i),
                    *finish.args(i),
                ],
            )
            for i in range(lanes)
        ]
        for i in range(lanes):
            self.A.lane(i).bind(A_fifos[i].prod())
            self.C.lane(i).bind(C_fifos[i].cons())
        if not dynamic:
            self.tiles.bind(rtps, 0)
        self.batches.bind(rtps, 1)
        prepare.bind()
        finish.bind()
        return workers + barriers

    def sequence(self, rt):
        """The runtime sequence: each lane's stream carries, per batch, B's
        head tile, a tile of each prologue input, and then the batch's rows
        of A, as derived (each lane's rows, or, under a bound, output tiles
        round-robin over the lanes) and narrowed to matrix ``b // repeat``,
        a tile of each finish input after each output tile's rows. C drains
        as derived, issued first: a core whose C could not drain would stop
        taking A while its queue waits on it. Every transfer is unmanaged,
        so the compiler meters each queue and recycles descriptors however
        many batches.
        """
        if self.repeat > 1:
            for buf in (self.A, self.C):
                if buf.bounded is not None:
                    raise ValueError(
                        f"GEMV.{buf.name}: a repeated GEMV takes no per-call bound"
                    )
        M, K, tsi = self.M, self.K, self.tile_size_input
        drains = [
            rt.drain(slot, (self.C, tap), wait=True, size_by=size_by, managed=False)
            for slot, tap, size_by in rt.plan(self.C)
        ]
        rows = rt.plan(self.A)
        if self.num_matrices > 1 and self.A.bounded is None:
            parts = TensorAccessPattern.full((M, K)).partition(len(rows), 0)
            rows = [
                (
                    slot,
                    TensorAccessPattern(
                        self.A.shape, part.offset, part.sizes, part.strides
                    ),
                    None,
                )
                for (slot, _, _), part in zip(rows, parts, strict=True)
            ]
        elif self.num_matrices > 1:
            # The round-robin pattern walks every matrix in its outermost
            # dimension.
            rows = [
                (
                    slot,
                    TensorAccessPattern(
                        tap.tensor_dims,
                        tap.offset,
                        [1, *tap.sizes[1:]],
                        [0, *tap.strides[1:]],
                    ),
                    size_by,
                )
                for slot, tap, size_by in rows
            ]
        # Each lane's share of a batch's C, which a finish's inputs ride A for.
        share = M // len(rows)
        output = TensorAccessPattern.full(self.C.shape)
        for b in range(self.num_batches):
            # B's row repeated over a whole A tile, in the iteration
            # dimension, the one whose stride may be 0; so is each prologue
            # input's.
            head = TensorAccessPattern(
                self.B.shape, b * K, [tsi, 1, 1, K], [0, 0, 0, 1]
            )
            line = TensorAccessPattern((K,), 0, [tsi, 1, 1, K], [0, 0, 0, 1])
            for slot, tap, size_by in rows:
                rt.fill(slot, (self.B, head), managed=False)
                for extra in self.prepare_inputs:
                    rt.fill(slot, (extra, line), managed=False)
                matrix = TensorAccessPattern(
                    tap.tensor_dims,
                    tap.offset + b // self.repeat * M * K,
                    tap.sizes,
                    tap.strides,
                )
                finishing = None
                if self.finish_inputs:
                    lane_rows = slice(slot.index * share, (slot.index + 1) * share)
                    finishing = (
                        output[b, lane_rows]
                        if self.num_batches > 1
                        else output[lane_rows]
                    )
                rt.fill(
                    slot,
                    (self.A, matrix),
                    size_by=size_by,
                    managed=False,
                    finishing=finishing,
                )
        for task in drains:
            task.await_()

    def ops(self) -> int:
        return 2 * self.M * self.K * self.num_batches

    def reference(self, A, B, *extras):
        """``C = A @ B``, B through its prologue and C through its finish,
        ``extras`` their steps' other inputs in turn: one product per batch
        when ``A`` is ``(batches, M, K)`` and ``B`` ``(batches, K)``, each
        matrix of ``A`` serving ``repeat`` consecutive batches.
        """
        op = self.resolved()
        prologue = len(op.prepare_inputs)
        if op.prepare:
            B = Prepare(op).reference(B, *extras[:prologue])
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
        if op.finish:
            return Finish(op).reference(C, *extras[prologue:])
        return C

    def tolerance(self) -> Tolerance:
        """The gate GEMV's sweeps hold: C accumulates in f32 and rounds
        once, a prologue widens that by its steps' gates carried through
        the product, and a finish carries it through its steps' own gates.
        Tighter than linalg.mv's contract, the C++ matmul harness's 0.05
        and 0.5.
        """
        if self.finish:
            return Finish(self).tolerance()
        if self.prepare:
            return Prepare(self).tolerance()
        return Tolerance.relative(0.04, 1e-3, note="f32 accumulation, rounded once")
