# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import sys
import argparse

import torch
import numpy as np

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)

from golden_model_lib import export, torch_to_numpy, torch_dtype_map


def main():
    parser = argparse.ArgumentParser(
        description="Generate PyTorch golden reference for matrix multiplication"
    )
    parser.add_argument(
        "--dtype",
        type=str,
        choices=torch_dtype_map.keys(),
        default="bf16",
        help="Input data type",
    )
    parser.add_argument(
        "--output-header",
        type=str,
        default="golden_reference.h",
        help="Output header file path",
    )
    parser.add_argument(
        "--output-bin",
        type=str,
        default="golden_reference.bin",
        help="Output binary file path",
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    parser.add_argument("--heads", type=int, default=1, help="Number of heads")
    parser.add_argument(
        "--S_q", type=int, default=256, help="Sequence length for query (Q)"
    )
    parser.add_argument(
        "--S_kv", type=int, default=256, help="Sequence length for key/value (KV)"
    )
    parser.add_argument("-d", type=int, default=256, help="Embedding dimension (d)")
    parser.add_argument(
        "--num_KV_heads",
        type=int,
        default=2,
        help="Number of heads for Key-Value pairs",
    )

    parser.add_argument(
        "--num_pipeline",
        type=int,
        default=1,
        help="Number of pipelines for padding calculation",
    )

    args = parser.parse_args()

    num_kv_heads = args.num_KV_heads
    if args.num_KV_heads == 0:
        num_kv_heads = args.heads
    number_of_groups = args.heads // num_kv_heads

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    val_range = 4

    dtype = torch_dtype_map[args.dtype]

    Q = torch.rand(args.heads, args.S_q, args.d, dtype=dtype) * val_range
    K = torch.rand(num_kv_heads, args.S_kv, args.d, dtype=dtype) * val_range
    V = torch.rand(num_kv_heads, args.S_kv, args.d, dtype=dtype) * val_range

    K = K.repeat_interleave(number_of_groups, dim=0)
    V = V.repeat_interleave(number_of_groups, dim=0)

    # MHA from PyTorch
    inv_scale = 1 / np.sqrt(K.shape[-1])
    O = torch.nn.functional.scaled_dot_product_attention(
        Q.to(torch.bfloat16),
        K.to(torch.bfloat16),
        V.to(torch.bfloat16),
        dropout_p=0.0,
        is_causal=True,
        scale=inv_scale,
    )

    def pad_to_multiple_of_64(tensor, seq_dim, num_pipeline=1):
        seq_len = tensor.shape[seq_dim]
        padded_seq_len = ((seq_len + 63 * num_pipeline) // (64 * num_pipeline)) * (
            64 * num_pipeline
        )
        if padded_seq_len == seq_len:
            return tensor

        pad_size = padded_seq_len - seq_len
        pad_dims = [0] * (2 * tensor.ndim)
        pad_dims[2 * (tensor.ndim - 1 - seq_dim) + 1] = pad_size

        return torch.nn.functional.pad(tensor, pad_dims)

    Q = pad_to_multiple_of_64(Q, seq_dim=1, num_pipeline=args.num_pipeline)
    K = pad_to_multiple_of_64(K, seq_dim=1, num_pipeline=args.num_pipeline)
    V = pad_to_multiple_of_64(V, seq_dim=1, num_pipeline=args.num_pipeline)
    O = pad_to_multiple_of_64(O, seq_dim=1, num_pipeline=args.num_pipeline)

    tensor_dict = {
        "Q": torch_to_numpy(Q),
        "K": torch_to_numpy(K),
        "V": torch_to_numpy(V),
        "O": torch_to_numpy(O),
    }

    export(tensor_dict, header_path=args.output_header, bin_path=args.output_bin)


if __name__ == "__main__":
    main()
