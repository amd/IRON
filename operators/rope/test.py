#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.rope.op import AIERope
from operators.rope.reference import generate_golden_reference
from operators.common.test_utils import run_test



regular_test_cases = [
    "--rows 64 --cols 64 --columns 1 --channels 1",
    "--rows 64 --cols 64 --columns 2 --channels 1",
]


extensive_test_cases = [
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=64)
    parser.add_argument("--cols", type=int, default=64)
    parser.add_argument("--columns", type=int, default=1)
    parser.add_argument("--channels", type=int, default=1)
    args = parser.parse_args()
    
    golden_ref = generate_golden_reference(rows=args.rows, cols=args.cols)
    
    operator = AIERope(
        size=args.rows,
        last_dim=args.cols,
        num_columns=args.columns,
        num_channels=args.channels
    )
    
    input_buffers = {
        'in': golden_ref['A'].flatten(),
        'angles': golden_ref['B'].flatten()
    }
    output_buffers = {'output': golden_ref['C'].flatten()}
    
    passed, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-3
    )
    
    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")
    
    if passed:
        print("PASS!\n")
        return 0
    else:
        print("fail.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
