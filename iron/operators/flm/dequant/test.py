#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os

import numpy as np
import pytest
import torch

import aie.utils as aie_utils
from aie.dialects._aie_enum_gen import AIEArch

from iron.common.test_utils import run_test
from iron.operators.flm.dequant.op import DequantBFP
from iron.operators.flm.dequant.reference import (
    random_q4nx,
    reference,
    scatter_runs,
)

# K = 512 is excluded: flm.GEMM picks tile_n = 128 there, which this operator
# refuses. test_rejects_unservable_shapes covers it.
SHAPES = [(1024, 128), (1024, 512), (1536, 640), (2048, 256)]


def _on_aie2p():
    dev = aie_utils.get_current_device()
    return dev is not None and dev.arch == AIEArch.AIE2p


requires_aie2p = pytest.mark.skipif(
    not _on_aie2p(), reason="bfp16ebs8 exists only on AIE2P"
)


def _check(op, blob, expected, label):
    errors, _, _ = run_test(
        op,
        {"in": torch.from_numpy(blob)},
        {"out": torch.from_numpy(expected)},
        rel_tol=0.0,
        abs_tol=0.0,
    )
    assert not errors, f"{label}: {errors}"


@requires_aie2p
@pytest.mark.parametrize("K, N", SHAPES)
def test_matches_reference(K, N, aie_context):
    """Byte-exact. Every rounding on the device is reproducible on the host, so
    a tolerance would hide a value landing in the wrong block."""
    qw = random_q4nx(K, N, seed=0)
    op = DequantBFP(K=K, N=N, context=aie_context)
    _check(op, qw, reference(qw, K, N), f"K={K} N={N}")


@requires_aie2p
def test_output_feeds_gemm_unchanged(aie_context):
    """The output must equal what GEMM.pack_B produces, which is the contract
    that makes it a drop-in. Comparing against pack_B catches a drift in either
    operator's tiling that a self-consistent reference would not."""
    from iron.operators.flm.gemm.op import GEMM
    from iron.operators.flm.dequant.reference import dequantize, f32_to_bf16_floor

    K, N = 1024, 128
    qw = random_q4nx(K, N, seed=3)
    w = dequantize(qw, K, N)
    w = (f32_to_bf16_floor(w).astype(np.uint32) << 16).view(np.float32)
    gemm = GEMM(M=256, K=K, N=N, tile_n=64, rounding="floor", context=aie_context)
    packed = gemm.pack_B(torch.from_numpy(np.ascontiguousarray(w.T))).numpy()

    _check(DequantBFP(K=K, N=N, context=aie_context), qw, packed, "vs pack_B")


@requires_aie2p
def test_gate_up_interleaved_blob(aie_context):
    """gate and up share one blob at 512 out-features in a 1024 period."""
    K, N, run, period = 1024, 1024, 512, 1024
    qw = random_q4nx(K, N, seed=12)
    blob = scatter_runs(qw, K, N, run, period, seed=12)

    op = DequantBFP(
        K=K,
        N=N,
        run_out_features=run,
        run_period_out_features=period,
        context=aie_context,
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
def test_large_k_shapes(K, N, aie_context):
    """E2B's tall projections, whose k-tiles outnumber a shim tile's buffer
    descriptors. K = 12288 is 24 k-tiles, the deepest E2B reaches."""
    qw = random_q4nx(K, N, seed=21)
    op = DequantBFP(K=K, N=N, context=aie_context)
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
def test_e4b_shapes(K, N, aie_context):
    """E4B's projections, as B is (K, N). These are the shapes flm.GEMM's own
    extensive set covers, so the two operators are exercised on the same model."""
    qw = random_q4nx(K, N, seed=33)
    op = DequantBFP(K=K, N=N, context=aie_context)
    _check(op, qw, reference(qw, K, N), f"K={K} N={N}")


@requires_aie2p
@pytest.mark.extensive
def test_e4b_gate_up_interleaved(aie_context):
    """E4B's gate/up blob: 5120 out-features each in a 10240 period."""
    K, N, run, period = 2560, 10240, 5120, 10240
    qw = random_q4nx(K, N, seed=34)
    blob = scatter_runs(qw, K, N, run, period, seed=34)

    op = DequantBFP(
        K=K,
        N=N,
        run_out_features=run,
        run_period_out_features=period,
        context=aie_context,
    )
    assert op.quantized_size() == blob.size
    _check(op, blob, reference(qw, K, N), "E4B gate/up interleave")


@requires_aie2p
def test_one_xclbin_serves_every_shape(aie_context):
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
        op = DequantBFP(context=aie_context, **case)
        qw = random_q4nx(K, N, seed=7)
        blob = qw
        if case.get("run_out_features"):
            blob = scatter_runs(
                blob, K, N, case["run_out_features"], case["run_period_out_features"], 7
            )
        _check(op, blob, reference(qw, K, N), str(case))

        stamp = (
            op.xclbin_artifact.filename,
            os.path.getmtime(op.xclbin_artifact.filename),
        )
        if xclbin is None:
            xclbin = stamp
        assert stamp == xclbin, f"{case} rebuilt the xclbin"


@pytest.mark.parametrize(
    "K, N, exc, match",
    [
        # Only AIE2P's flm.GEMM picks tile_n=128 for a single-k-iteration shape.
        # AIE2 always picks 64, which is the order this operator emits, so there
        # is nothing to refuse there. The shape checks below are arch-independent.
        pytest.param(512, 128, NotImplementedError, "tile_n", marks=requires_aie2p),
        (1000, 128, ValueError, "multiple of"),
        (1024, 100, ValueError, "multiple of"),
    ],
)
def test_rejects_unservable_shapes(K, N, exc, match, aie_context):
    with pytest.raises(exc, match=match):
        DequantBFP(K=K, N=N, context=aie_context)


if __name__ == "__main__":
    run_test(__file__)
