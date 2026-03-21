# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Token sampling strategies for autoregressive generation.

This module provides the TokenSampler class for sampling tokens from
model logits with various strategies.

FEATURES:
- Temperature scaling for creative vs. deterministic output
- Top-k filtering to limit candidate tokens
- Top-p (nucleus) sampling for probability-mass based filtering
- Repetition penalty to discourage repetitive output
- Greedy decoding (temperature = 0)

EXAMPLE USAGE:
    >>> from iron.generation.sampling import TokenSampler
    >>>
    >>> # Create sampler with custom parameters
    >>> sampler = TokenSampler(
    ...     temperature=0.7,
    ...     top_k=50,
    ...     top_p=0.9,
    ...     repetition_penalty=1.1
    ... )
    >>>
    >>> # Sample from logits
    >>> logits = model.forward(tokens)
    >>> token_id = sampler.sample(logits)
    >>>
    >>> # Greedy decoding
    >>> greedy_sampler = TokenSampler(temperature=0.0)
    >>> token_id = greedy_sampler.sample(logits)

CLASSES:
    TokenSampler: Main sampling class with all strategies

Author: Jordan Lee
Version: 1.0.0
"""

from __future__ import annotations

import logging
from typing import Optional, Dict, Any, Tuple
from scipy.special import softmax

import numpy as np

logger = logging.getLogger(__name__)


class TokenSampler:
    """Token sampler with temperature, top_k, top_p, and repetition penalty.

    This class implements various token sampling strategies commonly used
    in autoregressive language model generation.

    Sampling Strategy:
    1. Apply repetition penalty to logits (if > 1.0)
    2. Apply temperature scaling
    3. Apply top-k filtering (keep only top k tokens)
    4. Apply top-p (nucleus) filtering (keep tokens with cumulative prob <= p)
    5. Sample from the resulting distribution (or take argmax for greedy)

    Attributes:
        temperature: Sampling temperature (0.0 = greedy)
        top_k: Number of top tokens to keep (0 = no limit)
        top_p: Cumulative probability threshold for nucleus sampling
        repetition_penalty: Penalty for token repetition (> 1.0 discourages)

    Example:
        >>> sampler = TokenSampler(temperature=0.7, top_k=50, top_p=0.9)
        >>> token = sampler.sample(logits)
    """

    def __init__(
        self,
        temperature: float = 0.7,
        top_k: int = 50,
        top_p: float = 0.9,
        repetition_penalty: float = 1.0,
    ) -> None:
        """Initialize token sampler.

        Args:
            temperature: Sampling temperature. Higher values (e.g., 1.0) make
                output more random; lower values (e.g., 0.1) make it more
                deterministic. Use 0.0 for greedy decoding.
            top_k: Number of top tokens to keep. Only tokens with the highest
                logits are considered for sampling. Use 0 for no limit.
            top_p: Cumulative probability threshold for nucleus sampling.
                Only the smallest set of tokens whose cumulative probability
                exceeds top_p are considered. Use 0.0 or 1.0 to disable.
            repetition_penalty: Penalty factor for token repetition. Values
                > 1.0 discourage repetition; values < 1.0 encourage it.
                Use 1.0 for no penalty.

        Raises:
            ValueError: If any parameter is out of valid range

        Example:
            >>> sampler = TokenSampler(
            ...     temperature=0.8,
            ...     top_k=40,
            ...     top_p=0.92,
            ...     repetition_penalty=1.1
            ... )
        """
        # Validate parameters
        if temperature < 0:
            raise ValueError(f"temperature must be >= 0, got {temperature}")
        if top_k < 0:
            raise ValueError(f"top_k must be >= 0, got {top_k}")
        if not (0 <= top_p <= 1):
            raise ValueError(f"top_p must be in [0, 1], got {top_p}")
        if repetition_penalty < 0:
            raise ValueError(
                f"repetition_penalty must be >= 0, got {repetition_penalty}"
            )

        self.temperature = temperature
        self.top_k = top_k
        self.top_p = top_p
        self.repetition_penalty = repetition_penalty

        logger.debug(
            f"TokenSampler initialized: temp={temperature}, "
            f"top_k={top_k}, top_p={top_p}, rep_penalty={repetition_penalty}"
        )

    def apply_temperature(self, logits: np.ndarray) -> np.ndarray:
        """Apply temperature scaling to logits.

        Temperature scaling affects the probability distribution:
        - High temperature (> 1.0): Flatter distribution, more random
        - Low temperature (< 1.0): Sharper distribution, more confident
        - Temperature = 0: Greedy decoding (argmax)

        Args:
            logits: Raw logits, shape [vocab_size]

        Returns:
            Scaled logits, same shape as input

        Example:
            >>> logits = np.array([1.0, 2.0, 3.0])
            >>> scaled = sampler.apply_temperature(logits)
        """
        if self.temperature == 0:
            # Greedy decoding - return logits as-is (will use argmax later)
            return logits

        if self.temperature == 1.0:
            # No scaling needed
            return logits

        return logits / self.temperature

    def apply_top_k(self, logits: np.ndarray, k: Optional[int] = None) -> np.ndarray:
        """Filter logits to keep only top-k tokens.

        All tokens not in the top-k have their logits set to -inf,
        effectively removing them from consideration.

        Args:
            logits: Raw logits, shape [vocab_size]
            k: Number of tokens to keep. If None, uses self.top_k.

        Returns:
            Filtered logits with non-top-k tokens set to -inf

        Raises:
            ValueError: If k is negative

        Example:
            >>> logits = np.array([1.0, 5.0, 2.0, 8.0, 3.0])
            >>> filtered = sampler.apply_top_k(logits, k=2)
            >>> # Result: [-inf, 5.0, -inf, 8.0, -inf]
        """
        if k is None:
            k = self.top_k

        if k <= 0:
            # No filtering
            return logits

        if k >= len(logits):
            # All tokens kept
            return logits

        # Find top-k indices
        top_k_indices = np.argpartition(logits, -k)[-k:]

        # Create mask for non-top-k tokens
        mask = np.ones_like(logits, dtype=bool)
        mask[top_k_indices] = False

        # Set non-top-k logits to -inf
        result = logits.copy()
        result[mask] = float("-inf")

        return result

    def apply_top_p(self, logits: np.ndarray, p: Optional[float] = None) -> np.ndarray:
        """Apply nucleus (top-p) sampling filter.

        Nucleus sampling keeps only the smallest set of tokens whose
        cumulative probability exceeds p. This provides a dynamic
        number of candidates based on the distribution shape.

        Args:
            logits: Raw logits, shape [vocab_size]
            p: Cumulative probability threshold. If None, uses self.top_p.

        Returns:
            Filtered logits with low-probability tokens set to -inf

        Raises:
            ValueError: If p is not in [0, 1]

        Example:
            >>> logits = np.array([0.1, 0.2, 0.3, 0.4])
            >>> filtered = sampler.apply_top_p(logits, p=0.7)
            >>> # Keeps tokens that sum to ~70% probability
        """
        if p is None:
            p = self.top_p

        if p <= 0 or p >= 1:
            # No filtering
            return logits

        # Sort logits in descending order
        sorted_indices = np.argsort(logits)[::-1]
        sorted_logits = logits[sorted_indices]

        # Convert to probabilities
        probs = softmax(sorted_logits)

        # Calculate cumulative probabilities
        cumulative_probs = np.cumsum(probs)

        # Find cutoff: tokens with cumulative prob > p are removed
        # But we include the first token that exceeds p
        cutoff_mask = cumulative_probs <= p
        # Include the first token that exceeds p
        if not np.all(cutoff_mask) and np.any(cutoff_mask):
            cutoff_mask[np.argmax(~cutoff_mask)] = True

        # Create result with -inf for removed tokens
        result = logits.copy()
        removed_indices = sorted_indices[~cutoff_mask]
        result[removed_indices] = float("-inf")

        return result

    def apply_repetition_penalty(
        self, logits: np.ndarray, input_ids: Optional[np.ndarray] = None
    ) -> np.ndarray:
        """Apply repetition penalty to logits.

        The repetition penalty reduces the probability of tokens that
        have already appeared in the generated sequence. This helps
        prevent repetitive output.

        Penalty formula:
        - If token in input_ids: logit /= repetition_penalty
        - Otherwise: logit unchanged

        Args:
            logits: Raw logits, shape [vocab_size]
            input_ids: Previously generated token IDs. If None or empty,
                no penalty is applied.

        Returns:
            Penalized logits, same shape as input

        Example:
            >>> logits = np.array([1.0, 2.0, 3.0])
            >>> input_ids = np.array([2])  # Token 2 was generated
            >>> penalized = sampler.apply_repetition_penalty(logits, input_ids)
            >>> # Token 2's logit is reduced
        """
        if self.repetition_penalty == 1.0:
            # No penalty
            return logits

        if input_ids is None or len(input_ids) == 0:
            # No tokens to penalize
            return logits

        result = logits.copy()

        # Apply penalty to tokens that appeared in input
        for token_id in np.unique(input_ids):
            if 0 <= token_id < len(logits):
                if result[token_id] > 0:
                    result[token_id] /= self.repetition_penalty
                else:
                    result[token_id] *= self.repetition_penalty

        return result

    def sample(
        self,
        logits: np.ndarray,
        input_ids: Optional[np.ndarray] = None,
        return_probs: bool = False,
    ) -> int | Tuple[int, np.ndarray]:
        """Sample next token from logits.

        This is the main sampling method that applies all configured
        transformations and returns a sampled token.

        Sampling order:
        1. Apply repetition penalty (if input_ids provided and penalty > 1.0)
        2. Apply temperature scaling
        3. Apply top-k filtering
        4. Apply top-p filtering
        5. Sample from distribution (or argmax for greedy)

        Args:
            logits: Raw logits from model, shape [vocab_size]
            input_ids: Previously generated tokens for repetition penalty
            return_probs: If True, also return the probability distribution

        Returns:
            Sampled token ID, or tuple of (token_id, probs) if return_probs

        Raises:
            ValueError: If logits are invalid (empty, all -inf)

        Example:
            >>> logits = model(tokens)
            >>> token = sampler.sample(logits)
            >>>
            >>> # With repetition penalty
            >>> token = sampler.sample(logits, input_ids=generated_tokens)
            >>>
            >>> # Get probabilities
            >>> token, probs = sampler.sample(logits, return_probs=True)
        """
        if len(logits) == 0:
            raise ValueError("Logits cannot be empty")

        # Work with a copy
        processed_logits = logits.copy()

        # Step 1: Apply repetition penalty
        if self.repetition_penalty != 1.0 and input_ids is not None:
            processed_logits = self.apply_repetition_penalty(
                processed_logits, input_ids
            )

        # Step 2: Apply temperature
        if self.temperature > 0:
            processed_logits = self.apply_temperature(processed_logits)

        # Step 3: Apply top-k filtering
        if self.top_k > 0:
            processed_logits = self.apply_top_k(processed_logits)

        # Step 4: Apply top-p filtering
        if 0 < self.top_p < 1:
            processed_logits = self.apply_top_p(processed_logits)

        # Handle edge case: all logits are -inf
        if np.all(processed_logits == float("-inf")):
            logger.warning("All logits are -inf after filtering, using original logits")
            processed_logits = logits.copy()

        # Step 5: Sample or argmax
        if self.temperature == 0:
            # Greedy decoding
            token_id = int(np.argmax(processed_logits))
            probs = np.zeros_like(logits)
            probs[token_id] = 1.0
        else:
            # Convert to probabilities
            # Subtract max for numerical stability
            shifted_logits = processed_logits - np.max(processed_logits)
            exp_logits = np.exp(shifted_logits)
            probs = exp_logits / np.sum(exp_logits)

            # Sample from distribution
            token_id = int(np.random.choice(len(logits), p=probs))

        logger.debug(f"Sampled token {token_id} with prob {probs[token_id]:.4f}")

        if return_probs:
            return token_id, probs
        return token_id

    def sample_multiple(
        self,
        logits_batch: np.ndarray,
        input_ids_batch: Optional[np.ndarray] = None,
        return_probs: bool = False,
    ) -> np.ndarray | Tuple[np.ndarray, np.ndarray]:
        """Sample multiple tokens from a batch of logits.

        Args:
            logits_batch: Batch of logits, shape [batch_size, vocab_size]
            input_ids_batch: Optional batch of input IDs for repetition penalty
            return_probs: If True, also return probability distributions

        Returns:
            Sampled token IDs, shape [batch_size], or tuple of
            (token_ids, probs) if return_probs

        Example:
            >>> logits = model(batch_tokens)
            >>> tokens = sampler.sample_multiple(logits)
        """
        batch_size = logits_batch.shape[0]
        token_ids = np.zeros(batch_size, dtype=np.int32)
        probs_list = []

        for i in range(batch_size):
            input_ids = None
            if input_ids_batch is not None:
                input_ids = input_ids_batch[i]

            result = self.sample(logits_batch[i], input_ids, return_probs=True)
            token_ids[i] = result[0]
            if return_probs:
                probs_list.append(result[1])

        if return_probs:
            return token_ids, np.array(probs_list)
        return token_ids

    def get_config(self) -> Dict[str, Any]:
        """Get sampler configuration as dictionary.

        Returns:
            Dictionary with all sampler parameters

        Example:
            >>> config = sampler.get_config()
            >>> print(f"Temperature: {config['temperature']}")
        """
        return {
            "temperature": self.temperature,
            "top_k": self.top_k,
            "top_p": self.top_p,
            "repetition_penalty": self.repetition_penalty,
        }

    def set_config(self, config: Dict[str, Any]) -> None:
        """Update sampler configuration.

        Args:
            config: Dictionary with sampler parameters

        Raises:
            ValueError: If any parameter is invalid

        Example:
            >>> sampler.set_config({"temperature": 0.5, "top_k": 40})
        """
        if "temperature" in config:
            self.temperature = config["temperature"]
        if "top_k" in config:
            self.top_k = config["top_k"]
        if "top_p" in config:
            self.top_p = config["top_p"]
        if "repetition_penalty" in config:
            self.repetition_penalty = config["repetition_penalty"]

        # Validate
        TokenSampler(
            temperature=self.temperature,
            top_k=self.top_k,
            top_p=self.top_p,
            repetition_penalty=self.repetition_penalty,
        )

    def __repr__(self) -> str:
        """Get string representation of sampler."""
        return (
            f"TokenSampler(temperature={self.temperature}, "
            f"top_k={self.top_k}, top_p={self.top_p}, "
            f"repetition_penalty={self.repetition_penalty})"
        )


# Convenience functions for common sampling configurations


def greedy_sampler() -> TokenSampler:
    """Create a greedy (deterministic) sampler.

    Returns:
        TokenSampler with temperature=0.0

    Example:
        >>> sampler = greedy_sampler()
        >>> token = sampler.sample(logits)  # Always picks highest probability
    """
    return TokenSampler(temperature=0.0)


def creative_sampler(temperature: float = 1.0, top_p: float = 0.95) -> TokenSampler:
    """Create a high-creativity sampler.

    Args:
        temperature: High temperature for variety (default: 1.0)
        top_p: Nucleus sampling threshold (default: 0.95)

    Returns:
        TokenSampler configured for creative output

    Example:
        >>> sampler = creative_sampler()
        >>> token = sampler.sample(logits)  # More varied output
    """
    return TokenSampler(temperature=temperature, top_p=top_p, top_k=0)


def balanced_sampler(
    temperature: float = 0.7, top_k: int = 50, top_p: float = 0.9
) -> TokenSampler:
    """Create a balanced sampler.

    Args:
        temperature: Moderate temperature (default: 0.7)
        top_k: Top-k limit (default: 50)
        top_p: Nucleus threshold (default: 0.9)

    Returns:
        TokenSampler with balanced settings

    Example:
        >>> sampler = balanced_sampler()
        >>> token = sampler.sample(logits)  # Balanced creativity/coherence
    """
    return TokenSampler(
        temperature=temperature, top_k=top_k, top_p=top_p, repetition_penalty=1.0
    )
