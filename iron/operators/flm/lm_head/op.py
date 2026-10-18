# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import functools

import numpy as np
from aie.dialects._aie_enum_gen import AIEArch
from aie.iron import CompileTime, In, Out
from aie.iron.kernels import flm_gemma4
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Auto, Operator, Unresolvable, field
from iron.common.testing import Case, Testing
from iron.operators.flm.lm_head import reference
from iron.operators.flm.lm_head.design import lm_head
from iron.operators.flm.q4nx import GROUP, K_TILE, M_TILE, packed_bytes

# Error bounds from README.md's Numerics section.
PROJECTION_ERROR = 0.025
TANH_ERROR = 0.04

GEMMA4_SOFTCAP = 30.0


def _draw(op):
    """A q4nx vocabulary and a token with its RMS weight.

    Negative minima and small scales keep the logits in the range a softcap
    of 30 bends.
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
    """Softcapped logits from a q4nx vocabulary, with the RMS norm folded in.

    ``dim`` in-features, ``vocab`` out-features, ``softcap`` the tanh bound.
    X holds the token followed by its RMS weight. W holds the q4nx vocabulary.
    Y receives the logits. See README.md.
    """

    test = Testing(
        [
            # Gemma 4 E2B's and E4B's hidden sizes.
            Case(dict(dim=1536, vocab=4096, softcap=GEMMA4_SOFTCAP)),
            Case(dict(dim=2560, vocab=4096, softcap=GEMMA4_SOFTCAP)),
            # A softcap of 5 saturates most logits.
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

    dim: CompileTime[int] = field()
    vocab: CompileTime[int] = field()
    softcap: CompileTime[float] = field()
    w_words: CompileTime[int] = field(
        derive=lambda op: packed_bytes(op.vocab * op.dim) // 4, repr=False
    )
    x_len: CompileTime[int] = field(derive=lambda op: 2 * op.dim, repr=False)
    cols: CompileTime[int] = Auto(repr=False)
    rows: CompileTime[int] = Auto(repr=False)

    # The runtime sequence's argument order.
    y = Out(vocab, dtype=bfloat16)
    w = In(w_words, dtype=np.uint32)
    x = In(x_len, dtype=bfloat16)

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
        return dataclasses.replace(
            self,
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

    def exported_design(self):
        kernel = flm_gemma4.flm_gemma4_q4nx_lm_head(
            dim=self.dim, m_tile=M_TILE, k_tile=K_TILE, group=GROUP
        )
        return functools.partial(
            lm_head,
            self.dev,
            self.dim,
            self.vocab,
            self.softcap,
            lm_head_kernel=kernel,
        )

    def tolerance(self) -> Tolerance:
        return Tolerance(
            bound=lambda w, x: self.projection_error(w, x) + TANH_ERROR * self.softcap,
            note="README.md's Numerics section",
        )

    def projection_error(self, w, x) -> float:
        """The bound on the projection's error: a share of the largest logit
        before the softcap.
        """
        uncapped = type(self)(dim=self.dim, vocab=self.vocab, softcap=1e30)
        return PROJECTION_ERROR * np.abs(uncapped.reference(w, x)).max()

    def reference(self, w, x):
        """The softcapped logits of X for W, in float64."""
        weights = reference.dequantize(w, self.dim, self.vocab, self.resolved().rows)
        return reference.reference(weights, np.asarray(x, np.float64), self.softcap)
