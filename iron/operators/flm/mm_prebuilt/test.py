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

import pytest

import aie.utils as aie_utils

from iron.common.test_utils import run_test
from iron.operators.flm.gemm.reference import generate_golden_reference
from iron.operators.flm.mm_prebuilt.op import MMPrebuilt

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
        (256, 512, 1024, "none", None),  # exactly one full 8-column sweep
        (512, 1024, 2048, "none", None),  # two full sweeps
        (256, 512, 640, "none", None),  # remainder only: 5 of 8 cols
        (256, 512, 1280, "none", None),  # full sweep + remainder: 1 of 8 cols
        (256, 512, 1024, "silu", None),
        (256, 512, 1024, "gelu", None),
        (256, 512, 1024, "sigmoid", None),
        (256, 512, 1024, "none", (-2.0, 2.0)),
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

    # Same absolute-mass bound as flm.gemm/test.py, for the same reason: with
    # signed A the K-sum cancels by ~sqrt(K), leaving near-zero outputs
    # relatively uncheckable under a plain relative tolerance.
    #
    # sigmoid and clamp are the exception: their output is bounded to a known,
    # narrow range (sigmoid to (0, 1), this clamp to (-2, 2)), far smaller than
    # the mass-based bound above -- which would then pass even an all-zero
    # result. Scale the tolerance to the actual output domain for those instead.
    if epilogue == "sigmoid":
        abs_tol = BUDGET_FLOOR
    elif clamp is not None:
        abs_tol = BUDGET_FLOOR * (clamp[1] - clamp[0])
    else:
        mass = (
            K
            * golden_ref["input"].abs().float().mean()
            * golden_ref["input_b"].abs().float().mean()
        )
        abs_tol = float(BUDGET_FLOOR * mass)
    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        rel_tol=0.04,
        abs_tol=abs_tol,
    )
    assert not errors, "Test failed"
