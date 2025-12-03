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
    (
        "mha",
        "--seq-len 16384 --dim 64 --num-heads 1 --num-pipelines 8",
    ),
]

extensive_test_cases = []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seq-len", type=int, default=16384)
    parser.add_argument("--dim", type=int, default=64)
    parser.add_argument("--num-heads", type=int, default=1)
    parser.add_argument("--num-pipelines", type=int, default=8)
    args = parser.parse_args()

    golden_ref = generate_golden_reference(
        S_q=args.seq_len,
        S_kv=args.seq_len,
        d=args.dim,
        heads=args.num_heads,
        num_kv_heads=args.num_heads,
        num_pipeline=args.num_pipelines,
    )

    operator = AIEMHA(
        num_heads=args.num_heads,
        seq_len=args.seq_len,
        d=args.dim,
        num_KV_heads=args.num_heads,
        num_of_pipelines=args.num_pipelines,
    )

    input_buffers = {
        "Q": golden_ref["Q"].flatten(),
        "K": golden_ref["K"].flatten(),
        "V": golden_ref["V"].flatten(),
    }
    output_buffers = {"O": golden_ref["O"].flatten()}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=4.0e-2, abs_tol=1.5e-1
    )

    error_threshold = 0.005
    max_acceptable_errors = int(
        args.seq_len * args.dim * args.num_heads * error_threshold
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")
    print(
        "({} errors out of {} max allowable)".format(
            len(errors["O"]), max_acceptable_errors
        )
    )

    if len(errors["O"]) <= max_acceptable_errors:
        print("PASS!\n")
        return 0
    else:
        print("fail.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
