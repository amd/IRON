#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.axpy.op import AIEAXPY
from operators.axpy.reference import generate_golden_reference
from operators.common.test_utils import run_test


regular_test_cases = []
extensive_test_cases = []

max_columns = 8
num_channels = 2
regular_input_lengths = [2048]
regular_scalar_factors = [3.0]

extensive_input_lengths = [1024, 2048, 4096, 8192]
extensive_scalar_factors = [3.0, 10.0]

for test_cases, input_lengths, scalar_factors in [
    (regular_test_cases, regular_input_lengths, regular_scalar_factors),
    (extensive_test_cases, extensive_input_lengths, extensive_scalar_factors),
]:
    for input_length in input_lengths:
        for num_aie_columns in range(1, max_columns + 1):
            tile_size = input_length // num_aie_columns
            if tile_size * num_aie_columns != input_length:
                continue
            for scalar in scalar_factors:
                name = f"axpy_{num_aie_columns}_cols_{num_channels}_channels_{input_length}_tile_{tile_size}_{scalar}"
                cmd = f"-l {input_length} --aie-columns {num_aie_columns} --channels {num_channels} --tile-size {tile_size} --scalar-factor {scalar}"
                test_cases.append((name, cmd))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=4096)
    parser.add_argument("--aie-columns", type=int, default=1)
    parser.add_argument("--channels", type=int, default=1)
    parser.add_argument("--tile-size", type=int, default=2048)
    parser.add_argument("--scalar-factor", type=float, default=3.0)
    args = parser.parse_args()

    golden_ref = generate_golden_reference(
        input_length=args.length, scalar=args.scalar_factor
    )

    operator = AIEAXPY(
        size=args.length,
        num_aie_columns=args.aie_columns,
        num_channels=args.channels,
        tile_size=args.tile_size,
        scalar_factor=args.scalar_factor,
    )

    input_buffers = {"x": golden_ref["A"], "y": golden_ref["B"]}
    output_buffers = {"output": golden_ref["C"]}

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
