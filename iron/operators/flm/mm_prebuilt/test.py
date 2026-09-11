#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Correctness for :class:`iron.operators.flm.MMPrebuilt`.

Extensive only: constructing the operator downloads FastFlowLM's shipped
``mm.xclbin`` over the network (see ``op.py``), and a developer running the
default operator suite should not trip that download. Unlike
``iron/operators/flm/gemm/benchmark.py`` -- which times this operator against
``flm.GEMM`` and IRON's ``GEMM`` at production shapes but is never collected,
named as it is -- this module IS named ``test.py``, so the extensive CI job
actually runs it.
"""

import numpy as np
import pytest
import torch

import aie.utils as aie_utils

from iron.common.test_utils import run_test
from iron.operators.flm.gemm.reference import (
    apply_epilogue,
    generate_golden_reference,
)
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.mm_prebuilt.op import MMPrebuilt

NONE, GELU, SILU, SIGMOID = Epilogue

# Largest |d/dx| of each epilogue, used to carry the accumulator's error bound
# through to the output. sigmoid's is exactly 1/4; silu and gelu both peak at
# 1.0998 (gelu here being the x*sigmoid(1.702x) approximation the overlay
# implements, whose derivative happens to share silu's maximum), rounded up.
MAX_SLOPE = {NONE: 1.0, SIGMOID: 0.25, SILU: 1.1, GELU: 1.1}

pytestmark = pytest.mark.extensive

_dev = aie_utils.get_current_device()
if _dev.resolve().name != "npu2" or _dev.cols < 8:
    pytest.skip(
        "the prebuilt FastFlowLM overlay is an 8-column NPU2 binary; "
        f"this device is {_dev.resolve().name!r} with {_dev.cols} columns",
        allow_module_level=True,
    )

# The overlay never calls set_rounding, so it runs in the core's power-up floor
# mode and carries a ~1% truncation bias -- not a bug. See gemm/benchmark.py.
BUDGET_FLOOR = 2e-2


@pytest.mark.parametrize(
    "M,K,N,epilogue,clamp",
    [
        (256, 512, 1024, NONE, None),  # exactly one full 8-column sweep
        (512, 1024, 2048, NONE, None),  # two full sweeps
        (256, 512, 640, NONE, None),  # remainder only: 5 of 8 cols
        (256, 512, 1280, NONE, None),  # full sweep + remainder: 1 of 8 cols
        (256, 512, 1024, SILU, None),
        (256, 512, 1024, GELU, None),
    ],
)
def test_mm_prebuilt(M, K, N, epilogue, clamp, aie_context):
    golden_ref = generate_golden_reference(
        M=M, K=K, N=N, epilogue=epilogue, clamp=clamp
    )

    operator = MMPrebuilt(
        M=M, K=K, N=N, epilogue=epilogue, clamp=clamp, context=aie_context
    )

    input_buffers = {
        "A": golden_ref["input"].flatten(),
        # B is consumed pre-packed; see MMPrebuilt.pack_B.
        "B": operator.pack_B(golden_ref["input_b"]),
    }
    output_buffers = {"C": golden_ref["output"].flatten()}

    # The overlay's error is made in the ACCUMULATOR -- it runs in the core's
    # power-up floor rounding, worth about BUDGET_FLOOR of the accumulated mass
    # -- and the epilogue then maps that accumulator through an activation. So
    # the output bound is the accumulator bound carried through the activation,
    # |f(x+e) - f(x)| <= max|f'| * |e|, rather than a tolerance invented in the
    # output domain.
    #
    # Only the unbounded epilogues are checked this way. For sigmoid and clamp
    # no bound over this reference can be both correct and useful -- the
    # accumulator error alone exceeds their whole output range -- so they are
    # covered functionally by test_mm_prebuilt_epilogue_matches_accumulator.
    mass = float(
        K
        * golden_ref["input"].abs().float().mean()
        * golden_ref["input_b"].abs().float().mean()
    )
    abs_tol = MAX_SLOPE[epilogue] * BUDGET_FLOOR * mass
    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        rel_tol=0.04,
        abs_tol=abs_tol,
    )
    assert not errors, "Test failed"


@pytest.mark.parametrize(
    "epilogue,clamp",
    [
        (SIGMOID, None),
        (NONE, (-2.0, 2.0)),
        (SILU, None),
        (GELU, None),
    ],
)
def test_mm_prebuilt_epilogue_matches_accumulator(epilogue, clamp, aie_context):
    """The epilogue is the right function of the accumulator the device produced.

    Checking a bounded epilogue against the idealized CPU reference cannot work.
    The overlay accumulates in the core's power-up floor rounding, worth ~2% of
    the accumulated mass, which here is ~65 -- larger than sigmoid's entire (0,1)
    range and than this clamp's (-2, 2). Any bound wide enough to admit that
    accumulator error also admits an all-zero result, and any bound tight enough
    to reject all-zeros also rejects correct hardware. That is why the earlier
    flat tolerance failed on working arithmetic.

    So compare the epilogue against the device's OWN accumulator instead: run
    the same inputs with no epilogue, apply the activation and clamp to that on
    the host, and require the epilogue build to agree. The accumulator error is
    then common to both sides and cancels, leaving only the epilogue under test.
    An all-zero result still fails, because the reference side is not zero.
    """
    M, K, N = 256, 512, 1024
    # A small input scale keeps the accumulator in the range where these curves
    # are actually curved; at the default scale the product lands around +-900,
    # where gelu and silu are indistinguishable from the identity.
    golden_ref = generate_golden_reference(M=M, K=K, N=N, scale=0.5)
    A = golden_ref["input"]
    B = golden_ref["input_b"]

    def run(epi, clm):
        op = MMPrebuilt(M=M, K=K, N=N, epilogue=epi, clamp=clm, context=aie_context)
        op.compile()
        tensor = aie_utils.DEFAULT_TENSOR_CLASS
        out = tensor((M, N), dtype=np.dtype("bfloat16"))
        op.get_callable()(
            tensor.from_torch(A.flatten()), tensor.from_torch(op.pack_B(B)), out
        )
        return out.to_torch().reshape(M, N).float()

    acc = run(NONE, None)
    got = run(epilogue, clamp)
    expected = apply_epilogue(acc, epilogue, clamp)

    # Both sides see the same accumulator, so what is left is the epilogue.
    # Two terms, and they are different in kind.
    #
    # The bf16 term is per element rather than one global number: the
    # accumulator read back is bf16, good to ~2^-8 RELATIVELY, and clamp is only
    # sensitive near its boundary, so a tolerance taken from the accumulator's
    # largest magnitude would be wider there than the clamp range itself -- i.e.
    # vacuous.
    #
    # The activation term covers what bf16 rounding does NOT explain. Checked by
    # bounding the true accumulator to its bf16 rounding interval and evaluating
    # the epilogue across it: clamp lands inside for all 262144 elements, but
    # sigmoid, silu and gelu land outside for about half, by up to 0.018. That
    # residual is the overlay's own activation approximation -- a LUT or native
    # instruction, not exact math -- which no reference built on torch.sigmoid
    # can reproduce. 0.05 is ~3x the measured worst case and still ~20x below
    # where the bound would go vacuous; the assertion at the end pins that down.
    approx = 0.0 if epilogue is NONE else 0.05
    tol = MAX_SLOPE[epilogue] * acc.abs() * 2.0**-8 + 2.0**-8 + approx
    err = (got - expected).abs()
    over = err > tol
    assert not over.any(), (
        f"{epilogue} clamp={clamp}: {int(over.sum())} of {over.numel()} elements "
        f"differ from epilogue(device accumulator) by more than the bf16 bound; "
        f"worst {float((err - tol).max()):.4f} over"
    )
    # The bound must not be wide enough to admit a dead device.
    assert (
        expected.abs() > tol
    ).any(), f"{epilogue}: tolerance is vacuous -- an all-zero result would pass"
