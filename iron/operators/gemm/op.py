# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from pathlib import Path

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEGEMM(MLIROperator):
    """AIE-accelerated General Matrix Multiplication (GEMM) layer"""

    def __init__(
        self,
        M,
        K,
        N,
        tile_m=64,
        tile_k=64,
        tile_n=64,
        # TODO: Add support for partitioning M and/or K
        # partition_M=1,
        # partition_K=1,
        num_aie_columns=8,
        context=None,
        **gemm_kwargs,
    ):
        num_aie_rows = 4
        min_M = tile_m * num_aie_rows
        min_K = tile_k
        min_N = tile_n * num_aie_columns
        assert M % min_M == 0, f"M ({M}) must be multiple of {min_M}"
        assert K % min_K == 0, f"K ({K}) must be multiple of {min_K}"
        assert N % min_N == 0, f"N ({N}) must be multiple of {min_N}"
        self.M = M
        self.K = K
        self.N = N
        self.tile_m = tile_m
        self.tile_k = tile_k
        self.tile_n = tile_n

        self.num_aie_columns = num_aie_columns
        self.gemm_args = gemm_kwargs
        self.b_col_maj = gemm_kwargs.get("b_col_maj", False)
        self.c_col_maj = gemm_kwargs.get("c_col_maj", False)
        self.emulate_bf16_mmul_with_bfp16 = gemm_kwargs.get(
            "emulate_bf16_mmul_with_bfp16", True
        )
        self.prio_accuracy = gemm_kwargs.get("prio_accuracy", False)
        self.round_conv_even = gemm_kwargs.get("round_conv_even", True)

        if self.emulate_bf16_mmul_with_bfp16:
            min_tile_m, min_tile_k, min_tile_n = 8, 8, 8
        else:
            min_tile_m, min_tile_k, min_tile_n = 4, 8, 8
        assert tile_m >= min_tile_m, f"tile_m ({tile_m}) must be >= {min_tile_m}"
        assert tile_k >= min_tile_k, f"tile_k ({tile_k}) must be >= {min_tile_k}"
        assert tile_n >= min_tile_n, f"tile_n ({tile_n}) must be >= {min_tile_n}"

        super().__init__(context=context)

    def get_operator_name(self):
        return f"gemm_{self.M}x{self.K}x{self.N}_{self.tile_m}x{self.tile_k}x{self.tile_n}_{int(self.b_col_maj)}_{int(self.c_col_maj)}"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        operator_name = self.get_operator_name()
        device_str = self.context.device_manager.device_str()
        dtype_in = self.gemm_args.get("dtype_in", "bf16")
        dtype_out = self.gemm_args.get("dtype_out", "bf16")
        emulate_bf16_mmul_with_bfp16 = self.gemm_args.get(
            "emulate_bf16_mmul_with_bfp16", True
        )
        prio_accuracy = self.gemm_args.get("prio_accuracy", False)
        use_scalar = self.gemm_args.get("use_scalar", False)
        round_conv_even = self.gemm_args.get("round_conv_even", True)
        separate_c_tiles = self.gemm_args.get("separate_c_tiles", False)
        return PythonGeneratedMLIRArtifact(
            f"{operator_name}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_matmul",
            callback_kwargs={
                "dev": device_str,
                "M": self.M,
                "K": self.K,
                "N": self.N,
                "m": self.tile_m,
                "k": self.tile_k,
                "n": self.tile_n,
                "n_aie_cols": self.num_aie_columns,
                "dtype_in_str": dtype_in,
                "dtype_out_str": dtype_out,
                "b_col_maj": int(self.b_col_maj),
                "c_col_maj": int(self.c_col_maj),
                "use_scalar": use_scalar,
                "emulate_bf16_mmul_with_bfp16": emulate_bf16_mmul_with_bfp16,
                "prio_accuracy": prio_accuracy,
                "separate_c_tiles": int(separate_c_tiles),
                "trace_size": 0,
                "generate_taps": False,
            },
            requires_context=False,
        )

    def get_kernel_artifacts(self):
        base_dir = self.context.base_dir
        emulate_bf16_mmul_with_bfp16 = self.gemm_args.get(
            "emulate_bf16_mmul_with_bfp16", True
        )
        prio_accuracy = self.gemm_args.get("prio_accuracy", False)
        round_conv_even = self.gemm_args.get("round_conv_even", True)
        kernel_flags = [
            f"-DDIM_M={self.tile_m}",
            f"-DDIM_K={self.tile_k}",
            f"-DDIM_N={self.tile_n}",
        ]
        if prio_accuracy:
            kernel_flags.append("-Dbf16_f32_ONLY")
        else:
            kernel_flags.append("-Dbf16_bf16_ONLY")
        if round_conv_even:
            kernel_flags.append("-DROUND_CONV_EVEN")
        if emulate_bf16_mmul_with_bfp16:
            kernel_flags.append("-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16")
        if self.b_col_maj:
            kernel_flags.append("-DB_COL_MAJ")
        if self.c_col_maj:
            kernel_flags.append("-DC_COL_MAJ")

        # Include flags in the filename to avoid stale builds when flags change
        flags_suffix = f"_{int(prio_accuracy)}_{int(emulate_bf16_mmul_with_bfp16)}_{int(round_conv_even)}"

        return [
            KernelObjectArtifact(
                f"gemm_{self.tile_m}x{self.tile_k}x{self.tile_n}_{int(self.b_col_maj)}_{int(self.c_col_maj)}{flags_suffix}.o",
                extra_flags=kernel_flags,
                dependencies=[
                    SourceArtifact(base_dir / "aie_kernels" / "aie2p" / "mm.cc")
                ],
            ),
            KernelObjectArtifact(
                "convert_copy.o",
                [
                    SourceArtifact(
                        base_dir / "aie_kernels" / "generic" / "convert_copy.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.M, self.K)),  # input A
            AIERuntimeArgSpec(
                "in", (self.K, self.N) if not self.b_col_maj else (self.N, self.K)
            ),  # input B (weights)
            AIERuntimeArgSpec(
                "out", (self.M, self.N) if not self.c_col_maj else (self.N, self.M)
            ),  # output C
        ]

    def pad_A(self, A_np):
        """Pad A matrix to match operator dimensions (M, K)"""
        M, K = A_np.shape
        if M == self.M and K == self.K:
            return A_np

        M_padded = ((M + self.M - 1) // self.M) * self.M
        A_padded = np.zeros((M_padded, self.K), dtype=A_np.dtype)
        A_padded[:M, :K] = A_np
        return A_padded

    def pad_B(self, B_np):
        """Pad B matrix to match operator dimensions based on layout"""
        if self.b_col_maj:
            N, K = B_np.shape
            if N == self.N and K == self.K:
                return B_np
            B_padded = np.zeros((self.N, self.K), dtype=B_np.dtype)
            B_padded[:N, :K] = B_np
        else:
            K, N = B_np.shape
            if K == self.K and N == self.N:
                return B_np
            B_padded = np.zeros((self.K, self.N), dtype=B_np.dtype)
            B_padded[:K, :N] = B_np
        return B_padded

    def partition_B(self, B, partition_N):
        B_parts = [None] * partition_N
        if B is None:
            return B_parts
        for i in range(partition_N):
            col_start = i * self.N
            col_end = (i + 1) * self.N

            if self.b_col_maj:
                B_parts[i] = self.pad_B(B[col_start:col_end, :])
            else:
                B_parts[i] = self.pad_B(B[:, col_start:col_end])
        return B_parts
