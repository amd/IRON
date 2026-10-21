# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-Reranker's score against Hugging Face's Qwen3 in float32 over
Qwen3's toy, its logits recorded in ``goldens/``, device-free: the prompt
it asks, and "yes" over "no" after it.
"""

import math
import zlib

import numpy as np

from iron.applications.qwen3_reranker.model import PROMPT, Qwen3Reranker
from iron.lm import OnHost
from iron.lm.golden import HuggingFace
from tests.applications.qwen3.reference import test as qwen3


class Words:
    """A word a token, by its checksum: a tokenizer within the toy's vocab."""

    def encode(self, text: str) -> list[int]:
        return [zlib.crc32(w.encode()) % qwen3.TOY.vocab_size for w in text.split()]


def test_the_score_is_yes_over_no_after_the_prompt(npu2, golden):
    weights = qwen3.TestQwen3.weights()
    reference = golden(
        "toy",
        lambda: HuggingFace.build("qwen3", qwen3.TOY, weights),
        qwen3.TOY,
        weights,
    )
    model = type("Host", (OnHost, Qwen3Reranker), {"profile": None})(qwen3.TOY, weights)
    model.tokenizer = type("Tokenizer", (), {"encoding": Words()})()
    query, document = "what lights the north sky", "charged particles from the sun"
    got = model.score(query, document)
    text = PROMPT.format(
        instruction="Given a web search query, retrieve relevant passages "
        "that answer the query",
        query=query,
        document=document,
    )
    logits = reference.logits(Words().encode(text))
    [yes], [no] = Words().encode("yes"), Words().encode("no")
    want = 1 / (1 + math.exp(logits[no] - logits[yes]))
    assert np.isclose(got, want, atol=1e-2), (got, want)
