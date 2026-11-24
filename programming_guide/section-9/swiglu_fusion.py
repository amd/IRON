# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-9 example: a graph's steps fused on-chip by naming them in a profile.

``SwiGLU`` is Llama 3.2 1B's gated MLP for one token, up to its down
projection: two GEMVs, SiLU and a multiply. Unfused, each is its own step
and every intermediate goes through host memory. ``fused_profile`` names
the four as one ``stream`` fusion, so the projections' outputs feed SiLU
and the multiply on-chip and the version moves only ``x`` in and the
product out.
"""

import argparse

import numpy as np
from aie.utils.benchmark import run_interleaved
from aie.utils.verify import compare
from ml_dtypes import bfloat16

import iron
from iron.common.graph.fusion import candidates, fusions
from iron.operators import GEMV, ElementwiseMul, SiLU

HIDDEN, INTERMEDIATE = 2048, 8192

# Each edge is (producer, output, consumer, input), indices into the steps
# in the order body() records them: gate, up, SiLU, the multiply.
MLP_EDGES = [(0, "C", 2, "x"), (1, "C", 3, "b"), (2, "y", 3, "a")]


class SwiGLU(iron.Graph):
    """``silu(w_gate @ x) * (w_up @ x)``, against weights this graph holds."""

    def __init__(self, w_gate, w_up):
        self.w_gate, self.w_up = iron.param(w_gate), iron.param(w_up)

    def body(self, x):
        gate = GEMV.step(self.w_gate, x)
        up = GEMV.step(self.w_up, x)
        return SiLU.step(gate) * up


def tuned_profile() -> iron.Profile:
    """Llama's own npu2 tunables for these four steps (Section 7)."""
    profile = iron.Profile()
    profile.add(
        GEMV, M=INTERMEDIATE, K=HIDDEN, tile_size_input=4, tile_size_output=1024
    )
    profile.add(SiLU, size=INTERMEDIATE, tile_size=1024)
    profile.add(ElementwiseMul, size=INTERMEDIATE, tile_size=1024)
    return profile


def fused_profile() -> iron.Profile:
    """``tuned_profile()`` plus one fusion entry naming the whole MLP."""
    profile = tuned_profile()
    gemv = (GEMV, {"M": INTERMEDIATE, "K": HIDDEN})
    profile.add_fusion(
        iron.FusionKind.STREAM,
        [
            gemv,
            gemv,
            (SiLU, {"size": INTERMEDIATE}),
            (ElementwiseMul, {"size": INTERMEDIATE}),
        ],
        MLP_EDGES,
    )
    return profile


def main(argv=None):
    parser = argparse.ArgumentParser(description="Section 9: fusing steps on-chip")
    parser.add_argument("--rounds", type=int, default=8)
    parser.add_argument("--calls", type=int, default=50)
    args = parser.parse_args(argv)

    rng = np.random.default_rng(0)
    scale = 1 / np.sqrt(HIDDEN)
    w_gate = (rng.standard_normal((INTERMEDIATE, HIDDEN)) * scale).astype(bfloat16)
    w_up = (rng.standard_normal((INTERMEDIATE, HIDDEN)) * scale).astype(bfloat16)
    x = rng.standard_normal(HIDDEN).astype(bfloat16)

    apart = SwiGLU(w_gate, w_up)
    apart.profile = tuned_profile()
    fused = SwiGLU(w_gate, w_up)
    fused.profile = fused_profile()

    # What the recording admits on-chip, before any profile picks one.
    recording = fused.record(x=(HIDDEN,))
    for fusion in candidates(recording):
        names = ", ".join(type(recording.steps[s].op).__name__ for s in fusion.steps)
        print(f"candidate {fusion.kind.value}: steps {fusion.steps} ({names})")
    # The ones compile() builds fused: those the graph's profile names.
    (chosen,) = fusions(recording, fused.profile)
    print(f"the profile fuses steps {chosen.steps} as one {chosen.kind.value}")
    assert fusions(apart.record(x=(HIDDEN,)), apart.profile) == ()

    reference = fused.reference(x)
    versions = {
        "unfused": apart.compile(x=(HIDDEN,)),
        "fused": fused.compile(x=(HIDDEN,)),
    }
    results = {name: np.asarray(version(x)) for name, version in versions.items()}

    # Every step rounds once in float32; GEMV's sum is the one whose error
    # the chain's output is held to, as the operators' own fusion tests do.
    gemv = recording.steps[0].op.resolved()
    for name, result in results.items():
        verdict = compare(result, reference, gemv.tolerance())
        print(f"{name} vs. graph.reference(): {verdict.detail}")
        assert verdict, verdict.detail
    assert np.array_equal(
        results["fused"].view(np.uint16), results["unfused"].view(np.uint16)
    ), "the fused version differs from the steps run apart"
    print("fused and unfused outputs are bit-identical")

    # Each version's image alone, called again on the x already staged:
    # NPU time only, the two interleaved round by round.
    timed = run_interleaved(
        [version.callable for version in versions.values()],
        rounds=args.rounds,
        calls=args.calls,
        completion_cores=True,
    )
    for name, stats in zip(versions, timed):
        print(f"{name}: {stats.min_us:.1f} us min, {stats.median_us:.1f} us median")
    print("PASS!")


if __name__ == "__main__":
    main()
