# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Layer Builder for NPU Models

This module provides builder classes for constructing complete neural network
layers from NPU operators. It handles the composition of operators into
functional layers like attention, feed-forward networks, and transformer blocks.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
from dataclasses import dataclass, field

import torch
import torch.nn as nn
import numpy as np

from iron.common import AIEContext
from .operator_factory import OperatorFactory, OperatorType, create_operator_factory
from .shape_manager import ShapeManager


@dataclass
class LayerConfig:
    """Configuration for a neural network layer"""

    # Layer identification
    layer_type: str
    layer_idx: Optional[int] = None

    # Dimensions
    hidden_size: int = 768
    num_attention_heads: int = 12
    num_kv_heads: Optional[int] = None
    head_dim: Optional[int] = None
    intermediate_size: Optional[int] = None

    # Normalization
    norm_type: str = "rms_norm"
    norm_eps: float = 1e-6

    # Attention
    attention_dropout: float = 0.0
    rope_theta: float = 10000.0
    use_rope: bool = True

    # FFN
    ffn_type: str = "swiglu"  # swiglu, gelu, mlp
    activation_dropout: float = 0.0

    # NPU-specific
    num_aie_columns: int = 8
    use_aie_operators: bool = True


class AttentionLayerBuilder:
    """
    Builder for attention layers with NPU operators.

    Supports:
    - Multi-Head Attention (MHA)
    - Grouped Query Attention (GQA)
    - Multi-Query Attention (MQA)
    - Optional RoPE integration
    - KV cache for efficient decoding
    """

    def __init__(
        self,
        config: LayerConfig,
        factory: Optional[OperatorFactory] = None,
        shape_manager: Optional[ShapeManager] = None,
        context: Optional[AIEContext] = None,
        seq_len: int = 512,
        batch_size: int = 1,
    ):
        """
        Initialize the attention layer builder.

        Args:
            config: Layer configuration
            factory: Operator factory (created if not provided)
            shape_manager: Shape manager (created if not provided)
            context: AIE context
            seq_len: Sequence length for initialization
            batch_size: Batch size
        """
        self.config = config
        self.context = context or AIEContext()

        # Create factory and shape manager if not provided
        self.factory = factory or create_operator_factory(
            context=self.context,
            num_aie_columns=config.num_aie_columns,
        )

        self.shape_manager = shape_manager or ShapeManager(
            hidden_size=config.hidden_size,
            num_attention_heads=config.num_attention_heads,
            num_kv_heads=config.num_kv_heads or config.num_attention_heads,
            num_aie_columns=config.num_aie_columns,
        )

        # Store configuration
        self.seq_len = seq_len
        self.batch_size = batch_size
        self.hidden_size = config.hidden_size
        self.num_heads = config.num_attention_heads
        self.num_kv_heads = config.num_kv_heads or config.num_attention_heads
        self.head_dim = config.head_dim or (config.hidden_size // config.num_attention_heads)

        # Operators (created during build)
        self.q_proj = None
        self.k_proj = None
        self.v_proj = None
        self.o_proj = None
        self.mha = None
        self.rope = None

        # KV cache buffers (for decode phase)
        self.k_cache = None
        self.v_cache = None
        self.use_kv_cache = False

    def build(
        self,
        use_fused_mha: bool = False,
        use_aie_rope: bool = False,
        use_kv_cache: bool = False,
        is_decode: bool = False,
    ) -> "AttentionLayerBuilder":
        """
        Build the attention layer operators.

        Args:
            use_fused_mha: Use fused MHA operator
            use_aie_rope: Use AIE RoPE operator
            use_kv_cache: Enable KV cache
            is_decode: Build for decode phase

        Returns:
            Self for method chaining
        """
        self.use_kv_cache = use_kv_cache

        # Calculate shapes
        current_seq = 1 if is_decode else self.seq_len
        current_batch = self.batch_size

        if use_fused_mha:
            # Use fused MHA operator
            self._build_fused_mha(current_seq, current_batch)
        else:
            # Use separate QKV projection + attention
            self._build_qkv_projections(current_seq, current_batch)

        # Build RoPE if needed
        if use_aie_rope:
            self._build_rope(current_seq, current_batch)

        return self

    def _build_fused_mha(self, seq_len: int, batch_size: int):
        """Build fused MHA operator"""
        self.mha = self.factory.create_operator(
            OperatorType.MHA,
            name="attention.mha",
            num_heads=self.num_heads,
            seq_len=seq_len,
            d=self.head_dim,
            num_KV_heads=self.num_kv_heads,
            cache=True,
        )

    def _build_qkv_projections(self, seq_len: int, batch_size: int):
        """Build separate Q, K, V projection operators"""
        total_tokens = batch_size * seq_len

        # Q projection: hidden -> hidden
        self.q_proj = self.factory.create_gemm(
            name="attention.q_proj",
            M=total_tokens,
            K=self.hidden_size,
            N=self.hidden_size,
            use_static_weight=False,
        )

        # K projection: hidden -> num_kv_heads * head_dim
        kv_dim = self.num_kv_heads * self.head_dim
        self.k_proj = self.factory.create_gemm(
            name="attention.k_proj",
            M=total_tokens,
            K=self.hidden_size,
            N=kv_dim,
            use_static_weight=False,
        )

        # V projection: hidden -> num_kv_heads * head_dim
        self.v_proj = self.factory.create_gemm(
            name="attention.v_proj",
            M=total_tokens,
            K=self.hidden_size,
            N=kv_dim,
            use_static_weight=False,
        )

        # Output projection
        self.o_proj = self.factory.create_gemm(
            name="attention.o_proj",
            M=total_tokens,
            K=self.hidden_size,
            N=self.hidden_size,
            use_static_weight=False,
        )

    def _build_rope(self, seq_len: int, batch_size: int):
        """Build RoPE operator"""
        self.rope = self.factory.create_operator(
            OperatorType.ROPE,
            name="attention.rope",
            seq_len=seq_len,
            head_dim=self.head_dim,
            theta_base=self.config.rope_theta,
            cache=True,
        )

    def assign_weights(
        self,
        q_weight: Optional[np.ndarray] = None,
        k_weight: Optional[np.ndarray] = None,
        v_weight: Optional[np.ndarray] = None,
        o_weight: Optional[np.ndarray] = None,
    ) -> None:
        """
        Assign weights to the attention operators.

        Args:
            q_weight: Q projection weight matrix
            k_weight: K projection weight matrix
            v_weight: V projection weight matrix
            o_weight: Output projection weight matrix
        """
        if self.q_proj and q_weight is not None:
            self.q_proj.weight = q_weight.T if q_weight.ndim == 2 else q_weight

        if self.k_proj and k_weight is not None:
            self.k_proj.weight = k_weight.T if k_weight.ndim == 2 else k_weight

        if self.v_proj and v_weight is not None:
            self.v_proj.weight = v_weight.T if v_weight.ndim == 2 else v_weight

        if self.o_proj and o_weight is not None:
            self.o_proj.weight = o_weight.T if o_weight.ndim == 2 else o_weight

        if self.mha and q_weight is not None:
            # For fused MHA, weights may need special handling
            # This depends on the specific MHA operator implementation
            pass

    def forward(
        self,
        x: torch.Tensor,
        angles: Optional[torch.Tensor] = None,
        input_pos: Optional[torch.Tensor] = None,
        mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """
        Forward pass through attention layer.

        Args:
            x: Input tensor
            angles: RoPE angles (precomputed)
            input_pos: Input positions for RoPE
            mask: Attention mask

        Returns:
            Output tensor
        """
        if self.mha:
            # Fused MHA path
            return self._forward_fused(x)
        else:
            # Separate QKV path
            return self._forward_qkv(x, angles, input_pos, mask)

    def _forward_fused(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass with fused MHA"""
        # Reshape for MHA operator
        # Expected: (batch, num_heads, seq_len, head_dim)
        if x.ndim == 2:
            x = x.view(self.batch_size, self.seq_len, self.hidden_size)
        if x.ndim == 3:
            x = x.view(self.batch_size, self.seq_len, self.num_heads, self.head_dim)
            x = x.permute(0, 2, 1, 3)  # (batch, heads, seq, dim)

        # Run MHA
        q = x
        k = x  # For self-attention, K and V come from same input
        v = x

        output = self.mha(q, k, v)
        return output

    def _forward_qkv(
        self,
        x: torch.Tensor,
        angles: Optional[torch.Tensor],
        input_pos: Optional[torch.Tensor],
        mask: Optional[torch.Tensor],
    ) -> torch.Tensor:
        """Forward pass with separate QKV projections"""
        # Q projection
        q = self.q_proj(x)

        # K, V projections
        k = self.k_proj(x)
        v = self.v_proj(x)

        # Apply RoPE if available
        if self.rope and angles is not None:
            q = self.rope(q, angles, input_pos)
            k = self.rope(k, angles, input_pos)

        # TODO: Implement attention mechanism
        # For now, this is a placeholder - actual attention requires
        # score computation and softmax

        # Output projection
        output = self.o_proj(q)
        return output


class FeedForwardBuilder:
    """
    Builder for feed-forward network layers.

    Supports:
    - SwiGLU (Llama, Mistral)
    - GeGLU (Phi)
    - Standard MLP
    """

    def __init__(
        self,
        config: LayerConfig,
        factory: Optional[OperatorFactory] = None,
        shape_manager: Optional[ShapeManager] = None,
        context: Optional[AIEContext] = None,
        seq_len: int = 512,
        batch_size: int = 1,
    ):
        """Initialize the FFN builder"""
        self.config = config
        self.context = context or AIEContext()

        self.factory = factory or create_operator_factory(
            context=self.context,
            num_aie_columns=config.num_aie_columns,
        )

        self.shape_manager = shape_manager or ShapeManager(
            hidden_size=config.hidden_size,
            num_attention_heads=config.num_attention_heads,
            num_aie_columns=config.num_aie_columns,
        )

        # Configuration
        self.seq_len = seq_len
        self.batch_size = batch_size
        self.hidden_size = config.hidden_size
        self.intermediate_size = config.intermediate_size or (config.hidden_size * 4)
        self.ffn_type = config.ffn_type

        # Operators
        self.gate_proj = None
        self.up_proj = None
        self.down_proj = None
        self.swiglu = None
        self.silu = None
        self.mul = None

    def build(
        self,
        use_swiglu_runlist: bool = False,
        is_decode: bool = False,
    ) -> "FeedForwardBuilder":
        """
        Build the FFN operators.

        Args:
            use_swiglu_runlist: Use fused SwiGLU runlist
            is_decode: Build for decode phase

        Returns:
            Self for method chaining
        """
        current_seq = 1 if is_decode else self.seq_len
        total_tokens = self.batch_size * current_seq

        if self.ffn_type == "swiglu":
            if use_swiglu_runlist:
                self._build_swiglu_runlist(total_tokens)
            else:
                self._build_swiglu_separate(total_tokens)
        elif self.ffn_type == "geglu":
            self._build_geglu(total_tokens)
        else:
            self._build_mlp(total_tokens)

        return self

    def _build_swiglu_runlist(self, total_tokens: int):
        """Build SwiGLU with fused runlist"""
        # For SwiGLU, we need gate and up projections, then multiply, then silu, then down
        self.gate_proj = self.factory.create_gemm(
            name="ffn.gate_proj",
            M=total_tokens,
            K=self.hidden_size,
            N=self.intermediate_size,
            use_static_weight=False,
        )

        self.up_proj = self.factory.create_gemm(
            name="ffn.up_proj",
            M=total_tokens,
            K=self.hidden_size,
            N=self.intermediate_size,
            use_static_weight=False,
        )

        self.down_proj = self.factory.create_gemm(
            name="ffn.down_proj",
            M=total_tokens,
            K=self.intermediate_size,
            N=self.hidden_size,
            use_static_weight=False,
        )

        # SwiGLU fusion: silu(gate) * up
        self.swiglu = self.factory.create_operator(
            OperatorType.SWIGLU,
            name="ffn.swiglu",
            size=total_tokens,
            intermediate_size=self.intermediate_size,
        )

    def _build_swiglu_separate(self, total_tokens: int):
        """Build SwiGLU with separate operators"""
        self.gate_proj = self.factory.create_gemm(
            name="ffn.gate_proj",
            M=total_tokens,
            K=self.hidden_size,
            N=self.intermediate_size,
            use_static_weight=False,
        )

        self.up_proj = self.factory.create_gemm(
            name="ffn.up_proj",
            M=total_tokens,
            K=self.hidden_size,
            N=self.intermediate_size,
            use_static_weight=False,
        )

        self.silu = self.factory.create_operator(
            OperatorType.SILU,
            name="ffn.silu",
            size=total_tokens * self.intermediate_size,
        )

        self.mul = self.factory.create_operator(
            OperatorType.ELEMENTWISE_MUL,
            name="ffn.mul",
            size=total_tokens * self.intermediate_size,
        )

        self.down_proj = self.factory.create_gemm(
            name="ffn.down_proj",
            M=total_tokens,
            K=self.intermediate_size,
            N=self.hidden_size,
            use_static_weight=False,
        )

    def _build_geglu(self, total_tokens: int):
        """Build GeGLU FFN"""
        # Similar to SwiGLU but with GELU activation
        self.gate_proj = self.factory.create_gemm(
            name="ffn.gate_proj",
            M=total_tokens,
            K=self.hidden_size,
            N=self.intermediate_size,
            use_static_weight=False,
        )

        self.up_proj = self.factory.create_gemm(
            name="ffn.up_proj",
            M=total_tokens,
            K=self.hidden_size,
            N=self.intermediate_size,
            use_static_weight=False,
        )

        # GELU activation
        from iron.operators import AIEGELU
        self.gelu = AIEGELU(
            size=total_tokens * self.intermediate_size,
            context=self.context,
        )

        self.mul = self.factory.create_operator(
            OperatorType.ELEMENTWISE_MUL,
            name="ffn.mul",
            size=total_tokens * self.intermediate_size,
        )

        self.down_proj = self.factory.create_gemm(
            name="ffn.down_proj",
            M=total_tokens,
            K=self.intermediate_size,
            N=self.hidden_size,
            use_static_weight=False,
        )

    def _build_mlp(self, total_tokens: int):
        """Build standard MLP"""
        self.fc1 = self.factory.create_gemm(
            name="ffn.fc1",
            M=total_tokens,
            K=self.hidden_size,
            N=self.intermediate_size,
            use_static_weight=False,
        )

        self.gelu = self.factory.create_operator(
            OperatorType.GELU,
            name="ffn.gelu",
            size=total_tokens * self.intermediate_size,
        )

        self.fc2 = self.factory.create_gemm(
            name="ffn.fc2",
            M=total_tokens,
            K=self.intermediate_size,
            N=self.hidden_size,
            use_static_weight=False,
        )

    def assign_weights(
        self,
        gate_weight: Optional[np.ndarray] = None,
        up_weight: Optional[np.ndarray] = None,
        down_weight: Optional[np.ndarray] = None,
    ) -> None:
        """Assign weights to FFN operators"""
        if self.gate_proj and gate_weight is not None:
            self.gate_proj.weight = gate_weight.T

        if self.up_proj and up_weight is not None:
            self.up_proj.weight = up_weight.T

        if self.down_proj and down_weight is not None:
            self.down_proj.weight = down_weight.T

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass through FFN"""
        if self.ffn_type == "swiglu":
            return self._forward_swiglu(x)
        elif self.ffn_type == "geglu":
            return self._forward_geglu(x)
        else:
            return self._forward_mlp(x)

    def _forward_swiglu(self, x: torch.Tensor) -> torch.Tensor:
        """SwiGLU forward: silu(gate(x)) * up(x) then down"""
        if self.swiglu:
            # Fused SwiGLU path
            gate_out = self.gate_proj(x)
            up_out = self.up_proj(x)
            return self.down_proj(self.swiglu(gate_out, up_out))
        else:
            # Separate path
            gate = self.gate_proj(x)
            silu_out = self.silu(gate)
            up = self.up_proj(x)
            multiplied = self.mul(silu_out, up)
            return self.down_proj(multiplied)

    def _forward_geglu(self, x: torch.Tensor) -> torch.Tensor:
        """GeGLU forward: gelu(gate(x)) * up(x) then down"""
        gate = self.gate_proj(x)
        gelu_out = self.gelu(gate)
        up = self.up_proj(x)
        multiplied = self.mul(gelu_out, up)
        return self.down_proj(multiplied)

    def _forward_mlp(self, x: torch.Tensor) -> torch.Tensor:
        """MLP forward: gelu(fc1(x)) then fc2"""
        hidden = self.fc1(x)
        activated = self.gelu(hidden)
        return self.fc2(activated)


class TransformerBlockBuilder:
    """
    Builder for complete transformer blocks.

    Composes attention and FFN layers with normalization
    and residual connections.
    """

    def __init__(
        self,
        config: LayerConfig,
        context: Optional[AIEContext] = None,
        **kwargs,
    ):
        """Initialize transformer block builder"""
        self.config = config
        self.context = context or AIEContext()

        # Build sub-layers
        self.attention_builder = AttentionLayerBuilder(
            config=config,
            context=self.context,
            **kwargs,
        )

        self.ffn_builder = FeedForwardBuilder(
            config=config,
            context=self.context,
            **kwargs,
        )

        # Normalization layers
        self.norm1 = None  # Pre-attention norm
        self.norm2 = None  # Post-attention norm

        # Residual add operators
        self.residual_add1 = None
        self.residual_add2 = None

    def build(
        self,
        use_aie_norm: bool = True,
        use_aie_residual: bool = True,
        **attention_kwargs,
    ) -> "TransformerBlockBuilder":
        """
        Build the complete transformer block.

        Args:
            use_aie_norm: Use AIE normalization operators
            use_aie_residual: Use AIE residual add operators
            **attention_kwargs: Arguments for attention builder

        Returns:
            Self for method chaining
        """
        # Build normalization
        if use_aie_norm:
            self.norm1 = self.attention_builder.factory.create_rms_norm(
                name="norm1",
                size=self.config.hidden_size,
                eps=self.config.norm_eps,
            )
            self.norm2 = self.attention_builder.factory.create_rms_norm(
                name="norm2",
                size=self.config.hidden_size,
                eps=self.config.norm_eps,
            )
        else:
            # Use PyTorch RMSNorm
            self.norm1 = nn.RMSNorm(self.config.hidden_size, eps=self.config.norm_eps)
            self.norm2 = nn.RMSNorm(self.config.hidden_size, eps=self.config.norm_eps)

        # Build residual add
        if use_aie_residual:
            self.residual_add1 = self.attention_builder.factory.create_operator(
                OperatorType.ELEMENTWISE_ADD,
                name="residual_add1",
                size=self.config.hidden_size,
            )
            self.residual_add2 = self.attention_builder.factory.create_operator(
                OperatorType.ELEMENTWISE_ADD,
                name="residual_add2",
                size=self.config.hidden_size,
            )

        # Build sub-layers
        self.attention_builder.build(**attention_kwargs)
        self.ffn_builder.build()

        return self

    def assign_weights(
        self,
        norm1_weight: Optional[np.ndarray] = None,
        norm2_weight: Optional[np.ndarray] = None,
        **attention_weights,
    ) -> None:
        """Assign weights to block components"""
        # Normalization weights
        if self.norm1 and hasattr(self.norm1, "weight") and norm1_weight is not None:
            self.norm1.weight = norm1_weight

        if self.norm2 and hasattr(self.norm2, "weight") and norm2_weight is not None:
            self.norm2.weight = norm2_weight

        # Attention weights
        self.attention_builder.assign_weights(**attention_weights)

    def forward(
        self,
        x: torch.Tensor,
        mask: Optional[torch.Tensor] = None,
        angles: Optional[torch.Tensor] = None,
        input_pos: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """Forward pass through transformer block"""
        # Pre-norm
        if hasattr(self.norm1, "forward"):
            x_norm = self.norm1(x)
        else:
            x_norm = self.norm1(x)

        # Attention with residual
        attn_out = self.attention_builder.forward(x_norm, angles, input_pos, mask)

        if self.residual_add1:
            x = self.residual_add1(attn_out, x)
        else:
            x = attn_out + x

        # Post-norm
        if hasattr(self.norm2, "forward"):
            x_norm = self.norm2(x)
        else:
            x_norm = self.norm2(x)

        # FFN with residual
        ffn_out = self.ffn_builder.forward(x_norm)

        if self.residual_add2:
            x = self.residual_add2(ffn_out, x)
        else:
            x = ffn_out + x

        return x


def create_attention_layer(
    hidden_size: int,
    num_heads: int,
    num_kv_heads: Optional[int] = None,
    **kwargs,
) -> AttentionLayerBuilder:
    """Factory function to create attention layer"""
    config = LayerConfig(
        layer_type="attention",
        hidden_size=hidden_size,
        num_attention_heads=num_heads,
        num_kv_heads=num_kv_heads,
    )
    builder = AttentionLayerBuilder(config, **kwargs)
    return builder


def create_ffn_layer(
    hidden_size: int,
    intermediate_size: int,
    ffn_type: str = "swiglu",
    **kwargs,
) -> FeedForwardBuilder:
    """Factory function to create FFN layer"""
    config = LayerConfig(
        layer_type="ffn",
        hidden_size=hidden_size,
        intermediate_size=intermediate_size,
        ffn_type=ffn_type,
    )
    builder = FeedForwardBuilder(config, **kwargs)
    return builder


def create_transformer_block(
    hidden_size: int,
    num_heads: int,
    intermediate_size: int,
    num_kv_heads: Optional[int] = None,
    **kwargs,
) -> TransformerBlockBuilder:
    """Factory function to create transformer block"""
    config = LayerConfig(
        layer_type="transformer_block",
        hidden_size=hidden_size,
        num_attention_heads=num_heads,
        num_kv_heads=num_kv_heads,
        intermediate_size=intermediate_size,
    )
    builder = TransformerBlockBuilder(config, **kwargs)
    return builder
