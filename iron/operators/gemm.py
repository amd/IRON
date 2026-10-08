# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from dataclasses import field
from typing import Any

import numpy as np
from aie.dialects.aie import AIEArch
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Buffer,
    ObjectFifo,
    TaskGroup,
    Worker,
    WorkerRuntimeBarrier,
    ceildiv,
    kernels,
)
from aie.iron.controlflow import range_
from aie.iron.device import NPU1, NPU2, Device, NPU1Col1, NPU1Col2, Tile
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Extent,
    In,
    Operator,
    Out,
    Unresolvable,
    Value,
    auto,
    param,
    Select,
)
from iron.common.design import BdLimits
from iron.common.testing import Case, Testing

# fmt: off
# The rounding configuration that tracks the reference most closely (an f32
# accumulator, native bf16 mmul), over shapes, layouts and tiles:
#   M,     K,     N, columns, b_col_maj, c_col_maj,   m,   k,   n
_REGULAR = [
    (2048,  2048,  2048,       1,     False,     False,  64,  64,  64),
    (2048,  2048,  2048,       2,      True,     False,  64,  64,  64),
    (2048,  2048,  2048,       8,      True,      True,  64,  64,  64),
    ( 384,  1536,  1792,       4,      True,     False,  32,  48,  64),
    (1792,   896,  1152,       8,     False,      True,  64,  32,  48),
    ( 896,  1792,   640,       8,     False,      True,  32,  64,  80),
    ( 192,   384,    64,       4,     False,     False,  48,  96,  16),
    ( 192,   384,    64,       4,      True,      True,  48,  96,  16),
]
_EXTENSIVE = [
    (2048,  2048,  2048,       8,     False,     False,  32,  32, 128),
    (2048,  2048,  8192,       2,     False,     False,  64,  64,  64),
    (2048,  8192,  2048,       2,     False,     False,  64,  64,  64),
    (2048,    64,  2048,       2,     False,     False,  64,  64,  64),
    (2048,    64,  8192,       2,     False,     False,  64,  64,  64),
    (2048,  2048,  2048,       8,      True,     False, 128,  32,  32),
    (2048,  2048,  8192,       2,      True,     False,  64,  64,  64),
    (2048,  8192,  2048,       2,      True,     False,  64,  64,  64),
    # A down projection of a 2048-wide model with an 8192-wide feed-forward.
    (2048,  8192,  2048,       8,      True,     False,  64,  64,  64),
    (2048,    64,  2048,       2,      True,     False,  64,  64,  64),
    (2048,    64,  8192,       2,      True,     False,  64,  64,  64),
    (2048,  2048,  2048,       2,     False,      True,   8,  16,  32),
    (2048,  2048,  8192,       2,     False,      True,  64,  64,  64),
    (2048,  8192,  2048,       2,     False,      True,  64,  64,  64),
    (2048,    64,  2048,       2,     False,      True,  64,  64,  64),
    (2048,    64,  8192,       2,     False,      True,  64,  64,  64),
    # N wide enough that C's row stride (mem_tile_m_C * N) overflows the
    # shim BD's 20-bit iteration step, so the drain is issued as one
    # descriptor per row-block. Cover for that split.
    (1024,  2560, 10240,       8,     False,     False,  64,  64,  64),
    (2048,  2560, 10240,       8,     False,     False,  64,  64,  64),
]
# fmt: on


def _cases(cls, dev: Device):
    # aie2's mm kernels block m by 4 r (mm_aie2.h), not aie2p's 2 r: an
    # 8-row tile does not compile there.
    min_tile_m = 16 if dev.arch is AIEArch.AIE2 else 1
    out = []
    for rows, extensive in ((_REGULAR, False), (_EXTENSIVE, True)):
        for M, K, N, cols, b_col_maj, c_col_maj, m, k, n in rows:
            if m < min_tile_m:
                continue
            kwargs = dict(M=M, K=K, N=N, num_aie_columns=cols, tile_m=m, tile_k=k)
            kwargs.update(tile_n=n, b_col_maj=b_col_maj, c_col_maj=c_col_maj)
            kwargs.update(prio_accuracy=True, emulate_bf16_mmul_with_bfp16=False)
            out.append(Case(kwargs, extensive=extensive))
    # The defaults, which a graph's projections run: bfp16 inputs, and C
    # rounded to bf16 between K tiles.
    # The default-suite one is benched: it runs well past the dispatch cost.
    for K, extensive in ((2048, False), (8192, True)):
        kwargs = dict(M=2048, K=K, N=2048, b_col_maj=True)
        out.append(Case(kwargs, extensive, bench=not extensive))
    return out


