#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.softmax.op import AIESoftmax
from operators.softmax.reference import generate_golden_reference
from operators.common.test_utils import run_test



regular_test_cases = [
    "--rows 1 --cols 128 --columns 1 --channels 1 --tile-size 128",
    "--rows 1 --cols 128 --columns 2 --channels 1 --tile-size 64",
    "--rows 1 --cols 128 --columns 1 --channels 2 --tile-size 64",
    "--rows 1 --cols 128 --columns 2 --channels 2 --tile-size 32",
]


extensive_test_cases = [
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=1)
    parser.add_argument("--cols", type=int, default=128)
    parser.add_argument("--columns", type=int, default=1)
    parser.add_argument("--channels", type=int, default=1)
    parser.add_argument("--tile-size", type=int, default=128)
    args = parser.parse_args()
    
    golden_ref = generate_golden_reference(rows=args.rows, cols=args.cols)
    
    operator = AIESoftmax(
        rows=args.rows,
        cols=args.cols,
        num_columns=args.columns,
        num_channels=args.channels,
        tile_size=args.tile_size
    )
    
    input_buffers = {'in': golden_ref['input'].flatten()}
    output_buffers = {'output': golden_ref['output'].flatten()}
    
    passed, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-6
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
