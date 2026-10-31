# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generation's EOS exits and token counts over a real device loop.

A small Llama on drawn weights, loaded from a repository directory whose
``generation_config.json`` names the eos.
"""

import json

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.applications.llama import Llama
from iron.tests.support.llama_model import PROFILE, SMALL, checkpoint

pytestmark = pytest.mark.supported_devices("npu2")

PROMPT = [int(t) for t in np.random.default_rng(3).integers(0, SMALL.vocab_size, 8)]
MAX_TOKENS = 12


def _load(directory, eos=None) -> Llama:
    directory.mkdir()
    (directory / "config.json").write_text(json.dumps(SMALL.to_json()))
    (directory / "model.safetensors").symlink_to(checkpoint(SMALL).path)
    if eos is not None:
        (directory / "generation_config.json").write_text(
            json.dumps({"eos_token_id": eos})
        )
    model = Llama.from_checkpoint(directory, random_weights=0)
    model.profile = PROFILE
    model.load_versions()
    assert model.device_loop
    return model


@pytest.fixture
def release():
    held = []
    yield held.append
    for model in held:
        model.release()
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


@pytest.fixture(scope="module")
def draws(tmp_path_factory):
    """Return the greedy draws after ``PROMPT``, with no eos to stop at."""
    model = _load(tmp_path_factory.mktemp("draws") / "repo")
    try:
        drawn = model.generate(PROMPT, MAX_TOKENS)
        assert model.stats.tokens == MAX_TOKENS
        assert len(drawn) == MAX_TOKENS
        return drawn
    finally:
        model.release()


def test_generate_counts_the_draws_past_eos(draws, tmp_path, release):
    """The device loop draws all ``MAX_TOKENS`` before generate reads them, so its count holds every one.

    Stream reads each as it is drawn and stops at eos.
    """
    k = next((i for i in range(1, MAX_TOKENS) if draws[i] not in draws[:i]), 0)
    assert 0 < k < MAX_TOKENS - 1, f"no later first-seen draw in {draws}"
    model = _load(tmp_path / "repo", eos=draws[k])
    release(model)
    assert model.generate(PROMPT, MAX_TOKENS) == draws[: k + 1]
    assert model.stats.tokens == MAX_TOKENS
    model.forget(0)
    assert list(model.stream(PROMPT, MAX_TOKENS)) == draws[: k + 1]
    assert model.stats.tokens == k + 1


def test_a_first_token_eos_runs_no_decode_step(draws, tmp_path, release):
    """The prompt chunk draws eos.

    No decode step runs, so the device's ``drawn`` rows past the prompt are
    still the zeros they started as.
    """
    assert any(draws[1:]), "a decode step would leave no trace"
    model = _load(tmp_path / "repo", eos=draws[0])
    release(model)
    assert model.generate(PROMPT, MAX_TOKENS) == draws[:1]
    assert model.stats.tokens == 1
    rows = model.decode_step.read(model.drawn)
    n = len(PROMPT)
    assert rows[n - 1] == draws[0]
    assert not rows[n : n - 1 + MAX_TOKENS].any()
