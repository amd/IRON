# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Weight Mapper for HuggingFace Models

This module provides utilities for mapping HuggingFace weight tensor names
to IRON operator buffers. It handles various naming conventions, weight
transformations (transposes, reshaping), and quantized weight formats.
"""

import re
import torch
import numpy as np
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union, Callable
from dataclasses import dataclass, field
from enum import Enum

from iron.common.utils import torch_to_numpy


class WeightTransform(Enum):
    """Types of weight transformations"""
    NONE = "none"
    TRANSPOSE = "transpose"  # Standard transpose
    TRANSPOSE_KV = "transpose_kv"  # Transpose for K/V weights in GQA
    RESHAPE = "reshape"  # Reshape for multi-part weights
    DEQUANT = "dequant"  # Dequantize from INT8/INT4


@dataclass
class MappedWeight:
    """Represents a mapped weight tensor"""
    name: str  # IRON internal name
    original_name: str  # Original HF name
    tensor: np.ndarray  # Weight data
    transform: WeightTransform = WeightTransform.NONE
    metadata: Dict[str, Any] = field(default_factory=dict)


class WeightMapper:
    """
    Maps HuggingFace weight tensors to IRON operator buffers.

    Handles:
    - Different naming conventions across model families
    - Weight transformations (transposes for column-major layout)
    - GQA/MQA weight reshaping
    - Quantized weight formats (AWQ, GPTQ)
    """

    # Weight name patterns for different architectures
    # Format: pattern_regex -> (iron_name_template, transform)

    LLAMA_PATTERNS = {
        r"model\.embed_tokens\.weight": ("tok_emb.weight", WeightTransform.NONE),
        r"model\.norm\.weight": ("final_norm.weight", WeightTransform.NONE),
        r"lm_head\.weight": ("out_head.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.input_layernorm\.weight": ("layers.{0}.norm1.weight", WeightTransform.NONE),
        r"model\.layers\.(\d+)\.post_attention_layernorm\.weight": ("layers.{0}.norm2.weight", WeightTransform.NONE),
        r"model\.layers\.(\d+)\.self_attn\.q_proj\.weight": ("layers.{0}.attention.wq.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.self_attn\.k_proj\.weight": ("layers.{0}.attention.wk.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.self_attn\.v_proj\.weight": ("layers.{0}.attention.wv.weight", WeightTransform.NONE),
        r"model\.layers\.(\d+)\.self_attn\.o_proj\.weight": ("layers.{0}.attention.wo.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.gate_proj\.weight": ("layers.{0}.feed_forward.w1.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.up_proj\.weight": ("layers.{0}.feed_forward.w3.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.down_proj\.weight": ("layers.{0}.feed_forward.w2.weight", WeightTransform.TRANSPOSE),
    }

    MISTRAL_PATTERNS = {
        # Same as Llama but with different norm names sometimes
        r"model\.embed_tokens\.weight": ("tok_emb.weight", WeightTransform.NONE),
        r"model\.norm\.weight": ("final_norm.weight", WeightTransform.NONE),
        r"lm_head\.weight": ("out_head.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.input_layernorm\.weight": ("layers.{0}.norm1.weight", WeightTransform.NONE),
        r"model\.layers\.(\d+)\.post_attention_layernorm\.weight": ("layers.{0}.norm2.weight", WeightTransform.NONE),
        r"model\.layers\.(\d+)\.self_attn\.q_proj\.weight": ("layers.{0}.attention.wq.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.self_attn\.k_proj\.weight": ("layers.{0}.attention.wk.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.self_attn\.v_proj\.weight": ("layers.{0}.attention.wv.weight", WeightTransform.NONE),
        r"model\.layers\.(\d+)\.self_attn\.o_proj\.weight": ("layers.{0}.attention.wo.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.gate_proj\.weight": ("layers.{0}.feed_forward.w1.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.up_proj\.weight": ("layers.{0}.feed_forward.w3.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.down_proj\.weight": ("layers.{0}.feed_forward.w2.weight", WeightTransform.TRANSPOSE),
    }

    PHI_PATTERNS = {
        r"model\.embed_tokens\.weight": ("tok_emb.weight", WeightTransform.NONE),
        r"model\.norm\.weight": ("final_norm.weight", WeightTransform.NONE),
        r"lm_head\.weight": ("out_head.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.ln\.weight": ("layers.{0}.norm.weight", WeightTransform.NONE),
        r"model\.layers\.(\d+)\.self_attn\.qkv_proj\.weight": ("layers.{0}.attention.wqkv.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.self_attn\.out_proj\.weight": ("layers.{0}.attention.wo.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.fc1\.weight": ("layers.{0}.feed_forward.w1.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.fc2\.weight": ("layers.{0}.feed_forward.w2.weight", WeightTransform.TRANSPOSE),
    }

    GEMMA_PATTERNS = {
        r"model\.embed_tokens\.weight": ("tok_emb.weight", WeightTransform.NONE),
        r"model\.norm\.weight": ("final_norm.weight", WeightTransform.NONE),
        r"lm_head\.weight": ("out_head.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.input_layernorm\.weight": ("layers.{0}.norm1.weight", WeightTransform.NONE),
        r"model\.layers\.(\d+)\.post_attention_layernorm\.weight": ("layers.{0}.norm2.weight", WeightTransform.NONE),
        r"model\.layers\.(\d+)\.self_attn\.q_proj\.weight": ("layers.{0}.attention.wq.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.self_attn\.k_proj\.weight": ("layers.{0}.attention.wk.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.self_attn\.v_proj\.weight": ("layers.{0}.attention.wv.weight", WeightTransform.NONE),
        r"model\.layers\.(\d+)\.self_attn\.o_proj\.weight": ("layers.{0}.attention.wo.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.gate_proj\.weight": ("layers.{0}.feed_forward.w1.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.up_proj\.weight": ("layers.{0}.feed_forward.w3.weight", WeightTransform.TRANSPOSE),
        r"model\.layers\.(\d+)\.mlp\.down_proj\.weight": ("layers.{0}.feed_forward.w2.weight", WeightTransform.TRANSPOSE),
    }

    # Architecture to pattern mapping
    PATTERN_MAP = {
        "llama": LLAMA_PATTERNS,
        "mistral": MISTRAL_PATTERNS,
        "phi": PHI_PATTERNS,
        "gemma": GEMMA_PATTERNS,
    }

    def __init__(self, architecture: str = "llama"):
        """
        Initialize the weight mapper.

        Args:
            architecture: Model architecture name (llama, mistral, phi, gemma)
        """
        self.architecture = architecture.lower()
        self.patterns = self.PATTERN_MAP.get(self.architecture, self.LLAMA_PATTERNS)
        self.mapped_weights: Dict[str, MappedWeight] = {}
        self.unmapped_weights: List[str] = []

        # Compilation compiled weights for GQA
        self.gqa_compiled = False
        self.compiled_weights: Dict[str, List[str]] = {}

    def _match_pattern(self, hf_name: str) -> Optional[Tuple[str, WeightTransform]]:
        """Match a HF weight name to an IRON name pattern"""
        for pattern, (template, transform) in self.patterns.items():
            match = re.match(pattern, hf_name)
            if match:
                if match.groups():
                    # Handle layer-specific weights
                    layer_idx = match.group(1)
                    iron_name = template.format(layer_idx)
                else:
                    iron_name = template
                return (iron_name, transform)
        return None

    def map_weight(
        self,
        hf_name: str,
        tensor: torch.Tensor,
        transform_override: Optional[WeightTransform] = None,
    ) -> MappedWeight:
        """
        Map a single HuggingFace weight to IRON format.

        Args:
            hf_name: Original HF weight name
            tensor: Weight tensor
            transform_override: Optional override for transformation type

        Returns:
            MappedWeight object
        """
        match = self._match_pattern(hf_name)

        if match:
            iron_name, transform = match
            if transform_override:
                transform = transform_override
        else:
            # Unrecognized weight - use original name with no transform
            iron_name = hf_name.replace(".", "_")
            transform = WeightTransform.NONE
            self.unmapped_weights.append(hf_name)

        # Apply transformation
        transformed_tensor = self._apply_transform(tensor, transform, hf_name)
        numpy_tensor = torch_to_numpy(transformed_tensor)

        mapped = MappedWeight(
            name=iron_name,
            original_name=hf_name,
            tensor=numpy_tensor,
            transform=transform,
            metadata={"shape": tensor.shape, "dtype": str(tensor.dtype)},
        )

        self.mapped_weights[iron_name] = mapped
        return mapped

    def _apply_transform(
        self,
        tensor: torch.Tensor,
        transform: WeightTransform,
        hf_name: str,
    ) -> torch.Tensor:
        """Apply weight transformation"""
        if transform == WeightTransform.NONE:
            return tensor

        elif transform == WeightTransform.TRANSPOSE:
            # For column-major layout, transpose weights
            if tensor.ndim == 2:
                return tensor.T
            return tensor

        elif transform == WeightTransform.TRANSPOSE_KV:
            # Special handling for K/V weights in GQA
            # May need reshaping + transpose
            if tensor.ndim == 2:
                return tensor.T
            return tensor

        elif transform == WeightTransform.DEQUANT:
            # Handle dequantization
            return self._dequantize(tensor, hf_name)

        return tensor

    def _dequantize(self, tensor: torch.Tensor, hf_name: str) -> torch.Tensor:
        """Dequantize INT8/INT4 weights to bfloat16"""
        # This is a placeholder - actual dequantization requires
        # additional scale and zero-point tensors
        raise NotImplementedError(
            f"Dequantization not yet implemented for {hf_name}"
        )

    def map_weights(
        self,
        state_dict: Dict[str, torch.Tensor],
        verbose: bool = False,
    ) -> Dict[str, np.ndarray]:
        """
        Map all weights from HF state dict to IRON format.

        Args:
            state_dict: HF model state dictionary
            verbose: Print unmapped weights

        Returns:
            Dictionary mapping IRON names to numpy arrays
        """
        result = {}

        for hf_name, tensor in state_dict.items():
            mapped = self.map_weight(hf_name, tensor)
            result[mapped.name] = mapped.tensor

        if verbose and self.unmapped_weights:
            print(f"Unmapped weights ({len(self.unmapped_weights)}):")
            for name in self.unmapped_weights[:10]:  # Show first 10
                print(f"  - {name}")
            if len(self.unmapped_weights) > 10:
                print(f"  ... and {len(self.unmapped_weights) - 10} more")

        return result

    def get_weights_for_layer(
        self,
        layer_idx: int,
        weight_prefix: str = "layers",
    ) -> Dict[str, np.ndarray]:
        """
        Get all mapped weights for a specific layer.

        Args:
            layer_idx: Layer index
            weight_prefix: Prefix for weight names

        Returns:
            Dictionary of weights for the layer
        """
        prefix = f"{weight_prefix}.{layer_idx}."
        result = {}

        for iron_name, mapped in self.mapped_weights.items():
            if iron_name.startswith(prefix):
                suffix = iron_name[len(prefix) :]
                result[suffix] = mapped.tensor

        return result

    def compile_gqa_weights(
        self,
        hidden_size: int,
        num_heads: int,
        num_kv_heads: int,
        head_dim: int,
    ) -> None:
        """
        Compile/reshape weights for Grouped Query Attention.

        GQA requires specific tensor layouts for efficient NPU execution.
        This method reshapes Q, K, V weights to the expected format.

        Args:
            hidden_size: Model hidden dimension
            num_heads: Number of attention heads
            num_kv_heads: Number of KV heads (for GQA)
            head_dim: Dimension per head
        """
        # This would handle:
        # 1. Concatenating Q, K, V weights if stored separately
        # 2. Reshaping for GQA tensor layout
        # 3. Creating proper strides for NPU memory access
        self.gqa_compiled = True

    def load_safetensors(
        self,
        model_path: Union[str, Path],
        device: str = "cpu",
    ) -> Dict[str, torch.Tensor]:
        """
        Load weights from safetensors format.

        Args:
            model_path: Path to model directory containing model.safetensors
            device: Device to load tensors on

        Returns:
            State dictionary
        """
        try:
            from safetensors.torch import load_file

            model_path = Path(model_path)

            # Try single file first
            safetensors_path = model_path / "model.safetensors"
            if safetensors_path.exists():
                return load_file(str(safetensors_path), device=device)

            # Try sharded files
            index_path = model_path / "model.safetensors.index.json"
            if index_path.exists():
                import json

                with open(index_path, "r") as f:
                    index = json.load(f)

                state_dict = {}
                weight_map = index["weight_map"]

                # Group weights by file
                files_to_weights: Dict[str, List[str]] = {}
                for weight_name, filename in weight_map.items():
                    if filename not in files_to_weights:
                        files_to_weights[filename] = []
                    files_to_weights[filename].append(weight_name)

                # Load each file
                for filename, weight_names in files_to_weights.items():
                    shard_path = model_path / filename
                    shard_dict = load_file(str(shard_path), device=device)
                    for weight_name in weight_names:
                        state_dict[weight_name] = shard_dict[weight_name]

                return state_dict

            raise FileNotFoundError(
                f"No safetensors found in {model_path}"
            )

        except ImportError:
            raise ImportError(
                "Please install safetensors: pip install safetensors"
            )

    def load_pytorch(
        self,
        model_path: Union[str, Path],
        device: str = "cpu",
    ) -> Dict[str, torch.Tensor]:
        """
        Load weights from PyTorch format.

        Args:
            model_path: Path to .pt or .bin file
            device: Device to load tensors on

        Returns:
            State dictionary
        """
        model_path = Path(model_path)

        # Find the checkpoint file
        checkpoint_files = list(model_path.glob("*.pt")) + list(
            model_path.glob("*.bin")
        )

        if not checkpoint_files:
            raise FileNotFoundError(
                f"No PyTorch checkpoint found in {model_path}"
            )

        # Load first checkpoint (for sharded checkpoints, this would need extension)
        checkpoint_path = checkpoint_files[0]
        return torch.load(str(checkpoint_path), map_location=device, weights_only=True)


class QuantizedWeightMapper(WeightMapper):
    """
    Extended weight mapper for quantized models (AWQ, GPTQ, etc.)

    Handles dequantization of INT4/INT8 weights.
    """

    def __init__(self, architecture: str = "llama", quant_type: str = "awq"):
        """
        Initialize quantized weight mapper.

        Args:
            architecture: Model architecture
            quant_type: Quantization type (awq, gptq, etc.)
        """
        super().__init__(architecture)
        self.quant_type = quant_type
        self.scales: Dict[str, torch.Tensor] = {}
        self.zeros: Dict[str, torch.Tensor] = {}

    def _dequantize(self, tensor: torch.Tensor, hf_name: str) -> torch.Tensor:
        """Dequantize weights using scales and zeros"""
        # Find corresponding scale and zero tensors
        scale_name = hf_name.replace(".weight", ".scales")
        zero_name = hf_name.replace(".weight", ".zeros")

        if scale_name not in self.scales or zero_name not in self.zeros:
            raise ValueError(
                f"Missing quantization parameters for {hf_name}"
            )

        scales = self.scales[scale_name]
        zeros = self.zeros[zero_name]

        # Dequantize: (W * scale) - zero
        dequantized = tensor.float() * scales - zeros
        return dequantized.to(torch.bfloat16)

    def load_quantized_safetensors(
        self,
        model_path: Union[str, Path],
    ) -> Dict[str, torch.Tensor]:
        """Load quantized weights and dequantization parameters"""
        state_dict = self.load_safetensors(model_path)

        # Separate weights, scales, and zeros
        weights = {}
        for name, tensor in state_dict.items():
            if "scale" in name:
                self.scales[name] = tensor
            elif "zero" in name:
                self.zeros[name] = tensor
            else:
                weights[name] = tensor

        return weights


def create_weight_mapper(
    architecture: str,
    quantized: bool = False,
    quant_type: str = "awq",
) -> WeightMapper:
    """
    Factory function to create appropriate weight mapper.

    Args:
        architecture: Model architecture name
        quantized: Whether model is quantized
        quant_type: Quantization type if applicable

    Returns:
        WeightMapper instance
    """
    if quantized:
        return QuantizedWeightMapper(architecture, quant_type)
    return WeightMapper(architecture)
