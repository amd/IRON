# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import sys
import argparse

import torch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)

from golden_model_lib import export, torch_to_numpy


def main():
    parser = argparse.ArgumentParser(
        description="Generate PyTorch golden reference for SwiGLU"
    )
    parser.add_argument("--output-header", type=str, help="Output header file path")
    parser.add_argument("--output-bin", type=str, help="Output binary file path")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--dim", type=int, default=256, help="Embedding dimension")

    args = parser.parse_args()
    torch.manual_seed(args.seed)

    # Generate golden inputs, N: out features, K: in features, M: sequence length
    val_range = 4
    inp = torch.randn(args.dim, dtype=torch.bfloat16) * val_range
    W1 = torch.randn(args.dim, args.dim, dtype=torch.bfloat16) * val_range
    bias1 = torch.randn(args.dim, dtype=torch.bfloat16) * val_range
    W2 = torch.randn(args.dim, args.dim, dtype=torch.bfloat16) * val_range
    bias2 = torch.randn(args.dim, dtype=torch.bfloat16) * val_range

    # Generate golden outputs
    left = W1 @ inp  # + bias1
    left_swished = torch.nn.functional.silu(left)
    right = W2 @ inp  # + bias2
    result = left_swished * right

    export(
        {
            "inp": torch_to_numpy(inp),
            "W1": torch_to_numpy(W1),
            "W2": torch_to_numpy(W2),
            "left": torch_to_numpy(left),
            "left_swished": torch_to_numpy(left_swished),
            "right": torch_to_numpy(right),
            "result": torch_to_numpy(result),
        },
        header_path=args.output_header,
        bin_path=args.output_bin,
    )


if __name__ == "__main__":
    main()
