# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Model Analysis CLI

Usage:
    python -m iron.model_analysis check <model>
    python -m iron.model_analysis scan <model>
    python -m iron.model_analysis analyze <model>
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime


def cmd_check(args):
    """Quick check if model is supported"""
    from . import quick_check

    result = quick_check(args.model)

    if result:
        print(f"[+] {args.model}: Likely SUPPORTED")
        return 0
    else:
        print(f"[?] {args.model}: Needs detailed analysis")
        print("\nRun: python -m iron.model_analysis analyze <model>")
        return 1


def cmd_scan(args):
    """Scan model architecture"""
    from . import scan_model_from_transformers

    print(f"Scanning: {args.model}")
    print("-" * 60)

    try:
        info = scan_model_from_transformers(
            args.model, trust_remote_code=args.trust_remote_code
        )

        # Print summary directly from info object
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
        ]
        print("\n".join(lines))

        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            report = {
                "model_name": info.architecture_name,
                "model_type": info.model_type,
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
            }

            with open(output_path, "w") as f:
                json.dump(report, f, indent=2)

            print(f"\nSaved to: {output_path}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1

    return 0


def cmd_analyze(args):
    """Analyze model compatibility"""
    from . import generate_gap_report, print_gap_summary

    print(f"Analyzing: {args.model}")
    print("-" * 60)

    try:
        # Generate report
        report = generate_gap_report(args.model)

        # Print summary
        print(print_gap_summary(args.model))

        # Save if requested
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            report.save(output_path)
            print(f"\nReport saved to: {output_path}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1

    return 0


def cmd_spec(args):
    """Generate operator specification for a layer"""
    from .operator_spec import generate_operator_spec, save_operator_spec

    print(f"Generating spec for: {args.layer} in {args.model}")
    print("-" * 60)

    try:
        # Generate spec
        spec = generate_operator_spec(
            args.model, args.layer, trust_remote_code=args.trust_remote_code
        )

        # Output
        if args.output:
            save_operator_spec(spec, args.output)
            print(f"\nSpec saved to: {args.output}")
        else:
            print()
            print(spec.to_markdown())

        # Generate skeleton if requested
        if args.skeleton:
            from .extensibility import generate_operator_skeleton

            skeleton = generate_operator_skeleton(args.layer)
            skeleton_path = Path(args.skeleton)
            skeleton_path.parent.mkdir(parents=True, exist_ok=True)
            with open(skeleton_path, "w") as f:
                f.write(skeleton)
            print(f"\nOperator skeleton saved to: {skeleton_path}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1

    return 0


def cmd_master(args):
    """Generate master document for implementing an operator"""
    from .generate_master_doc import generate_master_document

    print(f"Generating master document for: {args.layer} in {args.model}")
    print("-" * 60)

    try:
        # Generate document
        doc = generate_master_document(args.model, args.layer)

        # Output
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(doc)

        print(f"\nMaster document saved to: {output_path.absolute()}")
        print("\nNext steps:")
        print(f"  1. Review {args.output}")
        print(f"  2. Create operator directory: mkdir {args.layer.lower()}")
        print(f"  3. Copy skeleton code from the document")
        print(f"  4. Implement design.py based on the templates")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1

    return 0


def main():
    parser = argparse.ArgumentParser(
        prog="python -m iron.model_analysis",
        description="IRON Model Analysis - Cross-platform model compatibility checker",
    )

    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # check
    check_p = subparsers.add_parser("check", help="Quick compatibility check")
    check_p.add_argument("model", help="HuggingFace model name")
    check_p.set_defaults(func=cmd_check)

    # scan
    scan_p = subparsers.add_parser("scan", help="Scan model architecture")
    scan_p.add_argument("model", help="HuggingFace model name or path")
    scan_p.add_argument("--output", "-o", help="Output file (JSON)")
    scan_p.add_argument(
        "--trust-remote-code", action="store_true", help="Trust remote code"
    )
    scan_p.set_defaults(func=cmd_scan)

    # analyze
    analyze_p = subparsers.add_parser("analyze", help="Analyze compatibility")
    analyze_p.add_argument("model", help="HuggingFace model name or path")
    analyze_p.add_argument("--output", "-o", help="Output file (JSON)")
    analyze_p.set_defaults(func=cmd_analyze)

    # spec - generate operator specification
    spec_p = subparsers.add_parser(
        "spec", help="Generate operator specification for a layer"
    )
    spec_p.add_argument("model", help="HuggingFace model name")
    spec_p.add_argument(
        "--layer", "-l", required=True, help="Layer class name (e.g., MistralAttention)"
    )
    spec_p.add_argument("--output", "-o", help="Output file (markdown)")
    spec_p.add_argument(
        "--skeleton", "-s", help="Generate operator skeleton code to file"
    )
    spec_p.add_argument(
        "--trust-remote-code", action="store_true", help="Trust remote code"
    )
    spec_p.set_defaults(func=cmd_spec)

    # master - generate master document
    master_p = subparsers.add_parser(
        "master",
        help="Generate MASTER document with ALL data for implementing an operator",
    )
    master_p.add_argument("model", help="HuggingFace model name")
    master_p.add_argument(
        "--layer", "-l", required=True, help="Layer class name (e.g., MistralAttention)"
    )
    master_p.add_argument(
        "--output",
        "-o",
        default="MASTER_DOC.md",
        help="Output file (default: MASTER_DOC.md)",
    )
    master_p.add_argument(
        "--trust-remote-code", action="store_true", help="Trust remote code"
    )
    master_p.set_defaults(func=cmd_master)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
