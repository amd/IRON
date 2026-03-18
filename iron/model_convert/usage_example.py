# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Usage Examples for IRON Model Converter

This file demonstrates the complete workflow for:
1. Scanning a new model architecture
2. Analyzing gaps between model requirements and IRON capabilities
3. Generating action items for adding support
4. Converting supported models
"""

# ============================================================================
# EXAMPLE 1: Quick Check if a Model is Supported
# ============================================================================


def example_quick_check():
    """Quick check if a model architecture is likely supported."""
    from iron.model_convert import quick_check

    models_to_check = [
        "meta-llama/Llama-2-7b-hf",
        "mistralai/Mistral-7B-v0.1",
        "google/gemma-7b",
        "microsoft/phi-2",
    ]

    for model_name in models_to_check:
        is_supported = quick_check(model_name)
        status = "SUPPORTED" if is_supported else "NEEDS REVIEW"
        print(f"{model_name}: {status}")


# ============================================================================
# EXAMPLE 2: Scan Model Architecture
# ============================================================================


def example_scan_architecture():
    """Scan a model's architecture to understand what layers it uses."""
    from iron.model_convert import ArchitectureScanner, get_model_info_summary

    # For a local model directory or HuggingFace model name
    model_path = "path/to/model"  # Replace with actual path

    scanner = ArchitectureScanner(model_path)
    requirements = scanner.scan()

    # Print detailed summary
    print(get_model_info_summary(requirements))

    # Access individual layer information
    print("\nDiscovered Layers:")
    for layer in requirements.discovered_layers:
        status = "✓" if layer.is_supported else "✗"
        print(f"  {status} {layer.name} ({layer.category.value})")
        print(f"      Module: {layer.module_path}")


# ============================================================================
# EXAMPLE 3: Generate Gap Analysis Report
# ============================================================================


def example_gap_analysis():
    """Generate a detailed gap analysis report."""
    from iron.model_convert import generate_gap_report, ArchitectureScanner

    # Scan the model
    model_path = "path/to/new_model"
    scanner = ArchitectureScanner(model_path)
    requirements = scanner.scan()

    # Analyze gaps
    report = generate_gap_report(model_path)

    # Print summary
    print(report.to_json(indent=2))

    # Save report to file
    report.save("gap_report.json")

    # Access specific information
    print(f"\nSupport Level: {report.support_percentage:.1f}%")
    print(f"Feasibility: {report.conversion_feasibility}")
    print(f"\nCritical Gaps: {len(report.critical_gaps)}")
    for gap in report.critical_gaps[:5]:
        print(f"  - {gap.component_name}: {gap.reason}")


# ============================================================================
# EXAMPLE 4: Print Human-Readable Gap Summary
# ============================================================================


def example_print_summary():
    """Print a formatted gap analysis summary."""
    from iron.model_convert import print_gap_summary

    summary = print_gap_summary("path/to/model")
    print(summary)


# ============================================================================
# EXAMPLE 5: Register Custom Operator for Unsupported Layer
# ============================================================================


def example_register_custom_operator():
    """Register support for a custom operator."""
    from iron.model_convert import quick_register_operator, LayerCategory

    # Quick registration for a custom attention variant
    quick_register_operator(
        name="CustomSlidingWindowAttention",
        module_patterns=[
            "mymodel.modeling.CustomAttention",
            "mymodel.layers.SlidingWindowAttention",
        ],
        category="attention",
        support_level="partial",  # or "full", "fallback", "unsupported"
    )

    # Or use the extensibility framework for full implementation
    from iron.model_convert import generate_operator_skeleton

    skeleton_path = generate_operator_skeleton(
        operator_name="SlidingWindowAttention",
        output_path="./extensions/sliding_window_attention.py",
    )
    print(f"Generated operator skeleton at: {skeleton_path}")


# ============================================================================
# EXAMPLE 6: Use Operator Templates
# ============================================================================


def example_operator_templates():
    """Use pre-built templates for common custom operators."""
    from iron.model_convert import get_operator_template, TEMPLATES

    # List available templates
    print("Available operator templates:")
    for name in TEMPLATES.keys():
        print(f"  - {name}")

    # Get a specific template
    template = get_operator_template("sliding_window_attention")
    if template:
        print(f"\nTemplate: {template.name}")
        print(f"Category: {template.category.value}")
        print(f"Description: {template.description}")
        print(f"\nRequired methods:")
        for method in template.required_methods:
            print(f"  - {method}")


# ============================================================================
# EXAMPLE 7: Compare Multiple Models
# ============================================================================


