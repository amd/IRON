#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Model Analysis Tool - Standalone Version

This is a STANDALONE version of the model analysis tools that works
without the full IRON package or AIE/MLIR dependencies.

Usage:
    python analyze_model.py scan <model_path>
    python analyze_model.py check <model_name>
    python analyze_model.py report <model_path> -o report.json

This tool can analyze any HuggingFace model to determine:
- What layers/components it uses
- Which are supported by IRON NPU
- What gaps need to be filled
- Conversion feasibility
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

# Import the analysis modules directly (they have no AIE dependencies)
exec(
    open(Path(__file__).parent / "architecture_scanner.py")
    .read()
    .replace(
        "from .architecture_scanner import",
        "#",  # Skip relative imports - we're running standalone
    )
)

# Re-define necessary imports for standalone mode
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
    ATTENTION = "attention"
    NORMALIZATION = "normalization"
    ACTIVATION = "activation"
    LINEAR = "linear"
    CONVOLUTION = "convolution"
    EMBEDDING = "embedding"
    POSITIONAL = "positional"
    POOLING = "pooling"
    CUSTOM = "custom"
    UNKNOWN = "unknown"


# Known IRON-supported patterns
SUPPORTED_PATTERNS = {
    "attention": [
        ".*Attention.*",
        ".*MHA.*",
        ".*MultiHead.*",
        ".*GQA.*",
        ".*GroupedQuery.*",
    ],
    "normalization": [".*Norm.*", ".*LayerNorm.*", ".*RMSNorm.*", ".*BatchNorm.*"],
    "activation": [".*ReLU.*", ".*GELU.*", ".*SiLU.*", ".*SwiGLU.*", ".*Softmax.*"],
    "linear": [".*Linear.*", ".*Dense.*", ".*Projection.*", ".*FFN.*", ".*MLP.*"],
    "positional": [".*RoPE.*", ".*Rotary.*", ".*Position.*", ".*Embedding.*"],
}

FALLBACK_PATTERNS = {
    "cpu_fallback": [".*Dropout.*", ".*Cast.*", ".*Slice.*"],
}


def check_layer_support(layer_name: str, module_path: str) -> tuple[bool, str]:
    """Check if a layer is supported by IRON"""
    import re

    combined = f"{layer_name} {module_path}".lower()

    # Check supported patterns
    for category, patterns in SUPPORTED_PATTERNS.items():
        for pattern in patterns:
            if re.match(pattern.lower(), combined):
                return True, f"Supported via {category}"

    # Check fallback patterns
    for fallback, patterns in FALLBACK_PATTERNS.items():
        for pattern in patterns:
            if re.match(pattern.lower(), combined):
                return False, f"Use {fallback}"

    # Unknown - mark as needs review
    return False, "Unknown - needs review"


def scan_model_simple(model_path: str) -> dict:
    """Simple model scanner that works without full IRON dependencies"""
    model_path = Path(model_path)

    result = {
        "model_name": model_path.name,
        "scan_timestamp": datetime.now().isoformat(),
        "layers": [],
        "summary": {
            "total": 0,
            "supported": 0,
            "unsupported": 0,
        },
    }

    # Try to load config.json
    config_path = model_path / "config.json"
    if config_path.exists():
        with open(config_path) as f:
            config = json.load(f)

        result["config"] = {
            "model_type": config.get("model_type", "unknown"),
            "architectures": config.get("architectures", []),
            "hidden_size": config.get("hidden_size", "N/A"),
            "num_layers": config.get("num_hidden_layers", "N/A"),
            "num_heads": config.get("num_attention_heads", "N/A"),
        }

    # Scan Python files for layer classes
    py_files = list(model_path.glob("modeling*.py"))

    for py_file in py_files:
        try:
            with open(py_file) as f:
                source = f.read()

            tree = ast.parse(source)

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_name = node.name

                    # Check if it's a layer class
                    if any(
                        "layer" in base.id.lower()
                        or "attention" in base.id.lower()
                        or "norm" in base.id.lower()
                        for base in node.bases
                        if isinstance(base, ast.Attribute | ast.Name)
                    ):

                        is_supported, note = check_layer_support(
                            class_name, py_file.name
                        )

                        layer_info = {
                            "name": class_name,
                            "module": py_file.name,
                            "is_supported": is_supported,
                            "note": note,
                        }
                        result["layers"].append(layer_info)

                        result["summary"]["total"] += 1
                        if is_supported:
                            result["summary"]["supported"] += 1
                        else:
                            result["summary"]["unsupported"] += 1

        except Exception as e:
            result["scan_error"] = str(e)

    # Calculate support percentage
    if result["summary"]["total"] > 0:
        result["summary"]["support_percentage"] = (
            result["summary"]["supported"] / result["summary"]["total"] * 100
        )
    else:
        result["summary"]["support_percentage"] = 0

    return result


