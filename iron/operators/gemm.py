# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from enum import StrEnum
from typing import Any

import numpy as np
from aie.dialects.aie import AIEArch
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, In, ObjectFifo, Out, TaskGroup, Worker, ceildiv, kernels
from aie.iron.controlflow import if_, range_
from aie.iron.device import (
    NPU1,
    NPU2,
    AnyComputeTile,
    AnyMemTile,
    Device,
    NPU1Col1,
    NPU1Col2,
    Tile,
)
from aie.utils.verify import Tolerance
from aie.utils.compile.jit.params import (
    Select,
    divisors,
    param,
    per_call,
    tunable,
    widths,
)
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Precision, Rtp, Unresolvable
from iron.common.testing import Case, Testing

# fmt: off
#   M,     K,     N, columns, b_col_maj, c_col_maj,   m,   k,   n
_REGULAR = [
    (2048,  2048,  2048,       1,     False,     False,  64,  64,  64),
    (2048,  2048,  2048,       2,      True,     False,  64,  64,  64),
    (2048,  2048,  2048,       8,      True,      True,  64,  64,  64),
    ( 384,  1536,  1792,       4,      True,     False,  32,  48,  64),
    (1792,   896,  1152,       8,     False,      True,  64,  32,  48),
    ( 896,  1792,   640,       8,     False,      True,  32,  64,  80),
    ( 192,   384,    64,       4,      True,      True,  48,  96,  16),
    # M short of four core rows of 16 (EmbeddingGemma 2's audio conv).
    (  32,  1152,  2048,       4,      True,      True,  16,  64,  64),
]
_EXTENSIVE = [
    (2048,  2048,  2048,       8,     False,     False,  32,  32, 128),
    (2048,  2048,  2048,       8,      True,     False, 128,  32,  32),
    # Many N tiles, a long K loop, one K tile, and both.
    (2048,  2048,  8192,       2,      True,     False,  64,  64,  64),
    (2048,  8192,  2048,       2,      True,     False,  64,  64,  64),
    (2048,    64,  2048,       2,      True,     False,  64,  64,  64),
    (2048,    64,  8192,       2,      True,     False,  64,  64,  64),
    (2048,  2048,  2048,       2,     False,      True,   8,  16,  32),
    # C's row stride past the shim BD's 20-bit step: a drain per row-block.
    (1024,  2560, 10240,       8,     False,     False,  64,  64,  64),
]
# fmt: on


def _cases(cls, dev: Device):
    # aie2's mm kernels block m by 4 r (mm_aie2.h): no 8-row tile there.
    min_tile_m = 16 if dev.arch is AIEArch.AIE2 else 1
    out = []
    for rows, extensive in ((_REGULAR, False), (_EXTENSIVE, True)):
        for M, K, N, cols, b_col_maj, c_col_maj, m, k, n in rows:
            if m < min_tile_m:
                continue
            kwargs = dict(M=M, K=K, N=N, num_aie_columns=cols, tile_m=m, tile_k=k)
            kwargs.update(tile_n=n, b_col_maj=b_col_maj, c_col_maj=c_col_maj)
            kwargs.update(precision=Precision.HIGHEST)
            lower = c_col_maj and not extensive
            out.append(Case(kwargs, extensive=extensive, lower=lower))
    # MEDIUM's bfp16 inputs, C rounded to bf16 between K tiles.
    out.append(
        Case(dict(M=2048, K=2048, N=2048, b_col_maj=True), bench=True, lower=True)
    )
    # An f32 C at the default 64-wide tiles overflows a core's memory.
    f32 = dict(M=512, K=256, N=512, output_dtype=np.float32, tile_m=32, tile_k=32)
    out.append(Case(dict(f32, tile_n=32), id="f32_out", lower=True))
    # The placement the tuner tries beside the default.
    kwargs = dict(M=2048, K=2048, N=2048, num_aie_columns=2, b_col_maj=True)
    out.append(Case(dict(kwargs, placement=GEMMPlacement.TILES), extensive=True))
    return out


# A core's stack, and the depth of each core-side fifo of A, B and C.
STACK_BYTES = 0xD00
FIFO_DEPTH = 2


