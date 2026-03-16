# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Llama3.2 weight structures.

This module provides dataclasses for organizing and accessing
Llama3.2 model weights in a type-safe manner.

Example:
    >>> from iron.models.llama32 import LlamaWeights, TransformerWeights
    >>> weights = LlamaWeights.from_raw_weights(raw_dict, config)
    >>> print(weights.layers[0].wq.shape)
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any, Union
import logging
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)

# Type alias for weight tensors (numpy arrays or memory-mapped arrays)
WeightTensor = Union[np.ndarray, np.memmap]


@dataclass
class TransformerWeights:
    """Weights for a single transformer layer.

    This dataclass holds all weight tensors for a single Llama3.2
    transformer layer, including attention and MLP components.

    Attributes:
        wq: Query projection weights [hidden_size, num_heads * head_dim]
        wk: Key projection weights [hidden_size, num_kv_heads * head_dim]
        wv: Value projection weights [hidden_size, num_kv_heads * head_dim]
        wo: Output projection weights [num_heads * head_dim, hidden_size]

        w1: MLP gate projection weights [hidden_size, intermediate_size]
        w2: MLP down projection weights [intermediate_size, hidden_size]
        w3: MLP up projection weights [hidden_size, intermediate_size]

        attn_norm: Attention layer normalization weights [hidden_size]
        ffn_norm: Feed-forward layer normalization weights [hidden_size]

    Example:
        >>> layer_weights = TransformerWeights(
        ...     wq=np.random.randn(2048, 2048),
        ...     wk=np.random.randn(2048, 512),
        ...     wv=np.random.randn(2048, 512),
        ...     wo=np.random.randn(2048, 2048),
        ...     w1=np.random.randn(2048, 8192),
        ...     w2=np.random.randn(8192, 2048),
        ...     w3=np.random.randn(2048, 8192),
        ...     attn_norm=np.random.randn(2048),
        ...     ffn_norm=np.random.randn(2048)
        ... )
    """

    # Attention projections
    wq: WeightTensor  # [hidden_size, num_heads * head_dim]
    wk: WeightTensor  # [hidden_size, num_kv_heads * head_dim]
    wv: WeightTensor  # [hidden_size, num_kv_heads * head_dim]
    wo: WeightTensor  # [num_heads * head_dim, hidden_size]

    # MLP projections (SwiGLU)
    w1: WeightTensor  # [hidden_size, intermediate_size] (gate)
    w2: WeightTensor  # [intermediate_size, hidden_size] (down)
    w3: WeightTensor  # [hidden_size, intermediate_size] (up)

    # Normalization
    attn_norm: WeightTensor  # [hidden_size]
    ffn_norm: WeightTensor  # [hidden_size]

    @property
    def total_params(self) -> int:
        """Calculate total parameters in this layer.

        Returns:
            Total number of parameters across all weight tensors

        Example:
            >>> layer_weights = TransformerWeights(...)
            >>> print(f"Layer has {layer_weights.total_params} params")
        """
        return sum(w.size for w in [
            self.wq, self.wk, self.wv, self.wo,
            self.w1, self.w2, self.w3,
            self.attn_norm, self.ffn_norm
        ])

    @property
    def memory_bytes(self) -> int:
        """Calculate memory required for this layer's weights.

        Returns:
            Total memory in bytes

        Example:
            >>> print(f"Layer uses {layer_weights.memory_bytes / 1e6:.1f}MB")
        """
        return sum(w.size * w.itemsize for w in [
            self.wq, self.wk, self.wv, self.wo,
            self.w1, self.w2, self.w3,
            self.attn_norm, self.ffn_norm
        ])

    def get_attention_weights(self) -> Dict[str, WeightTensor]:
        """Get all attention-related weights.

        Returns:
            Dictionary of attention weight tensors

        Example:
            >>> attn_weights = layer_weights.get_attention_weights()
            >>> print(attn_weights['wq'].shape)
        """
        return {
            "wq": self.wq,
            "wk": self.wk,
            "wv": self.wv,
            "wo": self.wo,
        }

    def get_mlp_weights(self) -> Dict[str, WeightTensor]:
        """Get all MLP-related weights.

        Returns:
            Dictionary of MLP weight tensors

        Example:
            >>> mlp_weights = layer_weights.get_mlp_weights()
            >>> print(mlp_weights['w1'].shape)
        """
        return {
            "w1": self.w1,
            "w2": self.w2,
            "w3": self.w3,
        }

    def get_norm_weights(self) -> Dict[str, WeightTensor]:
        """Get all normalization weights.

        Returns:
            Dictionary of normalization weight tensors

        Example:
            >>> norm_weights = layer_weights.get_norm_weights()
        """
        return {
            "attn_norm": self.attn_norm,
            "ffn_norm": self.ffn_norm,
        }


