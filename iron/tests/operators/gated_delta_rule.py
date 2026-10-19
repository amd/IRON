# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GatedDeltaRule's reference against transformers' token-by-token gated
delta rule, as Qwen3.5's Gated DeltaNet calls it, and its one refusal.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.operators.gated_delta_rule import GatedDeltaRule


def test_the_reference_matches_transformers_over_the_valid_rows():
    torch = pytest.importorskip("torch")
    qwen = pytest.importorskip("transformers.models.qwen3_5.modeling_qwen3_5")
    op = GatedDeltaRule(rows=6, k_heads=2, v_heads=4, key_dim=8, value_dim=16)
    op.__dict__["_extents"] = {"valid": 5}
    rng = np.random.default_rng(0)
    qkv = rng.standard_normal((op.rows, op.width)).astype(bfloat16)
    a, b = (rng.standard_normal((op.rows, 4)).astype(bfloat16) for _ in "ab")
    head = np.stack([rng.uniform(0, 2, 4), -rng.uniform(0.5, 8, 4)], 1)
    state = rng.standard_normal((4, 8, 16)).astype(np.float32)
    y, final = op.reference(qkv, a, b, head.astype(np.float32), state)

    t = lambda m: torch.from_numpy(np.asarray(m, np.float32)[None, :5])
    q, k, v = torch.split(t(qkv), [16, 16, 64], dim=-1)
    q, k = (m.reshape(1, 5, 2, 8).repeat_interleave(2, dim=2) for m in (q, k))
    dt_bias, A = (torch.from_numpy(c.astype(np.float32)) for c in head.T)
    want, want_final = qwen.torch_recurrent_gated_delta_rule(
        q,
        k,
        v.reshape(1, 5, 4, 16),
        g=A * torch.nn.functional.softplus(t(a) + dt_bias),
        beta=t(b).sigmoid(),
        initial_state=torch.from_numpy(state)[None],
        output_final_state=True,
        use_qk_l2norm_in_kernel=True,
    )
    np.testing.assert_allclose(final, want_final[0].numpy(), rtol=1e-5, atol=1e-5)
    np.testing.assert_allclose(
        y[:5].astype(np.float32),
        want[0].reshape(5, -1).numpy(),
        rtol=8e-3,
        atol=1e-3,
    )
    assert not y[5:].astype(np.float32).any()


def test_value_heads_must_be_whole_groups_of_key_heads():
    with pytest.raises(ValueError, match=r"v_heads \(3\) must be whole groups"):
        GatedDeltaRule(rows=1, k_heads=2, v_heads=3, key_dim=8, value_dim=8)
