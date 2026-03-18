#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Test Script for IRON Model Converter

This script demonstrates the complete workflow for:
1. Scanning a model architecture
2. Analyzing gaps
3. Converting supported models
4. Generating custom operator skeletons

Usage:
    python test_converter.py [--model MODEL_NAME]
"""

import sys
from pathlib import Path


def test_quick_check():
    """Test quick compatibility check"""
    print("\n" + "=" * 60)
    print("TEST: Quick Compatibility Check")
    print("=" * 60)

    from iron.model_convert import quick_check

    test_models = [
        "meta-llama/Llama-2-7b-hf",
        "meta-llama/Llama-3.2-1B",
        "mistralai/Mistral-7B-v0.1",
    ]

    for model in test_models:
        result = quick_check(model)
        status = "SUPPORTED" if result else "NEEDS REVIEW"
        print(f"  {model}: {status}")

    return True


def test_scan_architecture():
    """Test architecture scanning"""
    print("\n" + "=" * 60)
    print("TEST: Architecture Scanning")
    print("=" * 60)

    from iron.model_convert import ArchitectureScanner, get_model_info_summary

    # For demo purposes, we'll test with a known architecture pattern
    # In production, this would scan actual HF models

    print("  ArchitectureScanner: OK (class loaded)")
    print("  get_model_info_summary: OK (function loaded)")

    # Note: Full test requires actual model files
    print("\n  NOTE: Full scanning test requires model files on disk")

    return True


def test_gap_analysis():
    """Test gap analysis"""
    print("\n" + "=" * 60)
    print("TEST: Gap Analysis")
    print("=" * 60)

    from iron.model_convert import GapAnalyzer, GapReport, GapItem

    # Test GapAnalyzer creation
    analyzer = GapAnalyzer()
    print("  GapAnalyzer: OK (instance created)")

    # Test GapReport creation
    report = GapReport(
        model_name="TestModel",
        model_type="test",
        scan_timestamp="2025-01-01T00:00:00",
    )
    print("  GapReport: OK (instance created)")

    # Test report methods
    report_dict = report.to_dict()
    print(f"  to_dict(): OK ({len(report_dict)} keys)")

    report_json = report.to_json()
    print(f"  to_json(): OK ({len(report_json)} chars)")

    return True


def test_capability_registry():
    """Test capability registry"""
    print("\n" + "=" * 60)
    print("TEST: Capability Registry")
    print("=" * 60)

    from iron.model_convert import (
        CapabilityRegistry,
        get_capability_registry,
        register_custom_operator,
        SupportLevel,
        FallbackStrategy,
    )

    # Test registry access
    registry = get_capability_registry()
    print("  get_capability_registry(): OK")

    # Test custom operator registration
    register_custom_operator(
        name="TestOp",
        module_patterns=["test.models.TestOp"],
        support_level=SupportLevel.PARTIAL,
    )
    print("  register_custom_operator(): OK")

    # Test architecture support registration
    from iron.model_convert import register_architecture_support

    register_architecture_support(
        architecture_name="TestArch",
        model_types=["test_arch"],
        supported_layers=["TestOp", "RMSNorm"],
    )
    print("  register_architecture_support(): OK")

    return True


def test_extensibility():
    """Test extensibility framework"""
    print("\n" + "=" * 60)
    print("TEST: Extensibility Framework")
    print("=" * 60)

    from iron.model_convert import (
        CustomOperatorBase,
        OperatorRegistry,
        ArchitectureRegistry,
        ExtensionLoader,
        OperatorTemplate,
        TEMPLATES,
        get_operator_template,
        generate_operator_skeleton,
    )

    # Test template access
    print(f"  Available templates: {len(TEMPLATES)}")
    for name in TEMPLATES.keys():
        print(f"    - {name}")

    # Test template retrieval
    template = get_operator_template("sliding_window_attention")
    if template:
        print(f"  get_operator_template(): OK - {template.name}")

    # Test operator registry
    operators = OperatorRegistry.list_operators()
    print(f"  Registered operators: {len(operators)}")

    # Test architecture registry
    architectures = ArchitectureRegistry.list_handlers()
    print(f"  Registered architectures: {len(architectures)}")

    return True


def test_converter():
    """Test main converter"""
    print("\n" + "=" * 60)
    print("TEST: HuggingFace Converter")
    print("=" * 60)

    from iron.model_convert import (
        HuggingFaceConverter,
        ConversionConfig,
    )

    # Test config creation
    config = ConversionConfig(
        model_name_or_path="test/model",
        num_aie_columns=8,
        tile_m=64,
        tile_k=64,
        tile_n=64,
    )
    print("  ConversionConfig: OK")

    # Test converter class loads
    print("  HuggingFaceConverter: OK (class loaded)")

    # Note: Full test requires actual model and AIE context
    print("\n  NOTE: Full conversion test requires model files and AIE context")

    return True


def test_cli():
    """Test CLI"""
    print("\n" + "=" * 60)
    print("TEST: CLI")
    print("=" * 60)

    from iron.model_convert.cli import main

    # Test CLI loads
    print("  CLI main(): OK (function loaded)")

    # Test CLI help
    print("\n  Testing CLI help...")
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    try:
        with redirect_stdout(f):
            try:
                sys.argv = ["iron-convert", "--help"]
                main()
            except SystemExit:
                pass  # Expected from argparse --help

        output = f.getvalue()
        if "IRON Model Converter" in output:
            print("  CLI help: OK")
        else:
            print("  CLI help: FAILED")
            return False
    except Exception as e:
        print(f"  CLI help: ERROR - {e}")
        return False

    return True


def test_skeleton_generation():
    """Test operator skeleton generation"""
    print("\n" + "=" * 60)
    print("TEST: Operator Skeleton Generation")
    print("=" * 60)

    from iron.model_convert import generate_operator_skeleton
    import tempfile
    import os

    # Create temp directory
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "test_op.py"

        # Generate skeleton
        skeleton_path = generate_operator_skeleton(
            operator_name="TestCustomOp",
            output_path=str(output_path),
        )

        # Verify file was created
        if Path(skeleton_path).exists():
            print(f"  Skeleton generation: OK")

            # Read and verify content
            with open(skeleton_path) as f:
                content = f.read()

            if "TestCustomOp" in content:
                print(f"  Skeleton content: OK ({len(content)} chars)")
            else:
                print(f"  Skeleton content: FAILED")
                return False
        else:
            print(f"  Skeleton generation: FAILED - file not created")
            return False

    return True


def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("IRON Model Converter - Test Suite")
    print("=" * 60)

    tests = [
        ("Quick Check", test_quick_check),
        ("Architecture Scanning", test_scan_architecture),
        ("Gap Analysis", test_gap_analysis),
        ("Capability Registry", test_capability_registry),
        ("Extensibility Framework", test_extensibility),
        ("HuggingFace Converter", test_converter),
        ("CLI", test_cli),
        ("Skeleton Generation", test_skeleton_generation),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result, None))
        except Exception as e:
            results.append((name, False, str(e)))
            import traceback

            traceback.print_exc()

    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    passed = sum(1 for _, result, _ in results if result)
    total = len(results)

    for name, result, error in results:
        status = "PASS" if result else "FAIL"
        error_str = f" - {error}" if error else ""
        print(f"  [{status}] {name}{error_str}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\nAll tests passed!")
        return 0
    else:
        print(f"\n{total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Test IRON Model Converter")
    parser.add_argument(
        "--test",
        choices=[
            "all",
            "quick",
            "scan",
            "gap",
            "registry",
            "extensibility",
            "converter",
            "cli",
            "skeleton",
        ],
        default="all",
        help="Run specific test",
    )
    parser.add_argument(
        "--model",
        help="Model name for testing (default: use built-in test models)",
    )

    args = parser.parse_args()

    test_map = {
        "all": run_all_tests,
        "quick": test_quick_check,
        "scan": test_scan_architecture,
        "gap": test_gap_analysis,
        "registry": test_capability_registry,
        "extensibility": test_extensibility,
        "converter": test_converter,
        "cli": test_cli,
        "skeleton": test_skeleton_generation,
    }

    test_func = test_map.get(args.test, run_all_tests)
    sys.exit(test_func())
