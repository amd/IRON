# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Model Analysis Tools

Cross-platform model analysis using HuggingFace Transformers.
These tools work on Windows, macOS, and Linux WITHOUT requiring AIE/MLIR dependencies.

For full model conversion (Linux with NPU only), use iron.model_convert.

Usage:
    from iron.model_analysis import scan_model, get_architecture_summary, quick_check

    # Scan a model
    info = scan_model("Qwen/Qwen3.5-27B")
    print(get_architecture_summary(info))

    # Quick check
    if quick_check("meta-llama/Llama-2-7b-hf"):
        print("Model is likely supported")
"""

# These modules have NO AIE dependencies - they work cross-platform
from .transformers_integration import (
    TransformersScanner,
    TransformerModelInfo,
    scan_model_from_transformers,
    get_architecture_summary,
    ARCHITECTURE_MODULE_MAP,
)

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


# Convenience functions

def scan_model(model_name: str, use_transformers: bool = True) -> TransformerModelInfo:
    """
    Scan a model using Transformers library (preferred) or AST.

    Args:
        model_name: HuggingFace model name or path
        use_transformers: Use Transformers library (True) or AST scanning (False)

    Returns:
        TransformerModelInfo or ArchitectureRequirements
    """
    if use_transformers:
        return scan_model_from_transformers(model_name)
    else:
        scanner = ArchitectureScanner(model_name)
        return scanner.scan()


def analyze_model(model_name: str) -> GapReport:
    """
    Analyze a model for IRON NPU compatibility.

    Args:
        model_name: HuggingFace model name or path

    Returns:
        GapReport with compatibility analysis
    """
    return generate_gap_report(model_name)


def is_model_supported(model_name: str) -> bool:
    """
    Quick check if a model is likely supported.

    Args:
        model_name: HuggingFace model name

    Returns:
        True if likely supported
    """
    return quick_check(model_name)


__version__ = "0.1.0"

__all__ = [
    # Version
    "__version__",

    # Transformers integration (PREFERRED)
    "TransformersScanner",
    "TransformerModelInfo",
    "scan_model_from_transformers",
    "get_architecture_summary",
    "ARCHITECTURE_MODULE_MAP",

    # AST scanning (fallback)
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
    "analyze_model",
    "is_model_supported",
    "scan_model",

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
]
