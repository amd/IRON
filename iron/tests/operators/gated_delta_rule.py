# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GatedDeltaRule's reference against transformers' token-by-token gated
delta rule, as Qwen3.5's Gated DeltaNet calls it, also where a row's q and
k are so near zero that eps sets their norms; and the shapes it refuses.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.operators.gated_delta_rule import GatedDeltaRule


@pytest.mark.parametrize("scale", [1.0, 1e-4], ids=["unit", "near-zero"])
def test_the_reference_matches_transformers_over_the_valid_rows(scale):
    torch = pytest.importorskip("torch")
    qwen = pytest.importorskip("transformers.models.qwen3_5.modeling_qwen3_5")
    op = GatedDeltaRule(rows=6, k_heads=2, v_heads=4, key_dim=8, value_dim=16)
    op.__dict__["_extents"] = {"valid": 5}
    rng = np.random.default_rng(0)
    qkv = rng.standard_normal((op.rows, op.width))
    qkv[1, :32] *= scale
    qkv = qkv.astype(bfloat16)
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


@pytest.mark.parametrize(
    "k_heads,v_heads,value_dim",
    [(2, 4, 8), (4, 6, 16), (1, 3, 16)],
    ids=["value_dim-a-slice-apart", "v_heads-not-whole-groups", "v_heads-odd"],
)
def test_a_shape_the_cores_cannot_gather_is_refused(k_heads, v_heads, value_dim):
    with pytest.raises(ValueError, match="must be whole 16-column slices"):
        GatedDeltaRule(
            rows=1, k_heads=k_heads, v_heads=v_heads, key_dim=8, value_dim=value_dim
        )
