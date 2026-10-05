# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import functools

import numpy as np
from aie.dialects._aie_enum_gen import AIEArch
from aie.iron.kernels import flm_gemma4
from ml_dtypes import bfloat16

from iron.common import (
    In,
    Incompatible,
    Operator,
    Out,
    Unresolvable,
    auto,
    param,
)
from iron.operators.flm.lm_head import reference
from iron.operators.flm.lm_head.design import lm_head
from iron.operators.flm.q4nx import GROUP, K_TILE, M_TILE, packed_bytes


class LMHead(Operator):
    """Softcapped logits from a q4nx vocabulary, with the RMS norm folded in.

    ``dim`` in-features, ``vocab`` out-features, ``softcap`` the tanh bound.
    X holds the token followed by its RMS weight. W holds the q4nx vocabulary.
    Y receives the logits. See README.md.
    """

    dim: int = param()
    vocab: int = param()
    softcap: float = param()
    w_words: int = param(
        default=lambda op: packed_bytes(op.vocab * op.dim) // 4, repr=False
    )
    x_len: int = param(default=lambda op: 2 * op.dim, repr=False)
    cols: int = auto(repr=False)
    rows: int = auto(repr=False)

    # The runtime sequence's argument order.
    y = Out(vocab, dtype=bfloat16)
    w = In(w_words, dtype=np.uint32)
    x = In(x_len, dtype=bfloat16)

    def validate(self) -> None:
        if self.dim % K_TILE:
            raise ValueError(f"dim ({self.dim}) must be a multiple of {K_TILE}")
        if not (np.isfinite(self.softcap) and self.softcap > 0):
            raise ValueError(f"softcap ({self.softcap}) must be finite and positive")
        self.check_derived("w_words", "x_len")

    def resolve(self, dev):
        if dev is None:
            raise Unresolvable("the LM head's grid defaults from the device; none given")
        if dev.arch != AIEArch.AIE2p:
            raise Unresolvable("the q4nx_lm_head kernel is AIE2P only")
        return dataclasses.replace(
            self,
            cols=dev.cols if self.cols is None else self.cols,
            rows=len(dev.core_rows) if self.rows is None else self.rows,
        )

    def compatible(self) -> None:
        per_round = self.cols * self.rows * M_TILE
        if self.vocab % per_round:
            raise Incompatible(
                f"vocab ({self.vocab}) must be a multiple of {per_round}, "
                "the out-features one round produces"
            )

    def ops(self) -> int:
        return 2 * self.vocab * self.dim

    def exported_design(self, image: str):
        kernel = flm_gemma4.flm_gemma4_q4nx_lm_head(
            dim=self.dim, m_tile=M_TILE, k_tile=K_TILE, group=GROUP
        )
        return functools.partial(
            lm_head, self.dev, self.dim, self.vocab, self.softcap, 0, lm_head_kernel=kernel
        )

    def reference(self, w, x):
        """The softcapped logits of X for W, in float64."""
        op = self.resolved()
        weights = reference.dequantize(w, self.dim, self.vocab, op.cols, op.rows)
        return reference.reference(weights, np.asarray(x, np.float64), self.softcap)
