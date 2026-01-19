# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
import logging
from pathlib import Path

from iron.operators.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)

from iron.operators.common.utils import torch_to_numpy, numpy_to_torch


class AIEGEMM(AIEOperatorBase):
    """AIE-accelerated General Matrix Multiplication (GEMM) layer"""

    def __init__(
        self,
        M,
        K,
        N,
        use_static_weight=False,
        tile_m=64,
        tile_k=64,
        tile_n=64,
        # TODO: Add support for partitioning M and/or K
        # partition_M=1,
        # partition_K=1,
        partition_N=1,
        num_aie_columns=8,
        context=None,
        **gemm_kwargs,
    ):

        self.tile_m = tile_m
        self.tile_k = tile_k
        self.tile_n = tile_n
        self.num_aie_columns = num_aie_columns
        self.gemm_args = gemm_kwargs

        # Set frequently accessed gemm_args
        self.b_col_maj = gemm_kwargs.get("b_col_maj", False)
        self.c_col_maj = gemm_kwargs.get("c_col_maj", False)
        self.weight = (
            None
            if not use_static_weight
            else torch.zeros((K, N), dtype=torch.bfloat16).T
        )
        self.static_weight_shape = (K, N)

        # The operator's M, K, N represent what the NPU operator supports.
        # Calls to forward() may supply matrices of different sizes, and the
        # Python code will perform necessary padding/repeated application of
        # the NPU operator.
        assert (
            N % partition_N == 0
        ), f"N ({N}) must be divisible by partition_N ({partition_N})"
        M_padded, K_padded, N_padded = self._get_padded_dims(
            M, K, N // partition_N, tile_m, tile_k, tile_n
        )
        self.M = M_padded
        self.K = K_padded
        self.N = N_padded
        self.partition_N = partition_N

        # Artifacts created by set_up_artifacts()
        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def get_artifacts(self, prefix="gemm_"):
        # Extract parameters from self
        operator_dir = Path(__file__).parent
        tile_m = self.tile_m
        tile_k = self.tile_k
        tile_n = self.tile_n
        M = self.M
        K = self.K
        N = self.N
        num_aie_columns = self.num_aie_columns
        base_dir = self.context.base_dir
        device_str = self.context.device_manager.device_str()

        b_col_maj = self.b_col_maj
        c_col_maj = self.c_col_maj
        dtype_in = self.gemm_args.get("dtype_in", "bf16")
        dtype_out = self.gemm_args.get("dtype_out", "bf16")
        emulate_bf16_mmul_with_bfp16 = self.gemm_args.get(
            "emulate_bf16_mmul_with_bfp16", True
        )
        prio_accuracy = self.gemm_args.get("prio_accuracy", False)
        use_scalar = self.gemm_args.get("use_scalar", False)
        round_conv_even = self.gemm_args.get("round_conv_even", True)

        if emulate_bf16_mmul_with_bfp16:
            min_tile_m, min_tile_k, min_tile_n = 8, 8, 8
        else:
            min_tile_m, min_tile_k, min_tile_n = 4, 8, 8
        assert tile_m >= min_tile_m, f"tile_m ({tile_m}) must be >= {min_tile_m}"
        assert tile_k >= min_tile_k, f"tile_k ({tile_k}) must be >= {min_tile_k}"
        assert tile_n >= min_tile_n, f"tile_n ({tile_n}) must be >= {min_tile_n}"

        file_name_tile_base = f"{prefix}{tile_m}x{tile_k}x{tile_n}"
        file_name_total_base = f"{prefix}{M}x{K}x{N}_{tile_m}x{tile_k}x{tile_n}_{int(b_col_maj)}_{int(c_col_maj)}"
        xclbin_kernel_name = f"gemm_{file_name_tile_base}"
        kernel_flags = [
            f"-DDIM_M={tile_m}",
            f"-DDIM_K={tile_k}",
            f"-DDIM_N={tile_n}",
            "-DROUND_CONV_EVEN",
        ]
        if prio_accuracy:
            kernel_flags.append("-Dbf16_f32_ONLY")
        else:
            kernel_flags.append("-Dbf16_bf16_ONLY")
        if round_conv_even:
            kernel_flags.append("-DROUND_CONV_EVEN")
        if emulate_bf16_mmul_with_bfp16:
            kernel_flags.append("-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16")
        if b_col_maj:
            kernel_flags.append("-DB_COL_MAJ")
        if c_col_maj:
            kernel_flags.append("-DC_COL_MAJ")

        kernel_archive = (
            f"gemm_{tile_m}x{tile_k}x{tile_n}_{int(b_col_maj)}_{int(c_col_maj)}.a"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_total_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_matmul",
            callback_kwargs={
                "dev": device_str,
                "M": M,
                "K": K,
                "N": N,
                "m": tile_m,
                "k": tile_k,
                "n": tile_n,
                "n_aie_cols": num_aie_columns,
                "dtype_in_str": dtype_in,
                "dtype_out_str": dtype_out,
                "b_col_maj": int(b_col_maj),
                "c_col_maj": int(c_col_maj),
                "use_scalar": use_scalar,
                "emulate_bf16_mmul_with_bfp16": emulate_bf16_mmul_with_bfp16,
                "prio_accuracy": prio_accuracy,
                "separate_c_tiles": int(self.partition_N > 1),
                "trace_size": 0,
                "archive": kernel_archive,
                "generate_taps": False,
            },
            requires_context=False,
        )

        # FIXME: We should be able to reuse the same xclbin for same tile
        # sizes, only swapping out the instruction sequence for different
        # problem sizes. However, there seem to be cases where this does
        # not work and the GEMM appears to be misconfigured for the wrong
        # size (resulting in a timeout when trying to run it). Perhaps
        # XRT is caching something, or something is wrong with the run-
        # time parameter (synchronization)? For now, create separate
        # xclbins for each problem size.
        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_total_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelArchiveArtifact.new(
                    kernel_archive,
                    depends=[
                        KernelObjectArtifact.new(
                            f"gemm_{tile_m}x{tile_k}x{tile_n}_{int(b_col_maj)}_{int(c_col_maj)}.o",
                            extra_flags=kernel_flags,
                            depends=[
                                SourceArtifact.new(
                                    base_dir / "aie_kernels" / "aie2p" / "mm.cc"
                                )
                            ],
                        ),
                        KernelObjectArtifact.new(
                            "convert_copy.o",
                            [
                                SourceArtifact.new(
                                    base_dir
                                    / "aie_kernels"
                                    / "generic"
                                    / "convert_copy.cc"
                                )
                            ],
                        ),
                    ],
                ),
            ],
            extra_flags=["--dynamic-objFifos"],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_total_base}.bin",
            depends=[mlir_artifact],
            extra_flags=["--dynamic-objFifos"],
        )

        return (xclbin_artifact, insts_artifact)

    def set_up_artifacts(self):
        # Describe required artifacts (xclbin, insts.bin)
        device_str = self.context.device_manager.device_str()
        xclbin_artifact, insts_artifact = self.get_artifacts()

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact

        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        static_weights = None
        if self.weight is not None:
            static_weights = self.weight.T
            if isinstance(static_weights, torch.Tensor):
                static_weights = torch_to_numpy(static_weights)
        self.add_kernel(
            "gemm",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_buffer("A", self.M * self.K)
        B_parts = self._partition_B(static_weights)
        for i, B_part in enumerate(B_parts):
            self.add_buffer(
                f"B_{i}",
                self.K * self.N,
                static_data=B_part,
            )
            self.add_buffer(f"C_{i}", self.M * self.N)
            self.add_to_runlist("gemm", "A", f"B_{i}", f"C_{i}")

    def _get_B_dims(self, B_shape):
        """Extract K and N dimensions from B matrix shape based on layout.

        Returns:
            tuple: (K, N) dimensions regardless of B's layout
        """
        if self.b_col_maj:
            return B_shape[-1], B_shape[-2]  # B is (N, K) -> return (K, N)
        else:
            return B_shape[-2], B_shape[-1]  # B is (K, N) -> return (K, N)

    def forward(self, A, B=None):
        """Forward pass through GEMM operation: C = A @ B"""
        B_shape = B.shape if B is not None else self.static_weight_shape

        # Determine output dimensions based on matrix layout
        K2, N = self._get_B_dims(B_shape)
        N_part = N // self.partition_N

        # Build expected output shape based on C layout
        expected_output_shape = (
            A.shape[:-2] + (N, A.shape[-1]) if self.c_col_maj else A.shape[:-1] + (N,)
        )

        # Remove batch dimension, if any
        if len(A.shape) > 2:
            A = A.view(-1, A.shape[-1])
        if B is not None and len(B.shape) > 2:
            B = B.view(-1, B_shape[-1])

        M, K = A.shape

        applicable = (
            K == K2
            and (M <= self.M or not self.c_col_maj)
            and K <= self.K
            and N <= self.N
        )
        if not applicable:
            raise AIEOperatorConstraintError("AIEGEMM: incompatible tensor shape(s)")

        A_padded = self._pad_A(torch_to_numpy(A))
        if B is not None:
            B_parts = self._partition_B(torch_to_numpy(B))
        else:
            B_parts = None

        logging.debug(
            f"Executing GEMM for dimensions M={M}, K={K}, N={N} using NPU operator with M={self.M}, K={self.N}, N={self.N}"
        )

        if self.c_col_maj:
            result_padded = np.zeros((N, M), dtype=A_padded.dtype)
        else:
            result_padded = np.zeros((M, N), dtype=A_padded.dtype)
        for M_lo in range(0, M, self.M):
            A_part = A_padded[M_lo : M_lo + self.M, :]
            result_parts = self._execute_aie_operation(A_part, B_parts)
            max_M = min(M_lo + self.M, M)
            for part in range(self.partition_N):
                if self.c_col_maj:
                    result_padded[part * N_part : (part + 1) * N_part, M_lo:max_M] = (
                        result_parts[part][:N_part, :max_M]
                    )
                else:
                    result_padded[M_lo:max_M, part * N_part : (part + 1) * N_part] = (
                        result_parts[part][:max_M, :N_part]
                    )

        # GEMM produces 2D result, reshape to expected output shape
        if self.c_col_maj:
            result = numpy_to_torch(result_padded[:N, :M])
        else:
            result = numpy_to_torch(result_padded[:M, :N])
        result = result.view(expected_output_shape)

        return result

    def _get_padded_dims(self, M, K, N, tile_m, tile_k, tile_n):
        num_aie_columns = self.num_aie_columns
        num_aie_rows = 4

        min_M = tile_m * num_aie_rows
        min_K = tile_k
        min_N = tile_n * num_aie_columns

        # Calculate padded dimensions
        M_padded = ((M + min_M - 1) // min_M) * min_M
        K_padded = ((K + min_K - 1) // min_K) * min_K
        N_padded = ((N + min_N - 1) // min_N) * min_N

        return M_padded, K_padded, N_padded

    def _pad_A(self, A_np):
        """Pad A matrix to match operator dimensions (M, K)"""
        M, K = A_np.shape
        if M % self.M == 0 and K == self.K:
            return A_np

        M_padded = ((M + self.M - 1) // self.M) * self.M
        A_padded = np.zeros((M_padded, self.K), dtype=A_np.dtype)
        A_padded[:M, :K] = A_np
        return A_padded

    def _pad_B(self, B_np):
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

    def _partition_B(self, B):
        B_parts = [None] * self.partition_N
        if B is None:
            return B_parts
        for i in range(self.partition_N):
            col_start = i * self.N
            col_end = (i + 1) * self.N

            # Just in case, pad the weights before adding the buffer
            if self.b_col_maj:
                B_parts[i] = self._pad_B(B[col_start:col_end, :])
            else:
                B_parts[i] = self._pad_B(B[:, col_start:col_end])
        self.static_weight_shape = B_parts[0].shape
        return B_parts

    def _execute_aie_operation(self, A_np, B_nps=None):
        """Execute GEMM operation on AIE hardware"""
        M, K = A_np.shape
        B_shape = B_nps[0].shape if B_nps is not None else self.static_weight_shape
        K2, N = self._get_B_dims(B_shape)
        C_shape = (N, M) if self.c_col_maj else (M, N)

        # Validate dimensions match operator configuration
        assert M == self.M
        assert K == K2 and K == self.K
        assert N == self.N

        self.write_buffer("A", A_np)
        if B_nps is not None:
            for i, B_np in enumerate(B_nps):
                self.add_buffer(
                    f"B_{i}",
                    self.M * self.N,
                    static_data=B_np,
                )
        self.run_runlist()
        result_nps = [
            self.read_buffer(f"C_{i}", shape=C_shape, dtype=bfloat16)
            for i in range(self.partition_N)
        ]

        # Check for NaN and fail hard
        # for result_np in result_nps:
        #     if np.isnan(result_np).any():
        #         nan_count = np.isnan(result_np).sum()
        #         total_count = result_np.size
        #         raise RuntimeError(
        #             f"AIE execution returned {nan_count}/{total_count} NaN values. "
        #         )

        # Convert back to torch tensor
        return result_nps
