# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.validate`` end to end against real dispatch.

At SMALL's shape (``iron.tests.support.llama_model.small``, drawn weights, no checkpoint
directory needed): a candidate profile adding one on-chip fusion is live, compiles its
own image, and is bit-identical to stock and within its own accuracy of the graph's
reference.
"""

import pytest

from iron import Profile
from iron.common.graph.fusion import candidates
from iron.common.image.step import FusionKind
from iron.lm import validate
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.silu import SiLU
from iron.tests.support.llama_model import small

pytestmark = pytest.mark.supported_devices("npu2")


def _silu_mul_entry(recording):
    """Return the ``(SiLU, dims)`` -> ``(ElementwiseMul, dims)`` fusion entry ``recording`` admits, in ``Profile.add_fusion``'s own shape."""
    fusion = next(
        f
        for f in candidates(recording)
        if len(f.steps) == 2
        and type(recording.steps[f.steps[0]].op.resolved()).__name__ == "SiLU"
    )
    gate = recording.steps[fusion.steps[0]].op.resolved()
    mul = recording.steps[fusion.steps[1]].op.resolved()
    edge = fusion.edges[0]
    return (
        FusionKind.STREAM,
        [(SiLU, dict(size=gate.size)), (ElementwiseMul, dict(size=mul.size))],
        [(0, edge.output, 1, edge.input)],
    )


def test_validate_battery_on_small_llama():
    seed = 0
    stock = small(seed=seed)
    stock.random_weights = seed
    entry = _silu_mul_entry(stock.record(**stock.shapes()[0]))

    # A real candidate profile is stock's own tunables plus whatever changed
    # (iron.lm.tune writes one that way, never a bare diff): a profile holding
    # the fusion alone would also lose SMALL's own tuned tile sizes, and the
    # prompt chunk, which the fusion never touches, would build differently
    # from stock's for that reason alone.
    candidate_profile = Profile()
    for cls, dims, tunables in stock.profile:
        candidate_profile.add(cls, **dims, **tunables)
    candidate_profile.add_fusion(*entry)
    candidate = small(seed=seed)
    candidate.random_weights = seed
    candidate.profile = candidate_profile

    try:
        stock.load_versions(full_elf=True)
        candidate.load_versions(full_elf=True)

        stock_live = validate.verify_live("stock", stock)
        candidate_live = validate.verify_live("candidate", candidate)
        assert validate.changed_versions(stock_live, candidate_live) == ["decode"]
        assert candidate_live["decode"]["n_fusions"] == 2
        assert candidate_live["prompt"]["n_fusions"] == 0

        tokens = stock.prompt(200)
        mismatch = validate.bit_identity(stock, candidate, tokens, 4)
        assert not mismatch, f"logits differ at steps {mismatch}"

        stats, mismatches = validate.run_accuracy(candidate, stock.prompt(64), 4)
        assert stats["Max"] < 1.0, stats
        assert mismatches == 0
    finally:
        stock.release()
        candidate.release()
