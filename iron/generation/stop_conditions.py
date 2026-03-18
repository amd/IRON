# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Stop condition detection for autoregressive generation.

This module provides the StopConditionChecker class for detecting
when text generation should terminate.

FEATURES:
- EOS (End of Sequence) token detection
- Maximum token limit enforcement
- Stop string detection in generated text
- Multiple stop condition support
- Configurable stop conditions

STOP CONDITIONS:
1. EOS Token: Model-generated end-of-sequence token
2. Max Tokens: Configurable maximum generation length
3. Stop Strings: User-defined strings that trigger stopping

EXAMPLE USAGE:
    >>> from iron.generation.stop_conditions import StopConditionChecker
    >>> from iron.api.generation_config import GenerationConfig
    >>>
    >>> config = GenerationConfig(
    ...     eos_tokens=[128001, 128009],
    ...     max_new_tokens=512,
    ...     stop_strings=["</answer>", "Q:"]
    ... )
    >>>
    >>> checker = StopConditionChecker(config)
    >>>
    >>> # Check individual conditions
    >>> result = checker.check_eos(128001)
    >>> assert result.should_stop and result.reason == "eos_token"
    >>>
    >>> result = checker.check_max_tokens(512)
    >>> assert result.should_stop and result.reason == "max_tokens"
    >>>
    >>> # Check all conditions at once
    >>> result = checker.check_all(token_id, generated_text, num_generated)

CLASSES:
    StopConditionChecker: Main stop condition detection class
    StopResult: Result of stop condition check

Author: Jordan Lee
Version: 1.0.0
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import List, Optional, Set, Any

logger = logging.getLogger(__name__)


@dataclass
class StopResult:
    """Result of a stop condition check.

    This dataclass holds information about whether generation should
    stop and, if so, which condition triggered the stop.

    Attributes:
        should_stop: Whether generation should terminate
        reason: Stop reason identifier. One of:
            - "eos_token": End-of-sequence token detected
            - "max_tokens": Maximum token limit reached
            - "stop_string": Configured stop string found
            - "": No stop condition met (continuing)
        stop_string: The stop string that was detected (if applicable)
        token_id: The token that triggered the stop (if applicable)

    Example:
        >>> result = StopResult(
        ...     should_stop=True,
        ...     reason="eos_token",
        ...     token_id=128001
        ... )
        >>> if result.should_stop:
        ...     print(f"Stopping due to: {result.reason}")
    """

    should_stop: bool = False
    reason: str = ""
    stop_string: Optional[str] = None
    token_id: Optional[int] = None

    def __bool__(self) -> bool:
        """Allow using StopResult in boolean context."""
        return self.should_stop

    def __str__(self) -> str:
        """Get human-readable string representation."""
        if self.should_stop:
            return f"StopResult(stop={self.reason})"
        return "StopResult(continue)"


