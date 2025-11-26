#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.mha.op import AIEMHA
from operators.mha.reference import generate_golden_reference
from operators.common.test_utils import run_test



regular_test_cases = [
    "--M 32 --K 64 --N 128 --softmax-tile-size 128 --gemm-tile-size 1",
]


extensive_test_cases = [
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--M", type=int, default=32)
    parser.add_argument("--K", type=int, default=64)
    parser.add_argument("--N", type=int, default=128)
    parser.add_argument("--softmax-tile-size", type=int, default=128)
    parser.add_argument("--gemm-tile-size", type=int, default=1)
    args = parser.parse_args()
    
    golden_ref = generate_golden_reference(M=args.M, K=args.K, N=args.N)
    
    operator = AIEMHA(
        M=args.M,
        K=args.K,
        N=args.N,
        softmax_tile_size=args.softmax_tile_size,
        gemm_tile_size=args.gemm_tile_size
    )
    
    input_buffers = {
        'Q': golden_ref['Q'].flatten(),
        'K': golden_ref['K'].flatten(),
        'V': golden_ref['V'].flatten()
    }
    output_buffers = {'O': golden_ref['O'].flatten()}
    
    passed, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-3
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
