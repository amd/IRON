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
        description="Generate PyTorch golden reference for Transpose function."
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
    parser.add_argument("--rows", type=int, default=42, help="Number of rows")
    parser.add_argument("--cols", type=int, default=42, help="Number of columns")

    args = parser.parse_args()
    torch.manual_seed(args.seed)

    # Generate golden inputs
    val_range = 4
    A = torch.rand(args.rows, args.cols, dtype=torch_dtype_map[args.dtype]) * val_range

    # Generate golden outputs
    B = torch.transpose(A, 0, 1)

    export(
        tensor_dict={"A": torch_to_numpy(A), "B": torch_to_numpy(B)},
        header_path=args.output_header,
        bin_path=args.output_bin,
    )


if __name__ == "__main__":
    main()
