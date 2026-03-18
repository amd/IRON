# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Capability Registry for IRON

This module maintains a registry of what IRON supports:
- Supported operators (GEMM, RMSNorm, etc.)
- Supported layer patterns
- Supported architecture types
- Fallback strategies for unsupported components

This enables gap analysis when encountering new model architectures.
"""

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set, Tuple
from enum import Enum
import logging

from .architecture_scanner import (
    LayerCategory,
    AttentionType,
    NormType,
    ActivationType,
    LayerInfo,
    ArchitectureRequirements,
)

logger = logging.getLogger(__name__)


class SupportLevel(Enum):
    """Levels of support for a component"""

    FULL = "full"  # Fully supported with NPU operator
    PARTIAL = "partial"  # Partially supported, some limitations
    FALLBACK = "fallback"  # CPU fallback only
    UNSUPPORTED = "unsupported"  # Not supported at all


class FallbackStrategy(Enum):
    """Strategies for handling unsupported components"""

    CPU_FALLBACK = "cpu_fallback"  # Run on CPU
    DECOMPOSE = "decompose"  # Break into supported ops
    APPROXIMATE = "approximate"  # Use approximate version
    SKIP = "skip"  # Skip the component (if safe)
    CUSTOM_NEEDED = "custom_needed"  # Requires custom implementation


@dataclass
class OperatorCapability:
    """Describes a supported operator"""

    name: str
    category: LayerCategory
    support_level: SupportLevel
    module_patterns: List[str] = field(default_factory=list)
    name_patterns: List[str] = field(default_factory=list)
    description: str = ""
    limitations: List[str] = field(default_factory=list)
    fallback_strategy: FallbackStrategy = FallbackStrategy.CPU_FALLBACK
    fallback_operator: Optional[str] = None  # PyTorch equivalent
    config_requirements: Dict[str, Any] = field(default_factory=dict)
    example_usage: str = ""


@dataclass
class ArchitectureSupport:
    """Describes support for a complete architecture"""

    architecture_name: str
    model_types: List[str] = field(default_factory=list)
    support_level: SupportLevel = SupportLevel.FULL
    supported_layers: List[str] = field(default_factory=list)
    unsupported_layers: List[str] = field(default_factory=list)
    notes: str = ""
    example_models: List[str] = field(default_factory=list)


@dataclass
class ConversionRecipe:
    """Complete recipe for converting a model"""

    model_name: str
    architecture: str
    required_operators: List[str]
    unsupported_components: List[str]
    fallback_plan: Dict[str, FallbackStrategy]
    estimated_support_percentage: float
    custom_components_needed: List[str]
    steps: List[str]


class CapabilityRegistry:
    """
    Central registry for IRON capabilities.

    Tracks:
    - Which operators are supported
    - Which layer patterns are recognized
    - Which architectures are fully/partially supported
    - Fallback strategies for gaps
    """

    def __init__(self):
        self._operators: Dict[str, OperatorCapability] = {}
        self._architectures: Dict[str, ArchitectureSupport] = {}
        self._category_support: Dict[LayerCategory, bool] = {}
        self._module_patterns: Dict[str, str] = {}
        self._name_patterns: Dict[str, str] = {}

        # Initialize with known capabilities
        self._init_known_capabilities()

    def _init_known_capabilities(self):
        """Initialize registry with IRON's known capabilities"""

        # === Core Operators ===

        # GEMM
        self.register_operator(
            OperatorCapability(
                name="AIEGEMM",
                category=LayerCategory.LINEAR,
                support_level=SupportLevel.FULL,
                module_patterns=[
                    "torch.nn.Linear",
                    "iron.operators.AIEGEMM",
                ],
                name_patterns=["gemm", "linear", "dense", "proj", "fc"],
                description="General Matrix Multiply for linear projections",
                limitations=[
                    "Requires dimensions to be multiples of tile sizes",
                    "Weight must be transposed for column-major layout",
                ],
                fallback_strategy=FallbackStrategy.DECOMPOSE,
                fallback_operator="torch.nn.functional.linear",
                config_requirements={"tile_m": 64, "tile_k": 64, "tile_n": 64},
            )
        )

        # GEMV
        self.register_operator(
            OperatorCapability(
                name="AIEGEMV",
                category=LayerCategory.LINEAR,
                support_level=SupportLevel.PARTIAL,
                module_patterns=[
                    "torch.nn.Linear",
                    "iron.operators.AIEGEMV",
                ],
                name_patterns=["gemv", "mv"],
                description="General Matrix-Vector for decode phase",
                limitations=[
                    "Only efficient for single-token (decode) inference",
                    "Limited tile size configurations",
                ],
                fallback_strategy=FallbackStrategy.CPU_FALLBACK,
                fallback_operator="torch.nn.functional.linear",
            )
        )

        # RMSNorm
        self.register_operator(
            OperatorCapability(
                name="AIERMSNorm",
                category=LayerCategory.NORMALIZATION,
                support_level=SupportLevel.FULL,
                module_patterns=[
                    "torch.nn.RMSNorm",
                    "iron.operators.AIERMSNorm",
                ],
                name_patterns=["rmsnorm", "rms_norm"],
                description="Root Mean Square Layer Normalization",
                fallback_strategy=FallbackStrategy.CPU_FALLBACK,
                fallback_operator="torch.nn.RMSNorm",
                config_requirements={"eps": 1e-6},
            )
        )

        # LayerNorm
        self.register_operator(
            OperatorCapability(
                name="AIELayerNorm",
                category=LayerCategory.NORMALIZATION,
                support_level=SupportLevel.PARTIAL,
                module_patterns=[
                    "torch.nn.LayerNorm",
                    "iron.operators.AIELayerNorm",
                ],
                name_patterns=["layernorm", "layer_norm", "ln"],
                description="Layer Normalization",
                fallback_strategy=FallbackStrategy.CPU_FALLBACK,
                fallback_operator="torch.nn.LayerNorm",
            )
        )

        # RoPE
        self.register_operator(
            OperatorCapability(
                name="AIERoPE",
                category=LayerCategory.POSITIONAL,
                support_level=SupportLevel.FULL,
                module_patterns=[
                    "iron.operators.AIERope",
                ],
                name_patterns=["rope", "rotary"],
                description="Rotary Positional Embeddings",
                limitations=[
                    "Requires precomputed angle tables",
                    "Limited to certain head dimensions",
                ],
                fallback_strategy=FallbackStrategy.DECOMPOSE,
                fallback_operator="apply_rotary_pos_emb",
            )
        )

        # Multi-Head Attention
        self.register_operator(
            OperatorCapability(
                name="AIEMHA",
                category=LayerCategory.ATTENTION,
                support_level=SupportLevel.PARTIAL,
                module_patterns=[
                    "torch.nn.MultiheadAttention",
                    "iron.operators.AIEMHA",
                ],
                name_patterns=["mha", "multihead", "self_attention"],
                description="Multi-Head Attention (fused)",
                limitations=[
                    "Requires sequence length multiple of 64",
                    "Head dimension must be 64",
                    "Limited pipeline configurations",
                ],
                fallback_strategy=FallbackStrategy.DECOMPOSE,
                fallback_operator="torch.nn.functional.scaled_dot_product_attention",
            )
        )

        # Softmax
        self.register_operator(
            OperatorCapability(
                name="AIESoftmax",
                category=LayerCategory.ACTIVATION,
                support_level=SupportLevel.PARTIAL,
                module_patterns=[
                    "torch.nn.Softmax",
                    "iron.operators.AIESoftmax",
                ],
                name_patterns=["softmax"],
                description="Softmax activation",
                limitations=[
                    "Size must be multiple of 16",
                ],
                fallback_strategy=FallbackStrategy.CPU_FALLBACK,
                fallback_operator="torch.nn.functional.softmax",
            )
        )

        # SiLU
        self.register_operator(
            OperatorCapability(
                name="AIESiLU",
                category=LayerCategory.ACTIVATION,
                support_level=SupportLevel.FULL,
                module_patterns=[
                    "torch.nn.SiLU",
                    "iron.operators.AIESiLU",
                ],
                name_patterns=["silu"],
                description="Sigmoid Linear Unit activation",
                fallback_strategy=FallbackStrategy.CPU_FALLBACK,
                fallback_operator="torch.nn.functional.silu",
            )
        )

        # GELU
        self.register_operator(
            OperatorCapability(
                name="AIEGELU",
                category=LayerCategory.ACTIVATION,
                support_level=SupportLevel.FULL,
                module_patterns=[
                    "torch.nn.GELU",
                    "iron.operators.AIEGELU",
                ],
                name_patterns=["gelu"],
                description="Gaussian Error Linear Unit activation",
                fallback_strategy=FallbackStrategy.CPU_FALLBACK,
                fallback_operator="torch.nn.functional.gelu",
            )
        )

        # SwiGLU (fused)
        self.register_operator(
            OperatorCapability(
                name="AIESwiGLU",
                category=LayerCategory.ACTIVATION,
                support_level=SupportLevel.FULL,
                module_patterns=[
                    "iron.operators.AIESwiGLUPrefill",
                    "iron.operators.AIESwiGLUDecode",
                ],
                name_patterns=["swiglu", "swi_glu"],
                description="Fused SwiGLU activation (silu(x) * y)",
                limitations=[
                    "Separate operators for prefill and decode",
                ],
                fallback_strategy=FallbackStrategy.DECOMPOSE,
            )
        )

        # Element-wise Add
        self.register_operator(
            OperatorCapability(
                name="AIEElementwiseAdd",
                category=LayerCategory.NORMALIZATION_SEQUENCE,
                support_level=SupportLevel.FULL,
                module_patterns=[
                    "iron.operators.AIEElementwiseAdd",
                ],
                name_patterns=["add", "residual"],
                description="Element-wise addition for residual connections",
                fallback_strategy=FallbackStrategy.CPU_FALLBACK,
                fallback_operator="torch.add",
            )
        )

        # Element-wise Mul
        self.register_operator(
            OperatorCapability(
                name="AIEElementwiseMul",
                category=LayerCategory.ACTIVATION,
                support_level=SupportLevel.FULL,
                module_patterns=[
                    "iron.operators.AIEElementwiseMul",
                ],
                name_patterns=["mul", "multiply"],
                description="Element-wise multiplication",
                fallback_strategy=FallbackStrategy.CPU_FALLBACK,
                fallback_operator="torch.mul",
            )
        )

        # === Category-level support ===
        self._category_support = {
            LayerCategory.LINEAR: True,
            LayerCategory.NORMALIZATION: True,
            LayerCategory.ACTIVATION: True,
            LayerCategory.ATTENTION: True,  # Partial
            LayerCategory.POSITIONAL: True,
            LayerCategory.EMBEDDING: False,  # CPU fallback
            LayerCategory.CONVOLUTION: False,  # Not supported
            LayerCategory.POOLING: False,  # Not typically needed
            LayerCategory.CUSTOM: False,
        }

        # === Module pattern mappings ===
        self._module_patterns = {
            "torch.nn.Linear": "AIEGEMM",
            "torch.nn.RMSNorm": "AIERMSNorm",
            "torch.nn.LayerNorm": "AIELayerNorm",
            "torch.nn.SiLU": "AIESiLU",
            "torch.nn.GELU": "AIEGELU",
            "torch.nn.Softmax": "AIESoftmax",
            "torch.nn.MultiheadAttention": "AIEMHA",
            "torch.nn.Embedding": "CPU_FALLBACK",
        }

        # === Architecture support ===
        self._register_architecture(
            ArchitectureSupport(
                architecture_name="Llama",
                model_types=["llama", "llama2", "llama3", "codellama"],
                support_level=SupportLevel.FULL,
                supported_layers=[
                    "RMSNorm",
                    "GEMM",
                    "RoPE",
                    "GQA",
                    "SiLU",
                    "SwiGLU",
                ],
                unsupported_layers=[],
                notes="Full support via AIEGEMM, AIERMSNorm, AIERoPE, AIESwiGLU",
                example_models=["meta-llama/Llama-2-7b", "meta-llama/Llama-3-8B"],
            )
        )

        self._register_architecture(
            ArchitectureSupport(
                architecture_name="Mistral",
                model_types=["mistral", "mixtral"],
                support_level=SupportLevel.PARTIAL,
                supported_layers=["RMSNorm", "GEMM", "RoPE", "GQA", "SiLU", "SwiGLU"],
                unsupported_layers=["SlidingWindowAttention"],
                notes="Sliding window attention requires custom implementation",
                example_models=["mistralai/Mistral-7B-v0.1"],
            )
        )

        self._register_architecture(
            ArchitectureSupport(
                architecture_name="Phi",
                model_types=["phi", "phi3"],
                support_level=SupportLevel.PARTIAL,
                supported_layers=["LayerNorm", "GEMM", "RoPE", "GELU"],
                unsupported_layers=[],
                notes="Uses LayerNorm instead of RMSNorm",
                example_models=["microsoft/phi-2", "microsoft/Phi-3-mini-4k"],
            )
        )

    def register_operator(self, capability: OperatorCapability) -> None:
        """Register an operator capability"""
        self._operators[capability.name] = capability

        # Index by patterns
        for pattern in capability.module_patterns:
            self._module_patterns[pattern.lower()] = capability.name
        for pattern in capability.name_patterns:
            self._name_patterns[pattern.lower()] = capability.name

    def _register_architecture(self, support: ArchitectureSupport) -> None:
        """Register architecture support"""
        self._architectures[support.architecture_name] = support
        for model_type in support.model_types:
            self._architectures[model_type] = support

    def get_operator(self, name: str) -> Optional[OperatorCapability]:
        """Get operator capability by name"""
        return self._operators.get(name)

    def is_module_supported(self, module_path: str) -> bool:
        """Check if a module type is supported"""
        module_lower = module_path.lower()

        # Direct pattern match
        if module_lower in self._module_patterns:
            op_name = self._module_patterns[module_lower]
            if op_name == "CPU_FALLBACK":
                return False
            op = self._operators.get(op_name)
            return op and op.support_level in [SupportLevel.FULL, SupportLevel.PARTIAL]

        # Check by category
        for category, supported in self._category_support.items():
            if category.value in module_lower and supported:
                return True

        return False

    def is_category_supported(self, category: LayerCategory) -> bool:
        """Check if a layer category is supported"""
        return self._category_support.get(category, False)

    def is_name_pattern_supported(self, name: str) -> bool:
        """Check if a layer name pattern is supported"""
        name_lower = name.lower()
        for pattern, op_name in self._name_patterns.items():
            if pattern in name_lower and op_name in self._operators:
                op = self._operators[op_name]
                return op.support_level in [SupportLevel.FULL, SupportLevel.PARTIAL]
        return False

    def get_architecture_support(
        self, architecture_name: str
    ) -> Optional[ArchitectureSupport]:
        """Get architecture support info"""
        return self._architectures.get(architecture_name)

    def list_supported_operators(self) -> List[Dict[str, Any]]:
        """List all registered operators"""
        return [
            {
                "name": op.name,
                "category": op.category.value,
                "support_level": op.support_level.value,
                "description": op.description,
                "limitations": op.limitations,
            }
            for op in self._operators.values()
        ]

    def list_supported_architectures(self) -> List[Dict[str, Any]]:
        """List all registered architectures"""
        return [
            {
                "architecture": arch.architecture_name,
                "model_types": arch.model_types,
                "support_level": arch.support_level.value,
                "supported_layers": arch.supported_layers,
                "unsupported_layers": arch.unsupported_layers,
                "notes": arch.notes,
                "example_models": arch.example_models,
            }
            for arch in self._architectures.values()
        ]

    def get_fallback_strategy(self, component_name: str) -> FallbackStrategy:
        """Get fallback strategy for a component"""
        # Try to find matching operator
        for pattern, op_name in self._module_patterns.items():
            if pattern in component_name.lower() and op_name in self._operators:
                return self._operators[op_name].fallback_strategy

        return FallbackStrategy.CUSTOM_NEEDED