class GEMM(Operator):
    """AIE-accelerated General Matrix Multiplication (GEMM) layer.

    ``C = A @ B`` on the device's rows of cores, one column of B per AIE column,
    tiled m x k x n. A is broadcast across columns and distributed across
    rows in (m * n_A_tiles_per_shim, k) blocks; B is distributed across
    columns and broadcast across rows in (k, n) blocks; C is joined across
    rows and distributed across columns in (m * n_aie_rows, n) blocks. The core's
    reduction and tile counts are values the sequence writes, so the array
    does not depend on the extents.
    """

    test = Testing(_cases, draw=dict(normal=("A",)))

    M: int = param()
    K: int = param()
    N: int = param()
    # None: the widest of 64, 32, 16 and 8 rows that splits M over the rows
    # of cores and that the kernel's m block divides.
    tile_m: int = auto(array=True)
    tile_k: int = auto(64, array=True)
    tile_n: int = auto(64, array=True)
    # None: the most columns the device's shim budget allows that split N
    # into whole tile_n-wide tiles.
    num_aie_columns: int = auto()
    # A @ B = C, with either operand optionally stored column-major. The
    # layout flags transpose a declared shape rather than resize it.
    b_col_maj: bool = param(default=False, array=True)
    c_col_maj: bool = param(default=False, array=True)
    emulate_bf16_mmul_with_bfp16: bool = param(default=True, repr=False, array=True)
    prio_accuracy: bool = param(default=False, repr=False, array=True)
    round_conv_even: bool = param(default=True, repr=False, array=True)
    dtype_in: Any = field(default=bfloat16, repr=False)
    dtype_out: Any = field(default=bfloat16, repr=False)
    use_scalar: bool = param(default=False, repr=False, array=True)
    # Filled by resolve: the device's rows of cores, the L2 tile of each
    # stream and how many shims carry A.
    n_aie_rows: int = auto(repr=False, array=True, derived=True)
    n_shim_mem_a: int = auto(repr=False, derived=True)
    a_l2: int = auto(repr=False, derived=True)
    b_l2: int = auto(repr=False, derived=True)
    c_l2: int = auto(repr=False, derived=True)

    A = In(M, K, dtype=dtype_in, tile=(a_l2,), per=(n_shim_mem_a,))
    B = In(
        Select(b_col_maj, (N, K), (K, N)),
        dtype=dtype_in,
        tile=(b_l2,),
        per=(num_aie_columns,),
    )
    C = Out(
        Select(c_col_maj, (N, M), (M, N)),
        dtype=dtype_out,
        tile=(c_l2,),
        per=(num_aie_columns,),
    )
    # M, or fewer rows per call (``A[:n]`` in a graph). The DMAs stream
    # every row either way, since A's pattern uses all four descriptor
    # dimensions; the cores compute the tiles the bound covers and pass the
    # rest through, so the work follows the call and the traffic does not.
    valid = Extent(M)
    # Reduction steps per output tile, and output tiles per core.
    k_div_k = Value(np.int32, derive=lambda op: op.K // op.tile_k)
    n_tiles = Value(
        np.int32,
        derive=lambda op: (op.M // op.mem_tile_m_c) * (op.N // op.mem_tile_n),
    )
    # The tiles the bound covers: whole row blocks of it, every column tile.
    n_tiles_valid = Value(
        np.int32,
        derive=lambda op: ceildiv(op.valid, op.mem_tile_m_c) * (op.N // op.mem_tile_n),
        optional=True,  # nothing reads it unbounded
    )

    def extent_unit(self, buffer: str) -> int:
        return 0  # nothing is shortened: the cores bound their compute

    # -- derived geometry ---------------------------------------------------

    @property
    def n_a_tiles_per_shim(self) -> int:
        # Integer division when there are fewer columns than rows, otherwise
        # 1: with more columns than rows only n_aie_rows shim/mem tiles carry
        # A, distributed by rows.
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

    # -- checks ---------------------------------------------------------------

    def validate(self) -> None:
        # The kernel's own geometry rather than a second copy of it: mm.cc's
        # matmul_vectorized_2x2_mmul works in r x s x t blocks, so a tile that
        # does not divide into them cannot be compiled for.
        #
        # aie2p's geometry whatever the device: the messages name
        # aie_kernels/linalg/mm_aie2p.h, and no device is known here anyway, since
        # this runs at construction, before resolution picks one. array()
        # asks for the geometry of the device it builds for, which on npu1
        # is the looser (4, 8, 4).
        r, s, t = kernels.mm.mac_dims(
            self.dtype_in,
            self.dtype_out,
            arch="aie2p",
            emulate_bf16_mmul_with_bfp16=self.emulate_bf16_mmul_with_bfp16,
        )
        min_tile_m, min_tile_k, min_tile_n = 2 * r, s, 2 * t
        if self.tile_m is not None and self.tile_m % min_tile_m != 0:
            raise ValueError(
                f"tile_m ({self.tile_m}) must be a multiple of {min_tile_m} "
                f"(aie_kernels/linalg/mm_aie2p.h requires m % (2*r) == 0, r={r})"
            )
        if self.tile_k % min_tile_k != 0:
            raise ValueError(
                f"tile_k ({self.tile_k}) must be a multiple of {min_tile_k} "
                f"(aie_kernels/linalg/mm_aie2p.h requires k % s == 0, s={s})"
            )
        if self.tile_n % min_tile_n != 0:
            raise ValueError(
                f"tile_n ({self.tile_n}) must be a multiple of {min_tile_n} "
                f"(aie_kernels/linalg/mm_aie2p.h requires n % (2*t) == 0, t={t})"
            )
        din, dout = np.dtype(self.dtype_in), np.dtype(self.dtype_out)
        if self.prio_accuracy and dout != np.dtype(bfloat16):
            raise ValueError(
                "prio_accuracy flag is a feature only for bfloat16 output data types"
            )
        if np.issubdtype(din, np.integer) != np.issubdtype(dout, np.integer):
            raise ValueError(
                f"Input dtype ({din}) and output dtype ({dout}) must either both be integral or both be float"
            )
        if dout.itemsize < din.itemsize:
            raise ValueError(
                f"Output dtype ({dout}) must be equal or larger to input dtype ({din})"
            )
        # The extents that need no tunable, at construction, so a bad shape is
        # reported where it is written: K, and M once the rows of cores are
        # known (resolved, or the bound device's). N waits for the columns.
        if self.K % self.tile_k != 0:
            raise ValueError(f"K ({self.K}) must be a multiple of {self.tile_k}")
        rows = self.n_aie_rows or (self.dev and len(self.dev.core_rows))
        # An open tile_m is at least the kernel's narrowest.
        m = self.tile_m or min_tile_m
        if rows and self.M % (m * rows) != 0:
            raise ValueError(
                f"M ({self.M}) must be a multiple of {m * rows}: C is "
                f"tiled into (m * n_aie_rows, n)-sized blocks"
            )

    def resolve(self, dev):
        if dev is None:
            raise Unresolvable(
                "GEMM: the rows of cores are the device's; none is bound"
            )
        cols = self.resolve_columns(
            dev, self.num_aie_columns, fits=lambda c: self.N % (self.tile_n * c) == 0
        )
        rows = len(dev.core_rows)
        tile_m = self.tile_m
        if tile_m is None:
            r, _, _ = kernels.mm.mac_dims(
                self.dtype_in,
                self.dtype_out,
                device=dev,
                emulate_bf16_mmul_with_bfp16=self.emulate_bf16_mmul_with_bfp16,
                vectorized=not self.use_scalar,
            )
            # aie2's mm kernels block m by 4 r (mm_aie2.h), aie2p's by 2 r.
            block = (4 if dev.arch is AIEArch.AIE2 else 2) * r
            # None splits M: the narrowest, and validate() names the rule.
            tile_m = next(
                (
                    m
                    for m in (64, 32, 16, 8)
                    if m % block == 0 and self.M % (m * rows) == 0
                ),
                block,
            )
        new = dataclasses.replace(
            self, tile_m=tile_m, num_aie_columns=cols, n_aie_rows=rows
        )
        return dataclasses.replace(
            new,
            n_shim_mem_a=min(cols, rows),
            a_l2=new.mem_tile_m_a * self.tile_k,
            b_l2=self.tile_k * self.tile_n,
            c_l2=new.mem_tile_m_c * self.tile_n,
        )

    def compatible(self) -> None:
        if self.N % self.mem_tile_n != 0:
            raise ValueError(
                f"N ({self.N}) must be a multiple of {self.mem_tile_n}: B is "
                f"tiled into (k, n * num_aie_columns)-sized blocks"
            )
        if self.M % self.mem_tile_m_a != 0:
            raise ValueError(
                "A must be tileable into (m * n_A_tiles_per_shim, k)-sized blocks"
            )

    def device(self, target):
        if target.dev.arch is AIEArch.AIE2:
            return {1: NPU1Col1, 2: NPU1Col2, 4: NPU1}[self.num_aie_columns]()
        return NPU2()

    # -- the array ----------------------------------------------------------

    def array(self, target) -> list:
        m, k, n = self.tile_m, self.tile_k, self.tile_n
        n_aie_cols = self.num_aie_columns
        n_aie_rows = self.n_aie_rows
        n_shim_mem_A = self.n_shim_mem_a
        n_A_tiles_per_shim = self.n_a_tiles_per_shim
        b_col_maj, c_col_maj = self.b_col_maj, self.c_col_maj
        use_scalar = self.use_scalar
        dtype_in, dtype_out = self.dtype_in, self.dtype_out
        use_larger_internal_buffer = self.prio_accuracy
        # bfloat16 accumulates in place in an f32 buffer, converted to bf16
        # after the reduction loop for the transfer to L2.
        dtype_out_internal = np.float32
        # If you get errors during CDO generation due to running out of program
        # memory, it may be because too much code is generated due to ObjectFIFO
        # loop unrollings. Reducing the depth to 1 here will work around that at
        # a big performance cost.
        fifo_depth = 2

        A_l2_ty = self.A.tile
        B_l2_ty = self.B.tile
        C_l2_ty = self.C.tile
        A_l1_ty = np.ndarray[(m, k), np.dtype[dtype_in]]
        B_l1_ty = np.ndarray[(k, n), np.dtype[dtype_in]]
        C_l1_ty = np.ndarray[(m, n), np.dtype[dtype_out]]

        # AIE Core Function declarations: upstream's factories, which pick the
        # source and the -D set for the device they are resolved against.
        # prio_accuracy accumulates in f32 in L1 and converts on the way out,
        # so the matmul's C, and the buffer that gets zeroed, are f32 even
        # when C is bf16. All three kernels declare their buffers flat.
        dtype_acc = dtype_out_internal if use_larger_internal_buffer else dtype_out
        matmul_kernel = kernels.linalg.mm(
            m,
            k,
            n,
            input_dtype=dtype_in,
            output_dtype=dtype_acc,
            vectorized=not use_scalar,
            b_col_maj=b_col_maj,
            c_col_maj=c_col_maj,
            emulate_bf16_mmul_with_bfp16=self.emulate_bf16_mmul_with_bfp16,
            round_conv_even=self.round_conv_even,
        )
        r, s, t = matmul_kernel.mac_dims
        assert m % r == 0 and k % s == 0 and n % t == 0
        streams = matmul_kernel.stream_dims
        zero_kernel = kernels.zero(m * n, dtype_acc, vectorized=not use_scalar)
        convert_copy_kernel = None
        C_l1_ty_internal = np.ndarray[(m * n,), np.dtype[dtype_out_internal]]
        if use_larger_internal_buffer:
            # Fix fifo depth for C objfifo to 1 since 1 buffer will be used for
            # accumulation and another for transfer to L2
            fifo_depth_out = 1
            convert_copy_kernel = kernels.datamovement.convert_copy(m * n)
        else:
            fifo_depth_out = fifo_depth

        # AIE-array data movement with object fifos
        A_l3l2_fifos: list[Any] = [None] * n_shim_mem_A
        A_l2l1_fifos: list[Any] = [None] * n_aie_rows
        B_l3l2_fifos: list[Any] = [None] * n_aie_cols
        B_l2l1_fifos: list[Any] = [None] * n_aie_cols
        C_l1l2_fifos: list[list[Any]] = [[None] * n_aie_cols for _ in range(n_aie_rows)]
        C_l2l3_fifos: list[Any] = [None] * n_aie_cols

        # Runtime parameters: [K_div_k, n_tiles_per_core] per core
        rtps = [
            [
                Buffer(
                    np.ndarray[(2,), np.dtype[np.int32]],
                    name=f"rtp{row}_{col}",
                    initial_value=np.zeros(2, dtype=np.int32),
                    use_write_rtp=True,
                )
                for col in range(n_aie_cols)
            ]
            for row in range(n_aie_rows)
        ]
        workerBarriers = [
            [WorkerRuntimeBarrier() for col in range(n_aie_cols)]
            for row in range(n_aie_rows)
        ]

        # Input A
        for i in range(n_shim_mem_A):
            A_l3l2_fifos[i] = ObjectFifo(A_l2_ty, name=f"A_L3L2_{i}", depth=fifo_depth)
            # If n_shim_mem_A == n_rows, n_A_tiles_per_shim is 1 and this simply
            # links a_l3l2_fifos[i] to a_l2l1_fifos[i] directly. If n_shim_mem_A
            # < n_rows, each column receives multiple rows of tiles; distribute
            # it along rows of AIE cores.
            start_row = i * n_A_tiles_per_shim
            stop_row = start_row + n_A_tiles_per_shim
            of_offsets = [m * k * j for j in range(stop_row - start_row)]
            a_tmp_fifos = (
                A_l3l2_fifos[i]
                .cons()
                .split(
                    of_offsets,
                    obj_types=[A_l1_ty] * (stop_row - start_row),
                    names=[f"A_L2L1_{row}" for row in range(start_row, stop_row)],
                    to_stream=[streams.A] * (stop_row - start_row),
                )
            )
            for j in range(stop_row - start_row):
                A_l2l1_fifos[j + start_row] = a_tmp_fifos[j]

        # Input B
        for col in range(n_aie_cols):
            B_l3l2_fifos[col] = ObjectFifo(
                B_l2_ty, name=f"B_L3L2_{col}", depth=fifo_depth
            )
            B_l2l1_fifos[col] = (
                B_l3l2_fifos[col]
                .cons()
                .forward(
                    obj_type=B_l1_ty,
                    name=f"B_L2L1_{col}",
                    to_stream=streams.B,
                )
            )
            # Output C
            C_l2l3_fifos[col] = ObjectFifo(
                C_l2_ty,
                name=f"C_L2L3_{col}",
                depth=fifo_depth,
                to_stream=streams.C,
            )
            of_offsets = [m * n * i for i in range(n_aie_rows)]
            # join along one column
            c_tmp_fifos = (
                C_l2l3_fifos[col]
                .prod()
                .join(
                    of_offsets,
                    obj_types=[C_l1_ty] * n_aie_rows,
                    names=[f"C_L1L2_{col}_{row}" for row in range(n_aie_rows)],
                    depths=[fifo_depth_out] * n_aie_rows,
                )
            )
            for j in range(n_aie_rows):
                C_l1l2_fifos[j][col] = c_tmp_fifos[j]

        # Under a bound on M each core computes the tiles the bound covers
        # and passes the rest through: the DMAs still move every row.
        bounded = "valid" in self.bound_extents and target.image == "elf"
        n_valid_param = self.n_tiles_valid.param if bounded else None

        # Tasks for each worker to perform
        def core_fn(
            in_a,
            in_b,
            out_c,
            zero,
            matmul,
            convert_copy,
            my_rtp,
            barrier,
            elem_out_internal,
            n_valid=None,
        ):
            barrier.wait_for_value(1)
            rtp_K_div_k = my_rtp[0]
            rtp_n_tiles_per_core = my_rtp[1]
            n_compute = n_valid.read() if bounded else None
            barrier.release_with_value(1)

            def tile(compute: bool):
                nonlocal elem_out_internal
                if not use_larger_internal_buffer:
                    elem_out_internal = out_c.acquire(1)
                if compute:
                    zero(elem_out_internal)
                for _ in range_(rtp_K_div_k):
                    elem_in_a = in_a.acquire(1)
                    elem_in_b = in_b.acquire(1)
                    if compute:
                        matmul(elem_in_a, elem_in_b, elem_out_internal)
                    in_a.release(1)
                    in_b.release(1)
                if use_larger_internal_buffer:
                    elem_out_transfer = out_c.acquire(1)
                    if compute:
                        convert_copy(elem_out_internal, elem_out_transfer, m * n)
                    out_c.release(1)
                else:
                    out_c.release(1)

            if bounded:
                for _ in range_(n_compute):
                    tile(compute=True)
                for _ in range_(rtp_n_tiles_per_core - n_compute):
                    tile(compute=False)  # a padding tile: passed through
                return
            loop = range(1)  # Workaround for issue #1547
            if rtp_n_tiles_per_core > 1:
                loop = range_(rtp_n_tiles_per_core)
            for _ in loop:
                tile(compute=True)

        # Set up compute tiles
        workers = []
        for row in range(n_aie_rows):
            for col in range(n_aie_cols):
                acc_buffer = None
                if use_larger_internal_buffer:
                    acc_buffer = Buffer(
                        type=C_l1_ty_internal, name=f"acc_buffer_{row}_{col}"
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
                            convert_copy_kernel if use_larger_internal_buffer else None,
                            rtps[row][col],
                            workerBarriers[row][col],
                            acc_buffer,
                        ]
                        + ([n_valid_param] if bounded else []),
                        stack_size=0xD00,
                    )
                )

        # The shim ends stay pinned, and A on alternate columns in the 4x8
        # case is the reason: the memtiles and the workers place themselves
        # fine, but relaxing these three as well piles the descriptors of a
        # real shape (2048x8192x2048, b_col_maj) onto one tile, and DMA
        # lowering rejects it with "Too many simultaneously active buffer
        # descriptors on tile (3,0), which supports up to 16".
        for c, f in enumerate(A_l3l2_fifos):
            self.A.lane(c).bind(f.prod(tile=Tile(2 * c if n_aie_cols == 8 else c, 0)))
        for c, f in enumerate(B_l3l2_fifos):
            self.B.lane(c).bind(f.prod(tile=Tile(c, 0)))
        for c, f in enumerate(C_l2l3_fifos):
            self.C.lane(c).bind(f.cons(tile=Tile(c, 0)))
        flat_rtps = [
            rtps[row][col] for row in range(n_aie_rows) for col in range(n_aie_cols)
        ]
        self.k_div_k.bind(flat_rtps, 0)
        self.n_tiles.bind(flat_rtps, 1)
        return workers + [b for row in workerBarriers for b in row]

    # -- the runtime sequence --------------------------------------------------

    def sequence(self, rt):
        M, K, N = self.M, self.K, self.N
        m, k, n = self.tile_m, self.tile_k, self.tile_n
        n_aie_cols, n_aie_rows = self.num_aie_columns, self.n_aie_rows
        n_shim_mem_A = self.n_shim_mem_a
        mem_tile_m_A, mem_tile_m_C, mem_tile_n = (
            self.mem_tile_m_a,
            self.mem_tile_m_c,
            self.mem_tile_n,
        )
        c_col_maj, b_col_maj = self.c_col_maj, self.b_col_maj
        dtype_out = self.dtype_out

        # What one shim descriptor holds. The compiler splits a constant
        # pattern that does not fit, but the transfer blocks below count
        # descriptors, so B and C are checked here and shaped to fit.
        shim = BdLimits.of(self.dev, 0, 0)

        n_c_col_tiles_per_core = N // mem_tile_n
        n_c_row_tiles_per_core = M // mem_tile_m_C

        # We are limited in the number of BDs. After synchronizing, we can reuse BDs.
        # We only transfer 6 rows of tiles at once before starting a new transfer block.
        # tb = transfer block; block of transfers before sync call
        tb_max_n_rows = 4 if not c_col_maj else 2

        # Define tensor access patterns (tiling) for A, B, and C
        # A: one row of (mem_tile_m_A, k) tiles, repeated so it can be
        # distributed across the whole column.
        A_rows = TensorAccessPattern.full((M, K)).tile((mem_tile_m_A, k))
        # B: every n_aie_cols-th (n)-wide block of columns from the shim's
        # own, each block whole down K before the next.
        if b_col_maj:
            B_grid = TensorAccessPattern.full((N, K)).tile((n, k))
            B_tiles = [B_grid[col::n_aie_cols] for col in range(n_aie_cols)]
        else:
            B_grid = TensorAccessPattern.full((K, N)).tile((k, n))
            B_tiles = [
                B_grid[:, col::n_aie_cols].permute((1, 0, 2, 3))
                for col in range(n_aie_cols)
            ]

        # A B fill that does not fit one descriptor (a column-major B whose
        # column-block stride is past the step field) is split by the
        # compiler, one descriptor per column block. The BD accounting below
        # (12 of 16 with two transfer blocks in flight) assumes one; when B
        # unrolls, the transfer blocks are not overlapped so that a shim
        # never holds more than one block's descriptors.
        b_unrolled = not all(shim.fits(tap, self.B.dtype) for tap in B_tiles)

        def fill(col, c_row, tg):
            # A input transfer: the smallest unit is a
            # (m*n_A_tiles_per_shim)-sized sub-tile, one per column,
            # repeated (N//n//n_aie_cols) times; each shim carries
            # separate rows.
            tile_offset = (c_row * n_shim_mem_A + col) % (M // mem_tile_m_A)
            # always equal to n_aie_rows since we have n_aie_rows row tiles for matrix A
            if col < n_aie_rows:
                A_tile = A_rows[tile_offset].repeat(n_c_col_tiles_per_core)
                rt.fill(self.A.lane(col), A_tile, group=tg)
            # B input transfer: the first (n)-wide block of columns
            # of B, then the (n_aie_columns)-th such block, and so
            # on; each shim starts at a different column offset.
            rt.fill(self.B.lane(col), B_tiles[col], group=tg)

        # C: (n_aie_rows * m)-by-n tiles, every n_aie_cols-th column block, for
        # c_n_rows row-blocks from c_row_base. Column-major, one row-block
        # (tb_max_n_rows halves to 1) in its n_aie_rows m-tall pieces.
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

        # Task groups determine when to sync, await and free DMA runtime ops.
        tg = TaskGroup()
        for tb in range(ceildiv(n_c_row_tiles_per_core, tb_max_n_rows)):
            for pingpong in [0, 1]:
                row_base = tb * tb_max_n_rows + pingpong * tb_max_n_rows // 2
                current_tb_n_rows = min(
                    [tb_max_n_rows // 2, n_c_row_tiles_per_core - row_base]
                )
                if current_tb_n_rows <= 0:
                    # For small input sizes, we may not even need a "pong" iteration
                    break
                for col in range(n_aie_cols):
                    # C Output Transfer for smaller N dimensions:
                    # The smallest transfer unit is a (m*n_aie_rows)-x-(n)-sized sub-tile of the matrix.
                    # Transfer one such tile for every (n_aie_cols)-th column, evenly spaced,
                    # then repeat that (current_tb_n_rows) times for the next contiguous blocks of rows.
                    # Each shim will start at a different column offset, transferring interleaved
                    # columns.
                    #
                    # Normally one descriptor walks all current_tb_n_rows
                    # row-blocks. When it does not fit one (a wide N puts the
                    # row-block stride, mem_tile_m_C * N, past the shim's
                    # 20-bit iteration step: M=1024 K=2560 N=10240), issue one
                    # descriptor per row-block instead, carrying the row jump
                    # in the OFFSET (which has no such limit). Same bytes,
                    # same order, same number of objects; only the
                    # descriptor is reshaped.
                    #
                    # These extra tasks are safe against the two shim
                    # limits neither the toolchain nor the verifier models.
                    # BD ids: all of a (tb, pingpong) iteration's tasks stay
                    # live until tg.finish() below, so they stay distinct:
                    # 2 iterations x (2 C + 2 A + 2 B) = 12 of 16. Channel
                    # task queue: the C channel goes from 2 outstanding to
                    # current_tb_n_rows x 2 = 4, which is where A and B
                    # already sit.
                    C_tiles = [c_tile(col, row_base, current_tb_n_rows)]
                    if not c_col_maj and not shim.fits(C_tiles[0], dtype_out):
                        C_tiles = [
                            c_tile(col, row_base + r, 1)
                            for r in range(current_tb_n_rows)
                        ]
                    for C_tile in C_tiles:
                        rt.drain(self.C.lane(col), C_tile, group=tg, wait=True)
                    if not b_unrolled:
                        for tile_row in range(current_tb_n_rows):
                            fill(col, row_base + tile_row, tg)
                if b_unrolled:
                    # Row-block by row-block across every column, where a
                    # single B descriptor issues column by column. A shim
                    # channel queues only a few tasks, and a push past that
                    # stalls the whole instruction stream until one retires.
                    # Column by column, the second row-block's B descriptors
                    # stall it on a column whose cores still wait for A from
                    # the columns not yet issued: a hang (2048x8192x2048,
                    # b_col_maj, on eight columns).
                    for tile_row in range(current_tb_n_rows):
                        for col in range(n_aie_cols):
                            fill(col, row_base + tile_row, tg)
                if b_unrolled or tb > 0 or (tb == 0 and pingpong > 0):
                    tg.finish()
                    tg = TaskGroup()
        tg.finish()

    # -- host-side helpers ---------------------------------------------------

    def ops(self) -> int:
        return 2 * self.M * self.K * self.N

    def reference(self, A, B):
        """``C = A @ B`` from the stored inputs: ``B`` is ``(N, K)`` when
        ``b_col_maj``, and ``C`` ``(N, M)`` when ``c_col_maj``.
        """
        # Not linalg.mm's contract: that is one tile's product, and mm_ref's
        # float64 would double the host copy of the largest weight a graph
        # reference multiplies. The exact product in float32, rounded once:
        # what the design rounds on the way (bfp16 inputs, a bf16 C between
        # K tiles) is its error, which tolerance() bounds.
        b = B.T if self.b_col_maj else B
        C = np.matmul(A.astype(np.float32), b.astype(np.float32)).astype(A.dtype)
        return C.T if self.c_col_maj else C

    def tolerance(self) -> Tolerance:
        """Each element of C within the roundings the design makes, in
        units of 2^-8 of what each rounds. A conversion to bf16 is off by
        less than 2 units even truncating: 2 of ``|A| @ |B|`` for C's own,
        and 2 of every K tile's partial sum but the last when C accumulates
        in bf16 between tiles. bfp16 inputs add 2 more of ``|A| @ |B|``,
        measured at most 0.5.

        A relative tolerance cannot hold this: an element whose products
        cancel is small against the error of the terms it summed, and the
        bf16 accumulator's error grows with K. On npu2 over K = 256 to
        8192, normal and all-positive inputs, no configuration's worst
        element came above 0.83 of it.
        """
        if np.issubdtype(np.dtype(self.dtype_in), np.integer):
            return Tolerance.exact(note="integer matmul")
        units = 4.0 if self.emulate_bf16_mmul_with_bfp16 else 2.0
        per_tile = (
            np.dtype(self.dtype_out) == np.dtype(bfloat16) and not self.prio_accuracy
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
