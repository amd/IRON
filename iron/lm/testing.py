# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a model's device test checks: speed, accuracy against the
CPU reference, and determinism, each over a ``Runner`` and
the model it loaded.

A test module defines module-scoped ``runner`` and ``model`` fixtures, the
model loaded from the runner once for the module, and each test calls one
of these on the two, with its ``record_property``, through which the
figures reach the CSV.
"""

import os
import time
from contextlib import contextmanager
from pathlib import Path

import numpy as np
import pytest

from .generation import (
    SEED,
    Sampler,
    accuracy,
    determinism,
    differing_steps,
    divergence,
    generate,
    greedy,
    greedy_logits,
    kl_stats,
)


def weights_dir(name: str) -> Path:
    """Where the tests find a model's files: ``$IRON_EXAMPLE_WEIGHTS_DIR/<name>``."""
    return Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv")) / name


def require(*files: Path) -> None:
    """Skip the test unless every one of ``files`` exists, except in CI,
    where a missing file is a failure.
    """
    missing = [str(f) for f in files if not f.exists()]
    if missing and not os.environ.get("CI"):
        pytest.skip(f"not found outside CI: {missing}")


def prompt(runner, chars: int, num_tokens: int, skip: int = 0) -> list[int]:
    tokens = runner.prompt(chars, skip=skip)
    assert len(tokens) + num_tokens <= runner.config.max_seq_len
    return tokens


def check_generation(runner, model, prompt_len: int, num_tokens: int, *, record):
    """Sample ``num_tokens`` after a prompt of ``prompt_len`` characters;
    record the time to the first token and the tokens per second after it.
    """
    tokens = prompt(runner, prompt_len, num_tokens)
    sample = Sampler(0.7, 50, np.random.default_rng(SEED))
    drawn, first, later = generate(model, tokens, num_tokens, sample)
    print(runner.decode(drawn))
    record("TTFT", first)
    if num_tokens > 1:
        record("TPS", 1 / later)


def check_device_loop(runner, model, prompt_len: int, num_tokens: int, *, record):
    """Sample ``num_tokens`` after a prompt of ``prompt_len`` characters with
    the host out of the loop (``CausalLM.generate``); record its time to the
    first token and tokens per second, then sample again on the host from
    the same seed: the text is the same, token for token.
    """
    tokens = prompt(runner, prompt_len, num_tokens)

    def sampler():
        return Sampler(0.7, 50, np.random.default_rng(SEED))

    drawn, first, later = model.generate(tokens, num_tokens, sampler())
    print(runner.decode(drawn))
    record("TTFT", first)
    if num_tokens > 1:
        record("TPS", 1 / later)
    host, _, _ = generate(model, tokens, num_tokens, sampler())
    differing = [i for i, (a, b) in enumerate(zip(drawn, host)) if a != b]
    record("DifferingTokens", len(differing))
    assert not differing, f"tokens {differing} of {num_tokens} differ from the host's"


def check_accuracy(
    runner,
    model,
    bounds: dict[str, float],
    num_tokens: int = 40,
    chars: int = 1024,
    *,
    record,
):
    """KL(reference || model) of the next-token distribution, teacher-forced
    over ``num_tokens`` steps from a ``chars``-character prompt, within
    ``bounds`` (``{"Mean": .., "P90": .., "Max": ..}``). The mean and p90
    bound a drift across many steps, the max a single broken step.
    """
    tokens = prompt(runner, chars, num_tokens)
    # Built here alone: a float32 oracle is twice the weights.
    results = accuracy(model, runner.cpu(), tokens, num_tokens)
    stats = kl_stats(results)
    for stat, value in stats.items():
        record(f"{stat}KL", float(value))
    record("Top1Mismatches", sum(not t for _, t in results))
    for stat, bound in bounds.items():
        assert stats[stat] <= bound, f"{stat.lower()} KL {stats[stat]} > {bound}"


def check_determinism(
    runner,
    model,
    num_tokens: int = 4,
    rounds: int = 5,
    chars: int = 1024,
    *,
    record,
):
    """Repeated runs produce bit-identical logits.

    Two prompts of ``chars`` characters, alternated: a host write that never
    reaches the device then reads the other prompt's data, so a missing
    flush fails every run rather than some. (A prefill KV hand-off never
    flushed made 12% of runs diverge; alternated, 38/38 in each of three
    trials.)
    """
    prompts = [
        prompt(runner, chars, num_tokens),
        prompt(runner, chars, num_tokens, skip=chars),
    ]
    differing = determinism(model, prompts, num_tokens, rounds)
    record("DifferingRuns", differing)
    total = len(prompts) * (rounds - 1)
    assert differing == 0, f"{differing}/{total} runs' logits differ bitwise"


