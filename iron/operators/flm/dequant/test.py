#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
from typing import Any

import numpy as np
import pytest
from aie.iron.device import from_name
from aie.utils.verify import Tolerance


from iron.common.harness import run_test
from iron.common.image import OperatorImage
from iron.operators.flm.aie2p_math_emulation import f32_to_bf16_floor, rb
from iron.operators.flm.dequant.design import N_TILE, qw_bytes_for
from iron.operators.flm.dequant.op import DequantBFP, dequantize
from iron.operators.flm.gemm.op import GEMM
from iron.operators.flm.q4nx import GROUP, K_TILE, M_TILE, packed_bytes
from iron.operators.flm.testing import requires_aie2p

# K = 512 is one k-tile, where flm.GEMM at tile_n = 128 wins on NPU2. It
# defaults to 64 regardless, which is the order this operator emits.
SHAPES = [(512, 128), (1024, 128), (1024, 512), (1536, 640), (2048, 256)]


def scatter_runs(qw, K, N, run_out_features, run_period_out_features, seed=0):
    """Place a matrix's column blocks at their offsets in an interleaved
    buffer. The gaps hold noise, so an operator that reads them fails.
    """
    cb_bytes = packed_bytes(N_TILE * K)
    run_blocks = run_out_features // N_TILE
    period_blocks = run_period_out_features // N_TILE

    total = qw_bytes_for(K, N, run_out_features, run_period_out_features)
    out = np.random.default_rng(seed + 1).integers(0, 256, total, dtype=np.uint8)
    src = np.asarray(qw, dtype=np.uint8).reshape(-1, cb_bytes)
    for cb in range(N // N_TILE):
        at = ((cb // run_blocks) * period_blocks + cb % run_blocks) * cb_bytes
        out[at : at + cb_bytes] = src[cb]
    return out


def random_q4nx(K, N, seed=0):
    """A random q4nx blob. Scales and mins are bf16 in the file, so they are
    generated there and widened.
    """
    rng = np.random.default_rng(seed)
    n_blocks = (K // K_TILE) * (N // M_TILE)
    sm = (K_TILE // GROUP) * M_TILE

    scales = f32_to_bf16_floor(
        rng.uniform(0.002, 0.05, (n_blocks, sm)).astype(np.float32)
    )
    mins = f32_to_bf16_floor(rng.uniform(-0.4, 0.4, (n_blocks, sm)).astype(np.float32))
    codes = rng.integers(0, 256, (n_blocks, M_TILE * K_TILE // 2), dtype=np.uint8)
    return np.concatenate(
        [
            scales.view(np.uint8).reshape(n_blocks, -1),
            mins.view(np.uint8).reshape(n_blocks, -1),
            codes,
        ],
        axis=1,
    ).ravel()


def _check(op, blob, expected, label, record=None):
    errors, _, _ = run_test(
        op,
        {"qw": blob},
        {"out": expected},
        tolerance=Tolerance.exact(),
        record=record,
    )
    assert not errors, f"{label}: {errors}"


@requires_aie2p
@pytest.mark.parametrize("K, N", SHAPES)
def test_matches_reference(K, N, npu_runtime, record_property):
    """Byte-exact. Every rounding on the device is reproducible on the host, so
    a tolerance would hide a value landing in the wrong block.
    """
    qw = random_q4nx(K, N, seed=0)
    op = DequantBFP(K=K, N=N)
    _check(op, qw, op.reference(qw), f"K={K} N={N}", record_property)


@requires_aie2p
def test_output_feeds_gemm_unchanged(npu_runtime):
    """The output must equal what GEMM.pack_B produces, which is the contract
    that makes it a drop-in. Comparing against pack_B catches a drift in either
    operator's tiling that a self-consistent reference would not.
    """
    K, N = 1024, 128
    qw = random_q4nx(K, N, seed=3)
    w = dequantize(qw, K, N)
    w = rb(w)
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
    _check(op, blob, op.reference(qw), "gate/up interleave")


@requires_aie2p
@pytest.mark.parametrize(
    "K, N",
    [
        (4096, 1536),
        # Gemma 4 E2B's MLP down projection.
        pytest.param(6144, 1536, marks=pytest.mark.bench),
        pytest.param(12288, 1536, marks=pytest.mark.extensive),
    ],
)
def test_large_k_shapes(K, N, npu_runtime, record_property):
    """E2B's tall projections, whose k-tiles outnumber a shim tile's buffer
    descriptors. K = 12288 is 24 k-tiles, the deepest E2B reaches.
    """
    qw = random_q4nx(K, N, seed=21)
    op = DequantBFP(K=K, N=N)
    _check(op, qw, op.reference(qw), f"K={K} N={N}", record_property)


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
    _check(op, qw, op.reference(qw), f"K={K} N={N}")


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
    _check(op, blob, op.reference(qw), "E4B gate/up interleave")


@requires_aie2p
def test_one_xclbin_serves_every_shape(npu_runtime):
    """Several shapes and parameter sets back to back on one loaded xclbin.

    A model dispatches ten weight shapes against a budget of 16 hardware
    contexts. The parametrised tests cannot catch a regression here: each gets
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
        K, N = case["K"], case["N"]
        op = DequantBFP(**case)
        qw = random_q4nx(K, N, seed=7)
        blob = qw
        if case.get("run_out_features"):
            blob = scatter_runs(
                blob, K, N, case["run_out_features"], case["run_period_out_features"], 7
            )
        _check(op, blob, op.reference(qw), str(case))

        # A cache hit: the image _check built and ran.
        image = OperatorImage(op).compile().artifacts.image
        stamp = (str(image), os.path.getmtime(image))
        if xclbin is None:
            xclbin = stamp
        assert stamp == xclbin, f"{case} rebuilt the xclbin"


@pytest.mark.parametrize(
    "K, N, extra, exc, match",
    [
        # flm.GEMM may be asked for tile_n=128, the NPU2 winner at K = 512;
        # this operator does not emit that order and must say so.
        (512, 128, dict(tile_n=128), ValueError, "tile_n"),
        # Extents the grid does not divide: refused once the grid is known.
        (1000, 128, {}, ValueError, "multiple of"),
        (1024, 100, {}, ValueError, "multiple of"),
    ],
)
def test_rejects_unservable_shapes(K, N, extra, exc, match):
    with pytest.raises(exc, match=match):
        DequantBFP(K=K, N=N, **extra).resolved(from_name("npu2", n_cols=8))
