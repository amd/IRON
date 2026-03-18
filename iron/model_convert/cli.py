#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Model Converter CLI

Command-line interface for converting HuggingFace models to IRON NPU format.

Usage:
    # Scan a model to check compatibility
    iron-convert scan meta-llama/Llama-2-7b-hf

    # Generate gap analysis report
    iron-convert analyze Qwen/Qwen3.5-27B --output gap_report.json

    # Convert a model to IRON format
    iron-convert convert mistralai/Mistral-7B-v0.1 --output ./iron_model

    # Quick check if model is supported
    iron-convert check google/gemma-7b
"""

import argparse
import json
import sys
import os
from pathlib import Path
from datetime import datetime


def cmd_scan(args):
    """Scan model architecture and display summary"""
    from iron.model_convert import ArchitectureScanner, get_model_info_summary

    print(f"Scanning model: {args.model}")
    print("-" * 60)

    # Try Transformers integration first (more accurate)
    if args.transformers or args.auto:
        try:
            return cmd_scan_transformers(args)
        except Exception as e:
            if not args.auto:
                raise
            print(f"Falling back to AST scanner: {e}")

    try:
        scanner = ArchitectureScanner(args.model)
        requirements = scanner.scan()

        summary = get_model_info_summary(requirements)
        print(summary)

        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Save as JSON
            report_data = {
                "model_name": requirements.model_name,
                "model_type": requirements.model_type,
                "scan_timestamp": datetime.now().isoformat(),
                "discovered_layers": [
                    {
                        "name": layer.name,
                        "module_path": layer.module_path,
                        "category": layer.category.value,
                        "is_supported": layer.is_supported,
                        "parameters": layer.parameters,
                    }
                    for layer in requirements.discovered_layers
                ],
                "attention": (
                    {
                        "type": (
                            requirements.attention.type.value
                            if requirements.attention
                            else None
                        ),
                        "num_heads": (
                            requirements.attention.num_heads
                            if requirements.attention
                            else None
                        ),
                        "num_kv_heads": (
                            requirements.attention.num_kv_heads
                            if requirements.attention
                            else None
                        ),
                        "sliding_window": (
                            requirements.attention.sliding_window
                            if requirements.attention
                            else None
                        ),
                    }
                    if requirements.attention
                    else None
                ),
                "ffn": (
                    {
                        "type": (
                            requirements.ffn.type.value if requirements.ffn else None
                        ),
                        "hidden_dim": (
                            requirements.ffn.hidden_dim if requirements.ffn else None
                        ),
                        "num_experts": (
                            requirements.ffn.num_experts if requirements.ffn else None
                        ),
                    }
                    if requirements.ffn
                    else None
                ),
            }

            with open(output_path, "w") as f:
                json.dump(report_data, f, indent=2)

            print(f"\nScan results saved to: {output_path}")

    except Exception as e:
        print(f"Error scanning model: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1

    return 0


def cmd_scan_transformers(args):
    """Scan model using Transformers library directly"""
    from iron.model_convert import (
        TransformersScanner,
        scan_model_from_transformers,
        get_architecture_summary,
    )

    print(f"Scanning model via Transformers: {args.model}")
    print("-" * 60)

    try:
        info = scan_model_from_transformers(
            args.model, trust_remote_code=args.trust_remote_code
        )

        # Print summary
        print(get_architecture_summary(info.architecture_name))

        # Save if requested
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            report_data = {
                "model_name": info.architecture_name,
                "model_type": info.model_type,
                "config_class": info.config_class,
                "config_dict": info.config_dict,
                "layer_classes": info.layer_classes,
                "special_features": {
                    "has_sliding_window": info.has_sliding_window,
                    "has_moe": info.has_moe,
                    "has_rope": info.has_rope,
                    "has_qk_norm": info.has_qk_norm,
                    "attention_type": info.attention_type,
                    "ffn_type": info.ffn_type,
                },
                "is_known_architecture": info.is_known_architecture,
                "support_notes": info.support_notes,
            }

            with open(output_path, "w") as f:
                json.dump(report_data, f, indent=2)

            print(f"\nScan results saved to: {output_path}")

    except Exception as e:
        print(f"Error scanning with Transformers: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1

    return 0


def cmd_analyze(args):
    """Analyze gaps between model requirements and IRON capabilities"""
    from iron.model_convert import (
        ArchitectureScanner,
        GapAnalyzer,
        generate_gap_report,
        print_gap_summary,
    )

    print(f"Analyzing gaps for: {args.model}")
    print("-" * 60)

    try:
        if args.quick:
            # Quick analysis
            from iron.model_convert import quick_check

            is_supported = quick_check(args.model)

            if is_supported:
                print("Model is likely SUPPORTED for conversion")
            else:
                print("Model NEEDS REVIEW - may have unsupported components")

        # Full analysis
        report = generate_gap_report(args.model)

        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            report.save(output_path)
            print(f"Full report saved to: {output_path}")

        # Print summary
        print()
        print(print_gap_summary(args.model))

        if args.json:
            print(json.dumps(report.to_dict(), indent=2))

        # Return non-zero if not feasible
        if report.conversion_feasibility == "not_feasible":
            print(
                "\nWARNING: Conversion is NOT FEASIBLE without significant custom development"
            )
            return 1

    except Exception as e:
        print(f"Error analyzing model: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1

    return 0


def cmd_check(args):
    """Quick check if model is supported"""
    from iron.model_convert import quick_check

    is_supported = quick_check(args.model)

    if is_supported:
        print(f"✓ {args.model}: SUPPORTED")
        return 0
    else:
        print(f"✗ {args.model}: NEEDS REVIEW")
        print("\nRun 'iron-convert analyze' for detailed gap analysis")
        return 1


def cmd_convert(args):
    """Convert model to IRON format"""
    from iron.model_convert import (
        HuggingFaceConverter,
        ConversionConfig,
        generate_gap_report,
        quick_check,
    )

    print(f"Converting model: {args.model}")
    print("=" * 60)

    # Step 1: Check compatibility
    print("\n[Step 1/4] Checking model compatibility...")

    if not args.skip_check:
        report = generate_gap_report(args.model)

        if report.conversion_feasibility == "not_feasible":
            print(f"ERROR: Model is not feasible for conversion")
            print(f"  Support level: {report.support_percentage:.1f}%")
            print(f"  Critical gaps: {len(report.critical_gaps)}")

            if not args.force:
                print("\nUse --force to attempt conversion anyway")
                print("Recommended: Run 'iron-convert analyze' for details")
                return 1

            print("\n--force specified, proceeding with conversion...")

    # Step 2: Create conversion config
    print("\n[Step 2/4] Configuring conversion...")

    config = ConversionConfig(
        model_name_or_path=args.model,
        num_aie_columns=args.aie_columns or 8,
        tile_m=args.tile_m or 64,
        tile_k=args.tile_k or 64,
        tile_n=args.tile_n or 64,
        enable_aie_gemm=not args.disable_aie_gemm,
        enable_aie_gemv=args.enable_aie_gemv,
        enable_aie_norm=not args.disable_aie_norm,
        enable_aie_mha=args.enable_aie_mha,
        enable_aie_rope=args.enable_aie_rope,
        enable_aie_ffn=not args.disable_aie_ffn,
        use_kv_cache=not args.disable_kv_cache,
        max_seq_len=args.max_seq_len or 512,
        batch_size=args.batch_size or 1,
        quantize=args.quantize,
        quant_type=args.quant_type,
    )

    print(f"  NPU columns: {config.num_aie_columns}")
    print(f"  Tile sizes: M={config.tile_m}, K={config.tile_k}, N={config.tile_n}")
    print(f"  Max sequence length: {config.max_seq_len}")

    # Step 3: Convert weights
    print("\n[Step 3/4] Converting weights...")

    try:
        converter = HuggingFaceConverter(args.model, config=config)

        output_dir = args.output or f"./iron_{args.model.replace('/', '_')}"

        converted_weights = converter.convert_weights(
            output_dir=output_dir,
            output_format="numpy" if args.numpy_format else "torch",
        )

        print(f"  Converted {len(converted_weights)} weight tensors")

        # Step 4: Create NPU model
        print("\n[Step 4/4] Creating NPU model...")

        assembler = converter.create_npu_model(
            compile_artifacts=args.compile,
        )

        # Get memory info
        mem_info = assembler.get_memory_info()
        print(f"\nMemory Requirements:")
        print(f"  KV Cache: {mem_info['kv_cache_bytes'] / 1024 / 1024:.1f} MB")
        print(
            f"  Prefill activations: {mem_info['prefill_activation_bytes'] / 1024 / 1024:.1f} MB"
        )
        print(
            f"  Total decode memory: {mem_info['total_decode_bytes'] / 1024 / 1024:.1f} MB"
        )

        # Save model info
        model_info_path = Path(output_dir) / "model_info.json"
        model_info = converter.get_model_info()
        with open(model_info_path, "w") as f:
            json.dump(model_info, f, indent=2)

        print(f"\nModel saved to: {output_dir}")
        print(f"Model info saved to: {model_info_path}")

        if args.compile:
            print("\nArtifacts compiled and ready for NPU execution")
        else:
            print("\nNOTE: Run 'iron-convert compile' to compile AIE artifacts")

        return 0

    except Exception as e:
        print(f"\nError during conversion: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


def cmd_compile(args):
    """Compile AIE artifacts for a converted model"""
    from iron.model_convert import ModelAssembler, ModelAssemblyConfig, ConfigAdapter

    print(f"Compiling AIE artifacts for: {args.model_dir}")
    print("-" * 60)

    try:
        # Load config
        config_path = Path(args.model_dir) / "model_info.json"
        if not config_path.exists():
            raise FileNotFoundError(f"model_info.json not found in {args.model_dir}")

        with open(config_path) as f:
            model_info = json.load(f)

        # TODO: Load and compile model
        print("Compilation not yet implemented in this CLI version")
        print("Use the Python API for full compilation support")

        return 0

    except Exception as e:
        print(f"Error during compilation: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


def cmd_infer(args):
    """Run inference with a converted model"""
    print(f"Running inference with: {args.model_dir}")
    print("-" * 60)

    try:
        # TODO: Load model and run inference
        print("Inference not yet implemented in this CLI version")
        print("Use the Python API for inference support")

        return 0

    except Exception as e:
        print(f"Error during inference: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


def cmd_skeleton(args):
    """Generate skeleton for custom operator"""
    from iron.model_convert import generate_operator_skeleton

    print(f"Generating skeleton for: {args.operator_name}")
    print("-" * 60)

    try:
        output_path = args.output or f"./{args.operator_name.lower()}.py"

        skeleton_path = generate_operator_skeleton(
            operator_name=args.operator_name,
            output_path=output_path,
        )

        print(f"Skeleton generated at: {skeleton_path}")
        print("\nNext steps:")
        print("  1. Implement set_up_artifacts() method")
        print("  2. Implement set_up_runtime() method")
        print("  3. Implement forward() method")
        print("  4. Register operator using quick_register_operator()")

        return 0

    except Exception as e:
        print(f"Error generating skeleton: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


def cmd_list_templates(args):
    """List available operator templates"""
    from iron.model_convert import TEMPLATES, get_operator_template

    print("Available Operator Templates")
    print("=" * 60)

    for name, template in TEMPLATES.items():
        print(f"\n{name}:")
        print(f"  Class: {template.name}")
        print(f"  Category: {template.category.value}")
        print(f"  Description: {template.description}")
        print(f"  Required methods: {', '.join(template.required_methods)}")

    return 0


def main():
    parser = argparse.ArgumentParser(
        prog="iron-convert",
        description="IRON Model Converter - Convert HuggingFace models to NPU format",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # === scan command ===
    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan model architecture",
        description="Scan a model's architecture to identify layers and components",
    )
    scan_parser.add_argument(
        "model",
        help="HuggingFace model name or path to model directory",
    )
    scan_parser.add_argument(
        "--output",
        "-o",
        help="Output path for scan results (JSON)",
    )
    scan_parser.add_argument(
        "--transformers",
        "-t",
        action="store_true",
        help="Use Transformers library directly (more accurate)",
    )
    scan_parser.add_argument(
        "--auto",
        "-a",
        action="store_true",
        help="Try Transformers first, fall back to AST scanner",
    )
    scan_parser.add_argument(
        "--trust-remote-code",
        action="store_true",
        help="Trust remote code for custom architectures",
    )
    scan_parser.set_defaults(func=cmd_scan)

    # === analyze command ===
    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze model compatibility",
        description="Analyze gaps between model requirements and IRON capabilities",
    )
    analyze_parser.add_argument(
        "model",
        help="HuggingFace model name or path to model directory",
    )
    analyze_parser.add_argument(
        "--output",
        "-o",
        help="Output path for gap report (JSON)",
    )
    analyze_parser.add_argument(
        "--quick",
        "-q",
        action="store_true",
        help="Quick check only",
    )
    analyze_parser.add_argument(
        "--json",
        action="store_true",
        help="Output full report as JSON",
    )
    analyze_parser.set_defaults(func=cmd_analyze)

    # === check command ===
    check_parser = subparsers.add_parser(
        "check",
        help="Quick compatibility check",
        description="Quick check if a model is likely supported",
    )
    check_parser.add_argument(
        "model",
        help="HuggingFace model name or path",
    )
    check_parser.set_defaults(func=cmd_check)

    # === convert command ===
    convert_parser = subparsers.add_parser(
        "convert",
        help="Convert model to IRON format",
        description="Convert a HuggingFace model to IRON NPU format",
    )
    convert_parser.add_argument(
        "model",
        help="HuggingFace model name or path",
    )
    convert_parser.add_argument(
        "--output",
        "-o",
        help="Output directory for converted model",
    )
    convert_parser.add_argument(
        "--aie-columns",
        type=int,
        help="Number of AIE columns (default: 8)",
    )
    convert_parser.add_argument(
        "--tile-m",
        type=int,
        help="Tile size for M dimension (default: 64)",
    )
    convert_parser.add_argument(
        "--tile-k",
        type=int,
        help="Tile size for K dimension (default: 64)",
    )
    convert_parser.add_argument(
        "--tile-n",
        type=int,
        help="Tile size for N dimension (default: 64)",
    )
    convert_parser.add_argument(
        "--disable-aie-gemm",
        action="store_true",
        help="Disable AIE GEMM operators",
    )
    convert_parser.add_argument(
        "--enable-aie-gemv",
        action="store_true",
        help="Enable AIE GEMV operators (for decode)",
    )
    convert_parser.add_argument(
        "--disable-aie-norm",
        action="store_true",
        help="Disable AIE normalization operators",
    )
    convert_parser.add_argument(
        "--enable-aie-mha",
        action="store_true",
        help="Enable fused MHA operators",
    )
    convert_parser.add_argument(
        "--enable-aie-rope",
        action="store_true",
        help="Enable AIE RoPE operators",
    )
    convert_parser.add_argument(
        "--disable-aie-ffn",
        action="store_true",
        help="Disable AIE FFN operators",
    )
    convert_parser.add_argument(
        "--disable-kv-cache",
        action="store_true",
        help="Disable KV cache",
    )
    convert_parser.add_argument(
        "--max-seq-len",
        type=int,
        help="Maximum sequence length (default: 512)",
    )
    convert_parser.add_argument(
        "--batch-size",
        type=int,
        help="Batch size (default: 1)",
    )
    convert_parser.add_argument(
        "--quantize",
        action="store_true",
        help="Enable quantization",
    )
    convert_parser.add_argument(
        "--quant-type",
        choices=["awq", "gptq"],
        help="Quantization type",
    )
    convert_parser.add_argument(
        "--numpy-format",
        action="store_true",
        help="Save weights in NumPy format",
    )
    convert_parser.add_argument(
        "--compile",
        action="store_true",
        help="Compile AIE artifacts after conversion",
    )
    convert_parser.add_argument(
        "--skip-check",
        action="store_true",
        help="Skip compatibility check",
    )
    convert_parser.add_argument(
        "--force",
        action="store_true",
        help="Force conversion even if not feasible",
    )
    convert_parser.set_defaults(func=cmd_convert)

    # === compile command ===
    compile_parser = subparsers.add_parser(
        "compile",
        help="Compile AIE artifacts",
        description="Compile AIE artifacts for a converted model",
    )
    compile_parser.add_argument(
        "model_dir",
        help="Path to converted model directory",
    )
    compile_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print compilation commands without running",
    )
    compile_parser.set_defaults(func=cmd_compile)

    # === infer command ===
    infer_parser = subparsers.add_parser(
        "infer",
        help="Run inference",
        description="Run inference with a converted model",
    )
    infer_parser.add_argument(
        "model_dir",
        help="Path to converted model directory",
    )
    infer_parser.add_argument(
        "--prompt",
        type=str,
        help="Input prompt text",
    )
    infer_parser.add_argument(
        "--input-file",
        type=str,
        help="File containing input token IDs",
    )
    infer_parser.add_argument(
        "--max-tokens",
        type=int,
        default=100,
        help="Maximum tokens to generate (default: 100)",
    )
    infer_parser.add_argument(
        "--temperature",
        type=float,
        default=1.0,
        help="Sampling temperature (default: 1.0)",
    )
    infer_parser.add_argument(
        "--top-k",
        type=int,
        help="Top-k sampling (optional)",
    )
    infer_parser.set_defaults(func=cmd_infer)

    # === skeleton command ===
    skeleton_parser = subparsers.add_parser(
        "skeleton",
        help="Generate operator skeleton",
        description="Generate skeleton code for a custom operator",
    )
    skeleton_parser.add_argument(
        "operator_name",
        help="Name of the operator",
    )
    skeleton_parser.add_argument(
        "--output",
        "-o",
        help="Output file path",
    )
    skeleton_parser.set_defaults(func=cmd_skeleton)

    # === list-templates command ===
    templates_parser = subparsers.add_parser(
        "list-templates",
        help="List operator templates",
        description="List available operator templates",
    )
    templates_parser.set_defaults(func=cmd_list_templates)

    # Parse and execute
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
