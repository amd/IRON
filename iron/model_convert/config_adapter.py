# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Configuration Adapter for HuggingFace Models

This module provides a unified interface for parsing HuggingFace model configurations
and normalizing them into IRON-compatible formats. It handles the various naming
conventions used by different model architectures (Llama, Mistral, Phi, Gemma, etc.)
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, field
from enum import Enum


class ModelArchitecture(Enum):
    """Supported model architectures"""

    LLAMA = "llama"
    MISTRAL = "mistral"
    PHI = "phi"
    GEMMA = "gemma"
    QWEN = "qwen"
    UNKNOWN = "unknown"


class NormType(Enum):
    """Normalization types"""

    RMS_NORM = "rms_norm"
    LAYER_NORM = "layer_norm"


class FFNType(Enum):
    """Feed-forward network types"""

    SWIGLU = "swiglu"
    GEGEU = "geglu"
    MLP = "mlp"
    MOE = "moe"


class AttentionType(Enum):
    """Attention mechanism types"""

    MHA = "mha"  # Multi-head attention
    GQA = "gqa"  # Grouped query attention
    MQA = "mqa"  # Multi-query attention


@dataclass
class NormalizedConfig:
    """
    Normalized model configuration with unified naming conventions.

    This provides a consistent interface regardless of the original
    HuggingFace config format.
    """

    # Model identification
    architecture: ModelArchitecture = ModelArchitecture.UNKNOWN
    model_type: str = ""

    # Core dimensions
    hidden_size: int = 0
    vocab_size: int = 0
    num_hidden_layers: int = 0
    num_attention_heads: int = 0

    # Attention configuration
    num_kv_heads: int = 0  # For GQA/MQA, equals num_attention_heads for MHA
    head_dim: int = 0
    attention_bias: bool = False
    attention_dropout: float = 0.0
    max_position_embeddings: int = 2048

    # RoPE configuration
    rope_theta: float = 10000.0
    rope_scaling: Optional[Dict] = None

    # FFN configuration
    intermediate_size: int = 0
    ffn_type: FFNType = FFNType.MLP
    ffn_bias: bool = False

    # Normalization configuration
    norm_type: NormType = NormType.RMS_NORM
    norm_eps: float = 1e-6
    norm_bias: bool = False

    # Architecture flags
    tie_word_embeddings: bool = False
    use_cache: bool = True

    # NPU-specific configuration (can be overridden)
    npu_config: Dict[str, Any] = field(default_factory=dict)

    # Original config preserved for reference
    original_config: Dict[str, Any] = field(default_factory=dict)

    @property
    def num_kv_groups(self) -> int:
        """Number of KV groups for GQA"""
        if self.num_kv_heads == 0:
            return self.num_attention_heads
        return self.num_attention_heads // self.num_kv_heads

    @property
    def is_gqa(self) -> bool:
        """Whether model uses Grouped Query Attention"""
        return 0 < self.num_kv_heads < self.num_attention_heads

    @property
    def is_mqa(self) -> bool:
        """Whether model uses Multi-Query Attention"""
        return self.num_kv_heads == 1

    @property
    def is_mha(self) -> bool:
        """Whether model uses standard Multi-Head Attention"""
        return self.num_kv_heads == self.num_attention_heads or self.num_kv_heads == 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "architecture": self.architecture.value,
            "model_type": self.model_type,
            "hidden_size": self.hidden_size,
            "vocab_size": self.vocab_size,
            "num_hidden_layers": self.num_hidden_layers,
            "num_attention_heads": self.num_attention_heads,
            "num_kv_heads": self.num_kv_heads or self.num_attention_heads,
            "head_dim": self.head_dim or (self.hidden_size // self.num_attention_heads),
            "intermediate_size": self.intermediate_size,
            "norm_type": self.norm_type.value,
            "norm_eps": self.norm_eps,
            "ffn_type": self.ffn_type.value,
            "rope_theta": self.rope_theta,
            "max_position_embeddings": self.max_position_embeddings,
            "tie_word_embeddings": self.tie_word_embeddings,
            "use_cache": self.use_cache,
            "npu_config": self.npu_config,
        }


