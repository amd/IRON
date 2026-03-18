# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""KV cache management for autoregressive generation.

This module provides the KVCacheManager class for managing KV cache
during token-by-token generation.

FEATURES:
- Per-sequence KV cache management
- Block allocation and deallocation
- KV entry write/read operations
- Sequence state tracking
- Memory-efficient caching

ARCHITECTURE:
The KVCacheManager wraps the C++ PagedKVCache to provide Python-level
abstraction for managing KV state during generation.

EXAMPLE USAGE:
    >>> from iron.generation.kv_manager import KVCacheManager
    >>> from iron.runtime import PagedKVCache
    >>> from iron.models.llama32 import Llama32Config
    >>>
    >>> # Create KV cache
    >>> kv_cache = PagedKVCache(config)
    >>> manager = KVCacheManager(kv_cache, config)
    >>>
    >>> # Start sequence
    >>> seq_id = manager.start_sequence(prompt_length=100)
    >>>
    >>> # Write KV entries
    >>> manager.write_kv(seq_id, position=100, key=key_vec, value=value_vec, layer=0)
    >>>
    >>> # Read KV context
    >>> keys, values = manager.read_kv_context(seq_id, context_length=100, layer=0)
    >>>
    >>> # End sequence
    >>> manager.end_sequence(seq_id)

CLASSES:
    KVCacheManager: Main KV cache management class
    SequenceInfo: Sequence state information

Author: Jordan Lee
Version: 1.0.0
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any

import numpy as np

from ..models.llama32.config import Llama32Config

logger = logging.getLogger(__name__)


@dataclass
class SequenceInfo:
    """Information about a generation sequence.

    This dataclass tracks the state of a single generation sequence,
    including allocated KV blocks and generated tokens.

    Attributes:
        sequence_id: Unique sequence identifier
        kv_blocks: List of allocated KV block IDs
        current_length: Current sequence length (prompt + generated)
        prompt_length: Original prompt length
        generated_tokens: List of generated token IDs
        is_complete: Whether generation is finished
        created_at: Timestamp when sequence started
        updated_at: Timestamp of last update

    Example:
        >>> info = SequenceInfo(
        ...     sequence_id=1,
        ...     kv_blocks=[0, 1, 2],
        ...     current_length=103,
        ...     prompt_length=100
        ... )
    """

    sequence_id: int
    kv_blocks: List[int] = field(default_factory=list)
    current_length: int = 0
    prompt_length: int = 0
    generated_tokens: List[int] = field(default_factory=list)
    is_complete: bool = False
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)

    @property
    def num_generated(self) -> int:
        """Get number of generated tokens."""
        return len(self.generated_tokens)

    @property
    def total_blocks(self) -> int:
        """Get total number of allocated blocks."""
        return len(self.kv_blocks)

    def update_timestamp(self) -> None:
        """Update the last modified timestamp."""
        self.updated_at = time.time()

    def __str__(self) -> str:
        """Get human-readable string representation."""
        return (
            f"SequenceInfo(id={self.sequence_id}, "
            f"length={self.current_length}, "
            f"generated={self.num_generated}, "
            f"blocks={self.total_blocks})"
        )


