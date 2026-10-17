#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM-256M-Instruct on the NPU, from the real checkpoint: a small
accuracy sweep (device vs. the float32 oracle, teacher-forced to the real
prompt's last position) over a few image/question pairs, one image each,
no splitting (module docstring, ``iron.applications.idefics3.model``). Not a full
generation loop or a 40-step accuracy treatment the way the text-only
models get -- a single-image VLM's real signal is whether the splice
agrees with the oracle at all, not how it drifts over many decode steps
(``generate()`` does not thread ``pixel_values`` through yet, the same gap
``Oracle.logits()`` has: both call ``embed(x)`` with one argument, and
``iron.lm.Multimodal`` is what generalizes this).

``--random-weights SEED`` runs it on drawn weights, a synthetic image and
random prompts, on a host without the checkpoint.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.idefics3.model import VLMRunner, build_prompt
from iron.lm.testing import require, weights_dir

WEIGHTS = weights_dir("smolvlm-256m-instruct") / "model.safetensors"
TOKENIZER = weights_dir("smolvlm-256m-instruct") / "tokenizer.json"
CONFIG = weights_dir("smolvlm-256m-instruct") / "config.json"

pytestmark = pytest.mark.supported_devices("npu2")

# Mean KL(oracle || device) measured 0.0061-0.0094 over the three
# questions below (distinct synthetic images each); comfortable headroom.
MAX_KL = 0.05

QUESTIONS = [
    "What is in this image?",
    "Describe this photo in detail, please.",
    "What colors do you see?",
]


@pytest.fixture(scope="module")
def runner(request):
    """``VLMRunner.from_options``, the same way the CLI builds one: the
    options pytest's own ``--random-weights``/``--max-seq-len`` flags
    (``conftest.py``'s, ``Runner.FLAGS``) were given, as option strings.
    """
    seed = request.config.getoption("--random-weights")
    max_seq_len = request.config.getoption("--max-seq-len")
    options = [str(WEIGHTS)]
    if seed is not None:
        require(WEIGHTS, CONFIG)
        options += ["--random-weights", str(seed)]
    else:
        require(WEIGHTS, TOKENIZER, CONFIG)
        options.append(str(TOKENIZER))
    if max_seq_len is not None:
        options += ["--max-seq-len", str(max_seq_len)]
    return VLMRunner.from_options(options)


@pytest.fixture(scope="module")
def model(runner, request):
    yield runner.npu(request.config.getoption("--cost-table"))


def _log_softmax(x):
    x = x - x.max()
    return x - np.log(np.exp(x).sum())


def _divergence(ref, got):
    la, lb = _log_softmax(ref.astype(np.float64)), _log_softmax(got.astype(np.float64))
    kl = float(np.sum(np.exp(la) * (la - lb)))
    return kl, int(got.argmax()) == int(ref.argmax())


@pytest.mark.parametrize("seed,question", list(enumerate(QUESTIONS)))
def test_smolvlm_accuracy(runner, model, seed, question, record_property):
    """One real image (a distinct synthetic one a seed), one question,
    one forward pass: the device's logits at the prompt's last position
    against the float32 oracle's, the same splice both take.
    """
    rng = np.random.default_rng(seed + 10)
    image_u8 = rng.integers(0, 256, (512, 512, 3), dtype=np.uint8)
    image = (image_u8.astype(np.float32) / 255.0 - 0.5) / 0.5
    tokens = np.array(build_prompt(runner.tokenizer, question), dtype=np.int64)

    oracle = runner.oracle()
    angles = oracle.angles[: tokens.size]
    pixel_values = image.reshape(512, 512 * 3)
    x = oracle.embed(oracle.embedding[tokens], pixel_values)
    for w in oracle.layers:
        x = oracle.layer(angles, w, x)
    expected = oracle.head(x[-1])

    rows = tokens.size
    ids = model.prompt_ids(tokens)
    image_bf16 = image.astype(bfloat16).reshape(512, 512 * 3)
    out, _ = model(
        ids, image_bf16, token=int(tokens[-1]), position=rows - 1, chunk=0, rows=rows
    )
    got = np.asarray(out.numpy()).reshape(-1).astype(np.float32)

    kl, top1 = _divergence(expected, got)
    record_property("KL", kl)
    record_property("Top1Match", top1)
    assert kl <= MAX_KL, f"KL {kl} > {MAX_KL}"
    assert top1, "device and oracle disagree on the top token"
