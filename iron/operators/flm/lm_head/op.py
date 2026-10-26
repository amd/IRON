# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses

import numpy as np
from aie.dialects._aie_enum_gen import AIEArch
from aie.helpers.npdtypes import np_ndarray_type_get_shape
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, In, ObjectFifo, Out, TaskGroup, Worker
from aie.iron.controlflow import range_
from aie.iron.device import Tile
from aie.iron.kernels import flm_gemma4
from aie.utils.verify import Tolerance
from aie.utils.compile.jit.params import param, tunable, widths
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Unresolvable
from iron.common.testing import Case, Testing
from iron.operators.flm.lm_head import reference
from iron.operators.flm.q4nx import BLOCK_BYTES, GROUP, K_TILE, M_TILE, packed_bytes

# Error bounds from README.md's Numerics section.
PROJECTION_ERROR = 0.025
TANH_ERROR = 0.04

GEMMA4_SOFTCAP = 30.0

# The sequence finishes each round's TaskGroup DEPTH rounds later. The finish
# frees the round's BDs for the bd-id allocator. A shim tile holds 16 BDs.
DEPTH = 2


@dataclasses.dataclass(frozen=True, kw_only=True)
class _Built(Built):
    """LMHead's build, with each core's softcap word for ``sequence()`` to write."""

    softcaps: list[Buffer]


