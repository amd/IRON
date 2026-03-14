# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Shape Manager for NPU Operations

This module handles NPU-specific shape calculations, padding requirements,
tiling configurations, and memory layout transformations for efficient
execution on AMD Ryzen AI NPUs.
"""

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Union


@dataclass
class TilingConfig:
    """Configuration for matrix tiling on NPU"""

    # Tile dimensions for GEMM operations
    tile_m: int = 64  # Row tile size
    tile_k: int = 64  # Reduction dimension tile size
    tile_n: int = 64  # Column tile size

    # Number of AIE columns to use (1, 2, 4, or 8 for NPU2)
    num_aie_columns: int = 8

    # Minimum tile sizes based on NPU microkernel
    min_tile_m: int = 8
    min_tile_k: int = 8
    min_tile_n: int = 8

    @property
    def min_M(self) -> int:
        """Minimum M dimension (tiles * rows)"""
        return self.tile_m * 4  # 4 AIE rows

    @property
    def min_K(self) -> int:
        """Minimum K dimension"""
        return self.tile_k

    @property
    def min_N(self) -> int:
        """Minimum N dimension (tiles * columns)"""
        return self.tile_n * self.num_aie_columns


@dataclass
class PaddedShape:
    """Represents a padded tensor shape for NPU"""

    original_shape: Tuple[int, ...]
    padded_shape: Tuple[int, ...]
    padding: Dict[str, int] = field(default_factory=dict)
    reason: str = ""

    @property
    def is_padded(self) -> bool:
        """Whether any padding was applied"""
        return self.original_shape != self.padded_shape


class ShapeManager:
    """
    Manages NPU-specific shape calculations and padding requirements.

    The AMD Ryzen AI NPU has specific requirements for tensor dimensions:
    - GEMM operations require dimensions to be multiples of tile sizes
    - AIE array has 4 rows x 8 columns (NPU2) or 4 rows x 4 columns (NPU1)
    - Memory access patterns must align with ObjectFIFO configurations

    This class handles all the necessary calculations for:
    - Padding input tensors to meet NPU requirements
    - Computing optimal tile sizes for given problem dimensions
    - Managing KV cache buffer sizes
    - Handling batch and sequence dimension variations
    """

    # NPU hardware constraints
    NPU2_NUM_ROWS = 4
    NPU2_NUM_COLS = 8
    NPU1_NUM_ROWS = 4
    NPU1_NUM_COLS = 4

    # Default tile sizes for different operations
    DEFAULT_GEMM_TILES = {"tile_m": 64, "tile_k": 64, "tile_n": 64}
    DEFAULT_GEMV_TILES = {"tile_m": 1, "tile_k": 64, "tile_n": 64}

    def __init__(
        self,
        hidden_size: int,
        num_attention_heads: int,
        num_kv_heads: Optional[int] = None,
        num_aie_columns: int = 8,
        tiling_config: Optional[TilingConfig] = None,
    ):
        """
        Initialize the shape manager.

        Args:
            hidden_size: Model hidden dimension
            num_attention_heads: Number of attention heads
            num_kv_heads: Number of KV heads (for GQA), defaults to num_attention_heads
            num_aie_columns: Number of AIE columns to utilize
            tiling_config: Optional custom tiling configuration
        """
        self.hidden_size = hidden_size
        self.num_attention_heads = num_attention_heads
        self.num_kv_heads = num_kv_heads or num_attention_heads
        self.num_aie_columns = min(num_aie_columns, self.NPU2_NUM_COLS)

        # Calculate derived dimensions
        self.head_dim = hidden_size // num_attention_heads

        # Tiling configuration
        if tiling_config:
            self.tiling_config = tiling_config
        else:
            self.tiling_config = TilingConfig(
                num_aie_columns=self.num_aie_columns,
                **self.DEFAULT_GEMM_TILES,
            )

        # Cache for computed shapes
        self._shape_cache: Dict[str, PaddedShape] = {}

    def pad_to_multiple(self, value: int, multiple: int) -> int:
        """Pad a value to the next multiple"""
        if value % multiple == 0:
            return value
        return ((value + multiple - 1) // multiple) * multiple

    def calculate_padded_gemm_shape(
        self,
        M: int,
        K: int,
        N: int,
        partition_N: int = 1,
    ) -> PaddedShape:
        """
        Calculate padded dimensions for GEMM operation.

        Args:
            M: Input matrix rows
            K: Reduction dimension
            N: Output matrix columns
            partition_N: Number of partitions for N dimension

        Returns:
            PaddedShape with computed dimensions
        """
        tc = self.tiling_config

        # Calculate minimum dimensions based on tiling
        min_M = tc.tile_m * self.NPU2_NUM_ROWS
        min_K = tc.tile_k
        min_N = tc.tile_n * tc.num_aie_columns

        # Account for N partitioning
        if partition_N > 1:
            assert (
                N % partition_N == 0
            ), f"N ({N}) must be divisible by partition_N ({partition_N})"
            min_N_per_partition = min_N // partition_N
        else:
            min_N_per_partition = min_N

        # Calculate padded dimensions
        M_padded = self.pad_to_multiple(M, min_M)
        K_padded = self.pad_to_multiple(K, min_K)
        N_padded = self.pad_to_multiple(N // partition_N, min_N_per_partition) * partition_N

        original = (M, K, N)
        padded = (M_padded, K_padded, N_padded)

        padding = {
            "M": M_padded - M,
            "K": K_padded - K,
            "N": N_padded - N,
        }

        reason = self._get_padding_reason("GEMM", padding)

        return PaddedShape(
            original_shape=original,
            padded_shape=padded,
            padding=padding,
            reason=reason,
        )

    def calculate_attention_shape(
        self,
        batch_size: int,
        seq_len: int,
        is_decode: bool = False,
    ) -> Dict[str, PaddedShape]:
        """
        Calculate shapes for attention operation components.

        Args:
            batch_size: Batch dimension
            seq_len: Sequence length
            is_decode: Whether this is for decode phase (seq_len=1)

        Returns:
            Dictionary with shapes for Q, K, V projections and output
        """
        hs = self.hidden_size
        nh = self.num_attention_heads
        nkv = self.num_kv_heads
        hd = self.head_dim

        shapes = {}

        if is_decode:
            # Decode phase: single token
            # Q: (batch, hidden_size) -> (batch, nh, hd)
            shapes["q_proj"] = self.calculate_padded_gemm_shape(
                batch_size * seq_len, hs, hs
            )

            # K/V: For GQA, project to (batch, nkv, hd)
            shapes["k_proj"] = self.calculate_padded_gemm_shape(
                batch_size * seq_len, hs, nkv * hd
            )
            shapes["v_proj"] = self.calculate_padded_gemm_shape(
                batch_size * seq_len, hs, nkv * hd
            )

            # Output projection
            shapes["o_proj"] = self.calculate_padded_gemm_shape(
                batch_size * seq_len, hs, hs
            )
        else:
            # Prefill phase: full sequence
            total_tokens = batch_size * seq_len

            shapes["q_proj"] = self.calculate_padded_gemm_shape(total_tokens, hs, hs)
            shapes["k_proj"] = self.calculate_padded_gemm_shape(
                total_tokens, hs, nkv * hd
            )
            shapes["v_proj"] = self.calculate_padded_gemm_shape(
                total_tokens, hs, nkv * hd
            )
            shapes["o_proj"] = self.calculate_padded_gemm_shape(total_tokens, hs, hs)

        return shapes

    def calculate_ffn_shape(
        self,
        batch_size: int,
        seq_len: int,
        intermediate_size: int,
        is_decode: bool = False,
    ) -> Dict[str, PaddedShape]:
        """
        Calculate shapes for feed-forward network.

        Args:
            batch_size: Batch dimension
            seq_len: Sequence length
            intermediate_size: FFN intermediate dimension
            is_decode: Whether this is for decode phase

        Returns:
            Dictionary with shapes for FFN weights
        """
        tokens = batch_size * seq_len if not is_decode else batch_size

        shapes = {}

        # Gate/Up projections (typically together for SwiGLU)
        shapes["gate_up"] = self.calculate_padded_gemm_shape(
            tokens, self.hidden_size, intermediate_size * 2
        )

        # Down projection
        shapes["down"] = self.calculate_padded_gemm_shape(
            tokens, intermediate_size, self.hidden_size
        )

        return shapes

    def calculate_kv_cache_size(
        self,
        max_seq_len: int,
        batch_size: int = 1,
    ) -> Dict[str, int]:
        """
        Calculate KV cache buffer sizes.

        Args:
            max_seq_len: Maximum sequence length to cache
            batch_size: Batch size

        Returns:
            Dictionary with cache sizes in elements (not bytes)
        """
        nkv = self.num_kv_heads
        hd = self.head_dim

        # KV cache shape: (batch, n_kv_heads, seq_len, head_dim)
        # Stored as: (batch, seq_len, n_kv_heads, head_dim) for efficient access
        cache_elements = batch_size * max_seq_len * nkv * hd

        return {
            "k_cache_elements": cache_elements,
            "v_cache_elements": cache_elements,
            "k_cache_bytes": cache_elements * 2,  # bfloat16 = 2 bytes
            "v_cache_bytes": cache_elements * 2,
        }

    def calculate_norm_shape(
        self,
        batch_size: int,
        seq_len: int,
        is_decode: bool = False,
    ) -> PaddedShape:
        """
        Calculate shape for normalization layer.

        Args:
            batch_size: Batch dimension
            seq_len: Sequence length
            is_decode: Whether this is for decode phase

        Returns:
            PaddedShape for norm operation
        """
        # RMSNorm operates on hidden dimension
        # For NPU, we may need to pad to column boundaries
        total_elements = batch_size * (seq_len if not is_decode else 1)
        size_to_normalize = total_elements * self.hidden_size

        # Pad to AIE column boundary
        max_multiple = self.num_aie_columns * self.tiling_config.tile_n
        padded_size = self.pad_to_multiple(size_to_normalize, max_multiple)

        return PaddedShape(
            original_shape=(total_elements, self.hidden_size),
            padded_shape=(padded_size,),
            padding={"total": padded_size - size_to_normalize},
            reason="NPU column alignment",
        )

    def calculate_embedding_shape(
        self,
        vocab_size: int,
        embedding_dim: int,
    ) -> PaddedShape:
        """
        Calculate shape for embedding table.

        Args:
            vocab_size: Vocabulary size
            embedding_dim: Embedding dimension

        Returns:
            PaddedShape for embedding table
        """
        # Embedding table: (vocab_size, embedding_dim)
        # May need padding for efficient NPU access
        vocab_padded = self.pad_to_multiple(vocab_size, 64)  # Cache line alignment

        return PaddedShape(
            original_shape=(vocab_size, embedding_dim),
            padded_shape=(vocab_padded, embedding_dim),
            padding={"vocab": vocab_padded - vocab_size},
            reason="Cache line alignment",
        )

    def get_optimal_tile_sizes(
        self,
        M: int,
        K: int,
        N: int,
    ) -> Tuple[int, int, int]:
        """
        Compute optimal tile sizes for given problem dimensions.

        Args:
            M: Input matrix rows
            K: Reduction dimension
            N: Output matrix columns

        Returns:
            Tuple of (tile_m, tile_k, tile_n)
        """
        tc = self.tiling_config

        # Start with default tile sizes
        best_tiles = (tc.tile_m, tc.tile_k, tc.tile_n)

        # For small problems, use smaller tiles to reduce overhead
        if M < 128:
            best_tiles = (min(32, tc.tile_m), best_tiles[1], best_tiles[2])
        if N < 128:
            best_tiles = (best_tiles[0], best_tiles[1], min(32, tc.tile_n))
        if K < 128:
            best_tiles = (best_tiles[0], min(32, tc.tile_k), best_tiles[2])

        # Ensure tiles meet minimum requirements
        best_tiles = (
            max(best_tiles[0], tc.min_tile_m),
            max(best_tiles[1], tc.min_tile_k),
            max(best_tiles[2], tc.min_tile_n),
        )

        return best_tiles

    def calculate_lm_head_shape(
        self,
        batch_size: int,
        seq_len: int,
        vocab_size: int,
        is_decode: bool = False,
    ) -> PaddedShape:
        """
        Calculate shape for LM head (final projection to vocab).

        Args:
            batch_size: Batch dimension
            seq_len: Sequence length
            vocab_size: Vocabulary size
            is_decode: Whether this is for decode phase

        Returns:
            PaddedShape for LM head
        """
        tokens = batch_size * seq_len if not is_decode else batch_size

        # LM head is typically a large GEMM: (tokens, hidden) x (hidden, vocab)
        # For large vocabularies, partition the N dimension
        return self.calculate_padded_gemm_shape(tokens, self.hidden_size, vocab_size)

    def _get_padding_reason(self, op_name: str, padding: Dict[str, int]) -> str:
        """Generate human-readable padding reason"""
        reasons = []
        for dim, pad_amount in padding.items():
            if pad_amount > 0:
                reasons.append(f"{dim}+{pad_amount}")

        if reasons:
            return f"{op_name}: padded {', '.join(reasons)} for NPU alignment"
        return f"{op_name}: no padding needed"

    def get_memory_requirements(
        self,
        max_seq_len: int,
        batch_size: int = 1,
        intermediate_size: Optional[int] = None,
    ) -> Dict[str, int]:
        """
        Calculate total memory requirements for model execution.

        Args:
            max_seq_len: Maximum sequence length
            batch_size: Batch size
            intermediate_size: FFN intermediate size (optional)

        Returns:
            Dictionary with memory requirements in bytes
        """
        intermediate = intermediate_size or (self.hidden_size * 4)  # Default 4x expansion

        # KV Cache
        kv_cache = self.calculate_kv_cache_size(max_seq_len, batch_size)

        # Activations (rough estimates)
        # For prefill: store all intermediate activations
        prefill_tokens = batch_size * max_seq_len
        activation_memory = (
            prefill_tokens * self.hidden_size * 2  # Input activations
            + prefill_tokens * intermediate * 2  # FFN intermediate
            + prefill_tokens * self.hidden_size * 2  # Attention outputs
        ) * 2  # bfloat16

        # For decode: only current token activations
        decode_activation_memory = (
            batch_size * self.hidden_size * 2
            + batch_size * intermediate * 2
            + batch_size * self.hidden_size * 2
        ) * 2

        return {
            "kv_cache_bytes": kv_cache["k_cache_bytes"] + kv_cache["v_cache_bytes"],
            "prefill_activation_bytes": activation_memory,
            "decode_activation_bytes": decode_activation_memory,
            "total_prefill_bytes": kv_cache["k_cache_bytes"]
            + kv_cache["v_cache_bytes"]
            + activation_memory,
            "total_decode_bytes": kv_cache["k_cache_bytes"]
            + kv_cache["v_cache_bytes"]
            + decode_activation_memory,
        }


@dataclass
class NPUOperatorShape:
    """
    Complete shape configuration for an NPU operator.

    Encapsulates all shape-related information for a single operator
    instance, including input/output shapes, padding, and tiling.
    """

    # Operator identification
    operator_type: str  # e.g., "GEMM", "RMSNorm", "MHA"
    operator_name: str  # e.g., "q_proj", "norm1"

    # Original and padded shapes
    input_shape: Tuple[int, ...]
    output_shape: Tuple[int, ...]
    weight_shape: Optional[Tuple[int, ...]] = None

    # Tiling configuration
    tile_m: int = 64
    tile_k: int = 64
    tile_n: int = 64
    num_aie_columns: int = 8

    # Padding information
    is_padded: bool = False
    padding_info: Dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, any]:
        """Convert to dictionary"""
        return {
            "operator_type": self.operator_type,
            "operator_name": self.operator_name,
            "input_shape": self.input_shape,
            "output_shape": self.output_shape,
            "weight_shape": self.weight_shape,
            "tile_m": self.tile_m,
            "tile_k": self.tile_k,
            "tile_n": self.tile_n,
            "num_aie_columns": self.num_aie_columns,
            "is_padded": self.is_padded,
            "padding_info": self.padding_info,
        }


def create_shape_manager(
    hidden_size: int,
    num_heads: int,
    num_kv_heads: Optional[int] = None,
    **kwargs,
) -> ShapeManager:
    """
    Factory function to create ShapeManager.

    Args:
        hidden_size: Model hidden dimension
        num_heads: Number of attention heads
        num_kv_heads: Number of KV heads (optional)
        **kwargs: Additional arguments for ShapeManager

    Returns:
        ShapeManager instance
    """
    return ShapeManager(
        hidden_size=hidden_size,
        num_attention_heads=num_heads,
        num_kv_heads=num_kv_heads,
        **kwargs,
    )
