# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Check every engine projection's bounded sequence and derived row counts."""

import numpy as np
import pytest
from aie.helpers.taplib import PerCall, TensorAccessPattern

from iron.common.design import OperatorDesign
from iron.operators.flm.gemma4_engine.build import GEMMS, MAX_M, PLI_MAX_M, gemm


@pytest.mark.parametrize(
    "M,K,N,gelu",
    [(MAX_M, *shape) for shape in GEMMS]
    + [
        (PLI_MAX_M, 1536, 8960, False),
        (PLI_MAX_M, 1536, 256, True),
        (PLI_MAX_M, 256, 1536, False),
    ],
)
def test_every_projection_lowers_with_a_symbolic_row_bound(npu2, M, K, N, gelu):
    op = gemm(M, K, N, gelu).resolved()
    design = OperatorDesign(op, full_elf=False).compilable()
    assert design.generate_mlir().operation.verify()
    rows = PerCall("m", None, np.int32).affine()
    for value in op.values:
        if value.derive is None:
            continue
        expression = op.derived_at(value.name, valid=rows)
        for m in range(256, M + 1, 256):
            assert expression.evaluate({"m": m}) == op.derived_at(value.name, valid=m)


def test_packed_b_descriptors_count_host_bytes(npu2):
    b = gemm(MAX_M, 4096, 1536, False).resolved().B
    assert b.dtype is np.uint8
    assert b.shape == (4096 * 1536 * 9 // 8,)
    # Re-read one contiguous packed tile, in its host storage units.
    tap = TensorAccessPattern((32768,), 0, [2, 1, 1, 2048], [0, 0, 0, 1])
    assert b.fits(tap)
    # This byte stride exceeds the shim's 20-bit step field.
    step = 1 << 23
    oversized = TensorAccessPattern((2 * step,), 0, [1, 1, 2, 2048], [0, 0, step, 1])
    assert not b.fits(oversized)
