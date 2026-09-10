#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Benchmark flm_gemm against the shipped FastFlowLM overlay and IRON's generic GEMM.

Kept out of ``test.py`` on purpose: this file needs an external FastFlowLM
install, which the operator itself does not. ``test.py`` must stay runnable in
CI with nothing but this repo; this one skips the whole module when the install
is absent.

Every shape is one test, covering the real Gemma4 projections (E2B and E4B x
{q, kv, o, gateup, down}) at three prefill lengths. Three competitors run per
shape:

  iron : the ``FLMGEMM`` operator (arg order A, B, C)
  flm  : FastFlowLM's shipped ``mm.xclbin`` + its dumped TXN insts (order C, A, B)
  gemm : IRON's generic ``GEMM`` operator, same emulated-bfp16 numerics

The box is bimodal by ~6% (see the npu-bimodal-timing note), so the three are
interleaved round-robin over several rounds and each is scored by the MINIMUM
of its per-round medians. Running all of one competitor and then all of another
fabricates differences of about that size. Everything is compiled up front;
nothing is rebuilt between rounds.

No time is reported for a dispatch whose output was not checked.

Usage::

    pytest iron/operators/flm_gemm/bench_vs_flm.py --iterations 1
    pytest iron/operators/flm_gemm/bench_vs_flm.py -k E2B --csv-output flm.csv
