# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Weights made from their shapes alone."""

import math
from collections.abc import Mapping
from typing import Any

import numpy as np

#: A ``Clipped`` bound's leaf name (``iron.applications.gemma4.audio``): drawn
#: fixed rather than per-tensor, so every one agrees (``Clipped.same_input``'s
#: linears, which share an input, among them) and a min never exceeds its max.
_CLIP_BOUNDS = {
    "input_min": -1.0,
    "output_min": -1.0,
    "input_max": 1.0,
    "output_max": 1.0,
}


def filled(
    fill: str, named: Mapping[str, tuple[tuple[int, ...], Any]], seed: int = 0
) -> dict[str, np.ndarray]:
    """Return an array for each of ``named``'s ``(shape, dtype)``, by name.

    ``"random"`` draws matrices normal at deviation ``1/sqrt(in)``, a ``Clipped`` bound
    (``_CLIP_BOUNDS``) fixed, and the rest about one (a bias zero) at 0.1, so swapping
    two changes the output; ``"unread"`` is lazy zeros.
    """
    if fill == "unread":
        return {n: np.zeros(shape, dtype) for n, (shape, dtype) in named.items()}
    rng = np.random.default_rng(seed)
    out = {}
    for n, (shape, dtype) in named.items():
        x = rng.standard_normal(shape, dtype=np.float32)
        bound = _CLIP_BOUNDS.get(n.rsplit(".", 1)[-1])
        if bound is not None:
            out[n] = np.asarray(bound, dtype)
        elif len(shape) >= 2:
            out[n] = (x / np.sqrt(math.prod(shape[1:]))).astype(dtype)
        else:
            # An array even of no axes, where numpy's arithmetic gives a scalar.
            out[n] = np.asarray(x / 10 + (not n.endswith("bias")), dtype)
    return out