class StopConditionChecker:
    """Checks stop conditions during autoregressive generation.

    This class monitors multiple stop conditions and determines when
    text generation should terminate. It supports:

    1. EOS Token Detection: Identifies end-of-sequence tokens specific
       to the model (e.g., 128001 for Llama3.2)

    2. Max Tokens: Enforces a maximum generation length to prevent
       infinite generation

    3. Stop Strings: Detects user-defined strings in the generated
       text (e.g., "</answer>", "Q:", "\\n\\n")

    Attributes:
        config: Generation configuration with stop parameters

    Example:
        >>> checker = StopConditionChecker(config)
        >>> result = checker.check_all(token_id, text, num_tokens)
        >>> if result.should_stop:
        ...     print(f"Generation stopped: {result.reason}")
    """

    def __init__(self, config: Any) -> None:
        """Initialize stop condition checker.

        Args:
            config: Generation configuration with stop parameters.
                Expected attributes:
                - eos_tokens: List of EOS token IDs
                - max_new_tokens: Maximum tokens to generate
                - stop_strings: List of stop strings

        Example:
            >>> config = GenerationConfig(
            ...     eos_tokens=[128001],
            ...     max_new_tokens=512
            ... )
            >>> checker = StopConditionChecker(config)
        """
        self.config = config

        # Extract stop parameters
        # Handle both GenerationConfig and dict-like objects
        if hasattr(config, "eos_tokens"):
            self.eos_tokens: Set[int] = set(config.eos_tokens or [])
            self.max_tokens: int = config.max_new_tokens or 2048
            self.stop_strings: List[str] = list(config.stop_strings or [])
        elif isinstance(config, dict):
            self.eos_tokens = set(config.get("eos_tokens", []) or [])
            self.max_tokens = config.get("max_new_tokens", 2048)
            self.stop_strings = list(config.get("stop_strings", []) or [])
        else:
            # Defaults
            self.eos_tokens = {128001}  # Llama3.2 default
            self.max_tokens = 2048
            self.stop_strings = []

        logger.debug(
            f"StopConditionChecker initialized: "
            f"eos_tokens={self.eos_tokens}, max_tokens={self.max_tokens}, "
            f"stop_strings={self.stop_strings}"
        )

    def check_eos(self, token_id: int) -> StopResult:
        """Check if token is an EOS token.

        Checks whether the generated token ID matches any configured
        end-of-sequence token.

        Args:
            token_id: Generated token ID to check

        Returns:
            StopResult with should_stop=True if token is EOS

        Example:
            >>> result = checker.check_eos(128001)
            >>> assert result.should_stop and result.reason == "eos_token"
        """
        if token_id in self.eos_tokens:
            logger.info(f"EOS token {token_id} detected")
            return StopResult(should_stop=True, reason="eos_token", token_id=token_id)
        return StopResult(should_stop=False)

    def check_max_tokens(self, num_generated: int) -> StopResult:
        """Check if maximum token limit is reached.

        Args:
            num_generated: Number of tokens generated so far

        Returns:
            StopResult with should_stop=True if limit reached

        Example:
            >>> result = checker.check_max_tokens(512)
            >>> assert result.should_stop and result.reason == "max_tokens"
        """
        if num_generated >= self.max_tokens:
            logger.info(f"Max tokens ({self.max_tokens}) reached")
            return StopResult(should_stop=True, reason="max_tokens")
        return StopResult(should_stop=False)

    def check_stop_string(self, generated_text: str) -> StopResult:
        """Check if generated text contains a stop string.

        Searches the generated text for any configured stop strings.
        Comparison is case-sensitive and exact.

        Args:
            generated_text: Full generated text to check

        Returns:
            StopResult with should_stop=True if stop string found

        Example:
            >>> result = checker.check_stop_string("The answer is </answer>")
            >>> assert result.should_stop and result.stop_string == "</answer>"
        """
        if not self.stop_strings:
            return StopResult(should_stop=False)

        for stop_string in self.stop_strings:
            if stop_string in generated_text:
                logger.info(f"Stop string '{stop_string}' detected")
                return StopResult(
                    should_stop=True, reason="stop_string", stop_string=stop_string
                )

        return StopResult(should_stop=False)

    def check_all(
        self, token_id: int, generated_text: str = "", num_generated: int = 0
    ) -> StopResult:
        """Check all stop conditions.

        Evaluates all stop conditions in priority order:
        1. EOS token (highest priority - model decided to stop)
        2. Max tokens (hard limit)
        3. Stop strings (user-defined)

        Args:
            token_id: Current generated token ID
            generated_text: Full generated text so far
            num_generated: Number of tokens generated

        Returns:
            StopResult with first triggered condition, or
            StopResult(should_stop=False) if all checks pass

        Example:
            >>> result = checker.check_all(
            ...     token_id=5023,
            ...     generated_text="Hello, world!",
            ...     num_generated=10
            ... )
            >>> if not result.should_stop:
            ...     continue_generating()
        """
        # Check EOS (highest priority)
        result = self.check_eos(token_id)
        if result.should_stop:
            return result

        # Check max tokens
        result = self.check_max_tokens(num_generated)
        if result.should_stop:
            return result

        # Check stop strings
        if self.stop_strings and generated_text:
            result = self.check_stop_string(generated_text)
            if result.should_stop:
                return result

        return StopResult(should_stop=False)

    def check_batch(
        self, token_ids: List[int], generated_texts: List[str], num_generated: List[int]
    ) -> List[StopResult]:
        """Check stop conditions for a batch of sequences.

        Args:
            token_ids: List of token IDs for each sequence
            generated_texts: List of generated texts
            num_generated: List of token counts

        Returns:
            List of StopResult for each sequence

        Example:
            >>> results = checker.check_batch(
            ...     token_ids=[128001, 5023],
            ...     generated_texts=["End", "Continue"],
            ...     num_generated=[100, 50]
            ... )
            >>> assert results[0].should_stop  # EOS detected
            >>> assert not results[1].should_stop  # Continue
        """
        results = []
        for token_id, text, count in zip(token_ids, generated_texts, num_generated):
            result = self.check_all(token_id, text, count)
            results.append(result)
        return results

    def set_stop_strings(self, stop_strings: List[str]) -> None:
        """Update stop strings configuration.

        Args:
            stop_strings: New list of stop strings

        Example:
            >>> checker.set_stop_strings(["</answer>", "Q:"])
        """
        self.stop_strings = list(stop_strings)
        logger.debug(f"Stop strings updated: {self.stop_strings}")

    def set_max_tokens(self, max_tokens: int) -> None:
        """Update maximum token limit.

        Args:
            max_tokens: New maximum token count

        Raises:
            ValueError: If max_tokens is less than 1

        Example:
            >>> checker.set_max_tokens(1024)
        """
        if max_tokens < 1:
            raise ValueError("max_tokens must be >= 1")
        self.max_tokens = max_tokens
        logger.debug(f"Max tokens updated: {self.max_tokens}")

    def set_eos_tokens(self, eos_tokens: List[int]) -> None:
        """Update EOS token list.

        Args:
            eos_tokens: New list of EOS token IDs

        Example:
            >>> checker.set_eos_tokens([128001, 128009])
        """
        self.eos_tokens = set(eos_tokens)
        logger.debug(f"EOS tokens updated: {self.eos_tokens}")

    def get_config(self) -> dict:
        """Get stop condition configuration.

        Returns:
            Dictionary with current configuration

        Example:
            >>> config = checker.get_config()
            >>> print(f"Max tokens: {config['max_tokens']}")
        """
        return {
            "eos_tokens": list(self.eos_tokens),
            "max_tokens": self.max_tokens,
            "stop_strings": self.stop_strings,
        }

    def __repr__(self) -> str:
        """Get string representation."""
        return (
            f"StopConditionChecker(eos_tokens={len(self.eos_tokens)}, "
            f"max_tokens={self.max_tokens}, stop_strings={len(self.stop_strings)})"
        )


