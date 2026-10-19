# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SelectiveScan: Mamba2's state space recurrence over a run of rows.
Reference only: no kernel yet.
"""

import numpy as np
from aie.iron import CompileTime, In, Out
from ml_dtypes import bfloat16

from iron.common import Extent, Operator, field


class SelectiveScan(Operator):
    """Each row ``t`` of ``xbc``, split into ``x`` ``(heads, head_dim)``
    and ``groups`` rows each of ``B`` and ``C`` ``(state_size,)``, updates
    each head's state ``(head_dim, state_size)`` and reads it out:

        dt = softplus(dt[t] + dt_bias)
        state = exp(dt * A) * state + dt * outer(x, B)
        y[t] = state @ C + D * x

    head ``h`` reading group ``h // (heads // groups)``'s ``B`` and ``C``.
    ``state`` is the state before the first row; ``final`` the state after
    the last valid one. Float32 throughout, ``y`` rounded once.
    """

    reference_only = True

    rows: CompileTime[int] = field()
    heads: CompileTime[int] = field()
    head_dim: CompileTime[int] = field()
    state_size: CompileTime[int] = field()
    groups: CompileTime[int] = field(default=1)
    inner: CompileTime[int] = field(
        derive=lambda op: op.heads * op.head_dim, repr=False
    )
    width: CompileTime[int] = field(
        derive=lambda op: op.inner + 2 * op.groups * op.state_size, repr=False
    )

    xbc = In(rows, width)
    dt = In(rows, heads)
    dt_bias = In(heads, dtype=np.float32)
    A = In(heads, dtype=np.float32)
    D = In(heads, dtype=np.float32)
    state = In(heads, head_dim, state_size, dtype=np.float32)
    y = Out(rows, inner)
    final = Out(heads, head_dim, state_size, dtype=np.float32)
    valid = Extent(rows)

    def reference(self, xbc, dt, dt_bias, A, D, state):
        H, P, N, G = self.heads, self.head_dim, self.state_size, self.groups
        xbc, dt = np.asarray(xbc, np.float32), np.asarray(dt, np.float32)
        state = np.array(state, np.float32)
        y = np.zeros((self.rows, self.inner), np.float32)
        for t in range(self.valid):
            x = xbc[t, : self.inner].reshape(H, P)
            B, C = (
                np.repeat(m.reshape(G, N), H // G, axis=0)
                for m in np.split(xbc[t, self.inner :], 2)
            )
            step = np.logaddexp(0, dt[t] + dt_bias)[:, None, None]
            state = np.exp(step * A[:, None, None]) * state
            state += step * x[:, :, None] * B[:, None, :]
            y[t] = (np.einsum("hpn,hn->hp", state, C) + D[:, None] * x).reshape(-1)
        return y.astype(bfloat16), state
