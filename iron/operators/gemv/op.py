# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
import aie.utils as aie_utils
from iron.common.device_utils import get_kernel_dir
import numpy as np
from ml_dtypes import bfloat16
import aie.dialects.index as index
from aie.dialects.aie import T
from aie.helpers.dialects.scf import _for as range_
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker
import torch


@dataclass
class GEMV(MLIROperator):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer"""

    M: int
    K: int
    num_aie_columns: int = 1
    tile_size_input: int = 2
    tile_size_output: int | None = None
    num_batches: int = 1
    # None picks the widest legal size for K (see _resolve_kernel_vector_size).
    kernel_vector_size: int | None = field(default=None, repr=False)
    # Optional fused activation applied to each output tile in the producing core.
    # "none" (default) leaves the output unchanged; "gelu" applies GELU(tanh approx).
    # repr=False keeps operator/artifact names stable for the default path.
    epilogue: str = field(default="none", repr=False)
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_aie_columns": "col",
        "tile_size_input": "tsi",
        "tile_size_output": "tso",
        "num_batches": "batch",
    }

    def __post_init__(self):
        if self.tile_size_output is None:
            self.tile_size_output = self.tile_size_input

        if not (
            self.tile_size_output % self.tile_size_input == 0
            and self.tile_size_output >= self.tile_size_input
        ):
            raise ValueError("tile_size_output must be a multiple of tile_size_input")
        self.kernel_vector_size = self._resolve_kernel_vector_size()
        if self.epilogue not in ("none", "gelu"):
            raise ValueError(
                f"unknown epilogue {self.epilogue!r} (expected 'none' or 'gelu')"
            )
        if self.epilogue == "gelu" and self.tile_size_output % 16 != 0:
            raise ValueError(
                f"gelu epilogue needs tile_size_output % 16 == 0 (got {self.tile_size_output})"
            )

        MLIROperator.__init__(self, context=self.context)

    # Vector widths mv.cc's matvec_vectorized is instantiated at, widest first.
    # Each is a legal aie::vector<bfloat16, r> width; anything narrower than 16
    # is not worth a kernel launch, so a K below 32 is rejected rather than
    # silently run at a width nothing has been tested at.
    _KERNEL_VECTOR_SIZES: ClassVar[tuple[int, ...]] = (64, 32, 16)

    def _resolve_kernel_vector_size(self) -> int:
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

    @property
    def name(self) -> str:
        # epilogue is repr=False so the default path keeps a stable name, but the fused
        # variant must not share an artifact name with the plain GEMV of the same shape:
        # both would emit the same .mlir/.xclbin, and in a shared build dir a cached unfused
        # build can then satisfy the fused op (running the raw matvec with no activation).
        base = super().name
        if self.epilogue == "none":
            return base
        return f"{base}_epi{self.epilogue}"

    @property
    def kernel_object(self):
        # With the gelu epilogue the core also links the gelu kernel, so the object becomes an
        # archive of (matvec, gelu); the plain matvec stays a single object.
        if self.epilogue == "gelu":
            return f"gemv_{self.K}k_{self.kernel_vector_size}vs_gelu_kernels.a"
        return f"gemv_{self.K}k_{self.kernel_vector_size}vs.o"

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                fn=my_matvec,
                bind_from=self,
            ),
        )

    def get_kernel_artifacts(self):
        matvec_obj = KernelObjectArtifact(
            f"gemv_{self.K}k_{self.kernel_vector_size}vs.o",
            dependencies=[
                SourceArtifact(self.context.kernels_dir / "generic" / "mv.cc")
            ],
            extra_flags=[
                f"-DDIM_K={self.K}",
                f"-DVEC_SIZE={self.kernel_vector_size}",
            ],
        )
        if self.epilogue == "gelu":
            # The gelu kernel lives in aie2p/gelu.cc, so the fused epilogue is NPU2-only.
            if get_kernel_dir() != "aie2p":
                raise NotImplementedError(
                    "gemv gelu epilogue is only available on NPU2 (aie2p); "
                    f"current kernel dir is {get_kernel_dir()!r}"
                )
            gelu_obj = KernelObjectArtifact(
                "gelu.o",
                dependencies=[
                    SourceArtifact(self.context.kernels_dir / "aie2p" / "gelu.cc")
                ],
            )
            return [
                KernelArchiveArtifact(
                    self.kernel_object, dependencies=[matvec_obj, gelu_obj]
                )
            ]
        return [matvec_obj]

    @staticmethod
    def arg_spec(M, K, num_batches=1):
        # A single batch carries no batch dimension at all, rather than one of
        # extent 1, so the unbatched shapes stay exactly as they were.
        batch_dim = (num_batches,) if num_batches > 1 else ()
        return [
            AIERuntimeArgSpec("in", batch_dim + (M, K)),  # matrix
            AIERuntimeArgSpec("in", batch_dim + (K,)),  # vector
            AIERuntimeArgSpec("out", batch_dim + (M,)),  # output
        ]

    def reference(self, A, B):
        """CPU reference: (optionally batched) matrix-vector product."""
        return reference(A, B)


# --------------------------------------------------------------------------
# The MLIR this operator generates.
# --------------------------------------------------------------------------

"""
Matrix-vector design