# Global registry instance
_registry: Optional[CapabilityRegistry] = None


def get_capability_registry() -> CapabilityRegistry:
    """Get or create the global capability registry"""
    global _registry
    if _registry is None:
        _registry = CapabilityRegistry()
    return _registry


def register_custom_operator(
    name: str,
    category: LayerCategory,
    module_patterns: List[str],
    support_level: SupportLevel = SupportLevel.FULL,
    **kwargs,
) -> None:
    """
    Register a custom operator with the capability registry.

    This allows extending IRON support for new operators without
    modifying the core registry code.

    Args:
        name: Operator name
        category: Layer category
        module_patterns: Module path patterns to match
        support_level: Level of support
        **kwargs: Additional OperatorCapability arguments
    """
    registry = get_capability_registry()
    registry.register_operator(
        OperatorCapability(
            name=name,
            category=category,
            support_level=support_level,
            module_patterns=module_patterns,
            **kwargs,
        )
    )


def register_architecture_support(
    architecture_name: str,
    model_types: List[str],
    supported_layers: List[str],
    unsupported_layers: Optional[List[str]] = None,
    support_level: SupportLevel = SupportLevel.PARTIAL,
    notes: str = "",
) -> None:
    """
    Register support for a new architecture.

    Args:
        architecture_name: Name of the architecture
        model_types: List of model type strings
        supported_layers: Layers that are supported
        unsupported_layers: Layers that are not supported
        support_level: Overall support level
        notes: Additional notes
    """
    registry = get_capability_registry()
    registry._register_architecture(
        ArchitectureSupport(
            architecture_name=architecture_name,
            model_types=model_types,
            supported_layers=supported_layers,
            unsupported_layers=unsupported_layers or [],
            support_level=support_level,
            notes=notes,
        )
    )


