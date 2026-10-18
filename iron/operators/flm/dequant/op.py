# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses

import numpy as np
from aie.dialects._aie_enum_gen import AIEArch
from aie.helpers.taplib import TensorAccessPattern
from aie.helpers.util import v8bfp16ebs8
from aie.iron import ObjectFifo, TaskGroup, Worker
from aie.iron.kernels import quant
from aie.utils import bfp

from iron.common import Auto, Built, In, Operand, Operator, Out, Param, Unresolvable

# flm.GEMM's B tiling, imported rather than restated: this design has to write
# the buffer in the order that one reads it, and two copies would drift.
from iron.operators.flm.gemm.design import CT_MAX_K_FOR_N, S, T
from iron.operators.flm.gemm.design import K_TILE as K_TILE_B
from iron.operators.flm.gemm.design import N_TILE_DEFAULT as N_TILE
from iron.operators.flm.q4nx import (
    BLOCK_BYTES,
    GROUP,
    K_TILE,
    M_TILE,
    packed_bytes,
    parts,
)

CT_K = CT_MAX_K_FOR_N[N_TILE]

# Four cores per column: each takes one n-half and one k-half of the column
# block. The column count is the device's, so it lives on the overlay.
ROWS = 4

CORE_BLOCKS = M_TILE * K_TILE // bfp.BLOCK
SLAB_BLOCKS = N_TILE * K_TILE_B // bfp.BLOCK
HALF_BLOCKS = SLAB_BLOCKS // 2

