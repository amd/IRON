# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Model Architecture Scanner

This module provides tools for introspecting HuggingFace model architectures
to extract their structural requirements, layer types, and operational needs.
It analyzes both configuration files AND model code to build a comprehensive
understanding of what a model requires.

Key capabilities:
- Parse model config.json for basic architecture info
- Analyze modeling_*.py code to extract layer types
- Identify novel/unknown components not in IRON's registry
- Build detailed capability requirements
"""

import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class LayerCategory(Enum):
    """Categories of neural network layers"""

    ATTENTION = "attention"
    NORMALIZATION = "normalization"
    ACTIVATION = "activation"
    LINEAR = "linear"
    CONVOLUTION = "convolution"
    EMBEDDING = "embedding"
    POSITIONAL = "positional"
    POOLING = "pooling"
    NORMALIZATION_SEQUENCE = "norm_sequence"
    CUSTOM = "custom"
    UNKNOWN = "unknown"


class AttentionType(Enum):
    """Types of attention mechanisms"""

    MHA = "mha"  # Multi-head attention
    GQA = "gqa"  # Grouped query attention
    MQA = "mqa"  # Multi-query attention
    FUSED = "fused_mha"  # Fused MHA kernel
    SLIDING_WINDOW = "sliding_window"
    LOCAL = "local"
    FLASH = "flash_attention"
    CUSTOM = "custom"


class NormType(Enum):
    """Types of normalization"""

    LAYER_NORM = "layer_norm"
    RMS_NORM = "rms_norm"
    BATCH_NORM = "batch_norm"
    INSTANCE_NORM = "instance_norm"
    GROUP_NORM = "group_norm"
    CUSTOM = "custom"


class ActivationType(Enum):
    """Types of activation functions"""

    RELU = "relu"
    GELU = "gelu"
    SILU = "silu"
    SWISH = "swish"
    TANH = "tanh"
    SOFTMAX = "softmax"
    NONE = "none"
    CUSTOM = "custom"


@dataclass
class LayerInfo:
    """Information about a specific layer type"""

    name: str
    category: LayerCategory
    module_path: str
    parameters: Dict[str, Any] = field(default_factory=dict)
    sub_layers: List[str] = field(default_factory=list)
    is_supported: bool = False
    support_notes: str = ""


@dataclass
class AttentionInfo:
    """Information about attention mechanism"""

    attention_type: AttentionType
    num_heads: int = 0
    num_kv_heads: int = 0
    head_dim: int = 0
    use_bias: bool = False
    use_qkv_bias: bool = False
    sliding_window: Optional[int] = None
    use_attention_mask: bool = True
    has_rotary_embeddings: bool = False
    rotary_config: Dict[str, Any] = field(default_factory=dict)
    custom_params: Dict[str, Any] = field(default_factory=dict)


@dataclass
class FFNInfo:
    """Information about feed-forward network"""

    ffn_type: str = "mlp"  # mlp, swiglu, geglu, moe
    hidden_size: int = 0
    intermediate_size: int = 0
    activation: ActivationType = ActivationType.NONE
    use_bias: bool = False
    num_experts: int = 0
    top_k_experts: int = 0
    moe_aux_loss: float = 0.0
    custom_params: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ArchitectureRequirements:
    """Complete architectural requirements for a model"""

    # Model identification
    model_name: str = ""
    model_type: str = ""
    architectures: List[str] = field(default_factory=list)

    # Core dimensions
    hidden_size: int = 0
    vocab_size: int = 0
    max_position_embeddings: int = 0
    num_hidden_layers: int = 0

    # Attention
    attention: Optional[AttentionInfo] = None

    # FFN
    ffn: Optional[FFNInfo] = None

    # Normalization
    norm_type: NormType = NormType.RMS_NORM
    norm_eps: float = 1e-6

    # Positional embeddings
    positional_embedding_type: str = "learned"
    rotary_config: Dict[str, Any] = field(default_factory=dict)

    # Discovered layers
    discovered_layers: List[LayerInfo] = field(default_factory=list)

    # Unsupported components
    unsupported_components: List[str] = field(default_factory=list)

    # Special features
    special_features: List[str] = field(default_factory=list)

    # Model-specific config
    raw_config: Dict[str, Any] = field(default_factory=dict)

    @property
    def support_summary(self) -> Dict[str, Any]:
        """Get summary of support status"""
        supported = len([l for l in self.discovered_layers if l.is_supported])
        total = len(self.discovered_layers)
        return {
            "supported_layers": supported,
            "total_layers": total,
            "support_percentage": (supported / total * 100) if total > 0 else 0,
            "unsupported_components": self.unsupported_components,
            "special_features": self.special_features,
        }


class ModelCodeAnalyzer(ast.NodeVisitor):
    """
    AST-based analyzer for PyTorch model code.

    Visits the AST of modeling files to extract:
    - Class definitions and inheritance
    - Module instantiations
    - Function calls (especially F.something for functionals)
    - Control flow that might indicate special handling
    """

    def __init__(self):
        self.layers: List[LayerInfo] = []
        self.attention_patterns: List[str] = []
        self.norm_patterns: List[str] = []
        self.activation_patterns: List[str] = []
        self.imports: Dict[str, str] = {}
        self.class_defs: Dict[str, Dict] = {}
        self.function_calls: List[str] = []
        self.module_attributes: Dict[str, str] = {}

    def visit_Import(self, node):
        for alias in node.names:
            self.imports[alias.name] = alias.asname or alias.name
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        module = node.module or ""
        for alias in node.names:
            full_name = f"{module}.{alias.name}"
            local_name = alias.asname or alias.name
            self.imports[local_name] = full_name
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """Capture class definitions"""
        bases = [self._get_base_name(base) for base in node.bases]

        self.class_defs[node.name] = {
            "name": node.name,
            "bases": bases,
            "is_module": any("Module" in b for b in bases),
            "line_number": node.lineno,
        }

        # Check if this is a Module subclass
        if any("Module" in b for b in bases):
            self._analyze_module_class(node)

        self.generic_visit(node)

    def _get_base_name(self, node):
        """Extract base class name from AST node"""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return ast.unparse(node)
        return ""

    def _analyze_module_class(self, node):
        """Analyze a nn.Module subclass for layer instantiations"""
        for item in node.body:
            if isinstance(item, ast.Assign):
                # Look for self.layer_name = ModuleType(...)
                self._analyze_assignment(item)
            elif isinstance(item, ast.FunctionDef):
                # Look for layer usage in methods
                self._analyze_method(item)

    def _analyze_assignment(self, node):
        """Analyze assignments for module instantiations"""
        if not isinstance(node.targets[0], ast.Attribute):
            return

        target = node.targets[0]
        if not (isinstance(target.value, ast.Name) and target.value.id == "self"):
            return

        attr_name = target.attr

        # Get the instantiated module type
        if isinstance(node.value, ast.Call):
            module_type = self._get_call_name(node.value)
            kwargs = self._get_call_kwargs(node.value)

            self.module_attributes[attr_name] = module_type

            # Categorize the layer
            category = self._categorize_module(module_type)
            if category != LayerCategory.UNKNOWN:
                self.layers.append(
                    LayerInfo(
                        name=attr_name,
                        category=category,
                        module_path=module_type,
                        parameters=kwargs,
                    )
                )

    def _analyze_method(self, node):
        """Analyze method for layer usage patterns"""
        if node.name == "forward":
            for child in ast.walk(node):
                if isinstance(child, ast.Call):
                    func_name = self._get_call_name(child)
                    self.function_calls.append(func_name)

                    # Check for functional activations
                    if func_name.startswith("F."):
                        self.activation_patterns.append(func_name)
                    # Check for torch operations
                    elif func_name.startswith("torch.") or func_name.startswith("nn."):
                        pass  # Standard operations

    def _get_call_name(self, node):
        """Get the function/module name from a Call node"""
        if isinstance(node.func, ast.Name):
            return node.func.id
        elif isinstance(node.func, ast.Attribute):
            return ast.unparse(node.func)
        return ""

    def _get_call_kwargs(self, node):
        """Extract keyword arguments from a Call node"""
        kwargs = {}
        for kw in node.keywords:
            if kw.arg:
                try:
                    kwargs[kw.arg] = ast.literal_eval(kw.value)
                except (ValueError, TypeError):
                    kwargs[kw.arg] = "<dynamic>"
        return kwargs

    def _categorize_module(self, module_type: str) -> LayerCategory:
        """Categorize a module type"""
        module_lower = module_type.lower()

        # Attention
        if any(x in module_lower for x in ["attention", "mha", "multihead"]):
            return LayerCategory.ATTENTION

        # Normalization
        if any(
            x in module_lower for x in ["norm", "layernorm", "rmsnorm", "batchnorm"]
        ):
            return LayerCategory.NORMALIZATION

        # Activation
        if any(
            x in module_lower
            for x in ["relu", "gelu", "silu", "swish", "tanh", "softmax", "sigmoid"]
        ):
            return LayerCategory.ACTIVATION

        # Linear
        if "linear" in module_lower or module_lower in ["dense"]:
            return LayerCategory.LINEAR

        # Convolution
        if any(x in module_lower for x in ["conv", "conv1d", "conv2d"]):
            return LayerCategory.CONVOLUTION

        # Embedding
        if "embed" in module_lower:
            return LayerCategory.EMBEDDING

        # Positional
        if any(x in module_lower for x in ["rope", "rotary", "positional"]):
            return LayerCategory.POSITIONAL

        # Pooling
        if any(x in module_lower for x in ["pool", "avgpool", "maxpool"]):
            return LayerCategory.POOLING

        return LayerCategory.UNKNOWN


class ArchitectureScanner:
    """
    Scanner for extracting architectural requirements from HF models.

    Analyzes:
    1. config.json - Basic architecture parameters
    2. modeling_*.py - Actual layer implementations
    3. configuration_*.py - Custom configuration logic

    Outputs ArchitectureRequirements with complete layer inventory.
    """

    # Known architecture patterns
    ATTENTION_MODULE_PATTERNS = {
        "attention": AttentionType.MHA,
        "mha": AttentionType.MHA,
        "grouped_query": AttentionType.GQA,
        "gqa": AttentionType.GQA,
        "multi_query": AttentionType.MQA,
        "mqa": AttentionType.MQA,
        "fused_attention": AttentionType.FUSED,
        "flash_attention": AttentionType.FLASH,
        "sliding_window": AttentionType.SLIDING_WINDOW,
    }

    NORM_MODULE_PATTERNS = {
        "layernorm": NormType.LAYER_NORM,
        "layer_norm": NormType.LAYER_NORM,
        "rmsnorm": NormType.RMS_NORM,
        "rms_norm": NormType.RMS_NORM,
        "batchnorm": NormType.BATCH_NORM,
        "batch_norm": NormType.BATCH_NORM,
    }

    ACTIVATION_MODULE_PATTERNS = {
        "relu": ActivationType.RELU,
        "gelu": ActivationType.GELU,
        "silu": ActivationType.SILU,
        "swish": ActivationType.SWISH,
        "tanh": ActivationType.TANH,
        "softmax": ActivationType.SOFTMAX,
    }

    def __init__(self, model_path: str):
        """
        Initialize scanner for a model.

        Args:
            model_path: Path to model directory or HF model name
        """
        self.model_path = Path(model_path)
        self.config_path = self.model_path / "config.json"

        # Results
        self.requirements = ArchitectureRequirements()
        self.code_analyzer = ModelCodeAnalyzer()

    def scan(self) -> ArchitectureRequirements:
        """
        Perform complete architecture scan.

        Returns:
            ArchitectureRequirements object
        """
        logger.info(f"Scanning model at {self.model_path}")

        # Step 1: Parse config.json
        if self.config_path.exists():
            self._scan_config()
        else:
            logger.warning(f"config.json not found at {self.model_path}")

        # Step 2: Find and analyze modeling code
        self._scan_modeling_code()

        # Step 3: Categorize and analyze discovered layers
        self._analyze_discovered_layers()

        # Step 4: Check for special features
        self._detect_special_features()

        return self.requirements

    def _scan_config(self):
        """Parse config.json for basic architecture info"""
        with open(self.config_path, "r") as f:
            config = json.load(f)

        self.requirements.raw_config = config
        self.requirements.model_type = config.get("model_type", "unknown")
        self.requirements.model_name = config.get("name_or_path", str(self.model_path))
        self.requirements.architectures = config.get("architectures", [])

        # Core dimensions
        self.requirements.hidden_size = self._get_config_value(
            config, ["hidden_size", "emb_dim", "n_embd", "d_model"]
        )
        self.requirements.vocab_size = self._get_config_value(
            config, ["vocab_size", "padded_vocab_size", "n_vocab"]
        )
        self.requirements.max_position_embeddings = self._get_config_value(
            config, ["max_position_embeddings", "n_ctx", "n_positions", "max_seq_len"]
        )
        self.requirements.num_hidden_layers = self._get_config_value(
            config, ["num_hidden_layers", "n_layers", "num_layers", "n_layer"]
        )

        # Attention config
        self._extract_attention_config(config)

        # FFN config
        self._extract_ffn_config(config)

        # Normalization config
        self._extract_norm_config(config)

        # Positional embedding config
        self._extract_positional_config(config)

        logger.info(f"  Model type: {self.requirements.model_type}")
        logger.info(f"  Hidden size: {self.requirements.hidden_size}")
        logger.info(f"  Layers: {self.requirements.num_hidden_layers}")
        logger.info(
            f"  Attention heads: {self.requirements.attention.num_heads if self.requirements.attention else 'N/A'}"
        )

    def _get_config_value(self, config: Dict, keys: List[str], default: Any = None):
        """Get config value trying multiple possible keys"""
        for key in keys:
            if key in config:
                return config[key]
        return default

    def _extract_attention_config(self, config: Dict):
        """Extract attention configuration"""
        num_heads = self._get_config_value(
            config, ["num_attention_heads", "n_heads", "num_heads"]
        )
        num_kv_heads = self._get_config_value(
            config,
            ["num_key_value_heads", "n_kv_heads", "num_kv_heads"],
            num_heads,  # Default to same as num_heads (MHA)
        )
        head_dim = self._get_config_value(
            config,
            ["head_dim", "d_head"],
            self.requirements.hidden_size // num_heads if num_heads else 0,
        )

        # Detect attention type
        attention_type = AttentionType.MHA
        if num_kv_heads and num_kv_heads != num_heads:
            if num_kv_heads == 1:
                attention_type = AttentionType.MQA
            else:
                attention_type = AttentionType.GQA

        # Check for sliding window
        sliding_window = config.get("sliding_window")

        self.requirements.attention = AttentionInfo(
            attention_type=attention_type,
            num_heads=num_heads or 0,
            num_kv_heads=num_kv_heads or 0,
            head_dim=head_dim,
            use_bias=config.get("attention_bias", False),
            sliding_window=sliding_window,
        )

        # Detect RoPE
        if config.get("rope_theta") or config.get("rotary_emb_base"):
            self.requirements.attention.has_rotary_embeddings = True
            self.requirements.attention.rotary_config = {
                "theta": config.get("rope_theta", config.get("rotary_emb_base", 10000)),
                "scaling": config.get("rope_scaling"),
            }

    def _extract_ffn_config(self, config: Dict):
        """Extract FFN configuration"""
        intermediate_size = self._get_config_value(
            config, ["intermediate_size", "ffn_hidden_size", "n_inner", "hidden_dim"]
        )

        # Determine FFN type
        ffn_type = "mlp"
        activation = ActivationType.NONE

        # Check for SwiGLU indicators
        if any(x in str(config.get("architectures", [])) for x in ["Llama", "Mistral"]):
            ffn_type = "swiglu"
            activation = ActivationType.SILU

        # Check for GeGLU indicators
        if "phi" in config.get("model_type", "").lower():
            ffn_type = "geglu"
            activation = ActivationType.GELU

        # Check for MoE
        num_experts = config.get("num_experts", config.get("n_experts", 0))
        if num_experts:
            ffn_type = "moe"

        self.requirements.ffn = FFNInfo(
            ffn_type=ffn_type,
            hidden_size=self.requirements.hidden_size,
            intermediate_size=intermediate_size or (self.requirements.hidden_size * 4),
            activation=activation,
            num_experts=num_experts,
            top_k_experts=config.get("num_experts_per_tok", config.get("top_k", 0)),
            moe_aux_loss=config.get("router_aux_loss_coef", 0.0),
        )

    def _extract_norm_config(self, config: Dict):
        """Extract normalization configuration"""
        # Determine norm type from config keys
        if "rms_norm_eps" in config:
            self.requirements.norm_type = NormType.RMS_NORM
            self.requirements.norm_eps = config["rms_norm_eps"]
        elif "layer_norm_eps" in config or "layernorm_epsilon" in config:
            self.requirements.norm_type = NormType.LAYER_NORM
            self.requirements.norm_eps = config.get(
                "layer_norm_eps", config.get("layernorm_epsilon", 1e-5)
            )
        elif "norm_epsilon" in config:
            self.requirements.norm_type = NormType.LAYER_NORM
            self.requirements.norm_eps = config["norm_epsilon"]

    def _extract_positional_config(self, config: Dict):
        """Extract positional embedding configuration"""
        # Check for RoPE
        if config.get("rope_theta") or config.get("rotary_emb_base"):
            self.requirements.positional_embedding_type = "rope"
            self.requirements.rotary_config = {
                "theta": config.get("rope_theta", config.get("rotary_emb_base", 10000)),
                "max_position_embeddings": self.requirements.max_position_embeddings,
                "rope_type": config.get("rope_type", "default"),
                "scaling": config.get("rope_scaling"),
            }
        elif config.get("vocab_size"):
            self.requirements.positional_embedding_type = "learned"

    def _scan_modeling_code(self):
        """Find and analyze modeling code files"""
        modeling_files = list(self.model_path.glob("modeling*.py"))

        # Filter out special files
        modeling_files = [
            f
            for f in modeling_files
            if not f.name.endswith("_flash.py")  # Separate flash attention
            and "tokenization" not in f.name
        ]

        if not modeling_files:
            logger.warning("No modeling*.py files found")
            return

        logger.info(f"Found {len(modeling_files)} modeling file(s)")

        for modeling_file in modeling_files:
            logger.info(f"  Analyzing {modeling_file.name}")
            self._analyze_code_file(modeling_file)

    def _analyze_code_file(self, file_path: Path):
        """Analyze a single Python file"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()

            tree = ast.parse(code)
            analyzer = ModelCodeAnalyzer()
            analyzer.visit(tree)

            # Merge results
            self.code_analyzer.layers.extend(analyzer.layers)
            self.code_analyzer.module_attributes.update(analyzer.module_attributes)
            self.code_analyzer.function_calls.extend(analyzer.function_calls)

        except SyntaxError as e:
            logger.warning(f"  Syntax error parsing {file_path}: {e}")
        except Exception as e:
            logger.warning(f"  Error parsing {file_path}: {e}")

    def _analyze_discovered_layers(self):
        """Analyze and categorize discovered layers"""
        for layer in self.code_analyzer.layers:
            # Check if it's a known supported type
            layer.is_supported = self._check_layer_support(layer)

        self.requirements.discovered_layers = self.code_analyzer.layers

    def _check_layer_support(self, layer: LayerInfo) -> bool:
        """Check if a layer type is supported by IRON"""
        # Import here to avoid circular imports
        from .capability_registry import get_capability_registry

        registry = get_capability_registry()

        # Check by module path
        if registry.is_module_supported(layer.module_path):
            layer.support_notes = "Directly supported"
            return True

        # Check by category
        if registry.is_category_supported(layer.category):
            layer.support_notes = "Category supported"
            return True

        # Check by name patterns
        if registry.is_name_pattern_supported(layer.name):
            layer.support_notes = "Pattern matched"
            return True

        # Not supported
        layer.support_notes = "No matching support found"
        return False

    def _detect_special_features(self):
        """Detect special features in the model architecture"""
        features = []

        # Check for MoE
        if self.requirements.ffn and self.requirements.ffn.num_experts > 0:
            features.append(f"MoE with {self.requirements.ffn.num_experts} experts")

        # Check for sliding window attention
        if self.requirements.attention and self.requirements.attention.sliding_window:
            features.append(
                f"Sliding window attention (size={self.requirements.attention.sliding_window})"
            )

        # Check for attention sinks
        func_calls = " ".join(self.code_analyzer.function_calls)
        if "attention_sink" in func_calls.lower() or "_sink" in func_calls.lower():
            features.append("Attention sinks detected")

        # Check for multi-token prediction
        if self.requirements.raw_config.get("num_predict_tokens", 1) > 1:
            features.append(
                f"Multi-token prediction ({self.requirements.raw_config['num_predict_tokens']} tokens)"
            )

        # Check for custom RoPE scaling
        if self.requirements.rotary_config.get("scaling"):
            features.append(
                f"Custom RoPE scaling: {self.requirements.rotary_config['scaling']}"
            )

        # Check for tied embeddings
        if self.requirements.raw_config.get("tie_word_embeddings", False):
            features.append("Tied word embeddings")

        self.requirements.special_features = features

        # Identify unsupported components
        unsupported = []
        for layer in self.requirements.discovered_layers:
            if not layer.is_supported:
                unsupported.append(f"{layer.name} ({layer.module_path})")
        self.requirements.unsupported_components = unsupported


