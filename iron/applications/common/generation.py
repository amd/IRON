# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sampling, and the loops that generate and check, over any model.

A model is anything with ``logits(tokens)``: the logits after the last of
``tokens``, the whole history so far, as ``(vocab_size,)``. A
:class:`~.model.CausalLM` on the NPU is one, and so is a CPU reference.
"""

import time

import numpy as np

#: Seeds the sampler, so a run's text is reproducible.
SEED = 1608560892


class Sampler:
    """Temperature, then top-k, then a draw from the softmax.

    Logits are divided by the temperature, every logit below the
    ``top_k``-th largest is dropped (ties with it are kept), and a token is
    drawn from the softmax of what is left. The arithmetic is float32 over
    the (bf16) logits and the draw float64; a temperature of 0 is greedy
    (the argmax). The draw comes from ``rng``, so a seeded generator makes
    it reproducible.
    """

    def __init__(
        self,
        temperature: float,
        top_k: int | None,
        rng: np.random.Generator,
    ):
        if temperature < 0:
            raise ValueError(f"temperature {temperature} is negative")
        if top_k is not None and top_k < 1:
            raise ValueError(f"top_k {top_k} keeps no token")
        self.temperature = temperature
        self.top_k = top_k
        self.rng = rng

    def probabilities(self, logits: np.ndarray) -> np.ndarray:
        """The distribution a token is drawn from, float64, over ``logits`` (1-D)."""
        x = np.asarray(logits, dtype=np.float32).reshape(-1)
        x = x / np.float32(self.temperature)
        if self.top_k is not None and self.top_k < x.size:
            kth = np.partition(x, -self.top_k)[-self.top_k]
            x = np.where(x < kth, -np.inf, x)
        e = np.exp((x - x.max()).astype(np.float64))
        return e / e.sum()

    def __call__(self, logits: np.ndarray) -> int:
        """One token id drawn from a row of logits (any shape of one row)."""
        if self.temperature == 0:
            return greedy(logits)
        probs = self.probabilities(logits)
        cdf = np.cumsum(probs)
        # The first token whose cumulative mass exceeds the draw; a zero-mass
        # token never exceeds its predecessor, so it is never picked.
        token = int(np.searchsorted(cdf, self.rng.random() * cdf[-1], side="right"))
        # A draw just under 1 can round up to the total, past every token;
        # it belongs to the last one with any mass.
        return token if token < cdf.size else int(np.flatnonzero(probs)[-1])


def greedy(logits: np.ndarray) -> int:
    return int(np.argmax(np.asarray(logits, dtype=np.float32).reshape(-1)))


def generate(model, tokens, num_tokens, sample, show=None):
    """Draw ``num_tokens`` after ``tokens``, each passed to ``show``.

    Returns the tokens drawn, the seconds to the first and the mean seconds
    per token after it (NaN for one token).
    """
    history, seconds = [int(t) for t in tokens], []
    for _ in range(num_tokens):
        start = time.perf_counter()
        history.append(sample(model.logits(history)))
        seconds.append(time.perf_counter() - start)
        if show is not None:
            show(history[-1])
    later = np.mean(seconds[1:]) if num_tokens > 1 else float("nan")
    return history[-num_tokens:], seconds[0], float(later)


def _log_softmax(logits):
    x = np.asarray(logits, dtype=np.float64).reshape(-1)
    x = x - x.max()
    return x - np.log(np.exp(x).sum())


def accuracy(model, reference, tokens, num_tokens) -> list[tuple[float, bool]]:
    """``model``'s next-token distributions against ``reference``'s, over
    ``num_tokens`` steps from ``tokens``.

    Teacher-forced: both are fed the reference's greedy token, so a
    divergence at a step is the model's own error there rather than the
    consequence of an earlier different choice. One ``(kl, top1)`` per step:
    KL(reference || model), and whether both rank the same token first.
    """
    history, results = [int(t) for t in tokens], []
    for step in range(num_tokens):
        got = _log_softmax(model.logits(history))
        ref = _log_softmax(reference.logits(history))
        kl = float(np.sum(np.exp(ref) * (ref - got)))
        top1 = int(got.argmax()) == int(ref.argmax())
        results.append((kl, top1))
        print(f"step {step:3d}  KL {kl:.5f}  top-1 {'match' if top1 else 'MISMATCH'}")
        history.append(int(ref.argmax()))
    return results


def kl_stats(results) -> dict[str, float]:
    """The mean, p90 and max KL of :func:`accuracy`'s results.

    Over every step, prefill and decode alike: one step's KL depends as much
    on how confident the reference is at that position as on the model.
    """
    kl = np.array([k for k, _ in results])
    return {"Mean": kl.mean(), "P90": np.percentile(kl, 90), "Max": kl.max()}


def determinism(model, prompts, num_tokens, rounds) -> int:
    """How many runs' logits differ bitwise from the first of their prompt.

    Each prompt runs ``rounds`` times, alternating, ``num_tokens`` greedy
    tokens each. Alternating prompts with different text matters: a host
    write that never reaches the device then reads the other prompt's data,
    not a leftover copy of its own.
    """
    first: list = [None] * len(prompts)
    differ = 0
    for r in range(rounds * len(prompts)):
        p = r % len(prompts)
        history, rows = [int(t) for t in prompts[p]], []
        for _ in range(num_tokens):
            logits = model.logits(history)
            rows.append(logits.view(np.uint8))  # NaNs and signed zeros too
            history.append(greedy(logits))
        run = np.stack(rows)
        if first[p] is None:
            first[p] = run
            continue
        steps = np.flatnonzero((run != first[p]).any(axis=1)).tolist()
        if steps:
            differ += 1
            print(f"round {r} (prompt {p}): logits differ at steps {steps}")
    return differ
