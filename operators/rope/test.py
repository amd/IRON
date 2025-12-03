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


regular_test_cases = []
extensive_test_cases = []

max_aie_columns = 8
num_channels = 2
regular_input_lengths = [4096]
regular_method_types = [0]  # 0: Two-halves method
extensive_input_lengths = [1024, 8192]
extensive_method_types = [0, 1]  # 0: Two-halves method, 1: interleaved method

for test_cases, input_lengths, method_types in [
    (regular_test_cases, regular_input_lengths, regular_method_types),
    (extensive_test_cases, extensive_input_lengths, extensive_method_types),
]:
    for input_length in input_lengths:
        for num_aie_columns in range(1, max_aie_columns + 1):
            tile_size = input_length // num_aie_columns
            if tile_size > 4096:
                tile_size = 4096
            check_length = tile_size * num_aie_columns
            if check_length == input_length:
                for method_type in method_types:
                    name = f"rope_{num_aie_columns}_cols_{num_channels}_channels_{input_length}_tile_{tile_size}_{method_type}"
                    cmd = f"-l {input_length} --aie-columns {num_aie_columns} --channels {num_channels} --tile-size {tile_size} --method-type {method_type}"
                    test_cases.append((name, cmd))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=4096)
    parser.add_argument("--aie-columns", type=int, default=1)
    parser.add_argument("--channels", type=int, default=2)
    parser.add_argument("--tile-size", type=int, default=1024)
    parser.add_argument("--method-type", type=int, default=0)
    args = parser.parse_args()

    rows = args.length // args.tile_size
    cols = args.tile_size

    golden_ref = generate_golden_reference(
        rows=rows, cols=cols, method_type=args.method_type
    )

    operator = AIERope(
        size=args.length,
        num_aie_columns=args.aie_columns,
        num_channels=args.channels,
        last_dim=args.tile_size,
        method_type=args.method_type,
    )

    input_buffers = {
        "in": golden_ref["A"].flatten(),
        "angles": golden_ref["B"].flatten(),
    }
    output_buffers = {"output": golden_ref["C"].flatten()}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.05, abs_tol=0.5
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
