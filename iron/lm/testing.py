# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a model's device test checks: speed, accuracy against the
CPU reference, and determinism, each over a model ``Model.load`` loaded,
its figures through the test's ``record_property``; and where it finds the
model's files.
"""

import dataclasses
import functools
import hashlib
import os
import time
import urllib.request
from contextlib import contextmanager
from pathlib import Path

import numpy as np
from aie.utils.compile import NPU_CACHE_HOME

from iron.common.graph.compiled import _leaves

from .blocks import KVCache
from .generation import (
    SEED,
    Sampler,
    accuracy,
    determinism,
    differing_steps,
    divergence,
    generate_on_host,
    greedy,
    greedy_logits,
    kl_stats,
)


def weights_dir(name: str) -> Path:
    """Where the tests find a model's files: ``$IRON_EXAMPLE_WEIGHTS_DIR/<name>``."""
    return Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv")) / name


def cache_dir() -> Path:
    """Where a ``Download`` is cached: IRON's own writable cache
    (``NPU_CACHE_HOME``), not the weights directory, which CI mounts
    read-only.
    """
    return Path(NPU_CACHE_HOME) / "data"


@dataclasses.dataclass(frozen=True)
class Download:
    """A file a test reads that the repository does not hold, fetched from
    ``url`` and pinned by its ``sha256``.
    """

    url: str
    sha256: str

    def fetch(self) -> Path:
        """The file in ``cache_dir()``, by digest: fetched unless a file of
        the pinned content is already there.

        Raises:
            ValueError: ``url`` is not https.
            RuntimeError: What ``url`` serves is not the pinned content.
        """
        target = cache_dir() / self.url.rsplit("/", 1)[-1]
        if target.exists():
            with open(target, "rb") as f:
                if hashlib.file_digest(f, "sha256").hexdigest() == self.sha256:
                    return target
        if not self.url.startswith("https://"):
            raise ValueError(f"refusing to download over {self.url!r}")
        target.parent.mkdir(parents=True, exist_ok=True)
        # Beside the target and renamed, so an interrupted fetch leaves no
        # truncated file behind; by process, so concurrent workers share none.
        partial = target.with_name(f".{target.name}.{os.getpid()}.part")
        with urllib.request.urlopen(self.url, timeout=60) as response:
            data = response.read()
        if (got := hashlib.sha256(data).hexdigest()) != self.sha256:
            raise RuntimeError(f"{self.url} has SHA-256 {got}, expected {self.sha256}")
        partial.write_bytes(data)
        partial.replace(target)
        return target


def require(*files: Path, staged: bool = True) -> None:
    """Skip the test unless every one of ``files`` exists, except in CI where
    they are ``staged``: there a missing file fails it, naming what the
    runner must hold.
    """
    missing = [str(f) for f in files if not f.exists()]
    if not missing:
        return
    import pytest

    if staged and os.environ.get("CI"):
        pytest.fail(
            f"this CI runner lacks {', '.join(missing)}: install the model's "
            "files at that path; its README says which and how",
            pytrace=False,
        )
    pytest.skip(f"not found outside CI: {missing}")


def load_from_flags(
    request, model, weights: Path, tokenizer="tokenizer.json", staged=True
):
    """``model.load`` of ``weights``' directory, to call with any further
    options, as the CLI loads it at the ``--random-weights`` and
    ``--max-seq-len`` pytest was given. ``require``s ``weights``, the
    config.json beside it and, unless the weights are random, the
    ``tokenizer`` file there.
    """
    seed = request.config.getoption("--random-weights")
    files = [weights, weights.with_name("config.json")]
    if seed is None:
        files.append(weights.with_name(tokenizer))
    require(*files, staged=staged)
    max_seq_len = request.config.getoption("--max-seq-len")
    return functools.partial(
        model.load, weights.parent, seed=seed, max_seq_len=max_seq_len
    )


def prompt(model, chars: int, num_tokens: int, skip: int = 0) -> list[int]:
    tokens = model.prompt(chars, skip=skip)
    assert len(tokens) + num_tokens <= model.config.max_seq_len
    return tokens


def check_generation(model, prompt_len: int, num_tokens: int, *, record):
    """Sample ``num_tokens`` on the device after a prompt of ``prompt_len``
    characters (``CausalLM.generate``); record the time to the first token
    and the tokens per second after it. Returns the prompt and the tokens
    drawn.
    """
    tokens = prompt(model, prompt_len, num_tokens)
    drawn = model.generate(tokens, num_tokens, Sampler())
    print(drawn if model.tokenizer is None else model.tokenizer.decode(drawn))
    record("TTFT", model.stats.ttft)
    if num_tokens > 1:
        record("TPS", model.stats.tokens_per_s)
    return tokens, drawn


