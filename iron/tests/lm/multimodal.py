# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.Multimodal`` over a causal model on the device: a small Llama
whose prompt holds a run of soft tokens crossing a chunk's end, run through
its own host loop (``CausalLM.use``) on the multimodal graph's versions,
against the oracle with the soft tokens at their placeholders.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.lm import Sampler
from iron.tests.common.llama_reference import _assert_close
from iron.tests.common.multimodal import IMAGE, oracle_logits
from iron.tests.common.multimodal import causal  # noqa: F401 (a fixture)

# The relative top-2 gap each step's argmax is checked at: past
# _assert_close's 5% of the logits' scale, so the device's error cannot
# swap them.
GAP = 0.05


def gapped(logits: np.ndarray) -> np.ndarray:
    top = np.sort(logits)[-2:]
    assert (top[1] - top[0]) / np.abs(logits).max() > GAP, "a top-2 tie"
    return logits


@pytest.fixture(scope="module")
def loaded(causal):
    model, oracle, tokens, soft = causal
    yield model.load(), oracle, tokens, soft


@pytest.mark.supported_devices("npu2")
def test_a_causal_model_places_soft_tokens_across_its_chunks(loaded):
    model, oracle, tokens, first = loaded
    soft = (np.random.default_rng(9).standard_normal(first.shape) / 8).astype(bfloat16)
    want = gapped(oracle_logits(oracle, tokens, soft))
    _assert_close([model.logits(tokens, {IMAGE: (soft,)})], [want])
    # One more token with the same image: a decode step on the caches.
    more = np.append(tokens, want.argmax())
    want = gapped(oracle_logits(oracle, more, soft))
    _assert_close([model.logits(more, {IMAGE: (soft,)})], [want])
    # Another image: the towers rerun, and the chunks from its first
    # placeholder on.
    _assert_close(
        [model.logits(tokens, {IMAGE: (first,)})],
        [gapped(oracle_logits(oracle, tokens, first))],
    )


@pytest.mark.supported_devices("npu2")
def test_a_causal_model_draws_after_its_soft_tokens(loaded):
    model, oracle, tokens, first = loaded
    soft = (np.random.default_rng(9).standard_normal(first.shape) / 8).astype(bfloat16)
    expected, history = [], tokens
    for _ in range(3):
        token = int(gapped(oracle_logits(oracle, history, soft)).argmax())
        expected.append(token)
        history = np.append(history, token)
    sample = Sampler(0.0, 40, np.random.default_rng(0))
    drawn, _, _ = model.generate(tokens, 3, sample, {IMAGE: (soft,)})
    assert drawn == expected
