# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-Reranker on the NPU: Qwen3 asked, in the prompt its model card
gives, whether a document meets a query and an instruction; its score is
the probability of "yes" over "no" as the answer's first token.
"""

import math

from iron.applications.qwen3.model import Qwen3

PROMPT = (
    "<|im_start|>system\nJudge whether the Document meets the requirements "
    "based on the Query and the Instruct provided. Note that the answer can "
    'only be "yes" or "no".<|im_end|>\n<|im_start|>user\n'
    "<Instruct>: {instruction}\n<Query>: {query}\n<Document>: {document}"
    "<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n"
)
INSTRUCTION = (
    "Given a web search query, retrieve relevant passages that answer the query"
)


class Qwen3Reranker(Qwen3):
    """Qwen3 scoring a document against a query (``score``)."""

    def score(self, query: str, document: str, instruction=INSTRUCTION) -> float:
        """The probability that ``document`` meets ``query`` and
        ``instruction``.
        """
        encode = self.tokenizer.encoding.encode
        text = PROMPT.format(instruction=instruction, query=query, document=document)
        logits = self.logits(encode(text))
        [yes], [no] = encode("yes"), encode("no")
        return 1 / (1 + math.exp(logits[no] - logits[yes]))
