#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.mem_copy.op import AIEMemCopy
from operators.mem_copy.reference import generate_golden_reference
from operators.common.test_utils import run_test


regular_input_lengths = [2048]
extensive_input_lengths = [1024, 2048, 4096, 8192]
bypass_modes = [False]
extensive_bypass_modes = [False, True]

regular_test_cases = []
extensive_test_cases = []

for tests, input_lengths, bypass_list in [
    (regular_test_cases, regular_input_lengths, bypass_modes),
    (extensive_test_cases, extensive_input_lengths, extensive_bypass_modes),
]:
    for input_length in input_lengths:
        for num_cores in range(1, 17):  # 1 to 16 cores
            for num_channels in range(1, 3):  # 1 or 2 channels
                for bypass in bypass_list:
                    # Calculate the maximum cores that can be utilized with 1 or 2 shim channels
                    max_cores = 8 * num_channels  # MAX_COLUMNS (8) * num_channels
                    
                    if max_cores >= num_cores and num_cores >= num_channels:
                        tile_size = input_length // num_cores
                        
                        # Cap tile_size at 8192
                        if tile_size > 8192:
                            tile_size = 8192
                        
                        # Only proceed if tile_size * num_cores == input_length (exact division)
                        if tile_size * num_cores == input_length:
                            bypass_str = "bypass" if bypass else "no_bypass"
                            test_name = f"mem_copy_{num_cores}_cores_{num_channels}_chans_{input_length}_tile_{tile_size}_{bypass_str}"
                            cmd = f"-l {input_length} --num-cores {num_cores} --num-channels {num_channels} --bypass {int(bypass)} --tile-size {tile_size}"
                            tests.append((test_name, cmd))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=2048, help="Input length")
    parser.add_argument("--num-cores", type=int, default=2, help="Number of cores")
    parser.add_argument("--num-channels", type=int, default=1, help="Number of channels")
    parser.add_argument("--bypass", type=int, default=0, help="Use bypass mode (0 or 1)")
    parser.add_argument("--tile-size", type=int, default=1024, help="Tile size")
    args = parser.parse_args()

    bypass = bool(args.bypass)

    golden_ref = generate_golden_reference(
        input_length=args.length,
    )

    operator = AIEMemCopy(
        size=args.length,
        num_cores=args.num_cores,
        num_channels=args.num_channels,
        bypass=bypass,
        tile_size=args.tile_size,
    )

    input_buffers = {
        "input": golden_ref["inout"],
    }
    output_buffers = {"output": golden_ref["inout"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.01, abs_tol=1e-6
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
