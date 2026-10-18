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
    (silu(g) * u)`` where ``g`` and ``u`` are the halves of ``gate_up[e] @
    x``, in float32, rounded once. ``ids`` and ``weights`` are
    ``TopKRouter``'s; ``gate_up`` and ``down`` stack the experts as
    transformers holds them.
    """

    reference_only = True

    rows: CompileTime[int] = field()
    hidden: CompileTime[int] = field()
    width: CompileTime[int] = field()
    experts: CompileTime[int] = field()
    top_k: CompileTime[int] = field()
    weights_width: CompileTime[int] = field(derive=lambda op: 2 * op.top_k, repr=False)
    gate_up_width: CompileTime[int] = field(derive=lambda op: 2 * op.width, repr=False)

    x = In(rows, hidden)
    ids = In(rows, top_k, dtype=np.int32)
    weights = In(rows, weights_width)
    gate_up = In(experts, gate_up_width, hidden)
    down = In(experts, hidden, width)
    y = Out(rows, hidden)
    valid = Extent(rows)

    def reference(self, x, ids, weights, gate_up, down):
        x, weights = (np.asarray(a, np.float32) for a in (x, weights))
        y = np.zeros(x.shape, np.float32)
        for r, chosen in enumerate(np.asarray(ids)):
            for j, e in enumerate(chosen):
                g, u = np.split(gate_up[e].astype(np.float32) @ x[r], 2)
                h = g / (1 + np.exp(-g)) * u
                y[r] += weights[r, 2 * j] * (down[e].astype(np.float32) @ h)
        return y.astype(bfloat16)
