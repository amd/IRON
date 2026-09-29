# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sampling, and the loops that generate and check, over any model.

A model is anything with ``logits(tokens)``: the logits after the last of
``tokens``, the whole history so far, as ``(vocab_size,)``. A
``CausalLM`` on the NPU is one, and so is a CPU reference.
"""

import time

import numpy as np
from aie.iron.kernels.sample import (
    ROW_WORDS,
    check_order_preserving,
    draw_row,
    sample_ref,
    sample_weights,
)

#: Seeds the sampler, so a run's text is reproducible.
SEED = 1608560892


class Sampler:
    """Temperature, then top-k, then a draw from the softmax, exactly as
    the device draws.

    Every draw is ``aie.iron.kernels.sample.sample_ref``, the definition the
    ``Sample`` operator meets bit for bit, so
    the host and the device pick the same token from the same logits and
    the same uniform. Logits are rounded to bf16 first. Every logit below
    the ``top_k``-th largest is dropped, ties with it kept; ``None`` keeps
    the whole row (the host only: the device's top-k is bounded). A
    temperature of 0 is greedy (the first largest).

    Each draw takes one uniform from ``rng``, greedy or not, so a seeded
    generator makes the draws reproducible, and ``rows`` hands the
    device the same uniforms.
    """

    def __init__(
        self,
        temperature: float,
        top_k: int | None,
        rng: np.random.Generator,
    ):
        if temperature < 0:
            raise ValueError(f"temperature {temperature} is negative")
        if temperature > 0:
            # The draw thresholds bf16 keys, which is exact only when
            # dividing by the temperature keeps every logit's order.
            check_order_preserving(temperature)
        if top_k is not None and top_k < 1:
            raise ValueError(f"top_k {top_k} keeps no token")
        self.temperature = np.float32(temperature)
        self.top_k = top_k
        self.rng = rng

    def _top_k(self, size: int) -> int:
        return size if self.top_k is None else self.top_k

    def _n53(self) -> int:
        # random() is n53 * 2^-53 for the generator's next 53 bits, exactly.
        return int(self.rng.random() * 2.0**53)

    def probabilities(self, logits: np.ndarray) -> np.ndarray:
        """The distribution a token is drawn from, float64, over ``logits`` (1-D)."""
        size = np.asarray(logits).size
        probs = np.zeros(size, dtype=np.float64)
        if self.temperature == 0:
            probs[sample_ref(logits, self.temperature, 1, 0)] = 1.0
            return probs
        candidates, weights = sample_weights(
            logits, self.temperature, self._top_k(size)
        )
        probs[candidates] = weights / weights.sum()
        return probs

    def __call__(self, logits: np.ndarray) -> int:
        """One token id drawn from a row of logits (any shape of one row)."""
        top_k = self._top_k(np.asarray(logits).size)
        return sample_ref(logits, self.temperature, top_k, self._n53())

    def rows(self, count: int, k_max: int) -> np.ndarray:
        """``count`` draws for the device, ``(count, ROW_WORDS)`` int32, one
        per position, taking the uniforms ``count`` host draws would, in
        order.

        ``k_max`` is the device's largest top-k; a larger one, or ``None``,
        would be clamped there, not honoured, so it is refused.
        """
        if self.top_k is None or self.top_k > k_max:
            raise ValueError(
                f"top_k {self.top_k} is not one the device draws (1..{k_max})"
            )
        rows = np.empty((count, ROW_WORDS), dtype=np.int32)
        for i in range(count):
            rows[i] = draw_row(self.temperature, self.top_k, self._n53())
        return rows


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


def divergence(reference, logits) -> tuple[float, bool]:
    """KL(reference || model) of two rows of logits, and whether both rank
    the same token first.
    """
    ref, got = _log_softmax(reference), _log_softmax(logits)
    kl = float(np.sum(np.exp(ref) * (ref - got)))
    return kl, int(got.argmax()) == int(ref.argmax())


def accuracy(model, reference, tokens, num_tokens) -> list[tuple[float, bool]]:
    """``model``'s next-token distributions against ``reference``'s, over
    ``num_tokens`` steps from ``tokens``.

    Teacher-forced: both are fed the reference's greedy token, so a
    divergence at a step is the model's own error there rather than the
    consequence of an earlier different choice. One ``divergence`` per
    step.
    """
    history, results = [int(t) for t in tokens], []
    for step in range(num_tokens):
        ref = reference.logits(history)
        kl, top1 = divergence(ref, model.logits(history))
        results.append((kl, top1))
        print(f"step {step:3d}  KL {kl:.5f}  top-1 {'match' if top1 else 'MISMATCH'}")
        history.append(greedy(ref))
    return results


def kl_stats(results) -> dict[str, float]:
    """The mean, p90 and max KL of ``accuracy``'s results.

    Over every step, prefill and decode alike: one step's KL depends as much
    on how confident the reference is at that position as on the model.
    """
    kl = np.array([k for k, _ in results])
    return {"Mean": kl.mean(), "P90": np.percentile(kl, 90), "Max": kl.max()}


def greedy_logits(model, tokens, num_tokens) -> np.ndarray:
    """The logits of ``num_tokens`` greedy steps from ``tokens``, one row
    each, the first the prompt's.
    """
    history, rows = [int(t) for t in tokens], []
    for _ in range(num_tokens):
        rows.append(model.logits(history))
        history.append(greedy(rows[-1]))
    return np.stack(rows)


def differing_steps(run, first) -> list[int]:
    """The steps at which two ``greedy_logits`` runs differ bitwise,
    NaNs and signed zeros included.
    """
    run, first = (np.ascontiguousarray(r).view(np.uint8) for r in (run, first))
    return np.flatnonzero((run != first).any(axis=1)).tolist()


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
        run = greedy_logits(model, prompts[p], num_tokens)
        if first[p] is None:
            first[p] = run
            continue
        steps = differing_steps(run, first[p])
        if steps:
            differ += 1
            print(f"round {r} (prompt {p}): logits differ at steps {steps}")
    return differ
