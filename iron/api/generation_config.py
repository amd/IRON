# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Generation configuration for autoregressive inference.

This module provides the GenerationConfig class for configuring
text generation parameters with sensible defaults for Llama3.2 models.

FEATURES:
- Sampling parameters (temperature, top_p, top_k)
- Stopping criteria (EOS tokens, max_length, stop_strings)
- Model-specific defaults
- JSON serialization for API integration
- Parameter validation

EXAMPLE USAGE:
    >>> config = GenerationConfig(
    ...     temperature=0.7,
    ...     max_new_tokens=512,
    ... )
    >>> config.is_eos_token(128001)
    True
    >>> should_stop, reason = config.should_stop(128001, 100)
    >>> assert should_stop and reason == "eos_token"
"""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple
import json


@dataclass
class GenerationConfig:
    """Configuration for text generation.

    This dataclass holds all configuration parameters for autoregressive
    text generation, including sampling parameters, stopping criteria,
    and model-specific settings.

    Attributes:
        # Stopping criteria
        eos_tokens: List of EOS token IDs (model-specific)
        max_new_tokens: Maximum tokens to generate
        max_length: Maximum total sequence length
        stop_strings: Strings that trigger stopping

        # Sampling parameters
        temperature: Sampling temperature (0.0 = greedy)
        top_p: Nucleus sampling threshold
        top_k: Top-k sampling
        repetition_penalty: Penalty for repetition (>1.0 discourages)

        # Performance
        use_cache: Use KV cache for generation
        pad_token_id: Padding token ID

        # Model-specific configuration
        model_type: Model type identifier

    Raises:
        ValueError: If any parameter is out of valid range

    Example:
        >>> config = GenerationConfig(
        ...     model_type="llama3",
        ...     temperature=0.7,
        ...     max_new_tokens=512,
        ... )
        >>> print(config.temperature)
        0.7
    """

    # Stopping criteria
    eos_tokens: Optional[List[int]] = None
    max_new_tokens: int = 2048
    max_length: Optional[int] = None
    stop_strings: Optional[List[str]] = None

    # Sampling parameters
    temperature: float = 0.7
    top_p: float = 0.9
    top_k: int = 50
    repetition_penalty: float = 1.0

    # Performance
    use_cache: bool = True
    pad_token_id: int = 128001  # Llama3.2 default

    # Model-specific configuration
    model_type: str = "llama3"

    def __post_init__(self):
        """Initialize defaults and validate parameters.

        Sets model-specific EOS tokens if not provided and validates
        all parameters are within acceptable ranges.

        Raises:
            ValueError: If any parameter validation fails
        """
        # Set model-specific EOS tokens
        if self.eos_tokens is None:
            if self.model_type == "llama3":
                # Llama3.2 EOS tokens:
                # - 128001: <|end_of_text|>
                # - 128009: <|eot_id|>
                self.eos_tokens = [128001, 128009]
            else:
                self.eos_tokens = [128001]

        # Validate parameters
        self._validate()

    def _validate(self):
        """Validate configuration parameters.

        Checks that all parameters are within their valid ranges:
        - temperature >= 0
        - top_p in [0, 1]
        - top_k >= 1
        - repetition_penalty >= 0
        - max_new_tokens >= 1

        Raises:
            ValueError: If any parameter is out of range
        """
        if self.temperature < 0:
            raise ValueError("temperature must be >= 0")
        if not (0 <= self.top_p <= 1):
            raise ValueError("top_p must be in [0, 1]")
        if self.top_k < 1:
            raise ValueError("top_k must be >= 1")
        if self.repetition_penalty < 0:
            raise ValueError("repetition_penalty must be >= 0")
        if self.max_new_tokens < 1:
            raise ValueError("max_new_tokens must be >= 1")

    def is_eos_token(self, token_id: int) -> bool:
        """Check if token is an EOS token.

        Args:
            token_id: Token ID to check

        Returns:
            True if token_id is in the EOS tokens list

        Example:
            >>> config = GenerationConfig()
            >>> config.is_eos_token(128001)
            True
            >>> config.is_eos_token(500)
            False
        """
        return token_id in self.eos_tokens

    def should_stop(
        self,
        token_id: int,
        current_length: int,
        generated_text: str = ""
    ) -> Tuple[bool, str]:
        """Check if generation should stop.

        Evaluates all stopping criteria in order:
        1. EOS token detection
        2. Maximum length check
        3. Stop string detection

        Args:
            token_id: Current token ID
            current_length: Current sequence length
            generated_text: Generated text so far

        Returns:
            Tuple of (should_stop, reason) where reason is one of:
            - "eos_token": Generation hit an EOS token
            - "max_length": Maximum sequence length reached
            - "stop_string": A stop string was detected
            - "": Generation should continue

        Example:
            >>> config = GenerationConfig(max_length=100)
            >>> should_stop, reason = config.should_stop(500, 100)
            >>> assert should_stop and reason == "max_length"
        """
        # Check EOS tokens
        if self.is_eos_token(token_id):
            return True, "eos_token"

        # Check max length
        if self.max_length is not None and current_length >= self.max_length:
            return True, "max_length"

        # Check stop strings
        if self.stop_strings:
            for stop_str in self.stop_strings:
                if stop_str in generated_text:
                    return True, "stop_string"

        return False, ""

    def to_dict(self) -> dict:
        """Convert configuration to dictionary.

        Returns:
            Dictionary representation of the configuration

        Example:
            >>> config = GenerationConfig(temperature=0.5)
            >>> d = config.to_dict()
            >>> assert d["temperature"] == 0.5
        """
        return {
            "eos_tokens": self.eos_tokens,
            "max_new_tokens": self.max_new_tokens,
            "max_length": self.max_length,
            "stop_strings": self.stop_strings,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "repetition_penalty": self.repetition_penalty,
            "use_cache": self.use_cache,
            "pad_token_id": self.pad_token_id,
            "model_type": self.model_type,
        }

    def to_json(self) -> str:
        """Convert configuration to JSON string.

        Returns:
            JSON string representation of the configuration

        Example:
            >>> config = GenerationConfig(temperature=0.7)
            >>> json_str = config.to_json()
            >>> assert '"temperature": 0.7' in json_str
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict) -> "GenerationConfig":
        """Create configuration from dictionary.

        Args:
            data: Dictionary with configuration values

        Returns:
            New GenerationConfig instance

        Note:
            None values are filtered out to use class defaults

        Example:
            >>> config = GenerationConfig.from_dict({"temperature": 0.5})
            >>> assert config.temperature == 0.5
        """
        # Filter out None values to use defaults
        filtered = {k: v for k, v in data.items() if v is not None}
        return cls(**filtered)

    @classmethod
    def from_json(cls, json_str: str) -> "GenerationConfig":
        """Create configuration from JSON string.

        Args:
            json_str: JSON string with configuration

        Returns:
            New GenerationConfig instance

        Example:
            >>> config = GenerationConfig.from_json('{"temperature": 0.7}')
            >>> assert config.temperature == 0.7
        """
        return cls.from_dict(json.loads(json_str))


#==============================================================================
# Preset Configurations
#==============================================================================

LLAMA3_CONFIG = GenerationConfig(
    model_type="llama3",
    eos_tokens=[128001, 128009],
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    max_new_tokens=2048,
)
"""Standard Llama3 configuration with balanced sampling."""

LLAMA3_GREEDY_CONFIG = GenerationConfig(
    model_type="llama3",
    eos_tokens=[128001, 128009],
    temperature=0.0,  # Greedy decoding
    max_new_tokens=2048,
)
"""Llama3 configuration for deterministic greedy decoding."""

LLAMA3_HIGH_CREATIVE_CONFIG = GenerationConfig(
    model_type="llama3",
    eos_tokens=[128001, 128009],
    temperature=1.0,
    top_p=0.95,
    top_k=100,
    max_new_tokens=4096,
)
"""Llama3 configuration for high creativity/variety output."""
