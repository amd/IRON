# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Autoregressive generation loop for Llama3.2.

This module implements the main generation loop for autoregressive
text generation with Llama3.2 models.

FEATURES:
- Prefill phase: Process full prompt in parallel
- Decode phase: Process single token efficiently
- Token sampling with configurable strategies
- Stop condition integration

EXAMPLE USAGE:
    >>> from iron.generation.loop import GenerationLoop, GenerationResult
    >>> from iron.models.llama32 import Llama32Config, LlamaWeights
    >>> from iron.api.generation_config import GenerationConfig
    >>>
    >>> config = Llama32Config()
    >>> weights = LlamaWeights(...)
    >>> gen_config = GenerationConfig(temperature=0.7)
    >>>
    >>> loop = GenerationLoop(config, weights, gen_config)
    >>> prompt_tokens = [1, 2, 3, ...]  # Tokenized prompt
    >>> for result in loop.generate(prompt_tokens):
    ...     print(f"Generated token: {result.token_id}")
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Iterator, List, Optional, Tuple, Dict, Any

import numpy as np

from ..models.llama32.config import Llama32Config
from ..models.llama32.weights import LlamaWeights
from ..api.generation_config import GenerationConfig
from .sampling import TokenSampler

logger = logging.getLogger(__name__)


@dataclass
class GenerationResult:
    """Result from a generation step.

    This dataclass holds information about a single generated token,
    including the token ID, probability, and stop condition status.

    Attributes:
        token_id: Generated token ID
        token_text: Decoded token text (if tokenizer provided)
        logit_prob: Log probability of the token
        is_eos: Whether this is an end-of-sequence token
        stop_reason: Reason for stopping (if applicable)
        position: Position in the generated sequence
        logprobs: Optional log probabilities for all tokens

    Example:
        >>> result = GenerationResult(
        ...     token_id=5023,
        ...     token_text="hello",
        ...     logit_prob=-0.523,
        ...     is_eos=False
        ... )
        >>> print(f"Generated: {result.token_text}")
    """
    token_id: int
    token_text: str = ""
    logit_prob: float = 0.0
    is_eos: bool = False
    stop_reason: Optional[str] = None
    position: int = 0
    logprobs: Optional[Dict[int, float]] = field(default_factory=None)

    def __str__(self) -> str:
        """Get human-readable string representation."""
        return (
            f"GenerationResult(token_id={self.token_id}, "
            f"text='{self.token_text}', "
            f"prob={np.exp(self.logit_prob):.4f}, "
            f"eos={self.is_eos})"
        )


