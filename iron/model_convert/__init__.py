# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Model Converter

A modular framework for converting HuggingFace models to IRON NPU format
for efficient execution on AMD Ryzen AI NPUs.

This package provides:
- Configuration parsing and normalization for various model architectures
- Weight mapping and transformation for NPU memory layouts
- Shape management with NPU-specific padding and tiling
- Operator factory for creating NPU-optimized operators
- Layer builders for constructing transformer blocks
- Model assembler for complete model construction

Example usage:
    from iron.model_convert import HuggingFaceConverter

    # Convert a model
    converter = HuggingFaceConverter("meta-llama/Llama-2-7b-hf")
    model = converter.create_npu_model()

    # Run inference
    output = model.generate(input_ids, max_new_tokens=100)

Supported architectures:
- Llama / Llama-2 / Llama-3
- Mistral / Mixtral
- Phi / Phi-2 / Phi-3
- Gemma
- Qwen

Supports:
- Full precision (BF16, FP16, FP32)
- Quantized models (AWQ, GPTQ) - experimental
- KV cache for efficient decoding
- Grouped Query Attention (GQA)
- Multi-Query Attention (MQA)
- RoPE embeddings
- SwiGLU / GeGLU activations
"""

from .config_adapter import (
    ConfigAdapter,
    NormalizedConfig,
    ModelArchitecture,
    NormType,
    FFNType,
    AttentionType,
    load_hf_config,
    get_iron_ready_config,
)

from .weight_mapper import (
    WeightMapper,
    QuantizedWeightMapper,
    MappedWeight,
    WeightTransform,
    create_weight_mapper,
)

from .shape_manager import (
    ShapeManager,
    TilingConfig,
    PaddedShape,
    NPUOperatorShape,
    create_shape_manager,
)

from .operator_factory import (
    OperatorFactory,
    OperatorType,
    OperatorConfig,
    OperatorBuilder,
    create_operator_factory,
)

from .layer_builder import (
    LayerConfig,
    AttentionLayerBuilder,
    FeedForwardBuilder,
    TransformerBlockBuilder,
    create_attention_layer,
    create_ffn_layer,
    create_transformer_block,
)

from .model_assembler import (
    ModelAssembler,
    ModelAssemblyConfig,
    create_model,
)

from .converter import (
    HuggingFaceConverter,
    ConversionConfig,
    convert_model,
    load_iron_model,
)

# Architecture scanning and gap analysis
from .architecture_scanner import (
    ArchitectureScanner,
    ModelCodeAnalyzer,
    ArchitectureRequirements,
    LayerInfo,
    AttentionInfo,
    FFNInfo,
    LayerCategory,
    scan_model_architecture,
    get_model_info_summary,
)

from .capability_registry import (
    CapabilityRegistry,
    OperatorCapability,
    SupportLevel,
    FallbackStrategy,
    ConversionRecipe,
    ArchitectureSupport,
    get_capability_registry,
    register_custom_operator,
    register_architecture_support,
    analyze_model_support,
)

from .gap_analyzer import (
    GapAnalyzer,
    GapItem,
    GapReport,
    ComparativeAnalysis,
    generate_gap_report,
    print_gap_summary,
    quick_check,
)

from .extensibility import (
    CustomOperatorBase,
    OperatorRegistry,
    ArchitectureRegistry,
    ExtensionLoader,
    OperatorTemplate,
    ArchitectureHandler,
    TEMPLATES,
    get_operator_template,
    generate_operator_skeleton,
    register_extension_point,
    invoke_extension_point,
    quick_register_operator,
    quick_register_architecture,
)

# Transformers integration (direct HF library scanning)
from .transformers_integration import (
    TransformersScanner,
    TransformerModelInfo,
    scan_model_from_transformers,
    get_architecture_summary,
    ARCHITECTURE_MODULE_MAP,
)


__version__ = "0.1.0"

__all__ = [
    # Version
    "__version__",

    # Main converter
    "HuggingFaceConverter",
    "ConversionConfig",
    "convert_model",
    "load_iron_model",

    # Model assembler
    "ModelAssembler",
    "ModelAssemblyConfig",
    "create_model",

    # Config adapter
    "ConfigAdapter",
    "NormalizedConfig",
    "ModelArchitecture",
    "NormType",
    "FFNType",
    "AttentionType",
    "load_hf_config",
    "get_iron_ready_config",

    # Weight mapper
    "WeightMapper",
    "QuantizedWeightMapper",
    "MappedWeight",
    "WeightTransform",
    "create_weight_mapper",

    # Shape manager
    "ShapeManager",
    "TilingConfig",
    "PaddedShape",
    "NPUOperatorShape",
    "create_shape_manager",

    # Operator factory
    "OperatorFactory",
    "OperatorType",
    "OperatorConfig",
    "OperatorBuilder",
    "create_operator_factory",

    # Layer builder
    "LayerConfig",
    "AttentionLayerBuilder",
    "FeedForwardBuilder",
    "TransformerBlockBuilder",
    "create_attention_layer",
    "create_ffn_layer",
    "create_transformer_block",

    # Architecture scanning
    "ArchitectureScanner",
    "ModelCodeAnalyzer",
    "ArchitectureRequirements",
    "LayerInfo",
    "AttentionInfo",
    "FFNInfo",
    "LayerCategory",
    "scan_model_architecture",
    "get_model_info_summary",

    # Capability registry
    "CapabilityRegistry",
    "OperatorCapability",
    "SupportLevel",
    "FallbackStrategy",
    "ConversionRecipe",
    "ArchitectureSupport",
    "get_capability_registry",
    "register_custom_operator",
    "register_architecture_support",
    "analyze_model_support",

    # Gap analysis
    "GapAnalyzer",
    "GapItem",
    "GapReport",
    "ComparativeAnalysis",
    "generate_gap_report",
    "print_gap_summary",
    "quick_check",

    # Extensibility
    "CustomOperatorBase",
    "OperatorRegistry",
    "ArchitectureRegistry",
    "ExtensionLoader",
    "OperatorTemplate",
    "ArchitectureHandler",
    "TEMPLATES",
    "get_operator_template",
    "generate_operator_skeleton",
    "register_extension_point",
    "invoke_extension_point",
    "quick_register_operator",
    "quick_register_architecture",

    # Transformers integration
    "TransformersScanner",
    "TransformerModelInfo",
    "scan_model_from_transformers",
    "get_architecture_summary",
    "ARCHITECTURE_MODULE_MAP",
]
