# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-Reranker 0.6B on the NPU, from the real checkpoint: ``score()``
over its model card's queries and documents, and over a document of two
prompt chunks, each against the score transformers' float32 logits give
(``golden.npz`` beside the checkpoint), from one compile.
"""

import math

import aie.utils as aie_utils
import pytest

from iron.applications.qwen3_reranker import Qwen3Reranker
from iron.applications.qwen3_reranker.model import INSTRUCTION, PROMPT
from iron.lm.generation import divergence
from iron.lm.model import prompt_text
from iron.lm.testing import load_from_flags, weights_dir

WEIGHTS = weights_dir("qwen3-reranker-0.6b") / "model.safetensors"

pytestmark = pytest.mark.supported_devices("npu2")

# The model card's queries and documents.
CAPITAL = "What is the capital of China?"
GRAVITY = "Explain gravity"
BEIJING = "The capital of China is Beijing."
FORCE = (
    "Gravity is a force that attracts two bodies towards each other. It gives "
    "weight to physical objects and is responsible for the movement of planets "
    "around the sun."
)
# 12000 characters of prompt.txt: the prompt is two chunks.
LONG = prompt_text(12000)

PAIRS = {
    "capital_beijing": (CAPITAL, BEIJING),
    "capital_force": (CAPITAL, FORCE),
    "gravity_beijing": (GRAVITY, BEIJING),
    "gravity_force": (GRAVITY, FORCE),
    "gravity_long": (GRAVITY, LONG),
}

# The score's error, and its input's: |logit("yes") - logit("no")| apart
# from transformers'. The next-token KL beside them is held to Qwen3's.
MAX_SCORE_ERROR = 0.02
MAX_MARGIN_ERROR = 0.5
MAX_KL = 0.2


@pytest.fixture(scope="module")
def model(request):
    """The model, compiled and loaded once for every pair."""
    yield load_from_flags(request, Qwen3Reranker, WEIGHTS)()
    aie_utils.cleanup_npu_runtime()


@pytest.fixture(scope="module")
def reference(model):
    return model.cpu_reference()


def margin(logits, encode) -> float:
    """How far "yes" leads "no" as the answer's first token."""
    [yes], [no] = encode("yes"), encode("no")
    return float(logits[yes] - logits[no])


@pytest.mark.parametrize("pair", list(PAIRS))
def test_qwen3_reranker_0_6b_scores_as_transformers(
    model, reference, pair, record_property
):
    query, document = PAIRS[pair]
    encode = model.tokenizer.encoding.encode
    tokens = encode(
        PROMPT.format(instruction=INSTRUCTION, query=query, document=document)
    )
    want = reference.logits(tokens)
    expected = 1 / (1 + math.exp(-margin(want, encode)))
    got = model.score(query, document)
    logits = model.logits(tokens)
    error = abs(margin(logits, encode) - margin(want, encode))
    kl, _ = divergence(want, logits)
    record_property("Score", got)
    record_property("ExpectedScore", expected)
    record_property("MarginError", error)
    record_property("KL", kl)
    assert abs(got - expected) <= MAX_SCORE_ERROR, f"score {got} against {expected}"
    assert error <= MAX_MARGIN_ERROR, f"yes over no {error} from transformers'"
    assert kl <= MAX_KL, f"KL {kl} > {MAX_KL}"
