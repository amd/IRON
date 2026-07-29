#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The operand layouts IRON's kernels are compiled for must match stream-dse's.

stream-dse generates the DMAs that feed the kernel objects IRON compiles from
``aie_kernels``; both sides must agree on how an operand is tiled in memory. The
layouts declared in :mod:`iron.common.stream.ops` are that contract. They happen
to coincide with stream-dse's built-in kernel layouts today, so no override is
needed -- this test fails if a future stream-dse release changes them, which would
otherwise corrupt results silently.
"""

import pytest

pytest.importorskip(
    "stream", reason="stream-dse not installed (see requirements_stream.txt)"
)

from stream.compiler.kernels import AIEKernels  # noqa: E402

from iron.common.stream.ops import (  # noqa: E402
    ELTWISE_MUL,
    GEMM,
    SILU,
    elementwise_layouts,
    gemm_layouts,
)


def _assert_same(iron_layouts, stream_kernel):
    expected = [layout.to_snaxc() for layout in iron_layouts]
    actual = list(stream_kernel.operand_layouts())
    assert [str(layout) for layout in expected] == [str(layout) for layout in actual]


@pytest.mark.parametrize("bfp16_mmul", [False, True])
@pytest.mark.parametrize("m,k,n", [(32, 32, 64), (32, 64, 32), (64, 64, 64)])
def test_gemm_layouts_match_stream(m, k, n, bfp16_mmul):
    _assert_same(
        gemm_layouts(m, k, n, bfp16_mmul),
        AIEKernels[GEMM.key](61.8, m, k, n, "default", bfp16_mmul),
    )


@pytest.mark.parametrize("bfp16_mmul", [False, True])
def test_silu_layouts_match_stream(bfp16_mmul):
    _assert_same(
        elementwise_layouts(2, bfp16_mmul),
        AIEKernels[SILU.key](50.0, "default", bfp16_mmul=bfp16_mmul),
    )


@pytest.mark.parametrize("bfp16_mmul", [False, True])
def test_eltwise_mul_layouts_match_stream(bfp16_mmul):
    _assert_same(
        elementwise_layouts(3, bfp16_mmul),
        AIEKernels[ELTWISE_MUL.key](50.0, "default", bfp16_mmul=bfp16_mmul),
    )


@pytest.mark.parametrize("kernel", [GEMM, SILU, ELTWISE_MUL])
def test_kernel_keys_exist_in_stream(kernel):
    assert kernel.key in AIEKernels