# One core's contiguous run: every n it owns over one k slice.
RUN = (M_TILE // T) * (CT_K // S) * T
SPLIT = 2


# Core i takes n-half i % 2 and k-half i // 2, so cores 0/1 form the k-half 0
# object and cores 2/3 the k-half 1 object.
CORE_JOIN_OFFSETS = [0, CORE_BLOCKS]
HALVES = 2


def drain_halves(out_blocks):
    """The output's drain, per half slab.

    Args:
        out_blocks: The output's size, in bfp16 blocks.

    Returns:
        The walk over the output's half slabs, indexed by half: each one's
        n-half, k slice, then the core's run, split so the innermost size
        stays inside the BD's field.
    """
    halves = TensorAccessPattern.full(
        (out_blocks // HALF_BLOCKS, K_TILE // CT_K, N_TILE // M_TILE, RUN)
    )
    return halves.permute((0, 2, 1, 3)).split(3, RUN // SPLIT)


def run_geometry(run_out_features, run_period_out_features, n_blocks):
    if run_out_features is None and run_period_out_features is None:
        return n_blocks, n_blocks
    if run_out_features is None or run_period_out_features is None:
        raise ValueError(
            "DequantBFP: run_out_features and run_period_out_features go together"
        )
    for name, v in (
        ("run_out_features", run_out_features),
        ("run_period_out_features", run_period_out_features),
    ):
        if v % N_TILE:
            raise ValueError(f"DequantBFP: {name} ({v}) must be a multiple of {N_TILE}")
    if run_period_out_features < run_out_features:
        raise ValueError(
            f"DequantBFP: run_period_out_features ({run_period_out_features}) "
            f"must be at least run_out_features ({run_out_features})"
        )
    return run_out_features // N_TILE, run_period_out_features // N_TILE


def qw_bytes_for(K, N, run_out_features=None, run_period_out_features=None):
    """Bytes the operator reads, counting any gap it strides over."""
    n_blocks = N // N_TILE
    run_blocks, period_blocks = run_geometry(
        run_out_features, run_period_out_features, n_blocks
    )
    last = n_blocks - 1
    cb = (last // run_blocks) * period_blocks + last % run_blocks + 1
    return packed_bytes(cb * N_TILE * K)


def _blocks(qw):
    """The q4nx blob as rows of BLOCK_BYTES."""
    qw = np.asarray(qw, dtype=np.uint8).ravel()
    if qw.size % BLOCK_BYTES:
        raise ValueError(
            f"DequantBFP: a q4nx blob of {qw.size} bytes is not a whole number of blocks"
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
    codes, scales, mins = parts(_blocks(qw))
    grp = np.arange(K_TILE) // GROUP
    vals = mins[..., grp] + scales[..., grp] * codes
    out = np.empty((N, K), dtype=np.float32)
    for i, (r0, c0) in enumerate(_block_origins(len(vals), K)):
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

    K: int = Param()
    N: int = Param()
    # A projection interleaved with another in the same buffer: this one
    # occupies ``run_out_features`` of every ``run_period_out_features``.
    run_out_features: int | None = Param(default=None)
    run_period_out_features: int | None = Param(default=None)
    # Each buffer is declared in the unit its transfers count in. The q4nx
    # input is bytes, because a block interleaves three tables at 5 bits per
    # weight and the fill walks it bytewise. The output is bfp16ebs8 blocks,
    # because the drains index blocks; declared in its 9-byte equivalent,
    # every offset and length would address a ninth of what it names.
    # Filled by validate() from K, N and the interleave.
    quantized_bytes: int = Param(derive=lambda op: op.quantized_size(), repr=False)
    packed_blocks: int = Param(derive=lambda op: op.K * op.N // bfp.BLOCK, repr=False)
    # cols follows the device. ROWS is baked into the split offsets and the
    # join, so it is not a field; halves is, because a stream's replication
    # count must be declared to be indexed, but the join bakes it too.
    cols: int = Auto(repr=False)
    halves: int = Auto(default=HALVES, repr=False, init=False)

    # One q4nx block per core, delivered as one per-column object the cores
    # split; one packed half-tile out per (column, n-half), joined from the
    # two cores that share it.
    qw = In(
        quantized_bytes,
        dtype=np.uint8,
        obj_type=(ROWS * BLOCK_BYTES,),
        per=(cols,),
        depth=2,
    )
    out = Out(
        packed_blocks,
        dtype=v8bfp16ebs8,
        obj_type=(HALF_BLOCKS,),
        per=(cols, halves),
        depth=2,
    )

    def validate(self) -> None:
        self.check_derived("quantized_bytes", "packed_blocks")
        # Validates the pair and the multiples.
        run_geometry(
            self.run_out_features, self.run_period_out_features, self.N // N_TILE
        )

    def resolve(self, dev):
        if dev is None:
            raise Unresolvable(
                "DequantBFP: the q4nx dequant grid defaults from the device; none given"
            )
        if dev.arch != AIEArch.AIE2p:
            raise Unresolvable("DequantBFP: bfp16ebs8 exists only on AIE2P")
        return dataclasses.replace(
            self,
            cols=dev.cols if self.cols is None else self.cols,
        )

    def compatible(self) -> None:
        if self.K % K_TILE_B:
            raise ValueError(
                f"DequantBFP: K ({self.K}) must be a multiple of {K_TILE_B}"
            )
        if self.N % N_TILE:
            raise ValueError(f"DequantBFP: N ({self.N}) must be a multiple of {N_TILE}")

    @property
    def config_name(self) -> str:
        """Stem of the artifacts that do not depend on the shape: the xclbin's."""
        dev = self.dev
        if dev is None:
            raise Unresolvable(
                "DequantBFP: the xclbin is named for a device; none is bound"
            )
        t = self if self._resolved else self.resolved(dev)
        return f"FLM_DequantBFP_tn{N_TILE}_c{t.cols}_{dev.name}"

    @property
    def name(self) -> str:
        """The configuration's stem, then the shape: two instruction streams
        never share a name.
        """
        base = f"{self.config_name}_K{self.K}_N{self.N}"
        if self.run_out_features is not None:
            base = f"{base}_run{self.run_out_features}p{self.run_period_out_features}"
        return base

    class Array(Operator.Array):
        cols: int
        halves: int
        qw: Operand
        out: Operand

        def build(self) -> Built:
            cols = self.cols
            qw_col_ty, out_half_ty = self.qw.obj_type, self.out.obj_type
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

            workers, qws, outs = [], [], []
            for c in range(cols):
                of_qw = ObjectFifo(qw_col_ty, depth=2)
                qws.append(of_qw.prod())
                qw_cores = of_qw.cons().split(
                    [BLOCK_BYTES * r for r in range(ROWS)],
                    obj_types=[qw_blk_ty] * ROWS,
                )

                out_cores = []
                for h in range(HALVES):
                    of_out = ObjectFifo(out_half_ty, depth=2)
                    outs.append(of_out.cons())
                    out_cores += of_out.prod().join(
                        CORE_JOIN_OFFSETS,
                        obj_types=[out_blk_ty] * (ROWS // HALVES),
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
            self.qw.bind(qws)
            self.out.bind(outs)
            return Built(workers)

    def quantized_size(self) -> int:
        """Bytes of q4nx input, counting any interleave gap it strides over."""
        return qw_bytes_for(
            self.K, self.N, self.run_out_features, self.run_period_out_features
        )

    def sequence(self, rt):
        cols = self.cols
        k_tiles = self.K // K_TILE_B
        blocks_per_row = self.K // K_TILE
        n_blocks = self.N // N_TILE
        out_blocks = self.K * self.N // bfp.BLOCK
        cb_bytes = packed_bytes(N_TILE * self.K)
        qw_bytes = self.quantized_size()
        run_blocks, period_blocks = run_geometry(
            self.run_out_features, self.run_period_out_features, n_blocks
        )

        # A column block is read straight through. The block is split 10 x 512
        # so the innermost size stays inside the BD's field.
        qw = TensorAccessPattern.full(
            (qw_bytes // cb_bytes, blocks_per_row, 2, BLOCK_BYTES // 512, 512)
        )
        out = drain_halves(out_blocks)

        for cb0 in range(0, n_blocks, cols):
            columns = [(c, cb0 + c) for c in range(cols) if cb0 + c < n_blocks]

            tg_fill = TaskGroup()
            for c, cb in columns:
                at = (cb // run_blocks) * period_blocks + cb % run_blocks
                self.qw.fill(qw[at], lane=c, group=tg_fill)

            # Each k-tile's drains are awaited while the next one's run.
            for kb, tg in TaskGroup.pipelined(k_tiles, depth=2):
                for c, cb in columns:
                    for h in range(HALVES):
                        self.out.drain(
                            out[(cb * k_tiles + kb) * HALVES + h],
                            lane=c * HALVES + h,
                            wait=True,
                            group=tg,
                        )
            # The fill is not awaited. A core reads it before it writes the
            # output a drain takes, so a completed drain implies a completed
            # fill.
            tg_fill.finish()

    @property
    def _reference_shape(self) -> tuple[int, int]:
        """The shape the configuration-only module is emitted at. Its runtime
        sequence is discarded; only its device body reaches the xclbin.
        """
        return 2 * K_TILE_B, N_TILE * self.cols

    def xclbin_operator(self):
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
            out[c0 // CT_K : (c0 + K_TILE) // CT_K, r0 // T : (r0 + M_TILE) // T] = enc[
                i
            ]
        # pack_b's order: (cb, kb, k slice, n // T in cb, k // S in the slice,
        # n % T).
        out = out.reshape(
            K // K_TILE_B, K_TILE_B // CT_K, N // N_TILE, N_TILE // T, CT_K // S, T, 9
        )
        return out.transpose(2, 0, 1, 3, 4, 5, 6).ravel()
