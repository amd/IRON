#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.layer_norm.op import AIELayerNorm
from operators.layer_norm.reference import generate_golden_reference
from operators.common.test_utils import run_test

regular_test_cases = []
extensive_test_cases = []

max_aie_columns = 8
regular_input_lengths = [2048]
extensive_input_lengths = [1024, 4096, 8192]

for test_cases, input_lengths in [
    (regular_test_cases, regular_input_lengths),
    (extensive_test_cases, extensive_input_lengths),
]:
    for input_length in input_lengths:
        for num_aie_columns in range(1, max_aie_columns + 1):
            for num_channels_layer in range(1, 3):  # 1 or 2
                total_cores = num_aie_columns * num_channels_layer
                tile_size = input_length // total_cores
                if tile_size > 8192:
                    tile_size = 8192
                check_length = tile_size * total_cores
                if check_length == input_length:
                    name = f"layer_norm_{num_aie_columns}_cols_{num_channels_layer}_channels_{input_length}_tile_{tile_size}"
                    cmd = f"-l {input_length} --aie-columns {num_aie_columns} --channels {num_channels_layer} --tile-size {tile_size}"
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

    operator = AIELayerNorm(
        size=args.length,
        num_aie_columns=args.aie_columns,
        num_channels=args.channels,
        tile_size=args.tile_size,
    )

    input_buffers = {"input": golden_ref["input"]}
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.1, abs_tol=0.1
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
