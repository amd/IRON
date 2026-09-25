# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from dataclasses import field

import numpy as np

from aie.iron import kernels
from ml_dtypes import bfloat16

from iron.common.kernels import target_arch
from iron.common.declare import (
    Incompatible,
    In,
    Operator,
    Out,
    Overlay,
    Resident,
    StreamIn,
    StreamOut,
    Untunable,
    dim,
    operator,
    select,
    tunable,
)


def ceildiv(a, b):
    return (a + b - 1) // b


N_AIE_ROWS = 4


# --------------------------------------------------------------------------
# The overlay: the whole-array matmul, tiled m x k x n.
# --------------------------------------------------------------------------


@operator
class GEMMOverlay(Overlay):
    """The array for C = A @ B: a 4-row grid of cores, one column of B per AIE column.

    A is broadcast across columns and distributed across rows in
    (m * n_A_tiles_per_shim, k) blocks; B is distributed across columns and
    broadcast across rows in (k, n) blocks; C is joined across rows and
    distributed across columns in (m * 4, n) blocks. The extents M, K, N
    belong to :class:`GEMM`; the core's reduction and tile counts are
    residents the sequence writes.
    """

    tile_m: int = tunable(64)
    tile_k: int = tunable(64)
    tile_n: int = tunable(64)
    num_aie_columns: int = tunable(8)
    b_col_maj: bool = False
    c_col_maj: bool = False
    emulate_bf16_mmul_with_bfp16: bool = field(default=True, repr=False)
    prio_accuracy: bool = field(default=False, repr=False)
    round_conv_even: bool = field(default=True, repr=False)
    dtype_in: object = field(default=bfloat16, repr=False)
    dtype_out: object = field(default=bfloat16, repr=False)
    use_scalar: bool = field(default=False, repr=False)
    # Filled by tuning: the L2 tile of each stream and how many shims carry A.
    n_shim_mem_a: int | None = tunable(None, repr=False)
    a_l2: int | None = tunable(None, repr=False)
    b_l2: int | None = tunable(None, repr=False)
    c_l2: int | None = tunable(None, repr=False)

    a = StreamIn(a_l2, dtype=dtype_in, per=n_shim_mem_a)
    b = StreamIn(b_l2, dtype=dtype_in, per=num_aie_columns)
    c = StreamOut(c_l2, dtype=dtype_out, per=num_aie_columns)
    k_div_k = Resident(np.int32)  # reduction steps per output tile
    n_tiles = Resident(np.int32)  # output tiles per core

    # -- derived geometry ---------------------------------------------------

    @property
    def n_a_tiles_per_shim(self) -> int:
        # Integer division when n_aie_cols < 4, otherwise 1: with more columns
        # than rows only n_aie_rows shim/mem tiles carry A, distributed by rows.
        c = self.num_aie_columns
        return N_AIE_ROWS // c if c < 4 else 1

    @property
    def mem_tile_m_a(self) -> int:
        return self.tile_m * self.n_a_tiles_per_shim

    @property
    def mem_tile_m_c(self) -> int:
        return self.tile_m * N_AIE_ROWS

    @property
    def mem_tile_n(self) -> int:
        return self.tile_n * self.num_aie_columns

    def mac_dims(self, dev=None) -> tuple[int, int, int]:
        """r, s, t: the aie::mmul tile dims the kernel is built from.

        Read from the kernel factory rather than tabulated here: the geometry
        belongs to the kernel mm.cc compiles, and upstream's table is the one
        its ``combos(X) X(..., r, s, t)`` macros are kept in step with.
        """
        return kernels.mm.mac_dims(
            self.dtype_in,
            self.dtype_out,
            arch=target_arch(dev),
            emulate_bf16_mmul_with_bfp16=self.emulate_bf16_mmul_with_bfp16,
        )

    # -- construction-time checks -------------------------------------------

    def validate(self) -> None:
        # The kernel's own geometry rather than a second copy of it: mm.cc's
        # matmul_vectorized_2x2_mmul works in r x s x t blocks, so a tile that
        # does not divide into them cannot be compiled for.
        #
        # aie2p unconditionally, which is what these checks have always
        # assumed and what their messages name, because the source is
        # aie_kernels/aie2p/mm.cc. A device is not known here anyway: this
        # runs at construction, before tuning picks one. design() asks for
        # the geometry of the device it is actually building for, which on
        # npu1 is the looser (4, 8, 4).
        r, s, t = kernels.mm.mac_dims(
            self.dtype_in,
            self.dtype_out,
            arch="aie2p",
            emulate_bf16_mmul_with_bfp16=self.emulate_bf16_mmul_with_bfp16,
        )
        min_tile_m, min_tile_k, min_tile_n = 2 * r, s, 2 * t
        if self.tile_m % min_tile_m != 0:
            raise ValueError(
                f"tile_m ({self.tile_m}) must be a multiple of {min_tile_m} "
                f"(aie_kernels/aie2p/mm.cc requires m % (2*r) == 0, r={r})"
            )
        if self.tile_k % min_tile_k != 0:
            raise ValueError(
                f"tile_k ({self.tile_k}) must be a multiple of {min_tile_k} "
                f"(aie_kernels/aie2p/mm.cc requires k % s == 0, s={s})"
            )
        if self.tile_n % min_tile_n != 0:
            raise ValueError(
                f"tile_n ({self.tile_n}) must be a multiple of {min_tile_n} "
                f"(aie_kernels/aie2p/mm.cc requires n % (2*t) == 0, t={t})"
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

    def tuning(self, dev) -> "GEMMOverlay":
        if dev is not None:
            name = dev.resolve().name
            if name == "npu1" and self.num_aie_columns > 4:
                raise Untunable(
                    "Invalid configuration: NPU (Phoenix/Hawk) has 4 columns"
                )
            if name == "npu2" and self.num_aie_columns > 8:
                raise Untunable(
                    "Invalid configuration: NPU2 (Strix/Strix Halo/Krackan) has 8 columns"
                )
        return dataclasses.replace(
            self,
            n_shim_mem_a=min(self.num_aie_columns, N_AIE_ROWS),
            a_l2=self.mem_tile_m_a * self.tile_k,
            b_l2=self.tile_k * self.tile_n,
            c_l2=self.mem_tile_m_c * self.tile_n,
        )

    # -- kernels ------------------------------------------------------------

    def device(self, target):
        from aie.iron.device import NPU1, NPU1Col1, NPU1Col2, NPU2

        if target.dev.resolve().name == "npu1":
            return {1: NPU1Col1, 2: NPU1Col2, 4: NPU1}[self.num_aie_columns]()
        return NPU2()

    # -- the array ----------------------------------------------------------

    def design(self, target) -> list:
        from aie.iron import Buffer, ObjectFifo, Worker
        from aie.iron.controlflow import range_
        from aie.iron.device import Tile

        m, k, n = self.tile_m, self.tile_k, self.tile_n
        n_aie_cols = self.num_aie_columns
        n_aie_rows = N_AIE_ROWS
        n_shim_mem_A = self.n_shim_mem_a
        n_A_tiles_per_shim = self.n_a_tiles_per_shim
        b_col_maj, c_col_maj = self.b_col_maj, self.c_col_maj
        use_scalar = self.use_scalar
        dtype_in, dtype_out = self.dtype_in, self.dtype_out
        use_larger_internal_buffer = self.prio_accuracy
        if use_larger_internal_buffer:
            # bfloat16 accumulates in place in an f32 buffer, converted to bf16
            # after the reduction loop for the transfer to L2.
            dtype_out_internal = np.float32
        r, s, t = self.mac_dims(target.dev)
        if not use_scalar:
            assert m % r == 0
            assert k % s == 0
            assert n % t == 0
        # If you get errors during CDO generation due to running out of program
        # memory, it may be because too much code is generated due to ObjectFIFO
        # loop unrollings. Reducing the depth to 1 here will work around that at
        # a big performance cost.
        fifo_depth = 2

        A_l2_ty = self.a.tile
        B_l2_ty = self.b.tile
        C_l2_ty = self.c.tile
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
        zero_kernel = kernels.zero(m * n, dtype_acc, vectorized=not use_scalar)
        convert_copy_kernel = None
        if use_larger_internal_buffer:
            # Fix fifo depth for C objfifo to 1 since 1 buffer will be used for
            # accumulation and another for transfer to L2
            fifo_depth_out = 1
            C_l1_ty_internal = np.ndarray[(m * n,), np.dtype[dtype_out_internal]]
            convert_copy_kernel = kernels.datamovement.convert_copy(m * n)
        else:
            fifo_depth_out = fifo_depth

        # AIE-array data movement with object fifos
        A_l3l2_fifos = [None] * n_shim_mem_A
        A_l2l1_fifos = [None] * n_aie_rows
        B_l3l2_fifos = [None] * n_aie_cols
        B_l2l1_fifos = [None] * n_aie_cols
        C_l1l2_fifos = [[None] * n_aie_cols for _ in range(n_aie_rows)]
        C_l2l3_fifos = [None] * n_aie_cols

        # Runtime parameters: [K_div_k, n_tiles_per_core] per core
        rtps = [
            [
                target.rtp(
                    np.ndarray[(2,), np.dtype[np.int32]],
                    name=f"rtp{row}_{col}",
                    initial_value=np.zeros(2, dtype=np.int32),
                )
                for col in range(n_aie_cols)
            ]
            for row in range(n_aie_rows)
        ]
        workerBarriers = [
            [target.barrier() for col in range(n_aie_cols)] for row in range(n_aie_rows)
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
            dims_to_stream = [
                [
                    (m // r, r * k),
                    (k // s, s),
                    (r, k),
                    (s, 1),
                ]
            ] * (stop_row - start_row)
            a_tmp_fifos = (
                A_l3l2_fifos[i]
                .cons()
                .split(
                    of_offsets,
                    obj_types=[A_l1_ty] * (stop_row - start_row),
                    names=[f"A_L2L1_{row}" for row in range(start_row, stop_row)],
                    dims_to_stream=dims_to_stream,
                )
            )
            for j in range(stop_row - start_row):
                A_l2l1_fifos[j + start_row] = a_tmp_fifos[j]

        # Input B
        for col in range(n_aie_cols):
            B_l3l2_fifos[col] = ObjectFifo(
                B_l2_ty, name=f"B_L3L2_{col}", depth=fifo_depth
            )
            if b_col_maj:
                dims_to_stream = [(n // t, t * k), (k // s, s), (t, k), (s, 1)]
            else:
                dims_to_stream = [(k // s, s * n), (n // t, t), (s, n), (t, 1)]
            B_l2l1_fifos[col] = (
                B_l3l2_fifos[col]
                .cons()
                .forward(
                    obj_type=B_l1_ty,
                    name=f"B_L2L1_{col}",
                    dims_to_stream=dims_to_stream,
                )
            )
            # Output C
            if c_col_maj:
                dims_to_stream = [(n // t, t * m), (t, r), (m // r, r * t), (r, 1)]
            else:
                dims_to_stream = [(m // r, r * n), (r, t), (n // t, r * t), (t, 1)]
            C_l2l3_fifos[col] = ObjectFifo(
                C_l2_ty,
                name=f"C_L2L3_{col}",
                depth=fifo_depth,
                dims_to_stream=dims_to_stream,
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
        ):
            barrier.wait_for_value(1)
            rtp_K_div_k = my_rtp[0]
            rtp_n_tiles_per_core = my_rtp[1]
            loop = range(1)  # Workaround for issue #1547
            if rtp_n_tiles_per_core > 1:
                loop = range_(rtp_n_tiles_per_core)
            for _ in loop:
                if not use_larger_internal_buffer:
                    elem_out_internal = out_c.acquire(1)
                zero(elem_out_internal)

                for _ in range_(rtp_K_div_k):
                    elem_in_a = in_a.acquire(1)
                    elem_in_b = in_b.acquire(1)
                    matmul(elem_in_a, elem_in_b, elem_out_internal)
                    in_a.release(1)
                    in_b.release(1)

                if use_larger_internal_buffer:
                    elem_out_transfer = out_c.acquire(1)
                    convert_copy(elem_out_internal, elem_out_transfer, m * n)
                    out_c.release(1)
                else:
                    out_c.release(1)

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
                        ],
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
            self.a[c].bind(f.prod(tile=Tile(2 * c if n_aie_cols == 8 else c, 0)))
        for c, f in enumerate(B_l3l2_fifos):
            self.b[c].bind(f.prod(tile=Tile(c, 0)))
        for c, f in enumerate(C_l2l3_fifos):
            self.c[c].bind(f.cons(tile=Tile(c, 0)))
        flat_rtps = [
            rtps[row][col] for row in range(n_aie_rows) for col in range(n_aie_cols)
        ]
        self.k_div_k.bind(flat_rtps, 0)
        self.n_tiles.bind(flat_rtps, 1)
        return workers


# --------------------------------------------------------------------------
# The operator: the host ABI, declared against the overlay.
# --------------------------------------------------------------------------


@operator
class GEMM(Operator[GEMMOverlay]):
    """AIE-accelerated General Matrix Multiplication (GEMM) layer"""

    M: int = dim()
    K: int = dim()
    N: int = dim()
    # A @ B = C, with either operand optionally stored column-major. The
    # layout flags transpose a declared shape rather than resize it.
    A = In(M, K, dtype=GEMMOverlay.dtype_in, to=GEMMOverlay.a)
    B = In(
        select(GEMMOverlay.b_col_maj, (N, K), (K, N)),
        dtype=GEMMOverlay.dtype_in,
        to=GEMMOverlay.b,
    )
    C = Out(
        select(GEMMOverlay.c_col_maj, (N, M), (M, N)),
        dtype=GEMMOverlay.dtype_out,
        from_=GEMMOverlay.c,
    )

    # -- checks ----------------------------------------------------------------

    def compatible(self) -> None:
        ov = self.ov
        min_M = ov.tile_m * N_AIE_ROWS
        min_K = ov.tile_k
        min_N = ov.tile_n * ov.num_aie_columns
        if self.M % min_M != 0:
            raise Incompatible(f"M ({self.M}) must be a multiple of {min_M}")
        if self.K % min_K != 0:
            raise Incompatible(f"K ({self.K}) must be a multiple of {min_K}")
        if self.N % min_N != 0:
            raise Incompatible(f"N ({self.N}) must be a multiple of {min_N}")
        if self.M % ov.mem_tile_m_a != 0:
            raise Incompatible(
                "A must be tileable into (m * n_A_tiles_per_shim, k)-sized blocks"
            )
        if self.N % ov.mem_tile_n != 0:
            raise Incompatible(
                "B must be tileable into (k, n * n_aie_cols)-sized blocks"
            )
        if self.M % ov.mem_tile_m_c != 0:
            raise Incompatible(
                "C must be tileable into (m * n_aie_rows, n)-sized blocks"
            )

    def validate(self) -> None:
        # The same checks at construction, so a bad shape is reported where it
        # is written rather than at tune time.
        ov = self.ov
        for name, value, unit in (
            ("M", self.M, ov.tile_m * N_AIE_ROWS),
            ("K", self.K, ov.tile_k),
            ("N", self.N, ov.tile_n * ov.num_aie_columns),
        ):
            if value % unit != 0:
                raise ValueError(f"{name} ({value}) must be a multiple of {unit}")

    def residents(self) -> dict[str, int]:
        ov = self.ov
        return {
            "k_div_k": self.K // ov.tile_k,
            "n_tiles": (self.M // ov.mem_tile_m_c) * (self.N // ov.mem_tile_n),
        }

    # -- the runtime sequence --------------------------------------------------

    def design(self, rt):
        from aie.helpers.taplib import TensorAccessPattern, TensorTiler2D

        from iron.common.tiling import legalize

        def legal(buffer, tap):
            """The tiler's pattern as descriptors the shim holds: one when it
            fits, else the outermost dimension unrolled (a column-major B
            whose column-block stride is past the 20-bit step)."""
            return legalize(
                buffer.elements, tap.offset, tap.sizes, tap.strides, buffer.dtype
            )

        ov = self.ov
        M, K, N = self.M, self.K, self.N
        m, k, n = ov.tile_m, ov.tile_k, ov.tile_n
        n_aie_cols, n_aie_rows = ov.num_aie_columns, N_AIE_ROWS
        n_shim_mem_A = ov.n_shim_mem_a
        mem_tile_m_A, mem_tile_m_C, mem_tile_n = (
            ov.mem_tile_m_a,
            ov.mem_tile_m_c,
            ov.mem_tile_n,
        )
        c_col_maj, b_col_maj = ov.c_col_maj, ov.b_col_maj
        dtype_out = ov.dtype_out

        # A shim BD's outermost descriptor dimension lands in the ITERATION field,
        # whose step is 20 bits wide (AIETargetModel::getDmaBdStepBits for
        # ShimNOCTile). An element stride S is re-expressed as (S - 1) * itemsize
        # / 4-byte address granularity before the check, so a wide N pushes C's row
        # stride past it: M=1024 K=2560 N=10240 needs mem_tile_m_C * N = 2621440
        # and aiecc rejects the build with "Stride 3 exceeds the [1:1048576]
        # range". See the C drain below for how that is split, and flm_gemm's
        # design.py for the same fix worked through in more detail.
        def _hw_stride_ok(stride_elems, itemsize):
            return (stride_elems - 1) * itemsize // 4 <= (1 << 20) - 1

        K_div_k = K // k
        n_c_col_tiles_per_core = N // mem_tile_n
        n_c_row_tiles_per_core = M // mem_tile_m_C

        # We are limited in the number of BDs. After synchronizing, we can reuse BDs.
        # We only transfer 6 rows of tiles at once before starting a new transfer block.
        # tb = transfer block; block of transfers before sync call
        tb_max_n_rows = 4 if not c_col_maj else 2

        # Define tensor access patterns (tiling) for A, B, and C
        A_tiles = TensorTiler2D.group_tiler(
            (M, K),  # Size of A matrix
            (mem_tile_m_A, k),  # Size of A (smallest) tile
            (1, K_div_k),  # Size of "group" of tiles
            # Repeat data so can distribute across whole column
            pattern_repeat=n_c_col_tiles_per_core,
            prune_step=False,
        )
        if b_col_maj:
            B_tiles = TensorTiler2D.step_tiler(
                (N, K),  # Size of B matrix
                (n, k),  # Size of B tile
                # Number of tiles per transfer in each dimension (whole col, partial row)
                tile_group_repeats=(n_c_col_tiles_per_core, K_div_k),
                # Contiguous tile group in col, but send every n_aie_cols-th tile in the row
                tile_group_steps=(n_aie_cols, 1),
                prune_step=False,
            )
        else:
            B_tiles = TensorTiler2D.step_tiler(
                (K, N),  # Size of B matrix
                (k, n),  # Size of B tile
                # Number of tiles per transfer in each dimension (whole col, partial row)
                tile_group_repeats=(K_div_k, n_c_col_tiles_per_core),
                # Contiguous tile group in col, but send every n_aie_cols-th tile in the row
                tile_group_steps=(1, n_aie_cols),
                tile_group_col_major=True,  # Send all tiles in column before moving on to next column
                prune_step=False,
            )

        A_fills = [legal(self.A, tap) for tap in A_tiles]
        B_fills = [legal(self.B, tap) for tap in B_tiles]
        # An unrolled B fill costs one descriptor per column block. The BD
        # accounting below (12 of 16 with two transfer blocks in flight)
        # assumes one; when B unrolls, the transfer blocks are not overlapped
        # so that a shim never holds more than one block's descriptors.
        b_unrolled = any(len(f) > 1 for f in B_fills)

        # Task groups determine when to sync, await and free DMA runtime ops.
        tg = rt.new_group()
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
                    # row-blocks. When that outermost stride overflows the
                    # shim's 20-bit iteration step (see _hw_stride_ok
                    # above), issue one descriptor per row-block instead,
                    # carrying the row jump in the OFFSET -- which has no
                    # such limit -- and leaving the outer dimension
                    # degenerate. Same bytes, same order, same number of
                    # objects; only the descriptor is reshaped.
                    #
                    # These extra tasks are safe against the two shim
                    # limits neither the toolchain nor the verifier models.
                    # BD ids: all of a (tb, pingpong) iteration's tasks stay
                    # live until tg.finish() below, so they stay distinct --
                    # 2 iterations x (2 C + 2 A + 2 B) = 12 of 16. Channel
                    # task queue: the C channel goes from 2 outstanding to
                    # current_tb_n_rows x 2 = 4, which is where A and B
                    # already sit.
                    C_rows = [(row_base, current_tb_n_rows)]
                    if not c_col_maj:
                        row_stride = mem_tile_m_C * N
                        if current_tb_n_rows > 1 and not _hw_stride_ok(
                            row_stride, np.dtype(dtype_out).itemsize
                        ):
                            C_rows = [
                                (row_base + r, 1) for r in range(current_tb_n_rows)
                            ]
                    for c_row_base, c_n_rows in C_rows:
                        if not c_col_maj:
                            C_row_offset = c_row_base * mem_tile_m_C * N
                            C_col_offset = col * n
                            C_offset = C_col_offset + C_row_offset
                            C_sizes = [c_n_rows, N // mem_tile_n, mem_tile_m_C, n]
                            C_strides = [
                                mem_tile_m_C * N if c_n_rows > 1 else 0,
                                mem_tile_n,
                                N,
                                1,
                            ]
                        else:
                            C_row_offset = c_row_base * mem_tile_m_C
                            C_col_offset = col * n * M
                            C_offset = C_col_offset + C_row_offset
                            C_sizes = [N // mem_tile_n, n_aie_rows, n, m]
                            C_strides = [M * mem_tile_n, m, M, 1]
                        C_tile = TensorAccessPattern(
                            (N, M) if c_col_maj else (M, N),
                            offset=C_offset,
                            sizes=C_sizes,
                            strides=C_strides,
                        )
                        rt.drain(ov.c[col], (self.C, C_tile), group=tg, wait=True)
                    for tile_row in range(current_tb_n_rows):
                        # A input transfer: the smallest unit is a
                        # (m*n_A_tiles_per_shim)-sized sub-tile, one per column,
                        # repeated (N//n//n_aie_cols) times; each shim carries
                        # separate rows.
                        tile_offset = (
                            (row_base + tile_row) * n_shim_mem_A + col
                        ) % len(A_tiles)
                        # always equal to n_aie_rows since we have n_aie_rows row tiles for matrix A
                        if col < n_aie_rows:
                            for acc in A_fills[tile_offset]:
                                rt.fill(ov.a[col], (self.A, acc), group=tg)
                        # B input transfer: the first (n)-wide block of columns
                        # of B, then the (n_aie_columns)-th such block, and so
                        # on; each shim starts at a different column offset.
                        for acc in B_fills[col]:
                            rt.fill(ov.b[col], (self.B, acc), group=tg)
                if b_unrolled or tb > 0 or (tb == 0 and pingpong > 0):
                    tg.finish()
                    tg = rt.new_group()
        tg.finish()

    # -- host-side helpers ---------------------------------------------------

    def reference(self, A, B):
        """CPU reference: ``C = A @ B`` honoring ``b_col_maj`` / ``c_col_maj``."""
        return reference(A, B, self.ov.b_col_maj, self.ov.c_col_maj)


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(input_a, input_b, b_col_maj=False, c_col_maj=False):
    """CPU reference GEMM ``C = A @ B`` from *stored* inputs (ground truth).

    ``input_b`` is in the operator's storage layout: it is transposed back to
    ``(K, N)`` when ``b_col_maj`` is set before the matmul, and the result is
    transposed to ``(N, M)`` when ``c_col_maj`` is set.
    """
    B = input_b.T if b_col_maj else input_b
    # float32 accumulate, rounded once, as the kernel's f32 accumulator does.
    C = np.matmul(input_a.astype(np.float32), B.astype(np.float32)).astype(
        input_a.dtype
    )
    if c_col_maj:
        C = C.T
    return C
