#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-Embedding 0.6B on the NPU against Hugging Face's own model in
float32, from one compile: the unit-length last hidden state of a query
behind its instruction, of a document, and of documents of four prompt
chunks and of the native 32768-token context's last, recorded in
``golden.npz`` beside the checkpoint (``pytest --record-goldens``).
"""

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.applications.qwen3_embedding import Qwen3Embedding
from iron.lm.model import prompt_text
from iron.lm.testing import require, weights_dir

DIRECTORY = weights_dir("qwen3-embedding-0.6b")
TASK = "Given a web search query, retrieve relevant passages that answer the query"

# Each text, the task it is a query of (None: a document), and the least
# cosine its embedding reaches against transformers'.
TEXTS = {
    "query": ("What is the capital of China?", TASK, 0.99),
    "document": (
        "The capital of China is Beijing, its seat of government.",
        None,
        0.99,
    ),
    # 7625 tokens and the end of text: four prompt chunks.
    "four_chunks": (prompt_text(28000), None, 0.99),
    # 32682 tokens and the end of text: the native context's last chunk.
    "native_context": (prompt_text(120000), None, 0.99),
}


@pytest.fixture(scope="module")
def model():
    require(DIRECTORY / "model.safetensors", DIRECTORY / "tokenizer.json")
    yield Qwen3Embedding.load(DIRECTORY)
    aie_utils.cleanup_npu_runtime()


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize(
    "name",
    [
        "query",
        "document",
        pytest.param("four_chunks", marks=pytest.mark.extensive),
        pytest.param("native_context", marks=pytest.mark.extensive),
    ],
)
def test_qwen3_embedding_0_6b_accuracy(model, name, record_property):
    text, task, min_cosine = TEXTS[name]
    query = text if task is None else f"Instruct: {task}\nQuery:{text}"
    tokens = [*model.tokenizer.encoding.encode(query), model.end_of_text]
    assert len(tokens) <= model.config.max_seq_len
    got = model.embed(text, task)
    want = model.cpu_reference().logits(tokens)
    cosine = float(got @ want)
    record_property("Tokens", len(tokens))
    record_property("Cosine", cosine)
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=1e-3)
    assert cosine >= min_cosine, cosine