"""

import os
import statistics
import subprocess
import time
from pathlib import Path

import numpy as np
import pytest
import torch

import aie.utils as aie_utils
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

from iron.operators.flm_gemm.op import FLMGEMM
from iron.operators.gemm.op import GEMM

# ---------------------------------------------------------------------------
# External FastFlowLM install. Both are overridable so this is not pinned to
# one machine's layout; absent either, the module skips rather than errors.
# ---------------------------------------------------------------------------
FLM_XCLBIN = Path(
    os.environ.get(
        "FLM_MM_XCLBIN",
        "/scratch/ehunhoff/flm-release-1.0.4/extracted/opt/fastflowlm/share/flm"
        "/xclbins/Gemma4-E2B-IT-NPU2/mm.xclbin",
    )
)
# Dumps the overlay's control instructions for one (M, K, N). The generator
# baked into it is gemma4_e2b_mm_txn, so it belongs to the xclbin above.
# Previously lived in /tmp, which is tmpfs here and did not survive reboots.
TXN_DUMP = Path(
    os.environ.get("FLM_TXN_DUMP", "/scratch/ehunhoff/flm_gemm_bench/txn/dump")
)
TXN_CACHE = Path(os.environ.get("FLM_TXN_CACHE", TXN_DUMP.parent))

# The shipped overlay is a fixed n=128 design; its B layout is not negotiable.
FLM_N_TILE = 128
# B's memtile odometer, shared by both packers. K_TILE is the operator's.
K_TILE, S, T = 512, 8, 8

# Interleaved rounds per test, and timed dispatches per competitor per round.
# 6 rounds is the floor at which min and median stopped disagreeing on this box.
ROUNDS = 6
ITERS = 30
WARMUP = 20

# err/mass budgets. iron and gemm both round conv_even; the shipped overlay
# never calls set_rounding, so it runs in the core's power-up floor mode and
# carries a ~1% truncation bias that is not a bug to fix here.
BUDGET_CONV_EVEN = 4e-3
BUDGET_FLOOR = 2e-2


def _flm_available():
    return FLM_XCLBIN.is_file() and os.access(TXN_DUMP, os.X_OK)


if not _flm_available():
    pytest.skip(
        f"FastFlowLM install not found (looked for {FLM_XCLBIN} and {TXN_DUMP}); "
        "set FLM_MM_XCLBIN / FLM_TXN_DUMP to point at one",
        allow_module_level=True,
    )

_dev = aie_utils.get_current_device()
if _dev.cols < 8 or _dev.resolve().name != "npu2":
    pytest.skip(
        "flm_gemm is a fixed 4x8 npu2 design; this device cannot run it",
        allow_module_level=True,
    )


# ---------------------------------------------------------------------------
# Shapes
# ---------------------------------------------------------------------------
# Every projection of both Gemma4 variants FastFlowLM ships, at three prefill
# lengths. E2B is dim 1536 / ffn 6144; E4B is dim 2560 / ffn 10240.
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

# The two E4B projections with a 10240-wide dimension need a shim DMA
# descriptor stride past the AIE2p shim's 20-bit step field once M walks more
# than one mega_row. design.py rejects them at construction; see its comment
# and test.py's test_flm_gemm_stride_overflow_rejected. They are skipped here
# rather than left to raise, so the sweep reports 26 results and 4 known
# blocks instead of 4 errors.
BLOCKED = "K/N=10240 at M>256 overflows the shim's 20-bit DMA stride field"


def get_params():
    params = []
    for model, projections in (("E2B", E2B_PROJ), ("E4B", E4B_PROJ)):
        for M in PREFILL_LENGTHS:
            for proj, K, N in projections:
                blocked = M > 256 and max(K, N) > 8191
                marks = [pytest.mark.skip(reason=BLOCKED)] if blocked else []
                params.append(
                    pytest.param(
                        model, proj, M, K, N, marks=marks, id=f"{model}-{proj}-M{M}"
                    )
                )
    return params


# ---------------------------------------------------------------------------
# Inputs and packing
# ---------------------------------------------------------------------------
def make_inputs(M, K, N):
    """Identical data for all three competitors, and the reference to check."""
    torch.manual_seed(1234)
    A = (torch.randn(M, K) * 4).to(torch.bfloat16)
    B = (torch.rand(K, N) * 4).to(torch.bfloat16)
    Af, Bf = A.float(), B.float()
    # Error is bounded against accumulated mass, not relatively: with signed A
    # the K-sum cancels by ~sqrt(K), so |C| ends up far smaller than the
    # magnitude the bfp16 error actually tracks, and near-zero outputs are
    # relatively uncheckable. Same rationale as test.py's bound.
    return A, B, Af @ Bf, float((Af.abs() @ Bf.abs()).mean())


def flm_pack_B(Bt, n_tile=FLM_N_TILE):
    """(K, N) row-major -> the shipped overlay's memtile order.

    Odometer (n//T, k%S, k//S, n%T), tiles ordered by column stripe then
    k-block. Mirrors ``FLMGEMM.pack_B``'s tiling but stops at bf16: the
    overlay consumes bf16, not the bfp16 blocks the IRON operator takes, and
    is fixed at n=128 regardless of what the IRON operator chooses.
    """
    b = Bt.float().numpy()
    K, N = b.shape
    out = []
    for cb in range(N // n_tile):
        stripe = b[:, cb * n_tile : (cb + 1) * n_tile]
        for kb in range(K // K_TILE):
            tile = stripe[kb * K_TILE : (kb + 1) * K_TILE, :]
            out.append(
                tile.reshape(K_TILE // S, S, n_tile // T, T)
                .transpose(2, 1, 0, 3)
                .ravel()
            )
    return torch.from_numpy(np.concatenate(out).astype(np.float32)).to(torch.bfloat16)


def flm_insts(M, K, N):
    """Path to the overlay's TXN insts for one shape, dumping it if absent."""
    path = TXN_CACHE / f"txn_{M}_{K}_{N}.bin"
    if not path.is_file():
        path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([str(TXN_DUMP), str(M), str(K), str(N), str(path)], check=True)
    return path


# ---------------------------------------------------------------------------
# Competitors. Each returns (run, c_bo, label, xclbin_path) with the buffers
# already bound, so the timed section is nothing but the dispatch.
# ---------------------------------------------------------------------------
def _bind(xclbin, insts, args):
    from aie.utils.npukernel import NPUKernel

    handle = aie_utils.DefaultNPURuntime.load(NPUKernel(str(xclbin), str(insts)))
    return lambda: aie_utils.DefaultNPURuntime.run(handle, list(args))


def setup_iron(M, K, N, A, B, ctx):
    op = FLMGEMM(M=M, K=K, N=N, context=ctx)
    built_before = _artifacts_exist(op, ctx)
    t0 = time.perf_counter()
    op.compile()
    compile_s = time.perf_counter() - t0
    c_bo = XRTTensor((M, N), dtype=np.dtype("bfloat16"))
    run = op.get_callable()
    args = [
        XRTTensor.from_torch(A.flatten()),
        XRTTensor.from_torch(op.pack_B(B).flatten()),
        c_bo,
    ]
    return _Competitor(
        "iron",
        lambda: run(*args),
        c_bo,
        Path(op.xclbin_artifact.filename),
        None if built_before else compile_s,
        BUDGET_CONV_EVEN,
    )


def setup_gemm(M, K, N, A, B, ctx):
    # Left at the operator's defaults, which are the same emulated-bfp16 mmul
    # and conv_even rounding flm_gemm uses -- a like-for-like comparison, not
    # flm_gemm against a more accurate and necessarily slower configuration.
    op = GEMM(M=M, K=K, N=N, context=ctx)
    built_before = _artifacts_exist(op, ctx)
    t0 = time.perf_counter()
    op.compile()
    compile_s = time.perf_counter() - t0
    c_bo = XRTTensor((M, N), dtype=np.dtype("bfloat16"))
    run = op.get_callable()
    # b_col_maj defaults False, so B goes in as plain row-major (K, N).
    args = [XRTTensor.from_torch(A.flatten()), XRTTensor.from_torch(B.flatten()), c_bo]
    return _Competitor(
        "gemm",
        lambda: run(*args),
        c_bo,
        Path(op.xclbin_artifact.filename),
        None if built_before else compile_s,
        BUDGET_CONV_EVEN,
    )


def setup_flm(M, K, N, A, B, ctx):
    c_bo = XRTTensor((M, N), dtype=np.dtype("bfloat16"))
    # The shipped overlay's host contract is C, A, B -- not IRON's A, B, C.
    args = [
        c_bo,
        XRTTensor.from_torch(A.flatten()),
        XRTTensor.from_torch(flm_pack_B(B).flatten()),
    ]
    run = _bind(FLM_XCLBIN, flm_insts(M, K, N), args)
    # Prebuilt and shipped: there is no compile to time.
    return _Competitor("flm", run, c_bo, FLM_XCLBIN, None, BUDGET_FLOOR)


class _Competitor:
    def __init__(self, name, run, c_bo, xclbin, compile_s, budget):
        self.name = name
        self.run = run
        self.c_bo = c_bo
        self.xclbin = xclbin
        self.compile_s = compile_s
        self.budget = budget
        self.round_medians = []

    def verify(self, M, N, expected, mass):
        self.run()
        C = self.c_bo.to_torch().reshape(M, N).float()
        self.err = float((C - expected).abs().mean()) / mass
        return self.err < self.budget

    def time_round(self):
        ts = []
        for _ in range(ITERS):
            t0 = time.perf_counter()
            self.run()
            ts.append((time.perf_counter() - t0) * 1e6)
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


def _artifacts_exist(op, ctx):
    """Whether this operator's xclbin is already built in ctx's build dir.

    Compile time is only meaningful on a genuine miss; on a hit ``compile()``
    returns in milliseconds and reporting that as a build time would be a lie.
    """
    if not op.artifacts:
        op.set_up_artifacts()
    return (Path(ctx.build_dir) / f"{op.name}.xclbin").is_file()


# ---------------------------------------------------------------------------
# The benchmark
# ---------------------------------------------------------------------------
@pytest.mark.metrics(
    IronLatency=r"iron latency \(us\): (?P<value>[\d\.]+)",
    FLMLatency=r"flm latency \(us\): (?P<value>[\d\.]+)",
    GEMMLatency=r"gemm latency \(us\): (?P<value>[\d\.]+)",
    SpeedupVsFLM=r"speedup vs flm: (?P<value>[\d\.]+)",
    SpeedupVsGEMM=r"speedup vs gemm: (?P<value>[\d\.]+)",
    IronThroughput=r"iron throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
    IronJitterPct=r"iron jitter \(%\): (?P<value>[\d\.]+)",
    IronXclbinKB=r"iron xclbin \(KB\): (?P<value>[\d\.]+)",
    IronCompileTime=r"iron compile \(s\): (?P<value>[\d\.]+)",
)
@pytest.mark.parametrize("model,proj,M,K,N", get_params())
def test_flm_gemm_vs_flm(model, proj, M, K, N, aie_context):
    A, B, expected, mass = make_inputs(M, K, N)

    # Build everything before timing anything. Comparing frozen binaries is
    # the only way an A/B here means what it says.
    competitors = [
        setup_iron(M, K, N, A, B, aie_context),
        setup_flm(M, K, N, A, B, aie_context),
        setup_gemm(M, K, N, A, B, aie_context),
    ]

    bad = [c for c in competitors if not c.verify(M, N, expected, mass)]
    assert not bad, "; ".join(
        f"{c.name} err/mass {c.err:.3g} exceeds {c.budget:g}" for c in bad
    )

    for c in competitors:
        for _ in range(WARMUP):
            c.run()
    # Round-robin, never all of one then all of another.
    for _ in range(ROUNDS):
        for c in competitors:
            c.time_round()

    by_name = {c.name: c for c in competitors}
    iron = by_name["iron"]

    print()
    for c in competitors:
        print(f"{c.name} latency (us): {c.us:.1f}")
        print(f"{c.name} err/mass: {c.err:.3e}")
    print(f"speedup vs flm: {by_name['flm'].us / iron.us:.3f}")
    print(f"speedup vs gemm: {by_name['gemm'].us / iron.us:.3f}")
    print(f"iron throughput: {2.0 * M * K * N / (iron.us * 1e-6) / 1e9:.6e} GFLOP/s")
    print(f"iron jitter (%): {iron.jitter_pct:.2f}")
    print(f"iron xclbin (KB): {iron.xclbin.stat().st_size / 1024:.1f}")
    if iron.compile_s is not None:
        print(f"iron compile (s): {iron.compile_s:.1f}")
    print()