def scan_model_architecture(model_path: str) -> ArchitectureRequirements:
    """
    Convenience function to scan a model architecture.

    Args:
        model_path: Path to model or HF model name

    Returns:
        ArchitectureRequirements object
    """
    scanner = ArchitectureScanner(model_path)
    return scanner.scan()


def get_model_info_summary(model_path: str) -> str:
    """
    Get a human-readable summary of model architecture.

    Args:
        model_path: Path to model or HF model name

    Returns:
        Formatted summary string
    """
    requirements = scan_model_architecture(model_path)

    lines = [
        f"Model Architecture Summary",
        f"=" * 50,
        f"Model: {requirements.model_name}",
        f"Type: {requirements.model_type}",
        f"Architectures: {', '.join(requirements.architectures)}",
        f"",
        f"Core Dimensions:",
        f"  Hidden size: {requirements.hidden_size}",
        f"  Vocab size: {requirements.vocab_size}",
        f"  Max positions: {requirements.max_position_embeddings}",
        f"  Num layers: {requirements.num_hidden_layers}",
        f"",
        f"Attention:",
        f"  Type: {requirements.attention.attention_type.value if requirements.attention else 'N/A'}",
        f"  Heads: {requirements.attention.num_heads if requirements.attention else 'N/A'}",
        f"  KV Heads: {requirements.attention.num_kv_heads if requirements.attention else 'N/A'}",
        f"  Head dim: {requirements.attention.head_dim if requirements.attention else 'N/A'}",
        f"  RoPE: {'Yes' if requirements.attention and requirements.attention.has_rotary_embeddings else 'No'}",
        f"",
        f"FFN:",
        f"  Type: {requirements.ffn.ffn_type if requirements.ffn else 'N/A'}",
        f"  Intermediate: {requirements.ffn.intermediate_size if requirements.ffn else 'N/A'}",
        f"",
        f"Normalization: {requirements.norm_type.value}",
        f"Norm epsilon: {requirements.norm_eps}",
        f"",
        f"Special Features:",
    ]

    for feature in requirements.special_features or ["None"]:
        lines.append(f"  - {feature}")

    if requirements.unsupported_components:
        lines.extend(
            [
                f"",
                f"Potentially Unsupported Components:",
            ]
        )
        for comp in requirements.unsupported_components[:10]:
            lines.append(f"  - {comp}")
        if len(requirements.unsupported_components) > 10:
            lines.append(
                f"  ... and {len(requirements.unsupported_components) - 10} more"
            )

    return "\n".join(lines)
