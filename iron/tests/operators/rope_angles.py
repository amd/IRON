#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""RoPE's angle table (``rope_angles``) and Llama 3's frequency scaling
(``LLAMA_3_2``) against their formulas and Meta's published reference.
No NPU.
"""

import math

import numpy as np

from iron.operators.rope.op import LLAMA_3_2, rope_angles


def test_rope_is_the_formula_rounded_once():
    """Each entry is cos or sin, in float64, of the float32 frequency times
    the float32 position, rounded once; and within float32 rounding of the
    formula evaluated in float64 throughout.
    """
    D, L, base = 64, 2048, 500000.0
    angles = rope_angles(D, L, base)
    assert angles.dtype == np.float32 and angles.shape == (L, D)

    exponents = np.arange(0, D, 2, dtype=np.float32) / np.float32(D)
    inv_freq = (1.0 / base ** exponents.astype(np.float64)).astype(np.float32)
    freqs = np.outer(np.arange(L, dtype=np.float32), inv_freq).astype(np.float64)
    assert np.array_equal(angles[:, ::2], np.cos(freqs).astype(np.float32))
    assert np.array_equal(angles[:, 1::2], np.sin(freqs).astype(np.float32))

    exact_freqs = np.outer(np.arange(L), 1.0 / base ** (np.arange(0, D, 2) / D))
    exact = np.empty((L, D))
    exact[:, ::2], exact[:, 1::2] = np.cos(exact_freqs), np.sin(exact_freqs)
    # float32 frequencies at position 2047 are off by up to 2047 ulps of the
    # frequency: about 2e-4 at the fastest one.
    assert np.abs(angles - exact).max() < 5e-4


def test_rope_is_correctly_rounded_at_position_zero_and_one():
    """Row 0 is exactly (1, 0) per frequency; row 1 is cos/sin of inv_freq."""
    D, base = 64, 500000.0
    angles = rope_angles(D, 2, base)
    assert np.array_equal(angles[0, ::2], np.ones(D // 2, np.float32))
    assert np.array_equal(angles[0, 1::2], np.zeros(D // 2, np.float32))
    inv = (1.0 / base ** (np.arange(0, D, 2, dtype=np.float32) / np.float32(D))).astype(
        np.float32
    )
    assert np.array_equal(
        angles[1, ::2], np.cos(inv.astype(np.float64)).astype(np.float32)
    )


def _published_llama3_scaling(freqs, factor, low, high, original):
    """``apply_scaling`` from Meta's llama-models reference, as published:
    one frequency at a time, in float64.
    """
    low_wavelen, high_wavelen = original / low, original / high
    scaled = []
    for freq in freqs:
        wavelen = 2 * math.pi / freq
        if wavelen < high_wavelen:
            scaled.append(freq)
        elif wavelen > low_wavelen:
            scaled.append(freq / factor)
        else:
            smooth = (original / wavelen - low) / (high - low)
            scaled.append((1 - smooth) * freq / factor + smooth * freq)
    return np.array(scaled)


def test_llama3_scaling_is_the_published_formula():
    """Every frequency of Llama 3.2 1B's (head_dim 64, base 500000) matches
    Meta's reference, and all three bands are exercised: the fastest fifteen
    kept, three interpolated, the slowest fourteen divided by 32.
    """
    D, base = 64, 500000.0
    inv_freq = 1.0 / base ** (np.arange(0, D, 2) / D)
    ours = LLAMA_3_2(inv_freq)
    published = _published_llama3_scaling(inv_freq, 32.0, 1.0, 4.0, 8192)
    np.testing.assert_allclose(ours, published, rtol=1e-15, atol=0)

    kept = ours == inv_freq
    divided = np.isclose(ours, inv_freq / 32.0, rtol=1e-15, atol=0)
    between = ~kept & ~divided
    assert (kept.sum(), between.sum(), divided.sum()) == (15, 3, 14)
    # The bands are contiguous, fastest to slowest, and the interpolation
    # moves each frequency part of the way to its divided value.
    assert list(np.flatnonzero(kept)) == list(range(15))
    assert list(np.flatnonzero(between)) == [15, 16, 17]
    assert np.all(inv_freq[between] / 32.0 < ours[between])
    assert np.all(ours[between] < inv_freq[between])


def test_scaled_rope_table_rotates_by_the_scaled_frequencies():
    """The scaled table is the unscaled table's formula over the scaled
    frequencies, rounded once; the kept band is the unscaled table's.
    """
    D, L, base = 64, 2048, 500000.0
    exponents = np.arange(0, D, 2, dtype=np.float32) / np.float32(D)
    inv_freq = 1.0 / base ** exponents.astype(np.float64)
    scaled = LLAMA_3_2(inv_freq).astype(np.float32)
    freqs = np.outer(np.arange(L, dtype=np.float32), scaled).astype(np.float64)

    angles = rope_angles(D, L, base, LLAMA_3_2)
    assert angles.dtype == np.float32 and angles.shape == (L, D)
    assert np.array_equal(angles[:, ::2], np.cos(freqs).astype(np.float32))
    assert np.array_equal(angles[:, 1::2], np.sin(freqs).astype(np.float32))

    unscaled = rope_angles(D, L, base)
    assert np.array_equal(angles[:, :30], unscaled[:, :30]), "the kept band moved"
    assert not np.array_equal(angles[:, 30:], unscaled[:, 30:])
