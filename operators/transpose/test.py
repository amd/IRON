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



regular_test_cases = []
extensive_test_cases = []

max_aie_columns = 8
regular_input_lengths = [2048]
regular_n_list = [64]
extensive_input_lengths = [64, 2048]
extensive_n_list = [64, 128, 256, 512]
s_list = [8]

m = 64
n = 64

for (test_cases, input_lengths, n_list) in [
    (regular_test_cases, regular_input_lengths, regular_n_list),
    (extensive_test_cases, extensive_input_lengths, extensive_n_list)
]:
    for M in input_lengths:
        for N in n_list:
            for s in s_list:
                for num_aie_columns in range(1, max_aie_columns + 1):
                    for num_channels in [1, 2]:
                        row_part = M // num_channels
                        col_part = N // num_aie_columns
                        if row_part % m != 0 or col_part % n != 0:
                            continue
                        check_length = row_part * col_part * num_channels * num_aie_columns
                        length = M * N
                        if check_length != length:
                            continue
                        name = f"transpose_{M}_M_{N}_N_{num_aie_columns}_cols_{num_channels}_channels_{m}_m_{n}_n_{s}_s"
                        cmd = f"-M {M} -N {N} --aie-columns {num_aie_columns} --channels {num_channels} -m {m} -n {n} -s {s}"
                        test_cases.append((name, cmd))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-M", type=int, default=2048)
    parser.add_argument("-N", type=int, default=64)
    parser.add_argument("--aie-columns", type=int, default=1)
    parser.add_argument("--channels", type=int, default=1)
    parser.add_argument("-m", type=int, default=64)
    parser.add_argument("-n", type=int, default=64)
    parser.add_argument("-s", type=int, default=8)
    args = parser.parse_args()
    
    golden_ref = generate_golden_reference(rows=args.M, cols=args.N)
    
    operator = AIETranspose(
        M=args.M,
        N=args.N,
        num_aie_columns=args.aie_columns,
        num_channels=args.channels,
        m=args.m,
        n=args.n,
        s=args.s
    )
    
    input_buffers = {'input': golden_ref['input']}
    output_buffers = {'output': golden_ref['output']}
    
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