class GEMMPlacement(StrEnum):
    """The tiles GEMM's array pins; aiecc's placer takes the rest. The shim
    ends stay pinned in both: unpinned, a large b_col_maj GEMM piles too many
    active buffer descriptors onto one shim tile. The tuner tries both.
    """

    SHIMS = "shims"
    TILES = "tiles"  # and each core and memtile in its stream's column


class GEMM(Operator):
    """AIE-accelerated General Matrix Multiplication (GEMM) layer.

    ``C = A @ B``, tiled m x k x n: A is broadcast across columns and split
    across rows of cores, B split across columns and broadcast across rows,
    C joined across rows and split across columns.

    Every GEMM but ``F.linear``'s weight GEMM (``flm.ProjectionGEMM``) is
    this one: Precision.HIGHEST, an activation times an activation,
    convolutions, integer types and f32 output.
    """

    test = Testing(_cases, draw=lambda op: dict(normal=(op.A,)))

    M: int = param()
    K: int = param()
    N: int = param()
    # None: the widest of 64, 32, 16, 8 that splits M and the m block divides.
    tile_m: int = tunable(
        domain=lambda op, dev, t: divisors(
            t, of=op.M // op.n_aie_rows, step=op.mac_block(dev)[0]
        ),
    )
    # Searched at HIGHEST alone: below it C rounds to bf16 after every K
    # tile, so tile_k changes the result.
    tile_k: int = tunable(
        default=64,
        domain=lambda op, dev, t: (
            divisors(t, of=op.K, step=op.mac_block(dev)[1])
            if op.precision == Precision.HIGHEST
            else ()
        ),
    )
    tile_n: int = tunable(
        default=64,
        domain=lambda op, dev, t: divisors(t, of=op.N, step=op.mac_block(dev)[2]),
    )
    # None: the most columns the shim budget allows that split N into tiles.
    num_aie_columns: int = tunable(domain=widths)
    placement: GEMMPlacement = tunable(
        default=GEMMPlacement.SHIMS, domain=GEMMPlacement
    )
    b_col_maj: bool = param(default=False, array=True)
    c_col_maj: bool = param(default=False, array=True)
    precision: Precision = tunable(default=Precision.MEDIUM, domain=Precision)
    input_dtype: Any = param(default=bfloat16, repr=False)
    output_dtype: Any = param(default=bfloat16, repr=False)
    # Filled by resolve.
    n_aie_rows: int = tunable(repr=False, init=False)
    n_shim_mem_a: int = tunable(repr=False, init=False)
    a_l2: int = tunable(repr=False, init=False)
    b_l2: int = tunable(repr=False, init=False)
    c_l2: int = tunable(repr=False, init=False)

    A = In(M, K, dtype=input_dtype, obj_shape=(a_l2,), per=(n_shim_mem_a,))
    B = In(
        Select(b_col_maj, (N, K), (K, N)),
        dtype=input_dtype,
        obj_shape=(b_l2,),
        per=(num_aie_columns,),
    )
    C = Out(
        Select(c_col_maj, (N, M), (M, N)),
        dtype=output_dtype,
        obj_shape=(c_l2,),
        per=(num_aie_columns,),
    )
    # A bound limits the compute, not the DMAs: A's pattern fills all four BD dims.
    valid = per_call(bounds=M)
    # The last K tile zeroes A's columns and B's rows past the bound.
    valid_k = per_call(bounds=K)
    # Reduction steps per output tile, and output tiles per core.
    k_div_k = per_call(derive=lambda op: op.K // op.tile_k)
    n_tiles = per_call(
        derive=lambda op: (op.M // op.mem_tile_m_c) * (op.N // op.mem_tile_n),
    )
    # Under a bound: the row blocks it covers, and the column tiles of each.
    row_blocks_valid = per_call(derive=lambda op: ceildiv(op.valid, op.mem_tile_m_c))
    col_tiles = per_call(derive=lambda op: op.N // op.mem_tile_n)
    k_valid = per_call(derive=lambda op: op.valid_k)

    def extent_unit(self, buffer: str) -> int:
        return 0  # nothing is shortened: the cores bound their compute

    @property
    def n_a_tiles_per_shim(self) -> int:
        c, rows = self.num_aie_columns, self.n_aie_rows
        return rows // c if c < rows else 1

    @property
    def mem_tile_m_a(self) -> int:
        return self.tile_m * self.n_a_tiles_per_shim

    @property
    def mem_tile_m_c(self) -> int:
        return self.tile_m * self.n_aie_rows

    @property
    def mem_tile_n(self) -> int:
        return self.tile_n * self.num_aie_columns

    def mac_block(self, dev) -> tuple[int, int, int]:
        """What `tile_m`, `tile_k` and `tile_n` must each be a multiple of:
        mm.cc's r x s x t blocks, two in m and n (four in m on aie2).

        Args:
            dev: The device the kernel is built for, or None for aie2p's
                geometry.
        """
        r, s, t = kernels.mm.mac_dims(
            self.input_dtype,
            self.output_dtype,
            device=dev,
            arch=None if dev is not None else "aie2p",
            emulate_bf16_mmul_with_bfp16=self.precision == Precision.MEDIUM,
        )
        aie2 = dev is not None and dev.arch is AIEArch.AIE2
        return (4 if aie2 else 2) * r, s, 2 * t

    def validate(self) -> None:
        # aie2p's geometry: no device is resolved yet, and npu1's is looser.
        min_tile_m, min_tile_k, min_tile_n = self.mac_block(None)
        if self.tile_m is not None and self.tile_m % min_tile_m != 0:
            raise ValueError(
                f"GEMM: tile_m ({self.tile_m}) must be a multiple of {min_tile_m} "
                f"(aie_kernels/linalg/mm_aie2p.h requires m % (2*r) == 0)"
            )
        if self.tile_k % min_tile_k != 0:
            raise ValueError(
                f"GEMM: tile_k ({self.tile_k}) must be a multiple of {min_tile_k} "
                f"(aie_kernels/linalg/mm_aie2p.h requires k % s == 0)"
            )
        if self.tile_n % min_tile_n != 0:
            raise ValueError(
                f"GEMM: tile_n ({self.tile_n}) must be a multiple of {min_tile_n} "
                f"(aie_kernels/linalg/mm_aie2p.h requires n % (2*t) == 0)"
            )
        din, dout = np.dtype(self.input_dtype), np.dtype(self.output_dtype)
        if np.issubdtype(din, np.integer) != np.issubdtype(dout, np.integer):
            raise ValueError(
                f"GEMM: input_dtype ({din}) and output_dtype ({dout}) must both be "
                "integer or both be float"
            )
        if dout.itemsize < din.itemsize:
            raise ValueError(
                f"GEMM: output_dtype ({dout}) must be at least as wide as input_dtype ({din})"
            )
        # Checked at construction where no tunable is needed; N waits for the columns.
        if self.K % self.tile_k != 0:
            raise ValueError(f"GEMM: K ({self.K}) must be a multiple of {self.tile_k}")
        rows, tile_m = self.n_aie_rows, self.tile_m
        if not rows and self.dev:
            rows, tile_m = self._auto_tiling(self.dev)
        tile_m = tile_m or min_tile_m
        if rows and self.M % (tile_m * rows) != 0:
            raise ValueError(
                f"GEMM: M ({self.M}) must be a multiple of {tile_m * rows}: C is "
                f"tiled into (m * n_aie_rows, n)-sized blocks"
            )

    def _auto_tiling(self, dev) -> tuple[int, int]:
        """The rows of ``dev``'s cores C is split over, and ``tile_m``."""
        block, _, _ = self.mac_block(dev)
        rows = len(dev.core_rows)
        widths = [self.tile_m] if self.tile_m else [64, 32, 16, 8]
        return next(
            (
                (r, m)
                for r in (rows >> i for i in range(rows.bit_length()))
                for m in widths
                if m % block == 0 and self.M % (m * r) == 0
            ),
            (rows, self.tile_m or block),
        )

    def held(self, dev, tile_m: int) -> int:
        """Core memory a core of ``dev`` holds at ``tile_m``."""
        m, k, n = tile_m, self.tile_k, self.tile_n
        din = np.dtype(self.input_dtype).itemsize
        dout = np.dtype(self.output_dtype).itemsize
        wider = self.replace(tile_m=m).array_config().wider_accumulator
        c = m * n * (dout + 4 if wider else FIFO_DEPTH * dout)
        return FIFO_DEPTH * (m * k + k * n) * din + c + STACK_BYTES

    def resolve(self, dev):
        if dev is None:
            raise Unresolvable(
                "GEMM: the rows of cores are the device's; none is bound"
            )
        rows = len(dev.core_rows)
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            fits=lambda c: self.N % (self.tile_n * c) == 0
            and (c >= rows or rows % c == 0),
        )
        rows, tile_m = self._auto_tiling(dev)
        block, _, _ = self.mac_block(dev)
        # An open tile_m narrows until a core holds its tiles.
        while (
            self.tile_m is None
            and tile_m // 2 % block == 0
            and self.held(dev, tile_m) > dev.core_memory_bytes
        ):
            tile_m //= 2
        new = self.replace(tile_m=tile_m, num_aie_columns=cols, n_aie_rows=rows)
        held = new.held(dev, tile_m)
        if held > dev.core_memory_bytes:
            raise ValueError(
                f"GEMM: tile_m={new.tile_m}, tile_k={self.tile_k}, "
                f"tile_n={self.tile_n}: a core holds {held} bytes, past its "
                f"{dev.core_memory_bytes}"
            )
        return new.replace(
            n_shim_mem_a=min(cols, new.n_aie_rows),
            a_l2=new.mem_tile_m_a * self.tile_k,
            b_l2=self.tile_k * self.tile_n,
            c_l2=new.mem_tile_m_c * self.tile_n,
        )

    def compatible(self) -> None:
        if self.N % self.mem_tile_n != 0:
            raise ValueError(
                f"GEMM: N ({self.N}) must be a multiple of {self.mem_tile_n}: B is "
                f"tiled into (k, n * num_aie_columns)-sized blocks"
            )
        if self.M % self.mem_tile_m_a != 0:
            raise ValueError(
                f"GEMM: M ({self.M}) must be a multiple of {self.mem_tile_m_a}: A is "
                "tiled into (tile_m * n_a_tiles_per_shim, k)-sized blocks"
            )
        cols, rows = self.num_aie_columns, self.n_aie_rows
        if cols < rows and rows % cols:
            raise ValueError(
                f"GEMM: {cols} columns do not divide the {rows} rows of cores "
                f"among them, each shim carrying A to as many"
            )

    def array_device(self):
        if self.dev.arch is AIEArch.AIE2:
            return {1: NPU1Col1, 2: NPU1Col2, 4: NPU1}[self.num_aie_columns]()
        return NPU2()

    class Array(Operator.Array):
        @property
        def wider_accumulator(self) -> bool:
            """Whether ``build()`` and ``GEMM.held()`` build HIGHEST's f32
            buffer for a bf16 C's partial sums, beside C's own.
            """
            return self.precision == Precision.HIGHEST and (
                np.dtype(self.output_dtype) == np.dtype(bfloat16)
            )

        def matmul(self):
            """The m x k x n kernel each core runs."""
            return kernels.linalg.mm(
                self.tile_m,
                self.tile_k,
                self.tile_n,
                input_dtype=self.input_dtype,
                # HIGHEST accumulates in f32 in L1, so the matmul's C is f32.
                output_dtype=(
                    np.float32 if self.wider_accumulator else self.output_dtype
                ),
                b_col_maj=self.b_col_maj,
                c_col_maj=self.c_col_maj,
                emulate_bf16_mmul_with_bfp16=self.precision == Precision.MEDIUM,
                round_conv_even=True,
            )

        def build(self) -> Built:
            m, k, n = self.tile_m, self.tile_k, self.tile_n
            n_aie_cols = self.num_aie_columns
            n_aie_rows = self.n_aie_rows
            pinned = self.placement is GEMMPlacement.TILES
            a_cols = [2 * i if n_aie_cols == 8 else i for i in range(self.n_shim_mem_a)]
            n_A_tiles_per_shim = (
                n_aie_rows // n_aie_cols if n_aie_cols < n_aie_rows else 1
            )
            input_dtype, output_dtype = self.input_dtype, self.output_dtype
            wider = self.wider_accumulator

            A_l2_ty = self.A.obj_type
            B_l2_ty = self.B.obj_type
            C_l2_ty = self.C.obj_type
            A_l1_ty = np.ndarray[(m, k), np.dtype[input_dtype]]
            B_l1_ty = np.ndarray[(k, n), np.dtype[input_dtype]]
            C_l1_ty = np.ndarray[(m * n,), np.dtype[output_dtype]]

            dtype_acc = np.float32 if wider else output_dtype
            matmul_kernel = self.matmul()
            streams = matmul_kernel.stream_dims
            zero_kernel = kernels.zero(m * n, dtype_acc)
            convert_copy_kernel = None
            if wider:
                fifo_depth_out = 1  # the f32 accumulator is the other buffer
                convert_copy_kernel = kernels.datamovement.convert_copy(m * n)
            else:
                fifo_depth_out = FIFO_DEPTH

            A_l3l2_fifos: list[Any] = [None] * self.n_shim_mem_a
            A_l2l1_fifos: list[Any] = [None] * n_aie_rows
            B_l3l2_fifos: list[Any] = [None] * n_aie_cols
            B_l2l1_fifos: list[Any] = [None] * n_aie_cols
            C_l1l2_fifos: list[list[Any]] = [
                [None] * n_aie_cols for _ in range(n_aie_rows)
            ]
            C_l2l3_fifos: list[Any] = [None] * n_aie_cols

            bounded = self.valid.in_scratchpad
            k_bounded = self.valid_k.per_call
            read = [self.k_div_k, self.n_tiles]
            if bounded:
                read += [self.row_blocks_valid, self.col_tiles]
            if k_bounded:
                read.append(self.k_valid)
            rtps = [Rtp(read) for _ in range(n_aie_rows * n_aie_cols)]

            for i in range(self.n_shim_mem_a):
                A_l3l2_fifos[i] = ObjectFifo(A_l2_ty, depth=FIFO_DEPTH)
                # Fewer A shims than rows: a shim's tiles split over several rows.
                start_row = i * n_A_tiles_per_shim
                stop_row = start_row + n_A_tiles_per_shim
                of_offsets = [m * k * j for j in range(stop_row - start_row)]
                a_tmp_fifos = (
                    A_l3l2_fifos[i]
                    .cons()
                    .split(
                        of_offsets,
                        obj_types=[A_l1_ty] * (stop_row - start_row),
                        to_stream=[streams.A] * (stop_row - start_row),
                        tile=Tile(a_cols[i], 1) if pinned else AnyMemTile,
                    )
                )
                for j in range(stop_row - start_row):
                    A_l2l1_fifos[j + start_row] = a_tmp_fifos[j]

            for col in range(n_aie_cols):
                B_l3l2_fifos[col] = ObjectFifo(B_l2_ty, depth=FIFO_DEPTH)
                B_l2l1_fifos[col] = (
                    B_l3l2_fifos[col]
                    .cons()
                    .forward(
                        obj_type=B_l1_ty,
                        to_stream=streams.B,
                        tile=Tile(col, 1) if pinned else AnyMemTile,
                    )
                )
                C_l2l3_fifos[col] = ObjectFifo(
                    C_l2_ty,
                    depth=FIFO_DEPTH,
                    to_stream=streams.C,
                )
                of_offsets = [m * n * i for i in range(n_aie_rows)]
                c_tmp_fifos = (
                    C_l2l3_fifos[col]
                    .prod()
                    .join(
                        of_offsets,
                        obj_types=[C_l1_ty] * n_aie_rows,
                        depths=[fifo_depth_out] * n_aie_rows,
                        tile=Tile(col, 1) if pinned else AnyMemTile,
                    )
                )
                for j in range(n_aie_rows):
                    C_l1l2_fifos[j][col] = c_tmp_fifos[j]

            def core_fn(
                in_a,
                in_b,
                out_c,
                zero,
                matmul,
                convert_copy,
                k_tail_zero,
                rtp,
                elem_out_internal,
            ):
                words = rtp.read()
                rtp_K_div_k = words[self.k_div_k]
                rtp_n_tiles_per_core = words[self.n_tiles]
                if bounded:
                    row_blocks = words[self.row_blocks_valid]
                    col_tiles = words[self.col_tiles]
                # (K tiles, whether they are multiplied), in the order they arrive.
                spans = [(rtp_K_div_k, True)]
                if k_bounded:
                    k_bound = words[self.k_valid]
                    k_compute = (k_bound + (k - 1)) // k
                    last = k_compute - 1
                    kept = k_bound - last * k
                    spans = [(k_compute, True), (rtp_K_div_k - k_compute, False)]

                def tile(compute: bool):
                    if wider:
                        acc = elem_out_internal
                    else:
                        acc = c = out_c.acquire(1)
                    if compute:
                        zero(acc)
                    for count, multiply in spans:
                        for kk in range_(count):
                            elem_in_a = in_a.acquire(1)
                            elem_in_b = in_b.acquire(1)
                            if compute and multiply:
                                if k_bounded:
                                    with if_(
                                        arith.index_cast(kk, to=last.type) == last
                                    ):
                                        k_tail_zero(elem_in_a, elem_in_b, kept)
                                matmul(elem_in_a, elem_in_b, acc)
                            in_a.release(1)
                            in_b.release(1)
                    if wider:
                        c = out_c.acquire(1)
                        if compute:
                            convert_copy(acc, c, m * n)
                    out_c.release(1)

                if bounded:
                    for _ in range_(row_blocks):
                        for _ in range_(col_tiles):
                            tile(compute=True)
                    for _ in range_(rtp_n_tiles_per_core - row_blocks * col_tiles):
                        tile(compute=False)  # a padding tile: passed through
                    return
                for _ in range_(rtp_n_tiles_per_core):
                    tile(compute=True)

            workers = []
            for row in range(n_aie_rows):
                for col in range(n_aie_cols):
                    acc_buffer = None
                    if wider:
                        acc_buffer = Buffer(
                            type=np.ndarray[(m * n,), np.dtype[np.float32]]
                        )
                    workers.append(
                        Worker(
                            core_fn,
                            [
                                A_l2l1_fifos[row].cons(),
                                B_l2l1_fifos[col].cons(),
                                C_l1l2_fifos[row][col].prod(),
                                zero_kernel,
                                matmul_kernel,
                                convert_copy_kernel,
                                matmul_kernel.k_tail if k_bounded else None,
                                rtps[row * n_aie_cols + col],
                                acc_buffer,
                            ],
                            stack_size=STACK_BYTES,
                            tile=Tile(col, 2 + row) if pinned else AnyComputeTile,
                        )
                    )

            self.A.bind(
                [f.prod(tile=Tile(a_cols[c], 0)) for c, f in enumerate(A_l3l2_fifos)]
            )
            self.B.bind([f.prod(tile=Tile(c, 0)) for c, f in enumerate(B_l3l2_fifos)])
            self.C.bind([f.cons(tile=Tile(c, 0)) for c, f in enumerate(C_l2l3_fifos)])
            return Built(workers, rtps)

    def sequence(self, rt):
        M, K, N = self.M, self.K, self.N
        m, k, n = self.tile_m, self.tile_k, self.tile_n
        n_aie_cols, n_aie_rows = self.num_aie_columns, self.n_aie_rows
        mem_tile_m_A, mem_tile_m_C, mem_tile_n = (
            self.mem_tile_m_a,
            self.mem_tile_m_c,
            self.mem_tile_n,
        )
        c_col_maj, b_col_maj = self.c_col_maj, self.b_col_maj

        # The transfer blocks count descriptors, so B and C are checked against one.
        n_c_col_tiles_per_core = N // mem_tile_n
        n_c_row_tiles_per_core = M // mem_tile_m_C

        # A transfer block's BDs free at its sync: 4 row tiles, 2 col-major.
        tb_max_n_rows = 4 if not c_col_maj else 2

        A_rows = TensorAccessPattern.full((M, K)).tile((mem_tile_m_A, k))
        if b_col_maj:
            B_grid = TensorAccessPattern.full((N, K)).tile((n, k))
            B_tiles = [B_grid[col::n_aie_cols] for col in range(n_aie_cols)]
        else:
            B_grid = TensorAccessPattern.full((K, N)).tile((k, n))
            B_tiles = [
                B_grid[:, col::n_aie_cols].permute((1, 0, 2, 3))
                for col in range(n_aie_cols)
            ]

        # A B fill the compiler splits is not overlapped: 12 of 16 BDs assumes one.
        b_unrolled = not all(self.B.fits(tap) for tap in B_tiles)

        def fill(col, c_row, tg):
            tile_offset = (c_row * self.n_shim_mem_a + col) % (M // mem_tile_m_A)
            if col < n_aie_rows:
                A_tile = A_rows[tile_offset].repeat(n_c_col_tiles_per_core)
                self.A.fill(A_tile, lane=col, group=tg)
            self.B.fill(B_tiles[col], lane=col, group=tg)

        C_grid = (
            TensorAccessPattern.full((N, M)).tile((n, m))
            if c_col_maj
            else TensorAccessPattern.full((M, N)).tile((mem_tile_m_C, n))
        )

        def c_tile(col, c_row_base, c_n_rows):
            if c_col_maj:
                pieces = slice(c_row_base * n_aie_rows, (c_row_base + 1) * n_aie_rows)
                return C_grid[col::n_aie_cols, pieces]
            return C_grid[c_row_base : c_row_base + c_n_rows, col::n_aie_cols]

        tg = TaskGroup()
        for tb in range(ceildiv(n_c_row_tiles_per_core, tb_max_n_rows)):
            for pingpong in [0, 1]:
                row_base = tb * tb_max_n_rows + pingpong * tb_max_n_rows // 2
                current_tb_n_rows = min(
                    [tb_max_n_rows // 2, n_c_row_tiles_per_core - row_base]
                )
                if current_tb_n_rows <= 0:
                    break
                for col in range(n_aie_cols):
                    # A row stride past the BD's 20-bit step: a drain per row-block.
                    C_tiles = [c_tile(col, row_base, current_tb_n_rows)]
                    if not c_col_maj and not self.C.fits(C_tiles[0]):
                        C_tiles = [
                            c_tile(col, row_base + r, 1)
                            for r in range(current_tb_n_rows)
                        ]
                    for C_tile in C_tiles:
                        self.C.drain(C_tile, lane=col, group=tg, wait=True)
                    if not b_unrolled:
                        for tile_row in range(current_tb_n_rows):
                            fill(col, row_base + tile_row, tg)
                if b_unrolled:
                    # Row-block first: column-first hangs on a full task queue.
                    for tile_row in range(current_tb_n_rows):
                        for col in range(n_aie_cols):
                            fill(col, row_base + tile_row, tg)
                if b_unrolled or tb > 0 or (tb == 0 and pingpong > 0):
                    tg.finish()
                    tg = TaskGroup()
        tg.finish()

    def ops(self) -> int:
        return 2 * self.M * self.K * self.N

    def matmul_calls(self, values: Mapping[str, int]) -> int:
        """The fewest matmul kernel calls the busiest core makes in a step
        at per-call ``values``: each output tile under the bound takes one
        call per K tile under it.
        """
        calls = (
            ceildiv(values.get("valid", self.M), self.tile_m)
            * ceildiv(values.get("valid_k", self.K), self.tile_k)
            * (self.N // self.tile_n)
        )
        return ceildiv(calls, self.n_aie_rows * self.num_aie_columns)

    def reference(self, A, B):
        """``A @ B`` over the first ``valid_k`` of K, a bounded call's."""
        # float32, not mm_ref's float64, which doubles the weight's host copy.
        a = A.astype(np.float32)[:, : self.valid_k]
        b = (B.T if self.b_col_maj else B).astype(np.float32)[: self.valid_k]
        C = np.matmul(b.T, a.T) if self.c_col_maj else np.matmul(a, b)
        return C.astype(self.output_dtype)

    def tolerance(self) -> Tolerance:
        """Each element of C within the roundings the design makes, in
        units of 2^-8 of what each rounds: 2 of ``|A| @ |B|`` for C's own, 2
        of every K tile's partial sum but the last when C accumulates in
        bf16, and 2 more for bfp16 inputs. Measured on npu2 at no more than
        0.83 of it over K = 256 to 8192.
        """
        if np.issubdtype(np.dtype(self.input_dtype), np.integer):
            return Tolerance.exact(note="integer matmul")
        units = 4.0 if self.precision == Precision.MEDIUM else 2.0
        per_tile = (
            np.dtype(self.output_dtype) == np.dtype(bfloat16)
            and self.precision != Precision.HIGHEST
        )

        def bound(A, B):
            a = A.astype(np.float32)
            b = (B.T if self.b_col_maj else B).astype(np.float32)
            err = units * (np.abs(a) @ np.abs(b))
            if per_tile:
                partial = np.zeros_like(err)
                for k0 in range(0, self.K - self.tile_k, self.tile_k):
                    partial += a[:, k0 : k0 + self.tile_k] @ b[k0 : k0 + self.tile_k]
                    err += 2 * np.abs(partial)
            err *= 2.0**-8
            return err.T if self.c_col_maj else err

        return Tolerance.bounded(
            bound,
            note=f"{units:g} units of |A| @ |B|"
            + (", 2 of each bf16 partial sum" if per_tile else ""),
        )