def check_chat_turn(
    runner, model, chars: int, turn: int, num_tokens: int = 2, *, record
):
    """A prompt extended by a turn, as a chat's next message extends it:
    the model reruns the chunks from the one holding the turn's first token
    over the caches the prompt left, and its logits, and those of the greedy
    steps after, are bit for bit those of the whole run from scratch.

    The prompt is ``chars`` characters, the turn its last ``turn`` tokens.
    Before the run from scratch a prompt of other text overwrites the
    caches, so it reuses nothing of the turn's. Records both runs' seconds.
    """
    whole = prompt(runner, chars, num_tokens)
    C = runner.config.prefill_chunk
    assert (len(whole) - turn) // C, "the turn reuses no chunk"
    other = prompt(runner, chars, 0, skip=1)
    runs = []
    for name, before in (("Turn", whole[:-turn]), ("Scratch", other)):
        model.logits(before)
        start = time.perf_counter()
        runs.append(greedy_logits(model, whole, num_tokens))
        record(f"{name}Seconds", time.perf_counter() - start)
    steps = differing_steps(*runs)
    assert not steps, f"the turn's logits differ from scratch's at steps {steps}"


def check_deep_decode(
    runner, model, position: int, bound: float, chars: int = 1024, *, record
):
    """A decode step at ``position``, deep in the caches, against the
    graph's own reference (``Graph.reference``: each operator's
    ``reference()`` on host tensors, the caches as state), for a context
    the float32 oracle would take too long over, within ``bound`` of its
    KL. Whether both rank the same token first is recorded, not required:
    at a near-tie a step can differ in it at a KL of 0.014.

    The caches hold a real prompt, ``chars`` characters of it, repeated up
    to ``position`` (``_fill_caches``).
    """
    tokens = prompt(runner, chars, 1)
    token = greedy(model.logits(tokens))
    # A decode step takes the token; the device gathers its embedding row.
    values = dict(token=token, position=position, chunk=0, rows=1)
    with _fill_caches(model, len(tokens), position):
        got, _ = model(**values)
        got = got.numpy()
        expected, _ = model.reference(**values)
    kl, top1 = divergence(expected, got)
    record("DeepKL", kl)
    record("DeepTop1", top1)
    assert kl <= bound, f"at {position}: KL {kl} > {bound}"


def check_deep_prompt(
    runner, model, rows: int, bound: float, chars: int = 1024, *, record
):
    """The last prompt chunk the caches hold, ``rows`` rows of it, against
    the graph's own reference within ``bound`` of its KL, every position
    before it filled as ``check_deep_decode`` fills them: the chunk attends
    over the whole context. Records its seconds, the longest a prompt
    chunk takes, which the driver's watchdog bounds where a chunk is one
    dispatch.
    """
    tokens = prompt(runner, chars, 1)
    model.logits(tokens)
    C, L = runner.config.prefill_chunk, runner.config.max_seq_len
    chunk = np.resize(tokens, rows)
    x = np.zeros((C, runner.config.emb_dim), dtype=model.embedding.array.dtype)
    x[:rows] = model.embedding.array[chunk]
    values = dict(
        token=int(chunk[-1]), position=L - C + rows - 1, chunk=L // C - 1, rows=rows
    )
    with _fill_caches(model, len(tokens), L - C):
        start = time.perf_counter()
        got, _ = model(x, **values)
        record("DeepPromptSeconds", time.perf_counter() - start)
        got = got.numpy()
        expected, _ = model.reference(x, **values)
    kl, top1 = divergence(expected, got)
    record("DeepPromptKL", kl)
    record("DeepPromptTop1", top1)
    assert kl <= bound, f"the chunk at {L - C}: KL {kl} > {bound}"


@contextmanager
def _fill_caches(model, n: int, position: int):
    """The caches' first ``n`` rows, a prompt's, repeated up to ``position``
    on the device and as the graph reference's state, for the body of the
    ``with``; the reference's state is dropped after it. The prompt's own
    rows are left as it wrote them, so the model's record of what its
    caches hold stays true, and the step attends over a real prompt's
    scale of keys and values, the same ones on the device and in the
    reference.
    """
    version = next(iter(model.versions.values()))
    caches = [*model.keys, *model.values]
    for cache in caches:
        rows = np.array(version.read(cache))
        rows[n:position] = np.resize(rows[:n], (position - n, *rows.shape[1:]))
        version.write(cache, rows)
        cache.host = rows  # the reference's, written in place as the device's
    try:
        yield
    finally:
        for cache in caches:
            cache.host = None
