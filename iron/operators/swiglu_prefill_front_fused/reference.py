# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def pack_weights(input_b_gate, input_b_up, tile_k, tile_n, num_aie_columns):
    """Pack gate/up weights by AIE column for legal shim DMA strides."""
    if input_b_gate.shape != input_b_up.shape:
        raise ValueError("Gate and up weights must have the same shape")

    K, N = input_b_gate.shape
    if K % tile_k != 0:
        raise ValueError(f"K ({K}) must be divisible by tile_k ({tile_k})")
    tile_group_n = tile_n * num_aie_columns
    if N % tile_group_n != 0:
        raise ValueError(
            f"N ({N}) must be divisible by tile_n * num_aie_columns "
            f"({tile_group_n})"
        )

    K_div_k = K // tile_k
    n_tile_groups = N // tile_group_n

    def tile(weight):
        return weight.reshape(
            K_div_k, tile_k, n_tile_groups, num_aie_columns, tile_n
        ).permute(2, 3, 0, 1, 4)

    return (
        torch.stack((tile(input_b_gate), tile(input_b_up)), dim=3)
        .permute(1, 0, 2, 4, 3, 5)
        .reshape(num_aie_columns, n_tile_groups, K_div_k, tile_k, 2 * tile_n)
        .contiguous()
    )


def unpack_weights(packed_weights, K, N, tile_k, tile_n, num_aie_columns):
    """Unpack the fused operator's flat weight buffer into two ``(K, N)`` tensors."""
    K_div_k = K // tile_k
    n_tile_groups = N // (tile_n * num_aie_columns)
    packed = packed_weights.reshape(
        num_aie_columns,
        n_tile_groups,
        K_div_k,
        tile_k,
        2,
        tile_n,
    )

    def untile(projection):
        return (
            packed[:, :, :, :, projection]
            .permute(2, 3, 1, 0, 4)
            .contiguous()
            .reshape(K, N)
        )

    return untile(0), untile(1)


def reference(
    input_a,
    packed_weights,
    K,
    N,
    tile_k,
    tile_n,
    num_aie_columns,
):
    """CPU reference ``C = SiLU(A @ B_gate) * (A @ B_up)``.

    The packed input is unpacked from the exact tile order consumed by the
    fused operator. The result is transposed when ``c_col_maj`` is set.
    """
    B_gate, B_up = unpack_weights(packed_weights, K, N, tile_k, tile_n, num_aie_columns)
    C = torch.nn.functional.silu(torch.matmul(input_a, B_gate))
    C = C * torch.matmul(input_a, B_up)
    return C


def generate_golden_reference(
    M: int,
    K: int,
    N: int,
    dtype="bf16",
    seed=42,
    partition_N=1,
    tile_k=64,
    tile_n=64,
    num_aie_columns=1,
):
    torch.manual_seed(seed)
    val_range = 4
    dtype_torch = torch_dtype_map[dtype]
    input_a = torch.randn(M, K, dtype=dtype_torch) * val_range
    input_b_gate_full = torch.rand(K, N, dtype=dtype_torch) * val_range
    input_b_up_full = torch.rand(K, N, dtype=dtype_torch) * val_range
    if False:
        # The following inputs are useful for debugging;
        # the A matrix becomes a matrix where each element encodes its row and column index,
        # and the B matrix is an identity matrix.
        col_digits = len(str(K - 1)) if K > 0 else 1
        factor = 10 ** (col_digits + 1)
        row_indices = torch.arange(M, dtype=torch.int64).unsqueeze(1)
        col_indices = torch.arange(K, dtype=torch.int64).unsqueeze(0)
        input_a = (row_indices * factor + col_indices).to(dtype=dtype_torch)
        input_b_gate_full = torch.zeros(K, N, dtype=dtype_torch)
        input_b_up_full = torch.zeros(K, N, dtype=dtype_torch)
        diag_dim = min(K, N)
        identity = torch.eye(diag_dim, dtype=dtype_torch)
        input_b_gate_full[:diag_dim, :diag_dim] = identity
        input_b_up_full[:diag_dim, :diag_dim] = identity
    packed_weights_full = pack_weights(
        input_b_gate_full,
        input_b_up_full,
        tile_k,
        tile_n,
        num_aie_columns,
    )
    output_full = reference(
        input_a,
        packed_weights_full,
        K,
        N,
        tile_k,
        tile_n,
        num_aie_columns,
    )

    # Create partitioned packed weight buffers.
    input_b = []
    for i in range(partition_N):
        col_start = i * (N // partition_N)
        col_end = (i + 1) * (N // partition_N)
        input_b.append(
            pack_weights(
                input_b_gate_full[:, col_start:col_end],
                input_b_up_full[:, col_start:col_end],
                tile_k,
                tile_n,
                num_aie_columns,
            )
        )

    # Create partitioned buffers for C (output)
    output = []
    for i in range(partition_N):
        col_start = i * (N // partition_N)
        col_end = (i + 1) * (N // partition_N)
        output.append(output_full[:, col_start:col_end])

    return {
        "input": input_a,
        "input_b": input_b,
        "output": output,
    }