def check_prompt_time(model, length: int, runs: int = 3, *, record):
    """Record the median seconds to the first token after a prompt of
    ``length`` tokens over ``runs`` timed runs, each a fresh prompt (random
    ids after BOS: a prompt's time does not follow its ids), so no run
    reuses a chunk another wrote.
    """
    rng = np.random.default_rng(SEED)
    seconds = []
    for _ in range(runs):
        tokens = [model.bos, *rng.integers(0, model.config.vocab_size, length - 1)]
        model.generate(tokens, 1, Sampler())
        seconds.append(model.stats.ttft)
    record("TTFT", float(np.median(seconds)))
    record("Tokens", length)


def check_device_sampling(model, prompt_len: int, num_tokens: int, *, record):
    """Sample ``num_tokens`` on the device after a prompt of ``prompt_len``
    characters (``CausalLM.generate``); record its time to the first token
    and tokens per second, then sample again on the host from each step's
    logits from the same seed: the text is the same, token for token.
    """
    tokens, drawn = check_generation(model, prompt_len, num_tokens, record=record)
    host = generate_on_host(model, tokens, num_tokens, Sampler())
    differing = [i for i, (a, b) in enumerate(zip(drawn, host)) if a != b]
    record("DifferingTokens", len(differing))
    assert not differing, f"tokens {differing} of {num_tokens} differ from the host's"


#: How far a bf16 graph's logits may lie from float32 transformers' on the
#: same weights: a share of the largest logit. Set by hand between what the
#: toys' host references measure, at most 2.2% (LFM2's), and the faults they
#: must catch: half a clip's encoder rows (8.4%), a stale recurrent slot
#: (124%), a position table for RoPE (143%).
LOGITS = 0.05


def assert_close(got, want: np.ndarray, what: str = "the logits") -> None:
    """``got`` within ``LOGITS`` of ``want``, the reference's logits, at
    their largest magnitude; and where the reference's top two lie further
    apart than that bound, the same argmax. A nearer pair may go either
    way. The gate is the bound, not twice the error: a pair further apart
    than twice the error cannot swap, so that gate would check nothing.
    """
    got = np.asarray(got, np.float32).reshape(want.shape)
    scale = np.abs(want).max()
    bound, err = LOGITS * scale, np.abs(got - want).max()
    assert err <= bound, f"{what}: max |diff| {err:.4f} against |logits| {scale:.3f}"
    second, first = np.sort(want)[-2:]
    if first - second > bound:
        assert (
            got.argmax() == want.argmax()
        ), f"{what}: argmax {got.argmax()} != {want.argmax()}"


