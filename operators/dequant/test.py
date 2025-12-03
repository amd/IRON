#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.dequant.op import AIEDequant
from operators.dequant.reference import generate_golden_reference
from operators.common.test_utils import run_test


regular_input_lengths = [2048]
extensive_input_lengths = [1024, 2048, 4096, 8192]
group_size = 32

regular_test_cases = []
extensive_test_cases = []

for tests, input_lengths in [
    (regular_test_cases, regular_input_lengths),
    (extensive_test_cases, extensive_input_lengths),
]:
    for input_length in input_lengths:
        for num_columns in range(1, 9):  # 1 to 8 columns
            for num_channels in range(1, 3):  # 1 or 2 channels
                total_cores = num_columns * num_channels
                tile_size = input_length // total_cores

                # Cap tile_size at 16384
                if tile_size > 16384:
                    tile_size = 16384

                # Only proceed if tile_size * total_cores == input_length (exact division)
                if tile_size * total_cores == input_length:
                    test_name = f"dequant_{num_columns}_cols_{num_channels}_channels_{input_length}_tile_{tile_size}"
                    cmd = f"-l {input_length} --aie-columns {num_columns} --num-channels {num_channels} --tile-size {tile_size} --group-size {group_size}"
                    tests.append((test_name, cmd))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--length", type=int, default=2048, help="Input length (output elements)"
    )
    parser.add_argument(
        "--aie-columns", type=int, default=2, help="Number of AIE columns"
    )
    parser.add_argument(
        "--num-channels", type=int, default=1, help="Number of channels"
    )
    parser.add_argument("--tile-size", type=int, default=1024, help="Tile size")
    parser.add_argument(
        "--group-size", type=int, default=32, help="Group size for dequantization"
    )
    args = parser.parse_args()

    golden_ref = generate_golden_reference(
        input_length=args.length,
        tile_size=args.tile_size,
        group_size=args.group_size,
    )

    operator = AIEDequant(
        size=args.length,
        num_aie_columns=args.aie_columns,
        num_channels=args.num_channels,
        tile_size=args.tile_size,
        group_size=args.group_size,
    )

    input_buffers = {
        "input": golden_ref["input"].flatten(),
    }
    output_buffers = {"output": golden_ref["output"].flatten()}

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
