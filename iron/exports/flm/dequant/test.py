#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.dialects._aie_enum_gen import AIEArch

from iron.common.harness import run_test
from iron.exports.flm.dequant.op import DequantBFP
from iron.exports.flm.dequant.reference import (
    dequantize,
    f32_to_bf16_floor,
    random_q4nx,
    reference,
    scatter_runs,
)
from iron.exports.flm.gemm.op import GEMM

# K = 512 is one k-tile, where flm.GEMM at tile_n = 128 wins on NPU2. It
# defaults to 64 regardless, which is the order this operator emits.
SHAPES = [(512, 128), (1024, 128), (1024, 512), (1536, 640), (2048, 256)]


def _on_aie2p():
    dev = aie_utils.get_current_device()
    return dev is not None and dev.arch == AIEArch.AIE2p


requires_aie2p = pytest.mark.skipif(
    not _on_aie2p(), reason="bfp16ebs8 exists only on AIE2P"
)


def _check(op, blob, expected, label):
    errors, _, _ = run_test(
        op,
        {"in": blob},
        {"out": expected},
        rel_tol=0.0,
        abs_tol=0.0,
    )
    assert not errors, f"{label}: {errors}"


@requires_aie2p
@pytest.mark.parametrize("K, N", SHAPES)
def test_matches_reference(K, N, npu_runtime):
    """Byte-exact. Every rounding on the device is reproducible on the host, so
    a tolerance would hide a value landing in the wrong block.
    """
    qw = random_q4nx(K, N, seed=0)
    op = DequantBFP(K=K, N=N)
    _check(op, qw, reference(qw, K, N), f"K={K} N={N}")


@requires_aie2p
def test_output_feeds_gemm_unchanged(npu_runtime):
    """The output must equal what GEMM.pack_B produces, which is the contract
    that makes it a drop-in. Comparing against pack_B catches a drift in either
    operator's tiling that a self-consistent reference would not.
    """
    K, N = 1024, 128
    qw = random_q4nx(K, N, seed=3)
    w = dequantize(qw, K, N)
    w = (f32_to_bf16_floor(w).astype(np.uint32) << 16).view(np.float32)
    gemm = GEMM(M=256, K=K, N=N, tile_n=64, rounding="floor")
    packed = gemm.pack_B(np.ascontiguousarray(w.T))

    _check(DequantBFP(K=K, N=N), qw, packed, "vs pack_B")


@requires_aie2p
def test_gate_up_interleaved_blob(npu_runtime):
    """Gate and up share one blob at 512 out-features in a 1024 period."""
    K, N, run, period = 1024, 1024, 512, 1024
    qw = random_q4nx(K, N, seed=12)
    blob = scatter_runs(qw, K, N, run, period, seed=12)

    op = DequantBFP(
        K=K,
        N=N,
        run_out_features=run,
        run_period_out_features=period,
    )
    assert op.quantized_size() == blob.size
    _check(op, blob, reference(qw, K, N), "gate/up interleave")


@requires_aie2p
@pytest.mark.parametrize(
    "K, N",
    [
        (4096, 1536),
        (6144, 1536),
        pytest.param(12288, 1536, marks=pytest.mark.extensive),
    ],
)
def test_large_k_shapes(K, N, npu_runtime):
    """E2B's tall projections, whose k-tiles outnumber a shim tile's buffer
    descriptors. K = 12288 is 24 k-tiles, the deepest E2B reaches.
    """
    qw = random_q4nx(K, N, seed=21)
    op = DequantBFP(K=K, N=N)
    _check(op, qw, reference(qw, K, N), f"K={K} N={N}")


@requires_aie2p
@pytest.mark.extensive
@pytest.mark.parametrize(
    "K, N",
    [
        (2560, 2560),  # o-proj
        (10240, 2560),  # down
        (2560, 10240),  # gate/up
    ],
)
def test_e4b_shapes(K, N, npu_runtime):
    """E4B's projections, as B is (K, N). These are the shapes flm.GEMM's own
    extensive set covers, so the two operators are exercised on the same model.
    """
    qw = random_q4nx(K, N, seed=33)
    op = DequantBFP(K=K, N=N)
    _check(op, qw, reference(qw, K, N), f"K={K} N={N}")


@requires_aie2p
@pytest.mark.extensive
def test_e4b_gate_up_interleaved(npu_runtime):
    """E4B's gate/up blob: 5120 out-features each in a 10240 period."""
    K, N, run, period = 2560, 10240, 5120, 10240
    qw = random_q4nx(K, N, seed=34)
    blob = scatter_runs(qw, K, N, run, period, seed=34)

    op = DequantBFP(
        K=K,
        N=N,
        run_out_features=run,
        run_period_out_features=period,
    )
    assert op.quantized_size() == blob.size
    _check(op, blob, reference(qw, K, N), "E4B gate/up interleave")


@requires_aie2p
def test_one_xclbin_serves_every_shape(npu_runtime):
    """Several shapes and parameter sets back to back on one loaded xclbin.

    A model dispatches ten weight shapes against a budget of 16 hardware
    contexts. The parametrised tests cannot catch a regression here: each gets
    a fresh context, so the array is reconfigured between cases anyway. One
    case leaves three of the eight columns without work.
    """
    cases = [
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
        K, N = case["K"], case["N"]
        op = DequantBFP(**case)
        qw = random_q4nx(K, N, seed=7)
        blob = qw
        if case.get("run_out_features"):
            blob = scatter_runs(
                blob, K, N, case["run_out_features"], case["run_period_out_features"], 7
            )
        _check(op, blob, reference(qw, K, N), str(case))

        image = op.artifacts.image
        stamp = (str(image), os.path.getmtime(image))
        if xclbin is None:
            xclbin = stamp
        assert stamp == xclbin, f"{case} rebuilt the xclbin"


@pytest.mark.parametrize(
    "K, N, extra, exc, match",
    [
        # flm.GEMM may be asked for tile_n=128, the NPU2 winner at K = 512;
        # this operator does not emit that order and must say so.
        (512, 128, dict(tile_n=128), NotImplementedError, "tile_n"),
        (1000, 128, {}, ValueError, "multiple of"),
        (1024, 100, {}, ValueError, "multiple of"),
    ],
)
def test_rejects_unservable_shapes(K, N, extra, exc, match):
    with pytest.raises(exc, match=match):
        DequantBFP(K=K, N=N, **extra)
