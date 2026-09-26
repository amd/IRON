# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from dataclasses import field
from typing import ClassVar

import numpy as np
from aie.iron.kernels import activation, linalg
from ml_dtypes import bfloat16

from iron.common.declare import (
    Contraction,
    Semantics,
    BoundBuffer,
    Incompatible,
    In,
    Operator,
    Order,
    Out,
    Overlay,
    StreamIn,
    StreamOut,
    dim,
    operator,
    optional,
    tunable,
)
from iron.common.tiling import Access
from iron.common.tiling import DMA_BD_MAX_WRAP

_GRAN_ELEMS = 2  # 4-byte shim granularity / 2-byte bf16 element
_MAX_STRIDE = ((1 << 20) - 1) * _GRAN_ELEMS


def _factor_run(run, lim=DMA_BD_MAX_WRAP, gran=_GRAN_ELEMS):
    """``(hi, lo)`` with both at most ``lim`` elements.

    Stricter than :func:`iron.common.tiling.split_run`, whose ``lo`` may run
    to ``lim`` granules rather than ``lim`` elements.
    """
    lo_start = (lim // gran) * gran
    for lo in range(lo_start, 0, -gran):
        if run % lo == 0 and (run // lo) <= lim:
            return (run // lo, lo)
    return None


# --------------------------------------------------------------------------
# The overlay: what configures the array.
# --------------------------------------------------------------------------


@operator
class GEMVOverlay(Overlay):
    """The array configuration for ``C = A @ B``: row-blocks of A per column.

    Calls into the mv.cc kernel, which computes ``tile_size_input`` output rows
    per call. ``K`` is baked into the kernel (``-DDIM_K``), so it is overlay-tier;
    the number of rows ``M`` is not, and lives on :class:`GEMV`.

    - num_aie_columns: columns to split the rows of A across
    - tile_size_input: rows of A stored on each core per acquire (chunk size of A)
    - tile_size_output: rows of C stored on each core per acquire (chunk size of C)
    """

    K: int = dim()
    num_aie_columns: int = tunable(1)
    tile_size_input: int = tunable(2)
    tile_size_output: int | None = tunable(None)
    # None picks the widest legal size for K (see validate).
    kernel_vector_size: int | None = tunable(None, repr=False)
    # Optional fused activation applied to each output tile in the producing core.
    # "none" (default) leaves the output unchanged; "gelu" applies GELU(tanh approx).
    # repr=False keeps operator/artifact names stable for the default path.
    epilogue: str = field(default="none", repr=False)

    # One fifo per column for each of A, B and C. B is the whole vector, sent
    # to every column's own fifo.
    a = StreamIn(tile_size_input, K, per=num_aie_columns, depth=2)
    b = StreamIn(K, per=num_aie_columns, replicate=True, depth=1)
    c = StreamOut(tile_size_output, per=num_aie_columns, depth=2)

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

        mv.cc requires ``DIM_K % VEC_SIZE == 0`` *and* ``DIM_K >= 2 * VEC_SIZE``
        -- its inner loop carries a pipelining pragma that assumes at least two
        iterations, and both are static_asserts, so getting this wrong is a C++
        error from inside a kernel build rather than anything a caller can read.
        The second condition is the one that is easy to miss: K == VEC_SIZE
        divides evenly and still does not build.

        Left unset, the widest legal width for this K is chosen, so callers do
        not have to know the rule. Set explicitly, the value is checked and the
        reason is spelled out here instead of in Peano's output.
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

    def tuning(self, dev) -> "GEMVOverlay":
        # Device-independent today: the tunables that are None are derived from
        # K and from each other, not from the device. (The column count is not
        # defaulted from the device; every caller sets it.)
        return dataclasses.replace(
            self,
            tile_size_output=self.tile_size_output or self.tile_size_input,
            kernel_vector_size=self._legal_kernel_vector_size(),
        )

    def semantics(self) -> Semantics:
        """K is reduced inside one core, so a released C tile is final."""
        return Contraction(final_at_release=True)

    def design(self, target):
        from aie.dialects.aie import T
        import aie.dialects.index as index
        from aie.helpers.dialects.scf import _for as range_
        from aie.iron import ObjectFifo, Worker

        K = self.K
        num_aie_columns = self.num_aie_columns
        tile_size_input = self.tile_size_input
        tile_size_output = self.tile_size_output
        vectorized = True
        L1_A_ty = self.a.tile
        L1_B_ty = self.b.tile
        L1_C_ty = self.c.tile

        # The kernels are declared and built by one object each. Constructing
        # them here rather than at import is required, not stylistic: an
        # ExternalFunction registers itself into a process-global set that
        # CompilableDesign clears when it starts generating, so anything built
        # before that is discarded.
        matvec = linalg.mv(
            tile_size_input,
            K,
            bfloat16,
            bfloat16,
            vectorized=vectorized,
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
                "gelu_tile_bf16", [np.int32, L1_C_ty]
            )

        A_L3L1_fifos = [
            ObjectFifo(L1_A_ty, name=f"A_L3L1_{i}", depth=self.a.depth)
            for i in range(num_aie_columns)
        ]
        B_L3L1_fifos = [
            ObjectFifo(L1_B_ty, name=f"B_L3L1_{i}", depth=self.b.depth)
            for i in range(num_aie_columns)
        ]
        C_L1L3_fifos = [
            ObjectFifo(L1_C_ty, name=f"C_L1L3_{i}", depth=self.c.depth)
            for i in range(num_aie_columns)
        ]

        def core_body(A_L3L1_fifo, B_L3L1_fifo, C_L1L3_fifo, matvec, gelu_kernel=None):
            one_idx = index.constant(1)
            for _ in range_(0xFFFFFFFF):  # batch dim handled as part of this loop
                b = B_L3L1_fifo.acquire(1)
                # The kernel function computes m output rows; each core is
                # responsible for (M/num_aie_columns) output rows, so we call the
                # kernel (M/num_aie_columns)/m times.
                for i_idx in range_(self._rows_per_column // tile_size_output):
                    c = C_L1L3_fifo.acquire(1)
                    i_i32 = index.casts(T.i32(), i_idx)
                    for j_idx in range_(tile_size_output // tile_size_input):
                        j_i32 = index.casts(T.i32(), j_idx)
                        output_row_offset = j_i32 * tile_size_input
                        a = A_L3L1_fifo.acquire(1)
                        matvec(tile_size_input, output_row_offset, a, b, c)
                        A_L3L1_fifo.release(1)
                    if gelu_kernel is not None:
                        gelu_kernel(tile_size_output, c)
                    C_L1L3_fifo.release(1)
                B_L3L1_fifo.release(1)

        workers = [
            Worker(
                core_body,
                [
                    A_L3L1_fifos[i].cons(),
                    B_L3L1_fifos[i].cons(),
                    C_L1L3_fifos[i].prod(),
                    matvec,
                ]
                + ([gelu_kernel] if self.epilogue == "gelu" else []),
            )
            for i in range(num_aie_columns)
        ]
        for i in range(num_aie_columns):
            self.a[i].bind(A_L3L1_fifos[i].prod())
            self.b[i].bind(B_L3L1_fifos[i].prod())
            self.c[i].bind(C_L1L3_fifos[i].cons())
        return workers

    # The core's inner trip count still depends on the extent M, through
    # _rows_per_column, which GEMV.design sets before the overlay's design runs.
    # That makes this overlay extent-dependent, against the reuse discipline
    # in OPERATOR_MODEL_PLAN.md §3; it is kept so the object stays
    # byte-identical to today's, and moves to a Resident in step 2.
    _rows_per_column: int = field(default=0, init=False, repr=False, compare=False)


# --------------------------------------------------------------------------
# The operator: the host ABI, declared against the overlay.
# --------------------------------------------------------------------------


@operator
class GEMV(Operator[GEMVOverlay]):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer"""

    M: int = dim()
    num_batches: int = dim(1)

    # A single batch carries no batch dimension at all, rather than one of
    # extent 1, so the unbatched shapes stay exactly as they were.
    A = In(optional(num_batches), M, GEMVOverlay.K, to=GEMVOverlay.a)  # matrix
    B = In(optional(num_batches), GEMVOverlay.K, to=GEMVOverlay.b)  # vector
    C = Out(optional(num_batches), M, from_=GEMVOverlay.c)  # output

    def compatible(self):
        ov = self.ov
        rows = self.M // ov.num_aie_columns
        if self.M % ov.num_aie_columns:
            raise Incompatible(
                f"M={self.M} does not divide across {ov.num_aie_columns} columns"
            )
        # We first acquire output rows from the C FIFO, then fill those rows
        # from the A input, so both tiles must divide each column's share.
        for name, tile in (
            ("tile_size_output", ov.tile_size_output),
            ("tile_size_input", ov.tile_size_input),
        ):
            if tile > rows:
                raise Incompatible(f"{name}={tile} exceeds M/num_aie_columns={rows}")
            if rows % tile:
                raise Incompatible(
                    f"{name}={tile} does not evenly divide M/num_aie_columns={rows}"
                )
        ov._rows_per_column = rows

    @property
    def name(self) -> str:
        # epilogue is repr=False so the default path keeps a stable name, but the
        # fused variant must not share an artifact name with the plain GEMV of the
        # same shape: both would emit the same .mlir/.xclbin, and in a shared build
        # dir a cached unfused build can then satisfy the fused op.
        base = super().name
        if self.ov.epilogue == "none":
            return base
        return f"{base}_epi{self.ov.epilogue}"

    # -- the runtime sequence --------------------------------------------------

    def _batch_split(self) -> tuple[tuple[int, int], tuple[int, int]] | None:
        """A's and C's ``(run_hi, run_lo)`` when every batch goes out as one
        iterated descriptor per column, else ``None`` (one per batch).

        Within one batch a column's run is contiguous and the batch stride is
        the full matrix; the run is split in two only to fit the shim's wrap
        field. :mod:`iron.common.tiling` states the general rules; this keeps
        GEMV's own (both halves at most 1023 elements, ``run_lo`` even) so the
        instruction stream stays what it was. A and C coalesce together or
        not at all, since they share the per-batch waits.
        """
        nb, M, K, cols = self.num_batches, self.M, self.ov.K, self.ov.num_aie_columns
        if nb == 1:
            return None
        a_split = _factor_run((M // cols) * K)
        c_split = _factor_run(M // cols)
        strides_fit = all(s <= _MAX_STRIDE and s % _GRAN_ELEMS == 0 for s in (M * K, M))
        if a_split is None or c_split is None or not strides_fit:
            return None
        return a_split, c_split

    def order(self, buffer: BoundBuffer) -> Order:
        """A and C: each column's contiguous rows, one descriptor per batch or
        every batch in one iterated descriptor (:meth:`_batch_split`). B: the
        derived order of a ``replicate`` stream, the whole vector to every
        column."""
        if buffer is self.B:
            return super().order(buffer)
        ov = self.ov
        M, nb, cols = self.M, self.num_batches, ov.num_aie_columns
        width = ov.K if buffer is self.A else 1
        stream = ov.a if buffer is self.A else ov.c
        run, n = (M // cols) * width, buffer.elements
        split = self._batch_split()
        if split is None:
            return Order(
                stream,
                tuple(
                    tuple(
                        Access(
                            n,
                            col * run + batch * M * width,
                            (1, 1, 1, run),
                            (0, 0, 0, 1),
                        )
                        for batch in range(nb)
                    )
                    for col in range(cols)
                ),
            )
        run_hi, run_lo = split[0] if buffer is self.A else split[1]
        return Order(
            stream,
            tuple(
                (
                    Access(
                        n, col * run, (1, nb, run_hi, run_lo), (0, M * width, run_lo, 1)
                    ),
                )
                for col in range(cols)
            ),
        )

    def design(self, rt):
        """B once per column in an outer group, then A and C in one group per
        batch, or in one group for all of them when the batches coalesce."""
        ov = self.ov
        cols = ov.num_aie_columns
        a, b, c = self.order(self.A), self.order(self.B), self.order(self.C)
        if self._batch_split() is not None:
            # Dropping the per-batch drain wait lets the single iterated fill BD
            # run ahead of the core. ObjectFifo lock backpressure keeps that
            # safe: a producer that gets ahead blocks on the buffer lock (worst
            # case a stall, never a corrupting overrun). depth>=2 only buys
            # overlap of fill with compute, so it is a performance guard here.
            assert (
                ov.a.depth >= 2 and ov.c.depth >= 2
            ), "coalesced GEMV wants A/C ObjectFifo depth>=2 for fill/compute overlap"
        with rt.group() as tg_b:
            for col in range(cols):
                for tap in b[col]:
                    rt.fill(ov.b[col], (self.B, tap), group=tg_b)
            for w in range(len(a[0])):
                with rt.group() as tg_ac:
                    for col in range(cols):
                        rt.fill(ov.a[col], (self.A, a[col][w]), group=tg_ac)
                    for col in range(cols):
                        rt.drain(ov.c[col], (self.C, c[col][w]), group=tg_ac, wait=True)

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
