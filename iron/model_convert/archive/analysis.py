# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Model Analysis Tools

Cross-platform tools for analyzing HuggingFace models and generating gap reports.
These tools do NOT require the AIE/MLIR dependencies and work on Windows.

Usage:
    from iron.model_convert.analysis import analyze_model, quick_check

    # Quick check
    if quick_check("meta-llama/Llama-2-7b-hf"):
        print("Model is likely supported")

    # Full analysis
    report = analyze_model("path/to/model")
    print(f"Support: {report.support_percentage}%")
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
_parent_dir = Path(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

# Import analysis modules (these don't need AIE)
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


def analyze_model(
    model_path: str,
    output_report: bool = False,
    output_path: Optional[str] = None,
) -> GapReport:
    """
    Analyze a model for IRON NPU compatibility.

    Args:
        model_path: Path to model or HuggingFace model name
        output_report: Whether to save report to file
        output_path: Optional path for report output

    Returns:
        GapReport with compatibility analysis
    """
    report = generate_gap_report(model_path)

    if output_report:
        save_path = output_path or f"{model_path.replace('/', '_')}_gap_report.json"
        report.save(save_path)
        print(f"Report saved to: {save_path}")

    return report


__all__ = [
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
    "analyze_model",

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
