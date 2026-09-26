#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compare ``flm.GEMM`` against the overlay it was ported from and IRON's GEMM.

Up to three implementations run per shape, on identical inputs:

  flm      :class:`iron.exports.flm.GEMM`, the port
  gemm     :class:`iron.operators.GEMM` at its defaults, which are the same
           emulated-bfp16 mmul and conv_even rounding, so the comparison is
           like-for-like rather than against a more accurate, slower build
  prebuilt ``Shipped(...)`` (:mod:`iron.exports.flm.gemm.shipped`), FastFlowLM's shipped
           ``mm.xclbin``, pinned by digest. NPU2 only, since that binary is a
           fixed 8-column overlay; elsewhere it is dropped and the flm-vs-gemm
           comparison still runs.

The overlay is a ``RemoteFileArtifact`` pinned by SHA-256 against an immutable
FastFlowLM commit and fetched into the gitignored build dir, so nothing here
needs an external install or a host-specific path.

pytest never collects this: ``pytest.ini`` sets ``python_files = test.py``. It
is a timing comparison meant to be invoked directly, not a correctness gate;
the correctness half lives in ``iron/exports/flm/gemm/test.py``.

Timing is the runtime's device-side ``npu_time`` rather than a host wall clock,
so it compares the designs rather than the driver.

Pass ``--iterations 1``. Each test already averages ``ITERS`` dispatches over
``ROUNDS`` interleaved rounds, so conftest's default of 5 repeats the whole
matrix five times for nothing.

Usage::

    pytest iron/exports/flm/gemm/benchmark.py --iterations 1
    pytest iron/exports/flm/gemm/benchmark.py --iterations 1 -k E2B --csv-output flm.csv