def example_compare_models():
    """Compare support across multiple model architectures."""
    from iron.model_convert import GapAnalyzer, ArchitectureScanner

    models = [
        "meta-llama/Llama-2-7b-hf",
        "mistralai/Mistral-7B-v0.1",
        "google/gemma-7b",
    ]

    # Scan all models
    scanners = [ArchitectureScanner(m) for m in models]
    requirements_list = [s.scan() for s in scanners]

    # Compare
    analyzer = GapAnalyzer()
    comparison = analyzer.compare_models(requirements_list)

    print("Comparative Analysis:")
    print("=" * 60)
    for model in comparison.models:
        pct = comparison.support_percentages.get(model, 0)
        rec = comparison.recommendations.get(model, "Unknown")
        print(f"{model}:")
        print(f"  Support: {pct:.1f}%")
        print(f"  Recommendation: {rec}")

    print(f"\nCommon gaps across all models:")
    for gap in comparison.common_gaps[:5]:
        print(f"  - {gap}")


# ============================================================================
# EXAMPLE 8: Full Conversion Workflow (for supported models)
# ============================================================================


def example_full_conversion():
    """Complete workflow for converting a supported model."""
    from iron.model_convert import (
        HuggingFaceConverter,
        scan_model_architecture,
        generate_gap_report,
    )

    model_name = "meta-llama/Llama-2-7b-hf"

    # Step 1: Check if supported
    print(f"Checking {model_name}...")
    if not quick_check(model_name):
        print("Model may need review. Generating gap report...")
        report = generate_gap_report(model_name)
        print(f"Support level: {report.support_percentage:.1f}%")

    # Step 2: Convert
    converter = HuggingFaceConverter(
        model_name_or_path=model_name,
        num_aie_columns=8,
        enable_aie_gemm=True,
        enable_aie_norm=True,
    )

    # Step 3: Create NPU model
    model = converter.create_npu_model()

    # Step 4: Run inference
    import torch

    input_ids = torch.tensor([[1, 2, 3, 4, 5]])
    output = model.generate(input_ids, max_new_tokens=100)
    print(f"Generated: {output}")


# ============================================================================
# EXAMPLE 9: Using Extension Points
# ============================================================================


def example_extension_points():
    """Use extension points to hook into the conversion pipeline."""
    from iron.model_convert import register_extension_point, invoke_extension_point
    from iron.model_convert import ArchitectureRequirements

    def my_custom_hook(requirements: ArchitectureRequirements):
        """Custom hook that runs before conversion."""
        print(f"Processing {requirements.model_name}...")

        # Modify requirements or add custom logic
        return {
            "custom_setting": "my_value",
        }

    # Register the hook
    register_extension_point("before_conversion", my_custom_hook)

    # Later, the hook will be invoked automatically during conversion
    # results = invoke_extension_point("before_conversion", requirements)


# ============================================================================
# EXAMPLE 10: Architecture-Specific Handler
# ============================================================================


def example_architecture_handler():
    """Register a custom architecture handler."""
    from iron.model_convert import ArchitectureHandler, ArchitectureRegistry

    # Create handler for a custom architecture
    handler = ArchitectureHandler(
        architecture_name="CustomModel",
        model_types=["custom_model", "my_custom_arch"],
        layer_mappings={
            "CustomAttention": "attention",
            "CustomNorm": "normalization",
            "CustomFFN": "linear",
        },
        default_config={
            "use_custom_kernel": True,
            "optimization_level": "O3",
        },
    )

    # Register the handler
    ArchitectureRegistry.register_handler(handler)

    # Now the converter knows how to handle this architecture


# ============================================================================
# MAIN: Run examples
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("IRON Model Converter - Usage Examples")
    print("=" * 60)

    # Example 1: Quick check
    print("\n1. Quick Check Example")
    print("-" * 40)
    # example_quick_check()  # Uncomment to run

    # Example 2: Scan architecture
    print("\n2. Scan Architecture Example")
    print("-" * 40)
    # example_scan_architecture()  # Uncomment to run

    # Example 3: Gap analysis
    print("\n3. Gap Analysis Example")
    print("-" * 40)
    # example_gap_analysis()  # Uncomment to run

    # Example 4: Print summary
    print("\n4. Print Summary Example")
    print("-" * 40)
    # example_print_summary()  # Uncomment to run

    # Example 5: Register custom operator
    print("\n5. Register Custom Operator Example")
    print("-" * 40)
    # example_register_custom_operator()  # Uncomment to run

    # Example 6: Operator templates
    print("\n6. Operator Templates Example")
    print("-" * 40)
    example_operator_templates()

    # Example 7: Compare models
    print("\n7. Compare Models Example")
    print("-" * 40)
    # example_compare_models()  # Uncomment to run

    # Example 8: Full conversion
    print("\n8. Full Conversion Example")
    print("-" * 40)
    # example_full_conversion()  # Uncomment to run

    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
