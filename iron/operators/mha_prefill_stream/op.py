# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import In, Out
from aie.utils.compile.jit.params import param
from aie.utils.compile.utils import resolve_target_arch
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common.stream.operator import StreamOperator
from iron.common.testing import Case, Testing

# The workload's layers, in the order they run, and the tensor each produces
# for the next.
SCORES, SOFTMAX, CONTEXT = "Attn_Scores", "Attn_Softmax", "Attn_Context"
LAYERS = (SCORES, SOFTMAX, CONTEXT)
RESULTS = {SCORES: "scores", SOFTMAX: "probs"}


class MHAPrefillStream(StreamOperator):
    """Flash attention ``softmax(q @ k_t) @ v`` for every head, as stream-dse places it.

    Over a pre-scaled ``q`` (by ``1 / sqrt(d_head)``) and a pre-transposed
    ``k_t``, heads leading; one fused group whose key axis runs in the
    flash kernels' block, causal unless ``causal`` is False. ``query_block``
    pins the query block; None leaves it to stream-dse's tile search. See
    README.md.
    """

    test = Testing(
        [
            Case(dict(heads=32, seq_len=256), bench=True),
            Case(dict(heads=32, seq_len=2048), extensive=True),
            Case(dict(heads=32, seq_len=1024, d_head=128), extensive=True),
            Case(dict(heads=32, seq_len=1024, causal=False), extensive=True),
        ],
        draw=lambda op: dict(normal=(op.q, op.k_t, op.v), scale=op.d_head**-0.25),
    )

    heads: int = param()
    seq_len: int = param()
    d_head: int = param(default=64)
    causal: bool = param(default=True)
    query_block: int | None = param(default=None)

    q = In(heads, seq_len, d_head, dtype=bfloat16)
    k_t = In(heads, d_head, seq_len, dtype=bfloat16)
    v = In(heads, seq_len, d_head, dtype=bfloat16)
    output = Out(heads, seq_len, d_head, dtype=bfloat16)

    def key_blocks(self) -> tuple[int, ...]:
        """Return the key blocks the flash kernels compile, finest first."""
        from iron.common.stream.kernel_library import blocks

        return blocks(resolve_target_arch(self.dev), "matmul_PV", "k")

    def query_blocks(self) -> tuple[int, ...]:
        """Return the query blocks the flash kernels compile, finest first."""
        from iron.common.stream.kernel_library import blocks

        return blocks(resolve_target_arch(self.dev), "partial_softmax", "m")

    def compatible(self) -> None:
        from iron.common.stream.kernel_library import load_library

        head = load_library(resolve_target_arch(self.dev)).spec("matmul_PV").dim("n")
        if not head.accepts(self.d_head):
            raise ValueError(
                f"MHAPrefillStream: d_head ({self.d_head}) is not a head "
                "matmul_PV compiles"
            )
        if self.seq_len % self.key_blocks()[-1]:
            raise ValueError(
                f"MHAPrefillStream: seq_len ({self.seq_len}) must be a multiple of "
                f"{self.key_blocks()[-1]}"
            )
        if self.query_block is not None and self.query_block not in self.query_blocks():
            raise ValueError(
                f"MHAPrefillStream: query_block ({self.query_block}) must be one of "
                f"{self.query_blocks()}"
            )

    def workload(self):
        from .design import workload

        return workload(self.heads, self.seq_len, self.d_head)

    def candidates(self):
        from .design import mapping

        seed = self.query_block or self.query_blocks()[0]
        return [mapping(seed, self.key_blocks()[-1], self.d_head, self.causal)]

    def library(self):
        from iron.common.stream.kernel_library import pinned_to_block

        if self.query_block is None:
            return super().library()
        return pinned_to_block(resolve_target_arch(self.dev), self.query_block)

    def layers(self):
        return LAYERS

    def ops(self) -> int:
        # The score and context products; causal, about half of each is computed.
        full = 4 * self.heads * self.seq_len * self.seq_len * self.d_head
        return full // 2 if self.causal else full

    def reference(self, q, k_t, v):
        """Return each head's attention in float32, causal if the operator is."""
        q, k_t, v = (np.asarray(t, dtype=np.float32) for t in (q, k_t, v))
        scores = q @ k_t
        if self.causal:
            future = np.triu(np.ones(scores.shape[-2:], dtype=bool), k=1)
            scores = np.where(future, -np.inf, scores)
        p = np.exp(scores - scores.max(axis=-1, keepdims=True))
        return (p / p.sum(axis=-1, keepdims=True)) @ v

    def tolerance(self) -> Tolerance:
        return Tolerance(
            rtol=0.04,
            atol=0.15,
            max_mismatch_frac=0.005,
            note="MHA's: rtol about the softmax contract's aie::exp2 envelope; "
            "atol and the mismatch share set by hand",
        )
