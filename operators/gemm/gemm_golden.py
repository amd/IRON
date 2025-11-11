# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import sys
import argparse

import torch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)

from golden_model_lib import export, torch_to_numpy, torch_dtype_map


def main():
    parser = argparse.ArgumentParser(
        description="Generate PyTorch golden reference for SiLU activation function."
    )
    parser.add_argument(
        "--dtype",
        type=str,
        choices=torch_dtype_map.keys(),
        default="bf16",
        help="IO data type",
    )
    parser.add_argument(
        "--output-header", required=True, type=str, help="Output header file path"
    )
    parser.add_argument(
        "--output-bin", required=True, type=str, help="Output binary file path"
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    # Function-specific argument(s)
    parser.add_argument("-M", type=int, default=256, help="Input left mtx rows")
    parser.add_argument(
        "-K", type=int, default=256, help="Input left matx cols/right mtx rows"
    )
    parser.add_argument("-N", type=int, default=256, help="Input right mtx cols")
    parser.add_argument(
        "-b-col-maj",
        type=int,
        choices=[0, 1],
        default=0,
        help="B is read from in column-major or row-major order",
    )
    parser.add_argument(
        "-c-col-maj",
        type=int,
        choices=[0, 1],
        default=0,
        help="C is written to column-major or row-major order",
    )

    args = parser.parse_args()
    torch.manual_seed(args.seed)

    # Generate golden inputs, N: out features, K: in features, M: sequence length
    val_range = 4
    dtype = torch_dtype_map[args.dtype]
    A = torch.randn(args.M, args.K, dtype=dtype) * val_range
    B = torch.rand(args.K, args.N, dtype=dtype) * val_range

    # Generate golden outputs
    C = torch.matmul(A, B)

    if args.b_col_maj:
        B = B.t()  # Transpose B for column-major order

    if args.c_col_maj:
        C = C.t()  # Transpose C for column-major order

    export(
        tensor_dict={
            "A": torch_to_numpy(A),
            "B": torch_to_numpy(B),
            "C": torch_to_numpy(C),
        },
        header_path=args.output_header,
        bin_path=args.output_bin,
    )


if __name__ == "__main__":
    main()
