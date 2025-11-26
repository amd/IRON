#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.gemm.op import AIEGEMM
from operators.gemm.reference import generate_golden_reference
from operators.common.test_utils import run_test


regular_M_list = [2048]
regular_K_list = [2048]
regular_N_list = [2048]
extensive_M_list = [2048]
extensive_K_list = [2048, 8192, 64]
extensive_N_list = [2048, 8192]

m, k, n = 64, 64, 64
NUM_COLUMNS = 2
B_COL_MAJ = 0
C_COL_MAJ = 0
TRACE_SIZE = 0

regular_test_cases = []
extensive_test_cases = []

# Populate regular_test_cases
for (tests, M_list, K_list, N_list) in [
    (regular_test_cases, regular_M_list, regular_K_list, regular_N_list),
    (extensive_test_cases, extensive_M_list, extensive_K_list, extensive_N_list),
]:
    for M in M_list:
        for K in K_list:
            for N in N_list:
                if N == 8192 and K == 8192:
                    continue  # Untested combination because huge & slow, unused in our application
                tests.append(
                    (
                        f"gemm_{M}x{K}x{N}_{m}x{m}x{n}_{NUM_COLUMNS}_cols_{B_COL_MAJ}_bcolmaj_{C_COL_MAJ}_ccolmaj_{TRACE_SIZE}",
                        f"-M {M} -K {K} -N {N} --columns {NUM_COLUMNS}",
                    )
                )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-M", type=int, default=256)
    parser.add_argument("-K", type=int, default=256)
    parser.add_argument("-N", type=int, default=256)
    parser.add_argument("--columns", type=int, default=1)
    parser.add_argument("--prio-accuracy", type=int, default=1)
    parser.add_argument("--emulate-bf16-mmul-with-bfp16", type=int, default=0)
    args = parser.parse_args()
    
    golden_ref = generate_golden_reference(M=args.M, K=args.K, N=args.N)
    
    operator = AIEGEMM(
        M=args.M,
        K=args.K,
        N=args.N,
        num_columns=args.columns,
        prio_accuracy=bool(args.prio_accuracy)
        emulate_bf16_mmul_with_bfp16=bool(args.emulate_bf16_mmul_with_bfp16)
    )
    
    input_buffers = {
        'A': golden_ref['input'].flatten(),
        'B': golden_ref['input_b'].flatten()
    }
    output_buffers = {'C': golden_ref['output'].flatten()}
    
    passed, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.005, abs_tol=0.005
    )
    
    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")
    
    gflops = (2.0 * args.M * args.K * args.N) / (latency_us * 1e-6) / 1e9
    print(f"Performance: {gflops:.2f} GFLOPS\n")
    
    if passed:
        print("PASS!\n")
        return 0
    else:
        print("fail.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
