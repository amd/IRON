# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Model Assembler for NPU Models

This module provides the ModelAssembler class that orchestrates the
construction of complete neural network models from NPU operators.
It handles weight assignment, memory management, and model execution.
"""

import torch
import torch.nn as nn
import numpy as np
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
from dataclasses import dataclass, field

from iron.common import AIEContext
from .config_adapter import ConfigAdapter, NormalizedConfig, ModelArchitecture
from .weight_mapper import WeightMapper, create_weight_mapper
from .operator_factory import OperatorFactory, create_operator_factory
from .shape_manager import ShapeManager
from .layer_builder import (
    LayerConfig,
    AttentionLayerBuilder,
    FeedForwardBuilder,
    TransformerBlockBuilder,
)


@dataclass
class ModelAssemblyConfig:
    """Configuration for model assembly"""

    # Model configuration
    normalized_config: NormalizedConfig

    # NPU configuration
    num_aie_columns: int = 8
    default_dtype: str = "bfloat16"

    # Operator enable flags
    use_aie_gemm: bool = True
    use_aie_gemv: bool = False  # For decode phase
    use_aie_norm: bool = True
    use_aie_attention: bool = False
    use_aie_rope: bool = False
    use_aie_ffn: bool = True

    # Phase-specific settings
    is_decode: bool = False
    use_kv_cache: bool = True
    max_seq_len: int = 512
    batch_size: int = 1

    # Memory settings
    compile_artifacts: bool = True
    verbose: bool = False


class ModelAssembler:
    """
    Assembles complete neural network models for NPU execution.

    This class:
    1. Creates operator instances based on model configuration
    2. Manages weight loading and assignment
    3. Handles memory allocation for buffers
    4. Orchestrates model execution
    """

    def __init__(
        self,
        config: Union[NormalizedConfig, ModelAssemblyConfig, Dict],
        context: Optional[AIEContext] = None,
    ):
        """
        Initialize the model assembler.

        Args:
            config: Model configuration
            context: AIE context
        """
        # Parse configuration
        if isinstance(config, dict):
            adapter = ConfigAdapter(config)
            self.norm_config = adapter.normalize()
            self.assembly_config = ModelAssemblyConfig(
                normalized_config=self.norm_config
            )
        elif isinstance(config, NormalizedConfig):
            self.norm_config = config
            self.assembly_config = ModelAssemblyConfig(normalized_config=config)
        elif isinstance(config, ModelAssemblyConfig):
            self.norm_config = config.normalized_config
            self.assembly_config = config
        else:
            raise ValueError(f"Unknown config type: {type(config)}")

        # Initialize AIE context
        self.context = context or AIEContext()

        # Create operator factory
        self.factory = create_operator_factory(
            context=self.context,
            num_aie_columns=self.assembly_config.num_aie_columns,
            default_dtype=self.assembly_config.default_dtype,
        )

        # Create shape manager
        self.shape_manager = ShapeManager(
            hidden_size=self.norm_config.hidden_size,
            num_attention_heads=self.norm_config.num_attention_heads,
            num_kv_heads=self.norm_config.num_kv_heads,
            num_aie_columns=self.assembly_config.num_aie_columns,
        )

        # Create weight mapper
        self.weight_mapper = create_weight_mapper(
            architecture=self.norm_config.architecture.value,
        )

        # Model components (populated during assembly)
        self.embedding = None
        self.layers: List[TransformerBlockBuilder] = []
        self.final_norm = None
        self.lm_head = None

        # Assembly state
        self._assembled = False
        self._weights_loaded = False
        self._artifacts_compiled = False

    def assemble(self) -> "ModelAssembler":
        """
        Assemble the model architecture.

        Creates all operators and buffers needed for the model.

        Returns:
            Self for method chaining
        """
        cfg = self.norm_config
        acfg = self.assembly_config

        # Create embedding
        self.embedding = self._create_embedding()

        # Create transformer blocks
        self.layers = self._create_transformer_blocks()

        # Create final norm
        self.final_norm = self._create_final_norm()

        # Create LM head
        self.lm_head = self._create_lm_head()

        self._assembled = True
        return self

    def _create_embedding(self) -> nn.Embedding:
        """Create token embedding layer"""
        # For now, use PyTorch embedding
        # Future: Add AIE embedding lookup if beneficial
        return nn.Embedding(
            self.norm_config.vocab_size,
            self.norm_config.hidden_size,
            dtype=torch.bfloat16,
        )

    def _create_transformer_blocks(self) -> List[TransformerBlockBuilder]:
        """Create all transformer blocks"""
        layers = []
        cfg = self.norm_config
        acfg = self.assembly_config

        layer_config = LayerConfig(
            layer_type="transformer_block",
            layer_idx=None,  # Will be set per layer
            hidden_size=cfg.hidden_size,
            num_attention_heads=cfg.num_attention_heads,
            num_kv_heads=cfg.num_kv_heads,
            head_dim=cfg.head_dim,
            intermediate_size=cfg.intermediate_size,
            norm_type=cfg.norm_type.value,
            norm_eps=cfg.norm_eps,
            rope_theta=cfg.rope_theta,
            ffn_type=cfg.ffn_type.value,
            num_aie_columns=acfg.num_aie_columns,
        )

        for i in range(cfg.num_hidden_layers):
            layer_cfg = LayerConfig(
                **{**layer_config.__dict__, "layer_idx": i},
            )

            builder = TransformerBlockBuilder(
                config=layer_cfg,
                context=self.context,
                seq_len=acfg.max_seq_len,
                batch_size=acfg.batch_size,
            )

            # Build the layer
            builder.build(
                use_aie_norm=acfg.use_aie_norm,
                use_aie_residual=True,
                use_fused_mha=acfg.use_aie_attention,
                use_aie_rope=acfg.use_aie_rope,
                use_kv_cache=acfg.use_kv_cache,
                is_decode=acfg.is_decode,
            )

            layers.append(builder)

        return layers

    def _create_final_norm(self):
        """Create final normalization layer"""
        if self.assembly_config.use_aie_norm:
            return self.factory.create_rms_norm(
                name="final_norm",
                size=self.norm_config.hidden_size,
                eps=self.norm_config.norm_eps,
            )
        else:
            return nn.RMSNorm(
                self.norm_config.hidden_size, eps=self.norm_config.norm_eps
            )

    def _create_lm_head(self):
        """Create LM head (output projection)"""
        if self.assembly_config.use_aie_gemm:
            # Use AIE GEMM for large vocab projection
            batch_tokens = self.assembly_config.batch_size * (
                1
                if self.assembly_config.is_decode
                else self.assembly_config.max_seq_len
            )

            return self.factory.create_gemm(
                name="lm_head",
                M=batch_tokens,
                K=self.norm_config.hidden_size,
                N=self.norm_config.vocab_size,
                use_static_weight=False,
                partition_N=4,  # Partition for large vocab
            )
        else:
            return nn.Linear(
                self.norm_config.hidden_size,
                self.norm_config.vocab_size,
                bias=False,
                dtype=torch.bfloat16,
            )

    def load_weights(
        self,
        weights_path: Union[str, Path],
        weights_format: str = "auto",
        device: str = "cpu",
    ) -> "ModelAssembler":
        """
        Load model weights from checkpoint.

        Args:
            weights_path: Path to weights file or directory
            weights_format: Format of weights (auto, safetensors, pytorch)
            device: Device to load weights on

        Returns:
            Self for method chaining
        """
        weights_path = Path(weights_path)

        # Auto-detect format
        if weights_format == "auto":
            if (weights_path / "model.safetensors").exists():
                weights_format = "safetensors"
            elif (weights_path / "model.safetensors.index.json").exists():
                weights_format = "safetensors"
            elif list(weights_path.glob("*.pt")) or list(weights_path.glob("*.bin")):
                weights_format = "pytorch"
            else:
                raise ValueError(
                    f"Could not determine weights format in {weights_path}"
                )

        # Load weights
        if weights_format == "safetensors":
            state_dict = self.weight_mapper.load_safetensors(weights_path, device)
        elif weights_format == "pytorch":
            state_dict = self.weight_mapper.load_pytorch(weights_path, device)
        else:
            raise ValueError(f"Unknown weights format: {weights_format}")

        # Map weights to IRON format
        mapped_weights = self.weight_mapper.map_weights(state_dict)

        # Assign weights to operators
        self._assign_weights()

        self._weights_loaded = True
        return self

    def _assign_weights(self):
        """Assign mapped weights to model operators"""
        wm = self.weight_mapper.mapped_weights

        # Embedding
        if "tok_emb.weight" in wm:
            if isinstance(self.embedding, nn.Embedding):
                self.embedding.weight.data = torch.from_numpy(
                    wm["tok_emb.weight"].tensor
                )

        # Transformer blocks
        for i, layer in enumerate(self.layers):
            prefix = f"layers.{i}."

            # Attention weights
            attn_weights = {}
            for key in ["q", "k", "v", "o"]:
                wk = f"{prefix}attention.w{key}.weight"
                if wk in wm:
                    attn_weights[f"{key}_weight"] = wm[wk].tensor

            if attn_weights:
                layer.attention_builder.assign_weights(**attn_weights)

            # FFN weights (SwiGLU naming)
            ffn_weights = {}
            for name, key in [
                ("gate", f"{prefix}feed_forward.w1.weight"),
                ("up", f"{prefix}feed_forward.w3.weight"),
                ("down", f"{prefix}feed_forward.w2.weight"),
            ]:
                if key in wm:
                    ffn_weights[f"{name}_weight"] = wm[key].tensor

            if ffn_weights:
                layer.ffn_builder.assign_weights(**ffn_weights)

            # Normalization weights
            norm1_key = f"{prefix}norm1.weight"
            norm2_key = f"{prefix}norm2.weight"

            if norm1_key in wm and hasattr(layer.norm1, "weight"):
                layer.norm1.weight = wm[norm1_key].tensor

            if norm2_key in wm and hasattr(layer.norm2, "weight"):
                layer.norm2.weight = wm[norm2_key].tensor

        # Final norm
        if "final_norm.weight" in wm and hasattr(self.final_norm, "weight"):
            self.final_norm.weight = wm["final_norm.weight"].tensor

        # LM head
        if "out_head.weight" in wm:
            if hasattr(self.lm_head, "weight"):
                self.lm_head.weight = wm["out_head.weight"].tensor
            elif hasattr(self.lm_head, "weight"):
                self.lm_head.weight = wm["out_head.weight"].tensor

    def compile_artifacts(self, dry_run: bool = False) -> "ModelAssembler":
        """
        Compile all AIE artifacts.

        Args:
            dry_run: If True, only print compilation commands

        Returns:
            Self for method chaining
        """
        if not self._assembled:
            raise RuntimeError("Model must be assembled before compiling artifacts")

        # Set up artifacts for all operators
        self._setup_all_artifacts()

        # Compile using the context
        self.context.compile(dry_run=dry_run)

        self._artifacts_compiled = True
        return self

    def _setup_all_artifacts(self):
        """Set up artifacts for all operators"""
        # Transformer blocks
        for layer in self.layers:
            # Attention
            if layer.attention_builder.mha:
                layer.attention_builder.mha.set_up_artifacts()
            if layer.attention_builder.q_proj:
                layer.attention_builder.q_proj.set_up_artifacts()
            if layer.attention_builder.k_proj:
                layer.attention_builder.k_proj.set_up_artifacts()
            if layer.attention_builder.v_proj:
                layer.attention_builder.v_proj.set_up_artifacts()
            if layer.attention_builder.o_proj:
                layer.attention_builder.o_proj.set_up_artifacts()

            # FFN
            if layer.ffn_builder.gate_proj:
                layer.ffn_builder.gate_proj.set_up_artifacts()
            if layer.ffn_builder.up_proj:
                layer.ffn_builder.up_proj.set_up_artifacts()
            if layer.ffn_builder.down_proj:
                layer.ffn_builder.down_proj.set_up_artifacts()

            # Residual adds
            if layer.residual_add1:
                layer.residual_add1.set_up_artifacts()
            if layer.residual_add2:
                layer.residual_add2.set_up_artifacts()

        # Final norm
        if hasattr(self.final_norm, "set_up_artifacts"):
            self.final_norm.set_up_artifacts()

        # LM head
        if hasattr(self.lm_head, "set_up_artifacts"):
            self.lm_head.set_up_artifacts()

    def forward(
        self,
        input_ids: torch.Tensor,
        input_pos: Optional[torch.Tensor] = None,
        use_kv_cache: bool = True,
    ) -> torch.Tensor:
        """
        Forward pass through the model.

        Args:
            input_ids: Input token IDs
            input_pos: Input positions (for RoPE with KV cache)
            use_kv_cache: Whether to use KV cache

        Returns:
            Logits tensor
        """
        if not self._assembled:
            raise RuntimeError("Model must be assembled before forward pass")

        # Embed tokens
        x = self.embedding(input_ids)

        # Get RoPE angles (precomputed)
        angles = self._get_rope_angles(input_ids, input_pos)

        # Create attention mask
        mask = self._create_attention_mask(input_ids, input_pos, use_kv_cache)

        # Process through transformer blocks
        for i, layer in enumerate(self.layers):
            x = layer.forward(x, mask, angles, input_pos)

        # Final normalization
        if hasattr(self.final_norm, "forward"):
            x = self.final_norm(x)
        else:
            x = self.final_norm(x)

        # LM head projection
        if hasattr(self.lm_head, "forward"):
            logits = self.lm_head(x)
        else:
            logits = self.lm_head(x)

        return logits

    def _get_rope_angles(
        self,
        input_ids: torch.Tensor,
        input_pos: Optional[torch.Tensor],
    ) -> Optional[torch.Tensor]:
        """Get precomputed RoPE angles"""
        # This would access precomputed RoPE cache
        # For now, return None - actual implementation needs RoPE cache
        return None

    def _create_attention_mask(
        self,
        input_ids: torch.Tensor,
        input_pos: Optional[torch.Tensor],
        use_kv_cache: bool,
    ) -> Optional[torch.Tensor]:
        """Create attention mask"""
        if use_kv_cache and input_pos is not None:
            # In decode mode with KV cache, no mask needed
            return None

        # Causal mask for prefill
        seq_len = input_ids.shape[-1] if input_ids.ndim == 2 else 1
        if seq_len > 1:
            return torch.triu(
                torch.ones(seq_len, seq_len, dtype=torch.bool),
                diagonal=1,
            )
        return None

    def generate(
        self,
        input_ids: torch.Tensor,
        max_new_tokens: int,
        temperature: float = 1.0,
        top_k: Optional[int] = None,
        use_kv_cache: bool = True,
        verbose: bool = False,
    ) -> torch.Tensor:
        """
        Generate tokens autoregressively.

        Args:
            input_ids: Prompt token IDs
            max_new_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            top_k: Top-k sampling
            use_kv_cache: Use KV cache for efficiency
            verbose: Print progress

        Returns:
            Generated token IDs
        """
        all_tokens = input_ids
        input_pos = torch.arange(0, input_ids.shape[1], device=input_ids.device)

        for i in range(max_new_tokens):
            # Forward pass
            logits = self.forward(
                all_tokens, input_pos=input_pos, use_kv_cache=use_kv_cache
            )

            # Get last token logits
            next_token_logits = logits[:, -1, :]

            # Apply temperature
            if temperature != 1.0:
                next_token_logits = next_token_logits / temperature

            # Top-k sampling
            if top_k is not None:
                indices_to_remove = (
                    next_token_logits
                    < torch.topk(next_token_logits, top_k)[0][..., -1, None]
                )
                next_token_logits[indices_to_remove] = float("-inf")

            # Sample
            probs = torch.softmax(next_token_logits, dim=-1)
            next_token = torch.multinomial(probs, num_samples=1)

            # Append to sequence
            all_tokens = torch.cat([all_tokens, next_token], dim=-1)

            # Update position
            input_pos = torch.tensor(
                [all_tokens.shape[1] - 1],
                device=input_ids.device,
            )

            if verbose and (i + 1) % 10 == 0:
                print(f"Generated {i + 1}/{max_new_tokens} tokens")

            # Check for EOS
            # This would need EOS token configuration

        return all_tokens

    def get_memory_info(self) -> Dict[str, Any]:
        """Get memory usage information"""
        return self.shape_manager.get_memory_requirements(
            max_seq_len=self.assembly_config.max_seq_len,
            batch_size=self.assembly_config.batch_size,
            intermediate_size=self.norm_config.intermediate_size,
        )


def create_model(
    config_path: Union[str, Path, Dict],
    weights_path: Optional[Union[str, Path]] = None,
    num_aie_columns: int = 8,
    **kwargs,
) -> ModelAssembler:
    """
    Factory function to create and optionally load a model.

    Args:
        config_path: Path to model config or config dict
        weights_path: Optional path to model weights
        num_aie_columns: Number of AIE columns to use
        **kwargs: Additional assembly configuration

    Returns:
        ModelAssembler instance
    """
    # Load config
    adapter = ConfigAdapter(config_path)
    norm_config = adapter.normalize()

    # Create assembly config
    assembly_config = ModelAssemblyConfig(
        normalized_config=norm_config,
        num_aie_columns=num_aie_columns,
        **kwargs,
    )

    # Create and assemble model
    assembler = ModelAssembler(assembly_config)
    assembler.assemble()

    # Load weights if provided
    if weights_path:
        assembler.load_weights(weights_path)

    return assembler