def cmd_scan(args):
    """Scan a model"""
    print(f"Scanning model: {args.model}")
    print("-" * 60)

    result = scan_model_simple(args.model)

    # Print config info
    if "config" in result:
        cfg = result["config"]
        print(f"\nModel Configuration:")
        print(f"  Type: {cfg.get('model_type', 'N/A')}")
        print(f"  Architectures: {', '.join(cfg.get('architectures', ['N/A']))}")
        print(f"  Hidden size: {cfg.get('hidden_size', 'N/A')}")
        print(f"  Layers: {cfg.get('num_layers', 'N/A')}")
        print(f"  Attention heads: {cfg.get('num_heads', 'N/A')}")

    # Print layer summary
    print(f"\nDiscovered Layers:")
    for layer in result.get("layers", []):
        status = "+" if layer["is_supported"] else "-"
        print(f"  [{status}] {layer['name']} ({layer['module']})")
        print(f"      {layer['note']}")

    # Print summary
    summary = result["summary"]
    print(f"\nSummary:")
    print(f"  Total layers: {summary['total']}")
    print(f"  Supported: {summary['supported']} ({summary['support_percentage']:.1f}%)")
    print(f"  Unsupported: {summary['unsupported']}")

    # Save if requested
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nResults saved to: {output_path}")

    return 0


def cmd_check(args):
    """Quick check if model is likely supported"""
    model = args.model

    # Simple heuristic based on model type
    supported_types = ["llama", "mistral", "phi", "gemma", "qwen", "gpt2", "opt"]

    model_lower = model.lower()
    for supported_type in supported_types:
        if supported_type in model_lower:
            print(f"[+] {model}: Likely SUPPORTED")
            return 0

    print(f"[?] {model}: Needs detailed analysis")
    print("\nRun 'python analyze_model.py scan <path>' for full analysis")
    return 1


def cmd_report(args):
    """Generate detailed report"""
    print(f"Generating report for: {args.model}")
    print("-" * 60)

    result = scan_model_simple(args.model)

    # Build feasibility assessment
    support_pct = result["summary"]["support_percentage"]
    if support_pct >= 80:
        feasibility = "FEASIBLE"
        recommendation = "Proceed with conversion"
    elif support_pct >= 50:
        feasibility = "CHALLENGING"
        recommendation = "Custom operators needed for unsupported components"
    else:
        feasibility = "NOT FEASIBLE"
        recommendation = "Significant NPU operator development required"

    report = {
        "model_name": result["model_name"],
        "report_timestamp": datetime.now().isoformat(),
        "analysis": result,
        "feasibility": feasibility,
        "recommendation": recommendation,
    }

    # Save report
    output_path = (
        Path(args.output)
        if args.output
        else Path(f"{result['model_name']}_report.json")
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"\nFeasibility: {feasibility}")
    print(f"Recommendation: {recommendation}")
    print(f"\nReport saved to: {output_path}")

    return 0


def main():
    parser = argparse.ArgumentParser(
        prog="analyze_model.py",
        description="IRON Model Analysis Tool - Analyze HuggingFace models for NPU compatibility",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # scan command
    scan_parser = subparsers.add_parser("scan", help="Scan model architecture")
    scan_parser.add_argument("model", help="Path to model directory")
    scan_parser.add_argument("--output", "-o", help="Output file for results (JSON)")
    scan_parser.set_defaults(func=cmd_scan)

    # check command
    check_parser = subparsers.add_parser("check", help="Quick compatibility check")
    check_parser.add_argument("model", help="HuggingFace model name")
    check_parser.set_defaults(func=cmd_check)

    # report command
    report_parser = subparsers.add_parser("report", help="Generate detailed report")
    report_parser.add_argument("model", help="Path to model directory")
    report_parser.add_argument("--output", "-o", help="Output file for report")
    report_parser.set_defaults(func=cmd_report)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
