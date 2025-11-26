#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.transpose.op import AIETranspose
from operators.transpose.reference import generate_golden_reference
from operators.common.test_utils import run_test



extensive_test_cases = []
MAX_COLUMNS = 8
regular_test_cases = []
extensive_test_cases = []

# Generate tests following the logic in example/transpose/CMakeLists.txt
INPUT_LENGTHS = [2048]
N_LIST = [64]
S_LIST = [8]
EXTENSIVE_TESTING = False
if EXTENSIVE_TESTING:
    INPUT_LENGTHS = [64, 2048]
    N_LIST = [64, 128, 256, 512]

m = 64
n = 64

for M in INPUT_LENGTHS:
    for N in N_LIST:
        for s in S_LIST:
            for NUM_COLUMNS in range(1, MAX_COLUMNS + 1):
                for NUM_CHANNELS in [1, 2]:
                    row_part = M // NUM_CHANNELS
                    col_part = N // NUM_COLUMNS
                    if row_part % m != 0 or col_part % n != 0:
                        continue
                    check_length = row_part * col_part * NUM_CHANNELS * NUM_COLUMNS
                    length = M * N
                    if check_length != length:
                        continue
                    name = f"transpose_{M}x{N}_{NUM_COLUMNS}cols_{NUM_CHANNELS}ch_{s}s"
                    cmd = f"--rows {M} --cols {N} --columns {NUM_COLUMNS}"
                    regular_test_cases.append((name, cmd))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=4096)
    parser.add_argument("--columns", type=int, default=1)
    parser.add_argument("--channels", type=int, default=1)
    parser.add_argument("--tile-size", type=int, default=1024)
    args = parser.parse_args()
    
    golden_ref = generate_golden_reference(rows=args.rows, cols=args.cols)
    
    operator = AIETranspose(
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
