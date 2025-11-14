# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import sys
import argparse

import torch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)

from golden_model_lib import export, torch_to_numpy, torch_dtype_map

tensor_type_to_quant = {torch.uint8: torch.quint8}


def main():
    parser = argparse.ArgumentParser(
        description="Generate golden reference for Copy function."
    )
    parser.add_argument(
        "--inp_dtype",
        type=str,
        choices=torch_dtype_map.keys(),
        default="ui8",
        help="IO data type",
    )
    parser.add_argument(
        "--out_dtype",
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
    parser.add_argument("--input_length", type=int, default=42, help="Input length")
    parser.add_argument("--tile_size", type=int, default=42, help="Tile size")
    parser.add_argument("--group_size", type=int, default=42, help="Tile size")

    args = parser.parse_args()
    torch.manual_seed(args.seed)
    out_type = torch_dtype_map[args.out_dtype]
    in_type = torch_dtype_map[args.inp_dtype]

    input_length = args.input_length
    tile_size = args.tile_size
    group_size = args.group_size
    if input_length % tile_size != 0:
        raise ValueError("Input length must be a multiple of tile size.")
    if tile_size % group_size != 0:
        raise ValueError("Tile size must be a multiple of group size.")

    num_tiles = args.input_length // tile_size
    num_scale_factors = tile_size // group_size
    scale_size = num_scale_factors * 2  # Total bytes (uint8 elements) for scale factors
    per_tile_size = tile_size // 2
    per_tile_bytes = (
        scale_size + per_tile_size
    )  # Total bytes (uint8 elements) after processing each file
    val_range = 3.75  # Values in [0, 3.75)

    # Generate golden output with uniform distribution between 0 and 8,
    # This output which will be quantized to be used as the input
    A = (
        torch.rand(num_tiles * num_scale_factors, group_size, dtype=out_type)
        * val_range
    )

    # Generate scale factors in [0.25, 1) for each tile. The quantized values will thus be within [0,15],
    # which is the range of int4, i.e. no overflow in the data.
    # Zero points for each tile are fixed to 0 since the kernel only uses the scale factors
    r1, r2 = 1 / val_range, 1
    scaled_tensor = torch.rand(2, 3)
    scales = r1 + (r2 - r1) * torch.rand(num_tiles * num_scale_factors, dtype=out_type)
    zero_points = torch.zeros(num_tiles * num_scale_factors, dtype=out_type)
    A = torch.quantize_per_channel(
        A.to(torch.float32),
        scales=scales.to(torch.float32),
        zero_points=zero_points.to(torch.float32),
        axis=0,
        dtype=tensor_type_to_quant[in_type],
    )
    B = torch.dequantize(A)

    # Convert A from a quantized tensor type to regular tensor type for data packing. We do the data packing here instead of the host
    # to show how the data would need to be manipulated from a PyTorch standpoint in order to use the dequant kernel.
    A = A.int_repr()

    # Concatenate the bottom four bits of every two elements across the tiles in A to generate an 8-bit value (little endian order).
    # This is because there's no native 4-bit datatype in C++.
    # At the end of each tile, concatenate the bf16 scale factor, which comes out to two int8 values.
    A_concat = torch.zeros(num_tiles, per_tile_bytes, dtype=in_type)
    for i in range(num_tiles):
        for j in range(num_scale_factors):
            for k in range(group_size // 2):
                A_concat[i, j * (group_size // 2) + k] = torch.bitwise_or(
                    torch.bitwise_and(A[i * num_scale_factors + j, 2 * k], 0x0F),
                    torch.bitwise_and(A[i * num_scale_factors + j, 2 * k + 1], 0x0F)
                    * 2**4,
                )
        for j in range(num_scale_factors):
            A_concat[i, per_tile_size + 2 * j] = torch.bitwise_and(
                scales[i * num_scale_factors + j].view(torch.uint16), 0xFF
            )
            A_concat[i, per_tile_size + 2 * j + 1] = torch.bitwise_and(
                (scales[i * num_scale_factors + j].view(torch.uint16) / 2**8).to(
                    torch.uint16
                ),
                0xFF,
            )

    export(
        tensor_dict={
            "A": torch_to_numpy(A_concat),
            "B": torch_to_numpy(B.to(out_type)),
        },
        header_path=args.output_header,
        bin_path=args.output_bin,
    )

    # Uncomment below to do a quick comparison of 2 quantized inputs with the corresponding float outputs
    # print(f"\nInput in int8 format: {A[0,0]}, in int4 format: {torch.bitwise_and(A_concat[0,0], 0x0F)}")
    # scale = (A_concat[0, per_tile_size].to(torch.int32) + (A_concat[0, per_tile_size + 1].to(torch.int32) * 2**8)).to(torch.uint16).view(torch.bfloat16)
    # print(f"Scale in bloat16 format: {scales[0]}, and converted to bfloat16 from two int8 values: {scale}")
    # print(f"Output in float format: {B[0,0]}, converted to float using int4 data and scale: {torch.bitwise_and(A_concat[0,0], 0x0F) * scale}\n")

    # print(f"Input in int8 format: {A[0,1]}, in int4 format: {(torch.bitwise_and(A_concat[0,0], 0xF0) / 2**4).to(torch.uint8)}")
    # scale = (A_concat[0, per_tile_size].to(torch.int32) + (A_concat[0, per_tile_size + 1].to(torch.int32) * 2**8)).to(torch.uint16).view(torch.bfloat16)
    # print(f"Scale in bloat16 format: {scales[0]}, and converted to bfloat16 from two int8 values: {scale}")
    # print(f"Output in float format: {B[0,1]}, converted to float using int4 data and scale: {torch.bitwise_and(A_concat[0,0], 0xF0) / 2**4 * scale}\n")


if __name__ == "__main__":
    main()
