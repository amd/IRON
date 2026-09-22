# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from dataclasses import field
from typing import ClassVar

import numpy as np
import torch

from iron.common.declare import (
    Incompatible,
    In,
    Operator,
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
from iron.common.utils import DMA_BD_MAX_WRAP

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
    # to every column's own fifo; the sequence fills each one (see GEMV.design).
    a = StreamIn(tile_size_input, K, per=num_aie_columns, depth=2)
    b = StreamIn(K, per=num_aie_columns, depth=1)
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
        func_type = "vectorized" if vectorized else "scalar"
        matvec = target.kernel(
            f"matvec_{func_type}_bf16_bf16",
            [np.int32, np.int32, L1_A_ty, L1_B_ty, L1_C_ty],
            source=target.kernels_dir / "generic" / "mv.cc",
            # mv.cc is a template over both: one source, one object per shape.
            compile_flags=[f"-DDIM_K={K}", f"-DVEC_SIZE={self.kernel_vector_size}"],
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
            # A second object, not an archive bundled with the first: each
            # func.func carries its own link_with and aie-assign-core-link-files
            # aggregates them onto the core.
            gelu_kernel = target.kernel(
                "gelu_tile_bf16",
                [np.int32, L1_C_ty],
                source=target.kernels_dir / "aie2p" / "gelu.cc",
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

    def design(self, rt):
        """The runtime sequence, kept as it was: B once per column in an outer
        group, then A/C per batch, coalesced into one iterated descriptor per
        column when the shim can hold it.
        """
        ov = self.ov
        M, K, nb, cols = self.M, ov.K, self.num_batches, ov.num_aie_columns
        A_elems, B_elems, C_elems = self.A.elements, self.B.elements, self.C.elements

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
        # this keeps GEMV's own (both halves <= 1023 elements, run_lo even) so
        # the instruction stream stays what it was.
        GRAN_ELEMS = 2  # 4-byte shim granularity / 2-byte bf16 element
        MAX_STRIDE = ((1 << 20) - 1) * GRAN_ELEMS

        def split_run(run, lim=DMA_BD_MAX_WRAP, gran=GRAN_ELEMS):
            lo_start = (lim // gran) * gran
            for lo in range(lo_start, 0, -gran):
                if run % lo == 0 and (run // lo) <= lim:
                    return (run // lo, lo)
            return None

        A_run, A_bstride = (M // cols) * K, M * K
        C_run, C_bstride = (M // cols), M
        A_split, C_split = split_run(A_run), split_run(C_run)
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

        if coalesce:
            # Dropping the per-batch drain wait lets the single iterated fill BD
            # run ahead of the core. ObjectFifo lock backpressure keeps that
            # safe: a producer that gets ahead blocks on the buffer lock (worst
            # case a stall, never a corrupting overrun). depth>=2 only buys
            # overlap of fill with compute, so it is a performance guard here.
            assert ov.a.depth >= 2 and ov.c.depth >= 2, (
                "coalesced GEMV wants A/C ObjectFifo depth>=2 for fill/compute overlap"
            )
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
                rt.fill(ov.b[col], (self.B, B_tap), group=tg_b)
            # Coalesced: one iterated BD per column covers all batches (one
            # drain wait per column). Fallback (incl. num_batches==1): the
            # per-batch unroll, one wait per batch. Only the tap and the wait
            # count differ.
            num_waits = 1 if coalesce else nb
            for w in range(num_waits):
                with rt.group() as tg_ac:
                    for col in range(cols):
                        a_tap = A_coalesced[col] if coalesce else A_taps[col][w]
                        rt.fill(ov.a[col], (self.A, a_tap), group=tg_ac)
                    for col in range(cols):
                        c_tap = C_coalesced[col] if coalesce else C_taps[col][w]
                        rt.drain(ov.c[col], (self.C, c_tap), group=tg_ac, wait=True)

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
    if A.dim() == 3:
        return torch.einsum("bmk,bk->bm", A, B.reshape(A.shape[0], A.shape[2]))
    return A @ B.reshape(A.shape[-1])


def gelu_tanh_approx(x):
    """Tanh-approximation GELU, matching aie_kernels/aie2p/gelu.cc.

    0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3))). Computed in float32.
    """
    xf = np.asarray(x, dtype=np.float32)
    inner = 0.79788456 * (xf + 0.044715 * xf**3)
    return 0.5 * xf * (1.0 + np.tanh(inner))
