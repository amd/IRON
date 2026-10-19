#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-Embedding's graph against Hugging Face's Qwen3 model in float32
over Qwen3's toy, its last hidden state recorded in ``goldens/``,
device-free: a query behind its instruction, closed by end of text.
"""

import numpy as np
import pytest

from iron.applications.qwen3_embedding.model import Qwen3Embedding
from iron.lm.golden import HuggingFace
from iron.lm.model import _HostOutput
from iron.tests.support.llama_model import checkpoint
from tests.applications.qwen3.reference import test as qwen3
from tests.applications.qwen3_reranker.reference.test import Words

#: The end of text, within the toy's vocab.
EOS = 5


class LastHidden(HuggingFace):
    """transformers' Qwen3 model without its head: the last token's final
    hidden state.
    """

    model_class = "AutoModel"

    def logits(self, tokens) -> np.ndarray:
        import torch

        with torch.no_grad():
            out = self.model(torch.tensor([list(tokens)]), use_cache=False)
        return out.last_hidden_state[0, -1].numpy()


class Host(Qwen3Embedding):
    """The embedder, its call the graph's reference."""

    profile = None
    end_of_text = EOS

    def __call__(self, *tensors, **values):
        return _HostOutput(self.reference(*tensors, **values))


@pytest.mark.parametrize("task", [None, "Given a web search query"])
def test_an_embedding_is_the_last_hidden_state_unit_length(npu2, golden, task):
    names = {k.removeprefix("model."): v for k, v in qwen3.TestQwen3.names().items()}
    weights = checkpoint(qwen3.TOY, names).tree("random")
    reference = golden(
        "toy", lambda: LastHidden.build("qwen3", qwen3.TOY, weights), qwen3.TOY, weights
    )
    model = Host(qwen3.TOY, weights)
    model.tokenizer = type("Tokenizer", (), {"encoding": Words()})()
    text = "what lights the north sky at night"
    got = model.embed(text, task)
    query = text if task is None else f"Instruct: {task}\nQuery:{text}"
    want = reference.logits([*Words().encode(query), EOS])
    want = want / np.linalg.norm(want)
    assert np.isclose(np.linalg.norm(got), 1)
    assert got @ want > 0.999, got @ want
