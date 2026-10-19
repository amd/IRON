# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GatedDeltaRule: Gated DeltaNet's recurrence over a run of rows."""

import numpy as np
from aie.iron import CompileTime, In, Out
from ml_dtypes import bfloat16

from iron.common import Extent, Operator, field


class GatedDeltaRule(Operator):
    """Each row ``t`` of ``qkv``, split into ``q`` and ``k`` ``(k_heads,
    key_dim)`` and ``v`` ``(v_heads, value_dim)``, updates each value head's
    state ``(key_dim, value_dim)`` and reads it out:

        q, k = q / |q| / sqrt(key_dim), k / |k|
        g = A * softplus(a[t] + dt_bias), beta = sigmoid(b[t])
        state = exp(g) * state
        state += outer(k, beta * (v - k @ state))
        y[t] = q @ state

    value head ``h`` reading key head ``h // (v_heads // k_heads)``'s ``q``
    and ``k``, and its ``(dt_bias, A)`` from ``head``. ``state`` is the
    state before the first row; ``final`` the state after the last valid
    one. Float32 throughout, ``y`` rounded once. No kernel yet.
    """

    reference_only = True

    rows: CompileTime[int] = field()
    k_heads: CompileTime[int] = field()
    v_heads: CompileTime[int] = field()
    key_dim: CompileTime[int] = field()
    value_dim: CompileTime[int] = field()
    width: CompileTime[int] = field(
        derive=lambda op: 2 * op.k_heads * op.key_dim + op.v_heads * op.value_dim,
        repr=False,
    )
    inner: CompileTime[int] = field(
        derive=lambda op: op.v_heads * op.value_dim, repr=False
    )

    qkv = In(rows, width)
    a = In(rows, v_heads)
    b = In(rows, v_heads)
    head = In(v_heads, 2, dtype=np.float32)
    state = In(v_heads, key_dim, value_dim, dtype=np.float32)
    y = Out(rows, inner)
    final = Out(v_heads, key_dim, value_dim, dtype=np.float32)
    valid = Extent(rows)

    def validate(self) -> None:
        if self.v_heads % self.k_heads:
            raise ValueError(
                f"GatedDeltaRule: v_heads ({self.v_heads}) must be whole "
                f"groups of k_heads ({self.k_heads})"
            )

    def reference(self, qkv, a, b, head, state):
        K, V, Dk = self.k_heads, self.v_heads, self.key_dim
        qkv, a, b = (np.asarray(m, np.float32) for m in (qkv, a, b))
        dt_bias, A = np.asarray(head, np.float32).T
        state = np.array(state, np.float32)
        y = np.zeros((self.rows, self.inner), np.float32)
        for t in range(self.valid):
            q, k = (
                np.repeat(m.reshape(K, Dk), V // K, axis=0)
                for m in np.split(qkv[t, : 2 * K * Dk], 2)
            )
            v = qkv[t, 2 * K * Dk :].reshape(V, self.value_dim)
            q = q / np.sqrt((q * q).sum(-1, keepdims=True) + 1e-6) / np.sqrt(Dk)
            k = k / np.sqrt((k * k).sum(-1, keepdims=True) + 1e-6)
            g = A * np.logaddexp(0, a[t] + dt_bias)
            beta = 1 / (1 + np.exp(-b[t]))
            state *= np.exp(g)[:, None, None]
            delta = beta[:, None] * (v - np.einsum("hk,hkv->hv", k, state))
            state += k[:, :, None] * delta[:, None, :]
            y[t] = np.einsum("hk,hkv->hv", q, state).reshape(-1)
        return y.astype(bfloat16), state
