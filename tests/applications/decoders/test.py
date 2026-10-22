# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Each decoder below on the NPU, from its real checkpoint: speed, accuracy
against the float32 reference and determinism. Each model is compiled and
loaded once, and every test of it calls it in-process.

``--random-weights SEED`` runs them on weights drawn in each checkpoint's
shapes and random prompts, on a host without the tokenizer, and
``--max-seq-len`` at another context.
"""

import aie.utils as aie_utils
import pytest

from iron.applications.gemma3 import Gemma3
from iron.applications.gemma4 import Gemma4
from iron.applications.qwen3_5 import Qwen35
from iron.applications.qwen3_moe import Qwen3Moe
from iron.applications.smollm3 import SmolLM3
from iron.lm.testing import (
    check_accuracy,
    check_determinism,
    check_generation,
    load_from_flags,
    weights_dir,
)

INDEX = "model.safetensors.index.json"

# Each decoder's class, checkpoint file, and the lengths of the long and the
# short prompt it generates from.
DECODERS = [
    pytest.param((Gemma3, "gemma-3-1b-it/model.safetensors", (256, 13)), id="gemma3"),
    pytest.param((Gemma4, "gemma-4-e2b-it/model.safetensors", (256, 13)), id="gemma4"),
    pytest.param((SmolLM3, f"smollm3-3b/{INDEX}", (1024, 13)), id="smollm3"),
    pytest.param((Qwen35, f"qwen3.5-0.8b/{INDEX}", (1024, 13)), id="qwen3_5"),
    # 30B, its experts paged from the checkpoint: nightly only, a toy one per PR
    # (tests/applications/qwen3_moe).
    pytest.param(
        (Qwen3Moe, f"qwen3-30b-a3b/{INDEX}", (1024, 13)),
        id="qwen3_moe",
        marks=pytest.mark.extensive,
    ),
]

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module", params=DECODERS)
def decoder(request):
    """A decoder, compiled and loaded once, and its prompts' lengths. Its
    runtime is released before the next decoder loads.
    """
    cls, weights, prompts = request.param
    yield load_from_flags(request, cls, weights_dir(weights), staged=False)(), prompts
    aie_utils.cleanup_npu_runtime()


# Qwen3's bounds: none of these decoders has been measured on the NPU.
MAX_KL = {"Mean": 0.03, "P90": 0.08, "Max": 0.2}
# bf16 transformers itself reaches p90 0.065 on Qwen3-MoE's steps: near-tie experts.
MOE_KL = {**MAX_KL, "P90": 0.1}


@pytest.mark.bench
@pytest.mark.parametrize(
    "prompt,num_tokens", [(0, 40), (1, 1)], ids=["long-40", "short-1"]
)
def test_generation(decoder, prompt, num_tokens, record_property):
    model, prompts = decoder
    check_generation(model, prompts[prompt], num_tokens, record=record_property)


@pytest.mark.bench
def test_accuracy(decoder, record_property):
    bounds = MOE_KL if isinstance(decoder[0], Qwen3Moe) else MAX_KL
    check_accuracy(decoder[0], bounds, record=record_property)


def test_determinism(decoder, record_property):
    if isinstance(decoder[0], Qwen3Moe):
        pytest.skip("15 min at 30B; test_host_steps holds a host step's calls exact")
    check_determinism(decoder[0], record=record_property)
