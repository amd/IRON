# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import time
import argparse
from pathlib import Path
from typing import Literal

import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
import numpy as np

# Add project root to Python path to enable imports from golden_model
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from golden_model.src.operator.aie_mha import AIEMHA
from golden_model.src.operator.aie_base import AIEOperatorBase

torch_attention_backends = {
    "math": SDPBackend.MATH,
    "flash-attention": SDPBackend.FLASH_ATTENTION,
}


def torch_mha_reference(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    torch_attention_impl: Literal["MATH", "FLASH_ATTENTION"],
) -> torch.Tensor:
    """PyTorch reference implementation matching mha_golden.py"""

    inv_scale = 1 / np.sqrt(k.shape[-1])
    with sdpa_kernel(backends=torch_attention_impl):
        return torch.nn.functional.scaled_dot_product_attention(
            q.to(torch.bfloat16),
            k.to(torch.bfloat16),
            v.to(torch.bfloat16),
            dropout_p=0.0,
            is_causal=True,
            scale=inv_scale,
        )


def compare_outputs(
    aie_output: torch.Tensor,
    torch_output: torch.Tensor,
    abs_tol: float = 0.15,
    rel_tol: float = 0.04,
    percentage_of_error_threshold: float = 0.005,
) -> tuple:
    """Compare AIE and PyTorch outputs with tolerance checking

    Args:
        aie_output: Output from AIE
        torch_output: Output from PyTorch reference
        abs_tol: Absolute tolerance threshold
        rel_tol: Relative tolerance threshold
        percentage_of_error_threshold: Maximum percentage of elements allowed to exceed tolerances (default 0.5%)
    """

    # Convert to float32 for comparison
    aie_float = aie_output.float()
    torch_float = torch_output.float()

    # Calculate differences
    abs_diff = torch.abs(aie_float - torch_float)
    rel_diff = abs_diff / (torch.abs(torch_float) + 1e-8)

    # Count violations (elements that exceed BOTH absolute AND relative tolerances)
    violations_mask = (abs_diff > abs_tol) & (rel_diff > rel_tol)
    num_violations = torch.sum(violations_mask).item()

    # Statistics
    max_abs_diff = torch.max(abs_diff).item()
    mean_abs_diff = torch.mean(abs_diff).item()
    max_rel_diff = torch.max(rel_diff).item()
    mean_rel_diff = torch.mean(rel_diff).item()

    num_elements = aie_float.numel()
    num_abs_violations = torch.sum(abs_diff > abs_tol).item()
    num_rel_violations = torch.sum(rel_diff > rel_tol).item()

    # Calculate maximum acceptable errors based on percentage threshold
    max_acceptable_errors = int(np.floor(num_elements * percentage_of_error_threshold))

    # Pass if number of violations is within acceptable threshold
    threshold_pass = num_violations <= max_acceptable_errors

    return {
        "threshold_pass": threshold_pass,
        "num_violations": num_violations,
        "max_acceptable_errors": max_acceptable_errors,
        "percentage_threshold": percentage_of_error_threshold
        * 100,  # Convert to percentage
        "max_abs_diff": max_abs_diff,
        "mean_abs_diff": mean_abs_diff,
        "max_rel_diff": max_rel_diff,
        "mean_rel_diff": mean_rel_diff,
        "num_elements": num_elements,
        "num_abs_violations": num_abs_violations,
        "num_rel_violations": num_rel_violations,
    }


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="MHA Operator Test and Benchmark")
    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="Run in benchmark mode (performance only, no accuracy comparison)",
    )
    parser.add_argument(
        "--impl",
        choices=["aie", "pytorch", "both"],
        default="both",
        help="Implementation to benchmark: aie, pytorch, or both (default: both)",
    )
    parser.add_argument(
        "--seq-len", type=int, default=2048, help="Sequence length (default: 2048)"
    )
    parser.add_argument(
        "--head-dim", type=int, default=64, help="Head dimension (default: 64)"
    )
    parser.add_argument(
        "--num-heads", type=int, default=32, help="Number of heads (default: 32)"
    )
    parser.add_argument(
        "--warmup",
        type=int,
        default=10,
        help="Number of warmup iterations (default: 10)",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=10,
        help="Number of timed iterations (default: 10)",
    )

    args = parser.parse_args()

    seq_len = args.seq_len
    head_dim = args.head_dim
    num_heads = args.num_heads
    num_warmup = args.warmup
    num_iterations = args.iterations
    benchmark_mode = args.benchmark
    impl_choice = args.impl

    torch_attention_impl = torch_attention_backends["flash-attention"]

    print(f"\n{'='*60}")
    print(f"MHA {'Benchmark' if benchmark_mode else 'Test'} Configuration:")
    print(
        f"  Mode: {'Benchmark' if benchmark_mode else 'Test (with accuracy comparison)'}"
    )
    print(f"  Implementation: {impl_choice.upper()}")
    print(f"  Heads: {num_heads}")
    print(f"  Sequence Length: {seq_len}")
    print(f"  Head Dimension: {head_dim}")
    print(f"  Warmup iterations: {num_warmup}")
    print(f"  Test iterations: {num_iterations}")
    print(f"{'='*60}\n")

    # Initialize AIE MHA if needed
    aie_mha = None
    if impl_choice in ["aie", "both"]:
        print("Initializing AIE MHA operator...")
        aie_mha = AIEMHA(
            num_heads=num_heads,
            seq_len=seq_len,
            d=head_dim,
            num_KV_heads=0,
        )
        AIEOperatorBase.compile_all_operators()
        AIEOperatorBase.prepare_runtime()
        print("AIE MHA initialization complete.\n")

    # Generate random test data
    torch.manual_seed(42)
    q = torch.rand(1, num_heads, seq_len, head_dim, dtype=torch.bfloat16) * 4
    k = torch.rand(1, num_heads, seq_len, head_dim, dtype=torch.bfloat16) * 4
    v = torch.rand(1, num_heads, seq_len, head_dim, dtype=torch.bfloat16) * 4

    # Run PyTorch benchmark if needed
    torch_output = None
    torch_time_avg = None
    if impl_choice in ["pytorch", "both"]:
        # Warmup iterations for PyTorch
        print(f"Running {num_warmup} warmup iterations on PyTorch...")
        for i in range(num_warmup):
            _ = torch_mha_reference(q, k, v, torch_attention_impl)
        print("PyTorch warmup complete.\n")

        # Timed iterations for PyTorch
        print(f"Running {num_iterations} timed iterations on PyTorch...")
        torch_times = []
        for i in range(num_iterations):
            torch_start = time.perf_counter()
            torch_output = torch_mha_reference(q, k, v, torch_attention_impl)
            torch_end = time.perf_counter()
            torch_times.append((torch_end - torch_start) * 1000)  # Convert to ms

        torch_time_avg = np.mean(torch_times)
        torch_time_min = np.min(torch_times)
        torch_time_max = np.max(torch_times)
        torch_time_std = np.std(torch_times)
        print("PyTorch timing complete.\n")

    # Run AIE benchmark if needed
    aie_output = None
    aie_time_avg = None
    if impl_choice in ["aie", "both"]:
        # Warmup iterations for AIE
        print(f"Running {num_warmup} warmup iterations on AIE...")
        for i in range(num_warmup):
            _ = aie_mha(q, k, v)
        print("AIE warmup complete.\n")

        # Timed iterations for AIE
        print(f"Running {num_iterations} timed iterations on AIE...")
        aie_times = []
        for i in range(num_iterations):
            aie_start = time.perf_counter()
            aie_output = aie_mha(q, k, v)
            aie_end = time.perf_counter()
            aie_times.append((aie_end - aie_start) * 1000)  # Convert to ms

        aie_time_avg = np.mean(aie_times)
        aie_time_min = np.min(aie_times)
        aie_time_max = np.max(aie_times)
        aie_time_std = np.std(aie_times)

    # Print performance results
    print(f"\n{'='*60}")
    print(f"Performance Results:")
    print(f"{'='*60}")

    if impl_choice in ["pytorch", "both"]:
        print(f"PyTorch MHA:")
        print(f"  Average time: {torch_time_avg:.3f} ms")
        print(f"  Min time: {torch_time_min:.3f} ms")
        print(f"  Max time: {torch_time_max:.3f} ms")
        print(f"  Std dev: {torch_time_std:.3f} ms")

    if impl_choice in ["aie", "both"]:
        if impl_choice == "both":
            print()
        print(f"AIE MHA:")
        print(f"  Average time: {aie_time_avg:.3f} ms")
        print(f"  Min time: {aie_time_min:.3f} ms")
        print(f"  Max time: {aie_time_max:.3f} ms")
        print(f"  Std dev: {aie_time_std:.3f} ms")

    if (
        impl_choice == "both"
        and torch_time_avg is not None
        and aie_time_avg is not None
    ):
        print(f"\nSpeedup: {torch_time_avg / aie_time_avg:.2f}x")

    print(f"{'='*60}\n")

    # Compare outputs only if not in benchmark mode and both implementations were run
    if (
        not benchmark_mode
        and impl_choice == "both"
        and aie_output is not None
        and torch_output is not None
    ):
        print("Comparing AIE and PyTorch outputs...")
        comparison = compare_outputs(aie_output, torch_output)

        print(f"\n{'='*60}")
        print(f"Accuracy Results:")
        print(f"{'='*60}")
        print(f"Absolute difference:")
        print(f"  Max: {comparison['max_abs_diff']:.6f}")
        print(f"  Mean: {comparison['mean_abs_diff']:.6f}")
        print(
            f"  Elements exceeding abs_tol (0.15): {comparison['num_abs_violations']} / {comparison['num_elements']}"
        )
        print(f"\nRelative difference:")
        print(f"  Max: {comparison['max_rel_diff']:.6f}")
        print(f"  Mean: {comparison['mean_rel_diff']:.6f}")
        print(
            f"  Elements exceeding rel_tol (0.04): {comparison['num_rel_violations']} / {comparison['num_elements']}"
        )
        print(f"\nError threshold check:")
        print(
            f"  Elements exceeding BOTH tolerances: {comparison['num_violations']} / {comparison['num_elements']}"
        )
        print(
            f"  Maximum acceptable errors ({comparison['percentage_threshold']:.1f}%): {comparison['max_acceptable_errors']}"
        )
        print(f"  Status: {'PASS' if comparison['threshold_pass'] else 'FAIL'}")
        print(f"{'='*60}\n")

        if comparison["threshold_pass"]:
            print("✓ Test PASSED!")
            print(
                f"  ({comparison['num_violations']} errors within acceptable threshold of {comparison['max_acceptable_errors']})"
            )
        else:
            print("✗ Test FAILED!")
            print(
                f"  ({comparison['num_violations']} errors exceed acceptable threshold of {comparison['max_acceptable_errors']})"
            )
    elif benchmark_mode:
        print("Benchmark mode: Skipping accuracy comparison.")

    print(f"\n{'Benchmark' if benchmark_mode else 'Test'} complete.")