class ConfigAdapter:
    """
    Adapter for converting HuggingFace model configurations to IRON format.

    Handles the various naming conventions used by different model families
    and normalizes them into a unified configuration format.
    """

    # Mapping of architecture types to their HuggingFace identifiers
    ARCHITECTURE_MAP = {
        "LlamaForCausalLM": ModelArchitecture.LLAMA,
        "MistralForCausalLM": ModelArchitecture.MISTRAL,
        "MixtralForCausalLM": ModelArchitecture.MISTRAL,
        "PhiForCausalLM": ModelArchitecture.PHI,
        "Phi3ForCausalLM": ModelArchitecture.PHI,
        "GemmaForCausalLM": ModelArchitecture.GEMMA,
        "Qwen2ForCausalLM": ModelArchitecture.QWEN,
        "RWForCausalLM": ModelArchitecture.LLAMA,  # Falcon uses Llama architecture
        "BaichuanForCausalLM": ModelArchitecture.LLAMA,
    }

    # Key mappings for normalizing config keys
    HIDDEN_SIZE_KEYS = ["hidden_size", "emb_dim", "n_embd", "d_model"]
    VOCAB_SIZE_KEYS = ["vocab_size", "padded_vocab_size", "n_vocab"]
    NUM_LAYERS_KEYS = ["num_hidden_layers", "n_layers", "num_layers", "n_layer"]
    NUM_HEADS_KEYS = ["num_attention_heads", "n_heads", "num_heads", "n_head"]
    NUM_KV_HEADS_KEYS = [
        "num_key_value_heads",
        "n_kv_heads",
        "num_kv_heads",
        "num_kv_groups",
    ]
    INTERMEDIATE_SIZE_KEYS = [
        "intermediate_size",
        "ffn_hidden_size",
        "n_inner",
        "hidden_dim",
    ]
    NORM_EPS_KEYS = [
        "rms_norm_eps",
        "layer_norm_eps",
        "norm_eps",
        "layernorm_epsilon",
        "layer_norm_epsilon",
    ]
    ROPE_THETA_KEYS = ["rope_theta", "rotary_emb_base", "rope_base", "theta"]
    MAX_POS_KEYS = ["max_position_embeddings", "n_ctx", "max_seq_len", "context_length"]

    def __init__(self, config: Optional[Union[Dict, str, Path]] = None):
        """
        Initialize the config adapter.

        Args:
            config: Either a dictionary, path to config.json, or None for empty config
        """
        self.raw_config: Dict[str, Any] = {}

        if config is not None:
            if isinstance(config, (str, Path)):
                self.load_from_file(config)
            elif isinstance(config, dict):
                self.raw_config = config.copy()

    def load_from_file(self, path: Union[str, Path]) -> None:
        """Load config from JSON file"""
        path = Path(path)
        with open(path, "r") as f:
            self.raw_config = json.load(f)

    def _get_value(self, keys: List[str], default: Any = None) -> Any:
        """Get value from config trying multiple possible keys"""
        for key in keys:
            if key in self.raw_config:
                return self.raw_config[key]
            # Try with variations
            if key.startswith("n_"):
                alt_key = key[2:]  # Remove n_ prefix
                if alt_key in self.raw_config:
                    return self.raw_config[alt_key]
        return default

    def _detect_architecture(self) -> ModelArchitecture:
        """Detect model architecture from config"""
        arch_key = self._get_value(["architectures", "model_type", "auto_map"])

        if isinstance(arch_key, list):
            arch_key = arch_key[0] if arch_key else ""

        # Direct mapping
        if arch_key in self.ARCHITECTURE_MAP:
            return self.ARCHITECTURE_MAP[arch_key]

        # Check model_type string
        model_type = self.raw_config.get("model_type", "").lower()
        if "llama" in model_type or "lla" in model_type:
            return ModelArchitecture.LLAMA
        elif "mistral" in model_type:
            return ModelArchitecture.MISTRAL
        elif "phi" in model_type:
            return ModelArchitecture.PHI
        elif "gemma" in model_type:
            return ModelArchitecture.GEMMA
        elif "qwen" in model_type:
            return ModelArchitecture.QWEN

        return ModelArchitecture.UNKNOWN

    def _detect_norm_type(self) -> NormType:
        """Detect normalization type from config"""
        # Check for RMSNorm indicators
        if any(key in self.raw_config for key in ["rms_norm_eps"]):
            return NormType.RMS_NORM

        # Check for LayerNorm indicators
        if any(
            key in self.raw_config for key in ["layer_norm_eps", "layernorm_epsilon"]
        ):
            return NormType.LAYER_NORM

        # Architecture-based defaults
        arch = self._detect_architecture()
        if arch == ModelArchitecture.PHI:
            return NormType.LAYER_NORM
        return NormType.RMS_NORM

    def _detect_ffn_type(self) -> FFNType:
        """Detect feed-forward network type from config"""
        arch = self._detect_architecture()

        # Check for MoE
        if "num_experts" in self.raw_config or "moe_config" in self.raw_config:
            return FFNType.MOE

        # Architecture-based defaults
        if arch in [ModelArchitecture.LLAMA, ModelArchitecture.MISTRAL]:
            return FFNType.SWIGLU
        elif arch == ModelArchitecture.PHI:
            return FFNType.GEGEU

        return FFNType.MLP

    def normalize(self) -> NormalizedConfig:
        """
        Convert raw HuggingFace config to normalized IRON config.

        Returns:
            NormalizedConfig with unified naming conventions
        """
        architecture = self._detect_architecture()

        # Extract core dimensions
        hidden_size = self._get_value(self.HIDDEN_SIZE_KEYS, 0)
        num_heads = self._get_value(self.NUM_HEADS_KEYS, 0)

        # Calculate derived values
        head_dim = self._get_value(["head_dim", "d_head"])
        if head_dim is None and hidden_size > 0 and num_heads > 0:
            head_dim = hidden_size // num_heads

        num_kv_heads = self._get_value(self.NUM_KV_HEADS_KEYS, 0)
        if num_kv_heads == 0:
            # Check for explicit GQA config
            gqa_ratio = self._get_value(["gqa_ratio", "num_kv_groups"])
            if gqa_ratio and num_heads > 0:
                num_kv_heads = num_heads // gqa_ratio
            else:
                num_kv_heads = num_heads  # Default to MHA

        intermediate_size = self._get_value(self.INTERMEDIATE_SIZE_KEYS, 0)

        # Handle Llama-3.2 style config
        if "llama3_config" in self.raw_config:
            llama3_cfg = self.raw_config["llama3_config"]
            if isinstance(llama3_cfg, dict):
                if intermediate_size == 0:
                    intermediate_size = llama3_cfg.get("ffn_hidden_size", 0)

        config = NormalizedConfig(
            architecture=architecture,
            model_type=self.raw_config.get("model_type", ""),
            hidden_size=hidden_size,
            vocab_size=self._get_value(self.VOCAB_SIZE_KEYS, 0),
            num_hidden_layers=self._get_value(self.NUM_LAYERS_KEYS, 0),
            num_attention_heads=num_heads,
            num_kv_heads=num_kv_heads,
            head_dim=head_dim,
            attention_bias=self._get_value(["attention_bias", "bias"], False),
            attention_dropout=self._get_value(["attention_dropout", "attn_pdrop"], 0.0),
            max_position_embeddings=self._get_value(self.MAX_POS_KEYS, 2048),
            rope_theta=self._get_value(self.ROPE_THETA_KEYS, 10000.0),
            rope_scaling=self.raw_config.get("rope_scaling"),
            intermediate_size=intermediate_size,
            ffn_type=self._detect_ffn_type(),
            ffn_bias=self._get_value(["ffn_bias", "mlp_bias"], False),
            norm_type=self._detect_norm_type(),
            norm_eps=self._get_value(self.NORM_EPS_KEYS, 1e-6),
            norm_bias=False,
            tie_word_embeddings=self._get_value(
                ["tie_word_embeddings", "tie_embeddings"], False
            ),
            use_cache=True,
            original_config=self.raw_config.copy(),
        )

        return config

    def get_iron_config(self, **npu_overrides) -> Dict[str, Any]:
        """
        Get configuration dictionary suitable for IRON operators.

        Args:
            **npu_overrides: NPU-specific configuration overrides

        Returns:
            Dictionary with IRON-compatible configuration
        """
        normalized = self.normalize()

        # Build IRON config with sensible defaults
        iron_config = {
            "emb_dim": normalized.hidden_size,
            "vocab_size": normalized.vocab_size,
            "n_layers": normalized.num_hidden_layers,
            "n_heads": normalized.num_attention_heads,
            "n_kv_groups": normalized.num_kv_heads,
            "context_length": normalized.max_position_embeddings,
            "rope_base": normalized.rope_theta,
            "dtype": "bfloat16",
            # Default NPU operator settings (all disabled by default)
            "use_aie_rope": False,
            "use_aie_attn_projection_gemm": False,
            "use_aie_fused_mha": False,
            "use_aie_gqa_gemv": False,
            "use_aie_ffn_gemm": False,
            "use_aie_ffn_silu": False,
            "use_aie_ffn_swiglu": False,
            "use_aie_norm1": False,
            "use_aie_norm2": False,
            "use_aie_final_norm": False,
            "use_aie_final_gemm": False,
            # Apply NPU overrides
            **npu_overrides,
        }

        # Add RoPE frequency config if available
        if normalized.rope_scaling:
            iron_config["rope_freq"] = normalized.rope_scaling

        return iron_config


def load_hf_config(config_path: Union[str, Path, Dict]) -> NormalizedConfig:
    """
    Convenience function to load and normalize a HuggingFace config.

    Args:
        config_path: Path to config.json or config dictionary

    Returns:
        NormalizedConfig object
    """
    adapter = ConfigAdapter(config_path)
    return adapter.normalize()


def get_iron_ready_config(
    config_path: Union[str, Path, Dict], **kwargs
) -> Dict[str, Any]:
    """
    Convenience function to get an IRON-ready configuration.

    Args:
        config_path: Path to config.json or config dictionary
        **kwargs: Additional NPU configuration options

    Returns:
        Dictionary ready to use with IRON model classes
    """
    adapter = ConfigAdapter(config_path)
    return adapter.get_iron_config(**kwargs)
