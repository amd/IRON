#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.swiglu_decode.op import AIESwiGLUDecode
from operators.swiglu_decode.reference import generate_golden_reference
from operators.common.test_utils import run_test



regular_test_cases = [
    "--M 1 --K 2048 --N 8192",
]


extensive_test_cases = [
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--M", type=int, default=1)
    parser.add_argument("--K", type=int, default=2048)
    parser.add_argument("--N", type=int, default=8192)
    args = parser.parse_args()
    
    golden_ref = generate_golden_reference(M=args.M, K=args.K, N=args.N)
    
    operator = AIESwiGLUDecode(M=args.M, K=args.K, N=args.N)
    
    input_buffers = {
        'x': golden_ref['x'].flatten(),
        'w_gate': golden_ref['w_gate'].flatten(),
        'w_up': golden_ref['w_up'].flatten(),
        'w_down': golden_ref['w_down'].flatten()
    }
    output_buffers = {'y': golden_ref['y'].flatten()}
    intermediate_buffers = {
        'left': golden_ref['left'].flatten(),
        'left_swished': golden_ref['left_swished'].flatten(),
        'right': golden_ref['right'].flatten(),
        'intermediate': golden_ref['intermediate'].flatten()
    }
    
    passed, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, intermediate_buffers, rel_tol=0.04, abs_tol=1e-3
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