@dataclass
class LlamaWeights:
    """Complete Llama3.2 weights.

    This dataclass holds all weight tensors for a complete Llama3.2
    model, including embeddings, all transformer layers, and output
    projections.

    Attributes:
        token_embd: Token embedding weights [vocab_size, hidden_size]
        layers: List of transformer layer weights (length: num_hidden_layers)
        output_norm: Final layer normalization weights [hidden_size]
        output: Output projection weights [hidden_size, vocab_size], or None if tied
        vocab_size: Vocabulary size
        hidden_size: Hidden layer dimension
        num_layers: Number of transformer layers

    Example:
        >>> model_weights = LlamaWeights(
        ...     token_embd=np.random.randn(128256, 2048),
        ...     layers=[TransformerWeights(...) for _ in range(16)],
        ...     output_norm=np.random.randn(2048),
        ...     output=None,  # Tied with embeddings
        ...     vocab_size=128256,
        ...     hidden_size=2048,
        ...     num_layers=16
        ... )
    """

    # Embeddings
    token_embd: WeightTensor  # [vocab_size, hidden_size]

    # Transformer layers
    layers: List[TransformerWeights]

    # Final normalization
    output_norm: WeightTensor  # [hidden_size]

    # Output projection (None if tied with embeddings)
    output: Optional[WeightTensor]  # [hidden_size, vocab_size]

    # Metadata
    vocab_size: int
    hidden_size: int
    num_layers: int

    @property
    def total_params(self) -> int:
        """Calculate total parameters in the model.

        Returns:
            Total number of parameters across all weight tensors

        Example:
            >>> print(f"Model has {model_weights.total_params / 1e6:.1f}M params")
        """
        layer_params = sum(layer.total_params for layer in self.layers)
        embedding_params = self.token_embd.size
        norm_params = self.output_norm.size
        output_params = self.output.size if self.output is not None else 0

        return embedding_params + layer_params + norm_params + output_params

    @property
    def memory_bytes(self) -> int:
        """Calculate memory required for all weights.

        Returns:
            Total memory in bytes

        Example:
            >>> print(f"Model uses {model_weights.memory_bytes / 1e9:.2f}GB")
        """
        layer_bytes = sum(layer.memory_bytes for layer in self.layers)
        embedding_bytes = self.token_embd.size * self.token_embd.itemsize
        norm_bytes = self.output_norm.size * self.output_norm.itemsize
        output_bytes = (
            self.output.size * self.output.itemsize
            if self.output is not None else 0
        )

        return embedding_bytes + layer_bytes + norm_bytes + output_bytes

    @property
    def is_output_tied(self) -> bool:
        """Check if output weights are tied with embeddings.

        Returns:
            True if output projection uses embedding weights

        Example:
            >>> if model_weights.is_output_tied:
            ...     print("Using tied embeddings")
        """
        return self.output is None

    def get_output_weights(self) -> WeightTensor:
        """Get output projection weights.

        Returns the output projection weights, or the embedding
        weights if output is tied.

        Returns:
            Output projection weights [hidden_size, vocab_size]

        Raises:
            ValueError: If called when output is tied (returns embeddings instead)

        Example:
            >>> out_weights = model_weights.get_output_weights()
        """
        if self.output is not None:
            return self.output
        # When tied, use transposed embeddings
        return self.token_embd

    def get_layer_weights(self, layer_idx: int) -> TransformerWeights:
        """Get weights for a specific layer.

        Args:
            layer_idx: Layer index (0 to num_layers-1)

        Returns:
            TransformerWeights for the specified layer

        Raises:
            IndexError: If layer_idx is out of range

        Example:
            >>> layer0 = model_weights.get_layer_weights(0)
            >>> print(layer0.wq.shape)
        """
        if layer_idx < 0 or layer_idx >= len(self.layers):
            raise IndexError(
                f"Layer index {layer_idx} out of range [0, {len(self.layers) - 1}]"
            )
        return self.layers[layer_idx]

    def get_all_weight_names(self) -> List[str]:
        """Get names of all weight tensors.

        Returns:
            List of weight tensor names

        Example:
            >>> names = model_weights.get_all_weight_names()
            >>> print(names[:5])
            ['token_embd', 'layers.0.wq', ...]
        """
        names = ["token_embd"]

        for i, layer in enumerate(self.layers):
            names.extend([
                f"layers.{i}.wq",
                f"layers.{i}.wk",
                f"layers.{i}.wv",
                f"layers.{i}.wo",
                f"layers.{i}.w1",
                f"layers.{i}.w2",
                f"layers.{i}.w3",
                f"layers.{i}.attn_norm",
                f"layers.{i}.ffn_norm",
            ])

        names.append("output_norm")

        if self.output is not None:
            names.append("output")

        return names

    @classmethod
    def from_raw_weights(
        cls,
        raw_weights: Dict[str, WeightTensor],
        config: Any
    ) -> "LlamaWeights":
        """Construct LlamaWeights from raw weight dictionary.

        This method takes a dictionary of raw weights (as loaded from
        safetensors) and organizes them into the LlamaWeights structure.

        Args:
            raw_weights: Dictionary mapping weight names to tensors.
                Expected keys follow HuggingFace naming convention:
                - "model.embed_tokens.weight"
                - "model.layers.{i}.self_attn.q_proj.weight"
                - "model.layers.{i}.self_attn.k_proj.weight"
                - "model.layers.{i}.self_attn.v_proj.weight"
                - "model.layers.{i}.self_attn.o_proj.weight"
                - "model.layers.{i}.mlp.gate_proj.weight"
                - "model.layers.{i}.mlp.down_proj.weight"
                - "model.layers.{i}.mlp.up_proj.weight"
                - "model.layers.{i}.input_layernorm.weight"
                - "model.layers.{i}.post_attention_layernorm.weight"
                - "model.norm.weight"
                - "lm_head.weight" (optional, may be tied)
            config: Llama32Config with model architecture parameters

        Returns:
            LlamaWeights instance with organized weight tensors

        Raises:
            KeyError: If required weights are missing

        Example:
            >>> from safetensors import safe_open
            >>> raw = {}
            >>> with safe_open("model.safetensors", framework="numpy") as f:
            ...     for key in f.keys():
            ...         raw[key] = f.get_tensor(key)
            >>> weights = LlamaWeights.from_raw_weights(raw, config)
        """
        layers = []

        for i in range(config.num_hidden_layers):
            layer_prefix = f"model.layers.{i}"

            layer = TransformerWeights(
                # Attention projections
                wq=raw_weights[f"{layer_prefix}.self_attn.q_proj.weight"],
                wk=raw_weights[f"{layer_prefix}.self_attn.k_proj.weight"],
                wv=raw_weights[f"{layer_prefix}.self_attn.v_proj.weight"],
                wo=raw_weights[f"{layer_prefix}.self_attn.o_proj.weight"],
                # MLP projections (SwiGLU)
                w1=raw_weights[f"{layer_prefix}.mlp.gate_proj.weight"],
                w2=raw_weights[f"{layer_prefix}.mlp.down_proj.weight"],
                w3=raw_weights[f"{layer_prefix}.mlp.up_proj.weight"],
                # Normalization
                attn_norm=raw_weights[f"{layer_prefix}.input_layernorm.weight"],
                ffn_norm=raw_weights[f"{layer_prefix}.post_attention_layernorm.weight"],
            )
            layers.append(layer)

        # Handle output projection (may be tied with embeddings)
        output_weight = raw_weights.get("lm_head.weight")

        return cls(
            token_embd=raw_weights["model.embed_tokens.weight"],
            layers=layers,
            output_norm=raw_weights["model.norm.weight"],
            output=output_weight,
            vocab_size=config.vocab_size,
            hidden_size=config.hidden_size,
            num_layers=config.num_hidden_layers,
        )

    @classmethod
    def from_safetensors(
        cls,
        model_path: Path,
        config: Any
    ) -> "LlamaWeights":
        """Load weights from safetensors files.

        This method loads all safetensors files from a model directory
        and constructs a LlamaWeights instance.

        Args:
            model_path: Path to model directory containing safetensors files
            config: Llama32Config with model architecture parameters

        Returns:
            LlamaWeights instance

        Raises:
            FileNotFoundError: If no safetensors files are found
            KeyError: If required weights are missing

        Example:
            >>> weights = LlamaWeights.from_safetensors(
            ...     Path("/models/llama-3.2-1b"),
            ...     config
            ... )
        """
        try:
            from safetensors import safe_open
        except ImportError as e:
            raise ImportError(
                "safetensors is required for from_safetensors(). "
                "Install it with: pip install safetensors"
            ) from e

        model_path = Path(model_path)
        safetensors_files = sorted(model_path.glob("*.safetensors"))

        if not safetensors_files:
            raise FileNotFoundError(
                f"No safetensors files found in {model_path}"
            )

        logger.info(f"Loading weights from {len(safetensors_files)} safetensors file(s)...")

        # Collect all weights from all files
        raw_weights: Dict[str, WeightTensor] = {}

        for file_path in safetensors_files:
            logger.debug(f"Loading {file_path.name}...")
            with safe_open(file_path, framework="numpy") as f:
                for key in f.keys():
                    raw_weights[key] = f.get_tensor(key)

        logger.info(f"Loaded {len(raw_weights)} weight tensors")

        return cls.from_raw_weights(raw_weights, config)

    def to_dict(self) -> Dict[str, WeightTensor]:
        """Convert weights to dictionary format.

        Returns:
            Dictionary of all weight tensors

        Example:
            >>> weight_dict = model_weights.to_dict()
            >>> print(weight_dict.keys())
        """
        result = {
            "model.embed_tokens.weight": self.token_embd,
            "model.norm.weight": self.output_norm,
        }

        for i, layer in enumerate(self.layers):
            prefix = f"model.layers.{i}"
            result[f"{prefix}.self_attn.q_proj.weight"] = layer.wq
            result[f"{prefix}.self_attn.k_proj.weight"] = layer.wk
            result[f"{prefix}.self_attn.v_proj.weight"] = layer.wv
            result[f"{prefix}.self_attn.o_proj.weight"] = layer.wo
            result[f"{prefix}.mlp.gate_proj.weight"] = layer.w1
            result[f"{prefix}.mlp.down_proj.weight"] = layer.w2
            result[f"{prefix}.mlp.up_proj.weight"] = layer.w3
            result[f"{prefix}.input_layernorm.weight"] = layer.attn_norm
            result[f"{prefix}.post_attention_layernorm.weight"] = layer.ffn_norm

        if self.output is not None:
            result["lm_head.weight"] = self.output

        return result

    def __repr__(self) -> str:
        """Get string representation of weights."""
        return (
            f"LlamaWeights("
            f"vocab_size={self.vocab_size}, "
            f"hidden_size={self.hidden_size}, "
            f"num_layers={self.num_layers}, "
            f"total_params={self.total_params:,}, "
            f"memory={self.memory_bytes / 1e9:.2f}GB)"
        )
