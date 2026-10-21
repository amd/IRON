#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-Embedding 0.6B on the NPU against Hugging Face's own model in
float32: the unit-length last hidden state of a query behind its
instruction and of a document, recorded in ``golden.npz`` beside the
checkpoint (``pytest --record-goldens``).
"""

import numpy as np
import pytest

from iron.applications.qwen3_embedding import Qwen3Embedding
from iron.lm import Checkpoint
from iron.lm.golden import Golden, HuggingFace
from iron.lm.testing import require, weights_dir

DIRECTORY = weights_dir("qwen3-embedding-0.6b")
TASK = "Given a web search query, retrieve relevant passages that answer the query"
MIN_COSINE = 0.99


class LastHidden(HuggingFace):
    """transformers' Qwen3 model without its head: the last token's final
    hidden state, unit length.
    """

    model_class = "AutoModel"

    def logits(self, tokens) -> np.ndarray:
        import torch

        with torch.no_grad():
            out = self.model(torch.tensor([list(tokens)]), use_cache=False)
        last = out.last_hidden_state[0, -1].numpy()
        return last / np.linalg.norm(last)


@pytest.fixture(scope="module")
def model():
    require(DIRECTORY / "model.safetensors", DIRECTORY / "tokenizer.json")
    return Qwen3Embedding.load(DIRECTORY)


@pytest.fixture(scope="module")
def reference():
    inputs = (
        (DIRECTORY / "config.json").read_text(),
        Checkpoint(DIRECTORY / "model.safetensors").fingerprint(),
    )
    return Golden(DIRECTORY / "golden.npz", lambda: LastHidden.load(DIRECTORY), inputs)


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize(
    "text,task",
    [
        ("What is the capital of China?", TASK),
        ("The capital of China is Beijing, its seat of government.", None),
    ],
    ids=["query", "document"],
)
def test_qwen3_embedding_0_6b_accuracy(model, reference, text, task, record_property):
    if task is not None:
        query = f"Instruct: {task}\nQuery:{text}"
    else:
        query = text
    tokens = [*model.tokenizer.encoding.encode(query), model.end_of_text]
    got = model.embed(text, task)
    want = reference.logits(tokens)
    cosine = float(got @ want)
    record_property("Cosine", cosine)
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=1e-3)
    assert cosine >= MIN_COSINE, cosine
