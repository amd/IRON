#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.tanh.op import AIETanh
from operators.tanh.reference import generate_golden_reference
from operators.common.test_utils import run_test



MAX_COLUMNS = 8
regular_test_cases = []
extensive_test_cases = []

INPUT_LENGTHS = [2048]
NUM_CHANNELS = 1
TRACE_SIZE = 65536
EXTENSIVE_TESTING = False
if EXTENSIVE_TESTING:
    INPUT_LENGTHS = [1024, 2048, 4096, 8192]

for input_length in INPUT_LENGTHS:
    for num_columns in range(1, MAX_COLUMNS + 1):
        tile_size = input_length // num_columns
        if tile_size * num_columns != input_length:
            continue
        name = f"tanh_{input_length}_{num_columns}cols_1ch_{tile_size}t"
        cmd = f"-l {input_length} --columns {num_columns} --channels {NUM_CHANNELS} --tile-size {tile_size}"
        if input_length == 2048:
            regular_test_cases.append((name, cmd))
        else:
            extensive_test_cases.append((name, cmd))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=4096)
    parser.add_argument("--columns", type=int, default=1)
    parser.add_argument("--channels", type=int, default=1)
    parser.add_argument("--tile-size", type=int, default=1024)
    args = parser.parse_args()
    
    golden_ref = generate_golden_reference(input_length=args.length)
    
    operator = AIETanh(
        size=args.length,
        num_columns=args.columns,
        num_channels=args.channels,
        tile_size=args.tile_size
    )
    
    input_buffers = {'input': golden_ref['input']}
    output_buffers = {'output': golden_ref['output']}
    
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
