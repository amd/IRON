# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import sys
import argparse

import torch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)

from golden_model_lib import export, torch_to_numpy, torch_dtype_map


def compute_rope_params(
    head_dim,
    theta_base=10_000,
    context_length=4096,
    method_type=0,
    freq_config=None,
    dtype=torch.float32,
):
    assert head_dim % 2 == 0, "Embedding dimension must be even"

    # Compute the inverse frequencies
    inv_freq = 1.0 / (
        theta_base
        ** (
            torch.arange(0, head_dim, 2, dtype=dtype)[: (head_dim // 2)].float()
            / head_dim
        )
    )

    # Frequency adjustments
    if freq_config is not None:
        low_freq_wavelen = (
            freq_config["original_context_length"] / freq_config["low_freq_factor"]
        )
        high_freq_wavelen = (
            freq_config["original_context_length"] / freq_config["high_freq_factor"]
        )

        wavelen = 2 * torch.pi / inv_freq

        inv_freq_llama = torch.where(
            wavelen > low_freq_wavelen, inv_freq / freq_config["factor"], inv_freq
        )

        smooth_factor = (
            freq_config["original_context_length"] / wavelen
            - freq_config["low_freq_factor"]
        ) / (freq_config["high_freq_factor"] - freq_config["low_freq_factor"])

        smoothed_inv_freq = (1 - smooth_factor) * (
            inv_freq / freq_config["factor"]
        ) + smooth_factor * inv_freq

        is_medium_freq = (wavelen <= low_freq_wavelen) & (wavelen >= high_freq_wavelen)
        inv_freq_llama = torch.where(is_medium_freq, smoothed_inv_freq, inv_freq_llama)
        inv_freq = inv_freq_llama

    # Generate position indices
    positions = torch.arange(context_length, dtype=dtype)

    # Compute the angles
    angles = positions.unsqueeze(1) * inv_freq.unsqueeze(
        0
    )  # Shape: (context_length, head_dim / 2)

    # Precompute sine and cosine
    cos = torch.cos(angles)
    sin = torch.sin(angles)

    return cos, sin


def apply_rope(x, cos, sin, method_type=0):
    if method_type == 0:  # For the two-halves method used in HF transformers
        # x: (seq_len, head_dim)
        seq_len, head_dim = x.shape
        assert head_dim % 2 == 0, "Head dimension must be even"

        # Split x into first half and second half
        x1 = x[..., : head_dim // 2]  # First half
        x2 = x[..., head_dim // 2 :]  # Second half

        # Adjust sin and cos shapes
        cos = cos[:seq_len, :]  # Shape: (seq_len, head_dim / 2)
        sin = sin[:seq_len, :]

        # Apply the rotary transformation
        x_rotated = torch.empty_like(x)
        x_rotated[..., : head_dim // 2] = (x1 * cos) + (-x2 * sin)
        x_rotated[..., head_dim // 2 :] = (x2 * cos) + (x1 * sin)

        # It's ok to use lower-precision after applying cos and sin rotation
        return x_rotated.to(dtype=x.dtype)
    elif method_type == 1:  # For the interleaved method used in the Llama paper
        # x: (seq_len, head_dim)
        seq_len, head_dim = x.shape
        assert head_dim % 2 == 0, "Head dimension must be even"

        # Split x into even and odd columns
        x_even = x[..., ::2]  # Even columns
        x_odd = x[..., 1::2]  # Odd columns

        # Adjust sin and cos shapes
        cos = cos[:seq_len, :]  # Shape: (seq_len, head_dim / 2)
        sin = sin[:seq_len, :]

        # Apply the rotary transformation and interleave the even and odd outputs
        x_rotated = torch.empty_like(x)
        x_rotated[..., ::2] = (x_even * cos) - (x_odd * sin)
        x_rotated[..., 1::2] = (x_even * sin) + (x_odd * cos)

        # It's ok to use lower-precision after applying cos and sin rotation
        return x_rotated.to(dtype=x.dtype)
    else:
        raise ValueError("Invalid method_type. Must be 0 or 1.")


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
    # Function-specific argument(s)
    parser.add_argument(
        "--rows", type=int, default=4096, help="Input length: Num tokens"
    )
    parser.add_argument("--cols", type=int, default=64, help="Tile size: Head dim")
    parser.add_argument(
        "--context_len", type=int, default=131072, help="Context length"
    )
    parser.add_argument(
        "--method_type",
        type=int,
        default=0,
        choices=[0, 1],
        help="Method type: two-halves (0), interleaved (1)",
    )
    parser.add_argument(
        "--rope_theta_base", type=float, default=500000.0, help="RoPE theta base"
    )
    parser.add_argument(
        "--rope_freq_factor", type=float, default=32.0, help="RoPE frequency factor"
    )
    parser.add_argument(
        "--rope_freq_low_factor",
        type=float,
        default=1.0,
        help="RoPE frequency: Low frequency factor",
    )
    parser.add_argument(
        "--rope_freq_high_factor",
        type=float,
        default=4.0,
        help="RoPE frequency: High frequency factor",
    )
    parser.add_argument(
        "--rope_freq_orig_ctx_len",
        type=int,
        default=8192,
        help="RoPE frequency: original context length",
    )

    args = parser.parse_args()
    torch.manual_seed(args.seed)

    # Generate golden inputs
    freq_config = {
        "factor": args.rope_freq_factor,
        "low_freq_factor": args.rope_freq_low_factor,
        "high_freq_factor": args.rope_freq_high_factor,
        "original_context_length": args.rope_freq_orig_ctx_len,
    }
    cos, sin = compute_rope_params(
        head_dim=args.cols,
        theta_base=args.rope_theta_base,
        context_length=args.context_len,
        method_type=args.method_type,
        freq_config=freq_config,
    )
    val_range = 4
    A = torch.rand(args.rows, args.cols, dtype=torch_dtype_map[args.dtype]) * val_range

    # Create the lut by interleaving cos and sin
    B = torch.empty_like(A)
    B[:, ::2] = cos[: args.rows, : args.cols // 2]
    B[:, 1::2] = sin[: args.rows, : args.cols // 2]

    # Generate golden outputs
    C = apply_rope(A, cos, sin, args.method_type)

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
