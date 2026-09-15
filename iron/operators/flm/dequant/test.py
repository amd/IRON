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
from iron.operators.flm.dequant.design import QwLayout
from iron.operators.flm.dequant.op import DequantBFP
from iron.operators.flm.dequant.reference import (
    random_q4nx,
    reference,
    scatter_runs,
    to_engine_order,
)

# K must be a multiple of 512 and N of 64. K = 512 is excluded on purpose:
# flm.GEMM picks tile_n = 128 there, which this operator refuses, and
# test_rejects_the_tile_n_128_shape covers that.
SHAPES = [(1024, 128), (1536, 640), (2048, 256)]


def _on_aie2p():
    dev = aie_utils.get_current_device()
    return dev is not None and dev.arch == AIEArch.AIE2p


requires_aie2p = pytest.mark.skipif(
    not _on_aie2p(), reason="bfp16ebs8 exists only on AIE2P"
)


@requires_aie2p
@pytest.mark.parametrize("K, N", SHAPES)
def test_matches_reference(K, N, aie_context):
    """Byte-exact, not approximate.

    Every rounding on the device is reproducible on the host: the q4nx dequant
    is exact in f32, the f32 to bf16 step rounds toward negative infinity, and
    the bfp16 conversion truncates. A tolerance here would hide exactly the
    failure this operator is prone to -- a value landing in the wrong block.
    """
    op = DequantBFP(K=K, N=N, context=aie_context)
    qw = random_q4nx(K, N, seed=0)

    errors, _, _ = run_test(
        op,
        {"in": torch.from_numpy(qw)},
        {"out": torch.from_numpy(reference(qw, K, N))},
        rel_tol=0.0,
        abs_tol=0.0,
    )
    assert not errors, f"byte mismatch: {errors}"


@requires_aie2p
def test_output_feeds_gemm_unchanged(aie_context):
    """The operator's output must be what GEMM.pack_B would have produced.

    This is the contract that makes it a drop-in: the runtime stops packing
    weights on the host and points the GEMM at this buffer instead. Comparing
    against pack_B directly catches a drift in either operator's tiling, which
    a self-consistent reference would not.
    """
    from iron.operators.flm.gemm.op import GEMM
    from iron.operators.flm.dequant.reference import dequantize, f32_to_bf16_floor

    K, N = 1024, 128
    qw = random_q4nx(K, N, seed=3)

    w = dequantize(qw, K, N)
    w = (f32_to_bf16_floor(w).astype(np.uint32) << 16).view(np.float32)
    gemm = GEMM(M=256, K=K, N=N, tile_n=64, rounding="floor", context=aie_context)
    packed = gemm.pack_B(torch.from_numpy(np.ascontiguousarray(w.T))).numpy()

    errors, _, _ = run_test(
        DequantBFP(K=K, N=N, context=aie_context),
        {"in": torch.from_numpy(qw)},
        {"out": torch.from_numpy(packed)},
        rel_tol=0.0,
        abs_tol=0.0,
    )
    assert not errors, f"does not match GEMM.pack_B: {errors}"


@requires_aie2p
@pytest.mark.parametrize("K, N", [(1024, 512), (1536, 640)])
def test_engine_order_input(K, N, aie_context):
    """The engine reorders blocks as it reads from disk, so the operator has to
    read that order. Same bytes out as from file order, by construction."""
    qw = random_q4nx(K, N, seed=11)
    errors, _, _ = run_test(
        DequantBFP(K=K, N=N, qw_layout=QwLayout.ENGINE, context=aie_context),
        {"in": torch.from_numpy(to_engine_order(qw, K, N))},
        {"out": torch.from_numpy(reference(qw, K, N))},
        rel_tol=0.0,
        abs_tol=0.0,
    )
    assert not errors, f"K={K} N={N} byte mismatch: {errors}"


@requires_aie2p
def test_gate_up_interleaved_blob(aie_context):
    """gate and up share one blob at 512 out-features in a 1024 period.

    The gaps hold the other matrix, filled with noise here: an operator that
    strides wrongly reads it and fails the byte check rather than producing
    something plausible.
    """
    K, N, run, period = 1024, 1024, 512, 1024
    qw = random_q4nx(K, N, seed=12)
    blob = scatter_runs(to_engine_order(qw, K, N), K, N, run, period, seed=12)

    op = DequantBFP(
        K=K,
        N=N,
        qw_layout=QwLayout.ENGINE,
        run_out_features=run,
        run_period_out_features=period,
        context=aie_context,
    )
    assert op.quantized_size() == blob.size

    errors, _, _ = run_test(
        op,
        {"in": torch.from_numpy(blob)},
        {"out": torch.from_numpy(reference(qw, K, N))},
        rel_tol=0.0,
        abs_tol=0.0,
    )
    assert not errors, f"byte mismatch: {errors}"


