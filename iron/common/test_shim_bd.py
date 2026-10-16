#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests for the shared ShimNOC BD run-split helper.

The point of the shared helper is that one hardware invariant has one implementation. The
differential test below is what makes that claim checkable: it pins the helper against the
inline algorithm `repeat` used before the extraction, over the whole parameter range rather
than a few chosen shapes.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common.shim_bd import (
    SHIM_ADDR_GRAN_BITS,
    SHIM_MAX_WRAP,
    shim_gran_elems,
    split_run,
)


def _repeat_inline_pre_extraction(cols, granule, lim=SHIM_MAX_WRAP):
    """`repeat`'s own divisor search as it stood after amd/IRON#161, before this helper.

    Searches divisors upward and takes the first legal one, which maximises the chunk.
    split_run searches the chunk downward. Same objective, opposite direction -- which is
    exactly the equivalence worth pinning.
    """
    for divisor in range(1, cols + 1):
        if cols % divisor:
            continue
        chunk = cols // divisor
        if chunk <= lim and divisor <= lim and chunk % granule == 0:
            return divisor
    return None


@pytest.mark.parametrize("granule", [1, 2, 4])
def test_split_run_matches_the_algorithm_it_replaced(granule):
    """Opposite search directions must agree on every cols, including the no-split cases."""
    for cols in range(1, 3000):
        expected = _repeat_inline_pre_extraction(cols, granule)
        got = split_run(cols, gran=granule)
        assert (got[0] if got else None) == expected, (
            f"cols={cols} granule={granule}: split_run gave {got}, "
            f"pre-extraction search gave count {expected}"
        )


@pytest.mark.parametrize("granule", [1, 2, 4])
def test_split_run_output_satisfies_the_bd_constraints(granule):
    """Whatever it returns must actually be emittable: both dims within the wrap field,
    the inner dim granule-aligned, and the factorisation exact."""
    for cols in range(1, 3000):
        got = split_run(cols, gran=granule)
        if got is None:
            continue
        hi, lo = got
        assert hi * lo == cols, f"cols={cols}: {hi}*{lo} != {cols}"
        assert hi <= SHIM_MAX_WRAP and lo <= SHIM_MAX_WRAP
        assert lo % granule == 0


@pytest.mark.parametrize("granule", [1, 2, 4])
def test_split_run_maximises_the_inner_run(granule):
    """`lo` innermost is the whole point -- a short innermost dim is legal but slow, so a
    regression that still satisfies the constraints would otherwise pass silently."""
    for cols in range(1, 2000):
        got = split_run(cols, gran=granule)
        if got is None:
            continue
        _, lo = got
        bigger = [
            c
            for c in range(lo + granule, min(cols, SHIM_MAX_WRAP) + 1, granule)
            if cols % c == 0 and cols // c <= SHIM_MAX_WRAP and c % granule == 0
        ]
        assert (
            not bigger
        ), f"cols={cols} granule={granule}: lo={lo} but {bigger[0]} is legal"


def test_shim_gran_elems_tracks_the_dtype():
    """The bf16-only constant this replaced was wrong for every other width."""
    assert shim_gran_elems(np.int8) == SHIM_ADDR_GRAN_BITS // 8
    assert shim_gran_elems(bfloat16) == 2
    assert shim_gran_elems(np.float32) == 1
    # A dtype at least as wide as the granule is trivially aligned, and must not assert --
    # `repeat` accepts arbitrary dtypes, unlike gemv.
    assert shim_gran_elems(np.float64) == 1


def test_shim_gran_elems_accepts_the_generic_form():
    """Designs carry `np.dtype[T]`, tests tend to pass the bare type."""
    assert shim_gran_elems(np.dtype[bfloat16]) == shim_gran_elems(bfloat16)
