# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.Multimodal`` over a causal model on the device.

A small Llama whose prompt holds a run of soft tokens crossing a chunk's
end, run through its own host loop (``CausalLM.use``) on the multimodal
graph's versions, against Hugging Face's Llama with the soft tokens at
their placeholders (``goldens/multimodal.npz``).
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.lm import Sampler
from iron.lm.testing import LOGITS, assert_close
from iron.tests.support.multimodal import IMAGE, small_causal


def gapped(logits: np.ndarray) -> np.ndarray:
    """Return ``logits``, checked to hold a top-2 gap past ``LOGITS``.

    So that the argmax a greedy draw takes is unambiguous.
    """
    top = np.sort(logits)[-2:]
    assert (top[1] - top[0]) / np.abs(logits).max() > LOGITS, "a top-2 tie"
    return logits


@pytest.fixture(scope="module")
def loaded(golden):
    model, reference, tokens, soft = small_causal(golden)
    yield model.load_versions(), reference, tokens, soft


@pytest.mark.supported_devices("npu2")
def test_a_causal_model_places_soft_tokens_across_its_chunks(loaded):
    model, reference, tokens, first = loaded
    soft = (np.random.default_rng(9).standard_normal(first.shape) / 8).astype(bfloat16)
    want = gapped(reference(tokens, soft))
    assert_close(model.logits(tokens, {IMAGE: (soft,)}), want)
    # One more token with the same image: a decode step on the caches.
    more = np.append(tokens, want.argmax())
    want = gapped(reference(more, soft))
    assert_close(model.logits(more, {IMAGE: (soft,)}), want)
    # Another image: the towers rerun, and the chunks from its first
    # placeholder on.
    assert_close(
        model.logits(tokens, {IMAGE: (first,)}), gapped(reference(tokens, first))
    )


@pytest.mark.supported_devices("npu2")
def test_a_causal_model_draws_after_its_soft_tokens(loaded):
    model, reference, tokens, first = loaded
    soft = (np.random.default_rng(9).standard_normal(first.shape) / 8).astype(bfloat16)
    expected, history = [], tokens
    for _ in range(3):
        token = int(gapped(reference(history, soft)).argmax())
        expected.append(token)
        history = np.append(history, token)
    sample = Sampler(0.0, 40, seed=0)
    drawn = model.generate(tokens, 3, sample, raw={IMAGE: (soft,)})
    assert drawn == expected
