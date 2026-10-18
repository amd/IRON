# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Experts: a mixture of experts' feed-forwards, each row through the
experts ``TopKRouter`` chose for it. Reference only: no kernel yet.
"""

import numpy as np
from aie.iron import CompileTime, In, Out
from ml_dtypes import bfloat16

from iron.common import Extent, Operator, field


class Experts(Operator):
    """Row ``r`` of ``x``: the sum over ``j < top_k`` of ``weights[r, 2 * j]``
    times expert ``e = ids[r, j]``'s gated feed-forward, ``down[e] @
    (silu(gate[e] @ x) * (up[e] @ x))``, in float32, rounded once.
    ``ids`` and ``weights`` are ``TopKRouter``'s.
    """

    reference_only = True

    rows: CompileTime[int] = field()
    hidden: CompileTime[int] = field()
    width: CompileTime[int] = field()
    experts: CompileTime[int] = field()
    top_k: CompileTime[int] = field()
    weights_width: CompileTime[int] = field(derive=lambda op: 2 * op.top_k, repr=False)

    x = In(rows, hidden)
    ids = In(rows, top_k, dtype=np.int32)
    weights = In(rows, weights_width)
    gate = In(experts, width, hidden)
    up = In(experts, width, hidden)
    down = In(experts, hidden, width)
    y = Out(rows, hidden)
    valid = Extent(rows)

    def reference(self, x, ids, weights, gate, up, down):
        x, weights = (np.asarray(a, np.float32) for a in (x, weights))
        y = np.zeros(x.shape, np.float32)
        for r, chosen in enumerate(np.asarray(ids)):
            for j, e in enumerate(chosen):
                g = gate[e].astype(np.float32) @ x[r]
                h = g / (1 + np.exp(-g)) * (up[e].astype(np.float32) @ x[r])
                y[r] += weights[r, 2 * j] * (down[e].astype(np.float32) @ h)
        return y.astype(bfloat16)
