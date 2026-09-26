# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Next-token sampling over one row of logits, exactly as the NPU draws it."""

from __future__ import annotations

import numpy as np

from aie.iron.kernels.sample import (
    ROW_WORDS,
    check_order_preserving,
    draw_row,
    sample_ref,
    sample_weights,
)


class Sampler:
    """Temperature, then top-k, then a draw from the softmax: bit-exact.

    Every draw is ``aie.iron.kernels.sample.sample_ref``, the definition the
    device's :class:`~iron.operators.Sample` meets bit for bit, so the host
    and the device pick the same token from the same logits and the same
    uniform. Logits in another dtype (the torch reference's float32) are
    rounded to bf16 first. A temperature of 0 is greedy (the first argmax). Every logit
    below the ``top_k``-th largest is dropped, ties with it kept; ``None``
    keeps the whole row (the host only: the device's top-k is bounded).

    Each draw takes one uniform from ``rng``, ``rng.random()``, greedy or
    not; a seeded generator makes the draws reproducible, and :meth:`rows`
    takes the same uniforms for the device.
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
        """``count`` draws for the device, ``(count, 4)`` int32, one per position.

        They take the uniforms ``count`` host draws would, in order. ``k_max``
        is the device's largest top-k; a larger one, or ``None``, would be
        clamped there, not honoured, so it is refused.
        """
        if self.top_k is None or self.top_k > k_max:
            raise ValueError(
                f"top_k {self.top_k} is not one the device draws (1..{k_max})"
            )
        rows = np.empty((count, ROW_WORDS), dtype=np.int32)
        for i in range(count):
            rows[i] = draw_row(self.temperature, self.top_k, self._n53())
        return rows
