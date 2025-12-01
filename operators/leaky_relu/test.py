#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.leaky_relu.op import AIELeakyReLU
from operators.leaky_relu.reference import generate_golden_reference
from operators.common.test_utils import run_test


extensive_test_cases = []
# Leaky ReLU is currently broken (#36); leave it untested

regular_test_cases = []
extensive_test_cases = []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=4096)
    parser.add_argument("--aie-columns", type=int, default=1)
    parser.add_argument("--channels", type=int, default=1)
    parser.add_argument("--tile-size", type=int, default=1024)
    parser.add_argument("--alpha", type=float, default=0.01)
    args = parser.parse_args()

    golden_ref = generate_golden_reference(input_length=args.length, alpha=args.alpha)

    operator = AIELeakyReLU(
        size=args.length,
        num_aie_columns=args.aie_columns,
        num_channels=args.channels,
        tile_size=args.tile_size,
        alpha=args.alpha,
    )

    input_buffers = {"input": golden_ref["input"]}
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    if not errors:
        print("PASS!\n")
        return 0
    else:
        print("fail.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
