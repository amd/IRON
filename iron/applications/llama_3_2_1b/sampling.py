# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Next-token sampling over one row of logits, in numpy."""

from __future__ import annotations

import numpy as np


class Sampler:
    """Temperature, then top-k, then a draw from the softmax.

    The steps the harness took in torch before this replaced them: logits
    are divided by the temperature, every logit below the ``top_k``-th
    largest is dropped (ties with it are kept, as ``torch.where(logits <
    kth, -inf, ...)`` kept them), and a token is drawn from the softmax of
    what is left.

    Two differences from that pipeline, both deliberate. The arithmetic is
    float32 over the (bf16) logits and the draw float64, where torch stayed
    in bf16 throughout; and a temperature of 0 is greedy (the argmax), where
    torch skipped the scaling and still sampled. The draw comes from ``rng``,
    so a seeded generator makes it reproducible; it is not torch's
    ``multinomial`` stream, so the same seed does not pick the same tokens.
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
            return int(np.argmax(np.asarray(logits, dtype=np.float32).reshape(-1)))
        probs = self.probabilities(logits)
        cdf = np.cumsum(probs)
        # The first token whose cumulative mass exceeds the draw; a zero-mass
        # token never exceeds its predecessor, so it is never picked.
        token = int(np.searchsorted(cdf, self.rng.random() * cdf[-1], side="right"))
        # A draw just under 1 can round up to the total, past every token;
        # it belongs to the last one with any mass.
        return token if token < cdf.size else int(np.flatnonzero(probs)[-1])