def analyze_model_support(requirements: ArchitectureRequirements) -> ConversionRecipe:
    """
    Analyze a model's requirements and generate a conversion recipe.

    Args:
        requirements: ArchitectureRequirements from scanner

    Returns:
        ConversionRecipe with conversion plan
    """
    registry = get_capability_registry()

    # Determine required operators
    required_operators = set()
    unsupported_components = []
    fallback_plan = {}

    for layer in requirements.discovered_layers:
        if layer.is_supported:
            # Find matching operator
            for pattern, op_name in registry._module_patterns.items():
                if pattern in layer.module_path.lower():
                    required_operators.add(op_name)
                    break
        else:
            unsupported_components.append(f"{layer.name} ({layer.module_path})")
            fallback_plan[layer.name] = registry.get_fallback_strategy(
                layer.module_path
            )

    # Calculate support percentage
    total_layers = len(requirements.discovered_layers)
    supported_layers = len(
        [l for l in requirements.discovered_layers if l.is_supported]
    )
    support_percentage = (
        (supported_layers / total_layers * 100) if total_layers > 0 else 0
    )

    # Determine custom components needed
    custom_components = []
    for comp in unsupported_components:
        strategy = fallback_plan.get(comp.split()[0], FallbackStrategy.CUSTOM_NEEDED)
        if strategy == FallbackStrategy.CUSTOM_NEEDED:
            custom_components.append(comp)

    # Generate conversion steps
    steps = [
        f"1. Verify model config is compatible: {requirements.model_type}",
        f"2. Load and map weights using WeightMapper",
        f"3. Create NPU operators for supported layers",
    ]

    if unsupported_components:
        steps.append(
            f"4. Implement fallback for {len(unsupported_components)} unsupported components"
        )

    if custom_components:
        steps.append(
            f"5. Implement custom NPU operators for: {', '.join(custom_components[:3])}"
        )

    steps.append(f"6. Compile AIE artifacts")
    steps.append(f"7. Test inference against reference implementation")

    return ConversionRecipe(
        model_name=requirements.model_name,
        architecture=requirements.model_type,
        required_operators=list(required_operators),
        unsupported_components=unsupported_components,
        fallback_plan=fallback_plan,
        estimated_support_percentage=support_percentage,
        custom_components_needed=custom_components,
        steps=steps,
    )