Calls into the mv.cc kernel code. That kernel computes `tile_size_input` output rows per call.


 - num_aie_columns: Number of AIE columns to split work across
 - M: number of rows in the matrix
 - K: number of columns in the matrix == number of rows in the vector
 - tile_size_input: number of input rows stored on each AIE core == chunk size for data movement of input A
 - tile_size_output: number of output rows stored on each AIE core == chunk size for data movement of output C
 - num_batches: number of iterations of this mat-vec to perform on contiguous matrices and vectors in memory (results concatenated)
"""


def my_matvec(
    dev,
    num_aie_columns,
    M,
    K,
    tile_size_input,
    tile_size_output=None,
    num_batches=1,
    kernel_object="mv.o",
    func_prefix="",
    verbose=False,
    epilogue="none",
):
    if tile_size_output is None:
        tile_size_output = tile_size_input

    if verbose:
        print(f"Device: {dev}")
        print(f"Matrix dimensions: M={M}, K={K}")
        print(
            f"Tiling: tile_size_input={tile_size_input}, tile_size_output={tile_size_output}"
        )
        print(f"Columns: {num_aie_columns}")

    # The reason for the following requirement is because we first acquire output rows from the C FIFO, then fill those acquiring rows of the A input.
    assert (
        tile_size_output % tile_size_input == 0 and tile_size_output >= tile_size_input
    ), "tile_size_output must be a multiple of tile_size_input"
    assert (
        tile_size_output <= M // num_aie_columns
    ), "tile_size_output must be less than or equal to M/num_aie_columns"
    assert (
        M // num_aie_columns
    ) % tile_size_output == 0, "tile_size_output must evenly divide M/num_aie_columns"
    assert (
        tile_size_input <= M // num_aie_columns
    ), "tile_size_input must be less than or equal to M/num_aie_columns"
    assert (
        M // num_aie_columns
    ) % tile_size_input == 0, "tile_size_input must evenly divide M/num_aie_columns"

    vectorized = True
    dtype_in = np.dtype[bfloat16]
    dtype_in_str = "bf16"
    dtype_out = np.dtype[bfloat16]
    dtype_out_str = "bf16"

    assert M % num_aie_columns == 0

    L1_A_ty = np.ndarray[
        (
            tile_size_input,
            K,
        ),
        dtype_in,
    ]
    L1_B_ty = np.ndarray[(K,), dtype_in]
    L1_C_ty = np.ndarray[(tile_size_output,), dtype_out]
    L3_A_ty = np.ndarray[
        (num_batches * M * K,),
        dtype_in,
    ]
    L3_B_ty = np.ndarray[(num_batches * K,), dtype_in]
    L3_C_ty = np.ndarray[(num_batches * M,), dtype_out]

    func_type = "vectorized" if vectorized else "scalar"
    matvec = Kernel(
        f"{func_prefix}matvec_{func_type}_{dtype_in_str}_{dtype_out_str}",
        f"{func_prefix}{kernel_object}",
        [np.int32, np.int32, L1_A_ty, L1_B_ty, L1_C_ty],
    )
    # Optional fused activation over the full tile_size_output C-tile, applied once per tile in core_body
    # (after the matvec inner-loop has filled all rows) rather than per matvec call, whose tile_size_input
    # tile can be smaller than the 16-wide activation vector.
    assert epilogue in ("none", "gelu")
    gelu_kernel = None
    if epilogue == "gelu":
        assert (
            tile_size_output % 16 == 0
        ), f"gelu epilogue needs tile_size_output % 16 == 0 (got {tile_size_output})"
        gelu_kernel = Kernel(
            f"{func_prefix}gelu_tile_bf16",
            f"{func_prefix}{kernel_object}",
            [np.int32, L1_C_ty],
        )

    A_L3L1_fifos = [
        ObjectFifo(L1_A_ty, name=f"A_L3L1_{i}", depth=2) for i in range(num_aie_columns)
    ]
    B_L3L1_fifos = [
        ObjectFifo(L1_B_ty, name=f"B_L3L1_{i}", depth=1) for i in range(num_aie_columns)
    ]
    C_L1L3_fifos = [
        ObjectFifo(L1_C_ty, name=f"C_L1L3_{i}", depth=2) for i in range(num_aie_columns)
    ]

    def core_body(A_L3L1_fifo, B_L3L1_fifo, C_L1L3_fifo, matvec, gelu_kernel=None):
        one_idx = index.constant(1)
        for _ in range_(0xFFFFFFFF):  # batch dim handled as part of this loop
            b = B_L3L1_fifo.acquire(1)
            # The kernel function computes m output rows; each core is responsible for (M/num_aie_columns) output rows, so we need to call the kernel (M/num_aie_columns)/m times.
            for i_idx in range_(M // tile_size_output // num_aie_columns):
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
            + ([gelu_kernel] if epilogue == "gelu" else []),
        )
        for i in range(num_aie_columns)
    ]

    # Distribution pattern for the input matrix A: each AIE core gets a contiguous chunk of rows.
    # The input matrix in DDR is MxK-sized (row-major); each core processes (M/num_aie_columns)xK-sized matrices in chunks of mxK-sized tiles.
    # The chunking into mxK-sized tiles happens in the ObjectFIFO; the shim puts all data on the stream in sequence.
    A_taps = [
        [
            TensorAccessPattern(
                tensor_dims=L3_A_ty.__args__[0],
                offset=col * (M // num_aie_columns) * K + batch * M * K,
                sizes=[1, 1, 1, (M // num_aie_columns) * K],
                strides=[0, 0, 0, 1],
            )
            for batch in range(num_batches)
        ]
        for col in range(num_aie_columns)
    ]

    # Every column gets the entirety of the vector B.
    # This design assumes that all of B fits on the cores.
    B_tap = TensorAccessPattern(
        tensor_dims=L3_B_ty.__args__[0],
        offset=0,
        sizes=[1, 1, 1, num_batches * K],
        strides=[0, 0, 0, 1],
    )

    # Collection pattern for the output vector C: each AIE core writes back its contiguous chunk of rows.
    C_taps = [
        [
            TensorAccessPattern(
                tensor_dims=L3_C_ty.__args__[0],
                offset=col * (M // num_aie_columns) + batch * M,
                sizes=[1, 1, 1, (M // num_aie_columns)],
                strides=[0, 0, 0, 1],
            )
            for batch in range(num_batches)
        ]
        for col in range(num_aie_columns)
    ]

    # Batch coalescing replaces the per-batch unroll with a single iterated BD.
    #
    # Within one batch the run is contiguous (A_run = (M//num_aie_columns)*K elements).
    # The batch stride is the full matrix (A_bstride = M*K), so for num_aie_columns>1 each column
    # gathers its own slice out of every batch with a gap in between.
    #
    # The contiguous run is then split into two wrap dims [run_hi, run_lo] ONLY to fit
    # the AIE shim's 10-bit (1023) wrap-size cap.
    #
    # FIXME: pull these shim BD bounds from the MLIR-AIE target model rather than
    # hard-coding them; they live in verifyStridesWraps in
    # https://github.com/Xilinx/mlir-aie/blob/main/lib/Dialect/AIEX/IR/AIEXDialect.cpp
    MAX_WRAP = 1023
    GRAN_ELEMS = 2  # 4-byte shim granularity / 2-byte bf16 element
    # The 20-bit shim BD step field counts address granules, not elements, so the
    # bound converts: an element-unit bound is 2x too strict for bf16.
    MAX_STRIDE = ((1 << 20) - 1) * GRAN_ELEMS

    def split_run(run, lim=MAX_WRAP, gran=GRAN_ELEMS):
        """Factor a contiguous run into (hi, lo), both <= lim and lo a multiple of gran
        (the address-granularity-aligned inner size), lo maximal. None if no such
        split exists (caller then falls back to the per-batch path)."""
        lo_start = (lim // gran) * gran
        for lo in range(lo_start, 0, -gran):
            if run % lo == 0 and (run // lo) <= lim:
                return (run // lo, lo)
        return None

    A_run, A_bstride = (M // num_aie_columns) * K, M * K
    C_run, C_bstride = (M // num_aie_columns), M
    A_split, C_split = split_run(A_run), split_run(C_run)
    coalesce = (
        num_batches > 1
        and A_bstride <= MAX_STRIDE
        and C_bstride <= MAX_STRIDE
        and A_bstride % GRAN_ELEMS == 0
        and C_bstride % GRAN_ELEMS == 0
        and A_split is not None
        and C_split is not None
    )

    def coalesced_tap(L3_ty, col_off, split, bstride):
        run_hi, run_lo = split
        return TensorAccessPattern(
            tensor_dims=L3_ty.__args__[0],
            offset=col_off,
            sizes=[1, num_batches, run_hi, run_lo],
            strides=[0, bstride, run_lo, 1],
        )

    if coalesce:
        # Dropping the per-batch drain wait lets the single iterated fill BD run ahead of
        # the core. ObjectFifo lock backpressure keeps that safe: a producer that gets
        # ahead BLOCKS on the buffer lock (worst case a stall, never a corrupting
        # overrun). depth>=2 only buys OVERLAP of fill with compute, so it is a
        # performance guard here, not a correctness requirement (depth==1 is correct but
        # fully serial).
        assert all(f.depth >= 2 for f in A_L3L1_fifos) and all(
            f.depth >= 2 for f in C_L1L3_fifos
        ), "coalesced GEMV wants A/C ObjectFifo depth>=2 for fill/compute overlap"
        A_taps_coalesced = [
            coalesced_tap(L3_A_ty, col * (M // num_aie_columns) * K, A_split, A_bstride)
            for col in range(num_aie_columns)
        ]
        C_taps_coalesced = [
            coalesced_tap(L3_C_ty, col * (M // num_aie_columns), C_split, C_bstride)
            for col in range(num_aie_columns)
        ]

    def sequence(A, B, C, B_L3L1_fifos_prods, A_L3L1_fifos_prods, C_L1L3_fifos_conss):
        tg_b = TaskGroup()
        for col in range(num_aie_columns):
            # Simple linear transfer of B, includes all batches in sequence
            B_L3L1_fifos_prods[col].fill(B, B_tap, group=tg_b)
        # Coalesced: one iterated BD per column covers all batches (num_waits==1, a
        # single drain wait for the whole column). Fallback (incl. num_batches==1): the
        # stock per-batch unroll (num_waits==num_batches, one wait per batch). The fills
        # and drains are otherwise identical; only the TAP and the wait count differ.
        num_waits = 1 if coalesce else num_batches
        for w in range(num_waits):
            tg_ac = TaskGroup()
            for col in range(num_aie_columns):
                a_tap = A_taps_coalesced[col] if coalesce else A_taps[col][w]
                A_L3L1_fifos_prods[col].fill(A, a_tap, group=tg_ac)
            for col in range(num_aie_columns):
                c_tap = C_taps_coalesced[col] if coalesce else C_taps[col][w]
                C_L1L3_fifos_conss[col].drain(
                    C,
                    c_tap,
                    group=tg_ac,
                    wait=True,
                )
            tg_ac.finish()
        tg_b.finish()

    rt = Runtime(
        sequence,
        [
            L3_A_ty,
            L3_B_ty,
            L3_C_ty,
            [of.prod() for of in B_L3L1_fifos],
            [of.prod() for of in A_L3L1_fifos],
            [of.cons() for of in C_L1L3_fifos],
        ],
    )
    return Program(dev, rt, workers=workers).resolve_program()


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(A, B):
    """CPU reference: matrix-vector product ``C = A @ B`` (ground truth)."""
    return A @ B


def generate_golden_reference(
    M=128, K=128, seed=42
):  # Defaults are tile-aligned minimums; tests always pass explicit values
    """
    Generate golden reference data for GEMV (General Matrix-Vector Multiplication).

    Parameters:
        M: Number of rows of matrix A
        K: Number of columns of matrix A (equals vector B length)
        seed: Random seed

    Returns:
        dict: Contains 'A' (matrix), 'B' (vector), 'C' (output vector)
    """
    torch.manual_seed(seed)

    # Generate golden inputs
    val_range = 4
    A = torch.randn(M, K, dtype=torch.bfloat16) * val_range
    B = torch.randn(K, dtype=torch.bfloat16) * val_range

    # Generate golden outputs
    C = reference(A, B)

    return {
        "A": A,
        "B": B,
        "C": C,
    }


def generate_golden_reference_batched(M=128, K=128, num_batches=2, seed=42):
    """
    Generate golden reference data for a batched GEMV (num_batches independent
    matrix-vector products stacked contiguously, matching the GEMV op layout).

    Parameters:
        M: Number of rows of each matrix A
        K: Number of columns of each matrix A (equals vector B length)
        num_batches: Number of independent GEMVs
        seed: Random seed

    Returns:
        dict: Contains 'A' (matrices), 'B' (vectors), 'C' (output vectors)
    """
    torch.manual_seed(seed)
    val_range = 4
    A = torch.randn(num_batches, M, K, dtype=torch.bfloat16) * val_range
    B = torch.randn(num_batches, K, dtype=torch.bfloat16) * val_range
    C = torch.empty(num_batches, M, dtype=torch.bfloat16)
    for b in range(num_batches):
        C[b] = A[b] @ B[b]
    return {"A": A, "B": B, "C": C}


def gelu_tanh_approx(x):
    """Tanh-approximation GELU, matching aie_kernels/aie2p/gelu.cc.

    0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3))). Computed in float32.
    """
    xf = np.asarray(x, dtype=np.float32)
    inner = 0.79788456 * (xf + 0.044715 * xf**3)
    return 0.5 * xf * (1.0 + np.tanh(inner))
