#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.swiglu_prefill.op import AIESwiGLUPrefill
from operators.swiglu_decode.reference import generate_golden_reference
from operators.common.test_utils import run_test, verify_buffer


# This operation is currently untested except for the integrated llama application tests.
regular_test_cases = []

extensive_test_cases = []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seq-len", type=int, default=512)
    parser.add_argument("--embedding-dim", type=int, default=512)
    parser.add_argument("--hidden-dim", type=int, default=512)
    parser.add_argument("--prio-accuracy", type=int, default=1)
    args = parser.parse_args()

    golden_ref = generate_golden_reference(
        M=args.seq_len, K=args.embedding_dim, N=args.hidden_dim
    )

    operator = AIESwiGLUPrefill(
        seq_len=args.seq_len,
        embedding_dim=args.embedding_dim,
        hidden_dim=args.hidden_dim,
        prio_accuracy=bool(args.prio_accuracy),
    )
    operator.weights_1 = golden_ref["w_gate"]
    operator.weights_2 = golden_ref["w_up"]
    operator.weights_3 = golden_ref["w_down"]

    # In the following, some buffers are commented out.
    # Because this operator calls multiple kernels in sequence, rounding errors due to the smaller bf16 data type accumulate, which can cause it to fail verification.
    # So, instead of verifying the intermediate and final output buffers against the float32-calculated reference, we calculate another reference for those two buffers:
    # This reference is based on the previous intermediate results read back from the AIE operator, "resetting"  the accumulated error to zero.
    # Note that those intermediate results _are_ still verified up to the given tolerance.

    input_buffers = {"input": golden_ref["input"]}
    # output_buffers = {'output': golden_ref['output']}
    output_buffers = {}
    intermediate_buffers = {
        "left": golden_ref["left"],
        "left_swished": golden_ref["left_swished"],
        "right": golden_ref["right"],
        # 'intermediate': golden_ref['intermediate']
    }

    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        intermediate_buffers,
        rel_tol=0.07,
        abs_tol=0.7,
    )

    ref_2 = operator.read_buffer_as_torch(
        "left_swished", (args.seq_len, args.hidden_dim)
    ) * operator.read_buffer_as_torch("right", (args.seq_len, args.hidden_dim))
    errors_2 = verify_buffer(operator, "intermediate", ref_2, rel_tol=0.04, abs_tol=0.4)
    if errors_2:
        errors["intermediate"] = errors_2

    ref_3 = (
        operator.read_buffer_as_torch("intermediate", (args.seq_len, args.hidden_dim))
        @ golden_ref["w_down"].T
    )
    errors_3 = verify_buffer(operator, "output", ref_3, rel_tol=0.04, abs_tol=0.4)
    if errors_3:
        errors["output"] = errors_2

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
