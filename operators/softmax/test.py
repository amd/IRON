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



regular_test_cases = []
extensive_test_cases = []

regular_input_lengths = [4096]
regular_tile_sizes = [1024, 512, 2048]
extensive_input_lengths = []  # Commented out in CMakeLists: 1024, 8192

def get_optimal_columns_channels(input_length, tile_size):
    """Helper function to determine optimal columns and channels for a given input length and tile size"""
    total_cores = input_length // tile_size
    
    if total_cores == 4:
        return 2, 2  # 4 cores: use 2x2 configuration
    elif total_cores == 8:
        return 2, 2  # 8 cores: use 2x2 configuration (each core handles 2 iterations)
    elif total_cores == 2:
        return 1, 2  # 2 cores: use 1x2 configuration
    elif total_cores == 1:
        return 1, 1  # 1 core: use 1x1 configuration
    elif total_cores == 16:
        return 4, 4  # 16 cores: use 4x4 configuration
    else:
        return 2, 2  # Default fallback

for (test_cases, input_lengths, tile_sizes) in [
    (regular_test_cases, regular_input_lengths, regular_tile_sizes),
    (extensive_test_cases, extensive_input_lengths, regular_tile_sizes)
]:
    for input_length in input_lengths:
        for tile_size in tile_sizes:
            optimal_columns, optimal_channels = get_optimal_columns_channels(input_length, tile_size)
            name = f"softmax_{optimal_columns}_cols_{optimal_channels}_channels_{input_length}_tile_{tile_size}"
            cmd = f"-l {input_length} --aie-columns {optimal_columns} --channels {optimal_channels} --tile-size {tile_size}"
            test_cases.append((name, cmd))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=4096)
    parser.add_argument("--aie-columns", type=int, default=1)
    parser.add_argument("--channels", type=int, default=1)
    parser.add_argument("--tile-size", type=int, default=1024)
    args = parser.parse_args()
    
    rows = args.length // args.tile_size
    cols = args.tile_size
    
    golden_ref = generate_golden_reference(rows=rows, cols=cols)
    
    operator = AIESoftmax(
        rows=rows,
        cols=cols,
        num_aie_columns=args.aie_columns,
        num_channels=args.channels,
        tile_size=args.tile_size
    )
    
    input_buffers = {'in': golden_ref['input'].flatten()}
    output_buffers = {'output': golden_ref['output'].flatten()}
    
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
