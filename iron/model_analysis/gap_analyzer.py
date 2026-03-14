# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Gap Analysis Engine

This module compares model requirements against IRON capabilities to:
1. Identify gaps in support
2. Generate detailed reports on what's missing
3. Suggest fallback strategies
4. Provide conversion feasibility assessment
5. Generate action items for adding support
"""

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import logging

from .architecture_scanner import (
    ArchitectureRequirements,
    LayerInfo,
    AttentionInfo,
    FFNInfo,
    LayerCategory,
)
from .capability_registry import (
    CapabilityRegistry,
    OperatorCapability,
    SupportLevel,
    FallbackStrategy,
    ConversionRecipe,
    get_capability_registry,
    analyze_model_support,
)

logger = logging.getLogger(__name__)


@dataclass
class GapItem:
    """A single gap item"""
    component_name: str
    component_type: str
    module_path: str
    reason: str
    impact: str  # high, medium, low
    fallback_available: bool
    fallback_strategy: str
    effort_estimate: str  # low, medium, high
    notes: str = ""


@dataclass
class GapReport:
    """Complete gap analysis report"""
    # Model info
    model_name: str
    model_type: str
    scan_timestamp: str

    # Summary
    total_components: int = 0
    supported_components: int = 0
    unsupported_components: int = 0
    support_percentage: float = 0.0

    # Detailed gaps
    gaps: List[GapItem] = field(default_factory=list)

    # Categorized gaps
    critical_gaps: List[GapItem] = field(default_factory=list)
    moderate_gaps: List[GapItem] = field(default_factory=list)
    minor_gaps: List[GapItem] = field(default_factory=list)

    # Feasibility
    conversion_feasibility: str = "unknown"  # feasible, challenging, not_feasible
    recommended_approach: str = ""

    # Action items
    action_items: List[str] = field(default_factory=list)

    # Conversion recipe
    recipe: Optional[ConversionRecipe] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "model_name": self.model_name,
            "model_type": self.model_type,
            "scan_timestamp": self.scan_timestamp,
            "summary": {
                "total_components": self.total_components,
                "supported_components": self.supported_components,
                "unsupported_components": self.unsupported_components,
                "support_percentage": self.support_percentage,
                "conversion_feasibility": self.conversion_feasibility,
            },
            "gaps": [asdict(g) for g in self.gaps],
            "critical_gaps": [asdict(g) for g in self.critical_gaps],
            "moderate_gaps": [asdict(g) for g in self.moderate_gaps],
            "minor_gaps": [asdict(g) for g in self.minor_gaps],
            "action_items": self.action_items,
            "recommended_approach": self.recommended_approach,
        }

    def to_json(self, indent: int = 2) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=indent)

    def save(self, path: str) -> None:
        """Save report to JSON file"""
        with open(path, "w") as f:
            f.write(self.to_json())
        logger.info(f"Gap report saved to {path}")


@dataclass
class ComparativeAnalysis:
    """Comparison between multiple models"""
    models: List[str]
    support_percentages: Dict[str, float]
    common_gaps: List[str]
    unique_gaps: Dict[str, List[str]]
    recommendations: Dict[str, str]


class GapAnalyzer:
    """
    Analyzes gaps between model requirements and IRON capabilities.

    Produces detailed reports on:
    - What components are unsupported
    - Impact level of each gap
    - Available fallbacks
    - Effort to add support
    - Overall conversion feasibility
    """

    # Impact levels for different component types
    HIGH_IMPACT_COMPONENTS = [
        "attention",
        "mha",
        "gqa",
        "mqa",
        "feed_forward",
        "ffn",
        "mlp",
    ]

    MEDIUM_IMPACT_COMPONENTS = [
        "norm",
        "normalization",
        "layernorm",
        "rmsnorm",
        "positional",
        "rope",
        "rotary",
    ]

    def __init__(self, registry: Optional[CapabilityRegistry] = None):
        """
        Initialize gap analyzer.

        Args:
            registry: Capability registry (uses global if not provided)
        """
        self.registry = registry or get_capability_registry()

    def analyze(
        self,
        requirements: ArchitectureRequirements,
    ) -> GapReport:
        """
        Perform gap analysis on model requirements.

        Args:
            requirements: Architecture requirements from scanner

        Returns:
            GapReport with detailed analysis
        """
        logger.info(f"Analyzing gaps for {requirements.model_name}")

        # Initialize report
        report = GapReport(
            model_name=requirements.model_name,
            model_type=requirements.model_type,
            scan_timestamp=datetime.now().isoformat(),
        )

        # Analyze each discovered layer
        for layer in requirements.discovered_layers:
            if not layer.is_supported:
                gap = self._analyze_layer_gap(layer, requirements)
                report.gaps.append(gap)

                # Categorize by impact
                if gap.impact == "high":
                    report.critical_gaps.append(gap)
                elif gap.impact == "medium":
                    report.moderate_gaps.append(gap)
                else:
                    report.minor_gaps.append(gap)

        # Calculate summary statistics
        total = len(requirements.discovered_layers)
        supported = len([l for l in requirements.discovered_layers if l.is_supported])
        unsupported = total - supported

        report.total_components = total
        report.supported_components = supported
        report.unsupported_components = unsupported
        report.support_percentage = (supported / total * 100) if total > 0 else 0

        # Generate conversion recipe
        report.recipe = analyze_model_support(requirements)

        # Determine feasibility
        report.conversion_feasibility = self._assess_feasibility(report)
        report.recommended_approach = self._generate_recommendation(report, requirements)

        # Generate action items
        report.action_items = self._generate_action_items(report)

        return report

    def _analyze_layer_gap(
        self,
        layer: LayerInfo,
        requirements: ArchitectureRequirements,
    ) -> GapItem:
        """Analyze a single unsupported layer"""
        # Determine impact level
        impact = self._determine_impact(layer)

        # Check for fallback
        fallback_strategy = self.registry.get_fallback_strategy(layer.module_path)
        fallback_available = fallback_strategy != FallbackStrategy.CUSTOM_NEEDED

        # Estimate effort
        effort = self._estimate_effort(layer, requirements)

        # Generate reason
        reason = self._generate_gap_reason(layer, requirements)

        return GapItem(
            component_name=layer.name,
            component_type=layer.category.value,
            module_path=layer.module_path,
            reason=reason,
            impact=impact,
            fallback_available=fallback_available,
            fallback_strategy=fallback_strategy.value,
            effort_estimate=effort,
        )

    def _determine_impact(self, layer: LayerInfo) -> str:
        """Determine impact level of a gap"""
        layer_lower = layer.name.lower()
        module_lower = layer.module_path.lower()
        combined = f"{layer_lower} {module_lower}"

        # High impact components
        for pattern in self.HIGH_IMPACT_COMPONENTS:
            if pattern in combined:
                return "high"

        # Medium impact components
        for pattern in self.MEDIUM_IMPACT_COMPONENTS:
            if pattern in combined:
                return "medium"

        # Everything else is low impact
        return "low"

    def _estimate_effort(
        self,
        layer: LayerInfo,
        requirements: ArchitectureRequirements,
    ) -> str:
        """Estimate effort to add support for a component"""
        # Simple heuristics based on component type

        if layer.category == LayerCategory.CONVOLUTION:
            return "high"  # Convolutions are complex on NPU

        if layer.category == LayerCategory.ATTENTION:
            if "sliding" in layer.module_path.lower():
                return "high"  # Sliding window is complex
            return "medium"

        if layer.category == LayerCategory.NORMALIZATION:
            return "low"  # Most norms are straightforward

        if layer.category == LayerCategory.ACTIVATION:
            return "low"  # Activations are usually simple

        if "custom" in layer.module_path.lower():
            return "high"  # Custom components need full implementation

        return "medium"

    def _generate_gap_reason(
        self,
        layer: LayerInfo,
        requirements: ArchitectureRequirements,
    ) -> str:
        """Generate human-readable reason for the gap"""
        reasons = []

        # Check if it's a known unsupported category
        if not self.registry.is_category_supported(layer.category):
            reasons.append(f"Category '{layer.category.value}' is not supported")

        # Check for specific limitations
        op = self.registry.get_operator(layer.module_path)
        if op and op.limitations:
            reasons.append(f"Limitations: {', '.join(op.limitations[:2])}")

        # Check architecture-specific issues
        if requirements.attention:
            if requirements.attention.sliding_window:
                if "attention" in layer.name.lower():
                    reasons.append("Sliding window attention requires custom implementation")

        if requirements.ffn and requirements.ffn.num_experts > 0:
            if "moe" not in layer.name.lower():
                reasons.append("MoE routing not yet supported")

        return "; ".join(reasons) if reasons else "No matching NPU operator available"

    def _assess_feasibility(self, report: GapReport) -> str:
        """Assess overall conversion feasibility"""
        support_pct = report.support_percentage
        critical_count = len(report.critical_gaps)

        if support_pct >= 90 and critical_count == 0:
            return "feasible"
        elif support_pct >= 70 and critical_count <= 2:
            return "challenging"
        else:
            return "not_feasible"

    def _generate_recommendation(
        self,
        report: GapReport,
        requirements: ArchitectureRequirements,
    ) -> str:
        """Generate recommended approach for conversion"""
        feasibility = report.conversion_feasibility

        if feasibility == "feasible":
            return (
                "Proceed with conversion using existing IRON operators. "
                f"{len(report.gaps)} minor components will use CPU fallback."
            )

        elif feasibility == "challenging":
            recommendations = []

            if report.critical_gaps:
                critical_names = [g.component_name for g in report.critical_gaps[:3]]
                recommendations.append(
                    f"Implement custom NPU operators for: {', '.join(critical_names)}"
                )

            if report.recipe and report.recipe.custom_components_needed:
                recommendations.append(
                    f"Priority: {len(report.recipe.custom_components_needed)} custom components needed"
                )

            return " | ".join(recommendations) if recommendations else (
                "Consider hybrid CPU/NPU execution for unsupported components"
            )

        else:  # not_feasible
            return (
                f"Model has {len(report.critical_gaps)} critical unsupported components. "
                "Significant NPU operator development required before conversion is practical. "
                "Consider running on CPU or contributing new operators to IRON."
            )

    def _generate_action_items(self, report: GapReport) -> List[str]:
        """Generate prioritized action items"""
        items = []

        # Critical gaps first
        if report.critical_gaps:
            items.append("=== CRITICAL (Blocking Conversion) ===")
            for gap in report.critical_gaps[:5]:
                items.append(
                    f"  - Implement NPU operator for {gap.component_name} "
                    f"({gap.module_path})"
                )

        # Moderate gaps
        if report.moderate_gaps:
            items.append("\n=== MODERATE (Performance Impact) ===")
            for gap in report.moderate_gaps[:5]:
                strategy = gap.fallback_strategy
                if strategy == "custom_needed":
                    items.append(
                        f"  - Consider implementing NPU operator for {gap.component_name}"
                    )
                else:
                    items.append(
                        f"  - Use {strategy} fallback for {gap.component_name}"
                    )

        # Minor gaps
        if report.minor_gaps:
            items.append(f"\n=== MINOR ({len(report.minor_gaps)} items) ===")
            items.append("  - Use CPU fallbacks for remaining components")

        # General actions
        items.append("\n=== GENERAL ===")
        items.append(f"  - Support level: {report.support_percentage:.1f}%")
        items.append(f"  - Feasibility: {report.conversion_feasibility}")

        if report.recipe and report.recipe.custom_components_needed:
            custom = report.recipe.custom_components_needed[:3]
            items.append(f"  - Custom implementations needed: {len(custom)}")

        return items

    def compare_models(
        self,
        requirements_list: List[ArchitectureRequirements],
    ) -> ComparativeAnalysis:
        """
        Compare support across multiple models.

        Args:
            requirements_list: List of requirements from different models

        Returns:
            ComparativeAnalysis
        """
        models = []
        support_percentages = {}
        all_gaps = {}
        gap_counts = {}

        for req in requirements_list:
            report = self.analyze(req)
            models.append(req.model_name)
            support_percentages[req.model_name] = report.support_percentage
            all_gaps[req.model_name] = set(g.component_name for g in report.gaps)
            gap_counts[req.model_name] = len(report.gaps)

        # Find common gaps
        if all_gaps:
            common_gaps = set.intersection(*all_gaps.values())
        else:
            common_gaps = set()

        # Find unique gaps per model
        unique_gaps = {}
        for model, gaps in all_gaps.items():
            other_gaps = set.union(*[all_gaps[m] for m in all_gaps if m != model]) if len(all_gaps) > 1 else set()
            unique_gaps[model] = list(gaps - other_gaps)

        # Generate recommendations
        recommendations = {}
        for req in requirements_list:
            report = self.analyze(req)
            if report.support_percentage >= 80:
                recommendations[req.model_name] = "Ready for conversion"
            elif report.support_percentage >= 50:
                recommendations[req.model_name] = "Needs custom operators"
            else:
                recommendations[req.model_name] = "Not recommended for NPU"

        return ComparativeAnalysis(
            models=models,
            support_percentages=support_percentages,
            common_gaps=list(common_gaps),
            unique_gaps=unique_gaps,
            recommendations=recommendations,
        )


def generate_gap_report(
    model_path: str,
    output_path: Optional[str] = None,
) -> GapReport:
    """
    Convenience function to generate a gap report for a model.

    Uses HuggingFace Transformers library to analyze models from HF Hub.
    For local models, ensure they are cached by Transformers first.

    Args:
        model_path: HuggingFace model name (e.g., "meta-llama/Llama-2-7b-hf")
        output_path: Optional path to save JSON report

    Returns:
        GapReport

    Raises:
        Exception: If model cannot be loaded via Transformers
    """
    from .architecture_scanner import NormType

    # Use Transformers integration (works with HF Hub model names)
    from .transformers_integration import scan_model_from_transformers
    info = scan_model_from_transformers(model_path)

    # Convert TransformerModelInfo to ArchitectureRequirements for gap analysis
    from .architecture_scanner import ArchitectureRequirements, LayerInfo, LayerCategory

    # Build discovered layers from config
    discovered_layers = []
    if info.layer_classes:
        discovered_layers = [
            LayerInfo(
                name=layer['name'],
                category=LayerCategory(layer['category']) if layer['category'] in [c.value for c in LayerCategory] else LayerCategory.UNKNOWN,
                module_path=layer.get('module', ''),
                is_supported=_is_layer_supported(layer['name'], layer['category']),
            )
            for layer in info.layer_classes
        ]
    else:
        # Infer layers from config - create representative layers
        discovered_layers = _infer_layers_from_config(info)

    requirements = ArchitectureRequirements(
        model_name=model_path,
        model_type=info.model_type,
        architectures=[info.architecture_name],
        hidden_size=info.config_dict.get('hidden_size', 0),
        vocab_size=info.config_dict.get('vocab_size', 0),
        max_position_embeddings=info.config_dict.get('max_position_embeddings', 0),
        num_hidden_layers=info.config_dict.get('num_hidden_layers', 0),
        discovered_layers=discovered_layers,
        attention=AttentionInfo(
            attention_type=info.attention_type,
            num_heads=info.config_dict.get('num_attention_heads', 0),
            num_kv_heads=info.config_dict.get('num_key_value_heads', info.config_dict.get('num_attention_heads', 0)),
        ) if info.config_dict else None,
        ffn=FFNInfo(
            ffn_type=info.ffn_type,
            intermediate_size=info.config_dict.get('intermediate_size', 0),
        ) if info.config_dict else None,
    )

    # Analyze gaps
    analyzer = GapAnalyzer()
    report = analyzer.analyze(requirements)

    # Save if requested
    if output_path:
        report.save(output_path)

    return report


def _is_layer_supported(name: str, category: str) -> bool:
    """Check if a layer is likely supported"""
    supported_patterns = [
        'attention', 'norm', 'rmsnorm', 'layernorm', 'linear', 'dense',
        'embedding', 'mlp', 'ffn', 'rms_norm', 'layer_norm'
    ]
    unsupported_patterns = ['moe', 'expert', 'mixtral', 'switch']

    name_lower = name.lower()
    category_lower = category.lower() if category else ''

    # Check unsupported first
    for pattern in unsupported_patterns:
        if pattern in name_lower or pattern in category_lower:
            return False

    # Check supported
    for pattern in supported_patterns:
        if pattern in name_lower or pattern in category_lower:
            return True

    return True


def _infer_layers_from_config(info) -> List[LayerInfo]:
    """
    Infer representative layers from config data when layer_classes is empty.

    This creates a minimal set of layers based on the model type and features.
    """
    from .architecture_scanner import LayerInfo, LayerCategory

    layers = []
    model_type = info.model_type.lower()

    # Standard transformer layers that most models have
    standard_layers = [
        ("Embedding", LayerCategory.EMBEDDING),
        ("Attention", LayerCategory.ATTENTION),
        ("RMSNorm", LayerCategory.NORMALIZATION),
        ("MLP", LayerCategory.LINEAR),
    ]

    # Add standard layers
    for name, category in standard_layers:
        layers.append(LayerInfo(
            name=name,
            category=category,
            module_path=f"transformers.models.{model_type}",
            is_supported=True,
        ))

    # Add MoE layer if applicable
    if info.has_moe:
        layers.append(LayerInfo(
            name="MoESparseTopK",
            category=LayerCategory.UNKNOWN,
            module_path=f"transformers.models.{model_type}",
            is_supported=False,  # MoE not supported yet
        ))

    # Add positional encoding if RoPE
    if info.has_rope:
        layers.append(LayerInfo(
            name="RotaryEmbedding",
            category=LayerCategory.POSITIONAL,
            module_path=f"transformers.models.{model_type}",
            is_supported=True,  # RoPE is supported
        ))

    return layers


def print_gap_summary(model_path: str) -> str:
    """
    Print a human-readable gap summary.

    Args:
        model_path: Path to model or HF model name

    Returns:
        Formatted summary string
    """
    report = generate_gap_report(model_path)

    lines = [
        "=" * 60,
        f"GAP ANALYSIS REPORT: {report.model_name}",
        "=" * 60,
        "",
        "SUMMARY",
        "-" * 40,
        f"  Model Type: {report.model_type}",
        f"  Total Components: {report.total_components}",
        f"  Supported: {report.supported_components} ({report.support_percentage:.1f}%)",
        f"  Unsupported: {report.unsupported_components}",
        f"  Feasibility: {report.conversion_feasibility}",
        "",
        "CRITICAL GAPS (Blocking)",
        "-" * 40,
    ]

    if report.critical_gaps:
        for gap in report.critical_gaps[:5]:
            lines.append(f"  ! {gap.component_name}: {gap.module_path}")
            lines.append(f"    Impact: {gap.impact}, Effort: {gap.effort_estimate}")
    else:
        lines.append("  None")

    lines.extend([
        "",
        "MODERATE GAPS (Performance Impact)",
        "-" * 40,
    ])

    if report.moderate_gaps:
        for gap in report.moderate_gaps[:5]:
            lines.append(f"  ~ {gap.component_name}: {gap.fallback_strategy}")
    else:
        lines.append("  None")

    lines.extend([
        "",
        "RECOMMENDED APPROACH",
        "-" * 40,
        f"  {report.recommended_approach}",
        "",
        "ACTION ITEMS",
        "-" * 40,
    ])

    for item in report.action_items[:15]:
        lines.append(item)

    lines.append("")
    lines.append("=" * 60)

    return "\n".join(lines)


def quick_check(model_name: str) -> bool:
    """
    Quick check if a model is likely supported.

    Uses Transformers library to fetch model config from HuggingFace Hub.

    Args:
        model_name: HF model name (e.g., "meta-llama/Llama-2-7b-hf")

    Returns:
        True if model is likely supported, False otherwise
    """
    try:
        from .transformers_integration import scan_model_from_transformers
        info = scan_model_from_transformers(model_name)

        # Check if model type is known/supported
        supported_types = ['llama', 'mistral', 'phi', 'gemma', 'qwen', 'qwen2']
        model_type = info.model_type.lower()

        # Check for MoE - needs custom implementation
        if info.has_moe:
            return False  # MoE models need custom operators

        # Check for sliding window - needs custom implementation
        if info.has_sliding_window:
            return False  # Sliding window needs custom operators

        # Known architectures are likely supported
        if model_type in supported_types:
            return True

        # Check architecture name
        arch_name = info.architecture_name.lower()
        for supported in supported_types:
            if supported in arch_name:
                return True

        return info.is_known_architecture

    except Exception as e:
        logger.warning(f"Could not analyze model {model_name}: {e}")
        return False