# Convenience functions


def create_llama3_stop_checker(
    max_tokens: int = 2048, stop_strings: Optional[List[str]] = None
) -> StopConditionChecker:
    """Create a stop checker configured for Llama3.2.

    Args:
        max_tokens: Maximum tokens to generate
        stop_strings: Optional additional stop strings

    Returns:
        StopConditionChecker for Llama3.2

    Example:
        >>> checker = create_llama3_stop_checker(max_tokens=512)
    """
    from ..api.generation_config import GenerationConfig

    config = GenerationConfig(
        model_type="llama3",
        eos_tokens=[128001, 128009],  # Llama3.2 EOS tokens
        max_new_tokens=max_tokens,
        stop_strings=stop_strings,
    )

    return StopConditionChecker(config)


def create_permissive_checker(max_tokens: int = 4096) -> StopConditionChecker:
    """Create a permissive checker (EOS only).

    Only stops on EOS token or max tokens. No stop string detection.

    Args:
        max_tokens: Maximum tokens to generate

    Returns:
        Permissive StopConditionChecker

    Example:
        >>> checker = create_permissive_checker()
    """
    from ..api.generation_config import GenerationConfig

    config = GenerationConfig(
        eos_tokens=[128001, 128009], max_new_tokens=max_tokens, stop_strings=None
    )

    return StopConditionChecker(config)


def create_strict_checker(
    max_tokens: int = 512, stop_strings: Optional[List[str]] = None
) -> StopConditionChecker:
    """Create a strict checker with many stop conditions.

    Includes common stop strings for structured output.

    Args:
        max_tokens: Maximum tokens to generate
        stop_strings: Additional stop strings to include

    Returns:
        Strict StopConditionChecker

    Example:
        >>> checker = create_strict_checker(
        ...     stop_strings=["User:", "Human:"]
        ... )
    """
    default_stop_strings = [
        "\n\n",  # Double newline
        "</s>",  # Common EOS marker
        "###",  # Section marker
    ]

    if stop_strings:
        default_stop_strings.extend(stop_strings)

    from ..api.generation_config import GenerationConfig

    config = GenerationConfig(
        eos_tokens=[128001, 128009],
        max_new_tokens=max_tokens,
        stop_strings=default_stop_strings,
    )

    return StopConditionChecker(config)
