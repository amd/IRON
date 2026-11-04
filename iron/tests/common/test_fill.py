# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.common.graph.fill.filled``'s ``"random"`` draw.

A ``Clipped`` bound (``iron.applications.gemma4.audio``'s ``input_min``/``input_max``/
``output_min``/``output_max``) is fixed rather than per-tensor, so linears sharing an
input (``Clipped.same_input``) always agree and a min never exceeds its max, whichever
seed or how many layers name one.
"""

import math
import tracemalloc

import numpy as np
import pytest
from ml_dtypes import bfloat16

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


def test_a_large_matrix_draws_as_one_whole_draw_would():
    """Drawn a chunk at a time, every value is the one a single draw gives."""
    shape = (1031, 9001)
    drawn = filled("random", {"w": (shape, bfloat16), "b": ((7,), bfloat16)}, seed=3)
    rng = np.random.default_rng(3)
    whole = rng.standard_normal(shape, dtype=np.float32) / np.sqrt(shape[1])
    assert np.array_equal(drawn["w"], whole.astype(bfloat16))
    after = rng.standard_normal(7, dtype=np.float32) / 10 + 1
    assert np.array_equal(drawn["b"], after.astype(bfloat16))


def test_a_large_matrix_holds_no_full_precision_copy():
    """Gemma 4 E2B's per-layer embeddings drawn whole took ~28 GB beside their 4.7."""
    shape = (4096, 8200)
    tracemalloc.start()
    try:
        drawn = filled("random", {"w": (shape, bfloat16)}, seed=0)
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    assert drawn["w"].nbytes == 2 * math.prod(shape)
    assert peak < 3 * drawn["w"].nbytes, peak
