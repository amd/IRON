# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import math
from typing import Any, ClassVar

import numpy as np
from aie.iron import ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import activation, linalg
from ml_dtypes import bfloat16

from iron.common import (
    Extent,
    In,
    Incompatible,
    Operator,
    Out,
    Value,
    auto,
    optional,
    param,
)
from iron.common.tiling import DMA_BD_MAX_WRAP, Access

_I32 = np.ndarray[(1,), np.dtype[np.int32]]  # type: ignore[misc]


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

    M: int = param()
    K: int = param()
    num_batches: int = param(default=1)
    # None: every column the device's shim budget allows that leaves each
    # column a whole number of tiles of M.
    num_aie_columns: int = auto()
    tile_size_input: int = auto(2)
    tile_size_output: int = auto()  # None: tile_size_input
    # None picks the widest legal size for K (see validate).
    kernel_vector_size: int = auto(repr=False, array=True)
    # Optional fused activation applied to each output tile in the producing core.
    # "none" (default) leaves the output unchanged; "gelu" applies GELU(tanh approx).
    # repr=False keeps operator/artifact names stable for the default path.
    epilogue: str = param(default="none", repr=False, array=True)

    # A single batch carries no batch dimension at all, rather than one of
    # extent 1, so an unbatched operator has 2-D shapes. One fifo per column
    # for each of A, B and C; B is the whole vector, sent to every column's
    # own fifo (see sequence).
    A = In(
        optional(num_batches),
        M,
        K,
        tile=(tile_size_input, K),
        per=(num_aie_columns,),
        depth=2,
    )
    B = In(optional(num_batches), K, tile=(K,), per=(num_aie_columns,), depth=1)
    C = Out(
        optional(num_batches),
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
        derive=lambda op: op.valid // (op.num_aie_columns * op.tile_size_output),
    )

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
        tso = self.tile_size_output
        if tso is not None and not (
            tso % self.tile_size_input == 0 and tso >= self.tile_size_input
        ):
            raise ValueError("tile_size_output must be a multiple of tile_size_input")
        self._legal_kernel_vector_size()
        if self.epilogue not in ("none", "gelu"):
            raise ValueError(
                f"unknown epilogue {self.epilogue!r} (expected 'none' or 'gelu')"
            )
        if self.epilogue == "gelu" and tso is not None and tso % 16 != 0:
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
        leave each column a whole number of tiles of M; the rest follows
        from K and from each other, not from the device.
        """
        tile = self.tile_size_output or self.tile_size_input
        unit = tile * self.tile_size_input // math.gcd(tile, self.tile_size_input)
        cols = self.resolve_columns(
            dev, self.num_aie_columns, fits=lambda c: self.M % (c * unit) == 0
        )
        return dataclasses.replace(
            self,
            num_aie_columns=cols,
            tile_size_output=self.tile_size_output or self.tile_size_input,
            kernel_vector_size=self._legal_kernel_vector_size(),
        )

    def compatible(self):
        cols = self.num_aie_columns
        rows = self.M // cols
        if self.M % cols:
            raise Incompatible(f"M={self.M} does not divide across {cols} columns")
        # We first acquire output rows from the C FIFO, then fill those rows
        # from the A input, so both tiles must divide each column's share.
        for name, tile in (
            ("tile_size_output", self.tile_size_output),
            ("tile_size_input", self.tile_size_input),
        ):
            if tile > rows:
                raise Incompatible(f"{name}={tile} exceeds M/num_aie_columns={rows}")
            if rows % tile:
                raise Incompatible(
                    f"{name}={tile} does not evenly divide M/num_aie_columns={rows}"
                )

    @property
    def name(self) -> str:
        # epilogue is repr=False so the default path keeps a stable name, but the
        # fused variant must not share an artifact name with the plain GEMV of the
        # same shape: both would emit the same .mlir/.xclbin, and in a shared build
        # dir a cached unfused build can then satisfy the fused op.
        base = super().name
        if self.epilogue == "none":
            return base
        return f"{base}_epi{self.epilogue}"

    def array(self, target):
        import aie.dialects.index as index
        from aie.dialects.aie import T

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
        # Optional fused activation over the full tile_size_output C-tile, applied
        # once per tile in core_body (after the matvec inner-loop has filled all
        # rows) rather than per matvec call, whose tile_size_input tile can be
        # smaller than the 16-wide activation vector.
        gelu_kernel = None
        if self.epilogue == "gelu":
            if target.arch != "aie2p":
                raise NotImplementedError(
                    "gemv gelu epilogue is only available on NPU2 (aie2p); "
                    f"current kernel dir is {target.arch!r}"
                )
            # gelu.cc's in-place gelu_tile_bf16, which only aie2p's gelu.cc
            # exports; it rides in the object the gelu factory builds. A second
            # object, not an archive bundled with the first: each func.func
            # carries its own link_with and aie-assign-core-link-files
            # aggregates them onto the core.
            gelu_kernel = activation.gelu().object_file.bind(
                "gelu_tile_bf16", [np.int32, self.C.tile]
            )

        A_fifos = [
            ObjectFifo(self.A.tile, name=f"A_L3L1_{i}", depth=self.A.depth)
            for i in range(cols)
        ]
        B_fifos = [
            ObjectFifo(self.B.tile, name=f"B_L3L1_{i}", depth=self.B.depth)
            for i in range(cols)
        ]
        C_fifos = [
            ObjectFifo(self.C.tile, name=f"C_L1L3_{i}", depth=self.C.depth)
            for i in range(cols)
        ]
        # The trip count: an RTP written once per build, or a scratchpad
        # word each core reads per call when a graph bounds M.
        dynamic = self.uses_value("tiles") and target.image == "elf"
        tiles = (
            [self.tiles.param] * cols
            if dynamic
            else [target.rtp(_I32, name=f"tiles_{i}") for i in range(cols)]
        )
        barriers = [target.barrier() for _ in range(cols)]

        def core_body(A_fifo, B_fifo, C_fifo, matvec, tiles, barrier, gelu_kernel=None):
            barrier.wait_for_value(1)
            n = tiles.read() if dynamic else tiles[0]
            for _ in range_(0xFFFFFFFF):  # batch dim handled as part of this loop
                b = B_fifo.acquire(1)
                # Each column produces tiles output tiles of tile_size_output
                # rows per batch, tile_size_input rows per kernel call.
                for _ in range_(n):
                    c = C_fifo.acquire(1)
                    for j_idx in range_(tile_size_output // tile_size_input):
                        j_i32: Any = index.casts(T.i32(), j_idx)  # pyright: ignore
                        output_row_offset = j_i32 * tile_size_input
                        a = A_fifo.acquire(1)
                        matvec(tile_size_input, output_row_offset, a, b, c)
                        A_fifo.release(1)
                    if gelu_kernel is not None:
                        gelu_kernel(tile_size_output, c)
                    C_fifo.release(1)
                B_fifo.release(1)

        workers = [
            Worker(
                core_body,
                [
                    A_fifos[i].cons(),
                    B_fifos[i].cons(),
                    C_fifos[i].prod(),
                    matvec,
                    tiles[i],
                    barriers[i],
                ]
                + ([gelu_kernel] if self.epilogue == "gelu" else []),
            )
            for i in range(cols)
        ]
        for i in range(cols):
            self.A.lane(i).bind(A_fifos[i].prod())
            self.B.lane(i).bind(B_fifos[i].prod())
            self.C.lane(i).bind(C_fifos[i].cons())
        if not dynamic:
            self.tiles.bind(tiles)
        return workers

    def sequence(self, rt):
        """The runtime sequence: B once per column in an outer
        group, then A/C per batch, coalesced into one iterated descriptor per
        column when the shim can hold it.
        """
        M, K, nb, cols = self.M, self.K, self.num_batches, self.num_aie_columns
        A_elems, B_elems, C_elems = self.A.elements, self.B.elements, self.C.elements
        if self.A.bounded is not None:
            # M bounded per call: B as below, then A and C round-robin over
            # the columns in output tiles, each lane's count patched.
            with rt.group() as tg_b:
                for col in range(cols):
                    rt.fill(
                        self.B.lane(col),
                        Access(B_elems, 0, (1, 1, 1, nb * K), (0, 0, 0, 1)),
                        group=tg_b,
                    )
            with rt.group() as tg:
                for slot, acc, size_by in rt.plan(self.A):
                    rt.fill(slot, (self.A, acc), group=tg, size_by=size_by)
                for slot, acc, size_by in rt.plan(self.C):
                    rt.drain(slot, (self.C, acc), group=tg, wait=True, size_by=size_by)
            return

        # Distribution pattern for the input matrix A: each AIE core gets a
        # contiguous chunk of rows; the shim puts all data on the stream in
        # sequence and the ObjectFifo chunks it into tile_size_input x K tiles.
        A_taps = [
            [
                Access(
                    A_elems,
                    col * (M // cols) * K + batch * M * K,
                    (1, 1, 1, (M // cols) * K),
                    (0, 0, 0, 1),
                )
                for batch in range(nb)
            ]
            for col in range(cols)
        ]
        # Every column gets the entirety of the vector B (all batches in sequence).
        B_tap = Access(B_elems, 0, (1, 1, 1, nb * K), (0, 0, 0, 1))
        # Collection pattern for C: each core writes back its contiguous chunk.
        C_taps = [
            [
                Access(
                    C_elems,
                    col * (M // cols) + batch * M,
                    (1, 1, 1, M // cols),
                    (0, 0, 0, 1),
                )
                for batch in range(nb)
            ]
            for col in range(cols)
        ]

        # Batch coalescing replaces the per-batch unroll with a single iterated
        # BD: within one batch the run is contiguous, the batch stride is the
        # full matrix, and the run is split into [run_hi, run_lo] only to fit
        # the shim's wrap field. iron.common.tiling states the general rules;
        # this keeps GEMV's own (both halves <= 1023 elements, run_lo even).
        GRAN_ELEMS = 2  # 4-byte shim granularity / 2-byte bf16 element
        MAX_STRIDE = ((1 << 20) - 1) * GRAN_ELEMS

        def factor_run(run, lim=DMA_BD_MAX_WRAP, gran=GRAN_ELEMS):
            """``(hi, lo)`` with both at most ``lim`` elements.

            Stricter than :func:`iron.common.tiling.split_run`, whose ``lo``
            may run to ``lim`` granules rather than ``lim`` elements.
            """
            lo_start = (lim // gran) * gran
            for lo in range(lo_start, 0, -gran):
                if run % lo == 0 and (run // lo) <= lim:
                    return (run // lo, lo)
            return None

        A_run, A_bstride = (M // cols) * K, M * K
        C_run, C_bstride = (M // cols), M
        A_split, C_split = factor_run(A_run), factor_run(C_run)
        coalesce = (
            nb > 1
            and A_bstride <= MAX_STRIDE
            and C_bstride <= MAX_STRIDE
            and A_bstride % GRAN_ELEMS == 0
            and C_bstride % GRAN_ELEMS == 0
            and A_split is not None
            and C_split is not None
        )

        def coalesced(elems, col_off, split, bstride):
            run_hi, run_lo = split
            return Access(
                elems, col_off, (1, nb, run_hi, run_lo), (0, bstride, run_lo, 1)
            )

        A_coalesced: list[Access] = []
        C_coalesced: list[Access] = []
        if coalesce:
            # Dropping the per-batch drain wait lets the single iterated fill BD
            # run ahead of the core. ObjectFifo lock backpressure keeps that
            # safe: a producer that gets ahead blocks on the buffer lock (worst
            # case a stall, never a corrupting overrun). A and C are declared
            # at depth 2, which only buys overlap of fill with compute.
            A_coalesced = [
                coalesced(A_elems, col * (M // cols) * K, A_split, A_bstride)
                for col in range(cols)
            ]
            C_coalesced = [
                coalesced(C_elems, col * (M // cols), C_split, C_bstride)
                for col in range(cols)
            ]

        with rt.group() as tg_b:
            for col in range(cols):
                # Simple linear transfer of B, includes all batches in sequence
                rt.fill(self.B.lane(col), B_tap, group=tg_b)
            # Coalesced: one iterated BD per column covers all batches (one
            # drain wait per column). Fallback (incl. num_batches==1): the
            # per-batch unroll, one wait per batch. Only the tap and the wait
            # count differ.
            num_waits = 1 if coalesce else nb
            for w in range(num_waits):
                with rt.group() as tg_ac:
                    for col in range(cols):
                        a_tap = A_coalesced[col] if coalesce else A_taps[col][w]
                        rt.fill(self.A.lane(col), a_tap, group=tg_ac)
                    for col in range(cols):
                        c_tap = C_coalesced[col] if coalesce else C_taps[col][w]
                        rt.drain(self.C.lane(col), c_tap, group=tg_ac, wait=True)

    def reference(self, A, B):
        """CPU reference: (optionally batched) matrix-vector product."""
        return reference(A, B)


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(A, B):
    """CPU reference: matrix-vector product ``C = A @ B`` (ground truth).

    Batched when ``A`` is ``(batches, M, K)`` and ``B`` ``(batches, K)``: one
    product per batch, as the operator's ``num_batches`` runs them.
    """
    # In float32 and rounded once: numpy's matmul would otherwise accumulate
    # in bfloat16, where the AIE kernel's accumulator is f32. einsum has no
    # bfloat16 loop at all, so the batched case reshapes into a matmul.
    a, b = A.astype(np.float32), B.astype(np.float32)
    if A.ndim == 3:
        b = b.reshape(A.shape[0], A.shape[2], 1)
        return np.matmul(a, b).reshape(A.shape[0], A.shape[1]).astype(A.dtype)
    return (a @ b.reshape(A.shape[-1])).astype(A.dtype)


def gelu_tanh_approx(x):
    """Tanh-approximation GELU, matching aie_kernels/aie2p/gelu.cc.

    0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3))). Computed in float32.
    """
    xf = np.asarray(x, dtype=np.float32)
    inner = 0.79788456 * (xf + 0.044715 * xf**3)
    return 0.5 * xf * (1.0 + np.tanh(inner))
