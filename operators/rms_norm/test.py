#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.rms_norm.op import AIERMSNorm
from operators.rms_norm.reference import generate_golden_reference
from operators.common.test_utils import run_test



MAX_COLUMNS = 8
regular_test_cases = []
extensive_test_cases = []

INPUT_LENGTHS = [2048]
NUM_CHANNELS = 2
TRACE_SIZE = 65536
EXTENSIVE_TESTING = False
if EXTENSIVE_TESTING:
    INPUT_LENGTHS = [1024, 2048, 4096, 8192]

for input_length in INPUT_LENGTHS:
    for num_columns in range(1, MAX_COLUMNS + 1):
        for num_channels_rms in [1, 2]:
            total_cores = num_columns * num_channels_rms
            tile_size = input_length // total_cores
            if tile_size > 8192:
                tile_size = 8192
            if tile_size * total_cores != input_length:
                continue
            name = f"rms_norm_{num_columns}cols_{num_channels_rms}ch_{input_length}_tile_{tile_size}"
            cmd = f"--rows 1 --cols {tile_size} --columns {num_columns} --channels {num_channels_rms} --tile-size {tile_size}"
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
    
    golden_ref = generate_golden_reference(rows=args.rows, cols=args.cols)
    
    operator = AIERMSNorm(
        size=args.length,
        num_columns=args.columns,
        num_channels=args.channels,
        tile_size=args.tile_size
    )
    
    input_buffers = {
        'input1': golden_ref['input'],
        'input2': golden_ref['weight']
    }
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
