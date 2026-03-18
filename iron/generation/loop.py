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
        # Stores (K, V) tuples for each layer: [num_kv_heads, seq_len, head_dim]
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

        Implements the Llama3.2 transformer layer architecture:
        1. Input RMSNorm -> Attention -> Output projection -> Residual
        2. FFN RMSNorm -> SwiGLU MLP -> Residual

        Args:
            hidden: Input hidden states, shape [seq_len, hidden_size]
            layer_weights: Layer weights (TransformerWeights dataclass)
            layer_idx: Layer index for KV cache
            positions: Token positions
            is_prefill: Whether this is prefill phase

        Returns:
            Output hidden states, shape [seq_len, hidden_size]
        """
        seq_len = hidden.shape[0]

        # =====================
        # ATTENTION BLOCK
        # =====================

        # 1. Input RMSNorm for attention path
        hidden_norm = self._rms_norm(hidden, layer_weights.attn_norm)

        # 2. Compute Q, K, V projections
        # Q: [seq_len, num_heads * head_dim]
        # K: [seq_len, num_kv_heads * head_dim]
        # V: [seq_len, num_kv_heads * head_dim]
        q = hidden_norm @ layer_weights.wq
        k = hidden_norm @ layer_weights.wk
        v = hidden_norm @ layer_weights.wv

        # 3. Reshape for multi-head attention
        num_heads = self.config.num_attention_heads
        num_kv_heads = self.config.num_key_value_heads
        head_dim = self.config.head_dim

        # Q: [seq_len, num_heads, head_dim] -> [num_heads, seq_len, head_dim]
        q = q.reshape(seq_len, num_heads, head_dim).transpose(1, 0, 2)
        # K: [seq_len, num_kv_heads, head_dim] -> [num_kv_heads, seq_len, head_dim]
        k = k.reshape(seq_len, num_kv_heads, head_dim).transpose(1, 0, 2)
        # V: [seq_len, num_kv_heads, head_dim] -> [num_kv_heads, seq_len, head_dim]
        v = v.reshape(seq_len, num_kv_heads, head_dim).transpose(1, 0, 2)

        # 4. Apply RoPE to Q and K
        q, k = self._apply_rope_to_qk(q, k, positions)

        # 5. Compute attention with KV cache
        if is_prefill:
            # Store KV cache for all positions
            self._store_kv_cache(layer_idx, k, v, positions)
            k_full, v_full = k, v
        else:
            # Single token decode - retrieve cached KV
            self._store_kv_cache(layer_idx, k, v, positions)
            k_full, v_full = self._get_full_kv_cache(layer_idx)

        # 6. Scaled dot-product attention
        # Handle GQA (Grouped Query Attention) - repeat KV heads
        if num_heads != num_kv_heads:
            # Repeat K and V for each head group
            n_groups = num_heads // num_kv_heads
            k_full = np.repeat(k_full, n_groups, axis=0)
            v_full = np.repeat(v_full, n_groups, axis=0)

        # Compute attention scores: Q @ K^T / sqrt(head_dim)
        inv_scale = 1.0 / np.sqrt(head_dim)
        attn_scores = np.einsum('nsh,nth->nst', q, k_full) * inv_scale

        # Apply causal mask
        attn_scores = self._apply_causal_mask(attn_scores, positions, is_prefill)

        # Softmax
        attn_weights = self._softmax(attn_scores)

        # Apply attention to values: attn_weights @ V
        # [num_heads, seq_len, kv_seq_len] @ [num_heads, kv_seq_len, head_dim]
        attn_output = np.einsum('nst,nth->nsh', attn_weights, v_full)

        # Transpose back: [num_heads, seq_len, head_dim] -> [seq_len, num_heads * head_dim]
        attn_output = attn_output.transpose(1, 0, 2).reshape(seq_len, num_heads * head_dim)

        # 7. Output projection
        attn_output = attn_output @ layer_weights.wo

        # 8. Residual connection
        hidden = hidden + attn_output

        # =====================
        # MLP BLOCK (SwiGLU)
        # =====================

        # 9. FFN RMSNorm
        hidden_norm = self._rms_norm(hidden, layer_weights.ffn_norm)

        # 10. SwiGLU: SiLU(gate) * up
        # gate = hidden @ w1, up = hidden @ w3
        gate = hidden_norm @ layer_weights.w1
        up = hidden_norm @ layer_weights.w3

        # SiLU activation on gate
        gate_activated = self._silu(gate)

        # Element-wise multiply
        mlp_output = gate_activated * up

        # 11. Down projection
        mlp_output = mlp_output @ layer_weights.w2

        # 12. Final residual connection
        hidden = hidden + mlp_output

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

    def _silu(self, x: np.ndarray) -> np.ndarray:
        """Apply SiLU (Sigmoid Linear Unit) activation.

        SiLU(x) = x * sigmoid(x) = x / (1 + exp(-x))

        Args:
            x: Input array

        Returns:
            Activated output
        """
        return x * (1.0 / (1.0 + np.exp(-x)))

    def _softmax(self, x: np.ndarray) -> np.ndarray:
        """Apply softmax along last axis.

        Args:
            x: Input array

        Returns:
            Softmax output
        """
        # Subtract max for numerical stability
        x_max = np.max(x, axis=-1, keepdims=True)
        exp_x = np.exp(x - x_max)
        return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

    def _apply_causal_mask(
        self,
        attn_scores: np.ndarray,
        positions: List[int],
        is_prefill: bool
    ) -> np.ndarray:
        """Apply causal attention mask.

        Args:
            attn_scores: Attention scores [num_heads, seq_len, kv_seq_len]
            positions: Current positions
            is_prefill: Whether in prefill phase

        Returns:
            Masked attention scores
        """
        num_heads, seq_len, kv_seq_len = attn_scores.shape

        # Create causal mask (upper triangular = -inf)
        mask = np.triu(np.full((seq_len, kv_seq_len), -np.inf), k=1)

        # Apply mask to all heads
        attn_scores = attn_scores + mask

        return attn_scores

    def _apply_rope_to_qk(
        self,
        q: np.ndarray,
        k: np.ndarray,
        positions: List[int]
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Apply Rotary Positional Embedding to Q and K.

        Args:
            q: Query tensor [num_heads, seq_len, head_dim]
            k: Key tensor [num_kv_heads, seq_len, head_dim]
            positions: Token positions

        Returns:
            Rotated Q and K tensors
        """
        num_heads, seq_len, head_dim = q.shape
        num_kv_heads, _, _ = k.shape

        # Compute RoPE angles for each position
        # Using the Llama3.2 RoPE formula with theta_base
        theta_base = self.config.rope_theta
        inv_freq = 1.0 / np.power(theta_base, np.arange(0, head_dim, 2) / head_dim)

        # Compute angles for each position
        angles = np.outer(positions, inv_freq)  # [seq_len, head_dim/2]

        # Compute cos and sin
        cos = np.cos(angles)  # [seq_len, head_dim/2]
        sin = np.sin(angles)  # [seq_len, head_dim/2]

        # Apply RoPE to Q
        q_rotated = self._apply_rope_single(q, cos, sin)

        # Apply RoPE to K
        k_rotated = self._apply_rope_single(k, cos, sin)

        return q_rotated, k_rotated

    def _apply_rope_single(
        self,
        x: np.ndarray,
        cos: np.ndarray,
        sin: np.ndarray
    ) -> np.ndarray:
        """Apply RoPE to a single tensor.

        RoPE formula (two-halves method, Llama3.2 style):
        [x0, x1, ..., x_{d/2-1}, x_{d/2}, ..., x_{d-1}] * cos +
        [-x_{d/2}, ..., -x_{d-1}, x0, ..., x_{d/2-1}] * sin

        Args:
            x: Input tensor [num_heads, seq_len, head_dim]
            cos: Cosine values [seq_len, head_dim/2]
            sin: Sine values [seq_len, head_dim/2]

        Returns:
            Rotated tensor
        """
        num_heads, seq_len, head_dim = x.shape
        half_dim = head_dim // 2

        # Split into first half and second half
        x1 = x[:, :, :half_dim]  # First half
        x2 = x[:, :, half_dim:]  # Second half

        # Expand cos/sin for broadcasting: [seq_len, half_dim] -> [1, seq_len, half_dim]
        cos_expanded = cos[np.newaxis, :, :]
        sin_expanded = sin[np.newaxis, :, :]

        # Apply rotation
        # rotated_first = x1 * cos - x2 * sin
        # rotated_second = x1 * sin + x2 * cos
        rotated_first = x1 * cos_expanded - x2 * sin_expanded
        rotated_second = x1 * sin_expanded + x2 * cos_expanded

        # Concatenate back
        x_rotated = np.concatenate([rotated_first, rotated_second], axis=-1)

        return x_rotated

    def _store_kv_cache(
        self,
        layer_idx: int,
        k: np.ndarray,
        v: np.ndarray,
        positions: List[int]
    ) -> None:
        """Store or update KV cache for a layer.

        Args:
            layer_idx: Layer index
            k: Key tensor [num_kv_heads, seq_len, head_dim]
            v: Value tensor [num_kv_heads, seq_len, head_dim]
            positions: Token positions
        """
        if self._kv_cache is None:
            self._kv_cache = {}

        if layer_idx not in self._kv_cache:
            # Initialize cache for this layer
            self._kv_cache[layer_idx] = (k.copy(), v.copy())
        else:
            # Append to existing cache
            k_cached, v_cached = self._kv_cache[layer_idx]
            k_new = np.concatenate([k_cached, k], axis=1)
            v_new = np.concatenate([v_cached, v], axis=1)
            self._kv_cache[layer_idx] = (k_new, v_new)

    def _get_full_kv_cache(
        self,
        layer_idx: int
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Get full KV cache for a layer.

        Args:
            layer_idx: Layer index

        Returns:
            Tuple of (K, V) tensors [num_kv_heads, cached_seq_len, head_dim]
        """
        if self._kv_cache is None or layer_idx not in self._kv_cache:
            raise RuntimeError(f"KV cache not initialized for layer {layer_idx}")

        return self._kv_cache[layer_idx]

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
