# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a model's device test checks: speed, accuracy against the
CPU reference, and determinism, each over a :class:`~.runner.Runner` and
the model it loaded.

A test module defines a module-scoped ``runner`` fixture; the ``model``
fixture (``iron/lm/conftest.py``) loads the model from it once
for the module, and each test calls one of these on the two.
"""

import os
from pathlib import Path

import numpy as np
import pytest

from iron.common.harness import record_metric

from .generation import SEED, Sampler, accuracy, determinism, generate, kl_stats


def weights_dir(name: str) -> Path:
    """Where the tests find a model's files: ``$IRON_EXAMPLE_WEIGHTS_DIR/<name>``."""
    return Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv")) / name


def requires(*files: Path):
    """Skip unless every one of ``files`` exists, except in CI, where a
    missing file is a failure.
    """
    missing = [str(f) for f in files if not f.exists()]
    return pytest.mark.skipif(
        not os.environ.get("CI") and bool(missing),
        reason=f"not found outside CI: {missing}",
    )


def prompt(runner, chars: int, num_tokens: int, skip: int = 0) -> list[int]:
    tokens = runner.prompt(chars, skip=skip)
    assert len(tokens) + num_tokens <= runner.config.max_seq_len
    return tokens


def check_generation(runner, model, prompt_len: int, num_tokens: int):
    """Sample ``num_tokens`` after a prompt of ``prompt_len`` characters;
    record the time to the first token and the tokens per second after it.
    """
    tokens = prompt(runner, prompt_len, num_tokens)
    sample = Sampler(0.7, 50, np.random.default_rng(SEED))
    drawn, first, later = generate(model, tokens, num_tokens, sample)
    print(runner.tokenizer.decode(drawn))
    record_metric("TTFT", first)
    if num_tokens > 1:
        record_metric("TPS", 1 / later)


def check_accuracy(runner, model, bounds: dict[str, float], num_tokens: int = 40):
    """KL(reference || model) of the next-token distribution, teacher-forced
    over ``num_tokens`` steps from a 1024-character prompt, within
    ``bounds`` (``{"Mean": .., "P90": .., "Max": ..}``). The mean and p90
    bound a drift across many steps, the max a single broken step.
    """
    tokens = prompt(runner, 1024, num_tokens)
    # Built here alone: a float32 oracle is twice the weights.
    results = accuracy(model, runner.cpu(), tokens, num_tokens)
    stats = kl_stats(results)
    for stat, value in stats.items():
        record_metric(f"{stat}KL", float(value))
    record_metric("Top1Mismatches", sum(not t for _, t in results))
    for stat, bound in bounds.items():
        assert stats[stat] <= bound, f"{stat.lower()} KL {stats[stat]} > {bound}"


def check_determinism(runner, model, num_tokens: int = 4, rounds: int = 5):
    """Repeated runs produce bit-identical logits.

    Two prompts, alternated: a host write that never reaches the device then
    reads the other prompt's data, so a missing flush fails every run rather
    than some. (A prefill KV hand-off never flushed made 12% of runs
    diverge; alternated, 38/38 in each of three trials.)
    """
    prompts = [
        prompt(runner, 1024, num_tokens),
        prompt(runner, 1024, num_tokens, skip=1024),
    ]
    differing = determinism(model, prompts, num_tokens, rounds)
    record_metric("DifferingRuns", differing)
    total = len(prompts) * (rounds - 1)
    assert differing == 0, f"{differing}/{total} runs' logits differ bitwise"
