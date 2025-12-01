#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.gemv.op import AIEGEMV
from operators.gemv.reference import generate_golden_reference
from operators.common.test_utils import run_test


regular_test_cases = [
    ("matrix_vector_mul_128x128_32_1col", "-M 128 -K 128 --aie-columns 1 --tile-size 32"),
    ("matrix_vector_mul_2048x8192_1_1col", "-M 2048 -K 8192 --aie-columns 1 --tile-size 1"),
    ("matrix_vector_mul_8192x2048_4_1col", "-M 8192 -K 2048 --aie-columns 1 --tile-size 4"),
    ("matrix_vector_mul_2048x8192_1_2col", "-M 2048 -K 8192 --aie-columns 2 --tile-size 1"),
    ("matrix_vector_mul_8192x2048_4_2col", "-M 8192 -K 2048 --aie-columns 2 --tile-size 4"),
    ("matrix_vector_mul_2048x8192_1_4col", "-M 2048 -K 8192 --aie-columns 4 --tile-size 1"),
    ("matrix_vector_mul_8192x2048_4_4col", "-M 8192 -K 2048 --aie-columns 4 --tile-size 4"),
    ("matrix_vector_mul_2048x8192_1_8col", "-M 2048 -K 8192 --aie-columns 8 --tile-size 1"),
    ("matrix_vector_mul_8192x2048_4_8col", "-M 8192 -K 2048 --aie-columns 8 --tile-size 4"),
]

extensive_test_cases = list(regular_test_cases)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-M", type=int, default=128)
    parser.add_argument("-K", type=int, default=128)
    parser.add_argument("--aie-columns", type=int, default=1)
    parser.add_argument("--tile-size", type=int, default=1)
    args = parser.parse_args()
    
    golden_ref = generate_golden_reference(M=args.M, K=args.K)
    
    operator = AIEGEMV(
        M=args.M,
        K=args.K,
        num_aie_columns=args.aie_columns,
        tile_size=args.tile_size
    )
    
    input_buffers = {
        'matrix': golden_ref['A'].flatten(),
        'vector': golden_ref['B']
    }
    output_buffers = {'output': golden_ref['C']}
    
    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-3
    )
    
    print(f"\nLatency: {latency_us:.0f} us")
    
    gflops = (2.0 * args.M * args.K) / (latency_us * 1e-6) / 1e9
    print(f"Throughput: {gflops:.6e} GFLOP/s")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")
    
    if not errors:
        print("PASS!\n")
        return 0
    else:
        print("fail.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