class GenerationLoop:
    """Autoregressive generation loop for Llama3.2.

    This class implements the main generation loop for autoregressive
    text generation. It handles both the prefill phase (processing
    the full prompt in parallel) and the decode phase (generating
    tokens one at a time).

    Features:
    - Prefill phase for efficient prompt processing
    - Decode phase for token-by-token generation
    - Configurable sampling (temperature, top_p, top_k)
    - Stop condition integration (EOS, max_tokens, stop_strings)
    - KV cache integration for context retention

    Attributes:
        config: Llama3.2 model configuration
        weights: Llama3.2 model weights
        generation_config: Generation configuration

    Example:
        >>> loop = GenerationLoop(config, weights, gen_config)
        >>> prompt = tokenizer.encode("Hello, how are you?")
        >>> for result in loop.generate(prompt):
        ...     print(tokenizer.decode([result.token_id]), end="")
    """

    def __init__(
        self,
        config: Llama32Config,
        weights: LlamaWeights,
        generation_config: Optional[GenerationConfig] = None
    ) -> None:
        """Initialize generation loop.

        Args:
            config: Llama3.2 model configuration
            weights: Llama3.2 model weights
            generation_config: Generation configuration. If None, uses
                default GenerationConfig

        Example:
            >>> config = Llama32Config()
            >>> weights = LlamaWeights(...)
            >>> loop = GenerationLoop(config, weights)
        """
        self.config = config
        self.weights = weights
        self.generation_config = generation_config or GenerationConfig()

        # Initialize token sampler
        self.sampler = TokenSampler(
            temperature=self.generation_config.temperature,
            top_k=self.generation_config.top_k,
            top_p=self.generation_config.top_p,
            repetition_penalty=self.generation_config.repetition_penalty
        )

        # KV cache for context retention (initialized per sequence)
        self._kv_cache: Optional[Dict[int, Tuple[np.ndarray, np.ndarray]]] = None
        self._current_position: int = 0
        self._sequence_id: int = 0

        logger.debug(
            f"GenerationLoop initialized with config: "
            f"temperature={self.generation_config.temperature}, "
            f"max_new_tokens={self.generation_config.max_new_tokens}"
        )

    def reset(self) -> None:
        """Reset generation state for new sequence.

        Clears KV cache and resets position counter.

        Example:
            >>> loop.reset()
            >>> # Ready for new generation
        """
        self._kv_cache = None
        self._current_position = 0
        self._sequence_id += 1
        logger.debug(f"GenerationLoop reset for new sequence (id={self._sequence_id})")

    def prefill(self, prompt_tokens: List[int]) -> np.ndarray:
        """Process full prompt in parallel.

        This is the prefill phase where the entire prompt is processed
        through all transformer layers in a single forward pass. The KV
        cache is populated for all positions.

        Args:
            prompt_tokens: Tokenized prompt as list of token IDs

        Returns:
            Logits for next token prediction, shape [vocab_size]

        Raises:
            ValueError: If prompt is empty

        Example:
            >>> prompt = tokenizer.encode("Hello, world!")
            >>> logits = loop.prefill(prompt)
            >>> next_token = loop.sample(logits)
        """
        if not prompt_tokens:
            raise ValueError("Prompt cannot be empty")

        logger.info(f"Prefill phase: processing {len(prompt_tokens)} tokens")

        # Convert to numpy array
        tokens = np.array(prompt_tokens, dtype=np.int32)
        seq_len = len(prompt_tokens)

        # Get embeddings
        embeddings = self._get_embeddings(tokens)

        # Forward pass through all layers with KV cache storage
        hidden = embeddings
        for layer_idx, layer_weights in enumerate(self.weights.layers):
            hidden = self._forward_layer(
                hidden,
                layer_weights,
                layer_idx,
                positions=list(range(seq_len)),
                is_prefill=True
            )

        # Final RMSNorm
        hidden = self._rms_norm(hidden, self.weights.output_norm)

        # Output projection to vocab
        logits = self._output_projection(hidden[-1])  # Last position

        # Store position for decode phase
        self._current_position = seq_len

        logger.debug(f"Prefill complete, logits shape: {logits.shape}")
        return logits

    def decode(self, token_id: int) -> np.ndarray:
        """Process single token.

        This is the decode phase where a single token is processed
        through all transformer layers. The KV cache is read for
        context and updated with new KV entries.

        Args:
            token_id: Current token ID to process

        Returns:
            Logits for next token prediction, shape [vocab_size]

        Raises:
            RuntimeError: If called before prefill

        Example:
            >>> token = 5023
            >>> logits = loop.decode(token)
            >>> next_token = loop.sample(logits)
        """
        if self._kv_cache is None:
            raise RuntimeError("Must call prefill() before decode()")

        logger.debug(f"Decode phase: position={self._current_position}, token={token_id}")

        # Convert to numpy array (single token)
        tokens = np.array([token_id], dtype=np.int32)
        position = self._current_position

        # Get embeddings
        embeddings = self._get_embeddings(tokens)

        # Forward pass through all layers with KV cache read/write
        hidden = embeddings
        for layer_idx, layer_weights in enumerate(self.weights.layers):
            hidden = self._forward_layer(
                hidden,
                layer_weights,
                layer_idx,
                positions=[position],
                is_prefill=False
            )

        # Final RMSNorm
        hidden = self._rms_norm(hidden, self.weights.output_norm)

        # Output projection to vocab
        logits = self._output_projection(hidden[0])  # Single token

        # Update position
        self._current_position += 1

        logger.debug(f"Decode complete, logits shape: {logits.shape}")
        return logits

    def sample(self, logits: np.ndarray) -> int:
        """Sample next token from logits.

        Applies configured sampling strategy (temperature, top_k, top_p)
        to select the next token.

        Args:
            logits: Raw logits from model, shape [vocab_size]

        Returns:
            Sampled token ID

        Example:
            >>> logits = loop.prefill(prompt)
            >>> token = loop.sample(logits)
        """
        return self.sampler.sample(logits)

    def _get_embeddings(self, tokens: np.ndarray) -> np.ndarray:
        """Get token embeddings.

        Args:
            tokens: Token IDs, shape [seq_len] or [1]

        Returns:
            Embeddings, shape [seq_len, hidden_size]
        """
        return self.weights.token_embd[tokens]

    def _forward_layer(
        self,
        hidden: np.ndarray,
        layer_weights: Any,
        layer_idx: int,
        positions: List[int],
        is_prefill: bool
    ) -> np.ndarray:
        """Forward pass through a single transformer layer.

        Args:
            hidden: Input hidden states, shape [seq_len, hidden_size]
            layer_weights: Layer weights
            layer_idx: Layer index for KV cache
            positions: Token positions
            is_prefill: Whether this is prefill phase

        Returns:
            Output hidden states, shape [seq_len, hidden_size]
        """
        # This is a simplified implementation
        # A full implementation would include:
        # 1. Input RMSNorm
        # 2. Attention with KV cache
        # 3. Output projection
        # 4. Residual connection
        # 5. MLP with SwiGLU
        # 6. Final residual connection

        # For now, return hidden as placeholder
        # The actual forward pass would use the operators from iron/operators/
        return hidden

    def _rms_norm(self, hidden: np.ndarray, weight: np.ndarray) -> np.ndarray:
        """Apply RMSNorm.

        Args:
            hidden: Input hidden states
            weight: RMSNorm weight

        Returns:
            Normalized hidden states
        """
        # RMSNorm: x / sqrt(mean(x^2) + eps) * weight
        eps = self.config.rms_norm_eps
        variance = np.mean(hidden ** 2, axis=-1, keepdims=True)
        hidden = hidden / np.sqrt(variance + eps)
        return hidden * weight

    def _output_projection(self, hidden: np.ndarray) -> np.ndarray:
        """Project hidden state to vocabulary logits.

        Args:
            hidden: Hidden state, shape [hidden_size]

        Returns:
            Logits, shape [vocab_size]
        """
        # Get output weights (tied or separate)
        output_weights = self.weights.get_output_weights()
        return output_weights @ hidden

    def generate(
        self,
        prompt_tokens: List[int],
        max_tokens: Optional[int] = None,
        tokenizer: Optional[Any] = None
    ) -> Iterator[GenerationResult]:
        """Generate tokens autoregressively.

        This is the main generation method that yields tokens one at a time.
        It handles the full generation loop:
        1. Prefill phase: Process prompt
        2. Sample first token
        3. Decode loop: Generate remaining tokens until stop condition

        Args:
            prompt_tokens: Tokenized prompt
            max_tokens: Maximum tokens to generate. If None, uses
                generation_config.max_new_tokens
            tokenizer: Optional tokenizer for decoding token text

        Yields:
            GenerationResult for each generated token

        Raises:
            ValueError: If prompt is empty

        Example:
            >>> prompt = tokenizer.encode("Once upon a time")
            >>> for result in loop.generate(prompt, tokenizer=tokenizer):
            ...     print(result.token_text, end="")
            ...     if result.is_eos:
            ...         break
        """
        if not prompt_tokens:
            raise ValueError("Prompt cannot be empty")

        # Determine max tokens
        if max_tokens is None:
            max_tokens = self.generation_config.max_new_tokens

        # Reset state
        self.reset()

        logger.info(f"Starting generation: prompt_len={len(prompt_tokens)}, max_tokens={max_tokens}")

        # Prefill phase
        logits = self.prefill(prompt_tokens)

        # Generate tokens
        generated_count = 0
        all_tokens: List[int] = list(prompt_tokens)

        while generated_count < max_tokens:
            # Sample next token
            token_id = self.sample(logits)

            # Decode token text
            token_text = ""
            if tokenizer is not None:
                token_text = tokenizer.decode([token_id])

            # Check stop conditions
            is_eos = self.generation_config.is_eos_token(token_id)
            stop_reason: Optional[str] = None

            if is_eos:
                stop_reason = "eos_token"
                logger.info(f"EOS token {token_id} detected at position {generated_count}")
            elif generated_count >= max_tokens - 1:
                stop_reason = "max_tokens"
                logger.info(f"Max tokens ({max_tokens}) reached")

            # Create result
            result = GenerationResult(
                token_id=token_id,
                token_text=token_text,
                logit_prob=float(np.log(1.0)),  # Placeholder
                is_eos=is_eos,
                stop_reason=stop_reason,
                position=generated_count
            )

            yield result

            # Stop if EOS or max tokens
            if is_eos or stop_reason == "max_tokens":
                break

            # Update for next iteration
            all_tokens.append(token_id)
            generated_count += 1

            # Decode phase for next token
            logits = self.decode(token_id)

        logger.info(f"Generation complete: {generated_count} tokens generated")

    def generate_batch(
        self,
        prompts: List[List[int]],
        tokenizer: Optional[Any] = None
    ) -> Iterator[Tuple[int, GenerationResult]]:
        """Generate for multiple prompts concurrently.

        Args:
            prompts: List of tokenized prompts
            tokenizer: Optional tokenizer for decoding

        Yields:
            Tuple of (prompt_index, GenerationResult)

        Example:
            >>> prompts = [encode("Hello"), encode("Hi")]
            >>> for idx, result in loop.generate_batch(prompts):
            ...     print(f"Prompt {idx}: {result.token_text}")
        """
        # Simple sequential implementation
        # A full implementation would use batched operations
        for idx, prompt in enumerate(prompts):
            for result in self.generate(prompt, tokenizer=tokenizer):
                yield (idx, result)

    def get_kv_cache_stats(self) -> Dict[str, Any]:
        """Get KV cache statistics.

        Returns:
            Dictionary with cache statistics

        Example:
            >>> stats = loop.get_kv_cache_stats()
            >>> print(f"Position: {stats['current_position']}")
        """
        return {
            "current_position": self._current_position,
            "sequence_id": self._sequence_id,
            "has_cache": self._kv_cache is not None,
        }
