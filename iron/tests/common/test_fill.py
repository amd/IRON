# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.common.graph.fill.filled``'s ``"random"`` draw.

A ``Clipped`` bound (``iron.applications.gemma4.audio``'s ``input_min``/``input_max``/
``output_min``/``output_max``) is fixed rather than per-tensor, so linears sharing an
input (``Clipped.same_input``) always agree and a min never exceeds its max, whichever
seed or how many layers name one.
"""

import numpy as np
import pytest

from iron.common.graph.fill import filled


def _named(*leaves: str) -> dict[str, tuple[tuple[int, ...], type]]:
    return {leaf: ((), np.float32) for leaf in leaves}


@pytest.mark.parametrize("seed", [0, 1, 7])
def test_clip_bounds_of_linears_sharing_an_input_agree(seed):
    drawn = filled(
        "random",
        _named(
            "layers.0.self_attn.q_proj.input_min",
            "layers.0.self_attn.k_proj.input_min",
            "layers.0.self_attn.v_proj.input_min",
            "layers.0.self_attn.q_proj.input_max",
            "layers.0.self_attn.k_proj.input_max",
            "layers.0.self_attn.v_proj.input_max",
        ),
        seed,
    )
    mins = {float(v) for k, v in drawn.items() if k.endswith("input_min")}
    maxes = {float(v) for k, v in drawn.items() if k.endswith("input_max")}
    assert len(mins) == 1
    assert len(maxes) == 1
    assert next(iter(mins)) < next(iter(maxes))


def test_clip_bound_never_inverts():
    drawn = filled("random", _named("q_proj.input_min", "q_proj.input_max"), seed=0)
    assert drawn["q_proj.input_min"] < drawn["q_proj.input_max"]


def test_an_unrelated_scalar_still_draws_per_tensor():
    """Only ``filled``'s own four leaf names are fixed; any other scalar (a bias, a norm's weight) still draws its own, as before."""
    drawn = filled("random", _named("a.bias", "b.bias"), seed=0)
    assert drawn["a.bias"] != drawn["b.bias"]
