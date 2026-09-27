# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3 on the NPU: its layer and head over the shared decoder
(:class:`~iron.applications.common.CausalLM`).

The operators' knobs are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Llama 3.2 1B's shape and a ``max_seq_len`` of
2048. A call site gives a knob only where two operators of one shape want
different ones.
"""

from pathlib import Path

import numpy as np

from iron.applications.common import CausalLM, project
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv.op import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.silu import SiLU


class Llama(CausalLM):
    """Llama 3 on ``config``'s shape and ``weights`` (``embedding``, which is
    the output head too, ``norm`` and ``layers``). Every matrix is read
    ``(out, in)``, as the checkpoint ships it: GEMV's ``(M, K)`` and GEMM's
    column-major B.
    """

    profile = Path(__file__).with_name("profiles")
    norm: np.ndarray

    def layer(self, step, i, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        h = RMSNorm(x, w.norm1)
        # Half a head per tile for one row; q's shape is o's when H * D is
        # the width, so it is given here rather than by the profile.
        q, k, v = (project(h, p, tile_size_output=D // 2) for p in (w.q, w.k, w.v))
        # One angle row per position, applied to that position's heads.
        q = RoPE(q.reshape(n * H, D), step.angles)
        k = RoPE(k.reshape(n * G, D), step.angles)
        x = ElementwiseAdd(x, project(self.attend(step, i, q, k, v), w.o))
        h = RMSNorm(x, w.norm2)
        gate, up = project(h, w.gate), project(h, w.up)
        return ElementwiseAdd(x, project(ElementwiseMul(SiLU(gate), up), w.down))

    def head(self, x):
        return GEMV(self.embedding, RMSNorm(x, self.norm))
