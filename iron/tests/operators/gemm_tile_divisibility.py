#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GEMM.__post_init__ must reject tile sizes the kernel cannot build.

aie_kernels/linalg/mm_aie2p.h's matmul_vectorized_*x*x*_bf16_* wrappers static_assert
m % (2*r) == 0, k % s == 0 and n % (2*t) == 0 for the (r, s, t) triple selected
by emulate_bf16_mmul_with_bfp16 (r=t=8 when enabled, the default; r=4, t=8
otherwise). A tile size that meets a lower bound without dividing evenly
constructs here without error and then fails that static_assert at kernel
compile time, from a file this class never names.
"""

import pytest
from aie.iron.device import from_name

from iron.operators.gemm import GEMM


def _construct(tile_m=64, tile_k=64, tile_n=64, emulate_bf16_mmul_with_bfp16=True):
    return GEMM(
        M=512,
        K=512,
        N=512,
        tile_m=tile_m,
        tile_k=tile_k,
        tile_n=tile_n,
        emulate_bf16_mmul_with_bfp16=emulate_bf16_mmul_with_bfp16,
    )


def test_tile_m_not_a_multiple_of_16_is_rejected_under_emulation():
    """mm.cc needs m % 16 == 0 under the default emulate_bf16_mmul_with_bfp16
    (r=8), which tile_m=8 satisfies as a bound but not as a divisor.
    """
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
    with pytest.raises(ValueError, match="tile_n .* multiple of 16"):
        _construct(tile_n=8, emulate_bf16_mmul_with_bfp16=True)


def test_tile_m_not_a_multiple_of_8_is_rejected_without_emulation():
    """mm.cc needs m % 8 == 0 without emulation (r=4), which tile_m=4
    satisfies as a bound but not as a divisor.
    """
    with pytest.raises(ValueError, match="tile_m .* multiple of 8"):
        _construct(tile_m=4, emulate_bf16_mmul_with_bfp16=False)


def test_tile_k_not_a_multiple_of_8_is_rejected():
    # tile_k=4 still divides K=512 evenly (the outer K % tile_k check), so
    # this exercises the s-divisibility check rather than that one.
    with pytest.raises(ValueError, match="tile_k .* multiple of 8"):
        _construct(tile_k=4)


@pytest.mark.parametrize(
    "device, emulate, M, tile_m",
    [
        ("npu2", True, 2048, 64),
        ("npu2", True, 128, 32),
        ("npu2", True, 64, 16),
        ("npu2", False, 32, 8),
        ("npu1", False, 64, 16),
    ],
)
def test_an_open_tile_m_is_the_widest_that_splits_m(device, emulate, M, tile_m):
    """Four rows of cores each take tile_m of M's rows, so a short M takes a
    short tile rather than padding to 256 rows: down to the kernel's m block,
    16 under emulation (2 r, r=8) and on aie2 (4 r, r=4), else 8.
    """
    op = GEMM(M=M, K=64, N=512, emulate_bf16_mmul_with_bfp16=emulate)
    assert op.resolved(from_name(device)).tile_m == tile_m


@pytest.mark.parametrize("device, emulate", [("npu2", True), ("npu1", False)])
def test_an_m_no_tile_splits_is_rejected(device, emulate):
    """Refused when constructed if the bound device has no such tile, else when resolved for ``device``."""
    with pytest.raises(ValueError, match=r"M \(32\) must be a multiple of 64"):
        op = GEMM(M=32, K=64, N=512, emulate_bf16_mmul_with_bfp16=emulate)
        op.resolved(from_name(device))
