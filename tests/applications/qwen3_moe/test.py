# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-MoE on the NPU at a toy shape, on drawn weights: a prompt chunk and
decode steps, each call's chosen experts staged by the host between the
router and the experts (``iron.on_host``), held to the graph's own
reference on the host. Needs no checkpoint; the decoders suite runs the
real 30B nightly.
"""

import dataclasses

import numpy as np
import pytest

from iron.applications.qwen3_moe.model import Qwen3Moe
from iron.lm.generation import divergence
from iron.tests.support.llama_model import checkpoint
from iron.tests.support.qwen3_moe import TOY, names

SEED = 7
# A chunk's router logits are flm.ProjectionGEMM's (N a multiple of 64), and
# a bounded row of its ids a 16-byte unit: 64 experts, 4 a token, not TOY's 8 and 2.
MOE = dataclasses.replace(TOY, num_experts=64, num_experts_per_tok=4)

pytestmark = pytest.mark.supported_devices("npu2")


def test_paged_experts_follow_the_graph_reference():
    """A 37-token prompt chunk, then three decode steps: each call's next-token
    distribution within KL 0.1 of the graph's reference, as long_context's deep
    checks hold a decoder to it, its top token the same.
    """
    model = Qwen3Moe(MOE, checkpoint(MOE, names(MOE)).tree("random", SEED))
    model.random_weights = SEED
    model.load_versions()
    reference = model.cpu_reference()
    tokens = np.random.default_rng(SEED).integers(0, MOE.vocab_size, 40).tolist()
    for n in (37, 38, 39, 40):
        kl, top1 = divergence(reference.logits(tokens[:n]), model.logits(tokens[:n]))
        assert kl <= 0.1 and top1, f"{n} tokens: KL {kl}, top-1 {top1}"
