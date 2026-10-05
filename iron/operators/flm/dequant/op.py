# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses

import numpy as np
from aie.dialects._aie_enum_gen import AIEArch
from aie.helpers.taplib import TensorAccessPattern
from aie.helpers.util import v8bfp16ebs8
from aie.iron import ObjectFifo, Worker
from aie.iron.kernels import quant

from iron.common import (
    In,
    Incompatible,
    Operator,
    Out,
    Unresolvable,
    auto,
    param,
)
from iron.operators.flm.dequant.design import (
    BFP16_GROUP,
    CORE_BLOCKS,
    CORE_JOIN_OFFSETS,
    CT_K,
    DRAIN_SIZES,
    DRAIN_STRIDES,
    HALF_BLOCKS,
    HALVES,
    K_TILE_B,
    N_TILE,
    ROWS,
    SLAB_BLOCKS,
    S,
    T,
    qw_bytes_for,
    run_geometry,
)
from iron.operators.flm.q4nx import (
    BLOCK_BYTES,
    GROUP,
    K_TILE,
    M_TILE,
    bf16_to_f32,
    packed_bytes,
)

BFP16_GROUP_BYTES = 9
# Out-features one run of code bytes spans.
PARALLEL = 16


def _blocks(qw):
    """The q4nx blob as rows of BLOCK_BYTES."""
    qw = np.asarray(qw, dtype=np.uint8).ravel()
    if qw.size % BLOCK_BYTES:
        raise ValueError(
            f"q4nx blob of {qw.size} bytes is not a whole number of blocks"
        )
    return qw.reshape(-1, BLOCK_BYTES)


def _block_origins(n_blocks, K):
    """(first out-feature, first in-feature) of each block of the blob.

    Block i of the blob is the i'th block that the cores consume: README.md
    layers 6-9.
    """
    k_tiles = K // K_TILE_B
    for i in range(n_blocks):
        cb, rest = divmod(i, 4 * k_tiles)
        kb, rest = divmod(rest, 4)
        k_half, n_half = divmod(rest, 2)
        yield (2 * cb + n_half) * M_TILE, (2 * kb + k_half) * K_TILE


