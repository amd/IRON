# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses

import numpy as np

import aie.utils as aie_utils
from aie.dialects._aie_enum_gen import AIEArch
from aie.helpers.util import v8bfp16ebs8
from aie.iron.kernels import quant

from iron.common.declare import (
    BoundBuffer,
    In,
    Incompatible,
    Operator,
    Order,
    Out,
    Overlay,
    StreamIn,
    StreamOut,
    Untunable,
    dim,
    operator,
    tunable,
)
from iron.common.image.artifacts import Artifacts, Design, Step
from iron.common.image.jit_compile import insts_design, xclbin_design
from iron.common.tiling import Access

from iron.operators.flm.dequant.design import (
    BFP16_GROUP,
    BLOCK_BYTES,
    CORE_BLOCKS,
    CORE_JOIN_OFFSETS,
    CT_K,
    DRAIN_SIZES,
    DRAIN_STRIDES,
    GROUP,
    HALF_BLOCKS,
    HALVES,
    K_TILE,
    K_TILE_B,
    M_TILE,
    N_TILE,
    ROWS,
    S,
    SLAB_BLOCKS,
    T,
    qw_bytes_for,
    run_geometry,
)

BFP16_GROUP_BYTES = 9


@operator
class FLMDequantOverlay(Overlay):
    """The 4-row grid, as wide as the device, for one q4nx tiling.

    Nothing here depends on K or N: every core loops forever over identical
    per-block work, so one xclbin serves every weight shape. See README.md.
    """

    # The n tile width the packed output is written for. It has to match the
    # tile_n flm.GEMM reads B at, or the GEMM reads the right bytes in the
    # wrong order.
    tile_n: int | None = tunable(None)
    # cols follows the device. ROWS is structural -- it is baked into the
    # split offsets and the join -- so it is not a field; halves is, because
    # a stream's replication count has to be declared to be indexed.
    cols: int | None = tunable(None, repr=False)
    halves: int = tunable(HALVES, repr=False)

    # One q4nx block per core, delivered as one per-column object the cores
    # split; one packed half-tile out per (column, n-half), joined from the
    # two cores that share it.
    qw = StreamIn(ROWS * BLOCK_BYTES, dtype=np.uint8, per=cols, depth=2)
    out = StreamOut(HALF_BLOCKS, dtype=v8bfp16ebs8, per=(cols, halves), depth=2)

    def validate(self) -> None:
        # Not a ValueError: tile_n=128 is a legitimate thing for flm.GEMM to
        # pick, and this operator simply does not emit that order yet.
        if self.tile_n is not None and self.tile_n != N_TILE:
            raise NotImplementedError(
                f"tile_n must be {N_TILE}; this operator emits that order only. "
                f"flm.GEMM picks {self.tile_n} for some shapes, and the two must "
                "agree or the GEMM reads B in the wrong order"
            )

    def tuning(self, dev) -> "FLMDequantOverlay":
        if dev is None:
            raise Untunable(
                "the q4nx dequant grid defaults from the device; none given"
            )
        if dev.arch != AIEArch.AIE2p:
            raise Untunable("bfp16ebs8 exists only on AIE2P")
        return dataclasses.replace(
            self,
            tile_n=N_TILE if self.tile_n is None else self.tile_n,
            cols=dev.cols if self.cols is None else self.cols,
        )

    def config_name(self, dev_name: str) -> str:
        """Stem of the artifacts that do not depend on the shape."""
        return f"FLM_DequantBFP_tn{self.tile_n}_c{self.cols}_{dev_name}"

    def name_parts(self) -> list[str]:
        return [self.config_name(aie_utils.get_current_device().resolve().name)]

    # -- the array -------------------------------------------------------------

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker

        cols = self.cols
        qw_col_ty, out_half_ty = self.qw.tile, self.out.tile
        qw_blk_ty = np.ndarray[(BLOCK_BYTES,), np.dtype[np.uint8]]
        out_blk_ty = np.ndarray[(CORE_BLOCKS,), np.dtype[v8bfp16ebs8]]

        # The factory declares both operands in bytes; the output FIFO carries
        # bfp16ebs8 blocks.
        kernel = quant.q4nx_dequant(
            m_tile=M_TILE, k_tile=K_TILE, group=GROUP, ct_k=CT_K, s=S, t=T
        ).object_file.bind("q4nx_dequant_bfp", [qw_blk_ty, out_blk_ty])

        def core_body(qw_in, out_of, k):
            qw = qw_in.acquire(1)
            out = out_of.acquire(1)
            k(qw, out)
            qw_in.release(1)
            out_of.release(1)

        workers = []
        for c in range(cols):
            of_qw = ObjectFifo(qw_col_ty, name=f"qw_{c}", depth=2)
            self.qw[c].bind(of_qw.prod())
            qw_cores = of_qw.cons().split(
                [BLOCK_BYTES * r for r in range(ROWS)],
                obj_types=[qw_blk_ty] * ROWS,
                names=[f"qw_{c}_{r}" for r in range(ROWS)],
            )

            out_cores = []
            for h in range(HALVES):
                of_out = ObjectFifo(out_half_ty, name=f"w_{c}_{h}", depth=2)
                self.out[c * HALVES + h].bind(of_out.cons())
                out_cores += of_out.prod().join(
                    CORE_JOIN_OFFSETS,
                    obj_types=[out_blk_ty] * (ROWS // HALVES),
                    names=[f"w_{c}_{h}_{r}" for r in range(ROWS // HALVES)],
                )

            # aiecc measures 1216 bytes against the 1024-byte device default.
            workers += [
                Worker(
                    core_body,
                    [qw_cores[r].cons(), out_cores[r].prod(), kernel],
                    stack_size=2048,
                )
                for r in range(ROWS)
            ]
        return workers


@operator
class DequantBFP(Operator[FLMDequantOverlay]):
    """q4nx weights to bfp16, packed the way ``flm.GEMM`` reads B.

    K, N and the interleave are runtime parameters: they move offsets inside
    the instruction stream only, so every shape shares one xclbin. See
    README.md for the layout, the parameters and the constraints.
    """

    K: int = dim()
    N: int = dim()
    # A projection interleaved with another in the same buffer: this one
    # occupies ``run_out_features`` of every ``run_period_out_features``.
    run_out_features: int | None = dim(None)
    run_period_out_features: int | None = dim(None)
    # Each buffer is declared in the unit its transfers count in. The q4nx
    # input is bytes, because a block interleaves three tables at 5 bits per
    # weight and the fill walks it bytewise. The output is bfp16ebs8 blocks,
    # because that is what the drains index -- declaring it in its 9-byte
    # equivalent would make every offset and length address a ninth of what
    # it names. Filled by validate() from K, N and the interleave.
    quantized_bytes: int | None = dim(None, repr=False)
    packed_blocks: int | None = dim(None, repr=False)

    qw = In(quantized_bytes, dtype=np.uint8, to=FLMDequantOverlay.qw)
    out = Out(packed_blocks, dtype=v8bfp16ebs8, from_=FLMDequantOverlay.out)

    # -- legacy accessors ------------------------------------------------------

    @property
    def tile_n(self) -> int:
        return self.ov.tile_n

    @property
    def config_name(self) -> str:
        """Stem of the artifacts that do not depend on the shape: the xclbin's."""
        return self.ov.config_name(aie_utils.get_current_device().resolve().name)

    @property
    def name(self) -> str:
        """Stem of the instruction stream, which does depend on the shape.

        The build cache keys on filename, and ``iron.operators.Dequant`` would
        otherwise share this stem.
        """
        base = f"{self.config_name}_K{self.K}_N{self.N}"
        if self.run_out_features is not None:
            base = f"{base}_run{self.run_out_features}p{self.run_period_out_features}"
        return base

    # -- checks ----------------------------------------------------------------

    def validate(self) -> None:
        self._check_shape(ValueError)
        # Validates the pair and the multiples; the result is used below.
        run_geometry(
            self.run_out_features, self.run_period_out_features, self.N // N_TILE
        )
        for name, computed in (
            ("quantized_bytes", self.quantized_size()),
            ("packed_blocks", self.K * self.N // BFP16_GROUP),
        ):
            declared = getattr(self, name)
            if declared is None:
                setattr(self, name, computed)
            elif declared != computed:
                raise ValueError(
                    f"{name}={declared} does not match K={self.K}, N={self.N} "
                    f"({computed})"
                )

    @staticmethod
    def _check_extents(K, N, error) -> None:
        """The divisibility rule. It names K or N, never the tile_n a caller
        did not pass."""
        if K % K_TILE_B:
            raise error(f"K ({K}) must be a multiple of {K_TILE_B}")
        if N % N_TILE:
            raise error(f"N ({N}) must be a multiple of {N_TILE}")

    def _check_shape(self, error) -> None:
        self._check_extents(self.K, self.N, error)

    def compatible(self) -> None:
        self._check_shape(Incompatible)

    # -- host-side sizes ---------------------------------------------------------

    def packed_size(self) -> int:
        """Bytes the operator writes: 9 per 8 values."""
        return self.K * self.N // BFP16_GROUP * BFP16_GROUP_BYTES

    def quantized_size(self) -> int:
        """Bytes of q4nx input, counting any interleave gap it strides over."""
        return qw_bytes_for(
            self.K, self.N, self.run_out_features, self.run_period_out_features
        )

    # -- the runtime sequence --------------------------------------------------

    def _sweeps(self) -> list[list[tuple[int, int]]]:
        """The column blocks, a device width at a time: per sweep, ``(column,
        column block)`` for every column with a block left."""
        cols, n_blocks = self.ov.cols, self.N // N_TILE
        return [
            [(c, cb0 + c) for c in range(cols) if cb0 + c < n_blocks]
            for cb0 in range(0, n_blocks, cols)
        ]

    def _qw(self, cb: int) -> Access:
        """Column block ``cb``'s q4nx input, read straight through. The block
        is split 10 x 512 so the innermost size stays inside the BD's field."""
        run_blocks, period_blocks = run_geometry(
            self.run_out_features, self.run_period_out_features, self.N // N_TILE
        )
        cb_bytes = N_TILE * self.K * 5 // 8
        offset = ((cb // run_blocks) * period_blocks + cb % run_blocks) * cb_bytes
        return Access(
            self.quantized_size(),
            offset,
            (self.K // K_TILE, 2, BLOCK_BYTES // 512, 512),
            (2 * BLOCK_BYTES, BLOCK_BYTES, 512, 1),
        )

    def _out(self, cb: int, kb: int, h: int) -> Access:
        """Half ``h`` of k-tile ``kb`` of column block ``cb``, packed."""
        k_tiles = self.K // K_TILE_B
        return Access(
            self.K * self.N // BFP16_GROUP,
            (cb * k_tiles + kb) * SLAB_BLOCKS + h * HALF_BLOCKS,
            DRAIN_SIZES,
            DRAIN_STRIDES,
        )

    def order(self, buffer: BoundBuffer) -> Order:
        """Per column, its column block of every sweep: the q4nx block in,
        and each k-tile's half out on each of the column's two halves."""
        ov = self.ov
        sweeps = self._sweeps()
        if buffer is self.qw:
            return Order(
                ov.qw,
                tuple(
                    tuple(
                        self._qw(cb)
                        for sweep in sweeps
                        for col, cb in sweep
                        if col == c
                    )
                    for c in range(ov.cols)
                ),
            )
        k_tiles = self.K // K_TILE_B
        return Order(
            ov.out,
            tuple(
                tuple(
                    self._out(cb, kb, h)
                    for sweep in sweeps
                    for col, cb in sweep
                    if col == c
                    for kb in range(k_tiles)
                )
                for c in range(ov.cols)
                for h in range(HALVES)
            ),
        )

    def design(self, rt):
        """Per sweep: the fills in one group, then each k-tile's drains in a
        group of their own, closing the previous k-tile's as the next runs."""
        ov = self.ov
        k_tiles = self.K // K_TILE_B
        for columns in self._sweeps():
            tg_fill = rt.new_group()
            for c, cb in columns:
                rt.fill(ov.qw[c], (self.qw, self._qw(cb)), group=tg_fill)

            prev = None
            for kb in range(k_tiles):
                tg = rt.new_group()
                for c, cb in columns:
                    for h in range(HALVES):
                        rt.drain(
                            ov.out[c * HALVES + h],
                            (self.out, self._out(cb, kb, h)),
                            wait=True,
                            group=tg,
                        )
                # finish() awaits the group, so closing the previous k-tile
                # here overlaps its wait with this one, already running.
                if prev is not None:
                    prev.finish()
                prev = tg
            prev.finish()
            # The fill is not awaited. A core reads it before it writes the
            # output a drain takes, so a completed drain implies a completed
            # fill.
            tg_fill.finish()

    # -- packaging: one xclbin per configuration ----------------------------------

    @property
    def _reference_shape(self) -> tuple[int, int]:
        """The shape the configuration-only module is emitted at. Its runtime
        sequence is discarded; only its device body reaches the xclbin."""
        return 2 * K_TILE_B, N_TILE * self.ov.cols

    def _build(self):
        """The configuration's xclbin plus this shape's instruction stream.

        Two compiles rather than one, for the same reason as flm.GEMM: the
        xclbin is emitted at a reference shape so every shape sharing the
        configuration reuses it, and only the instruction stream is per shape.
        """
        tuned = self.tuned(aie_utils.get_current_device())
        K, N = tuned._reference_shape
        reference = dataclasses.replace(
            tuned,
            K=K,
            N=N,
            run_out_features=None,
            run_period_out_features=None,
            quantized_bytes=None,
            packed_blocks=None,
        )
        image = xclbin_design(reference.generator(), kernel_name="MLIR_AIE")
        stream = insts_design(self.generator())
        config, own = image.get_cache_entry(), stream.get_cache_entry()
        self._design = stream
        return Artifacts(
            kind="xclbin",
            image=config.xclbin,
            insts=own.insts,
            entry=own,
            designs=(
                Design(
                    name=self.config_name,
                    operators=(self.name,),
                    entry=config,
                    image=config.xclbin,
                    insts=own.insts,
                ),
            ),
            steps=(
                Step(
                    0,
                    self.name,
                    self.config_name,
                    tuple(b.name for b in self._members_io()),
                ),
            ),
            buffers=self.buffer_map(),
        )

    # -- host-side helpers -------------------------------------------------------

    def reference(self, qw):
        """CPU reference, bit-exact against the device."""
        from iron.operators.flm.dequant.reference import reference

        return reference(qw, self.K, self.N)
