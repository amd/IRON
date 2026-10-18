#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
from typing import Any

import pytest
from aie.utils.verify import Tolerance

from iron.common.testing import run_test, vectors
from iron.operators.flm import q4nx
from iron.operators.flm.aie2p_math_emulation import rb
from iron.operators.flm.dequant.op import DequantBFP
from iron.operators.flm.gemm.op import ProjectionGEMM


def _check(op, inputs, outputs=None):
    errors = run_test(op, inputs, outputs, tolerance=Tolerance.exact())
    assert not errors, f"{op.name}: {errors}"


@pytest.mark.supported_devices("npu2")
def test_output_feeds_gemm_unchanged():
    """The output must equal what ProjectionGEMM.pack_B produces, which is the contract
    that makes it a drop-in. Comparing against pack_B catches a drift in either
    operator's tiling that a self-consistent reference would not.
    """
    op = DequantBFP(K=1024, N=128)
    v = vectors(op, **op.test.draw(op))
    gemm = ProjectionGEMM(M=256, K=op.K, N=op.N, tile_n=64, rounding="floor")
    packed = gemm.pack_B(rb(q4nx.dequantize(op.grid(v["qw"]))).T.copy())
    _check(op, v.inputs, {"out": packed})


@pytest.mark.supported_devices("npu2")
def test_one_xclbin_serves_every_shape():
    """Several shapes and parameter sets back to back on one loaded xclbin.

    A model dispatches ten weight shapes against a budget of 16 hardware
    contexts. The catalog's cases cannot catch a regression here: each gets
    a fresh context, so the array is reconfigured between cases anyway. One
    case leaves three of the eight columns without work.
    """
    cases: list[dict[str, Any]] = [
        dict(K=1536, N=2048),
        dict(K=1024, N=320),
        dict(K=2048, N=1536),
        dict(
            K=1024,
            N=1024,
            run_out_features=512,
            run_period_out_features=1024,
        ),
        dict(K=1536, N=2048),
    ]
    xclbin = None
    for case in cases:
        op = DequantBFP(**case)
        _check(op, vectors(op, **op.test.draw(op)))

        # A cache hit: the image _check built and ran.
        image = op.compile().image
        stamp = (str(image), os.path.getmtime(image))
        if xclbin is None:
            xclbin = stamp
        assert stamp == xclbin, f"{case} rebuilt the xclbin"