def check_accuracy(
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
    tokens = prompt(model, chars, num_tokens)
    results = accuracy(model, model.cpu_reference(), tokens, num_tokens)
    stats = kl_stats(results)
    for stat, value in stats.items():
        record(f"{stat}KL", float(value))
    record("Top1Mismatches", sum(not t for _, t in results))
    for stat, bound in bounds.items():
        assert stats[stat] <= bound, f"{stat.lower()} KL {stats[stat]} > {bound}"


def check_embedding(
    got: np.ndarray,
    want: np.ndarray,
    min_cosine: float,
    max_error: float,
    *,
    percentile: float = 1,
    record,
):
    """``got``'s rows against ``want``'s embeddings: the token cosines' low
    percentile (one bad token should not fail every other) and the
    relative error of the whole array.

    Args:
        min_cosine: The percentile cosine must reach.
        max_error: ``||got - want|| / ||want||`` must not exceed.
        percentile: Which percentile of the per-row cosines is judged (1:
            every row but the worst may miss ``min_cosine``).
        record: A test's ``record_property``: the judged cosine, the worst
            row's and the relative error.
    """
    cosines = (got * want).sum(-1) / (
        np.linalg.norm(got, axis=-1) * np.linalg.norm(want, axis=-1)
    )
    error = float(np.linalg.norm(got - want) / np.linalg.norm(want))
    judged = float(np.percentile(cosines, percentile))
    record("Cosine", judged)
    record("Worst cosine", float(cosines.min()))
    record("Relative error", error)
    assert judged >= min_cosine, judged
    assert error <= max_error, error


def check_determinism(
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
    flush fails every run rather than some.
    """
    prompts = [
        prompt(model, chars, num_tokens),
        prompt(model, chars, num_tokens, skip=chars),
    ]
    differing = determinism(model, prompts, num_tokens, rounds)
    record("DifferingRuns", differing)
    total = len(prompts) * (rounds - 1)
    assert differing == 0, f"{differing}/{total} runs' logits differ bitwise"


def check_chat_turn(model, chars: int, turn: int, num_tokens: int = 2, *, record):
    """A prompt extended by a turn, as a chat's next message extends it:
    the model runs from the turn's first token (``CausalLM.resume``) over
    the caches the prompt left, and its logits, and those of the greedy
    steps after, are bit for bit those of the whole run from scratch.

    The prompt is ``chars`` characters, the turn its last ``turn`` tokens.
    Before the run from scratch a prompt of other text overwrites the
    caches, so it reuses nothing of the turn's. Records both runs' seconds.
    """
    whole = prompt(model, chars, num_tokens)
    C = model.config.prefill_chunk
    assert (len(whole) - turn) // C, "the turn reuses no chunk"
    other = prompt(model, chars, 0, skip=1)
    runs = []
    for name, before in (("Turn", whole[:-turn]), ("Scratch", other)):
        model.logits(before)
        start = time.perf_counter()
        runs.append(greedy_logits(model, whole, num_tokens))
        record(f"{name}Seconds", time.perf_counter() - start)
    steps = differing_steps(*runs)
    assert not steps, f"the turn's logits differ from scratch's at steps {steps}"


def check_deep_decode(model, position: int, bound: float, chars: int = 1024, *, record):
    """A decode step at ``position``, deep in the caches, against the
    graph's own reference (``Graph.reference``: each operator's
    ``reference()`` on host tensors, the caches as state), for a context
    transformers would take too long over, within ``bound`` of its
    KL. Whether both rank the same token first is recorded, not required:
    at a near-tie a step can differ in it at a KL of 0.014.

    The caches hold a real prompt, ``chars`` characters of it, repeated up
    to ``position`` (``_fill_caches``).
    """
    tokens = prompt(model, chars, 1)
    token = greedy(model.logits(tokens))
    # A decode step takes the token; the device gathers its embedding row.
    values = dict(token=token, position=position, start=0, rows=1, rope_start=0)
    with _fill_caches(model, len(tokens), position):
        got, _ = model(**values)
        got = got.numpy()
        expected, _ = model.reference(**values)
    kl, top1 = divergence(expected, got)
    record("DeepKL", kl)
    record("DeepTop1", top1)
    assert kl <= bound, f"at {position}: KL {kl} > {bound}"


def check_deep_prompt(model, rows: int, bound: float, chars: int = 1024, *, record):
    """The deepest prompt chunk, the one holding position ``max_seq_len -
    1``, at most ``rows`` rows of it, against the graph's own reference
    within ``bound`` of its KL, every position before it filled as
    ``check_deep_decode`` fills them: the chunk attends over the whole
    context. Records its seconds, the longest a prompt chunk takes, which
    the driver's watchdog bounds where a chunk is one dispatch.
    """
    tokens = prompt(model, chars, 1)
    model.logits(tokens)
    C, L = model.config.prefill_chunk, model.config.max_seq_len
    deepest = (L - 1) // C
    rows = min(rows, L - deepest * C)
    chunk = np.resize(tokens, rows)
    ids = model.session.prompt_ids(chunk)
    begin = deepest * C
    rope = model.rotary_emb
    table = 0 if rope is None else rope.table_start(begin + rows)
    values = dict(
        token=int(chunk[-1]),
        position=begin + rows - 1,
        start=begin,
        rows=rows,
        rope_start=table + begin,
    )
    with _fill_caches(model, len(tokens), begin):
        start = time.perf_counter()
        got, _ = model(ids, **values)
        record("DeepPromptSeconds", time.perf_counter() - start)
        got = got.numpy()
        expected, _ = model.reference(ids, **values)
    kl, top1 = divergence(expected, got)
    record("DeepPromptKL", kl)
    record("DeepPromptTop1", top1)
    assert kl <= bound, f"the chunk at {begin}: KL {kl} > {bound}"


@contextmanager
def _fill_caches(model, n: int, position: int):
    """The caches' first ``n`` rows, a prompt's, repeated up to ``position``
    on the device and as the graph reference's state (the device buffers'
    own host memory, filled in place), for the body of the ``with``; the
    prompt's own rows stay as it wrote them. A state checkpointed at each
    chunk boundary (``Checkpoints``) holds, in the slot a call at
    ``position`` reads, the state the prompt left.
    """
    version = next(iter(model.versions.values()))
    caches = [x for _, x, p, _ in _leaves(model) if isinstance(p, KVCache)]
    for cache in caches:
        rows = version.read(cache)
        for start in range(n, position, n):
            rows[start : min(start + n, position)] = rows[: min(n, position - start)]
        version.push(cache)
        cache.host = rows
    checkpoints = model.recurrent
    for c in checkpoints:
        slots = version.read(c.slots)
        slots[c.slot(position)] = slots[c.slot(n)]
        version.push(c.slots)
        c.slots.host = slots
    try:
        yield
    finally:
        for state in [*caches, *(c.slots for c in checkpoints)]:
            version.push(state)
            state.host = None