class KVCacheManager:
    """Manages KV cache during autoregressive generation.

    This class provides high-level KV cache management for token-by-token
    generation. It handles:
    - Sequence lifecycle (start, update, end)
    - KV block allocation and deallocation
    - KV entry write and read operations
    - Memory tracking and cleanup

    The manager supports multiple concurrent sequences, each with its
    own KV cache allocation.

    Attributes:
        config: Llama3.2 model configuration
        block_size: Tokens per KV block

    Example:
        >>> manager = KVCacheManager(config)
        >>> seq_id = manager.start_sequence(prompt_tokens)
        >>> manager.write_kv(seq_id, position, key, value, layer)
        >>> keys, values = manager.read_kv_context(seq_id, layer)
    """

    def __init__(
        self,
        config: Llama32Config,
        max_sequences: int = 16,
        max_blocks_per_sequence: int = 1024,
    ) -> None:
        """Initialize KV cache manager.

        Args:
            config: Llama3.2 model configuration
            max_sequences: Maximum concurrent sequences
            max_blocks_per_sequence: Maximum blocks per sequence

        Example:
            >>> config = Llama32Config()
            >>> manager = KVCacheManager(config, max_sequences=8)
        """
        self.config = config
        self.max_sequences = max_sequences
        self.max_blocks_per_sequence = max_blocks_per_sequence

        # Sequence tracking
        self.sequences: Dict[int, SequenceInfo] = {}
        self._next_sequence_id: int = 1

        # KV cache storage (Python implementation)
        # Structure: {layer_id: {block_id: {offset: (key, value)}}}
        self._kv_cache: Dict[
            int, Dict[int, Dict[int, Tuple[np.ndarray, np.ndarray]]]
        ] = {}

        # Block allocation tracking
        self._allocated_blocks: set[int] = set()
        self._block_to_sequence: Dict[int, int] = {}  # block_id -> sequence_id

        # Statistics
        self._total_allocations: int = 0
        self._total_deallocations: int = 0
        self._peak_blocks: int = 0

        logger.debug(
            f"KVCacheManager initialized: max_sequences={max_sequences}, "
            f"max_blocks={max_blocks_per_sequence}"
        )

    def start_sequence(
        self, prompt_tokens: List[int], max_new_tokens: Optional[int] = None
    ) -> int:
        """Start a new generation sequence.

        Allocates KV blocks for the sequence and initializes tracking.

        Args:
            prompt_tokens: Input prompt token IDs
            max_new_tokens: Maximum new tokens to generate. If None,
                uses config.max_position_embeddings

        Returns:
            Unique sequence ID

        Raises:
            RuntimeError: If maximum sequences reached
            MemoryError: If insufficient blocks available

        Example:
            >>> prompt = tokenizer.encode("Hello, world!")
            >>> seq_id = manager.start_sequence(prompt)
        """
        if len(self.sequences) >= self.max_sequences:
            raise RuntimeError(f"Maximum sequences ({self.max_sequences}) reached")

        # Generate unique sequence ID
        sequence_id = self._generate_sequence_id()

        # Calculate required blocks
        prompt_length = len(prompt_tokens)
        if max_new_tokens is None:
            max_new_tokens = self.config.max_position_embeddings

        total_tokens = prompt_length + max_new_tokens
        num_blocks = self._calculate_blocks_needed(total_tokens)

        # Allocate blocks
        allocated_blocks = self._allocate_blocks(num_blocks)

        if len(allocated_blocks) < num_blocks:
            raise MemoryError(
                f"Could not allocate enough blocks: needed {num_blocks}, "
                f"got {len(allocated_blocks)}"
            )

        # Create sequence info
        self.sequences[sequence_id] = SequenceInfo(
            sequence_id=sequence_id,
            kv_blocks=allocated_blocks,
            current_length=prompt_length,
            prompt_length=prompt_length,
        )

        # Initialize KV cache structure for all layers
        for layer_idx in range(self.config.num_hidden_layers):
            if layer_idx not in self._kv_cache:
                self._kv_cache[layer_idx] = {}
            for block_id in allocated_blocks:
                self._kv_cache[layer_idx][block_id] = {}

        logger.info(
            f"Started sequence {sequence_id}: prompt_len={prompt_length}, "
            f"blocks={len(allocated_blocks)}"
        )

        return sequence_id

    def write_kv(
        self,
        sequence_id: int,
        position: int,
        key: np.ndarray,
        value: np.ndarray,
        layer: int,
    ) -> None:
        """Write KV entry for a token.

        Stores the key and value vectors for a specific token position
        in the KV cache.

        Args:
            sequence_id: Sequence ID
            position: Token position in sequence
            key: Key vector, shape [num_heads, head_dim] or [head_dim]
            value: Value vector, shape [num_heads, head_dim] or [head_dim]
            layer: Layer index (0 to num_layers-1)

        Raises:
            ValueError: If sequence not found or layer invalid
            IndexError: If position is out of range

        Example:
            >>> key = np.random.randn(config.num_attention_heads, config.head_dim)
            >>> value = np.random.randn(config.num_attention_heads, config.head_dim)
            >>> manager.write_kv(seq_id, position=100, key=key, value=value, layer=0)
        """
        if sequence_id not in self.sequences:
            raise ValueError(f"Unknown sequence {sequence_id}")

        if layer < 0 or layer >= self.config.num_hidden_layers:
            raise ValueError(
                f"Invalid layer {layer}, must be in [0, {self.config.num_hidden_layers - 1}]"
            )

        seq_info = self.sequences[sequence_id]

        # Find block for this position
        block_index = (
            position // self.config.block_size
            if hasattr(self.config, "block_size")
            else position // 32
        )
        block_offset = (
            position % self.config.block_size
            if hasattr(self.config, "block_size")
            else position % 32
        )

        if block_index >= len(seq_info.kv_blocks):
            raise IndexError(
                f"Position {position} exceeds allocated blocks "
                f"(block_index={block_index}, total_blocks={len(seq_info.kv_blocks)})"
            )

        block_id = seq_info.kv_blocks[block_index]

        # Ensure layer cache exists
        if layer not in self._kv_cache:
            self._kv_cache[layer] = {}
        if block_id not in self._kv_cache[layer]:
            self._kv_cache[layer][block_id] = {}

        # Store KV entry
        self._kv_cache[layer][block_id][block_offset] = (key.copy(), value.copy())

        logger.debug(
            f"Wrote KV: seq={sequence_id}, layer={layer}, "
            f"block={block_id}, offset={block_offset}"
        )

    def read_kv(
        self, sequence_id: int, position: int, layer: int
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Read KV entry for a specific token.

        Retrieves the key and value vectors for a specific token position.

        Args:
            sequence_id: Sequence ID
            position: Token position in sequence
            layer: Layer index

        Returns:
            Tuple of (key, value) vectors

        Raises:
            ValueError: If sequence not found
            KeyError: If KV entry not found

        Example:
            >>> key, value = manager.read_kv(seq_id, position=100, layer=0)
        """
        if sequence_id not in self.sequences:
            raise ValueError(f"Unknown sequence {sequence_id}")

        seq_info = self.sequences[sequence_id]

        # Find block for this position
        block_index = (
            position // self.config.block_size
            if hasattr(self.config, "block_size")
            else position // 32
        )
        block_offset = (
            position % self.config.block_size
            if hasattr(self.config, "block_size")
            else position % 32
        )

        if block_index >= len(seq_info.kv_blocks):
            raise KeyError(
                f"No KV entry at position {position} "
                f"(block_index={block_index} >= total_blocks={len(seq_info.kv_blocks)})"
            )

        block_id = seq_info.kv_blocks[block_index]

        # Retrieve KV entry
        if layer not in self._kv_cache:
            raise KeyError(f"Layer {layer} not initialized")
        if block_id not in self._kv_cache.get(layer, {}):
            raise KeyError(f"Block {block_id} not found in layer {layer}")
        if block_offset not in self._kv_cache[layer][block_id]:
            raise KeyError(f"No KV entry at block {block_id}, offset {block_offset}")

        key, value = self._kv_cache[layer][block_id][block_offset]
        return key.copy(), value.copy()

    def read_kv_context(
        self, sequence_id: int, context_length: int, layer: int
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Read KV context for attention computation.

        Retrieves KV entries for multiple consecutive tokens, suitable
        for attention computation.

        Args:
            sequence_id: Sequence ID
            context_length: Number of tokens to read
            layer: Layer index

        Returns:
            Tuple of (keys, values) with shape [context_length, num_heads, head_dim]

        Raises:
            ValueError: If sequence not found or context_length invalid

        Example:
            >>> keys, values = manager.read_kv_context(seq_id, context_length=100, layer=0)
            >>> # keys shape: [100, num_heads, head_dim]
        """
        if sequence_id not in self.sequences:
            raise ValueError(f"Unknown sequence {sequence_id}")

        seq_info = self.sequences[sequence_id]
        current_pos = seq_info.current_length

        # Validate context length
        if context_length <= 0:
            raise ValueError("context_length must be positive")
        if context_length > current_pos:
            logger.warning(
                f"Context length {context_length} > current position {current_pos}, "
                f"clamping to {current_pos}"
            )
            context_length = current_pos

        # Determine start position
        start_pos = current_pos - context_length

        # Calculate number of heads and head dim
        num_heads = self.config.num_attention_heads
        head_dim = self.config.head_dim

        # Allocate output arrays
        keys = np.zeros((context_length, num_heads, head_dim), dtype=np.float32)
        values = np.zeros((context_length, num_heads, head_dim), dtype=np.float32)

        # Read each position
        for i in range(context_length):
            position = start_pos + i
            try:
                key, value = self.read_kv(sequence_id, position, layer)
                # Handle different key shapes
                if key.ndim == 1:
                    # Shape [head_dim] - single head, need to broadcast
                    key = key.reshape(1, head_dim)
                elif key.ndim == 2 and key.shape[0] == num_heads:
                    # Shape [num_heads, head_dim] - correct
                    pass
                else:
                    logger.warning(f"Unexpected key shape: {key.shape}")

                keys[i] = key
                values[i] = value
            except KeyError:
                # Entry not found - leave as zeros
                logger.debug(f"KV entry not found at position {position}")

        return keys, values

    def append_token(
        self,
        sequence_id: int,
        token_id: int,
        key: np.ndarray,
        value: np.ndarray,
        layer: Optional[int] = None,
    ) -> None:
        """Append a generated token to the sequence.

        Convenience method that updates sequence state and optionally
        writes KV entries for all layers.

        Args:
            sequence_id: Sequence ID
            token_id: Generated token ID
            key: Key vector (for single layer)
            value: Value vector (for single layer)
            layer: Layer index. If None, only updates token list

        Example:
            >>> token = sampler.sample(logits)
            >>> manager.append_token(seq_id, token, key, value, layer=0)
        """
        if sequence_id not in self.sequences:
            raise ValueError(f"Unknown sequence {sequence_id}")

        seq_info = self.sequences[sequence_id]
        position = seq_info.current_length

        # Update sequence state
        seq_info.generated_tokens.append(token_id)
        seq_info.current_length += 1
        seq_info.update_timestamp()

        # Write KV if layer specified
        if layer is not None:
            self.write_kv(sequence_id, position, key, value, layer)

        logger.debug(
            f"Appended token {token_id} to sequence {sequence_id} "
            f"at position {position}"
        )

    def end_sequence(self, sequence_id: int) -> None:
        """End a sequence and free resources.

        Releases all KV blocks allocated to the sequence.

        Args:
            sequence_id: Sequence ID to end

        Raises:
            ValueError: If sequence not found

        Example:
            >>> manager.end_sequence(seq_id)
        """
        if sequence_id not in self.sequences:
            logger.warning(f"Cannot end unknown sequence {sequence_id}")
            return

        seq_info = self.sequences[sequence_id]

        # Free allocated blocks
        for block_id in seq_info.kv_blocks:
            self._free_block(block_id)

        # Remove sequence
        del self.sequences[sequence_id]

        logger.info(f"Ended sequence {sequence_id}")

    def get_sequence_info(self, sequence_id: int) -> SequenceInfo:
        """Get information about a sequence.

        Args:
            sequence_id: Sequence ID

        Returns:
            SequenceInfo for the sequence

        Raises:
            ValueError: If sequence not found

        Example:
            >>> info = manager.get_sequence_info(seq_id)
            >>> print(f"Generated {info.num_generated} tokens")
        """
        if sequence_id not in self.sequences:
            raise ValueError(f"Unknown sequence {sequence_id}")
        return self.sequences[sequence_id]

    def get_all_sequences(self) -> List[int]:
        """Get all active sequence IDs.

        Returns:
            List of active sequence IDs

        Example:
            >>> active = manager.get_all_sequences()
        """
        return list(self.sequences.keys())

    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics.

        Returns:
            Dictionary with cache statistics

        Example:
            >>> stats = manager.get_stats()
            >>> print(f"Active sequences: {stats['active_sequences']}")
            >>> print(f"Allocated blocks: {stats['allocated_blocks']}")
        """
        return {
            "active_sequences": len(self.sequences),
            "allocated_blocks": len(self._allocated_blocks),
            "total_allocations": self._total_allocations,
            "total_deallocations": self._total_deallocations,
            "peak_blocks": self._peak_blocks,
            "block_utilization": (
                len(self._allocated_blocks)
                / (self.max_sequences * self.max_blocks_per_sequence)
                if self.max_sequences * self.max_blocks_per_sequence > 0
                else 0.0
            ),
        }

    def clear(self) -> None:
        """Clear all sequences and free all resources.

        Example:
            >>> manager.clear()
        """
        # End all sequences
        sequence_ids = list(self.sequences.keys())
        for seq_id in sequence_ids:
            self.end_sequence(seq_id)

        # Clear cache
        self._kv_cache.clear()

        logger.info("KVCacheManager cleared")

    def _generate_sequence_id(self) -> int:
        """Generate unique sequence ID.

        Returns:
            Unique sequence ID
        """
        seq_id = self._next_sequence_id
        self._next_sequence_id += 1
        return seq_id

    def _calculate_blocks_needed(self, num_tokens: int) -> int:
        """Calculate number of blocks needed for tokens.

        Args:
            num_tokens: Number of tokens

        Returns:
            Number of blocks required
        """
        block_size = (
            self.config.block_size if hasattr(self.config, "block_size") else 32
        )
        return (num_tokens + block_size - 1) // block_size

    def _allocate_blocks(self, num_blocks: int) -> List[int]:
        """Allocate blocks from the pool.

        Args:
            num_blocks: Number of blocks to allocate

        Returns:
            List of allocated block IDs
        """
        allocated = []
        block_id = 0

        while len(allocated) < num_blocks:
            if block_id not in self._allocated_blocks:
                self._allocated_blocks.add(block_id)
                allocated.append(block_id)
                self._block_to_sequence[block_id] = -1  # Will be set by caller
            block_id += 1

        self._total_allocations += len(allocated)
        self._peak_blocks = max(self._peak_blocks, len(self._allocated_blocks))

        logger.debug(f"Allocated {len(allocated)} blocks: {allocated}")
        return allocated

    def _free_block(self, block_id: int) -> None:
        """Free a single block.

        Args:
            block_id: Block ID to free
        """
        if block_id in self._allocated_blocks:
            self._allocated_blocks.remove(block_id)
            self._total_deallocations += 1

            # Remove from sequence mapping
            if block_id in self._block_to_sequence:
                del self._block_to_sequence[block_id]

            # Clear KV cache for this block
            for layer_cache in self._kv_cache.values():
                if block_id in layer_cache:
                    del layer_cache[block_id]

            logger.debug(f"Freed block {block_id}")

    def __len__(self) -> int:
        """Get number of active sequences."""
        return len(self.sequences)

    def __contains__(self, sequence_id: int) -> bool:
        """Check if sequence exists."""
        return sequence_id in self.sequences

    def __repr__(self) -> str:
        """Get string representation."""
        stats = self.get_stats()
        return (
            f"KVCacheManager(sequences={stats['active_sequences']}, "
            f"blocks={stats['allocated_blocks']}, "
            f"peak={stats['peak_blocks']})"
        )