def _draw(op):
    """A q4nx vocabulary and a token with its RMS weight: negative minima and
    small scales keep the logits in the range a softcap of 30 bends.
    """
    rng = np.random.default_rng(1)
    groups = K_TILE // GROUP
    n_blocks = op.vocab * op.dim // (M_TILE * K_TILE)
    params = np.concatenate(
        [
            rng.uniform(0, 0.02, (n_blocks, groups * M_TILE)),
            rng.uniform(-0.15, 0, (n_blocks, groups * M_TILE)),
        ],
        axis=1,
    )
    params = params.astype(bfloat16).view(np.uint8)
    codes = rng.integers(0, 256, (n_blocks, M_TILE * K_TILE // 2), dtype=np.uint8)
    w = np.concatenate([params, codes], axis=1).view(np.uint32).reshape(-1)
    x = np.concatenate([rng.standard_normal(op.dim), rng.uniform(0.5, 1.5, op.dim)])
    return dict(given={op.w: w, op.x: x.astype(bfloat16)})


class LMHead(Operator):
    """Softcapped logits from a q4nx vocabulary, with the RMS norm folded in:
    ``x`` holds the token then its RMS weight, ``w`` the q4nx vocabulary,
    ``y`` the logits. See README.md.
    """

    test = Testing(
        [
            # Gemma 4 E2B's and E4B's hidden sizes.
            Case(dict(dim=1536, vocab=4096, softcap=GEMMA4_SOFTCAP)),
            Case(dict(dim=2560, vocab=4096, softcap=GEMMA4_SOFTCAP)),
            # A softcap of 5 bends every logit and saturates the largest.
            Case(dict(dim=1536, vocab=1024, softcap=5.0)),
            # Gemma 4's whole vocabulary.
            Case(
                dict(dim=1536, vocab=262144, softcap=GEMMA4_SOFTCAP),
                extensive=True,
                bench=True,
            ),
            Case(dict(dim=2560, vocab=262144, softcap=GEMMA4_SOFTCAP), extensive=True),
        ],
        draw=_draw,
    )

    dim: int = param(array=True)
    vocab: int = param(array=True)
    softcap: float = param()
    w_words: int = param(
        derive=lambda op: packed_bytes(op.vocab * op.dim) // 4, repr=False
    )
    x_len: int = param(derive=lambda op: 2 * op.dim, repr=False)
    cols: int = tunable(repr=False, domain=widths)
    rows: int = tunable(repr=False)

    # The runtime sequence's argument order. A w or y column object holds one
    # block per core row, which the cores split or join. One broadcast sends
    # the token and its RMS weight to every core.
    y = Out(vocab, dtype=bfloat16, obj_shape=(rows, M_TILE), per=(cols,))
    w = In(w_words, dtype=np.uint32, obj_shape=(rows, BLOCK_BYTES // 4), per=(cols,))
    x = In(x_len, dtype=bfloat16, obj_shape=(x_len,))

    def validate(self) -> None:
        if self.dim % K_TILE:
            raise ValueError(f"LMHead: dim ({self.dim}) must be a multiple of {K_TILE}")
        if not (np.isfinite(self.softcap) and self.softcap > 0):
            raise ValueError(
                f"LMHead: softcap ({self.softcap}) must be finite and positive"
            )

    def resolve(self, dev):
        if dev is None:
            raise Unresolvable(
                "LMHead: the LM head's grid defaults from the device; none given"
            )
        if dev.arch != AIEArch.AIE2p:
            raise Unresolvable("LMHead: the q4nx_lm_head kernel is AIE2P only")
        return self.replace(
            cols=dev.cols if self.cols is None else self.cols,
            rows=len(dev.core_rows) if self.rows is None else self.rows,
        )

    def compatible(self) -> None:
        per_round = self.cols * self.rows * M_TILE
        if self.vocab % per_round:
            raise ValueError(
                f"LMHead: vocab ({self.vocab}) must be a multiple of {per_round}, "
                "the out-features one round produces"
            )

    def ops(self) -> int:
        return 2 * self.vocab * self.dim

    def build(self) -> Built:
        """Each core RMS-normalizes the token once. Each round, it
        accumulates one weight block per K_TILE in-features into M_TILE
        out-features and applies the tanh softcap to the sums.
        """
        cols, rows, dim = self.cols, self.rows, self.dim
        rounds = self.vocab // (cols * rows * M_TILE)
        kernel = flm_gemma4.flm_gemma4_q4nx_lm_head(
            dim=dim, m_tile=M_TILE, k_tile=K_TILE, group=GROUP
        )
        # The kernels' argument types are the x and w fifos' element types
        # and the core-local scratch.
        w_blk_ty, x_ty, y_acc_ty, sums_ty, _ = kernel.q4nx_lm_head_block.arg_types()
        y_blk_ty, _, rtp_ty = kernel.q4nx_lm_head_epilogue.arg_types()
        # The w fifos move the host's words as bf16 elements. The kernel
        # reinterprets the bytes.
        (w_blk,) = np_ndarray_type_get_shape(w_blk_ty)
        w_col_ty = np.ndarray[(rows, w_blk), np.dtype[bfloat16]]

        def core_fn(x_in, w_in, y_out, k_rms, k_zero, k_block, k_epi, y_acc, sums, rtp):
            x = x_in.acquire(1)
            k_rms(x, sums)
            for _ in range_(rounds):
                k_zero(y_acc)
                for k in range_(dim // K_TILE):
                    w = w_in.acquire(1)
                    k_block(w, x, y_acc, sums, k)
                    w_in.release(1)
                y = y_out.acquire(1)
                k_epi(y, y_acc, rtp)
                y_out.release(1)
            x_in.release(1)

        # The host addresses the DMAs by column. The build therefore pins
        # the shim tiles. The placer places the other tiles.
        shim = [Tile(j, 0) for j in range(cols)]
        of_x = ObjectFifo(x_ty)
        self.x.bind(of_x.prod(tile=shim[0]))

        workers, ws, ys, softcaps = [], [], [], []
        for j in range(cols):
            of_w = ObjectFifo(w_col_ty)
            ws.append(of_w.prod(tile=shim[j]))
            w_cores = of_w.cons().split(
                [w_blk * i for i in range(rows)],
                obj_types=[w_blk_ty] * rows,
                names=[f"w{j}_{i}" for i in range(rows)],
            )

            of_y = ObjectFifo(self.y.obj_type)
            ys.append(of_y.cons(tile=shim[j]))
            y_cores = of_y.prod().join(
                [M_TILE * i for i in range(rows)],
                obj_types=[y_blk_ty] * rows,
                names=[f"y{j}_{i}" for i in range(rows)],
            )

            for i in range(rows):
                y_acc = Buffer(type=y_acc_ty, name=f"yacc_{i}_{j}")
                sums = Buffer(type=sums_ty, name=f"sums_{i}_{j}")
                rtp = Buffer(type=rtp_ty, name=f"rtp_{i}_{j}", use_write_rtp=True)
                softcaps.append(rtp)
                workers.append(
                    Worker(
                        core_fn,
                        [
                            of_x.cons(),
                            w_cores[i].cons(),
                            y_cores[i].prod(),
                            kernel.q4nx_lm_head_rms,
                            kernel.q4nx_lm_head_zero,
                            kernel.q4nx_lm_head_block,
                            kernel.q4nx_lm_head_epilogue,
                            y_acc,
                            sums,
                            rtp,
                        ],
                    )
                )
        self.w.bind(ws)
        self.y.bind(ys)
        return _Built(workers, softcaps=softcaps)

    def sequence(self, rt):
        # npu_write_rtp writes i32 words. The softcap travels as its f32 bit
        # pattern.
        for rtp in rt.built.softcaps:
            rtp[0] = int(np.float32(self.softcap).view(np.int32))

        # The broadcast has no completion token. x.free() frees its BD at the end.
        x = self.x.fill(managed=False)

        rounds = self.vocab // (self.cols * self.rows * M_TILE)
        n = rounds * self.cols
        # Tap i covers round i // cols of column i % cols. A strided
        # descriptor places weight rows at the wrong on-chip positions, so
        # each column reads one contiguous slice of w.
        y_taps = TensorAccessPattern.full((self.vocab,)).partition(n)
        w_taps = TensorAccessPattern.full((self.w_words,)).partition(n)
        window = []
        for rnd in range(rounds):
            tg = TaskGroup()
            for col in range(self.cols):
                i = rnd * self.cols + col
                self.y.drain(y_taps[i], lane=col, wait=True, group=tg)
                self.w.fill(w_taps[i], lane=col, group=tg)
            window.append(tg)
            if len(window) > DEPTH:
                window.pop(0).finish()
        for tg in window:
            tg.finish()
        x.free()

    def tolerance(self) -> Tolerance:
        return Tolerance.bounded(
            lambda w, x: self.projection_error(w, x) + TANH_ERROR * self.softcap,
            note="README.md's Numerics section",
        )

    def projection_error(self, w, x) -> float:
        """The bound on the projection's error: a share of the largest logit
        before the softcap.
        """
        uncapped = type(self)(dim=self.dim, vocab=self.vocab, softcap=1e30)
        return PROJECTION_ERROR * float(np.abs(uncapped.reference(w, x)).max())

    def reference(self, w, x):
        """The softcapped logits of X for W, computed in float64 and rounded
        to Y's bf16.
        """
        weights = reference.dequantize(w, self.dim, self.vocab, self.resolved().rows)
        logits = reference.reference(weights, np.asarray(x, np.float64), self.softcap)
        return logits.astype(bfloat16)
