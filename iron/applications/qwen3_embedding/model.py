# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-Embedding on the NPU: Qwen3's decoder without its head, over
``CausalLM``'s prompt chunks and caches, so one compile serves every
length up to its native context. A text's embedding is its last token's
final hidden state, unit length; the tokenizer's end of text closes it,
and a query goes behind its task's instruction.
"""

import numpy as np

import iron
from iron.applications.qwen3.model import Qwen3
from iron.lm import subtree


class Qwen3Embedding(Qwen3):
    """Qwen3-Embedding on ``config``'s shape from a checkpoint's
    ``weights``, Qwen3's ``model`` modules at its root. A call returns the
    last row's final hidden state; nothing is drawn.
    """

    # The end-of-text token each input ends in.
    end_of_text = 151643

    def __init__(self, config, weights):
        super().__init__(config, subtree(weights, model=weights))

    @property
    def hugging_face(self):
        """transformers' Qwen3 model, imported only where a golden is recorded."""
        from .hugging_face import LastHidden

        return LastHidden

    def head(self, x):
        return self.model.norm(x)

    def draw(self, logits, call):
        return logits, iron.carry(token=call.token, position=call.position + 1)

    def embed(self, text: str, task: str | None = None) -> np.ndarray:
        """The unit-length embedding of ``text``, a query behind ``task``'s
        instruction where given, else a document, float32.
        """
        if task is not None:
            text = f"Instruct: {task}\nQuery:{text}"
        tokens = [*self.tokenizer.encoding.encode(text), self.end_of_text]
        y = self.logits(tokens).astype(np.float32)
        return y / np.linalg.norm(y)
