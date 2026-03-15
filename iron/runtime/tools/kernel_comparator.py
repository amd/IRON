# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: Apache-2.0

"""
Kernel Compatibility Comparator

Compares FastFlowLM kernel interfaces with IRON operator signatures
to determine compatibility and identify required adaptations.

This is part of the Discovery Phase for IRON-Lemonade integration.

Usage:
    python kernel_comparator.py <ff_kernel.json> [iron_signatures.json] [output.md]
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, field, asdict
from enum import Enum


class MatchType(Enum):
    """Kernel match classification"""
    EXACT = "EXACT"  # Drop-in replacement possible
    COMPATIBLE = "COMPATIBLE"  # Wrapper/adaptation needed
    INCOMPATIBLE = "INCOMPATIBLE"  # Significant changes required
    UNKNOWN = "UNKNOWN"  # Insufficient information


@dataclass
class SignatureMatch:
    """Result of signature comparison"""
    iron_operator: str
    fastflowlm_kernel: str
    match_type: str
    compatibility_score: int  # 0-10
    differences: List[str] = field(default_factory=list)
    similarities: List[str] = field(default_factory=list)
    adaptation_notes: List[str] = field(default_factory=list)
    recommendation: str = ""


@dataclass
class CompatibilityReport:
    """Complete compatibility analysis report"""
    fastflowlm_file: str
    iron_operators_analyzed: int
    kernels_found: int
    matches: List[SignatureMatch] = field(default_factory=list)
    summary: Dict[str, Any] = field(default_factory=dict)


def load_default_iron_signatures() -> Dict[str, Dict]:
    """
    Load default IRON operator signatures from codebase analysis.

    These signatures are extracted from iron/operators/*/op.py files
    and represent the canonical interface for each operator.
    """
    return {
        "AIEGEMM": {
            "description": "General Matrix Multiplication",
            "category": "linear",
            "inputs": [
                {"name": "A", "type": "bfloat16*", "direction": "input", "layout": "row-major"},
                {"name": "B", "type": "bfloat16*", "direction": "input", "layout": "col-major"},
            ],
            "outputs": [
                {"name": "C", "type": "bfloat16*", "direction": "output", "layout": "row-major"},
            ],
            "scalars": [
                {"name": "M", "type": "uint32", "description": "Rows of A, C"},
                {"name": "K", "type": "uint32", "description": "Cols of A, rows of B"},
                {"name": "N", "type": "uint32", "description": "Cols of B, C"},
            ],
            "critical": True
        },
        "AIEGEMV": {
            "description": "General Matrix-Vector Multiplication",
            "category": "linear",
            "inputs": [
                {"name": "A", "type": "bfloat16*", "direction": "input"},
                {"name": "x", "type": "bfloat16*", "direction": "input"},
            ],
            "outputs": [
                {"name": "y", "type": "bfloat16*", "direction": "output"},
            ],
            "scalars": [
                {"name": "M", "type": "uint32"},
                {"name": "N", "type": "uint32"},
            ],
            "critical": True
        },
        "AIERMSNorm": {
            "description": "RMS Layer Normalization",
            "category": "normalization",
            "inputs": [
                {"name": "input", "type": "bfloat16*", "direction": "input"},
                {"name": "weight", "type": "bfloat16*", "direction": "input"},
            ],
            "outputs": [
                {"name": "output", "type": "bfloat16*", "direction": "output"},
            ],
            "scalars": [
                {"name": "hidden_size", "type": "uint32"},
                {"name": "epsilon", "type": "float32", "default": 1e-6},
            ],
            "critical": True
        },
        "AIERoPE": {
            "description": "Rotary Position Embeddings",
            "category": "embedding",
            "inputs": [
                {"name": "q", "type": "bfloat16*", "direction": "input"},
                {"name": "k", "type": "bfloat16*", "direction": "input"},
                {"name": "cos", "type": "bfloat16*", "direction": "input"},
                {"name": "sin", "type": "bfloat16*", "direction": "input"},
            ],
            "outputs": [
                {"name": "q_rot", "type": "bfloat16*", "direction": "output"},
                {"name": "k_rot", "type": "bfloat16*", "direction": "output"},
            ],
            "scalars": [
                {"name": "seq_len", "type": "uint32"},
                {"name": "head_dim", "type": "uint32"},
            ],
            "critical": True
        },
        "AIESoftmax": {
            "description": "Softmax activation",
            "category": "activation",
            "inputs": [
                {"name": "input", "type": "bfloat16*", "direction": "input"},
            ],
            "outputs": [
                {"name": "output", "type": "bfloat16*", "direction": "output"},
            ],
            "scalars": [
                {"name": "dim", "type": "int32", "description": "Dimension to apply softmax"},
                {"name": "scale", "type": "float32", "default": 1.0},
            ],
            "critical": True
        },
        "AIESwiGLU": {
            "description": "SwiGLU activation for MLP",
            "category": "activation",
            "inputs": [
                {"name": "input", "type": "bfloat16*", "direction": "input"},
                {"name": "weight_gate", "type": "bfloat16*", "direction": "input"},
                {"name": "weight_up", "type": "bfloat16*", "direction": "input"},
            ],
            "outputs": [
                {"name": "output", "type": "bfloat16*", "direction": "output"},
            ],
            "scalars": [
                {"name": "hidden_size", "type": "uint32"},
                {"name": "intermediate_size", "type": "uint32"},
            ],
            "critical": True
        },
        "AIELayerNorm": {
            "description": "Layer Normalization",
            "category": "normalization",
            "inputs": [
                {"name": "input", "type": "bfloat16*", "direction": "input"},
                {"name": "weight", "type": "bfloat16*", "direction": "input"},
                {"name": "bias", "type": "bfloat16*", "direction": "input"},
            ],
            "outputs": [
                {"name": "output", "type": "bfloat16*", "direction": "output"},
            ],
            "scalars": [
                {"name": "hidden_size", "type": "uint32"},
                {"name": "epsilon", "type": "float32", "default": 1e-5},
            ],
            "critical": False
        },
        "AIEDequant": {
            "description": "Weight dequantization",
            "category": "quantization",
            "inputs": [
                {"name": "input", "type": "int8*", "direction": "input"},
                {"name": "scale", "type": "float32*", "direction": "input"},
            ],
            "outputs": [
                {"name": "output", "type": "bfloat16*", "direction": "output"},
            ],
            "scalars": [
                {"name": "size", "type": "uint32"},
            ],
            "critical": True
        },
        "AIEMHA": {
            "description": "Multi-Head Attention (fused)",
            "category": "attention",
            "inputs": [
                {"name": "query", "type": "bfloat16*", "direction": "input"},
                {"name": "key", "type": "bfloat16*", "direction": "input"},
                {"name": "value", "type": "bfloat16*", "direction": "input"},
            ],
            "outputs": [
                {"name": "output", "type": "bfloat16*", "direction": "output"},
            ],
            "scalars": [
                {"name": "batch_size", "type": "uint32"},
                {"name": "seq_len", "type": "uint32"},
                {"name": "num_heads", "type": "uint32"},
                {"name": "head_dim", "type": "uint32"},
            ],
            "critical": True
        },
        "AIETranspose": {
            "description": "Tensor transpose",
            "category": "layout",
            "inputs": [
                {"name": "input", "type": "bfloat16*", "direction": "input"},
            ],
            "outputs": [
                {"name": "output", "type": "bfloat16*", "direction": "output"},
            ],
            "scalars": [
                {"name": "dim0", "type": "int32"},
                {"name": "dim1", "type": "int32"},
                {"name": "rank", "type": "uint32"},
            ],
            "critical": False
        },
    }


def load_ff_kernels(ff_kernel_json: str) -> List[Dict]:
    """Load FastFlowLM kernel data from JSON file"""
    with open(ff_kernel_json, 'r') as f:
        data = json.load(f)

    # Handle both direct kernel list and wrapped format
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        if 'kernels' in data:
            return data['kernels']
        else:
            # Single kernel info
            return [data]
    else:
        raise ValueError(f"Unexpected format in {ff_kernel_json}")


def normalize_type(type_str: str) -> str:
    """Normalize type string for comparison"""
    type_str = type_str.lower().strip()

    # Common aliases
    type_map = {
        'bfloat16': ['bfloat16', 'bf16', 'bf16_t', 'ml_dtypes.bfloat16'],
        'float32': ['float32', 'float', 'fp32', 'float32_t'],
        'float16': ['float16', 'half', 'fp16', 'float16_t'],
        'int8': ['int8', 'int8_t', 'char'],
        'int32': ['int32', 'int', 'int32_t'],
        'uint32': ['uint32', 'uint', 'uint32_t', 'size_t'],
    }

    for canonical, aliases in type_map.items():
        if type_str in aliases:
            return canonical

    return type_str


def types_compatible(iron_type: str, ff_type: str) -> bool:
    """Check if two type strings are compatible"""
    iron_norm = normalize_type(iron_type)
    ff_norm = normalize_type(ff_type)

    # Direct match
    if iron_norm == ff_norm:
        return True

    # Pointer stripping (handle "bfloat16*" vs "bfloat16")
    iron_base = iron_norm.rstrip('*').strip()
    ff_base = ff_norm.rstrip('*').strip()

    return iron_base == ff_base


def _score_kernel_match(iron_sig: Dict, ff_kernel: Dict) -> Tuple[int, MatchType, List[str], List[str], List[str]]:
    """
    Score how well a FastFlowLM kernel matches an IRON operator.

    Returns: (score, match_type, differences, similarities, adaptation_notes)
    """
    score = 0
    differences = []
    similarities = []
    adaptation_notes = []

    iron_inputs = iron_sig.get('inputs', [])
    iron_outputs = iron_sig.get('outputs', [])
    iron_scalars = iron_sig.get('scalars', [])

    ff_args = ff_kernel.get('arguments', [])

    # Separate FF arguments by type (buffer vs scalar)
    ff_buffers = [a for a in ff_args if a.get('address_qualifier') == 1]
    ff_scalars = [a for a in ff_args if a.get('address_qualifier') == 0]

    # Score input buffer count match
    iron_buffer_count = len(iron_inputs)
    ff_buffer_count = len(ff_buffers)

    if ff_buffer_count == iron_buffer_count:
        score += 3
        similarities.append(f"Input/output buffer count matches ({iron_buffer_count})")
    else:
        differences.append(f"Buffer count mismatch: IRON={iron_buffer_count}, FF={ff_buffer_count}")
        adaptation_notes.append(f"Need adapter for buffer count difference")

    # Score output buffer count match
    iron_output_count = len(iron_outputs)
    # (Assuming outputs are also in ff_buffers, typically at the end)

    # Score argument types
    type_matches = 0
    type_mismatches = 0

    for i, iron_arg in enumerate(iron_inputs):
        if i < len(ff_buffers):
            ff_type = ff_buffers[i].get('type_name', '')
            if types_compatible(iron_arg['type'], ff_type):
                type_matches += 1
                similarities.append(f"Argument {i} ({iron_arg['name']}) type compatible")
            else:
                type_mismatches += 1
                differences.append(f"Type mismatch on arg {i}: {iron_arg['type']} vs {ff_type}")
                adaptation_notes.append(f"May need type conversion for {iron_arg['name']}")

    # Score scalar parameters
    iron_scalar_names = {s['name'].lower() for s in iron_scalars}
    ff_scalar_names = {s.get('name', '').lower() for s in ff_scalars}

    scalar_matches = iron_scalar_names & ff_scalar_names
    scalar_missing = iron_scalar_names - ff_scalar_names
    scalar_extra = ff_scalar_names - iron_scalar_names

    if scalar_matches:
        score += len(scalar_matches)
        similarities.append(f"Common scalars: {', '.join(scalar_matches)}")

    if scalar_missing:
        differences.append(f"Missing scalars: {', '.join(scalar_missing)}")
        adaptation_notes.append(f"Missing scalars may need default values")

    if scalar_extra:
        similarities.append(f"Additional FF scalars: {', '.join(scalar_extra)}")

    # Score work group size (indicates compute pattern)
    iron_wg = iron_sig.get('work_group_size', [1, 1, 1])
    ff_wg = ff_kernel.get('work_group_size', [1, 1, 1])

    if iron_wg == ff_wg:
        similarities.append("Work group size matches")
        score += 1

    # Determine match type based on score
    max_score = 10

    if score >= 8:
        match_type = MatchType.EXACT
    elif score >= 5:
        match_type = MatchType.COMPATIBLE
    elif score >= 2:
        match_type = MatchType.INCOMPATIBLE
    else:
        match_type = MatchType.UNKNOWN

    return score, match_type, differences, similarities, adaptation_notes


def find_best_match(iron_op_name: str, iron_sig: Dict, ff_kernels: List[Dict]) -> SignatureMatch:
    """Find the best matching FastFlowLM kernel for an IRON operator"""

    best_match = None
    best_score = 0
    best_match_type = MatchType.UNKNOWN
    best_differences = []
    best_similarities = []
    best_adaptation = []

    for ff_kernel in ff_kernels:
        ff_name = ff_kernel.get('name', 'unknown')

        # Quick name-based heuristic
        name_similarity = _name_similarity(iron_op_name, ff_name)

        score, match_type, differences, similarities, adaptation = _score_kernel_match(iron_sig, ff_kernel)

        # Boost score for name similarity
        if name_similarity > 0.5:
            score += 1
            similarities.append(f"Name similarity with '{ff_name}'")

        if score > best_score:
            best_score = score
            best_match = ff_name
            best_match_type = match_type
            best_differences = differences
            best_similarities = similarities
            best_adaptation = adaptation

    # Generate recommendation
    recommendation = _generate_recommendation(
        iron_op_name, best_match, best_match_type,
        best_score, best_differences, best_adaptation
    )

    return SignatureMatch(
        iron_operator=iron_op_name,
        fastflowlm_kernel=best_match or "NO_MATCH_FOUND",
        match_type=best_match_type.value,
        compatibility_score=best_score,
        differences=best_differences,
        similarities=best_similarities,
        adaptation_notes=best_adaptation,
        recommendation=recommendation
    )


def _name_similarity(iron_name: str, ff_name: str) -> float:
    """Calculate name similarity between IRON operator and FF kernel"""
    iron_lower = iron_name.lower()
    ff_lower = ff_name.lower()

    # Remove common prefixes
    iron_lower = iron_lower.replace('aie', '').replace('gpu', '')
    ff_lower = ff_lower.replace('kernel', '').replace('_kernel', '')

    # Direct substring match
    if iron_lower in ff_lower or ff_lower in iron_lower:
        return 0.8

    # Key operation matching
    operations = ['gemm', 'gemv', 'norm', 'rms', 'softmax', 'rope', 'swiglu', 'transpose', 'dequant', 'mha', 'attention']

    for op in operations:
        if op in iron_lower and op in ff_lower:
            return 0.7

    return 0.0


def _generate_recommendation(iron_op: str, ff_kernel: str, match_type: MatchType,
                            score: int, differences: List[str], adaptation: List[str]) -> str:
    """Generate actionable recommendation"""

    if match_type == MatchType.EXACT:
        return f"DIRECT USE: {ff_kernel} can be used as drop-in replacement for {iron_op}"

    elif match_type == MatchType.COMPATIBLE:
        return f"WRAPPER NEEDED: {ff_kernel} can work with {iron_op} with adaptation layer. Issues: {'; '.join(adaptation[:3])}"

    elif match_type == MatchType.INCOMPATIBLE:
        return f"SIGNIFICANT CHANGES: {ff_kernel} has fundamental incompatibilities with {iron_op}. Consider using IRON's MLIR-compiled kernel."

    else:
        return f"UNKNOWN: No suitable kernel match found for {iron_op} in FastFlowLM. Must use IRON implementation."


def compare_signatures(iron_sigs: Dict[str, Dict], ff_kernels: List[Dict]) -> List[SignatureMatch]:
    """Compare all IRON operators with FastFlowLM kernels"""

    matches = []

    for iron_op, iron_sig in iron_sigs.items():
        match = find_best_match(iron_op, iron_sig, ff_kernels)
        matches.append(match)

    return matches


def generate_report(matches: List[SignatureMatch], ff_file: str) -> CompatibilityReport:
    """Generate complete compatibility report"""

    # Calculate summary statistics
    total = len(matches)
    exact = sum(1 for m in matches if m.match_type == "EXACT")
    compatible = sum(1 for m in matches if m.match_type == "COMPATIBLE")
    incompatible = sum(1 for m in matches if m.match_type == "INCOMPATIBLE")
    unknown = sum(1 for m in matches if m.match_type == "UNKNOWN")

    critical_ops = [m for m in matches if m.iron_operator in [
        "AIEGEMM", "AIERMSNorm", "AIERoPE", "AIESwiGLU", "AIESoftmax"
    ]]

    critical_compatible = sum(1 for m in critical_ops if m.match_type in ["EXACT", "COMPATIBLE"])

    report = CompatibilityReport(
        fastflowlm_file=ff_file,
        iron_operators_analyzed=total,
        kernels_found=0,  # Would need kernel count from FF
        matches=matches,
        summary={
            "total_operators": total,
            "exact_matches": exact,
            "compatible_matches": compatible,
            "incompatible_matches": incompatible,
            "unknown_matches": unknown,
            "critical_operators_analyzed": len(critical_ops),
            "critical_operators_compatible": critical_compatible,
            "compatibility_percentage": (exact + compatible) / total * 100 if total > 0 else 0,
            "critical_compatibility_percentage": critical_compatible / len(critical_ops) * 100 if critical_ops else 0
        }
    )

    return report


def format_markdown_report(report: CompatibilityReport) -> str:
    """Format report as Markdown"""
    lines = []

    lines.append("# FastFlowLM Kernel Compatibility Report")
    lines.append("")
    lines.append(f"**FastFlowLM kernel file:** {report.fastflowlm_file}")
    lines.append(f"**Analysis date:** Generated by kernel_comparator.py")
    lines.append("")

    # Summary
    lines.append("## Executive Summary")
    lines.append("")
    s = report.summary
    lines.append(f"- **IRON operators analyzed:** {s['total_operators']}")
    lines.append(f"- **Exact matches:** {s['exact_matches']}")
    lines.append(f"- **Compatible (needs wrapper):** {s['compatible_matches']}")
    lines.append(f"- **Incompatible:** {s['incompatible_matches']}")
    lines.append(f"- **Unknown/No match:** {s['unknown_matches']}")
    lines.append(f"- **Overall compatibility:** {s['compatibility_percentage']:.1f}%")
    lines.append("")

    # Critical operators
    lines.append("## Critical Operators Status")
    lines.append("")
    lines.append(f"- **Critical operators analyzed:** {s['critical_operators_analyzed']}")
    lines.append(f"- **Critical operators compatible:** {s['critical_compatibility_percentage']:.1f}%")
    lines.append("")

    # GO/NO-GO recommendation
    critical_threshold = 80  # Need 80% of critical ops compatible
    go_no_go = "GO" if s['critical_compatibility_percentage'] >= critical_threshold else "NO-GO"

    lines.append(f"### GO/NO-GO Recommendation: **{go_no_go}**")
    lines.append("")
    if go_no_go == "GO":
        lines.append(f"Critical operator compatibility ({s['critical_compatibility_percentage']:.1f}%) meets threshold ({critical_threshold}%).")
        lines.append("Proceed with C++ runtime abstraction development.")
    else:
        lines.append(f"Critical operator compatibility ({s['critical_compatibility_percentage']:.1f}%) below threshold ({critical_threshold}%).")
        lines.append("Significant technical blockers identified. Consider alternative approach.")
    lines.append("")

    # Detailed matches
    lines.append("## Detailed Compatibility Analysis")
    lines.append("")
    lines.append("| IRON Operator | FF Kernel | Match Type | Score | Recommendation |")
    lines.append("|--------------|-----------|-----------|-------|----------------|")

    for match in report.matches:
        rec_short = match.recommendation[:60] + "..." if len(match.recommendation) > 60 else match.recommendation
        lines.append(f"| {match.iron_operator} | {match.fastflowlm_kernel} | {match.match_type} | {match.compatibility_score}/10 | {rec_short} |")

    lines.append("")

    # Detailed sections per operator
    for match in report.matches:
        lines.append(f"### {match.iron_operator}")
        lines.append("")
        lines.append(f"**Best match:** {match.fastflowlm_kernel}")
        lines.append(f"**Match type:** {match.match_type}")
        lines.append(f"**Compatibility score:** {match.compatibility_score}/10")
        lines.append("")

        if match.similarities:
            lines.append("**Similarities:**")
            for sim in match.similarities:
                lines.append(f"- {sim}")
            lines.append("")

        if match.differences:
            lines.append("**Differences:**")
            for diff in match.differences:
                lines.append(f"- {diff}")
            lines.append("")

        if match.adaptation_notes:
            lines.append("**Adaptation needed:**")
            for note in match.adaptation_notes:
                lines.append(f"- {note}")
            lines.append("")

        lines.append(f"**Recommendation:** {match.recommendation}")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Kernel Compatibility Comparator")
        print("=" * 50)
        print("\nCompares FastFlowLM kernel interfaces with IRON operator signatures.")
        print("\nUsage: python kernel_comparator.py <ff_kernel.json> [iron_signatures.json] [output.md]")
        print("\nArguments:")
        print("  ff_kernel.json       - FastFlowLM kernel JSON from xclbin_inspector.py")
        print("  iron_signatures.json - Optional custom IRON signatures (uses defaults if omitted)")
        print("  output.md            - Optional output file for Markdown report")
        sys.exit(1)

    ff_kernel_file = sys.argv[1]
    iron_sig_file = sys.argv[2] if len(sys.argv) > 2 else None
    output_file = sys.argv[3] if len(sys.argv) > 3 else None

    # Load FastFlowLM kernels
    print(f"Loading FastFlowLM kernels from {ff_kernel_file}...")
    ff_kernels = load_ff_kernels(ff_kernel_file)
    print(f"  Found {len(ff_kernels)} kernels")

    # Load IRON signatures
    if iron_sig_file:
        print(f"Loading IRON signatures from {iron_sig_file}...")
        with open(iron_sig_file, 'r') as f:
            iron_sigs = json.load(f)
    else:
        print("Using default IRON operator signatures...")
        iron_sigs = load_default_iron_signatures()
    print(f"  Analyzing {len(iron_sigs)} operators")

    # Compare
    print("\nComparing signatures...")
    matches = compare_signatures(iron_sigs, ff_kernels)

    # Generate report
    report = generate_report(matches, ff_kernel_file)

    # Output Markdown report
    md_report = format_markdown_report(report)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(md_report)
        print(f"\nReport written to {output_file}")
    else:
        print("\n" + "=" * 60)
        print(md_report)

    # Print summary
    s = report.summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Compatibility: {s['compatibility_percentage']:.1f}%")
    print(f"Critical ops: {s['critical_compatibility_percentage']:.1f}% compatible")

    go_no_go = "GO" if s['critical_compatibility_percentage'] >= 80 else "NO-GO"
    print(f"\nRecommendation: {go_no_go}")


if __name__ == '__main__':
    main()