@requires_aie2p
@pytest.mark.parametrize(
    "K, N",
    [
        (4096, 1536),  # o, global layers
        (6144, 1536),  # down
        pytest.param(12288, 1536, marks=pytest.mark.extensive),  # down, skip layers
    ],
)
def test_large_k_shapes(K, N, aie_context):
    """E2B's tall projections, which need more k-tiles than a shim tile has BDs.

    A column block costs BDS_PER_K_TILE descriptors per k-tile, so queueing a
    whole one at K = 4096 asks for 25 of a shim tile's 16. The sequence windows
    them instead. K = 12288 is 24 k-tiles, the deepest E2B reaches.
    """
    qw = random_q4nx(K, N, seed=21)
    errors, _, _ = run_test(
        DequantBFP(K=K, N=N, qw_layout=QwLayout.ENGINE, context=aie_context),
        {"in": torch.from_numpy(to_engine_order(qw, K, N))},
        {"out": torch.from_numpy(reference(qw, K, N))},
        rel_tol=0.0,
        abs_tol=0.0,
    )
    assert not errors, f"K={K} N={N} byte mismatch: {errors}"


@requires_aie2p
def test_layout_flag_survives_a_plain_string(aie_context):
    """The design must accept the layout as a bare str, not only as the enum.

    QwLayout is a StrEnum and the design generator round-trips its arguments,
    so the design sees ``"engine"`` rather than ``QwLayout.ENGINE``. An ``is``
    comparison against the enum is silently false there and falls through to
    file order, which emits a right-sized buffer in the wrong order -- the one
    failure mode nothing but a byte check catches.
    """
    from iron.operators.flm.dequant.design import dequant_bfp

    dev = aie_utils.get_current_device()
    as_enum = str(dequant_bfp(dev, 1024, 512, qw_layout=QwLayout.ENGINE))
    as_str = str(dequant_bfp(dev, 1024, 512, qw_layout="engine"))
    as_file = str(dequant_bfp(dev, 1024, 512, qw_layout=QwLayout.FILE))

    assert as_enum == as_str, "a bare string took a different path than the enum"
    assert as_enum != as_file, "the layout flag changed nothing"


@requires_aie2p
def test_one_xclbin_serves_every_shape(aie_context):
    """Several shapes back to back on one loaded xclbin.

    This is what makes the operator usable in a model. A model dispatches ten
    weight shapes against a budget of 16 hardware contexts, so a shape-keyed
    xclbin would exhaust it and pay a reconfiguration per projection. The
    parametrised tests above cannot catch a regression here: each gets a fresh
    context, so the array is reconfigured between cases anyway.

    One shape leaves three of the eight columns without work, which is the case
    that a compile-time trip count could not express -- a core that never
    acquires fails lowering outright.
    """
    # The last two vary qw_layout and the interleave, which must not reach the
    # xclbin either: they only move offsets and strides in the sequence.
    cases = [
        dict(K=1536, N=2048),
        dict(K=1024, N=320),
        dict(K=2048, N=1536),
        dict(K=1536, N=2560),
        dict(K=1024, N=512, qw_layout=QwLayout.ENGINE),
        dict(
            K=1024,
            N=1024,
            qw_layout=QwLayout.ENGINE,
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
        if case.get("qw_layout") is QwLayout.ENGINE:
            blob = to_engine_order(qw, K, N)
        if case.get("run_out_features"):
            blob = scatter_runs(
                blob, K, N, case["run_out_features"], case["run_period_out_features"], 7
            )
        errors, _, _ = run_test(
            op,
            {"in": torch.from_numpy(blob)},
            {"out": torch.from_numpy(reference(qw, K, N))},
            rel_tol=0.0,
            abs_tol=0.0,
        )
        assert not errors, f"{case} byte mismatch: {errors}"

        stamp = (
            op.xclbin_artifact.filename,
            os.path.getmtime(op.xclbin_artifact.filename),
        )
        if xclbin is None:
            xclbin = stamp
        assert stamp == xclbin, f"K={K} N={N} rebuilt the xclbin"


@requires_aie2p
def test_rejects_the_tile_n_128_shape(aie_context):
    """K = 512 makes flm.GEMM choose tile_n = 128, a different packed order.

    Emitting the tile_n = 64 order there would produce a buffer of the right
    size that the GEMM reads wrongly, with no error anywhere.
    """
    with pytest.raises(NotImplementedError, match="tile_n"):
        DequantBFP(K=512, N=128, context=aie_context)


@pytest.mark.parametrize("K, N", [(1000, 128), (1024, 100)])
def test_rejects_untileable_shapes(K, N, aie_context):
    with pytest.raises(ValueError, match="multiple of"):
        DequantBFP(K=K, N=N, context=aie_context)


if __name__ == "__main__":
    run_test(__file__)