def dequantize(qw, K, N):
    """q4nx blob to f32, shaped (N out-features, K in-features)."""
    b = _blocks(qw)
    n_blocks = len(b)

    n_groups = K_TILE // GROUP
    sm = n_groups * M_TILE * 2
    scales = bf16_to_f32(b[:, :sm].view(np.uint16).reshape(n_blocks, n_groups, M_TILE))
    mins = bf16_to_f32(
        b[:, sm : 2 * sm].view(np.uint16).reshape(n_blocks, n_groups, M_TILE)
    )

    qs = b[:, 2 * sm :].reshape(n_blocks, M_TILE // PARALLEL, K_TILE, PARALLEL // 2)
    q = np.empty((n_blocks, M_TILE // PARALLEL, K_TILE, PARALLEL), dtype=np.float32)
    q[..., 0::2] = (qs & 0xF).astype(np.float32)
    q[..., 1::2] = (qs >> 4).astype(np.float32)
    q = q.transpose(0, 1, 3, 2).reshape(n_blocks, M_TILE, K_TILE)

    grp = np.arange(K_TILE) // GROUP
    s = scales[:, grp, :].transpose(0, 2, 1)
    m = mins[:, grp, :].transpose(0, 2, 1)
    vals = m + s * q

    out = np.empty((N, K), dtype=np.float32)
    for i, (r0, c0) in enumerate(_block_origins(n_blocks, K)):
        out[r0 : r0 + M_TILE, c0 : c0 + K_TILE] = vals[i]
    return out


class DequantBFP(Operator):
    """q4nx weights to bfp16, packed the way ``flm.GEMM`` reads B.

    The array is the 4-row grid, as wide as the device, for one q4nx
    tiling: nothing in it depends on K or N, since every core loops forever
    over identical per-block work, so one xclbin serves every weight shape.
    K, N and the interleave move offsets inside the instruction stream only.
    See README.md for the layout, the parameters and the constraints.
    """

    K: int = param()
    N: int = param()
    # A projection interleaved with another in the same buffer: this one
    # occupies ``run_out_features`` of every ``run_period_out_features``.
    run_out_features: int | None = param(default=None)
    run_period_out_features: int | None = param(default=None)
    # Each buffer is declared in the unit its transfers count in. The q4nx
    # input is bytes, because a block interleaves three tables at 5 bits per
    # weight and the fill walks it bytewise. The output is bfp16ebs8 blocks,
    # because the drains index blocks; declared in its 9-byte equivalent,
    # every offset and length would address a ninth of what it names.
    # Filled by validate() from K, N and the interleave.
    quantized_bytes: int = param(default=lambda op: op.quantized_size(), repr=False)
    packed_blocks: int = param(
        default=lambda op: op.K * op.N // BFP16_GROUP, repr=False
    )
    # The n tile width the packed output is written for. It has to match the
    # tile_n flm.GEMM reads B at, or the GEMM reads the right bytes in the
    # wrong order.
    tile_n: int = auto()
    # cols follows the device. ROWS is baked into the split offsets and the
    # join, so it is not a field; halves is, because a stream's replication
    # count must be declared to be indexed.
    cols: int = auto(repr=False)
    halves: int = auto(HALVES, repr=False)

    # One q4nx block per core, delivered as one per-column object the cores
    # split; one packed half-tile out per (column, n-half), joined from the
    # two cores that share it.
    qw = In(
        quantized_bytes,
        dtype=np.uint8,
        tile=(ROWS * BLOCK_BYTES,),
        per=(cols,),
        depth=2,
    )
    out = Out(
        packed_blocks,
        dtype=v8bfp16ebs8,
        tile=(HALF_BLOCKS,),
        per=(cols, halves),
        depth=2,
    )

    # -- checks ----------------------------------------------------------------

    def validate(self) -> None:
        # NotImplementedError rather than ValueError: flm.GEMM may legitimately
        # pick tile_n=128; this operator does not emit that order yet.
        if self.tile_n is not None and self.tile_n != N_TILE:
            raise NotImplementedError(
                f"tile_n must be {N_TILE}; this operator emits that order only. "
                f"flm.GEMM picks {self.tile_n} for some shapes, and the two must "
                "agree or the GEMM reads B in the wrong order"
            )
        self.check_derived("quantized_bytes", "packed_blocks")
        # Validates the pair and the multiples.
        run_geometry(
            self.run_out_features, self.run_period_out_features, self.N // N_TILE
        )

    def resolve(self, dev):
        if dev is None:
            raise Unresolvable(
                "the q4nx dequant grid defaults from the device; none given"
            )
        if dev.arch != AIEArch.AIE2p:
            raise Unresolvable("bfp16ebs8 exists only on AIE2P")
        return dataclasses.replace(
            self,
            tile_n=N_TILE if self.tile_n is None else self.tile_n,
            cols=dev.cols if self.cols is None else self.cols,
        )

    @staticmethod
    def _check_extents(K, N, error) -> None:
        """The divisibility rule. It names K or N, never the tile_n a caller
        did not pass.
        """
        if K % K_TILE_B:
            raise error(f"K ({K}) must be a multiple of {K_TILE_B}")
        if N % N_TILE:
            raise error(f"N ({N}) must be a multiple of {N_TILE}")

    def compatible(self) -> None:
        self._check_extents(self.K, self.N, Incompatible)

    # -- names -----------------------------------------------------------------

    @property
    def config_name(self) -> str:
        """Stem of the artifacts that do not depend on the shape: the xclbin's."""
        dev = self.dev
        if dev is None:
            raise Unresolvable(
                "FLM dequant: the xclbin is named for a device; none is bound"
            )
        t = self if self._resolved else self.resolved(dev)
        return f"FLM_DequantBFP_tn{t.tile_n}_c{t.cols}_{dev.name}"

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

    # -- the array -------------------------------------------------------------

    def array(self, target) -> list:

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
            self.qw.lane(c).bind(of_qw.prod())
            qw_cores = of_qw.cons().split(
                [BLOCK_BYTES * r for r in range(ROWS)],
                obj_types=[qw_blk_ty] * ROWS,
                names=[f"qw_{c}_{r}" for r in range(ROWS)],
            )

            out_cores = []
            for h in range(HALVES):
                of_out = ObjectFifo(out_half_ty, name=f"w_{c}_{h}", depth=2)
                self.out.lane(c * HALVES + h).bind(of_out.cons())
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

    def sequence(self, rt):
        cols = self.cols
        k_tiles = self.K // K_TILE_B
        blocks_per_row = self.K // K_TILE
        n_blocks = self.N // N_TILE
        out_blocks = self.K * self.N // BFP16_GROUP
        cb_bytes = packed_bytes(N_TILE * self.K)
        qw_bytes = self.quantized_size()
        run_blocks, period_blocks = run_geometry(
            self.run_out_features, self.run_period_out_features, n_blocks
        )

        # A column block is read straight through. The block is split 10 x 512
        # so the innermost size stays inside the BD's field.
        qw_sizes = (blocks_per_row, 2, BLOCK_BYTES // 512, 512)
        qw_strides = (2 * BLOCK_BYTES, BLOCK_BYTES, 512, 1)

        for cb0 in range(0, n_blocks, cols):
            columns = [(c, cb0 + c) for c in range(cols) if cb0 + c < n_blocks]

            tg_fill = rt.new_group()
            for c, cb in columns:
                offset = (
                    (cb // run_blocks) * period_blocks + cb % run_blocks
                ) * cb_bytes
                rt.fill(
                    self.qw.lane(c),
                    TensorAccessPattern((qw_bytes,), offset, qw_sizes, qw_strides),
                    group=tg_fill,
                )

            prev = rt.new_group()  # empty: closed on the first k-tile's turn
            for kb in range(k_tiles):
                tg = rt.new_group()
                for c, cb in columns:
                    for h in range(HALVES):
                        rt.drain(
                            self.out.lane(c * HALVES + h),
                            TensorAccessPattern(
                                (out_blocks,),
                                (cb * k_tiles + kb) * SLAB_BLOCKS + h * HALF_BLOCKS,
                                DRAIN_SIZES,
                                DRAIN_STRIDES,
                            ),
                            wait=True,
                            group=tg,
                        )
                # finish() awaits the group, so closing the previous k-tile
                # here overlaps its wait with this one, already running.
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
        sequence is discarded; only its device body reaches the xclbin.
        """
        return 2 * K_TILE_B, N_TILE * self.cols

    def configuration(self):
        """This configuration at its reference shape: its xclbin serves every
        shape sharing the configuration, and only the instruction stream is
        per shape, as flm.GEMM's.
        """
        K, N = self._reference_shape
        return dataclasses.replace(
            self,
            K=K,
            N=N,
            run_out_features=None,
            run_period_out_features=None,
            quantized_bytes=None,
            packed_blocks=None,
        )

    def reference(self, qw):
        """The bytes the operator must produce from the compact q4nx blob
        ``qw``, as a flat uint8 array: bit-exact against the device, as the
        cores round to bf16 toward negative infinity. See README.md for the
        layout and the rounding.
        """
        K, N = self.K, self.N
        b = _blocks(qw)
        enc = quant.q4nx_dequant_ref(
            b, m_tile=M_TILE, k_tile=K_TILE, group=GROUP, ct_k=CT_K, s=S, t=T
        )
        # Each block's bytes are indexed [k slice, n // T, k // S in the slice,
        # n % T, 9]. Place the blocks in one such array for the whole matrix.
        enc = enc.reshape(len(b), K_TILE // CT_K, M_TILE // T, CT_K // S, T, 9)
        out = np.empty((K // CT_K, N // T, CT_K // S, T, 9), dtype=np.uint8)
        for i, (r0, c0) in enumerate(_block_origins(len(b), K)):
            out[c0 // CT_K : (c0 + K_TILE) // CT_K, r0 // T : (r0 + M_TILE) // T] = (
                enc[i]
            )
        # pack_b's order: (cb, kb, k slice, n // T in cb, k // S in the slice,
        # n % T).
        out = out.reshape(
            K // K_TILE_B, K_TILE_B // CT_K, N // N_TILE, N_TILE // T, CT_K // S, T, 9
        )
        return out.transpose(2, 0, 1, 3, 4, 5, 6).ravel()
