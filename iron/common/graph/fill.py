# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Weights made from their shapes alone."""

import math
from collections.abc import Mapping
from typing import Any

import numpy as np


def filled(
    fill: str, named: Mapping[str, tuple[tuple[int, ...], Any]], seed: int = 0
) -> dict[str, np.ndarray]:
    """An array for each of ``named``'s ``(shape, dtype)``, by name.

    Args:
        fill: ``"random"``: drawn at ``seed`` in ``named``'s order, each
            matrix normal with deviation ``1/sqrt(in)`` (an embedding's
            ``in`` its width), anything of fewer than two axes normal with
            deviation 0.1, about zero if it is a bias and about one
            otherwise (a norm), so that swapping two changes the output.
            ``"unread"``: allocated and never written, for recording,
            building and measuring a model, none of which reads a weight;
            the pages are reserved, not touched, and a scalar is zero,
            since a graph may read one as it is built (a clamp's bounds).
        seed: The seed ``"random"`` draws at.
    """
    if fill == "unread":
        return {
            n: np.zeros((), dtype) if not shape else np.empty(shape, dtype)
            for n, (shape, dtype) in named.items()
        }
    rng = np.random.default_rng(seed)
    out = {}
    for n, (shape, dtype) in named.items():
        x = rng.standard_normal(shape, dtype=np.float32)
        if len(shape) >= 2:
            out[n] = (x / np.sqrt(math.prod(shape[1:]))).astype(dtype)
        else:
            out[n] = (x / 10 + (not n.endswith("bias"))).astype(dtype)
    return out
