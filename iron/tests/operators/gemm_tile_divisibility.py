#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GEMM.__post_init__ must reject tile sizes the kernel cannot build, not just
undersized ones.

aie_kernels/aie2p/mm.cc's matmul_vectorized_*x*x*_bf16_* wrappers static_assert
m % (2*r) == 0 and n % (2*t) == 0 for the (r, t) pair selected by
emulate_bf16_mmul_with_bfp16 (8/8 when enabled, the default; 4/8 otherwise).
The previous check only asserted tile_m/tile_k/tile_n >= a minimum, which
admits e.g. tile_m=8 under emulation even though the kernel requires a
multiple of 16 -- GEMM(...) constructs without error and fails a C++
static_assert at kernel compile time, from a file this class never names.
"""

import pytest

from iron.operators.gemm.op import GEMM


def _construct(tile_m=64, tile_k=64, tile_n=64, emulate_bf16_mmul_with_bfp16=True):
    return GEMM(
        M=512,
        K=512,
        N=512,
        tile_m=tile_m,
        tile_k=tile_k,
        tile_n=tile_n,
        emulate_bf16_mmul_with_bfp16=emulate_bf16_mmul_with_bfp16,
        context=None,
    )


def test_tile_m_that_only_satisfies_the_old_greater_equal_check_is_rejected():
    """tile_m=8 is >= the old min_tile_m of 8, but mm.cc needs m % 16 == 0
    under the default emulate_bf16_mmul_with_bfp16=True (r=8)."""
    with pytest.raises(ValueError, match="tile_m .* multiple of 16"):
        _construct(tile_m=8)


def test_tile_m_multiple_of_16_is_accepted_under_emulation():
    _construct(tile_m=16)
    _construct(tile_m=64)


def test_tile_m_multiple_of_8_is_accepted_without_emulation():
    """r=4 without emulation, so the requirement relaxes to a multiple of 8."""
    _construct(tile_m=8, emulate_bf16_mmul_with_bfp16=False)


def test_tile_n_not_a_multiple_of_16_is_rejected_regardless_of_emulation():
    """t=8 for both emulation settings, so n % 16 == 0 always."""
    with pytest.raises(ValueError, match="tile_n .* multiple of 16"):
        _construct(tile_n=8, emulate_bf16_mmul_with_bfp16=False)


def test_tile_k_not_a_multiple_of_8_is_rejected():
    # tile_k=4 still divides K=512 evenly (the outer K % tile_k check), so
    # this exercises the new s-divisibility check rather than that one.
    with pytest.raises(ValueError, match="tile_k .* multiple of 8"):
        _construct(tile_k=4)
