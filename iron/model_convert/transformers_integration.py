# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
HuggingFace Transformers Integration for Model Scanning

This module provides direct integration with the HuggingFace Transformers library
to accurately scan model architectures by:
1. Loading configuration directly from transformers.models.<type>
2. Inspecting modeling files for exact layer types
3. Extracting architecture details programmatically

This is MORE accurate than AST parsing because it uses the actual classes.
"""

import importlib
import inspect
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple
import logging

logger = logging.getLogger(__name__)


# Mapping of architecture names to transformers module paths
ARCHITECTURE_MODULE_MAP = {
    "LlamaForCausalLM": "transformers.models.llama",
    "MistralForCausalLM": "transformers.models.mistral",
    "MixtralForCausalLM": "transformers.models.mixtral",
    "Qwen2ForCausalLM": "transformers.models.qwen2",
    "Qwen3_5_MoEForCausalLM": "transformers.models.qwen3_5_moe",
    "Qwen3OmniMoeForCausalLM": "transformers.models.qwen3_omni_moe",
    "GemmaForCausalLM": "transformers.models.gemma",
    "PhiForCausalLM": "transformers.models.phi",
    "Phi3ForCausalLM": "transformers.models.phi3",
    "GPT2LMHeadModel": "transformers.models.gpt2",
    "OPTForCausalLM": "transformers.models.opt",
    "FalconForCausalLM": "transformers.models.falcon",
    "MambaForCausalLM": "transformers.models.mamba",
    "StarCoder2ForCausalLM": "transformers.models.starcoder2",
}


@dataclass
class TransformerModelInfo:
    """Information extracted from Transformers library"""
    model_type: str
    architecture_name: str
    config_class: str
    modeling_module: str

    # Architecture details from config
    config_dict: Dict[str, Any] = field(default_factory=dict)

    # Discovered layer classes
    layer_classes: List[Dict[str, Any]] = field(default_factory=list)

    # Special features detected
    has_sliding_window: bool = False
    has_moe: bool = False
    has_rope: bool = False
    has_qk_norm: bool = False
    attention_type: str = "unknown"
    ffn_type: str = "unknown"

    # Support assessment
    is_known_architecture: bool = True
    support_notes: str = ""


class TransformersScanner:
    """
    Scanner that uses the Transformers library directly to analyze models.

    This is the PREFERRED scanning method when the model architecture is
    already supported by Transformers.

    Example usage:
        scanner = TransformersScanner()
        info = scanner.scan_from_hf_hub("Qwen/Qwen3.5-27B")
        print(info.has_moe)  # True
        print(info.has_sliding_window)  # True
    """

    def __init__(self):
        self._config_cache: Dict[str, Any] = {}
        self._module_cache: Dict[str, Any] = {}

    def scan_from_hf_hub(
        self,
        model_name: str,
        trust_remote_code: bool = False,
    ) -> TransformerModelInfo:
        """
        Scan a model directly from HuggingFace Hub.

        Args:
            model_name: HuggingFace model name (e.g., "Qwen/Qwen3.5-27B")
            trust_remote_code: Whether to trust custom code from HF Hub

        Returns:
            TransformerModelInfo with architecture details
        """
        try:
            from transformers import AutoConfig
            from huggingface_hub import HfApi

            # Load config
            config = AutoConfig.from_pretrained(
                model_name,
                trust_remote_code=trust_remote_code,
            )

            return self._extract_info_from_config(config, model_name)

        except ImportError as e:
            logger.error(f"Transformers library required: {e}")
            raise
        except Exception as e:
            logger.warning(f"Could not scan from HF Hub: {e}")
            raise

    def scan_from_local(
        self,
        config_path: str,
        trust_remote_code: bool = False,
    ) -> TransformerModelInfo:
        """
        Scan a model from local config file.

        Args:
            config_path: Path to config.json
            trust_remote_code: Whether to trust custom code

        Returns:
            TransformerModelInfo with architecture details
        """
        try:
            from transformers import AutoConfig

            config = AutoConfig.from_pretrained(
                config_path,
                trust_remote_code=trust_remote_code,
            )

            return self._extract_info_from_config(config, config_path)

        except Exception as e:
            logger.warning(f"Could not load local config: {e}")
            raise

    def _extract_info_from_config(
        self,
        config,
        source: str,
    ) -> TransformerModelInfo:
        """Extract detailed info from a Transformers config object"""

        # Get architecture name
        architectures = getattr(config, "architectures", [])
        arch_name = architectures[0] if architectures else "Unknown"

        # Get model type
        model_type = getattr(config, "model_type", "unknown")

        # Find the transformers module for this architecture
        modeling_module = self._get_modeling_module(arch_name)

        # Extract config values
        config_dict = self._extract_config_values(config)

        # Create info object
        info = TransformerModelInfo(
            model_type=model_type,
            architecture_name=arch_name,
            config_class=type(config).__name__,
            modeling_module=modeling_module,
            config_dict=config_dict,
        )

        # Detect special features
        info.has_sliding_window = self._detect_sliding_window(config)
        info.has_moe = self._detect_moe(config)
        info.has_rope = self._detect_rope(config)
        info.has_qk_norm = self._detect_qk_norm(config)
        info.attention_type = self._determine_attention_type(config)
        info.ffn_type = self._determine_ffn_type(config)

        # Get layer classes from modeling module
        if modeling_module:
            info.layer_classes = self._extract_layer_classes(modeling_module)

        # Check if this is a known architecture
        info.is_known_architecture = arch_name in ARCHITECTURE_MODULE_MAP

        return info

    def _extract_config_values(self, config) -> Dict[str, Any]:
        """Extract relevant config values"""
        values = {}

        # Basic architecture
        for attr in [
            "hidden_size", "num_attention_heads", "num_hidden_layers",
            "intermediate_size", "vocab_size", "max_position_embeddings",
            "num_key_value_heads", "head_dim",
        ]:
            if hasattr(config, attr):
                values[attr] = getattr(config, attr)

        # Normalization
        if hasattr(config, "rms_norm_eps"):
            values["rms_norm_eps"] = config.rms_norm_eps
        if hasattr(config, "layer_norm_eps"):
            values["layer_norm_eps"] = config.layer_norm_eps

        # RoPE
        if hasattr(config, "rope_theta"):
            values["rope_theta"] = config.rope_theta
        if hasattr(config, "rope_scaling"):
            values["rope_scaling"] = config.rope_scaling

        # MoE-specific
        if hasattr(config, "num_experts"):
            values["num_experts"] = config.num_experts
        if hasattr(config, "num_experts_per_tok"):
            values["num_experts_per_tok"] = config.num_experts_per_tok
        if hasattr(config, "expert_intermediate_size"):
            values["expert_intermediate_size"] = config.expert_intermediate_size

        # Attention-specific
        if hasattr(config, "sliding_window"):
            values["sliding_window"] = config.sliding_window
        if hasattr(config, "attention_bias"):
            values["attention_bias"] = config.attention_bias
        if hasattr(config, "qk_norm"):
            values["qk_norm"] = config.qk_norm

        return values

    def _detect_sliding_window(self, config) -> bool:
        """Detect if model uses sliding window attention"""
        if hasattr(config, "sliding_window") and config.sliding_window is not None:
            return config.sliding_window > 0

        # Check for window size in various forms
        for attr in ["window_size", "local_window_size", "attention_window"]:
            if hasattr(config, attr):
                val = getattr(config, attr)
                if val is not None and val > 0:
                    return True

        return False

    def _detect_moe(self, config) -> bool:
        """Detect if model uses MoE (Mixture of Experts)"""
        # Check architecture name
        arch_names = getattr(config, "architectures", [])
        for name in arch_names:
            if "moe" in name.lower() or "MoE" in name:
                return True

        # Check for expert-related config
        if hasattr(config, "num_experts") and config.num_experts > 1:
            return True

        if hasattr(config, "num_experts_per_tok"):
            return True

        # Check model type
        model_type = getattr(config, "model_type", "")
        if "moe" in model_type.lower():
            return True

        return False

    def _detect_rope(self, config) -> bool:
        """Detect if model uses RoPE embeddings"""
        # Most modern LLMs use RoPE
        if hasattr(config, "rope_theta"):
            return True

        if hasattr(config, "rotary_emb"):
            return True

        # Check for explicit positional embedding type
        if hasattr(config, "position_embedding_type"):
            return config.position_embedding_type == "rotary"

        # Default to True for known RoPE architectures
        model_type = getattr(config, "model_type", "").lower()
        rope_models = ["llama", "mistral", "qwen", "phi", "gemma"]
        return any(m in model_type for m in rope_models)

    def _detect_qk_norm(self, config) -> bool:
        """Detect if model uses QK normalization"""
        if hasattr(config, "qk_norm"):
            return config.qk_norm

        # Qwen models typically have QK norm
        model_type = getattr(config, "model_type", "").lower()
        return "qwen" in model_type

    def _determine_attention_type(self, config) -> str:
        """Determine the attention mechanism type"""
        num_heads = getattr(config, "num_attention_heads", 0)
        num_kv_heads = getattr(config, "num_key_value_heads", num_heads)

        if num_heads == num_kv_heads:
            return "mha"  # Multi-head attention
        elif num_kv_heads == 1:
            return "mqa"  # Multi-query attention
        else:
            return "gqa"  # Grouped query attention

    def _determine_ffn_type(self, config) -> str:
        """Determine the feed-forward network type"""
        # Check for SwiGLU variant
        model_type = getattr(config, "model_type", "").lower()

        if "llama" in model_type or "mistral" in model_type:
            return "swiglu"
        elif "gemma" in model_type:
            return "geglu"
        elif "phi" in model_type:
            return "gelu"
        elif "qwen" in model_type:
            return "silu"

        # Check intermediate size pattern (SwiGLU often has specific ratios)
        hidden = getattr(config, "hidden_size", 0)
        intermediate = getattr(config, "intermediate_size", 0)

        if intermediate > hidden * 3:
            return "swiglu"  # SwiGLU typically has larger intermediate

        return "mlp"

    def _get_modeling_module(self, arch_name: str) -> Optional[str]:
        """Get the transformers modeling module for an architecture"""
        # Check our map
        if arch_name in ARCHITECTURE_MODULE_MAP:
            return ARCHITECTURE_MODULE_MAP[arch_name]

        # Try to infer from architecture name
        model_type = arch_name.lower()
        for pattern, module in ARCHITECTURE_MODULE_MAP.items():
            if pattern.lower().replace("forcausallm", "") in model_type:
                return module

        return None

    def _extract_layer_classes(self, module_path: str) -> List[Dict[str, Any]]:
        """Extract layer class information from a transformers module"""
        layers = []

        try:
            modeling = importlib.import_module(f"{module_path}.modeling_{module_path.split('.')[-1]}")

            # Find all classes in the module
            for name, obj in inspect.getmembers(modeling, inspect.isclass):
                # Check if it's a layer class
                if self._is_layer_class(obj):
                    layers.append({
                        "name": name,
                        "module": module_path,
                        "category": self._categorize_layer(name),
                        "signature": self._get_class_signature(obj),
                    })

        except Exception as e:
            logger.warning(f"Could not extract layers from {module_path}: {e}")

        return layers

    def _is_layer_class(self, cls) -> bool:
        """Check if a class is a layer/module class"""
        import torch.nn as nn

        # Check if it's a nn.Module subclass
        try:
            if issubclass(cls, nn.Module):
                # Filter out base classes
                name = cls.__name__
                if any(x in name.lower() for x in ["layer", "attention", "norm", "embedding", "block", "mlp", "mo"]):
                    return True
        except TypeError:
            pass

        return False

    def _categorize_layer(self, name: str) -> str:
        """Categorize a layer by its name"""
        name_lower = name.lower()

        if "attention" in name_lower:
            return "attention"
        elif "norm" in name_lower:
            return "normalization"
        elif "mlp" in name_lower or "ffn" in name_lower or "feedforward" in name_lower:
            return "linear"
        elif "embedding" in name_lower:
            return "embedding"
        elif "moe" in name_lower or "expert" in name_lower:
            return "moe"
        elif "rope" in name_lower or "rotary" in name_lower:
            return "positional"
        else:
            return "other"

    def _get_class_signature(self, cls) -> Dict[str, Any]:
        """Get the constructor signature for a class"""
        try:
            sig = inspect.signature(cls.__init__)
            params = {}
            for name, param in sig.parameters.items():
                if name == "self":
                    continue
                params[name] = {
                    "default": str(param.default) if param.default != inspect.Parameter.empty else None,
                    "annotation": str(param.annotation) if param.annotation != inspect.Parameter.empty else None,
                }
            return params
        except Exception:
            return {}


def scan_model_from_transformers(
    model_name: str,
    trust_remote_code: bool = False,
) -> TransformerModelInfo:
    """
    Convenience function to scan a model using Transformers.

    Args:
        model_name: HuggingFace model name
        trust_remote_code: Whether to trust custom code

    Returns:
        TransformerModelInfo
    """
    scanner = TransformersScanner()
    return scanner.scan_from_hf_hub(model_name, trust_remote_code)


def get_architecture_summary(model_name: str) -> str:
    """
    Get a human-readable summary of a model's architecture.

    Args:
        model_name: HuggingFace model name

    Returns:
        Formatted summary string
    """
    scanner = TransformersScanner()
    info = scanner.scan_from_hf_hub(model_name)

    lines = [
        f"Architecture Summary: {info.architecture_name}",
        "=" * 60,
        f"Model Type: {info.model_type}",
        f"Config Class: {info.config_class}",
        "",
        "Architecture Details:",
        f"  Hidden Size: {info.config_dict.get('hidden_size', 'N/A')}",
        f"  Attention Heads: {info.config_dict.get('num_attention_heads', 'N/A')}",
        f"  KV Heads: {info.config_dict.get('num_key_value_heads', 'N/A')}",
        f"  Layers: {info.config_dict.get('num_hidden_layers', 'N/A')}",
        f"  Intermediate Size: {info.config_dict.get('intermediate_size', 'N/A')}",
        "",
        "Special Features:",
        f"  Sliding Window: {'Yes' if info.has_sliding_window else 'No'}",
        f"  MoE: {'Yes' if info.has_moe else 'No'}",
        f"  RoPE: {'Yes' if info.has_rope else 'No'}",
        f"  QK Norm: {'Yes' if info.has_qk_norm else 'No'}",
        "",
        f"Attention Type: {info.attention_type}",
        f"FFN Type: {info.ffn_type}",
        "",
        "Layer Classes:" if info.layer_classes else "No layer classes found:",
    ]

    for layer in info.layer_classes[:10]:
        lines.append(f"  - {layer['name']} ({layer['category']})")

    return "\n".join(lines)
