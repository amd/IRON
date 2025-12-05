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
num_aie_columns = 8
col_maj = [(False, False), (True, False), (False, True)]
trace_size = 0

regular_test_cases = []
extensive_test_cases = []

# Populate regular_test_cases
for tests, M_list, K_list, N_list, col_maj_choices in [
    (regular_test_cases, regular_M_list, regular_K_list, regular_N_list, col_maj),
    (
        extensive_test_cases,
        extensive_M_list,
        extensive_K_list,
        extensive_N_list,
        col_maj,
    ),
]:
    for b_col_maj, c_col_maj in col_maj_choices:
        for M in M_list:
            for K in K_list:
                for N in N_list:
                    if N == 8192 and K == 8192:
                        continue  # Untested combination because huge & slow, unused in our application
                    tests.append(
                        (
                            f"gemm_{M}x{K}x{N}_{m}x{k}x{n}_{num_aie_columns}_cols_{int(b_col_maj)}_bcolmaj_{int(c_col_maj)}_ccolmaj_{trace_size}",
                            f"-M {M} -K {K} -N {N} --aie-columns {num_aie_columns} --b-col-maj {int(b_col_maj)} --c-col-maj {int(c_col_maj)}",
                        )
                    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-M", type=int, default=256)
    parser.add_argument("-K", type=int, default=256)
    parser.add_argument("-N", type=int, default=256)
    parser.add_argument("--aie-columns", type=int, default=8)
    parser.add_argument("--prio-accuracy", type=int, default=1)
    parser.add_argument("--emulate-bf16-mmul-with-bfp16", type=int, default=0)
    parser.add_argument("--b-col-maj", type=int, default=0)
    parser.add_argument("--c-col-maj", type=int, default=0)
    # parser.add_argument("--partition-M", type=int, default=1, help="Partition size for M")
    # parser.add_argument("--partition-K", type=int, default=1, help="Partition size for K")
    parser.add_argument(
        "--partition-N", type=int, default=1, help="Partition size for N"
    )
    args = parser.parse_args()

    golden_ref = generate_golden_reference(
        M=args.M,
        K=args.K,
        N=args.N,
        b_col_maj=bool(args.b_col_maj),
        c_col_maj=bool(args.c_col_maj),
        partition_N=args.partition_N,
    )

    gemm_config = {
        "separate_c_tiles": True,
    }
    operator = AIEGEMM(
        M=args.M,
        K=args.K,
        N=args.N,
        num_aie_columns=args.aie_columns,
        prio_accuracy=bool(args.prio_accuracy),
        emulate_bf16_mmul_with_bfp16=bool(args.emulate_bf16_mmul_with_bfp16),
        b_col_maj=bool(args.b_col_maj),
        c_col_maj=bool(args.c_col_maj),
        # partition_M=args.partition_M,
        # partition_K=args.partition_K,
        partition_N=args.partition_N,
        **gemm_config,
    )

    input_buffers = {
        "A": golden_ref["input"].flatten(),
    }
    output_buffers = {}

    # Create A, B, C dictionaries from the partitioned buffers
    for i in range(args.partition_N):
        input_buffers[f"B_{i}"] = golden_ref["input_b"][i].flatten()
        output_buffers[f"C_{i}"] = golden_ref["output"][i].flatten()
    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.005, abs_tol=0.005
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s")

    gflops = (2.0 * args.M * args.K * args.N) / (latency_us * 1e-6) / 1e9
    print(f"Throughput: {gflops:.6e} GFLOP/s\n")

    if not errors:
        print("PASS!\n")
        return 0
    else:
        print("fail.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