Do not pass ``-s`` when you want the CSV: conftest's reporter parses the
captured stdout, so disabling capture yields a CSV with no metric columns.
"""

import statistics
from pathlib import Path

import numpy as np
import pytest
import torch
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

from iron.common.device import bound_device, device_name
from iron.common.harness import record_metric
from iron.exports.flm import GEMM as FLMGEMM
from iron.exports.flm import Shipped
from iron.operators import GEMM as IronGEMM

# Opt-in only: this module downloads the overlay, so keep it out of the default
# run. See the note in the module docstring.
pytestmark = pytest.mark.extensive

_dev = bound_device()
# The shipped overlay is a fixed 8-column NPU2 binary. Where that does not
# match the device, drop that one candidate rather than skipping the module,
# since flm vs iron.operators.GEMM is measurable on every supported device.
HAVE_PREBUILT = _dev is not None and device_name(_dev) == "npu2" and _dev.cols >= 8

# Every projection of both Gemma4 variants FastFlowLM ships, at three prefill
# lengths. E2B is dim 1536 / ffn 6144; E4B is dim 2560 / ffn 10240. Both ship
# the same mm.xclbin blob (checked at FastFlowLM f81eba71), so between them
# they cover it. Gemma4-12B ships no mm.xclbin at all -- its projections go
# through a quantized matmul -- so it cannot be compared against the shipped image.
#             proj,      K,      N
E2B_PROJ = [
    ("q", 1536, 4096),
    ("kv", 1536, 512),
    ("o", 4096, 1536),
    ("gateup", 1536, 6144),
    ("down", 6144, 1536),
]
E4B_PROJ = [
    ("q", 2560, 4096),
    ("kv", 2560, 1024),
    ("o", 4096, 2560),
    ("gateup", 2560, 10240),
    ("down", 10240, 2560),
]
PREFILL_LENGTHS = [256, 1024, 2048]

# Interleaved rounds per test, and timed dispatches per implementation per
# round. 6 rounds is the floor at which min and median stopped disagreeing.
ROUNDS = 6
ITERS = 30
WARMUP = 20

# err/mass budgets. flm.GEMM and IRON's GEMM both round conv_even; the shipped
# overlay never calls set_rounding, so it runs in the core's power-up floor mode
# and carries a ~1% truncation bias that is not a bug to fix here.
BUDGET_CONV_EVEN = 4e-3
BUDGET_FLOOR = 2e-2


def get_params():
    # No shape is skipped. The four E4B projections with a 10240-wide dimension
    # at M > 256 once overflowed the shim BD's 20-bit mega_row iteration step,
    # but flm.GEMM and IRON's GEMM both split that leg into per-mega_row
    # transfers now (design.py's a_split/c_split, test_gemm_split_leg_bounds).
    params = []
    for model, projections in (("E2B", E2B_PROJ), ("E4B", E4B_PROJ)):
        for M in PREFILL_LENGTHS:
            for proj, K, N in projections:
                params.append(
                    pytest.param(model, proj, M, K, N, id=f"{model}-{proj}-M{M}")
                )
    return params


def make_inputs(M, K, N):
    """Identical data for all three, and the reference to check them against."""
    torch.manual_seed(1234)
    A = (torch.randn(M, K) * 4).to(torch.bfloat16)
    B = (torch.rand(K, N) * 4).to(torch.bfloat16)
    Af, Bf = A.float(), B.float()
    # Bounded against accumulated mass rather than relatively; see test.py.
    return A, B, Af @ Bf, float((Af.abs() @ Bf.abs()).mean())


class Candidate:
    """One implementation under test, with its buffers already bound so the
    timed section contains nothing but the dispatch.
    """

    def __init__(self, name, op, A, B, M, N, budget, ctx):
        self.name = name
        self.budget = budget
        self.round_medians = []

        op.compile()
        self.xclbin = Path(op.artifacts.image)
        self.c_bo = XRTTensor((M, N), dtype=np.dtype("bfloat16"))
        run = op.get_callable()
        # Only the flm operators take B pre-packed. iron.operators.GEMM
        # reorders in the descriptor, so it wants plain row-major (K, N).
        packed_b = op.pack_B(B) if hasattr(op, "pack_B") else B
        args = [
            XRTTensor.from_torch(A.flatten()),
            XRTTensor.from_torch(packed_b.flatten()),
            self.c_bo,
        ]
        self.run = lambda: run(*args)

    def verify(self, M, N, expected, mass):
        self.run()
        C = self.c_bo.to_torch().reshape(M, N).float()
        self.err = float((C - expected).abs().mean()) / mass
        return self.err < self.budget

    def time_round(self):
        # npu_time is the device-side execution time the runtime reports, in ns.
        ts = [self.run().npu_time / 1e3 for _ in range(ITERS)]
        self.round_medians.append(statistics.median(ts))

    @property
    def us(self):
        # Minimum of the per-round medians: the median rejects the tail within
        # a round, the min rejects rounds that landed in the slow mode.
        return min(self.round_medians)

    @property
    def jitter_pct(self):
        """Spread of the per-round medians -- how bimodal this run actually was."""
        return (max(self.round_medians) - self.us) / self.us * 100.0


@pytest.mark.parametrize("model,proj,M,K,N", get_params())
def test_gemm_vs_prebuilt(model, proj, M, K, N, npu_runtime):
    A, B, expected, mass = make_inputs(M, K, N)

    # Build everything before timing anything. Comparing frozen binaries is the
    # only way an A/B here means what it says.
    candidates = [
        Candidate(
            "flm",
            FLMGEMM(M=M, K=K, N=N),
            A,
            B,
            M,
            N,
            BUDGET_CONV_EVEN,
            npu_runtime,
        ),
        Candidate(
            "gemm",
            IronGEMM(M=M, K=K, N=N),
            A,
            B,
            M,
            N,
            BUDGET_CONV_EVEN,
            npu_runtime,
        ),
    ]
    if HAVE_PREBUILT:
        candidates.append(
            Candidate(
                "prebuilt",
                Shipped(M=M, K=K, N=N),
                A,
                B,
                M,
                N,
                BUDGET_FLOOR,
                npu_runtime,
            )
        )

    bad = [c for c in candidates if not c.verify(M, N, expected, mass)]
    assert not bad, "; ".join(
        f"{c.name} err/mass {c.err:.3g} exceeds {c.budget:g}" for c in bad
    )

    for c in candidates:
        for _ in range(WARMUP):
            c.run()
    # Round-robin, never all of one then all of another. Dispatch latency here
    # is bimodal with modes about 6% apart, so a batch landing wholly in one
    # mode turns min-of-medians into a mode selector. That is how a change
    # later shown to do nothing once produced a convincing 5% "win".
    for _ in range(ROUNDS):
        for c in candidates:
            c.time_round()

    by_name = {c.name: c for c in candidates}
    flm = by_name["flm"]

    # Recorded for the CSV as well as printed: the error budget below is loose
    # enough that a toolchain change could move the error a long way inside it
    # unnoticed, so the numbers are kept too.
    print()
    label = {"flm": "FLM", "prebuilt": "Prebuilt", "gemm": "GEMM"}
    for c in candidates:
        kb = c.xclbin.stat().st_size / 1024
        print(f"{c.name} latency (us): {c.us:.1f}")
        print(f"{c.name} err/mass: {c.err:.3e}")
        print(f"{c.name} xclbin (KB): {kb:.1f}")
        record_metric(f"{label[c.name]}Latency", c.us)
        record_metric(f"{label[c.name]}Err", c.err)
        record_metric(f"{label[c.name]}XclbinKB", kb)
    if "prebuilt" in by_name:
        print(f"speedup vs prebuilt: {by_name['prebuilt'].us / flm.us:.3f}")
        record_metric("SpeedupVsPrebuilt", by_name["prebuilt"].us / flm.us)
    print(f"speedup vs gemm: {by_name['gemm'].us / flm.us:.3f}")
    record_metric("SpeedupVsGEMM", by_name["gemm"].us / flm.us)
    throughput = 2.0 * M * K * N / (flm.us * 1e-6) / 1e9
    print(f"flm throughput: {throughput:.6e} GFLOP/s")
    print(f"flm jitter (%): {flm.jitter_pct:.2f}")
    record_metric("FLMThroughput", throughput)
    record_metric("FLMJitterPct", flm.jitter_pct)
    print()
